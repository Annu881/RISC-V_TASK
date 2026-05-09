# RISC-V Instruction Set Explorer

This project implements the RISC-V Mentorship Coding Challenge. It parses the RISC-V extensions landscape from a JSON dictionary and cross-references it against the official RISC-V ISA manual.

## Structure
- `src/parser.py`: Parses the instruction dictionary to group properties and find overlaps (Tier 1).
- `src/analyzer.py`: Scans the AsciiDoc files of the official RISC-V ISA manual to extract valid extensions and cross-references them against the JSON mappings (Tier 2).
- `src/graph.py`: Generates a text-based graph of extensions that share instructions (Tier 3).
- `src/main.py`: Ties everything together to print the final output.
- `tests/`: Basic strict unit testing using Python's `unittest`.
- `sample_output.txt`: The system output showing the tool in action.

## Running the Application

1. Make sure Python 3.7+ is installed.
2. Clone the `riscv-isa-manual` repo inside this directory (if you haven't):
   ```bash
   git clone https://github.com/riscv/riscv-isa-manual riscv-isa-manual
   ```
3. Execute the script:
   ```bash
   export PYTHONPATH=$(pwd)
   python3 src/main.py
   ```

## Running Tests
Run the test suite from the project root:
```bash
export PYTHONPATH=$(pwd)
python3 -m unittest discover tests/ -v
```

## Design Decisions
- **Normalization:** In `instr_dict.json`, extensions use prefixes like `rv_` or `rv64_`. When comparing against the manual tags, these prefixes are stripped and unified to lowercase.
- **ISA Extractor:** Scanning AsciiDoc manually can be painfully slow if the regex catches open-ended text. The analyzer simply hooks onto `ext:...` tags and `== "..." Extension` headers directly. It's clean, robust, and lightning fast. 
