

# Resource control policies for Amazon Bedrock AgentCore

Resource control policies (RCPs) are an AWS Organizations policy type that sets the maximum permissions available for resources in your organization. You attach an RCP to the organization root, an organizational unit (OU), or an account. Use one RCP to limit access to the Amazon Bedrock AgentCore resources in every member account below it. You do not need to change each resource.

Use RCPs to apply the same guardrails to your AgentCore resources, including for callers outside your organization. For example, you can require that gateway invocations come from your network. For more information, see [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) in the * AWS Organizations User Guide*.

RCPs for AgentCore use the `bedrock-agentcore` service prefix. AWS Agent Registry uses the `agent-registry` prefix, so these RCPs do not apply to Agent Registry.

**Topics**
+ [Compare RCPs with other policy types](#resource-control-policies-compare)
+ [Considerations](#resource-control-policies-considerations)
+ [Avoid blocking requests that AgentCore makes for you](#resource-control-policies-service-calls)
+ [Use RCPs with AgentCore Gateway](#resource-control-policies-gateway)
+ [Example RCPs for AgentCore Gateway](#resource-control-policies-examples)

## Compare RCPs with other policy types
<a name="resource-control-policies-compare"></a>

Choose a policy type based on what you want to control. The following table compares RCPs with the other policy types that control access to AgentCore resources.


| Policy type | What it applies to | Use it to | 
| --- | --- | --- | 
| Resource control policy (RCP) | Requests to resources in your member accounts, including requests from outside your organization. | Set organization-wide limits on access to your resources, including access by callers that are not IAM principals in your organization. | 
| Service control policy (SCP) | Requests that IAM principals in your member accounts make. | Set organization-wide limits on what your IAM principals can do. See [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the * AWS Organizations User Guide*. | 
| Resource-based policy | Requests to one resource. | Allow or deny access to a single resource. See [Resource-based policies for Amazon Bedrock AgentCore](resource-based-policies.md). | 

## Considerations
<a name="resource-control-policies-considerations"></a>

Before you attach an RCP, review how RCPs work with AgentCore.
+ RCPs do not grant permissions. They only set the maximum permissions available. You still need identity-based or resource-based policies that allow access.
+ An RCP affects the resources in the member accounts under the root, OU, or account where you attach it. It never affects resources in the management account, even when you attach it to the organization root. For more information, see [RCP effects on permissions](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html#rcp-effects-on-permissions) in the * AWS Organizations User Guide*.
+ Every RCP statement uses a wildcard principal, `"Principal": "*"`. AWS Organizations does not accept any other principal in an RCP. Use conditions to choose which requests a statement applies to.
+ A condition key that is absent from the request changes how a condition evaluates. Negated operators such as `StringNotEquals`, and operators with the `IfExists` suffix, evaluate to true when the key is absent. To limit a statement to requests that include a key, add a `Null` condition for that key. For more information, see [IAM JSON policy elements: Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) in the *IAM User Guide*.
+ Test an RCP on a test account or organizational unit before you attach it to the organization root. To find requests that an RCP denies, review AWS CloudTrail logs for access denied errors.

## Avoid blocking requests that AgentCore makes for you
<a name="resource-control-policies-service-calls"></a>

AgentCore makes requests on your behalf to complete your requests. For example, AgentCore Gateway uses the gateway service role to invoke gateway targets. It also uses the role to get OAuth tokens and API keys for targets from AgentCore Identity. When you create or delete a gateway, AgentCore Gateway also creates or deletes its workload identity in AgentCore Identity through a forward access session. These requests come from the AgentCore network, not from your VPC or your corporate network. A network perimeter policy that covers the services AgentCore calls can deny them.

To avoid blocking these requests, exempt them from your network perimeter statements. For the AWS guidance on network perimeters and exemptions, see [Establish permissions guardrails using data perimeters](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_data-perimeters.html) in the *IAM User Guide*.

Exempt each of the following kinds of requests:

Requests through forward access sessions (FAS)  
 AWS services make these requests with your credentials. To exempt them, use the `aws:ViaAWSService` condition key.

Requests from AWS service principals  
 AWS services make these requests as themselves. To exempt them, use the `aws:PrincipalIsAWSService` condition key.

Requests from AgentCore service roles  
Service roles, such as the gateway service role, make these requests. To exempt them, use a principal tag, such as `dp:exclude:network`.

Add all three exemptions to each network perimeter statement. To find out which kind of request an RCP denied, review the `userIdentity` element of the CloudTrail event for the denied request. CloudTrail logs the AgentCore Identity requests that AgentCore makes for you, such as `GetWorkloadAccessToken`, `GetResourceOauth2Token`, and `GetResourceApiKey`, as management events in the account that owns the resource. The `userIdentity` element shows the kind of request as follows:
+ For a request through FAS, `arn` names your IAM principal, and `invokedBy` names the AWS service that made the request.
+ For a request from a service principal, `type` is `AWSService`.
+ For a request from a service role, `arn` names a session of the service role. `invokedBy` can also name the AWS service, so use `arn`, not `invokedBy`, to tell it apart from a request through FAS.

For more information, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html) in the *IAM User Guide*, and [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html) in the * AWS CloudTrail User Guide*.

To exempt a service role, tag it with `dp:exclude:network` set to `true`. Then exclude principals with that tag from your network perimeter statements.

**Note**  
Restrict who can add or change tags that start with `dp:`. Use the tag exemption only together with an identity perimeter statement that denies principals outside your organization. Otherwise, principals in other accounts can tag themselves to bypass your controls.

### Example: Gateway network perimeter with service exemptions
<a name="resource-control-policies-example-service-calls"></a>

The following RCP denies gateway invocations that come from outside your corporate network and your VPC. It exempts the three kinds of requests that AgentCore makes for you. Add the same exemptions to network perimeter statements for the services that AgentCore calls.

Replace {{192.0.2.0/24}} with the IP address range of your corporate network. Replace {{vpc-1a2b3c4d}} with your VPC ID. Use the following JSON RCP:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnforceGatewayInvokeNetworkPerimeter",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "bedrock-agentcore:InvokeGateway",
            "Resource": "*",
            "Condition": {
                "NotIpAddressIfExists": {
                    "aws:SourceIp": "192.0.2.0/24"
                },
                "StringNotEqualsIfExists": {
                    "aws:SourceVpc": "vpc-1a2b3c4d",
                    "aws:PrincipalTag/dp:exclude:network": "true"
                },
                "BoolIfExists": {
                    "aws:ViaAWSService": "false",
                    "aws:PrincipalIsAWSService": "false"
                }
            }
        }
    ]
}
```

**Note**  
AgentCore Identity and AgentCore Policy control plane actions do not receive the `aws:SourceVpc` and `aws:SourceVpce` condition keys. Keep these actions out of network perimeter statements that use these keys.

For more network perimeter RCPs, see the [data perimeter policy examples](https://github.com/aws-samples/data-perimeter-policy-examples) repository on the GitHub website.

## Use RCPs with AgentCore Gateway
<a name="resource-control-policies-gateway"></a>

Your RCPs apply to `InvokeGateway` requests for every inbound authorization type: `AWS_IAM`, `AUTHENTICATE_ONLY`, `CUSTOM_JWT`, and `NONE`. AgentCore Gateway uses the RCPs that apply to the account that owns the gateway.

Use RCPs to control access to gateways that use JSON Web Token (JWT) inbound authorization or no inbound authorization. Callers of these gateways are not IAM principals, so SCPs do not apply to them.

Review the following before you write an RCP for gateway invocations:
+ For gateways that use `CUSTOM_JWT` or `NONE` inbound authorization, AgentCore Gateway evaluates the request as an anonymous principal, even if the caller signs it with SigV4. The request context does not include principal condition keys, such as `aws:PrincipalArn`, `aws:PrincipalAccount`, `aws:PrincipalOrgID`, and `aws:PrincipalTag`.
+ For gateways that use `CUSTOM_JWT` or `NONE` inbound authorization, use condition keys that are present in the request, such as `aws:SourceIp` and `aws:SourceVpce`. For `CUSTOM_JWT` gateways, you can also use the `bedrock-agentcore:InboundJwtClaim/*` keys. For more information about these keys, see [Gateway invocation condition keys](security-gateway-condition-keys.md#gateway-invocation-condition-keys).
+ For gateways that use `AWS_IAM` inbound authorization, the request context includes the principal condition keys.
+ For gateways with any inbound authorization type, enable CloudTrail data event logging to find requests that an RCP denies. `InvokeGateway` is a data event, so CloudTrail does not log it by default. For more information, see [Enable CloudTrail data event logging for Amazon Bedrock AgentCore Gateway resources](enabling-cloudtrail-data-event-logging.md).
+ For `InvokeGateway`, the error returned to the caller does not identify the policy that denied the request. For gateways that use `AWS_IAM` inbound authorization, the `errorMessage` field of the CloudTrail data event names the RCP. For gateways that use `CUSTOM_JWT` inbound authorization, the `errorMessage` field says only that a resource control policy denied the request.

For more information about the gateway service role, see [Set up permissions for AgentCore Gateway](gateway-prerequisites-permissions.md).

## Example RCPs for AgentCore Gateway
<a name="resource-control-policies-examples"></a>

The following examples show common RCPs for gateway invocations.

**Important**  
Each example uses `"Principal": "*"` because RCPs require a wildcard principal. Each statement only denies access, and its conditions select the requests that it denies. An RCP never grants access to any caller.

### Example: Require gateway invocations to come from your VPCs
<a name="resource-control-policies-example-network"></a>

The following RCP requires that gateway invocations arrive through an interface VPC endpoint in one of your VPCs.

It denies `InvokeGateway` requests that do not arrive through an interface VPC endpoint in one of your VPCs. It applies to gateways with any inbound authorization type. The `BoolIfExists` condition exempts requests that AWS services make through forward access sessions or as service principals.

The RCP also denies agents on AgentCore Runtime and other AWS compute outside the listed VPCs. To allow them, have them reach the gateway through an interface VPC endpoint in one of those VPCs. For more information about interface VPC endpoints, see [Use interface VPC endpoints (AWS PrivateLink) to create a private connection between your VPC and your Amazon Bedrock AgentCore resources](vpc-interface-endpoints.md).

In the `aws:SourceVpc` list, replace {{vpc-1a2b3c4d}} and {{vpc-5e6f7a8b}} with your VPC IDs. Add one entry for each VPC. Use the following JSON RCP:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnforceGatewayNetworkPerimeter",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "bedrock-agentcore:InvokeGateway",
            "Resource": "*",
            "Condition": {
                "StringNotEqualsIfExists": {
                    "aws:SourceVpc": [
                        "vpc-1a2b3c4d",
                        "vpc-5e6f7a8b"
                    ]
                },
                "BoolIfExists": {
                    "aws:ViaAWSService": "false",
                    "aws:PrincipalIsAWSService": "false"
                }
            }
        }
    ]
}
```

### Example: Require JWTs from your identity provider
<a name="resource-control-policies-example-issuer"></a>

The following RCP requires that the JWT in each gateway invocation comes from your identity provider.

It denies `InvokeGateway` requests whose JWT comes from an issuer other than your identity provider. The `Null` condition limits the statement to requests that include a JWT with an `iss` claim. As a result, the RCP does not deny requests to gateways that do not use JWT inbound authorization.

Replace {{https://example.org}} with the issuer URL of your identity provider. Use the following JSON RCP:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RequireApprovedTokenIssuer",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "bedrock-agentcore:InvokeGateway",
            "Resource": "*",
            "Condition": {
                "Null": {
                    "bedrock-agentcore:InboundJwtClaim/iss": "false"
                },
                "StringNotEquals": {
                    "bedrock-agentcore:InboundJwtClaim/iss": "https://example.org"
                }
            }
        }
    ]
}
```

### Example: Require a scope in the JWT
<a name="resource-control-policies-example-scope"></a>

The following RCP requires that the JWT in each gateway invocation includes a specific scope.

It denies `InvokeGateway` requests whose JWT does not include the `gateway:invoke` scope. The `scope` claim is a list, so the statement uses the `ForAllValues` set operator. The statement also denies a JWT that has no `scope` claim. The `Null` condition limits the statement to requests that include a JWT with an `iss` claim.

Replace {{gateway:invoke}} with the scope that your callers must have. Use the following JSON RCP:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RequireGatewayInvokeScope",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "bedrock-agentcore:InvokeGateway",
            "Resource": "*",
            "Condition": {
                "Null": {
                    "bedrock-agentcore:InboundJwtClaim/iss": "false"
                },
                "ForAllValues:StringNotEquals": {
                    "bedrock-agentcore:InboundJwtClaim/scope": "gateway:invoke"
                }
            }
        }
    ]
}
```

### Example: Block a JWT client
<a name="resource-control-policies-example-client"></a>

The following RCP blocks gateway invocations from one OAuth client.

It denies `InvokeGateway` requests from a specific OAuth client, for example a client whose credentials were exposed.

Replace {{example-client-id}} with the client ID to block. Use the following JSON RCP:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "BlockOAuthClient",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "bedrock-agentcore:InvokeGateway",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "bedrock-agentcore:InboundJwtClaim/client_id": "example-client-id"
                }
            }
        }
    ]
}
```

For SCP examples that control how administrators create and configure gateways, see [Example policies](security-gateway-condition-keys.md#gateway-condition-key-examples).