"""Returns a string of the form 'One for [name], one for me.'"""


def two_fer(name=None):
    """Formats string with specified name. If no name is supplied, 'you' will be substituded.

    :param name: The name to insert.
    :return: The formatted string with name substituted.
    """
    if name is None:
        name = 'you'

    return f"One for {name}, one for me."
