# Tutorial: Use input transformers to transform events in EventBridge

You can use the [Input transformer](eb-transform-target-input.md "eb-transform-target-input.md") in EventBridge
to customize text from an [event](eb-events.md "eb-events.md") before you send it to the
target of a [rule](eb-rules.md "eb-rules.md").

To do this, you define JSON paths from the event and assign their outputs to different
variables. Then you can use those variables in the input template. The characters < and

> can't be escaped. For more information, see [Amazon EventBridge input transformation](eb-transform-target-input.md "eb-transform-target-input.md")

###### Note

If you specify a variable to match a JSON path that doesn't exist in the event, that
variable isn't created and doesn't appear in the output.

In this tutorial, you create a rule that matches an event with `detail-type: "customerCreated"`.
The input transformer maps the `type` variable to the $.detail-type JSON path from the event. Then EventBridge
puts the variable into the input template "This event was <type>." The result is the following Amazon SNS message.

```
"This event was of customerCreated type."
```

###### Steps:

- [Step 1: Create an Amazon SNS topic](#eb-input-transformer-tutorial-create-topic "#eb-input-transformer-tutorial-create-topic")
- [Step 2: Create an Amazon SNS subscription](#eb-input-transformer-tutorial-create-sns "#eb-input-transformer-tutorial-create-sns")
- [Step 3: Create a rule](#eb-input-transformer-create-rule "#eb-input-transformer-create-rule")
- [Step 4: Send test events](#eb-input-transformer-send-test-events "#eb-input-transformer-send-test-events")
- [Step 5: Confirm success](#success "#success")
- [Step 6: Clean up your resources](#cleanup "#cleanup")

## Step 1: Create an Amazon SNS topic

Create a topic to receive the events from EventBridge.

###### To create a topic

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. Choose **Create topic**.
4. For **Type**, choose
   **Standard**.
5. Enter `eventbridge-IT-test` as the name of the topic.
6. Choose **Create topic**.

## Step 2: Create an Amazon SNS subscription

Create a subscription to get emails with the transformed information.

###### To create a subscription

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Subscriptions**.
3. Choose **Create subscription**.
4. For **Topic ARN**, choose the topic you created in step 1.
   For this tutorial, choose **eventbridge-IT-test**.
5. For **Protocol**, choose **Email**.
6. For **Endpoint**, enter your email address.
7. Choose **Create subscription**.
8. Confirm the subscription by choosing **Confirm subscription** in the email you receive from
   AWS notifications.

## Step 3: Create a rule

Create a rule to use the input transformer to customize the instance state information that
goes to a target.

###### To create a rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. For example, name the rule `ARTestRule`
5. For **Event bus**, choose the event bus that you want
   to associate with this rule. If you want this rule to match events that come
   from your account, select **default**. When an
   AWS service in your account emits an event, it always goes to your account’s
   default event bus.
6. For **Rule type**, choose **Rule with an event
   pattern**.
7. Choose **Next**.
8. For **Event source**, choose
   **Other**.
9. For **Event pattern**, enter the following:

```
`{
 "detail-type": [
 "customerCreated"
 ]
}`
```

10. Choose **Next**.
11. For **Target types**, choose **AWS service**.
12. For **Select a target**, choose **SNS topic** from the drop-down list.
13. For **Topic**, select the Amazon SNS topic that you created in step 1. For this tutorial, choose **eventbridge-IT-test**.
14. For **Additional settings**, do the following:
    1.  For **Configure target input**, choose **Input transformer** from the drop-down list.
    2.  Choose **Configure input transformer**
    3.  for **Sample events**, enter the following:

    ```
    `{
     "detail-type": "customerCreated"
    }`
    ```

    4.  For **Target input transformer** do the following:
        1. For **Input Path**, enter the following:

        ```
        `{"detail-type":"$.detail-type"}`
        ```

        2. For **Input Template**, enter the following:

        ```
        `"This event was of <detail-type> type."`
        ```

    5.  Choose **Confirm.**.

15. Choose **Next**.
16. Choose **Next**.
17. Review the details of the rule and choose **Create rule**.

## Step 4: Send test events

Now that you've set up the SNS topic and the rule, we'll send test events to make sure
the rule is working correctly.

###### To send test events (console)

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Event buses**.
3. In the **Default event bus** tile, choose **Actions**, **Send events**.
4. Enter an event source. For example, `TestEvent`.
5. For **Detail type**, enter `customerCreated`.
6. For **Event detail**, enter `{}`.
7. Choose **Send**.

## Step 5: Confirm success

If you get an email from AWS notifications that matches the expected output, you've successfully completed the tutorial.

## Step 6: Clean up your resources

You can now delete the resources that you created for this tutorial, unless you want to retain them. By deleting AWS resources that you are no longer using, you prevent unnecessary charges to your AWS account.

###### To delete the SNS topic

1. Open the [Topics page](https://console.aws.amazon.com/sns/v3/home#/topics "https://console.aws.amazon.com/sns/v3/home#/topics") of the SNS console.
2. Select the topic that you created.
3. Choose **Delete**.
4. Enter `delete me`.
5. Choose **Delete**.

###### To delete the SNS subscription

1. Open the [Subscriptions page](https://console.aws.amazon.com/sns/v3/home#/subscriptions "https://console.aws.amazon.com/sns/v3/home#/subscriptions") of the SNS console.
2. Select the subscription that you created.
3. Choose **Delete**.
4. Choose **Delete**.

###### To delete the EventBridge rule(s)

1. Open the [Rules page](https://console.aws.amazon.com/events/home#/rules "https://console.aws.amazon.com/events/home#/rules") of the EventBridge console.
2. Select the rule(s) that you created.
3. Choose **Delete**.
4. Choose **Delete**.
