# RDS Database Stack | Update (For Aurora)

Modify the properties of an existing AWS Relational Database Service (RDS) Aurora stack created using CT ID ct-2jvzjwunghrhy, version 1.0.

**Full classification:** Management | Advanced stack components | RDS database stack | Update (for Aurora)

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-2dphvdy1krpj6 |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Update DB (for Aurora)

Screenshot of this change type in the AMS console:

![Change type details for updating an RDS Aurora stack, including description and execution mode.](images/guiRdsStackAuroraUpdate2CT.png)
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
aws amscm create-rfc --region us-east-1 --change-type-id "ct-2dphvdy1krpj6" --change-type-version "1.0" --title "`Test - Update Aurora RDS`"  --execution-parameters "{\"VpcId\":\"`VPC_ID`\",\"StackId\":\"`STACK_ID`\",\"Parameters\":{\"AutoMinorVersionUpgrade\":\"`true`\",\"BackupRetentionPeriod\":`5`,\"EngineVersion\":\"`10.4`\",\"InstanceType\":\"`db.r4.large`\",\"MultiAZ\":\"`true`\",\"PerformanceInsights\":\"`true`\",\"PerformanceInsightsKMSKey\":\"`default`\",\"PerformanceInsightsRetentionPeriod\":\"`7`\",\"Port\":\"`1151`\",\"PreferredBackupWindow\":\"`22:00-23:00`\",\"PreferredMaintenanceWindow\":\"`wed:03:32-wed:04:02`\",\"MasterUserPassword\":\"`PW`\"}}"
```

_TEMPLATE CREATE_ (all parameters shown):

1. Output the execution parameters for this change type to a JSON file named UpdateAuroraRdsParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-2dphvdy1krpj6" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateAuroraRdsParams.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
  "VpcId": "`VPC_ID`",
  "StackId": "`STACK_ID`",
  "Parameters": {
    "AutoMinorVersionUpgrade": "`true`",
    "BackupRetentionPeriod": `5`,
    "EngineVersion": "`10.4`",
    "InstanceType": "`db.r4.large`",
    "MultiAZ": "`true`",
    "PerformanceInsights": "`true`",
    "PerformanceInsightsKMSKey": "`default`",
    "PerformanceInsightsRetentionPeriod": "`7`",
    "Port": "`1151`",
    "PreferredBackupWindow": "`22:00-23:00`",
    "PreferredMaintenanceWindow": "`wed:03:32-wed:04:02`",
    "MasterUserPassword": "**********"
  }
}
```

3. Output the JSON template to a file in your current folder; this example names it UpdateAuroraRdsRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > UpdateAuroraRdsRfc.json
```

4. Modify and save the UpdateAuroraRdsRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-2dphvdy1krpj6",
"Title":                "`RDS-Aurora-Update-RFC`"
}
```

5. Create the RFC, specifying the execution parameters file and the UpdateAuroraRdsRfc file:

```
aws amscm create-rfc --cli-input-json file://UpdateAuroraRdsRfc.json --execution-parameters file://UpdateAuroraRdsParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start. 6. To view the RDS, look in the execution output: Use the "stack_id" to view the RDS in the Cloud Formation Console.

###### Note

AMS employs drift detection on certain stacks, including RDS stacks, to determine if configuration changes. The AMS disallows updates to an RDS stack that has been determined to
have configuration drift. The RFC will fail with the following error message: "Update cannot be performed on this stack, please contact AMS for further assistance."

To learn more about Amazon RDS, including size recommendations, see
[Amazon Relational Database Service Documentation](https://aws.amazon.com/documentation/rds/ "https://aws.amazon.com/documentation/rds/").

To update a non-Aurora RDS stack, see
[Update DB stack](management-advanced-rds-database-stack-update.md#ex-rds-update-stack-col "management-advanced-rds-database-stack-update.md#ex-rds-update-stack-col").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-2dphvdy1krpj6](schemas.md#ct-2dphvdy1krpj6-schema-section "schemas.md#ct-2dphvdy1krpj6-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "VpcId": "vpc-12345678901234567",
  "StackId": "stack-a1b2c3d4e5f67890e",
  "Parameters": {
    "AutoMinorVersionUpgrade": "true",
    "BackupRetentionPeriod": 7,
    "InstanceType": "db.serverless",
    "MasterUserPassword": "dbpassword",
    "MultiAZ": "true",
    "PerformanceInsights": "true",
    "PerformanceInsightsKMSKey": "default",
    "PerformanceInsightsRetentionPeriod": "7",
    "Port": "1150",
    "PreferredBackupWindow": "22:00-23:00",
    "PreferredMaintenanceWindow": "wed:03:32-wed:04:02",
    "ServerlessScalingMinCapacity": 1.0,
    "ServerlessScalingMaxCapacity": 2.0
  }
}

```
