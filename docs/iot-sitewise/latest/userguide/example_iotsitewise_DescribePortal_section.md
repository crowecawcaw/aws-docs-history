# Use `DescribePortal` with an AWS SDK or CLI

The following code examples show how to use `DescribePortal`.

CLI

**AWS CLI**

**To describe a portal**

The following `describe-portal` example describes a web portal for a wind farm company.

```
`aws iotsitewise describe-portal \
 --portal-id `a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE``

```

Output:

```
{
    "portalId": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE",
    "portalArn": "arn:aws:iotsitewise:us-west-2:123456789012:portal/a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE",
    "portalName": "WindFarmPortal",
    "portalDescription": "A portal that contains wind farm projects for Example Corp.",
    "portalClientId": "E-a1b2c3d4e5f6_a1b2c3d4e5f6EXAMPLE",
    "portalStartUrl": "https://a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE.app.iotsitewise.aws",
    "portalContactEmail": "support@example.com",
    "portalStatus": {
        "state": "ACTIVE"
    },
    "portalCreationDate": "2020-02-04T23:01:52.90248068Z",
    "portalLastUpdateDate": "2020-02-04T23:01:52.90248078Z",
    "roleArn": "arn:aws:iam::123456789012:role/MySiteWiseMonitorServiceRole"
}
```

For more information, see [Administering your portals](administer-portals.md "administer-portals.md") in the _AWS IoT SiteWise User Guide_.

- For API details, see
  [DescribePortal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-portal.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-portal.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iotsitewise#code-examples").

```
    /**
     * Retrieves a portal's description.
     *
     * @param portalId the ID of the portal to describe.
     * @return a {@link CompletableFuture} that represents a {@link String} result of the portal's start URL
     *         (see: {@link DescribePortalResponse#portalStartUrl()}). The calling code can attach callbacks, then handle the
     *         result or exception by calling {@link CompletableFuture#join()} or {@link CompletableFuture#get()}.
     *         <p>
     *         If any completion stage in this method throws an exception, the method logs the exception cause and keeps
     *         it available to the calling code as a {@link CompletionException}. By calling
     *         {@link CompletionException#getCause()}, the calling code can access the original exception.
     */
    public CompletableFuture<String> describePortalAsync(String portalId) {
        DescribePortalRequest request = DescribePortalRequest.builder()
            .portalId(portalId)
            .build();

        return getAsyncClient().describePortal(request)
            .handle((response, exception) -> {
                if (exception != null) {
                   logger.error("An exception occurred retrieving the portal description: {}", exception.getCause().getMessage());
                   throw (CompletionException) exception;
                }
                return response.portalStartUrl();
            });
    }


```

- For API details, see
  [DescribePortal](../../../goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribePortal.md "../../../goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribePortal.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iotsitewise#code-examples").

```
import {
  DescribePortalCommand,
  IoTSiteWiseClient,
} from "@aws-sdk/client-iotsitewise";
import { parseArgs } from "node:util";

/**
 * Describe a portal.
 * @param {{ portalId: string }}
 */
export const main = async ({ portalId }) => {
  const client = new IoTSiteWiseClient({});
  try {
    const result = await client.send(
      new DescribePortalCommand({
        portalId: portalId, // The ID of the Gateway to describe.
      }),
    );
    console.log("Portal information retrieved successfully.");
    return result;
  } catch (caught) {
    if (caught instanceof Error && caught.name === "ResourceNotFound") {
      console.warn(
        `${caught.message}. The Portal could not be found. Please check the Portal Id.`,
      );
    } else {
      throw caught;
    }
  }
};


```

- For API details, see
  [DescribePortal](../../../AWSJavaScriptSDK/v3/latest/client/iotsitewise/command/DescribePortalCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iotsitewise/command/DescribePortalCommand.md")
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


    def create_gateway(self, gateway_name: str, my_thing: str) -> str:
        """
        Creates an AWS IoT SiteWise Gateway.

        :param gateway_name: The name of the gateway to create.
        :param my_thing: The core device thing name.
        :return: The ID of the created gateway.
        """
        try:
            response = self.iotsitewise_client.create_gateway(
                gatewayName=gateway_name,
                gatewayPlatform={
                    "greengrassV2": {"coreDeviceThingName": my_thing},
                },
                tags={"Environment": "Production"},
            )
            gateway_id = response["gatewayId"]
            return gateway_id
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceAlreadyExistsException":
                logger.error("Gateway %s already exists.", gateway_name)
            else:
                logger.error(
                    "Error creating gateway %s. Here's why %s",
                    gateway_name,
                    err.response["Error"]["Message"],
                )
            raise



```

- For API details, see
  [DescribePortal](../../../goto/boto3/iotsitewise-2019-12-02/DescribePortal.md "../../../goto/boto3/iotsitewise-2019-12-02/DescribePortal.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
