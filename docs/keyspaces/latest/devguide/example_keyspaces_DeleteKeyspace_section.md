# Use `DeleteKeyspace` with an AWS SDK

The following code examples show how to use `DeleteKeyspace`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](example_keyspaces_Scenario_GetStartedKeyspaces_section.md "example_keyspaces_Scenario_GetStartedKeyspaces_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Keyspaces#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Keyspaces#code-examples").

```
    /// <summary>
    /// Delete an existing keyspace.
    /// </summary>
    /// <param name="keyspaceName"></param>
    /// <returns>A Boolean value indicating the success of the action.</returns>
    public async Task<bool> DeleteKeyspace(string keyspaceName)
    {
        var response = await _amazonKeyspaces.DeleteKeyspaceAsync(
            new DeleteKeyspaceRequest { KeyspaceName = keyspaceName });
        return response.HttpStatusCode == HttpStatusCode.OK;
    }



```

- For API details, see
  [DeleteKeyspace](../../../goto/DotNetSDKV3/keyspaces-2022-02-10/DeleteKeyspace.md "../../../goto/DotNetSDKV3/keyspaces-2022-02-10/DeleteKeyspace.md")
  in _AWS SDK for .NET API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/keyspaces#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/keyspaces#code-examples").

```
    public static void deleteKeyspace(KeyspacesClient keyClient, String keyspaceName) {
        try {
            DeleteKeyspaceRequest deleteKeyspaceRequest = DeleteKeyspaceRequest.builder()
                    .keyspaceName(keyspaceName)
                    .build();

            keyClient.deleteKeyspace(deleteKeyspaceRequest);

        } catch (KeyspacesException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }


```

- For API details, see
  [DeleteKeyspace](../../../goto/SdkForJavaV2/keyspaces-2022-02-10/DeleteKeyspace.md "../../../goto/SdkForJavaV2/keyspaces-2022-02-10/DeleteKeyspace.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/keyspaces#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/keyspaces#code-examples").

```
suspend fun deleteKeyspace(keyspaceNameVal: String?) {
    val deleteKeyspaceRequest =
        DeleteKeyspaceRequest {
            keyspaceName = keyspaceNameVal
        }

    KeyspacesClient.fromEnvironment { region = "us-east-1" }.use { keyClient ->
        keyClient.deleteKeyspace(deleteKeyspaceRequest)
    }
}


```

- For API details, see
  [DeleteKeyspace](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/keyspaces#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/keyspaces#code-examples").

```
class KeyspaceWrapper:
    """Encapsulates Amazon Keyspaces (for Apache Cassandra) keyspace and table actions."""

    def __init__(self, keyspaces_client):
        """
        :param keyspaces_client: A Boto3 Amazon Keyspaces client.
        """
        self.keyspaces_client = keyspaces_client
        self.ks_name = None
        self.ks_arn = None
        self.table_name = None

    @classmethod
    def from_client(cls):
        keyspaces_client = boto3.client("keyspaces")
        return cls(keyspaces_client)


    def delete_keyspace(self):
        """
        Deletes the keyspace.
        """
        try:
            self.keyspaces_client.delete_keyspace(keyspaceName=self.ks_name)
            self.ks_name = None
        except ClientError as err:
            logger.error(
                "Couldn't delete keyspace %s. Here's why: %s: %s",
                self.ks_name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [DeleteKeyspace](../../../goto/boto3/keyspaces-2022-02-10/DeleteKeyspace.md "../../../goto/boto3/keyspaces-2022-02-10/DeleteKeyspace.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
