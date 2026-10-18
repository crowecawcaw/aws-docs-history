

# Set a time-to-live for long-term memory records
<a name="long-term-record-ttl"></a>

By default, long-term memory records do not expire. You can optionally set a time-to-live (TTL) so that records are automatically deleted after a retention period that you choose. Use a TTL to meet data-retention requirements, control storage growth, or ensure that stale insights age out of a memory.

You configure a TTL with a `recordExpirySpecification`, which you can provide in two ways:
+  **Strategy-level** – On `CreateMemory` and `UpdateMemory`, set a `recordExpirySpecification` on a strategy. The TTL applies to the long-term memory records that the strategy generates. This works for both [built-in strategies](long-term-configuring-built-in-strategies.md) and [custom (built-in with overrides) strategies](long-term-configuring-custom-strategies.md).
+  **Request-level** – On `BatchCreateMemoryRecords` and `BatchUpdateMemoryRecords`, set a `recordExpirySpecification` on the request. The TTL applies to every record in that batch. For more information, see [Set a time-to-live on a batch request](#long-term-record-ttl-batch-examples).

## Configure a time-to-live
<a name="long-term-record-ttl-configure"></a>

A `recordExpirySpecification` accepts one of two mutually exclusive fields:
+  `recordExpiryDurationDays` – The number of days (minimum 31) after which records expire. Use this field to set or update a TTL.
+  `action` – Set to `REMOVE` to clear a previously configured TTL, so that records generated after the change no longer expire.

The service applies a TTL to each record at the time the record is generated. Changing or removing a TTL affects only records that are created after the change. Previously stored records keep their original expiration, and expired records cannot be recovered.

## Consistency across strategies
<a name="long-term-record-ttl-consistency"></a>

When you configure `recordExpiryDurationDays` on more than one strategy in the same memory, the value must be consistent within each of the following strategy groups:
+  **Semantic and user preference strategies** – Must use the same `recordExpiryDurationDays`. This applies to the `semanticMemoryStrategy` and `userPreferenceMemoryStrategy` built-in strategies, and to custom strategies that override `semanticOverride` or `userPreferenceOverride`.
+  **Summary and episodic strategies** – Must use the same `recordExpiryDurationDays`. This applies to the `summaryMemoryStrategy` and `episodicMemoryStrategy` built-in strategies, and to custom strategies that override `summaryOverride` or `episodicOverride`.

A `recordExpirySpecification` is not applicable to the self-managed strategy (`selfManagedConfiguration`). For a self-managed strategy, you provide the records yourself through the batch APIs, so you control retention per request with the `recordExpirySpecification` on `BatchCreateMemoryRecords` and `BatchUpdateMemoryRecords`. For more information, see [Self-managed strategy](memory-self-managed-strategies.md).

## When records are deleted
<a name="long-term-record-ttl-deletion-timing"></a>

Deletion of an expired long-term memory record can typically take a few days to complete after its time-to-live elapses. The service removes expired records as a background process rather than at the exact expiration moment. During that window, an expired record can still be returned by read operations such as `RetrieveMemoryRecords`, `GetMemoryRecord`, and `ListMemoryRecords`. If you need a record removed immediately, delete it explicitly with `DeleteMemoryRecord` or `BatchDeleteMemoryRecords` instead of relying on a TTL.

## Permissions for configuring long-term memory time-to-live
<a name="long-term-record-ttl-permissions"></a>

Any request that configures or removes a `recordExpirySpecification` — whether it provides `recordExpiryDurationDays` or sets `action` to `REMOVE` — requires the `bedrock-agentcore:UpdateMemoryRecordExpirySpecification` permission. This permission is required in addition to the base action for the operation. This applies to all four entry points that can carry a `recordExpirySpecification`:
+  `CreateMemory` and `UpdateMemory` (strategy-level)
+  `BatchCreateMemoryRecords` and `BatchUpdateMemoryRecords` (request-level)

Requests that do not carry a `recordExpirySpecification` are unaffected and require only their existing actions. If you set or remove a TTL, you must add `bedrock-agentcore:UpdateMemoryRecordExpirySpecification` to the IAM policy of the principal that makes the request. Without it, a request that carries a `recordExpirySpecification` is denied with `AccessDeniedException`, even if the caller is allowed to perform the base operation.

Setting a TTL on a record is a deferred, service-executed deletion: once the duration elapses, the service deletes the record. Without a dedicated permission, any principal that can call `CreateMemory`, `UpdateMemory`, `BatchCreateMemoryRecords`, or `BatchUpdateMemoryRecords` could delete records by configuring a short TTL. This is true even if that principal cannot call `DeleteMemoryRecord` or `BatchDeleteMemoryRecords`. Conversely, a principal that can remove a TTL could keep data that was meant to expire. The `bedrock-agentcore:UpdateMemoryRecordExpirySpecification` action lets you control who can configure or remove a record time-to-live. This control is independent of the base operation and the record-deletion actions.

## Set a time-to-live on a strategy
<a name="long-term-record-ttl-strategy-examples"></a>

The following IAM policy grants a principal the ability to manage memory resources and configure retention, while withholding on-demand record deletion. The principal can set or remove a TTL. However, because `DeleteMemoryRecord` and `BatchDeleteMemoryRecords` are not granted, the principal cannot delete individual records directly.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ManageMemoryAndRetention",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:CreateMemory",
                "bedrock-agentcore:UpdateMemory",
                "bedrock-agentcore:UpdateMemoryRecordExpirySpecification"
            ],
            "Resource": "arn:aws:bedrock-agentcore:us-east-1:123456789012:memory/*"
        }
    ]
}
```

To set a TTL when you create a memory, provide a `recordExpirySpecification` on the strategy.

```
aws bedrock-agentcore-control create-memory \
  --name "SupportAgentFactMemory" \
  --event-expiry-duration 90 \
  --memory-strategies '[
    {
      "semanticMemoryStrategy": {
        "name": "FactExtractor",
        "namespaceTemplates": ["/support_cases/{sessionId}/facts/"],
        "recordExpirySpecification": {
          "recordExpiryDurationDays": 60
        }
      }
    }
  ]'
```

To change the retention on an existing strategy, pass `recordExpirySpecification` with `recordExpiryDurationDays` in a `modifyMemoryStrategies` entry.

```
aws bedrock-agentcore-control update-memory \
  --memory-id "SupportAgentFactMemory-abc123" \
  --memory-strategies '{
    "modifyMemoryStrategies": [
      {
        "memoryStrategyId": "FactExtractor-xyz789",
        "recordExpirySpecification": {
          "recordExpiryDurationDays": 45
        }
      }
    ]
  }'
```

To remove a previously configured TTL so that records generated afterward no longer expire, set `action` to `REMOVE`.

```
aws bedrock-agentcore-control update-memory \
  --memory-id "SupportAgentFactMemory-abc123" \
  --memory-strategies '{
    "modifyMemoryStrategies": [
      {
        "memoryStrategyId": "FactExtractor-xyz789",
        "recordExpirySpecification": {
          "action": "REMOVE"
        }
      }
    ]
  }'
```

## Set a time-to-live on a batch request
<a name="long-term-record-ttl-batch-examples"></a>

When you write records directly with the batch APIs, you set a request-level TTL that applies to every record in the request. The following IAM policy grants a principal the ability to write records through the batch APIs and to configure retention on those requests.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "BatchWriteWithRetention",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:BatchCreateMemoryRecords",
                "bedrock-agentcore:BatchUpdateMemoryRecords",
                "bedrock-agentcore:UpdateMemoryRecordExpirySpecification"
            ],
            "Resource": "arn:aws:bedrock-agentcore:us-east-1:123456789012:memory/*"
        }
    ]
}
```

To set a TTL on created records, provide a `recordExpirySpecification` at the top level of the request. It applies to every record created by the call.

```
aws bedrock-agentcore batch-create-memory-records \
  --memory-id "your-memory-id" \
  --records '[
    {
      "requestIdentifier": "1",
      "namespaces": ["/actor/Jane/"],
      "content": {"text": "Customer prefers window seats"},
      "timestamp": 1705312800
    }
  ]' \
  --record-expiry-specification '{
    "recordExpiryDurationDays": 31
  }'
```

To change retention on the records in an update request, provide `recordExpiryDurationDays`. To remove a previously configured TTL, set `action` to `REMOVE`.

```
aws bedrock-agentcore batch-update-memory-records \
  --memory-id "your-memory-id" \
  --records '[
    {
      "memoryRecordId": "mem-12345678-1234-1234-1234-123456789012",
      "namespaces": ["/actor/Jane/"],
      "content": {"text": "Customer prefers aisle seats"},
      "timestamp": 1705395600
    }
  ]' \
  --record-expiry-specification '{
    "action": "REMOVE"
  }'
```

### How BatchUpdateMemoryRecords applies a time-to-live
<a name="long-term-record-ttl-batch-behavior"></a>

When `BatchUpdateMemoryRecords` modifies an existing record, the resulting TTL depends on two things. The first is whether the request includes a `recordExpirySpecification`. The second is whether the record already has one.
+  **If the request contains an explicit `recordExpirySpecification` ** – the service applies it directly, and it takes precedence in all cases. If the record already had a TTL, the new value overwrites it. If the record did not have one, the new value sets one.
+  **If the request does not contain a `recordExpirySpecification`, and the record already has one** – the record’s TTL is reset using its last known applied duration.
+  **If the request does not contain a `recordExpirySpecification`, and the record has none** – no TTL is applied, and the record remains non-expiring.

On the batch APIs, a record’s TTL comes only from the `recordExpirySpecification` on the request. The service never derives it from the record’s associated strategy. A record’s strategy might configure `recordExpiryDurationDays`. However, that strategy-level setting does not apply to records written or updated through `BatchCreateMemoryRecords` or `BatchUpdateMemoryRecords`. To change retention for batch-written records, you must set it explicitly on the request.