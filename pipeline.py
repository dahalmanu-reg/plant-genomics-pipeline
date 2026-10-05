import os
def analyze_sequence(name, seq):
    dna = seq.upper()
    length = len(dna)
    g = dna.count('G')
    c = dna.count('C')
    gc_content = ((g + c) / length) * 100 if length > 0 else 0
    rna = dna.replace('T', 'U')
    
    return {
        "name": name,
        "length": length,
        "gc_content": round(gc_content, 2),
        "rna": rna
    }

def run_pipeline():
    print("=== STARTING PLANT GENOMICS PIPELINE ===")
    
    # Sample plant sequences (e.g., different gene fragments or species)
    plant_samples = {
        "Rice_Drought_Gene": "ATGCGATCGATCGATCGATCGATAGCTAGCTA",
        "Barley_Stress_Gene": "GCTAGCTAGCTAGCTACGATCGATCGATCGAT",
        "Arabidopsis_Control": "AAAAATTTTTCCCCGGGGGAAAAATTTTCCCC"
    }
    
    results_report = []
    
    for name, seq in plant_samples.items():
        res = analyze_sequence(name, seq)
        results_report.append(res)
        print(f"Processed: {res['name']} | Length: {res['length']} bp | GC: {res['gc_content']}%")
        
    # Save a summary output file
    output_filename = "pipeline_summary.txt"
    with open(output_filename, "w") as f:
        f.write("Plant ID\tLength(bp)\tGC_Content(%)\tRNA_Sequence\n")
        for r in results_report:
            f.write(f"{r['name']}\t{r['length']}\t{r['gc_content']}\t{r['rna']}\n")
            
    print(f"\nPipeline completed successfully! Summary saved to {output_filename}")
    print("========================================")

if __name__ == "__main__":
    run_pipeline()
