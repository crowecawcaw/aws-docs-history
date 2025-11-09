# S3 Storage | Update Versioning

Change S3 bucket versioning setting through direct API calls. The S3 bucket can be standalone or belong to a CloudFormation stack; in the latter case, the change might cause stack drift. To avoid causing stack drift, please use ct-1gi93jhvj28eg instead, or ct-361tlo1k7339x if the S3 bucket was provisioned via CFN ingestion.

**Full classification:** Management | Advanced stack components | S3 storage | Update versioning

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-2hh93eyzmwbkd |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Update S3 bucket versioning

Screenshot of this change type in the AMS console:

![S3 bucket versioning change type with ID, execution mode, version, and description details.](images/guiS3UpdateVersioningCT.png)
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
aws amscm create-rfc --change-type-id "ct-2hh93eyzmwbkd" --change-type-version "1.0" --title "`Update bucket versioning`" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateBucketVersioning\",\"Region\":\"`us-east-1`\",\"Parameters\":{\"BucketName\":[\"`BucketName`\"],\"Versioning\": \"`Enabled`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named UpdateBucketVersioningParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-2hh93eyzmwbkd" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateBucketVersioningParams.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
  "DocumentName": "AWSManagedServices-UpdateBucketVersioning",
  "Region": "`us-east-1`",
  "Parameters": {
    "BucketName": [
      "`BucketName`"
    ],
    "Versioning": "`Enabled`"
  }
}
```

3. Output the JSON template to a file in your current folder; this example names it UpdateBucketVersioningRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > UpdateBucketVersioningRfc.json
```

4. Modify and save the UpdateBucketVersioningRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-2hh93eyzmwbkd",
"Title":                "`Update bucket versioning`"
}
```

5. Create the RFC, specifying the execution parameters file and the UpdateRdsRfc file:

```
aws amscm create-rfc --cli-input-json file://UpdateBucketVersioningRfc.json --execution-parameters file://UpdateBucketVersioningParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
To learn more about Amazon S3, see [Amazon Simple Storage Service Documentation](https://aws.amazon.com/documentation/s3/ "https://aws.amazon.com/documentation/s3/").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-2hh93eyzmwbkd](schemas.md#ct-2hh93eyzmwbkd-schema-section "schemas.md#ct-2hh93eyzmwbkd-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "DocumentName": "AWSManagedServices-UpdateBucketVersioning",
  "Region": "us-east-1",
  "Parameters": {
    "BucketName": [
      "rt123456789"
    ],
    "Versioning": "Enabled"
  }
}
```
