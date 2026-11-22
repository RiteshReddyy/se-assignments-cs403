"""Properties for absent values, Unicode text, valid addresses and links."""
from hypothesis import given, strategies as st
from spam_scoring import sender_domain, first_link, shout_ratio

inputs = st.one_of(st.none(), st.text(), st.integers(), st.binary())


@given(inputs)
def test_sender_domain_no_crash(value):
    result = sender_domain(value)
    assert isinstance(result, str)
    if not isinstance(value, str) or "@" not in value:
        assert result == ""


@given(st.from_regex(r"[a-z]{1,15}", fullmatch=True),
       st.from_regex(r"[A-Z]{1,10}", fullmatch=True))
def test_valid_sender(local, domain):
    assert sender_domain(f"{local}@{domain}.ORG") == domain.lower() + ".org"


@given(inputs)
def test_first_link_no_crash(value):
    result = first_link(value)
    assert isinstance(result, str)
    if result:
        assert result in value
        assert result.lower().startswith(("http://", "https://"))


@given(st.sampled_from([" ", "\n", "\t"]), st.integers(0, 1000))
def test_first_of_two_links(separator, index):
    first = f"https://example.org/{index}"
    assert first_link(f"Read {first}{separator}https://example.net") == first


@given(inputs)
def test_shout_ratio_no_crash(value):
    letters = [c for c in value if c.isalpha()] if isinstance(value, str) else []
    expected = sum(c.isupper() for c in letters) / len(letters) if letters else 0.0
    assert shout_ratio(value) == expected


def test_specific_examples():
    assert sender_domain("a@@b") == ""
    assert first_link("https://[ https://example.org") == "https://example.org"
    assert shout_ratio("Go NOW!") == 4 / 5
