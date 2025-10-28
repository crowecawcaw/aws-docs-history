This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Start the bot with password prompt

(no AWS service)

The following Docker command starts the data retention bot. Password is entered
when prompted by the data retention bot. It will start using the default file
streaming using the default values defined in the [Environment variables to configure
data retention bot in AWS Wickr](data-retention-bot-env-variables.md "data-retention-bot-env-variables.md") section of this guide.

```
docker run -v /opt/`compliance_1234567890_bot`:/tmp/`compliance_1234567890_bot` \
-d --restart on-failure:5 --name="`compliance_1234567890_bot`" -ti \
-e WICKRIO_BOT_NAME='`compliance_1234567890_bot`' \
wickr/bot-compliance-cloud:latest

docker attach `compliance_1234567890_bot`
.
.
.
Enter the password:************
Re-enter the password:************
```

Run the bot using the `-ti` option to receive the password prompt. You
should also run the `docker attach `<container ID or container
 name>`` command immediately after starting the docker
image so that you get the password prompt. You should run both of these commands in
a script. If you attach to the docker image and don’t see the prompt, press
**Enter** and you will see the prompt.
