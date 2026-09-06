

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Recovery Point \| Delete
<a name="management-aws-recovery-point-delete"></a>

Delete one or more recovery points (snapshots) from the specified vault. Use this change type to delete recovery points that were manually created, and recovery points that were created through a backup plan, and that are older than 30 days. The deletion of recovery points cannot be rolled back.

**Full classification:** Management \| AWS Backup \| Recovery point \| Delete

## Change Type Details
<a name="ct-1r1vbr8ahr156-MARd-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-1r1vbr8ahr156 | 
| Current version | 2.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-aws-recovery-point-delete-info"></a>

### Delete AWS Backup recovery points
<a name="ex-backup-recovery-point-delete-col"></a>

#### Deleting recovery points with the console
<a name="backup-recovery-point-delete-con"></a>

The following shows this change type in the AMS console.

![Delete Recovery Points change type showing ID ct-1r1vbr8ahr156 and version 2.0.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiAwsBackupRecoveryPointDeleteCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

#### Deleting recovery points with the CLI
<a name="backup-recovery-point-delete-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1r1vbr8ahr156" --change-type-version "2.0" --title "{{AWS Backup Delete Recovery Points}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-DeleteRecoveryPoints\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"BackupVaultName\":[\"{{ams-manual-backups}}\"],\"RecoveryPointArns\":[\"{{arn:aws:ec2:us-east-1::snapshot/snap-0000000000000000}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it DeleteRecoveryPointsParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1r1vbr8ahr156" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeleteRecoveryPointsParams.json
   ```

1. Modify and save the DeleteRecoveryPointsParams file.

   ```
   {
       "DocumentName": "AWSManagedServices-DeleteRecoveryPoints",
       "Region": "{{us-east-1}}",
       "Parameters": {
           "BackupVaultName": [
               "{{ams-manual-backups}}"
            ],
           "RecoveryPointArns": [
               "arn:aws:backup:us-east-1:000000000000:recovery-point:24f48ec5-79a7-4a40-b992-d97583518f2f",
               "arn:aws:backup:us-east-1:000000000000:recovery-point:3b6a599e-b5a3-4028-87b3-be9a1fdc01e8"
           ]
       }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it DeleteRecoveryPointsRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeleteRecoveryPointsRfc.json
   ```

1. Modify and save the DeleteRecoveryPointsRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
       "ChangeTypeId": "ct-1r1vbr8ahr156",
       "ChangeTypeVersion": "2.0",
       "Title": "{{AWS Backup Delete Recovery Points}}"
   }
   ```

1. Create the RFC, specifying the DeleteRecoveryPointsRfc file and the DeleteRecoveryPointsParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DeleteRecoveryPointsRfc.json --execution-parameters file://DeleteRecoveryPointsParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-backup-recovery-point-delete-tip"></a>

**Note**  
This CT is now at version 2.0. This reflects development to allow you to delete more than one recovery point at a time.

To learn more about AWS Backup, see [AWS Backup: How It Works](https://docs.aws.amazon.com/aws-backup/latest/devguide/how-it-works.html).

## Execution Input Parameters
<a name="management-aws-recovery-point-delete-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-1r1vbr8ahr156](schemas.md#ct-1r1vbr8ahr156-schema-section).

## Example: Required Parameters
<a name="management-aws-recovery-point-delete-ex-min"></a>

```
{
  "DocumentName": "AWSManagedServices-DeleteRecoveryPoints",
  "Region": "us-east-1",
  "Parameters": {
    "BackupVaultName": [ "backup-vault" ],
    "RecoveryPointArns": [ "arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45", "arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D41" ]
  }
}
```

## Example: All Parameters
<a name="management-aws-recovery-point-delete-ex-max"></a>

```
{
  "DocumentName": "AWSManagedServices-DeleteRecoveryPoints",
  "Region": "us-east-1",
  "Parameters": {
    "BackupVaultName": [ "backup-vault" ],
    "RecoveryPointArns": [ "arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45", "arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D41" ]
  }
}
```