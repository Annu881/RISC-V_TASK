import os
import re

def extract_extensions_from_manual(manual_src_path):
    extensions = set()
    
    if not os.path.exists(manual_src_path):
        return extensions

    for root, _, files in os.walk(manual_src_path):
        if "vendor" in root or "build" in root:
            continue
            
        for file in files:
            if not (file.endswith('.adoc') or file.endswith('.asciidoc')):
                continue
                
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    # check for modern ext macro usage like ext:zba
                    if 'ext:' in line:
                        for m in re.findall(r'ext:([a-zA-Z0-9_]+)', line, re.IGNORECASE):
                            extensions.add(m)
                    
                    # check for heading declarations e.g. == "M" Standard Extension
                    if line.startswith('=') and 'Extension' in line:
                        match = re.search(r'^==+\s+"?([A-Za-z0-9_]+)"?', line)
                        if match:
                            ext = match.group(1)
                            # ignore common generic words
                            if ext.lower() not in ["standard", "additional", "custom", "possible", "compressed", "base", "unprivileged", "supervisor"]:
                                extensions.add(ext)

    return extensions

def normalize_extension(ext):
    ext = ext.lower()
    ext = re.sub(r'^rv(?:32|64|128)?_', '', ext)
    ext = re.sub(r'^rv(?:32|64|128)', '', ext)
    return ext

def cross_reference(json_dict, manual_set):
    json_norm = {normalize_extension(k): k for k in json_dict.keys()}
    manual_norm = {normalize_extension(k): k for k in manual_set}
    
    js = set(json_norm.keys())
    ms = set(manual_norm.keys())
    
    return {
        "json_only": [json_norm[k] for k in js - ms],
        "manual_only": [manual_norm[k] for k in ms - js],
        "both": [json_norm[k] for k in js & ms]
    }

def generate_tier2_summary(cross_ref_data):
    json_only = cross_ref_data["json_only"]
    manual_only = cross_ref_data["manual_only"]
    both = cross_ref_data["both"]
    
    return f"""=== Tier 2 Cross-Reference ===
Summary: {len(both)} matched, {len(json_only)} in JSON only, {len(manual_only)} in manual only.

Extensions ONLY in JSON ({len(json_only)}):
{", ".join(sorted(json_only)) if json_only else "None"}

Extensions ONLY in Manual ({len(manual_only)}):
{", ".join(sorted(manual_only)) if manual_only else "None"}"""
