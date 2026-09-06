

# Use `CancelImportTask` with a CLI
<a name="example_ec2_CancelImportTask_section"></a>

The following code examples show how to use `CancelImportTask`.

------
#### [ CLI ]

**AWS CLI**  
**To cancel an import task**  
The following `cancel-import-task` example cancels the specified import image task.  

```
aws ec2 cancel-import-task \
    --import-task-id {{import-ami-1234567890abcdef0}}
```
Output:  

```
{
    "ImportTaskId": "import-ami-1234567890abcdef0",
    "PreviousState": "active",
    "State": "deleting"
}
```
+  For API details, see [CancelImportTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-import-task.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example cancels the specified import task (either snapshot or image import). If required, a reason can be providing using the `-CancelReason` parameter.**  

```
Stop-EC2ImportTask -ImportTaskId import-ami-abcdefgh
```
+  For API details, see [CancelImportTask](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example cancels the specified import task (either snapshot or image import). If required, a reason can be providing using the `-CancelReason` parameter.**  

```
Stop-EC2ImportTask -ImportTaskId import-ami-abcdefgh
```
+  For API details, see [CancelImportTask](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.