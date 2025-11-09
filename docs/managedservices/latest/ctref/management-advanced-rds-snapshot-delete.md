# RDS Snapshot | Delete

Delete DB instance or cluster snapshots. This document only supports deletion of 'manual' and 'awsbackup' snapshot types. If the snapshot is being copied, the copy operation is terminated. The snapshot must be in available state to be deleted. If one or more snapshots cannot be deleted, automation fails. Up to 20 snapshots can be deleted in one execution.

**Full classification:** Management | Advanced stack components | RDS snapshot | Delete

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-0idxb0xsg1ui6 |
| Current version             | 2.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Delete RDS snapshots

Screenshot of this change type in the AMS console:

![Delete RDS Snapshots change type details including ID, execution mode, and description.](images/guiRdsDbSnapshotDeleteCT.png)
How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.
2. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the
   **Choose by category** view.
   - **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the
     **Run RFC** page. Note that you cannot choose an older CT version with quick create.

   To sort CTs, use the **All change types** area in either the **Card** or **Table** view.
   In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable,
   a **Create with older version** option appears next to the **Create RFC** button.
   - **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to
     **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

3. On the **Run RFC** page, open the CT name area to see the CT details box.
   A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the
   **Additional configuration** area to add information about the RFC.

In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure
optional execution parameters, open the **Additional configuration** area. 4. When finished, click **Run**. If there are no errors, the **RFC successfully created**
page displays with the submitted RFC details, and the initial **Run output**. 5. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status.
Optionally, cancel the RFC or create a copy of it with the options at the top of the page.
How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or
   Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc`
   command with the two files as input. Both methods are described here.
2. Submit the RFC: `aws amscm submit-rfc --rfc-id `ID`` command with the returned RFC ID.

Monitor the RFC: `aws amscm get-rfc --rfc-id `ID`` command.
To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value=`CT_ID`
```

###### Note

You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the
change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the
RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the
[AMS Change Management API Reference](../ApiReference-cm/API_CreateRfc.md "../ApiReference-cm/API_CreateRfc.md").

_INLINE CREATE_:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0idxb0xsg1ui6" --change-type-version "2.0" --title "Delete RDS Snapshots" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-DeleteRDSSnapshots\",\"Region\": \"`us-east-1`\",\"Parameters\": {\"SnapshotNamesOrArns\": [\"`snapshot1`\", \"`snapshot2`\"]}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named DeleteRdsDbSnapshotParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-0idxb0xsg1ui6" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeleteRDSSnapshotsGroupParameters.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
  "DocumentName": "AWSManagedServices-DeleteRDSSnapshots",
  "Region": "`us-east-1`",
  "SnapshotNamesOrArns": ["`snapshot1`","`snapshot2`"]
}
```

3. Output the JSON template to a file in your current folder; this example names it DeleteRdsDbSnapshotRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > DeleteRDSSnapshots.json
```

4. Modify and save the DeleteRdsDbSnapshotRfc.json file. For example, you can replace the contents with something like this:

```
{
  "ChangeTypeVersion": "2.0",
  "ChangeTypeId": "ct-0idxb0xsg1ui6",
  "Title": "`Delete RDS Snapshots`"
}
```

5. Create the RFC, specifying the DeleteRDSSnapshots.json file and the execution parameters file,
   DeleteRDSSnapshotsGroupParameters.json:

```
aws amscm create-rfc --cli-input-json file://DeleteRDSSnapshots.json --execution-parameters file://DeleteRDSSnapshotsGroupParameters.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
For more information about RDS snapshots, see
[Backing up and restoring an Amazon RDS DB instance](../../../AmazonRDS/latest/UserGuide/CHAP_CommonTasks.md "../../../AmazonRDS/latest/UserGuide/CHAP_CommonTasks.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0idxb0xsg1ui6](schemas.md#ct-0idxb0xsg1ui6-schema-section "schemas.md#ct-0idxb0xsg1ui6-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "DocumentName": "AWSManagedServices-DeleteRDSSnapshotsV2",
  "Region": "us-east-1",
  "Parameters": {
    "SnapshotNamesOrArns": [
      "dbsnapshot",
      "arn:aws:rds:us-east-1:945533541580:snapshot:db2-snapshot",
      "arn:aws:rds:us-east-1:945533541580:cluster-snapshot:db2-snapshot"
    ]
  }
}
```
