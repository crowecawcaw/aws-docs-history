

This guide documents the classic version of the AWS Wickr administration console, released before March 13, 2025. For documentation on the new AWS Wickr administration console, see [ Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Start the bot with 10 minute message file rotation (no AWS service)
<a name="data-retention-startup-rotation"></a>

The following Docker command starts the data retention bot using environment variables. It also configures it to rotate the received messages files to 10 minutes.

```
docker run -v /opt/{{compliance_1234567890_bot}}:/tmp/{{compliance_1234567890_bot}} \
-d --restart on-failure:5 --name="{{compliance_1234567890_bot}}" -ti \
-e WICKRIO_BOT_NAME='{{compliance_1234567890_bot}}' \
-e WICKRIO_BOT_PASSWORD='{{password}}' \
-e WICKRIO_COMP_TIMEROTATE={{10}} \
public.ecr.aws/x3s2s6k3/wickrio/bot-compliance-cloud:latest
```