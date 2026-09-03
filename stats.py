"""Statistics over a document.

Every function here is pure: it takes the document it is given and returns a
number. Nothing in this module opens a file.
"""

from document import Document


def count_lines(document: Document) -> int:
    """Count every line, blank ones included."""
    return len(document.lines)


def count_blank_lines(document: Document) -> int:
    """Count lines that are empty or contain nothing but whitespace."""
    return sum(1 for line in document.lines if not line.strip())


def count_characters(document: Document) -> int:
    """Count the characters in the text, not counting the line breaks."""
    return sum(len(line) for line in document.lines)


def longest_line_length(document: Document) -> int:
    """Return the length of the longest line, excluding its line break."""
    return max(
        (len(line.rstrip("\r\n")) for line in document.lines), default=0
    )


def count_words(document: Document) -> int:
    """Count words, where a word is whatever whitespace separates.

    Punctuation stays attached to the token beside it, so ``"don't"`` is
    one word and ``"stop."`` keeps its full stop.
    """
    return sum(len(line.split()) for line in document.lines)
