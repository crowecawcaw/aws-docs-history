# Managing Amazon SNS phone numbers and subscriptions

Amazon SNS provides several options for managing who receives SMS messages from your account.
With a limited frequency, you can opt in phone numbers that have opted out of receiving SMS
messages from your account. To stop sending messages to SMS subscriptions, you can remove
subscriptions or the topics that publish to them.

## Opting out of receiving SMS messages

Where required by local laws and regulations (such as the US and Canada), SMS
recipients can use their devices to opt-out by replying to the message with any of the
following:

- ARRET (French)
- CANCEL
- END
- OPT-OUT
- OPTOUT
- QUIT
- REMOVE
- STOP
- TD
- UNSUBSCRIBE

To opt-out, the recipient must reply to the same [origination number](../../../sms-voice/latest/userguide/phone-numbers.md "../../../sms-voice/latest/userguide/phone-numbers.md") that
Amazon SNS used to deliver the message. After opting-out, the recipient will no longer
receive SMS messages delivered from your AWS account unless you opt-in the phone
number.

If the phone number is subscribed to an Amazon SNS topic, opting-out does not remove the
subscription, but SMS messages will fail to deliver to that subscription unless you
opt-in the phone number.

## Managing phone numbers and subscriptions using the

Amazon SNS console

You can use the Amazon SNS console to control which phone numbers receive SMS messages from
your account.

### Opting-in a phone number that has been

opted-out the Amazon SNS console

You can view which phone numbers have been opted-out of receiving SMS messages
from your account, and you can opt-in these phone numbers to resume sending messages
to them.

You can opt-in a phone number only once every 30 days.

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the console menu, set the region selector to a [region that supports SMS messaging](../../../general/latest/gr/end-user-messaging.md "../../../general/latest/gr/end-user-messaging.md").
3. On the navigation panel, choose **Text messaging
   (SMS)**.
4. On the **Mobile text messaging (SMS)** page, in the
   **Opted-out phone numbers** section, opted-out phone
   numbers are displayed.
5. Select the check box for the phone number that you want to opt-in, and
   choose **Opt in**. The phone number is no longer opted-out
   and will receive SMS messages that you send to it.

#### Deleting an SMS subscription

the Amazon SNS console

Delete an SMS subscription to stop sending SMS messages to that phone number
when you publish to your topics.

1. On the navigation panel, choose
   **Subscriptions**.
2. Select the check boxes for the subscriptions that you want to delete.
   Then choose **Actions**, and choose **Delete
   Subscriptions**.
3. In the **Delete** window, choose
   **Delete**. Amazon SNS deletes the subscription and
   displays a success message.

#### Deleting a topic the Amazon SNS

console

Delete a topic when you no longer want to publish messages to its subscribed
endpoints.

1. On the navigation panel, choose **Topics**.
2. Select the check boxes for the topics that you want to delete. Then
   choose **Actions**, and choose **Delete
   Topics**.
3. In the **Delete** window, choose
   **Delete**. Amazon SNS deletes the topic and displays a
   success message.

### Managing phone numbers and subscriptions using the

AWS SDK

You can use the AWS SDKs to make programmatic requests to Amazon SNS and manage which
phone numbers can receive SMS messages from your account.

To use an AWS SDK, you must configure it with your credentials. For more
information, see [Shared config and credentials
files](../../../sdkref/latest/guide/file-format.md "../../../sdkref/latest/guide/file-format.md") in the _AWS SDKs and Tools Reference Guide_.

#### Viewing all opted-out phone numbers using

the AWS SDK

To view all opted-out phone numbers, submit a
`ListPhoneNumbersOptedOut` request with the Amazon SNS API.

The following code examples show how to use `ListPhoneNumbersOptedOut`.

CLI

**AWS CLI**

**To list SMS message opt-outs**

The following `list-phone-numbers-opted-out` example lists the phone numbers opted out of receiving SMS messages.

```
`aws sns list-phone-numbers-opted-out`

```

Output:

```
{
    "phoneNumbers": [
        "+15555550100"
    ]
}
```

- For API details, see
  [ListPhoneNumbersOptedOut](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-phone-numbers-opted-out.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-phone-numbers-opted-out.html")
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
import software.amazon.awssdk.services.sns.model.ListPhoneNumbersOptedOutRequest;
import software.amazon.awssdk.services.sns.model.ListPhoneNumbersOptedOutResponse;
import software.amazon.awssdk.services.sns.model.SnsException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class ListOptOut {
    public static void main(String[] args) {
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();

        listOpts(snsClient);
        snsClient.close();
    }

    public static void listOpts(SnsClient snsClient) {
        try {
            ListPhoneNumbersOptedOutRequest request = ListPhoneNumbersOptedOutRequest.builder().build();
            ListPhoneNumbersOptedOutResponse result = snsClient.listPhoneNumbersOptedOut(request);
            System.out.println("Status is " + result.sdkHttpResponse().statusCode() + "\n\nPhone Numbers: \n\n"
                    + result.phoneNumbers());

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [ListPhoneNumbersOptedOut](../../../goto/SdkForJavaV2/sns-2010-03-31/ListPhoneNumbersOptedOut.md "../../../goto/SdkForJavaV2/sns-2010-03-31/ListPhoneNumbersOptedOut.md")
  in _AWS SDK for Java 2.x API Reference_.

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
 * Returns a list of phone numbers that are opted out of receiving SMS messages from your AWS SNS account.
 *
 * This code expects that you have AWS credentials set up per:
 * https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html
 */

$SnSclient = new SnsClient([
    'profile' => 'default',
    'region' => 'us-east-1',
    'version' => '2010-03-31'
]);

try {
    $result = $SnSclient->listPhoneNumbersOptedOut();
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}



```

- For more information, see [AWS SDK for PHP Developer Guide](../../../sdk-for-php/v3/developer-guide/sns-examples-sending-sms.md#list-opted-out-phone-numbers "../../../sdk-for-php/v3/developer-guide/sns-examples-sending-sms.md#list-opted-out-phone-numbers").
- For API details, see
  [ListPhoneNumbersOptedOut](../../../goto/SdkForPHPV3/sns-2010-03-31/ListPhoneNumbersOptedOut.md "../../../goto/SdkForPHPV3/sns-2010-03-31/ListPhoneNumbersOptedOut.md")
  in _AWS SDK for PHP API Reference_.

#### Checking whether a phone number is

opted-out using the AWS SDK

To check whether a phone number is opted-out, submit a
`CheckIfPhoneNumberIsOptedOut` request with the Amazon SNS API.

The following code examples show how to use `CheckIfPhoneNumberIsOptedOut`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SNS#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SNS#code-examples").

```
    using System;
    using System.Threading.Tasks;
    using Amazon.SimpleNotificationService;
    using Amazon.SimpleNotificationService.Model;

    /// <summary>
    /// This example shows how to use the Amazon Simple Notification Service
    /// (Amazon SNS) to check whether a phone number has been opted out.
    /// </summary>
    public class IsPhoneNumOptedOut
    {
        public static async Task Main()
        {
            string phoneNumber = "+15551112222";

            IAmazonSimpleNotificationService client = new AmazonSimpleNotificationServiceClient();

            await CheckIfOptedOutAsync(client, phoneNumber);
        }

        /// <summary>
        /// Checks to see if the supplied phone number has been opted out.
        /// </summary>
        /// <param name="client">The initialized Amazon SNS Client object used
        /// to check if the phone number has been opted out.</param>
        /// <param name="phoneNumber">A string representing the phone number
        /// to check.</param>
        public static async Task CheckIfOptedOutAsync(IAmazonSimpleNotificationService client, string phoneNumber)
        {
            var request = new CheckIfPhoneNumberIsOptedOutRequest
            {
                PhoneNumber = phoneNumber,
            };

            try
            {
                var response = await client.CheckIfPhoneNumberIsOptedOutAsync(request);

                if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
                {
                    string optOutStatus = response.IsOptedOut ? "opted out" : "not opted out.";
                    Console.WriteLine($"The phone number: {phoneNumber} is {optOutStatus}");
                }
            }
            catch (AuthorizationErrorException ex)
            {
                Console.WriteLine($"{ex.Message}");
            }
        }
    }



```

- For API details, see
  [CheckIfPhoneNumberIsOptedOut](../../../goto/DotNetSDKV3/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut.md "../../../goto/DotNetSDKV3/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To check SMS message opt-out for a phone number**

The following `check-if-phone-number-is-opted-out` example checks whether the specified phone number is opted out of receiving SMS messages from the current AWS account.

```
`aws sns check-if-phone-number-is-opted-out \
 --phone-number `+1555550100``

```

Output:

```
{
    "isOptedOut": false
}
```

- For API details, see
  [CheckIfPhoneNumberIsOptedOut](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/check-if-phone-number-is-opted-out.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/check-if-phone-number-is-opted-out.html")
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
import software.amazon.awssdk.services.sns.model.CheckIfPhoneNumberIsOptedOutRequest;
import software.amazon.awssdk.services.sns.model.CheckIfPhoneNumberIsOptedOutResponse;
import software.amazon.awssdk.services.sns.model.SnsException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class CheckOptOut {
    public static void main(String[] args) {

        final String usage = """

                Usage:    <phoneNumber>

                Where:
                   phoneNumber - The mobile phone number to look up (for example, +1XXX5550100).

                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String phoneNumber = args[0];
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();

        checkPhone(snsClient, phoneNumber);
        snsClient.close();
    }

    public static void checkPhone(SnsClient snsClient, String phoneNumber) {
        try {
            CheckIfPhoneNumberIsOptedOutRequest request = CheckIfPhoneNumberIsOptedOutRequest.builder()
                    .phoneNumber(phoneNumber)
                    .build();

            CheckIfPhoneNumberIsOptedOutResponse result = snsClient.checkIfPhoneNumberIsOptedOut(request);
            System.out.println(
                    result.isOptedOut() + "Phone Number " + phoneNumber + " has Opted Out of receiving sns messages." +
                            "\n\nStatus was " + result.sdkHttpResponse().statusCode());

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [CheckIfPhoneNumberIsOptedOut](../../../goto/SdkForJavaV2/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut.md "../../../goto/SdkForJavaV2/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut.md")
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
import { CheckIfPhoneNumberIsOptedOutCommand } from "@aws-sdk/client-sns";

import { snsClient } from "../libs/snsClient.js";

export const checkIfPhoneNumberIsOptedOut = async (
  phoneNumber = "5555555555",
) => {
  const command = new CheckIfPhoneNumberIsOptedOutCommand({
    phoneNumber,
  });

  const response = await snsClient.send(command);
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '3341c28a-cdc8-5b39-a3ee-9fb0ee125732',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   isOptedOut: false
  // }
  return response;
};


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v3/developer-guide/sns-examples-sending-sms.md#sending-sms-checkifphonenumberisoptedout "../../../sdk-for-javascript/v3/developer-guide/sns-examples-sending-sms.md#sending-sms-checkifphonenumberisoptedout").
- For API details, see
  [CheckIfPhoneNumberIsOptedOut](../../../AWSJavaScriptSDK/v3/latest/client/sns/command/CheckIfPhoneNumberIsOptedOutCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/sns/command/CheckIfPhoneNumberIsOptedOutCommand.md")
  in _AWS SDK for JavaScript API Reference_.

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
 * Indicates whether the phone number owner has opted out of receiving SMS messages from your AWS SNS account.
 *
 * This code expects that you have AWS credentials set up per:
 * https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html
 */

$SnSclient = new SnsClient([
    'profile' => 'default',
    'region' => 'us-east-1',
    'version' => '2010-03-31'
]);

$phone = '+1XXX5550100';

try {
    $result = $SnSclient->checkIfPhoneNumberIsOptedOut([
        'phoneNumber' => $phone,
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}



```

- For more information, see [AWS SDK for PHP Developer Guide](../../../sdk-for-php/v3/developer-guide/sns-examples-sending-sms.md#check-if-a-phone-number-has-opted-out "../../../sdk-for-php/v3/developer-guide/sns-examples-sending-sms.md#check-if-a-phone-number-has-opted-out").
- For API details, see
  [CheckIfPhoneNumberIsOptedOut](../../../goto/SdkForPHPV3/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut.md "../../../goto/SdkForPHPV3/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut.md")
  in _AWS SDK for PHP API Reference_.

#### Opting-in a phone number that has been

opted-out using the Amazon SNS API

To opt-in a phone number, submit an `OptInPhoneNumber` request with
the Amazon SNS API.

You can opt-in a phone number only once every 30 days.

#### Deleting an SMS subscription

using the AWS SDK

To delete an SMS subscription from an Amazon SNS topic, get the subscription ARN by
submitting a `ListSubscriptions` request with the Amazon SNS API, and then
pass the ARN to an `Unsubscribe` request.

The following code examples show how to use `Unsubscribe`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/TopicsAndQueues#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/TopicsAndQueues#code-examples").

Unsubscribe from a topic by a subscription ARN.

```
    /// <summary>
    /// Unsubscribe from a topic by a subscription ARN.
    /// </summary>
    /// <param name="subscriptionArn">The ARN of the subscription.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> UnsubscribeByArn(string subscriptionArn)
    {
        var unsubscribeResponse = await _amazonSNSClient.UnsubscribeAsync(
            new UnsubscribeRequest()
            {
                SubscriptionArn = subscriptionArn
            });
        return unsubscribeResponse.HttpStatusCode == HttpStatusCode.OK;
    }


```

- For API details, see
  [Unsubscribe](../../../goto/DotNetSDKV3/sns-2010-03-31/Unsubscribe.md "../../../goto/DotNetSDKV3/sns-2010-03-31/Unsubscribe.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples").

```
//! Delete a subscription to an Amazon Simple Notification Service (Amazon SNS) topic.
/*!
  \param subscriptionARN: The Amazon Resource Name (ARN) for an Amazon SNS topic subscription.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::SNS::unsubscribe(const Aws::String &subscriptionARN,
                              const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::SNS::SNSClient snsClient(clientConfiguration);

    Aws::SNS::Model::UnsubscribeRequest request;
    request.SetSubscriptionArn(subscriptionARN);

    const Aws::SNS::Model::UnsubscribeOutcome outcome = snsClient.Unsubscribe(request);

    if (outcome.IsSuccess()) {
        std::cout << "Unsubscribed successfully " << std::endl;
    }
    else {
        std::cerr << "Error while unsubscribing " << outcome.GetError().GetMessage()
                  << std::endl;
    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [Unsubscribe](../../../goto/SdkForCpp/sns-2010-03-31/Unsubscribe.md "../../../goto/SdkForCpp/sns-2010-03-31/Unsubscribe.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**To unsubscribe from a topic**

The following `unsubscribe` example deletes the specified subscription from a topic.

```
`aws sns unsubscribe \
 --subscription-arn `arn:aws:sns:us-west-2:0123456789012:my-topic:8a21d249-4329-4871-acc6-7be709c6ea7f``

```

This command produces no output.

- For API details, see
  [Unsubscribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/unsubscribe.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/unsubscribe.html")
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
import software.amazon.awssdk.services.sns.model.SnsException;
import software.amazon.awssdk.services.sns.model.UnsubscribeRequest;
import software.amazon.awssdk.services.sns.model.UnsubscribeResponse;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class Unsubscribe {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <subscriptionArn>

                Where:
                   subscriptionArn - The ARN of the subscription to delete.
                """;

        if (args.length < 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String subscriptionArn = args[0];
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();

        unSub(snsClient, subscriptionArn);
        snsClient.close();
    }

    public static void unSub(SnsClient snsClient, String subscriptionArn) {
        try {
            UnsubscribeRequest request = UnsubscribeRequest.builder()
                    .subscriptionArn(subscriptionArn)
                    .build();

            UnsubscribeResponse result = snsClient.unsubscribe(request);
            System.out.println("\n\nStatus was " + result.sdkHttpResponse().statusCode()
                    + "\n\nSubscription was removed for " + request.subscriptionArn());

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [Unsubscribe](../../../goto/SdkForJavaV2/sns-2010-03-31/Unsubscribe.md "../../../goto/SdkForJavaV2/sns-2010-03-31/Unsubscribe.md")
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
import { UnsubscribeCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string} subscriptionArn - The ARN of the subscription to cancel.
 */
const unsubscribe = async (
  subscriptionArn = "arn:aws:sns:us-east-1:xxxxxxxxxxxx:mytopic:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
) => {
  const response = await snsClient.send(
    new UnsubscribeCommand({
      SubscriptionArn: subscriptionArn,
    }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '0178259a-9204-507c-b620-78a7570a44c6',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   }
  // }
  return response;
};


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v3/developer-guide/sns-examples-managing-topics.md#sns-examples-unsubscribing "../../../sdk-for-javascript/v3/developer-guide/sns-examples-managing-topics.md#sns-examples-unsubscribing").
- For API details, see
  [Unsubscribe](../../../AWSJavaScriptSDK/v3/latest/client/sns/command/UnsubscribeCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/sns/command/UnsubscribeCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples").

```
suspend fun unSub(subscriptionArnVal: String) {
    val request =
        UnsubscribeRequest {
            subscriptionArn = subscriptionArnVal
        }

    SnsClient.fromEnvironment { region = "us-east-1" }.use { snsClient ->
        snsClient.unsubscribe(request)
        println("Subscription was removed for ${request.subscriptionArn}")
    }
}


```

- For API details, see
  [Unsubscribe](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
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
 * Deletes a subscription to an Amazon SNS topic.
 *
 * This code expects that you have AWS credentials set up per:
 * https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html
 */

$SnSclient = new SnsClient([
    'profile' => 'default',
    'region' => 'us-east-1',
    'version' => '2010-03-31'
]);

$subscription = 'arn:aws:sns:us-east-1:111122223333:MySubscription';

try {
    $result = $SnSclient->unsubscribe([
        'SubscriptionArn' => $subscription,
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}



```

- For more information, see [AWS SDK for PHP Developer Guide](../../../sdk-for-php/v3/developer-guide/sns-examples-subscribing-unsubscribing-topics.md#unsubscribe-from-a-topic "../../../sdk-for-php/v3/developer-guide/sns-examples-subscribing-unsubscribing-topics.md#unsubscribe-from-a-topic").
- For API details, see
  [Unsubscribe](../../../goto/SdkForPHPV3/sns-2010-03-31/Unsubscribe.md "../../../goto/SdkForPHPV3/sns-2010-03-31/Unsubscribe.md")
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


    @staticmethod
    def delete_subscription(subscription):
        """
        Unsubscribes and deletes a subscription.
        """
        try:
            subscription.delete()
            logger.info("Deleted subscription %s.", subscription.arn)
        except ClientError:
            logger.exception("Couldn't delete subscription %s.", subscription.arn)
            raise



```

```
class SnsWrapper:
    """Wrapper class for managing Amazon SNS operations."""

    def __init__(self, sns_client: Any) -> None:
        """
        Initialize the SnsWrapper.

        :param sns_client: A Boto3 Amazon SNS client.
        """
        self.sns_client = sns_client

    @classmethod
    def from_client(cls) -> 'SnsWrapper':
        """
        Create an SnsWrapper instance using a default boto3 client.

        :return: An instance of this class.
        """
        sns_client = boto3.client('sns')
        return cls(sns_client)


    def unsubscribe(self, subscription_arn: str) -> bool:
        """
        Unsubscribe from an SNS topic.

        :param subscription_arn: The ARN of the subscription to remove.
        :return: True if successful.
        :raises ClientError: If the unsubscribe operation fails.
        """
        try:
            self.sns_client.unsubscribe(SubscriptionArn=subscription_arn)

            logger.info(f"Unsubscribed: {subscription_arn}")
            return True

        except ClientError as e:
            error_code = e.response.get('Error', {}).get('Code', 'Unknown')

            if error_code == 'NotFound':
                logger.warning(f"Subscription not found: {subscription_arn}")
                return True  # Already unsubscribed
            else:
                logger.error(f"Error unsubscribing: {error_code} - {e}")
                raise



```

- For API details, see
  [Unsubscribe](../../../goto/boto3/sns-2010-03-31/Unsubscribe.md "../../../goto/boto3/sns-2010-03-31/Unsubscribe.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sns#code-examples").

```
    TRY.
        lo_sns->unsubscribe( iv_subscriptionarn = iv_subscription_arn ).
        MESSAGE 'Subscription deleted.' TYPE 'I'.
      CATCH /aws1/cx_snsnotfoundexception.
        MESSAGE 'Subscription does not exist.' TYPE 'E'.
      CATCH /aws1/cx_snsinvalidparameterex.
        MESSAGE 'Subscription with "PendingConfirmation" status cannot be deleted/unsubscribed. Confirm subscription before performing unsubscribe operation.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [Unsubscribe](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/sns#code-examples").

```
import AWSSNS

        let config = try await SNSClient.SNSClientConfiguration(region: region)
        let snsClient = SNSClient(config: config)

        _ = try await snsClient.unsubscribe(
            input: UnsubscribeInput(
                subscriptionArn: arn
            )
        )

        print("Unsubscribed.")


```

- For API details, see
  [Unsubscribe](<https://sdk.amazonaws.com/swift/api/awssns/latest/documentation/awssns/snsclient/unsubscribe(input:)> "https://sdk.amazonaws.com/swift/api/awssns/latest/documentation/awssns/snsclient/unsubscribe(input:)")
  in _AWS SDK for Swift API reference_.

#### Deleting a topic using the AWS

SDK

To delete a topic and all of its subscriptions, get the topic ARN by
submitting a `ListTopics` request with the Amazon SNS API, and then pass
the ARN to the `DeleteTopic` request.

The following code examples show how to use `DeleteTopic`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/TopicsAndQueues#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/TopicsAndQueues#code-examples").

Delete a topic by its topic ARN.

```
    /// <summary>
    /// Delete a topic by its topic ARN.
    /// </summary>
    /// <param name="topicArn">The ARN of the topic.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteTopicByArn(string topicArn)
    {
        var deleteResponse = await _amazonSNSClient.DeleteTopicAsync(
            new DeleteTopicRequest()
            {
                TopicArn = topicArn
            });
        return deleteResponse.HttpStatusCode == HttpStatusCode.OK;
    }


```

- For API details, see
  [DeleteTopic](../../../goto/DotNetSDKV3/sns-2010-03-31/DeleteTopic.md "../../../goto/DotNetSDKV3/sns-2010-03-31/DeleteTopic.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples").

```
//! Delete an Amazon Simple Notification Service (Amazon SNS) topic.
/*!
  \param topicARN: The Amazon Resource Name (ARN) for an Amazon SNS topic.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::SNS::deleteTopic(const Aws::String &topicARN,
                              const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::SNS::SNSClient snsClient(clientConfiguration);

    Aws::SNS::Model::DeleteTopicRequest request;
    request.SetTopicArn(topicARN);

    const Aws::SNS::Model::DeleteTopicOutcome outcome = snsClient.DeleteTopic(request);

    if (outcome.IsSuccess()) {
        std::cout << "Successfully deleted the Amazon SNS topic " << topicARN << std::endl;
    }
    else {
        std::cerr << "Error deleting topic " << topicARN << ":" <<
                  outcome.GetError().GetMessage() << std::endl;
    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [DeleteTopic](../../../goto/SdkForCpp/sns-2010-03-31/DeleteTopic.md "../../../goto/SdkForCpp/sns-2010-03-31/DeleteTopic.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**To delete an SNS topic**

The following `delete-topic` example deletes the specified SNS topic.

```
`aws sns delete-topic \
 --topic-arn `"arn:aws:sns:us-west-2:123456789012:my-topic"``

```

This command produces no output.

- For API details, see
  [DeleteTopic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/delete-topic.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/delete-topic.html")
  in _AWS CLI Command Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/topics_and_queues#code-examples").

```

import (
	"context"
	"encoding/json"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/sns"
	"github.com/aws/aws-sdk-go-v2/service/sns/types"
)

// SnsActions encapsulates the Amazon Simple Notification Service (Amazon SNS) actions
// used in the examples.
type SnsActions struct {
	SnsClient *sns.Client
}



// DeleteTopic delete an Amazon SNS topic.
func (actor SnsActions) DeleteTopic(ctx context.Context, topicArn string) error {
	_, err := actor.SnsClient.DeleteTopic(ctx, &sns.DeleteTopicInput{
		TopicArn: aws.String(topicArn)})
	if err != nil {
		log.Printf("Couldn't delete topic %v. Here's why: %v\n", topicArn, err)
	}
	return err
}



```

- For API details, see
  [DeleteTopic](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sns#Client.DeleteTopic "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sns#Client.DeleteTopic")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.DeleteTopicRequest;
import software.amazon.awssdk.services.sns.model.DeleteTopicResponse;
import software.amazon.awssdk.services.sns.model.SnsException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DeleteTopic {
    public static void main(String[] args) {
        final String usage = """

                Usage:     <topicArn>

                Where:
                   topicArn - The ARN of the topic to delete.
                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String topicArn = args[0];
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();

        System.out.println("Deleting a topic with name: " + topicArn);
        deleteSNSTopic(snsClient, topicArn);
        snsClient.close();
    }

    public static void deleteSNSTopic(SnsClient snsClient, String topicArn) {
        try {
            DeleteTopicRequest request = DeleteTopicRequest.builder()
                    .topicArn(topicArn)
                    .build();

            DeleteTopicResponse result = snsClient.deleteTopic(request);
            System.out.println("\n\nStatus was " + result.sdkHttpResponse().statusCode());

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [DeleteTopic](../../../goto/SdkForJavaV2/sns-2010-03-31/DeleteTopic.md "../../../goto/SdkForJavaV2/sns-2010-03-31/DeleteTopic.md")
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
import { DeleteTopicCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string} topicArn - The ARN of the topic to delete.
 */
export const deleteTopic = async (topicArn = "TOPIC_ARN") => {
  const response = await snsClient.send(
    new DeleteTopicCommand({ TopicArn: topicArn }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: 'a10e2886-5a8f-5114-af36-75bd39498332',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   }
  // }
};


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v3/developer-guide/sns-examples-managing-topics.md#sns-examples-managing-topics-deletetopic "../../../sdk-for-javascript/v3/developer-guide/sns-examples-managing-topics.md#sns-examples-managing-topics-deletetopic").
- For API details, see
  [DeleteTopic](../../../AWSJavaScriptSDK/v3/latest/client/sns/command/DeleteTopicCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/sns/command/DeleteTopicCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples").

```
suspend fun deleteSNSTopic(topicArnVal: String) {
    val request =
        DeleteTopicRequest {
            topicArn = topicArnVal
        }

    SnsClient.fromEnvironment { region = "us-east-1" }.use { snsClient ->
        snsClient.deleteTopic(request)
        println("$topicArnVal was successfully deleted.")
    }
}


```

- For API details, see
  [DeleteTopic](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
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
 * Deletes an SNS topic and all its subscriptions.
 *
 * This code expects that you have AWS credentials set up per:
 * https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html
 */

$SnSclient = new SnsClient([
    'profile' => 'default',
    'region' => 'us-east-1',
    'version' => '2010-03-31'
]);

$topic = 'arn:aws:sns:us-east-1:111122223333:MyTopic';

try {
    $result = $SnSclient->deleteTopic([
        'TopicArn' => $topic,
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}



```

- For API details, see
  [DeleteTopic](../../../goto/SdkForPHPV3/sns-2010-03-31/DeleteTopic.md "../../../goto/SdkForPHPV3/sns-2010-03-31/DeleteTopic.md")
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


    @staticmethod
    def delete_topic(topic):
        """
        Deletes a topic. All subscriptions to the topic are also deleted.
        """
        try:
            topic.delete()
            logger.info("Deleted topic %s.", topic.arn)
        except ClientError:
            logger.exception("Couldn't delete topic %s.", topic.arn)
            raise



```

```
class SnsWrapper:
    """Wrapper class for managing Amazon SNS operations."""

    def __init__(self, sns_client: Any) -> None:
        """
        Initialize the SnsWrapper.

        :param sns_client: A Boto3 Amazon SNS client.
        """
        self.sns_client = sns_client

    @classmethod
    def from_client(cls) -> 'SnsWrapper':
        """
        Create an SnsWrapper instance using a default boto3 client.

        :return: An instance of this class.
        """
        sns_client = boto3.client('sns')
        return cls(sns_client)


    def delete_topic(self, topic_arn: str) -> bool:
        """
        Delete an SNS topic.

        :param topic_arn: The ARN of the topic to delete.
        :return: True if successful.
        :raises ClientError: If the topic deletion fails.
        """
        try:
            self.sns_client.delete_topic(TopicArn=topic_arn)

            logger.info(f"Deleted topic: {topic_arn}")
            return True

        except ClientError as e:
            error_code = e.response.get('Error', {}).get('Code', 'Unknown')

            if error_code == 'NotFound':
                logger.warning(f"Topic not found: {topic_arn}")
                return True  # Already deleted
            else:
                logger.error(f"Error deleting topic: {error_code} - {e}")
                raise



```

- For API details, see
  [DeleteTopic](../../../goto/boto3/sns-2010-03-31/DeleteTopic.md "../../../goto/boto3/sns-2010-03-31/DeleteTopic.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sns#code-examples").

```
    TRY.
        lo_sns->deletetopic( iv_topicarn = iv_topic_arn ).
        MESSAGE 'SNS topic deleted.' TYPE 'I'.
      CATCH /aws1/cx_snsnotfoundexception.
        MESSAGE 'Topic does not exist.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [DeleteTopic](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/sns#code-examples").

```
import AWSSNS

        let config = try await SNSClient.SNSClientConfiguration(region: region)
        let snsClient = SNSClient(config: config)

        _ = try await snsClient.deleteTopic(
            input: DeleteTopicInput(topicArn: arn)
        )


```

- For API details, see
  [DeleteTopic](<https://sdk.amazonaws.com/swift/api/awssns/latest/documentation/awssns/snsclient/deletetopic(input:)> "https://sdk.amazonaws.com/swift/api/awssns/latest/documentation/awssns/snsclient/deletetopic(input:)")
  in _AWS SDK for Swift API reference_.
