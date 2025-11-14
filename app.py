from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DEFAULT_GREETING = "Hey there! 😊 I’m CivicEase Help Bot. How can I assist you today?"

# Emergency numbers
EMERGENCY_CONTACTS = (
    "Here are important emergency contacts for Nashik City:<br>"
    "🚔 <b>Police:</b> 100 or +91-253-2317100<br>"
    "🚑 <b>Ambulance:</b> 108 or +91-253-6510108<br>"
    "🚒 <b>Fire:</b> 101 or +91-253-2501001"
)

@app.route("/")
def index():
    return render_template("index.html", greeting=DEFAULT_GREETING)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower().strip()

    # Abusive word filter
    abusive_words = ["mad", "idiot", "fool", "mc", "bc", "stupid", "chutiya","pagal","pgl","chutta","chutya"]
    if any(bad in user_msg for bad in abusive_words):
        return jsonify({"reply": "I’m here to assist you politely 😊 Let’s keep things friendly. How can I help you?"})

    # Greetings
    if user_msg in ["hi", "hii", "hello", "hey", "hey bot"]:
        return jsonify({"reply": DEFAULT_GREETING})

    if "how are you" in user_msg:
        return jsonify({"reply": "I’m doing great and always ready to help you! 💪 How can I assist you today?"})

    # NMC Address/location
    if any(word in user_msg for word in ["address", "location", "nmc", "municipal"]):
        return jsonify({"reply": "🏛️ <b>Nashik Municipal Corporation Address:</b><br>📍 Rajiv Gandhi Bhavan, Sharanpur Road, Nashik – 422002<br>👉 <a href='https://share.google/7qM0MPm78cp0YVVyj' target='_blank'>View on Google Maps</a>"})

    # Service requests (Street cleaning, tree pruning/removal, infrastructure)
    if any(word in user_msg for word in ["street cleaning", "clean street", "tree pruning", "tree removal", "broken", "damaged", "bench", "sign", "barrier", "public infrastructure"]):
        return jsonify({"reply":
            "For street cleaning, tree pruning/removal, or broken public infrastructure 🛠️, "
            "please raise a complaint in your dashboard. Describe the issue and upload a photo 📸. "
            "The admin will handle it and assign it to the right department, similar to earlier complaints."
        })

    # Garbage collection (schedule/missed pickup)
    if "garbage" in user_msg or "missed pickup" in user_msg or "garbage schedule" in user_msg:
        return jsonify({"reply":
            "For garbage collection schedule or missed pickups 🗑️, please contact the NMC Helpline at +91-253-2578500 or +91-253-2578450."
        })

    # Raise complaint section
    if "raise" in user_msg and "complaint" in user_msg:
        return jsonify({"reply":
            "To file a complaint 📝, go to your dashboard → 'Complaint Section' → raise a complaint and describe the issue along with a photo. Once submitted, the admin will validate your complaint, generate a token, and assign it to a sub-admin. You’ll be notified automatically. 🚀"
        })

    # Track complaint status
    if "track" in user_msg or "status" in user_msg:
        return jsonify({"reply":
            "To track your complaint status 🔍, log in to your account → go to 'My Complaints'. There you can see complaint status, assigned sub-admin, updates, and completion progress."
        })

    # Department wise help
    if "water" in user_msg:
        return jsonify({"reply":
            "For water or drainage-related issues 💧, contact the <b>Water Supply & Drainage Department</b>. Just raise your complaint, and admin will assign it to the correct sub-admin and worker department."
        })

    if any(word in user_msg for word in ["electric", "light", "power"]):
        return jsonify({"reply":
            "For electricity or traffic light issues ⚡, contact the <b>Electricity Department</b>. Just raise your complaint — admin will assign the right sub-admin."
        })

    if any(word in user_msg for word in ["road", "street", "pothole"]):
        return jsonify({"reply":
            "For road, street, or maintenance issues 🛣️, contact the <b>Maintenance Department</b>. Raise your complaint and the admin will take care of the rest."
        })

    if any(word in user_msg for word in ["illegal", "construction"]):
        return jsonify({"reply":
            "For illegal construction issues 🚧, contact the <b>Town Planning Department</b>. Raise your complaint → admin will assign token + sub-admin."
        })

    # City events/amenities (announcement dashboard)
    if any(word in user_msg for word in ["events", "amenity", "amenities", "festival", "community center", "library", "park"]):
        return jsonify({"reply":
            "For city events, amenities, and public facility timings 🗓️, please check the Announcement Section in your CivicEase app dashboard."
        })

    # Emergency contacts
    if any(word in user_msg for word in ["emergency", "ambulance", "police", "fire"]):
        return jsonify({"reply": f"{EMERGENCY_CONTACTS}<br><br>Stay safe! How else can I assist you?"})

    # Bus route information (public transport)
    if any(word in user_msg for word in ["bus route", "bus", "metro", "public transport"]):
        return jsonify({"reply":
            "For Nashik city government bus routes and metro details 🚌, please install the 'City Link Nashik KM' app from the Play Store for the latest routes and timings."
        })

    # Announcements (existing)
    if any(word in user_msg for word in ["announcement", "important news"]):
        return jsonify({"reply":
            "To see important civic announcements 📢, go to the <b>Announcement Section</b> in your CivicEase app."
        })
    
    if any(word in user_msg for word in ["bye", "thankyou","thanks", "thankyou for the help", "byee see you","bbye","bbe","bye cu"]):
        return jsonify({"reply": "Bye!I'm always ready to help you,anything you need just ask me!!"})

    # Service requests (Street cleaning, tree pruning/removal, infrastructure)

    # Default unknown handler
    return jsonify({"reply":
        "Sorry 😅, I didn’t quite understand that. Could you please rephrase or ask in another way?"
    })

if __name__ == "__main__":
    app.run(debug=True)
