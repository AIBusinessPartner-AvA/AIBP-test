from dataclasses import dataclass, field
from itertools import combinations
import random
from typing import Dict, List, Set, Tuple

@dataclass
class Network:
    participants: Set[str] = field(default_factory=set)
    meetings: List[Dict[str, List[str]]] = field(default_factory=list)
    pair_counts: Dict[frozenset, int] = field(default_factory=dict)

    def add_participant(self, name: str) -> None:
        self.participants.add(name)

    def add_meeting(self, table_assignments: Dict[str, List[str]]) -> None:
        """Add meeting table assignments and update pair counts."""
        for table, names in table_assignments.items():
            for name in names:
                self.add_participant(name)
            for pair in combinations(names, 2):
                key = frozenset(pair)
                self.pair_counts[key] = self.pair_counts.get(key, 0) + 1
        self.meetings.append(table_assignments)

    def generate_table_plan(self, table_size: int) -> Dict[str, List[str]]:
        """Generate a new table plan with minimal repeated pairs."""
        if not self.participants:
            return {}
        participants = list(self.participants)
        random.shuffle(participants)
        tables: List[List[str]] = []
        for name in participants:
            best_table = None
            best_score = None
            for table in tables:
                if len(table) >= table_size:
                    continue
                score = sum(self.pair_counts.get(frozenset([name, p]), 0) for p in table)
                if best_score is None or score < best_score:
                    best_table = table
                    best_score = score
            if best_table is None:
                best_table = []
                tables.append(best_table)
            best_table.append(name)
        return {f"Table {i+1}": names for i, names in enumerate(tables)}

if __name__ == "__main__":
    import json
    import argparse

    parser = argparse.ArgumentParser(description="Manage network meetings")
    subparsers = parser.add_subparsers(dest="command")

    add_part = subparsers.add_parser("add_participant")
    add_part.add_argument("name")

    add_meet = subparsers.add_parser("add_meeting")
    add_meet.add_argument("file", help="JSON file with table assignments")

    gen_plan = subparsers.add_parser("generate_plan")
    gen_plan.add_argument("table_size", type=int)

    args = parser.parse_args()
    network = Network()

    if args.command == "add_participant":
        network.add_participant(args.name)
        print(f"Added participant {args.name}")
    elif args.command == "add_meeting":
        with open(args.file) as f:
            data = json.load(f)
        network.add_meeting(data)
        print("Meeting added")
    elif args.command == "generate_plan":
        plan = network.generate_table_plan(args.table_size)
        print(json.dumps(plan, indent=2, ensure_ascii=False))
    else:
        parser.print_help()
