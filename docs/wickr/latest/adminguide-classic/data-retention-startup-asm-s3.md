This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Start the bot and configure Amazon S3

with Secrets Manager

You can use the Secrets Manager to host the credentials, and the Amazon S3 bucket information.
When you start the data retention bot, you will need to set an environment variable
that specifies the Secrets Manager where this information is stored.

```
docker run -v /opt/`compliance_1234567890_bot`:/tmp/`compliance_1234567890_bot` --network=host \
-d --restart on-failure:5 --name="`compliance_1234567890_bot`" -ti \
 -e WICKRIO_BOT_NAME='`compliance_1234567890_bot`' \
 -e AWS_SECRET_NAME='`wickrpro/alpha/compliance_1234567890_bot`' \
wickr/bot-compliance-cloud:latest
```

The `wickrpro/compliance/compliance_1234567890_bot` secret has the
following secret value in it, shown as plaintext.

```
{
    "password":"`password`",
    "s3_bucket_name":"`bucket-name`",
    "s3_region":"`us-east-1`",
    "s3_folder_name":"`folder-name`"
}
```

Messages and files received by the bot will be put in the
`bot-compliance` bucket in the folder named
`network1234567890`.
