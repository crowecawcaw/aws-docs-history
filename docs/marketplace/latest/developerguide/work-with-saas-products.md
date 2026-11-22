

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with SaaS products using the AWS Marketplace APIs

You can use the AWS Marketplace Catalog API to automate tasks for working with SaaS-based products. For information about creating SaaS-based products, see [Create a product](work-with-seller-products.md#create-product). The following topics describe how to perform Catalog API actions:

**Topics**
+ [Configure Free pricing model for SaaS products](#saas-free-pricing-model)
+ [Configure pricing for Agentic Commerce products](#saas-agentic-commerce-pricing)
+ [SaaS Quick Launch options](#saas-quick-launch-resources)
+ [Add delivery options](#add-delivery-options)
+ [SaaSUrlDeliveryOption](#saas-url-delivery-option)

## Configure Free pricing model for SaaS products
<a name="saas-free-pricing-model"></a>

SaaS products can be offered with a Free pricing model, which allows buyers to use your product at no cost. When using the Free pricing model for SaaS products, you must configure pricing dimensions with zero-dollar pricing in either UsageBasedPricingTerm or ConfigurableUpfrontPricingTerm.

**Note**  
The Free pricing model requirement for SaaS products is unique. For SaaS products with Free pricing, you must create at least one dimension with either UsageBasedPricingTerm or ConfigurableUpfrontPricingTerm, and all dimensions must be priced at $0.00. This requirement does not apply to AMI, container, or machine learning products.

**Note**  
Agentic Commerce products can't use the Free pricing model. For more information, see [Agentic Commerce API delivery options](#agentic-commerce-delivery-option).

To configure Free pricing for a SaaS product:

1. Create pricing dimensions for your product using the `AddDimensions` change type. For more information, see [Add pricing dimensions](work-with-seller-products.md#add-dimensions) in the seller products documentation.

1. Create an offer with the `PricingModel` set to `Free` and include either `UsageBasedPricingTerm` or `ConfigurableUpfrontPricingTerm` with all dimension prices set to $0.00. For more information about creating offers, see [Work with offers using the AWS Marketplace APIs](work-with-offers.md).

When configuring the offer, ensure that:
+ All rate card prices in `UsageBasedPricingTerm` are set to "0.00" (string format)
+ All charge amounts in `ConfigurableUpfrontPricingTerm` are set to "0.00" (string format)
+ At least one dimension with $0.00 pricing is included

## Configure pricing for Agentic Commerce products
<a name="saas-agentic-commerce-pricing"></a>

Agentic Commerce products use one reserved usage pricing dimension, `agentic_commerce_default`, that AWS Marketplace meters for each verified payment. When you list the product in the AWS Marketplace console, AWS Marketplace adds this dimension and its rate for you. When you use the AWS Marketplace Catalog API, you add the dimension and set its rate yourself.

**Note**  
The `agentic_commerce_default` requirement is unique to Agentic Commerce products. Don't send metering records for this dimension. Buyers pay the amount in your signed quote. For more information, see [Agentic Commerce API delivery options](#agentic-commerce-delivery-option).

To configure pricing for an Agentic Commerce product with the AWS Marketplace Catalog API:

1. Add the Agentic Commerce API delivery option with the `AddDeliveryOptions` change type.

1. Add the `agentic_commerce_default` dimension with the `AddDimensions` change type, later in the same change set or in a later change set. For more information, see [Add pricing dimensions](work-with-seller-products.md#add-dimensions) in the seller products documentation.

1. Create a public offer with the `PricingModel` set to `Usage`, and include one `UsageBasedPricingTerm` in USD with one rate card item for `agentic_commerce_default`. For more information about creating offers, see [Work with offers using the AWS Marketplace APIs](work-with-offers.md).

When you configure the dimension and the offer, make sure that:
+ The dimension `Key` is `agentic_commerce_default`.
+ The dimension `Name` is `Agentic Commerce x402`.
+ The dimension `Description` is `Agentic Commerce meters this unit to bill buyers the seller's x402 quote price.`
+ The dimension `Types` are `["Metered", "ExternallyMetered"]`.
+ The dimension `Unit` is `Units`.
+ The rate card `Price` for `agentic_commerce_default` is "1.00" (string format, USD). This price is a metering unit, not the price of a request, so don't change it.

## SaaS Quick Launch options
<a name="saas-quick-launch-resources"></a>

**Note**  
Agentic Commerce products can't use Quick Launch. For more information, see [Agentic Commerce API delivery options](#agentic-commerce-delivery-option).

For information about Quick Launch options, see the following resources:
+ (Buyers) For Quick Launch options for SaaS products, see [Configuring and launching Saas products using Quick Launch](https://docs.aws.amazon.com/marketplace/latest/buyerguide/saas-quick-launch.html) in the *AWS Marketplace Buyer Guide*.
+ (Sellers) For Quick Launch options for SaaS products, see [Configure Quick Launch](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-product-settings.html#saas-quick-launch) in the *AWS Marketplace Seller Guide*.
+ For a Quick Launch workshop for SaaS products, see [Lab: Enable SaaS Quick Launch](https://catalog.workshops.aws/mpseller/en-US/saas/quick-launch-integration) in the *AWS Marketplace seller workshop*.

## Add delivery options
<a name="add-delivery-options"></a>

You can use the Catalog API to add delivery options for a SaaS product in AWS Marketplace. API delivery options enable sellers to offer API-based services that integrate with AWS services such as Amazon Bedrock for AI agent workflows. An API delivery option can also use the Agentic Commerce access model (`AGENTIC_COMMERCE`), where buyers pay for each request through the x402 payment protocol. For more information, see [Agentic Commerce API delivery options](#agentic-commerce-delivery-option).

To add API delivery options, call the `StartChangeSet` API operation with the `AddDeliveryOptions` change type to add delivery details, as shown in the following example. 

The following topics explain how to add use the `ApiDeliveryOptionDetails` and `SaaSUrlDeliveryOptionDetails` options.

**Topics**
+ [ApiDeliveryOptionDetails](#api-delivery-option-details)
+ [Agentic Commerce API delivery options](#agentic-commerce-delivery-option)
+ [Update delivery options](#update-delivery-options)
+ [Update delivery option visibility](#update-delivery-options-visibility)

### ApiDeliveryOptionDetails
<a name="api-delivery-option-details"></a>

The example in this section supports the `ApiDeliveryOptionDetails` delivery option type, which allows you to specify API endpoints, authentication methods, and integration protocols for your SaaS product.

**Request Syntax**

```json
POST /StartChangeSet HTTP/1.1 
Content-type: application/json
   {
  "ChangeType": "AddDeliveryOptions",
  "Entity": {
    "Identifier": "prod-{{1234567890123}}",
    "Type": "SaaSProduct@1.0"
  },
  "Details": {
    "DeliveryOptions": [
      {
        "Details": {
          "ApiDeliveryOptionDetails": {
            "ApiType": "AGENT",
            "QuickLaunchEnabled": true,
            "FulfillmentUrl": "{{https://example.com/fulfillment}}",
            "UsageInstructions": "# {{Getting Started}}\\n\\n{{To use this API:}}\\n{{1. Register for an API key}}\\n{{2. Configure your endpoint}}\\n{{3. Start making requests}}",
            "CompatibleServices": ["Bedrock-AgentCore"],
            "Endpoints": [
              {
                "Name": "GenerateContent",
                "EndpointUrl": "{{https://api.example.com/v1/{tenantId}/generate}}",
                "EndpointType": "DYNAMIC",
                "EndpointUrlParameters": [
                  {
                    "Name": "tenantId",
                    "Description": "{{The unique identifier for the buyer's tenant}}",
                    "DefaultValue": "{{default}}"
                  }
                ],
                "Description": "Generate content using AI models",
                "AuthorizationTypes": ["API_KEY"],
                "Schemas": [{
                  "Type": "OPEN_API",
                  "SchemaUrl": "{{https://example.com/schemas/example-schema.json}}"
                }],
                "IntegrationProtocols": [
                  {
                    "Type": "MCP",
                    "UsageInstructions": "{{Connect using Model Context Protocol for seamless integration}}"
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

Provide information for the fields to add the `AddDeliveryOptions` change type:
+ `Entity` (object) (required) – Your SaaS-based product.
  + `Identifier` (string) (required) – Your product ID. For more information, see Identifier.
  + `Type` (string) (required) – The Type is based on the delivery method (product type) that your product will be using: `SaaSProduct@1.0`.
+ `DetailsDocument` (object) (required) – Details of the request.
  + `DeliveryOptions` (array) – Details of the API delivery options being added.
    + `Details` (object) – Contains the `ApiDeliveryOptionDetails` of a delivery option to be added.
      + `ApiDeliveryOptionDetails` (object) – Contains the API delivery option details for a SaaS product.
        + `AccessModels` (array) (optional) – How buyers get access to the API. Must contain exactly 1 value. Valid values: `REGISTRATION_WITH_SELLER` (buyers register with you to get credentials) and `AGENTIC_COMMERCE` (buyers pay for each request through the x402 payment protocol). If you omit it, the delivery option uses `REGISTRATION_WITH_SELLER`. You can't change it after you add the delivery option. For more information, see [Agentic Commerce API delivery options](#agentic-commerce-delivery-option).
        + `AgenticCommerceConfiguration` (object) (conditional) – The payment protocol and quote-verification public key for an Agentic Commerce delivery option. Required when `AccessModels` contains `AGENTIC_COMMERCE`, and not allowed otherwise.
          + `PaymentProtocols` (array) (required) – Must contain exactly 1 value: `X402`.
          + `PublicKeySource` (object) (required) – Contains `Type` (`JWKS` or `KMS`), plus `JwksUri` for `JWKS`, or `AliasArn` and `RoleArn` for `KMS`.
        + `ApiType` (string) (required) – Type of API offering. Valid values: `MCP_SERVER`, `KNOWLEDGE_BASE`, `AGENT`, `GUARDRAIL`, `OTHER`.
        + `QuickLaunchEnabled` (boolean) (required) – Determines if buyers can use Quick Launch to configure and launch the software. Must be `false` when `AccessModels` contains `AGENTIC_COMMERCE`.
        + `FulfillmentUrl` (string) (required) – The URL to the seller's software registration landing page.
        + `UsageInstructions` (string) (required) – Instructions for using this API delivery option. Supports markdown formatting. Maximum 30,000 characters.
        + `CompatibleServices` (array) (optional) – Supported AWS services for this delivery option. Currently supports `Bedrock-AgentCore`. Not allowed when `AccessModels` contains `AGENTIC_COMMERCE`.
        + `Endpoints` (array) (required) – The API endpoints available for this offering. Must contain exactly one endpoint.
          + `Name` (string) (optional) – The name of the API endpoint. Must match pattern `^[A-Za-z][a-zA-Z0-9-]+$`. Maximum 100 characters.
          + `EndpointUrl` (string) (required) – The URL of the API endpoint. Must be a valid HTTPS URL. Can contain placeholder parameters using `{paramName}` syntax when `EndpointType` is `DYNAMIC`.
          + `EndpointType` (string) (optional) – The endpoint type. Valid values: `STATIC`, `DYNAMIC`. Use `DYNAMIC` for endpoints with placeholder parameters that resolve to buyer-specific values. Requires `EndpointUrlParameters` and `QuickLaunchEnabled` set to `true`. Not allowed when `AccessModels` contains `AGENTIC_COMMERCE`.
          + `EndpointUrlParameters` (array) (optional) – The placeholder parameters in a dynamic endpoint URL. Required when `EndpointType` is `DYNAMIC`. Limited to 1-5 parameters. Not allowed when `AccessModels` contains `AGENTIC_COMMERCE`.
            + `Name` (string) (required) – The parameter name. Must match a `{paramName}` placeholder in the `EndpointUrl`. Must match pattern `^[a-zA-Z][a-zA-Z0-9_]*$`. Maximum 100 characters.
            + `Description` (string) (optional) – A description of the parameter. Maximum 1,000 characters.
            + `DefaultValue` (string) (optional) – The default value for the parameter until the seller delivers a value. Must match pattern `^[a-zA-Z0-9._~-]+$`. Maximum 256 characters.
          + `Description` (string) (optional) – A description of the API endpoint and its functionality. Maximum 4,000 characters.
          + `AuthorizationTypes` (array) (required) – The types of authorization required to access the API endpoint. Valid values: `API_KEY`, `OAUTH2`. Must contain 1-2 unique values. When `AccessModels` contains `AGENTIC_COMMERCE`, must be exactly `["PAYMENT_TOKEN"]`. `PAYMENT_TOKEN` isn't allowed with any other access model.
          + `EstimatedUsageCost` (string) (conditional) – A plain-text estimate of what a request to the endpoint costs. AWS Marketplace shows this estimate to buyers. Required when `AccessModels` contains `AGENTIC_COMMERCE`, and not allowed otherwise. 1–200 characters.
          + `Schemas` (array) (optional) – The schema specifications for the API endpoint. Maximum 1 schema.
            + `Type` (string) (required) – Schema type. Valid value: `OPEN_API`.
            + `SchemaUrl` (string) (required) – The S3 URL of the schema that has been ingested into a Marketplace owned S3 bucket.
          + `IntegrationProtocols` (array) (optional) – Protocol types supported by the endpoint. Maximum 2 protocols.
            + `Type` (string) (required) – Protocol identifier. Valid values: `MCP`, `A2A`.
            + `UsageInstructions` (string) (required) – Additional instructions for utilizing the protocol with the endpoint. Maximum 30,000 characters.

****Response Syntax****

A change set is created for your request. The response to this request gives you the ID for the change set and looks like the following.

```json
{
"ChangeSetId": "{{example123456789012abcdef}}", 
"ChangeSetArn": "arn:aws:aws-marketplace:us-east-
1:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

**Synchronous Validations**


| Error condition | Message | HTTP code | 
| --- | --- | --- | 
| Invalid API Type | You provided an invalid API type. Valid values are: MCP\_SERVER, KNOWLEDGE\_BASE, AGENT, GUARDRAIL, OTHER. | 422 | 
| Invalid Fulfillment Url | Provide a valid fulfillment URL beginning with "https://". | 422 | 
| Missing Required Fields | Required parameter is missing. You must provide ApiType, QuickLaunchEnabled, FulfillmentUrl, UsageInstructions, and Endpoints. | 422 | 
| Invalid Endpoint URL | Provide a valid endpoint URL beginning with "https://". | 422 | 
| Missing Authorization Types | You must provide at least one authorization type. Valid values are: API\_KEY, OAUTH2. | 422 | 
| Invalid Authorization Types | You provided invalid authorization types. Valid values are: API\_KEY, OAUTH2. | 422 | 
| Too Many Endpoints | You cannot provide more than 1 endpoint for API delivery options. | 422 | 
| Invalid Endpoint Type | EndpointType must be STATIC or DYNAMIC. | 422 | 
| Endpoint URL Parameters Required | EndpointUrlParameters is required when EndpointType is DYNAMIC. | 422 | 
| Endpoint URL Parameters Forbidden | EndpointUrlParameters is not allowed when EndpointType is STATIC or absent. | 422 | 
| Invalid Endpoint URL Parameters Count | EndpointUrlParameters must contain between 1 and 5 parameters. | 422 | 
| Invalid Endpoint URL Parameter | EndpointUrlParameters contains an invalid entry. Check that Name starts with a letter (letters, digits, underscores only) and DefaultValue uses only unreserved characters. | 422 | 
| Duplicate Endpoint URL Parameter Names | EndpointUrlParameters must not contain duplicate parameter names. | 422 | 
| Dynamic Endpoint Requires Quick Launch | QuickLaunchEnabled must be true when EndpointType is DYNAMIC. | 422 | 
| Invalid Compatible Services | You provided invalid compatible services. Valid values are: Bedrock-AgentCore. | 422 | 
| Invalid Schema Type | You provided an invalid schema type. Valid value is: OPEN\_API. | 422 | 
| Invalid Schema URL | Provide a valid schema URL that points to a Marketplace owned S3 bucket. | 422 | 
| Invalid Integration Protocol | You provided an invalid integration protocol type. Valid values are: MCP, A2A. | 422 | 
| Too Many Integration Protocols | You cannot provide more than 2 integration protocols. | 422 | 
| Invalid Usage Instructions | Usage instructions exceed the maximum length of 30,000 characters. | 422 | 
| Invalid Access Models | AccessModels must be REGISTRATION\_WITH\_SELLER or AGENTIC\_COMMERCE. | 422 | 
| Invalid Access Models Count | AccessModels must contain exactly 1 value. | 422 | 
| Quick Launch Not Allowed for Agentic Commerce | QuickLaunchEnabled must be false when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Invalid Agentic Commerce Authorization Types | AuthorizationTypes must be exactly PAYMENT\_TOKEN on every endpoint when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Payment Token Authorization Type Not Allowed | AuthorizationTypes may contain PAYMENT\_TOKEN only when AccessModels contains AGENTIC\_COMMERCE. To use Agentic Commerce, set AccessModels to ["AGENTIC\_COMMERCE"]; on UpdateDeliveryOptions, send AccessModels whenever the request includes Agentic Commerce fields. | 422 | 
| Endpoint Type Not Allowed for Agentic Commerce | EndpointType is not allowed when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Endpoint URL Parameters Not Allowed for Agentic Commerce | EndpointUrlParameters is not allowed when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Endpoint URL Placeholders Not Allowed for Agentic Commerce | EndpointUrl must not contain placeholders when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Missing Agentic Commerce Configuration | AgenticCommerceConfiguration is required when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Agentic Commerce Configuration Not Allowed | AgenticCommerceConfiguration is only valid when AccessModels contains AGENTIC\_COMMERCE. To use Agentic Commerce, set AccessModels to ["AGENTIC\_COMMERCE"]; on UpdateDeliveryOptions, send AccessModels whenever the request includes Agentic Commerce fields. | 422 | 
| Compatible Services Not Allowed for Agentic Commerce | CompatibleServices is not allowed when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Invalid Payment Protocols Count | PaymentProtocols must contain exactly 1 value. | 422 | 
| Invalid Payment Protocol | PaymentProtocols values must be X402. | 422 | 
| Missing Public Key Source | PublicKeySource is required in AgenticCommerceConfiguration. | 422 | 
| Invalid Public Key Source Type | Type must be JWKS or KMS. | 422 | 
| Missing JWKS URI | JwksUri is required when Type is JWKS. | 422 | 
| Missing KMS ARNs | AliasArn and RoleArn are required when Type is KMS. | 422 | 
| JWKS URI Not Allowed | JwksUri is not allowed when Type is KMS. | 422 | 
| KMS ARNs Not Allowed | AliasArn and RoleArn are not allowed when Type is JWKS. | 422 | 
| Invalid JWKS URI | JwksUri must begin with "https://" and point to a JSON file under a /.well-known/ path. | 422 | 
| Invalid KMS Alias ARN | AliasArn must be a valid KMS alias ARN. | 422 | 
| Invalid KMS Role ARN | RoleArn must be a valid IAM role ARN. | 422 | 
| Missing Estimated Usage Cost | EstimatedUsageCost is required on every endpoint when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Invalid Estimated Usage Cost | EstimatedUsageCost must be between 1 and 200 characters. | 422 | 
| Estimated Usage Cost Not Allowed | EstimatedUsageCost is only valid when AccessModels contains AGENTIC\_COMMERCE. To use Agentic Commerce, set AccessModels to ["AGENTIC\_COMMERCE"]; on UpdateDeliveryOptions, send AccessModels whenever the request includes Agentic Commerce fields. | 422 | 

**Asynchronous Errors**


| Error code | Error message | 
| --- | --- | 
| DUPLICATE\_DELIVERY\_OPTIONS | You provided one or more delivery option types that already exist for this product. Provide a unique delivery option type or use `UpdateDeliveryOptions` if you intended to change an existing delivery option. | 
| INVALID\_FULFILLMENT\_URL | The URL you provided returned HTTP status code [x]. Provide a fulfillment URL that renders with a 200. | 
| INVALID\_ENDPOINT\_URL | The URL you provided returned HTTP status code [x]. Provide an endpoint URL that renders with a 200. | 
| INVALID\_SCHEMA\_URL | The schema URL you provided is invalid or inaccessible. Provide a valid schema URL that points to an Amazon S3 bucket owned by AWS Marketplace. | 
| INVALID\_ENDPOINT\_SCHEMA\_URL | The schema file is larger than 1 MB: `There was an issue copying the schema from S3. Schema size exceeds 1 MB. Provide a schema that is under 1 MB.` | 
| INVALID\_ENDPOINT\_SCHEMA | For an Agentic Commerce delivery option, the message describes what's wrong with the OpenAPI specification file. It is one of the following:+ `The OpenAPI specification file isn't valid JSON or YAML. Fix the file syntax and upload it again.`<br />+ `The OpenAPI specification file has no openapi or swagger version field. Upload an OpenAPI 3.x or Swagger 2.0 file.`<br />+ `OpenAPI version [x] isn't supported. Upload an OpenAPI 3.x or Swagger 2.0 file.`<br />+ `Swagger version [x] isn't supported. Upload an OpenAPI 3.x or Swagger 2.0 file.`<br />+ `The OpenAPI specification file is missing required top-level fields: [x]. Add them and upload the file again.`<br />+ `The OpenAPI specification file has top-level errors: [x] Fix them and upload the file again.`<br />+ `The OpenAPI specification file has no paths object. Add the API paths and upload the file again.` | 
| INVALID\_ACCESS\_MODELS | AccessModels must contain exactly 1 value: REGISTRATION\_WITH\_SELLER or AGENTIC\_COMMERCE. | 
| UNSUPPORTED\_QUICK\_LAUNCH\_ENABLED | QuickLaunchEnabled must be false when AccessModels contains AGENTIC\_COMMERCE. | 
| MISSING\_AGENTIC\_COMMERCE\_CONFIGURATION | A public key is required when AccessModels contains AGENTIC\_COMMERCE. Provide AgenticCommerceConfiguration with a PublicKeySource. | 
| INVALID\_AGENTIC\_COMMERCE\_CONFIGURATION | AgenticCommerceConfiguration is only valid when AccessModels contains AGENTIC\_COMMERCE. Remove AgenticCommerceConfiguration or set AccessModels to AGENTIC\_COMMERCE. | 
| INCOMPATIBLE\_AGENTIC\_COMMERCE\_AND\_AGENTCORE | AGENTIC\_COMMERCE and Bedrock-AgentCore cannot be used together on the same delivery option. Remove either AGENTIC\_COMMERCE from AccessModels or Bedrock-AgentCore from CompatibleServices. | 
| INVALID\_AGENTIC\_COMMERCE\_AUTHORIZATION\_TYPES | Endpoint AuthorizationTypes must be exactly PAYMENT\_TOKEN when AccessModels contains AGENTIC\_COMMERCE, and may not contain PAYMENT\_TOKEN otherwise. | 
| INVALID\_PAYMENT\_PROTOCOLS | PaymentProtocols must contain exactly 1 value: X402. | 
| INVALID\_PUBLIC\_KEY\_SOURCE | PublicKeySource requires either JwksUri, or AliasArn and RoleArn. | 
| INVALID\_JWKS\_URI | JwksUri must begin with "https://" and be between 8 and 2048 characters. | 
| INVALID\_KMS\_ALIAS\_ARN | AliasArn must be a valid KMS alias ARN. | 
| INVALID\_KMS\_ROLE\_ARN | RoleArn must be a valid IAM role ARN. | 
| MISSING\_ESTIMATED\_USAGE\_COST | EstimatedUsageCost is required on the endpoint when AccessModels contains AGENTIC\_COMMERCE. | 
| INVALID\_ESTIMATED\_USAGE\_COST | EstimatedUsageCost must be between 1 and 200 characters. | 
| UNSUPPORTED\_ESTIMATED\_USAGE\_COST | EstimatedUsageCost is only valid when AccessModels contains AGENTIC\_COMMERCE. Remove EstimatedUsageCost from the endpoint. | 

### Agentic Commerce API delivery options
<a name="agentic-commerce-delivery-option"></a>

An API delivery option can use the Agentic Commerce access model. With Agentic Commerce, buyers and their AI agents don't register with you or get an API key. Instead, the buyer pays for each request through the x402 payment protocol. Your endpoint returns HTTP 402 with a quote that you sign. The buyer pays the quote, and the agent retries the request with a payment token that your endpoint verifies. AWS Marketplace meters each verified payment and bills the buyer.

Every quote that your Agentic Commerce endpoint signs must carry the product's ID in its `settlement.product_id` claim: the `Identifier` of the SaaS product entity in the `AddDeliveryOptions` request below. AWS Marketplace uses it to resolve the public key that you registered and rejects a quote without it. Registration delivery options have no quotes, so this doesn't apply to them. To look up the ID, see [Find your product ID](work-with-seller-products.md#seller-product-id). For the other quote requirements, see [Quote guidelines](https://docs.aws.amazon.com/marketplace/latest/userguide/agentic-commerce-products.html#agentic-commerce-quotes) in the *AWS Marketplace Seller Guide*.

You choose the access model with the `AccessModels` field when you call `AddDeliveryOptions`. Delivery options without `AccessModels` use the registration access model (`REGISTRATION_WITH_SELLER`), where buyers register with you to get credentials.

#### Requirements and limitations
<a name="agentic-commerce-delivery-option-requirements"></a>
+ You set the access model when you add the delivery option, and you can't change it later. You can't add Agentic Commerce to an existing delivery option or remove it from one. To sell with Agentic Commerce, create a new SaaS product.
+ Agentic Commerce products are priced with usage pricing in a public offer, using the reserved `agentic_commerce_default` dimension. For more information, see [Configure pricing for Agentic Commerce products](#saas-agentic-commerce-pricing).
+ Agentic Commerce products don't support the Free pricing model, private offers, Quick Launch, Concurrent Agreements, or Amazon Bedrock AgentCore as a compatible service.
+ When you use the AWS Marketplace Catalog API, add the reserved `agentic_commerce_default` dimension yourself with `AddDimensions`, after you add the Agentic Commerce delivery option. In the AWS Marketplace console, AWS Marketplace adds it for you. For more information, see [Configure pricing for Agentic Commerce products](#saas-agentic-commerce-pricing).
+ You don't meter usage for Agentic Commerce requests. Don't call `BatchMeterUsage` or `ResolveCustomer` for this traffic.

#### Field rules
<a name="agentic-commerce-delivery-option-field-rules"></a>

When `AccessModels` contains `AGENTIC_COMMERCE`, the `ApiDeliveryOptionDetails` object follows these rules in addition to the rules for all API delivery options:
+ `AccessModels` (array) – Must contain exactly 1 value: `AGENTIC_COMMERCE`.
+ `AgenticCommerceConfiguration` (object) (required on `AddDeliveryOptions`) – The payment protocol that your endpoint accepts and the public key that AWS Marketplace uses to verify your signed quotes. Valid only when `AccessModels` contains `AGENTIC_COMMERCE`.
  + `PaymentProtocols` (array) (required) – Must contain exactly 1 value: `X402`.
  + `PublicKeySource` (object) (required) – Where AWS Marketplace gets the public key for your quote signatures.
    + `Type` (string) (required) – Valid values: `JWKS` for a JSON Web Key Set that you host, or `KMS` for an asymmetric AWS Key Management Service (AWS KMS) key in your account.
    + `JwksUri` (string) – Required when `Type` is `JWKS`, and not allowed when `Type` is `KMS`. The HTTPS URL of your JSON Web Key Set. It must begin with `https://`, and its path must contain `/.well-known/` and end in `.json`, for example `https://example.com/.well-known/jwks.json`. 8–2,048 characters.
    + `AliasArn` (string) – Required when `Type` is `KMS`, and not allowed when `Type` is `JWKS`. The ARN of the AWS KMS alias for your signing key. Use an alias ARN, not a key ARN.
    + `RoleArn` (string) – Required when `Type` is `KMS`, and not allowed when `Type` is `JWKS`. The ARN of an IAM role in your account that grants `kms:GetPublicKey` on the signing key. The key must be an asymmetric AWS KMS key with the key usage `SIGN_VERIFY`. The role's trust policy must allow the AWS Marketplace Agentic Commerce service principal to assume the role, with an `sts:ExternalId` condition whose value is the service principal name. If the trust policy doesn't allow AWS Marketplace to assume the role, AWS Marketplace can't read your public key. For the exact trust policy, see [Use an AWS KMS key](https://docs.aws.amazon.com/marketplace/latest/userguide/agentic-commerce-signing-key.html#agentic-commerce-kms) in the *AWS Marketplace Seller Guide*.
+ `QuickLaunchEnabled` (boolean) – Required on `AddDeliveryOptions`, and must be `false`.
+ `FulfillmentUrl` (string) (required on `AddDeliveryOptions`) – A valid HTTPS URL.
+ `CompatibleServices` (array) – Not allowed. Omit it.
+ `Endpoints` (array) – Every endpoint follows these rules:
  + `EndpointUrl` (string) (required) – A static HTTPS URL. It must not contain `{paramName}` placeholders.
  + `AuthorizationTypes` (array) (required) – Must be exactly `["PAYMENT_TOKEN"]`.
  + `EstimatedUsageCost` (string) (required) – A plain-text estimate of what a request costs, for example `About USD $0.01 per request`. AWS Marketplace shows this estimate to buyers. The amount that a buyer pays is the amount in your signed quote. 1–200 characters.
  + `EndpointType` and `EndpointUrlParameters` – Not allowed.

#### Examples
<a name="agentic-commerce-delivery-option-examples"></a>

**Example: Add an Agentic Commerce delivery option with a JWKS public key**

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "AddDeliveryOptions",
      "Entity": {
        "Identifier": "{{prod-1234567890123}}",
        "Type": "SaaSProduct@1.0"
      },
      "DetailsDocument": {
        "DeliveryOptions": [
          {
            "Details": {
              "ApiDeliveryOptionDetails": {
                "AccessModels": ["AGENTIC_COMMERCE"],
                "AgenticCommerceConfiguration": {
                  "PaymentProtocols": ["X402"],
                  "PublicKeySource": {
                    "Type": "JWKS",
                    "JwksUri": "{{https://example.com/.well-known/jwks.json}}"
                  }
                },
                "ApiType": "AGENT",
                "QuickLaunchEnabled": false,
                "FulfillmentUrl": "{{https://example.com/start}}",
                "UsageInstructions": "{{Call the endpoint. If it returns HTTP 402, pay the quote and retry the request with the payment token.}}",
                "Endpoints": [
                  {
                    "Name": "{{SearchApi}}",
                    "EndpointUrl": "{{https://api.example.com/v1/search}}",
                    "Description": "{{Semantic web search}}",
                    "AuthorizationTypes": ["PAYMENT_TOKEN"],
                    "EstimatedUsageCost": "{{About USD $0.01 per search request}}",
                    "IntegrationProtocols": [
                      {
                        "Type": "MCP",
                        "UsageInstructions": "{{Add the endpoint URL to your MCP client configuration.}}"
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

**Example: Add an Agentic Commerce delivery option with an AWS KMS public key**

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "AddDeliveryOptions",
      "Entity": {
        "Identifier": "{{prod-1234567890123}}",
        "Type": "SaaSProduct@1.0"
      },
      "DetailsDocument": {
        "DeliveryOptions": [
          {
            "Details": {
              "ApiDeliveryOptionDetails": {
                "AccessModels": ["AGENTIC_COMMERCE"],
                "AgenticCommerceConfiguration": {
                  "PaymentProtocols": ["X402"],
                  "PublicKeySource": {
                    "Type": "KMS",
                    "AliasArn": "arn:aws:kms:us-east-1:{{123456789012}}:alias/{{quote-signing-key}}",
                    "RoleArn": "arn:aws:iam::{{123456789012}}:role/{{MarketplaceQuoteKeyAccess}}"
                  }
                },
                "ApiType": "MCP_SERVER",
                "QuickLaunchEnabled": false,
                "FulfillmentUrl": "{{https://example.com/start}}",
                "UsageInstructions": "{{Connect your MCP client to the endpoint. Each tool call is paid for through x402.}}",
                "Endpoints": [
                  {
                    "Name": "{{WeatherMcp}}",
                    "EndpointUrl": "{{https://mcp.example.com/mcp}}",
                    "Description": "{{Weather data MCP server}}",
                    "AuthorizationTypes": ["PAYMENT_TOKEN"],
                    "EstimatedUsageCost": "{{USD $0.002 per tool call}}",
                    "IntegrationProtocols": [
                      {
                        "Type": "MCP",
                        "UsageInstructions": "{{Add the endpoint URL to your MCP client configuration.}}"
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

For the response syntax and the validation errors, see [ApiDeliveryOptionDetails](#api-delivery-option-details).

**Example: Update an Agentic Commerce delivery option**

When you call `UpdateDeliveryOptions` on an Agentic Commerce delivery option, follow these rules:
+ Send `AccessModels` with the stored value, `["AGENTIC_COMMERCE"]`, whenever the request includes `Endpoints` or `AgenticCommerceConfiguration`. If you omit `AccessModels`, AWS Marketplace validates the request against the registration access model rules and rejects it.
+ `Endpoints` replaces the whole list. Resend every endpoint field that you want to keep, including `EstimatedUsageCost`. To keep the API specification, send `Schemas` with the stored `SchemaUrl`.
+ `AgenticCommerceConfiguration` is optional. If you omit it, AWS Marketplace keeps the stored configuration. If you send it, it replaces the stored configuration and must include `PaymentProtocols` and `PublicKeySource`.
+ If you send `QuickLaunchEnabled`, AWS Marketplace rejects the request.

The following example changes the endpoint's estimated usage cost and points to a new JSON Web Key Set.

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateDeliveryOptions",
      "Entity": {
        "Identifier": "{{prod-1234567890123}}",
        "Type": "SaaSProduct@1.0"
      },
      "DetailsDocument": {
        "DeliveryOptions": [
          {
            "Id": "{{do-1234567891234567891234}}",
            "Details": {
              "ApiDeliveryOptionDetails": {
                "AccessModels": ["AGENTIC_COMMERCE"],
                "AgenticCommerceConfiguration": {
                  "PaymentProtocols": ["X402"],
                  "PublicKeySource": {
                    "Type": "JWKS",
                    "JwksUri": "{{https://example.com/.well-known/jwks-2027.json}}"
                  }
                },
                "Endpoints": [
                  {
                    "Name": "{{SearchApi}}",
                    "EndpointUrl": "{{https://api.example.com/v1/search}}",
                    "Description": "{{Semantic web search}}",
                    "AuthorizationTypes": ["PAYMENT_TOKEN"],
                    "EstimatedUsageCost": "{{About USD $0.02 per search request}}",
                    "Schemas": [
                      {
                        "Type": "OPEN_API",
                        "SchemaUrl": "{{https://marketplace-hosted-bucket.s3.amazonaws.com/prod-1234567890123/openapi.json}}"
                      }
                    ],
                    "IntegrationProtocols": [
                      {
                        "Type": "MCP",
                        "UsageInstructions": "{{Add the endpoint URL to your MCP client configuration.}}"
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

For the response syntax and the validation errors, see [Update delivery options](#update-delivery-options).

**Example: DescribeEntity output**

`DescribeEntity` returns an Agentic Commerce delivery option in `DetailsDocument.Versions[].DeliveryOptions`, as in the following example. Note the following:
+ `Type` is `ApiRegistration` for every API delivery option. Use `AccessModels` to identify an Agentic Commerce delivery option.
+ `PublicKeySource` includes `Type` (`JWKS` or `KMS`).
+ The output isn't an `UpdateDeliveryOptions` payload. To build one from it:
  + Send `Id` as the delivery option's `Id`.
  + Put the fields that you change under `Details.ApiDeliveryOptionDetails`.
  + Send `AccessModels` with the stored value, `["AGENTIC_COMMERCE"]`, whenever the request includes `Endpoints` or `AgenticCommerceConfiguration`.
  + Leave out `Type`, `Visibility`, `Targeting`, `QuickLaunchEnabled`, and `CompatibleServices`.
  + Keep `Schemas` on each endpoint, with the stored `SchemaUrl`, to keep the API specification.

  `CompatibleServices` isn't allowed on an Agentic Commerce delivery option.

```json
{
  "Id": "{{do-1234567891234567891234}}",
  "Type": "ApiRegistration",
  "FulfillmentUrl": "{{https://example.com/start}}",
  "Visibility": "Public",
  "QuickLaunchEnabled": false,
  "UsageInstructions": "{{Call the endpoint. If it returns HTTP 402, pay the quote and retry the request with the payment token.}}",
  "CompatibleServices": [],
  "ApiType": "AGENT",
  "AccessModels": ["AGENTIC_COMMERCE"],
  "AgenticCommerceConfiguration": {
    "PaymentProtocols": ["X402"],
    "PublicKeySource": {
      "Type": "JWKS",
      "JwksUri": "{{https://example.com/.well-known/jwks.json}}"
    }
  },
  "Endpoints": [
    {
      "Name": "{{SearchApi}}",
      "EndpointUrl": "{{https://api.example.com/v1/search}}",
      "Description": "{{Semantic web search}}",
      "AuthorizationTypes": ["PAYMENT_TOKEN"],
      "Schemas": [
        {
          "Type": "OPEN_API",
          "SchemaUrl": "{{https://marketplace-hosted-bucket.s3.amazonaws.com/prod-1234567890123/openapi.json}}"
        }
      ],
      "IntegrationProtocols": [
        {
          "Type": "MCP",
          "UsageInstructions": "{{Add the endpoint URL to your MCP client configuration.}}"
        }
      ],
      "EstimatedUsageCost": "{{About USD $0.01 per search request}}"
    }
  ]
}
```

### Update delivery options
<a name="update-delivery-options"></a>

You can use the Catalog API to update the delivery options for a SaaS product in AWS Marketplace. 

To update the delivery options, call the `StartChangeSet` API operation with the `UpdateDeliveryOptions` change type, as shown in the following example.

**Note**  
This supports the `ApiDeliveryOptionDetails` delivery option type. You must provide the delivery option ID to identify which option to update.  
Each request updates one delivery option. `Endpoints` replaces the whole list of endpoints, so resend every endpoint field that you want to keep. To update an Agentic Commerce delivery option, send `AccessModels` with the stored value. For the rules and an example, see [Agentic Commerce API delivery options](#agentic-commerce-delivery-option).

**Request Syntax**

```json
POST /StartChangeSet HTTP/1.1 
Content-type: application/json
{
    "Catalog": "AWSMarketplace",
    "ChangeSet": [
        {
            "ChangeType": "UpdateDeliveryOptions",
            "Entity": {
                "Identifier": "{{example1-abcd-1234-5ef6-7890abcdef12@1}}",
                "Type": "SaaSProduct@1.0"
            },
            "DetailsDocument": {
                "DeliveryOptions": [
                    {
                        "Id": "{{do-1234567891234567891234}}",
                        "Details": {
                            "ApiDeliveryOptionDetails": {
                                "ApiType": "AGENT",
                                "FulfillmentUrl": "{{https://example.com/fulfillment-updated}}",
                                "UsageInstructions": "# {{Updated Getting Started}}\\n\\n{{To use this updated API:}}\\n{{1. Register for an API key}}\\n{{2. Configure your endpoint}}\\n{{3. Start making requests}}",
                                "CompatibleServices": ["Bedrock-AgentCore"],
                                "Endpoints": [
                                    {
                                        "Name": "GenerateContent",
                                        "EndpointUrl": "{{https://api.example.com/v2/{tenantId}/generate}}",
                                        "EndpointType": "DYNAMIC",
                                        "EndpointUrlParameters": [
                                            {
                                                "Name": "tenantId",
                                                "Description": "{{The unique identifier for the buyer's tenant}}",
                                                "DefaultValue": "{{default}}"
                                            }
                                        ],
                                        "Description": "{{Generate content using updated AI models}}",
                                        "AuthorizationTypes": ["API_KEY", "OAUTH2"],
                                        "Schemas": [{
                                            "Type": "OPEN_API",
                                            "SchemaUrl": "{{https://example.com/schemas/updated-schema.json}}"
                                        }],
                                        "IntegrationProtocols": [
                                            {
                                                "Type": "MCP",
                                                "UsageInstructions": "{{Connect using Model Context Protocol for seamless integration}}"
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

Provide information for the fields to update the `UpdateDeliveryOptions` change type with API delivery options:
+ `Entity` (object) (required) – Your SaaS-based product.
  + `Identifier` (string) (required) – Your product ID. For more information, see Identifier.
  + `Type` (string) (required) – The Type is based on the delivery method (product type) that your product will be using: `SaaSProduct@1.0`.
+ `DetailsDocument` (object) (required) – Details of the request.
  + `DeliveryOptions` (array) – Contains the details of the API delivery options being updated.
    + `Id` (string) (required) – Unique identifier for the DeliveryOption. (Get the unique identifier for the DeliveryOption by calling the `DescribeEntity` action on the product you are updating.)
    + `Details` (object) – Contains the `ApiDeliveryOptionDetails` of the delivery option to be updated.
      + `ApiDeliveryOptionDetails` (object) – Contains the API delivery option details for SaaS product. Include at least one field. Top-level fields that you omit keep their stored values. `Endpoints` and `AgenticCommerceConfiguration` replace the stored value when you send them.
        + `AccessModels` (array) (conditional) – The access model of the delivery option. If you send it, it must equal the stored value; the access model can't be changed. Required for an Agentic Commerce delivery option whenever the request includes `Endpoints` or `AgenticCommerceConfiguration`.
        + `AgenticCommerceConfiguration` (object) (optional) – Replaces the stored configuration of an Agentic Commerce delivery option. If you omit it, AWS Marketplace keeps the stored configuration. If you send it, include `PaymentProtocols` and `PublicKeySource`. Valid only when `AccessModels` contains `AGENTIC_COMMERCE`.
        + `ApiType` (string) (optional) – Type of API offering. Valid values: `MCP_SERVER`, `KNOWLEDGE_BASE`, `AGENT`, `GUARDRAIL`, `OTHER`.
        + `QuickLaunchEnabled` (boolean) – Not accepted by `UpdateDeliveryOptions`. If you send it, AWS Marketplace rejects the request. You set Quick Launch when you add the delivery option. An endpoint with `EndpointUrlParameters` requires that the delivery option was added with `QuickLaunchEnabled` set to true.
        + `FulfillmentUrl` (string) (optional) – The URL to be updated for the SaaS product.
        + `UsageInstructions` (string) (optional) – Instructions for using this API delivery option. Supports markdown formatting. Maximum 30,000 characters.
        + `CompatibleServices` (array) (optional) – Supported AWS services for this delivery option. Currently supports `Bedrock-AgentCore`. Not allowed when `AccessModels` contains `AGENTIC_COMMERCE`.
        + `Endpoints` (array) (optional) – The API endpoints available for this offering. If you send it, it must contain exactly one endpoint.
          + `Name` (string) (optional) – The name of the API endpoint.
          + `EndpointUrl` (string) (required) – The URL of the API endpoint to be updated. Can contain placeholder parameters using `{paramName}` syntax when `EndpointType` is `DYNAMIC`.
          + `EndpointType` (string) (optional) – The endpoint type. Valid values: `STATIC`, `DYNAMIC`. Use `DYNAMIC` for endpoints with placeholder parameters that resolve to buyer-specific values. Requires `EndpointUrlParameters`. Not allowed for an Agentic Commerce delivery option.
          + `EndpointUrlParameters` (array) (optional) – The placeholder parameters in a dynamic endpoint URL. Required when `EndpointType` is `DYNAMIC`. Limited to 1-5 parameters. Not allowed when `AccessModels` contains `AGENTIC_COMMERCE`.
            + `Name` (string) (required) – The parameter name. Must match a `{paramName}` placeholder in the `EndpointUrl`. Must match pattern `^[a-zA-Z][a-zA-Z0-9_]*$`. Maximum 100 characters.
            + `Description` (string) (optional) – A description of the parameter. Maximum 1,000 characters.
            + `DefaultValue` (string) (optional) – The default value for the parameter until the seller delivers a value. Must match pattern `^[a-zA-Z0-9._~-]+$`. Maximum 256 characters. Required for any parameter that is new or that previously had a `DefaultValue` and no longer does, if the product is already public. This protects existing buyers from a required parameter with no default value.
          + `Description` (string) (optional) – A description of the API endpoint and its functionality.
          + `AuthorizationTypes` (array) (required) – The types of authorization required to access the API endpoint. Valid values: `API_KEY`, `OAUTH2`. For an Agentic Commerce delivery option, must be exactly `["PAYMENT_TOKEN"]`.
          + `EstimatedUsageCost` (string) (conditional) – A plain-text estimate of what a request to the endpoint costs. AWS Marketplace shows this estimate to buyers. Required on every endpoint of an Agentic Commerce delivery option, and not allowed otherwise. 1–200 characters.
          + `Schemas` (array) (optional) – The schema specifications for the API endpoint.
            + `Type` (string) (required) – Schema type. Valid value: `OPEN_API`.
            + `SchemaUrl` (string) (required) – The S3 URL of the updated schema.
          + `IntegrationProtocols` (array) (optional) – Protocol types supported by the endpoint.
            + `Type` (string) (required) – Protocol identifier. Valid values: `MCP`, `A2A`.
            + `UsageInstructions` (string) (required) – Additional instructions for utilizing the protocol with the endpoint.

**Response Syntax**

```json
{
"ChangeSetId": "{{example123456789012abcdef}}", 
"ChangeSetArn": "arn:aws:aws-marketplace:us-east-
1:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This includes validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. You can check the status of the request through the AWS Marketplace Management Portal, or in the Catalog API with the `DescribeChangeSet` action.

**Synchronous Validations**


| Error condition | Message | HTTP code | 
| --- | --- | --- | 
| Empty Delivery Option Ids | Provided Details is not valid. String '' at /DeliveryOptions/0/Id does not match required schema regex, '^do-[a-zA-Z0-9]\+$' | 422 | 
| Missing Delivery Option Ids | Provided Details is not valid. JSON at /DeliveryOptions/0 is missing required properties: ['Id']. | 422 | 
| Duplicate Delivery Option Ids | Provide unique delivery option IDs. | 422 | 
| Invalid Fulfillment Url | Provide a valid fulfillment URL beginning with "https://". | 422 | 
| Invalid Delivery Option IDs | Provide delivery option IDs that can be found in the product. IDs not found: [x] | 422 | 
| Multiple URL Delivery Options | You provided more than one URL delivery option. Provide one URL delivery option. | 422 | 
| Missing delivery option ids | The delivery option ID is missing. Provide one or more valid delivery option IDs that you wish to update, or use AddDeliveryOptions if you intended to add a new delivery option. | 422 | 
| Invalid Launch URL | Provide a valid launch URL beginning with "https://". | 422 | 
| Missing Launch Url | Required parameter LaunchUrl is missing. You must provide a LaunchUrl. | 422 | 
| Missing deployment templates | The deployment template is missing. Provide at least one deployment template. | 422 | 
| Too many deployment templates | You cannot provide more than 20 deployment templates. | 422 | 
| Invalid template URL | Quick Start URL is invalid. Provide deployment template URL that is published through AWS QuickStarts to Amazon S3. Invalid deployment templates URL: [x] | 422 | 
| Invalid deployment template stack name | The deployment template stack name is invalid. Provide a valid stack name using only alphanumeric characters and hyphens. It must start with an alphabetical character and can't be longer than 128 characters. | 422 | 
| Duplicate deployment template title | You provided duplicate deployment template titles. Provide unique deployment template titles. | 422 | 
| Duplicate deployment template URL | You provided duplicate deployment template urls. Provide unique deployment template urls. | 422 | 
| Invalid deployment template type | The deployment template type is invalid. Provide a valid deployment template type. Supported values are ["CloudFormation@1.0"]. | 422 | 
| Invalid deployment template IAM policy | The deployment template IAM policy is invalid. Provide a valid IAM policy. | 422 | 
| Invalid usage instructions |  +  Images aren't supported by the usage instructions. Remove the image [x]. <br />+  You provided a link to an invalid URL in the usage instructions: [x]. Provide a valid URL. <br />+  You provided a link with an unsupported URI scheme in the usage instructions. Use a supported scheme: ["http", "https", "tel", "mailto"].   | 422 | 
| Invalid Access Models | AccessModels must be REGISTRATION\_WITH\_SELLER or AGENTIC\_COMMERCE. | 422 | 
| Invalid Access Models Count | AccessModels must contain exactly 1 value. | 422 | 
| Invalid Agentic Commerce Authorization Types | AuthorizationTypes must be exactly PAYMENT\_TOKEN on every endpoint when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Payment Token Authorization Type Not Allowed | AuthorizationTypes may contain PAYMENT\_TOKEN only when AccessModels contains AGENTIC\_COMMERCE. To use Agentic Commerce, set AccessModels to ["AGENTIC\_COMMERCE"]; on UpdateDeliveryOptions, send AccessModels whenever the request includes Agentic Commerce fields. | 422 | 
| Endpoint Type Not Allowed for Agentic Commerce | EndpointType is not allowed when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Endpoint URL Parameters Not Allowed for Agentic Commerce | EndpointUrlParameters is not allowed when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Endpoint URL Placeholders Not Allowed for Agentic Commerce | EndpointUrl must not contain placeholders when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Agentic Commerce Configuration Not Allowed | AgenticCommerceConfiguration is only valid when AccessModels contains AGENTIC\_COMMERCE. To use Agentic Commerce, set AccessModels to ["AGENTIC\_COMMERCE"]; on UpdateDeliveryOptions, send AccessModels whenever the request includes Agentic Commerce fields. | 422 | 
| Compatible Services Not Allowed for Agentic Commerce | CompatibleServices is not allowed when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Invalid Payment Protocols Count | PaymentProtocols must contain exactly 1 value. | 422 | 
| Invalid Payment Protocol | PaymentProtocols values must be X402. | 422 | 
| Missing Public Key Source | PublicKeySource is required in AgenticCommerceConfiguration. | 422 | 
| Invalid Public Key Source Type | Type must be JWKS or KMS. | 422 | 
| Missing JWKS URI | JwksUri is required when Type is JWKS. | 422 | 
| Missing KMS ARNs | AliasArn and RoleArn are required when Type is KMS. | 422 | 
| JWKS URI Not Allowed | JwksUri is not allowed when Type is KMS. | 422 | 
| KMS ARNs Not Allowed | AliasArn and RoleArn are not allowed when Type is JWKS. | 422 | 
| Invalid JWKS URI | JwksUri must begin with "https://" and point to a JSON file under a /.well-known/ path. | 422 | 
| Invalid KMS Alias ARN | AliasArn must be a valid KMS alias ARN. | 422 | 
| Invalid KMS Role ARN | RoleArn must be a valid IAM role ARN. | 422 | 
| Missing Estimated Usage Cost | EstimatedUsageCost is required on every endpoint when AccessModels contains AGENTIC\_COMMERCE. | 422 | 
| Invalid Estimated Usage Cost | EstimatedUsageCost must be between 1 and 200 characters. | 422 | 
| Estimated Usage Cost Not Allowed | EstimatedUsageCost is only valid when AccessModels contains AGENTIC\_COMMERCE. To use Agentic Commerce, set AccessModels to ["AGENTIC\_COMMERCE"]; on UpdateDeliveryOptions, send AccessModels whenever the request includes Agentic Commerce fields. | 422 | 

**Asynchronous Errors**


| Error code  | Error message | 
| --- | --- | 
| INVALID\_DELIVERY\_OPTION\_IDS | Provide delivery option IDs that can be found in the product. IDs not found: [x] | 
| AUDIT\_ERROR | AWS MP Catalog Audits List - CQ team | 
| INVALID\_FULFILLMENT\_URL | The URL you provided returned HTTP status code [x]. Provide a fulfillment URL that renders with a 200. | 
| INVALID\_LAUNCH\_URL | The URL you provided returned HTTP status code [x]. Provide a launch URL that renders with a 200. | 
| INVALID\_TEMPLATE\_URL  | Quick Start URL is invalid. Provide deployment template URL that is published through AWS QuickStarts to Amazon S3. Invalid deployment templates URL: [x] | 
| DEFAULT\_VALUE\_REQUIRED\_FOR\_NEW\_PARAMETER | Endpoint '[x]' has parameter '[x]' with no DefaultValue. A DefaultValue is required when the product is already Public and this update either introduces the parameter or removes a DefaultValue the parameter previously had. Provide a DefaultValue for the parameter. | 
| INVALID\_ENDPOINT\_SCHEMA\_URL | The schema file is larger than 1 MB: `There was an issue copying the schema from S3. Schema size exceeds 1 MB. Provide a schema that is under 1 MB.` | 
| INVALID\_ENDPOINT\_SCHEMA | For an Agentic Commerce delivery option, the message describes what's wrong with the OpenAPI specification file. It is one of the following:+ `The OpenAPI specification file isn't valid JSON or YAML. Fix the file syntax and upload it again.`<br />+ `The OpenAPI specification file has no openapi or swagger version field. Upload an OpenAPI 3.x or Swagger 2.0 file.`<br />+ `OpenAPI version [x] isn't supported. Upload an OpenAPI 3.x or Swagger 2.0 file.`<br />+ `Swagger version [x] isn't supported. Upload an OpenAPI 3.x or Swagger 2.0 file.`<br />+ `The OpenAPI specification file is missing required top-level fields: [x]. Add them and upload the file again.`<br />+ `The OpenAPI specification file has top-level errors: [x] Fix them and upload the file again.`<br />+ `The OpenAPI specification file has no paths object. Add the API paths and upload the file again.` | 
| INVALID\_ACCESS\_MODELS | AccessModels must contain exactly 1 value: REGISTRATION\_WITH\_SELLER or AGENTIC\_COMMERCE. | 
| ACCESS\_MODELS\_IMMUTABLE | AccessModels cannot be changed after the delivery option is created. Send the stored value or omit the field. | 
| UNSUPPORTED\_ACCESS\_MODEL\_ADDITION | AGENTIC\_COMMERCE cannot be added to an existing delivery option that was not created with AGENTIC\_COMMERCE. Create a new product with AccessModels set to AGENTIC\_COMMERCE instead. | 
| UNSUPPORTED\_ACCESS\_MODEL\_REMOVAL | AGENTIC\_COMMERCE cannot be removed from a delivery option that was created with AGENTIC\_COMMERCE. Create a new product without AGENTIC\_COMMERCE instead. | 
| INVALID\_AGENTIC\_COMMERCE\_CONFIGURATION | AgenticCommerceConfiguration is only valid when AccessModels contains AGENTIC\_COMMERCE. Remove AgenticCommerceConfiguration or set AccessModels to AGENTIC\_COMMERCE. | 
| INCOMPATIBLE\_AGENTIC\_COMMERCE\_AND\_AGENTCORE | AGENTIC\_COMMERCE and Bedrock-AgentCore cannot be used together on the same delivery option. Remove either AGENTIC\_COMMERCE from AccessModels or Bedrock-AgentCore from CompatibleServices. | 
| INVALID\_AGENTIC\_COMMERCE\_AUTHORIZATION\_TYPES | Endpoint AuthorizationTypes must be exactly PAYMENT\_TOKEN when AccessModels contains AGENTIC\_COMMERCE, and may not contain PAYMENT\_TOKEN otherwise. | 
| INVALID\_PAYMENT\_PROTOCOLS | PaymentProtocols must contain exactly 1 value: X402. | 
| INVALID\_PUBLIC\_KEY\_SOURCE | PublicKeySource requires either JwksUri, or AliasArn and RoleArn. | 
| INVALID\_JWKS\_URI | JwksUri must begin with "https://" and be between 8 and 2048 characters. | 
| INVALID\_KMS\_ALIAS\_ARN | AliasArn must be a valid KMS alias ARN. | 
| INVALID\_KMS\_ROLE\_ARN | RoleArn must be a valid IAM role ARN. | 
| MISSING\_ESTIMATED\_USAGE\_COST | EstimatedUsageCost is required on the endpoint when AccessModels contains AGENTIC\_COMMERCE. | 
| INVALID\_ESTIMATED\_USAGE\_COST | EstimatedUsageCost must be between 1 and 200 characters. | 
| UNSUPPORTED\_ESTIMATED\_USAGE\_COST | EstimatedUsageCost is only valid when AccessModels contains AGENTIC\_COMMERCE. Remove EstimatedUsageCost from the endpoint. | 

### Update delivery option visibility
<a name="update-delivery-options-visibility"></a>

You can use the Catalog API to configure permissions so that only some users can change the visibility for a SaaS product in AWS Marketplace. 

To configure permissions so that only some users can change the visibility for a SaaS product, call the `StartChangeSet` API operation with the `UpdateDeliveryOptionsVisibility` change type, as shown in the following example. 

**Note**  
This is only supported for one delivery option: `SaaSUrlDeliveryOptionDetails`. 

**Request Syntax**

```json
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
        "Identifier": "{{prod-example12345}}",
        "Type": "SaaSProduct@1.0"
      },
      "DetailsDocument":
      {
        "DeliveryOptions":
        [
          {
            "Id": "do-{{1234567891234567891234}}",
            "TargetVisibility": "Public"
          },
          {
            "Id": "do-{{43210987654321}}",
            "TargetVisibility": "Limited",
            "Targeting":
            {
              "PositiveTargeting":
              {
                "BuyerAccounts":
                [
                  "{{123456789012}}"
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

Provide information for the fields to add the `UpdateDeliveryOptionsVisibility` change type:
+ `Entity` (object) (required) – Your SaaS-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `SaaSProduct@1.0`. 
+ `DetailsDocument` (object) (required) – Details of the request.
  + `DeliveryOptions` (array) – List of `DeliveryOptions` to be updated.
    + `TargetVisibility` (string) – The delivery option id to be updated.
    + `TargetVisibility` (string) – The intended new visibility of the delivery option.

      Possible values: `Limited`, `Public`, and `Unavailable`.
**Note**  
There is always exactly one `Public` delivery option, and a maximum of one `Limited` delivery option.
    + `Targeting` (object) *optional * – Targeting of the delivery option, used in conjunction with the `Limited` visibility status to be able to test the new delivery option before changing the visibility to `Public`.
      + `PositiveTargeting` (object) – Specifying inclusive targeting.
        + `BuyerAccounts` (array of strings) – The list of buyer AWS account ids who will be able to use the new delivery option. 

          Min size: 0. Max size: 100.

**Response Syntax**

```json
{
"ChangeSetId": "{{example123456789012abcdef}}", 
"ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. You can check the status of the request through the AWS Marketplace Management Portal, or in the Catalog API with the `DescribeChangeSet` action.

**Synchronous Validations**


| Error condition | Message | HTTP code | 
| --- | --- | --- | 
| Missing delivery option ids | The delivery option ID is missing. Provide one or more valid delivery option IDs that you wish to update, or use AddDeliveryOptions if you intended to add a new delivery option. | 422 | 
| Invalid visibility | You provided invalid option for TargetVisibility. Allowed options are: Limited, Public, Unavailable. | 422 | 
| Invalid targeting | You provided invalid option for PositiveTargeting. You must provide a valid parameter for BuyerAccounts. | 422 | 
| Missing Visibility and Targeting | You provided invalid delivery option visibility details. You must provide a valid parameter for at least one of TargetVisibility or Targeting. | 422 | 
| Too many AWS account ids | You cannot provide more than 100 targeted buyer accounts. | 422 | 

**Asynchronous Errors**


| Error code  | Error message | 
| --- | --- | 
| INVALID\_DELIVERY\_OPTION\_IDS | You provided invalid delivery option details. Provide delivery option IDs that can be found in the product. IDs not found: [x] | 
| INVALID\_VISIBILITY | You provided more than one delivery option for the public state. Provide only one public delivery option. | 
| INVALID\_VISIBILITY | You didn't provide a public delivery option. Provide one public delivery option. | 
| AUDIT\_ERROR | Varies based on MCO manual review. | 

## SaaSUrlDeliveryOption
<a name="saas-url-delivery-option"></a>

The following example shows how to use the `SaaSUrlDeliveryOptionDetails` to update the `FulfillmentUrl`.

**Request Syntax**

```json
POST /StartChangeSet HTTP/1.1 
Content-type: application/json
     
{
    "Catalog": "AWSMarketplace",
    "ChangeSet": [
        {
            "ChangeType": "UpdateDeliveryOptions",
            "Entity": {
                "Identifier": "{{example1-abcd-1234-5ef6-7890abcdef12@1}}",
                "Type": "SaaSProduct@1.0"
            },
            "DetailsDocument": {
                "DeliveryOptions": [
                    {
                        "Id": "do-{{1234567891234567891234}}",
                        "Details": {
                            "SaaSUrlDeliveryOptionDetails": {
                                "FulfillmentUrl": "https://www.aws.amazon.com/marketplace/management",
                                "LaunchUrl": "{{URL}}",
                                "UsageInstructions": "{{Instructions}}",
                                "DeploymentTemplates": [
                                    {
                                        "Title": "{{CloudFormation Template 123}}",
                                        "Description": "{{CloudFormation description}}",
                                        "IamPolicy": "{\"Version\":\"2012-10-17\",		 	 	 \"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"s3:Get*\",\"s3:List*\"],\"Resource\":\n[\"arn:aws:s3:::amzn-s3-demo-bucket\",\"arn:aws:s3:::amzn-s3-demo-bucket/*\"]}]}"
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

Provide information for the fields to add the `AddDeliveryOptions` change type:
+ `Entity` (object) (required) – Your SaaS-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `SaaSProduct@1.0`. 
+ **DetailsDocument** (object) (required) – Details of the request.
  + `DeliveryOptions` (array) – Contains the details of the delivery options being updated.
    + `TargetVisibility` (string) – Unique identifier for the `DeliveryOption`. (Get the unique identifier for the `DeliveryOption` by calling the `DescribeEntity` action on the product you are updating.)
    + `Details` (object) – Contains the `SaaSUrlDeliveryOptionDetails` of the delivery option to be updated.
      + `SaaSUrlDeliveryOptionDetails` (object) – Contains the `FulfillmentUrl` of a delivery option for SaaS product.
        + `FulfillmentUrl` (string) – The URL to be updated for the SaaS product.
        + `LaunchUrl` (string) – The URL to your SaaS product's landing page. This is required if `QuickLaunchEnabled` is set to `True`.
        + `UsageInstructions` (string) – Instructions for using this delivery option. Include documentation for manual steps for customers who won't use `DeploymentTemplates`.
        + `DeploymentTemplates` (array) – Deployment templates that customers can use to set up and conﬁgure the SaaS product and any related AWS resources.
          + `Title` (string) – The display name of the deployment template.
          + `Description` (string) – A description for what the deployment template contains.
          + `IamPolicy` (string) – An IAM policy describing the permissions needed to deploy the template. Buyers can use this IAM policy to quickly deploy the template.
          + `CloudFormationDetails` (object) – The details of a CloudFormation template.
            + `TemplateUrl` (string) – The URL for the deployment template.
            + `DefaultStackName` (string) – The default name used in CloudFormation when the customer creates the template.

**Response Syntax**

```json
{
"ChangeSetId": "{{example123456789012abcdef}}", 
"ChangeSetArn": "arn:aws:aws-marketplace:us-east-
1:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This includes validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. You can check the status of the request through the AWS Marketplace Management Portal, or in the Catalog API with the `DescribeChangeSet` action.

**Synchronous Validations**


| Error condition | Message | HTTP code | 
| --- | --- | --- | 
| Empty Delivery Option Ids | Provided Details is not valid. String '' at /DeliveryOptions/0/Id does not match required schema regex, '^do-[a-zA-Z0-9]\+$' | 422 | 
| Missing Delivery Option Ids | Provided Details is not valid. JSON at /DeliveryOptions/0 is missing required properties: ['Id']. | 422 | 
| Duplicate Delivery Option Ids | Provide unique delivery option IDs. | 422 | 
| Invalid Fulfillment Url | Provide a valid fulfillment URL beginning with "https://". | 422 | 
| Invalid Delivery Option IDs | Provide delivery option IDs that can be found in the product. IDs not found: [x] | 422 | 
| Multiple URL Delivery Options | You provided more than one URL delivery option. Provide one URL delivery option. | 422 | 
| Missing delivery option ids | The delivery option ID is missing. Provide one or more valid delivery option IDs that you wish to update, or use AddDeliveryOptions if you intended to add a new delivery option. | 422 | 
| Invalid Launch URL | Provide a valid launch URL beginning with "https://". | 422 | 
| Missing Launch Url | Required parameter LaunchUrl is missing. You must provide a LaunchUrl. | 422 | 
| Missing deployment templates | The deployment template is missing. Provide at least one deployment template. | 422 | 
| Too many deployment templates | You cannot provide more than 20 deployment templates. | 422 | 
| Invalid template URL | Quick Start URL is invalid. Provide deployment template URL that is published through AWS QuickStarts to Amazon S3. Invalid deployment templates URL: [x] | 422 | 
| Invalid deployment template stack name | The deployment template stack name is invalid. Provide a valid stack name using only alphanumeric characters and hyphens. It must start with an alphabetical character and can't be longer than 128 characters. | 422 | 
| Duplicate deployment template title | You provided duplicate deployment template titles. Provide unique deployment template titles. | 422 | 
| Duplicate deployment template URL | You provided duplicate deployment template urls. Provide unique deployment template urls. | 422 | 
| Invalid deployment template type | The deployment template type is invalid. Provide a valid deployment template type. Supported values are ["CloudFormation@1.0"]. | 422 | 
| Invalid deployment template IAM policy | The deployment template IAM policy is invalid. Provide a valid IAM policy. | 422 | 
| Invalid usage instructions |  +  Images aren't supported by the usage instructions. Remove the image [x]. <br />+  You provided a link to an invalid URL in the usage instructions: [x]. Provide a valid URL. <br />+  You provided a link with an unsupported URI scheme in the usage instructions. Use a supported scheme: ["http", "https", "tel", "mailto"].   | 422 | 

**Asynchronous Errors**


| Error code  | Error message | 
| --- | --- | 
| INVALID\_DELIVERY\_OPTION\_IDS | Provide delivery option IDs that can be found in the product. IDs not found: [x] | 
| AUDIT\_ERROR | AWS MP Catalog Audits List - CQ team | 
| INVALID\_FULFILLMENT\_URL | The URL you provided returned HTTP status code [x]. Provide a fulfillment URL that renders with a 200. | 
| INVALID\_LAUNCH\_URL | The URL you provided returned HTTP status code [x]. Provide a launch URL that renders with a 200. | 
| INVALID\_TEMPLATE\_URL  | Quick Start URL is invalid. Provide deployment template URL that is published through AWS QuickStarts to Amazon S3. Invalid deployment templates URL: [x] | 

### Update delivery option visibility
<a name="update-delivery-options-visibility"></a>

You can use the Catalog API to configure permissions so that only some users can change the visibility for a SaaS product in AWS Marketplace. 

To do so, call the `StartChangeSet` API operation with the `UpdateDeliveryOptionsVisibility` change type, as shown in the following example. 

**Note**  
This is only supported for one delivery option: `SaaSUrlDeliveryOptionDetails`. 

**Request Syntax**

```json
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
        "Identifier": "{{prod-example12345}}",
        "Type": "SaaSProduct@1.0"
      },
      "DetailsDocument":
      {
        "DeliveryOptions":
        [
          {
            "Id": "do-{{1234567891234567891234}}",
            "TargetVisibility": "Public"
          },
          {
            "Id": "do-{{43210987654321}}",
            "TargetVisibility": "Limited",
            "Targeting":
            {
              "PositiveTargeting":
              {
                "BuyerAccounts":
                [
                  "{{123456789012}}"
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

Provide information for the fields to add the `UpdateDeliveryOptionsVisibility` change type:
+ `Entity` (object) (required) – Your SaaS-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `SaaSProduct@1.0`. 
+ `DetailsDocument` (object) (required) – Details of the request.
  + `DeliveryOptions` (array) – List of `DeliveryOptions` to be updated.
    + `TargetVisibility` (string) – The delivery option id to be updated.
    + `TargetVisibility` (string) – The intended new visibility of the delivery option.

      Possible values: `Limited`, `Public`, and `Unavailable`.
**Note**  
There is always exactly one `Public` delivery option, and a maximum of one `Limited` delivery option.
    + `Targeting` (object) *optional * – Targeting of the delivery option, used in conjunction with the `Limited` visibility status to be able to test the new delivery option before changing the visibility to `Public`.
      + `PositiveTargeting` (object) – Specifying inclusive targeting.
        + `BuyerAccounts` (array of strings) – The list of buyer AWS account ids who will be able to use the new delivery option. 

          Min size: 0. Max size: 100.

**Response Syntax**

```json
{
"ChangeSetId": "{{example123456789012abcdef}}", 
"ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. You can check the status of the request through the AWS Marketplace Management Portal, or in the Catalog API with the `DescribeChangeSet` action.

**Synchronous Validations**


| Error condition | Message | HTTP code | 
| --- | --- | --- | 
| Missing delivery option ids | The delivery option ID is missing. Provide one or more valid delivery option IDs that you wish to update, or use AddDeliveryOptions if you intended to add a new delivery option. | 422 | 
| Invalid visibility | You provided invalid option for TargetVisibility. Allowed options are: Limited, Public, Unavailable. | 422 | 
| Invalid targeting | You provided invalid option for PositiveTargeting. You must provide a valid parameter for BuyerAccounts. | 422 | 
| Missing Visibility and Targeting | You provided invalid delivery option visibility details. You must provide a valid parameter for at least one of TargetVisibility or Targeting. | 422 | 
| Too many AWS account ids | You cannot provide more than 100 targeted buyer accounts. | 422 | 

**Asynchronous Errors**


| Error code  | Error message | 
| --- | --- | 
| INVALID\_DELIVERY\_OPTION\_IDS | You provided invalid delivery option details. Provide delivery option IDs that can be found in the product. IDs not found: [x] | 
| INVALID\_VISIBILITY | You provided more than one delivery option for the public state. Provide only one public delivery option. | 
| INVALID\_VISIBILITY | You didn't provide a public delivery option. Provide one public delivery option. | 
| AUDIT\_ERROR | Varies based on MCO manual review. | 