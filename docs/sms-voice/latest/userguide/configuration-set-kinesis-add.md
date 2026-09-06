

# Create an Amazon Data Firehose event destination in AWS End User Messaging SMS
<a name="configuration-set-kinesis-add"></a>

Before you can create a Amazon Data Firehose event destination, you must first create a Amazon Data Firehose stream. For more inforation about creating log groups, see [Creating an Amazon Data Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) in the *Amazon Data Firehose Developer Guide*.

You have to create an IAM role that allows the AWS End User Messaging SMS and Voice v2 API to send data to the stream. The following section contains information about the requirements for this role.

You also have already setup a configuration set to associate the event destinations with, see [Configuration sets in AWS End User Messaging SMS](configuration-sets.md).

------
#### [ Create Amazon Data Firehose event destination (Console) ]

To create an Amazon Data Firehose event destination using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Configuration sets**.

1. On the **Configuration sets** page, choose the configuration set to add an event destination to. 

1. On the **Configuration set details** page, choose **Add destination event**.

1. Under the **Event details** section, enter a friendly name for **Event destination name**.

1. From the **Destination type** dropdown choose Amazon Data Firehose.

1. For **IAM role arn** enter the ARN of the IAM role. For more information on the IAM role arn, see [IAM policy for Amazon Data Firehose](configuration-sets-kinesis-creating-role.md).

1. For **Delivery stream arn** enter the ARN of the Amazon Data Firehose log group to deliver the events to. 

1. Turn on **Event publishing**.

1. Under **Event types**, choose:
   + **All SMS events (Recommended)** – Choose this option to send all SMS events listed in [Event types](configuration-sets-event-types.md) to Amazon Data Firehose.
   + **Custom SMS events** – Choose specific SMS events to send to Amazon Data Firehose. To edit the list of events choose **Edit SMS event selection**. On **Edit SMS event selection** check only the events you want to send to Amazon Data Firehose. Choose **Save selection**.
   + **All voice events (Recommended)** – Choose this option to send all voice events listed in [Event types](configuration-sets-event-types.md) to Amazon Data Firehose.
   + **Custom voice events** – Choose specific voice events to send to Amazon Data Firehose. To edit the list of events choose **Edit voice event selection**. On **Edit voice event selection** check only the events you want to send to Amazon Data Firehose. Choose **Save selection**.
   + **All MMS events (Recommended)** – Choose this option to send all MMS events listed in [Event types](configuration-sets-event-types.md) to Amazon Data Firehose.
   + **Custom MMS events** – Choose t specific MMS events to send to Amazon Data Firehose. To edit the list of events choose **Edit MMS event selection**. On **Edit MMS event selection** check only the events you want to send to Amazon Data Firehose. Choose **Save selection**.

1. Choose **Create event**.

------
#### [ Create Amazon Data Firehose event destination (AWS CLI) ]

After you create the IAM role and the Amazon Data Firehose delivery stream, you can create the event destination.

You can use the [create-event-destination](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/create-event-destination.html) command to create an event destination.

```
$ aws pinpoint-sms-voice-v2 create-event-destination \
> --event-destination-name {{eventDestinationName}} \
> --configuration-set-name {{configurationSet}} \
> --matching-event-types {{eventTypes}} \
> --kinesis-firehose-destination IamRoleArn=arn:aws:iam::{{111122223333}}:role/{{AKFSMSRole}},DeliveryStreamArn=arn:aws:firehose:{{us-east-1}}:{{111122223333}}:deliverystream/{{MyDeliveryStream}}
```

In the preceding command, make the following changes:
+ Replace {{eventDestinationName}} with a name that describes the event destination.
+ Replace {{configurationSet}} with the name of the configuration set that you want to associate the event destination with.
+ Replace {{eventTypes}} with one or more of the event types listed in [Event types for SMS, MMS, and voice](configuration-sets-event-types.md).
+ Replace the value of `IamRoleArn` with the Amazon Resource Name (ARN) of an IAM role that has the policies described in [IAM policy for Amazon Data Firehose](configuration-sets-kinesis-creating-role.md).
+ Replace the value of `DeliveryStreamArn` with the ARN of the Amazon Data Firehose stream that you want to send events to. 

------