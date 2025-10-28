# Use `PurgeQueue` with a CLI

The following code examples show how to use `PurgeQueue`.

CLI

**AWS CLI**

**To purge a queue**

This example deletes all messages in the specified queue.

Command:

```
`aws sqs purge-queue --queue-url `https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyNewQueue``

```

Output:

```
None.
```

- For API details, see
  [PurgeQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/purge-queue.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/purge-queue.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes all messages from the specified queue.**

```
Clear-SQSQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue

```

- For API details, see
  [PurgeQueue](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes all messages from the specified queue.**

```
Clear-SQSQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue

```

- For API details, see
  [PurgeQueue](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon SQS with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
