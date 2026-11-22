

# List, read, archive, and restore Agent Insights

Use the Agent Insights data-plane APIs to review findings from online and batch evaluations and control whether they appear in the active or archived view.

## List Agent Insights
<a name="insights-list"></a>

 `ListAgentInsights` returns up to 50 summaries per request. By default, it returns active Agent Insights. You can:
+ Omit both locator filters to list across the account in the current Region.
+ Set `applicationName` to list findings for one application.
+ Set `batchEvaluationId` to list findings produced from one batch evaluation.
+ Set `archiveStatus` to `ACTIVE` or `ARCHIVED`.
+ Use `maxResults` and `nextToken` for pagination.

For online evaluation insights, `applicationName` is the agent’s OpenTelemetry service name (`service.name`), configured as `serviceName` in the online evaluation data source. For batch-generated insights, use `batchEvaluationId` to list the findings from a specific evaluation.

The following AWS CLI examples list Agent Insights across the account, for an application, or for a batch evaluation. Replace `MyAgent.DEFAULT` and `<batch-evaluation-id>` with your application name and batch evaluation ID:

```bash
# List active Agent Insights across the account
aws bedrock-agentcore list-agent-insights \
    --region us-west-2

# List archived Agent Insights for one application
aws bedrock-agentcore list-agent-insights \
    --application-name "MyAgent.DEFAULT" \
    --archive-status ARCHIVED \
    --max-results 25 \
    --region us-west-2

# List Agent Insights from one batch evaluation
aws bedrock-agentcore list-agent-insights \
    --batch-evaluation-id <batch-evaluation-id> \
    --region us-west-2
```

The following AgentCore CLI commands list the same Agent Insights:

```bash
agentcore eval insight list --region us-west-2

agentcore eval insight list --application-name MyAgent.DEFAULT \
    --archive-status ARCHIVED --max-results 25 --region us-west-2

agentcore eval insight list --batch-evaluation-id <batch-evaluation-id> --region us-west-2
```

## Get Agent Insight details
<a name="insights-get"></a>

 `GetAgentInsight` requires both the `agentInsightId` and its `applicationName`.

The following Python example reads one Agent Insight. Replace the `applicationName` and `agentInsightId` values with values returned by `ListAgentInsights`:

```python
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

insight = client.get_agent_insight(
    applicationName="MyAgent.DEFAULT",
    agentInsightId="a7f3c2e1b0d94f56",
)

print(insight["name"])
print(insight["description"])
print("Affected sessions:", insight.get("affectedSessionCount", 0))

for cause in insight.get("rootCauses", []):
    print(cause["name"])
    print(cause.get("explanation"))
    print(cause.get("suggestedFix"))
```

Generated fields for online evaluation insights can change as later results contribute to the pattern. Use the ID, not the generated name, to track the Agent Insight. Batch evaluation `insightResults` are point-in-time results for that job.

The following AgentCore CLI command gets the details of one Agent Insight:

```bash
agentcore eval insight get --application-name MyAgent.DEFAULT \
    --id <agent-insight-id> --region us-west-2
```

## Archive or restore an Agent Insight
<a name="insights-archive"></a>

When you archive an Agent Insight, it remains available but moves out of the default `ACTIVE` list. To restore it, set `archiveStatus` to `ACTIVE`.

The following AWS CLI commands archive and restore an Agent Insight. Replace the application name and Agent Insight ID with values returned by `ListAgentInsights`:

```bash
# Archive
aws bedrock-agentcore update-agent-insight \
    --application-name "MyAgent.DEFAULT" \
    --agent-insight-id a7f3c2e1b0d94f56 \
    --archive-status ARCHIVED \
    --region us-west-2

# Restore
aws bedrock-agentcore update-agent-insight \
    --application-name "MyAgent.DEFAULT" \
    --agent-insight-id a7f3c2e1b0d94f56 \
    --archive-status ACTIVE \
    --region us-west-2
```

 `UpdateAgentInsight` is idempotent. If two callers update the same Agent Insight concurrently, retry a `ConflictException` after reading its current state.

The following AgentCore CLI commands archive and restore an Agent Insight:

```bash
agentcore eval insight update --application-name MyAgent.DEFAULT \
    --id <agent-insight-id> --archive-status ARCHIVED --region us-west-2

agentcore eval insight update --application-name MyAgent.DEFAULT \
    --id <agent-insight-id> --archive-status ACTIVE --region us-west-2
```

## Generated metadata availability
<a name="insights-metadata-status"></a>

Use `customerMetadataStatus` to determine whether the generated name, description, root causes, and sample-session details are available.

The following table lists the `customerMetadataStatus` values and their meanings.


| Value | Meaning | 
| --- | --- | 
|  `AVAILABLE`  | AgentCore read and decrypted the generated content. | 
|  `CUSTOMER_KEY_UNAVAILABLE`  | The customer managed AWS KMS key used for the content isn’t usable. Restore the key and its permissions. | 
|  `UNAVAILABLE`  | AgentCore couldn’t read the generated content for another storage or service reason. Retry the request. If the condition continues, contact AWS Support. | 

When metadata is unavailable, the API still returns the stable identifiers and status fields that it can read, but generated content and samples can be replaced with unavailable placeholders.