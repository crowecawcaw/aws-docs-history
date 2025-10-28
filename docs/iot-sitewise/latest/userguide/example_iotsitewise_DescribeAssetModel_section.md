# Use `DescribeAssetModel` with an AWS SDK or CLI

The following code examples show how to use `DescribeAssetModel`.

CLI

**AWS CLI**

**To describe an asset model**

The following `describe-asset-model` example describes a wind farm asset model.

```
`aws iotsitewise describe-asset-model \
 --asset-model-id `a1b2c3d4-5678-90ab-cdef-22222EXAMPLE``

```

Output:

```
{
    "assetModelId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
    "assetModelArn": "arn:aws:iotsitewise:us-west-2:123456789012:asset-model/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
    "assetModelName": "Wind Farm Model",
    "assetModelDescription": "Represents a wind farm that comprises many wind turbines",
    "assetModelProperties": [
        {
            "id": "a1b2c3d4-5678-90ab-cdef-99999EXAMPLE",
            "name": "Total Generated Power",
            "dataType": "DOUBLE",
            "unit": "kW",
            "type": {
                "metric": {
                    "expression": "sum(power)",
                    "variables": [
                        {
                            "name": "power",
                            "value": {
                                "propertyId": "a1b2c3d4-5678-90ab-cdef-66666EXAMPLE",
                                "hierarchyId": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE"
                            }
                        }
                    ],
                    "window": {
                        "tumbling": {
                            "interval": "1h"
                        }
                    }
                }
            }
        },
        {
            "id": "a1b2c3d4-5678-90ab-cdef-88888EXAMPLE",
            "name": "Region",
            "dataType": "STRING",
            "type": {
                "attribute": {
                    "defaultValue": " "
                }
            }
        }
    ],
    "assetModelHierarchies": [
        {
            "id": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE",
            "name": "Wind Turbines",
            "childAssetModelId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"
        }
    ],
    "assetModelCreationDate": 1575671284.0,
    "assetModelLastUpdateDate": 1575671988.0,
    "assetModelStatus": {
        "state": "ACTIVE"
    }
}
```

For more information, see [Describing a specific asset model](discover-asset-resources.md#describe-asset-model "discover-asset-resources.md#describe-asset-model") in the _AWS IoT SiteWise User Guide_.

- For API details, see
  [DescribeAssetModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-model.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-model.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iotsitewise#code-examples").

```
    /**
     * Retrieves the property IDs associated with a specific asset model.
     *
     * @param assetModelId the ID of the asset model that defines the properties.
     * @return a {@link CompletableFuture} that represents a {@link Map} result that associates the property name to the
     *         propert ID. The calling code can attach callbacks, then handle the result or exception by calling
     *         {@link CompletableFuture#join()} or {@link CompletableFuture#get()}.
     *         <p>
     *         If any completion stage in this method throws an exception, the method logs the exception cause and keeps
     *         it available to the calling code as a {@link CompletionException}. By calling
     *         {@link CompletionException#getCause()}, the calling code can access the original exception.
     */
    public CompletableFuture<Map<String, String>> getPropertyIds(String assetModelId) {
        ListAssetModelPropertiesRequest modelPropertiesRequest = ListAssetModelPropertiesRequest.builder().assetModelId(assetModelId).build();
        return getAsyncClient().listAssetModelProperties(modelPropertiesRequest)
            .handle((response, throwable) -> {
                if (response != null) {
                    return response.assetModelPropertySummaries().stream()
                        .collect(Collectors
                            .toMap(AssetModelPropertySummary::name, AssetModelPropertySummary::id));
                } else {
                    logger.error("Error occurred while fetching property IDs: {}.", throwable.getCause().getMessage());
                    throw (CompletionException) throwable;
                }
            });
    }


```

- For API details, see
  [DescribeAssetModel](../../../goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeAssetModel.md "../../../goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeAssetModel.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iotsitewise#code-examples").

```
import {
  DescribeAssetModelCommand,
  IoTSiteWiseClient,
} from "@aws-sdk/client-iotsitewise";
import { parseArgs } from "node:util";

/**
 * Describe an asset model.
 * @param {{ assetModelId : string }}
 */
export const main = async ({ assetModelId }) => {
  const client = new IoTSiteWiseClient({});
  try {
    const { assetModelDescription } = await client.send(
      new DescribeAssetModelCommand({
        assetModelId: assetModelId, // The ID of the Gateway to describe.
      }),
    );
    console.log("Asset model information retrieved successfully.");
    return { assetModelDescription: assetModelDescription };
  } catch (caught) {
    if (caught instanceof Error && caught.name === "ResourceNotFound") {
      console.warn(
        `${caught.message}. The asset model could not be found. Please check the asset model id.`,
      );
    } else {
      throw caught;
    }
  }
};


```

- For API details, see
  [DescribeAssetModel](../../../AWSJavaScriptSDK/v3/latest/client/iotsitewise/command/DescribeAssetModelCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iotsitewise/command/DescribeAssetModelCommand.md")
  in _AWS SDK for JavaScript API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
