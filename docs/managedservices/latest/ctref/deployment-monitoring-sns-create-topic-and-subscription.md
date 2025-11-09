# SNS | Create (Topic and Subscription)

Create an SNS topic and up to five subscriptions.

**Full classification:** Deployment | Monitoring and notification | SNS | Create (topic and subscription)

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-3dfnglm4ombbs |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create SNS topic and subscription

Screenshot of this change type in the AMS console:

![Change type details for creating an SNS topic with ID, version, and execution mode.](images/guiSnsTopSubCreateCT.png)
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
aws amscm create-rfc --change-type-id "ct-3dfnglm4ombbs" --change-type-version "1.0" --title "`CREATE_SNS_TOPIC`" --execution-parameters "{\"Description\":\"`SNS_TOPIC_DESCRIPTION`\",\"VpcId\":\"`VPC_ID`\",\"Name\":\"`SNS_TOPIC_NAME`\",\"StackTemplateId\":\"stm-eakrsalqo9m62tpun\",\"TimeoutInMinutes\":60,\"Parameters\":{\"TopicName\":\"`mytopic-cli`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it CreateSnsTopicSubParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-3dfnglm4ombbs" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateSnsTopicSubParams.json
```

2. Modify and save the CreateSnsTopicSubParams file. For example, you can replace the contents with something like this:

```
{
"Description":      "`SnsTopicSub-Create`",
"VpcId": "`VPC_ID`",
"Name":             "`My-SnsTopicSub`",
"Parameters":{
    "TopicName": "`mytopic-cli-all-params`",
    "DisplayName": "`testsns`",
    "Subscription1Protocol": "`email`",
    "Subscription1Endpoint": "`abc@xyz.com`",
    "Subscription1RawMessageDelivery": "`false`",
    "Subscription2Protocol": "`sms`",
    "Subscription2Endpoint": "`+61500444777`",
    "Subscription2RawMessageDelivery": "`false`",
    "KmsMasterKeyId": "`arn:aws:kms:us-east-1:123456789101:key/cfe0542d-3be9-4166-9eac-d0cd6af61445`"
    }
}
```

3. Output the RFC template JSON file to a file named CreateSnsTopicSubRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateSnsTopicSubRfc.json
```

4. Modify and save the CreateSnsTopicSubRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-3dfnglm4ombbs",
"Title":                "`SnsTopicSub-Create-RFC`"
}
```

5. Create the RFC, specifying the CreateSnsTopicSub Rfc file and the CreateSnsTopicSubParams file:

```
aws amscm create-rfc --cli-input-json file://CreateSnsTopicSubRfc.json  --execution-parameters file://CreateSnsTopicSubParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
To learn more about AWS Simple Notification Service (SNS) and creating SNS topics and subscriptions, see
[Amazon Simple Notification Service](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/"). Also see
[Getting Started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md"). For pricing information,
see [Amazon SNS pricing](https://aws.amazon.com/sns/pricing/ "https://aws.amazon.com/sns/pricing/").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-3dfnglm4ombbs](schemas.md#ct-3dfnglm4ombbs-schema-section "schemas.md#ct-3dfnglm4ombbs-schema-section").

## Example: Required Parameters

```
{
  "Description" : "Creates SNS Topic using random Topic name with no input or parameter given.",
  "VpcId" : "vpc-12345678901234567",
  "Name" : "TestStack",
  "StackTemplateId" : "stm-eakrsalqo9m62tpun",
  "TimeoutInMinutes" : 60,
  "Parameters" : { }
}

```

## Example: All Parameters

```
{
  "Description" : "Creates just SNS Topic per the given name",
  "VpcId" : "vpc-12345678",
  "Name" : "TestStack",
  "Tags" : [
    {
      "Key" : "foo",
      "Value" : "bar"
    }
  ],
  "StackTemplateId" : "stm-eakrsalqo9m62tpun",
  "TimeoutInMinutes" : 60,
  "Parameters" : {
    "TopicName" : "MySNSTopic",
    "DisplayName" : "",
    "Subscription1Endpoint" : "",
    "Subscription1RawMessageDelivery" : "false",
    "Subscription2Endpoint" : "",
    "Subscription2RawMessageDelivery" : "false",
    "Subscription3Endpoint" : "",
    "Subscription3RawMessageDelivery" : "false",
    "Subscription4Endpoint" : "",
    "Subscription4RawMessageDelivery" : "false",
    "Subscription5Endpoint" : "",
    "Subscription5RawMessageDelivery" : "false",
    "KmsMasterKeyId" : ""
  }
}

```
