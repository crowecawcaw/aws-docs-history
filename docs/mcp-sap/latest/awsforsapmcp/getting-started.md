

# Getting Started
<a name="getting-started"></a>

Before you deploy the AWS for SAP Model Context Protocol (MCP) Server by using the CloudFormation template, verify that you meet the following prerequisites across your AWS environment, SAP system, and network.

## AWS Prerequisites
<a name="aws-prerequisites"></a>
+ An AWS account with access to AWS Bedrock AgentCore for hosting the AWS for SAP MCP Server.
+ You (or the IAM role you use for deployment) must have the following IAM permissions.

### IAM permissions required for CloudFormation deployment
<a name="iam-permissions"></a>

The AWS for SAP MCP Server can be deployed via a CloudFormation template (see [Deployment via AWS CloudFormation](deployment.md)). The following IAM permissions are required for the user or role deploying the CloudFormation template. These permissions allow CloudFormation to create and manage the resources defined in the template.


|  AWS Service | Actions | Resources | 
| --- | --- | --- | 
|  AWS CloudFormation |  `cloudformation:CreateStack`, `cloudformation:UpdateStack`, `cloudformation:DeleteStack`, `cloudformation:DescribeStacks`, `cloudformation:DescribeStackEvents`, `cloudformation:GetTemplate`, `cloudformation:CreateChangeSet`  |  `arn:aws:cloudformation:*:*:stack/*`  | 
|  AWS Secrets Manager |  `secretsmanager:GetSecretValue`, `secretsmanager:DescribeSecret`, `secretsmanager:CreateSecret`, `secretsmanager:DeleteSecret`  |  `arn:aws:secretsmanager:*:*:secret:<your-secret-name>*`  | 
| Amazon Cognito |  `cognito-idp:CreateUserPool`, `cognito-idp:CreateUserPoolClient`, `cognito-idp:CreateUserPoolDomain`, `cognito-idp:CreateResourceServer`, `cognito-idp:DeleteUserPool`, `cognito-idp:DeleteUserPoolClient`, `cognito-idp:DeleteUserPoolDomain`, `cognito-idp:DeleteResourceServer`, `cognito-idp:DescribeUserPool`, `cognito-idp:DescribeUserPoolClient`, `cognito-idp:DescribeResourceServer`, `cognito-idp:DescribeUserPoolDomain`  |  `*`  | 
|  AWS IAM |  `iam:CreateRole`, `iam:DeleteRole`, `iam:GetRole`, `iam:PutRolePolicy`, `iam:DeleteRolePolicy`, `iam:AttachRolePolicy`, `iam:DetachRolePolicy`, `iam:PassRole`, `iam:ListRolePolicies`, `iam:ListAttachedRolePolicies`, `iam:GetRolePolicy`  |  `arn:aws:iam::*:role/*`  | 
|  AWS Lambda |  `lambda:CreateFunction`, `lambda:DeleteFunction`, `lambda:GetFunction`, `lambda:GetFunctionConfiguration`, `lambda:InvokeFunction`, `lambda:UpdateFunctionCode`, `lambda:UpdateFunctionConfiguration`, `lambda:AddPermission`, `lambda:RemovePermission`  |  `arn:aws:lambda:*:*:function:*`  | 
| Amazon Bedrock AgentCore |  `bedrock-agentcore:CreateRuntime`, `bedrock-agentcore:UpdateRuntime`, `bedrock-agentcore:DeleteRuntime`, `bedrock-agentcore:GetRuntime`, `bedrock-agentcore:CreateOauth2CredentialProvider`, `bedrock-agentcore:GetOauth2CredentialProvider`, `bedrock-agentcore:DeleteOauth2CredentialProvider`, `bedrock-agentcore:CreateTokenVault`  |  `*`  | 
| Amazon S3 |  `s3:GetObject`  | CloudFormation template S3 URI | 
| Amazon ECR |  `ecr:BatchGetImage`, `ecr:GetDownloadUrlForLayer`, `ecr:GetAuthorizationToken`  |  `*`  | 
| Amazon CloudWatch Logs |  `logs:CreateLogGroup`, `logs:DescribeLogGroups`, `logs:DescribeLogStreams`, `logs:CreateLogStream`, `logs:PutLogEvents`  |  `arn:aws:logs:*:*:log-group:/aws/bedrock-agentcore/runtimes/*`  | 
| Amazon CloudWatch |  `cloudwatch:PutMetricData`  |  `*`  | 
|  AWS X-Ray |  `xray:PutTraceSegments`, `xray:PutTelemetryRecords`, `xray:GetSamplingRules`, `xray:GetSamplingTargets`  |  `*`  | 

## SAP Prerequisites
<a name="sap-prerequisites"></a>
+ SAP S/4HANA or SAP ERP Central Component (ECC) system with OData (Open Data Protocol) enabled. For more information about SAP Gateway and OData support, see [SAP documentation](https://help.sap.com/saphelp_gateway20sp12/helpdata/en/88/889a8cbf6046378e274d6d9cd04e4d/content.htm?no_cache=true).
+ SAP OData Service Activation via [OData Service in SAP Gateway Hub](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/1b/023c1cad774eeb8b85b25c86d94f87/frameset.htm).
+ Enable the OData API to use service type `WEB_API`. This setting is recommended and applies only to SAP S/4HANA.
+ SAP’s OData Service Catalog `IWFND/CATALOGSERVICE;v=2` must be available on the SAP system for service discovery. This is required only for the use of Standard Catalog.
+ Valid SAP credentials (System User / OAuth) for your chosen authentication flow.

## Network Prerequisites
<a name="network-prerequisites"></a>
+ Allow outbound HTTPS access from the Amazon Bedrock AgentCore Runtime elastic network interface (ENI) to the SAP system. If traffic flows through an Application Load Balancer (ALB) or Network Load Balancer (NLB), allow outbound HTTPS access to that ALB or NLB instead.
+ Allow outbound HTTPS access from Amazon Bedrock AgentCore Runtime to AWS services such as AWS Secrets Manager, Amazon S3, and Amazon Bedrock AgentCore Identity. Because these service endpoints are public, the private subnet where Amazon Bedrock AgentCore Runtime runs must provide internet access through a NAT Gateway. As an alternative, you can use VPC endpoints to access these services privately.
+ Inbound connectivity on HTTPS (443) port from the MCP client (AI agent) to Amazon Bedrock AgentCore Runtime.
+ For detailed prerequisites, refer to the Amazon Bedrock AgentCore documentation:
  +  [AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) 
  +  [AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) 
  +  [AgentCore VPC configuration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html) 

## Authentication Prerequisites
<a name="auth-prerequisites"></a>

The prerequisites for credential setup depend on which authentication flow you plan to use.

### Inbound authentication
<a name="inbound-auth-prereqs"></a>

Inbound authentication requires a JSON Web Token (JWT) compatible identity provider. The CloudFormation template supports two options:
+  **Amazon Cognito:** No prerequisites.
+  **External Identity Provider (Entra ID):** If you use an external identity provider (IdP) for inbound authentication, you must configure your IdP before deployment and provide the following through the CloudFormation template parameters:
  +  **Discovery URL:** Your identity provider’s well-known configuration endpoint, used by AgentCore Identity to fetch token validation keys and issuer information.
  +  **Allowed audiences:** The audience values that AgentCore Identity accepts when validating incoming tokens.

### Outbound Authentication
<a name="outbound-auth-prereqs"></a>

 AWS for SAP MCP Server supports Basic Auth and OAuth2 (M2M, User Federation, and On-Behalf-Of Token Exchange).

 **Basic Authentication** 

 AWS Secrets Manager secret containing SAP username and password is required in the following Key-Value Pair format.

```
username: <sap_username>
password: <sap_password>
```

 **OAuth 2.0 Authentication** 

 AWS Secrets Manager secret containing IdP clientId and clientSecret is required in the following Key-Value Pair format, for both M2M and User Federation.

```
clientId: <oauth_client_id>
clientSecret: <oauth_client_secret>
```

Additionally, SAP and IdP related OAuth2/OIDC/SAML configuration are required as outlined for different patterns.

#### Machine to Machine (2-Legged OAuth)
<a name="m2m-outbound-prereqs"></a>

 **Pattern 1: SAP as Authorization Server with OAuth2** 
+ • SAP Application Server (Gateway), when hosted inside your VPC without public internet exposure will require AgentCore Identity to have private connectivity in order to reach the IdP’s token/Auth endpoints. In these cases, configure a Private Endpoint on the outbound OAuth credential provider (SAP in this case) using VPC Lattice (managed or self-managed). See [Connect to private identity providers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-private-idp.html) for the required VPC, subnet, security group, and IAM setup.
+ OAuth Client Setup via [OAuth client configuration](https://help.sap.com/docs/ABAP_PLATFORM_NEW/fd0fc52fd22b45f29d274a7f8236e768/cdb122d5b0784c77bf1bcce17f730e74.html).
+ Scopes correspond to SAP OData service names (for example, `ZAPI_SALES_ORDER_SRV_0001`).

 **Pattern 2: External IdP (Entra ID) with OIDC** 
+ Your identity provider must be configured and accessible before deployment. You will need the authorization URL, token URL, and scope from your IdP for the CloudFormation template parameters.
+ OIDC Trust Setup via [SOIDC configuration](https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_752/e815bb97839a4d83be6c4fca48ee5777/d72c1a254a584d579c476a998b8ec0b2.html).
+ This is applicable only to SAP S/4HANA.

#### User Federation (3-Legged OAuth)
<a name="user-federation-outbound-prereqs"></a>

 **Pattern 1: SAP as Authorization Server with OAuth2** 
+ Same as M2M Pattern 1 prerequisites, plus:
  + The AgentCore callback URL must be registered with SAP as a redirect URI in the OAuth2 client configuration. This URL is auto-generated during deployment.

 **Pattern 2: SAP as Authorization Server with OAuth2 \+ SAML IdP (Entra ID)** 
+ Same as M2M Pattern 1 prerequisites, plus:
  + A SAML identity provider (Entra ID) configured as a trusted provider in SAP ([SAML2 transaction](https://help.sap.com/doc/saphelp_scm700_ehp02/7.0.2/en-US/4a/b4c93185376d61e10000000a42189c/frameset.htm)).
  + The AgentCore callback URL must be registered with SAP as a redirect URI in the OAuth2 client configuration. This URL is auto-generated during deployment.

 **Pattern 3: External IdP (Entra ID) with OIDC** 
+ Same as External IdP M2M OIDC prerequisites, plus:
  + The AgentCore callback URL must be registered as a redirect URI in your identity provider’s application configuration. This URL is auto-generated during deployment.
  + This is applicable only to SAP S/4HANA.

#### On-Behalf-Of Token Exchange
<a name="obo-token-exchange-outbound-prereqs"></a>

 **Pattern: External IdP (Entra ID) with token exchange** 
+ Same as M2M Pattern 2 (External IdP with OIDC) prerequisites, plus:
  + Two Entra ID app registrations are required: an inbound app (for user authentication) and an outbound app (for the token exchange).
  + The outbound app must authorize the inbound app as a client.
  + User consent (or admin consent) granted to the outbound app in Entra ID.
  + The AgentCore callback URL must be registered as a redirect URI in the outbound app’s configuration. This URL is auto-generated during deployment.
  + Certain MCP Clients might need a Three App setup. Three Entra ID app registrations include a Client app (for user authentication), a Resource app (representing AgentCore for token validation), and an Outbound app (for the token exchange to SAP). The Resource app performs the OBO exchange using its own credentials to obtain a token scoped to the Outbound app.