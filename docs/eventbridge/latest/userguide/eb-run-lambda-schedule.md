# Tutorial: Create an EventBridge scheduled rule for AWS Lambda functions

You can set up a [rule](eb-rules.md "eb-rules.md") to run an [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") function on a
schedule. This tutorial shows how to use the AWS Management Console or the AWS CLI to create the rule. If
you want to use the AWS CLI but haven't installed it, see the [Installing, updating, and uninstalling the AWS CLI version 2](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md").

For schedules, EventBridge doesn't provide second-level precision in [schedule expressions](eb-create-rule-schedule.md "eb-create-rule-schedule.md"). The finest resolution
using a cron expression is one minute. Due to the distributed nature of EventBridge and the
target services, there can be a delay of several seconds between the time the scheduled
rule is triggered and the time the target service runs the target resource.

###### Steps:

- [Step 1: Create a Lambda function](#eb-create-lambda-function "#eb-create-lambda-function")
- [Step 2: Create a Rule](#eb-schedule-create-rule "#eb-schedule-create-rule")
- [Step 3: Verify the rule](#eb-schedule-test-rule "#eb-schedule-test-rule")
- [Step 4: Confirm success](#success "#success")
- [Step 5: Clean up your resources](#cleanup "#cleanup")

## Step 1: Create a Lambda function

Create a Lambda function to log the scheduled events.

###### To create a Lambda function

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**.
3. Choose **Author from scratch**.
4. Enter a name and description for the Lambda function. For example,
   name the function `LogScheduledEvent`.
5. Leave the rest of the options as the defaults and choose **Create function**.
6. On the **Code** tab of the function page, double-click **index.js**.
7. Replace the existing code with the following code.

```
'use strict';

exports.handler = (event, context, callback) => {
    console.log('LogScheduledEvent');
    console.log('Received event:', JSON.stringify(event, null, 2));
    callback(null, 'Finished');
};
```

8. Choose **Deploy**.

## Step 2: Create a Rule

Create a rule to run the Lambda function you created in step 1 on a schedule.

You can use either the console or the AWS CLI to create the rule. To use the AWS CLI, you
first grant the rule permission to invoke your Lambda function. Then you can create the
rule and add the Lambda function as a target.

###### To create a rule (console)

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and on the
same event bus. 5. For **Event bus**, choose the event bus that you want
to associate with this rule. If you want this rule to match events that come
from your account, select **AWS default event bus**. When an
AWS service in your account emits an event, it always goes to your account’s
default event bus. 6. For **Rule type**, choose **Schedule**. 7. Choose **Next**. 8. For **Schedule pattern**, choose **A schedule that runs at a regular rate, such as every 10 minutes.** and
enter `5` and choose **Minutes** from the drop-down list. 9. Choose **Next**. 10. For **Target types**, choose **AWS service**. 11. For **Select a target**, choose **Lambda
function** from the drop-down list. 12. For **Function**, select the Lambda function that you created
in the **Step 1: Create a Lambda function** section. In this example, select `LogScheduledEvent`. 13. Choose **Next**. 14. Choose **Next**. 15. Review the details of the rule and choose **Create rule**.

###### To create a rule (AWS CLI)

1. To create a rule that runs on a schedule, use the
   `put-rule` command.

```
aws events put-rule \
--name `my-scheduled-rule` \
--schedule-expression 'rate(5 minutes)'
```

When this rule runs, it creates an event and then sends it to the targets. The
following is an example event.

```
{
    "version": "0",
    "id": "53dc4d37-cffa-4f76-80c9-8b7d4a4d2eaa",
    "detail-type": "Scheduled Event",
    "source": "aws.events",
    "account": "123456789012",
    "time": "2015-10-08T16:53:06Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:events:us-east-1:123456789012:rule/my-scheduled-rule"
    ],
    "detail": {}
}
```

2. To grant the EventBridge service principal (`events.amazonaws.com`)
   permission to run the rule, use the
   `add-permission` command.

```
aws lambda add-permission \
--function-name `LogScheduledEvent` \
--statement-id `my-scheduled-event` \
--action 'lambda:InvokeFunction' \
--principal events.amazonaws.com \
--source-arn arn:aws:events:`us-east-1`:`123456789012`:rule/`my-scheduled-rule`
```

3. Create the file `targets.json` with the following
   contents.

```
[
  {
    "Id": "1",
    "Arn": "arn:aws:lambda:`us-east-1`:`123456789012`:function:`LogScheduledEvent`"
  }
]
```

4. To add the Lambda function that you created in step 1 to the rule, use the
   `put-targets`command .

```
aws events put-targets --rule `my-scheduled-rule` --targets file://targets.json
```

## Step 3: Verify the rule

Wait at least five minutes after completing step 2, and then you can verify that your
Lambda function was invoked.

###### View the output from your Lambda function

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**.
3. Select the name of the log group for your Lambda function
   (`/aws/lambda/`function-name``).
4. Select the name of the log stream to view the data provided by the
   function for the instance that you launched.

## Step 4: Confirm success

If you see the Lambda event in the CloudWatch logs, you've successfully completed this tutorial. If the event isn't in your CloudWatch logs, start troubleshooting by verifying the rule was created successfully
and, if the rule looks correct, verify the code of your Lambda function is correct.

## Step 5: Clean up your resources

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
