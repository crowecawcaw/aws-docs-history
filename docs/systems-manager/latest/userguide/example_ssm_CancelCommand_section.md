

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `CancelCommand` with a CLI
<a name="example_ssm_CancelCommand_section"></a>

The following code examples show how to use `CancelCommand`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To cancel a command for all instances**  
The following `cancel-command` example attempts to cancel the specified command that is already running for all instances.  

```
aws ssm cancel-command \
    --command-id {{"662add3d-5831-4a10-b64a-f2ff3EXAMPLE"}}
```
This command produces no output.  
**Example 2: To cancel a command for specific instances**  
The following `cancel-command` example attempts to cancel a command for the specified instance only.  

```
aws ssm cancel-command \
    --command-id {{"662add3d-5831-4a10-b64a-f2ff3EXAMPLE"}}
    --instance-ids {{"i-02573cafcfEXAMPLE"}}
```
This command produces no output.  
For more information, see [Tagging Systems Manager Parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-tag.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [CancelCommand](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/cancel-command.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example attempts to cancel a command. There is no output if the operation succeeds.**  

```
Stop-SSMCommand -CommandId "9ded293e-e792-4440-8e3e-7b8ec5feaa38"
```
+  For API details, see [CancelCommand](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example attempts to cancel a command. There is no output if the operation succeeds.**  

```
Stop-SSMCommand -CommandId "9ded293e-e792-4440-8e3e-7b8ec5feaa38"
```
+  For API details, see [CancelCommand](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.