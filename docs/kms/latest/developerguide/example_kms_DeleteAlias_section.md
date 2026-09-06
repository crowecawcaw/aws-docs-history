

# Use `DeleteAlias` with an AWS SDK or CLI
<a name="example_kms_DeleteAlias_section"></a>

The following code examples show how to use `DeleteAlias`.

------
#### [ CLI ]

**AWS CLI**  
**To delete an AWS KMS alias**  
The following `delete-alias` example deletes the alias `alias/example-alias`. The alias name must begin with alias/.  

```
aws kms delete-alias \
    --alias-name {{alias/example-alias}}
```
This command produces no output. To find the alias, use the `list-aliases` command.  
For more information, see [Deleting an alias](https://docs.aws.amazon.com/kms/latest/developerguide/alias-manage.html#alias-delete) in the *AWS Key Management Service Developer Guide*.  
+  For API details, see [DeleteAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/delete-alias.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/kms#code-examples). 

```
    /**
     * Deletes a specific KMS alias asynchronously.
     *
     * @param aliasName the name of the alias to be deleted
     * @return a {@link CompletableFuture} representing the asynchronous operation of deleting the specified alias
     */
    public CompletableFuture<Void> deleteSpecificAliasAsync(String aliasName) {
        DeleteAliasRequest deleteAliasRequest = DeleteAliasRequest.builder()
            .aliasName(aliasName)
            .build();

        return getAsyncClient().deleteAlias(deleteAliasRequest)
            .thenRun(() -> {
                logger.info("Alias {} has been deleted successfully", aliasName);
            })
            .exceptionally(throwable -> {
                throw new RuntimeException("Failed to delete alias: " + aliasName, throwable);
            });
    }
```
+  For API details, see [DeleteAlias](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/DeleteAlias) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ PHP ]

**SDK for PHP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/kms#code-examples). 

```
    /***
     * @param string $aliasName
     * @return void
     */
    public function deleteAlias(string $aliasName)
    {
        try {
            $this->client->deleteAlias([
                'AliasName' => $aliasName,
            ]);
        }catch(KmsException $caught){
            echo "There was a problem deleting the alias: {$caught->getAwsErrorMessage()}\n";
            throw $caught;
        }
    }
```
+  For API details, see [DeleteAlias](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/DeleteAlias) in *AWS SDK for PHP API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples). 

```
class AliasManager:
    def __init__(self, kms_client):
        self.kms_client = kms_client
        self.created_key = None

    @classmethod
    def from_client(cls) -> "AliasManager":
        """
        Creates an AliasManager instance with a default KMS client.

        :return: An instance of AliasManager initialized with the default KMS client.
        """
        kms_client = boto3.client("kms")
        return cls(kms_client)


    def delete_alias(self, alias: str) -> None:
        """
        Deletes an alias.

        :param alias: The alias to delete.
        """
        try:
            self.kms_client.delete_alias(AliasName=alias)
        except ClientError as err:
            logger.error(
                "Couldn't delete alias %s. Here's why: %s",
                alias,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DeleteAlias](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/DeleteAlias) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/kms#code-examples). 

```
    TRY.
        " iv_alias_name = 'alias/my-key-alias'
        lo_kms->deletealias( iv_aliasname = iv_alias_name ).
        MESSAGE 'Alias deleted successfully.' TYPE 'I'.
      CATCH /aws1/cx_kmsnotfoundexception.
        MESSAGE 'Alias not found.' TYPE 'E'.
      CATCH /aws1/cx_kmskmsinternalex.
        MESSAGE 'An internal error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DeleteAlias](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.