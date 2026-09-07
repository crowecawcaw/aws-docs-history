

This guide documents the classic version of the AWS Wickr administration console, released before March 13, 2025. For documentation on the new AWS Wickr administration console, see [ Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Start the bot with password environment variable (no AWS service)
<a name="data-retention-basic-startup"></a>

The following Docker command starts the data retention bot. The password is specified using the `WICKRIO_BOT_PASSWORD` environment variable. The bot starts using the default file streaming, and using the default values defined in the [Environment variables to configure data retention bot in AWS Wickr](data-retention-bot-env-variables.md) section of this guide.

```
docker run -v /opt/{{compliance_1234567890_bot}}:/tmp/{{compliance_1234567890_bot}} \
-d --restart on-failure:5 --name="{{compliance_1234567890_bot}}" -ti \
-e WICKRIO_BOT_NAME='{{compliance_1234567890_bot}}' \
-e WICKRIO_BOT_PASSWORD='{{password}}' \
public.ecr.aws/x3s2s6k3/wickrio/bot-compliance-cloud:latest
```