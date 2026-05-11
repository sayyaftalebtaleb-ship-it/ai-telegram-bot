import os, sys, time

print("Running...", flush=True)
time.sleep(1)

if not os.environ.get("7965345356:AAEiY2Q3UQ6WZvpFQAAmap0eebvLRvWXVuY"):
    print("MISSING BOT_TOKEN", flush=True)
    sys.exit(1)
if not os.environ.get("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"):
    print("MISSING GROQ_API_KEY", flush=True)
    sys.exit(1)
print("All good!", flush=True)
