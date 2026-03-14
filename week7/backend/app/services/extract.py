import re


ACTION_PATTERNS = [
    r"^\s*[-*]?\s*(TODO:.*)",
    r"^\s*[-*]?\s*(ACTION:.*)",
    r"^\s*[-*]?\s*(.*!$)",
]


def extract_action_items(text: str) -> list[str]:
    """
    Extract actionable items from text using pattern matching.

    Recognizes:
    - TODO items
    - ACTION items
    - emphasized lines ending with !
    """

    results: list[str] = []

    for line in text.splitlines():
        line = line.strip()

        for pattern in ACTION_PATTERNS:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                results.append(match.group(1).strip())
                break

    return results