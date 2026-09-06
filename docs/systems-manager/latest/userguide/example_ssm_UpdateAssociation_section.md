

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `UpdateAssociation` with a CLI
<a name="example_ssm_UpdateAssociation_section"></a>

The following code examples show how to use `UpdateAssociation`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To update a document association**  
The following `update-association` example updates an association with a new document version.  

```
aws ssm update-association \
    --association-id {{"8dfe3659-4309-493a-8755-0123456789ab"}} \
    --document-version {{"\$LATEST"}}
```
Output:  

```
{
    "AssociationDescription": {
        "Name": "AWS-UpdateSSMAgent",
        "AssociationVersion": "2",
        "Date": 1550508093.293,
        "LastUpdateAssociationDate": 1550508106.596,
        "Overview": {
            "Status": "Pending",
            "DetailedStatus": "Creating"
        },
        "DocumentVersion": "$LATEST",
        "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab",
        "Targets": [
            {
                "Key": "tag:Name",
                "Values": [
                    "Linux"
                ]
            }
        ],
        "LastExecutionDate": 1550508094.879,
        "LastSuccessfulExecutionDate": 1550508094.879
    }
}
```
For more information, see [Editing and creating a new version of an association](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-edit.html) in the *AWS Systems Manager User Guide*.  
**Example 2: To update the schedule expression of an association**  
The following `update-association` example updates the schedule expression for the specified association.  

```
aws ssm update-association \
    --association-id {{"8dfe3659-4309-493a-8755-0123456789ab"}} \
    --schedule-expression {{"cron(0 0 0/4 1/1 * ? *)"}}
```
Output:  

```
{
    "AssociationDescription": {
        "Name": "AWS-HelloWorld",
        "AssociationVersion": "2",
        "Date": "2021-02-08T13:54:19.203000-08:00",
        "LastUpdateAssociationDate": "2021-06-29T11:51:07.933000-07:00",
        "Overview": {
            "Status": "Pending",
            "DetailedStatus": "Creating"
        },
        "DocumentVersion": "$DEFAULT",
        "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab",
        "Targets": [
            {
                "Key": "aws:NoOpAutomationTag",
                "Values": [
                    "AWS-NoOpAutomationTarget-Value"
                ]
            }
        ],
        "ScheduleExpression": "cron(0 0 0/4 1/1 * ? *)",
        "LastExecutionDate": "2021-06-26T19:00:48.110000-07:00",
        "ApplyOnlyAtCronInterval": false
    }
}
```
For more information, see [Editing and creating a new version of an association](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-edit.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [UpdateAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-association.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example updates an association with a new document version.**  

```
Update-SSMAssociation -AssociationId "93285663-92df-44cb-9f26-2292d4ecc439" -DocumentVersion "1"
```
**Output:**  

```
Name                  : AWS-UpdateSSMAgent
InstanceId            :
Date                  : 3/1/2017 6:22:21 PM
Status.Name           :
Status.Date           :
Status.Message        :
Status.AdditionalInfo :
```
+  For API details, see [UpdateAssociation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example updates an association with a new document version.**  

```
Update-SSMAssociation -AssociationId "93285663-92df-44cb-9f26-2292d4ecc439" -DocumentVersion "1"
```
**Output:**  

```
Name                  : AWS-UpdateSSMAgent
InstanceId            :
Date                  : 3/1/2017 6:22:21 PM
Status.Name           :
Status.Date           :
Status.Message        :
Status.AdditionalInfo :
```
+  For API details, see [UpdateAssociation](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.