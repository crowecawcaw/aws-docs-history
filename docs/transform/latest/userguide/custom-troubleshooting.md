# Troubleshooting

This section provides guidance for troubleshooting common issues with AWS Transform custom.

## Log Locations

AWS Transform CLI maintains logs in the following locations:

**Conversation logs:**

```
~/.aws/atx/custom/<conversation_id>/logs/<timestamp>-conversation.log
```

These logs contain the full conversation history for debugging specific transformation executions.

**Developer debug logs:**

```
~/.aws/atx/logs/debug*.log
~/.aws/atx/logs/error.log
```

These logs provide detailed information about CLI operations and errors.
Each log file has a 5MB limit before it rolls over. There may be multiple debug logs in this directory, such as debug1.log and debug2.log.

## Common Issues

**Installation issues:**

If installation fails, ensure you have Node.js 20 or later installed:

```
node --version
```

Download Node.js from https://nodejs.org/en/download if needed.

**Authentication issues:**

Verify your AWS credentials are configured correctly:

```
aws sts get-caller-identity
```

Ensure your IAM user or role has the required `transform-custom:*` permissions.

**Network connectivity issues:**

If you encounter connection errors, verify network access to required endpoints:

- `transform-cli.awsstatic.com`
- `transform-custom.<region>.api.aws`
- `*.s3.amazonaws.com`

If working in an internet-restricted environment, update firewall rules to allowlist these URLs.

**Region configuration issues:**

If you encounter region-related errors:

- Verify your region is supported
- Check for environment variables that may override your configuration: `echo $AWS_REGION $AWS_DEFAULT_REGION`
- Check your region configuration: `aws configure get region`
- Update your region if needed: `aws configure set region <your-region>`
- Check debug logs for region resolution details

**Git issues:**

Ensure Git is installed and your repository is under git source control:

```
git --version
git status
```

AWS Transform custom requires repositories to be under git source control.

**Transformation execution issues:**

If a transformation fails:

1. Review the conversation logs at `~/.aws/atx/custom/<conversation_id>/logs/`
2. Check for build or test failures in the transformation output
3. Verify the build command is correct for your project
4. Try running the transformation in interactive mode to provide feedback

**Conversation resumption issues:**

If you cannot resume a conversation:

- Verify the conversation is less than 30 days old
- Check the conversation ID is correct
- Ensure you have network connectivity

## Getting Support

For additional assistance, visit AWS Support through the [AWS Console](https://support.console.aws.amazon.com/support/home#/ "https://support.console.aws.amazon.com/support/home#/").

When opening a support ticket, include:

- Conversation logs from `~/.aws/atx/custom/<conversation_id>/logs/`
- Debug logs from `~/.aws/atx/logs/`
- Steps to reproduce the issue
- AWS Transform CLI version (`atx --version`)

## S3 access issues

The AWS Transform custom service vends S3 pre-signed URLs to facilitate uploading and downloading the potentially large transformation files to/from client machines. This means that not only does the CLI interact with the AWS Transform service endpoints but it also interacts with the S3 service endpoints. These interactions use pre-signed URLs so your client's IAM credentials **do not** require any S3 permissions but sometimes your local machine's proxy server configurations and your network's S3 VPC Endpoint Policies can restrict this traffic.

Please examine the [Log Locations](#custom-log-locations "#custom-log-locations") for more detailed error messages to help root cause any tool failures or S3 access denied relating to downloading and uploading transformation files.

If you are using a VPN/Proxy server that leverages the `https_proxy` and `no_proxy` environment variables, consider adding the following values to your `no_proxy` environment variable value to bypass the proxy for the S3 and AWS Transform custom service endpoints, for example:

`export no_proxy=.s3.amazonaws.com,.transform-custom.<region>.api.aws`

If you are using an [AWS PrivateLink for Amazon S3](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md") in your VPC,
this may have a policy defined to restrict S3 traffic. Please ensure your S3 VPC endpoint policy allows `GetObject` and `PutObject` operations for the AWS Transform
custom service-owned buckets. This can be accomplished by adding the following statement to your VPC endpoint policy:

```
{
    "Effect": "Allow",
    "Principal": "*",
    "Action": ["s3:PutObject","s3:GetObject"],
    "Resource": "arn:aws:s3:::aws-transform-custom-*/*"
}
```

Explicit `Deny` statements in policies take precedence over
`Allow` statements. Review S3 VPC Endpoint policies for
`Deny` statements that may be restricting access.
