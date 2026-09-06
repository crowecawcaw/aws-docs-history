

# Supported Inbound Authorization types
<a name="registry-supported-auth-types"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

Inbound authorization allows registry administrators to control which consumers can discover records in the registry — search, browse the approved-record catalog, invoke the registry’s MCP endpoint — via the AWS CLI, SDK, console, or an MCP-compatible client. Administrators can configure inbound authorization using IAM or JWT.

## IAM-based authorization
<a name="registry-iam-auth"></a>

IAM-based authorization uses the caller’s AWS IAM credentials (SigV4 signing) for authorization. Use this option if your consumers already have AWS IAM access.

### Setting up IAM-based authorization
<a name="registry-iam-auth-setup"></a>

1. Create or use an existing IAM identity for your registry consumers.

1. Create an identity-based IAM policy with the following permissions:

   1.  `agent-registry:SearchDiscoverableRegistryRecords` 

   1.  `agent-registry:ListDiscoverableRegistryRecords` 

   1.  `agent-registry:GetDiscoverableRegistryRecord` 

   1.  `agent-registry:InvokeRegistryMcp` 

   1. To restrict a consumer to specific registries in the same AWS account, list the target registry ARN(s) in the `Resource` field of the identity-based policy. Omit this scope (or use `"Resource": "*"`) to grant access to every registry in the account.

1. Attach the policy to the consumer identity (IAM User or Role).

### Example policy
<a name="registry-iam-auth-example"></a>

**Example**  

```
{
"Version": "2012-10-17",		 	 	 
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "agent-registry:SearchDiscoverableRegistryRecords",
      "agent-registry:ListDiscoverableRegistryRecords",
      "agent-registry:GetDiscoverableRegistryRecord",
      "agent-registry:InvokeRegistryMcp"
    ],
    "Resource": "arn:aws:agent-registry:us-east-1:123456789012:registry/<YOUR_REGISTRY_ID>"
  }]
}
```

```
{
"Version": "2012-10-17",		 	 	 
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "bedrock-agentcore:SearchRegistryRecords",
      "bedrock-agentcore:InvokeRegistryMcp"
    ],
    "Resource": "arn:aws:bedrock-agentcore:us-east-1:123456789012:registry/<YOUR_REGISTRY_ID>"
  }]
}
```

## JWT-based authorization
<a name="registry-jwt-auth"></a>

JSON Web Token (JWT) authorization lets consumers authorize using tokens from your organization’s identity provider — such as Amazon Cognito, Okta, Microsoft Azure AD, Auth0, or any OAuth 2.0-compatible provider. This is useful when you want to make the registry accessible to a broad set of users through existing corporate credentials, without provisioning individual IAM access.

### Set up a default JWT with Amazon Cognito
<a name="registry-jwt-cognito"></a>

When you create a registry through the console and select JWT authorization, you can choose the quick create option. AWS Agent Registry creates an Amazon Cognito user pool and configures the JWT authorization automatically. No additional setup is required.

### Set up a JWT manually with your own identity provider
<a name="registry-jwt-manual"></a>

If you have an existing identity provider, configure JWT authorization manually. You need:
+  **Discovery URL** (required) — The OpenID Connect discovery URL from your identity provider (for example, `https://cognito-idp.us-east-1.amazonaws.com/YOUR_POOL_ID/.well-known/openid-configuration` ). AWS Agent Registry uses this URL to fetch the login, token, and verification settings.

You must also configure at least one of the following JWT authorization rules:
+  **Allowed audiences** — Permitted values for the `aud` claim. An audience claim specifies which resource server the token is intended for, preventing token reuse across different APIs.
+  **Allowed clients** — Permitted values for the `client_id` claim. A client ID is a unique identifier for the application requesting access tokens.
+  **Allowed scopes** — Required permission scopes. At least one scope in the incoming token must match one of the configured values.
+  **Custom claims** — Rules that match specific claims in the incoming token against predefined values. For each rule, specify the claim name, value type (STRING or STRING\_ARRAY), and the required match value.

If you configure more than one authorization rule, AWS Agent Registry verifies all of them.

## Changing Authorization type
<a name="registry-changing-auth-type"></a>

You cannot change authorization Type after a Registry has been created. Additionally, for registries setup with JWT based authorization, the Discovery URL cannot be edited after the Registry has been created.

## Authorization scope
<a name="registry-auth-scope"></a>

The authorization type you configure only affects the data plane APIs — SearchDiscoverableRegistryRecords, ListDiscoverableRegistryRecords, BatchGetDiscoverableRegistryRecord, and InvokeRegistryMcp. All control plane APIs (CreateRegistry, CreateRegistryRecord, UpdateRegistryRecordStatus, and others) always require IAM authorization, regardless of the registry’s authorization setting.