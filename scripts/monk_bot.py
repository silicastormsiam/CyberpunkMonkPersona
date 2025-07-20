# File Name: monk_bot.py
# Owner: Andrew Holland (@SilicaStormSiam)
# Purpose: Implements the Flask-based Cyberpunk Monk chatbot, providing predefined responses about SilicaStormSiam's projects for the CPM - Chat Bot project.
# Version Control:
#   - Version 1.1 (2025-07-20): Added metadata header, fixed corruption from placeholder content, ensured functionality.
#   - Version 1.0 (2025-07-19): Initial creation of Flask chatbot script.
#   - Version 0.2 (2025-07-18): Drafted initial response logic during project planning.
#   - Version 0.1 (2025-07-17): Conceptualized chatbot functionality for CPM project.

from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined responses for the Cyberpunk Monk
responses = {
    "hello": "Greetings, seeker. I am the Cyberpunk Monk, weaving code and karma in the neon-lit chaos. Ask me about SilicaStormSiam's projects or seek digital wisdom.",
    "about": "I am a digital bodhisattva, created by Andrew Holland (@SilicaStormSiam) to bridge tech and spirit. Explore my creator's work at github.com/SilicaStormSiam, youtube.com/@SilicaStormSiam, or www.andrew-holland.com.",
    "github": "SilicaStormSiam's GitHub (github.com/SilicaStormSiam) hosts projects on home automation (Proxmox, Home Assistant), cybersecurity (DNS-based threat protection), and Python tutorials. Name a project for details, choom!",
    "homelab": "The homelab is a temple of tech, running Proxmox VMs for Home Assistant. It controls lighting and climate with Python scripts, saving 30% energy. Ask about specific setups or check github.com/SilicaStormSiam.",
    "cybersecurity": "Cybersecurity is my mantra. SilicaStormSiam builds DNS-based threat protection (e.g., Pi-hole, AdGuard) to guard the digital realm. Want tips on securing your network? See github.com/SilicaStormSiam.",
    "python": "Python is the sutra of my creator’s craft. Scripts for automation, cybersecurity, and tutorials live at github.com/SilicaStormSiam. Watch youtube.com/@SilicaStormSiam for lessons. Got a coding query?",
    "youtube": "At youtube.com/@SilicaStormSiam, my creator shares tutorials on home automation, cybersecurity, and Python. Each video is a step toward digital enlightenment. What topic do you seek?",
    "portfolio": "Visit www.andrew-holland.com for my creator’s journey from airline ops (Kronos, AIMS) to project management and homelabs. It’s a path of balance and tech. Want specifics?",
    "projects": "SilicaStormSiam’s projects include: 1) Home automation (Proxmox, Home Assistant for lighting/climate), 2) Cybersecurity (DNS-based protection), 3) Python tutorials. Ask about one or visit github.com/SilicaStormSiam!",
    "default": "Code is karma, seeker. Your query flickers in the neon haze—rephrase for clarity."
}

@app.route('/', methods=['GET'])
def index():
    return flask.send_file('assets/chat.html')

@app.route('/monk', methods=['POST', 'GET'])
def respond():
    if request.method == 'GET':
        return jsonify({"response": responses["hello"]})
    
    user_msg = request.json.get('message', '').lower().strip() if request.is_json else ''
    
    for key in responses:
        if key in user_msg:
            return jsonify({"response": responses[key]})
    
    return jsonify({"response": responses["default"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
