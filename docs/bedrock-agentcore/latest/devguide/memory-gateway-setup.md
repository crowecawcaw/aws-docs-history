# Set up a gateway with a Memory connector target

To front a Memory resource with a gateway, you create a gateway with an inbound authorizer, then add a target that uses the `agentcore-memory` connector.

###### Note

You can set up the Memory connector through the AWS SDK and AWS Command Line Interface (AWS CLI).

**Prerequisites**

- An AgentCore Memory resource. For more information, see [Create an AgentCore Memory](memory-create-a-memory-store.md "memory-create-a-memory-store.md").
- Permissions to create and configure an AgentCore Gateway. For more information, see [Prerequisites for using the Amazon Bedrock AgentCore gateway service](gateway-prerequisites.md "gateway-prerequisites.md").
- Depending on the outbound credential mode (see [Outbound credential mode](memory-gateway-connector.md#memory-gateway-connector-outbound "memory-gateway-connector.md#memory-gateway-connector-outbound")): for `GATEWAY_IAM_ROLE`, a gateway execution role that the gateway assumes to call Memory, with its identity policy scoped to only the Memory actions the gateway needs; for `CALLER_IAM_CREDENTIALS`, the caller’s own IAM identity must be permitted to perform the Memory actions, because the gateway forwards that identity to Memory.

**Steps**

The following steps use the AWS CLI. For the input and output shapes of each API operation, follow the links to the _Amazon Bedrock AgentCore Control API Reference_. Replace the example names, `memoryId`, and role ARN with your own values.

1. Create a gateway with [CreateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md") and choose its inbound authorizer type (`authorizerType`). The authorizer determines how callers authenticate to the gateway and which identity information is available to access-control policies. For more information, see [Inbound and outbound authentication modes](memory-gateway-connector.md#memory-gateway-connector-auth-modes "memory-gateway-connector.md#memory-gateway-connector-auth-modes").

The following example creates a gateway that authenticates end users with OAuth (`CUSTOM_JWT`) — the primary fine-grained access control path. Provide your OpenID Connect provider’s discovery URL and allowed client ids.

```
aws bedrock-agentcore-control create-gateway \
  --name my-memory-gateway \
  --role-arn arn:aws:iam::123456789012:role/my-gateway-execution-role \
  --authorizer-type CUSTOM_JWT \
  --authorizer-configuration '{
    "customJWTAuthorizer": {
      "discoveryUrl": "https://your-idp.example.com/.well-known/openid-configuration",
      "allowedClients": ["your-client-id"]
    }
  }'
```

The response includes the `gatewayId`, `gatewayArn`, and the invocation `gatewayUrl`. Creation is asynchronous; use [GetGateway](../../../bedrock-agentcore-control/latest/APIReference/API_GetGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_GetGateway.md") to wait until the gateway’s `status` is `READY`.

###### Note

This example uses OAuth inbound, which always uses the `GATEWAY_IAM_ROLE` outbound credential mode. The `--role-arn` value is the gateway execution role that the gateway uses to call Memory. For other inbound types and outbound modes, see [Inbound and outbound authentication modes](memory-gateway-connector.md#memory-gateway-connector-auth-modes "memory-gateway-connector.md#memory-gateway-connector-auth-modes"). 2. Add a target to the gateway with [CreateGatewayTarget](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.md"), using the `agentcore-memory` connector as the target configuration. For `--gateway-identifier`, use the `gatewayId` returned by `CreateGateway` in the previous step. Supply the connector id and the `memoryId` of the Memory resource to front. The target’s `credentialProviderConfigurations` set the outbound credential mode; with OAuth inbound this is `GATEWAY_IAM_ROLE`.

```
aws bedrock-agentcore-control create-gateway-target \
  --gateway-identifier <gateway-id> \
  --name my-memory \
  --target-configuration '{
    "http": {
      "connector": {
        "source": { "connectorId": "agentcore-memory" },
        "parameters": { "memoryId": "your-memory-id" }
      }
    }
  }' \
  --credential-provider-configurations '[
    { "credentialProviderType": "GATEWAY_IAM_ROLE" }
  ]'
```

Target creation is asynchronous; use [GetGatewayTarget](../../../bedrock-agentcore-control/latest/APIReference/API_GetGatewayTarget.md "../../../bedrock-agentcore-control/latest/APIReference/API_GetGatewayTarget.md") to wait until the target’s `status` is `READY`. The target name (`my-memory` here) becomes the prefix of every Cedar action id for this target. 3. Attach a policy engine and add fine-grained access control policies. This step is what enforces per-caller isolation. For the full procedure and Memory-specific policy examples, see [Fine-grained access control for Memory](memory-gateway-fgac.md "memory-gateway-fgac.md").

###### Note

The name you give the target becomes part of every Cedar action id for that target — a target named `<target-name>` produces action ids that begin with `<target-name>___`. Choose a target name you are comfortable referencing in access-control policies.
