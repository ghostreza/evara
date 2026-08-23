from flask import Flask, render_template, request
import content


TRANSLATIONS = {
    "en": {
        "charter": "Boat Charter", "home": "Home", "info_services": "Info & Services",
        "destinations": "Destinations", "booking": "Booking", "open_menu": "Open menu",
        "home_aria": "Evara - home", "hero_eyebrow": "BOAT CHARTER · OCEAN EXPERIENCES",
        "hero_title": "Sail with Evara", "hero_description": "with an experienced crew and complete equipment.",
        "book_now": "Book now", "see_destinations": "Explore destinations", "boat_length": "Boat length",
        "guest_capacity": "Guest capacity", "trip_options": "Trip options", "ready_journey": "Ready to accompany your journey",
        "story_title": "The Story Behind the Name", "boat_title": "Our Boat",
        "boat_description": "Regularly maintained and equipped with standard safety gear.",
        "name": "Name", "length": "Length", "capacity": "Capacity", "services_title": "Services & Packages",
        "services_description": "Choose your activity - crew and equipment are included.", "per_person": "/ person",
        "contact_us": "Contact us", "access_title": "Getting There & Booking",
        "access_description": "Choose your route to Tidung Island based on time, comfort, and budget.",
        "departure": "Departure", "fare": "Fare", "duration": "Duration", "schedule": "Schedule",
        "travel_steps": "Travel steps", "summary_title": "Choice summary", "from": "From", "boat": "Boat",
        "advantage": "Advantage", "important_tips": "Important tips", "ready_to_sail": "Ready to sail?",
        "check_book": "Check schedule & book", "dest_eyebrow": "EVARA JOURNEY MAP",
        "dest_title": "Destinations around Tidung", "dest_description": "Explore snorkeling, diving, and fishing spots from Tidung Island Pier.",
        "selected_spots": "SELECTED SPOTS", "sea_locations": "sea locations", "filter_dest": "Destination filter",
        "all": "All", "departure_point": "departure point", "see_map": "View on map",
        "booking_description": "Fill in the form - your message will be neatly prepared and sent to our WhatsApp/email to start the conversation.",
        "your_name": "Your name", "trip_date": "Trip date", "number_people": "Number of people", "package": "Package",
        "notes": "Notes", "special_request": "Special requests, own equipment, etc.", "estimate": "Cost estimate",
        "estimate_description": "Automatic estimate = package price x number of people. Final cost is confirmed by the crew and may vary by destination and fuel.",
        "send_whatsapp": "Send via WhatsApp", "send_email": "Send via Email", "contact_crew": "Contact crew",
    }
}


def localized_items(items, translations, fields):
    return [{**item, **{field: translations.get(item[field], item[field]) for field in fields}} for item in items]


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    @app.context_processor
    def inject_language():
        lang = request.args.get("lang", "id")
        if lang not in ("id", "en"):
            lang = "id"
        return {"lang": lang, "t": TRANSLATIONS.get(lang, {})}

    @app.route("/")
    def index():
        lang = request.args.get("lang", "id")
        data = content.localized_content(lang)
        return render_template("index.html",
                               site=data["site"], boat=data["boat"], services=data["services"],
                               steps=data["access_steps"], story=data["story"], story_sign=data["story_sign"],
                               story_media=data["story_media"], access_options=data["access_options"],
                               access_comparison=data["access_comparison"], access_tips=data["access_tips"])

    @app.route("/destinasi")
    def destinasi():
        data = content.localized_content(request.args.get("lang", "id"))
        return render_template("destinations.html", site=data["site"],
                               home_port=data["home_port"], rings=data["rings"], spots=data["spots"])

    @app.route("/booking")
    def booking():
        data = content.localized_content(request.args.get("lang", "id"))
        return render_template("booking.html",
                               site=data["site"], services=data["services"])

    return app


app = create_app()

if __name__ == "__main__":
    import os

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)