"""Boundary and integration tests for the assigned spam scoring filter."""
import pytest
from spam_scoring import classify, filter_inbox, inbox_status, score_message


@pytest.mark.parametrize("text,known,links,expected", [
    ("hello there", False, 0, 0),
    ("FREE! winner, prize.", False, 0, 6),
    ("LOUD FYI mixed", False, 0, 1),
    ("", False, 1, 1),
    ("", False, 3, 1),
    ("", False, 4, 4),
    ("free", True, 0, 0),
    ("FREE prize", True, 0, 1),
    ("free", True, 1, 0),
])
def test_score(text, known, links, expected):
    assert score_message(text, known, links) == expected


@pytest.mark.parametrize("score,label", [
    (1, "clean"), (3, "clean"), (4, "suspicious"),
    (7, "suspicious"), (8, "spam"), (9, "spam"),
])
def test_classification(score, label):
    assert classify(score) == label


def test_mixed_inbox():
    messages = [("FREE prize", False, 4), ("urgent cash", False, 0),
                ("hello", True, 0), ("FREE", True, 0)]
    assert filter_inbox(messages) == {"spam": 1, "suspicious": 1, "clean": 2}


def test_empty_inbox():
    assert filter_inbox([]) == {"spam": 0, "suspicious": 0, "clean": 0}


@pytest.mark.parametrize("spam,clean,status", [
    (0, 0, "empty"), (1, 4, "healthy"), (1, 3, "noisy"),
    (1, 1, "noisy"), (3, 2, "flooded"),
])
def test_status(spam, clean, status):
    assert inbox_status({"spam": spam, "suspicious": 0, "clean": clean}) == status
