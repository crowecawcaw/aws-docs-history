

# Generate a recommendation from insights findings
<a name="insights-generate-recommendation"></a>

After reviewing your insights results, you can use the same agent traces to generate an improved system prompt. Point `StartRecommendation` at the completed batch evaluation that produced your insights findings.

**Note**  
Recommendation generation from insights supports only `Builtin.Insight.FailureAnalysis` insights, and it produces only system prompt recommendations.

**Topics**
+ [Start a system prompt recommendation](#insights-recommendation-start)
+ [Retrieve the recommended prompt](#insights-recommendation-retrieve)
+ [Alternative trace sources](#insights-recommendation-trace-sources)

## Start a system prompt recommendation
<a name="insights-recommendation-start"></a>

Provide your current system prompt and reference the batch evaluation that contains the traces:

**Example**  
Reference the batch evaluation ARN produced by the completed insights run:  

```
agentcore eval recommendation start \
  --name improve-system-prompt \
  --type SYSTEM_PROMPT_RECOMMENDATION \
  --recommendation-config '{
    "systemPromptRecommendationConfig": {
      "systemPrompt": {
        "text": "You are a helpful customer support assistant."
      },
      "agentTraces": {
        "batchEvaluation": {
          "batchEvaluationArn": "<BATCH_EVALUATION_ARN>"
        }
      },
      "evaluationConfig": {
        "evaluators": [
          {
            "evaluatorArn": "arn:aws:bedrock-agentcore:::evaluator/Builtin.GoalSuccessRate"
          }
        ]
      }
    }
  }' \
  --json
```

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
            "evaluationConfig": {
                "evaluators": [
                    {
                        "evaluatorArn": "arn:aws:bedrock-agentcore:::evaluator/Builtin.GoalSuccessRate"
                    }
                ]
            },
        }
    },
    clientToken=str(uuid.uuid4()),
)

recommendation_id = response["recommendationId"]
print(f"Started recommendation: {recommendation_id}")
```
An insights-only batch evaluation does not contain evaluator scores. Specify one numerical evaluator in `evaluationConfig` to provide the optimization signal for the system prompt recommendation.

## Retrieve the recommended prompt
<a name="insights-recommendation-retrieve"></a>

Poll until complete, then retrieve the result:

**Example**  
Run the following command until `status` is `COMPLETED` or `FAILED`:  

```
agentcore eval recommendation get --id <RECOMMENDATION_ID> --json
```
The recommended prompt is in `recommendationResult.systemPromptRecommendationResult.recommendedSystemPrompt`, and the reasoning is in `recommendationResult.systemPromptRecommendationResult.explanation`.

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