# RISC-V Instruction Set Explorer

This is a Python-based exploration tool developed for the RISC-V Mentorship Coding Challenge. It parses, groups, and cross-references RISC-V instruction definitions against the official RISC-V ISA manual.

## Features
- **Tier 1 (Instruction Set Parsing):** Parses `instr_dict.json` to group instructions by extensions and identifies overlapping instructions across multiple extensions.
- **Tier 2 (ISA Reference Matching):** Scans the official RISC-V ISA manual AsciiDoc files to extract defined extensions, cross-referencing them with the JSON dataset to find mismatches and overlaps.
- **Tier 3 (Extension Mapping):** Generates a text-based topology of extensions that intersect by sharing common instructions.

## Prerequisites
- Python 3.7+
- A local copy of the RISC-V ISA manual

## Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Annu881/RISC-V_TASK.git
   cd RISC-V_TASK
   ```

2. Clone the official RISC-V manual into the project root:
   ```bash
   git clone https://github.com/riscv/riscv-isa-manual
   ```

## Usage

To run the main analysis script:
```bash
export PYTHONPATH=$(pwd)
python3 src/main.py
```

To run the unit tests:
```bash
export PYTHONPATH=$(pwd)
python3 -m unittest discover tests/ -v
```

## Implementation Notes

- **Naming Normalization:** The RISC-V JSON dictionary and the ISA manual adhere to different naming conventions. The `analyzer.py` module maps these accurately by parsing out standard architectural prefixes (e.g., `rv_`, `rv32_`) and converting variables to lowercase prior to computing intersections.
- **Parsing Strategy:** To ensure high performance during AsciiDoc scanning, the extraction module directly targets `ext:*` macros and explicit `==` definition headings, avoiding the heavy regex backtracking common with generic text-block scraping.
