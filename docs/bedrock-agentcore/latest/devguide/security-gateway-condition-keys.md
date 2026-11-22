

# Use IAM condition keys with Amazon Bedrock AgentCore Gateway

Use Amazon Bedrock AgentCore-specific condition keys to control how you create, configure, and invoke gateways in your organization. Gateway and gateway target condition keys apply to control plane operations. Invocation condition keys apply to the `InvokeGateway` operation. Use the gateway and gateway target keys in identity-based policies and service control policies (SCPs). Use the invocation keys in resource-based policies and resource control policies (RCPs). For more information about RCPs, see [Resource control policies for Amazon Bedrock AgentCore](resource-control-policies.md).

For example, you can:
+ Require that all gateways use a specific identity provider for authentication.
+ Restrict what types of targets can be created.
+ Enforce that targets use specific credential provider types.
+ Require that gateway targets connect through approved subnets and security groups.
+ Allow gateway invocations only with JSON Web Tokens (JWTs) that include specific claims.

A condition key is present in the request context only when the request includes the value that the key describes. For example, `bedrock-agentcore:KmsKeyArn` is absent from a `CreateGateway` request that does not specify a KMS key. To write policies that handle absent keys, see [Handle condition keys that are absent from a request](#gateway-condition-keys-absent).

## Gateway condition keys
<a name="gateway-condition-keys"></a>

The following condition keys apply to the `CreateGateway` and `UpdateGateway` operations.


| Condition key | Type | API operations | Description | 
| --- | --- | --- | --- | 
|  `bedrock-agentcore:DiscoveryUrl`  | String |  `CreateGateway`, `UpdateGateway`  | Filters access by the discovery URL configured on the gateway. Use this to ensure gateways use a specific identity provider. | 
|  `bedrock-agentcore:KmsKeyArn`  | String |  `CreateGateway`, `UpdateGateway`  | Filters access by the KMS key ARN used to encrypt gateway resources. | 
|  `bedrock-agentcore:PolicyEngineArn`  | String |  `CreateGateway`, `UpdateGateway`  | Filters access by the ARN of the policy engine configuration associated with the gateway. | 
|  `bedrock-agentcore:PolicyEngineMode`  | String |  `CreateGateway`, `UpdateGateway`  | Filters access by the mode of the policy engine configuration associated with the gateway. Valid values are `LOG_ONLY` and `ENFORCE`. | 
|  `bedrock-agentcore:ProtocolType`  | String |  `CreateGateway`, `UpdateGateway`  | Filters access by the protocol type of the gateway. The valid value is `MCP`. | 
|  `bedrock-agentcore:GatewayAuthorizerType`  | String |  `CreateGateway`, `UpdateGateway`  | Filters access by the authorizer type configured on the gateway. Valid values are `AUTHENTICATE_ONLY`, `AWS_IAM`, `CUSTOM_JWT`, and `NONE`. | 

## Gateway target condition keys
<a name="gateway-target-condition-keys"></a>

The following condition keys apply to the `CreateGatewayTarget` and `UpdateGatewayTarget` operations.


| Condition key | Type | API operations | Description | 
| --- | --- | --- | --- | 
|  `bedrock-agentcore:McpTargetConfigurationType`  | String |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the type of an MCP target. Valid values include `apiGateway`, `lambda`, `mcpServer`, `openApiSchema`, `smithyModel`, and `connector`. | 
|  `bedrock-agentcore:HttpTargetConfigurationType`  | String |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the type of an HTTP target. Valid values include `agentcoreRuntime`, `passthrough`, and `connector`. | 
|  `bedrock-agentcore:InferenceTargetConfigurationType`  | String |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the type of an inference target. Valid values include `connector` and `provider`. | 
|  `bedrock-agentcore:CredentialProviderType`  | String |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the credential provider type configured on the target. Valid values include `GATEWAY_IAM_ROLE`, `OAUTH`, `API_KEY`, `CALLER_IAM_CREDENTIALS`, and `JWT_PASSTHROUGH`. | 
|  `bedrock-agentcore:PrivateEndpointType`  | String |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the private endpoint type of a target. Valid values include `managedVpcResource` and `selfManagedLatticeResource`. | 
|  `bedrock-agentcore:ResourceConfigurationIdentifier`  | String |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the resource configuration identifier of a target’s private endpoint. | 
|  `bedrock-agentcore:subnets`  | ArrayOfString |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the subnets configured for the managed VPC resource of a target. See [Use IAM condition keys with AgentCore VPC settings](security-vpc-condition.md). | 
|  `bedrock-agentcore:securityGroups`  | ArrayOfString |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the security groups configured for the managed VPC resource of a target. | 
|  `bedrock-agentcore:AllowedQueryParameters`  | ArrayOfString |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the allowed query parameters in the target’s metadata configuration. | 
|  `bedrock-agentcore:AllowedRequestHeaders`  | ArrayOfString |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the allowed request headers in the target’s metadata configuration. | 
|  `bedrock-agentcore:AllowedResponseHeaders`  | ArrayOfString |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the allowed response headers in the target’s metadata configuration. | 
|  `bedrock-agentcore:CredentialProviderScope`  | ArrayOfString |  `CreateGatewayTarget`, `UpdateGatewayTarget`  | Filters access by the scopes configured on an OAuth credential provider for the target. | 

## Gateway invocation condition keys
<a name="gateway-invocation-condition-keys"></a>

The following condition keys apply to the `InvokeGateway` operation. AgentCore Gateway sets them from the claims of the JWT in the request. They are present only for gateways that use JWT inbound authorization (`CUSTOM_JWT`). A key is absent when the JWT does not include the claim.


| Condition key | Type | API operations | Description | 
| --- | --- | --- | --- | 
|  `bedrock-agentcore:InboundJwtClaim/iss`  | String |  `InvokeGateway`  | Filters access by the issuer (`iss`) claim in the JWT passed in the request. | 
|  `bedrock-agentcore:InboundJwtClaim/sub`  | String |  `InvokeGateway`  | Filters access by the subject (`sub`) claim in the JWT passed in the request. | 
|  `bedrock-agentcore:InboundJwtClaim/client_id`  | String |  `InvokeGateway`  | Filters access by the `client_id` claim in the JWT passed in the request. | 
|  `bedrock-agentcore:InboundJwtClaim/aud`  | ArrayOfString |  `InvokeGateway`  | Filters access by the audience (`aud`) claim in the JWT passed in the request. A single audience value becomes a list with one value. | 
|  `bedrock-agentcore:InboundJwtClaim/scope`  | ArrayOfString |  `InvokeGateway`  | Filters access by the `scope` claim in the JWT passed in the request. AgentCore Gateway splits the space-delimited `scope` claim into a list of individual scopes. | 

Because `aud` and `scope` can hold more than one value, use them with a set operator, such as `ForAnyValue:StringEquals`. For more information, see [Set operators for multivalued context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.html#reference_policies_condition-multi-valued-context-keys) in the *IAM User Guide*.

 `InvokeGateway` requests also include the following AWS global condition keys, for all inbound authorization types:
+  `aws:SourceIp` – The IP address of the caller.
+  `aws:SourceVpc` and `aws:SourceVpce` – The VPC and the VPC endpoint that the request came through. These keys are present only when the request reaches the gateway through an interface VPC endpoint. For more information, see [Use interface VPC endpoints (AWS PrivateLink) to create a private connection between your VPC and your Amazon Bedrock AgentCore resources](vpc-interface-endpoints.md).

## Handle condition keys that are absent from a request
<a name="gateway-condition-keys-absent"></a>

AgentCore Gateway adds a condition key to the request context only when the request includes the value that the key describes. How a condition evaluates when its key is absent depends on the condition operator:
+ Operators that require a match, such as `StringEquals`, evaluate to false.
+ Negated operators, such as `StringNotEquals`, evaluate to true.
+ Operators with the `IfExists` suffix evaluate to true.

For example, a `Deny` statement with `StringNotEquals` on `bedrock-agentcore:DiscoveryUrl` also denies gateways that do not use a JWT authorizer, because those requests do not include a discovery URL. To limit a statement to requests that include a key, add a `Null` condition with the value `false` for that key. To require that a request includes a key, deny requests where the `Null` condition for that key is `true`.

For more information, see [IAM JSON policy elements: Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) in the *IAM User Guide*.

## Example policies
<a name="gateway-condition-key-examples"></a>

The following examples show how to use condition keys in IAM policies and SCPs to enforce organizational controls on gateway configuration. For RCP examples that control gateway invocations, see [Example RCPs for AgentCore Gateway](resource-control-policies.md#resource-control-policies-examples).

### Require gateways to use a specific identity provider
<a name="example-require-specific-idp"></a>

Use the following SCP to deny gateway creation or updates when the gateway uses a JWT authorizer with a discovery URL other than your organization’s approved identity provider. The `Null` condition limits the statement to requests that include a discovery URL, so the statement does not deny gateways that use IAM inbound authorization. To also deny gateways without inbound authorization, see [Prevent gateways without inbound authorization](#example-deny-gateways-without-inbound-auth).

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnforceGatewayIdP",
            "Effect": "Deny",
            "Action": [
                "bedrock-agentcore:CreateGateway",
                "bedrock-agentcore:UpdateGateway"
            ],
            "Resource": "*",
            "Condition": {
                "Null": {
                    "bedrock-agentcore:DiscoveryUrl": "false"
                },
                "StringNotEquals": {
                    "bedrock-agentcore:DiscoveryUrl": "https://example.org/.well-known/openid-configuration"
                }
            }
        }
    ]
}
```

### Prevent gateways without inbound authorization
<a name="example-deny-gateways-without-inbound-auth"></a>

Use the following SCP to deny creating or updating a gateway that has no inbound authorization.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyGatewaysWithoutInboundAuth",
            "Effect": "Deny",
            "Action": [
                "bedrock-agentcore:CreateGateway",
                "bedrock-agentcore:UpdateGateway"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "bedrock-agentcore:GatewayAuthorizerType": "NONE"
                }
            }
        }
    ]
}
```

### Restrict credential provider types for targets
<a name="example-restrict-target-credential-types"></a>

Use the following SCP to restrict gateway targets to approved credential provider types. With this example, you restrict gateway targets to use only the gateway’s IAM role or caller IAM credentials. Targets cannot use externally managed API keys or OAuth tokens.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RestrictTargetCredentialTypes",
            "Effect": "Deny",
            "Action": [
                "bedrock-agentcore:CreateGatewayTarget",
                "bedrock-agentcore:UpdateGatewayTarget"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "bedrock-agentcore:CredentialProviderType": [
                        "GATEWAY_IAM_ROLE",
                        "CALLER_IAM_CREDENTIALS"
                    ]
                }
            }
        }
    ]
}
```

### Restrict the types of MCP targets that can be created
<a name="example-restrict-target-types"></a>

Use the following policy to deny creation of MCP targets that use certain configuration types. This example prevents targets from using direct MCP server URLs.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyDirectMcpServerTargets",
            "Effect": "Deny",
            "Action": [
                "bedrock-agentcore:CreateGatewayTarget",
                "bedrock-agentcore:UpdateGatewayTarget"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "bedrock-agentcore:McpTargetConfigurationType": "mcpServer"
                }
            }
        }
    ]
}
```

### Require targets to use private endpoints
<a name="example-enforce-private-endpoints"></a>

Use the following SCP to deny creation of targets that do not specify a private endpoint type. This ensures that all target traffic stays within private networks.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnforcePrivateEndpoints",
            "Effect": "Deny",
            "Action": [
                "bedrock-agentcore:CreateGatewayTarget",
                "bedrock-agentcore:UpdateGatewayTarget"
            ],
            "Resource": "*",
            "Condition": {
                "Null": {
                    "bedrock-agentcore:PrivateEndpointType": "true"
                }
            }
        }
    ]
}
```

### Require gateways to use a customer managed KMS key
<a name="example-require-encryption"></a>

Use this SCP to require that all gateways use a customer managed KMS key for encryption instead of the service default.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnforceCustomerManagedKey",
            "Effect": "Deny",
            "Action": [
                "bedrock-agentcore:CreateGateway",
                "bedrock-agentcore:UpdateGateway"
            ],
            "Resource": "*",
            "Condition": {
                "Null": {
                    "bedrock-agentcore:KmsKeyArn": "true"
                }
            }
        }
    ]
}
```

### Enforce approved subnets for gateway targets
<a name="example-enforce-approved-subnets-for-targets"></a>

Use the following policy to restrict gateway targets to approved subnets. For more information, see [Use IAM condition keys with AgentCore VPC settings](security-vpc-condition.md).

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnforceApprovedSubnets",
            "Effect": "Deny",
            "Action": [
                "bedrock-agentcore:CreateGatewayTarget",
                "bedrock-agentcore:UpdateGatewayTarget"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringNotEquals": {
                    "bedrock-agentcore:subnets": [
                        "subnet-0123456789abcdef0",
                        "subnet-0123456789abcdef1"
                    ]
                }
            }
        }
    ]
}
```