The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Work with SaaS products using the AWS Marketplace APIs

You can use the AWS Marketplace Catalog API to automate tasks for working with SaaS-based products.
For information about creating SaaS-based products, see [Create a product](work-with-seller-products.md#create-product "work-with-seller-products.md#create-product"). The following topics describe how to perform
Catalog API actions:

###### Topics

- [Configure Free pricing model for SaaS products](#saas-free-pricing-model "#saas-free-pricing-model")
- [SaaS Quick Launch options](#saas-quick-launch-resources "#saas-quick-launch-resources")
- [Add delivery options](#add-delivery-options "#add-delivery-options")
- [SaaSUrlDeliveryOption](#saas-url-delivery-option "#saas-url-delivery-option")

## Configure Free pricing model for SaaS products

SaaS products can be offered with a Free pricing model, which allows buyers to use your product at no cost. When using the Free pricing model for SaaS products, you must configure pricing dimensions with zero-dollar pricing in either UsageBasedPricingTerm or ConfigurableUpfrontPricingTerm.

###### Note

The Free pricing model requirement for SaaS products is unique. For SaaS products with Free pricing, you must create at least one dimension with either UsageBasedPricingTerm or ConfigurableUpfrontPricingTerm, and all dimensions must be priced at $0.00. This requirement does not apply to AMI, container, or machine learning products.

To configure Free pricing for a SaaS product:

1. Create pricing dimensions for your product using the `AddDimensions` change type. For more information, see [Add pricing dimensions](work-with-seller-products.md#add-dimensions "work-with-seller-products.md#add-dimensions") in the seller products documentation.
2. Create an offer with the `PricingModel` set to `Free` and include either `UsageBasedPricingTerm` or `ConfigurableUpfrontPricingTerm` with all dimension prices set to $0.00. For more information about creating offers, see [Work with offers using the AWS Marketplace APIs](work-with-offers.md "work-with-offers.md").

When configuring the offer, ensure that:

- All rate card prices in `UsageBasedPricingTerm` are set to "0.00" (string format)
- All charge amounts in `ConfigurableUpfrontPricingTerm` are set to "0.00" (string format)
- At least one dimension with $0.00 pricing is included

## SaaS Quick Launch options

For information about Quick Launch options, see the following resources:

- (Buyers) For Quick Launch options for SaaS products, see [Configuring and
  launching Saas products using Quick Launch](../buyerguide/saas-quick-launch.md "../buyerguide/saas-quick-launch.md") in the _AWS Marketplace Buyer Guide_.
- (Sellers) For Quick Launch options for SaaS products, see [Configure Quick Launch](../userguide/saas-product-settings.md#saas-quick-launch "../userguide/saas-product-settings.md#saas-quick-launch") in the _AWS Marketplace Seller
  Guide_.
- For a Quick Launch workshop for SaaS products, see [Lab: Enable SaaS Quick Launch](https://catalog.workshops.aws/mpseller/en-US/saas/quick-launch-integration "https://catalog.workshops.aws/mpseller/en-US/saas/quick-launch-integration") in the _AWS Marketplace
  seller workshop_.

## Add delivery options

You can use the Catalog API to add delivery options for a SaaS product in AWS Marketplace.
API delivery options enable sellers to offer API-based services that integrate with
AWS services such as Amazon Bedrock for AI agent workflows.

To add API delivery options, call the `StartChangeSet` API operation
with the `AddDeliveryOptions` change type to add delivery details, as
shown in the following example.

The following topics explain how to add use the `ApiDeliveryOptionDetails` and `SaaSUrlDeliveryOptionDetails` options.

###### Topics

- [ApiDeliveryOptionDetails](#api-delivery-option-details "#api-delivery-option-details")
- [Update delivery options](#update-delivery-options "#update-delivery-options")
- [Update delivery option visibility](#update-delivery-options-visibility "#update-delivery-options-visibility")

### ApiDeliveryOptionDetails

The example in this section supports the `ApiDeliveryOptionDetails` delivery option type,
which allows you to specify API endpoints, authentication methods, and
integration protocols for your SaaS product.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json
   {
  "ChangeType": "AddDeliveryOptions",
  "Entity": {
    "Identifier": "prod-`1234567890123`",
    "Type": "SaaSProduct@1.0"
  },
  "Details": {
    "DeliveryOptions": [
      {
        "Details": {
          "ApiDeliveryOptionDetails": {
            "ApiType": "AGENT",
            "QuickLaunchEnabled": true,
            "FulfillmentUrl": "`https://example.com/fulfillment`",
            "UsageInstructions": "# `Getting Started`\\n\\n`To use this API:`\\n`1. Register for an API key`\\n`2. Configure your endpoint`\\n`3. Start making requests`",
            "CompatibleServices": ["Bedrock-AgentCore"],
            "Endpoints": [
              {
                "Name": "GenerateContent",
                "EndpointUrl": "`https://api.example.com/v1/{tenantId}/generate`",
                "EndpointType": "DYNAMIC",
                "EndpointUrlParameters": [
                  {
                    "Name": "tenantId",
                    "Description": "`The unique identifier for the buyer's tenant`",
                    "DefaultValue": "`default`"
                  }
                ],
                "Description": "Generate content using AI models",
                "AuthorizationTypes": ["API_KEY"],
                "Schemas": [{
                  "Type": "OPEN_API",
                  "SchemaUrl": "`https://example.com/schemas/example-schema.json`"
                }],
                "IntegrationProtocols": [
                  {
                    "Type": "MCP",
                    "UsageInstructions": "`Connect using Model Context Protocol for seamless integration`"
                  }
                ]
              }
            ]
          }
        }
      }
    ]
  }
}
```

Provide information for the fields to add the `AddDeliveryOptions`
change type:

- `Entity` (object) (required) – Your SaaS-based
  product.

  - `Identifier` (string) (required) – Your product
    ID. For more information, see Identifier.
  - `Type` (string) (required) – The Type is based
    on the delivery method (product type) that your product will be
    using: `SaaSProduct@1.0`.

- `DetailsDocument` (object) (required) – Details of the
  request.

  - `DeliveryOptions` (array) – Details of the API
    delivery options being added.

    - `Details` (object) – Contains the
      `ApiDeliveryOptionDetails` of a delivery
      option to be added.

      - `ApiDeliveryOptionDetails` (object)
        – Contains the API delivery option details
        for a SaaS product.

        - `ApiType` (string) (required)
          – Type of API offering. Valid values:
          `MCP_SERVER`,
          `KNOWLEDGE_BASE`, `AGENT`,
          `GUARDRAIL`, `OTHER`.
        - `QuickLaunchEnabled` (boolean)
          (required) – Determines if buyers can use
          Quick Launch to configure and launch the
          software.
        - `FulfillmentUrl` (string)
          (required) – The URL to the seller's
          software registration landing page.
        - `UsageInstructions` (string)
          (required) – Instructions for using this
          API delivery option. Supports markdown formatting.
          Maximum 30,000 characters.
        - `CompatibleServices` (array)
          (optional) – Supported AWS services for
          this delivery option. Currently supports
          `Bedrock-AgentCore`.
        - `Endpoints` (array) (required)
          – The API endpoints available for this
          offering. Must contain exactly one
          endpoint.

          - `Name` (string) (optional)
            – The name of the API endpoint. Must match
            pattern `^[A-Za-z][a-zA-Z0-9-]+$`.
            Maximum 100 characters.
          - `EndpointUrl` (string) (required)
            – The URL of the API endpoint. Must be a
            valid HTTPS URL. Can contain placeholder
            parameters using `{paramName}` syntax
            when `EndpointType` is
            `DYNAMIC`.
          - `EndpointType` (string)
            (optional) – The endpoint type. Valid
            values: `STATIC`,
            `DYNAMIC`. Use `DYNAMIC`
            for endpoints with placeholder parameters that
            resolve to buyer-specific values. Requires
            `EndpointUrlParameters` and
            `QuickLaunchEnabled` set to
            `true`.
          - `EndpointUrlParameters` (array)
            (optional) – The placeholder parameters
            in a dynamic endpoint URL. Required when
            `EndpointType` is
            `DYNAMIC`. Limited to 1-5
            parameters.

            - `Name` (string) (required)
              – The parameter name. Must match a
              `{paramName}` placeholder in the
              `EndpointUrl`. Must match pattern
              `^[a-zA-Z][a-zA-Z0-9_]*$`. Maximum
              100 characters.
            - `Description` (string)
              (optional) – A description of the
              parameter. Maximum 1,000 characters.
            - `DefaultValue` (string)
              (optional) – The default value for the
              parameter until the seller delivers a value.
              Must match pattern
              `^[a-zA-Z0-9._~-]+$`. Maximum 256
              characters.

          - `Description` (string) (optional)
            – A description of the API endpoint and its
            functionality. Maximum 4,000 characters.
          - `AuthorizationTypes` (array)
            (required) – The types of authorization
            required to access the API endpoint. Valid values:
            `API_KEY`, `OAUTH2`. Must
            contain 1-2 unique values.
          - `Schemas` (array) (optional)
            – The schema specifications for the API
            endpoint. Maximum 1 schema.

            - `Type` (string) (required)
              – Schema type. Valid value:
              `OPEN_API`.
            - `SchemaUrl` (string) (required)
              – The S3 URL of the schema that has been
              ingested into a Marketplace owned S3
              bucket.

          - `IntegrationProtocols` (array)
            (optional) – Protocol types supported by
            the endpoint. Maximum 2 protocols.

            - `Type` (string) (required)
              – Protocol identifier. Valid values:
              `MCP`, `A2A`.
            - `UsageInstructions` (string)
              (required) – Additional instructions for
              utilizing the protocol with the endpoint. Maximum
              30,000 characters.

****Response
Syntax****

A change set is created for your request. The response to this request gives you
the ID for the change set and looks like the following.

```
{
"ChangeSetId": "`example123456789012abcdef`",
"ChangeSetArn": "arn:aws:aws-marketplace:us-east-
1:`123456789012`:AWSMarketplace/ChangeSet/`example123456789012abcdef`"
}

```

**Synchronous Validations**

| Error condition                        | Message                                                                                                                                                                           | HTTP code |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Invalid API Type                       | You provided an invalid API type. Valid values are:<br>MCP\_SERVER, KNOWLEDGE\_BASE, AGENT, GUARDRAIL, OTHER.                                                                     | 422       |
| Invalid Fulfillment Url                | Provide a valid fulfillment URL beginning with<br>"https://".                                                                                                                     | 422       |
| Missing Required Fields                | Required parameter is missing. You must provide ApiType,<br>QuickLaunchEnabled, FulfillmentUrl, UsageInstructions, and<br>Endpoints.                                              | 422       |
| Invalid Endpoint URL                   | Provide a valid endpoint URL beginning with "https://".                                                                                                                           | 422       |
| Missing Authorization Types            | You must provide at least one authorization type. Valid values<br>are: API\_KEY, OAUTH2.                                                                                          | 422       |
| Invalid Authorization Types            | You provided invalid authorization types. Valid values are:<br>API\_KEY, OAUTH2.                                                                                                  | 422       |
| Too Many Endpoints                     | You cannot provide more than 1 endpoint for API delivery<br>options.                                                                                                              | 422       |
| Invalid Endpoint Type                  | EndpointType must be STATIC or DYNAMIC.                                                                                                                                           | 422       |
| Endpoint URL Parameters Required       | EndpointUrlParameters is required when EndpointType is<br>DYNAMIC.                                                                                                                | 422       |
| Endpoint URL Parameters Forbidden      | EndpointUrlParameters is not allowed when EndpointType is<br>STATIC or absent.                                                                                                    | 422       |
| Invalid Endpoint URL Parameters Count  | EndpointUrlParameters must contain between 1 and 5<br>parameters.                                                                                                                 | 422       |
| Invalid Endpoint URL Parameter         | EndpointUrlParameters contains an invalid entry. Check that<br>Name starts with a letter (letters, digits, underscores only)<br>and DefaultValue uses only unreserved characters. | 422       |
| Duplicate Endpoint URL Parameter Names | EndpointUrlParameters must not contain duplicate parameter<br>names.                                                                                                              | 422       |
| Dynamic Endpoint Requires Quick Launch | QuickLaunchEnabled must be true when EndpointType is<br>DYNAMIC.                                                                                                                  | 422       |
| Invalid Compatible Services            | You provided invalid compatible services. Valid values are:<br>Bedrock-AgentCore.                                                                                                 | 422       |
| Invalid Schema Type                    | You provided an invalid schema type. Valid value is:<br>OPEN\_API.                                                                                                                | 422       |
| Invalid Schema URL                     | Provide a valid schema URL that points to a Marketplace owned<br>S3 bucket.                                                                                                       | 422       |
| Invalid Integration Protocol           | You provided an invalid integration protocol type. Valid<br>values are: MCP, A2A.                                                                                                 | 422       |
| Too Many Integration Protocols         | You cannot provide more than 2 integration protocols.                                                                                                                             | 422       |
| Invalid Usage Instructions             | Usage instructions exceed the maximum length of 30,000<br>characters.                                                                                                             | 422       |

**Asynchronous Errors**

| Error code                   | Error message                                                                                                                                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DUPLICATE\_DELIVERY\_OPTIONS | You provided one or more delivery option types that already<br>exist for this product. Provide a unique delivery option type or<br>use `UpdateDeliveryOptions` if you intended to change<br>an existing delivery option. |
| INVALID\_FULFILLMENT\_URL    | The URL you provided returned HTTP status code [x]. Provide a<br>fulfillment URL that renders with a 200.                                                                                                                |
| INVALID\_ENDPOINT\_URL       | The URL you provided returned HTTP status code [x]. Provide an<br>endpoint URL that renders with a 200.                                                                                                                  |
| INVALID\_SCHEMA\_URL         | The schema URL you provided is invalid or inaccessible.<br>Provide a valid schema URL that points to an Amazon S3 bucket owned<br>by AWS Marketplace.                                                                    |

### Update delivery options

You can use the Catalog API to update the delivery options for a SaaS product in
AWS Marketplace.

To update the delivery options, call the `StartChangeSet` API operation
with the `UpdateDeliveryOptions` change type, as shown in the following
example.

###### Note

This supports the `ApiDeliveryOptionDetails` delivery option type.
You must provide the delivery option ID to identify which option to
update.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json
{
    "Catalog": "AWSMarketplace",
    "ChangeSet": [
        {
            "ChangeType": "UpdateDeliveryOptions",
            "Entity": {
                "Identifier": "`example1-abcd-1234-5ef6-7890abcdef12@1`",
                "Type": "SaaSProduct@1.0"
            },
            "DetailsDocument": {
                "DeliveryOptions": [
                    {
                        "Id": "`do-1234567891234567891234`",
                        "Details": {
                            "ApiDeliveryOptionDetails": {
                                "ApiType": "AGENT",
                                "QuickLaunchEnabled": true,
                                "FulfillmentUrl": "`https://example.com/fulfillment-updated`",
                                "UsageInstructions": "# `Updated Getting Started`\\n\\n`To use this updated API:`\\n`1. Register for an API key`\\n`2. Configure your endpoint`\\n`3. Start making requests`",
                                "CompatibleServices": ["Bedrock-AgentCore"],
                                "Endpoints": [
                                    {
                                        "Name": "GenerateContent",
                                        "EndpointUrl": "`https://api.example.com/v2/{tenantId}/generate`",
                                        "EndpointType": "DYNAMIC",
                                        "EndpointUrlParameters": [
                                            {
                                                "Name": "tenantId",
                                                "Description": "`The unique identifier for the buyer's tenant`",
                                                "DefaultValue": "`default`"
                                            }
                                        ],
                                        "Description": "`Generate content using updated AI models`",
                                        "AuthorizationTypes": ["API_KEY", "OAUTH2"],
                                        "Schemas": [{
                                            "Type": "OPEN_API",
                                            "SchemaUrl": "`https://example.com/schemas/updated-schema.json`"
                                        }],
                                        "IntegrationProtocols": [
                                            {
                                                "Type": "MCP",
                                                "UsageInstructions": "`Connect using Model Context Protocol for seamless integration`"
                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    }
                ]
            }
        }
    ]
}
```

Provide information for the fields to update the
`UpdateDeliveryOptions` change type with API delivery options:

- `Entity` (object) (required) – Your SaaS-based
  product.

  - `Identifier` (string) (required) – Your product
    ID. For more information, see Identifier.
  - `Type` (string) (required) – The Type is based
    on the delivery method (product type) that your product will be
    using: `SaaSProduct@1.0`.

- `DetailsDocument` (object) (required) – Details of the
  request.

  - `DeliveryOptions` (array) – Contains the details
    of the API delivery options being updated.

    - `Id` (string) (required) – Unique
      identifier for the DeliveryOption. (Get the unique
      identifier for the DeliveryOption by calling the
      `DescribeEntity` action on the product you
      are updating.)
    - `Details` (object) – Contains the
      `ApiDeliveryOptionDetails` of the delivery
      option to be updated.

      - `ApiDeliveryOptionDetails` (object)
        – Contains the API delivery option details
        for SaaS product.

        - `ApiType` (string) (required)
          – Type of API offering. Valid values:
          `MCP_SERVER`,
          `KNOWLEDGE_BASE`, `AGENT`,
          `GUARDRAIL`, `OTHER`.
        - `QuickLaunchEnabled` (boolean)
          (required) – Determines if buyers can use
          Quick Launch to configure and launch the
          software.
        - `FulfillmentUrl` (string)
          (required) – The URL to be updated for the
          SaaS product.
        - `UsageInstructions` (string)
          (required) – Instructions for using this
          API delivery option. Supports markdown formatting.
          Maximum 30,000 characters.
        - `CompatibleServices` (array)
          (optional) – Supported AWS services for
          this delivery option. Currently supports
          `Bedrock-AgentCore`.
        - `Endpoints` (array) (required)
          – The API endpoints available for this
          offering. Must contain exactly one
          endpoint.

          - `Name` (string) (optional)
            – The name of the API endpoint.
          - `EndpointUrl` (string) (required)
            – The URL of the API endpoint to be
            updated. Can contain placeholder parameters
            using `{paramName}` syntax when
            `EndpointType` is
            `DYNAMIC`.
          - `EndpointType` (string)
            (optional) – The endpoint type. Valid
            values: `STATIC`,
            `DYNAMIC`. Use `DYNAMIC`
            for endpoints with placeholder parameters that
            resolve to buyer-specific values. Requires
            `EndpointUrlParameters`.
          - `EndpointUrlParameters` (array)
            (optional) – The placeholder parameters
            in a dynamic endpoint URL. Required when
            `EndpointType` is
            `DYNAMIC`. Limited to 1-5
            parameters.

            - `Name` (string) (required)
              – The parameter name. Must match a
              `{paramName}` placeholder in the
              `EndpointUrl`. Must match pattern
              `^[a-zA-Z][a-zA-Z0-9_]*$`. Maximum
              100 characters.
            - `Description` (string)
              (optional) – A description of the
              parameter. Maximum 1,000 characters.
            - `DefaultValue` (string)
              (optional) – The default value for the
              parameter until the seller delivers a value.
              Must match pattern
              `^[a-zA-Z0-9._~-]+$`. Maximum 256
              characters.

          - `Description` (string) (optional)
            – A description of the API endpoint and its
            functionality.
          - `AuthorizationTypes` (array)
            (required) – The types of authorization
            required to access the API endpoint. Valid values:
            `API_KEY`, `OAUTH2`.
          - `Schemas` (array) (optional)
            – The schema specifications for the API
            endpoint.

            - `Type` (string) (required)
              – Schema type. Valid value:
              `OPEN_API`.
            - `SchemaUrl` (string) (required)
              – The S3 URL of the updated schema.

          - `IntegrationProtocols` (array)
            (optional) – Protocol types supported by
            the endpoint.

            - `Type` (string) (required)
              – Protocol identifier. Valid values:
              `MCP`, `A2A`.
            - `UsageInstructions` (string)
              (required) – Additional instructions for
              utilizing the protocol with the endpoint.

**Response Syntax**

```
{
"ChangeSetId": "`example123456789012abcdef`",
"ChangeSetArn": "arn:aws:aws-marketplace:us-east-
1:`123456789012`:AWSMarketplace/ChangeSet/`example123456789012abcdef`"
}

```

The change request is added to a queue and processed. This includes validating
information to ensure it meets the AWS Marketplace guidelines. The validation process can take
anywhere from a few minutes to a few hours. You can check the status of the request
through the AWS Marketplace Management Portal, or in the Catalog API with the `DescribeChangeSet`
action.

**Synchronous Validations**

| Error condition                        | Message                                                                                                                                                                                                                                                                                                                               | HTTP code |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Empty Delivery Option Ids              | Provided Details is not valid. String '' at /DeliveryOptions/0/Id<br>does not match required schema regex, '^do-[a-zA-Z0-9]+$'                                                                                                                                                                                                        | 422       |
| Missing Delivery Option Ids            | Provided Details is not valid. JSON at /DeliveryOptions/0 is<br>missing required properties: ['Id'].                                                                                                                                                                                                                                  | 422       |
| Duplicate Delivery Option Ids          | Provide unique delivery option IDs.                                                                                                                                                                                                                                                                                                   | 422       |
| Invalid Fulfillment Url                | Provide a valid fulfillment URL beginning with<br>"https://".                                                                                                                                                                                                                                                                         | 422       |
| Invalid Delivery Option IDs            | Provide delivery option IDs that can be found in the product. IDs<br>not found: [x]                                                                                                                                                                                                                                                   | 422       |
| Multiple URL Delivery Options          | You provided more than one URL delivery option. Provide one URL<br>delivery option.                                                                                                                                                                                                                                                   | 422       |
| Missing delivery option ids            | The delivery option ID is missing. Provide one or more valid<br>delivery option IDs that you wish to update, or use<br>`AddDeliveryOptions` if you intended to add a new<br>delivery option.                                                                                                                                          | 422       |
| Invalid Launch URL                     | Provide a valid launch URL beginning with "https://".                                                                                                                                                                                                                                                                                 | 422       |
| Missing Launch Url                     | Required parameter `LaunchUrl` is missing. You must<br>provide a `LaunchUrl`.                                                                                                                                                                                                                                                         | 422       |
| Missing deployment templates           | The deployment template is missing. Provide at least one<br>deployment template.                                                                                                                                                                                                                                                      | 422       |
| Too many deployment templates          | You cannot provide more than 20 deployment templates.                                                                                                                                                                                                                                                                                 | 422       |
| Invalid template URL                   | Quick Start URL is invalid. Provide deployment template URL that<br>is published through AWS QuickStarts to Amazon S3. Invalid<br>deployment templates URL: [x]                                                                                                                                                                       | 422       |
| Invalid deployment template stack name | The deployment template stack name is invalid. Provide a valid<br>stack name using only alphanumeric characters and hyphens. It must<br>start with an alphabetical character and can't be longer than 128<br>characters.                                                                                                              | 422       |
| Duplicate deployment template title    | You provided duplicate deployment template titles. Provide unique<br>deployment template titles.                                                                                                                                                                                                                                      | 422       |
| Duplicate deployment template URL      | You provided duplicate deployment template urls. Provide unique<br>deployment template urls.                                                                                                                                                                                                                                          | 422       |
| Invalid deployment template type       | The deployment template type is invalid. Provide a valid<br>deployment template type. Supported values are<br>["CloudFormation@1.0"].                                                                                                                                                                                                 | 422       |
| Invalid deployment template IAM policy | The deployment template IAM policy is invalid. Provide a valid<br>IAM policy.                                                                                                                                                                                                                                                         | 422       |
| Invalid usage instructions             | • Images aren't supported by the usage instructions.<br>Remove the image [x].<br>• You provided a link to an invalid URL in the usage<br>instructions: [x]. Provide a valid URL.<br>• You provided a link with an unsupported URI scheme in<br>the usage instructions. Use a supported scheme: ["http",<br>"https", "tel", "mailto"]. | 422       |

**Asynchronous Errors**

| Error code                     | Error message                                                                                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INVALID\_DELIVERY\_OPTION\_IDS | **`Provide delivery option IDs that can be found in the<br>product. IDs not found: [x]`**                                                                             |
| AUDIT\_ERROR                   | **`AWS MP Catalog Audits List<br>• CQ<br>team`**                                                                                                                      |
| INVALID\_FULFILLMENT\_URL      | **`The URL you provided returned HTTP status code [x].<br>Provide a fulfillment URL that renders with a<br>200.`**                                                    |
| INVALID\_LAUNCH\_URL           | **`The URL you provided returned HTTP status code [x].<br>Provide a launch URL that renders with a<br>200.`**                                                         |
| INVALID\_TEMPLATE\_URL         | **`Quick Start URL is invalid. Provide deployment<br>template URL that is published through AWS QuickStarts to<br>Amazon S3. Invalid deployment templates URL: [x]`** |

### Update delivery option visibility

You can use the Catalog API to configure permissions so that only some users can
change the visibility for a SaaS product in AWS Marketplace.

To configure permissions so that only some users can change the visibility for a
SaaS product, call the `StartChangeSet` API operation with the
`UpdateDeliveryOptionsVisibility` change type, as shown in the
following example.

###### Note

This is only supported for one delivery option:
`SaaSUrlDeliveryOptionDetails`.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateDeliveryOptionsVisibility",
      "Entity":
      {
        "Identifier": "`prod-example12345`",
        "Type": "SaaSProduct@1.0"
      },
      "DetailsDocument":
      {
        "DeliveryOptions":
        [
          {
            "Id": "do-`1234567891234567891234`",
            "TargetVisibility": "Public"
          },
          {
            "Id": "do-`43210987654321`",
            "TargetVisibility": "Limited",
            "Targeting":
            {
              "PositiveTargeting":
              {
                "BuyerAccounts":
                [
                  "`123456789012`"
                ]
              }
            }
          }
        ]
      }
    }
  ]
}

```

Provide information for the fields to add the
`UpdateDeliveryOptionsVisibility` change type:

- `Entity` (object) (required) – Your SaaS-based product.

  - `Identifier` (string) (required) – Your product
    ID. For more information, see [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").
  - `Type` (string) (required) – The
    `Type` is based on the delivery method (product type)
    that your product will be using: `SaaSProduct@1.0`.

- `DetailsDocument` (object) (required) – Details of the
  request.

  - `DeliveryOptions` (array) – List of
    `DeliveryOptions` to be updated.

    - `TargetVisibility` (string) – The
      delivery option id to be updated.
    - `TargetVisibility` (string) – The
      intended new visibility of the delivery option.

    Possible values: `Limited`,
    `Public`, and `Unavailable`.

    ###### Note

    There is always exactly one `Public`
    delivery option, and a maximum of one
    `Limited` delivery option.
    - `Targeting` (object) _optional_ – Targeting of the delivery
      option, used in conjunction with the `Limited`
      visibility status to be able to test the new delivery option
      before changing the visibility to
      `Public`.

      - `PositiveTargeting` (object) –
        Specifying inclusive targeting.

        - `BuyerAccounts` (array of
          strings) – The list of buyer AWS account
          ids who will be able to use the new delivery
          option.

        Min size: 0. Max size: 100.

**Response Syntax**

```
{
"ChangeSetId": "`example123456789012abcdef`",
"ChangeSetArn": "arn:aws:aws-marketplace:`us-east-1`:`123456789012`:AWSMarketplace/ChangeSet/`example123456789012abcdef`"
}

```

The change request is added to a queue and processed. This includes validating
information to ensure that it meets the AWS Marketplace guidelines. The validation process can
take anywhere from a few minutes to a few hours. You can check the status of the
request through the AWS Marketplace Management Portal, or in the Catalog API with the
`DescribeChangeSet` action.

**Synchronous Validations**

| Error condition                  | Message                                                                                                                                                                                      | HTTP code |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Missing delivery option ids      | The delivery option ID is missing. Provide one or more valid<br>delivery option IDs that you wish to update, or use<br>`AddDeliveryOptions` if you intended to add a new<br>delivery option. | 422       |
| Invalid visibility               | You provided invalid option for `TargetVisibility`.<br>Allowed options are: `Limited`, `Public`,<br>`Unavailable`.                                                                           | 422       |
| Invalid targeting                | You provided invalid option for `PositiveTargeting`.<br>You must provide a valid parameter for<br>`BuyerAccounts`.                                                                           | 422       |
| Missing Visibility and Targeting | You provided invalid delivery option visibility details. You must<br>provide a valid parameter for at least one of<br>`TargetVisibility` or `Targeting`.                                     | 422       |
| Too many AWS account ids         | You cannot provide more than 100 targeted buyer accounts.                                                                                                                                    | 422       |

**Asynchronous Errors**

| Error code                     | Error message                                                                                                                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| INVALID\_DELIVERY\_OPTION\_IDS | **`You provided invalid delivery option details. Provide<br>delivery option IDs that can be found in the product. IDs not<br>found: [x]`** |
| INVALID\_VISIBILITY            | **`You provided more than one delivery option for the<br>public state. Provide only one public delivery<br>option.`**                      |
| INVALID\_VISIBILITY            | **`You didn't provide a public delivery option. Provide<br>one public delivery option.`**                                                  |
| AUDIT\_ERROR                   | **`Varies based on MCO manual review.`**                                                                                                   |

## SaaSUrlDeliveryOption

The following example shows how to use the `SaaSUrlDeliveryOptionDetails` to update the
`FulfillmentUrl`.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
    "Catalog": "AWSMarketplace",
    "ChangeSet": [
        {
            "ChangeType": "UpdateDeliveryOptions",
            "Entity": {
                "Identifier": "`example1-abcd-1234-5ef6-7890abcdef12@1`",
                "Type": "SaaSProduct@1.0"
            },
            "DetailsDocument": {
                "DeliveryOptions": [
                    {
                        "Id": "do-`1234567891234567891234`",
                        "Details": {
                            "SaaSUrlDeliveryOptionDetails": {
                                "FulfillmentUrl": "https://www.aws.amazon.com/marketplace/management",
                                "LaunchUrl": "`URL`",
                                "UsageInstructions": "`Instructions`",
                                "DeploymentTemplates": [
                                    {
                                        "Title": "`CloudFormation Template 123`",
                                        "Description": "`CloudFormation description`",
                                        "IamPolicy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"s3:Get*\",\"s3:List*\"],\"Resource\":\n[\"arn:aws:s3:::amzn-s3-demo-bucket\",\"arn:aws:s3:::amzn-s3-demo-bucket/*\"]}]}"
                                    }
                                ]
                            }
                        }
                    }
                ]
            }
        }
    ]
}
```

Provide information for the fields to add the `AddDeliveryOptions`
change type:

- `Entity` (object) (required) – Your
  SaaS-based product.

  - `Identifier` (string) (required) – Your product
    ID. For more information, see [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").
  - `Type` (string) (required) –
    The `Type` is based on the delivery method (product type)
    that your product will be using: `SaaSProduct@1.0`.

- **DetailsDocument** (object) (required)
  – Details of the request.

  - `DeliveryOptions` (array) – Contains the details
    of the delivery options being updated.

    - `TargetVisibility` (string) –
      Unique identifier for the `DeliveryOption`. (Get
      the unique identifier for the `DeliveryOption` by
      calling the `DescribeEntity` action on the
      product you are updating.)
    - `Details` (object) –
      Contains the `SaaSUrlDeliveryOptionDetails` of
      the delivery option to be updated.

      - `SaaSUrlDeliveryOptionDetails` (object)
        – Contains the `FulfillmentUrl` of
        a delivery option for SaaS product.

        - `FulfillmentUrl` (string)
          – The URL to be updated for the SaaS
          product.
        - `LaunchUrl` (string) – The URL to
          your SaaS product's landing page. This is required
          if `QuickLaunchEnabled` is set to
          `True`.
        - `UsageInstructions` (string) –
          Instructions for using this delivery option.
          Include documentation for manual steps for
          customers who won't use
          `DeploymentTemplates`.
        - `DeploymentTemplates` (array) –
          Deployment templates that customers can use to set
          up and conﬁgure the SaaS product and any related
          AWS resources.

          - `Title` (string) – The display
            name of the deployment template.
          - `Description` (string) – A
            description for what the deployment template
            contains.
          - `IamPolicy` (string) – An IAM
            policy describing the permissions needed to deploy
            the template. Buyers can use this IAM policy to
            quickly deploy the template.
          - `CloudFormationDetails` (object)
            – The details of a CloudFormation template.

            - `TemplateUrl` (string) – The URL
              for the deployment template.
            - `DefaultStackName` (string) – The
              default name used in CloudFormation when the customer
              creates the template.

**Response Syntax**

```
{
"ChangeSetId": "`example123456789012abcdef`",
"ChangeSetArn": "arn:aws:aws-marketplace:us-east-
1:`123456789012`:AWSMarketplace/ChangeSet/`example123456789012abcdef`"
}

```

The change request is added to a queue and processed. This includes validating
information to ensure it meets the AWS Marketplace guidelines. The validation process can take
anywhere from a few minutes to a few hours. You can check the status of the request
through the AWS Marketplace Management Portal, or in the Catalog API with the `DescribeChangeSet`
action.

**Synchronous Validations**

| Error condition                        | Message                                                                                                                                                                                                                                                                                                                               | HTTP code |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Empty Delivery Option Ids              | Provided Details is not valid. String '' at /DeliveryOptions/0/Id<br>does not match required schema regex, '^do-[a-zA-Z0-9]+$'                                                                                                                                                                                                        | 422       |
| Missing Delivery Option Ids            | Provided Details is not valid. JSON at /DeliveryOptions/0 is<br>missing required properties: ['Id'].                                                                                                                                                                                                                                  | 422       |
| Duplicate Delivery Option Ids          | Provide unique delivery option IDs.                                                                                                                                                                                                                                                                                                   | 422       |
| Invalid Fulfillment Url                | Provide a valid fulfillment URL beginning with<br>"https://".                                                                                                                                                                                                                                                                         | 422       |
| Invalid Delivery Option IDs            | Provide delivery option IDs that can be found in the product. IDs<br>not found: [x]                                                                                                                                                                                                                                                   | 422       |
| Multiple URL Delivery Options          | You provided more than one URL delivery option. Provide one URL<br>delivery option.                                                                                                                                                                                                                                                   | 422       |
| Missing delivery option ids            | The delivery option ID is missing. Provide one or more valid<br>delivery option IDs that you wish to update, or use<br>`AddDeliveryOptions` if you intended to add a new<br>delivery option.                                                                                                                                          | 422       |
| Invalid Launch URL                     | Provide a valid launch URL beginning with "https://".                                                                                                                                                                                                                                                                                 | 422       |
| Missing Launch Url                     | Required parameter `LaunchUrl` is missing. You must<br>provide a `LaunchUrl`.                                                                                                                                                                                                                                                         | 422       |
| Missing deployment templates           | The deployment template is missing. Provide at least one<br>deployment template.                                                                                                                                                                                                                                                      | 422       |
| Too many deployment templates          | You cannot provide more than 20 deployment templates.                                                                                                                                                                                                                                                                                 | 422       |
| Invalid template URL                   | Quick Start URL is invalid. Provide deployment template URL that<br>is published through AWS QuickStarts to Amazon S3. Invalid<br>deployment templates URL: [x]                                                                                                                                                                       | 422       |
| Invalid deployment template stack name | The deployment template stack name is invalid. Provide a valid<br>stack name using only alphanumeric characters and hyphens. It must<br>start with an alphabetical character and can't be longer than 128<br>characters.                                                                                                              | 422       |
| Duplicate deployment template title    | You provided duplicate deployment template titles. Provide unique<br>deployment template titles.                                                                                                                                                                                                                                      | 422       |
| Duplicate deployment template URL      | You provided duplicate deployment template urls. Provide unique<br>deployment template urls.                                                                                                                                                                                                                                          | 422       |
| Invalid deployment template type       | The deployment template type is invalid. Provide a valid<br>deployment template type. Supported values are<br>["CloudFormation@1.0"].                                                                                                                                                                                                 | 422       |
| Invalid deployment template IAM policy | The deployment template IAM policy is invalid. Provide a valid<br>IAM policy.                                                                                                                                                                                                                                                         | 422       |
| Invalid usage instructions             | • Images aren't supported by the usage instructions.<br>Remove the image [x].<br>• You provided a link to an invalid URL in the usage<br>instructions: [x]. Provide a valid URL.<br>• You provided a link with an unsupported URI scheme in<br>the usage instructions. Use a supported scheme: ["http",<br>"https", "tel", "mailto"]. | 422       |

**Asynchronous Errors**

| Error code                     | Error message                                                                                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INVALID\_DELIVERY\_OPTION\_IDS | **`Provide delivery option IDs that can be found in the<br>product. IDs not found: [x]`**                                                                             |
| AUDIT\_ERROR                   | **`AWS MP Catalog Audits List<br>• CQ<br>team`**                                                                                                                      |
| INVALID\_FULFILLMENT\_URL      | **`The URL you provided returned HTTP status code [x].<br>Provide a fulfillment URL that renders with a<br>200.`**                                                    |
| INVALID\_LAUNCH\_URL           | **`The URL you provided returned HTTP status code [x].<br>Provide a launch URL that renders with a<br>200.`**                                                         |
| INVALID\_TEMPLATE\_URL         | **`Quick Start URL is invalid. Provide deployment<br>template URL that is published through AWS QuickStarts to<br>Amazon S3. Invalid deployment templates URL: [x]`** |

### Update delivery option visibility

You can use the Catalog API to configure permissions so that only some users can
change the visibility for a SaaS product in AWS Marketplace.

To do so, call the `StartChangeSet` API operation with the
`UpdateDeliveryOptionsVisibility` change type, as shown in the
following example.

###### Note

This is only supported for one delivery option:
`SaaSUrlDeliveryOptionDetails`.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateDeliveryOptionsVisibility",
      "Entity":
      {
        "Identifier": "`prod-example12345`",
        "Type": "SaaSProduct@1.0"
      },
      "DetailsDocument":
      {
        "DeliveryOptions":
        [
          {
            "Id": "do-`1234567891234567891234`",
            "TargetVisibility": "Public"
          },
          {
            "Id": "do-`43210987654321`",
            "TargetVisibility": "Limited",
            "Targeting":
            {
              "PositiveTargeting":
              {
                "BuyerAccounts":
                [
                  "`123456789012`"
                ]
              }
            }
          }
        ]
      }
    }
  ]
}

```

Provide information for the fields to add the
`UpdateDeliveryOptionsVisibility` change type:

- `Entity` (object) (required) – Your
  SaaS-based product.

  - `Identifier` (string) (required) – Your product
    ID. For more information, see [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").
  - `Type` (string) (required) –
    The `Type` is based on the delivery method (product type)
    that your product will be using: `SaaSProduct@1.0`.

- `DetailsDocument` (object) (required) – Details of the
  request.

  - `DeliveryOptions` (array) – List of
    `DeliveryOptions` to be updated.

    - `TargetVisibility` (string) – The
      delivery option id to be updated.
    - `TargetVisibility`
      (string) – The intended new visibility of the
      delivery option.

    Possible values: `Limited`,
    `Public`, and `Unavailable`.

    ###### Note

    There is always exactly one `Public`
    delivery option, and a maximum of one
    `Limited` delivery option.
    - `Targeting` (object) _optional_ – Targeting of the delivery
      option, used in conjunction with the `Limited`
      visibility status to be able to test the new delivery option
      before changing the visibility to
      `Public`.

      - `PositiveTargeting` (object) –
        Specifying inclusive targeting.

        - `BuyerAccounts` (array of
          strings) – The list of buyer AWS account
          ids who will be able to use the new delivery
          option.

        Min size: 0. Max size: 100.

**Response Syntax**

```
{
"ChangeSetId": "`example123456789012abcdef`",
"ChangeSetArn": "arn:aws:aws-marketplace:`us-east-1`:`123456789012`:AWSMarketplace/ChangeSet/`example123456789012abcdef`"
}

```

The change request is added to a queue and processed. This includes validating
information to ensure that it meets the AWS Marketplace guidelines. The validation process can
take anywhere from a few minutes to a few hours. You can check the status of the
request through the AWS Marketplace Management Portal, or in the Catalog API with the
`DescribeChangeSet` action.

**Synchronous Validations**

| Error condition                  | Message                                                                                                                                                                                      | HTTP code |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Missing delivery option ids      | The delivery option ID is missing. Provide one or more valid<br>delivery option IDs that you wish to update, or use<br>`AddDeliveryOptions` if you intended to add a new<br>delivery option. | 422       |
| Invalid visibility               | You provided invalid option for `TargetVisibility`.<br>Allowed options are: `Limited`, `Public`,<br>`Unavailable`.                                                                           | 422       |
| Invalid targeting                | You provided invalid option for `PositiveTargeting`.<br>You must provide a valid parameter for<br>`BuyerAccounts`.                                                                           | 422       |
| Missing Visibility and Targeting | You provided invalid delivery option visibility details. You must<br>provide a valid parameter for at least one of<br>`TargetVisibility` or `Targeting`.                                     | 422       |
| Too many AWS account ids         | You cannot provide more than 100 targeted buyer accounts.                                                                                                                                    | 422       |

**Asynchronous Errors**

| Error code                     | Error message                                                                                                                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| INVALID\_DELIVERY\_OPTION\_IDS | **`You provided invalid delivery option details. Provide<br>delivery option IDs that can be found in the product. IDs not<br>found: [x]`** |
| INVALID\_VISIBILITY            | **`You provided more than one delivery option for the<br>public state. Provide only one public delivery<br>option.`**                      |
| INVALID\_VISIBILITY            | **`You didn't provide a public delivery option. Provide<br>one public delivery option.`**                                                  |
| AUDIT\_ERROR                   | **`Varies based on MCO manual review.`**                                                                                                   |
