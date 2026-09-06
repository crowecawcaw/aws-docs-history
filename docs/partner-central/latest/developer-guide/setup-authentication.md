

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Setup and authentication
<a name="setup-authentication"></a>

Setting up and authenticating with the AWS Partner Central API involves three steps. Here’s an overview of the process:

1. Link your AWS Marketplace Seller account to Partner Central.

1. Set up permissions using IAM.

1. Authenticate your API calls using Signature Version 4 (SigV4).

## Linking your AWS account to Partner Central
<a name="linking-aws-account"></a>

Linking your AWS account to Partner Central is a prerequisite for using the API. For more information, see [Linking AWS Partner Central accounts with AWS Marketplace seller accounts](https://docs.aws.amazon.com/partner-central/latest/getting-started/account-linking.html). You must sign in to Partner Central with an account that has alliance-lead or cloud-administrator permissions, navigate to the **Account Linking** section, and follow the prompts.

## Setting up IAM
<a name="setting-up-iam"></a>

To use the AWS Partner Central API, you will need an AWS Identity and Access Management (IAM) role or an IAM user to start making calls. For more information, see [When do I use IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/when-to-use-iam.html). Follow the steps for [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) and [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) in your AWS account guides for this. You must create this IAM Role/User in your Partner Central-linked AWS Marketplace Seller account. IAM role/user creation does not incur any costs.

1. Create an IAM Role/User

   Sign in to the AWS Management Console, navigate to the IAM service, and follow the steps to create an IAM role or an IAM user.

1. Assign Policies:

   Attach managed policies or create custom policies as needed. To modify or expand permissions, apply additional policies to the IAM Role instead of copying and combining the content from `AWSPartnerCentralOpportunityManagement` with other permissions. Avoid duplicating managed policies, as doing so will prevent you from automatically gaining access to new features as they're released, and you'll have to manually update your policies in the future. For more details about access policies, see the [Access Control documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Managing AWS Marketplace offers
<a name="managing-marketplace-offers"></a>

For managing AWS Marketplace offers and linking them to opportunities, partners must give the IAM role permission to access Catalog APIs. Ensure the role/user has permissions, such as `aws-marketplace:ListEntities` and `aws-marketplace:SearchAgreements`.

## Authenticating API calls
<a name="authenticating-api-calls"></a>

AWS Partner Central API uses Signature Version 4 (SigV4) for authentication. Here’s how to implement it:

### Using the AWS SDK
<a name="using-aws-sdk"></a>

AWS SDKs automatically handle request signing. Provide your AWS credentials, and the SDK does the rest.

1. For Java, see [Provide temporary credentials to the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html).

1. For Python (Boto3), see [Credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

1. For JavaScript (Node.js), see [Setting credentials in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html).

1. For .NET, see [Credential and profile resolution](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/creds-assign.html).

1. For other programming languages and more examples, see the [Tools to Build on AWS](https://aws.amazon.com/tools/).

### Authentication without using the AWS SDK
<a name="authentication-without-sdk"></a>

If an AWS SDK is not available for your chosen programming language, authentication involves manually creating a canonical request, signing the request, and handling the session tokens. AWS offers comprehensive guidance for [using SigV4 signing](https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html). However, please note that using the AWS SDK is recommended as manual request signing increases the complexity and requires careful management of security tokens.

Every request for the awsJson1\_0 protocol MUST be sent to the root URL (/) using the HTTP "POST" method using following headers.

### Required Headers
<a name="required-headers"></a>

Every API request for the awsJson1\_0 protocol MUST be sent to the root URL (/) using the HTTP "POST" method using following headers.


| Header | Required | Description | 
| --- | --- | --- | 
| Content-Type | true | This header has a static value of application/x-amz-json-1.0. | 
| Content-Length | true | The standard Content-Length header defined by [RFC 9110\#section-8.6](https://datatracker.ietf.org/doc/html/rfc9110.html#section-8.6). | 
| X-Amz-Target | true for requests | For example, the value for the operation CreatePartner of the service PartnerCentralAccount is PartnerCentralAccount.CreatePartner. | 

## Signing your calls with custom user-agent
<a name="signing-your-calls"></a>

When making API requests to AWS Partner Central, we recommends including the `X-Amzn-User-Agent` header to help AWS identify the source of the client application, monitor usage, and audit performance. AWS uses this header to distinguish the type of client application making the call and to gather insights about the success rate of different client implementations.

### Custom user-agent header
<a name="custom-user-agent-header"></a>

**Header Name:** `X-Amzn-User-Agent`

**Purpose:** Distinguishes the type of client making the API request, categorizing the source of the interaction.

**Format:** `{Integrator}|{Product}`

**Example Value:** `AWS|AWS Partner CRM Connector`

Including this header in every request enables AWS to analyze request patterns, track integrations, and improve the API experience for different client systems.

### Using custom headers in SDKs
<a name="using-custom-headers"></a>

To include the `X-Amzn-User-Agent` header in SDK calls, you can modify the client request behavior before making the API call. Below is a selling API example using the AWS SDK for Python (Boto3):

```
import boto3

# Define service and endpoint details
service_name = "partnercentral-selling"
endpoint_url = "https://partnercentral-selling.us-east-1.api.aws"

# Create a boto3 client for Partner Central
partner_central_client = boto3.client(
service_name=service_name,
='us-east-1',
endpoint_url=endpoint_url
)

# Function to add the custom User-Agent header

def add_version_header(params, **kwargs):
params["headers"]['X-Amzn-User-Agent'] = 'AWS|AWS Partner CRM Connector'

# Register the event to modify the request before the call is made
partner_central_client.meta.events.register(
f'before-call.{service_name}.*', add_version_header
)

# Now, whenever an API call is made using this client, the custom User-Agent header will be included
```

This example demonstrates how to register an event in the Boto3 SDK to automatically append the `X-Amzn-User-Agent` header to every API request. The same approach can be applied to other AWS SDKs by modifying their respective request-interception mechanisms.

**Note**  
The `X-Amzn-User-Agent` header format has been simplified. We recommend to use the new format. The previous format (`CompanyName|ProductName|CRMName|ProductVersion`) remains supported for backward compatibility. Existing integrations will continue to work without modification.