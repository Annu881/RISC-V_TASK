import json
from collections import defaultdict

def load_instructions(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def parse_instructions(instructions):
    extensions = defaultdict(list)
    shared_instructions = {}
    
    for mnemonic, details in instructions.items():
        exts = details.get("extension", [])
        for ext in exts:
            extensions[ext].append(mnemonic)
            
        if len(exts) > 1:
            shared_instructions[mnemonic] = exts
            
    return extensions, shared_instructions

def generate_tier1_summary(extensions, shared_instructions):
    lines = [
        "=== Tier 1 Classification ===",
        f"{'Extension':<15} | {'Count':<15} | {'Example'}",
        "-" * 45
    ]
    
    for ext, insts in sorted(extensions.items()):
        lines.append(f"{ext:<15} | {len(insts):<4} instructions | e.g. {insts[0].upper()}")
        
    lines.append("\n=== Shared Instructions ===")
    if not shared_instructions:
        lines.append("No instructions belong to more than one extension.")
    else:
        for inst, tags in sorted(shared_instructions.items()):
            lines.append(f"{inst.upper():<10} belongs to {', '.join(tags)}")
            
    return "\n".join(lines)

if __name__ == "__main__":
    data = load_instructions("../data/instr_dict.json")
    ext, shared = parse_instructions(data)
    print(generate_tier1_summary(ext, shared))
