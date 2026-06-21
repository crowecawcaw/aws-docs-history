# Generate a recommendation from insights findings

After reviewing your insights results, you can use the same agent traces to generate an improved system prompt. Point `StartRecommendation` at the completed batch evaluation that produced your insights findings.

###### Note

Recommendation generation is currently supported only for `Builtin.Insight.FailureAnalysis` insights, and only system prompt recommendations are provided today.

###### Topics

- [Start a system prompt recommendation](#insights-recommendation-start "#insights-recommendation-start")
- [Retrieve the recommended prompt](#insights-recommendation-retrieve "#insights-recommendation-retrieve")
- [Alternative trace sources](#insights-recommendation-trace-sources "#insights-recommendation-trace-sources")

## Start a system prompt recommendation

Provide your current system prompt and reference the batch evaluation that contains the traces:

```
import boto3
import uuid

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

response = client.start_recommendation(
    name=f"fix-rate-limiting-{uuid.uuid4().hex[:8]}",
    type="SYSTEM_PROMPT_RECOMMENDATION",
    recommendationConfig={
        "systemPromptRecommendationConfig": {
            "systemPrompt": {
                "text": "You are a helpful customer support assistant. Help users with their orders and returns."
            },
            "agentTraces": {
                "batchEvaluation": {
                    "batchEvaluationArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:batch-evaluate/insights-run-ABC1234567"
                }
            },
        }
    },
    clientToken=str(uuid.uuid4()),
)

recommendation_id = response["recommendationId"]
print(f"Started recommendation: {recommendation_id}")
```

## Retrieve the recommended prompt

Poll until complete, then retrieve the result:

```
import time

while True:
    rec = client.get_recommendation(recommendationId=recommendation_id)
    if rec["status"] in ("COMPLETED", "FAILED"):
        break
    time.sleep(15)

if rec["status"] == "COMPLETED":
    result = rec["recommendationResult"]["systemPromptRecommendationResult"]
    print(f"Recommended prompt:\n{result['recommendedSystemPrompt']}")
    print(f"\nExplanation:\n{result['explanation']}")
```

## Alternative trace sources

Instead of referencing a batch evaluation, you can also provide traces via CloudWatch Logs:

```
"agentTraces": {
    "cloudwatchLogs": {
        "logGroupArns": [
            "arn:aws:logs:us-west-2:123456789012:log-group:/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"
        ],
        "serviceNames": ["MyAgent.DEFAULT"],
        "startTime": "2026-05-27T00:00:00Z",
        "endTime": "2026-06-03T00:00:00Z",
    }
}
```
