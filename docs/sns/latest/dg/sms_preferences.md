# Setting SMS messaging preferences in Amazon SNS

Use Amazon SNS to specify preferences for SMS messaging. For example, you can specify whether
to optimize deliveries for cost or reliability, your monthly spending limit, how deliveries
are logged, and whether to subscribe to daily SMS usage reports.

These preferences take effect for every SMS message that you send from your account, but
you can override some of them when you send an individual message. For more information, see
[Publishing SMS messages to a mobile phone using
Amazon SNS](sms_sending-overview.md#sms_publish-to-phone "sms_sending-overview.md#sms_publish-to-phone").

## Setting SMS messaging preferences using the

AWS Management Console

1.  Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2.  Choose a [region that supports SMS
    messaging](../../../general/latest/gr/end-user-messaging.md "../../../general/latest/gr/end-user-messaging.md").
3.  On the navigation panel, choose **Mobile** and then
    **Text messaging (SMS)**.
4.  On the **Mobile text messaging (SMS)** page, in the
    **Text messaging preferences** section, choose
    **Edit**.
5.  On the **Edit text messaging preferences** page, in the
    **Details** section, do the following:
    1.  For **Default message type**, choose one of the
        following:

            * **Promotional** – Non-critical
             messages (for example, marketing). Amazon SNS optimizes message
             delivery to incur the lowest cost.
            * **Transactional** (default) – Critical
             messages that support customer transactions, such as one-time
             passcodes for multi-factor authentication. Amazon SNS optimizes
             message delivery to achieve the highest reliability.

        For pricing information for promotional and transactional messages,
        see [Global SMS
        Pricing](https://aws.amazon.com/sns/sms-pricing/ "https://aws.amazon.com/sns/sms-pricing/").

    2.  (Optional) For **Account spend limit**, enter the
        amount (in USD) that you want to spend on SMS messages each calendar
        month.

    ###### Important

        * By default, the spend quota is set to 1.00 USD. If you
         want to raise the service quota, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-sns "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-sns").
        * If the amount set in the console exceeds your service
         quota, Amazon SNS stops publishing SMS messages.
        * Because Amazon SNS is a distributed system, it stops sending
         SMS messages within minutes of the spend quota being
         exceeded. During this interval, if you continue to send SMS
         messages, you might incur costs that exceed your
         quota.

6.  (Optional) For **Default sender ID**, enter a custom ID, such
    as your business brand, which is displayed as the sender of the receiving
    device.

###### Note

Support for sender IDs varies by country. 7. (Optional) Enter the name of the **Amazon S3 bucket name for usage
reports**.

###### Note

The Amazon S3 bucket policy must grant write access to Amazon SNS. 8. Choose **Save changes**.

## Setting preferences (AWS SDKs)

To set your SMS preferences using one of the AWS SDKs, use the action in that SDK
that corresponds to the `SetSMSAttributes` request in the Amazon SNS API. With
this request, you assign values to the different SMS attributes, such as your monthly
spend quota and your default SMS type (promotional or transactional). For all SMS
attributes, see [SetSMSAttributes](../api/API_SetSMSAttributes.md "../api/API_SetSMSAttributes.md") in the _Amazon Simple Notification Service API Reference_.

The following code examples show how to use `SetSMSAttributes`.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples").

How to use Amazon SNS to set the DefaultSMSType attribute.

```
//! Set the default settings for sending SMS messages.
/*!
  \param smsType: The type of SMS message that you will send by default.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::SNS::setSMSType(const Aws::String &smsType,
                             const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::SNS::SNSClient snsClient(clientConfiguration);

    Aws::SNS::Model::SetSMSAttributesRequest request;
    request.AddAttributes("DefaultSMSType", smsType);

    const Aws::SNS::Model::SetSMSAttributesOutcome outcome = snsClient.SetSMSAttributes(
            request);

    if (outcome.IsSuccess()) {
        std::cout << "SMS Type set successfully " << std::endl;
    }
    else {
        std::cerr << "Error while setting SMS Type: '"
                  << outcome.GetError().GetMessage()
                  << "'" << std::endl;
    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [SetSMSAttributes](../../../goto/SdkForCpp/sns-2010-03-31/SetSMSAttributes.md "../../../goto/SdkForCpp/sns-2010-03-31/SetSMSAttributes.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**To set SMS message attributes**

The following `set-sms-attributes` example sets the default sender ID for SMS messages to `MyName`.

```
`aws sns set-sms-attributes \
 --attributes `DefaultSenderID=MyName``

```

This command produces no output.

- For API details, see
  [SetSMSAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-sms-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-sms-attributes.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples").

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

- For API details, see
  [SetSMSAttributes](../../../goto/SdkForJavaV2/sns-2010-03-31/SetSMSAttributes.md "../../../goto/SdkForJavaV2/sns-2010-03-31/SetSMSAttributes.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/sns#code-examples").

Create the client in a separate module and export it.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});


```

Import the SDK and client modules and call the API.

```
import { SetSMSAttributesCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {"Transactional" | "Promotional"} defaultSmsType
 */
export const setSmsType = async (defaultSmsType = "Transactional") => {
  const response = await snsClient.send(
    new SetSMSAttributesCommand({
      attributes: {
        // Promotional – (Default) Noncritical messages, such as marketing messages.
        // Transactional – Critical messages that support customer transactions,
        // such as one-time passcodes for multi-factor authentication.
        DefaultSMSType: defaultSmsType,
      },
    }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '1885b977-2d7e-535e-8214-e44be727e265',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   }
  // }
  return response;
};


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v3/developer-guide/sns-examples-sending-sms.md#sending-sms-setattributes "../../../sdk-for-javascript/v3/developer-guide/sns-examples-sending-sms.md#sending-sms-setattributes").
- For API details, see
  [SetSMSAttributes](../../../AWSJavaScriptSDK/v3/latest/client/sns/command/SetSMSAttributesCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/sns/command/SetSMSAttributesCommand.md")
  in _AWS SDK for JavaScript API Reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/sns#code-examples").

```
$SnSclient = new SnsClient([
    'profile' => 'default',
    'region' => 'us-east-1',
    'version' => '2010-03-31'
]);

try {
    $result = $SnSclient->SetSMSAttributes([
        'attributes' => [
            'DefaultSMSType' => 'Transactional',
        ],
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}



```

- For more information, see [AWS SDK for PHP Developer Guide](../../../sdk-for-php/v3/developer-guide/sns-examples-sending-sms.md#set-sms-attributes "../../../sdk-for-php/v3/developer-guide/sns-examples-sending-sms.md#set-sms-attributes").
- For API details, see
  [SetSMSAttributes](../../../goto/SdkForPHPV3/sns-2010-03-31/SetSMSAttributes.md "../../../goto/SdkForPHPV3/sns-2010-03-31/SetSMSAttributes.md")
  in _AWS SDK for PHP API Reference_.

## Setting SMS messaging preferences for

country-specific delivery

You can manage and control your SMS traffic by sending messages only to specific
destination countries. This ensures that your messages are sent only to approved
countries, avoiding unwanted SMS charges. The following instructions use Amazon
Pinpoint's Protect configuration to specify the countries you want to allow or
block.

1. Open the AWS SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Overview**, in the
   **Quick start** section, choose **Create a protect
   configuration**.
3. Under **Protect configuration details**, enter a
   **business-friendly name** for your protect configuration (for
   example, Allow-Only-AU).
4. Under **SMS country rules**, select the
   **Region/Country** checkbox to block sending messages to all
   supported countries.
5. Deselect the checkboxes for the countries where you want to send messages. For
   example, to allow messages only to Australia, deselect the checkbox for
   **Australia**.
6. In the **Protect configuration associations** section, under
   **Association type**, select **Account
   default**. This will ensure that the AWS End User Messaging SMS Protect configuration
   affects all messages sent through Amazon SNS, [Amazon Cognito](../../../cognito/latest/developerguide/cognito-user-identity-pools.md "../../../cognito/latest/developerguide/cognito-user-identity-pools.md"), and the Amazon Pinpoint [`SendMessages`](../../../pinpoint/latest/developerguide/send-messages-sms.md "../../../pinpoint/latest/developerguide/send-messages-sms.md") API call.
7. Choose **Create protect configuration** to save your
   settings.

The following confirmation message is displayed:

```
Success Protect configuration protect-*abc0123456789* has been created.
```

8. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
9. [Publish a message](sns-publishing.md "sns-publishing.md") to
   one of the blocked countries, such as India.

The message will not be delivered. You can verify this in the delivery failure
logs using [CloudWatch](sms_stats_cloudwatch.md "sms_stats_cloudwatch.md"). Search for log group
**sns/region/AccountID/DirectPublishToPhoneNumber/Failure** for
a response similar to the following example:

```
{
"notification": {
"messageId": "bd59a509-XXXX-XXXX-82f8-fbdb8cb68217",
"timestamp": "YYYY-MM-DD XX:XX:XX.XXXX“
},
"delivery": {
"destination": "+91XXXXXXXXXX",
"smsType": "Transactional",
"providerResponse": "Cannot deliver message to the specified destination country",
"dwellTimeMs": 85
},
"status": "FAILURE"
}
```
