# RDS Database Stack | Update Storage

Change the RDS instance storage type, capacity or IOPS through direct API calls. The RDS instance can be standalone or belong to a CloudFormation stack, in the latter case, the change might cause stack drift. To avoid causing stack drift, please use ct-12w49boaiwtzp instead, or ct-361tlo1k7339x if the RDS instance was provisioned via CFN ingestion.

**Full classification:** Management | Advanced stack components | RDS database stack | Update Storage

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-0loed9dzig1ze |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Update RDS storage

Screenshot of this change type in the AMS console:

![Update RDS Storage interface showing ID, execution mode, version, and description fields.](images/guiRdsUpdateStorageCT.png)
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
aws amscm create-rfc --change-type-id "ct-0loed9dzig1ze" --change-type-version "1.0" --title "`Update RDS storage`" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateRDSStorage\",\"Region\":\"`us-east-1`\",\"Parameters\": {\"DBInstanceIdentifier\":[\"`rt123456789`\"], \"AllocatedStorage\": [\"`100`\"],,\"ApplyImmediately\": \"`true`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named UpdateStorageParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-0loed9dzig1ze" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateStorageParams.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
  "DocumentName": "AWSManagedServices-UpdateRDSStorage",
  "Region": "`us-east-1`",
  "Parameters": {
    "DBInstanceIdentifier": [
      "`rt123456789`"
    ],
    "AllocatedStorage": [
      "`100`"
    ],
    "ApplyImmediately": "`false`"
  }
}
```

3. Output the JSON template to a file in your current folder; this example names it UpdateStorageRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > UpdateStorageRfc.json
```

4. Modify and save the UpdateStorageRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-0loed9dzig1ze",
"Title":                "`Update RDS storage`"
}
```

5. Create the RFC, specifying the execution parameters file and the UpdateStorageRfc file:

```
aws amscm create-rfc --cli-input-json file://UpdateStorageRfc.json --execution-parameters file://UpdateStorageParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

AMS employs drift detection on certain stacks, including RDS stacks, to determine if configuration changes. The AMS disallows updates to an RDS stack that has been determined to
have configuration drift. The RFC will fail with the following error message: "Update cannot be performed on this stack, please contact AMS for further assistance."

To learn more about Amazon RDS, including size recommendations, see
[Amazon Relational Database Service Documentation](https://aws.amazon.com/documentation/rds/ "https://aws.amazon.com/documentation/rds/").

To update an RDS stack for Aurora, see
[RDS Database Stack | Update](management-advanced-rds-database-stack-update-for-aurora.md "management-advanced-rds-database-stack-update-for-aurora.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0loed9dzig1ze](schemas.md#ct-0loed9dzig1ze-schema-section "schemas.md#ct-0loed9dzig1ze-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "DocumentName": "AWSManagedServices-UpdateRDSStorage",
  "Region": "us-east-1",
  "Parameters": {
    "DBInstanceIdentifier": [
      "rt123456789"
    ],
    "AllocatedStorage": [
      "1000"
    ],
    "MaxAllocatedStorage": [
      "2000"
    ],
    "StorageType": [
      "gp3"
    ],
    "Iops": [
      "10000"
    ],
    "ApplyImmediately": "true"
  }
}
```
