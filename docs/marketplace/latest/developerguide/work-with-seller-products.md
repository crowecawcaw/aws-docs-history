

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with seller products
<a name="work-with-seller-products"></a>

You can use the AWS Marketplace Catalog API to automate tasks for working with seller products. This includes the ability to create, update, view, list, and sort products. This enables you to automate product management. For example, you can provide self-service publishing capabilities on the AWS Marketplace Management Portal.

A *product* is a unit or resource that you intend to sell in AWS Marketplace, often referred to as a base product. Buyers can't consume a base product until you add product information, deployment attributes, and billing information.

A *product* describes the product information, software deployment attributes, and billing mechanism of the listing that you intend to sell. The *product* must be paired with an *offer* to become a transactable unit that you can sell and buyers can use in AWS Marketplace.

You can also use the AWS Marketplace Catalog API to:
+ [Work with private offers using the AWS Marketplace APIs](work-with-private-offers.md)
+ [Work with resale authorizations using the AWS Marketplace APIs](work-with-resale-authorizations.md)
+ [Work with channel partner private offers using the AWS Marketplace APIs](work-with-cppos.md)

Each product type has a different product entity. An *entity* can be a product or an offer on AWS Marketplace. The following product types and entities are supported: 


| Product type | Entity | 
| --- | --- | 
| Amazon Machine Image (AMI) products | AmiProduct@1.0 | 
| Container products | ContainerProduct@1.0 | 
| Software as a service (SaaS) products | SaaSProduct@1.0 | 
| Machine learning (ML) products | MachineLearningProduct@1.0 | 

**Note**  
Single-AMI with CloudFormation product types, AWS Data Exchange data products, and professional services products are not supported.

The following topics assume you have access to the API and have completed any seller prerequisites, as described in [Access control for the AWS Marketplace Catalog API](catalog-api-access-control.md).

See the following resources:
+ To understand the basics of using the AWS Marketplace Catalog API, see [Using the AWS Marketplace Catalog API](catalog-apis.md).
+ For end-to-end labs with working code examples, see [Manage products with API](https://catalog.workshops.aws/mpseller/en-US/manage-products-with-api) in the *AWS Marketplace seller workshop*.
+ For code examples of API requests, see [Python](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/python/src/catalog_api/products) and [Java](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java/resources/changeSets/products) examples in *AWS Samples* on GitHub.

The following topics describe how to use the Catalog API to perform actions on your single-AMI products, container-based products, or SaaS products.

**Topics**
+ [Create a product](#create-product)
+ [Update product details](#update-information)
+ [Add pricing dimensions](#add-dimensions)
+ [Update pricing dimensions](#update-dimensions)
+ [Restrict pricing dimensions](#restrict-dimensions)
+ [Update targeting configuration](#update-targeting)
+ [Update product visibility](#update-visibility)
+ [Publish a product](#release-product)
+ [Find your product ID](#seller-product-id)
+ [Change set status and errors](#seller-product-change-set-errors)
+ [Work with AMI-based products](work-with-single-ami-products.md)
+ [Work with EC2 Image Builder component products](work-with-ec2-image-builder-products.md)
+ [Work with container-based products using the AWS Marketplace APIs](work-with-container-products.md)
+ [Work with SaaS products using the AWS Marketplace APIs](work-with-saas-products.md)
+ [Work with machine learning products using AWS Marketplace APIs](work-with-ml-products.md)

## Create a product
<a name="create-product"></a>

**Note**  
This change type is only needed when you intend to create a brand new product entity in the AWS Marketplace catalog. It is not needed when updating existing products.

You can use the Catalog API to create an AMI, container, machine learning, or SaaS product document with identifiers (product code and product ID) in AWS Marketplace. 

You create a product in `Draft` state by calling the `StartChangeSet` API operation with the `CreateProduct` change type. 

If your request is processed successfully, then AWS Marketplace Catalog API generates a product in `Draft` state for you. This is an incomplete product and isn't visible to buyers in AWS Marketplace. 

You then use `Update` change types to complete the create product process: [UpdateInformation](#update-information), [UpdateDimensions](#update-dimensions), [UpdateTargeting](#update-targeting), and [UpdateVisibility](#update-visibility). 

After the product is completed, you can use the [ReleaseProduct](#release-product) change type to complete the product creation process, and then release the offer. This process validates the entire product and moves the product to the `Limited` state.

**Note**  
For more information about creating a product using the AWS Marketplace Management Portal, see the following topics in the *AWS Marketplace Seller Guide*:  
[Create your single-AMI product](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#ami-create-product)  
You cannot update the AMI for the version. If you need to update the AMI, create a new version instead.
[Creating a container product](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#create-container-product)
[Creating a SaaS product](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-create-product.html)
 [Creating a machine learning product](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-creating-your-listing.html) 
If you use the AWS Marketplace Management Portal to create a product, the product will be in the `Staging` state.

To create a product in `Draft` state, call the `StartChangeSet` API operation with the `CreateProduct` change type, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
"Catalog": "AWSMarketplace",
"ChangeSet": [ 
  { 
    "ChangeType":"CreateProduct",
    "Entity":{
      "Type": "SaaSProduct@1.0" // choose from ["AmiProduct@1.0", "ContainerProduct@1.0", "SaaSProduct@1.0", "MachineLearningProduct@1.0"]
     },
     "DetailsDocument": {
        "ProductTitle": "{{Test product title set in CreateProduct}}"
     }
  }
]
}
```

Provide information for the fields to add the `CreateProduct` change type. This change type can take in `ProductTitle` attribute, subject to the same restrictions as that sent into `UpdateInformation` change type.
+ `Entity` (object) (required) – The named type of object being created.
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`, `ContainerProduct@1.0`, `MachineLearningProduct@1.0` or `SaaSProduct@1.0`. For more information, see [Identifier](catalog-apis.md#identifier). 
+ `DetailsDocument` (object) (required) – It may be empty.
  + `ProductTitle` (optional) – The title for your product, max length is 72 characters. Note that you can also later set or update the product title via the `UpdateInformation` change type.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

When the request is complete (if the `Status` is `SUCCEEDED`), a new `ProductId` is generated.

**Synchronous Validations**

The following schema validations are specific to `CreateProduct` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| ProductTitle (string) | Max length: 72 | 400 | 

**Asynchronous Errors**  
The following errors are specific to `CreateProduct` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more details about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INVALID\_INPUT | Inappropriate content '{InappropriateContent}' found in ProductTitle field. Provide ProductTitle with no inappropriate content. | 

## Update product details
<a name="update-information"></a>

If you already have a product in AWS Marketplace, you can use the Catalog API to update the product details for an AMI, container, ML, or SaaS product. 

**Note**  
For more information about updating the product details using the AWS Marketplace Management Portal, see the following topics in the *AWS Marketplace Seller Guide*:  
AMI-based product: [Update product information](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-updating-product)
Container-based product: [Creating or updating product information for your container product](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#container-product-updating-version)
SaaS-based product: [Update product information](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-product-settings.html#update-product-information)
Machine learning product: [Updating product information](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-update-product.html)

To update product details, call the `StartChangeSet` API operation with the `UpdateInformation` change type and the details that you want to change, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateInformation",
      "Entity":
      {
        "Identifier": "{{prod-example12345}}",
        "Type": "AmiProduct@1.0"
      },
      "DetailsDocument":
      {
        "ProductTitle": "{{My Product Title}}",
        "ShortDescription": "{{My product short description.}}",
        "LongDescription": "{{My product longer description.}}",
        "Sku": "{{123example456}}",
        "LogoUrl": "https://awsmp-logos.s3.amazonaws.com/{{ca60b754fe05a24257176cdbf31c4e0d}}",
        "VideoUrls":
        [
          "https://{{example.com/my-video}}"
        ],
        "Highlights":
        [
          "{{123example45}}"
        ],
        "AdditionalResources":
        [
          {
            "Text": "{{123example456}}",
            "Url": "https://{{example.com/some-link}}"
          }
        ],
        "SupportDescription": "{{Need help? Contact our experts at support@example.com \n\nYour purchase includes 24x7 support.}}",
        "Categories":
        [
          "Operating Systems",
          "Network Infrastructure",
          "Application Development"
        ],
        "SearchKeywords":
        [
          "{{123example456}}"
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateInformation` change type:
+ `Entity` (object) (required) – The named type of entity being created.
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`, `ContainerProduct@1.0`, `MachineLearningProduct@1.0`, or `SaaSProduct@1.0`. 
+ `DetailsDocument` (object) (required) – The details of the request including the information that you want to update for your product. Each field is optional, but you must include at least one change to update.
  + `ProductTitle` (string) – The name of the product to be displayed to buyers.
  + `ShortDescription` (string) – The description of key aspects of the product to be displayed to buyers. This is usually 2–3 sentences.
  + `LongDescription` (string) – The longer description of your product to be displayed to buyers. This is usually 1–3 paragraphs.
  + `Sku` (string or null) – The free-form string that you define as a reference for your own use. Use `null` to unset this field.
  + `LogoUrl` (string) – The URL to an image in a publicly accessible Amazon Simple Storage Service (Amazon S3) bucket. For more information, see [Company and product logo requirements](https://docs.aws.amazon.com/marketplace/latest/userguide/product-submission.html#seller-and-product-logos).
  + `VideoUrls` (array of strings) – The list of URLs to publicly available, externally hosted videos to be provided as a reference to buyers in your product information.
**Note**  
Currently, AWS Marketplace supports one URL in the array.
  + `Highlights` (array of strings) – The list of short callouts for key product features.
  + `AdditionalResources` (array of structures) – The list of references to additional resources to learn about your product. Each reference is made up of a text name and a URL:
    + `Text` (string) – The name or title of the resource.
    + `Url` (string) – The URL to a resource that might be helpful for a buyer to understand your product.
  + `SupportDescription` (string) – The details about your support offering for your product.
  + `Categories` (array of strings) – The list of AWS Marketplace defined product categories that describe your product. For more information, see [Product categories](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-product-categories.html) in the *AWS Marketplace Buyer Guide*.
  + `SearchKeywords` (array of strings) – The list of keywords for your product to enhance the search experience. Seller name, product name, and product categories are automatically included in search keywords and don't need to be repeated here.

**Note**  
When you are initially populating product information (metadata) for a `Draft` product, you will need to supply all of the following in the `DetailsDocument` object of `UpdateInformation` change type: `ProductTitle`, `ShortDescription`, `LongDescription`, `LogoUrl`, `Highlights`, `AdditionalResources`, `SupportDescription`, `Categories`, and `SearchKeywords`.   
The `ProductTitle` can be omitted if it has already been provided during `CreateProduct` change type. However, when you are updating existing fields on the product, you can include only the attributes that need to be changed in the `DetailsDocument` object of the `UpdateInformation` change type. 

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed.

To check request status, use the AWS Marketplace Management Portal or call the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API.

**Synchronous Validations**

The following schema validations are specific to `UpdateInformation` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| String (general)  | No control characters "\\\\x00-\\\\x08\\\\x0B-\\\\x1F" | 400 | 
| ProductTitle (string) | Max length: 72 Required | 400 | 
| ShortDescription (string) | Max length: 1000 Required | 400 | 
| LongDescription (string) | Max length: 5000 Required | 400 | 
| Sku (string) | Max length: 100 Optional | 400 | 
| LogoUrl (string) | URL pattern: <br />^https://(www\\.)?[-a-zA-Z0- 9@.]{1,256}\\.[a-zA-Z0-9()]{2,63}\\b([-a-zA- Z0-9@\+./]\*)<br />Required | 400 | 
| VideoUrls (array of strings) | URL pattern: <br />https://(www\\\\.)?[-a-zA-Z0- 9@.\_]{1,256}\\\\.[a-zA-Z0-9()]{2,63}\\\\b([-a-zA-Z0-9@\_\+.\\/] <br />Optional | 400 | 
| Highlights (array of strings) | Required: Min 1 - Max 3 | 400 | 
| AdditionalResources (array of structures) | Max length: 500 Optional | 400 | 
| SupportDescription (string) | Max length: 2000Required | 400 | 
| Categories (array of strings) | Min 1 - Max 3 Required | 400 | 
| SearchKeywords (array of strings) | Min 1 - Max 15 Max 50 chars for each item<br />Required | 400 | 

**Asynchronous Errors**

The following errors are specific to `UpdateInformation` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| MISSING\_DATA  | No data provided to perform an update. Provide data for at least 1 field of the product.  | 
| INVALID\_INPUT | Provide LogoUrl. | 
| INVALID\_INPUT | Provide ProductTitle. | 
| INVALID\_INPUT | Provide ShortDescription. | 
| INVALID\_INPUT | Provide LongDescription. | 
| INVALID\_INPUT | Provide SupportDescription. | 
| INVALID\_INPUT | Provide at least one search keyword. | 
| INVALID\_INPUT | Provide at least one highlight. | 
| INVALID\_INPUT | Provide between 1 and 3 product categories. | 
| INVALID\_INPUT | Inappropriate content '{InappropriateContent}' found in ProductTitle field. Provide ProductTitle with no inappropriate content. | 
| INVALID\_INPUT | Inappropriate content '{InappropriateContent}' found in ShortDescription field. Provide ShortDescription with no inappropriate content. | 
| INVALID\_INPUT | Inappropriate content '{InappropriateContent}' found in LongDescription field. Provide LongDescription with no inappropriate content. | 
| INVALID\_INPUT | Inappropriate content '{InappropriateContent}' found in SupportDescription field. Provide SupportDescription with no inappropriate content. | 
| INVALID\_INPUT | Invalid ProductTitle field. Remove spaces before trademark symbol. | 
| INVALID\_INPUT | Invalid ShortDescription field. Remove spaces before trademark symbol. | 
| INVALID\_INPUT | Invalid LongDescription field. Remove spaces before trademark symbol. | 
| INVALID\_INPUT | Invalid SupportDescription field. Remove spaces before trademark symbol. | 
| INVALID\_INPUT | Invalid ProductTitle field. Remove unsupported characters [UnsupportedCharacters]. | 
| INVALID\_INPUT | Invalid ShortDescription field. Remove unsupported characters [UnsupportedCharacters]. | 
| INVALID\_INPUT | Invalid LongDescription field. Remove unsupported characters [UnsupportedCharacters]. | 
| INVALID\_INPUT | Invalid SupportDescription field. Remove unsupported characters [UnsupportedCharacters]. | 
| INVALID\_INPUT | Search keywords must be no more than 250 combined characters. | 
| INVALID\_INPUT | The input for this change type could not be read. Submit a properly formatted input. | 
| INVALID\_ADDITIONAL\_RESOURCES | Invalid URLs in AdditionalResources: [InvalidAdditionalResourcesUrls] Provide valid URLs. | 
| INVALID\_CATEGORY\_NAMES | Provide valid category names supported by AWS Marketplace. | 
| InvalidImageProperties | Validation errors found: The file is not image type. Supported image types: [png\|jpg\|gif]. | 
| EXPLICIT\_CONTENT | Explicit content: '{ExplicitContent}' detected. Provide media with no explicit content. | 
| INVALID\_MEDIA | Invalid URL: {MediaUrl} Provide a new URL for media stored in S3. | 
| INVALID\_MEDIA | Invalid URL: {MediaUrl} Provide a valid URL that does not exceed 2048 characters. | 
| INVALID\_MEDIA | Location provided not accessible: {MediaUrl} Provide an accessible URL for media stored in S3. | 
| INVALID\_MEDIA | There was an issue copying the media from S3. Image size exceeds 5 MB. Provide an image that is under 5 MB. | 
| INVALID\_MEDIA | Malware detected in media. Please resubmit media without malware. | 
| TOO\_MANY\_MEDIA | Provide no more than 15 media items. | 
| DUPLICATE\_MEDIA | Duplicate media is not allowed for a product. Please provide media with no duplicates. | 

## Add pricing dimensions
<a name="add-dimensions"></a>

You can use the [AWS Marketplace Catalog Service Actions](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Catalog_Service.html) to add billable pricing dimensions that enable you to charge users for AMI, container, or SaaS products.

A *pricing dimension* is a unit of measure that sellers define for charging buyers. Sellers must set up this information to bill buyers for using the product, whether it's a usage-based or contract-based pricing model. The type of dimension depends on the product's pricing model. 

**Note**  
For SaaS products with Free pricing model, you must create at least one dimension with UsageBasedPricingTerm or ConfigurableUpfrontPricingTerm, and all dimensions must be priced at $0.00. This requirement is unique to SaaS products and does not apply to AMI, container, or machine learning products.

**Note**  
New pricing dimensions have the following impacts on SaaS buyers:  
For buyers with agreements created from public offers, you can report consumption on the new dimensions even though they did not exist in the offer when the agreement was created.
For buyers with agreements created from private offers, you can't report consumption on the new dimensions because they did not exist in the private offer when the agreement was created. Calls to the [BatchMeterUsage](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_BatchMeterUsage.html) API will succeed, but the buyer will not be billed, so you must keep track of which buyer can and cannot be billed for any new dimensions. You can also use the [GetAgreementTerms](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementTerms.html) API to see the dimensions included in each buyer agreement.  
To report consumption on a new dimension and bill the buyer, you must [extend a replacement offer](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-upgrades-and-renewals.html#private-offers-upgrades-and-renewals-supported-products) that includes the dimension, and the buyer must accept the offer.

For more information about product pricing, see the following topics in the *AWS Marketplace Seller Guide*:
+ [AMI product pricing](https://docs.aws.amazon.com/marketplace/latest/userguide/pricing-ami-products.html)
+ [Container products pricing](https://docs.aws.amazon.com/marketplace/latest/userguide/pricing-container-products.html)
+ [SaaS product pricing](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-pricing-models.html)
+ [Machine learning product pricing](https://docs.aws.amazon.com/marketplace/latest/userguide/machine-learning-pricing.html)

For more information about adding pricing dimensions using the AWS Marketplace Management Portal, see the following topics in the *AWS Marketplace Seller Guide*:
+ AMI-based products: [Update pricing](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-update-product-pricing).
+ Container-based products: [Adding a pricing dimension](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#container-add-pricing-dimensions).
+ SaaS-based products: [Add pricing dimensions](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-product-settings.html#saas-add-pricing-dimensions).
+ ML products: Not supported. Machine learning products have fixed pricing dimensions. However, you can [Update pricing](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-update-product-pricing).

To add pricing dimensions, call the `StartChangeSet` API with the `AddDimensions` change type, as shown in the following example.

**Note**  
After submitting the first `AddDimensions` change type with dimensions specifying a type of pricing model—usage, contract, or contract with consumption— you must work with the AWS Marketplace Seller Operations team. They help you add a dimension with types that are outside of the original pricing model.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "AddDimensions",
      "DetailsDocument":
      [
        {
          "Description": "{{Description of the dimension}}",
          "Key": "{{UniqueApiKey}}",
          "Unit": "HostHrs",
          "Name": "{{First Dimension}}",
          "Types":
          [
            "ExternallyMetered"
          ]
        }
      ],
      "Entity":
      {
        "Identifier": "{{prod-example12345}}",
        "Type": "SaaSProduct@1.0"
      }
    }
  ]
}
```

Provide the following fields for the `AddDimensions` change type.
+ `DetailsDocument` (array of objects) (required) – Details of the request. 
  + `Description` (string) (required) – Full details of the dimension that will be the long description on the buyer's viewing page.
  + `Key` (string) (required) – Enter in the facet that will be used for defining the rates in the offer. Also, enter the dimensions published to the AWS Marketplace Metering Service (MMS) if the dimension can't be metered externally. After the dimension is created, this can't be changed.
  + `Units` (string) (required) – The unit type for the dimension. Possible units are Users, Hosts, GB, MB, TB, Gbps, Mbps, Requests, Units, UserHrs, UnitHrs, Units, HostHrs, TierHrs, and TaskHrs.
  + `Name` (string) (required) – The display name for the dimension on the website and customer's bill.
    + `Types` (array of strings) (required) (also known as **Tags**) – These indicate whether the dimension covers metering, entitlement, or support for external metering. This is not changeable after the dimension is created.
    + 
      + `Metered` – Indicates that Commerce Platform usage types should be created to allow metering to occur for this dimension.
      + `ExternallyMetered` – Indicates that AWS Marketplace Metering Service (MMS) dimensions should be created during publishing to allow sellers to meter through the AWS SDK.
      + `Entitled` – Indicates that entitlements can be granted for the dimension during the product or offer publishing.

        The following table lists the supported combinations of pricing dimensions and products.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-seller-products.html)
+ `Entity` (object) (required) – The named type of entity being created.
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0` or `SaaSProduct@1.0`. 

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This includes validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `AddDimensions` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Description | Max length: 1000 Required | 400 | 
| Key | Max length: 100 Pattern: [A-Za-z0-9\_.-]\+$ <br />Required | 400 | 
| Dimension Units | Max length: 20 Required | 400 | 
| Name | Max length: 500 Required | 400 | 
| Type (tag) | Required: Min 1 - Max 3<br />Inputs: Entitled, Metered, ExternallyMetered <br />Required | 400 | 

**Asynchronous Errors**

The following errors are specific to `AddDimensions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| MISSING\_DATA | No data provided to perform an update. Provide data for at least 1 dimension. | 
| INVALID\_DIMENSION | Provide no more than 200 dimensions. | 
| INVALID\_DIMENSION | Can't add duplicate dimensions. | 
| INVALID\_DIMENSION | Dimension can't be added in current state '%s'. States that support dimension updates are %s. | 
| INVALID\_DIMENSION | Can't add dimension. The field '%s' has duplicate values '%s' in other dimensions. | 
| INVALID\_DIMENSION | Provide non-empty fields (Key, Unit, Name, Types) for each dimension. | 
| IINVALID\_TYPE | Remove invalid type '%s'. Valid types are ["Metered", "Entitled", "ExternallyMetered"]. | 
| INVALID\_UNIT | Remove invalid Unit '%s'. Valid units are ["GB", "Gbps", "HostHrs", "Hosts", "MB", "Mbps", "Requests", "TaskHrs", "TB", "TierHrs", "UnitHrs", "Units", "UserHrs", "Users"]. | 
| INVALID\_INPUT | Inappropriate content '%s' found in %s field. Provide %s with no inappropriate content. | 
| INVALID\_INPUT | Invalid '%s' field. Remove spaces before trademark symbol. | 
| INVALID\_INPUT | Invalid '%s' field. Remove unsupported characters %s. | 
| INVALID\_DIMENSION | Remove invalid dimension type combination %s. Allowed values are %s. | 
| INVALID\_DIMENSION | Remove invalid dimension key '%s' for Metered dimension. | 
| INVALID\_DIMENSION | Dimension named '%s' for productCode '%s' did not pass AWS Marketplace Metering Service validation %s. | 
| INVALID\_DIMENSION | Dimension named '%s' for productCode '%s' has no metering record present in Metering Service. The product has either never been launched for testing or is misconfigured and does not make the appropriate calls to the AWS Marketplace Metering Service. | 

## Update pricing dimensions
<a name="update-dimensions"></a>

You can use the Catalog API to update existing pricing dimensions of an AMI, container, or SaaS product in AWS Marketplace. 

Each dimension is uniquely identified by the dimension key and dimension types to perform the update. Updating a dimension doesn't affect any active offer or customers that the original dimension had created. 

**Note**  
For more information about updating pricing dimensions using the AWS Marketplace Management Portal, see the following topics in the *AWS Marketplace Seller Guide*:  
AMI-based product: [Update pricing](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-update-product-pricing)
Container-based product: [Updating dimension information](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#container-update-dimensions-information)
SaaS-based product: [Update pricing dimensions](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-product-settings.html#saas-update-dimension)
Machine learning product: [Update product pricing](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-update-public-offer.html)

To update pricing dimensions, call the `StartChangeSet` API operation with the `UpdateDimensions` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateDimensions",
      "DetailsDocument":
      [
        {
          "Key": "{{UniqueApiKey}}",
          "Types":
          [
            "{{ExternallyMetered}}"
          ],
          "Name": "{{First Dimension}}",
          "Description": "{{Description of the dimension}}"
        }
      ],
      "Entity":
      {
        "Identifier": "{{prod-example12345}}",
        "Type": "SaaSProduct@1.0"
      }
    }
  ]
}
```

Use the following fields with the `UpdateDimensions` change type:
+ `DetailsDocument` (array of objects) (required) – Details of the request.
  + `Key` (string) (required) – Provide key of existing dimension from the product to change description and name on. For `UpdateDimension`, this field is only for identifying the dimension to be changed.
  + `Types` (array of strings) (required) (also known as **Tags**) – These indicate whether the dimension covers metering, entitlement, or support for external metering. This is not changeable after the dimension is created.
    + `Metered` – Indicates that Commerce Platform usage types should be created to allow metering to occur for this dimension.
    + `ExternallyMetered` – Indicates that AWS Marketplace Metering Service (MMS) dimensions should be created during publishing to allow sellers to meter through the AWS SDK.
    + `Entitled` – Indicates that entitlements can be granted for the dimension during product/offer publishing.  
**Valid Pricing Dimension Types Combinations**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-seller-products.html)
  + `Description` (string) (optional – Full description of the dimension that will be the long description on the buyer's viewing page.
  + `Name` (string) optional – DIsplay name for the dimension on the website and customer's bill.
+ `Entity` (object) (required) – The named type of entity being created.
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0` or `SaaSProduct@1.0`. 

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdateDimensions` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Description  | Max length: 1000<br />Required | 400 | 
| Key  | Max length: 100<br />Pattern: [A-Za-z0-9\_.-]\+$ <br />Required | 400 | 
| Name | Max length: 5<br />Required | 400 | 
|  Types (tag)  | Required: Min 1 - Max 3<br />Inputs: `Entitled`, `Metered`, `ExternallyMetered` <br />Required | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateDimensions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_INPUT | Invalid '%s' field. Remove spaces before trademark symbol. | 
| INVALID\_INPUT | Invalid '%s' field. Remove unsupported characters %s. | 
| INVALID\_DIMENSION | Provide non-empty fields (Key, Types, Name and/or Description) for each dimension. | 
| INVALID\_DIMENSION | Cannot update dimension. The field Name has duplicate values '%s' in other dimensions. | 
| INVALID\_DIMENSION | Cannot update same dimension with key '%s' and types '%s' multiple times in the same request. | 
| INVALID\_DIMENSION | Cannot restrict dimension. The dimension key '%s' with types '%s' does not exist. | 
|  INVALID\_DIMENSION  | Cannot update dimension. The dimension key '%s' is Metered. | 
|  INVALID\_DIMENSION  | Dimension cannot be updated for an already restricted dimension. | 

## Restrict pricing dimensions
<a name="restrict-dimensions"></a>

You can use the Catalog API to restrict existing pricing dimensions of an AMI or SaaS product in AWS Marketplace. 

Each dimension is uniquely identified by the dimension key and dimension types to perform the update. Restricting a dimension doesn't affect any active offer or customers that the original dimension had created. 

To restrict pricing dimensions, call the `StartChangeSet` API with the `RestrictDimensions` change type.

**Note**  
Pricing dimension restrictions are only available while the product is in draft state. Changes are not permitted once the product moves to limited or public state.

The following example shows how to restrict the `Entitled` dimension for a SaaS product.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "RestrictDimensions",
      "DetailsDocument":
      [
        {
          "Key": "{{UniqueApiKey}}",
          "Types": ["Entitled"]
        }
      ],
      "Entity":
      {
        "Identifier": "{{prod-example12345}}",
        "Type": "SaaSProduct@1.0"
      }
    }
  ]
}
```

Use the following fields with the `RestrictDimensions` change type:
+ `DetailsDocument` (array of objects) (required) – Details of the request.
  + `Key` (string) (required) – Provide key of existing dimension from the product to change description and name on. For `RestrictDimensions`, this field is only for identifying the dimension to be changed.
  + `Types` (array of strings) (required) (also known as **Tags**) – These indicate whether the dimension covers metering, entitlement, or support for external metering. This is not changeable after the dimension is created.
    + `["ExternallyMetered", "Entitled"]` – You can only combine these types for SaaS Contract with Consumption pricing where dimensions can be prepaid or metered.
    + `["Metered"]` – For hourly pricing dimensions of AMI products. Indicates that Commerce Platform usage types should be created to allow metering to take place for this dimension.
    + `["ExternallyMetered"]` – For flexible consumption pricing dimensions (also known as custom metering) of AMI, container, and SaaS products. Indicates that AWS Marketplace Metering Service (MMS) dimensions should be created during publishing to allow sellers to meter through the AWS SDK.
    + `["Entitled"]` – For contract pricing dimensions of SaaS Contracts and professional services products. This tag grants rights to use a software or service, sets start and end dates for the usage, and grants usage-discount rights for AMI annual products. Each entitlement is identified by a Dimension Key in AWS Marketplace Entitlement Service for creating and updating the entitlements. The key indicates that entitlements can be granted for the dimension during product and offer publishing.
+ `Entity` (object) (required) – The named type of entity being created.
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on your product's delivery method (product type): `AmiProduct@1.0` or `SaaSProduct@1.0`. 

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or by calling the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API.

**Synchronous Validations**

The following schema validations are specific to `RestrictDimensions` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Description  | Max length: 1000<br />Required | 400 | 
| Key  | Max length: 100<br />Pattern: [A-Za-z0-9\_.-]\+$ <br />Required | 400 | 
| Name | Max length: 5<br />Required | 400 | 
|  Types (tag)  | Required: Min 1 - Max 3<br />Inputs: `Entitled`, `Metered`, `ExternallyMetered` <br />Required | 400 | 

**Asynchronous Errors**

The following errors are specific to `RestrictDimensions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` while a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_INPUT | Invalid '%s' field. Remove spaces before trademark symbol. | 
| INVALID\_INPUT | Invalid '%s' field. Remove unsupported characters %s. | 
| INVALID\_DIMENSION | The dimension key '%s' with types '%s' was already restricted | 
| INVALID\_DIMENSION | Cannot restrict dimension. The dimension key '%s' with types '%s' does not exist | 
| INVALID\_DIMENSION | Cannot restrict duplicate dimensions. | 
| INVALID\_DIMENSION | All Entitled dimensions cannot be restricted. There must be at least one active Entitled dimension. | 
|  INVALID\_DIMENSION  | The dimension key '%s' with types '%s' is associated with another dimension of different types '%s'. Both dimensions of the same key must be restricted at the same time to be valid. | 

## Update targeting configuration
<a name="update-targeting"></a>

You can use the Catalog API to add AWS account IDs that are allowed to view the AMI, container, ML, or SaaS product in AWS Marketplace before it's moved to a `Public` state by calling the `UpdateTargeting` change type. 

Managed Catalog Operations (MCO) accounts are automatically added to the allowed accounts list when new products are created. These MCO accounts are visible to sellers in the AWS Marketplace Management Portal (AMMP) when viewing allowed accounts, and in the `Targeting` section of the `DescribeEntity` API response.

**Note**  
For more information about adding AWS account IDs using the AWS Marketplace Management Portal, see the following topics in the *AWS Marketplace Seller Guide*:  
AMI-based product: [Update the allowlist (preview accounts)](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-updating-allowlist)
Container-based product: [Updating the allowlist of AWS account IDs](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#container-update-allowlist)
SaaS-based product: [Updating the allowlist of AWS account IDs](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-product-settings.html#update-allowlist)
 Machine learning product: [Updating the allowlist](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-update-allowlist.html) 

To add AWS account IDs that are allowed to view the AMI, container, ML, or SaaS product, call the `StartChangeSet` API operation with the `UpdateTargeting` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateTargeting",
      "Entity":
      {
        "Type": "SaaSProduct@1.0",
        "Identifier": "{{prod-example12345}}"
      },
      "DetailsDocument":
      {
        "PositiveTargeting":
        {
          "BuyerAccounts":
          [
            "{{1112223334444}}"
          ]
        }
      }
    }
  ]
}
```

Use the following the fields with the `UpdateTargeting` change type. 
+ `Entity` (object) (required) – The named type of entity being created.
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`, `MachineLearningProduct@1.0`, or `SaaSProduct@1.0`. 
+ `DetailsDocument` (object) (required) – The details required to run the ChangeSet.
  + `PositiveTargeting` (object) (optional) – Positive targeting defines the criteria which any buyer's profile should fulfill in order to be allowed to access the offer. This field is optional, but at least one targeting option should be provided when this field is present.
    + `BuyerAccounts` (array of strings) (optional) – List as an option to allow targeting based on AWS accounts (also known as, Private Offer). If the intention is to not target the offer to an AWS account, this field should be omitted.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

To check request status, use the AWS Marketplace Management Portal or call the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API.

When the request is complete (if the `Status` is `SUCCEEDED`), a new `ProductId` is generated.

**Synchronous Validations**

The following schema validations are specific to `UpdateTargeting` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Type of targeting | Valid current visibility states | BuyerAccounts (input) | Check | 
| --- | --- | --- | --- | 
| Positive | Public, Limited, or Draft | Array of 12-digit AWS account ID strings.<br />Min size: 0. <br />Max size: 5000. | The input must be different from the current document targeted accounts.Input must be in valid AWS accounts. | 

**Asynchronous Errors**

The following errors are specific to `DescribeChangeSet` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_PRODUCT\_VISIBILITY | Use an existing Public, Limited or Draft product. | 
| INVALID\_AWS\_ACCOUNT\_IDS | Provide valid AWS account IDs. AWS accounts not found: [x, y, z]. | 
| ValidationException | Professional services products do not have allowlists. Unlike other product types, professional services products in the limited state can be extended to any buyer without requiring an allowlist. | 

## Update product visibility
<a name="update-visibility"></a>

You can use the Catalog API to update the visibility (also known as lifecycle state) of an AMI, container, ML, or SaaS product in AWS Marketplace. 

**Note**  
For more information updating product visibility using the AWS Marketplace Management Portal, see the following topics in the *AWS Marketplace Seller Guide*:  
AMI-based product: [Update product visibility](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#ami-update-self-service-visibility)
Container-based product: [Updating product visibility](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#container-product-visibility)
SaaS-based product: [Update product visibility](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-product-settings.html#saas-update-visibility)
Machine learning product: [Updating product visibility](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-update-visibility.html)

Allowed target lifecycle states are `Limited`, `Public`, or `Restricted`.

`Limited`   
The product is complete and has successfully completed the `ReleaseProduct` `ChangeType`. Sellers can view details of the product in this state. The product is not public. However, sellers can target specific buyers to allow to preview the product.

`Public`   
The product is visible in AWS Marketplace. Buyers can view and subscribe to the product.

`Restricted`   
The product is no longer visible to the public and doesn't accept new subscribers. Existing subscribers can continue using this product until their subscription expires.

**Note**  
The `UpdateVisibility` change type requires a manual review from the AWS Marketplace Seller Operations team, which results in a longer execution time. Use `UpdateVisibility` separately in its own change set.

To update your product's visibility, call the `StartChangeSet` API operation with the `UpdateVisibility` change type, as shown in the following example.

**Request Syntax**

For when `TargetVisibility` is `Public` or `Limited`.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateVisibility",
      "Entity":
      {
        "Type": "SaaSProduct@1.0",
        "Identifier": "{{prod-example12345}}"
      },
      "DetailsDocument":
      {
        "TargetVisibility": "Public"
      }
    }
  ]
}
```

For when `TargetVisibility` is `Restricted`.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateVisibility",
      "Entity":
      {
        "Type": "SaaSProduct@1.0",
        "Identifier": "{{prod-example12345}}"
      },
      "DetailsDocument":
      {
        "TargetVisibility": "Restricted",
        "ReplacementProductId": "{{prod-example54321}}"
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateVisibility` change type. 
+ `Entity` (object) (required) – The named type of entity being created.
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`, `SaaSProduct@1.0`, `ContainerProduct@1.0`, `MachineLearningProduct@1.0`. For more information, see [Identifier](catalog-apis.md#identifier).
+ `DetailsDocument` (object) (required) – The details required to run the `ChangeSet`.
  + 
    + `TargetVisibility` – The intended new visibility of the product.

      Possible values: `Public`, `Limited`, and `Restricted`
    + `ReplacementProductId` (string) (optional) – Replacement product ID for the product to be `Restricted`. Used to notify current subscribers about the product restriction.

      Only accepts `Restricted` for `TargetVisibility`.

**Synchronous Validations**

The following schema validations are specific to `UpdateVisibility` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Type of targeting  | Valid current states | ReplacementProductId (input)  | Validation checks | 
| --- | --- | --- | --- | 
| Public | Limited and Restricted | Not allowed | Valid current state | 
| Limited | Public and Restricted | Not allowed | Valid current state | 
| Restricted | Public and Limited | String (Optional) | ReplacementProductId must belong to an existing Limited or Public product. | 

After triggering this change type, it can take up to 37 days to complete. This includes the time the AWS Marketplace Seller Operations Team needs to review, audit, and approve. When restricting a product, you have 24 hours to change your mind, by calling `CancelChangeSet`, before the AWS Marketplace Seller Operations Team begins auditing. For more information, see [`CancelChangeSet`](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_CancelChangeSet.html).

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

When the request is complete (if the `Status` is `SUCCEEDED`), a new `ProductId` is generated.

**Asynchronous Errors**

The following errors are specific to `UpdateVisibility` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INVALID\_PRODUCT\_STATE | Use an existing Public, Limited, or Restricted product. | 
| INVALID\_TARGET\_VISIBILITY | Provide a valid target visibility state: Public, Limited, or Restricted. | 
| EMPTY\_TARGET\_VISIBILITY | Provide a valid target visibility state: Public, Limited, or Restricted. | 
| INVALID\_REPLACEMENT\_PRODUCT\_ID | Use an existing Public or Limited product as replacement. | 
| INVALID\_REPLACEMENT\_PRODUCT\_ID | Replacement product ID is only valid when restricting a product. | 
| AUDIT\_ERROR | Varies based on MCO manual review. | 
| MISSING\_SELLER\_PROFILE\_INFORMATION | Before you can update your product to Public, you must add a public profile to your seller account. | 

## Publish a product
<a name="release-product"></a>

You can use the Catalog API to publish a `Draft` AMI, container, ML, or SaaS product into `Limited` state in AWS Marketplace. 

**Note**  
For `AmiProduct@1.0` and `SaaSProduct@1.0`, the `ReleaseProduct` change type must be accompanied by `ReleaseOffer` change type on the corresponding draft public `Offer@1.0` entity created for this product.

To publish a product, call the `StartChangeSet` API operation with the `ReleaseProduct` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "ReleaseProduct",
      "Entity":
      {
        "Type": "SaaSProduct@1.0",
        "Identifier": "{{prod-example12345}}"
      },
      "DetailsDocument": {}
    }
  ]
}
```

Provide information for the fields to add to the `ReleaseProduct` change type. This change type does not take any parameter payload.
+ `Entity` (object) (required) – The named type of entity being created.
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`, `SaaSProduct@1.0`, `ContainerProduct@1.0`, `MachineLearningProduct@1.0`. For more information, see [Identifier](catalog-apis.md#identifier).
+ `DetailsDocument` (object) (required) - Must be an empty object. The change type `ReleaseProduct` doesn't accept any details.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

When the request is complete (if the `Status` is `SUCCEEDED`), a new `ProductId` is generated.

**Asynchronous Errors**

The following errors are specific to `ReleaseProduct` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| VALIDATION\_FAILED | Provide Description information. | 
| VALIDATION\_FAILED | Provide Versions information. | 
| VALIDATION\_FAILED | Provide Dimensions information. | 
| VALIDATION\_FAILED | Provide Description\|PromotionalResources\|SupportInformation information. | 

## Find your product ID
<a name="seller-product-id"></a>

You must get the product ID for your product before you can modify it with AWS Marketplace Catalog API. There are two ways to find the product ID for server products:
+ Open the AWS Marketplace Management Portal and sign in with your seller account. From the **Products** menu, select **Server products**, then choose the product you are interested in. The product ID is listed in the **Product Summary** section.
+ Use the [`ListEntities`](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListEntities.html) action with the `EntityType` **AmiProduct** or **ContainerProduct**, **SaaSProduct**, **MachineLearningProduct**,or **DataProduct** to get a list of products, including their product IDs, via the Catalog API. `ListEntities` requires that you do not include the version of the entity type (for example, `AmiProduct@1.0`).

**Note**  
The product ID is only available after your product has been published and is visible to at least yourself in AWS Marketplace. When you first create your product, it can take several days to be reviewed and fully created. During this time, it will not have a product ID available. 

The following topics explain how to find a product by filtering on entity id, product title, last modified date, or visibility.

**Topics**
+ [Find a product based on product title](#find-product-using-title)
+ [Find a product based on last modified date](#find-product-using-last-mod-date)
+ [Find a product based on product visibility](#find-product-using-visibility)
+ [Find a product based on product title, last modified date, and product visibility](#find-product-using-all)
+ [Get additional details about a product](#get-additional-details)

### Find a product based on product title
<a name="find-product-using-title"></a>

**Request**

```
POST /ListEntities HTTP/1.1
Content-Type: application/json
      
{
    "Catalog": "AWSMarketplace",
    "EntityType": "AmiProduct",
    "MaxResults": 10,
    "EntityTypeFilters": {
        "AmiProductFilters": {
            "ProductTitle": {
                "WildCardValue": "{{XYZ}}"
            }
        }
    }
}
```

**Response**

```
HTTP/1.1 200
Content-type: application/json

{ 
  "EntitySummaryList": [ 
    { 
      "EntityArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/AmiProduct/example-abcd-1234",
      "EntityId": "example1-abcd-1234-5ef6-7890abcdef12@1",
      "EntityType": "AmiProduct",
      "LastModifiedDate": "2018-02-27T13:45:22Z",
       "AmiProductSummary": {
            "ProductTitle": "{{ABC-XYZ-123}}",
            "Visibility": "Public"
       }
    } 
  ],
  "NextToken": "" 
}
```

### Find a product based on last modified date
<a name="find-product-using-last-mod-date"></a>

**Request**

```
POST /ListEntities HTTP/1.1
Content-Type: application/json
      
{
    "Catalog": "AWSMarketplace",
    "EntityType": "AmiProduct",
    "MaxResults": 10,
    "EntityTypeFilters": {
        "AmiProductFilters": {
            "LastModifiedDate": {
                "DateRange": {
                    "BeforeValue": "{{2018-03-27T13:45:22Z}}",
                    "AfterValue": "{{2018-01-27T13:45:22Z}}"
                }
            }
        }
    }
}
```

**Response**

```
HTTP/1.1 200
Content-type: application/json

{ 
  "EntitySummaryList": [ 
    { 
      "EntityArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/AmiProduct/example-abcd-1234",
      "EntityId": "{{example1-abcd-1234-5ef6-7890abcdef12@1}}",
      "EntityType": "AmiProduct",
      "LastModifiedDate": "{{2018-02-27T13:45:22Z}}",
       "AmiProductSummary": {
            "ProductTitle": "{{ABC-XYZ-123}}",
            "Visibility": "Public"
       }
    } 
  ],
  "NextToken": "" 
}
```

### Find a product based on product visibility
<a name="find-product-using-visibility"></a>

**Request**

```
POST /ListEntities HTTP/1.1
Content-Type: application/json
      
{
    "Catalog": "AWSMarketplace",
    "EntityType": "AmiProduct",
    "MaxResults": 10,
    "EntityTypeFilters": {
        "AmiProductFilters": {
            "Visibility": {
                "ValueList": [
                    "Public"
                ]
            }
        }
    }
}
```

**Response**

```
HTTP/1.1 200
Content-type: application/json

{ 
  "EntitySummaryList": [ 
    { 
      "EntityArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/AmiProduct/example-abcd-1234",
      "EntityId": "{{example1-abcd-1234-5ef6-7890abcdef12@1}}",
      "EntityType": "AmiProduct",
      "LastModifiedDate": "{{2018-02-27T13:45:22Z}}",
       "AmiProductSummary": {
            "ProductTitle": "{{ABC-XYZ-123}}",
            "Visibility": "Public"
       }
    } 
  ],
  "NextToken": "" 
}
```

### Find a product based on product title, last modified date, and product visibility
<a name="find-product-using-all"></a>

**Request**

```
POST /ListEntities HTTP/1.1
Content-Type: application/json
      
{
    "Catalog": "AWSMarketplace",
    "EntityType": "AmiProduct",
    "MaxResults": 10,
    "EntityTypeFilters": {
        "AmiProductFilters": {
            "LastModifiedDate": {
                "DateRange": {
                    "BeforeValue": "{{2018-03-27T13:45:22Z}}",
                    "AfterValue": "{{2018-01-27T13:45:22Z}}"
                }
            },
            "Visibility": {
                "ValueList": [
                    "Public"
                ]
            },
            "ProductTitle": {
                "ValueList": [
                    "{{ABC-XYZ-123}}"
                ]
            }
        }
    }
}
```

**Response**

```
HTTP/1.1 200
Content-type: application/json

{ 
  "EntitySummaryList": [ 
    { 
      "EntityArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/AmiProduct/example-abcd-1234",
      "EntityId": "example1-abcd-1234-5ef6-7890abcdef12@1",
      "EntityType": "AmiProduct",
      "LastModifiedDate": "{{2018-02-27T13:45:22Z}}",
       "AmiProductSummary": {
            "ProductTitle": "{{ABC-XYZ-123}}",
            "Visibility": "Public"
       }
    } 
  ],
  "NextToken": "" 
}
```

### Get additional details about a product
<a name="get-additional-details"></a>

You can get additional details about the product using the entity id with the `DescribeEntity` action.

**Request**

```
GET /DescribeEntity?catalog=AWSMarketplace&entityId={{example-abcd-1234}} HTTP/1.1
```

**Response**

```
HTTP/1.1 200
Content-type: application/json

{
   "DetailsDocument": {
        "ProductTitle": "{{ABC-XYZ-123}}",
        "ShortDescription": "{{My product short description.}}", 
        "LongDescription": "{{My product longer description.}}", 
        "Sku": "123example456", 
        "SupportDescription": "{{Need help? Contact our experts at support@example.com \n\nYour purchase includes 24x7 support.}}", 
        "Categories": [ 
            "Operating Systems", 
            "Network Infrastructure", 
            "Application Development" 
            ] 
   }
    "EntityArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/AmiProduct/{{example-abcd-1234}}",
    "EntityId": "{{example1-abcd-1234-5ef6-7890abcdef12@1}}",
    "EntityType": "AmiProduct",
    "LastModifiedDate": "{{2018-02-27T13:45:22Z}}",
}
```

## Change set status and errors
<a name="seller-product-change-set-errors"></a>

Making changes to seller products in the AWS Marketplace Catalog API involves creating change sets that describe the changes you want to make, and then using the `StartChangeSet` action to start the changes. The changes from the request can take minutes to hours or longer to complete, depending on the request. The response to this request looks like the following.

```
{
    "ChangeSetId": "{{example123456789012abcdef}}",
    "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed, including scanning the files and information to ensure that it meets the AWS Marketplace guidelines for products. Depending on the change requests, this process can take a few minutes to days. You can check the status of the request through the AWS Marketplace Management Portal, or in the Catalog API with the `DescribeChangeSet` action. For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets).

To check the status of your request, use the `DescribeChangeSet` action.

```
POST /DescribeChangeSet HTTP/1.1
Content-type: application/json

{
   "Catalog": "AWSMarketplace",
   "ChangeSetID": "{{{{example123456789012abcdef}}}}"
}
```

The result of this call looks like the following (in this case, for adding a new version to a container product).

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
  "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}",
  "ChangeSetName": "Submitted by {{123456789012}}",
  "StartTime": "{{2020-10-27T22:21:26Z}}",
  "EndTime": "{{2020-10-27T22:32:19Z}}",
  "Status": "SUCCEEDED",
  "ChangeSet":
  [
    {
      "ChangeType": "AddDeliveryOptions",
      "Entity":
      {
        "Type": "ContainerProduct@1.0",
        "Identifier": "{{example-1234-abcd-56ef-abcdef12345678@4}}"
      },
      "Details": "{\"Version\": {\"VersionTitle\": \"1.1\",\"ReleaseNotes\": \"Minor bug fix\"},\"DeliveryOptions\": [{\"DeliveryOptionTitle\": \"EKSDelivery\",\"Details\": {\"EcrDeliveryOptionDetails\" : {\"ContainerImages\": [\"{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1\"],\"DeploymentResources\": [{\"Name\": \"HelmDeploymentTemplate\",\"Url\": \"{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1\"}],\"CompatibleServices\": [\"EKS\"],\"Description\": \"Sample Description\",\"UsageInstructions\":\"helm pull {{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1\"}}},{\"DeliveryOptionTitle\": \"HelmChartDeliveryOption\",\"Details\": {\"HelmDeliveryOptionDetails\": {\"CompatibleServices\": [\"EKS\", \"EKS-Anywhere\"],\"ContainerImages\": [\"{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1\"],\"HelmChartUri\": \"{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:helmchart1.1\",\"Description\": \"Helm chart description\",\"UsageInstructions\": \"Usage instructions\",\"MarketplaceServiceAccountName\": \"Service account name\",\"ReleaseName\": \"Optional release name\",\"Namespace\": \"Optional Kubernetes namespace\",\"OverrideParameters\": [{\"Key\": \"HelmKeyName1\",\"DefaultValue\": \"${AWSMP_LICENSE_SECRET}\"},{\"Key\": \"HelmKeyName2\",\"DefaultValue\": \"${AWSMP_SERVICE_ACCOUNT}\"}]}}}]}",
      "DetailsDocument":
      {
        "Version":
        {
          "VersionTitle": "1.1",
          "ReleaseNotes": "Minor bug fix"
        },
        "DeliveryOptions":
        [
          {
            "DeliveryOptionTitle": "EKSDelivery",
            "Details":
            {
              "EcrDeliveryOptionDetails":
              {
                "ContainerImages":
                [
                  "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                ],
                "DeploymentResources":
                [
                  {
                    "Name": "HelmDeploymentTemplate",
                    "Url": "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
                  }
                ],
                "CompatibleServices":
                [
                  "EKS"
                ],
                "Description": "Sample Description",
                "UsageInstructions": "helm pull {{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
              }
            }
          },
          {
            "DeliveryOptionTitle": "HelmChartDeliveryOption",
            "Details":
            {
              "HelmDeliveryOptionDetails":
              {
                "CompatibleServices":
                [
                  "EKS",
                  "EKS-Anywhere"
                ],
                "ContainerImages":
                [
                  "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                ],
                "HelmChartUri": "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:helmchart1.1",
                "Description": "Helm chart description",
                "UsageInstructions": "Usage instructions",
                "MarketplaceServiceAccountName": "Service account name",
                "ReleaseName": "Optional release name",
                "Namespace": "Optional Kubernetes namespace",
                "OverrideParameters":
                [
                  {
                    "Key": "HelmKeyName1",
                    "DefaultValue": "${AWSMP_LICENSE_SECRET}"
                  },
                  {
                    "Key": "HelmKeyName2",
                    "DefaultValue": "${AWSMP_SERVICE_ACCOUNT}"
                  }
                ]
              }
            }
          }
        ]
      },
      "ErrorDetailList":
      []
    }
  ]
}
```

The `Status` field shows the current status of the request, in this case, `SUCCEEDED`.

If there are failures, the result can include two types of errors. For most errors, the error message is included directly. However, errors found while scanning the product for security vulnerabilities instead include a URL to a file that lists all of the errors found, in the `ErrorMessage` field. Errors found while scanning have the `ErrorCode` "`SCAN_ERROR`".

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
  "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}",
  "ChangeSetName": "Submitted by {{123456789012}}",
  "StartTime": "{{2020-10-27T22:21:26Z}}",
  "EndTime": "{{2020-10-27T22:32:19Z}}",
  "Status": "FAILED",
  "FailureDescription": "Change set preparation has failed. For details see 'ErrorDetailList'.",
  "ChangeSet":
  [
    {
      "ChangeType": "AddDeliveryOptions",
      "Entity":
      {
        "Type": "ContainerProduct@1.0",
        "Identifier": "{{example-1234-abcd-56ef-abcdef12345678@4}}"
      },
      "Details": "{\"Version\": {\"VersionTitle\": \"1.1\",\"ReleaseNotes\": \"Minor bug fix\"},\"DeliveryOptions\": [{\"DeliveryOptionTitle\": \"EKSDelivery\",\"Details\": {\"EcrDeliveryOptionDetails\" : {\"ContainerImages\": [\"{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1\"],\"DeploymentResources\": [{\"Name\": \"HelmDeploymentTemplate\",\"Url\": \"{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1\"}],\"CompatibleServices\": [\"EKS\"],\"Description\": \"Sample Description\",\"UsageInstructions\":\"helm pull {{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1\"}}},{\"DeliveryOptionTitle\": \"HelmChartDeliveryOption\",\"Details\": {\"HelmDeliveryOptionDetails\": {\"CompatibleServices\": [\"EKS\", \"EKS-Anywhere\"],\"ContainerImages\": [\"{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1\"],\"HelmChartUri\": \"{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:helmchart1.1\",\"Description\": \"Helm chart description\",\"UsageInstructions\": \"Usage instructions\",\"MarketplaceServiceAccountName\": \"Service account name\",\"ReleaseName\": \"Optional release name\",\"Namespace\": \"Optional Kubernetes namespace\",\"OverrideParameters\": [{\"Key\": \"HelmKeyName1\",\"DefaultValue\": \"${AWSMP_LICENSE_SECRET}\"},{\"Key\": \"HelmKeyName2\",\"DefaultValue\": \"${AWSMP_SERVICE_ACCOUNT}\"}]}}}]}",
      "DetailsDocument":
      {
        "Version":
        {
          "VersionTitle": "1.1",
          "ReleaseNotes": "Minor bug fix"
        },
        "DeliveryOptions":
        [
          {
            "DeliveryOptionTitle": "EKSDelivery",
            "Details":
            {
              "EcrDeliveryOptionDetails":
              {
                "ContainerImages":
                [
                  "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                ],
                "DeploymentResources":
                [
                  {
                    "Name": "HelmDeploymentTemplate",
                    "Url": "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
                  }
                ],
                "CompatibleServices":
                [
                  "EKS"
                ],
                "Description": "Sample Description",
                "UsageInstructions": "helm pull {{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
              }
            }
          },
          {
            "DeliveryOptionTitle": "HelmChartDeliveryOption",
            "Details":
            {
              "HelmDeliveryOptionDetails":
              {
                "CompatibleServices":
                [
                  "EKS",
                  "EKS-Anywhere"
                ],
                "ContainerImages":
                [
                  "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                ],
                "HelmChartUri": "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:helmchart1.1",
                "Description": "Helm chart description",
                "UsageInstructions": "Usage instructions",
                "MarketplaceServiceAccountName": "Service account name",
                "ReleaseName": "Optional release name",
                "Namespace": "Optional Kubernetes namespace",
                "OverrideParameters":
                [
                  {
                    "Key": "HelmKeyName1",
                    "DefaultValue": "${AWSMP_LICENSE_SECRET}"
                  },
                  {
                    "Key": "HelmKeyName2",
                    "DefaultValue": "${AWSMP_SERVICE_ACCOUNT}"
                  }
                ]
              }
            }
          }
        ]
      },
      "ErrorDetailList":
      [
        {
          "ErrorCode": "DUPLICATE_VERSION_TITLE",
          "ErrorMessage": "The version title must be different from any other version titles of this product."
        },
        {
          "ErrorCode": "SCAN_ERROR",
          "ErrorMessage": "https://123sample456.cloudfront.net/example-1234-abcd-5678-abcdef12345678/1234abcdef567890"
        }
      ]
    }
  ]
}
```

In this example, there is one error directly reported (`DUPLICATE_VERSION_TITLE`). The other error has a file with error messages (a single `SCAN_ERROR` can have multiple found errors in the file that is linked). 

**Note**  
The link returned in the `ErrorMessage` is valid for 60 days.