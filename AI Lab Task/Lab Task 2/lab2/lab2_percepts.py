"""
Lab 2 - Stateful temperature/occupancy controller.

The controller retains the previous target mode and suppresses duplicate
commands. The temperature thresholds are explicit lab assumptions:
    temperature < 18 C  -> HEAT
    temperature > 24 C  -> COOL
    otherwise            -> OFF

Occupancy has priority:
    if occupancy > 0, temperature rules apply;
    if occupancy == 0, target is OFF.

The controller returns (target_mode, should_send).
"""

HEAT_THRESHOLD = 18.0
COOL_THRESHOLD = 24.0


def reflex_target(temperature, occupancy):
    """Compute the target mode from the current percept only."""
    if occupancy == 0:
        return "OFF"

    if temperature < HEAT_THRESHOLD:
        return "HEAT"

    if temperature > COOL_THRESHOLD:
        return "COOL"

    return "OFF"


class StatefulController:
    """Stateful version that remembers the previous target mode."""

    def __init__(self, previous_mode=None):
        self.previous_mode = previous_mode

    def step(self, temperature, occupancy):
        target = reflex_target(temperature, occupancy)
        should_send = target != self.previous_mode
        previous = self.previous_mode

        # Store the newly selected target mode as internal state.
        self.previous_mode = target

        return target, should_send, previous


def format_percept(temperature, occupancy):
    return f"temperature={temperature:g}C, occupancy={occupancy}"


if __name__ == "__main__":
    controller = StatefulController()
    for temperature, occupancy in [
        (20, 1),
        (20, 1),
        (18, 1),
        (17, 1),
        (17, 1),
        (25, 1),
        (25, 1),
        (25, 0),
    ]:
        target, send, previous = controller.step(temperature, occupancy)
        print(
            f"previous={previous!r}, percept=({format_percept(temperature, occupancy)}), "
            f"target={target}, command={'SEND' if send else 'NO-COMMAND'}"
        )
