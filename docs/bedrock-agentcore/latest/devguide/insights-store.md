

# Manage the Agent Insight Store

The Agent Insight Store is the account- and Region-scoped destination for Agent Insights generated from online and batch evaluations. Each account has one default Store in each supported Region. The Store starts with `enablementStatus` set to `DISABLED`. Enable it before Insight Evaluators can write Agent Insights.

Use:
+  `ListAgentInsightStores` to discover the default Store.
+  `GetAgentInsightStore` to read its current state.
+  `UpdateAgentInsightStore` to enable or disable it or change its encryption configuration.

An `UpdateAgentInsightStore` request can update `enablementStatus`, `encryptionConfiguration`, or both. To enable a disabled Store with a new key, set `enablementStatus` to `ENABLED` and include `encryptionConfiguration` in the same request. You can combine an encryption change only with `enablementStatus` set to `ENABLED`.

## Store states
<a name="insights-store-status"></a>

The following table describes the Store states. Read `status` together with `enablementStatus`.


|  `status`  | Typical `enablementStatus`  | Meaning | 
| --- | --- | --- | 
|  `ACTIVE`  |  `ENABLED`  | The Store accepts eligible output and its data is available. | 
|  `UPDATING`  |  `ENABLED` or `DISABLED`  | The service is applying an asynchronous enable, disable, or encryption update. Poll `GetAgentInsightStore` and don’t submit another update until it settles. | 
|  `INACTIVE`  |  `DISABLED`  | The Store is disabled and doesn’t accept eligible output. | 
|  `ERROR`  |  `ENABLED` or `DISABLED`  | An asynchronous operation failed. Read `failureReason`, correct the problem, and retry the relevant update with a new client token. | 

## Enable or disable the Store
<a name="insights-store-enable-disable"></a>

Enable the Store before you run Insight Evaluators that should generate Agent Insights.

The following AWS CLI commands enable the Store and check the asynchronous operation:

```bash
aws bedrock-agentcore-control update-agent-insight-store \
    --agent-insight-store-id default-insight-store \
    --enablement-status ENABLED \
    --region us-west-2

aws bedrock-agentcore-control get-agent-insight-store \
    --agent-insight-store-id default-insight-store \
    --region us-west-2
```

Poll until the Store has `enablementStatus` set to `ENABLED` and `status` set to `ACTIVE`.

The following AgentCore CLI commands enable the Store and check its status:

```bash
agentcore eval insight-store update --id default-insight-store \
    --enablement-status ENABLED --region us-west-2

agentcore eval insight-store get --id default-insight-store --region us-west-2
```

Disabling the Store stops it from accepting new eligible Agent Insights and also removes any existing data within the Store. It doesn’t delete the Store itself or impact any other evaluation configurations.

**Disable the Store?**  
Disabling removes the existing Agent Insights. After you re-enable the Store, it accepts new Agent Insights, but it doesn’t restore the removed findings.

The following AWS CLI command disables the Store:

```bash
aws bedrock-agentcore-control update-agent-insight-store \
    --agent-insight-store-id default-insight-store \
    --enablement-status DISABLED \
    --region us-west-2
```

After a disable request, use `GetAgentInsightStore` to poll until the Store reaches `INACTIVE`.

The following AgentCore CLI command disables the Store:

```bash
agentcore eval insight-store update --id default-insight-store \
    --enablement-status DISABLED --region us-west-2
```

## Change Store encryption
<a name="insights-store-encryption-update"></a>

Stores initially use an AWS owned key. To use a customer managed AWS KMS key, pass a key ARN from the same Region as the Store. Key IDs and alias ARNs aren’t supported.

**Important**  
 AWS KMS charges apply when you use a customer managed key. For more information, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).

Use the following AWS CLI command to enable the Store and change it to use a customer managed AWS KMS key. Include both fields in the same request when you enable a disabled Store:

```bash
aws bedrock-agentcore-control update-agent-insight-store \
    --agent-insight-store-id default-insight-store \
    --enablement-status ENABLED \
    --encryption-configuration '{
        "mode": "CUSTOMER_MANAGED_KMS",
        "kmsKeyArn": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }' \
    --region us-west-2
```

The Store reports `UPDATING` while AgentCore applies the encryption change and re-encrypts existing Agent Insights. Existing Agent Insights remain readable during the update while the keys that protect them remain available.

Keep the old and new keys enabled, and keep their required permissions in place, until the Store returns to `ACTIVE`. If re-encryption fails, the Store enters `ERROR`. Correct the key configuration and retry an encryption update with a new client token.

The following AWS CLI command returns the Store to an AWS owned key:

```bash
aws bedrock-agentcore-control update-agent-insight-store \
    --agent-insight-store-id default-insight-store \
    --encryption-configuration '{"mode":"AWS_OWNED_KMS_KEY"}' \
    --region us-west-2
```

Don’t enable a disabled Store in a separate request before changing its encryption configuration. Enable the Store and select the new key in the same request. If you move away from a customer managed key, keep the old key enabled. Keep its required permissions in place until AgentCore finishes reading and re-encrypting the existing data.

The following AgentCore CLI commands change the Store to a customer managed key, and then return it to an AWS owned key:

```bash
agentcore eval insight-store update --id default-insight-store \
    --enablement-status ENABLED \
    --encryption-mode CUSTOMER_MANAGED_KMS \
    --kms-key-arn arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --region us-west-2

agentcore eval insight-store update --id default-insight-store \
    --encryption-mode AWS_OWNED_KMS_KEY --region us-west-2
```