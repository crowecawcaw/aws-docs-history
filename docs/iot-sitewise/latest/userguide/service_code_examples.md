# Code examples for AWS IoT SiteWise using AWS SDKs

The following code examples show how to use AWS IoT SiteWise with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using AWS IoT SiteWise.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iotsitewise#code-examples").

```
public class HelloSitewise {
    private static final Logger logger = LoggerFactory.getLogger(HelloSitewise.class);
    public static void main(String[] args) {
         fetchAssetModels();
    }

    /**
     * Fetches asset models using the provided {@link IoTSiteWiseAsyncClient}.
     */
    public static void fetchAssetModels() {
        IoTSiteWiseAsyncClient siteWiseAsyncClient = IoTSiteWiseAsyncClient.create();
        ListAssetModelsRequest assetModelsRequest = ListAssetModelsRequest.builder()
            .assetModelTypes(AssetModelType.ASSET_MODEL)
            .build();

        // Asynchronous paginator - process paginated results.
        ListAssetModelsPublisher listModelsPaginator = siteWiseAsyncClient.listAssetModelsPaginator(assetModelsRequest);
        CompletableFuture<Void> future = listModelsPaginator.subscribe(response -> {
            response.assetModelSummaries().forEach(assetSummary ->
                logger.info("Asset Model Name: {} ", assetSummary.name())
            );
        });

        // Wait for the asynchronous operation to complete
        future.join();
    }
}


```

- For API details, see
  [ListAssetModels](../../../goto/SdkForJavaV2/iotsitewise-2019-12-02/ListAssetModels.md "../../../goto/SdkForJavaV2/iotsitewise-2019-12-02/ListAssetModels.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iotsitewise#code-examples").

```
import {
  paginateListAssetModels,
  IoTSiteWiseClient,
} from "@aws-sdk/client-iotsitewise";

// Call ListDocuments and display the result.
export const main = async () => {
  const client = new IoTSiteWiseClient();
  const listAssetModelsPaginated = [];
  console.log(
    "Hello, AWS Systems Manager! Let's list some of your documents:\n",
  );
  try {
    // The paginate function is a wrapper around the base command.
    const paginator = paginateListAssetModels({ client }, { maxResults: 5 });
    for await (const page of paginator) {
      listAssetModelsPaginated.push(...page.assetModelSummaries);
    }
  } catch (caught) {
    console.error(`There was a problem saying hello: ${caught.message}`);
    throw caught;
  }
  for (const { name, creationDate } of listAssetModelsPaginated) {
    console.log(`${name} - ${creationDate}`);
  }
};

// Call function if run directly.
import { fileURLToPath } from "node:url";
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  main();
}


```

- For API details, see
  [ListAssetModels](../../../AWSJavaScriptSDK/v3/latest/client/iotsitewise/command/ListAssetModelsCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iotsitewise/command/ListAssetModelsCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iotsitewise#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iotsitewise#code-examples").

```
import boto3


def hello_iot_sitewise(iot_sitewise_client):
    """
    Use the AWS SDK for Python (Boto3) to create an AWS IoT SiteWise
    client and list the asset models in your account.
    This example uses the default settings specified in your shared credentials
    and config files.

    :param iot_sitewise_client: A Boto3 AWS IoT SiteWise Client object. This object wraps
                             the low-level AWS IoT SiteWise service API.
    """
    print("Hello, AWS IoT SiteWise! Let's list some of your asset models:\n")
    paginator = iot_sitewise_client.get_paginator("list_asset_models")
    page_iterator = paginator.paginate(PaginationConfig={"MaxItems": 10})

    asset_model_names: [str] = []
    for page in page_iterator:
        for asset_model in page["assetModelSummaries"]:
            asset_model_names.append(asset_model["name"])

    print(f"{len(asset_model_names)} asset model(s) retrieved.")
    for asset_model_name in asset_model_names:
        print(f"\t{asset_model_name}")


if __name__ == "__main__":
    hello_iot_sitewise(boto3.client("iotsitewise"))


```

- For API details, see
  [ListAssetModels](../../../goto/boto3/iotsitewise-2019-12-02/ListAssetModels.md "../../../goto/boto3/iotsitewise-2019-12-02/ListAssetModels.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello AWS IoT SiteWise](example_iotsitewise_Hello_section.md "example_iotsitewise_Hello_section.md")
  - [Learn the basics](example_iotsitewise_Scenario_section.md "example_iotsitewise_Scenario_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [BatchPutAssetPropertyValue](example_iotsitewise_BatchPutAssetPropertyValue_section.md "example_iotsitewise_BatchPutAssetPropertyValue_section.md")
    - [CreateAsset](example_iotsitewise_CreateAsset_section.md "example_iotsitewise_CreateAsset_section.md")
    - [CreateAssetModel](example_iotsitewise_CreateAssetModel_section.md "example_iotsitewise_CreateAssetModel_section.md")
    - [CreateGateway](example_iotsitewise_CreateGateway_section.md "example_iotsitewise_CreateGateway_section.md")
    - [DeleteAsset](example_iotsitewise_DeleteAsset_section.md "example_iotsitewise_DeleteAsset_section.md")
    - [DeleteAssetModel](example_iotsitewise_DeleteAssetModel_section.md "example_iotsitewise_DeleteAssetModel_section.md")
    - [DeleteGateway](example_iotsitewise_DeleteGateway_section.md "example_iotsitewise_DeleteGateway_section.md")
    - [DescribeAssetModel](example_iotsitewise_DescribeAssetModel_section.md "example_iotsitewise_DescribeAssetModel_section.md")
    - [DescribeGateway](example_iotsitewise_DescribeGateway_section.md "example_iotsitewise_DescribeGateway_section.md")
    - [GetAssetPropertyValue](example_iotsitewise_GetAssetPropertyValue_section.md "example_iotsitewise_GetAssetPropertyValue_section.md")
    - [ListAssetModels](example_iotsitewise_ListAssetModels_section.md "example_iotsitewise_ListAssetModels_section.md")
