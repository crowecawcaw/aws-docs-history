# Tutorial: Archive and replay events in Amazon EventBridge

You can use EventBridge to route [events](eb-events.md "eb-events.md") to specific [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") functions using [rules](eb-rules.md "eb-rules.md").

In this tutorial, you’ll create a function to use as the target for the EventBridge rule using
the Lambda console. Then, you'll create an [archive](eb-archive-event.md "eb-archive-event.md")
and a rule that'll archive test events using the EventBridge console. Once there are events in
that archive, you'll [replay](eb-replay-archived-event.md "eb-replay-archived-event.md") them.

###### Steps:

- [Step 1: Create a Lambda function](#eb-create-lambda-function "#eb-create-lambda-function")
- [Step 2: Create archive](#eb-ar-create-archive "#eb-ar-create-archive")
- [Step 3: Create rule](#eb-ar-create-rule "#eb-ar-create-rule")
- [Step 4: Send test events](#eb-ar-send-test-events "#eb-ar-send-test-events")
- [Step 5: Replay events](#eb-ar-replay-events "#eb-ar-replay-events")
- [Step 6: Clean up your resources](#cleanup "#cleanup")

## Step 1: Create a Lambda function

First, create a Lambda function to log the events.

###### To create a Lambda function:

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**.
3. Choose **Author from scratch**.
4. Enter a name and description for the Lambda function. For example,
   name the function `LogScheduledEvent`.
5. Leave the rest of the options as the defaults and choose **Create function**.
6. On the **Code** tab of the function page, double-click
   **index.js**.
7. Replace the existing JavaScript code with the following code:

```
'use strict';

exports.handler = (event, context, callback) => {
    console.log('LogScheduledEvent');
    console.log('Received event:', JSON.stringify(event, null, 2));
    callback(null, 'Finished');
};
```

8. Choose **Deploy**.

## Step 2: Create archive

Next, create the archive that will hold all the test events.

###### To create an archive

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Archives**.
3. Choose **Create archive**.
4. Enter a name and description for the archive. For example,
   name the archive `ArchiveTest`.
5. Leave the rest of the options as the defaults and choose
   **Next**.
6. Choose **Create archive**.

## Step 3: Create rule

Create a rule to archive events that are sent to the event bus.

###### To create a rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. For example, name the rule `ARTestRule`.

A rule can't have the same name as another rule in the same Region and on the
same event bus. 5. For **Event bus**, choose the event bus that you want
to associate with this rule. If you want this rule to match events that come
from your account, select **default**. When an
AWS service in your account emits an event, it always goes to your account’s
default event bus. 6. For **Rule type**, choose **Rule with an event
pattern**. 7. Choose **Next**. 8. For **Event source**, choose
**Other**. 9. For **Event pattern**, enter the following:

```
{
  "detail-type": [
    "customerCreated"
  ]
}
```

10. Choose **Next**.
11. For **Target types**, choose **AWS service**.
12. For **Select a target**, choose **Lambda
    function** from the drop-down list.
13. For **Function**, select the Lambda function that you created
    in the **Step 1: Create a Lambda function** section. In this example, select `LogScheduledEvent`.
14. Choose **Next**.
15. Choose **Next**.
16. Review the details of the rule and choose **Create rule**.

## Step 4: Send test events

Now that you've set up the archive and the rule, we'll send test events to make sure
the archive is working correctly.

###### Note

It can take some time for events to get to the archive.

###### To send test events (console)

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Event buses**.
3. In the **Default event bus** tile, choose **Actions**, **Send events**.
4. Enter an event source. For example, `TestEvent`.
5. For **Detail type**, enter `customerCreated`.
6. For **Event detail**, enter `{}`.
7. Choose **Send**.

## Step 5: Replay events

Once the test events are in the archive you can replay them.

###### To replay archived events (console)

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Replays**.
3. Choose **Start new replay**.
4. Enter a name and description for the replay. For example,
   name the replay `ReplayTest`.
5. For **Source**, select the archive you created in the
   **Step 2: Create archive** section.
6. For **Replay time frame**, do the following.
   1. For **Start time**, select the date you sent test
      events and a time before you sent them. For example,
      `2021/08/11` and `08:00:00`.
   2. For **End time**, select the current date and time.
      For example, `2021/08/11` and `09:15:00`.

7. Choose **Start Replay**.

## Step 6: Clean up your resources

You can now delete the resources that you created for this tutorial, unless you want to retain them. By deleting AWS resources that you are no longer using, you prevent unnecessary charges to your AWS account.

###### To delete the Lambda function(s)

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Select the function(s) that you created.
3. Choose **Actions**, **Delete**.
4. Choose **Delete**.

###### To delete the EventBridge archives(s)

1. Open the [Archives page](https://console.aws.amazon.com/events/home#/archives "https://console.aws.amazon.com/events/home#/archives") of the EventBridge console.
2. Select the archive(s) you created.
3. Choose **Delete**.
4. Enter the archive name and choose **Delete**.

###### To delete the EventBridge rule(s)

1. Open the [Rules page](https://console.aws.amazon.com/events/home#/rules "https://console.aws.amazon.com/events/home#/rules") of the EventBridge console.
2. Select the rule(s) that you created.
3. Choose **Delete**.
4. Choose **Delete**.
