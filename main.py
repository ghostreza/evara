from flask import Flask, render_template
import content


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    @app.route("/")
    def index():
        return render_template("index.html",
                               site=content.SITE, boat=content.BOAT_INFO,
                               services=content.SERVICES, steps=content.ACCESS_STEPS,
                               story=content.STORY)

    @app.route("/destinasi")
    def destinasi():
        return render_template("destinations.html",
                               site=content.SITE, destinations=content.DESTINATIONS)

    @app.route("/booking")
    def booking():
        return render_template("booking.html",
                               site=content.SITE, services=content.SERVICES)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)