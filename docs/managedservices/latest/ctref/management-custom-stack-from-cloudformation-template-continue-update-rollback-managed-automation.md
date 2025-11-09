# Stack from CloudFormation Template | Continue Update Rollback (Managed Automation)

Request a ContinueUpdateRollback operation for the specified CloudFormation stack that's in the UPDATE_ROLLBACK_FAILED state. Use this operation when a CloudFormation stack is stopped due to a failed update rollback and you need AMS engineers to complete the rollback and return the stack to its last known working state.

**Full classification:** Management | Custom Stack | Stack From CloudFormation Template | Continue update rollback (managed automation)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-32r1igwrwag4i          |
| Current version             | 1.0                       |
| Expected execution duration | 240 minutes               |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

### Continue rollback on custom AWS CloudFormation stack

![AMS Advanced console, create RFC section, change type details box for ct-32r1igwrwag4i: Continue rollback on custom AWS CloudFormation stack.](images/guiCustomStackContinueRollback.png)

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
aws amscm create-rfc --change-type-id "ct-32r1igwrwag4i" --change-type-version "1.0" --title "`Continue Update Rollback`" --execution-parameters "{\"StackId\":\"`STACK_ID`\",\"Region\":\"`REGION`\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file in your current folder; this example names it ContinueRollbackParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-32r1igwrwag4i" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ContinueRollbackParams.json
```

2. Modify and save the ContinueRollbackParams.json file. For example, you can replace the contents with something like this:

```
{
    "StackId": "stack-a1b2c3d4e5f67890e",
    "Region": "`us-east-1`",
    "Priority": "`High`"
}
```

3. Output the JSON template for CreateRfc to a file in your current folder; this example names it ContinueRollbackRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > ContinueRollbackRfc.json
```

4. Modify and save the ContinueRollbackRfc.json file. For example, you can replace the contents with something like this:

```
{
  "ChangeTypeVersion": "1.0",
  "ChangeTypeId": "ct-32r1igwrwag4i",
  "Title": "`Continue Update Rollback`"
}
```

5. Create the RFC, specifying the ContinueRollbackRfc file and the execution parameters file:

```
aws amscm create-rfc --cli-input-json file://ContinueRollbackRfc.json --execution-parameters file://ContinueRollbackParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
For more information see
[Continue rolling back an update](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-32r1igwrwag4i](schemas.md#ct-32r1igwrwag4i-schema-section "schemas.md#ct-32r1igwrwag4i-schema-section").

## Example: Required Parameters

```
{
  "StackId": "stack-a1b2c3d4e5f67890e",
  "Region": "us-east-1"
}
```

## Example: All Parameters

```
{
  "StackId": "stack-a1b2c3d4e5f67890e",
  "Region": "us-east-1",
  "Priority": "Medium"
}
```
