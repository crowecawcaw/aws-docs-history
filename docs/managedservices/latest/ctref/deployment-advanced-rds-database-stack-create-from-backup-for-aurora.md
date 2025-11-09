# RDS Database Stack | Create from Backup (For Aurora)

Create an AWS Relational Database Service (RDS) Aurora stack from AWS Backup.

**Full classification:** Deployment | Advanced stack components | RDS database stack | Create from backup (for Aurora)

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-2wllq61djysxz |
| Current version             | 1.0              |
| Expected execution duration | 360 minutes      |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create DB stack from backup (for Aurora)

Screenshot of this change type in the AMS console:

![Details of an AWS RDS Aurora stack creation from backup, showing ID and version.](images/guiRdsStackCreateAuroraFromBackupCT.png)
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
aws --profile saml --region us-east-1 amscm create-rfc --change-type-id "ct-2wllq61djysxz" --change-type-version "1.0" --title "`TestCreateAuroraStackFromBackup`" --execution-parameters "{\"Description\":\"`TestCreateAuroraStackFromBackup`\",\"VpcId\":\"`VPC_ID`\",\"Name\":\"`Test Aurora Stack From Backup`\",\"Parameters\":{\"SnapshotIdentifier\":\"`SNAPSHOT_IDENTIFIER`\",\"AutoMinorVersionUpgrade\":\"`true`\",\"BackupRetentionPeriod\":`7`,\"ClusterName\":\"\",\"DBEngine\":\"`aurora`\",\"DBName\":\"\",\"EngineVersion\":\"\",\"InstanceType\":\"`db.r4.large`\",\"MultiAZ\":\"`true`\",\"Port\":\"`0`\",\"PreferredBackupWindow\":\"`22:00-23:00`\",\"PreferredMaintenanceWindow\":\"\",\"DBSubnetGroupName\":\"`DB_SUBNET_GROUP_NAME`\"},\"StackTemplateId\":\"stm-j24cifrdi0untnsn6\",\"TimeoutInMinutes\":`60`}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named CreateRdsArFrmBkupParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-2wllq61djysxz" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateRdsArFrmBkupParams.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
  "Description": "`TestCreateAuroraStackFromBackup`",
  "VpcId": "`VPC_ID`",
  "Name": "`Test Aurora Stack From Backup`",
  "Parameters": {
    "SnapshotIdentifier": "`SNAPSHOT_IDENTIFIER`",
    "AutoMinorVersionUpgrade": "`true`",
    "BackupRetentionPeriod": `7`,
    "ClusterName": "",
    "DBEngine": "`aurora`",
    "DBName": "",
    "EngineVersion": "",
    "InstanceType": "`db.r4.large`",
    "MultiAZ": "`true`",
    "Port": "`0`",
    "PreferredBackupWindow": "`22:00-23:00`",
    "PreferredMaintenanceWindow": "",
    "DBSubnetGroupName": "`DB_SUBNET_GROUP_NAME`"
  },
  "StackTemplateId": "stm-j24cifrdi0untnsn6",
  "TimeoutInMinutes": 60
}
```

3. Output the JSON template to a file in your current folder; this example names it CreateRdsArFrmBkupRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateRdsArFrmBkupRfc.json
```

4. Modify and save the CreateRdsArFrmBkupRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-2wllq61djysxz",
"Title":                "`RDS-Create-Aurora-From-Backup-RFC`"
}
```

5. Create the RFC, specifying the execution parameters file and the CreateRdsArFrmBkupRfc file:

```
aws amscm create-rfc --cli-input-json file://CreateRdsArFrmBkupRfc.json --execution-parameters file://CreateRdsArFrmBkupParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start. 6. To view the RDS, look in the execution output: Use the "stack_id" to view the RDS in the Cloud Formation Console.
To create a Delete Stack or Update RDS RFC, use the first part of the DatabaseEndpoint (the DB instance ID);
to create a Reboot RDS RFC, use the entire DatabaseEndpoint -> ClusterEndpoint to programmatically access the RDS DB. 7. You are now able to manage the database via a database management tool such as SQL server management studio. You do not have to request access from AMS.

###### Note

You can add up to 50 tags, but to do so you must enable the **Additional configuration** view.

For more information, see [Amazon Aurora – Relational Database Built for the Cloud - AWS](https://aws.amazon.com/rds/aurora/ "https://aws.amazon.com/rds/aurora/").

To learn more about Amazon RDS, including size recommendations, see [Amazon Relational Database Service Documentation](https://aws.amazon.com/documentation/rds/ "https://aws.amazon.com/documentation/rds/").

To create an Aurora RDS stack (not using backup), see
[Create DB stack (for Aurora)](deployment-advanced-rds-database-stack-create-for-aurora.md#ex-rds-create-aurora-stack-col "deployment-advanced-rds-database-stack-create-for-aurora.md#ex-rds-create-aurora-stack-col").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-2wllq61djysxz](schemas.md#ct-2wllq61djysxz-schema-section "schemas.md#ct-2wllq61djysxz-schema-section").

## Example: Required Parameters

```
{
  "Description": "Create an AWS Relational Database Service (RDS) Aurora stack from AWS Backup.",
  "VpcId": "vpc-12345678901234567",
  "StackTemplateId": "stm-j24cifrdi0untnsn6",
  "Name": "Stack Name",
  "Tags": [
    {
      "Key": "foo",
      "Value": "bar"
    },
    {
      "Key": "testkey",
      "Value": "testvalue"
    }
  ],
  "TimeoutInMinutes": 60,
  "Parameters": {
    "SnapshotIdentifier": "arn:aws:rds:xx-xxxx-x:000000000000:cluster-snapshot:awsbackup:job-00000000-0000-0000-0000-000000000000",
    "DBEngine": "aurora",
    "EngineVersion": "",
    "DBSubnetGroupName": "db-subnet-group"
  }
}

```

## Example: All Parameters

```
{
  "Description": "Create an AWS Relational Database Service (RDS) Aurora stack from AWS Backup.",
  "VpcId": "vpc-12345678901234567",
  "StackTemplateId": "stm-j24cifrdi0untnsn6",
  "Name": "Stack Name",
  "Tags": [
    {
      "Key": "foo",
      "Value": "bar"
    },
    {
      "Key": "testkey",
      "Value": "testvalue"
    }
  ],
  "TimeoutInMinutes": 60,
  "Parameters": {
    "SnapshotIdentifier": "arn:aws:rds:xx-xxxx-x:000000000000:cluster-snapshot:awsbackup:job-00000000-0000-0000-0000-000000000000",
    "AutoMinorVersionUpgrade": "true",
    "BackupRetentionPeriod": 7,
    "ClusterName": "dbcluster",
    "DBEngine": "aurora-postgresql",
    "EngineVersion": "10.4",
    "DBName": "dbname",
    "DBSubnetGroupName": "db-subnet-group",
    "InstanceType": "db.r4.large",
    "MultiAZ": "true",
    "Port": "1150",
    "PreferredBackupWindow": "22:00-23:00",
    "PreferredMaintenanceWindow": "wed:03:32-wed:04:02"
  }
}


```
