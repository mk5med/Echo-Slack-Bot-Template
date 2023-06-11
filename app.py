import logging
from slack_bolt import App
from slack_sdk.web import WebClient
import dotenv

dotenv.load_dotenv()
state = {"app": App(), "logger": None}


def action_echo(client: WebClient, text: str, channel: str):
    """
    Echos a users message back to them
    """
    msg = {
        "channel": channel,
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"> {text}",
                },
            }
        ],
    }

    client.chat_postMessage(**msg)


@state["app"].event("message")
def message(event, client):
    channel_id: str = event.get("channel")
    user_id: str = event.get("user")
    text: str = event.get("text")

    # Text can be None for non-text message events
    if text is not None and text.startswith("echo"):
        action_echo(client, text, channel_id)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    state["app"].start(3000)
