import json
from network_manager import Network

network = Network()

# Example participants
participants = ["Alice", "Bob", "Charlie", "Diana", "Erik", "Frida", "Gustav", "Hanne"]
for p in participants:
    network.add_participant(p)

# Example meeting history
network.add_meeting({
    "Bord 1": ["Alice", "Bob", "Charlie"],
    "Bord 2": ["Diana", "Erik", "Frida"],
    "Bord 3": ["Gustav", "Hanne"]
})

network.add_meeting({
    "Bord 1": ["Alice", "Diana", "Gustav"],
    "Bord 2": ["Bob", "Erik", "Hanne"],
    "Bord 3": ["Charlie", "Frida"]
})

# Generate a plan for next meeting with tables of size 3
plan = network.generate_table_plan(3)
print(json.dumps(plan, indent=2, ensure_ascii=False))
