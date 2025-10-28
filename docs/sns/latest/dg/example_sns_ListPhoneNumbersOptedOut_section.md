# Use `ListPhoneNumbersOptedOut` with an AWS SDK or CLI

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

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon SNS with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
