# Use `DeleteGateway` with an AWS SDK or CLI

The following code examples show how to use `DeleteGateway`.

CLI

**AWS CLI**

**To delete a gateway**

The following `delete-gateway` example deletes a gateway.

```
`aws iotsitewise delete-gateway \
 --gateway-id `a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE``

```

This command produces no output.

For more information, see [Ingesting data using a gateway](gateways.md "gateways.md") in the _AWS IoT SiteWise User Guide_.

- For API details, see
  [DeleteGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-gateway.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-gateway.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iotsitewise#code-examples").

```
    /**
     * Deletes the specified gateway.
     *
     * @param gatewayId the ID of the gateway to delete.
     * @return a {@link CompletableFuture} that represents a {@link DeleteGatewayResponse} result.. The calling code
     *         can attach callbacks, then handle the result or exception by calling {@link CompletableFuture#join()} or
     *         {@link CompletableFuture#get()}.
     *         <p>
     *         If any completion stage in this method throws an exception, the method logs the exception cause and keeps
     *         it available to the calling code as a {@link CompletionException}. By calling
     *         {@link CompletionException#getCause()}, the calling code can access the original exception.
     */
    public CompletableFuture<DeleteGatewayResponse> deleteGatewayAsync(String gatewayId) {
        DeleteGatewayRequest deleteGatewayRequest = DeleteGatewayRequest.builder()
            .gatewayId(gatewayId)
            .build();

        return getAsyncClient().deleteGateway(deleteGatewayRequest)
            .whenComplete((response, exception) -> {
                if (exception != null) {
                    logger.error("Failed to delete gateway: {}", exception.getCause().getMessage());
                }
            });
    }


```

- For API details, see
  [DeleteGateway](../../../goto/SdkForJavaV2/iotsitewise-2019-12-02/DeleteGateway.md "../../../goto/SdkForJavaV2/iotsitewise-2019-12-02/DeleteGateway.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iotsitewise#code-examples").

```
import {
  DeleteGatewayCommand,
  IoTSiteWiseClient,
} from "@aws-sdk/client-iotsitewise";
import { parseArgs } from "node:util";

/**
 * Create an SSM document.
 * @param {{ content: string, name: string, documentType?: DocumentType }}
 */
export const main = async ({ gatewayId }) => {
  const client = new IoTSiteWiseClient({});
  try {
    await client.send(
      new DeleteGatewayCommand({
        gatewayId: gatewayId, // The ID of the Gateway to describe.
      }),
    );
    console.log("Gateway deleted successfully.");
    return { gatewayDeleted: true };
  } catch (caught) {
    if (caught instanceof Error && caught.name === "ResourceNotFound") {
      console.warn(
        `${caught.message}. The Gateway could not be found. Please check the Gateway Id.`,
      );
    } else {
      throw caught;
    }
  }
};


```

- For API details, see
  [DeleteGateway](../../../AWSJavaScriptSDK/v3/latest/client/iotsitewise/command/DeleteGatewayCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iotsitewise/command/DeleteGatewayCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iotsitewise#code-examples").

```
class IoTSitewiseWrapper:
    """Encapsulates AWS IoT SiteWise actions using the client interface."""

    def __init__(self, iotsitewise_client: client) -> None:
        """
        Initializes the IoTSitewiseWrapper with an AWS IoT SiteWise client.

        :param iotsitewise_client: A Boto3 AWS IoT SiteWise client. This client provides low-level
                           access to AWS IoT SiteWise services.
        """
        self.iotsitewise_client = iotsitewise_client
        self.entry_id = 0 # Incremented to generate unique entry IDs for batch_put_asset_property_value.

    @classmethod
    def from_client(cls) -> "IoTSitewiseWrapper":
        """
        Creates an IoTSitewiseWrapper instance with a default AWS IoT SiteWise client.

        :return: An instance of IoTSitewiseWrapper initialized with the default AWS IoT SiteWise client.
        """
        iotsitewise_client = boto3.client("iotsitewise")
        return cls(iotsitewise_client)


    def delete_gateway(self, gateway_id: str) -> None:
        """
        Deletes an AWS IoT SiteWise Gateway.

        :param gateway_id: The ID of the gateway to delete.
        """
        try:
            self.iotsitewise_client.delete_gateway(gatewayId=gateway_id)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Gateway %s does not exist.", gateway_id)
            else:
                logger.error(
                    "Error deleting gateway %s. Here's why %s",
                    gateway_id,
                    err.response["Error"]["Message"],
                )
            raise



```

- For API details, see
  [DeleteGateway](../../../goto/boto3/iotsitewise-2019-12-02/DeleteGateway.md "../../../goto/boto3/iotsitewise-2019-12-02/DeleteGateway.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
