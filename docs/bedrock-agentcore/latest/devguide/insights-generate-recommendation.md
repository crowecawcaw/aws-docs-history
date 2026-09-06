

# Generate a recommendation from insights findings
<a name="insights-generate-recommendation"></a>

After reviewing your insights results, you can use the same agent traces to generate an improved system prompt. Point `StartRecommendation` at the completed batch evaluation that produced your insights findings.

**Note**  
Recommendation generation is currently supported only for `Builtin.Insight.FailureAnalysis` insights, and only system prompt recommendations are provided today.

**Topics**
+ [Start a system prompt recommendation](#insights-recommendation-start)
+ [Retrieve the recommended prompt](#insights-recommendation-retrieve)
+ [Alternative trace sources](#insights-recommendation-trace-sources)

## Start a system prompt recommendation
<a name="insights-recommendation-start"></a>

Provide your current system prompt and reference the batch evaluation that contains the traces:

**Example**  
Generate a recommendation from a completed insights run:  

```
agentcore run recommendation --from-insights <id> --type system-prompt --bundle-name my_bundle --json
```
Or reference a batch evaluation ARN directly:  

```
agentcore run recommendation --batch-evaluation-arn <arn> --type system-prompt --bundle-name my_bundle --json
```

1. Run `agentcore` to open the TUI, then select **run** and choose **Recommendation**:  
![Run menu: select Recommendation](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/insights-run-select.png)

   The wizard guides you through selecting a trace source (insights run or batch evaluation ARN), recommendation type, and config bundle.

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
<a name="insights-recommendation-retrieve"></a>

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
<a name="insights-recommendation-trace-sources"></a>

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