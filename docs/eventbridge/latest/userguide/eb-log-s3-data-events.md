# Tutorial: Log Amazon S3 object-level operations using

EventBridge

You can log the object-level API operations on your [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") buckets. Before Amazon EventBridge can
match these [events](eb-events.md "eb-events.md"), you must use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to set up and
configure a trail to receive these events.

In this tutorial, you create CloudTrail trail, create a [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") function,
and then create [rule](eb-rules.md "eb-rules.md") in the EventBridge console that invokes
that function in response to an S3 data event.

###### Steps:

- [Step 1: Configure your AWS CloudTrail trail](#eb-configure-trail "#eb-configure-trail")
- [Step 2: Create an AWS Lambda
  function](#eb-log-s3-create-lambda-function "#eb-log-s3-create-lambda-function")
- [Step 3: Create a Rule](#eb-log-s3-create-rule "#eb-log-s3-create-rule")
- [Step 4: Test the Rule](#eb-log-s3-test-rule "#eb-log-s3-test-rule")
- [Step 5: Confirm success](#success "#success")
- [Step 6: Clean up your resources](#cleanup "#cleanup")

## Step 1: Configure your AWS CloudTrail trail

To log data events for an S3 bucket to AWS CloudTrail and EventBridge, you first create a trail. A
_trail_ captures API calls and related events in your account and
then delivers the log files to an S3 bucket that you specify. You can update an existing
trail or create one.

For more information, see [Data Events](../../../awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.md#logging-data-events") in the _AWS CloudTrail User Guide_.

###### To create a trail

1. Open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. Choose **Trails**, **Create trail**.
3. For **Trail name**, type a name for the trail.
4. For **Storage location**, in **Create a new S3
   bucket**.
5. For **AWS KMS alias**, type an alias for the KMS key.
6. Choose **Next**.
7. For **Event type**, choose **Data events**
8. For **Data events,** do one of the following:
   - To log data events for all Amazon S3 objects in a bucket, specify an S3
     bucket and an empty prefix. When an event occurs on an object in that
     bucket, the trail processes and logs the event.
   - To log data events for specific Amazon S3 objects in a bucket, specify an
     S3 bucket and the object prefix. When an event occurs on an object in
     that bucket and the object starts with the specified prefix, the trail
     processes and logs the event.

9. For each resource, choose whether to log **Read** events,
   **Write** events, or both.
10. Choose **Next**.
11. Choose **Create trail**.

## Step 2: Create an AWS Lambda

function

Create a Lambda function to log data events for your S3 buckets.

###### To create a Lambda function

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**.
3. Choose **Author from scratch**.
4. Enter a name and description for the Lambda function. For example, name the
   function `LogS3DataEvents`.
5. Leave the rest of the options as the defaults and choose **Create function**.
6. On the **Code** tab of the function page, double-click **index.js**.
7. Replace the existing code with the following code.

```
'use strict';

exports.handler = (event, context, callback) => {
    console.log('LogS3DataEvents');
    console.log('Received event:', JSON.stringify(event, null, 2));
    callback(null, 'Finished');
};
```

8. Choose **Deploy**.

## Step 3: Create a Rule

Create a rule to run the Lambda function you created in Step 2. This rule runs in
response to an Amazon S3 data event.

###### To create a rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. For example, name the rule `TestRule`
5. For **Event bus**, choose the event bus that you want
   to associate with this rule. If you want this rule to match events that come
   from your account, select **default**. When an
   AWS service in your account emits an event, it always goes to your account’s
   default event bus.
6. For **Rule type**, choose **Rule with an event
   pattern**.
7. Choose **Next**.
8. For **Event source**, choose
   **AWS services**.
9. For **Event pattern**, do the following:
   1. For **Event source**, select **Simple
      Storage Service (S3)** from the drop-down list.
   2. For **Event type**, select **Object-Level
      API call via CloudTrail** from the drop-down list.
   3. Choose **Specific operation(s)**, and then choose
      **PutObject**.
   4. By default, the rule matches data events for all buckets in the
      Region. To match data events for specific buckets, choose
      **Specify bucket(s) by name** and enter one or
      more buckets.

10. Choose **Next**.
11. For **Target types**, choose **AWS service**.
12. For **Select a target**, choose **Lambda
    function** from the drop-down list.
13. For **Function**, select the `LogS3DataEvents` Lambda function that you created
    in step 1.
14. Choose **Next**.
15. Choose **Next**.
16. Review the details of the rule and choose **Create rule**.

## Step 4: Test the Rule

To test the rule, put an object in your S3 bucket. You can verify that your Lambda
function was invoked.

###### To view the logs for your Lambda function

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**.
3. Select the name of the log group for your Lambda function
   (`/aws/lambda/`function-name``).
4. Select the name of the log stream to view the data provided by the
   function for the instance that you launched.

You can also check your CloudTrail logs in the S3 bucket that you specified for your trail.
For more information, see [Getting and Viewing Your
CloudTrail Log Files](../../../awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.md "../../../awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.md") in the _AWS CloudTrail User Guide_.

## Step 5: Confirm success

If you see the Lambda event in the CloudWatch logs, you've successfully completed this tutorial. If the event isn't in your CloudWatch logs, start troubleshooting by verifying the rule was created successfully
and, if the rule looks correct, verify the code of your Lambda function is correct.

## Step 6: Clean up your resources

You can now delete the resources that you created for this tutorial, unless you want to retain them. By deleting AWS resources that you are no longer using, you prevent unnecessary charges to your AWS account.

###### To delete the EventBridge rule(s)

1. Open the [Rules page](https://console.aws.amazon.com/events/home#/rules "https://console.aws.amazon.com/events/home#/rules") of the EventBridge console.
2. Select the rule(s) that you created.
3. Choose **Delete**.
4. Choose **Delete**.

###### To delete the Lambda function(s)

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Select the function(s) that you created.
3. Choose **Actions**, **Delete**.
4. Choose **Delete**.

###### To delete the CloudTrail trail(s)

1. Open the [Trails page](https://console.aws.amazon.com/cloudtrail/home#/trails "https://console.aws.amazon.com/cloudtrail/home#/trails") of the CloudTrail console.
2. Select the trail(s) that you created.
3. Choose **Delete**.
4. Choose **Delete**.
