import os
import glob

def get_block_indices(lines, summary_keyword):
    summary_idx = -1
    for i, line in enumerate(lines):
        if f"<summary>{summary_keyword}</summary>" in line:
            summary_idx = i
            break
    if summary_idx == -1: return None, None
    
    # scan back for details start
    start_idx = -1
    for i in range(summary_idx, -1, -1):
        if "<details" in lines[i]:
            start_idx = i
            break
            
    # scan forward for details end
    end_idx = -1
    for i in range(summary_idx, len(lines)):
        if "</details>" in lines[i]:
            end_idx = i
            break
            
    if start_idx == -1 or end_idx == -1:
        return None, None
        
    return start_idx, end_idx

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    prod_start, prod_end = get_block_indices(lines, "生産活動")
    welf_start, welf_end = get_block_indices(lines, "福祉事業活動")
    
    if prod_start is None:
        print(f"Skipping {path}: 'Production Activity' not found")
        return
    if welf_start is None:
        print(f"Skipping {path}: 'Welfare Activity' not found")
        return
        
    # Only move if Production is CURRENTLY BEFORE Welfare
    if prod_start < welf_start:
        print(f"Updating {path}...")
        
        # Extract Production Block
        prod_block = lines[prod_start : prod_end + 1]
        
        # Remove Production Block from lines
        # We construct a new list excluding these lines
        remaining = lines[:prod_start] + lines[prod_end + 1:]
        
        # Recalculate Welfare indices in 'remaining'
        # Since we removed `len(prod_block)` lines BEFORE Welfare, we shift indices
        shift = len(prod_block)
        new_welf_start = welf_start - shift
        new_welf_end = welf_end - shift
        
        # Verify correctness (paranoid check)
        if f"<summary>福祉事業活動</summary>" not in remaining[new_welf_start + 1]: # +1 approx
             # Fallback: re-search in remaining
             new_welf_start, new_welf_end = get_block_indices(remaining, "福祉事業活動")
        
        if new_welf_end is None:
            print(f"Error in {path}: Lost Welfare block after removal")
            return

        # Insert Production Block AFTER Welfare Block
        insertion_point = new_welf_end + 1
        
        final_lines = remaining[:insertion_point] + prod_block + remaining[insertion_point:]
        
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(final_lines)
    else:
        print(f"Skipping {path}: Production is already after Welfare (or structure differs)")

html_files = glob.glob("*.html")
for html_file in html_files:
    process_file(html_file)
