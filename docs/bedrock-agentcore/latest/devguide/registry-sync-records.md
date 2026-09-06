

# Synchronize records from external sources
<a name="registry-sync-records"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Overview
<a name="registry-sync-overview"></a>

 AWS Agent Registry can automatically synchronize record metadata from external sources by connecting to the provided URL with outbound credentials. When you provide a URL and credential provider (Optional for public resources that do not require any Authorization to access), the system extracts server and tool definitions and populates the record’s descriptors conforming to the official protocol schemas. It also updates the record’s name, description, and version if those values are found at the source.

## Synchronize from a public MCP server
<a name="registry-sync-public"></a>

For Public MCP servers that don’t require authentication or authorization:

### Console
<a name="registry-sync-public-console"></a>

**Example**  

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. Choose **Synchronize from endpoint**.

1. Under **Record details**, for **Type**, choose **MCP**. The **Descriptor** is set to **MCP server**.

1. For **Endpoint**, enter the public MCP server URL (e.g., `https://knowledge-mcp.global.api.aws`). Must be a valid HTTPS URL.

1. Under **Credential type**, choose **None**.

1. (Optional) In the **Tags** section, choose **Add new tag** to attach one or more tags to the record. Each tag has a key and an optional value.

1. Choose **Create record**.

1. Open the registry detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. Choose **Synchronize from endpoint**.

1. Under **Record details**, choose **MCP** as the record type.

1. For **Endpoint**, enter the public MCP server URL (e.g., `https://knowledge-mcp.global.api.aws`). Must be a valid HTTPS URL.

1. Under **Credential type**, choose **None**.

1. Choose **Create record**.

The record is created in CREATING status. The registry connects to the endpoint, extracts server and tool definitions, and populates the record’s descriptors. After synchronization completes, the record transitions to DRAFT. If synchronization fails, the record transitions to CREATE\_FAILED status with the error details available in the Status Reason field. For troubleshooting, see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors).

### AWS CLI
<a name="registry-sync-public-cli"></a>

**Example**  

```
aws agent-registry-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "aws-knowledge-server" \
  --display-name "AWS Knowledge Server" \
  --record-type MCP \
  --descriptors '{
    "mcpServer": {
      "source": {
        "fromUrl": {
          "url": "https://knowledge-mcp.global.api.aws"
        }
      }
    }
  }' \
  --region us-east-1
```

```
aws bedrock-agentcore-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "aws-knowledge-server" \
  --descriptor-type MCP \
  --synchronization-type URL \
  --synchronization-configuration '{
    "fromUrl":
    {
        "url": "https://knowledge-mcp.global.api.aws"
    }
  }' \
  --region us-east-1
```

### AWS SDK
<a name="registry-sync-public-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.create_registry_record(
    registryId='<registryId>',
    name='aws-knowledge-server',
    displayName='AWS Knowledge Server',
    recordType='MCP',
    descriptors={
        'mcpServer': {
            'source': {
                'fromUrl': {
                    'url': 'https://knowledge-mcp.global.api.aws'
                }
            }
        }
    }
)
print(f"Record ARN: {response['recordArn']}")
print(f"Status: {response['status']}")  # CREATING
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.create_registry_record(
    registryId='<registryId>',
    name='aws-knowledge-server',
    descriptorType='MCP',
    synchronizationType='URL',
    synchronizationConfiguration={
        'fromUrl': {
            'url': 'https://knowledge-mcp.global.api.aws'
        }
    }
)
print(f"Record ARN: {response['recordArn']}")
print(f"Status: {response['status']}")  # CREATING
```

**Note**  
In the `agent-registry` namespace, sync configuration moves inside each descriptor as `source` (only supported on `mcpServer` and `a2aAgentCard` primary descriptors). The top-level `synchronizationType`/`synchronizationConfiguration` fields no longer exist.

The record is created in CREATING status. The synchronization time varies from seconds to minutes, depending on the size of the metadata. After synchronization completes, it transitions to DRAFT with descriptors extracted from the MCP server, including server and tools definitions.

## Synchronize from an OAuth-protected MCP server
<a name="registry-sync-oauth"></a>

When the MCP server is protected by OAuth, you will need to create an M2M client on the authorization server, and then configure a [credential provider from AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/resource-providers.html) containing the client ID and secret allowlisted to invoke the MCP server. Once you have the credential provider, you can supply it to the registry for synchronization:

### Console
<a name="registry-sync-oauth-console"></a>

**Example**  

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. Choose **Synchronize from endpoint**.

1. Under **Record details**, for **Type**, choose **MCP**. The **Descriptor** is set to **MCP server**.

1. For **Endpoint**, enter the OAuth-protected MCP server URL. Must be a valid HTTPS URL.

1. Under **Credential type**, choose **OAuth**.

1. For **Credential provider**, select or enter the credential provider ARN from AgentCore Identity.

1. (Optional) Expand **Additional configuration** to configure:

   1.  **Scopes** — OAuth scopes to request when obtaining an access token.

   1.  **Custom parameters** — Additional key-value parameters for the OAuth token request.

1. (Optional) In the **Tags** section, choose **Add new tag** to attach one or more tags to the record. Each tag has a key and an optional value.

1. Choose **Create record**.

1. Open the registry detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. Choose **Synchronize from endpoint**.

1. Under **Record details**, choose **MCP** as the record type.

1. For **Endpoint**, enter the OAuth-protected MCP server URL. Must be a valid HTTPS URL.

1. Under **Credential type**, choose **OAuth**.

1. For **Credential provider**, select or enter the credential provider ARN from AgentCore Identity.

1. (Optional) Expand **Additional configuration** to configure:

   1.  **Scopes** — OAuth scopes to request when obtaining an access token.

   1.  **Custom parameters** — Additional key-value parameters for the OAuth token request.

1. Choose **Create record**.

The record is created in CREATING status. The registry connects to the endpoint using the OAuth credentials, extracts server and tool definitions, and populates the record’s descriptors. After synchronization completes, the record transitions to DRAFT. If synchronization fails, the record transitions to CREATE\_FAILED status with the error details available in the Status Reason field. For troubleshooting, see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors).

### AWS CLI
<a name="registry-sync-oauth-cli"></a>

**Example**  

```
aws agent-registry-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "oauth-mcp-server" \
  --display-name "OAuth MCP Server" \
  --record-type MCP \
  --descriptors '{
    "mcpServer": {
      "source": {
        "fromUrl": {
          "url": "$MCP_OAUTH_URL",
          "credentialProviderConfigurations": [
            {
              "credentialProviderType": "OAUTH",
              "credentialProvider": {
                "oauthCredentialProvider": {
                  "providerArn": "$OAUTH_PROVIDER_ARN",
                  "grantType": "CLIENT_CREDENTIALS"
                }
              }
            }
          ]
        }
      }
    }
  }' \
  --region us-east-1
```

```
aws bedrock-agentcore-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "oauth-mcp-server" \
  --descriptor-type MCP \
  --synchronization-type URL \
  --synchronization-configuration '{
    "fromUrl":
    {
        "url": "$MCP_OAUTH_URL",
        "credentialProviderConfigurations":
        [
            {
                "credentialProviderType": "OAUTH",
                "credentialProvider":
                {
                    "oauthCredentialProvider":
                    {
                        "providerArn": "$OAUTH_PROVIDER_ARN",
                        "grantType": "CLIENT_CREDENTIALS"
                    }
                }
            }
        ]
    }
  }' \
  --region us-east-1
```

 **Additional IAM permissions required:** 

**Note**  
These sync-related IAM permissions authorize workload identity and OAuth credential provider resources managed by AgentCore Identity. Those resources intentionally remain under the `bedrock-agentcore` namespace, so this policy does not change.

```
{
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetWorkloadAccessToken"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:workload-identity-directory/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetResourceOauth2Token"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:<region>:<account>:token-vault/default/oauth2credentialprovider/<oauthProviderName>"
            ]
        }
    ]
}
```

**Note**  
Scope the `GetResourceOauth2Token` statement to the specific OAuth credential provider ARN whose access token this role needs. Avoid wildcards in the provider segment of the ARN — patterns such as `token-vault/ ` or `token-vault/default/oauth2credentialprovider/` grant access to every OAuth credential provider in the account, which can enable cross-team credential access. Follow the principle of least privilege by naming the specific provider in the `Resource` field, for example `arn:aws:bedrock-agentcore:<region>:<account>:token-vault/default/oauth2credentialprovider/<oauthProviderName>`.

Limitations:
+ The caller of CreateRegistryRecord or UpdateRegistryRecord must have GetWorkloadAccessToken registry-associated workload identity and GetResourceOauth2Token permission on the credential provider.
+ The credential provider must be coming from the same account.

## Synchronize from an IAM-protected MCP server
<a name="registry-sync-iam"></a>

For MCP servers on Amazon Bedrock AgentCore Runtime or Amazon Bedrock AgentCore Gateway, specify an IAM role for SigV4 signing. The role must have permission to access the target service. For example: `bedrock-agentcore:InvokeAgentRuntime` or `bedrock-agentcore:InvokeAgentRuntimeForUser` on AgentCore Runtime; `bedrock-agentcore:InvokeGateway` on AgentCore Gateway.

Besides the IAM role, you must specify the `service` field for SigV4 signing. If your MCP runs on AgentCore Runtime or AgentCore Gateway, the value should be `agent-registry`. If your MCP runs on Amazon API Gateway, it should be `execute-api`, and if your MCP runs on AWS Lambda, it should be `lambda`.

 `region` value is optional. By default, the request will be signed with same region as the registry.

### Console
<a name="registry-sync-iam-console"></a>

**Example**  

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. Choose **Synchronize from endpoint**.

1. Under **Record details**, for **Type**, choose **MCP**. The **Descriptor** is set to **MCP server**.

1. For **Endpoint**, enter the IAM-protected MCP server URL. Must be a valid HTTPS URL.

1. Under **Credential type**, choose **IAM**.

1. For **Role ARN**, enter the IAM role ARN to assume for SigV4 signing.

1. For **Service**, enter the service name for SigV4 signing (for example, `agent-registry`, `execute-api`, `lambda`).

1. (Optional) Expand **Additional configuration** and choose a **Region** for SigV4 signing. If not specified, the registry’s own region is used.

1. (Optional) In the **Tags** section, choose **Add new tag** to attach one or more tags to the record. Each tag has a key and an optional value.

1. Choose **Create record**.

1. Open the registry detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. Choose **Synchronize from endpoint**.

1. Under **Record details**, choose **MCP** as the record type.

1. For **Endpoint**, enter the IAM-protected MCP server URL. Must be a valid HTTPS URL.

1. Under **Credential type**, choose **IAM**.

1. For **Role ARN**, enter the IAM role ARN to assume for SigV4 signing.

1. For **Service**, enter the service name for SigV4 signing (e.g., `bedrock-agentcore`, `execute-api`, `lambda`).

1. (Optional) Expand **Additional configuration** and choose a **Region** for SigV4 signing. If not specified, the registry’s own region is used.

1. Choose **Create record**.

The record is created in CREATING status. The registry connects to the endpoint using IAM credentials, extracts server and tool definitions, and populates the record’s descriptors. After synchronization completes, the record transitions to DRAFT. If synchronization fails, the record transitions to CREATE\_FAILED status with the error details available in the Status Reason field. For troubleshooting, see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors).

### AWS CLI
<a name="registry-sync-iam-cli"></a>

**Example**  

```
aws agent-registry-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "gateway-mcp-server" \
  --display-name "Gateway MCP Server" \
  --record-type MCP \
  --descriptors '{
    "mcpServer": {
      "source": {
        "fromUrl": {
          "url": "$MCP_IAM_URL",
          "credentialProviderConfigurations": [
            {
              "credentialProviderType": "IAM",
              "credentialProvider": {
                "iamCredentialProvider": {
                  "roleArn": "$IAM_ROLE_ARN",
                  "service": "$SIGNING_SERVICE",
                  "region": "$SIGNING_REGION"
                }
              }
            }
          ]
        }
      }
    }
  }' \
  --region us-east-1
```

```
aws bedrock-agentcore-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "gateway-mcp-server" \
  --descriptor-type MCP \
  --synchronization-type URL \
  --synchronization-configuration '{
    "fromUrl":
    {
        "url": "$MCP_IAM_URL",
        "credentialProviderConfigurations":
        [
            {
                "credentialProviderType": "IAM",
                "credentialProvider":
                {
                    "iamCredentialProvider":
                    {
                        "roleArn": "$IAM_ROLE_ARN",
                        "service": "$SIGNING_SERVICE",
                        "region": "$SIGNING_REGION"
                    }
                }
            }
        ]
    }
  }' \
  --region us-east-1
```

 **Additional IAM permissions required:** 

**Note**  
This `iam:PassRole` policy authorizes registry to hand off a role to AgentCore Identity for outbound sync. The `iam:PassedToService` condition value `bedrock-agentcore.amazonaws.com` refers to the AgentCore Identity service principal and does not change.

```
{
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "iam:PassRole"
            ],
            "Resource":
            [
                "arn:aws:iam::<account>:role/<sync-role>"
            ],
            "Condition":
            {
                "StringEquals":
                {
                    "iam:PassedToService": "bedrock-agentcore.amazonaws.com"
                }
            }
        }
    ]
}
```

## Synchronize from an A2A agent card
<a name="registry-sync-a2a"></a>

Provide the agent card URL or the agent’s base URL where `.well-known/agent-card.json` can be discovered:

### Console
<a name="registry-sync-a2a-console"></a>

**Example**  

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. Choose **Synchronize from endpoint**.

1. Under **Record details**, for **Type**, choose **Agent**. The **Descriptor** is set to **A2A Agent Card**.

1. For **Endpoint**, enter the agent card URL (e.g., `https://agent.example.com/.well-known/agent-card.json`). Must be a valid HTTPS URL.

1. Under **Credential type**, choose the appropriate authorization method:

   1.  **None** — For publicly accessible agent cards.

   1.  **IAM** — For agents hosted on AgentCore Runtime or Gateway. Provide the **Role ARN** and **Service** name.

   1.  **OAuth** — For OAuth-protected agents. Select or enter the **Credential provider** ARN.

1. (Optional) In the **Tags** section, choose **Add new tag** to attach one or more tags to the record. Each tag has a key and an optional value.

1. Choose **Create record**.

1. Open the registry detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. Choose **Synchronize from endpoint**.

1. Under **Record details**, choose **Agent** as the record type.

1. For **Endpoint**, enter the agent card URL (e.g., `https://agent.example.com/.well-known/agent-card.json`). Must be a valid HTTPS URL.

1. Under **Credential type**, choose the appropriate authorization method:

   1.  **None** — For publicly accessible agent cards.

   1.  **IAM** — For agents hosted on AgentCore Runtime or Gateway. Provide the **Role ARN** and **Service** name.

   1.  **OAuth** — For OAuth-protected agents. Select or enter the **Credential provider** ARN.

1. Choose **Create record**.

The record is created in CREATING status. The registry connects to the endpoint, extracts the agent card metadata, and populates the record’s descriptors. After synchronization completes, the record transitions to DRAFT. If synchronization fails, the record transitions to CREATE\_FAILED status with the error details available in the Status Reason field. For troubleshooting, see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors).

### AWS CLI
<a name="registry-sync-a2a-cli"></a>

**Example**  

```
aws agent-registry-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "travel-agent" \
  --display-name "Travel Agent" \
  --record-type AGENT \
  --descriptors '{
    "a2aAgentCard": {
      "source": {
        "fromUrl": {
          "url": "https://agent.example.com/.well-known/agent-card.json"
        }
      }
    }
  }' \
  --region us-east-1
```

```
aws bedrock-agentcore-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "travel-agent" \
  --descriptor-type A2A \
  --synchronization-type URL \
  --synchronization-configuration '{"fromUrl": {"url": "https://agent.example.com/.well-known/agent-card.json"}}' \
  --region us-east-1
```

You can also specify credential providers for A2A synchronization, for example you can synchronize from an agent hosted on AgentCore. Use `agent-registry` as the `service` field when the sync target is an agent hosted on AgentCore Runtime or Gateway.

**Example**  

```
aws agent-registry-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "a2a_agent_record" \
  --display-name "A2A Agent Record" \
  --record-type AGENT \
  --descriptors "{
    \"a2aAgentCard\": {
      \"source\": {
        \"fromUrl\": {
          \"url\": \"$A2A_URL\",
          \"credentialProviderConfigurations\": [{
            \"credentialProviderType\": \"IAM\",
            \"credentialProvider\": {
              \"iamCredentialProvider\": {
                \"roleArn\": \"$IAM_INVOKER_ROLE\",
                \"service\": \"agent-registry\"
              }
            }
          }]
        }
      }
    }
  }"
```

```
aws bedrock-agentcore-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "a2a_agent_record" \
  --descriptor-type A2A \
  --synchronization-type URL \
  --synchronization-configuration "{
    \"fromUrl\": {
        \"url\": \"$A2A_URL\",
        \"credentialProviderConfigurations\": [{
            \"credentialProviderType\": \"IAM\",
            \"credentialProvider\": {
                \"iamCredentialProvider\": {
                    \"roleArn\": \"$IAM_INVOKER_ROLE\",
                    \"service\": \"bedrock-agentcore\"
                }
            }
        }]
    }
  }"
```

## Trigger synchronization on an existing record
<a name="registry-sync-trigger"></a>

### Console
<a name="registry-sync-trigger-console"></a>

1. Open the record detail page for an MCP or Agent record that has synchronization configured.

**Example**  

1. From the record detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#), choose **Manage**, then choose **Synchronization**.

1. In the confirmation dialog, review the message that syncing will revert the record to draft state.

1. Choose **Sync** to confirm.
Alternatively, you can trigger synchronization during editing:  

1. From the record detail page, choose **Manage**, then choose **Edit**.

1. Under **Synchronize from endpoint**, select the **Re-sync from endpoint** checkbox.

1. Choose **Save changes**.

1. From the record detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#), choose the **Sync** button in the header actions.

1. In the confirmation dialog, review the message that syncing will revert the record to draft state.

1. Choose **Sync** to confirm.
Alternatively, you can trigger synchronization during editing:  

1. From the record detail page, choose the three-dot menu (⋮), then choose **Edit**.

1. Under **Synchronize from endpoint**, select the **Re-sync from endpoint** checkbox.

1. Choose **Save changes**.

The record transitions to UPDATING status during synchronization. After completion, it returns to DRAFT with updated descriptors from the source. If synchronization fails, the record transitions to UPDATE\_FAILED status with the error details available in the Status Reason field. For troubleshooting, see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors).

### AWS CLI
<a name="registry-sync-trigger-cli"></a>

**Example**  

```
aws agent-registry-control update-registry-record \
  --registry-id $REGISTRY_ID \
  --record-id $RECORD_ID \
  --trigger-synchronization \
  --region us-east-1
```

```
aws bedrock-agentcore-control update-registry-record \
  --registry-id $REGISTRY_ID \
  --record-id $RECORD_ID \
  --trigger-synchronization \
  --region us-east-1
```

### AWS SDK
<a name="registry-sync-trigger-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    triggerSynchronization=True
)
print(f"Status: {response['status']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    triggerSynchronization=True
)
print(f"Status: {response['status']}")
```

**Note**  
If the record is in a non-DRAFT status (e.g., APPROVED), the update creates a new DRAFT revision. The approved revision remains discoverable.

 **Troubleshooting** : see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors).