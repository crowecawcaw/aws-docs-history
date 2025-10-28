This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Start the bot with password

environment variable (no AWS service)

The following Docker command starts the data retention bot. The password is
specified using the `WICKRIO_BOT_PASSWORD` environment variable. The bot
starts using the default file streaming, and using the default values defined in the
[Environment variables to configure
data retention bot in AWS Wickr](data-retention-bot-env-variables.md "data-retention-bot-env-variables.md") section of this guide.

```
docker run -v /opt/`compliance_1234567890_bot`:/tmp/`compliance_1234567890_bot` \
-d --restart on-failure:5 --name="`compliance_1234567890_bot`" -ti \
-e WICKRIO_BOT_NAME='`compliance_1234567890_bot`' \
-e WICKRIO_BOT_PASSWORD='`password`' \
wickr/bot-compliance-cloud:latest
```
