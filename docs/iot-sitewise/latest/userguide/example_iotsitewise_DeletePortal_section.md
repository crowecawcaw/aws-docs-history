# Use `DeletePortal` with an AWS SDK or CLI

The following code examples show how to use `DeletePortal`.

CLI

**AWS CLI**

**To delete a portal**

The following `delete-portal` example deletes a web portal for a wind farm company.

```
`aws iotsitewise delete-portal \
 --portal-id `a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE``

```

Output:

```
{
    "portalStatus": {
        "state": "DELETING"
    }
}
```

For more information, see [Deleting a portal](administer-portals.md#portal-delete-portal "administer-portals.md#portal-delete-portal") in the _AWS IoT SiteWise User Guide_.

- For API details, see
  [DeletePortal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-portal.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-portal.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iotsitewise#code-examples").

```
    /**
     * Deletes a portal.
     *
     * @param portalId the ID of the portal to be deleted.
     * @return a {@link CompletableFuture} that represents a {@link DeletePortalResponse}. The calling code can attach
     *         callbacks, then handle the result or exception by calling {@link CompletableFuture#join()} or
     *         {@link CompletableFuture#get()}.
     *         <p>
     *         If any completion stage in this method throws an exception, the method logs the exception cause and keeps
     *         it available to the calling code as a {@link CompletionException}. By calling
     *         {@link CompletionException#getCause()}, the calling code can access the original exception.
     */
    public CompletableFuture<DeletePortalResponse> deletePortalAsync(String portalId) {
        DeletePortalRequest deletePortalRequest = DeletePortalRequest.builder()
            .portalId(portalId)
            .build();

        return getAsyncClient().deletePortal(deletePortalRequest)
            .whenComplete((response, exception) -> {
                if (exception != null) {
                    logger.error("Failed to delete portal with ID: {}. Error: {}", portalId, exception.getCause().getMessage());
                }
            });
    }


```

- For API details, see
  [DeletePortal](../../../goto/SdkForJavaV2/iotsitewise-2019-12-02/DeletePortal.md "../../../goto/SdkForJavaV2/iotsitewise-2019-12-02/DeletePortal.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iotsitewise#code-examples").

```
import {
  DeletePortalCommand,
  IoTSiteWiseClient,
} from "@aws-sdk/client-iotsitewise";
import { parseArgs } from "node:util";

/**
 * List asset models.
 * @param {{ portalId : string }}
 */
export const main = async ({ portalId }) => {
  const client = new IoTSiteWiseClient({});
  try {
    await client.send(
      new DeletePortalCommand({
        portalId: portalId, // The id of the portal.
      }),
    );
    console.log("Portal deleted successfully.");
    return { portalDeleted: true };
  } catch (caught) {
    if (caught instanceof Error && caught.name === "ResourceNotFound") {
      console.warn(
        `${caught.message}. There was a problem deleting the portal. Please check the portal id.`,
      );
    } else {
      throw caught;
    }
  }
};


```

- For API details, see
  [DeletePortal](../../../AWSJavaScriptSDK/v3/latest/client/iotsitewise/command/DeletePortalCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iotsitewise/command/DeletePortalCommand.md")
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


    def delete_portal(self, portal_id: str) -> None:
        """
        Deletes an AWS IoT SiteWise Portal.

        :param portal_id: The ID of the portal to delete.
        """
        try:
            self.iotsitewise_client.delete_portal(portalId=portal_id)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Portal %s does not exist.", portal_id)
            else:
                logger.error(
                    "Error deleting portal %s. Here's why %s",
                    portal_id,
                    err.response["Error"]["Message"],
                )
            raise



```

- For API details, see
  [DeletePortal](../../../goto/boto3/iotsitewise-2019-12-02/DeletePortal.md "../../../goto/boto3/iotsitewise-2019-12-02/DeletePortal.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
