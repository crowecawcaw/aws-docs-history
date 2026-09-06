

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with solutions
<a name="work-with-solutions"></a>

A solution is a collection of products and services that work together to solve specific customer problems. Solutions can include AWS Marketplace products and non-AWS Marketplace products. Solutions help you showcase how multiple products integrate to address industry-specific use cases. The solution describes the customer problem, use cases, integration details, and related products.

## Solutions in AWS Marketplace and AWS Partner Central
<a name="solutions-in-marketplace-partner-central"></a>

When you migrate from Partner Central 2.0 to Partner Central 3.0, you're prompted to create an AWS account and register as an AWS Marketplace seller. For more information, see [Register and create your seller profile](https://docs.aws.amazon.com/marketplace/latest/userguide/create-public-profile.html). This registration is required to:
+ Migrate your existing Partner Central solutions to the AWS Marketplace catalog (all solutions will be migrated to `AWSMarketplace` catalog)
+ Enable your AWS Marketplace solutions to work with Partner Central APIs, such as [Selling APIs](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-your-opportunities.html).

### Understanding profile linking and migration
<a name="understanding-profile-linking-migration"></a>

There are two distinct scenarios for connecting your Partner Central and AWS Marketplace accounts:

**Profile linking only** – If you link your AWS Partner Central and AWS accounts without migrating to Partner Central 3.0, your AWS Marketplace solutions and Partner Central solutions remain separate. You manage each platform independently.

**Profile migration** – When you migrate to Partner Central 3.0 with linked AWS Marketplace seller profiles:
+ Your Partner Central 2.0 solutions migrate to AWS Marketplace
+ You manage solutions through AWS Marketplace only
+ Partner Central APIs can access migrated solutions

**Note**  
If you have already linked your AWS Partner Central and AWS accounts (see [Linking AWS Partner Central and AWS accounts](https://docs.aws.amazon.com/partner-central/latest/getting-started/account-linking.html)), you don't need to create a new AWS account. However, verify that your existing AWS account is registered as an AWS Marketplace seller. To make your solution publicly available on AWS Marketplace buyer website, you need a public profile as an AWS Marketplace seller. For AWS Marketplace seller registration instructions, see [Register and create your seller profile](https://docs.aws.amazon.com/marketplace/latest/userguide/create-public-profile.html).

### Making pre-existing AWS Marketplace solutions available to Partner Central APIs
<a name="making-pre-existing-solutions-available"></a>

AWS Marketplace solutions that you created before the Partner Central 3.0 profile migration aren't automatically recognized by Partner Central APIs. This applies even after you complete the migration and link your AWS account with a Partner Central account.

To make an existing pre-migration solution visible to Partner Central APIs, update any field in the solution. You can enter the same information that's currently there. Repeat this process for each solution you created before the Partner Central 3.0 profile migration.

For example, use the `UpdateInformation` change type to update a solution's name with its current value. After you update a solution once, Partner Central APIs will automatically recognize any future updates to that solution.

## Solution entity
<a name="solution-entity"></a>

A solution is a marketing document that helps buyers discover and understand your offerings. Solutions contain a title, description, use cases, AWS Marketplace products, and non-AWS Marketplace products. Solution is a separate entity type from product, offer, and offer sets. Each solution has its own discovery and listing experience that buyers can browse separately from individual products.

**Key characteristics**
+ Group multiple products, including both AWS Marketplace products and non-AWS Marketplace products.
+ Create a dedicated discovery and listing experience for buyers.
+ Group products that you own with products from other sellers.

The solution entity type is `Solution@1.0`.

**Entity identifiers**

Solutions use the `soln-*` identifier format (for example, `soln-abc123def456`).

**Entity ARN format**

Solutions follow the standard AWS ARN format:

```
arn:{aws-partition}:aws-marketplace:{region}:{account-id}:{aws-marketplace-catalog}/Solution/{solution-id}
```

Example:

```
arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/soln-abc123def456
```

## Getting started with solutions
<a name="getting-started-with-solutions"></a>

This section provides detailed information about creating and managing solutions using AWS Marketplace Catalog API [change types](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Change.html).

Before you begin, make sure you have:
+ Valid AWS Marketplace seller registration and a public profile. For more information, see [Register and create your seller profile](https://docs.aws.amazon.com/marketplace/latest/userguide/create-public-profile.html).
+ Access to the API and completed seller prerequisites. For more information, see [Access control for the AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-api-access-control.html).
+ Learned the basics of using the AWS Marketplace Catalog API, see [Using the AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html).

## List your solutions
<a name="list-your-solutions"></a>

To list all solutions in your account, call the `ListEntities` API operation and set `EntityType` to Solution.

**Request**

```
POST /ListEntities HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "EntityType": "Solution"
}
```

**Response**

```
{
  "EntitySummaryList": [
    {
      "EntityArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/soln-abc123456",
      "EntityId": "soln-abc123456",
      "EntityType": "Solution",
      "LastModifiedDate": "2024-10-10T19:50:43Z",
      "Name": "Test Solution 1",
      "Visibility": "Limited"
    }
  ],
  "NextToken": null
}
```

### Filter solutions by visibility
<a name="filter-solutions-by-visibility"></a>

You can filter solutions by visibility using the `FilterList` parameter.

**Request**

```
POST /ListEntities HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "EntityType": "Solution",
  "FilterList": [
    {
      "Name": "Visibility",
      "ValueList": [
        "Public"
      ]
    }
  ]
}
```

## Get solution details
<a name="get-solution-details"></a>

To get detailed information about a specific solution, call the `DescribeEntity` API operation.

**Note**  
The DescribeEntity response returns an `EntityIdentifier` that combines an `EntityId` with a `RevisionId.` For solutions, `EntityId` is the solution ID, and `RevisionId` can be used for optimistic locking. For more information, see [Identifiers](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#identifier).

**Request**

```
GET /DescribeEntity?catalog=AWSMarketplace&entityId=soln-abc123456 HTTP/1.1
```

**Response**

```
{
  "Details": "{...}",
  "DetailsDocument": {
    "Lifecycle": {
      "Visibility": "Limited"
    },
    "Identifiers": {
      "Id": "soln-abc123456"
    },
    "Presentation": {
      "Title": "My Solution",
      "Name": "solution_for_customer_X",
      "ShortDescription": "Solution value proposition",
      "LongDescription": "Detailed solution description",
      "LogoUrl": "https://s3.amazonaws.com/logo.jpg",
      "UseCases": [
        {
          "Group": "advertising_and_marketing",
          "SubGroup": "ad_intelligence_and_measurement",
          "Item": "amazon_ads_insights",
          "Description": "Use case description"
        }
      ]
    },
    "RelatedProducts": {
      "AwsMarketplaceProducts": [
        {
          "ProductId": "prod-123"
        }
      ],
      "IntegrationDescription": "How products work together",
      "NonAwsMarketplaceProducts": [
        {
          "Type": "Hardware",
          "Title": "A hardware product",
          "Url": "https://example.com",
          "Description": "My hardware product description"
        }
      ]
    },
    "BuyerEngagement": [
      {
        "EngagementOption": "RequestPrivateOffer"
      }
    ]
  },
  "EntityArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/soln-abc123456",
  "EntityIdentifier": "soln-abc123456@12",
  "EntityType": "Solution@1.0",
  "LastModifiedDate": "2025-04-22T01:02:48Z"
}
```

## List change history for a solution
<a name="list-change-history-for-solution"></a>

To view the change history for a specific solution, call the `ListChangeSets` API operation with an entity filter.

**Request Syntax**

```
POST /ListChangeSets HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "FilterList": [
    {
      "Name": "EntityId",
      "ValueList": [
        "soln-abc123456"
      ]
    }
  ]
}
```

## Tag solutions and change sets
<a name="tag-solutions-and-change-sets"></a>

You can add tags to solutions and change sets during creation or update them later.

**Tag during creation**

You can add `EntityTags` only to the `CreateSolution` change type, not to other solution change types. You can add `ChangeSetTags` to any `StartChangeSet` payload.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateSolution",
      "Entity": {
        "Type": "Solution@1.0"
      },
      "DetailsDocument": {
        "Name": "Test solution resource name"
      },
      "EntityTags": [
        {
          "Key": "Team",
          "Value": "Solutions"
        }
      ]
    }
  ],
  "ChangeSetTags": [
    {
      "Key": "Environment",
      "Value": "Production"
    }
  ]
}
```

**Manage tags on existing resources**

Use the `TagResource` and `UntagResource` API operations to manage tags on existing solutions and change sets. Use `ListTagsForResource` to view current tags.

For more information, see [Managing tags on resources](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-api-access-control.html#managing-tags-on-resources) and [Adding tags to an entity and change set during creation](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-api-access-control.html#example-adding-tags-entity-creation).

## Create a solution
<a name="create-solution"></a>

You can use the `CreateSolution` change type to create a new solution document with only a solution ID and name. Other values aren't yet filled in.

When your request is processed successfully, AWS Marketplace creates a solution in `Draft` status for you. This incomplete solution isn't visible to buyers on AWS Marketplace.

You then use other change types to complete the solution: `UpdateInformation`, `UpdateRelatedProducts`, `UpdateBuyerEngagementOptions` (optional for creating a `Limited` solution), and `ReleaseSolution`. The `ReleaseSolution` change type validates that all required fields needed for a `Limited` solution are present on the solution, and then moves it to `Limited` visibility.

**Note**  
To move a solution to Public status or to change a solution's status, use the `UpdateVisibility` change type after providing the required values.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateSolution",
      "Entity": {
        "Type": "Solution@1.0"
      },
      "ChangeName": "CreateSolutionChange",
      "DetailsDocument": {
        "Name": "solution_for_customerX_en",
        "Title": "New Partner Solution"
      }
    }
  ]
}
```

Provide information for the fields to add the `CreateSolution` change type:
+ `Entity` (object) (required) – The named type of the solution entity being created.
  + `Type` (string) (required) – The `Type` must be `Solution@1.0`.
+ `DetailsDocument` (object) (required) – The details of the request.
  + `Name` (string) (required) – AWS resource name for seller's own reference only (not visible to buyers). Max length: 100 characters. Must not contain leading or trailing whitespaces, linebreaks or control characters. You can also update the solution tile via the `UpdateInformation` change type.
  + `Title` (string) (optional) – The title for your solution. Max length: 255 characters. Must not contain leading or trailing whitespaces, linebreaks or control characters. You can also set or update the solution title via the `UpdateInformation` change type.

**Response Syntax**

A change set is created for your request. The response gives you the `ChangeSetId` and `ChangeSetArn`:

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. You can check the status using the AWS Marketplace Management Portal or the `DescribeChangeSet` API operation.

When the request is completed successfully (if the `Status` is `SUCCEEDED`), a new solution ID is generated.

**Asynchronous Errors**

`CreateSolution` actions return specific errors, in addition to [common asynchronous errors](#solution-error-codes). You receive these errors from `DescribeChangeSet` after a change set finishes processing. To learn how to get change request status, see [Working with change sets](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_NAME | The solution Name length isn't valid. Enter a Name that's between 1 and 100 characters and try again. | 
| MISSING\_NAME | A Name value is required. Specify a Name value and try again. | 
| INVALID\_TITLE | The solution Title length isn't valid. Enter a Title that's between 1 and 255 characters and try again. | 

## Update solution information
<a name="update-solution-information"></a>

If you already have a solution in AWS Marketplace, you can use the Catalog API to update the solution information.

To update solution information, call the `StartChangeSet` API operation with the `UpdateInformation` change type and your updated details. See the following example.

**Note**  
The `UpdateInformation` change types behave like HTTP PATCH operations for top-level attributes. How fields are updated:  
If a top-level attribute is present in the `DetailsDocument`, the workflow validates your input and overwrites existing values.
If a top-level field is not present in the `DetailsDocument`, the existing value is preserved.
To unset an optional field, send an explicit JSON `null` for that field.

AWS Marketplace verifies and ingests logo and promotional media assets into an AWS Marketplace-owned location. DescribeEntity returns an accessible URL for the ingested files, not your original input from StartChangeSet. To see your original submitted URLs, use the DescribeChangeSet API.

**Note**  
When you modify `PromotionalMedia` asset files (by providing new URLs) on a `Public` solution, `UpdateInformation` requires manual review from the AWS Marketplace Seller Operations team. This increases execution time. In this scenario, use `UpdateInformation` separately in its own change set.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateInformation",
      "Entity": {
        "Identifier": "soln-1234abcd",
        "Type": "Solution@1.0"
      },
      "DetailsDocument": {
        "Name": "project_cold_harbor",
        "Title": "My Awesome Solution",
        "ShortDescription": "Solution value proposition",
        "LongDescription": "Detailed solution description explaining how this addresses customer needs",
        "LogoUrl": "https://s3.amazonaws.com/awsmp-logos/logo.jpg",
        "PromotionalMedia": [
          {
            "Type": "Image",
            "Url": "https://s3.amazonaws.com/awsmp-media/image.jpg",
            "Title": "Sample image",
            "Description": "Sample image description"
          },
          {
            "Type": "Video",
            "Url": "https://s3.amazonaws.com/awsmp-media/video.mp4",
            "Title": "Sample video",
            "PreviewUrl": "https://s3.amazonaws.com/awsmp-media/preview.png",
            "Description": "Sample video description"
          }
        ],
        "AdditionalResources": [
          {
            "Text": "Troubleshooting guide",
            "Url": "https://example.com/troubleshooting"
          }
        ],
        "UseCases": [
          {
            "Group": "advertising_and_marketing",
            "SubGroup": "ad_intelligence_and_measurement",
            "Item": "amazon_ads_insights",
            "Description": "Highlight description of this use case"
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateInformation` change type:
+ `Entity` (object) (required) – The named type of entity being updated.
  + `Identifier` (string) (required) – The solution ID.
  + `Type` (string) (required) – Must be `Solution@1.0`.
+ `DetailsDocument` (object) (required) – The details of the request including the information that you want to update for your solution. Each field is optional, but you must include at least one change to update.
  + `Name` (string) — The resource name of the solution, visible only to the seller via Catalog API read operations, not visible to buyers. Max length: 100 characters. Must not contain leading or trailing whitespaces, linebreaks or control characters.
  + `Title` (string) – The title of the solution to be displayed to buyers. Max length: 255 characters. Must not contain leading or trailing whitespaces, linebreaks or control characters.
  + `ShortDescription` (string) – The value proposition description of key aspects of the solution to be displayed to buyers. This is usually 2–3 sentences. Max length: 1000 characters. Must not contain leading or trailing whitespaces or control characters.
  + `LongDescription` (string) – The longer description of this solution to be displayed to buyers. This is usually 1–3 paragraphs. Max length: 5000 characters. Must not contain leading or trailing whitespaces or control characters.
  + `LogoUrl` (string) – The URL to an image in a publicly accessible Amazon S3 bucket or a presigned S3 URL. Must be a direct S3 URL (not behind CloudFront or API Gateway). Max length: 2048 characters. For logo specifications, see [Company and product logo requirements](https://docs.aws.amazon.com/marketplace/latest/userguide/product-submission.html#seller-and-product-logos).
  + `PromotionalMedia` (array of objects) – The list of promotional images and videos. Max 15 items (5 videos and 10 images). For promotional media specifications, see [Enhance your AWS Marketplace product with promotional media](https://docs.aws.amazon.com/marketplace/latest/userguide/promotional-media.html).
    + `Type` (string) (required) – Either `Image` or `Video`.
    + `Url` (string) (required) – The URL to the media file. Must be a direct S3 URL or presigned S3 URL. Max length: 2048 characters. Must be an https URL.
    + `Title` (string) (required) – The title of the media. Max length: 100 characters. Must not contain leading or trailing whitespaces, linebreaks, or control characters.
    + `Description` (string) (required) – The description of the media. Max length: 200 characters. Must not contain leading or trailing whitespaces or control characters.
    + `PreviewUrl` (string) (optional) – For videos only, the URL to a preview image. Max length: 2048 characters. Must be an https URL.
  + `AdditionalResources` (array of objects) – The list of references to additional resources. Max 8 items.
    + `Text` (string) – The name or title of the resource. Max length: 500 characters. Must not contain leading or trailing whitespaces, linebreaks, or control characters.
    + `Url` (string) – The URL to the resource. Max length: 2048 characters. Must be an https URL.
  + `UseCases` (array of objects) – The list of use cases that this solution addresses. Max 3 items. For valid use case categories (a combination of Group, SubGroup, and Item), see [use case categories list](https://d1z4dgsxp8pfa2.cloudfront.net/awsmp-solutions/use-case-categories-list.json) for active accepted values and their [introduction labels](https://d1z4dgsxp8pfa2.cloudfront.net/awsmp-solutions/i18n/en.json). The combination of Group, SubGroup, and Item must be a valid item in the use case categories list.
    + `Group` (string) – Industry or technology category. Must be one of the Group values in [use case categories list](https://d1z4dgsxp8pfa2.cloudfront.net/awsmp-solutions/use-case-categories-list.json).
    + `SubGroup` (string) – Use case group within the category. Must be one of the SubGroup values in [use case categories list](https://d1z4dgsxp8pfa2.cloudfront.net/awsmp-solutions/use-case-categories-list.json).
    + `Item` (string) – Specific use case. Must be one of the Item values in [use case categories list](https://d1z4dgsxp8pfa2.cloudfront.net/awsmp-solutions/use-case-categories-list.json).
    + `Description` (string) – Description of how this solution addresses the use case. Max length: 500 characters. Must not contain leading or trailing whitespaces or control characters.

For presigned URL information, see [Sharing objects with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html).

**Note**  
When calling UpdateInformation change type, you can always provide a subset of fields to be updated in the `DetailsDocument` object. However, before moving a solution from `Draft` to `Limited`, the following fields must be set properly: `Title`, `ShortDescription`, `LongDescription`, and `LogoUrl`.  
However, when you are updating existing fields on the solution, you can include only the attributes that need to be changed in the `DetailsDocument` object of the `UpdateInformation` change type.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. To check request status, use the AWS Marketplace Management Portal or call the `DescribeChangeSet` API.

After triggering this change type with `PromotionalMedia` assets modified for a `Public` solution, it can take up to 37 days to complete. This includes the time the AWS Marketplace Seller Operations Team needs to review, audit, and approve.

**Asynchronous Errors**

In addition to [common asynchronous errors](#solution-error-codes), the following errors are specific to `UpdateInformation` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_SHORT\_DESCRIPTION | The solution ShortDescription length isn't valid. Enter a ShortDescription that's between 1 and 1000 characters and try again. | 
| INVALID\_LONG\_DESCRIPTION | The solution LongDescription length isn't valid. Enter a LongDescription that's between 1 and 5000 characters and try again. | 
| INVALID\_NAME | The solution Name length isn't valid. Enter a Name that's between 1 and 100 characters and try again. | 
| INVALID\_TITLE | The solution Title length isn't valid. Enter a Title that's between 1 and 255 characters and try again. | 
| INVALID\_ADDITIONAL\_RESOURCES | The solution AdditionalResources[%d].Text length isn't valid. Enter a Text that's between 1 and 500 characters and try again. | 
| INVALID\_ADDITIONAL\_RESOURCES | The following URLs in the provided additional resources are inaccessible: [%s]. Provide valid and accessible URLs | 
| INVALID\_ADDITIONAL\_RESOURCES | A Url value is required. Specify a Url value and try again. | 
| INVALID\_ADDITIONAL\_RESOURCES | Text cannot be missing. Provide a Text | 
| INVALID\_USE\_CASE | The solution UseCases[%d].Description length isn't valid. Enter a Description that's between 1 and 500 characters and try again. | 
| INVALID\_USE\_CASE | UseCases[%d].Group: The provided Group (%s) is invalid. Provide a valid Group. | 
| INVALID\_USE\_CASE | UseCases[%d].SubGroup: The provided Group (%s) is invalid. Provide a valid SubGroup. | 
| INVALID\_USE\_CASE | UseCases[%d].Item: The provided Item (%s) is invalid. Provide a valid Item. | 
| INVALID\_USE\_CASE | UseCases[%d].Item: The provided use case is inactive. Provide an active use case | 
| INVALID\_USE\_CASE | UseCases[%d].Group: Group cannot be missing. Provide a Group. | 
| INVALID\_USE\_CASE | UseCases[%d].SubGroup: SubGroup cannot be missing. Provide a SubGroup. | 
| INVALID\_USE\_CASE | UseCases[%d].Item: SubGroup cannot be missing. Provide a Item. | 
| INVALID\_MEDIA | The solution PromotionalMedia[%d].Title length isn't valid. Enter a Title that's between 1 and 100 characters and try again. | 
| INVALID\_MEDIA | The solution PromotionalMedia[%d].Description length isn't valid. Enter a Description that's between 1 and 200 characters and try again. | 
| INVALID\_MEDIA | Invalid URL: %s Provide a new URL for media stored in S3. | 
| INVALID\_MEDIA | Media location not accessible: %s Provide a new, accessible URL for media stored in one of the following locations: [S3]. | 
| INVALID\_MEDIA | Image size exceeds %s. Provide an image that is under %s. | 
| INVALID\_MEDIA | Video size exceeds %s. Provide an video that is under %s. | 
| INVALID\_MEDIA | Logo size exceeds %s. Provide an logo that is under %s. | 
| INVALID\_MEDIA | Malware detected in %s. Provide media without malware. | 
| INVALID\_MEDIA | Inappropriate content: %s detected. Provide media with no inappropriate content | 
| INVALID\_MEDIA | Explicit content in %s: '{ExplicitContent}' detected. Provide media without explicit content. | 
| INVALID\_MEDIA | PromotionalMedia[%s].Url: %s is not in a supported format (%s). Use a well-formed image in a supported format: [JPEG, PNG]. | 
| INVALID\_MEDIA | PromotionalMedia[%s].Url: %s is not in a supported format (%s). Use a well-formed video in a supported format: [MP4, MOV]. | 
| INVALID\_MEDIA | LogoUrl at %s has invalid aspect ratio. Provide an image with 1:1 (square) or 2:1 (wide) aspect ratio. | 
| INVALID\_MEDIA | Logo: %s has invalid dimensions. Provide an image between 120x120 and 1080x1080 pixels. | 
| INVALID\_MEDIA | PromotionalMedia[%d].Type is not supported. Provide PromotionalMedia in a supported type: %s | 
| DUPLICATE\_MEDIA | Duplicate media detected: [%s] Provide media items with no duplicates. | 
| INVALID\_MEDIA | PromotionalMedia[%d].Url: Malware detected in %s. Provide media without malware. | 
| TOO\_MANY\_ITEMS | Provide no more than %d %s. | 

## Update related products
<a name="update-related-products"></a>

You can use the Catalog API to update the products and services included in your solution, including AWS Marketplace products and non-AWS Marketplace products.

To update related products, call the `StartChangeSet` API operation with the `UpdateRelatedProducts` change type, as shown in the following example.

**Note**  
The `UpdateRelatedProducts` change type behaves like an HTTP PATCH operation for top-level attributes. You can provide all current AWS Marketplace product types as `AwsMarketplaceProducts` in `UpdateRelatedProducts`.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateRelatedProducts",
      "Entity": {
        "Type": "Solution@1.0",
        "Identifier": "soln-123456"
      },
      "DetailsDocument": {
        "IntegrationDescription": "How to use the products in this solution (usage guide)",
        "AwsMarketplaceProducts": [
          {
            "ProductId": "prod-123"
          },
          {
            "ProductId": "prod-456"
          }
        ],
        "NonAwsMarketplaceProducts": [
          {
            "Type": "Hardware",
            "Title": "Diamond engine",
            "Description": "Hardware details",
            "Url": "https://example.com/hardware-product-specs.html"
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateRelatedProducts` change type:
+ `Entity` (object) (required) – The named type of entity being updated.
  + `Identifier` (string) (required) – The solution ID.
  + `Type` (string) (required) – Must be `Solution@1.0`.
+ `DetailsDocument` (object) (required) – The details of the request. Each field is optional, but you must include at least one change to update.
  + `IntegrationDescription` (string) – Description of how the products work together in this solution. Max length: 5000 characters. Must not contain leading or trailing whitespaces or control characters.
  + `AwsMarketplaceProducts` (array of objects) – AWS Marketplace products included in this solution. Max 5 items
    + `ProductId` (string) – AWS Marketplace product ID (a UUID or a string beginning with `prod-`). Max length: 50 characters.
  + `NonAwsMarketplaceProducts` (array of objects) – Products not available on AWS Marketplace. Max 5 items.
    + `Type` (string) (required) – Type of the product. Possible values: `Software`, `Consulting`, `Hardware`, `Communication`, `Professional Service`, `Managed Service`, `Value-Added Resale`, `Training`
    + `Title` (string) (required) – Title of the product. Max length: 255 characters. Must not contain leading or trailing whitespaces, linebreaks, or control characters.
    + `Description` (string) (optional) – Description of the product. Max length: 220 characters. Must not contain leading or trailing whitespaces or control characters.
    + `Url` (string) (optional) – URL to more information about the product. Max length: 2048 characters. Must be an https url.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed.

To check request status, use the AWS Marketplace Management Portal or call the `DescribeChangeSet` API.

**Asynchronous Errors**

In addition to [common asynchronous errors](#solution-error-codes), the following errors are specific to `UpdateRelatedProducts` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_OPERATION\_UPDATE\_RELATED\_PRODUCTS\_SOLUTION | The operation to update related products isn't supported for public solutions. To make this change, first change the solution's visibility to limited and try again. | 
| INVALID\_AWS\_MARKETPLACE\_PRODUCTS | AWS Marketplace product '%s' is not available for your account. Choose a Public product or a Limited product where you have allowlist access, or contact the seller to request access. | 
| INVALID\_AWS\_MARKETPLACE\_PRODUCTS | The specified product type '%s' isn't supported. Provide one of these valid product types: [AmiProduct, SaaSProduct, ContainerProduct, MachineLearningProduct, ProfessionalServicesProduct, DataProduct] and try again. | 
| INVALID\_AWS\_MARKETPLACE\_PRODUCTS | Product '%s' not found. Provide a valid product ID in the same catalog. | 
| INVALID\_NON\_AWS\_MARKETPLACE\_PRODUCTS | The specified Non-AWS Marketplace product URLs aren't accessible: [%s]. Verify that the URLs are valid and publicly accessible, and try again. | 
| INVALID\_INTEGRATION\_DESCRIPTION | Provide a solution IntegrationDescription between 1 and 5000 characters. | 
| INVALID\_NON\_AWS\_MARKETPLACE\_PRODUCTS | The solution NonAwsMarketplaceProduct[%d].Title length isn't valid. Enter a Description that's between 1 and 255 characters and try again. | 
| INVALID\_NON\_AWS\_MARKETPLACE\_PRODUCTS | The solution NonAwsMarketplaceProduct[%d].Description length isn't valid. Enter a Description that's between 1 and 220 characters and try again. | 
| INVALID\_NON\_AWS\_MARKETPLACE\_PRODUCTS | The solution NonAwsMarketplaceProduct[%d].Type length isn't valid. Enter a Type that's between 1 and 50 characters and try again. | 
| INVALID\_NON\_AWS\_MARKETPLACE\_PRODUCTS | NonAwsMarketplaceProduct[%d].Type is not a valid non-AWS Marketplace product type. Provide one of the following non-AWS Marketplace product types: [%s] | 
| INVALID\_NON\_AWS\_MARKETPLACE\_PRODUCTS | A NonAwsMarketplaceProduct[%d].Title value is required. Specify a Title value and try again. | 
| INVALID\_NON\_AWS\_MARKETPLACE\_PRODUCTS | A NonAwsMarketplaceProduct[%d].Type value is required. Specify a Type value and try again. | 
| TOO\_MANY\_PRODUCTS | The maximum number of AWS Marketplace products you can link is %d. Remove existing linked products before adding new ones. | 
| TOO\_MANY\_PRODUCTS | The maximum number of none AWS Marketplace products you can add is %d. Remove existing none AWS Marketplace products before adding new ones. | 
| INVALID\_AWS\_MARKETPLACE\_PRODUCTS | Duplicate AWS Marketplace product IDs aren't allowed. Each product ID must be unique in your solution. | 
| INVALID\_REMOVE\_OPERATION | Invalid operation, you can not remove all products. | 

## Release a solution
<a name="release-solution"></a>

You can use the Catalog API to publish a `Draft` solution into `Limited` visibility in AWS Marketplace.

The `ReleaseSolution` change type validates that all required fields for a `Limited` solution are present. It then moves the solution from `Draft` to `Limited` visibility. Once a solution is in `Limited` visibility, you cannot move it back to `Draft` visibility.

To release a solution, call the `StartChangeSet` API operation with the `ReleaseSolution` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "ReleaseSolution",
      "Entity": {
        "Type": "Solution@1.0",
        "Identifier": "soln-1234abcd"
      },
      "DetailsDocument": {}
    }
  ]
}
```

Provide information for the fields to add the `ReleaseSolution` change type:
+ `Entity` (object) (required) – The named type of entity being released.
  + `Identifier` (string) (required) – The solution ID.
  + `Type` (string) (required) – Must be `Solution@1.0`.
+ `DetailsDocument` (object) (required) – Must be an empty object. The change type `ReleaseSolution` doesn't accept any details.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `DescribeChangeSet` API operation.

**Asynchronous Errors**

In addition to [common asynchronous errors](#solution-error-codes), the following errors are specific to `ReleaseSolution` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| MISSING\_REQUIRED\_FIELDS | The request is missing required parameters: [%s]. Specify values for all required parameters and try again. | 
| INCOMPATIBLE\_OPERATION\_RELEASE\_SOLUTION | The change type can only be invoked on Solutions in Draft status. Update the Solution's visibility to Draft and try again. | 

## Update buyer engagement options
<a name="update-buyer-engagement-options"></a>

You can use the Catalog API to configure how buyers engage with you about your solution.

**Note**  
To use this change type, you must have active enrollment in the [APN Customer Engagements (ACE)](https://aws.amazon.com/partners/programs/ace/) program. You must also link your AWS account with your AWS Partner Central account that has enrolled in ACE. For instructions, see [Linking AWS Partner Central and AWS accounts](https://docs.aws.amazon.com/partner-central/latest/getting-started/account-linking.html).

To update buyer engagement options, call the `StartChangeSet` API operation with the `UpdateBuyerEngagementOptions` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateBuyerEngagementOptions",
      "Entity": {
        "Type": "Solution@1.0",
        "Identifier": "soln-1234abcd"
      },
      "DetailsDocument": [
        {
          "EngagementOption": "RequestProductDemo"
        },
        {
          "EngagementOption": "RequestPrivateOffer"
        }
      ]
    }
  ]
}
```

Provide information for the fields to add the `UpdateBuyerEngagementOptions` change type:
+ `Entity` (object) (required) – The named type of entity being updated.
  + `Identifier` (string) (required) – The solution ID.
  + `Type` (string) (required) – Must be `Solution@1.0`.
+ `DetailsDocument` (array of objects) (required) – The buyer engagement options to enable.
  + `EngagementOption` (string) (required) – The type of engagement option. Valid values: `RequestPrivateOffer`, `RequestProductDemo`.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed.

To check request status, use the AWS Marketplace Management Portal or call the `DescribeChangeSet` API.

**Asynchronous Errors**

In addition to [common asynchronous errors](#solution-error-codes), the following errors are specific to `UpdateBuyerEngagementOptions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INELIGIBLE\_SELLER | ACE eligibility validation isn't complete. To proceed: 1) Link your AWS Marketplace account to your APN account, 2) Complete the ACE eligibility requirements. | 

## Update solution visibility
<a name="update-solution-visibility"></a>

You can use the Catalog API to update the visibility of a solution in AWS Marketplace.

You can set target visibilities to `Limited`, `Public`, or `Restricted`.
+ **`Limited`** – The solution is complete and has successfully completed the `ReleaseSolution` change type. You can preview buyer website details of the solution in this visibility. On the AWS Marketplace buyer website, the solution is visible only to the owning account, the owners of each AWS Marketplace product included in the solution, and the AWS Marketplace Seller Operations team.
+ **`Public`** – The solution is visible on AWS Marketplace. Buyers can view and engage with the solution.
+ **`Restricted`** – The solution is no longer visible to the public on the AWS Marketplace buyer website.

**Note**  
To move a solution to `Public` visibility, you must meet the following requirements:  
You must have a public profile on AWS Marketplace.
The solution must have no non-`Public` products.
The solution must have at least 2 `Public` AWS Marketplace products.
The solution must have at least 1 AWS Marketplace product from the same AWS account.
The solution must have the `RequestPrivateOffer` buyer engagement option enabled.
The AWS Marketplace Seller Operations team reviews all requests to move a solution to `Public` visibility. For support, see [Getting support for AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/getting-support.html).

When you set `TargetVisibility` to `Public`, the `UpdateVisibility` change type requires manual review from the AWS Marketplace Seller Operations team. This increases execution time. Use `UpdateVisibility` separately in its own change set.

To update your solution's visibility, call the `StartChangeSet` API operation with the `UpdateVisibility` change type, as shown in the following example.

**Request Syntax**

For when `TargetVisibility` is `Public` or `Limited`.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateVisibility",
      "Entity": {
        "Type": "Solution@1.0",
        "Identifier": "soln-1234abcd"
      },
      "DetailsDocument": {
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
  "ChangeSet": [
    {
      "ChangeType": "UpdateVisibility",
      "Entity": {
        "Type": "Solution@1.0",
        "Identifier": "soln-1234abcd"
      },
      "DetailsDocument": {
        "TargetVisibility": "Restricted"
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateVisibility` change type:
+ `Entity` (object) (required) – The named type of entity being updated.
  + `Identifier` (string) (required) – The solution ID.
  + `Type` (string) (required) – Must be `Solution@1.0`.
+ `DetailsDocument` (object) (required) – The details required to run the change set.
  + `TargetVisibility` (string) (required) – The intended new visibility of the solution. Possible values: `Public`, `Limited`, and `Restricted`.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `DescribeChangeSet` API operation.

After triggering this change type with `TargetVisibility` as `Public`, it can take up to 37 days to complete. This includes the time the AWS Marketplace Seller Operations Team needs to review, audit, and approve.

**Asynchronous Errors**

The following errors are specific to `UpdateVisibility` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_VISIBILITY\_TRANSITION | The solution can't be moved back to Draft state. Once released, solutions can only transition between Limited, Public, and Restricted states. | 
| TOO\_FEW\_USE\_CASES | At least one use case is required to make a solution public. Add a use case and try again. | 
| TOO\_FEW\_PUBLIC\_PRODUCTS | A minimum of 2 public AWS Marketplace products are required to make a solution public. Add the required products and try again. | 
| INCOMPATIBLE\_PRODUCTS | The solution contains one or more non-public AWS Marketplace products. To make the solution public, remove all non-public products and try again. | 
| TOO\_FEW\_SELF\_OWNED\_PRODUCTS | The solution requires at least one AWS Marketplace product owned by the solution owner. Add an AWS Marketplace product from your account and try again. | 
| INCOMPATIBLE\_BUYER\_ENGAGEMENT\_OPTIONS | The RequestPrivateOffer buyer engagement option must be enabled to make this solution public. Enable RequestPrivateOffer and try again. | 
| INCOMPATIBLE\_OPERATION\_UPDATE\_VISIBILITY | UpdateVisibility isn't supported for solutions in Draft state. Publish the solution first from Draft to Limited using ReleaseSolution, then use UpdateVisibility to change to Public or Restricted. | 
| LIMIT\_EXCEEDED\_TOO\_MANY\_PUBLIC\_SOLUTIONS | This account has reached its limit of 5 public solutions. Update an existing public solution to Limited or Restricted visibility and try again. | 
| MISSING\_SELLER\_PROFILE\_INFORMATION | A public seller profile is required to make solutions public. Create a public profile in your seller account and try again. | 

## Common asynchronous error codes
<a name="solution-error-codes"></a>

There are some asynchronous validation that applies across all solution change types, such as checks for url validity and unsupported character, and their error codes and error messages are listed here.

Each URL field provided must use HTTPS protocol, and conform to RFC2396 or RFC 2732 standards.


| Error code | Error message | 
| --- | --- | 
| INVALID\_INPUT | Invalid '%s' field. Remove unsupported characters %s. | 
| INVALID\_INPUT | Inappropriate content '%s' found in %s field. Provide %s with no inappropriate content. | 
| UNSUPPORTED\_CATALOG | Requested catalog %s is not supported by this change type. | 
| INVALID\_REMOVE\_OPERATION | Invalid operation, you can not remove %s | 
| AUDIT\_ERROR | (varies based on AWS Marketplace Seller Operations team audit result) | 

## Solution lifecycle
<a name="solution-lifecycle"></a>

Solutions progress through the following visibility values:
+ `Draft` - Initial visibility after creation. You can progressively add information using other change types.
+ `Limited` - Solution is complete and visible to you and product owners for preview. You achieve this by using `ReleaseSolution`.
+ `Public` - Solution is visible to all buyers browsing the AWS Marketplace website. This requires additional validation.
+ `Restricted` - Solution is no longer visible to new buyers.

**Important**  
Once a solution moves from `Draft` to `Limited` visibility, you cannot move it back to `Draft`. `ReleaseSolution` validates that all required fields for a `Limited` solution are present before the transition to `Limited` visibility.

### Minimum requirements for a complete solution
<a name="minimum-requirements-complete-solution"></a>

To create a complete solution and publish it beyond Draft status, you need the following change types and attributes:
+ **`CreateSolution`**: `Name`
+ **`UpdateInformation`**: `Title`, `ShortDescription`, `LongDescription`, `LogoUrl`
+ **`UpdateRelatedProducts`**: `IntegrationDescription`, at least one item across `AwsMarketplaceProducts` and `NonAwsMarketplaceProducts`
+ **`ReleaseSolution`**

The following example shows you how to create a complete solution with `Limited` visibility in a single change set:

```
{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateSolution",
      "Entity": {
        "Type": "Solution@1.0"
      },
      "ChangeName": "CreateSolutionChange",
      "DetailsDocument": {
        "Name": "complete_solution_example",
        "Title": "Complete Solution Example"
      }
    },
    {
      "ChangeType": "UpdateInformation",
      "Entity": {
        "Type": "Solution@1.0",
        "Identifier": "$CreateSolutionChange.Entity.Identifier"
      },
      "ChangeName": "UpdateInformationChange",
      "DetailsDocument": {
        "ShortDescription": "A comprehensive solution for customer needs",
        "LongDescription": "This solution combines multiple products to address specific customer requirements in the advertising and marketing space.",
        "LogoUrl": "https://s3.amazonaws.com/awsmp-logos/solution-logo.jpg",
        "UseCases": [
          {
            "Group": "advertising_and_marketing",
            "SubGroup": "ad_intelligence_and_measurement",
            "Item": "amazon_ads_insights",
            "Description": "Provides comprehensive advertising insights and measurement capabilities"
          }
        ]
      }
    },
    {
      "ChangeType": "UpdateRelatedProducts",
      "Entity": {
        "Type": "Solution@1.0",
        "Identifier": "$CreateSolutionChange.Entity.Identifier"
      },
      "ChangeName": "UpdateRelatedProductsChange",
      "DetailsDocument": {
        "AwsMarketplaceProducts": [
          {
            "ProductId": "prod-123"
          }
        ],
        "IntegrationDescription": "These products work together to provide end-to-end advertising analytics and optimization capabilities."
      }
    },
    {
      "ChangeType": "UpdateBuyerEngagementOptions",
      "Entity": {
        "Type": "Solution@1.0",
        "Identifier": "$CreateSolutionChange.Entity.Identifier"
      },
      "ChangeName": "UpdateBuyerEngagementChange",
      "DetailsDocument": [
        {
          "EngagementOption": "RequestPrivateOffer"
        }
      ]
    },
    {
      "ChangeType": "ReleaseSolution",
      "Entity": {
        "Type": "Solution@1.0",
        "Identifier": "$CreateSolutionChange.Entity.Identifier"
      },
      "ChangeName": "ReleaseSolutionChange",
      "DetailsDocument": {}
    }
  ]
}
```

## IAM permissions for solutions
<a name="solution-iam-permissions"></a>

AWS Marketplace Catalog API uses standard IAM permissions. See [Access control for the AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-api-access-control.html) for more details.

You can use `AWSMarketplaceSellerProductFullAccess` to perform all operations necessary for accessing Solution via Catalog API and Partner Central 3.0 in AWS Management Console.

### Sample IAM policy for solutions
<a name="sample-iam-policy-solutions"></a>

The following sample IAM policy allows specific actions (`DescribeEntity`, `ListEntities`, and `StartChangeSet`) on `Solution@1.0` entity. You can further narrow it down to restrict a principal's access to certain change types on certain entity IDs, or widen it up to allow a principal to also operate on another entity type supported by Catalog API.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartChangeSet"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/*",
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/*"
      ],
      "Condition": {
        "StringEquals": {
          "catalog:ChangeType": [
            "CreateSolution",
            "UpdateInformation",
            "UpdateRelatedProducts",
            "ReleaseSolution",
            "UpdateBuyerEngagementOptions",
            "UpdateVisibility"
          ]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:ListEntities",
        "aws-marketplace:DescribeEntity"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:DescribeChangeSet",
        "aws-marketplace:ListChangeSets",
        "aws-marketplace:CancelChangeSet"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:TagResource",
        "aws-marketplace:UntagResource",
        "aws-marketplace:ListTagsForResource"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/*",
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/*"
      ]
    }
  ]
}
```

### Restricting access to specific solutions
<a name="restricting-access-specific-solutions"></a>

You can restrict access to specific solutions by using the solution ID in the resource ARN:

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:DescribeEntity",
        "aws-marketplace:StartChangeSet"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/soln-specific123"
      ]
    }
  ]
}
```

### Restricting access to specific change types
<a name="restricting-access-specific-change-types"></a>

You can restrict access to specific change types using condition keys:

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartChangeSet"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/*"
      ],
      "Condition": {
        "StringEquals": {
          "catalog:ChangeType": [
            "UpdateInformation",
            "UpdateRelatedProducts"
          ]
        }
      }
    }
  ]
}
```