

# Setting SMS messaging preferences in Amazon SNS
<a name="sms_preferences"></a>

Use Amazon SNS to specify preferences for SMS messaging. For example, you can specify whether to optimize deliveries for cost or reliability, your monthly spending limit, how deliveries are logged, and whether to subscribe to daily SMS usage reports.

These preferences take effect for every SMS message that you send from your account, but you can override some of them when you send an individual message. For more information, see [Publishing SMS messages to a mobile phone using Amazon SNS](sms_sending-overview.md#sms_publish-to-phone).

## Setting SMS messaging preferences using the AWS Management Console
<a name="sms_preferences_console"></a>

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home).

1. Choose a [region that supports SMS messaging](https://docs.aws.amazon.com/general/latest/gr/end-user-messaging.html).

1. On the navigation panel, choose **Mobile** and then **Text messaging (SMS)**.

1. On the **Mobile text messaging (SMS)** page, in the **Text messaging preferences** section, choose **Edit**.

1. On the **Edit text messaging preferences** page, in the **Details** section, do the following:

   1. For **Default message type**, choose one of the following:
      + **Promotional** – Non-critical messages (for example, marketing). Amazon SNS optimizes message delivery to incur the lowest cost.
      + **Transactional** (default) – Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes message delivery to achieve the highest reliability.

      For pricing information for promotional and transactional messages, see [Global SMS Pricing](https://aws.amazon.com/sns/sms-pricing/).

   1. (Optional) For **Account spend limit**, enter the amount (in USD) that you want to spend on SMS messages each calendar month.
**Important**  
By default, the spend quota is set to 1.00 USD. If you want to raise the service quota, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-sns).
If the amount set in the console exceeds your service quota, Amazon SNS stops publishing SMS messages.
Because Amazon SNS is a distributed system, it stops sending SMS messages within minutes of the spend quota being exceeded. During this interval, if you continue to send SMS messages, you might incur costs that exceed your quota.

1. (Optional) For **Default sender ID**, enter a custom ID, such as your business brand, which is displayed as the sender of the receiving device.
**Note**  
Support for sender IDs varies by country.

1. (Optional) Enter the name of the **Amazon S3 bucket name for usage reports**.
**Note**  
The Amazon S3 bucket policy must grant write access to Amazon SNS.

1. (Optional) To log the delivery status of your SMS messages to CloudWatch Logs, expand the **Message delivery status logging** section, and then set a **Success sample rate** and provide an IAM role that grants Amazon SNS write access to CloudWatch Logs. For more information, see [Viewing CloudWatch Logs](sms_stats_cloudwatch.md#sns-viewing-cloudwatch-logs).

1. Choose **Save changes**.

## Setting preferences (AWS SDKs)
<a name="sms_preferences_sdk"></a>

To set your SMS preferences using one of the AWS SDKs, use the action in that SDK that corresponds to the `SetSMSAttributes` request in the Amazon SNS API. With this request, you assign values to the different SMS attributes, such as your monthly spend quota and your default SMS type (promotional or transactional). For all SMS attributes, see [SetSMSAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html) in the *Amazon Simple Notification Service API Reference*.

The following code examples show how to use `SetSMSAttributes`.

------
#### [ C\+\+ ]

**SDK for C\+\+**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples). 
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
+  For API details, see [SetSMSAttributes](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/SetSMSAttributes) in *AWS SDK for C\+\+ API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To set SMS message attributes**  
The following `set-sms-attributes` example sets the default sender ID for SMS messages to `MyName`.  

```
aws sns set-sms-attributes \
    --attributes {{DefaultSenderID=MyName}}
```
This command produces no output.  
For more information, see [Setting SMS messaging preferences in Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sms_preferences.html) in the *Amazon Simple Notification Service Developer Guide*.  
+  For API details, see [SetSMSAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-sms-attributes.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples). 

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
+  For API details, see [SetSMSAttributes](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/SetSMSAttributes) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/sns#code-examples). 
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
+  For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sns-examples-sending-sms.html#sending-sms-setattributes). 
+  For API details, see [SetSMSAttributes](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/sns/command/SetSMSAttributesCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ PHP ]

**SDK for PHP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/sns#code-examples). 

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
+  For more information, see [AWS SDK for PHP Developer Guide](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sns-examples-sending-sms.html#set-sms-attributes). 
+  For API details, see [SetSMSAttributes](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/SetSMSAttributes) in *AWS SDK for PHP API Reference*. 

------

## Setting SMS messaging preferences for country-specific delivery
<a name="sms_preferences_country_specific"></a>

You can control your SMS traffic by sending messages only to specific destination countries. This approach ensures that your messages reach only approved countries and helps you avoid unwanted SMS charges. To do this, you create a protect configuration in AWS End User Messaging SMS that defines per-country send rules for SMS.

**Note**  
To apply a protect configuration to the SMS messages that you send through Amazon SNS, you must associate the protect configuration as the *account default*. The account default applies at the account level and also affects SMS messages sent through Amazon Cognito and AWS End User Messaging SMS. You can have only one account default protect configuration at a time.

1. Open the [AWS End User Messaging SMS console](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Protect**, choose **Protect configuration**, and then choose **Create protect configuration**.

1. For **Protect configuration name**, enter a descriptive name (for example, Allow-Only-AU).

1. On the **SMS country rules** tab, select the check box for each country that you want to allow, and then choose **Allow**. For example, to allow SMS messages only to Australia, select **Australia** and then choose **Allow**.
**Note**  
By default, all destination countries are set to **Block**. Select only the countries that you want to allow.

1. In the **Status change confirmation** dialog box, review your changes and choose **Confirm**.

1. In the **Protect configuration associations** section, for **Association type**, choose **Account default** so that the protect configuration applies to all SMS messages sent through Amazon SNS.

1. Choose **Create protect configuration**.

   The following confirmation message appears:

   ```
   Success Protect configuration protect-abc0123456789 has been created.
   ```

When you set country rules in a protect configuration, you can apply one of the following modes to each destination country. You can apply a different mode to individual countries.

**Allow**  
Send messages to the destination country.

**Block**  
Block all messages to the destination country.

**Monitor**  
Send messages, but include the SMS protect blocking recommendation in metrics and events.

**Filter**  
Send messages, but block traffic suspected of being artificially inflated traffic (AIT).

**Note**  
The **Monitor** and **Filter** modes incur additional charges for artificially inflated traffic (AIT) risk evaluation.

After you associate the protect configuration as the account default, AWS End User Messaging SMS applies the protect configuration's country rules to the SMS messages that you publish through Amazon SNS. To see which messages are allowed or blocked, open the Amazon SNS console. In the navigation pane, choose **Mobile**, and then **Text messaging (SMS)**. This opens the **Mobile text messaging (SMS)** page, where you can do the following:
+ **Configure delivery status logging** – In the **Text messaging preferences** section, provide an IAM role that grants Amazon SNS write access to CloudWatch Logs. For detailed steps, see [Viewing CloudWatch Logs](sms_stats_cloudwatch.md#sns-viewing-cloudwatch-logs). Depending on the destination phone number's carrier, it can take up to 72 hours for delivery logs to appear in the Amazon SNS console.
+ **View delivery status logs** – In the **Delivery status logs** section, each message shows a **Status** and a **Provider response**. For a destination that the protect configuration blocks, the status is **FAILURE** and the provider response is `Destination country blocked by SMS protect configuration.`
+ **View delivery statistics** – In the **Delivery statistics** section, blocked messages are counted under **Failed**.

The same delivery events are also written to CloudWatch Logs in the log group `sns/region/AccountID/DirectPublishToPhoneNumber/Failure`.

For more information, see [Using protect configurations](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-configuration.html), [Change country rules](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-configuration-edit-countries.html), and [Country rule modes](https://docs.aws.amazon.com/sms-voice/latest/userguide/filter-and-monitor-messages.html) in the *AWS End User Messaging SMS User Guide*.