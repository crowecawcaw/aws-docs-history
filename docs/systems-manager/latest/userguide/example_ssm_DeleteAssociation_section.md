

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DeleteAssociation` with a CLI
<a name="example_ssm_DeleteAssociation_section"></a>

The following code examples show how to use `DeleteAssociation`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To delete an association using the association ID**  
The following `delete-association` example deletes the association for the specified association ID. There is no output if the command succeeds.  

```
aws ssm delete-association \
    --association-id {{"8dfe3659-4309-493a-8755-0123456789ab"}}
```
This command produces no output.  
For more information, see [Editing and creating a new version of an association](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-edit.html) in the *AWS Systems Manager User Guide*.  
**Example 2: To delete an association**  
The following `delete-association` example deletes the association between an instance and a document. There is no output if the command succeeds.  

```
aws ssm delete-association \
    --instance-id {{"i-1234567890abcdef0"}} \
    --name {{"AWS-UpdateSSMAgent"}}
```
This command produces no output.  
For more information, see [Working with associations in Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-associations.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DeleteAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-association.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the association between an instance and a document. There is no output if the command succeeds.**  

```
Remove-SSMAssociation -InstanceId "i-0cb2b964d3e14fd9f" -Name "AWS-UpdateSSMAgent"
```
+  For API details, see [DeleteAssociation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the association between an instance and a document. There is no output if the command succeeds.**  

```
Remove-SSMAssociation -InstanceId "i-0cb2b964d3e14fd9f" -Name "AWS-UpdateSSMAgent"
```
+  For API details, see [DeleteAssociation](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.