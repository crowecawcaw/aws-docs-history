# Management Account | Delete StackSets Stack (Managed Automation)

Delete AWS CloudFormation (CFN) StackSets-created stacks and instances.

**Full classification:** Management | Managed landing zone | Management account | Delete StackSets stack (managed automation)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-1yqy4frl5s8y8          |
| Current version             | 1.0                       |
| Expected execution duration | 240 minutes               |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

### Delete a Stacksets stack

Screenshot of this change type in the AMS console:

![](images/guiManLzStckstsStckDeleteCT.png)
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

###### Note

Run this change type from your Management account.

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1yqy4frl5s8y8" --change-type-version "1.0" --title "`Delete StackSets Stack`" --execution-parameters "{\"Name\": \"`Stackset name`\", \"Region\": \"`us-east-1`\"}"

```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it DeleteStacksetsStackParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-1yqy4frl5s8y8" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeleteStacksetsStackParams.json
```

2. Modify and save the DeleteStacksetsStackParams file. For example, you can replace the contents with something like this:

```
{
   "Name": "`Stackset name`",
   "Region": "`us-east-1`",
   "Priority": "`High`"
 }
```

3. Output the RFC template JSON file to a file; this example names it DeleteStacksetsStackRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > DeleteStacksetsStackRfc.json
```

4. Modify and save the DeleteStacksetsStackRfc.json file. For example, you can replace the contents with something like this:

```
{
  "ChangeTypeVersion": "1.0",
  "ChangeTypeId": "ct-1yqy4frl5s8y8",
  "Title": "`Delete StackSets Stack`"
}
```

5. Create the RFC, specifying the DeleteStacksetsStack Rfc file and the DeleteStacksetsStackParams file:

```
aws amscm create-rfc --cli-input-json file://DeleteStacksetsStackRfc.json  --execution-parameters file://DeleteStacksetsStackParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

- For AWS CloudFormation details, see
  [Delete a stack set](../../../AWSCloudFormation/latest/UserGuide/stacksets-delete.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-delete.md")
- For general AWS CloudFormation information on stack sets, see
  [StackSets concepts](../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md")
- To learn more about AMS multi-account landing zone, see
  [AWS Managed Services (AMS) Now Offers Managed Landing Zones](https://aws.amazon.com/about-aws/whats-new/2019/10/aws-managed-services-now-offers-managed-landing-zones/ "https://aws.amazon.com/about-aws/whats-new/2019/10/aws-managed-services-now-offers-managed-landing-zones/").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-1yqy4frl5s8y8](schemas.md#ct-1yqy4frl5s8y8-schema-section "schemas.md#ct-1yqy4frl5s8y8-schema-section").

## Example: Required Parameters

```
{
  "Name": "test-stackset"
}

```

## Example: All Parameters

```
{
  "Name": "test-stackset",
  "Region": "us-east-1",
  "Priority": "High"
}

```
