

# Custom multi-dimension evaluators
<a name="multi-dimension-evaluators"></a>

A multi-dimension evaluator is a custom LLM-as-a-judge evaluator that rates one target on several named *dimensions* in a single judge call. Each dimension has its own instruction and its own rating scale, and produces its own result.

For example, a customer-support agent’s reply can be rated on issue resolution, policy compliance, and tone. Instead of creating three evaluators that each read the same trace, you create one evaluator with three dimensions. The judge model reads the trace once and returns three results.

Use a multi-dimension evaluator when:
+ You rate the same target on several dimensions and want one judge call instead of several.
+ You want to mix scored dimensions (numerical) and classification dimensions (categorical) in one evaluator.

Use separate evaluators instead when:
+ The dimensions need different evaluation levels or different judge models.
+ You need the evaluator in an A/B test or a recommendation. Multi-dimension evaluators aren’t supported there.
+ You don’t want a single failed judge call to fail every dimension. See [Errors and token usage](#multi-dimension-evaluators-errors).

## Define a multi-dimension evaluator
<a name="multi-dimension-evaluators-define"></a>

To create a multi-dimension evaluator, set `llmAsAJudge.ratingScale.multiDimensional` to a list of dimensions when you call `CreateEvaluator`. `ratingScale` takes exactly one of `numerical`, `categorical`, or `multiDimensional`.

Each dimension has the following fields. All fields are required.


| Field | Description | 
| --- | --- | 
|  `dimensionName`  | The name of the dimension. Must start with a letter and contain only letters, digits, and underscores, up to 48 characters. Must be unique within the evaluator. The name identifies the dimension’s results. | 
|  `dimensionInstruction`  | What the judge model assesses for this dimension, 1–4,000 characters. It can use the same placeholders as `instructions` for the evaluator’s level, but doesn’t have to include one. | 
|  `dimensionRatingScale`  | The scale for this dimension: exactly one of `numerical` or `categorical`. Each is defined the same way as the `numerical` or `categorical` rating scale of a single-scale evaluator. | 

For the maximum number of dimensions, see [Quotas for Amazon Bedrock AgentCore](bedrock-agentcore-limits.md). Very long instructions across many dimensions can make the evaluator too large to store, and `CreateEvaluator` or `UpdateEvaluator` fails.

Multi-dimension evaluators support all three evaluation levels (`TOOL_CALL`, `TRACE`, and `SESSION`) and customer managed keys in AWS Key Management Service (AWS KMS). For encryption details, see [Encryption at rest for AgentCore Evaluations](evaluations-encryption.md).

The following configuration defines a trace-level evaluator with two numerical dimensions and one categorical dimension.

```
{
    "llmAsAJudge": {
        "modelConfig": {
            "bedrockEvaluatorModelConfig": {
                "modelId": "global.anthropic.claude-sonnet-4-5-20250929-v1:0",
                "inferenceConfig": {
                    "maxTokens": 2000,
                    "temperature": 0
                }
            }
        },
        "instructions": "You are reviewing a customer support assistant's reply. Rate the reply on each dimension below.\n\nContext: {context}\nCandidate Response: {assistant_turn}",
        "ratingScale": {
            "multiDimensional": [
                {
                    "dimensionName": "issue_resolution",
                    "dimensionInstruction": "Does the reply resolve the customer's issue, or give a clear next step that will resolve it?",
                    "dimensionRatingScale": {
                        "numerical": [
                            {"value": 1, "label": "Resolved", "definition": "The issue is resolved or a correct next step is given."},
                            {"value": 0.5, "label": "Partial", "definition": "The reply addresses part of the issue."},
                            {"value": 0, "label": "Unresolved", "definition": "The reply does not address the issue."}
                        ]
                    }
                },
                {
                    "dimensionName": "policy_compliance",
                    "dimensionInstruction": "Does the reply follow the support policy: no refunds promised without an order ID, no account details disclosed?",
                    "dimensionRatingScale": {
                        "numerical": [
                            {"value": 1, "label": "Compliant", "definition": "The reply follows the policy."},
                            {"value": 0, "label": "Violation", "definition": "The reply breaks the policy."}
                        ]
                    }
                },
                {
                    "dimensionName": "tone",
                    "dimensionInstruction": "Classify the tone of the reply.",
                    "dimensionRatingScale": {
                        "categorical": [
                            {"label": "friendly", "definition": "Warm and polite."},
                            {"label": "neutral", "definition": "Polite but impersonal."},
                            {"label": "curt", "definition": "Short, dismissive, or impolite."}
                        ]
                    }
                }
            ]
        }
    }
}
```

Create the evaluator the same way as any custom evaluator. For example, with the AWS SDK for Python (Boto3):

```
import json
import boto3

client = boto3.client("bedrock-agentcore-control")

with open("support_quality_config.json") as f:
    evaluator_config = json.load(f)

response = client.create_evaluator(
    evaluatorName="SupportQuality",
    level="TRACE",
    evaluatorConfig=evaluator_config,
)
print(response["evaluatorId"])
```

In the console, choose **Multiple dimensions** when you create the evaluator. For the steps, see [Create evaluator](create-evaluator.md).

The AgentCore CLI `--rating-scale` option takes a single numerical or categorical scale. To create a multi-dimension evaluator, use the console, the AWS SDK, or the AWS CLI.

## Write instructions for dimensions
<a name="multi-dimension-evaluators-instructions"></a>

The judge model receives the evaluator’s `instructions`, then a section for each dimension with its name, instruction, and rating scale. The service then adds the output format, which asks for a rating and reasoning for every dimension. Don’t describe an output format in your instructions. To get consistent results:
+ Put shared content in `instructions`: the task, the placeholders that bring in the trace or session, and how to read the conversation. `instructions` must include at least one placeholder for the evaluator’s level, as for any LLM-as-a-judge evaluator.
+ Keep each `dimensionInstruction` to the one thing that dimension rates. Don’t repeat the shared context.
+ Make dimensions independent. If two dimensions measure the same thing, merge them.
+ The judge model writes an explanation and a rating for every dimension, so its output grows with the number of dimensions. Set `maxTokens` (or `maxOutputTokens` for `responsesEvaluatorModelConfig`) high enough for all dimensions. If the output is cut off, the evaluation fails.

## Results
<a name="multi-dimension-evaluators-results"></a>

A multi-dimension evaluator produces one result per dimension for each target it evaluates. The dimension is identified as follows on each surface.


| Surface | Result format | 
| --- | --- | 
| On-demand evaluation (`Evaluate`) | One entry in `evaluationResults` per dimension. `evaluatorName` is the evaluator’s name, and `evaluationDimensionName` is the dimension’s name. Numerical dimensions return `value` and `label`, and categorical dimensions return `label`. | 
| Online and batch evaluation (CloudWatch Logs) | One result record per dimension. The `gen_ai.evaluation.name` attribute is `<evaluatorName>/<dimensionName>`, for example `SupportQuality/tone`. | 
| CloudWatch Metrics | One metric per numerical dimension, named `<evaluatorName>/<dimensionName>`, with the same metric dimensions as other evaluators. Categorical dimensions don’t publish metrics. Their results are in CloudWatch Logs. | 
| Batch evaluation | One entry in `evaluatorSummaries` per dimension, with `evaluationDimensionName` set. For categorical dimensions, `statistics` is empty. Sessions that fail before the judge runs are counted in a separate entry for the evaluator without `evaluationDimensionName`. See [Errors and token usage](#multi-dimension-evaluators-errors). | 

The following is an excerpt of an `Evaluate` response for the `SupportQuality` evaluator on one trace:

```
{
    "evaluationResults": [
        {
            "evaluatorId": "SupportQuality-a1b2c3d4e5",
            "evaluatorName": "SupportQuality",
            "evaluationDimensionName": "issue_resolution",
            "value": 1.0,
            "label": "Resolved",
            "explanation": "The assistant identified the missing order and gave the correct tracking link...",
            "context": {"spanContext": {"sessionId": "session-123", "traceId": "6a827b653032d37116d7c1931a9835b5"}},
            "tokenUsage": {"inputTokens": 1015, "outputTokens": 316, "totalTokens": 1331}
        },
        {
            "evaluatorId": "SupportQuality-a1b2c3d4e5",
            "evaluatorName": "SupportQuality",
            "evaluationDimensionName": "policy_compliance",
            "value": 1.0,
            "label": "Compliant",
            "explanation": "No refund was promised and no account details were shared...",
            "context": {"spanContext": {"sessionId": "session-123", "traceId": "6a827b653032d37116d7c1931a9835b5"}}
        },
        {
            "evaluatorId": "SupportQuality-a1b2c3d4e5",
            "evaluatorName": "SupportQuality",
            "evaluationDimensionName": "tone",
            "label": "friendly",
            "explanation": "The reply is warm and thanks the customer...",
            "context": {"spanContext": {"sessionId": "session-123", "traceId": "6a827b653032d37116d7c1931a9835b5"}}
        }
    ]
}
```

To query one dimension’s online results in CloudWatch Logs Insights, filter on the composite name:

```
fields @timestamp, attributes.gen_ai.evaluation.score.value, attributes.gen_ai.evaluation.score.label
| filter attributes.gen_ai.evaluation.name = "SupportQuality/policy_compliance"
| sort @timestamp desc
```

For more about result records and metrics, see [Results and output](results-and-output.md).

## Errors and token usage
<a name="multi-dimension-evaluators-errors"></a>
+  **Evaluation-level errors.** If the evaluation can’t run for a target:
  + In on-demand evaluation, every dimension returns an error.
  + In online and batch evaluation, you get a single error result named after the evaluator, without a dimension. In CloudWatch Logs, its `gen_ai.evaluation.name` is the evaluator name alone. In batch `evaluatorSummaries`, these sessions are counted in `totalFailed` of an entry for the evaluator that has no `evaluationDimensionName`.
+  **Judge call errors.** If the judge call fails or its output can’t be parsed, for example because it was cut off at `maxTokens`, every dimension returns an error.
+  **Dimension errors.** If the judge returns a missing or out-of-scale rating for a dimension, the service asks the judge to correct it. If the rating is still invalid, only that dimension returns an error. The other dimensions keep their results.
+  **Token usage.** Token usage is reported once per judge call, in `tokenUsage` on the first dimension that was scored successfully. If every dimension returned an error, no result includes `tokenUsage`. To get the token usage for a target, add up `tokenUsage` across that target’s results.

## Feature support
<a name="multi-dimension-evaluators-support"></a>


| Feature | Supported | Notes | 
| --- | --- | --- | 
| On-demand evaluation | Yes | One result per dimension. | 
| Online evaluation | Yes | One result record per dimension. | 
| Batch evaluation | Yes | One summary per dimension. | 
| A/B testing | No | Using a multi-dimension evaluator in an A/B test returns a validation error. See [A/B testing prerequisites](ab-testing-prereqs.md). | 
| Recommendations | No | A recommendation whose evaluator is a multi-dimension evaluator returns a validation error. See [System prompt recommendations](recommendations-system-prompt.md). | 