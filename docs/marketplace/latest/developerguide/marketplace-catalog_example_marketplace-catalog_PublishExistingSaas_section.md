The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Publish a SaaS product and associated public offer from an existing draft using an AWS SDK

The following code example shows how to publish a SaaS product and associated public offer from an existing draft. The product will be in a limited state by default.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#catalog-api-reference-code "https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#catalog-api-reference-code")
repository.

```
{
    "Catalog":"AWSMarketplace",
    "ChangeSet": [
        {
            "ChangeType": "UpdateVisibility",
            "ChangeName": "CreateProductChange",
            "Entity": {
                "Type": "SaaSProduct@1.0",
                "Identifier": "prod-1111111111111"
            },
            "DetailsDocument": {
                "TargetVisibility": "Public"
            }
        }
    ]
}


```

- For API details, see
  [StartChangeSet](../../../goto/SdkForJavaV2/marketplace-catalog-2018-09-17/StartChangeSet.md "../../../goto/SdkForJavaV2/marketplace-catalog-2018-09-17/StartChangeSet.md")
  in _AWS SDK for Java 2.x API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
