# Integrating API-based AI agent products

## API-based AI agent products guidelines

AWS Marketplace provides guidelines for all software as a service (SaaS) API-based AI agent products. These guidelines ensure a secure and trustworthy experience for customers.

###### Topics

- [Product review process](#product-review-process "#product-review-process")
- [Maintaining compliance](#maintaining-compliance "#maintaining-compliance")

### Product review process

When you submit a product, AWS Marketplace reviews the product and its metadata to verify that it meets current guidelines. We regularly update these guidelines to address evolving security requirements.

### Maintaining compliance

AWS Marketplace continuously monitors products to verify compliance. If your product doesn't meet current guidelines:

- Your product might be unavailable to new subscribers until you resolve the issues
- You must update your product to meet the new requirements

| Category                                | Guidelines                                                                                                                                                                                                                     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| API and agent functionality             | All the APIs should be functional and respond back appropriately. If you are listing an Agent, the solution must demonstrate autonomous capabilities by operating without explicit external commands or constant human inputs. |
| API access and authentication           | The customer should be able to subscribe to your listing and retrieve API Keys or follow the steps to generate the OAuth token.                                                                                                |
| Architecture guidelines                 | [Follow Architecture guidelines for more details.](saas-guidelines.md#saas-architecture "saas-guidelines.md#saas-architecture")                                                                                                |
| Customer information requirements       | [Follow Customer information requirements for more details.](saas-guidelines.md#saas-customer-information "saas-guidelines.md#saas-customer-information")                                                                      |
| Key management                          | Vendors should provide the customers ability to invalidate/rotate keys. Vendors should also have an mechanism to invalidate keys once the customer unsubscribes from the listing.                                              |
| MCP server requirements (if applicable) | For MCP Server, vendors should provide remote MCP configuration details alongside any prerequisite or environment variables for set up.                                                                                        |
| Product setup                           | [Follow Product setup guidelines for more details.](saas-guidelines.md#saas-guidelines-setup "saas-guidelines.md#saas-guidelines-setup")                                                                                       |
| Product usage                           | [Follow Product usage guidelines for more details.](saas-guidelines.md#saas-product-usage "saas-guidelines.md#saas-product-usage")                                                                                             |
| Usage instructions                      | The usage Instructions should clearly state prerequisites, authentication setup, supported endpoints, request/response schema, tool description, error codes, and additional resources.                                        |

## Integrating API-based AI agent products

### Integrating based on product pricing

Integrating your product with AWS Marketplace is one step in listing an API-based AI agent product. To integrate your API-based AI agent product with AWS Marketplace, you must write code and demonstrate that it can respond successfully to several customer scenarios.

For information about integrating your product based on different pricing models, see the following topics:

- For information about subscription-based products, see [Integrating your SaaS subscription or Pay-As-You-Go product with AWS Marketplace](saas-integrate-subscription.md "saas-integrate-subscription.md").
- For information about contract-based products, see [Integrating your SaaS contract product with AWS Marketplace](saas-integrate-contract.md "saas-integrate-contract.md").
- For information about contract with pay-as-you-go products, see [Integrating your SaaS contract-based product with AWS Marketplace](saas-integrate-contract-with-pay.md "saas-integrate-contract-with-pay.md").

### Customer onboarding

#### Redirect to Website fulfillment

When customers subscribe to your product through AWS Marketplace, they access the product in your AWS environment. After subscribing, we direct customers to your product's website to register their account and configure the product.

- Learn about onboarding customers using Redirect to Website fulfillment in [Onboarding customers to your SaaS product through AWS Marketplace](saas-product-customer-setup.md "saas-product-customer-setup.md").

#### QuickLaunch fulfillment

When customers subscribe to your product through AWS Marketplace, they receive an
API key or OAuth credentials to make calls to your API endpoint or MCP server.
The process works as follows:

- Customer subscribes to the product.
- Customer signs up or signs in to an account on your website.
- You use the **PutDeploymentParameter**
  API to store the API key or OAuth credentials in the customer's AWS
  Secrets Manager.
- If you store one parameter in the case of API keys, call the
  `PutDeploymentParameter` API with the
  `secretString` parameter being a string. If you store
  more than one parameter in the case of OAuth credentials, provide a JSON
  string with key-value pairs in the `secretString` parameter
  as shown below:

```
{
  "Client Id": "`12345`",
  "Client Secret": "`12345`",
  "Discovery URL" : "`https://auth.example.com/.well-known/openid-configuration`"
}
```

Learn more about QuickLaunch fulfillment in these resources:

- Learn about **PutDeploymentParameter** API in
  [AWS Marketplace Deployment API](../APIReference/API_Operations_AWS_Marketplace_Deployment_Service.md "../APIReference/API_Operations_AWS_Marketplace_Deployment_Service.md")
- Find customer onboarding instructions in [Onboarding customers to your SaaS product through AWS Marketplace](saas-product-customer-setup.md "saas-product-customer-setup.md")

### Accessing AWS Marketplace APIs

This following section outlines the process of integrating with the AWS Marketplace Metering Service or AWS Marketplace Entitlement Service, used to ensure that your billing and reporting for customer usage of your products is accurate.

- To learn more about accessing AWS Marketplace APIs, see [Accessing the AWS Marketplace
  Metering and Entitlement Service APIs](saas-integration-metering-and-entitlement-apis.md "saas-integration-metering-and-entitlement-apis.md").

### SNS notifications

Subscribe to Amazon Simple Notification Service (Amazon SNS) topics to receive notifications about customer subscription changes and contract entitlements for your products. AWS Marketplace provides these topics during product creation to help you manage customer access.

The following Amazon SNS topics are available for SaaS API-based products:

- [Amazon SNS topic:
  aws-mp-entitlement-notification](saas-notification.md#saas-sns-message-body "saas-notification.md#saas-sns-message-body") – Notifies you when customers create, upgrade, or renew contracts, or when contracts expires. This is only available for products with pricing models that include a contract.
- [Amazon SNS topic:
  aws-mp-subscription-notification](saas-notification.md#saas-sns-subscription-message-body "saas-notification.md#saas-sns-subscription-message-body") – Notifies you when customers subscribe or unsubscribe from your product and includes the `offer-identifier` for private offers and a free trials flag for SaaS free trials. This is available for all pricing models, including contracts and subscriptions.

## Usage instructions templates

### MCP server usage instructions template

The following example demonstrates usage instructions for an MCP server, including tool descriptions, prerequisites, authentication setup, configuration for popular clients, rate limits, and additional resources:

```

To get started using the remove MCP server, follow the instructions below:

**Availble Tools**
This MCP server support the following tools:
- Search - Performs a web search
- Summarize Website - Summarizes a webpage

**Prerequisites**
- Install **Node.js** and **npm**

**Authentication**
Replace `YOUR_API_KEY` with your actual key below.

**Claude Desktop**
Edit the configuration file at:
- macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
- Windows: %APPDATA%\Claude\claude_desktop_config.json

Add the below code:
```

{
"mcpServers": {
"demo-example": {
"command": "npx",
"args": [
"mcp-remote",
"https://remote.mcp.server/sse",
"--header",
"Authorization: Bearer <YOUR_API_KEY>"
]
},
}
}

```

**Cline**
Cline stores MCP server configurations in a JSON file that can be modified.
In the "Installed" tab, click "Configure MCP Servers" to access the settings file.

Add the following:
```

{
"mcpServers": {
"demoServer": {
"url": "https://remote.mcp.server/sse",
"disabled": false,
"autoApprove": ["searchWeb", "summarizeWebsite"],
"timeout": 30
}
}
}

```

**Rate Limits**
- 60 requests per minute per API key.
- Exceeding returns HTTP 429 Too Many Requests.
- Use retry and exponential backoff to handle limits.

**Learn More**
MCP Docs: https://mcp.search.demoproduct.com

```

### AI Agent and Agent & Tools usage instructions template

The following example demonstrates usage instructions for an Agent or Agent tools, including prerequisites, authentication setup, supported endpoints, request/response schema, error codes, and additional resources:

````

To get started follow the instructions below:

**Authentication**
All API requests require this HTTP header:
Authorization: Bearer `YOUR_API_KEY`
Replace `YOUR_API_KEY` with your actual key.

**Search Endpoint**

**Endpoint:** `GET /web/search`
Performs a web search.

**Query Parameters:**
| Param | Type | Description |
|------------|--------|-------------------------------------|
| `q` | string | Your search query (required) |
| `count` | int | Number of results (default: 10) |
| `offset` | int | Offset for pagination |
| `country` | string | Country code (e.g. `us`, `de`) |
| `safesearch` | string | `off`, `moderate`, or `strict` |

**Example Request:**
```bash
curl -X GET "https://api.search.demo.com/res/v1/web/search?q=searchtool" \
-H "Authorization: Bearer YOUR_API_KEY"
````

**Response Schema:**

```
{
    "results": [{
            "title": "string",
            "url": "string",
            "description": "string"
    }],
    "query" :"string",
    "total" :"number"
}
```

**Example Response:**

```
{
    "results": [
      {
        "title": "DemoProductAPI",
        "url": "https://demo.com",
        "description": "Demo Product API is a search tool for..."
      }
    ],
    "query": "searchtool",
    "total": 1
}
```

**Additional Search Types**
DemoProduct also supports:

- `GET /news/search – News articles`
- `GET /images/search – Image results`
- `GET /videos/search – Video results`

These endpoints follow the same format as /web/search.

**Summarize Endpoint**
**Endpoint:** `POST /summarize`

Summarizes a webpage
**Request Headers:**  
Content Type: application/json
**Request Body:**

```
{
    "input": "string" // URL or plain text
}
```

**Example Request:**

```
{
    "input": "https://example.com/article"
}
```

**Response Schema**

```
    {
            "summary": "string"
    }
```

**Example Response**

```
    {
         "summary": "This article explains our commitment to user privacy."
    }
```

**Error Codes**
| Status | Meaning |
| ------ | ------------------------------ |
| `401` | Unauthorized (check your key) |
| `429` | Too many requests (rate limit) |
| `500` | Server error |

All error responses follow this structure:

```
{
    "error": {
    "code": 401,
    "message": "Unauthorized"
    }
}
```

**Rate Limits**

- 60 requests per minute per API key.
- Exceeding returns HTTP 429 Too Many Requests.
- Use retry and exponential backoff to handle limits.

**Learn More**
API Docs: https://api.search.demoproduct.com

```

```
