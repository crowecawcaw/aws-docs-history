

# Get started with AWS Agent Registry
<a name="registry-get-started"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

In this guide, you’ll create your first registry, add a record, approve it, and search for it.

## Prerequisites
<a name="registry-get-started-prereqs"></a>

Complete the steps in [Prerequisites](registry-prerequisites.md).

## Step 1: Create a registry
<a name="registry-get-started-step1"></a>

Create a registry with IAM authorization and manual approval.

### Console
<a name="registry-get-started-step1-console"></a>

#### Creating a registry with IAM-based authorization
<a name="_creating_a_registry_with_iam_based_authorization"></a>

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**.

1. In the **Registries** section, choose **Create registry**.

1. In the **Registry details** section, for **Name**, enter a name for your registry. The name must start with an alphanumeric character. Valid characters are a–z, A–Z, 0–9, `_` (underscore), `-` (hyphen), `.` (period), and `/` (forward slash). The name can have up to 64 characters.

1. (Optional) Choose **Additional details** to expand the section, and then for **Description**, enter a description to help identify this registry.

1. In the **Discovery Authorization** section, for **Auth type**, choose **Use IAM Authorization** (inbound authorization).

1. In the **Record approval** section, turn on or turn off **Auto-approval**:
   + When **Auto-approval** is on, when you submit a record for approval, the record moves directly to **Approved** status and becomes visible in search results shortly after.
   + When **Auto-approval** is off, when you submit a record for approval, the record moves to **Pending approval** status and requires a curator to review and approve it before it’s published.

1. (Optional) In the **Tags** section, choose **Add new tag** to attach one or more tags to the registry. Each tag has a key and an optional value.

1. Choose **Create registry**.

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**.

1. In the **Registries** section, choose **Create registry**.

1. In the **Registry details** section, for **Name**, enter a name for your registry. The name must start with an alphanumeric character. Valid characters are a–z, A–Z, 0–9, `_` (underscore), `-` (hyphen), `.` (period), and `/` (forward slash). The name can have up to 64 characters.

1. (Optional) Choose **Additional details** to expand the section, and then for **Description**, enter a description to help identify this registry.

1. In the **Search API Authorization** section, for **Auth type**, choose **Use IAM Authorization** (inbound authorization).

1. In the **Record approval** section, turn on or turn off **Auto-approval**:
   + When **Auto-approval** is on, when you submit a record for approval, the record moves directly to **Approved** status and becomes visible in search results shortly after.
   + When **Auto-approval** is off, when you submit a record for approval, the record moves to **Pending approval** status and requires a curator to review and approve it before it’s published.

1. Choose **Create registry**.

#### Creating a registry with JWT-based authorization
<a name="_creating_a_registry_with_jwt_based_authorization"></a>

Identity provider authorization uses JSON Web Tokens (JWT) to control access to the registry’s discoverable data-plane APIs and MCP endpoint. You can use Amazon Cognito to quickly set up authorization, or bring your own identity provider to enable OAuth 2.0.

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**.

1. In the **Registries** section, choose **Create registry**.

1. In the **Registry details** section, for **Name**, enter a name for your registry. The name must start with an alphanumeric character. Valid characters are a–z, A–Z, 0–9, `_` (underscore), `-` (hyphen), `.` (period), and `/` (forward slash). The name can have up to 64 characters.

1. (Optional) Choose **Additional details** to expand the section, and then for **Description**, enter a description to help identify this registry.

1. In the **Discovery Authorization** section, for **Auth type**, choose **Use JSON Web Tokens (JWT)** (inbound authorization).

1. For **JWT schema configuration**, choose one of the following options:

   1.  **Quick create configurations with Cognito (recommended)** – AWS Agent Registry creates the authorization configurations on your behalf using Amazon Cognito as the identity provider. No additional configuration is required.

   1.  **Use existing Identity provider configurations** – Bring your own identity provider to enable OAuth 2.0. If you choose this option, complete the following steps:

      1. For **Discovery URL**, enter the discovery URL from your identity provider. AWS Agent Registry uses this URL to automatically fetch the login, token, and verification settings for your provider. You can find this URL in your identity provider’s dashboard or documentation (for example, `https://cognito-identity.amazonaws.com/.well-known/openid-configuration`).
**Note**  
The discovery URL cannot be changed after the registry is created.

      1. (Optional) Under **JWT authorization configuration**, select **Allowed audiences** to provide a list of permitted audiences that AWS Agent Registry validates against the `aud` claim in the JWT token. An audience claim (`aud`) in OAuth 2.0 specifies which resource server (API) the token is intended for. This ensures the token is the correct recipient before processing the request, preventing a token from being reused at a different API it was not issued for.

      1. (Optional) Select **Allowed clients** to provide a list of permitted client identifiers that AWS Agent Registry validates against the `client_id` claim in the JWT token. A `client_id` is a public, unique identifier for an application that is requesting access tokens to access the registry’s discoverable data-plane APIs or MCP endpoint. If you enable this option, enter one or more client IDs in the **Clients** field, and then choose **Add client** to add additional clients.

      1. (Optional) Select **Allowed scopes** to provide a list of permitted permissions, defined as scopes. If configured, at least one scope value in the incoming token must match one of the configured values. Scopes act as permissions to limit what an application can do.

      1. (Optional) Select **Custom claims** to provide a set of rules that match specific claims in the incoming token against predefined values. For each rule, specify the claim name, the value type (**STRING** or **STRING\_ARRAY**), and the required match value.

1. In the **Record approval** section, turn on or turn off **Auto-approval**:

   1. When **Auto-approval** is on, when you submit a record for approval, the record moves directly to **Approved** status and becomes immediately visible in search results.

   1. When **Auto-approval** is off, when you submit a record for approval, the record moves to **Pending approval** status and requires a registry admin to review and approve it before it’s published.

1. (Optional) In the **Tags** section, choose **Add new tag** to attach one or more tags to the registry. Each tag has a key and an optional value.

1. Choose **Create registry**.

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**.

1. In the **Registries** section, choose **Create registry**.

1. In the **Registry details** section, for **Name**, enter a name for your registry. The name must start with an alphanumeric character. Valid characters are a–z, A–Z, 0–9, `_` (underscore), `-` (hyphen), `.` (period), and `/` (forward slash). The name can have up to 64 characters.

1. (Optional) Choose **Additional details** to expand the section, and then for **Description**, enter a description to help identify this registry.

1. In the **Search API Authorization** section, for **Auth type**, choose **Use JSON Web Tokens (JWT)** (inbound authorization).

1. For **JWT schema configuration**, choose one of the following options:

   1.  **Quick create configurations with Cognito (recommended)** – AWS Agent Registry creates the authorization configurations on your behalf using Amazon Cognito as the identity provider. No additional configuration is required.

   1.  **Use existing Identity provider configurations** – Bring your own identity provider to enable OAuth 2.0. If you choose this option, complete the following steps:

      1. For **Discovery URL**, enter the discovery URL from your identity provider. AWS Agent Registry uses this URL to automatically fetch the login, token, and verification settings for your provider. You can find this URL in your identity provider’s dashboard or documentation (for example, `https://cognito-identity.amazonaws.com/.well-known/openid-configuration`).
**Note**  
The discovery URL cannot be changed after the registry is created.

      1. (Optional) Under **JWT authorization configuration**, select **Allowed audiences** to provide a list of permitted audiences that AWS Agent Registry validates against the `aud` claim in the JWT token. An audience claim (`aud`) in OAuth 2.0 specifies which resource server (API) the token is intended for. This ensures the token is the correct recipient before processing the request, preventing a token from being reused at a different API it was not issued for.

      1. (Optional) Select **Allowed clients** to provide a list of permitted client identifiers that AWS Agent Registry validates against the `client_id` claim in the JWT token. A `client_id` is a public, unique identifier for an application that is requesting access tokens to access the registry’s search API. If you enable this option, enter one or more client IDs in the **Clients** field, and then choose **Add client** to add additional clients.

      1. (Optional) Select **Allowed scopes** to provide a list of permitted permissions, defined as scopes. If configured, at least one scope value in the incoming token must match one of the configured values. Scopes act as permissions to limit what an application can do.

      1. (Optional) Select **Custom claims** to provide a set of rules that match specific claims in the incoming token against predefined values. For each rule, specify the claim name, the value type (**STRING** or **STRING\_ARRAY**), and the required match value.

1. In the **Record approval** section, turn on or turn off **Auto-approval**:

   1. When **Auto-approval** is on, when you submit a record for approval, the record moves directly to **Approved** status and becomes immediately visible in search results.

   1. When **Auto-approval** is off, when you submit a record for approval, the record moves to **Pending approval** status and requires a registry admin to review and approve it before it’s published.

1. Choose **Create registry**.

**Note**  
\* At least one **JWT authorization configuration** field is required: allowed audiences, allowed clients, allowed scopes, or custom claims. If you configure more than one, AWS Agent Registry verifies all of them. \* The discovery URL cannot be changed after the registry is created. \* The authorization type (IAM or JWT) cannot be changed after the registry is created. \* A registry supports only one form of inbound authorization type at a time — IAM SigV4 or JWT Bearer Token. You cannot use both simultaneously. Search via IAM is only supported via IAM-based registry; and search via Oauth is only supported via Oauth based registry.

After creating the registry, the console navigates to the registry details page. The registry status is initially **Creating** . AWS Agent Registry assigns the registry an ARN, which you can find in the **Registry details** section. The registry status changes to **Ready** after provisioning is complete. You can add records to the registry when its status is **Ready**.

### AWS CLI
<a name="registry-get-started-step1-cli"></a>

**Example**  

```
aws agent-registry-control create-registry \
  --name "MyFirstRegistry" \
  --description "My first Agent Registry" \
  --region us-east-1
```

```
aws bedrock-agentcore-control create-registry \
  --name "MyFirstRegistry" \
  --description "My first Agent Registry" \
  --region us-east-1
```

The registry status starts as CREATING and transitions to READY when provisioning completes.

### AWS SDK
<a name="registry-get-started-step1-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.create_registry(
    name='my-agent-registry',
    description='My first Agent Registry'
)
print(response['registryArn'])
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.create_registry(
    name='my-agent-registry',
    description='My first Agent Registry'
)
print(response['registryArn'])
```

## Step 2: Add a registry record
<a name="registry-get-started-step2"></a>

Create a record for an MCP server in your registry.

### Console
<a name="registry-get-started-step2-console"></a>

A registry record represents an agent, tool, skill, or custom resource.

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the name of the registry where you want to add a record.

1. In the **Registry records** section, choose **Create record**.

1. Choose a source type:

   1.  **Synchronize from endpoint** — Provide an endpoint URL and optional credentials to fetch metadata from an MCP server or Agent (A2A) endpoint. See [Synchronize records from external sources](registry-sync-records.md) for details.

   1.  **Manual** — Manually configure the record details and protocol configuration. Continue with the steps below.

1. In the **Record details** section, for **Name**, enter a unique name for the record. The name must be unique within the registry — the combination of `Name` and `Record version` must be unique. The name must start with an alphanumeric character. Valid characters are a–z, A–Z, 0–9, `_` (underscore), `-` (hyphen), `.` (period), and `/` (forward slash). The name can have up to 255 characters.

1. (Optional) For **Display name**, enter a human-readable label for the record. This appears in the registry records table and search results alongside the record’s technical name.

1. (Optional) For **Description**, enter a description for the record. The description can be 1 to 4,096 characters.

1. For **Record version**, enter a version identifier for the record (for example, `1.0.0` or `v2.1`).

1. In the **Record type and descriptor** section:

   1. Under **Type**, select the semantic type of the record. The type determines which primary descriptor keys are valid.
      +  **MCP** – Protocol designed for AI tool and agent communications. Handles context management and structured message formats.
      +  **Agent** – Protocol designed for secure agent-to-agent interactions. Enables distributed workflows and information exchange.
      +  **Skills** – Register agent skills with markdown documentation and an optional structured definition.
      +  **Custom** – Custom protocol implementation for specialized communication patterns. Define your own interface specification and integration requirements.

   1. Under **Descriptor**, choose the shape of the record’s descriptor data. Available options depend on the **Type** you selected:
      +  **MCP** → **MCP server** or **Custom** 
      +  **Agent** → **A2A Agent Card**, **MCP server**, or **Custom** 
      +  **Skills** → **Agent skills definition** or **Custom** 
      +  **Custom** → **Custom** 

1. A descriptor-specific editor appears based on your **Descriptor** selection:

   1.  **MCP server** – Select a schema version from the **Schema version** dropdown (for example, `2025-12-11`), and enter your [Model Context Protocol registry](https://registry.modelcontextprotocol.io/) server.json from the Model Context Protocol website in the **Your MCP server definition** editor. The definition must comply with the official MCP server schema for the selected version. To view the official schema as a reference, turn on **Show official schema**. (Optional) Select **Add tool definition** to add tools available on this server with their input parameters, outputs, and usage examples. Select a schema version (for example, `2025-11-25`) and enter your tool definition in the **Your Tool definition** editor.

   1.  **A2A Agent Card** – The schema version is `0.3`. Enter your agent card definition in the editor. To view the official schema as a reference, turn on **Show official schema**.

   1.  **Agent skills definition** – For **Skill documentation**, enter the markdown that describes this skill. (Optional) Select **Include skill definition** to add a structured definition. Select a schema version and enter the definition as a JSON object.

   1.  **Custom** – Enter your custom definition as a JSON object.

1. (Optional) In the **Tags** section, choose **Add new tag** to attach one or more tags to the record. Each tag has a key and an optional value.

1. Choose **Create record**.

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the name of the registry where you want to add a record.

1. In the **Registry records** section, choose **Create record**.

1. Choose a source type:

   1.  **Synchronize from endpoint** — Provide an endpoint URL and optional credentials to fetch metadata from an MCP server or Agent (A2A) endpoint. See [Synchronize records from external sources](registry-sync-records.md) for details.

   1.  **Manual** — Manually configure the record details and protocol configuration. Continue with the steps below.

1. In the **Record details** section, for **Name**, enter a name for the record. The name must start with an alphanumeric character. Valid characters are a–z, A–Z, 0–9, `_` (underscore), `-` (hyphen), `.` (period), and `/` (forward slash). The name can have up to 255 characters.

1. (Optional) For **Description**, enter a description for the record. The description can be 1 to 4,096 characters.

1. For **Record version**, enter a version identifier for the record (for example, `1.0.0` or `v2.1`).

1. In the **Record type** section, choose the type that matches your resource:

   1.  **MCP** – Protocol designed for AI tool and agent communications. Handles context management and structured message formats. If you choose this type, complete the following steps:

      1. In the **MCP server definition** section, select a schema version from the **Schema version** dropdown (for example, `2025-12-11`), and then enter [Model Context Protocol registry](https://registry.modelcontextprotocol.io/) server.json from the Model Context Protocol website in the **Your MCP server definition** editor. The definition must comply with the official MCP server schema for the selected version. To view the official schema as a reference, turn on **Show official schema**.

      1. (Optional) Select **Add tool definition** to add specific tools available on this server with their input parameters, outputs, and usage examples to enhance discoverability. If you select this option, select a schema version from the **Schema version** dropdown (for example, `2025-11-25`), and then enter your tool definition in the **Your Tool definition** editor. To view the official tool schema as a reference, turn on **Show official schema**.

   1.  **Agent** – Protocol designed for secure agent-to-agent interactions. Enables distributed workflows and information exchange. If you choose this type, the schema version is `0.3`. Enter your agent card definition in the editor. To view the official schema as a reference, turn on **Show official schema**.

   1.  **Agent Skills** – Register agent skills with markdown documentation and an optional structured definition. If you choose this type, complete the following steps:

      1. For **Skill documentation**, enter the markdown documentation that describes this skill.

      1. (Optional) Select **Include skill definition** to add a structured definition. If you select this option, select a schema version from the **Schema version** dropdown, and then enter the skill definition as a JSON object in the editor.

   1.  **Custom** – Custom protocol implementation for specialized communication patterns. Define your own interface specification and integration requirements. If you choose this type, enter your custom definition as a JSON object in the editor.

1. Choose **Create record**.

**Note**  
To add a server or agent to the registry that does not conform to the standard MCP or A2A protocol schemas, use the Custom record type.

After you choose Create record, AWS Agent Registry begins provisioning the record. The record status is initially Creating. When provisioning is complete, the status changes to Draft. To make the record available for others to discover, submit it for approval. For more information, see [Step 3: Submit the record for approval](#registry-get-started-step3).

### AWS CLI
<a name="registry-get-started-step2-cli"></a>

**Example**  

```
aws agent-registry-control create-registry-record \
  --registry-id <registryId> \
  --name "weather-server" \
  --display-name "WeatherServer" \
  --record-type MCP \
  --descriptors '{"mcpServer": {"data": "{\"name\": \"weather/mcp-server\", \"description\": \"Weather data service\", \"version\": \"1.0.0\"}", "dataSchemaVersion": "2025-12-11"}}' \
  --record-version "1.0" \
  --region us-east-1
```

```
aws bedrock-agentcore-control create-registry-record \
  --registry-id <registryId> \
  --name "WeatherServer" \
  --descriptor-type MCP \
  --descriptors '{"mcp": {"server": {"inlineContent": "{\"name\": \"weather/mcp-server\", \"description\": \"Weather data service\", \"version\": \"1.0.0\"}"}}}' \
  --record-version "1.0" \
  --region us-east-1
```

The record is created in CREATING status and transitions to DRAFT when processing completes. For more AWS CLI examples for creating records of other types, refer to the [Create and manage records](registry-create-manage-records.md) section.

### AWS SDK
<a name="registry-get-started-step2-sdk"></a>

**Example**  

```
import boto3
import json

client = boto3.client('agent-registry-control')

server_content = json.dumps({
    "name": "io.example/weather-server",
    "description": "A weather MCP server",
    "version": "1.0.0"
})

tools_content = json.dumps({
    "tools": [{
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "inputSchema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name"
                }
            },
            "required": ["location"]
        }
    }]
})

response = client.create_registry_record(
    registryId='<registryId>',
    name='my-mcp-server',
    displayName='My MCP Server',
    recordType='MCP',
    descriptors={
        'mcpServer': {
            'data': server_content,
            'dataSchemaVersion': '2025-12-11',
            'additionalData': {
                'tools': {
                    'data': tools_content,
                    'dataSchemaVersion': '2024-11-05'
                }
            }
        }
    },
    recordVersion='1.0'
)
print(f"Record ARN: {response['recordArn']}")
print(f"Status: {response['status']}")  # CREATING
```

```
import boto3
import json

client = boto3.client('bedrock-agentcore-control')

server_content = json.dumps({
    "name": "io.example/weather-server",
    "description": "A weather MCP server",
    "version": "1.0.0"
})

tools_content = json.dumps({
    "tools": [{
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "inputSchema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name"
                }
            },
            "required": ["location"]
        }
    }]
})

response = client.create_registry_record(
    registryId='<registryId>',
    name='my-mcp-server',
    descriptorType='MCP',
    descriptors={
        'mcp': {
            'server': {
                'schemaVersion': '2025-12-11',
                'inlineContent': server_content
            },
            'tools': {
                'protocolVersion': '2024-11-05',
                'inlineContent': tools_content
            }
        }
    },
    recordVersion='1.0'
)
print(f"Record ARN: {response['recordArn']}")
print(f"Status: {response['status']}")  # CREATING
```

## Step 3: Submit the record for approval
<a name="registry-get-started-step3"></a>

### Console
<a name="registry-get-started-step3-console"></a>

Submitting a record for approval starts the review process that makes the record available for discovery. You can submit a record from the registry records table or from the record details page.

 **To submit a record for approval from the registry records table** 

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry name.

1. In the **Registry records** section, select the record that you want to submit.

1. Choose **Update status**, and then choose **Submit for approval**.

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry name.

1. In the **Registry records** section, select the record that you want to submit.

1. Choose **Update status**, and then choose **Submit for approval**.

 **To submit a record for approval from the record details page** 

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry name.

1. In the **Registry records** section, choose the name of the record that you want to submit.

1. Choose **Update status**, and then choose **Submit for approval**.

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry name.

1. In the **Registry records** section, choose the name of the record that you want to submit.

1. Choose **Update status**, and then choose **Submit for approval**.

After you submit a record for approval, the record status changes based on the registry’s approval setting:
+ If the registry has **Auto-approval** turned on, the record status changes directly to **Approved** and becomes visible in search results shortly after.
+ If the registry has **Auto-approval** turned off, the record status changes to **Pending approval** and requires a registry admin to review and approve it before it’s published.

### AWS CLI
<a name="registry-get-started-step3-cli"></a>

**Example**  

```
aws agent-registry-control submit-registry-record-for-approval \
  --registry-id <registryId> \
  --record-id <recordId> \
  --region us-east-1
```

```
aws bedrock-agentcore-control submit-registry-record-for-approval \
  --registry-id <registryId> \
  --record-id <recordId> \
  --region us-east-1
```

The record moves to PENDING\_APPROVAL (or directly to APPROVED if auto-approval is enabled).

### AWS SDK
<a name="registry-get-started-step3-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.submit_registry_record_for_approval(
    registryId='<registryId>',
    recordId='<recordId>'
)
print(f"Record ARN: {response['recordArn']}")
print(f"Record ID: {response['recordId']}")
print(f"Status: {response['status']}")  # PENDING_APPROVAL or APPROVED
print(f"Updated At: {response['updatedAt']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.submit_registry_record_for_approval(
    registryId='<registryId>',
    recordId='<recordId>'
)
print(f"Record ARN: {response['recordArn']}")
print(f"Record ID: {response['recordId']}")
print(f"Status: {response['status']}")  # PENDING_APPROVAL or APPROVED
print(f"Updated At: {response['updatedAt']}")
```

## Step 4: Approve the record
<a name="registry-get-started-step4"></a>

### Console
<a name="registry-get-started-step4-console"></a>

 **To approve a record from the registry records table** 

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry name.

1. In the **Registry records** section, select the record that you want to approve.

1. Choose **Update status**, and then choose **Approve**.

1. In the confirmation dialog, enter a reason for the status change.

1. Choose **Confirm**.

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry name.

1. In the **Registry records** section, select the record that you want to approve.

1. Choose **Update status**, and then choose **Approve**.

1. In the confirmation dialog, enter a reason for the status change.

1. Choose **Confirm**.

 **To approve a record from the record details page** 

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry name.

1. In the **Registry records** section, choose the name of the record that you want to approve.

1. In record details page, choose **Update status**, and then choose **Approve**.

1. In the confirmation dialog, enter a reason for the status change.

1. Choose **Confirm**.

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry name.

1. In the **Registry records** section, choose the name of the record that you want to approve.

1. In record details page, choose **Update status**, and then choose **Approve**.

1. In the confirmation dialog, enter a reason for the status change.

1. Choose **Confirm**.

### AWS CLI
<a name="registry-get-started-step4-cli"></a>

**Example**  

```
aws agent-registry-control update-registry-record-status \
  --registry-id <registryId> \
  --record-id <recordId> \
  --status APPROVED \
  --status-reason "Reviewed and approved" \
  --region us-east-1
```

```
aws bedrock-agentcore-control update-registry-record-status \
  --registry-id <registryId> \
  --record-id <recordId> \
  --status APPROVED \
  --status-reason "Reviewed and approved" \
  --region us-east-1
```

### AWS SDK
<a name="registry-get-started-step4-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.update_registry_record_status(
    registryId='<registryId>',
    recordId='<recordId>',
    status='APPROVED',
    statusReason='Meets all requirements'
)
print(f"Record ARN: {response['recordArn']}")
print(f"Status: {response['status']}")  # APPROVED
print(f"Reason: {response['statusReason']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.update_registry_record_status(
    registryId='<registryId>',
    recordId='<recordId>',
    status='APPROVED',
    statusReason='Meets all requirements'
)
print(f"Record ARN: {response['recordArn']}")
print(f"Status: {response['status']}")  # APPROVED
print(f"Reason: {response['statusReason']}")
```

## Step 5: Discover approved records
<a name="registry-get-started-step5"></a>

The Record directory is the console page for browsing and searching approved records in a registry. When you select a registry on the Record directory page, the console automatically lists its approved records. From there you can page through the list, or use the search box to run a natural language query. Programmatically, use `ListDiscoverableRegistryRecords` to browse, `SearchDiscoverableRegistryRecords` to search, and `BatchGetDiscoverableRegistryRecord` to fetch full details for many records in one call.

### Console
<a name="registry-get-started-step5-console"></a>

**Note**  
Console-based discovery is available only for registries that use **Use IAM** as the authorization type. If your registry uses JSON Web Tokens (JWT), call the discoverable data-plane APIs directly using an HTTP client such as curl or Postman with a valid JWT Bearer Token in the request header. The AWS CLI and AWS SDKs use IAM SigV4 signing and cannot be used with JWT-authorized registries. For more details, see [Search for registry records](registry-search-records.md).

**Example**  
 **To browse or search approved records**   

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Record directory**.

1. Under **Registry**, select the registry whose approved records you want to explore. The page automatically lists all approved records in that registry.

1. (Optional) Toggle between **Card** and **Table** view in the top right of the page.

1. (Optional) In **Search approved records**, enter a natural language query or a name to narrow the results, then choose **Search**.

1. Choose a card or row to open the record’s full details.
The Record directory surfaces records in **Approved** status only. Records in Draft, Pending approval, Rejected, or Deprecated status don’t appear.
 **To search for registry records**   

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry name.

1. Choose the **Search records** tab.

1. In the **Search approved records** field, enter your search query.

1. (Optional) To filter results by a specific property, choose the search field to expand the **Properties** menu, and then choose a filter: **Name**, **Descriptor type**, or **Version**.

1. Choose **Search**.
Search returns only records in **Approved** status. Records in other states such as Draft, Pending approval, Rejected, or Deprecated status don’t appear in search results.

### AWS CLI
<a name="registry-get-started-step5-cli"></a>

 **Browse approved records** — list approved records in a registry:

```
aws agent-registry list-discoverable-registry-records \
  --registry-id "<registry-id>" \
  --region us-east-1
```

 **Search approved records** — run a hybrid semantic \+ keyword search:

**Example**  

```
aws agent-registry search-discoverable-registry-records \
  --search-query "weather" \
  --registry-ids "<registry-id>" \
  --region us-east-1
```

```
aws bedrock-agentcore search-registry-records \
  --search-query "weather" \
  --registry-ids "<registry-id>" \
  --region us-east-1
```

 **Retrieve full details for many records at once**:

```
aws agent-registry batch-get-discoverable-registry-record \
  --entries '[{"registryId": "<registry-id>", "recordIds": ["<recordId-1>", "<recordId-2>"]}]' \
  --region us-east-1
```

**Note**  
 `ListDiscoverableRegistryRecords` and `BatchGetDiscoverableRegistryRecord` are only available in the `agent-registry` namespace. They are not available in the `bedrock-agentcore` namespace.

### AWS SDK
<a name="registry-get-started-step5-sdk"></a>

 **Browse approved records**:

```
import boto3

client = boto3.client('agent-registry')

list_response = client.list_discoverable_registry_records(
    registryId='<registry-id>',
    maxResults=20
)
for record in list_response['registryRecords']:
    print(f"{record['displayName']} ({record['name']}) - {record['recordType']}")
```

 **Search approved records**:

**Example**  

```
import boto3

client = boto3.client('agent-registry')

response = client.search_discoverable_registry_records(
    registryIds=['arn:aws:agent-registry:us-east-1:<account>:registry/<registryId>'],
    searchQuery='weather forecast tool',
    maxResults=10
)
for record in response['registryRecords']:
    print(f"Record: {record['displayName']} ({record['recordId']})")
    print(f"  Name: {record['name']}")
    print(f"  Type: {record['recordType']}")
    print(f"  Status: {record['status']}")
    print(f"  Version: {record['recordVersion']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore')

response = client.search_registry_records(
    registryIds=['arn:aws:bedrock-agentcore:us-east-1:<account>:registry/<registryId>'],
    searchQuery='weather forecast tool',
    maxResults=10
)
for record in response['registryRecords']:
    print(f"Record: {record['name']} ({record['recordId']})")
    print(f"  Type: {record['descriptorType']}")
    print(f"  Status: {record['status']}")
    print(f"  Version: {record['version']}")
```

 **Retrieve full details for many records at once**:

```
batch_response = client.batch_get_discoverable_registry_record(
    entries=[{'registryId': '<registry-id>', 'recordIds': ['<recordId-1>', '<recordId-2>']}]
)
for record in batch_response['registryRecords']:
    print(f"{record['displayName']} ({record['name']}) - {record['recordType']}")
for err in batch_response['errors']:
    print(f"Error for {err['recordId']}: {err['errorCode']}")
```

## What you’ve built
<a name="registry-get-started-what-built"></a>
+ A **registry** with IAM authorization and manual approval
+ A **registry record** describing an MCP server
+ An **approved record** browsable and searchable through the Record directory

## Next steps
<a name="registry-get-started-next-steps"></a>
+ Build catalog-style discovery experiences on top of `ListDiscoverableRegistryRecords` and `BatchGetDiscoverableRegistryRecord` 
+ Set up Amazon EventBridge notifications to automate your approval workflow
+ Add more records for your agents, servers, skills, and custom resources