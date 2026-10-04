

# Configure Amazon Bedrock AgentCore Gateway VPC Egress for Gateway Targets
<a name="gateway-vpc-egress"></a>

The AgentCore Gateway service provides secure and controlled egress traffic management for your applications, enabling seamless communication with resources within your Virtual Private Cloud (VPC). This document outlines how egress traffic flows through the AgentCore Gateway to reach VPC resources. You’ll learn about the supported gateway target types (Lambda, API Gateway, and MCP servers via AgentCore Runtime), their configuration requirements, and the authentication methods supported for each target type. This guide covers the security considerations, routing mechanisms, and best practices needed to enable proper egress traffic flow while maintaining network isolation and following the principle of least privilege throughout your architecture.

## MCP
<a name="mcp-target"></a>

AgentCore Gateway supports Model Context Protocol (MCP) servers as target endpoints, providing flexible deployment options to meet various customer requirements. MCP servers can be configured in multiple ways depending on your infrastructure needs and security requirements.

Your MCP targets could be of two types, not hosted on AgentCore, or hosted on AgentCore Runtime or Gateway. We discuss both below.

### MCPs not hosted on AgentCore
<a name="self-hosted-mcp"></a>

AgentCore Gateway supports connecting to self-hosted MCP servers running inside your VPC using private endpoints powered by Amazon VPC Lattice. You can configure a `privateEndpoint` on your gateway target to route traffic privately to your MCP server without exposing it to the public internet.

The following example creates a private MCP server target using managed Lattice:

```
{
  "name": "my-private-mcp-target",
  "privateEndpoint": {
    "managedVpcResource": {
      "vpcIdentifier": "vpc-0abc123def456",
      "subnetIds": ["subnet-0abc123", "subnet-0def456"],
      "endpointIpAddressType": "IPV4",
      "securityGroupIds": ["sg-0abc123def"]
    }
  },
  "targetConfiguration": {
    "mcp": {
      "mcpServer": {
        "endpoint": "https://my-mcp-server.internal.example.com/mcp"
      }
    }
  }
}
```

If you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer, you can specify a `routingDomain` . For more information, see [Route traffic through an intermediate domain](vpc-egress-private-endpoints.md#lattice-vpc-egress-routing-domain).

If your MCP server uses a TLS certificate issued by a private certificate authority, you can configure the gateway to trust that CA directly. For more information, see [Connect to targets that use a private certificate authority](#gateway-private-certificate).

For self-managed Lattice, cross-account setups, and advanced configurations, see [Connect to private resources in your VPC using VPC Lattice](vpc-egress-private-endpoints.md).

### AgentCore Runtime or Gateway
<a name="agentcore-runtime"></a>

AgentCore Runtime provides native support for communicating with resources within your VPC through a managed infrastructure approach. All communication between AgentCore Gateway and AgentCore Runtime stays on the AWS backbone, ensuring your data never traverses the public internet (except for cross-region calls to China datacenters). For more information, see the [Connectivity](https://aws.amazon.com/vpc/faqs/#connectivity) section in the Amazon VPC FAQs. For detailed setup instructions on connecting AgentCore Runtime to your VPC, refer to the [Configure Amazon Bedrock AgentCore Runtime and tools for VPC](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html) 

For outbound authorization from AgentCore Gateway to AgentCore Runtime, two authentication methods are supported: no authorization (not recommended for production use) and OAuth with client credentials grant (for machine-to-machine authentication). When no authorization is configured, the request from AgentCore Gateway to AgentCore Runtime has no auth tokens. This architecture provides a seamless connection pathway while maintaining security isolation. As a security best practice, configure restrictive authentication and authorization permissions for both AgentCore Runtime and AgentCore Gateway, limiting access to only the necessary resources and operations required for your specific use case. To configure an OAuth Identity to be used by AgentCore Gateway for egress and ingress for AgentCore Runtime use the following documents:
+  [Configure an OAuth client](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-oauth-client.html) 
+  [Specify the authorization type and credentials to access the gateway target](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-adding-targets-authorization.html) 
+  [Authenticate and authorize with Inbound Auth and Outbound Auth](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html) 

![Architecture diagram showing AgentCore Gateway cannot connect to Private Link endpoint.](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/gateway-runtime-vpc-access.png)


 **Example CreateGatewayTarget with AgentCore Runtime as a the target** 

The following example shows how to create a gateway target with AgentCore Runtime:

```
POST /gateways/gatewayIdentifier/targets/ HTTP/1.1
Content-type: application/json

    {
    "clientToken": "string",
    "credentialProviderConfigurations": [
      {
         "credentialProvider": {
            "oauthCredentialProvider": {
               "providerArn": "string",
               "scopes": [ "string" ],
               ...
            }
         },
         "credentialProviderType": "OAUTH"
      }
    ],
    "description": "string",
    "metadataConfiguration": {
      "allowedQueryParameters": [ "string" ],
      "allowedRequestHeaders": [ "string" ],
      "allowedResponseHeaders": [ "string" ]
    },
    "name": "string",
    "targetConfiguration": {
      "mcp": {
         "mcpServer": {
            "endpoint": "https://bedrock-agentcore.<region>.amazonaws.com/runtimes/<runtime-id>/invocations?qualifier=DEFAULT&accountId=<account-id>"
         }
      }
    }
}
```

**Note**  
Avoid using a VPC endpoint (VPCE) URL with `privateEndpoint` to prevent an unnecessary extra network hop. Use the direct AgentCore Runtime endpoint instead, with which traffic remains on the AWS backbone.

## Open API target
<a name="openapi-target"></a>

### API Gateway endpoint via Open API Target
<a name="api-gateway-via-openapi"></a>

If your API Gateway can’t be directly added as a target, you can always export the resource as an OpenAPI spec and import the spec into AgentCore Gateway as a OpenAPI target.
+  [Export a REST API from API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-export-api.html) 
+  [OpenAPI schema targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-schema-openapi.html) 

If you have Private REST APIs in API Gateway, follow the instructions here: [Private REST APIs in API Gateway](#private-api-gateway).

### Other endpoints
<a name="other-endpoints"></a>

You can configure Open API targets to reach private endpoints inside your VPC using the `privateEndpoint` configuration. AgentCore Gateway uses Amazon VPC Lattice to establish private connectivity to your endpoint without exposing it to the public internet.

The following example creates a private OpenAPI target using managed Lattice:

```
{
  "name": "my-private-openapi-target",
  "privateEndpoint": {
    "managedVpcResource": {
      "vpcIdentifier": "vpc-0abc123def456",
      "subnetIds": ["subnet-0abc123", "subnet-0def456"],
      "endpointIpAddressType": "IPV4",
      "securityGroupIds": ["sg-0abc123def"]
    }
  },
  "targetConfiguration": {
    "mcp": {
      "openApiSchema": {
        "inlinePayload": "<your OpenAPI spec JSON with server URL pointing to your private endpoint>"
      }
    }
  }
}
```

If you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer, you can specify a `routingDomain` . For more information, see [Route traffic through an intermediate domain](vpc-egress-private-endpoints.md#lattice-vpc-egress-routing-domain).

If your endpoint uses a TLS certificate issued by a private certificate authority, you can configure the gateway to trust that CA directly. For more information, see [Connect to targets that use a private certificate authority](#gateway-private-certificate).

For self-managed Lattice, cross-account setups, and advanced configurations, see [Connect to private resources in your VPC using VPC Lattice](vpc-egress-private-endpoints.md).

**Note**  
The `privateEndpoint` configuration applies to a single domain in your OpenAPI schema. If your schema references multiple server endpoints with different domains, open an [AWS Support case](https://console.aws.amazon.com/support/home) to request support for `privateEndpointOverrides`.

## Smithy target
<a name="smithy-target"></a>

Private endpoint ( `privateEndpoint` ) configuration is not currently supported for Smithy targets. If your Smithy target requires private connectivity, open an [AWS Support case](https://console.aws.amazon.com/support/home) to request support.

## API Gateway
<a name="api-gateway-target"></a>

AgentCore Gateway supports API Gateway as a target type, which can serve as an intermediary layer for accessing VPC resources. AgentCore Gateway specifically supports REST API Gateways configured with regional endpoints only. While direct VPC communication from the Gateway is not currently available (this feature is planned for future release), the gateway communicates with API Gateway over the AWS backbone, ensuring that traffic never traverses the public internet (except for cross-region calls to China datacenters). The API Gateway can then communicate with resources using VPC Link, creating a secure pathway for the AgentCore Gateway to reach internal services while maintaining network isolation.

To implement security best practices, configure your API Gateway to restrict inbound traffic exclusively to the AgentCore Gateway service principal or the configured API key, preventing unauthorized access from other sources. For outbound authorization from AgentCore Gateway to API Gateway, only two authentication methods are supported: IAM-based authentication (using the gateway service role to authenticate with AWS Signature Version 4) and API key authentication (managed by AgentCore Gateway); OAuth-based authorization and Cross Account API Gateways are not supported for API Gateway targets, please use API Gateway endpoint via Open API Target for those. Limit the AgentCore Gateway execution role permissions to invoke only the specific API Gateway endpoint required, rather than granting broad API Gateway access, ensuring that the gateway cannot interact with unintended API resources and maintaining the principle of least privilege throughout your architecture.

 [Amazon API Gateway REST API stages as targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-api-gateway.html) 

### Permissions for API Gateway integration using IAM Auth
<a name="api-gateway-permissions"></a>

 **API Gateway Resource Policy Locked Down to AgentCore Gateway** 

The following resource policy restricts API Gateway access to AgentCore Gateway:

```
{
"Version": "2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "bedrock-agentcore.amazonaws.com"
        },
        "Action": "execute-api:Invoke",
        "Resource": [
          "arn:aws:execute-api:us-west-2:111122223333:rest-api-id/api-stage/*/*"
        ],
        "Condition": {
          "ArnEquals": {
            "aws:SourceArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:gateway/my-gateway-d4jrgkaske"
          }
        }
      }
    ]
}
```

 **AgentCore Gateway Execution Role policy** 

The following policy grants the gateway permission to invoke the API Gateway:

```
{
"Version": "2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "execute-api:Invoke"
        ],
        "Resource": [
          "arn:aws:execute-api:us-west-2:111122223333:abcd123/prod/*/*"
        ]
      }
    ]
}
```

 **AgentCore Gateway Execution Role trust policy** 

The following trust policy allows AgentCore Gateway to assume the execution role:

```
{
"Version": "2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "bedrock-agentcore.amazonaws.com"
        },
        "Action": "sts:AssumeRole",
        "Condition": {
          "StringEquals": {
            "aws:SourceAccount": "111122223333"
          },
          "ArnLike": {
            "aws:SourceArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:gateway/*"
          }
        }
      }
    ]
}
```

#### Private REST APIs in API Gateway
<a name="private-api-gateway"></a>

API Gateway targets with private endpoints are not natively supported. However, you can export your private API Gateway as an OpenAPI schema and use an Open API target with that schema, configured with a `privateEndpoint` . Set the `routingDomain` to your API Gateway VPC endpoint (VPCE) DNS name, and ensure the OpenAPI schema server URL uses the domain that matches your public TLS certificate.

```
{
  "name": "my-private-apigw-target",
  "privateEndpoint": {
    "managedVpcResource": {
      "vpcIdentifier": "vpc-0123456789abcdef0",
      "subnetIds": ["subnet-0123456789abcdef0", "subnet-0abcdef1234567890"],
      "endpointIpAddressType": "IPV4",
      "routingDomain": "<vpce-id>.execute-api.<region>.vpce.amazonaws.com"
    }
  },
  "targetConfiguration": {
    "mcp": {
      "openApiSchema": {
        "inlinePayload": "<OpenAPI spec JSON with server URL matching the public certificate domain for your API Gateway, for example https://<api-id>.execute-api.<region>.amazonaws.com>"
      }
    }
  }
}
```

For more details on private endpoint configuration, see [Connect to private resources in your VPC using VPC Lattice](vpc-egress-private-endpoints.md).
+  [Export a REST API from API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-export-api.html) 
+  [OpenAPI schema targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-schema-openapi.html) 

## Lambda
<a name="lambda-target"></a>

AgentCore Gateway supports Lambda targets as one of it target types, allowing seamless invocation of Lambda functions that can communicate with resources within your VPC. This functionality is available out-of-the-box and requires no additional configuration from customers - the gateway can immediately invoke Lambda functions that have been configured with VPC access to reach your internal resources such as databases, APIs, or other services. To maintain security best practices, it’s strongly recommended to configure the AgentCore Gateway execution role with minimal permissions, specifically limiting it to invoke only the intended Lambda function rather than granting broad Lambda execution permissions. This principle of least privilege ensures that the gateway, or any other caller using the same role, cannot inadvertently invoke unintended Lambda functions, thereby reducing your security attack surface and maintaining strict access controls within your AWS environment.

## Connect to targets that use a private certificate authority
<a name="gateway-private-certificate"></a>

AgentCore Gateway connects outbound to a gateway target over TLS. By default, the gateway trusts only server certificates that a public certificate authority (CA) issues. If your target presents a TLS server certificate that a private (custom) CA issues, you can register that private CA certificate with the target. For more information, see [Prerequisites](#gateway-private-certificate-prereqs) and [Certificate requirements](#gateway-private-certificate-requirements). The gateway then trusts the private CA when it connects to that target. This is the native approach, so you do not need to place an internal Application Load Balancer in front of your target.

You attach a reference to the CA certificate—not the certificate content itself—to an individual target when you create or update the target. This means the certificate content never appears in the API request. Instead, you reference a PEM-encoded CA certificate that you store in either Amazon S3 or AWS Secrets Manager. The gateway fetches, validates, and encrypts the CA certificate when you create or update the target. It then uses the certificate as the trust anchor for outbound TLS to that target.

### Prerequisites
<a name="gateway-private-certificate-prereqs"></a>

Before you register a private CA certificate on a target, ensure the following:
+ The target uses a private endpoint ( `privateEndpoint`) powered by Amazon VPC Lattice. Both managed and self-managed VPC Lattice resources qualify. For more information, see [Connect to private resources in your VPC using VPC Lattice](vpc-egress-private-endpoints.md).
+ The target is one of the following supported types:
  + MCP server targets ( `targetConfiguration.mcp.mcpServer`)
  + OpenAPI targets ( `targetConfiguration.mcp.openApiSchema`)
  + HTTP proxy (passthrough) targets ( `targetConfiguration.http.passthrough`)
+ The CA certificate meets the requirements described in [Certificate requirements](#gateway-private-certificate-requirements).

### Certificate requirements
<a name="gateway-private-certificate-requirements"></a>

The CA certificate that you register must meet the following requirements:
+ It must be a PEM-encoded X.509 certificate.
+ It must be a CA certificate, with the X.509 basic constraints extension set to `CA:TRUE`. The gateway rejects a leaf (end-entity) certificate.
+ It must be within its validity window. The gateway checks certificate validity during target validation on both create and update. Because this validation is asynchronous, an expired certificate causes the target to reach the `FAILED` status (create) or `UPDATE_UNSUCCESSFUL` status (update) rather than causing an immediate error. For more information, see [Validation and behavior](#gateway-private-certificate-validation).
+ The PEM file, including the full certificate chain, must be no larger than 16 KB.
+ If you store the certificate in Amazon S3, the S3 object must be in the same AWS Region as the gateway.

The gateway accepts a PEM file that contains a certificate chain. The gateway records the earliest expiration ( `notAfter`) across the certificates in the file.

### Provide the CA certificate
<a name="gateway-private-certificate-provide"></a>

You reference the CA certificate through the `certificateConfigurations` field on the `CreateGatewayTarget` and `UpdateGatewayTarget` operations. The `certificateConfigurations` array must contain exactly one entry. The entry must set exactly one of the following sources.

 `s3`   
References a PEM CA certificate that you store in Amazon S3.    
 `uri` (required)  
The S3 URI of the certificate object, in the form `s3://bucket/key.pem`.  
 `bucketOwnerAccountId` (optional)  
The 12-digit AWS account ID of the bucket owner. Amazon S3 verifies this value against the bucket owner using the bucket owner condition, so it must match the account that owns the bucket. For more information, see [Verifying bucket ownership with bucket owner condition](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-owner-condition.html) in the AWS Amazon Simple Storage Service User Guide.

 `secretsManager`   
References a PEM CA certificate that you store in AWS Secrets Manager.    
 `secretArn` (required)  
The ARN of the secret. The secret must be a string secret, not a binary secret.

### IAM and KMS permissions
<a name="gateway-private-certificate-permissions"></a>

The gateway fetches the CA certificate using the gateway execution role. Grant the following on that role:
+ The execution role trust policy must allow the AgentCore Gateway service to assume the role.
+ For an Amazon S3 source, grant `s3:GetObject` on the CA certificate object.
+ For an AWS Secrets Manager source, grant `secretsmanager:GetSecretValue` on the secret.
+ If the S3 object or the secret is encrypted with a customer managed key in AWS Key Management Service (AWS KMS), also grant the execution role permission to decrypt with that source key.

After the gateway fetches and validates the certificate, it encrypts the certificate with its own gateway AWS KMS key before it stores the certificate.

### Example requests
<a name="gateway-private-certificate-examples"></a>

The following example creates an MCP server target and references a CA certificate that you store in Amazon S3. The optional `bucketOwnerAccountId` identifies the account that owns the bucket.

```
{
  "name": "my-private-mcp-target",
  "privateEndpoint": {
    "managedVpcResource": {
      "vpcIdentifier": "vpc-0abc123def456",
      "subnetIds": ["subnet-0abc123", "subnet-0def456"],
      "endpointIpAddressType": "IPV4",
      "securityGroupIds": ["sg-0abc123def"]
    }
  },
  "targetConfiguration": {
    "mcp": {
      "mcpServer": {
        "endpoint": "https://my-mcp-server.internal.example.com/mcp"
      }
    }
  },
  "certificateConfigurations": [
    {
      "s3": {
        "uri": "s3://my-ca-bucket/private-ca.pem",
        "bucketOwnerAccountId": "111122223333"
      }
    }
  ]
}
```

The following example creates an OpenAPI target and references a CA certificate that you store in AWS Secrets Manager.

```
{
  "name": "my-private-openapi-target",
  "privateEndpoint": {
    "managedVpcResource": {
      "vpcIdentifier": "vpc-0abc123def456",
      "subnetIds": ["subnet-0abc123", "subnet-0def456"],
      "endpointIpAddressType": "IPV4",
      "securityGroupIds": ["sg-0abc123def"]
    }
  },
  "targetConfiguration": {
    "mcp": {
      "openApiSchema": {
        "inlinePayload": "<your OpenAPI spec JSON with server URL pointing to your private endpoint>"
      }
    }
  },
  "certificateConfigurations": [
    {
      "secretsManager": {
        "secretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:private-ca-AbCdEf"
      }
    }
  ]
}
```

To replace the CA certificate on an existing target, call `UpdateGatewayTarget`. You specify the gateway and target identifiers as path parameters ( `PUT /gateways/{gatewayIdentifier}/targets/{targetId}`); the request body contains the target configuration. The following example replaces the certificate with one stored in AWS Secrets Manager.

```
{
  "name": "my-private-mcp-target",
  "privateEndpoint": {
    "managedVpcResource": {
      "vpcIdentifier": "vpc-0abc123def456",
      "subnetIds": ["subnet-0abc123", "subnet-0def456"],
      "endpointIpAddressType": "IPV4",
      "securityGroupIds": ["sg-0abc123def"]
    }
  },
  "targetConfiguration": {
    "mcp": {
      "mcpServer": {
        "endpoint": "https://my-mcp-server.internal.example.com/mcp"
      }
    }
  },
  "certificateConfigurations": [
    {
      "secretsManager": {
        "secretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:private-ca-AbCdEf"
      }
    }
  ]
}
```

To remove the CA certificate and revert the target to public-CA trust, call `UpdateGatewayTarget` and omit `certificateConfigurations` from the request. You specify the gateway and target identifiers as path parameters ( `PUT /gateways/{gatewayIdentifier}/targets/{targetId}`); the request body contains the target configuration. The following example removes the certificate by omitting `certificateConfigurations`.

```
{
  "name": "my-private-mcp-target",
  "privateEndpoint": {
    "managedVpcResource": {
      "vpcIdentifier": "vpc-0abc123def456",
      "subnetIds": ["subnet-0abc123", "subnet-0def456"],
      "endpointIpAddressType": "IPV4",
      "securityGroupIds": ["sg-0abc123def"]
    }
  },
  "targetConfiguration": {
    "mcp": {
      "mcpServer": {
        "endpoint": "https://my-mcp-server.internal.example.com/mcp"
      }
    }
  }
}
```

### Validation and behavior
<a name="gateway-private-certificate-validation"></a>

Most certificate validation is asynchronous. When you create or update a target with a certificate, the gateway accepts the request and then validates the certificate as part of the target workflow. If validation succeeds, the target reaches the `READY` status and can receive traffic. If validation fails, the target reaches the `FAILED` status (for create) or the `UPDATE_UNSUCCESSFUL` status (for update), and the `statusReasons` field describes the problem. Common reasons include the following:
+ The target does not use a private endpoint.
+ The target type is not supported.
+ The gateway cannot find the S3 object or the secret.
+ The certificate is expired, is not a CA certificate, or exceeds the size limit.

Only the following checks are synchronous, and the gateway rejects the request immediately when one of them fails:
+ Each `certificateConfigurations` entry sets exactly one of `s3` or `secretsManager`.
+ The field formats (S3 URI, secret ARN, and account ID) are valid.

A failed update does not replace the certificate that the target is already using. The target continues to serve requests with its existing, working certificate.

### Certificate revocation
<a name="gateway-private-certificate-revocation"></a>

AgentCore Gateway does not perform certificate revocation checking. It does not check certificate revocation lists (CRLs), and it does not use the Online Certificate Status Protocol (OCSP). The gateway trusts any server certificate that chains to the configured private CA, is within its validity window, and matches the target host. The gateway continues to trust a certificate that the CA revokes until that certificate expires.

To stop trusting a revoked certificate, update the target’s trust material. You can do this in one of the following ways:
+ Call `UpdateGatewayTarget` and provide a new CA certificate (PEM) in `certificateConfigurations` that does not include, or no longer chains to, the revoked certificate. For an example, see the request that replaces the certificate in [Example requests](#gateway-private-certificate-examples).
+ Call `UpdateGatewayTarget` and omit `certificateConfigurations` to remove the private CA. This reverts the target to public-CA trust. For an example, see the request that removes the certificate in [Example requests](#gateway-private-certificate-examples).

Even after you update the trust material, existing open connections can keep using the previous certificate until the gateway recycles them. For more information, see [Runtime behavior and troubleshooting](#gateway-private-certificate-troubleshooting).

### Monitor certificate expiry
<a name="gateway-private-certificate-expiry-metric"></a>

AgentCore Gateway emits an Amazon CloudWatch metric named `EarliestCertificateDaysToExpiry` for targets that use a private certificate authority. The gateway emits this metric only for a target that has a private certificate configured. The metric reports the whole number of days remaining until the earliest expiration ( `notAfter`) among the certificates in the configured CA. A negative value means the certificate has already expired.

**Certificate expiry makes the target unreachable**  
When the configured certificate expires, the gateway can no longer complete the outbound TLS handshake to the target. The target becomes unreachable, and tool invocations to it fail. For more information about handshake failures, see [Runtime behavior and troubleshooting](#gateway-private-certificate-troubleshooting).

We recommend that you monitor the `EarliestCertificateDaysToExpiry` metric and create a CloudWatch alarm that triggers as the value approaches zero. This alarm gives you time to replace the certificate before it expires. To replace the certificate, call `UpdateGatewayTarget` with a new certificate. For an example, see the request that replaces the certificate in [Example requests](#gateway-private-certificate-examples). To stop trusting a revoked certificate, see [Certificate revocation](#gateway-private-certificate-revocation).

### Runtime behavior and troubleshooting
<a name="gateway-private-certificate-troubleshooting"></a>

At invocation time, the target’s server certificate must be issued by the private CA that you configured, must be within its validity window, and its hostname must match the target host. The subject alternative name (SAN) of the target server certificate must match the target host.

If the server certificate is not issued by the configured private CA, is expired, or does not match the target host, the TLS handshake fails. The gateway returns a client-side configuration error, not a service fault. To resolve the error, verify that the target server certificate is issued by the registered private CA, is current, and includes a SAN that matches the target host.

AgentCore Gateway reuses established TLS connections to a target. The gateway validates certificate trust and validity during the TLS handshake. It does not revalidate the certificate on every request that it sends over an already-open connection. A connection that the gateway opens while the certificate is valid can keep serving requests for the lifetime of that connection. This lifetime is up to 900 seconds (15 minutes). The connection can keep serving requests even if the certificate expires during that window. When the gateway recycles the connection at the end of its lifetime, it performs a new TLS handshake. That handshake revalidates the target against the current certificate. For the related gateway invocation timeout, see [Service quotas](bedrock-agentcore-limits.md#gateway-quotas).

**Certificate changes take effect gradually**  
A certificate change can take up to 900 seconds (15 minutes) to fully take effect for in-flight connections. This applies after a certificate expires, or after you rotate, replace, or remove a certificate by using `UpdateGatewayTarget`. Existing open connections can keep using the previous certificate and trust material until the gateway recycles them. New connections use the current certificate immediately.

## Private identity providers
<a name="private-idp"></a>

AgentCore now supports connecting to private OAuth identity providers for both inbound JWT authorization and outbound OAuth credential providers. This enables you to use self-hosted IdPs such as Keycloak, PingFederate, or other OIDC-compliant authorization servers running inside your VPC without exposing them to the public internet.

For detailed configuration instructions, see [Connect to private identity providers in your VPC](identity-private-idp.md).

Alternatively, you can use an interceptor Lambda function for inbound authentication and override the Authorization header in the interceptor Lambda for use with outbound auth:
+  [Gateway interceptors](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors.html) 
+  [Specify the authorization type and credentials to access the gateway target](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-adding-targets-authorization.html) 

## Limitations and considerations
<a name="gateway-vpc-access-limitations"></a>
+  **Inbound authorization required** : Gateway targets configured with a `privateEndpoint` cannot use `NO_AUTH` as the inbound authorizer type unless an interceptor Lambda is configured on the gateway.

For additional limitations related to cross-account connectivity and DNS TTL configuration, see [Limitations and considerations](vpc-egress-private-endpoints.md#lattice-vpc-egress-limitations) in [Connect to private resources in your VPC using VPC Lattice](vpc-egress-private-endpoints.md).