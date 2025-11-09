# Database Migration Service (DMS) | Create Target Endpoint (Kafka)

Create a Database Migration Service (DMS) target endpoint for kafka.

**Full classification:** Deployment | Advanced stack components | Database Migration Service (DMS) | Create target endpoint (kafka)

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-1mrqxscu15apz |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create AWS Database Migration Service target endpoint for Amazon MSK

AMS DMS can use Amazon Managed Streaming for Apache Kafka as a target endpoint.

Screenshot of this change type in the AMS console:

![AMS Advanced console, create RFC section, change type details box for ct-1mrqxscu15apz: Create AWS Database Migration Service target endpoint for Amazon MSK.](images/guiDmsCreateTargetEpKafkaCT.png)
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
aws --profile saml --region `us-east-1` amscm create-rfc --change-type-id "ct-1mrqxscu15apz" --change-type-version "1.0" --title "`TestDMSTargetEndpointKafka`" --execution-parameters "{\"Description\":\"`TestKafkaTE`\",\"VpcId\":\"`VPC-ID`\",\"Name\":\"`KafkaTE-NAME`\",\"StackTemplateId\":\"stm-knghtmmgefafdq89u"\",\"TimeoutInMinutes\":`60`,\"Parameters\":{\"EngineName\":\"`kafka`\",\"Broker": "`BROKER-ID`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named CreateDmsTeKafkaParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-1mrqxscu15apz" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateDmsTeKafkaParams.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
  "Description": "`Test description`",
  "VpcId": "`VPC-ID`",
  "Name": "`dmstargetsKafka`",
  "StackTemplateId": "stm-knghtmmgefafdq89u",
  "TimeoutInMinutes": `60`,
  "Parameters": {
    "EngineName": "`kafka`",
    "Broker": "`BROKER-ID`"
  }
}
```

3. Output the JSON template to a file in your current folder; this example names it CreateDmsTeKafkaRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateDmsTeKafkaRfc.json
```

4. Modify and save the CreateDmsTeKafkaRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-1mrqxscu15apz",
"Title":                "`Kafka-DMS-Target-Endpoint`"
}
```

5. Create the RFC, specifying the execution parameters file and the CreateDmsTeKafkaRfc file:

```
aws amscm create-rfc --cli-input-json file://CreateDmsTeKafkaRfc.json --execution-parameters file://CreateDmsTeKafkaParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

- To learn more about AWS Database Migration Service (AWS DMS) Amazon MSK endpoints, see
  [Using Apache Kafka as a target for AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Target.md "../../../dms/latest/userguide/CHAP_Target.md")
- To learn more about Amazon Managed Streaming for Apache Kafka see [What is Apache Kafka?](https://aws.amazon.com/what-is/apache-kafka/ "https://aws.amazon.com/what-is/apache-kafka/")
- For more information on AWS DMS targets, see [Targets for Data Migration](../../../dms/latest/userguide/CHAP_Target.md "../../../dms/latest/userguide/CHAP_Target.md").
- You can add up to 50 tags, but to do so you must enable the **Additional configuration** view.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-1mrqxscu15apz](schemas.md#ct-1mrqxscu15apz-schema-section "schemas.md#ct-1mrqxscu15apz-schema-section").

## Example: Required Parameters

```
{
  "Description": "Test description.",
  "VpcId": "vpc-1234567890abcdef0",
  "Name": "dmstargets301",
  "StackTemplateId": "stm-knghtmmgefafdq89u",
  "TimeoutInMinutes": 60,
  "Parameters": {
    "EngineName": "kafka",
    "Broker": "ec2-12-345-678-901.compute-1.amazonaws.com:2345"
  }
}
```

## Example: All Parameters

```
{
  "Description": "Test description.",
  "VpcId": "vpc-317a9856",
  "Name": "dmstargets301",
  "StackTemplateId": "stm-knghtmmgefafdq89u",
  "TimeoutInMinutes": 60,
  "Parameters": {
    "EndpointIdentifier": "mykafkadmstarget",
    "EngineName": "kafka",
    "Broker": "ec2-12-345-678-901.compute-1.amazonaws.com:2345",
    "Topic": "kafka-default-topic"
  }
}
```
