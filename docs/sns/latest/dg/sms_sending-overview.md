# Sending SMS messages using Amazon SNS

This section describes how to send SMS messages using Amazon SNS, including publishing to a
topic, subscribing phone numbers to topics, setting attributes on messages, and publishing
directly to mobile phones.

## Publishing SMS messages to an Amazon SNS topic

You can publish a single SMS message to many phone numbers at once by subscribing those
phone numbers to an Amazon SNS topic. An SNS topic is a communication channel to which you can
add subscribers and then publish messages to all of those subscribers. A subscriber receives
all messages published to the topic until you cancel the subscription, or until the
subscriber opts out of receiving SMS messages from your AWS account.

### Sending a message to a topic using the

AWS console

###### To create a topic

Complete the following steps if you don't already have a topic to which you want
to send SMS messages.

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the console menu, choose a [region that supports SMS
   messaging](../../../general/latest/gr/end-user-messaging.md "../../../general/latest/gr/end-user-messaging.md").
3. In the navigation pane, choose **Topics**.
4. On the **Topics** page, choose **Create
   topic**.
5. On the **Create topic** page, under
   **Details**, do the following:
   1. For **Type**, choose
      **Standard**.
   2. For **Name**, enter a topic name.
   3. (Optional) For **Display name**, enter a custom
      prefix for your SMS messages. When you send a message to the topic,
      Amazon SNS prepends the display name followed by a right angle bracket (>)
      and a space. Display names are not case sensitive, and Amazon SNS converts
      display names to uppercase characters. For example, if the display name
      of a topic is `MyTopic` and the message is `Hello
World!`, the message appears as:

   ```
   MYTOPIC> Hello World!
   ```

6. Choose **Create topic**. The topic's name and Amazon Resource
   Name (ARN) appear on the **Topics** page.

###### To create an SMS subscription

You can use subscriptions to send an SMS message to multiple recipients by
publishing the message only once to your topic.

###### Note

When you start using Amazon SNS to send SMS messages, your AWS account is in the
_SMS sandbox_. The SMS sandbox provides a safe
environment for you to try Amazon SNS features without risking your reputation as an
SMS sender. While your account is in the SMS sandbox, you can use all of the
features of Amazon SNS, but you can send SMS messages only to verified destination
phone numbers. For more information, see [Using the Amazon SNS SMS sandbox](sns-sms-sandbox.md "sns-sms-sandbox.md").

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the navigation pane, choose **Subscriptions**.
3. On the **Subscriptions** page, choose **Create
   subscription**.
4. On the **Create subscription** page, under
   **Details**, do the following:
   1. For **Topic ARN**, enter or choose the Amazon
      Resource Name (ARN) of the topic to which you want to send SMS
      messages.
   2. For **Protocol**, choose
      **SMS**.
   3. For **Endpoint**, enter the phone number that you
      want to subscribe to your topic.

5. Choose **Create subscription**. The subscription information
   appears on the **Subscriptions** page.

To add more phone numbers, repeat these steps. You can also add other types of
subscriptions, such as email.

###### To send a message

When you publish a message to a topic, Amazon SNS attempts to deliver that message to
every phone number that is subscribed to the topic.

1. In the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home"), on the
   **Topics** page, choose the name of the topic to which you
   want to send SMS messages.
2. On the topic details page, choose **Publish message**.
3. On the **Publish message to topic** page, under
   **Message details**, do the following:
   1. For **Subject**, keep the field blank unless your
      topic contains email subscriptions and you want to publish to both email
      and SMS subscriptions. Amazon SNS uses the **Subject** that
      you enter as the email subject line.
   2. (Optional) For **Time to Live (TTL)**, enter a number
      of seconds that Amazon SNS has to send your SMS message to any mobile
      application endpoint subscribers.

4. Under **Message body**, do the following:
   1. For **Message structure**, choose **Identical
      payload for all delivery protocols** to send the same
      message to all protocol types subscribed to your topic. Or, choose
      **Custom payload for each delivery protocol** to
      customize the message for subscribers of different protocol types. For
      example, you can enter a default message for phone number subscribers
      and a custom message for email subscribers.
   2. For **Message body to send to the endpoint**, enter
      your message, or your custom messages per delivery protocol.

   If your topic has a display name, Amazon SNS adds it to the message, which
   increases the message length. The display name length is the number of
   characters in the name plus two characters for the right angle bracket
   (>) and the space that Amazon SNS adds.

   For information about the size quotas for SMS messages, see [Publishing SMS messages to a mobile phone using
   Amazon SNS](#sms_publish-to-phone "#sms_publish-to-phone").

5. (Optional) For **Message attributes**, add message metadata
   such as timestamps, signatures, and IDs.
6. Choose **Publish message**. Amazon SNS sends the SMS message and
   displays a success message.

### Sending a message to a topic using the AWS

SDKs

To use an AWS SDK, you must configure it with your credentials. For more
information, see [The shared config and credentials
files](../../../sdkref/latest/guide/creds-config-files.md "../../../sdkref/latest/guide/creds-config-files.md") in the _AWS SDKs and Tools Reference Guide_.

The following code example shows how to:

- Create an Amazon SNS topic.
- Subscribe phone numbers to the topic.
- Publish SMS messages to the topic so that all subscribed phone numbers receive the message at once.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples").

Create a topic and return its ARN.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.CreateTopicRequest;
import software.amazon.awssdk.services.sns.model.CreateTopicResponse;
import software.amazon.awssdk.services.sns.model.SnsException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class CreateTopic {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <topicName>

                Where:
                   topicName - The name of the topic to create (for example, mytopic).

                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String topicName = args[0];
        System.out.println("Creating a topic with name: " + topicName);
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();

        String arnVal = createSNSTopic(snsClient, topicName);
        System.out.println("The topic ARN is" + arnVal);
        snsClient.close();
    }

    public static String createSNSTopic(SnsClient snsClient, String topicName) {
        CreateTopicResponse result;
        try {
            CreateTopicRequest request = CreateTopicRequest.builder()
                    .name(topicName)
                    .build();

            result = snsClient.createTopic(request);
            return result.topicArn();

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return "";
    }
}


```

Subscribe an endpoint to a topic.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.SnsException;
import software.amazon.awssdk.services.sns.model.SubscribeRequest;
import software.amazon.awssdk.services.sns.model.SubscribeResponse;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class SubscribeTextSMS {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <topicArn> <phoneNumber>

                Where:
                   topicArn - The ARN of the topic to subscribe.
                   phoneNumber - A mobile phone number that receives notifications (for example, +1XXX5550100).
                """;

        if (args.length < 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String topicArn = args[0];
        String phoneNumber = args[1];
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();

        subTextSNS(snsClient, topicArn, phoneNumber);
        snsClient.close();
    }

    public static void subTextSNS(SnsClient snsClient, String topicArn, String phoneNumber) {
        try {
            SubscribeRequest request = SubscribeRequest.builder()
                    .protocol("sms")
                    .endpoint(phoneNumber)
                    .returnSubscriptionArn(true)
                    .topicArn(topicArn)
                    .build();

            SubscribeResponse result = snsClient.subscribe(request);
            System.out.println("Subscription ARN: " + result.subscriptionArn() + "\n\n Status is "
                    + result.sdkHttpResponse().statusCode());

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

Set attributes on the message, such as the ID of the sender, the maximum price, and its type.
Message attributes are optional.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.SetSmsAttributesRequest;
import software.amazon.awssdk.services.sns.model.SetSmsAttributesResponse;
import software.amazon.awssdk.services.sns.model.SnsException;
import java.util.HashMap;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class SetSMSAttributes {
    public static void main(String[] args) {
        HashMap<String, String> attributes = new HashMap<>(1);
        attributes.put("DefaultSMSType", "Transactional");
        attributes.put("UsageReportS3Bucket", "janbucket");

        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();
        setSNSAttributes(snsClient, attributes);
        snsClient.close();
    }

    public static void setSNSAttributes(SnsClient snsClient, HashMap<String, String> attributes) {
        try {
            SetSmsAttributesRequest request = SetSmsAttributesRequest.builder()
                    .attributes(attributes)
                    .build();

            SetSmsAttributesResponse result = snsClient.setSMSAttributes(request);
            System.out.println("Set default Attributes to " + attributes + ". Status was "
                    + result.sdkHttpResponse().statusCode());

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

Publish a message to a topic. The message is sent to every subscriber.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.PublishRequest;
import software.amazon.awssdk.services.sns.model.PublishResponse;
import software.amazon.awssdk.services.sns.model.SnsException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class PublishTextSMS {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <message> <phoneNumber>

                Where:
                   message - The message text to send.
                   phoneNumber - The mobile phone number to which a message is sent (for example, +1XXX5550100).\s
                """;

        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String message = args[0];
        String phoneNumber = args[1];
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();
        pubTextSMS(snsClient, message, phoneNumber);
        snsClient.close();
    }

    public static void pubTextSMS(SnsClient snsClient, String message, String phoneNumber) {
        try {
            PublishRequest request = PublishRequest.builder()
                    .message(message)
                    .phoneNumber(phoneNumber)
                    .build();

            PublishResponse result = snsClient.publish(request);
            System.out
                    .println(result.messageId() + " Message sent. Status was " + result.sdkHttpResponse().statusCode());

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

## Publishing SMS messages to a mobile phone using

Amazon SNS

You can use Amazon SNS to send SMS messages directly to a mobile phone without subscribing the
phone number to an Amazon SNS topic.

###### Note

Subscribing phone numbers to a topic is useful if you want to send one message to
multiple phone numbers at once. For instructions on publishing an SMS message to a
topic, see [Publishing SMS messages to an Amazon SNS topic](#sms_publish-to-topic "#sms_publish-to-topic").

When you send a message, you can control whether the message is optimized for cost or
reliable delivery. You can also specify a [sender ID or origination number](channels-sms-originating-identities.md "channels-sms-originating-identities.md"). If
you send the message programmatically using the Amazon SNS API or the AWS SDKs, you can specify
a maximum price for the message delivery.

Each SMS message can contain up to 140 bytes, and the character quota depends on the
encoding scheme. For example, an SMS message can contain:

- 160 GSM characters
- 140 ASCII characters
- 70 UCS-2 characters

If you publish a message that exceeds the size quota, Amazon SNS sends it as multiple messages,
each fitting within the size quota. Messages are not cut off in the middle of a word, but
instead on whole-word boundaries. The total size quota for a single SMS publish action is
1,600 bytes.

When you send an SMS message, you specify the phone number using the E.164 format, a
standard phone numbering structure used for international telecommunication. Phone numbers
that follow this format can have a maximum of 15 digits along with the prefix of a plus sign
(+) and the country code. For example, a US phone number in E.164 format appears as
+1XXX5550100.

### Sending a message (console)

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the console menu, choose a [region that supports SMS
   messaging](../../../general/latest/gr/end-user-messaging.md "../../../general/latest/gr/end-user-messaging.md").
3. In the navigation pane, choose **Text messaging
   (SMS)**.
4. On the **Mobile text messaging (SMS)** page, choose
   **Publish text message**.
5. On the **Publish SMS message** page, for **Message
   type**, choose one of the following:
   - **Promotional** – Non-critical messages, such
     as marketing messages.
   - **Transactional** – Critical messages that
     support customer transactions, such as one-time passcodes for
     multi-factor authentication.

###### Note

This message-level setting overrides your account-level default message
type. You can set an account-level default message type from the
**Text messaging preferences** section of the
**Mobile text messaging (SMS)** page.

For pricing information for promotional and transactional messages, see [Worldwide SMS Pricing](https://aws.amazon.com/sns/sms-pricing/ "https://aws.amazon.com/sns/sms-pricing/"). 6. For **Destination phone number**, enter the phone number to
which you want to send the message. 7. For **Message**, enter the message to send. 8. (Optional) Under **Origination identities**, specify how to
identify yourself to your recipients:

    * To specify a **Sender ID**, type a custom ID that
     contains 3-11 alphanumeric characters, including at least one letter and
     no spaces. The sender ID is displayed as the message sender on the
     receiving device. For example, you can use your business brand to make
     the message source easier to recognize.


    Support for sender IDs varies by country and/or region. For example,
     messages delivered to U.S. phone numbers will not display the sender ID.
     For the countries and regions that support sender IDs, see [Supported countries and regions for SMS messaging with
     AWS End User Messaging SMS](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md") in the *AWS End User Messaging SMS User
     Guide*.


    If you do not specify a sender ID, one of the following is displayed
     as the originating identity:




    	+ In countries that support long codes, the long code is
    	 shown.
    	+ In countries where only sender IDs are supported,
    	 *NOTICE* is shown.
    This message-level sender ID overrides your default sender ID, which
     you set on the **Text messaging preferences**
     page.
    * To specify an **Origination number**, enter a string
     of 5-14 numbers to display as the sender's phone number on the
     receiver's device. This string must match an origination number that is
     configured in your AWS account for the destination country. The
     origination number can be a 10DLC number, toll-free number,
     person-to-person long code, or short codes. For more information, see
     [Origination identities for Amazon SNS SMS
     messages](channels-sms-originating-identities.md "channels-sms-originating-identities.md").


    If you don't specify an origination number, Amazon SNS selects an
     origination number to use for the SMS text message, based on your
     AWS account configuration.

9.  If you're sending SMS messages to recipients in India, expand
    **Country-specific attributes**, and specify the following
    attributes:

        * **Entity ID** – The entity ID or principal
         entity (PE) ID for sending SMS messages to recipients in India. This ID
         is a unique string of 1–50 characters that the Telecom Regulatory
         Authority of India (TRAI) provides to identify the entity that you
         registered with the TRAI.
        * **Template ID** – The template ID for sending
         SMS messages to recipients in India. This ID is a unique, TRAI-provided
         string of 1–50 characters that identifies the template that you
         registered with the TRAI. The template ID must be associated with the
         sender ID that you specified for the message.

    For more information on sending SMS messages to recipients in India, [India
    sender ID registration process](../../../sms-voice/latest/userguide/registrations-sms-senderid-india.md "../../../sms-voice/latest/userguide/registrations-sms-senderid-india.md") in the _AWS End User Messaging SMS User
    Guide_.

10. Choose **Publish message**.

###### Tip

To send SMS messages from an origination number, you can also choose
**Origination numbers** in the Amazon SNS console navigation panel.
Choose an origination number that includes **SMS** in the
**Capabilities** column, and then choose **Publish text
message**.

### Sending a message (AWS SDKs)

To send an SMS message using one of the AWS SDKs, use the API operation in that SDK
that corresponds to the `Publish` request in the Amazon SNS API. With this
request, you can send an SMS message directly to a phone number. You can also use the
`MessageAttributes` parameter to set values for the following attribute
names:

**`AWS.SNS.SMS.SenderID`**

A custom ID that contains 3–11 alphanumeric characters or hyphen
(-) characters, including at least one letter and no spaces. The sender ID
appears as the message sender on the receiving device. For example, you can
use your business brand to help make the message source easier to
recognize.

Support for sender IDs varies by country or region. For example, messages
delivered to US phone numbers don't display the sender ID. For a list of the
countries or regions that support sender IDs, see [Supported countries and regions for SMS messaging with AWS End User Messaging SMS](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md")
in the _AWS End User Messaging SMS User Guide_.

If you don't specify a sender ID, a [long code](../../../sms-voice/latest/userguide/phone-numbers-request-long-code.md "../../../sms-voice/latest/userguide/phone-numbers-request-long-code.md") appears as the sender ID in supported countries or
regions. For countries or regions that require an alphabetic sender ID,
_NOTICE_ appears as the sender ID.

This message-level attribute overrides the account-level attribute
`DefaultSenderID`, which you can set using the
`SetSMSAttributes` request.

**`AWS.MM.SMS.OriginationNumber`**

A custom string of 5–14 numbers, which can include an optional
leading plus sign (`+`). This string of numbers appears as the
sender's phone number on the receiving device. The string must match an
origination number that's configured in your AWS account for the
destination country. The origination number can be a 10DLC number, toll-free
number, person-to-person (P2P) long code, or short code. For more
information, see [Phone
numbers](../../../sms-voice/latest/userguide/phone-numbers.md "../../../sms-voice/latest/userguide/phone-numbers.md") in the _AWS End User Messaging SMS User Guide_.

If you don't specify an origination number, Amazon SNS chooses an origination
number based on your AWS account configuration.

**`AWS.SNS.SMS.MaxPrice`**

The maximum price in USD that you're willing to spend to send the SMS
message. If Amazon SNS determines that sending the message would incur a cost
that exceeds your maximum price, it doesn't send the message.

This attribute has no effect if your month-to-date SMS costs have already
exceeded the quota set for the `MonthlySpendLimit` attribute. You
can set the `MonthlySpendLimit` attribute using the
`SetSMSAttributes` request.

If you're sending the message to an Amazon SNS topic, the maximum price applies
to each message delivery to each phone number that is subscribed to the
topic.

**`AWS.SNS.SMS.SMSType`**

The type of message that you're sending:

- **`Promotional`**
  (default) – Non-critical messages, such as marketing
  messages.
- **`Transactional`**
  – Critical messages that support customer transactions, such
  as one-time passcodes for multi-factor authentication.

This message-level attribute overrides the account-level attribute
`DefaultSMSType`, which you can set using the
`SetSMSAttributes` request.

**`AWS.MM.SMS.EntityId`**

This attribute is required only for sending SMS messages to recipients in
India.

This is your entity ID or principal entity (PE) ID for sending SMS
messages to recipients in India. This ID is a unique string of 1–50
characters that the Telecom Regulatory Authority of India (TRAI) provides to
identify the entity that you registered with the TRAI.

**`AWS.MM.SMS.TemplateId`**

This attribute is required only for sending SMS messages to recipients in
India.

This is your template for sending SMS messages to recipients in India.
This ID is a unique, TRAI-provided string of 1–50 characters that
identifies the template that you registered with the TRAI. The template ID
must be associated with the sender ID that you specified for the
message.

#### Sending a message

The following code examples show how to publish SMS messages using Amazon SNS.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SNS#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SNS#code-examples").

```
namespace SNSMessageExample
{
    using System;
    using System.Threading.Tasks;
    using Amazon;
    using Amazon.SimpleNotificationService;
    using Amazon.SimpleNotificationService.Model;

    public class SNSMessage
    {
        private AmazonSimpleNotificationServiceClient snsClient;

        /// <summary>
        /// Initializes a new instance of the <see cref="SNSMessage"/> class.
        /// Constructs a new SNSMessage object initializing the Amazon Simple
        /// Notification Service (Amazon SNS) client using the supplied
        /// Region endpoint.
        /// </summary>
        /// <param name="regionEndpoint">The Amazon Region endpoint to use in
        /// sending test messages with this object.</param>
        public SNSMessage(RegionEndpoint regionEndpoint)
        {
            snsClient = new AmazonSimpleNotificationServiceClient(regionEndpoint);
        }

        /// <summary>
        /// Sends the SMS message passed in the text parameter to the phone number
        /// in phoneNum.
        /// </summary>
        /// <param name="phoneNum">The ten-digit phone number to which the text
        /// message will be sent.</param>
        /// <param name="text">The text of the message to send.</param>
        /// <returns>Async task.</returns>
        public async Task SendTextMessageAsync(string phoneNum, string text)
        {
            if (string.IsNullOrEmpty(phoneNum) || string.IsNullOrEmpty(text))
            {
                return;
            }

            // Now actually send the message.
            var request = new PublishRequest
            {
                Message = text,
                PhoneNumber = phoneNum,
            };

            try
            {
                var response = await snsClient.PublishAsync(request);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error sending message: {ex}");
            }
        }
    }
}



```

- For API details, see
  [Publish](../../../goto/DotNetSDKV3/sns-2010-03-31/Publish.md "../../../goto/DotNetSDKV3/sns-2010-03-31/Publish.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples").

```
/**
 * Publish SMS: use Amazon Simple Notification Service (Amazon SNS) to send an SMS text message to a phone number.
 * Note: This requires additional AWS configuration prior to running example.
 *
 *  NOTE: When you start using Amazon SNS to send SMS messages, your AWS account is in the SMS sandbox and you can only
 *  use verified destination phone numbers. See https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html.
 *  NOTE: If destination is in the US, you also have an additional restriction that you have use a dedicated
 *  origination ID (phone number). You can request an origination number using Amazon Pinpoint for a fee.
 *  See https://aws.amazon.com/blogs/compute/provisioning-and-using-10dlc-origination-numbers-with-amazon-sns/
 *  for more information.
 *
 *  <phone_number_value> input parameter uses E.164 format.
 *  For example, in United States, this input value should be of the form: +12223334444
 */

//! Send an SMS text message to a phone number.
/*!
  \param message: The message to publish.
  \param phoneNumber: The phone number of the recipient in E.164 format.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::SNS::publishSms(const Aws::String &message,
                             const Aws::String &phoneNumber,
                             const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::SNS::SNSClient snsClient(clientConfiguration);

    Aws::SNS::Model::PublishRequest request;
    request.SetMessage(message);
    request.SetPhoneNumber(phoneNumber);

    const Aws::SNS::Model::PublishOutcome outcome = snsClient.Publish(request);

    if (outcome.IsSuccess()) {
        std::cout << "Message published successfully with message id, '"
                  << outcome.GetResult().GetMessageId() << "'."
                  << std::endl;
    }
    else {
        std::cerr << "Error while publishing message "
                  << outcome.GetError().GetMessage()
                  << std::endl;
    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [Publish](../../../goto/SdkForCpp/sns-2010-03-31/Publish.md "../../../goto/SdkForCpp/sns-2010-03-31/Publish.md")
  in _AWS SDK for C++ API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.PublishRequest;
import software.amazon.awssdk.services.sns.model.PublishResponse;
import software.amazon.awssdk.services.sns.model.SnsException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class PublishTextSMS {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <message> <phoneNumber>

                Where:
                   message - The message text to send.
                   phoneNumber - The mobile phone number to which a message is sent (for example, +1XXX5550100).\s
                """;

        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String message = args[0];
        String phoneNumber = args[1];
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();
        pubTextSMS(snsClient, message, phoneNumber);
        snsClient.close();
    }

    public static void pubTextSMS(SnsClient snsClient, String message, String phoneNumber) {
        try {
            PublishRequest request = PublishRequest.builder()
                    .message(message)
                    .phoneNumber(phoneNumber)
                    .build();

            PublishResponse result = snsClient.publish(request);
            System.out
                    .println(result.messageId() + " Message sent. Status was " + result.sdkHttpResponse().statusCode());

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [Publish](../../../goto/SdkForJavaV2/sns-2010-03-31/Publish.md "../../../goto/SdkForJavaV2/sns-2010-03-31/Publish.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples").

```
suspend fun pubTextSMS(
    messageVal: String?,
    phoneNumberVal: String?,
) {
    val request =
        PublishRequest {
            message = messageVal
            phoneNumber = phoneNumberVal
        }

    SnsClient.fromEnvironment { region = "us-east-1" }.use { snsClient ->
        val result = snsClient.publish(request)
        println("${result.messageId} message sent.")
    }
}


```

- For API details, see
  [Publish](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/sns#code-examples").

```
require 'vendor/autoload.php';

use Aws\Exception\AwsException;
use Aws\Sns\SnsClient;


/**
 * Sends a text message (SMS message) directly to a phone number using Amazon SNS.
 *
 * This code expects that you have AWS credentials set up per:
 * https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html
 */

$SnSclient = new SnsClient([
    'profile' => 'default',
    'region' => 'us-east-1',
    'version' => '2010-03-31'
]);

$message = 'This message is sent from a Amazon SNS code sample.';
$phone = '+1XXX5550100';

try {
    $result = $SnSclient->publish([
        'Message' => $message,
        'PhoneNumber' => $phone,
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}



```

- For more information, see [AWS SDK for PHP Developer Guide](../../../sdk-for-php/v3/developer-guide/sns-examples-sending-sms.md#publish-to-a-text-message-sms-message "../../../sdk-for-php/v3/developer-guide/sns-examples-sending-sms.md#publish-to-a-text-message-sms-message").
- For API details, see
  [Publish](../../../goto/SdkForPHPV3/sns-2010-03-31/Publish.md "../../../goto/SdkForPHPV3/sns-2010-03-31/Publish.md")
  in _AWS SDK for PHP API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sns#code-examples").

```
class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self, sns_resource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource


    def publish_text_message(self, phone_number, message):
        """
        Publishes a text message directly to a phone number without need for a
        subscription.

        :param phone_number: The phone number that receives the message. This must be
                             in E.164 format. For example, a United States phone
                             number might be +12065550101.
        :param message: The message to send.
        :return: The ID of the message.
        """
        try:
            response = self.sns_resource.meta.client.publish(
                PhoneNumber=phone_number, Message=message
            )
            message_id = response["MessageId"]
            logger.info("Published message to %s.", phone_number)
        except ClientError:
            logger.exception("Couldn't publish message to %s.", phone_number)
            raise
        else:
            return message_id



```

- For API details, see
  [Publish](../../../goto/boto3/sns-2010-03-31/Publish.md "../../../goto/boto3/sns-2010-03-31/Publish.md")
  in _AWS SDK for Python (Boto3) API Reference_.
