# Logging and troubleshooting

## Setting up log delivery

Amazon Q can provide you with log files that will help you understand and
troubleshoot issues with your customization.

You can have your log files sent to a [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").
group, an [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") bucket, an [Amazon Data Firehose](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md"), or any
combination.

To set up log delivery, select the Log deliveries tab on the console page for your
customization. Follow the instructions in the interface to configure your log
deliveries. Then choose **Create log deliveries**.

The prefix of logs delivered to an Amazon S3 bucket will be:
`AWSLogs/`account_id`/codeWhispererCustomizationLogs/`region`/`customization_id`/`year`/`month`/`day`/`hour`/`

The files will be zipped, with the naming format:
``account_id`_codeWhispererCustomizationLogs_`customization_id`_`date`_`file_id`.log.gz`

###### Warning

In order to get the most use out of customization logs, it's best to set up log
delivery within five minutes of creating the customization.

To learn more about the permissions required to delivery logs to multiple resources,
see [Logging that requires additional permissions [V2]](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2") in the
_Amazon CloudWatch Logs User Guide_.

## Understanding

customization-related log messages

The following table lists log messages that may help you understand issues with your
customization.

| Log message                                                                                                                                                                         | Log level                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Starting to ingest `number`repos from source`source``                                                                                                                              | Info                                                                                                         |
| `Downloading data from repo: `repo name``                                                                                                                                           | Info                                                                                                         |
| `Received `amount`MB of supported data.`amount` MB required. Add more data and retry.`                                                                                              | Error                                                                                                        |
| `The provided CodeStar Connection ARN: `Arn` is invalid.`                                                                                                                           | Error                                                                                                        |
| `Access denied when attempting to reach the provided CodeStar Connection:` `Arn`                                                                                                    | Error                                                                                                        |
| `Failed to download with AWS CodeStar Connection: `Arn` probably deleted by customer`                                                                                               | Error                                                                                                        |
| `ProviderThrottlingException from CodeStar Connection: `Arn`while cloning repository:`repository``                                                                                  | Error                                                                                                        |
| `Processing data from S3: `S3 URI``                                                                                                                                                 | Info                                                                                                         |
| `Invalid S3 path specified: `S3 Directory``                                                                                                                                         | Error                                                                                                        |
| `Unable to access the provided S3 bucket: `bucket name``                                                                                                                            | Error                                                                                                        |
| `The provided S3 bucket: `bucket name` does not exist.`                                                                                                                             | Error                                                                                                        |
| `The provided S3 key `S3 URI` does not exist.`                                                                                                                                      | Error                                                                                                        |
| `Failed to ingest `number of failed repos / total number of repos` repositories`                                                                                                    | Error                                                                                                        |
| `Unable to process repository: `repo name`, with a size of `repo size`GB, exceeds the limit of`max size` GB.`                                                                       | Warn                                                                                                         |
| `Unable to process file: `file name`, with a size of `file size`, which exceeds the limit of `max file size` MB`                                                                    | Error                                                                                                        |
| `Unable to process collection: `collection name`, with total size of `total repo size`MB, which exceeds the limit of`max total repo size` MB`                                       | Error                                                                                                        |
| `The following languages will be used for customization: `list of languages`. Languages may be excluded from customization if they are not sufficiently represented in your files.` | Info                                                                                                         | ## Understanding customization-related error messages in the console The following table will help you understand customization-related messages in the Amazon Q console. |
| Error message                                                                                                                                                                       | Suggested action                                                                                             |
| ---                                                                                                                                                                                 | ---                                                                                                          |
| You have activated the maximum number of customizations.                                                                                                                            | Deactivate an active customization and try again.                                                            |
| You have exceeded the maximum number of group permissions limit of `limit`.                                                                                                         | Remove a group and retry.                                                                                    |
| You have exceeded the maximum number of user permissions limit of `limit`.                                                                                                          | Remove a user and retry.                                                                                     |
| Maximum active jobs reached.                                                                                                                                                        | Wait until an in-progress job in the same account has finished. Retry the operation.                         |
| Encountered an unexpected error when processing the request.                                                                                                                        | Retry the operation. If it continues to fail, contact customer support.                                      |
| Encountered an issue when retrieving some of the selected repositories from CodeConnections. Check the customization's log deliveries for details.                                  | Try creating or updating the customization again with valid repositories that your connection has access to. |
| Access denied when attempting to reach the provided AWS CodeConnections connection.                                                                                                 | Validate permissions on your connection and on your third-party provider. Then retry the operation.          |
| One or more repositories not found while accessing the provided AWS CodeConnections connection.                                                                                     | Validate permissions and list of repos from the third-party provider. Then retry the operation.              |
| The provided AWS CodeConnections connection ARN is invalid.                                                                                                                         | Update the customization with a corrected Connection ARN.                                                    |
| The Host associated with the provided AWS CodeConnections connection is unavailable.                                                                                                | Try again in 5 minutes.                                                                                      |
| Invalid Amazon S3 path specified.                                                                                                                                                   | Update the customization with a valid Amazon S3 URI.                                                         |
| Unable to access the provided Amazon S3 bucket.                                                                                                                                     | Validate permissions for the admin's role. Retry after fixing any permission issues.                         |
| The provided Amazon S3 bucket does not exist.                                                                                                                                       | Update the customization with a valid Amazon S3 URI.                                                         |
| The provided Amazon S3 key does not exist.                                                                                                                                          | Update the customization with a valid Amazon S3 URI.                                                         |
| Insufficient data to create a customization. Add more files from supported languages and retry.                                                                                     | Add more data to the same data source, and update the customization with the same reference.                 |
| Total size of the provided repositories exceeds the maximum allowed size of `size` for a customization.                                                                             | Remove some data from the provided data source. Update the customization with the same reference.            |
| You have created the maximum number of customizations. Delete an existing customization and try again.                                                                              | Delete the current customization and retry.                                                                  |
| Customizations exist within the account. You must delete all customizations prior to deleting the profile.                                                                          | Delete all customizations associated with the account and retry.                                             |
