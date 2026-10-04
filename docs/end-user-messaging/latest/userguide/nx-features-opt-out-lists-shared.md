

# List shared opt-out lists with the AWS CLI
<a name="nx-features-opt-out-lists-shared"></a>

You can use the [describe-opt-out-lists](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-opt-out-lists.html) to view opt-out lists shared with your account. For more information about shared resources, see the resource sharing documentation.

**To list all opt-out lists shared with your account using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 describe-opt-out-lists --owner {{SHARED}}
  ```

In the preceding command, replace {{SHARED}} with {{SELF}} to list the opt-out lists owned by your account.