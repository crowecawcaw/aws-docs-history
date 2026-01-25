# Use `DisableKey` with an AWS SDK or CLI

The following code examples show how to use `DisableKey`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](example_kms_Scenario_Basics_section.md "example_kms_Scenario_Basics_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/KMS#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/KMS#code-examples").

```
    using System;
    using System.Threading.Tasks;
    using Amazon.KeyManagementService;
    using Amazon.KeyManagementService.Model;

    /// <summary>
    /// Disable an AWS Key Management Service (AWS KMS) key and then retrieve
    /// the key's status to show that it has been disabled.
    /// </summary>
    public class DisableKey
    {
        public static async Task Main()
        {
            var client = new AmazonKeyManagementServiceClient();

            // The identifier of the AWS KMS key to disable. You can use the
            // key Id or the Amazon Resource Name (ARN) of the AWS KMS key.
            var keyId = "1234abcd-12ab-34cd-56ef-1234567890ab";

            var request = new DisableKeyRequest
            {
                KeyId = keyId,
            };

            var response = await client.DisableKeyAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                // Retrieve information about the key to show that it has now
                // been disabled.
                var describeResponse = await client.DescribeKeyAsync(new DescribeKeyRequest
                {
                    KeyId = keyId,
                });
                Console.WriteLine($"{describeResponse.KeyMetadata.KeyId} - state: {describeResponse.KeyMetadata.KeyState}");
            }
        }
    }



```

- For API details, see
  [DisableKey](../../../goto/DotNetSDKV3/kms-2014-11-01/DisableKey.md "../../../goto/DotNetSDKV3/kms-2014-11-01/DisableKey.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To temporarily disable a KMS key**

The following `disable-key` command disables a customer managed KMS key. To re-enable the KMS key, use the `enable-key` command.

```
`aws kms disable-key \
 --key-id `1234abcd-12ab-34cd-56ef-1234567890ab``

```

This command produces no output.

For more information, see [Enabling and Disabling Keys](enabling-keys.md "enabling-keys.md") in the _AWS Key Management Service Developer Guide_.

- For API details, see
  [DisableKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disable-key.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disable-key.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/kms#code-examples").

```
    /**
     * Asynchronously disables the specified AWS Key Management Service (KMS) key.
     *
     * @param keyId the ID or Amazon Resource Name (ARN) of the KMS key to be disabled
     * @return a CompletableFuture that, when completed, indicates that the key has been disabled successfully
     */
    public CompletableFuture<Void> disableKeyAsync(String keyId) {
        DisableKeyRequest keyRequest = DisableKeyRequest.builder()
            .keyId(keyId)
            .build();

        return getAsyncClient().disableKey(keyRequest)
            .thenRun(() -> {
                logger.info("Key {} has been disabled successfully",keyId);
            })
            .exceptionally(throwable -> {
                throw new RuntimeException("Failed to disable key: " + keyId, throwable);
            });
    }


```

- For API details, see
  [DisableKey](../../../goto/SdkForJavaV2/kms-2014-11-01/DisableKey.md "../../../goto/SdkForJavaV2/kms-2014-11-01/DisableKey.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/kms#code-examples").

```
suspend fun disableKey(keyIdVal: String?) {
    val request =
        DisableKeyRequest {
            keyId = keyIdVal
        }

    KmsClient.fromEnvironment { region = "us-west-2" }.use { kmsClient ->
        kmsClient.disableKey(request)
        println("$keyIdVal was successfully disabled")
    }
}


```

- For API details, see
  [DisableKey](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/kms#code-examples").

```

    /***
     * @param string $keyId
     * @return void
     */
    public function disableKey(string $keyId)
    {
        try {
            $this->client->disableKey([
                'KeyId' => $keyId,
            ]);
        }catch(KmsException $caught){
            echo "There was a problem disabling the key: {$caught->getAwsErrorMessage()}\n";
            throw $caught;
        }
    }



```

- For API details, see
  [DisableKey](../../../goto/SdkForPHPV3/kms-2014-11-01/DisableKey.md "../../../goto/SdkForPHPV3/kms-2014-11-01/DisableKey.md")
  in _AWS SDK for PHP API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples").

```
class KeyManager:
    def __init__(self, kms_client):
        self.kms_client = kms_client
        self.created_keys = []

    @classmethod
    def from_client(cls) -> "KeyManager":
        """
        Creates a KeyManager instance with a default KMS client.

        :return: An instance of KeyManager initialized with the default KMS client.
        """
        kms_client = boto3.client("kms")
        return cls(kms_client)


    def disable_key(self, key_id: str) -> None:
        try:
            self.kms_client.disable_key(KeyId=key_id)
        except ClientError as err:
            logging.error(
                "Couldn't disable key '%s'. Here's why: %s",
                key_id,
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [DisableKey](../../../goto/boto3/kms-2014-11-01/DisableKey.md "../../../goto/boto3/kms-2014-11-01/DisableKey.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/kms#code-examples").

```
    TRY.
        " iv_key_id = 'arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab'
        lo_kms->disablekey( iv_keyid = iv_key_id ).
        MESSAGE 'KMS key disabled successfully.' TYPE 'I'.
      CATCH /aws1/cx_kmsnotfoundexception.
        MESSAGE 'Key not found.' TYPE 'E'.
      CATCH /aws1/cx_kmskmsinternalex.
        MESSAGE 'An internal error occurred.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [DisableKey](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
