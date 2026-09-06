

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DeregisterManagedInstance` with a CLI
<a name="example_ssm_DeregisterManagedInstance_section"></a>

The following code examples show how to use `DeregisterManagedInstance`.

------
#### [ CLI ]

**AWS CLI**  
**To deregister a managed instance**  
The following `deregister-managed-instance` example deregisters the specified managed instance.  

```
aws ssm deregister-managed-instance \
    --instance-id '{{mi-08ab247cdfEXAMPLE}}'
```
This command produces no output.  
For more information, see [Deregistering managed nodes in a hybrid and multicloud environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-deregister-hybrid-nodes.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DeregisterManagedInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-managed-instance.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deregisters a managed instance. There is no output if the command succeeds.**  

```
Unregister-SSMManagedInstance -InstanceId "mi-08ab247cdf1046573"
```
+  For API details, see [DeregisterManagedInstance](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deregisters a managed instance. There is no output if the command succeeds.**  

```
Unregister-SSMManagedInstance -InstanceId "mi-08ab247cdf1046573"
```
+  For API details, see [DeregisterManagedInstance](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.