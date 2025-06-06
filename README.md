# Network Meeting Organizer

This repository contains a small Python utility to help manage network meetings.
It keeps track of participants, who they have previously sat with, and can
suggest a new table plan where participants meet new people.

## Files

- `network_manager.py` – core library and command line tool
- `demo.py` – example usage with sample data

## Usage

```
python demo.py
```

This will print a suggested table plan based on the sample meetings in
`demo.py`.

You can also use `network_manager.py` directly:

```
python network_manager.py generate_plan 3
```

See `--help` for more commands.
