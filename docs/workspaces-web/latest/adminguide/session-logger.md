# Setting up Session Logger for Amazon WorkSpaces Secure Browser

###### Warning

Enabling Session Logger disables the following Chrome features:

- Incognito mode
- Developer Tools
- Chrome Profile Switching
  To activate session logger for a WorkSpaces Secure Browser portal, you must first identify the Amazon S3 bucket
  where session events will be collected. You can use an existing bucket that already stores
  similar logs or create a new one specifically for this purpose.

The Amazon S3 bucket must have a bucket policy that grants WorkSpaces Secure Browser permission to write logs to it.
We recommend placing the Amazon S3 bucket in the same AWS account and region as your WorkSpaces Secure Browser
portal.

There is no naming requirement for the Amazon S3 bucket. To create a new bucket, follow the
steps below or see [Creating a general purpose
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_. For guidance on configuring
permissions, see [Bucket policies for Amazon S3](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md") in
the _Amazon Simple Storage Service User Guide_.

Below is an example of a policy for your Amazon S3 bucket. Make sure to update the policy with
the name of your Amazon S3 bucket. Note that the Principal is "workspaces-web.amazonaws.com".

```

  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSessionLogger",
            "Effect": "Allow",
            "Principal": {
                "Service": "workspaces-web.amazonaws.com"
            },
            "Action": [
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::`bucket-name`/*"
            ]
        }
    ]
 }

```

Activating Session Logger on your WorkSpaces Secure Browser portal might result in charges from Amazon S3. For
information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

For more information about the session-related events that Session Logger captures, see
[Session events in Session Logger for Amazon WorkSpaces Secure Browser](session-events-session-logger.md "session-events-session-logger.md").

## S3 buckets with KMS encryption (optional)

WorkSpaces Secure Browser Session Logger fully supports Amazon S3 buckets with AWS KMS encryption enabled. To ensure
proper logging functionality with your encrypted Amazon S3 bucket, you must grant Session Logger the
necessary permissions to use your AWS KMS key.

Add the following policy to your AWS KMS key configuration:

```

{
  "Sid": "Session Logger",
  "Effect": "Allow",
  "Principal": {
    "Service": "workspaces-web.amazonaws.com"
  },
  "Action": [
    "kms:Encrypt",
    "kms:GenerateDataKey*"
  ],
  "Resource": "*"
},

```

In the AWS console, select the WorkSpaces Secure Browser portal you will collect events from, and choose the
**Session logger** tab and **Edit**.

Enter the following information to configure Session Logger for the portal:

- **S3 Location (required)**: The name of your Amazon S3 bucket where events
  will be delivered.
- **Key Prefix (optional)**: The folder where events are delivered. If
  the folder does not exist, it will be created. If the field is left blank, Session Logger
  will write events at the root of the Amazon S3 bucket.

Under **Advanced**, you can configure the following fields:

- **Event filter**: This is the list of events monitored by Session
  Logger.
  - **All**: Selecting this option means all current and future events
    will be monitored
  - **Include**: This allows you to manually select specific events to
    monitor. Only the events explicitly selected will be logged. New events introduced in
    future updates will not be monitored, unless they are manually added to the
    selection.

- **File format**
  - **JSON (default)**: This is a file format where each log file is
    presented as an array of events. We recommend this format for most use cases.
  - **JSONLines**: This is a file format that is optimized for
    Amazon Athena.

- **Folder structure**: This determines how the log files are
  stored.
  - **Flat (default)**: All log files are in a single folder.
  - **Nested By date**: The log files are organized into folders by date
    and time. Partitioned for Amazon Athena, and optimized for Amazon Athena queries.

You can test the Session Logger setup and ensure that session logger is functioning
correctly. Once the configuration is complete, the system attempts to write a test file named
`_workspaces_secure_browser.tmp` to the specified Amazon S3 bucket
and folder. This serves as a validation of both logging functionality and permission
setup.

You can also run a test session by starting a Secure Browser session in the portal and
using the browser as you normally would. Session Logger writes log files to your configured
Amazon S3 bucket every 15 minutes during an active session, or when the session
ends.

After ending the session or waiting for the next logging interval, check the
Amazon S3 bucket to confirm that log files for your session have been generated and
stored as expected.
