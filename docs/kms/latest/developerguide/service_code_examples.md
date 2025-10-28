# Code examples for AWS KMS using AWS SDKs

The following code examples show how to use AWS KMS with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using AWS Key Management Service.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/kms#code-examples").

```
import software.amazon.awssdk.services.kms.KmsAsyncClient;
import software.amazon.awssdk.services.kms.model.ListKeysRequest;
import software.amazon.awssdk.services.kms.paginators.ListKeysPublisher;
import java.util.concurrent.CompletableFuture;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class HelloKMS {
    public static void main(String[] args) {
        listAllKeys();
    }

    public static void listAllKeys() {
        KmsAsyncClient kmsAsyncClient = KmsAsyncClient.builder()
            .build();
        ListKeysRequest listKeysRequest = ListKeysRequest.builder()
            .limit(15)
            .build();

        /*
         * The `subscribe` method is required when using paginator methods in the AWS SDK
         * because paginator methods return an instance of a `ListKeysPublisher`, which is
         * based on a reactive stream. This allows asynchronous retrieval of paginated
         * results as they become available. By subscribing to the stream, we can process
         * each page of results as they are emitted.
         */
        ListKeysPublisher keysPublisher = kmsAsyncClient.listKeysPaginator(listKeysRequest);
        CompletableFuture<Void> future = keysPublisher
            .subscribe(r -> r.keys().forEach(key ->
                System.out.println("The key ARN is: " + key.keyArn() + ". The key Id is: " + key.keyId())))
            .whenComplete((result, exception) -> {
                if (exception != null) {
                    System.err.println("Error occurred: " + exception.getMessage());
                } else {
                    System.out.println("Successfully listed all keys.");
                }
            });

        try {
            future.join();
        } catch (Exception e) {
            System.err.println("Failed to list keys: " + e.getMessage());
        }
    }
}


```

- For API details, see
  [ListKeys](../../../goto/SdkForJavaV2/kms-2014-11-01/ListKeys.md "../../../goto/SdkForJavaV2/kms-2014-11-01/ListKeys.md")
  in _AWS SDK for Java 2.x API Reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/kms#code-examples").

```
include "vendor/autoload.php";

use Aws\Kms\KmsClient;

echo "This file shows how to connect to the KmsClient, uses a paginator to get the keys for the account, and lists the KeyIds for up to 10 keys.\n";

$client = new KmsClient([]);

$pageLength = 10; // Change this value to change the number of records shown, or to break up the result into pages.

$keys = [];
$keysPaginator = $client->getPaginator("ListKeys", ['Limit' => $pageLength]);
foreach($keysPaginator as $page){
    foreach($page['Keys'] as $index => $key){
        echo "The $index index Key's ID is: {$key['KeyId']}\n";
    }
    echo "End of page one of results. Alter the \$pageLength variable to see more results.\n";
    break;
}



```

- For API details, see
  [ListKeys](../../../goto/SdkForPHPV3/kms-2014-11-01/ListKeys.md "../../../goto/SdkForPHPV3/kms-2014-11-01/ListKeys.md")
  in _AWS SDK for PHP API Reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello AWS KMS](example_kms_Hello_section.md "example_kms_Hello_section.md")
  - [Learn the basics](example_kms_Scenario_Basics_section.md "example_kms_Scenario_Basics_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [CreateAlias](example_kms_CreateAlias_section.md "example_kms_CreateAlias_section.md")
    - [CreateGrant](example_kms_CreateGrant_section.md "example_kms_CreateGrant_section.md")
    - [CreateKey](example_kms_CreateKey_section.md "example_kms_CreateKey_section.md")
    - [Decrypt](example_kms_Decrypt_section.md "example_kms_Decrypt_section.md")
    - [DeleteAlias](example_kms_DeleteAlias_section.md "example_kms_DeleteAlias_section.md")
    - [DescribeKey](example_kms_DescribeKey_section.md "example_kms_DescribeKey_section.md")
    - [DisableKey](example_kms_DisableKey_section.md "example_kms_DisableKey_section.md")
    - [EnableKey](example_kms_EnableKey_section.md "example_kms_EnableKey_section.md")
    - [EnableKeyRotation](example_kms_EnableKeyRotation_section.md "example_kms_EnableKeyRotation_section.md")
    - [Encrypt](example_kms_Encrypt_section.md "example_kms_Encrypt_section.md")
    - [GenerateDataKey](example_kms_GenerateDataKey_section.md "example_kms_GenerateDataKey_section.md")
    - [GenerateDataKeyWithoutPlaintext](example_kms_GenerateDataKeyWithoutPlaintext_section.md "example_kms_GenerateDataKeyWithoutPlaintext_section.md")
    - [GenerateRandom](example_kms_GenerateRandom_section.md "example_kms_GenerateRandom_section.md")
    - [GetKeyPolicy](example_kms_GetKeyPolicy_section.md "example_kms_GetKeyPolicy_section.md")
    - [ListAliases](example_kms_ListAliases_section.md "example_kms_ListAliases_section.md")
    - [ListGrants](example_kms_ListGrants_section.md "example_kms_ListGrants_section.md")
    - [ListKeyPolicies](example_kms_ListKeyPolicies_section.md "example_kms_ListKeyPolicies_section.md")
    - [ListKeys](example_kms_ListKeys_section.md "example_kms_ListKeys_section.md")
    - [PutKeyPolicy](example_kms_PutKeyPolicy_section.md "example_kms_PutKeyPolicy_section.md")
    - [ReEncrypt](example_kms_ReEncrypt_section.md "example_kms_ReEncrypt_section.md")
    - [RetireGrant](example_kms_RetireGrant_section.md "example_kms_RetireGrant_section.md")
    - [RevokeGrant](example_kms_RevokeGrant_section.md "example_kms_RevokeGrant_section.md")
    - [ScheduleKeyDeletion](example_kms_ScheduleKeyDeletion_section.md "example_kms_ScheduleKeyDeletion_section.md")
    - [Sign](example_kms_Sign_section.md "example_kms_Sign_section.md")
    - [TagResource](example_kms_TagResource_section.md "example_kms_TagResource_section.md")
    - [UpdateAlias](example_kms_UpdateAlias_section.md "example_kms_UpdateAlias_section.md")
    - [Verify](example_kms_Verify_section.md "example_kms_Verify_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Work with table encryption](example_dynamodb_Scenario_EncryptionExamples_section.md "example_dynamodb_Scenario_EncryptionExamples_section.md")
