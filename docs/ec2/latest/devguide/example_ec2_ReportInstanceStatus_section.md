

# Use `ReportInstanceStatus` with a CLI
<a name="example_ec2_ReportInstanceStatus_section"></a>

The following code examples show how to use `ReportInstanceStatus`.

------
#### [ CLI ]

**AWS CLI**  
**To report status feedback for an instance**  
The following `report-instance-status` example reports status feedback for the specified instance.  

```
aws ec2 report-instance-status \
    --instances {{i-1234567890abcdef0}} \
    --status {{impaired}} \
    --reason-codes {{unresponsive}}
```
This command produces no output.  
For more information, see [Status checks for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html) in the *Amazon EC2 User Guide*.  
+  For API details, see [ReportInstanceStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/report-instance-status.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example reports status feedback for the specified instance.**  

```
Send-EC2InstanceStatus -Instance i-12345678 -Status impaired -ReasonCode unresponsive
```
+  For API details, see [ReportInstanceStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example reports status feedback for the specified instance.**  

```
Send-EC2InstanceStatus -Instance i-12345678 -Status impaired -ReasonCode unresponsive
```
+  For API details, see [ReportInstanceStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.