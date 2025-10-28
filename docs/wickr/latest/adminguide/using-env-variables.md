This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Start the bot and configure Amazon S3 using

environment variables

If you don't want to use Secrets Manager to host the data retention bot credentials, you can
start the data retention bot Docker image with the following environment variables.
You must identify the name of the data retention bot using the
`WICKRIO_BOT_NAME` environment variable.

```
docker run -v /opt/`compliance_1234567890_bot`:/tmp/`compliance_1234567890_bot` --network=host \
-d --restart on-failure:5 --name="`compliance_1234567890_bot`" -ti \
-e WICKRIO_BOT_NAME='`compliance_1234567890_bot`' \
-e WICKRIO_BOT_PASSWORD='`password`' \
-e WICKRIO_S3_BUCKET_NAME='`bot-compliance`' \
-e WICKRIO_S3_FOLDER_NAME='`network1234567890`' \
-e WICKRIO_S3_REGION='`us-east-1`' \
wickr/bot-compliance-cloud:latest
```

You can use environment values to identify the data retention bot’s credentials,
information about Amazon S3 buckets, and configuration information for the default file
streaming.
