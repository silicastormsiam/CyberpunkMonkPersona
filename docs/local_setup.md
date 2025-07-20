---
File Name: local_setup.md
Owner: Andrew Holland (@SilicaStormSiam)
Purpose: Provides setup instructions for running the Cyberpunk Monk Chatbot locally, including requirements and testing steps.
Version Control:
  - Version 1.1 (2025-07-20): Added metadata header, updated setup instructions for CPM - Chat Bot project.
  - Version 1.0 (2025-07-19): Initial creation of setup guide for local hosting.
  - Version 0.2 (2025-07-18): Drafted initial setup steps during project planning.
  - Version 0.1 (2025-07-17): Conceptualized setup requirements for chatbot.
---

# Local Setup for Cyberpunk Monk Chatbot

## Requirements
- Python 3.11
- Flask (`pip install flask`)
- Git Bash (Windows) or Linux terminal

## Instructions
1. Clone: `git clone git@github.com:SilicaStormSiam/CyberpunkMonkPersona.git`
2. Install: `pip install flask`
3. Run: `python scripts/monk_bot.py`
4. Test: `curl -X POST -H "Content-Type: application/json" -d '{"message":"github"}' http://localhost:5000/monk` or visit `http://localhost:5000` in a browser.
5. Query examples: "homelab", "cybersecurity", "python".

## Notes
- Runs on `localhost:5000` by default.
- For network access, use your local IP (e.g., `192.168.x.x:5000`).
- Future: Deploy on Tor .onion site (see `scripts/tor_setup.sh`).
