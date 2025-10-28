# Amazon SQS cost allocation tags

To organize and identify your Amazon SQS queues for cost allocation, you can add metadata
_tags_ that identify a queue's purpose, owner, or environment. This
is especially useful when you have many queues. To configure tags using the Amazon SQS console,
see [Configuring cost allocation tags for a queue using
the Amazon SQS console](sqs-configure-tag-queue.md "sqs-configure-tag-queue.md")

You can use cost allocation tags to organize your AWS bill to reflect your own cost
structure. To do this, sign up to get your AWS account bill to include tag keys and
values. For more information, see [Setting Up a Monthly
Cost Allocation Report](../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md#allocation-report "../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md#allocation-report") in the _AWS Billing User Guide_.

Each tag consists of a key-value pair that you define. For example, you can easily
identify your _production_ and _testing_ queues if you
tag your queues as follows:

| Queue      | Key         | Value        |
| ---------- | ----------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MyQueueA` | `QueueType` | `Production` |
| `MyQueueB` | `QueueType` | `Testing`    | ###### Note When you use queue tags, keep the following guidelines in mind: <br>• We don't recommend adding more than 50 tags to a queue. Tagging supports Unicode characters in UTF-8. <br>• Tags don't have any semantic meaning. Amazon SQS interprets tags as character strings. <br>• Tags are case-sensitive. <br>• A new tag with a key identical to that of an existing tag overwrites the existing tag. <br>• Tagging actions are limited to 30 TPS per AWS account. If your application requires a higher throughput, [submit a request](https://console.aws.amazon.com/servicequotas/home/services/sqs/quotas "https://console.aws.amazon.com/servicequotas/home/services/sqs/quotas"). For a full list of tag restrictions, see [Amazon SQS standard queue quotas](quotas-queues.md "quotas-queues.md"). |
