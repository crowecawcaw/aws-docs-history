

# Use `RemovePermission` with a CLI
<a name="example_sqs_RemovePermission_section"></a>

The following code examples show how to use `RemovePermission`.

------
#### [ CLI ]

**AWS CLI**  
**To remove a permission**  
This example removes the permission with the specified label from the specified queue.  
Command:  

```
aws sqs remove-permission --queue-url {{https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue}} --label {{SendMessagesFromMyQueue}}
```
Output:  

```
None.
```
+  For API details, see [RemovePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/remove-permission.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example removes the permission settings with the specified label from the specified queue.**  

```
Remove-SQSPermission -Label SendMessagesFromMyQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [RemovePermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example removes the permission settings with the specified label from the specified queue.**  

```
Remove-SQSPermission -Label SendMessagesFromMyQueue -QueueUrl https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue
```
+  For API details, see [RemovePermission](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon SQS with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.