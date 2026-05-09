# RISC-V Instruction Set Explorer 🚀

A modular exploration tool designed to parse, group, and cross-reference the RISC-V extensions landscape. This project was developed as a solution to the **RISC-V Mentorship Coding Challenge**.

## 📖 Overview

The RISC-V Instruction Set Explorer elegantly compares machine-readable JSON definitions of the RISC-V instruction structure against the official text-based references found in the RISC-V ISA manual. The application successfully:

1. **Parses & Classifies (Tier 1):** Groups instructions directly from `instr_dict.json` to compute accurate extension metrics, along with mapping overlaps showing instructions shared across domains.
2. **Cross-References (Tier 2):** Scans the complex AsciiDoc files inside the official [RISC-V ISA manual](https://github.com/riscv/riscv-isa-manual) to identify exactly which architectural extensions overlap, exist solely in the JSON dictionaries, or exist solely in the official ISA document.
3. **Graphing Overlaps (Tier 3):** Generates an ASCII text-based network graph visually linking identical extensions based on shared CPU instruction calls.

## 📂 Project Structure

```text
.
├── src/
│   ├── analyzer.py   # AsciiDoc ISA macro scraping (Tier 2)
│   ├── graph.py      # Text-based topological graph generator (Tier 3)
│   ├── main.py       # Main orchestration logic
│   └── parser.py     # JSON instruction classification engine (Tier 1)
├── tests/
│   ├── test_analyzer.py  # Unit tests tracking prefix normalizations
│   └── test_parser.py    # Unit tests grouping validation
├── data/
│   └── instr_dict.json   # Instruction landscape input files
├── README.md         # You are here!
└── sample_output.txt # Verifiable console log of the tool's execution
```

## 🛠️ Usage & Installation

**Prerequisites:** You need Python 3.7+ installed.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Annu881/RISC-V_TASK.git
   cd RISC-V_TASK
   ```

2. **Clone the official RISC-V manual** (Wait to let it download):
   ```bash
   git clone https://github.com/riscv/riscv-isa-manual riscv-isa-manual
   ```

3. **Run the Explorer:**
   ```bash
   export PYTHONPATH=$(pwd)
   python3 src/main.py
   ```

### Running the Test Suite
The tool provides rock-solid reliability through Python's standard `unittest` framework:
```bash
export PYTHONPATH=$(pwd)
python3 -m unittest discover tests/ -v
```

## 🧠 Design Philosophy & Extensibility

- **String Normalization Magic:** To ensure reliable 1-to-1 matching across datasets written by entirely different teams, strings are stripped from conventional architecture prefixes (`rv_`, `rv32_`, `rv64_`) and lowercase mapped automatically before graph comparisons.
- **Micro-Scraping vs Heavy Regex:** Instead of running heavy catastrophic tracking Regex over massive text-blocks within the ISA manual strings, `analyzer.py` explicitly captures modern `ext:...` tags ensuring the script remains blazing fast whilst extracting hundreds of distinct extensions without faltering.
