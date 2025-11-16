AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Troubleshooting credentials

problems with Snowball Edge

Use the following topics to help you resolve credentials issues with the Snowball Edge device.

## Unable to locate AWS CLI

credentials for Snowball Edge

If you're communicating with the AWS Snowball Edge device through the Amazon S3
interface using the AWS CLI, you might encounter an error message that says
**`Unable to locate credentials. You can configure credentials by
 running "aws configure".`**

###### Action to take

Configure the AWS credentials that the AWS CLI uses to run commands for you. For
more information, see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the
_AWS Command Line Interface User Guide_.

## Troubleshooting Snowball Edge error message: Check Your Secret

Access Key and Signing

When using the Amazon S3 interface to transfer data to a Snowball Edge,
you might encounter the following error message.

```
An error occurred (SignatureDoesNotMatch) when calling the CreateMultipartUpload operation: The request signature we calculated does not match the signature you provided.
Check your AWS secret access key and signing method. For more details go to:
http://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html#ConstructingTheAuthenticationHeader

```

###### Action to take

Get your credentials from the Snowball Edge client. For more information, see
[Getting credentials for a Snowball Edge](using-client-commands.md#client-credentials "using-client-commands.md#client-credentials").
