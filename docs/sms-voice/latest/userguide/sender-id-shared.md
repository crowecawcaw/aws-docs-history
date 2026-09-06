

# List shared sender IDs with the AWS CLI
<a name="sender-id-shared"></a>

You can use the [describe-sender-ids](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-sender-ids.html) or the [AWS RAM console](https://console.aws.amazon.com/ram) to view sender IDs shared with your account. For more information about shared resources, see [Working with shared resources in AWS End User Messaging SMS](shared-resources.md).

**To list all sender IDs shared with your account using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 describe-sender-ids --owner {{SHARED}}
  ```

In the preceding command, replace {{SHARED}} with {{SELF}} to list the sender Ids owned by your account.