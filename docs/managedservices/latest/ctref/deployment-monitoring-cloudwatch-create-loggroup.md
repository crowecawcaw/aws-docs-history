

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# CloudWatch \| Create LogGroup
<a name="deployment-monitoring-cloudwatch-create-loggroup"></a>

Creates a CloudWatch LogGroup with optional subscription filter, up to 5 log streams and up to 5 metric filters.

**Full classification:** Deployment \| Monitoring and notification \| CloudWatch \| Create LogGroup

## Change Type Details
<a name="ct-0cyqd7laxyhlm-DMCc-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-0cyqd7laxyhlm | 
| Current version | 1.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="deployment-monitoring-cloudwatch-create-loggroup-info"></a>

### Create CloudWatch LogGroup
<a name="ex-cw-log-group-create-col"></a>

#### Creating a CloudWatch LogGroup with the console
<a name="cw-log-group-create-con"></a>

![Change type details showing CloudWatch LogGroup creation with ID, version 1.0, and automated execution mode.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiCwCreateLGCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

#### Creating a CloudWatch LogGroup with the CLI
<a name="cw-log-group-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm  --profile saml --region us-east-1 create-rfc --change-type-id "ct-0cyqd7laxyhlm" --change-type-version "1.0" --title '{{CloudWatch LogGroup}}' --description "{{CloudWatch LogGroup}}"  --execution-parameters "{\"Description\":\"{{My Test LogGroup}}\",\"VpcId\":\"{{VPC_ID}}\",\"Name\":\"{{Test LogGroup}}\",\"StackTemplateId\":\"stm-8ian3plt5a6jbv7jt\",\"TimeoutInMinutes\":60,\"Parameters\": {\"LogGroupName\":\"{{customer-testloggroup}}\",\"LogStream1Name\":\"{{LogStream1}}\",\"SubscriptionFilterPattern\":\"{{test}}\",\"SubscriptionDestinationARN\":\"{{arn:aws:lambda:us-east-1:123456789012:function:test_lambda}}\",\"MetricFilter1Name\":\"{{test_metric_filter1}}\",\"MetricFilter1Namespace\":\"{{test_metric_filter1_namespace}}\",\"MetricFilter1Pattern\":\"{{{$.eventType=\\\"test_event\\\"}}}\",\"MetricFilter1Value\":\"{{10}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file in your current folder; this example names it CwLGParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-ct-0cyqd7laxyhlm" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CwLGParams.json
   ```

1. Modify and save the CwLGParams.json file. For example, you can replace the contents with something like this:

   ```
   {
       "Description": "{{Test CloudWatch Description}}",
       "VpcId": "{{VPC_ID}}",
       "StackTemplateId": "stm-8ian3plt5a6jbv7jt",
       "Name": "{{My_CW_Loggroup}}",
       "TimeoutInMinutes": 60,
       "Parameters": {
           "LogGroupName": "{{customer-testloggroup}}",
           "LogStream1Name": "{{LogStream1}}",
           "SubscriptionFilterPattern": "{{test}}",
           "SubscriptionDestinationARN": "{{arn:aws:lambda:us-east-1:123456789012:function:test_lambda}}",
           "MetricFilter1Name": "{{test_metric_filter1}}",
           "MetricFilter1Namespace": "{{test_metric_filter1_namespace}}",
           "MetricFilter1Pattern": "{{{$.eventType=\"test_event\"}}}",
           "MetricFilter1Value": "{{10}}"
       }
   }
   ```

1. Output the JSON template for CreateRfc to a file in your current folder; example names it CwLGRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CwLGRfc.json
   ```

1. Modify and save the CwLGRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-0cyqd7laxyhlm",
   "Title":                "{{CW-LG-RFC}}"
   }
   ```

1. Create the RFC, specifying the CwLGRfc file and the execution parameters file:

   ```
   aws amscm create-rfc --cli-input-json file://CwLGRfc.json --execution-parameters file://CwLGParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-cw-log-group-create-tip"></a>

To learn more about CloudWatch, see [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html).

## Execution Input Parameters
<a name="deployment-monitoring-cloudwatch-create-loggroup-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-0cyqd7laxyhlm](schemas.md#ct-0cyqd7laxyhlm-schema-section).

## Example: Required Parameters
<a name="deployment-monitoring-cloudwatch-create-loggroup-ex-min"></a>

```
{
  "Description": "This is a test description",
  "VpcId": "vpc-1234567890abcdef0",
  "StackTemplateId": "stm-8ian3plt5a6jbv7jt",
  "Name": "Test Stack",
  "Tags": [
    {
      "Key": "foo",
      "Value": "bar"
    },
    {
      "Key": "testkey",
      "Value": "testvalue"
    }
  ],
  "TimeoutInMinutes": 60,
  "Parameters": {
    "LogGroupName": "customer-testloggroup"
  }
}
```

## Example: All Parameters
<a name="deployment-monitoring-cloudwatch-create-loggroup-ex-max"></a>

```
{
  "Description": "This is a test description",
  "VpcId": "vpc-1234567890abcdef0",
  "StackTemplateId": "stm-8ian3plt5a6jbv7jt",
  "Name": "Test Stack",
  "Tags": [
    {
      "Key": "foo",
      "Value": "bar"
    },
    {
      "Key": "testkey",
      "Value": "testvalue"
    }
  ],
  "TimeoutInMinutes": 60,
  "Parameters": {
    "LogGroupName":"customer-test",
    "LogGroupRetentionInDays":"7",
    "LogStream1Name":"logstream1",
    "LogStream2Name":"logstream2",
    "LogStream3Name":"logstream3",
    "LogStream4Name":"logstream4",
    "LogStream5Name":"logstream5",
    "SubscriptionFilterIAMroleARN":"arn:aws:iam::123456789012:role/example-role",
    "SubscriptionFilterPattern":"Error",
    "SubscriptionDestinationARN":"arn:aws:kinesis:us-east-1:123456789012:stream/example-stream-name",
    "MetricFilter1Name":"metricfilter1",
    "MetricFilter1Namespace":"metricfilter1namespace",
    "MetricFilter1Pattern":"Error",
    "MetricFilter1Value":"10",
    "MetricFilter1DefaultValue":"1",
    "MetricFilter2Name":"metricfilter2",
    "MetricFilter2Namespace":"metricfilter2namespace",
    "MetricFilter2Pattern":"Error",
    "MetricFilter2Value":"20",
    "MetricFilter2DefaultValue":"1",
    "MetricFilter3Name":"metricfilter3",
    "MetricFilter3Namespace":"metricfilter3namespace",
    "MetricFilter3Pattern":"Error",
    "MetricFilter3Value":"30",
    "MetricFilter3DefaultValue":"1",
    "MetricFilter4Name":"metricfilter4",
    "MetricFilter4Namespace":"metricfilter4namespace",
    "MetricFilter4Pattern":"40",
    "MetricFilter4Value":"2",
    "MetricFilter4DefaultValue":"1",
    "MetricFilter5Name":"metricfilter5",
    "MetricFilter5Namespace":"metricfilter5namespace",
    "MetricFilter5Pattern":"Error",
    "MetricFilter5Value":"50",
    "MetricFilter5DefaultValue":"1"
  }
}
```