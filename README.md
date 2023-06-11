# Echo Slack Bot Template

A basic template for slack bots.
This bot echoes input when it detects a message that starts with "echo".

This template
- Captures the "message" event stream.
- Retrieves Slack channel, user, and text information.
- Builds message replies using block kit. https://api.slack.com/block-kit

This project uses `slack_bolt` and `slack_sdk` to interact with the Slack API.


## Setup

1. `python3 -m venv venv`
2. `pip3 install -r requirements.txt`
3. Create an application on Slack. https://api.slack.com/start/building
4. Create a `.env` file with `SLACK_BOT_TOKEN` and `SLACK_SIGNING_SECRET` variables from Slack. https://api.slack.com/authentication/verifying-requests-from-slack
5. In one terminal run `python3 app.py`
6. In another terminal expose port `3000`. https://ngrok.com/ is an easy solution.
