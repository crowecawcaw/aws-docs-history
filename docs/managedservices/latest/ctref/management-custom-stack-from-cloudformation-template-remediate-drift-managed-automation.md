# Stack from CloudFormation Template | Remediate Drift (Managed Automation)

Remediate the drift (out-of-band changes) in a stack, bringing the stack in sync and enabling you to perform future updates using the available Update CTs. Drift remediation can be performed on EC2 resource types.

**Full classification:** Management | Custom Stack | Stack From CloudFormation Template | Remediate drift (managed automation)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-34sxfo53yuzah          |
| Current version             | 1.0                       |
| Expected execution duration | 240 minutes               |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

### Remediate stack drift (Managed Automation)

Screenshot of this change type in the AMS console:

![](images/guiStackRemediateDriftRrCT.png)
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
aws amscm create-rfc --change-type-id "ct-34sxfo53yuzah" --change-type-version "1.0" --title "`Remediate stack drift`" --execution-parameters '{"StackName":"`stack-a1b2c3d4e5f67890e`","DryRun":`false`}'
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it RemediateDriftParams.json:

```
aws amscm create-rfc --generate-cli-skeleton > RemediateDriftParams.json
```

2. Modify and save the RemediateDriftParams file. For example, you can replace the contents with something like this:

```
{
"StackName" : "`stack-a1b2c3d4e5f67890e`",
"DryRun" : false
}
```

3. Output the RFC template JSON file to a file; this example names it RemediateDriftRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > RemediateDriftRfc.json
```

4. Modify and save the RemediateDriftRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeId": "ct-34sxfo53yuzah",
"ChangeTypeVersion": "1.0",
"Title": "`Remediate stack drift`"
}
```

5. Create the RFC, specifying the RemediateDriftRfc file and the RemediateDriftParams file:

```
aws amscm create-rfc --cli-input-json file://RemediateDriftRfc.json  --execution-parameters file://RemediateDriftParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer
to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC,
be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.

###### Note

When using manual CTs, AMS recommends that you use the ASAP **Scheduling** option
(choose **ASAP** in the console, leave start and end time blank in the API/CLI) as these CTs require an AMS operator to examine the RFC, and
possibly communicate with you before it can be approved and run. If you schedule these RFCs, be sure to allow at least 24 hours. If approval does not
happen before the scheduled start time, the RFC is rejected automatically.

- There is an automated version of this change type that runs more quickly, though there are some limitations. For more details, see
  [Stack | Remediate Drift](management-standard-stack-remediate-drift-rr-auto.md "management-standard-stack-remediate-drift-rr-auto.md").
- Stack remediation modifies the stack template and/or parameter values. Once remediation is complete,
  you must update your local template repositories, or any automation, that would be updating the
  remediated stack, with the latest template and parameters provided in the RFC summary of the remeditation. It is very
  important to do this, because using the old template and/or parameters can cause destructive changes on the stack resources.

For more details, see [Drift remediation FAQs](../userguide/drift-rr-remediate-faqs.md "../userguide/drift-rr-remediate-faqs.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-34sxfo53yuzah](schemas.md#ct-34sxfo53yuzah-schema-section "schemas.md#ct-34sxfo53yuzah-schema-section").

## Example: Required Parameters

```
{
  "StackName": "stack-a1b2c3d4e5f678900"
}

```

## Example: All Parameters

```
{
  "StackName": "stack-a1b2c3d4e5f678900",
  "DryRun": false,
  "Priority": "Medium"
}

```
