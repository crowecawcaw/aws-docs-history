# Other | Update (Review Required)

Use to request a manual update to a resource.

**Full classification:** Management | Other | Other | Update (review required)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-0xdawir96cy7k          |
| Current version             | 1.0                       |
| Expected execution duration | 240 minutes               |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

### Update Other Other CTs

Screenshot of this change type in the AMS console:

![Change type details showing ID, version, description, and manual execution mode.](images/guiOtherUpdate.png)
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

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0xdawir96cy7k" --change-type-version "1.0" --title "`TITLE`" --execution-parameters "{\"Comment\": \"`What you want changed`\", \"Priority\": \"`Medium`\" \"RelatedIds\":[\"RESOURCE_ID\",\"RESOURCE_ID\"]}}"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named OtherUpdateParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-0xdawir96cy7k" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > OtherUpdateParams.json
```

2. Modify and save the OtherUpdateParams file. For example, you can replace the contents with something like this:

```
{
"Comment":          "`WHAT-TO-UPDATE`",
"Priority":         "`Medium`",
"RelatedIds":       `["RESOURCE_ID", "RESOURCE_ID"]`
}
```

3. Output the RFC template to a file in your current folder; this example names it OtherUpdateRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > OtherUpdateRfc.json
```

4. Modify and save the OtherUpdateRfc.json file. For example, you can replace the contents with something like this:.

```
{
"ChangeTypeId":         "ct-0xdawir96cy7k",
"ChangeTypeVersion":    "`1.0`",
"Title":                "`TITLE`"
}
```

5. Create the RFC, specifying the OtherUpdateRfc file and the OtherUpdateParams file:

```
aws amscm create-rfc --cli-input-json file://OtherUpdateRfc.json  --execution-parameters file://OtherUpdateParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Important

Updating or Deleting stacks can have unwanted and unanticipated consequences. AMS prefers to \*not\*
update or delete stacks or stack resources on behalf of customers for this reason. Note, that AMS
will only update or delete resources on your behalf (through a submitted Mangement | Other | Other | Update change type)
that are not possible to update or delete using the appropriate, automated, change type to delete.

This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer
to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC,
be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.

Use this CT when you can't find a change type for what you want; however, if you are unsure about specifying parameters in an existing CT, it is better
to submit a service request for help. For information on submitting service requests, see [Service Request Examples](../userguide/serv-req-mgmt-examples.md "../userguide/serv-req-mgmt-examples.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0xdawir96cy7k](schemas.md#ct-0xdawir96cy7k-schema-section "schemas.md#ct-0xdawir96cy7k-schema-section").

## Example: Required Parameters

```
{
  "Comment": "This is a test comment"
}

```

## Example: All Parameters

```
{
  "Comment": "This is a test comment",
  "Priority": "High",
  "RelatedIds": ["foo", "bar", "baz"]
}

```
