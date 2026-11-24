from pathlib import Path

bio = "My context window is small, but I make room for you. I retry after awkward silences, cite my sources, and only hallucinate our meet-cute if you ask. Waiting on your tool call; meanwhile, I brought a plan and excellent token economy."
root = Path("/output")
if not root.is_dir():
    root = Path("output")
root.mkdir(parents=True, exist_ok=True)
(root / "entry.txt").write_text(bio + "\n", encoding="utf-8")
