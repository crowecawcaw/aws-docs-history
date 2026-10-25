

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Start the data retention bot for your Wickr network
<a name="starting-data-retention-bot"></a>

Before you run the data retention bot, you should determine how you want to configure it. If you plan to run the bot on a host that:
+ Will not have access to AWS services, then your options are limited. In that case you will use the default message streaming options. You should decide whether you want to limit the size of the captured message files to a specific size or time interval. For more information, see [Environment variables to configure data retention bot in AWS Wickr](data-retention-bot-env-variables.md).
+ Will have access to AWS services, then you should create a Secrets Manager secret to store the bot credentials, and AWS service configuration details. After the AWS services are configured, you can proceed to start the data retention bot Docker image. For more information about the details you can store in a Secrets Manager secret, see [Secrets Manager values for AWS Wickr](data-retention-aws-secret-values.md)

The following sections show example commands to run the data retention bot Docker image. In each of the example commands, replace the following example values with your own:
+ `{{compliance_1234567890_bot}}` with the name of your data retention bot.
+ `{{password}}` with the password for your data retention bot.
+ `{{wickr/data/retention/bot}}` with the name of your Secrets Manager secret to use with your data retention bot.
+ `{{bucket-name}}` with the name of the Amazon S3 bucket where messages and files will be stored.
+ `{{folder-name}}` with the folder name in the Amazon S3 bucket where messages and files will be stored.
+ `{{us-east-1}}` with the AWS Region of the resource you're specifying. For example, the Region of the AWS KMS master key or the Region of the Amazon S3 bucket.
+ `{{arn:aws:kms:us-east-1:111122223333:key/12345678-1234-abcde-a617-abababababab}}` with the Amazon Resource Name (ARN) of your AWS KMS master key to use to re-encrypt message files and files.

**Persist bot data across restarts**

The data retention bot stores its device identity and encryption keys in the folder that you mount with the `-v` option in the run command (for example, `-v /opt/{{compliance_1234567890_bot}}:/tmp/{{compliance_1234567890_bot}}`). The bot uses this data to log in as the same device every time it starts. Make sure that the mounted host folder:
+ Is included in the run command every time you start the bot, with the same host folder and path.
+ Is on durable storage, such as the instance's Amazon EBS volume, and not on temporary storage.
+ Is kept when you restart, upgrade, or replace the container.

**Important**  
If you start the bot without this folder (for example, by running `docker run` without the `-v` option, or after deleting the host folder), the bot registers as a new device with new encryption keys. Messages sent to the previous device are not delivered to the new device, and the new device cannot decrypt data that was encrypted with the previous device's keys.