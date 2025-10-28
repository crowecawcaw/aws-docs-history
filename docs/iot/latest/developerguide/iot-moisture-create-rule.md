# Step 4: Create an AWS IoT rule to send an

email

An AWS IoT rule defines a query and one or more actions to take when a message is
received from a device. The AWS IoT rules engine listens for messages sent by devices
and uses the data in the messages to determine if some action should be taken. For
more information, see [Rules for AWS IoT](iot-rules.md "iot-rules.md").

In this tutorial, your Raspberry Pi publishes messages on
`aws/things/RaspberryPi/shadow/update`. This is an internal MQTT
topic used by devices and the Thing Shadow service. The Raspberry Pi publishes
messages that have the following form:

```
{
    "reported": {
        "moisture" : `moisture-reading`,
        "temp" : `temperature-reading`
    }
}
```

You create a query that extracts the moisture and temperature data from the
incoming message. You also create an Amazon SNS action that takes the data and sends it
to Amazon SNS topic subscribers if the moisture reading is below a threshold
value.

###### Create an Amazon SNS rule

1. In the [AWS IoT
   console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home"), choose **Message routing** and then
   choose **Rules**. If a **You don't have any rules
   yet** dialog box appears, choose **Create a
   rule**. Otherwise, choose **Create
   rule**.
2. In the **Rule properties** page, enter a **Rule
   name** such as `MoistureSensorRule`, and
   provide a short **Rule description** such as
   `Sends an alert when soil moisture level readings are too
low`.
3. Choose **Next** and configure your SQL statement.
   Choose **SQL version** as **2016-03-23**,
   and enter the following AWS IoT SQL query statement:

```

SELECT * FROM '$aws/things/RaspberryPi/shadow/update/accepted' WHERE state.reported.moisture < 400

```

This statement triggers the rule action when the `moisture`
reading is less than `400`.

###### Note

You might have to use a different value. After you have the code
running on your Raspberry Pi, you can see the values that you get from
your sensor by touching the sensor, placing it in water, or placing it
in a planter. 4. Choose **Next** and attach rule actions. For
**Action 1**, choose **Simple Notification
Service**. The description for this rule action is
**Send a message as an SNS push notification**. 5. For **SNS topic**, choose the topic that you created in
[Step 3: Create an Amazon SNS topic and
subscription](iot-moisture-create-sns-topic.md "iot-moisture-create-sns-topic.md"),
**MoistureSensorTopic**, and leave the
**Message format** as **RAW**. For
**IAM role**, choose **Create a new
role**. Enter a name for the role, for example,
`LowMoistureTopicRole`, and then choose
**Create role**. 6. Choose **Next** to review and then choose
**Create** to create the rule.
