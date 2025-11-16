# Tutorial: Send events to Amazon Kinesis using EventBridge schemas

You can send AWS API call [events](eb-events.md "eb-events.md") in EventBridge to an [Amazon Kinesis stream](../../../streams/latest/dev/introduction.md "../../../streams/latest/dev/introduction.md"), create Kinesis Data Streams applications,
and process large amounts of data. In this tutorial, you create a Kinesis stream, and then create a [rule](eb-rules.md "eb-rules.md") in the EventBridge console that sends events to that stream
when an [Amazon EC2](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md") instance stops.

###### Steps:

- [Prerequisites](#eb-stream-prerequisite "#eb-stream-prerequisite")
- [Step 1: Create an Amazon Kinesis stream](#eb-stream-create-stream "#eb-stream-create-stream")
- [Step 2: Create a rule](#eb-stream-create-rule "#eb-stream-create-rule")
- [Step 3: Test the rule](#eb-stream-test-rule "#eb-stream-test-rule")
- [Step 4: Verify that the event was sent](#eb-stream-verify-event "#eb-stream-verify-event")
- [Step 5: Clean up your resources](#cleanup "#cleanup")

## Prerequisites

In this tutorial, you'll use the following:

- Use the AWS CLI to work with Kinesis streams.

To install the AWS CLI, see the [Installing, updating, and uninstalling the AWS CLI version 2](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md").

###### Note

This tutorial uses AWS events and the built in `aws.events` schema registry.
You can also create an EventBridge rule based on the schema of your custom events by adding them
to a custom schema registry manually, or by using schema discovery.

For more information on schemas, see [Amazon EventBridge schemas](eb-schema.md "eb-schema.md"). For more information on creating a rule using other event pattern options, see [Creating rules in Amazon EventBridge](eb-create-rule-visual.md "eb-create-rule-visual.md").

## Step 1: Create an Amazon Kinesis stream

To create a stream, at a command prompt, use the `create-stream`

AWS CLI command.

```
`aws kinesis create-stream --stream-name `test` --shard-count 1`
```

When the stream status is `ACTIVE`, the stream is ready. To check the
stream status, use the `describe-stream`

command.

```
`aws kinesis describe-stream --stream-name `test``
```

## Step 2: Create a rule

Create a rule to send events to your stream when you stop an Amazon EC2 instance.

###### To create a rule

1.  Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2.  In the navigation pane, choose **Rules**.
3.  Choose **Create rule**.
4.  Enter a name and description for the rule. For example, name the rule `TestRule`
5.  For **Event bus**, select **default**.
6.  For **Rule type**, choose **Rule with an event
    pattern**.
7.  Choose **Next**.
8.  For **Event source**, choose
    **AWS events or EventBridge partner events**.
9.  For **Creation method**, choose
    **Use schema**.
10. For **Event pattern**, do the following:
    1. For **Schema type**, choose **Select schema from Schema registry**.
    2. For **Schema registry**, choose **aws.events** from the drop-down list.
    3. For **Schema**, choose **aws.ec2@EC2InstanceStateChangeNotification** from the drop-down list.

    EventBridge displays the event schema under **Models**.

    EventBridge displays a red asterisk next to any properties that are required _for the event_, not for the event pattern. 4. In **Models**, set the following event filter properties:

        1. Select **+ Edit** next to the **state** property.


        Leave **Relationship** empty. For **Value**, enter `running`. Choose **Set**.
        2. Select **+ Edit** next to the **source** property.


        Leave **Relationship** empty. For **Value**, enter `aws.ec2`. Choose **Set**.
        3. Select **+ Edit** next to the **detail-type** property.


        Leave **Relationship** empty. For **Value**, enter `EC2 Instance State-change Notification`. Choose **Set**.

    5. To view the event pattern you've constructed, choose **Generate event pattern in JSON**

    EventBridge displays the event pattern in JSON:

    ```
    {
      "detail": {
        "state": ["running"]
      },
      "detail-type": ["EC2 Instance State-change Notification"],
      "source": ["aws.ec2"]
    }
    ```

11. Choose **Next**.
12. For **Target types**, choose **AWS service**.
13. For **Select a target**, choose **Kinesis
    stream** from the drop-down list.
14. For **Stream**, select the Kinesis stream that you created
    in the **Step 1: Create an Amazon Kinesis stream** section. In this example, select `test`.
15. For **Execution role**, choose **Create a new for role for this specific resource**.
16. Choose **Next**.
17. Choose **Next**.
18. Review the details of the rule and choose **Create rule**.

## Step 3: Test the rule

To test your rule, stop an Amazon EC2 instance. Wait a few minutes for the instance to
stop, and then check your CloudWatch metrics to verify that your function ran.

###### To test your rule by stopping an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Launch an instance. For more information, see [Launch Your
   Instance](../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md "../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md") in the _Amazon EC2 User Guide_.
3. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
4. In the navigation pane, choose **Rules**.

Choose the name of the rule that you created and choose **Metrics for
the rule**. 5. (Optional) When you're finished, terminate the instance. For more information,
see [Terminate Your
Instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in the _Amazon EC2 User Guide_.

## Step 4: Verify that the event was sent

You can use the AWS CLI to get the record from the stream to verify that the event was
sent.

###### To get the record

1. To start reading from your Kinesis stream, at a command prompt, use the
   `get-shard-iterator`
   command.

```
`aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON --stream-name `test``
```

The following is example output.

```
{
    "ShardIterator": "AAAAAAAAAAHSywljv0zEgPX4NyKdZ5wryMzP9yALs8NeKbUjp1IxtZs1Sp+KEd9I6AJ9ZG4lNR1EMi+9Md/nHvtLyxpfhEzYvkTZ4D9DQVz/mBYWRO6OTZRKnW9gd+efGN2aHFdkH1rJl4BL9Wyrk+ghYG22D2T1Da2EyNSH1+LAbK33gQweTJADBdyMwlo5r6PqcP2dzhg="
}
```

2. To get the record, use the following `get-records` command. Use the
   shard iterator from the output in the previous step.

```
`aws kinesis get-records --shard-iterator `AAAAAAAAAAHSywljv0zEgPX4NyKdZ5wryMzP9yALs8NeKbUjp1IxtZs1Sp+KEd9I6AJ9ZG4lNR1EMi+9Md/nHvtLyxpfhEzYvkTZ4D9DQVz/mBYWRO6OTZRKnW9gd+efGN2aHFdkH1rJl4BL9Wyrk+ghYG22D2T1Da2EyNSH1+LAbK33gQweTJADBdyMwlo5r6PqcP2dzhg=``
```

If the command is successful, it requests records from your stream for the
specified shard. You can receive zero or more records. Any records returned
might not represent all records in your stream. If you don't receive the data
that you expect, keep calling `get-records`. 3. Records in Kinesis are encoded in Base64. Use a Base64 decoder to decode the data
so that you can verify that it's the event that was sent to the stream in JSON
form.

## Step 5: Clean up your resources

You can now delete the resources that you created for this tutorial, unless you want to retain them. By deleting AWS resources that you are no longer using, you prevent unnecessary charges to your AWS account.

###### To delete the EventBridge rule(s)

1. Open the [Rules page](https://console.aws.amazon.com/events/home#/rules "https://console.aws.amazon.com/events/home#/rules") of the EventBridge console.
2. Select the rule(s) that you created.
3. Choose **Delete**.
4. Choose **Delete**.

###### To delete the Kinesis stream(s)

1. Open the [Data streams page](https://console.aws.amazon.com/kinesis/home#/streams/list "https://console.aws.amazon.com/kinesis/home#/streams/list") of the Kinesis console.
2. Select the stream(s) that you created.
3. Choose **Actions**, **Delete**.
4. Enter **delete** in the fiekd and choose **Delete**.
