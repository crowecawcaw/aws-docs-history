This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Start the bot with 15 minute

message file rotation (no AWS service)

The following Docker command starts the data retention bot using environment
variables. It also configures it to rotate the received messages files to 15
minutes.

```
docker run -v /opt/`compliance_1234567890_bot`:/tmp/`compliance_1234567890_bot` --network=host \
-d --restart on-failure:5 --name="`compliance_1234567890_bot`" -ti \
-e WICKRIO_BOT_NAME='`compliance_1234567890_bot`' \
-e WICKRIO_BOT_PASSWORD='`password`' \
-e WICKRIO_COMP_TIMEROTATE=`15` \
wickr/bot-compliance-cloud:latest
```
