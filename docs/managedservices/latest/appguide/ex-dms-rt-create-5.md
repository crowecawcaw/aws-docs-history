# 5: AWS DMS replication task: Create

You can use the AMS console or API/CLI to create an AMS AWS DMS replication task.

## Create AWS DMS replication task

Screenshot of this change type in the AMS console:

![Create DMS replication task interface showing ID, version, and execution mode details.](images/guiDmsCreateRepTaskCT.png)
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
aws --profile saml --region us-east-1 amscm create-rfc --change-type-id "ct-1d2fml15b9eth" --change-type-version "1.0" --title "`TestDMSRepTask`" --execution-parameters "{\"Description\":\"`TestRepTask`\",\"VpcId\":\"`VPC-ID`\",\"Name\":\"`DMSRepTask`\",\"Parameters\":{\"CdcStartTime\":\`1533776569`\"MigrationType\":\"`full-load`\",\"ReplicationInstanceArn\":\"`REP_INSTANCE_ARN`\",\"SourceEndpointArn\":\"`SOURCE_ENDPOINT_ARN`\",\"TableMappings\":\"{\\\"rules\\\": [{\\\"rule-type\\\": \\\"selection\\\",\\\"rule-id\\\": \\\"1\\\",\\\"rule-name\\\": \\\"1\\\",\\\"object-locator\\\": {\\\"schema-name\\\": \\\"Test\\\",\\\"table-name\\\": \\\"%\\\"}, \\\"rule-action\\\": \\\"include\\\"}] }\",\"TargetEndpointArn\":\"`TARGET_ENDPOINT_ARN`\"},\"StackTemplateId\":\"stm-eos7uq0usnmeggdet\",\"TimeoutInMinutes\":60}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file; this example names it CreateDmsRtParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-1d2fml15b9eth" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateDmsRtParams.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
"Description":          "`DMSTestRepTask`",
"VpcId":                "`VPC_ID`",
"StackTemplateId":      "stm-eos7uq0usnmeggdet",
"Name":                 "`Test DMS RT`",
"TimeoutInMinutes":     `60`,
"Parameters":   {
    "CdcStartTime":           "`1533776569`",
    "MigrationType":          "`full-load`",
    "ReplicationInstanceArn": "`REP_INSTANCE_ARN`",
    "SourceEndpointArn":      "`SOURCE_ENDPOINT_ARN`",
    "TargetEndpointArn":      "`TARGET_ENDPOINT_ARN`"
    "TableMappings":          {"rules": [{"rule-type": "`selection`","rule-id": "`1`","rule-name": "`1`","object-locator": {"schema-name": "`Test`","table-name": "`%`"}, "rule-action": "`include`"}] }",
    }
}
```

3. Output the JSON template to a file in your current folder; this example names it CreateDmsRtRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateDmsRtRfc.json
```

4. Modify and save the CreateDmsRtRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-1d2fml15b9eth",
"Title":                "`DMS-RI-Create-RFC`"
}
```

5. Create the RFC, specifying the execution parameters file and the CreateDmsRtRfc file:

```
aws amscm create-rfc --cli-input-json file://CreateDmsRtRfc.json --execution-parameters file://CreateDmsRtParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
You can create a AWS DMS task that captures three different types of changes or data. For more information, see
[Working with AWS DMS Tasks](../../../dms/latest/userguide/CHAP_Tasks.md "../../../dms/latest/userguide/CHAP_Tasks.md"),
[Creating a Task](../../../dms/latest/userguide/CHAP_Tasks.md "../../../dms/latest/userguide/CHAP_Tasks.md"), and
[Creating Tasks for Ongoing Replication Using AWS DMS](../../../dms/latest/userguide/CHAP_Task.md "../../../dms/latest/userguide/CHAP_Task.md").
