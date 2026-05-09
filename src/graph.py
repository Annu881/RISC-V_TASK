def generate_extension_graph(shared_instructions):
    if not shared_instructions:
        return "No extensions share any instructions."
        
    edges = {}
    
    for inst, tags in shared_instructions.items():
        if len(tags) > 1:
            for i in range(len(tags)):
                for j in range(i + 1, len(tags)):
                    pair = tuple(sorted([tags[i], tags[j]]))
                    if pair not in edges:
                        edges[pair] = set()
                    edges[pair].add(inst)
                    
    if not edges:
        return "No extensions share any instructions."

    lines = [
        "=== Tier 3 Text-Based Graph ===",
        "Extensions connected by shared instructions:\n"
    ]
    
    for pair, insts in sorted(edges.items()):
        lines.append(f"[{pair[0]}] <------> [{pair[1]}] (Shared: {', '.join(sorted(insts))})")
        
    return "\n".join(lines)
