# AwsSqs resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsSqs` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsSqsQueue

The `AwsSqsQueue` object contains information about an Amazon Simple Queue Service
queue.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsSqsQueue` object. To view descriptions of `AwsSqsQueue`
attributes, see [AwsSqsQueueDetails](../../1.0/APIReference/API_AwsSqsQueueDetails.md "../../1.0/APIReference/API_AwsSqsQueueDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsSqsQueue": {
    "DeadLetterTargetArn": "arn:aws:sqs:us-west-2:123456789012:queue/target",
    "KmsDataKeyReusePeriodSeconds": 60,,
    "KmsMasterKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "QueueName": "sample-queue"
}
```
