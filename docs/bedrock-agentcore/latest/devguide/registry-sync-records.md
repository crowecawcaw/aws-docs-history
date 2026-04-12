# Synchronize records from external sources

## Overview

AWS Agent Registry can automatically synchronize record metadata from external sources by connecting to the provided URL with outbound credentials. When you provide a URL and credential provider (Optional for public resources that do not require any Authorization to access), the system extracts server and tool definitions and populates the record’s descriptors conforming to the official protocol schemas. It also updates the record’s name, description, and version if those values are found at the source.

###### Note

At public preview launch, SSE stream from MCP server is not supported yet.

## Synchronize from a public MCP server

For Public MCP servers that don’t require authentication or authorization:

### AWS CLI

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

The record is created in CREATING status. The synchronization time varies from seconds to minutes, depending on the size of the metadata. After synchronization completed, it transitions to DRAFT with descriptors extracted from the MCP server, including server and tools definitions.

## Synchronize from an OAuth-protected MCP server

When the MCP server is protected by OAuth, you will need to create an M2M client on the authorization server, and then configure a [credential provider from AgentCore Identity](resource-providers.md "resource-providers.md") containing the client ID and secret allowlisted to invoke the MCP server. Once you have the credential provider, you can supply it to the registry for synchronization:

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
                "arn:aws:bedrock-agentcore:*:<account>:token-vault/*"
            ]
        }
    ]
}
```

Limitations:

- The caller of CreateRegistryRecord or UpdateRegistryRecord must have GetWorkloadAccessToken registry-associated workload identity and GetResourceOauth2Token permission on the credential provider.
- The credential provider must be coming from the same account.

## Synchronize from an IAM-protected MCP server

For MCP servers on AgentCore Runtime or AgentCore Gateway, specify an IAM role for SigV4 signing. The role must have permission to access the target service. For example: `bedrock-agentcore:InvokeAgentRuntime` or `bedrock-agentcore:InvokeAgentRuntimeForUser` on AgentCore Runtime; `bedrock-agentcore:InvokeGateway` on AgentCore Gateway.

Besides the IAM role, you must specify `service` field for SigV4 signing. If your MCP runs on AgentCore Runtime or AgentCore Gateway, the value should be `bedrock-agentcore` . If your MCP runs on API gateway, it should be `execute-api` , and if your MCP runs on lambda, it should be `lambda`.

`region` value is optional. By default, the request will be signed with same region as the registry.

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

Provide the agent card URL or the agent’s base URL where `.well-known/agent-card.json` can be discovered:

```
aws bedrock-agentcore-control create-registry-record \
  --registry-id $REGISTRY_ID \
  --name "travel-agent" \
  --descriptor-type A2A \
  --synchronization-type URL \
  --synchronization-configuration '{"fromUrl": {"url": "https://agent.example.com/.well-known/agent-card.json"}}' \
  --region us-east-1
```

You can also specify credential providers for A2A synchronization, for example you can synchronize from an agent hosted on AgentCore:

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

### AWS CLI

```
aws bedrock-agentcore-control update-registry-record \
  --registry-id $REGISTRY_ID \
  --record-id $RECORD_ID \
  --trigger-synchronization \
  --region us-east-1
```

### AWS SDK

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

###### Note

If the record is in a non-DRAFT status (e.g., APPROVED), the update creates a new DRAFT revision. The approved revision remains searchable.

**Troubleshooting** : see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors "registry-troubleshooting.md#registry-troubleshooting-sync-errors").
