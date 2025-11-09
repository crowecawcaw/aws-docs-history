# Tag | Bulk Update (Managed Automation)

Bulk add tags to existing, supported resources except those in AMS infrastructure stacks (stacks named mc-\*). Tags simplify categorization, identification and targeting AWS resources. Use this with AWS Tag Editor when managing large numbers of tags (i.e. >50). For Autoscaling, EC2, Elastic Load Balancing, RDS resources and S3 buckets, use automated CT ct-3047c34zuvswh.

**Full classification:** Management | Advanced stack components | Tag | Bulk update (managed automation)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-0k4b96aatyqgl          |
| Current version             | 1.0                       |
| Expected execution duration | 240 minutes               |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

### Bulk update tags (Managed Automation)

Screenshot of this change type in the AMS console:

![](images/guiTagBulkUpdateRrCT.png)
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
aws amscm create-rfc --title `bulk-update-tags` --change-type-id ct-0k4b96aatyqgl --change-type-version 1.0 --execution-parameters '{"Description":"`test-tag-bulk-update`","CsvS3Url":"`PRE-SIGNED_S3_URL`"}'
```

_TEMPLATE CREATE_:

1. Output the RFC template to a file in your current folder. This example names it TagBulkUpdateRfc.json. Note
   that since there is only one execution parameter for starting a stack, the execution parameter can be in the schema JSON file itself and
   there is no need to create a separate execution parameters JSON file.

```
aws amscm create-rfc --generate-cli-skeleton > TagBulkUpdateRfc.json
```

2. Modify and save the TagBulkUpdateRfc.json file. For example, you can replace the contents with something like this:

```
{
  "ChangeTypeVersion": "1.0",
  "ChangeTypeId": "ct-0k4b96aatyqgl",
  "Title": "Bulk-Update_Tags",
  "ExecutionParameters": "{\"Description\":\"`Bulk tag resources`\",\"CsvS3Url\":\"`PRESIGNED_S3_URL`\"}"
}}
```

3. Create the RFC:

```
aws amscm create-rfc --cli-input-json file://TagBulkUpdateRfc.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

- The Tag Editor export populates a matrix of all tags against all resources, missing tags are populated with a value of 'not tagged'.
  Re-using this export CSV as input to the RFC results in all the previously missing tags being created, with literal values of 'not tagged'.
- This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer
  to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC,
  be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.

To use the automated version of this change type, recommended except in unusual circumstances, see
[Tag | Bulk Update](management-advanced-tag-bulk-update.md "management-advanced-tag-bulk-update.md").

- For supported services and other information, see
  [Tag bulk update notes](../userguide/ams-tags-bu-notes.md "../userguide/ams-tags-bu-notes.md").
- Bulk add tags to existing supported resources, except those in AMS infrastructure stacks (stacks named mc-\*).

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0k4b96aatyqgl](schemas.md#ct-0k4b96aatyqgl-schema-section "schemas.md#ct-0k4b96aatyqgl-schema-section").

## Example: Required Parameters

```
{
    "Description": "Tag all the instances for App A",
    "CsvS3Url": "https://example-bucket.s3.eu-central-1.amazonaws.com/tags.csv"
}
```

## Example: All Parameters

```
{
  "Description": "Tag all the instances for App A",
  "CsvS3Url": "https://example-bucket.s3.amazonaws.com/tags.csv?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE",
  "Priority": "Medium"
}
```
