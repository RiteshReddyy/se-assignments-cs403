"""Extract a sender domain, the first HTTP(S) link and the uppercase ratio."""
import re
from urllib.parse import urlsplit


def sender_domain(email):
    """Return the lower-case domain of a simple mailbox, or an empty string."""
    if not isinstance(email, str):
        return ""
    match = re.fullmatch(r"([^\s@]+)@([^\s@]+)", email.strip())
    return match.group(2).lower() if match else ""


def first_link(text):
    """Return the first whitespace-delimited HTTP(S) URL with a hostname."""
    if not isinstance(text, str):
        return ""
    for match in re.finditer(r"https?://[^\s]+", text, re.IGNORECASE):
        candidate = match.group().rstrip(".,;!?")
        try:
            if urlsplit(candidate).hostname:
                return candidate
        except ValueError:
            continue
    return ""


def shout_ratio(text):
    """Return uppercase alphabetic characters divided by all letters."""
    if not isinstance(text, str):
        return 0.0
    letters = [char for char in text if char.isalpha()]
    return sum(char.isupper() for char in letters) / len(letters) if letters else 0.0

def main():
    print("==== Running sender_domain ====")
    user_input = input("Enter a sender email (e.g. offers@Deals.com): ")
    result = sender_domain(user_input)
    print("Sender Domain:", result)

    print("\n==== Running first_link ====")
    user_input = input("Enter a message containing a link: ")
    result = first_link(user_input)
    print("First Link:", result)

    print("\n==== Running shout_ratio ====")
    user_input = input("Enter a message (e.g. FREE prize NOW): ")
    result = shout_ratio(user_input)
    print("Uppercase Ratio:", result)

if __name__ == "__main__":
    main()

