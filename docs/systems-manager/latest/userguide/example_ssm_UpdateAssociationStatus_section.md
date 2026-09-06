

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `UpdateAssociationStatus` with a CLI
<a name="example_ssm_UpdateAssociationStatus_section"></a>

The following code examples show how to use `UpdateAssociationStatus`.

------
#### [ CLI ]

**AWS CLI**  
**To update the association status**  
The following `update-association-status` example updates the association status of the association between an instance and a document.  

```
aws ssm update-association-status \
    --name {{"AWS-UpdateSSMAgent"}} \
    --instance-id {{"i-1234567890abcdef0"}} \
    --association-status {{"Date=1424421071.939,Name=Pending,Message=temp_status_change,AdditionalInfo=Additional-Config-Needed"}}
```
Output:  

```
{
    "AssociationDescription": {
        "Name": "AWS-UpdateSSMAgent",
        "InstanceId": "i-1234567890abcdef0",
        "AssociationVersion": "1",
        "Date": 1550507529.604,
        "LastUpdateAssociationDate": 1550507806.974,
        "Status": {
            "Date": 1424421071.0,
            "Name": "Pending",
            "Message": "temp_status_change",
            "AdditionalInfo": "Additional-Config-Needed"
        },
        "Overview": {
            "Status": "Success",
            "AssociationStatusAggregatedCount": {
                "Success": 1
            }
        },
        "DocumentVersion": "$DEFAULT",
        "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab",
        "Targets": [
            {
                "Key": "InstanceIds",
                "Values": [
                    "i-1234567890abcdef0"
                ]
            }
        ],
        "LastExecutionDate": 1550507808.0,
        "LastSuccessfulExecutionDate": 1550507808.0
    }
}
```
For more information, see [Working with associations in Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-associations.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [UpdateAssociationStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-association-status.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example updates the association status of the association between an instance and a configuration document.**  

```
Update-SSMAssociationStatus -Name "AWS-UpdateSSMAgent" -InstanceId "i-0000293ffd8c57862" -AssociationStatus_Date "2015-02-20T08:31:11Z" -AssociationStatus_Name "Pending" -AssociationStatus_Message "temporary_status_change" -AssociationStatus_AdditionalInfo "Additional-Config-Needed"
```
**Output:**  

```
Name                  : AWS-UpdateSSMAgent
InstanceId            : i-0000293ffd8c57862
Date                  : 2/23/2017 6:55:22 PM
Status.Name           : Pending
Status.Date           : 2/20/2015 8:31:11 AM
Status.Message        : temporary_status_change
Status.AdditionalInfo : Additional-Config-Needed
```
+  For API details, see [UpdateAssociationStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example updates the association status of the association between an instance and a configuration document.**  

```
Update-SSMAssociationStatus -Name "AWS-UpdateSSMAgent" -InstanceId "i-0000293ffd8c57862" -AssociationStatus_Date "2015-02-20T08:31:11Z" -AssociationStatus_Name "Pending" -AssociationStatus_Message "temporary_status_change" -AssociationStatus_AdditionalInfo "Additional-Config-Needed"
```
**Output:**  

```
Name                  : AWS-UpdateSSMAgent
InstanceId            : i-0000293ffd8c57862
Date                  : 2/23/2017 6:55:22 PM
Status.Name           : Pending
Status.Date           : 2/20/2015 8:31:11 AM
Status.Message        : temporary_status_change
Status.AdditionalInfo : Additional-Config-Needed
```
+  For API details, see [UpdateAssociationStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.