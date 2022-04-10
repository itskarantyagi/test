"""App entry point."""
import os
from app import create_app
import logging
app = create_app()

if __name__ == "__main__":
    logging.info("DONEEEEE *******************#************************* app")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
