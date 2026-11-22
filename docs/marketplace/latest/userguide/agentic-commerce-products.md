

# Listing Agentic Commerce products

With Agentic Commerce, AI agents pay for each request that they send to your API-based AI agent or tool product. Buyers don't subscribe, register, or receive credentials. Their agents pay through Amazon Bedrock AgentCore payments, and the charges appear on the buyer's AWS bill. Your endpoint asks for payment by using an extension of the open x402 protocol, which is based on the HTTP 402 `Payment Required` status code. For more information, see the [x402 website](https://docs.x402.org).

Agentic Commerce is an optional capability of the API delivery option for SaaS API-based AI agent products. You choose it as the access model when you configure the product's fulfillment options. For more information, see [Add the Agentic Commerce delivery option](#agentic-commerce-add-delivery-option).

## How Agentic Commerce works
<a name="agentic-commerce-how-it-works"></a>

A paid request follows these steps:

1. An AI agent sends a request to your endpoint without a payment.

1. Your endpoint responds with HTTP 402 and an x402 quote. The quote states the price of the request. You sign the quote with your quote-signing key.

1. The agent asks AgentCore payments to pay the quote. The buyer's payment manager in AgentCore payments uses the AWS Billing connector.

1. AWS Marketplace verifies the quote's signature against the key that you registered for the product. It then checks that the buyer can buy the product, and returns a payment token that AWS Marketplace signs.

1. The agent sends the request again with the payment token. Your endpoint verifies the payment token and serves the request.

1. AWS Marketplace creates the buyer's agreement and meters the charge. The buyer pays the amount of the quote on their AWS bill, and you receive payment through standard AWS Marketplace disbursement.

At run time, your only interaction with AWS Marketplace is verifying payment tokens. You don't call AWS Marketplace APIs to resolve customers, check entitlements, or meter usage.

## Requirements and limitations
<a name="agentic-commerce-requirements"></a>
+ **x402 endpoint** – Each endpoint must be a static HTTPS URL that returns HTTP 402 with a signed x402 quote when a request has no payment. Agentic Commerce supports only the x402 protocol.
+ **API specification** – If you upload an OpenAPI specification file for buyer agents, it must be an OpenAPI 3.x or Swagger 2.0 document in JSON or YAML, with the required top-level fields for its version, such as `info`. AWS Marketplace checks that the file parses, declares a supported version, and has those fields. It doesn't apply the Amazon Bedrock AgentCore Gateway rules, because buyers download the file instead of connecting through a gateway, and it doesn't resolve references in the file. If the check fails, the change request fails with `INVALID_ENDPOINT_SCHEMA` and a message that gives the reason. The file can be up to 1 MB. A larger file fails with `INVALID_ENDPOINT_SCHEMA_URL`.
+ **Quote-signing key** – You register the public key that verifies your quotes, as a JSON Web Key Set (JWKS) URL or an AWS Key Management Service (AWS KMS) key. For more information, see [Configuring your quote-signing key](agentic-commerce-signing-key.md).
+ **Separate product** – A product supports either Agentic Commerce or registration-based access, not both. You can't add Agentic Commerce to an existing product, and you can't change the access model after you add the delivery option. To offer both access models, list two products.
+ **Public usage offer only** – Agentic Commerce products have one usage-based public offer. They don't support private offers, free trials, free pricing, or Concurrent Agreements.
+ **Region and currency** – Agentic Commerce is available in the US East (N. Virginia) Region (`us-east-1`), and quotes are in US dollars (USD).
+ **No AgentCore Gateway integration** – You can't enable Amazon Bedrock AgentCore Gateway integration for an Agentic Commerce product.

## Add the Agentic Commerce delivery option
<a name="agentic-commerce-add-delivery-option"></a>

When you add the delivery option in the listing wizard, complete *To configure fulfillment options* in [Configure fulfillment options](listing-saas-ai-agents.md#step-2-fulfillment-options) first. It switches **Delivery method** to **API-based agents and tools**. Then use these steps instead of the procedures that follow it.

**To add the Agentic Commerce delivery option**

1. Choose your AI agent or tool type.

1. For **Access model**, choose **Agentic Commerce**. **Registration with seller** is selected by default. The console sets the authorization method to the payment token, and it doesn't show the fulfillment method choice or Amazon Bedrock AgentCore Gateway integration. You can't change the access model after you add the delivery option.

1. For the fulfillment URL, enter the URL of your sign-in page, or a setup page if buyers don't need an account.

1. Enter the endpoint URL: the static HTTPS URL of your x402 endpoint.

1. For **Estimated cost per request (USD)**, enter a typical price for one request, in US dollars (USD): an amount, such as `0.01`, or a range, such as `0.002 to 0.01`. Use up to 8 decimal places, and don't include a currency sign or code. The amount must be greater than 0, and in a range the first amount must be less than the second.

1. For **Public key source**, choose **JWKS endpoint URL** and enter the URL, or choose **KMS key** and enter the ARN of the key alias and the ARN of the IAM role that AWS Marketplace assumes. For the requirements, see [Configuring your quote-signing key](agentic-commerce-signing-key.md). The public key source stays editable after you add the delivery option, so that you can rotate your key.

1. (Optional) Under **API specification**, upload an OpenAPI specification file, up to 1 MB. Then complete the remaining fields and add the delivery option.

Put the product ID in every quote that your endpoint signs, as the `settlement.product_id` claim. AWS Marketplace uses it to find the public key that you registered for the product and to bill that product. The product has its ID as soon as it's created, so you can build the endpoint before you add the delivery option. To find the ID, open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central: it's in the **Product ID** column and on the product's page. If you use the AWS Marketplace Catalog API instead, see [Find your product ID](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-seller-products.html#seller-product-id) in the *AWS Marketplace Developer Guide*.

An endpoint signs quotes for one product. To list two Agentic Commerce products, sign a different `settlement.product_id` for each. For more information, see [Quote guidelines](#agentic-commerce-quotes).

## Building your endpoint with an AI agent
<a name="agentic-commerce-agent-skill"></a>

You can add the **AWS Marketplace Agentic Commerce agent skill** (`aws-marketplace-agentic-commerce`) to your own coding agent. The skill is a set of instructions and reference material. With it, your agent can add Agentic Commerce payments to your x402 endpoint. The skill includes guidance on the following:
+ The seller SDKs for Python and TypeScript
+ Quote signing with your AWS KMS key or with the private key behind your JWKS URL, and payment token verification
+ The product ID as the route's `payTo`
+ Troubleshooting for rejected payments

To get the skill without checking it out locally, install the [AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html) in your coding agent. The agent then loads the skill at runtime. For the skill source, see the [aws-marketplace-agentic-commerce skill on the GitHub website](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/aws-marketplace-skills/aws-marketplace-agentic-commerce).

The skill covers your endpoint only. It doesn't create the product or its delivery option, and it doesn't create your quote-signing key. Before you use the skill, you must have several values, including the following:
+ The product ID
+ The endpoint URL
+ The quote-signing key

Use the same endpoint URL and quote-signing key that you enter in the delivery option. Use the endpoint URL exactly as buyers call it.

Before you go live, apply all of the production settings that the skill describes, including the following:
+ Accept each payment only once, by recording verified payments in a store that every instance of your endpoint shares.
+ Use a DPoP nonce store that every instance of your endpoint shares.
+ The request URL that your endpoint sees must be the public URL that buyers call. Behind a proxy or load balancer, forward the original host and scheme. Trust forwarding headers only from your own proxy or load balancer.
+ An unpaid `HEAD` request must not be able to run a paid route.
+ If you use a JWKS URL, load the private key from a secrets manager or a mounted file, never from source control.
+ If you use an AWS KMS key, grant your endpoint's own role `kms:Sign` and `kms:GetPublicKey` on the key ARN, not the alias ARN. AWS Marketplace assumes a separate role. That role needs only `kms:GetPublicKey`.
+ Throttle paid routes.

## Pricing and metering
<a name="agentic-commerce-pricing"></a>

You set the price of each request in the quote that your endpoint returns. The AWS Marketplace offer doesn't set the price.

Every Agentic Commerce offer has one reserved pricing dimension, `agentic_commerce_default`, with the unit type `Units`. Each unit is one US dollar of quoted charges. For each verified payment, AWS Marketplace meters a quantity equal to the quote amount in dollars, so the buyer pays the quoted amount. An Agentic Commerce offer can't use other dimensions, and you can't meter usage against this one.

When you list the product in the console, AWS Marketplace adds this dimension to your product and sets its rate for you, and you can't change the rate. If you use the AWS Marketplace Catalog API instead, you add the dimension yourself and set the same fixed rate. For more information, see [Configure pricing for Agentic Commerce products](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-saas-products.html#saas-agentic-commerce-pricing) in the *AWS Marketplace Developer Guide*.

Don't send metering records for Agentic Commerce requests. AWS Marketplace meters each verified payment on the buyer's account.

Standard AWS Marketplace listing fees for SaaS public offers apply. For more information, see [Understanding listing fees for AWS Marketplace sellers](listing-fees.md).

## Quote guidelines
<a name="agentic-commerce-quotes"></a>
+ Set a short expiration time on each quote. A quote stays payable until it expires. After you rotate your key, quotes that the old key signed fail when AWS Marketplace can no longer resolve that key.
+ Sign every quote with the key that you registered. When you use a JWKS URL, include the key ID (`kid`) in the quote header. When you use an AWS KMS alias, either omit `kid` or set it to the alias name, for example `quote-signing-key` for `alias/quote-signing-key`.
+ AWS Marketplace rejects a quote unless it meets these requirements:
  + The quote has a `settlement.product_id` claim equal to the product ID of your Agentic Commerce product, for example `prod-1234567890123`. AWS Marketplace uses it to find the public key that you registered for the product and to bill that product. It rejects a quote without it, and a quote for a product that your key isn't registered for fails verification. With the seller SDKs, set the route's `payTo` to the product ID.
  + The quote has an `iss` (issuer) claim that identifies your endpoint.
  + The `aud` claim contains `aws:marketplace`.
  + The `scheme` claim is `exact`, and the `network` claim is `aws:base`.
  + The price currency is `USD`. The price amount is zero or more, at most 100,000, with no more than 8 decimal places.
  + The `iat` (issued at) time is no more than 5 minutes in the future and is before the `exp` (expiration) time. The quote is valid for no more than 30 days.
+ In the delivery option, provide an estimated cost per request. Buyers and their agents see this estimate before they pay. It's for display only and isn't used for billing.

## Refunds and reporting
<a name="agentic-commerce-refunds-reporting"></a>

Refunds for Agentic Commerce charges follow the standard AWS Marketplace refund process. AWS Marketplace meters each payment as usage on the buyer's agreement. After a charge appears on an invoice, you can apply a billing adjustment (refund) to that invoice. Billing adjustments apply to the invoice, not to individual payments. There's no separate API for adjusting individual Agentic Commerce payments. For more information about billing adjustments, see [Refunds and cancellations in AWS Marketplace](refunds.md).

In seller reports and data feeds, the usage quantity for the `agentic_commerce_default` dimension is in dollars. One unit is one US dollar of quoted charges. For more information, see [Usage dashboard](usage-dashboard.md).