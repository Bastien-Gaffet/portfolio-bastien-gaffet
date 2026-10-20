"""Exact single-occurrence replacements that keep each file's line endings."""
def rep(f, pairs):
    s = open(f, encoding="utf-8", newline="").read()
    nl = "\r\n" if "\r\n" in s else "\n"
    for old, new in pairs:
        old, new = old.replace("\n", nl), new.replace("\n", nl)
        c = s.count(old)
        assert c == 1, f"{f}: {c} x {old[:70]!r}"
        s = s.replace(old, new)
    open(f, "w", encoding="utf-8", newline="").write(s); print(f, "ok", len(pairs))
