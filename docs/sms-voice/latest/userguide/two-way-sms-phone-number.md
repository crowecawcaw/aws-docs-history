# Set up two-way SMS messaging for a phone number in AWS End User Messaging SMS

AWS End User Messaging SMS includes support for two-way SMS. When you set up two-way SMS, you can receive incoming
messages from your customers. You can also use two-way messaging together with other AWS services, such as Lambda and Amazon Lex, to create interactive text messaging experiences.

When one of your customers sends a message to your phone number, the message body is sent to
an Amazon SNS topic or Amazon Connect instance for processing.

###### Note

- Two-way SMS is only available in certain countries and regions. For more information
  about two-way SMS support by country or region, see [SMS and MMS country capabilities and limitations](phone-numbers-sms-support-by-country.md "phone-numbers-sms-support-by-country.md").
- Amazon Connect for two-way SMS is available in the AWS Regions listed in [Chat messaging: SMS subtype](../../../connect/latest/adminguide/regions.md#chatmessaging_region "../../../connect/latest/adminguide/regions.md#chatmessaging_region") in the _Amazon Connect
  Administrator Guide_.
- Two-way MMS is not supported but your phone number can still receive incoming SMS messages in
  response to an outbound MMS message.

Two-way SMS messaging (Console)
To enable two-way SMS using the AWS End User Messaging SMS console, follow these steps:

###### Enable two-way SMS

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Phone numbers**.
3. On the **Phone numbers** page, choose a phone
   number.
4. On the **Two-way SMS** tab, choose the **Edit
   settings** button.
5. On the **Edit settings** page, choose
   **Enable two-way message**.
6. For **Destination type**, choose either
   **Amazon SNS** or **Amazon Connect**.
   - For Amazon SNS choose either **New Amazon SNS topic**
     or **Existing Amazon SNS topic** and then for
     **Two-way channel role**, choose either
     **Choose existing IAM role** or
     **Use Amazon SNS topic policies**.
     - **New Amazon SNS topic** – If you
       choose this option, AWS End User Messaging SMS creates a topic in your
       account. The topic is automatically created with all of
       the required permissions. For more information on Amazon SNS
       topics see [Configuring Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").
     - **Existing Amazon SNS topic** – If
       you choose this option, you must choose an existing
       Amazon SNS topic from the **Incoming messages
       destination** dropdown.
     - For **Two-way channel role**, choose
       either:
       - **Choose existing IAM role**
         – Choose an existing IAM policy to apply
         to the Amazon SNS topic. For example Amazon SNS policies see
         [IAM policies for Amazon SNS topics](two-way-sms-iam-policy.md "two-way-sms-iam-policy.md").
       - **Use Amazon SNS topic policies**
         – The Amazon SNS topic requires the appropriate
         Amazon SNS topic policy to grant access to AWS End User Messaging SMS. For
         example Amazon SNS policies, see [Topic policies for Amazon SNS topics](two-way-sms-iam-policy-auto.md "two-way-sms-iam-policy-auto.md").

   - For Amazon Connect, in **Two-way channel role**,
     choose **Choose existing IAM roles**.
     - In the **Existing IAM roles** drop
       down choose an existing IAM role as the message
       destination. For example IAM policies, see [IAM policies for
       Amazon Connect](two-way-connect-iam-policy.md "two-way-connect-iam-policy.md") .

7. Choose **Save changes**.
8. _(Optional)_ If you've chosen Amazon Connect as the
   **Destination type** then in the **Import
   Phone Number to Amazon Connect** window:
   1. For the **Incoming messages destination**
      dropdown choose the Amazon Connect instance that will receive incoming
      messages.
   2. Choose **Import Phone Number**.

Two-way SMS messaging (AWS CLI)
You can use the [update-phone-number](../../../cli/latest/reference/pinpoint-sms-voice-v2/update-phone-number.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/update-phone-number.md") command to enable two-way SMS.

At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 update-phone-number \
`>` --phone-number-id `PhoneNumber` \
`>` --two-way-enabled `True` \
`>` --two-way-channel-arn `TwoWayARN` \
`>` --two-way-channel-role `TwoChannelWayRole`
```

In the preceding command, make the following changes:

- Replace `PhoneNumber` with the PhoneNumberID
  or Amazon Resource Name (ARN) of the of the phone number.
- Replace `TwoWayARN` with the Amazon Resource
  Name (ARN) to receive the incoming SMS messages. For example Amazon SNS
  policies, see [Topic policies for Amazon SNS topics](two-way-sms-iam-policy-auto.md "two-way-sms-iam-policy-auto.md"). To set Amazon Connect
  as the inbound destination set `TwoWayARN` to
  `connect.`region`.amazonaws.com`.
  Replace `region` with the AWS Region the
  Amazon Connect instance is hosted in.
- Replace `TwoChannelWayRole` with the Amazon
  Resource Name (ARN) of the IAM role to use. For example SNS permission
  policies, see [IAM policies for Amazon SNS topics](two-way-sms-iam-policy.md "two-way-sms-iam-policy.md") and for example
  Amazon Connect policies, see [IAM policies for
  Amazon Connect](two-way-connect-iam-policy.md "two-way-connect-iam-policy.md"). This
  parameter is only required if you choose to use IAM permission
  policies.
