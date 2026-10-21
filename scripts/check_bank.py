"""校验题库结构：python3 scripts/check_bank.py"""
import json, re, sys
b = json.load(open("data/cnc_question_bank.json", encoding="utf-8"))
err = []
for q in b["questions"]:
    if len(q["options"]) != 4 or not 0 <= q["answer"] < 4 or not q.get("explain") or not q.get("source"):
        err.append(f"question {q['id']}")
for g in b["bugs"]:
    if not 0 <= g["bad"] < len(g["code"]) or not g.get("fix") or not g.get("source"):
        err.append(f"bug {g['id']}")
for d in b["drawings"]:
    n = sum(len(re.findall(r"\{\{\d+\}\}", l)) for l in d["code"])
    if n != len(d["blanks"]) or any(len(x["options"]) != 4 or not 0 <= x["answer"] < 4 for x in d["blanks"]):
        err.append(f"drawing {d['id']}")
print(f"questions={len(b['questions'])} bugs={len(b['bugs'])} drawings={len(b['drawings'])} glossary={len(b['glossary'])}")
print("OK" if not err else "问题：" + ", ".join(err)); sys.exit(1 if err else 0)
