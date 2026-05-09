import os
from src.parser import load_instructions, parse_instructions, generate_tier1_summary
from src.analyzer import extract_extensions_from_manual, cross_reference, generate_tier2_summary
from src.graph import generate_extension_graph

def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    json_path = os.path.join(base_dir, 'data', 'instr_dict.json')
    manual_path = os.path.join(base_dir, 'riscv-isa-manual', 'src')
    
    try:
        data = load_instructions(json_path)
    except FileNotFoundError:
        print(f"Error: Could not find {json_path}")
        return
        
    ext_dict, shared_dict = parse_instructions(data)
    print(generate_tier1_summary(ext_dict, shared_dict))
    
    print("\n" + "="*45 + "\n")
    
    manual_exts = extract_extensions_from_manual(manual_path)
    if not manual_exts:
        print("Warning: No extensions found in ISA manual. Did you clone it into riscv-isa-manual?")
    
    cross_data = cross_reference(ext_dict, manual_exts)
    print(generate_tier2_summary(cross_data))
    
    print("\n" + "="*45 + "\n")
    print(generate_extension_graph(shared_dict))

if __name__ == "__main__":
    main()
