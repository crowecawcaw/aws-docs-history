# Ingest content into long-term memory

Use [IngestData](../APIReference/API_IngestData.md "../APIReference/API_IngestData.md") to submit content directly for long-term memory extraction, without persisting it as a short-term memory event.

## When to use IngestData

Use `IngestData` when you need content distilled into long-term memory but don’t need to keep the raw interaction as a retrievable event. For example:

- You only need the extracted memory records, not the verbatim interaction.
- You want to avoid the short-term storage overhead of persisting an event you would never read back.
- Your application already retains the raw interactions, so you need only the long-term records extracted from them.

Because `IngestData` does not store a short-term event, the submitted content cannot be retrieved with `GetEvent`, `ListEvents`, or `ListSessions`, or reorganized with branching.

###### Note

To keep the raw interaction as a short-term event, use [CreateEvent](short-term-create-event.md "short-term-create-event.md") instead.

## How IngestData works

A successful request confirms that your content was accepted; the resulting long-term memory records become available after the content is processed.

After processing completes, retrieve the resulting long-term memory records using `RetrieveMemoryRecords`, `ListMemoryRecords`, or `GetMemoryRecord` — the same operations used for any other long-term memory records.

`IngestData` supports two payload types:

**Conversational**

A conversation message with a role (for example, `USER` or `ASSISTANT`) and text content.

**JSON**

JSON-formatted data—such as behavioral events, activity logs, or system events.

You can optionally attach metadata to enrich the extracted records. For more information, see [Structured metadata for long-term memories](long-term-memory-metadata.md "long-term-memory-metadata.md").

The extracted records are scoped to a namespace. For more information, see [Specify long-term memory organization with namespaces](specify-long-term-memory-organization.md "specify-long-term-memory-organization.md").

The `actorId` identifies the entity (for example, an end user or agent) and the `sessionId` groups content within a session. Content sharing the same `actorId`, `sessionId`, and namespace is treated as related context during extraction.

###### Note

`IngestData` fans content out to the memory’s configured long-term memory strategies, except self-managed strategies, which have their own memory processing workflows.

## Example

The following example ingests both conversational and non-conversational content.

```
import boto3
from datetime import datetime

# Initialize the Boto3 client for data plane operations
data_client = boto3.client('bedrock-agentcore', region_name='us-west-2')

response = data_client.ingest_data(
    memoryId='mem-12345abcdef',
    actorId='customer-123',
    sessionId='session-456',
    contentTimestamp=datetime.now(),
    source={
        'inline': {
            'payload': [
                {
                    'conversational': {
                        'content': {'text': 'I prefer window seats on flights.'},
                        'role': 'USER'
                    }
                },
                {
                    'conversational': {
                        'content': {'text': "Noted — I'll remember your window seat preference."},
                        'role': 'ASSISTANT'
                    }
                },
                {
                    'json': {
                        'content': {
                            'customer_tier': 'gold',
                            'preferences': {'seat': 'window', 'meal': 'vegetarian'},
                            'loyalty_points': 48200
                        }
                    }
                }
            ]
        }
    }
)

# IngestData is asynchronous; the response echoes the session the content was ingested into.
print(f"Ingested content into session: {response['sessionId']}")
```

## Track ingestion progress

To track what happens after a successful request and detect issues, use the following approaches.

### Verify extraction results

After ingestion, memory records typically appear within seconds to minutes depending on content size and strategy configuration. To confirm extraction completed:

- Use [ListMemoryRecords](long-term-list-memory-records.md "long-term-list-memory-records.md") or [RetrieveMemoryRecords](long-term-retrieve-records.md "long-term-retrieve-records.md") to check whether the expected long-term memory
  records have appeared.
- Configure a Kinesis stream to receive real-time notifications when memory records are created. See [Memory record streaming](memory-record-streaming.md "memory-record-streaming.md") for setup instructions.

### Handle extraction failures

If extraction fails, AgentCore moves the failed job to a dedicated queue for your memory resource. Use `ListMemoryExtractionJobs` to view failed jobs, and `StartMemoryExtractionJob` to re-drive them after addressing the root cause.
For failure reason codes, remediation steps, and how to set up proactive monitoring with the `FailedExtraction` CloudWatch metric, see [Redrive failed ingestions](long-term-redrive.md "long-term-redrive.md").

To enable application logs and traces for deeper visibility into the processing lifecycle, see [Enabling observability for AgentCore runtime, memory, gateway, built-in tools, and identity resources](observability-configure.md#observability-configure-cloudwatch "observability-configure.md#observability-configure-cloudwatch").
