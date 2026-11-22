

# Connect to private identity providers

Amazon Bedrock AgentCore Identity supports connecting to OAuth 2.0 identity providers (IdPs) hosted inside your AWS VPC, such as self-hosted Keycloak, PingFederate, or other OIDC-compliant authorization servers, without exposing them to the public internet. This enables you to use private IdPs for both inbound JWT authorization with AgentCore Runtime and AgentCore Gateway as well as outbound OAuth2 credential providers.

Private connectivity to VPC hosted IdPs is established using [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) resource gateways and resource configurations, following the same pattern used by [AgentCore Gateway VPC egress](gateway-vpc-egress.md). AgentCore Identity uses the `AWSServiceRoleForBedrockAgentCoreIdentity` service-linked role to create and manage VPC Lattice resources in your account for private connectivity to your IdP endpoints.

**Important**  
AgentCore supports two VPC Lattice connectivity modes — **managed Lattice** (simpler, AgentCore handles resource lifecycle) and **self-managed Lattice** (advanced, with cross-account support and full governance visibility). Each mode has different trade-offs for complexity, cost, and control. For a detailed comparison with pros and cons, see [Supported VPC egress modes](vpc-egress-private-endpoints.md#lattice-vpc-egress-compare-modes).

## Use cases
<a name="private-idp-use-cases"></a>

Private identity providers are common in enterprise environments where organizations:
+ Run self-hosted authorization servers inside their VPC for compliance or data residency requirements
+ Use private IdP discovery endpoints that are not publicly accessible
+ Require all authentication traffic to stay within the AWS network without traversing the public internet

## Inbound JWT authorization with a private IdP
<a name="private-idp-inbound-auth"></a>

When you configure inbound JWT authorization for AgentCore Runtime or AgentCore Gateway, the authorizer uses the OpenID Connect (OIDC) or OAuth 2.0 Authorization Server Metadata (RFC 8414) discovery URL to fetch the IdP’s public keys (JWKS) and validate incoming JWT tokens. If your IdP is hosted inside a VPC and the discovery URL is not publicly accessible, you must configure a private endpoint so that AgentCore Identity can reach the IdP’s discovery and JWKS endpoints.

### Configure inbound authorization with a private IdP
<a name="private-idp-inbound-config"></a>

To configure inbound JWT authorization with a private IdP, include the `privateEndpoint` block in the authorizer configuration when creating or updating your AgentCore Runtime or Gateway.

 **Example: CreateAgentRuntime with private IdP for inbound auth** 

```json
{
  "agentRuntimeName": "my-runtime",
  "authorizerConfiguration": {
    "customJWTAuthorizer": {
      "discoveryUrl": "https://idp.internal.example.com/.well-known/openid-configuration",
      "allowedAudiences": [
        "my-agent-audience"
      ],
      "allowedClients": [
        "my-client-id"
      ],
      "privateEndpoint": {
        "managedVpcResource": {
          "vpcIdentifier": "vpc-0abc123def456",
          "subnetIds": [
            "subnet-0abc123",
            "subnet-0def456"
          ],
          "endpointIpAddressType": "IPV4",
          "securityGroupIds": [
            "sg-0abc123def"
          ]
        }
      }
    }
  }
}
```

 **Example: CreateGateway with private IdP for inbound auth** 

```json
{
  "name": "my-gateway",
  "authorizerConfiguration": {
    "customJWTAuthorizer": {
      "discoveryUrl": "https://idp.internal.example.com/.well-known/openid-configuration",
      "allowedAudiences": [
        "my-gateway-audience"
      ],
      "allowedClients": [
        "my-client-id"
      ],
      "privateEndpoint": {
        "managedVpcResource": {
          "vpcIdentifier": "vpc-0abc123def456",
          "subnetIds": [
            "subnet-0abc123",
            "subnet-0def456"
          ],
          "endpointIpAddressType": "IPV4",
          "securityGroupIds": [
            "sg-0abc123def"
          ]
        }
      }
    }
  }
}
```

For self-managed Lattice, replace `managedVpcResource` with `selfManagedLatticeResource`:

 **Example: CreateAgentRuntime with self-managed Lattice for inbound auth** 

```json
{
  "agentRuntimeName": "my-runtime",
  "authorizerConfiguration": {
    "customJWTAuthorizer": {
      "discoveryUrl": "https://idp.internal.example.com/.well-known/openid-configuration",
      "allowedAudiences": [
        "my-agent-audience"
      ],
      "allowedClients": [
        "my-client-id"
      ],
      "privateEndpoint": {
        "selfManagedLatticeResource": {
          "resourceConfigurationIdentifier": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-abc123"
        }
      }
    }
  }
}
```

 **Example: CreateGateway with self-managed Lattice for inbound auth** 

```json
{
  "name": "my-gateway",
  "authorizerConfiguration": {
    "customJWTAuthorizer": {
      "discoveryUrl": "https://idp.internal.example.com/.well-known/openid-configuration",
      "allowedAudiences": [
        "my-gateway-audience"
      ],
      "allowedClients": [
        "my-client-id"
      ],
      "privateEndpoint": {
        "selfManagedLatticeResource": {
          "resourceConfigurationIdentifier": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-abc123"
        }
      }
    }
  }
}
```

## Outbound OAuth credential provider with a private IdP
<a name="private-idp-outbound-auth"></a>

When you configure an outbound OAuth2 credential provider that uses a private IdP, AgentCore Identity needs to reach the IdP’s token endpoint to exchange authorization codes for access tokens or to perform client credentials grants. If the IdP’s token endpoint is hosted inside your VPC, you must configure a private endpoint on the credential provider.

### Configure outbound credential provider with a private IdP
<a name="private-idp-outbound-config"></a>

To configure an outbound OAuth credential provider with a private IdP, include the `privateEndpoint` block when creating the credential provider using a custom provider with manual configuration.

 **Example: Create an OAuth credential provider with a private IdP** 

```json
{
  "name": "my-private-idp-provider",
  "credentialProviderVendor": "CustomOauth2",
  "oauth2ProviderConfigInput": {
    "customOauth2ProviderConfig": {
      "oauthDiscovery": {
        "authorizationServerMetadata": {
          "issuer": "https://idp.internal.example.com/realms/my-realm",
          "authorizationEndpoint": "https://idp.internal.example.com/realms/my-realm/protocol/openid-connect/auth",
          "tokenEndpoint": "https://idp.internal.example.com/realms/my-realm/protocol/openid-connect/token"
        }
      },
      "clientId": "my-client-id",
      "clientSecret": "<client-secret>",
      "privateEndpoint": {
        "managedVpcResource": {
          "vpcIdentifier": "vpc-0abc123def456",
          "subnetIds": [
            "subnet-0abc123",
            "subnet-0def456"
          ],
          "endpointIpAddressType": "IPV4",
          "securityGroupIds": [
            "sg-0abc123def"
          ]
        }
      }
    }
  }
}
```

For self-managed Lattice, replace `managedVpcResource` with `selfManagedLatticeResource`:

```json
{
  "name": "my-private-idp-provider",
  "credentialProviderVendor": "CustomOauth2",
  "oauth2ProviderConfigInput": {
    "customOauth2ProviderConfig": {
      "oauthDiscovery": {
        "authorizationServerMetadata": {
          "issuer": "https://idp.internal.example.com/realms/my-realm",
          "authorizationEndpoint": "https://idp.internal.example.com/realms/my-realm/protocol/openid-connect/auth",
          "tokenEndpoint": "https://idp.internal.example.com/realms/my-realm/protocol/openid-connect/token"
        }
      },
      "clientId": "my-client-id",
      "clientSecret": "<client-secret>",
      "privateEndpoint": {
        "selfManagedLatticeResource": {
          "resourceConfigurationIdentifier": "arn:aws:vpc-lattice:us-east-1:444455556666:resourceconfiguration/rcfg-abc123"
        }
      }
    }
  }
}
```

## Connect to identity providers that use a private certificate authority
<a name="identity-private-certificate"></a>

For outbound OAuth requests, Amazon Bedrock AgentCore Identity trusts TLS server certificates issued by public certificate authorities (CAs) by default. If your private identity provider uses a certificate issued by your organization’s CA, you can configure a custom OAuth2 credential provider to trust that CA. You can connect directly to the private IdP without placing an Application Load Balancer with a public certificate in front of it.

Provide a reference to a CA certificate stored in Amazon S3 or AWS Secrets Manager. You provide the S3 URI or secret ARN, not the certificate contents or a private key. AgentCore Identity retrieves and validates the certificate when you create or update the configuration.

### Prerequisites
<a name="identity-private-certificate-prerequisites"></a>

Before you configure a private CA certificate, ensure the following:
+ Configure a private endpoint for your IdP, using either managed or self-managed VPC Lattice connectivity. The certificate establishes TLS trust; the private endpoint provides network access.
+ Use HTTPS for the IdP endpoints that AgentCore Identity contacts.
+ Store the CA certificate in the same AWS Region as the AgentCore resource.
+ Grant the IAM identity that creates or updates the configuration permission to read the certificate source. For more information about certificate access permissions, see [Certificate access permissions](#identity-private-certificate-permissions).

### Certificate requirements
<a name="identity-private-certificate-requirements"></a>

Use a Privacy-Enhanced Mail (PEM)-encoded X.509 CA certificate with the basic constraints extension set to `CA:TRUE`. Do not provide the IdP’s leaf server certificate or a private key. You can concatenate multiple PEM certificate blocks into one object or secret. Every certificate in the bundle must be within its validity window. The complete PEM bundle must be no larger than 16,384 bytes.

Store the certificate as PEM text. For Secrets Manager, use a plaintext string secret. Key/value (JSON) and binary secrets are not supported.

The IdP’s server certificate must be valid, chain to the configured CA certificates, and match the endpoint hostname. Configuring a private CA does not disable hostname verification.

### Provide the CA certificate
<a name="identity-private-certificate-sources"></a>

Set `oauth2ProviderConfigInput.customOauth2ProviderConfig.certificateConfigurations` on `CreateOauth2CredentialProvider` or `UpdateOauth2CredentialProvider`. The list must contain exactly one entry. That entry identifies one certificate source, which can contain a bundle of CA certificates. Set either `s3` or `secretsManager`, not both.

 `s3`   
References an S3 object containing the PEM certificate.    
 `uri` (required)  
The S3 URI, for example `s3://amzn-s3-demo-bucket/ca/root-ca.pem`.  
 `bucketOwnerAccountId` (optional)  
The 12-digit AWS account ID that owns the bucket. If omitted, AgentCore Identity uses the customer account that owns the configuration. If the bucket belongs to another account, specify that account ID and grant the caller access to the object. Amazon S3 checks that the specified account owns the bucket.

 `secretsManager`   
References a plaintext Secrets Manager secret containing the PEM certificate.    
 `secretArn` (required)  
The ARN of the secret.

### Certificate access permissions
<a name="identity-private-certificate-permissions"></a>

AgentCore Identity reads the certificate on behalf of the IAM identity that creates or updates the configuration. Grant that identity the applicable permission:
+  `s3:GetObject` on the certificate object for an S3 source.
+  `secretsmanager:GetSecretValue` on the certificate secret for a Secrets Manager source.

If the object or secret is encrypted with a customer managed AWS KMS key, the caller also needs permission to decrypt with that key. For cross-account access, the resource policy and key policy must permit access as applicable.

The service-linked role used to manage private networking does not replace these certificate-read permissions.

### Configure an OAuth client’s CA certificate in the console
<a name="identity-private-certificate-console"></a>

1. Follow the instructions in [Add OAuth client using custom provider](identity-add-oauth-client-custom.md).

1. In **Additional configurations**, configure **VPC security** using a managed or self-managed private endpoint.

1. Under **Root certificate authority**, choose **Add root certificate**.

1. Choose Amazon S3 or Secrets Manager as the certificate source. Provide the S3 URI and optional bucket owner account ID, or choose the secret containing the PEM certificate.

1. Choose **Apply** to add the certificate configuration.

1. Choose **Add OAuth Client**.

### Example requests
<a name="identity-private-certificate-examples"></a>

The following `CreateOauth2CredentialProvider` request configures a custom OAuth provider with a self-managed private endpoint and a CA certificate stored in Amazon S3. Replace the example identifiers and client credentials with your own values. For managed connectivity, use the `managedVpcResource` configuration shown in [Configure outbound credential provider with a private IdP](#private-idp-outbound-config).

```json
{
  "name": "my-private-idp-provider",
  "credentialProviderVendor": "CustomOauth2",
  "oauth2ProviderConfigInput": {
    "customOauth2ProviderConfig": {
      "oauthDiscovery": {
        "authorizationServerMetadata": {
          "issuer": "https://idp.internal.example.com",
          "authorizationEndpoint": "https://idp.internal.example.com/authorize",
          "tokenEndpoint": "https://idp.internal.example.com/token"
        }
      },
      "clientId": "my-client-id",
      "clientSecret": "<client-secret>",
      "privateEndpoint": {
        "selfManagedLatticeResource": {
          "resourceConfigurationIdentifier": "arn:aws:vpc-lattice:us-east-1:111122223333:resourceconfiguration/rcfg-0123456789abcdef0"
        }
      },
      "certificateConfigurations": [
        {
          "s3": {
            "uri": "s3://amzn-s3-demo-bucket/ca/root-ca.pem",
            "bucketOwnerAccountId": "111122223333"
          }
        }
      ]
    }
  }
}
```

For a Secrets Manager source, replace the `certificateConfigurations` value with the following list:

```json
[
  {
    "secretsManager": {
      "secretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:private-ca-AbCdEf"
    }
  }
]
```

### Update, rotate, or remove a CA certificate
<a name="identity-private-certificate-update"></a>

AgentCore Identity stores the certificate content retrieved during configuration. Changing the contents of the S3 object or secret does not automatically update the provider’s trust configuration.

To rotate the CA certificate, update the source object or secret, then call `UpdateOauth2CredentialProvider` with the provider’s name, vendor, and custom provider configuration, including `certificateConfigurations`. You can reuse the same source reference. The update retrieves the certificate content again. Keep the other provider settings that you want to retain in the request.

**Important: Certificate configuration removal**  
When you update a custom OAuth provider, omitting `certificateConfigurations` removes its saved CA configuration. Include the certificate reference when an update should retain private CA trust, even if the update changes another provider setting.

To remove the CA certificate, call `UpdateOauth2CredentialProvider` with the required provider configuration and omit `certificateConfigurations`. The provider returns to default public-CA trust. Do not use an empty list: a supplied `certificateConfigurations` list must contain exactly one entry. A provider whose endpoints still use privately issued certificates cannot connect using public-CA trust alone.

### Validation and troubleshooting
<a name="identity-private-certificate-troubleshooting"></a>

AgentCore Identity retrieves and validates the certificate as part of configuring the provider. Check the provider’s status after creating or updating it before requesting tokens. If configuration fails, verify the following:
+ The certificate source exists and is in the correct AWS Region.
+ The configuring IAM identity can read the source and decrypt it when applicable.
+ The S3 bucket owner account ID matches the bucket’s owner.
+ The source contains valid PEM-encoded CA certificates and is within the size limit.
+ The provider uses a private endpoint and HTTPS.

At runtime, a configured private CA supplies the trust certificates for the provider’s TLS connections. AgentCore Identity does not fall back to public-CA trust if private-CA validation fails. If a TLS connection fails, check the server certificate’s validity, chain, and hostname, as well as private endpoint routing and security groups. When you rotate a certificate, update the provider configuration as described in [Update, rotate, or remove a CA certificate](#identity-private-certificate-update).

## Prerequisites
<a name="private-idp-prerequisites"></a>

Before configuring a private identity provider, ensure the following:
+ Your identity provider is running and accessible within your VPC.
+ The IdP’s discovery endpoint ( `/.well-known/openid-configuration` or `/.well-known/oauth-authorization-server` ), JWKS endpoint, and token endpoint are reachable from the specified subnets.
+ Your security groups allow inbound traffic on the port used by your IdP (typically port 443 for HTTPS).
+ For managed Lattice, your IAM principal must have the `iam:CreateServiceLinkedRole` permission so that AgentCore can create the Identity Network service-linked role on your behalf. For the required IAM policy, see [Identity Network service-linked role](service-linked-roles.md#identity-network-service-linked-role).
+ For managed Lattice, your IAM principal needs the following Amazon EC2 permission: `ec2:CreateNetworkInterface` as well.

## Service-linked role for private identity providers
<a name="private-idp-slr"></a>

When you configure a private endpoint for an identity provider, AgentCore Identity uses the `AWSServiceRoleForBedrockAgentCoreIdentity` service-linked role to manage the connectivity to your VPC hosted IdP. This role is created automatically the first time you configure a managed private endpoint for an identity provider, provided your IAM principal has the required `iam:CreateServiceLinkedRole` permission.

For the full policy document and instructions for creating, editing, and deleting this role, see [Identity Network service-linked role](service-linked-roles.md#identity-network-service-linked-role).

## Limitations and considerations
<a name="private-idp-limitations"></a>
+  **Discovery URL must be HTTPS** : The IdP’s discovery URL must use HTTPS. HTTP endpoints are not supported.
+  **Private certificates** : For outbound custom OAuth providers, configure a CA certificate reference as described in [Connect to identity providers that use a private certificate authority](#identity-private-certificate).
+  **Cross-account** : Cross-account private IdP connectivity requires the self-managed Lattice option.

For additional limitations related to VPC Lattice connectivity, see [Limitations and considerations](vpc-egress-private-endpoints.md#lattice-vpc-egress-limitations) in [Connect to private resources in your VPC using VPC Lattice](vpc-egress-private-endpoints.md).