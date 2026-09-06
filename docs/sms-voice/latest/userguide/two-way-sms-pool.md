

# Set up two-way SMS messaging for a phone pool in AWS End User Messaging SMS
<a name="two-way-sms-pool"></a>

Use the AWS End User Messaging SMS console or AWS CLI to enable two way SMS for your phone pool.

------
#### [ Two-way SMS messaging (Console) ]

To enable two-way SMS using the AWS End User Messaging SMS console, follow these steps:

**Enable two-way SMS**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Phone pools**.

1. On the **Phone pools** page, choose a phone pool.

1. On the **Two-way SMS** tab, choose **Edit settings**.

1. On the **Edit settings** page turn on **Enable two-way message**.

1. For **Destination type**, choose either **Amazon SNS** or **Connect Customer**.
   + For Amazon SNS choose either **New Amazon SNS topic** or **Existing Amazon SNS topic** and then for **Two-way channel role**, choose either **Choose existing IAM role** or **Use Amazon SNS topic policies**.
     + **New Amazon SNS topic** – If you choose this option, AWS End User Messaging SMS creates a topic in your account. The topic is automatically created with all of the required permissions. For more information on Amazon SNS topics see [Configuring Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) in the *Amazon SNS developer guide*.
     + **Existing Amazon SNS topic** – If you choose this option, you must choose an existing Amazon SNS topic from the **Incoming messages destination** dropdown. 
     + For **Two-way channel role**, choose either:
       + **Choose existing IAM role** – Choose an existing IAM policy to apply to the Amazon SNS topic. For example Amazon SNS policies see [IAM policies for Amazon SNS topics](two-way-sms-iam-policy.md).
       + **Use Amazon SNS topic policies** – The Amazon SNS topic requires the appropriate Amazon SNS topic policy to grant access to AWS End User Messaging SMS. For example Amazon SNS policies, see [Topic policies for Amazon SNS topics](two-way-sms-iam-policy-auto.md).
   + For Connect Customer in **Two-way channel role**, choose **Choose existing IAM roles**. 
     + In the **Existing IAM roles** drop down choose an existing IAM role as the message destination. For example IAM policies, see [IAM policies for Connect Customer](two-way-connect-iam-policy.md) .

1. Choose **Save changes**.

------
#### [ Two-way SMS messaging (AWS CLI) ]

You can use the [update-pool](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/update-pool.html) command to enable two-way SMS.

At the command line, enter the following command:

```
$ aws pinpoint-sms-voice-v2 update-pool \
> --pool-id {{poolid}} \
> --two-way-channel-arn {{TwoWayARN}} \
> --two-way-channel-role {{TwoChannelWayRole}}
```

In the preceding command, make the following changes:
+ Replace {{poolid}} with the PhonePoolID or Amazon Resource Name (ARN) of the phone number. 
+ Replace {{TwoWayARN}} with the Amazon Resource Name (ARN) to receive the incoming SMS messages. For example Amazon SNS policies, see [Topic policies for Amazon SNS topics](two-way-sms-iam-policy-auto.md). To set Connect Customer as the inbound destination set {{TwoWayARN}} to `connect.{{region}}.amazonaws.com`. Replace {{region}} with the AWS Region the Connect Customer instance is hosted in.
+ Replace {{TwoChannelWayRole}} with the Amazon Resource Name (ARN) of the IAM role to use. For example SNS permission policies, see [IAM policies for Amazon SNS topics](two-way-sms-iam-policy.md) and for example Connect Customer policies, see [IAM policies for Connect Customer](two-way-connect-iam-policy.md). This parameter is only required if you choose to use IAM permission policies.

------