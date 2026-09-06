

# Deployment via AWS CloudFormation
<a name="deployment"></a>

You deploy the AWS for SAP Model Context Protocol (MCP) Server onto Amazon Bedrock AgentCore Runtime by using an AWS CloudFormation template. The template creates all required resources for you, including the AgentCore runtime, Identity and Access Management (IAM) roles, and networking configuration.

Before you begin, ensure you have completed the necessary setup detailed in the [Getting Started](getting-started.md) section.

## Summary of prerequisites
<a name="summary-of-prerequisites"></a>
+  **IAM Roles** with sufficient privileges to create CloudFormation stacks and the resources defined within the stack.
+  **VPC** with private subnets and security groups already configured in your target AWS Region.
+  **Network connectivity** from selected subnets to your SAP system (via Direct Connect, VPN, or internal routing).
+  ** AWS Secrets Manager secret** containing SAP or OAuth credentials.
+  **Private IdP** if your VPC-hosted SAP system (Application Server/Gateway) is used as an IdP, you must choose an Amazon VPC Lattice connectivity mode (managed or self-managed). For self-managed mode, pre-create a VPC Lattice resource configuration before deployment. For more information, see [Connect to private identity providers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-private-idp.html).

## Deployment Steps
<a name="deployment-steps"></a>

### Step 1: Launch the CloudFormation stack
<a name="step-1-launch"></a>

1. Sign in to the {aws-management-console}.

1. Navigate to **CloudFormation** → **Stacks** → **Create stack** → **With new resources (standard)**.

1. Under **Specify template**, select **Amazon S3 URL** and enter:

   ```
   https://awsforsap-mcp-server-setup-{region}.s3.{region}.amazonaws.com/cfn-launch-template/latest/AwsForSapMcpServerStack.template.json
   ```

   Example:

   ```
   https://awsforsap-mcp-server-setup-us-east-1.s3.us-east-1.amazonaws.com/cfn-launch-template/latest/AwsForSapMcpServerStack.template.json
   ```

1. Choose **Next**.

### Step 2: Specify stack details
<a name="step-2-stack-details"></a>

Provide a **Stack name** following these rules:
+ Must start with a letter (a–z, A–Z).
+ Can contain letters, numbers, and hyphens only.
+ Maximum 128 characters.

Example: `aws-for-sap-mcp-server` 

### Step 3: Configure Parameters
<a name="step-3-parameters"></a>

 **General configuration** 


| Parameter | Parameter Label | Description | Example | 
| --- | --- | --- | --- | 
|  `UniqueId`  | Unique Identifier | Short unique identifier for stack resources. Max 8 characters, lowercase alphanumeric. Used to namespace all resources within the stack. |  `mcp01`  | 

 **SAP system configuration** 


| Parameter | Parameter Label | Description | Example | 
| --- | --- | --- | --- | 
|  `SapBaseUrl`  | SAP Base OData Endpoint | Base URL of the SAP OData endpoint. |  `https://host:port/sap/opu/odata/sap/`  | 

 **Authentication configuration** 

The MCP Server supports the following authentication flows for connecting to SAP. Choose the one that matches your SAP system setup.


| Parameter | Parameter Label | Description | BASIC | M2M | USER\_FEDERATION | ON\_BEHALF\_OF\_TOKEN\_EXCHANGE | 
| --- | --- | --- | --- | --- | --- | --- | 
|  `AuthFlow`  | Authentication Flow | Authentication flow to use: `BASIC`, `M2M`, `USER_FEDERATION`, or `ON_BEHALF_OF_TOKEN_EXCHANGE`. | ✓ | ✓ | ✓ | ✓ | 
|  `SapCredentialsSecret`  | Auth Credentials Secret Name |  AWS Secrets Manager secret name containing SAP credentials (BASIC) or OAuth client credentials. | Required | Required | Required | Required | 
|  `SapAuthorizeUrl`  | Authorization Endpoint | OAuth2 authorization URL. | — | Required | Required | — | 
|  `SapTokenUrl`  | Token Endpoint | OAuth2 token URL. | — | Required | Required | — | 
|  `OauthScopes`  | Scope(s) | OAuth scopes for SAP access. | — | Required | Required | Required | 
|  `AppCallbackEndpoint`  | Application Callback Endpoint | Client application callback URL. | — | — | Required | — | 

 **Inbound Authentication Configuration** 


| Parameter | Parameter Label | Description | Notes | 
| --- | --- | --- | --- | 
|  `InboundAuthProvider`  | Inbound Authentication Provider | Identity provider for validating incoming requests to the MCP Server. | Default: Cognito (or Entra ID) | 
|  `DiscoveryUrl`  | Discovery Url | URL to fetch authorization server metadata for JWT validation. | Required for Entra ID; not needed for Cognito | 
|  `AllowedAudiences`  | Allowed Audiences | Audience values validated in incoming JWT tokens. | Required for Entra ID; not needed for Cognito | 

**Note**  
 `DiscoveryUrl` and `AllowedAudiences` are only required when using an external identity provider (for example, Entra ID). Leave these fields empty if using Cognito.

 **MCP Server Configuration** 


| Parameter | Parameter Label | Description | Allowed Values | Default | 
| --- | --- | --- | --- | --- | 
|  `McpServerLogLevel`  | MCP Server Log Level | Server log level. |  `DEBUG`, `INFO`, `WARNING`, `ERROR`  |  `INFO`  | 

 **MCP Server Permissions** 

Control which operations the MCP Server is permitted to perform against your SAP system. Start with the minimum permissions required.


| Parameter | Parameter Label | Default | Dependency | 
| --- | --- | --- | --- | 
|  `McpServerReadEnabled`  | Enable Read Access |  `TRUE`  | — | 
|  `McpServerWriteEnabled`  | Enable Write Access |  `FALSE`  | — | 
|  `McpServerCreateEnabled`  | Enable Create Access |  `FALSE`  | Requires `McpServerWriteEnabled=true`  | 
|  `McpServerUpdateEnabled`  | Enable Update Access |  `FALSE`  | Requires `McpServerWriteEnabled=true`  | 
|  `McpServerDeleteEnabled`  | Enable Delete Access |  `FALSE`  | Requires `McpServerWriteEnabled=true`  | 
|  `McpServerFunctionImportEnabled`  | Enable Function Import |  `FALSE`  | — | 

**Note**  
 `McpServerCreateEnabled`, `McpServerUpdateEnabled`, and `McpServerDeleteEnabled` have no effect unless `McpServerWriteEnabled` is set to `true`.

 **Network Configuration** 


| Parameter | Parameter Label | Description | 
| --- | --- | --- | 
|  `McpServerVpcSecurityGroup`  | VPC Security Groups | Comma-separated list of VPC security group IDs. The security group must allow outbound traffic to your SAP system on the `SapBaseUrl` port. If traffic is routed through a load balancer (ALB/NLB), allow traffic on the associated listener port instead. | 
|  `McpServerNetworkSubnets`  | VPC Subnets | Comma-separated list of private subnet IDs where AgentCore launches its ENIs. These subnets must have network connectivity to the SAP system. | 

 **Subnet selection guidance:** 
+ The subnets for the AWS for SAP MCP Server must use an Availability Zone that is supported by AgentCore. See [AgentCore supported Availability Zones](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html#agentcore-supported-azs).
+ If your SAP system runs in a multi-AZ high-availability setup, ensure the network route from the selected subnets to the SAP virtual IP always resolves to the active system.
+ If traffic is routed through an Elastic Load Balancer (ALB/NLB), ensure the subnets can reach the ELB’s resolved IPs.

### Step 4: Configure stack options
<a name="step-4-stack-options"></a>

On the **Configure stack options** page you can optionally add tags, set IAM permissions, and configure stack failure behavior. For most deployments, the defaults are sufficient.

Choose **Next**.

### Step 5: Review and Deploy
<a name="step-5-review"></a>

1. Review all parameters on the summary page.

1. If prompted, acknowledge the IAM capabilities checkbox: **"I acknowledge that AWS CloudFormation might create IAM resources"**.

1. Choose **Submit**.

### Step 6: Monitor Deployment
<a name="step-6-monitor"></a>

1. Navigate to **CloudFormation** → **Stacks** and select your stack.

1. Open the **Events** tab to monitor progress.

1. When the status shows `CREATE_COMPLETE`, the MCP Server is deployed and ready.

**Note**  
If the stack reaches `ROLLBACK_COMPLETE`, check the Events tab for the root cause error, correct the parameter values, and redeploy.

## Example: Basic Authentication Deployment
<a name="deploy-basic-auth"></a>

The following command deploys the AWS for SAP MCP Server with Basic Authentication. Replace the placeholder values with your actual configuration:

```
aws cloudformation create-stack \
  --stack-name <your-stack-name> \
  --template-urlhttps://awsforsap-mcp-server-setup-<region>.s3.<region>.amazonaws.com/cfn-launch-template/latest/AwsForSapMcpServerStack.template.json \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
  --parameters \
    ParameterKey=UniqueId,ParameterValue=<your-unique-id> \
    ParameterKey=SapBaseUrl,ParameterValue=<your-sap-base-url> \
    ParameterKey=AuthFlow,ParameterValue=BASIC \
    ParameterKey=SapCredentialsSecret,ParameterValue=<your-secret-name> \
    ParameterKey=McpServerLogLevel,ParameterValue=INFO \
    ParameterKey=McpServerReadEnabled,ParameterValue=true \
    ParameterKey=McpServerWriteEnabled,ParameterValue=false \
    ParameterKey=McpServerCreateEnabled,ParameterValue=false \
    ParameterKey=McpServerUpdateEnabled,ParameterValue=false \
    ParameterKey=McpServerDeleteEnabled,ParameterValue=false \
    ParameterKey=McpServerVpcSecurityGroup,ParameterValue="sg-1234567" \
    ParameterKey=McpServerNetworkSubnets,ParameterValue="subnet-1234567"
```

**Note**  
For Basic Authentication with Cognito as the inbound provider, `DiscoveryUrl` and `AllowedAudiences` are not required.

## Example: Machine-to-Machine (M2M) Authentication Deployment
<a name="deploy-m2m-auth"></a>

For machine-to-machine OAuth authentication, include the additional OAuth parameters:

```
aws cloudformation create-stack \
  --stack-name <your-stack-name> \
  --template-url https://awsforsap-mcp-server-setup-<region>.s3.<region>.amazonaws.com/cfn-launch-template/latest/AwsForSapMcpServerStack.template.json \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
  --parameters \
    ParameterKey=UniqueId,ParameterValue=<your-unique-id> \
    ParameterKey=SapBaseUrl,ParameterValue=<your-sap-base-url> \
    ParameterKey=SapSystemType,ParameterValue=S4HANA \
    ParameterKey=SapClientNumber,ParameterValue=<your-client-number> \
    ParameterKey=InboundAuthProvider,ParameterValue=<your-idp-provider> \
    ParameterKey=DiscoveryUrl,ParameterValue=<your-discovery-url> \
    ParameterKey=AllowedAudiences,ParameterValue=<your-allowed-audiences> \
    ParameterKey=AuthFlow,ParameterValue=M2M \
    ParameterKey=SapCredentialsSecret,ParameterValue=<your-secret-name> \
    ParameterKey=SapAuthorizeUrl,ParameterValue=<your-sap-authorize-url> \
    ParameterKey=SapTokenUrl,ParameterValue=<your-sap-token-url> \
    ParameterKey=OauthScopes,ParameterValue=<your-oauth-scopes> \
    ParameterKey=McpServerLogLevel,ParameterValue=INFO \
    ParameterKey=McpServerReadEnabled,ParameterValue=true \
    ParameterKey=McpServerWriteEnabled,ParameterValue=false \
    ParameterKey=McpServerCreateEnabled,ParameterValue=false \
    ParameterKey=McpServerUpdateEnabled,ParameterValue=false \
    ParameterKey=McpServerDeleteEnabled,ParameterValue=false \
    ParameterKey=McpServerFunctionImportEnabled,ParameterValue=false \
    ParameterKey=UseSapCatalog,ParameterValue=true \
    ParameterKey=McpServerCustomCatalogBucketUri,ParameterValue=None \
    ParameterKey=McpServerServiceHintsS3Uri,ParameterValue=None \
    ParameterKey=AllowedServicePrefixes,ParameterValue=None \
    ParameterKey=McpServerVpcSecurityGroup,ParameterValue=<your-security-group-id> \
    ParameterKey=McpServerNetworkSubnets,ParameterValue=<your-subnet-ids>
```

**Note**  
 `DiscoveryUrl` and `AllowedAudiences` are required when using any inbound auth provider other than Cognito.

## Example: User Federation Authentication Deployment
<a name="deploy-user-federation-auth"></a>

```
aws cloudformation create-stack \
  --stack-name <your-stack-name> \
  --template-url https://awsforsap-mcp-server-setup-<region>.s3.<region>.amazonaws.com/cfn-launch-template/latest/AwsForSapMcpServerStack.template.json \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
  --parameters \
    ParameterKey=UniqueId,ParameterValue=<your-unique-id> \
    ParameterKey=SapBaseUrl,ParameterValue=<your-sap-base-url> \
    ParameterKey=SapSystemType,ParameterValue=S4HANA \
    ParameterKey=SapClientNumber,ParameterValue=<your-client-number> \
    ParameterKey=InboundAuthProvider,ParameterValue=<your-idp-provider> \
    ParameterKey=DiscoveryUrl,ParameterValue=<your-discovery-url> \
    ParameterKey=AllowedAudiences,ParameterValue=<your-allowed-audiences> \
    ParameterKey=AuthFlow,ParameterValue=USER_FEDERATION \
    ParameterKey=SapAuthorizeUrl,ParameterValue=<your-sap-authorize-url> \
    ParameterKey=SapTokenUrl,ParameterValue=<your-sap-token-url> \
    ParameterKey=OauthScopes,ParameterValue=<your-oauth-scopes> \
    ParameterKey=AppCallbackEndpoint,ParameterValue=<your-callback-url> \
    ParameterKey=McpServerLogLevel,ParameterValue=INFO \
    ParameterKey=McpServerReadEnabled,ParameterValue=true \
    ParameterKey=McpServerWriteEnabled,ParameterValue=false \
    ParameterKey=McpServerCreateEnabled,ParameterValue=false \
    ParameterKey=McpServerUpdateEnabled,ParameterValue=false \
    ParameterKey=McpServerDeleteEnabled,ParameterValue=false \
    ParameterKey=McpServerFunctionImportEnabled,ParameterValue=false \
    ParameterKey=UseSapCatalog,ParameterValue=true \
    ParameterKey=McpServerCustomCatalogBucketUri,ParameterValue=None \
    ParameterKey=McpServerServiceHintsS3Uri,ParameterValue=None \
    ParameterKey=AllowedServicePrefixes,ParameterValue=None \
    ParameterKey=McpServerVpcSecurityGroup,ParameterValue=<your-security-group-id> \
    ParameterKey=McpServerNetworkSubnets,ParameterValue=<your-subnet-ids>
```

**Note**  
 `USER_FEDERATION` does not require `SapCredentialsSecret`. `AppCallbackEndpoint` is required for this flow only.

## Example: On-Behalf-Of Token Exchange Deployment
<a name="deploy-obo-token-exchange-auth"></a>

```
aws cloudformation create-stack \
  --stack-name <your-stack-name> \
  --template-url https://awsforsap-mcp-server-setup-<region>.s3.<region>.amazonaws.com/cfn-launch-template/latest/AwsForSapMcpServerStack.template.json \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
  --parameters \
    ParameterKey=UniqueId,ParameterValue=<your-unique-id> \
    ParameterKey=SapBaseUrl,ParameterValue=<your-sap-base-url> \
    ParameterKey=SapSystemType,ParameterValue=S4HANA \
    ParameterKey=SapClientNumber,ParameterValue=<your-client-number> \
    ParameterKey=InboundAuthProvider,ParameterValue=EntraId \
    ParameterKey=DiscoveryUrl,ParameterValue=<your-discovery-url> \
    ParameterKey=AllowedAudiences,ParameterValue=<your-allowed-audiences> \
    ParameterKey=AuthFlow,ParameterValue=ON_BEHALF_OF_TOKEN_EXCHANGE \
    ParameterKey=SapCredentialsSecret,ParameterValue=<your-secret-name> \
    ParameterKey=OauthScopes,ParameterValue=<your-oauth-scopes> \
    ParameterKey=McpServerLogLevel,ParameterValue=INFO \
    ParameterKey=McpServerReadEnabled,ParameterValue=true \
    ParameterKey=McpServerWriteEnabled,ParameterValue=false \
    ParameterKey=McpServerCreateEnabled,ParameterValue=false \
    ParameterKey=McpServerUpdateEnabled,ParameterValue=false \
    ParameterKey=McpServerDeleteEnabled,ParameterValue=false \
    ParameterKey=McpServerFunctionImportEnabled,ParameterValue=false \
    ParameterKey=UseSapCatalog,ParameterValue=true \
    ParameterKey=McpServerCustomCatalogBucketUri,ParameterValue=None \
    ParameterKey=McpServerServiceHintsS3Uri,ParameterValue=None \
    ParameterKey=AllowedServicePrefixes,ParameterValue=None \
    ParameterKey=McpServerVpcSecurityGroup,ParameterValue=<your-security-group-id> \
    ParameterKey=McpServerNetworkSubnets,ParameterValue=<your-subnet-ids>
```

**Note**  
 `ON_BEHALF_OF_TOKEN_EXCHANGE` requires `SapCredentialsSecret`, `DiscoveryUrl`, and `AllowedAudiences`. `AppCallbackEndpoint` and `SapAuthorizeUrl`/`SapTokenUrl` are not required for this flow.

## What to expect
<a name="deploy-expected-outcome"></a>

After a successful deployment, you have a Bedrock AgentCore runtime with AWS for SAP MCP Server installed. Your MCP clients (AI agents) can communicate with the server over Streamable HTTP through the AgentCore invocation endpoint. You can find the invocation endpoint in the CloudFormation stack **Outputs** tab after the stack reaches `CREATE_COMPLETE`.

## Troubleshooting deployment failures
<a name="deploy-troubleshooting"></a>

If the CloudFormation stack creation fails (status `CREATE_FAILED` or `ROLLBACK_COMPLETE`), open the AWS CloudFormation console, select your stack, and choose the **Events** tab. The events list shows each resource creation attempt in chronological order. Look for the first event with a `CREATE_FAILED` status to identify the root cause. Common failure reasons include invalid parameter values or insufficient IAM permissions.

 **Private IdP connectivity failure:** If the stack fails while creating the OAuth credential provider or the Runtime, check that the specified subnets can reach the IdP’s discovery and token endpoints over HTTPS. Verify that the security groups permit outbound traffic on the IdP’s port. For managed Lattice, also verify that the deployer has `iam:CreateServiceLinkedRole` permission. For more information, see [Troubleshooting](troubleshooting.md).