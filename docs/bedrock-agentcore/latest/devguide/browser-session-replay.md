# Browser session recording and replay

Browser session recording and replay provides comprehensive observability for debugging,
auditing, or training purposes. When you create a browser with session recording enabled,
Amazon Bedrock AgentCore automatically captures browser interactions and stores them in your
specified Amazon S3 bucket for later analysis.

Session replay captures comprehensive browser interaction data that enables you to view
replays and understand the actions that occurred during browser sessions. This functionality
helps you resolve errors and improve future invocations by providing detailed insights into
browser behavior.

Information collected during session replay includes:

- Session DOM changes and mutations
- User actions including clicks, scrolls, and form interactions
- Console logs and error messages
- Chrome DevTools Protocol (CDP) events
- Network events and HTTP requests

## Prerequisites for session recording

To enable session recording, you need:

- An Amazon S3 bucket to store recording data
- An IAM execution role with permissions to write to your Amazon S3 bucket
- A custom browser tool configured with recording enabled

## Configure IAM role for recording

To enable session recording, you need an IAM execution role with permissions to write
recording data to Amazon S3 and log activity to CloudWatch. For detailed instructions on setting up
permissions, see [Permissions](browser-resource-session-management.md#browser-permissions "browser-resource-session-management.md#browser-permissions").

The execution role requires additional permissions beyond the standard browser
permissions:

```
{
    "Sid": "S3Permissions",
    "Effect": "Allow",
    "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:ListMultipartUploadParts",
        "s3:AbortMultipartUpload"
    ],
    "Resource": [
        "arn:aws:s3:::your-recording-bucket",
        "arn:aws:s3:::your-recording-bucket/*"
    ]
},
{
    "Sid": "CloudWatchLogsPermissions",
    "Effect": "Allow",
    "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams"
    ],
    "Resource": "*"
}
```

Replace `your-recording-bucket` with your actual Amazon S3 bucket name.

The following sections show you how to use session replay and some programmatic
examples.

###### Topics

- [How to use session replay](session-replay-how-to-use.md "session-replay-how-to-use.md")
- [Session replay programmatic
  examples](session-replay-programmatic-usage.md "session-replay-programmatic-usage.md")
