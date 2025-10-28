# Cross-account

cross-Region account-level subscriptions using Firehose

To share log data across accounts, you need to establish a log data sender and
receiver:

- **Log data sender**—gets the destination
  information from the recipient and lets CloudWatch Logs know that it is ready to send
  its log events to the specified destination. In the procedures in the rest
  of this section, the log data sender is shown with a fictional AWS account
  number of 111111111111.
- **Log data recipient**—sets up a destination that
  encapsulates a Kinesis Data Streams stream and lets CloudWatch Logs know that the recipient wants to
  receive log data. The recipient then shares the information about this
  destination with the sender. In the procedures in the rest of this section,
  the log data recipient is shown with a fictional AWS account number of

222222222222. The example in this section uses a Firehose delivery stream with Amazon S3 storage. You
              can also set up Firehose delivery streams with different settings. For more
              information, see [Creating a Firehose Delivery
              Stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md").

###### Note

The log group and the destination must be in the same AWS Region. However,
the AWS resource that the destination points to can be located in a different
Region.

###### Note

Firehose subscription filter for a **_same
account_** and
**_cross-Region_** delivery stream
is supported.

###### Topics

- [Step 1: Create a Firehose delivery
  stream](CreateFirehoseStream-Account.md "CreateFirehoseStream-Account.md")
- [Step 2: Create a
  destination](CreateFirehoseStreamDestination-Account.md "CreateFirehoseStreamDestination-Account.md")
- [Step 3: Create an
  account-level subscription filter policy](CreateSubscriptionFilterFirehose-Account.md "CreateSubscriptionFilterFirehose-Account.md")
- [Validating the flow of
  log events](ValidateLogEventFlowFirehose-Account.md "ValidateLogEventFlowFirehose-Account.md")
- [Modifying
  destination membership at runtime](ModifyDestinationMembershipFirehose-Account.md "ModifyDestinationMembershipFirehose-Account.md")
