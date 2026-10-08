from pathlib import Path
targets = {
    "100+ Plug-and-Play n8n Templates/Youtube Videos Posting.json": [13],
    "100+ Plug-and-Play n8n Templates/Youtube Videos Posts.json": [34],
    "Youtube_Videos_Posting.json": [33],
    "100+ Plug-and-Play n8n Templates/Example AI Story Generator.json": [27],
    "Linkdein_Post_Generator.json": [39],
    "Perplexity_Node.json": [175],
    "100+ Plug-and-Play n8n Templates/Lead Generation using Apollo.json": [575],
}
for rel, lines in targets.items():
    p = Path(rel)
    rows = p.read_text(encoding="utf-8").splitlines()
    for n in lines:
        rows[n - 1] = '    "REDACTED": "PUT_KEY_IN_N8N_CREDENTIALS"'
    p.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print("rewrote", rel, lines)
