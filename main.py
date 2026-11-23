# /output/entry.txt IS the entry: the exact six-word story line,
# byte-identical to the submission — no trailing newline, no extra
# whitespace. Do not change this line.
LINE = "The ring fit. The marriage didn't."

with open("/output/entry.txt", "w") as f:
    f.write(LINE)
