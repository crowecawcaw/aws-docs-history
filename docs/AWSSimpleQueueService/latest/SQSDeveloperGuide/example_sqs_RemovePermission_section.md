# Use `RemovePermission` with a CLI

The following code examples show how to use `RemovePermission`.

CLI

**AWS CLI**

**To remove a permission**

This example removes the permission with the specified label from the specified queue.

Command:

```
`aws sqs remove-permission --queue-url `https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue` --label `SendMessagesFromMyQueue``

```

Output:

```
None.
```

- For API details, see
  [RemovePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/remove-permission.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/remove-permission.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example removes the permission settings with the specified label from the specified queue.**

```
Remove-SQSPermission -Label SendMessagesFromMyQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue

```

- For API details, see
  [RemovePermission](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example removes the permission settings with the specified label from the specified queue.**

```
Remove-SQSPermission -Label SendMessagesFromMyQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue

```

- For API details, see
  [RemovePermission](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon SQS with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
