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
                               story=content.STORY, story_sign=content.STORY_SIGN,
                               story_media=content.STORY_MEDIA,
                               access_options=content.ACCESS_OPTIONS,
                               access_comparison=content.ACCESS_COMPARISON,
                               access_tips=content.ACCESS_TIPS)

    @app.route("/destinasi")
    def destinasi():
        return render_template("destinations.html", site=content.SITE,
                               home_port=content.HOME_PORT, rings=content.RINGS,
                               spots=content.SPOTS)

    @app.route("/booking")
    def booking():
        return render_template("booking.html",
                               site=content.SITE, services=content.SERVICES)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)