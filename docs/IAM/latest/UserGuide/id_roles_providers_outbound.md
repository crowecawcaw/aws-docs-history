

# Federating AWS Identities to external services
<a name="id_roles_providers_outbound"></a>

IAM outbound identity federation enables your AWS workloads to securely access external services without storing long-term credentials. Your AWS workloads can request short-lived JSON Web Tokens (JWTs) from AWS Security Token Service (AWS STS) by calling the [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) API. These tokens are cryptographically signed, publicly verifiable and contain a comprehensive set of claims that assert your AWS workload's identity to external services. You can use these tokens with a wide range of third-party cloud providers, SaaS platforms, and self-hosted applications. External services verify the token's authenticity using AWS's verification keys published at well-known endpoints and use the information in the tokens to make authentication and authorization decisions.

Outbound identity federation eliminates the need to store long-term credentials such as API keys or passwords in your application code or environment variables, improving your security posture. You can control access to token generation and enforce token properties such as signing algorithms, permitted audiences and duration using IAM policies. All token requests are logged in AWS , providing complete audit trails for security monitoring and compliance reporting. You can also customize tokens with tags that appear as custom claims, enabling external services to implement fine-grained, attribute-based access control.

For instructions on setting up outbound federation, see [Getting started with outbound identity federation](id_roles_providers_outbound_getting_started.md). For more information about token contents, see [Understanding token claims](id_roles_providers_outbound_token_claims.md). For instructions on controlling which workloads can request tokens, see [Controlling access with IAM policies](id_roles_providers_outbound_policies.md).

## Common use cases
<a name="outbound-federation-use-cases"></a>

Using outbound identity federation, your AWS workloads can securely:
+ Access resources and services in external cloud providers. For example, a Lambda function processing data can write results to an external cloud provider's storage service or query their database.
+ Integrate with external software-as-a-service (SaaS) providers for analytics, data processing, monitoring etc. For example, your Lambda functions can send metrics to observability platforms.
+ Authenticate with your own applications hosted on AWS, external cloud providers or on-premises data centers, enabling secure hybrid and multi-cloud architectures. For example, your AWS workloads can interact with containerized applications running in your on-premises Kubernetes cluster.

## How It Works
<a name="outbound-federation-how-it-works"></a>

![Authentication flow between Lambda function, Security Token Service, External Service, and OIDC Issuer URL Discovery Endpoint.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/outbound-use-cases.png)


1. The Lambda function calls the [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) API to request a JSON Web Token (JWT) from AWS Security Token Service (AWS STS).

1. AWS STS validates the request and returns a signed JWT to the Lambda function.

1. The Lambda function sends the JWT to the external service.

1. The external service extracts the issuer URL from the token, verifies it matches a known trusted issuer, and fetches AWS's verification keys and metadata from the OIDC discovery endpoint.

1. The external service uses the verification keys to verify the token's signature and validates claims such as expiration time, subject and audience.

1. After successful validation, the external service grants access to the Lambda function.