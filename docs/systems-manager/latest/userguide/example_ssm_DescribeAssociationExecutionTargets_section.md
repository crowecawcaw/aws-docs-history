

# Use `DescribeAssociationExecutionTargets` with a CLI
<a name="example_ssm_DescribeAssociationExecutionTargets_section"></a>

The following code examples show how to use `DescribeAssociationExecutionTargets`.

------
#### [ CLI ]

**AWS CLI**  
**To get details of an association execution**  
The following `describe-association-execution-targets` example describes the specified association execution.  

```
aws ssm describe-association-execution-targets \
    --association-id {{"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}} \
    --execution-id {{"a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"}}
```
Output:  

```
{
    "AssociationExecutionTargets": [
        {
            "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "AssociationVersion": "1",
            "ExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "ResourceId": "i-1234567890abcdef0",
            "ResourceType": "ManagedInstance",
            "Status": "Success",
            "DetailedStatus": "Success",
            "LastExecutionDate": 1550505538.497,
            "OutputSource": {
                "OutputSourceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
                "OutputSourceType": "RunCommand"
            }
        }
    ]
}
```
For more information, see [Viewing association histories](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-history.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DescribeAssociationExecutionTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-association-execution-targets.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example displays the resource ID and its execution status that are part of the the association execution targets**  

```
Get-SSMAssociationExecutionTarget -AssociationId 123a45a0-c678-9012-3456-78901234db5e -ExecutionId 123a45a0-c678-9012-3456-78901234db5e | Select-Object ResourceId, Status
```
**Output:**  

```
ResourceId           Status
----------           ------
i-0b1b2a3456f7a890b  Success
i-01c12a45d6fc7a89f  Success
i-0a1caf234f56d7dc8  Success
i-012a3fd45af6dbcfe  Failed
i-0ddc1df23c4a5fb67  Success
```
**Example 2: This command checks the particular execution of a particular automation since yesterday, where a command document is associated. It further checkes if the association execution failed, and if so, it will display the command invocation details for the execution along with the instance id**  

```
$AssociationExecution= Get-SSMAssociationExecutionTarget -AssociationId 1c234567-890f-1aca-a234-5a678d901cb0 -ExecutionId 12345ca12-3456-2345-2b45-23456789012 | 
    Where-Object {$_.LastExecutionDate -gt (Get-Date -Hour 00 -Minute 00).AddDays(-1)} 

foreach ($execution in $AssociationExecution) {
    if($execution.Status -ne 'Success'){
        Write-Output "There was an issue executing the association $($execution.AssociationId) on $($execution.ResourceId)"
        Get-SSMCommandInvocation -CommandId $execution.OutputSource.OutputSourceId -Detail:$true | Select-Object -ExpandProperty CommandPlugins
    }
}
```
**Output:**  

```
There was an issue executing the association 1c234567-890f-1aca-a234-5a678d901cb0 on i-0a1caf234f56d7dc8


Name                   : aws:runPowerShellScript
Output                 : 
                         ----------ERROR-------
                         failed to run commands: exit status 1
OutputS3BucketName     : 
OutputS3KeyPrefix      : 
OutputS3Region         : eu-west-1
ResponseCode           : 1
ResponseFinishDateTime : 5/29/2019 11:04:49 AM
ResponseStartDateTime  : 5/29/2019 11:04:49 AM
StandardErrorUrl       : 
StandardOutputUrl      : 
Status                 : Failed
StatusDetails          : Failed
```
+  For API details, see [DescribeAssociationExecutionTargets](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example displays the resource ID and its execution status that are part of the the association execution targets**  

```
Get-SSMAssociationExecutionTarget -AssociationId 123a45a0-c678-9012-3456-78901234db5e -ExecutionId 123a45a0-c678-9012-3456-78901234db5e | Select-Object ResourceId, Status
```
**Output:**  

```
ResourceId           Status
----------           ------
i-0b1b2a3456f7a890b  Success
i-01c12a45d6fc7a89f  Success
i-0a1caf234f56d7dc8  Success
i-012a3fd45af6dbcfe  Failed
i-0ddc1df23c4a5fb67  Success
```
**Example 2: This command checks the particular execution of a particular automation since yesterday, where a command document is associated. It further checkes if the association execution failed, and if so, it will display the command invocation details for the execution along with the instance id**  

```
$AssociationExecution= Get-SSMAssociationExecutionTarget -AssociationId 1c234567-890f-1aca-a234-5a678d901cb0 -ExecutionId 12345ca12-3456-2345-2b45-23456789012 | 
    Where-Object {$_.LastExecutionDate -gt (Get-Date -Hour 00 -Minute 00).AddDays(-1)} 

foreach ($execution in $AssociationExecution) {
    if($execution.Status -ne 'Success'){
        Write-Output "There was an issue executing the association $($execution.AssociationId) on $($execution.ResourceId)"
        Get-SSMCommandInvocation -CommandId $execution.OutputSource.OutputSourceId -Detail:$true | Select-Object -ExpandProperty CommandPlugins
    }
}
```
**Output:**  

```
There was an issue executing the association 1c234567-890f-1aca-a234-5a678d901cb0 on i-0a1caf234f56d7dc8


Name                   : aws:runPowerShellScript
Output                 : 
                         ----------ERROR-------
                         failed to run commands: exit status 1
OutputS3BucketName     : 
OutputS3KeyPrefix      : 
OutputS3Region         : eu-west-1
ResponseCode           : 1
ResponseFinishDateTime : 5/29/2019 11:04:49 AM
ResponseStartDateTime  : 5/29/2019 11:04:49 AM
StandardErrorUrl       : 
StandardOutputUrl      : 
Status                 : Failed
StatusDetails          : Failed
```
+  For API details, see [DescribeAssociationExecutionTargets](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.