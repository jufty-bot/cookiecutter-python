"""
Example test case for {{ friendly_name }}.
"""

from {{ project_slug }} import __application__


def test_example() -> None:
    """
    Just a simple test case.
    """
    assert __application__ == "{{ friendly_name }}"
