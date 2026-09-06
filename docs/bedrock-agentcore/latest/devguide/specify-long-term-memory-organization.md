

# Specify long-term memory organization with namespaces
<a name="specify-long-term-memory-organization"></a>

When you [create](memory-create-a-memory-store.md) an AgentCore Memory, use a namespace to specify where the [long-term memories](memory-types.md#memory-long-term-memory) for a [memory strategy](memory-strategies.md) are logically grouped. Every time a new long-term memory is extracted using the memory strategy, it is saved under the namespace you set. This means that all long-term memories are scoped to their specific namespace, keeping them organized and preventing any mix-ups with other users or sessions. You should use a hierarchical format separated by forward slashes `/` . This helps keep memories organized clearly. As needed, you can choose to use the following pre-defined variables within braces in the namespace based on your application’s organization needs:
+  **actorId** – Identifies who the long-term memory belongs to.

  An actor refers to entity such as end users or agent/user combinations. For example, in a coding support chatbot, the actor is usually the developer asking questions. Using the actor ID helps the system know which user the memory belongs to, keeping each user’s data separate and organized.
+  **strategyId** – Shows which memory strategy is being used. This strategy identifier is auto-generated when you create an AgentCore Memory.
+  **sessionId** – Identifies which session or conversation the memory is from.

  A session is usually a single conversation or interaction period between the user and the AI agent. It groups all related messages and events that happen during that conversation.

For example, if you define the following namespace as the input to your strategy when creating an AgentCore Memory:

```
/strategy/{memoryStrategyId}/actor/{actorId}/session/{sessionId}/
```

After memory creation, this namespace might look like:

```
/strategy/summarization-93483043/actor/actor-9830m2w3/session/session-9330sds8
```

A namespace can have different levels of granularity. The following examples use built-in variables only:

 **Granular at the session level** 

 `/strategy/{memoryStrategyId}/actor/{actorId}/session/{sessionId}/` 

 **Granular at the actor level across sessions** 

 `/strategy/{memoryStrategyId}/actor/{actorId}/` 

 **Granular at the strategy level across actors** 

 `/strategy/{memoryStrategyId}/` 

 **Global across all strategies** 

 `/` 

For even more granular organization, you can add [custom namespace variables](#specify-custom-namespace-variables) to represent additional dimensions such as tenant, team, or environment.

For example code, see [Enable long-term memory](long-term-enabling-long-term-memory.md).

## Custom namespace variables
<a name="specify-custom-namespace-variables"></a>

In addition to the built-in variables (`actorId`, `sessionId`, `memoryStrategyId`), you can define custom namespace variables to represent your application’s unique organizational dimensions, such as company, organization, team, or environment. With custom variables, you can scope long-term memories along arbitrary hierarchies without creating duplicate strategies or overloading the built-in variables.

For example, a multi-tenant application might need memories scoped by organizations:

```
/org/{orgname}/team/{teamname}/actor/{actorId}/session/{sessionId}/
```

You define the custom variables when creating or updating an existing memory resource using the `namespaceKeys` parameter, and supply their values at runtime through the `extractionConfig.namespaceVariables` field in the [CreateEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CreateEvent.html) operation.

**Important**  
All custom namespace variable keys and values must be lowercase.

### Define namespace keys
<a name="specify-define-namespace-keys"></a>

When you create or update a memory resource, use the `namespaceKeys` parameter to declare your custom variable keys and optional validation rules. Each key must:
+ Contain only lowercase alphanumeric characters.
+ Not be a built-in variable name (`actorId`, `sessionId`, or `memoryStrategyId`).
+ Be at most 32 characters long.

You can define up to 5 namespace keys per memory resource, and up to 5 custom variables per `namespaceTemplate`.

Keep the following in mind when defining namespace keys:
+ You can define namespace keys that are not referenced by any strategy to pre-register keys for future use.
+ A single namespace key can be referenced by multiple strategies. For example, `{companyname}` can appear in the `namespaceTemplate` of both a semantic strategy and a summary strategy.
+ A namespace key that is currently referenced by a strategy’s `namespaceTemplate` cannot be deleted. You must first remove the reference from the strategy (de-reference the key), then delete it.

For each key, you can optionally specify validation rules that constrain the values accepted at runtime:
+  **allowedValues** – A list of up to 10 permitted values (case-sensitive). Values must start with a lowercase alphanumeric character and contain only lowercase alphanumeric characters, hyphens, and underscores.
+  **regexPattern** – A regex pattern (up to 64 characters) that the value must match.

When you specify both `allowedValues` and `regexPattern`, the service enforces both rules (logical `AND`).

The following example shows how to create a memory resource with custom namespace variables and validation:

```
aws bedrock-agentcore-control create-memory \
    --name "MultiTenantAgentMemory" \
    --description "Memory for a multi-tenant AI agent" \
    --event-expiry-duration 10 \
    --memory-strategies '[
        {
            "semanticMemoryStrategy": {
                "name": "TenantScopedStrategy",
                "namespaceTemplates": ["/org/{orgname}/team/{teamname}/actor/{actorId}/session/{sessionId}/"]
            }
        }
    ]' \
    --namespace-keys '[
        {"key": "orgname", "validation": {"allowedValues": ["acme", "globex", "initech"]}},
        {"key": "teamname", "validation": {"regexPattern": "^[a-z][a-z0-9-]*$"}}
    ]'
```

### Supply namespace values at runtime
<a name="specify-supply-namespace-values-at-runtime"></a>

When you create an event using the [CreateEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CreateEvent.html) operation, pass the custom namespace variable values in the `extractionConfig.namespaceVariables` field:

```
aws bedrock-agentcore create-event \
    --memory-id "MultiTenantAgentMemory-n29sh5ka8r" \
    --actor-id "user123" \
    --session-id "session67" \
    --event-timestamp "$(date -u +"%Y-%m-%dT%H:%M:%S.%3NZ")" \
    --payload '[
        {
            "conversational": {
                "content": {"text": "I need help debugging my application."},
                "role": "USER"
            }
        }
    ]' \
    --extraction-config '{
        "namespaceVariables": {
            "orgname": "acme",
            "teamname": "engineering"
        }
    }'
```

The service substitutes these values into the namespace templates during long-term memory extraction.

**Note**  
If a custom namespace variable that is referenced by a strategy’s `namespaceTemplate` is not provided in the `CreateEvent` request, namespace resolution does not take place for that strategy. As a result, long-term memory extraction is not initiated for that strategy. The `CreateEvent` operation still succeeds and the event is persisted in short-term memory.  
To detect these failures, set up vended logs and monitor for the `NamespaceResolutionFailure` metric, which reports with the dimensions: `Operation`, `Resource`, `StrategyType`, and `StrategyId` for which extraction was skipped.

### Update namespace keys
<a name="specify-update-namespace-keys"></a>

When you update namespace keys with the [UpdateMemory](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateMemory.html) operation, the `namespaceKeys` value fully replaces the existing set. To safely update, retrieve the current keys with `GetMemory`, apply your changes, and submit the complete list.

Keep the following constraints in mind:
+ If you omit a key that is still referenced by a strategy’s `namespaceTemplate`, the service throws a `ValidationException`. You must first remove the key from the strategy’s `namespaceTemplate` before you can remove it from `namespaceKeys`.
+ To add a new key, include it alongside all existing keys in the request.

```
# Get the current memory configuration
current = control_client.get_memory(memoryId="MultiTenantAgentMemory-n29sh5ka8r")
existing_keys = current['memory'].get('namespaceKeys', [])

# Add a new key while preserving existing ones
existing_keys.append({
    'key': 'category',
    'validation': {
        'allowedValues': ['backend', 'frontend', 'data']
    }
})

# Update with the full set
control_client.update_memory(
    memoryId="MultiTenantAgentMemory-n29sh5ka8r",
    namespaceKeys=existing_keys
)
```

### Restrict write-path access with IAM condition keys
<a name="specify-namespace-variable-iam"></a>

You can create IAM policies that use the `bedrock-agentcore:namespaceVariable/<variableName>` condition key to control which custom namespace variable values a caller can use when creating events. With this condition key, you can enforce tenant isolation at the write path.

The condition key follows the pattern `bedrock-agentcore:namespaceVariable/<key>` where `<key>` is the namespace variable name defined in `namespaceKeys`.

The following policy allows the caller to create events only when `orgname` is set to `acme`, and explicitly denies requests when `orgname` is set to `globex`:

```
{
"Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowCreateEventForAcme",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:CreateEvent",
      "Resource": "arn:aws:bedrock-agentcore:us-east-1:123456789012:memory/memory_id",
      "Condition": {
        "StringEquals": {
          "bedrock-agentcore:namespaceVariable/orgname": "acme"
        }
      }
    },
    {
      "Sid": "DenyCreateEventForGlobex",
      "Effect": "Deny",
      "Action": "bedrock-agentcore:CreateEvent",
      "Resource": "arn:aws:bedrock-agentcore:us-east-1:123456789012:memory/memory_id",
      "Condition": {
        "StringEquals": {
          "bedrock-agentcore:namespaceVariable/orgname": "globex"
        }
      }
    }
  ]
}
```

The following table shows how IAM evaluates requests based on whether a condition key is present in the policy and whether the request provides the namespace variable:


| Policy has condition on `namespaceVariable`? | Request provides the variable? | Result | Reason | 
| --- | --- | --- | --- | 
| No | No | Allowed | Condition not evaluated | 
| No | Yes | Allowed | Extra context keys are ignored | 
| Yes | Yes (matching value) | Allowed | Condition is satisfied | 
| Yes | No | Denied | Condition key is missing, cannot be satisfied | 
| Yes | Yes (non-matching value) | Denied | Condition is not satisfied | 

## Restrict read-path access with IAM
<a name="memory-scope-iam"></a>

You can create IAM policies to restrict memory read access by the scopes you define, such as actor, session, and namespace. Use the scopes as context keys in your IAM policies.

The following policy restricts access to retrieving memories to a specific namespace or records under a particular namespacePath hierarchy. In this example, the policy allows access only to memories with exact namespaces such as `summaries/agent1/` OR with namespaces under the following namespacePath hierarchy with `summaries/agent1/` , such as `summaries/agent1/session1/` or `summaries/agent1/session2/`.

```
{
"Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "SpecificNamespaceAccess",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:RetrieveMemoryRecords"
      ],
      "Resource": "arn:aws:bedrock-agentcore:us-east-1:123456789012:memory/memory_id",
      "Condition": {
        "StringEquals": {
          "bedrock-agentcore:namespace": "summaries/agent1/"
        }
      }
    },
    {
      "Sid": "SpecificNamespacePathAccess",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:RetrieveMemoryRecords"
      ],
      "Resource": "arn:aws:bedrock-agentcore:us-east-1:123456789012:memory/memory_id",
      "Condition": {
        "StringLike": {
          "bedrock-agentcore:namespacePath": "summaries/agent1/*"
        }
      }
    }
  ]
}
```

**Note**  
Retrieval APIs (`ListMemoryRecords`, `RetrieveMemoryRecords`) require the fully resolved namespace. Custom namespace variables are already substituted at this point, so the existing `bedrock-agentcore:namespace` and `bedrock-agentcore:namespacePath` condition keys cover the read path with no additional configuration.