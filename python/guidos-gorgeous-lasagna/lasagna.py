EXPECTED_BAKE_TIME = 40  # minutes
PREPARATION_TIME = 2  # minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """
    Calculates the remaining bake time of the lasagna.
    :param elapsed_bake_time: minutes the lasagna has baked.
    :return: minutes remaining to bake the lasagna.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """
    Calculates the time required to prep the lasagna before baking.
    :param layers: number of layers in the lasagna.
    :return: minutes of prep time.
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """
    Calculates the total time spent cooking the lasagna including bake and prep.
    :param layers: number of layers in the lasagna.
    :param elapsed_bake_time: minutes the lasagna has baked.
    :return: total minutes of prep and elapsed bake time.
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
