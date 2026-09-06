

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Using the AWS Marketplace Catalog API
<a name="catalog-apis"></a>

The AWS Marketplace Catalog API service provides an API interface to manage AWS Marketplace for your AWS organization or AWS account. For approved sellers, you can manage your products programmatically, including the self-service publishing capabilities on the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management). For private marketplace administrators, you can manage your private marketplace programmatically.

With Catalog API actions, you can view and update your existing product programmatically. You can automate your product update process by integrating the AWS Marketplace Catalog API with your AWS Marketplace product build or deployment pipelines. You can also create your own applications on top of the Catalog API to manage your products in AWS Marketplace. You can manage the products that users in your AWS account or AWS organization can see and purchase through your private marketplace.

The AWS Marketplace Catalog API service provides standard AWS API functionality. You can directly use the REST API actions described in [Actions](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_Operations.html), or you can use an AWS SDK to access an API that's tailored to the programming language or platform that you're using. For more information about AWS application development, see [Getting Started with AWS](https://aws.amazon.com/getting-started/). For more information about using AWS SDKs, see [AWS SDKs](https://aws.amazon.com/tools/#SDKs).

## Catalog API entities
<a name="catalog-api-entities"></a>

AWS Marketplace entities are containers of data which serve different business purposes, such as a product or offer. Entities are categorized by types. Each entity type encapsulates data related to a specific business domain (for example, a product or a seller account).

To simplify this paradigm, entities are designed with some level of commonality in their structures. As a result, introducing a new business domain doesn't require that you learn a completely new structure.

### General structure
<a name="general-structure"></a>

The general structure of any entity is:
+ A named type with a version
+ An identifier for the specific instance of the type
+ One or more facets that include the attributes of the entity

### Type versioning
<a name="versioning"></a>

Every named type has a type and version associated with it, for example, `{{Entity}}Product@1.0`. The *type* ({{Entity}}Product) represents the classification of the content. The *version* (1.0) represents the structure of {{Entity}}Product.

The version gives you details about the structure of the entity. The following describes when a version will be changed:
+ Existing entities won't be restructured without changing the version. Additions of optional new fields will result in a minor version update.
+ Any feature that fundamentally changes the structure of a type leads to a major version update. Examples include:
  + Removing a field
  + Renaming a field (different name for the same semantic)
  + Changing the semantic of an existing field (for example, changing the expected type)
+ A major version update can retain a subset of facets from the previous version. 
+ Users are provided notifications and documentation for new versions.

### Identifier
<a name="identifier"></a>

Each entity represents a unique *thing* within a business domain. To identify the unique thing, we use an identifier associating an `EntityId` with a `RevisionId`, for example, {{prod-ad8EXAMPLE651}}@{{3}}. In this example, the `EntityId` is `prod-ad8EXAMPLE651` and the `RevisionId` is `3`. Every successful change request to the entity will update the revision.

The following are important details about the identifier:
+ Each entity is uniquely identified by its `EntityId`, which is the key to globally distinguish one entity from another.
+ Each published revision of an entity has a `RevisionId`. The `RevisionId`, along with the `EntityId`, distinguish one published revision from another.
+ AWS Marketplace generates `EntityId`s and `RevisionId`s.

You can use the `DescribeEntity` action to find the details and the Identifier with the most recent `revisionId`.

The `RevisionId` is an optional part of requests to `StartChangeSet` (see [Working with change sets](#working-with-change-sets)). If you include a `RevisionId`, then the request to `StartChangeSet` will fail with a `ValidationException` if the `RevisionId` is not the latest revision of the entity. This allows you to implement optimistic locking in your application.

**Note**  
When you include a `RevisionId` that is not the latest revision, the `ValidationException` message includes the latest `RevisionId`.

If you omit the `RevisionId`, the request is performed on the latest revision of the entity automatically.

**Warning**  
Two requests to change the same object could result with one request overwriting the changes of the other request, as the second request rewrites data changed by the first request. Using `RevisionId`s in your requests prevents this issue by not allowing a change to an earlier revision to overwrite the current revision.

### Facets
<a name="facets"></a>

A facet is a logical grouping of attributes. An entity usually includes several facets which represent different aspects of the entity. The attributes within a facet have the following properties:
+ Each attribute has a unique name within the scope of the container it belongs to. 
+ Attributes can be of a simple type (string, integer, or floating number).
+ Attributes can be of a complex type (container/structure or array).

### Entity type
<a name="product-entity"></a>

The entity type defines what the entity represents. An entity can be a seller product in AWS Marketplace or a private marketplace. For more information, see [Working with seller products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html) and [Working with a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html).

## Working with change sets
<a name="working-with-change-sets"></a>

When using the Catalog API, requests are created and updated through entities and completed by using change requests. Every change specifies the entity to be changed, the type of change to be performed, and details of the change. The type of change to be performed is called a `ChangeType`. A collection of `ChangeType`s is called a `ChangeSet`.

 There are four actions that allow you to work with change sets: 
+  `StartChangeSet` – Requests a set of changes. The changes are added to a queue and processed. For more information, see [Working with seller products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html) and [Working with a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html).
+  `DescribeChangeSet` – Gets the details of a set of changes, including the status of the request. The statuses include: 
  + `PREPARING` – Getting ready to apply the changes.
  + `APPLYING` – In the process of making the requested changes.
  + `SUCCEEDED` – Request was completed successfully.
  + `CANCELLED` – Request was canceled by the user.
  + `FAILED` – Request was completed unsuccessfully. Further details are available in the response.
+  `ListChangeSets` – Gets a list of the change sets that are currently in process. 
+  `CancelChangeSet` – Requests a change set be canceled. Changes can only be canceled while in the `PREPARING` status. 

 A typical workflow is to request a change with `StartChangeSet`, and then use the returned `ChangeSetId` to poll the `DescribeChangeSet` action until the change is complete.

The following is an example of the `DescribeChangeSet` response.

```
{
  "ChangeSet":
  [
    {
      "ChangeName": "myChangeName",
      "ChangeType": "UpdateInformation",
      "Details": "{  \"ProductTitle\": \"My Product Title\",  \"ShortDescription\": \"My product short description.\",  \"LongDescription\": \"My product longer description.\",  \"Sku\": \"123example456\",  \"SupportDescription\": \"Need help? Contact our experts at support@example.com\\n\\nYour purchase includes 24x7 support.\",  \"Categories\": [    \"Operating Systems\",    \"Network Infrastructure\",    \"Application Development\"  ]}",
      "DetailsDocument":
      {
        "ProductTitle": "My Product Title",
        "ShortDescription": "My product short description.",
        "LongDescription": "My product longer description.",
        "Sku": "123example456",
        "SupportDescription": "Need help? Contact our experts at support@example.com\n\nYour purchase includes 24x7 support.",
        "Categories":
        [
          "Operating Systems",
          "Network Infrastructure",
          "Application Development"
        ]
      },
      "Entity":
      {
        "Identifier": "example1-abcd-1234-5ef6-7890abcdef12",
        "Type": "AmiProduct@1.0"
      },
      "ErrorDetailList":
      []
    }
  ],
  "ChangeSetArn": "arn:aws:aws-marketplace:[exampleARN]",
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetName": "myChangeSetName",
  "EndTime": "2023-03-03T00:00:00Z",
  "FailureCode": null,
  "FailureDescription": null,
  "StartTime": "2023-03-02T00:00:00Z",
  "Status": "SUCCEEDED"
}
```

**Note**  
When polling or working with change sets programmatically, you must adhere to the service limits. For more information, see [Service quotas for AWS Marketplace Catalog API](catalog-service-quotas.md).

After your change is complete, you can use `ListEntities` to find the entity that you created or modified (and its associated `EntityID`). You can then use `DescribeEntity` with the `EntityID` to get details about it.

For more information about working with change requests in the console for sellers, see [ Creating a change request](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-creating-change-request) in the *AWS Marketplace Seller Guide*. 

### Making multiple change requests simultaneously
<a name="parallel-requests"></a>

Within a **single change set**, you can bundle all change types and they are run together. Catalog API is built to make multiple changes simultaneously to provide the best performance. Sellers and Channel Partners can invoke changes with multiple `ChangeTypes` bundled into a `ChangeSet`. You can invoke multiple changes on single or different entities in the same `ChangeSet`. Catalog API evaluates which order the changes need to be applied and makes those changes.

However, if the requests are made as **separate change sets**, AWS Marketplace can't initiate conflicting change requests on the same product. In these cases, AWS Marketplace returns a `ResourceInUseException` error.
+ For modifying AMI and container products, most changes can be made without error, with the following exceptions:
  + If two requests are the same `ChangeType` on the same product, the second request returns an error.
  + If one request is to update the version information, and the other request is to restrict or add a version, then the second request returns an error.
  + If a request is `PREPARING`, another request can be made on the same product. However, a change that is currently `APPLYING` may block other requests, returning an error.
+ For other product types and private marketplaces, you can only have a single request for a product at a time. If a different request to update the same product is made while a first request is ongoing, the second returns an error.
+ If there is a request for any product that is pending with the AWS Marketplace Seller Operations team, then any other requests on that product return an error.

If you receive a `ResourceInUseException` error for a change request, you can retry the request later. Depending on the state of the ongoing request, you can also cancel the first request, to allow the resubmitted second request to complete sooner.

### Invoking multiple change types in one change set
<a name="multiple-change-types"></a>

You can use the Catalog API to combine and chain up to 20 changes in one `StartChangeSet` request targeting one or multiple different entities. 

A typical use case is to create a `SaaSProduct@1.0` draft product, an `Offer@1.0` draft offer, and also filling in the metadata information of the product and offer. This is done by including the following four change types in one change set:
+ `CreateProduct` on `SaaSProduct@1.0`

  Specify the `ChangeName` parameter. Then, the product created in this change type can be referenced in the same change set by subsequent changes. 

  For example, `CreateProductChange`.
+ `UpdateInformation` on the `SaaSProduct@1.0` created in the same change set

  In the `Entity.Identifier` field, you can refer to the product created by `CreateProduct` change type using the change name in this format: 

  `${ChangeName}.Entity.Identifier`

  For example, `$CreateProductChange.Entity.Identifier`.
+ `CreateOffer` on `Offer@1.0` tied to the `SaaSProduct@1.0` created in the same change set

  Specify the `ChangeName` parameter. Then, the product created in this change type can be referenced in the same change set by subsequent changes. For example, `CreateOfferChange`.

  For the `ProductId` parameter in the payload of `CreateOffer` change type, you can also refer to the SaaS product created in `CreateProduct` change type by using `${ChangeName}.Entity.Identifier` syntax.

  For example, `{"ProductId":"$CreateProductChange.Entity.Identifier"}`.
+ `UpdateInformation` on the `Offer@1.0` created in the same change set

  In the `Entity.Identifier` field, you can refer to the offer created by the `CreateOffer` change type using the change name in this format:

  `${ChangeName}.Entity.Identifier`

  For example, `$CreateOfferChange.Entity.Identifier`.

The following is an example of a combined change set.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateProduct",
      "Entity": {
        "Type": "SaaSProduct@1.0"
      },
      "ChangeName": "CreateProductChange",
      "DetailsDocument": {}
    },
    {
      "ChangeType": "UpdateInformation",
      "Entity": {
        "Type": "SaaSProduct@1.0",
        "Identifier": "$CreateProductChange.Entity.Identifier"
      },
      "ChangeName": "UpdateProductInformationChange",
      "DetailsDocument": {
        "ProductTitle": "My Product Title",
        "ShortDescription": "My product short description.",
        "LongDescription": "My product longer description.",
        "Sku": "123example456",
        "LogoUrl": "https://s3.amazonaws.com/presigned-or-public-url-to-logo-stored-in-s3",
        "VideoUrls": [
          "https://example.com"
        ],
        "Highlights": [
          "123example45"
        ],
        "AdditionalResources": "123example456",
        "SupportDescription": "Need help? Contact our experts at support@example.com \n\nYour purchase includes 24x7 support.",        
        "Categories": [
          "Operating Systems",
          "Network Infrastructure",
          "Application Development"
        ],
        "SearchKeywords": [
          "123example45"
        ],
      }
    },
    {
      "ChangeType": "CreateOffer",
      "Entity": {
        "Type": "Offer@1.0"
      },
      "ChangeName": "CreateOfferChange",
      "DetailsDocument": {
        "ProductId": "$CreateProductChange.Entity.Identifier"
      }
    },
    {
      "ChangeType": "UpdateInformation",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "$CreateOfferChange.Entity.Identifier"
      },
      "DetailsDocument": {
        "Name": "Offer created together with SaaSProduct",
        "Description": "Test offer created together with SaaSProduct in the same Catalog API change set"
      }
    }
  ]
}
```

## Working with the `Details` attribute (Legacy)
<a name="working-with-details"></a>

**Note**  
This section describes the legacy `Details` attribute in your change request, which requires additional formatting for your change details. We recommend using the alternative `DetailsDocument` attribute. It doesn't require additional formatting and the change details don't need to be changed. For examples of the `DetailsDocument` attribute, see [Working with seller products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html) and [Working with a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html).

The `Details` attribute of the `StartChangeSet` operation is a string value. Its contents are JSON objects. To put a JSON object into a string attribute, you must convert the object to a single-line string by escaping all JSON control characters, and removing line breaks.

For example, if you are using the `StartChangeSet` operation with `UpdateProcurementPolicy` to disable requests from users in your private marketplace, make a request like the following.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
   "Catalog": "AWSMarketplace",
   "ChangeSet": [ 
      { 
         "ChangeType": "UpdateProcurementPolicy",
         "Details": "{{<string>}}",
         "Entity": {
            "Type": "Experience@1.0",
            "Identifier" : "{{exp-1234example@5}}"
         }
      }
   ]
}
```

In this case, the JSON object that you use for the `Details` attribute looks like the following (before conversion to a string).

```
{
    "Configuration": {
        "PolicyResourceRequests": "Deny"
    }
}
```

But the `Details` attribute requires a string, not JSON. After converting this JSON object to a single line string, it looks like the following.

```
"{\"Configuration\" : {\"PolicyResourceRequests\" : \"Deny\"}}"
```

With this string, you can create the full change set request, as follows.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
   "Catalog": "AWSMarketplace",
   "ChangeSet": [ 
      { 
         "ChangeType": "UpdateProcurementPolicy",
         "Details": "{\"Configuration\" : {\"PolicyResourceRequests\" : \"Deny\"}}",
         "Entity": {
            "Type": "Experience@1.0",
            "Identifier" : "{{exp-1234example@5}}"
         }
      }
   ]
}
```

Generally, examples in this API reference show the JSON object already converted to a string. In some cases, more complicated samples with new lines are included to enhance understanding.

**Automate converting JSON to a string**

Converting a JSON object to a string can be automated using tools such as [jq](https://stedolan.github.io/jq/), a lightweight command-line JSON processor. The following example shows using `jq` to convert a JSON object to a string that can be used in the `Details` attribute.

```
DETAILS_JSON='{
  "ProductTitle": "My Product Title",
  "ShortDescription": "My product short description.",
  "LongDescription": "My product long description."
}';

DETAILS_JSON_STRING="$(echo "${DETAILS_JSON}" | jq 'tostring';)";
```

 If you echo `"${DETAILS_JSON_STRING}"`, the result is the following string with JSON properly escaped: `{\"ProductTitle\":\"My Product\",\"ShortDescription\":\"My product short description.\",\"LongDescription\":\"My product long description.\"}`

## Using DescribeEntity to get information about your entities
<a name="using-describe-entity"></a>

You can programmatically get information about your existing entities, including products and private marketplace, through the Catalog API.

The `ListEntities` action returns a list of entities. Then, you can use the `DescribeEntity` action to get details about an individual entity. This can be directly useful, for example, to catalog the products you sell. It can also be useful when updating entities, because you can get the current state of the entity before updating just the parts that you want to update.

The following example shows using `ListEntities` to get a list of container products, and then using `DescribeEntity` to get information about one of the specific products.

```
POST /ListEntities HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "EntityType": "ContainerProduct"
}
```

For the entity type, you must use the entity type without the version. It returns all entities of that type (and doesn't filter on version).

Here is a sample of the response to the `ListEntities` action.

```
{
    "EntitySummaryList": [
        {
            "Name": "Container Product 1",
            "EntityType": "ContainerProduct",
            "EntityId": "example1-abcd-1234-5ef6-7890abcdef12",
            "EntityArn": "arn:aws:aws-marketplace:[exampleARN]",
            "LastModifiedDate": "2021-03-01T00:00:00Z",
            "Visibility": "Public"
        },
        {
            "Name": "Container Product 2",
            "EntityType": "ContainerProduct",
            "EntityId": "example2-abcd-1234-5ef6-7890abcdef12",
            "EntityArn": "arn:aws:aws-marketplace:[exampleARN]",
            "LastModifiedDate": "2021-03-02T00:00:00Z",
            "Visibility": "Public"
        }
    ],
    "NextToken": "exampleabcdef12345..."
}
```

To get the details of one of these products, use the `DescribeEntity` action. The following example shows how to get details about the first product returned above.

```
GET /DescribeEntity?catalog=AWSMarketplace&entityId={{example1-abcd-1234-5ef6-7890abcdef12}} HTTP/1.1
```

The following shows the response to `DescribeEntity`.

```
{
  "EntityType": "ContainerProduct@1.0",
  "EntityIdentifier": "example1-abcd-1234-5ef6-7890abcdef12@9",
  "EntityArn": "arn:aws:aws-marketplace:[exampleARN]",
  "LastModifiedDate": "2021-03-02T20:19:14Z",
  "Details": "{\"Versions\":[{\"Id\":\"example2-0000-aaaa-5ef6-7890abcdef12\",\"ReleaseNotes\":\"My release notes\",\"UpgradeInstructions\":\"N/A\",\"VersionTitle\":\"1.0\",\"CreationDate\":\"2021-03-02T00:00:00.000Z\",\"Sources\":[{\"Type\":\"DockerImages\",\"Id\":\"example3-1111-bbbb-5ef6-7890abcdef12\",\"Images\":[\"111122223333.dkr.ecr.us-east-1.amazonaws.com/some-seller-prefix/my-repo-1:some-tag\"],\"Compatibility\":{\"Platform\":\"Linux\"}}],\"DeliveryOptions\":[{\"Id\":\"example4-2222-cccc-2222-cccccccccccc\",\"Type\":\"ElasticContainerRegistry\",\"SourceId\":\"example3-1111-bbbb-5ef6-7890abcdef12\",\"Title\":\"New delivery option 1\",\"ShortDescription\":\"Delivery option 1\",\"isRecommended\":false,\"Compatibility\":{\"AWSServices\":[\"ECS\",\"EKS\"]},\"Instructions\":{\"Usage\":\"test\"},\"Recommendations\":{\"AdditionalArtifacts\":[]},\"Visibility\":\"Limited\"}]}],\"Description\":{\"Highlights\":[\"Some highlight\"],\"LongDescription\":\"Description of my product\",\"ProductCode\":\"123456789012abcdef1234567\",\"Manufacturer\":null,\"Visibility\":\"Limited\",\"AssociatedProducts\":null,\"Sku\":null,\"SearchKeywords\":[\"some keyword\"],\"ProductTitle\":\"Container Product 1\",\"ShortDescription\":\"Description of my product\",\"Categories\":[\"Operating Systems\"]},\"PromotionalResources\":{\"LogoUrl\":\"https://awsmp-logos.s3.amazonaws.com/PLACEHOLDER_Logo_for_Containers_products.png\",\"AdditionalResources\":[],\"Videos\":[]},\"SupportInformation\":{\"Description\":\"Description of support information.\",\"Resources\":[]},\"RegionAvailability\":{\"Regions\":[\"ap-south-1\",\"eu-west-3\",\"eu-north-1\",\"eu-west-2\",\"eu-west-1\",\"ap-northeast-2\",\"ap-northeast-1\",\"me-south-1\",\"ca-central-1\",\"sa-east-1\",\"ap-east-1\",\"ap-southeast-1\",\"ap-southeast-2\",\"eu-central-1\",\"us-east-1\",\"us-east-2\",\"us-west-1\",\"us-west-2\"],\"FutureRegionSupport\":null},\"Repositories\":[{\"Url\":\"111122223333.dkr.ecr.us-east-1.amazonaws.com/some-seller-prefix/my-repo-1\",\"Type\":\"ECR\"}]}",
  "DetailsDocument":
  {
    "Versions":
    [
      {
        "Id": "example2-0000-aaaa-5ef6-7890abcdef12",
        "ReleaseNotes": "My release notes",
        "UpgradeInstructions": "N/A",
        "VersionTitle": "1.0",
        "CreationDate": "2021-03-02T00:00:00.000Z",
        "Sources":
        [
          {
            "Type": "DockerImages",
            "Id": "example3-1111-bbbb-5ef6-7890abcdef12",
            "Images":
            [
              "111122223333.dkr.ecr.us-east-1.amazonaws.com/some-seller-prefix/my-repo-1:some-tag"
            ],
            "Compatibility":
            {
              "Platform": "Linux"
            }
          }
        ],
        "DeliveryOptions":
        [
          {
            "Id": "example4-2222-cccc-2222-cccccccccccc",
            "Type": "ElasticContainerRegistry",
            "SourceId": "example3-1111-bbbb-5ef6-7890abcdef12",
            "Title": "New delivery option 1",
            "ShortDescription": "Delivery option 1",
            "isRecommended": false,
            "Compatibility":
            {
              "AWSServices":
              [
                "ECS",
                "EKS"
              ]
            },
            "Instructions":
            {
              "Usage": "test"
            },
            "Recommendations":
            {
              "AdditionalArtifacts":
              []
            },
            "Visibility": "Limited"
          }
        ]
      }
    ],
    "Description":
    {
      "Highlights":
      [
        "Some highlight"
      ],
      "LongDescription": "Description of my product",
      "ProductCode": "123456789012abcdef1234567",
      "Manufacturer": null,
      "Visibility": "Limited",
      "AssociatedProducts": null,
      "Sku": null,
      "SearchKeywords":
      [
        "some keyword"
      ],
      "ProductTitle": "Container Product 1",
      "ShortDescription": "Description of my product",
      "Categories":
      [
        "Operating Systems"
      ]
    },
    "PromotionalResources":
    {
      "LogoUrl": "https://awsmp-logos.s3.amazonaws.com/PLACEHOLDER_Logo_for_Containers_products.png",
      "AdditionalResources":
      [],
      "Videos":
      []
    },
    "SupportInformation":
    {
      "Description": "Description of support information.",
      "Resources":
      []
    },
    "RegionAvailability":
    {
      "Regions":
      [
        "ap-south-1",
        "eu-west-3",
        "eu-north-1",
        "eu-west-2",
        "eu-west-1",
        "ap-northeast-2",
        "ap-northeast-1",
        "me-south-1",
        "ca-central-1",
        "sa-east-1",
        "ap-east-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "eu-central-1",
        "us-east-1",
        "us-east-2",
        "us-west-1",
        "us-west-2"
      ],
      "FutureRegionSupport": null
    },
    "Repositories":
    [
      {
        "Url": "111122223333.dkr.ecr.us-east-1.amazonaws.com/some-seller-prefix/my-repo-1",
        "Type": "ECR"
      }
    ]
  }
}
```

**Note**  
The `DetailsDocument` attribute contains the entity details as a JSON object. The legacy `Details` attribute contains the same JSON object as a string.