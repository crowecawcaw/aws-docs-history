# Third-party evaluators

AgentCore Evaluations offers evaluators from the DeepEval and AutoEval open source libraries. If you already use these libraries, you can run the same metrics inside AgentCore Evaluations. The service handles hosting and evaluation code for you. With the managed option, the service also selects the model and runs inference, the same way it does for built-in evaluators.

There are two ways to use third-party evaluators:

- **Managed** – Select a third-party evaluator by ID and deploy it. The service runs it, selects the model, and manages the library version.
- **Custom** – Create an evaluator that runs an existing evaluator’s logic—a built-in or a managed third-party evaluator—on your own model and inference. For more information, see [Custom evaluators derived from a base evaluator](#third-party-evaluator-custom "#third-party-evaluator-custom").

###### Evaluator quality

AgentCore built-in evaluators are tested and benchmarked for performance. DeepEval and AutoEval are open source evaluators, and we don’t make claims about their quality.

###### Topics

- [Evaluator identity](#third-party-evaluator-identity "#third-party-evaluator-identity")
- [Discover available evaluators](#third-party-evaluator-discover "#third-party-evaluator-discover")
- [Managed third-party evaluators](#third-party-evaluator-managed "#third-party-evaluator-managed")
- [Custom evaluators derived from a base evaluator](#third-party-evaluator-custom "#third-party-evaluator-custom")
- [Results](#third-party-evaluator-results "#third-party-evaluator-results")
- [Initial set of evaluators](#third-party-evaluator-initial-set "#third-party-evaluator-initial-set")
- [Console](#third-party-evaluator-console "#third-party-evaluator-console")

## Evaluator identity

Two fields together identify every evaluator, including third-party evaluators:

- `evaluatorType` – The kind of resource: who provides it and how. `Builtin` and `ThirdParty` are AWS-managed global evaluators that you reference but don’t create. `Custom`, `CustomCode`, and `CustomDerived` are evaluators that you create.
- `provider` – Where the evaluation logic comes from: `AWS` for AWS-authored evaluators, `DeepEval` or `AutoEval` for the corresponding third-party libraries, or `Custom` for an evaluator you authored yourself.

The two fields are independent, so each evaluator is one `(evaluatorType, provider)` pair:

| Evaluator                                             | evaluatorType   | provider                 |
| ----------------------------------------------------- | --------------- | ------------------------ |
| Managed built-in                                      | `Builtin`       | `AWS`                    |
| Managed third-party                                   | `ThirdParty`    | `DeepEval` or `AutoEval` |
| Custom evaluator derived from a built-in              | `CustomDerived` | `AWS`                    |
| Custom evaluator derived from a third-party evaluator | `CustomDerived` | `DeepEval` or `AutoEval` |
| Custom code-based evaluator                           | `CustomCode`    | `Custom`                 |
| Custom LLM-as-a-judge evaluator                       | `Custom`        | `Custom`                 |

A managed third-party evaluator’s ID follows the `ThirdParty.<Provider>.<Metric>` format—for example, `ThirdParty.DeepEval.TaskCompletion` or `ThirdParty.AutoEval.Security`. This mirrors the `Builtin.<Metric>` format used for first-party built-in evaluators.

## Discover available evaluators

Third-party evaluators are returned by the `ListEvaluators` API alongside first-party built-in evaluators and any custom evaluators in your account.

```
{
  "evaluators": [
    {
      "evaluatorId": "Builtin.Helpfulness",
      "evaluatorType": "Builtin",
      "provider": "AWS",
      "level": "TRACE",
      "status": "ACTIVE"
    },
    {
      "evaluatorId": "ThirdParty.DeepEval.TaskCompletion",
      "evaluatorType": "ThirdParty",
      "provider": "DeepEval",
      "level": "TRACE",
      "status": "ACTIVE"
    },
    {
      "evaluatorId": "ThirdParty.AutoEval.Security",
      "evaluatorType": "ThirdParty",
      "provider": "AutoEval",
      "level": "TRACE",
      "status": "ACTIVE"
    }
  ]
}
```

## Managed third-party evaluators

Use a managed third-party evaluator exactly like a built-in evaluator: select it by ID, and the service runs it on a model it operates. You don’t supply a model, prompt, or configuration.

- **Model:** Managed third-party evaluators run on the same model as the built-in evaluators in Amazon Bedrock AgentCore. There’s no model field and no model configuration to set.
- **Versioning:** There’s no version selection for managed third-party evaluators. The service runs the library version it has validated and manages upgrades itself.

You can pass a managed third-party evaluator’s ID anywhere you would pass a built-in evaluator ID:

- **On-demand evaluation** – Pass the ID in the `Evaluate` API request.
- **Online evaluation** – Add the ID to the `evaluators` list of an [online evaluation configuration](create-online-evaluations.md "create-online-evaluations.md"). It mixes freely with built-in and custom evaluators, and is governed by the same sampling and filtering rules.
- **Batch evaluation** – Pass the ID in the `evaluators` list of a [batch evaluation job](batch-evaluations-start.md "batch-evaluations-start.md").

The following example runs a managed third-party evaluator with the `Evaluate` API:

```
import boto3

client = boto3.client('bedrock-agentcore')

response = client.evaluate(
    evaluatorId="ThirdParty.DeepEval.TaskCompletion",
    evaluationInput={"sessionSpans": session_span_logs}
)

for result in response["evaluationResults"]:
    print(f"Value: {result.get('value')}")
    print(f"Explanation: {result.get('explanation', '')}")
```

## Custom evaluators derived from a base evaluator

Use a custom derived evaluator to run an existing evaluator—a built-in or managed third-party evaluator—on your own model. Instead of using the model the service picks, you supply the model and inference parameters. The base evaluator supplies the prompt and the scoring. This applies only to LLM-based evaluators.

To create a custom derived evaluator, specify the `derived` member of `evaluatorConfig` with the ID of the base evaluator and your model configuration. Save the following as `derived_evaluator_config.json`:

```
{
    "derived": {
        "baseEvaluatorId": "ThirdParty.DeepEval.TaskCompletion",
        "modelConfig": {
            "bedrockEvaluatorModelConfig": {
                "modelId": "global.anthropic.claude-sonnet-4-5-20250929-v1:0",
                "inferenceConfig": {
                    "temperature": 0.0,
                    "topP": 1.0,
                    "maxTokens": 2048
                }
            }
        }
    }
}
```

You can also derive a custom evaluator from a built-in evaluator by setting `baseEvaluatorId` to a `Builtin.` ID instead of a `ThirdParty.` ID.

Create the evaluator with the AWS CLI:

```
aws bedrock-agentcore-control create-evaluator \
    --evaluator-name 'my_task_completion' \
    --evaluator-config file://derived_evaluator_config.json
```

The resulting evaluator has `evaluatorType` set to `CustomDerived`. The service derives `provider` automatically from the base evaluator: `AWS` for a `Builtin.` base, or the provider name for a `ThirdParty.` base. You don’t set `level`—the service derives it from the base evaluator, and it’s read-only on `GetEvaluator`. You also don’t set `instructions` or `ratingScale` because the base evaluator owns both.

After you create the evaluator, use it exactly like any other custom evaluator: pass its evaluator ID to `Evaluate`, or add it to the `evaluators` list of an online or batch evaluation.

- **Model:** Any Bedrock model, set through `bedrockEvaluatorModelConfig`.
- **Inference ownership:** The model runs using your own AWS account and credentials—the execution role for online evaluation, or the caller’s credentials for on-demand evaluation. This is the key difference from a managed third-party evaluator, where the service runs the model on its own capacity.
- **Quality ownership:** Because you choose the model, evaluation quality reflects that choice. The service doesn’t validate the model against each metric.

## Results

Third-party evaluators return the same result shape as built-in and custom evaluators, in the same locations. For more information, see [Results and output](results-and-output.md "results-and-output.md").

## Initial set of evaluators

The following evaluators are available at launch.

**DeepEval**

| Metric                   | What it checks                                                            |
| ------------------------ | ------------------------------------------------------------------------- |
| Bias                     | Whether the output shows gender, political, racial, or geographical bias. |
| Toxicity                 | Whether the output contains attacks, mockery, hate, or threats.           |
| PIILeakage               | Whether the response exposes personal information.                        |
| Summarization            | Whether the summary is faithful and comprehensive.                        |
| TaskCompletion           | Whether the agent accomplished the user’s goal.                           |
| ConversationCompleteness | Whether all user requests across the conversation were addressed.         |
| KnowledgeRetention       | Whether the agent remembered information shared earlier.                  |
| TurnRelevancy            | Whether each reply stays relevant to the prior turns.                     |
| GoalAccuracy             | Whether the agent achieved its goals across a multi-turn conversation.    |
| ToolUse                  | Whether the agent picked the right tool and passed correct arguments.     |

**AutoEval**

| Metric   | What it checks                                                          |
| -------- | ----------------------------------------------------------------------- |
| Security | Whether the response is malicious.                                      |
| Humor    | Whether the response is funny.                                          |
| Possible | Whether the agent attempted a solution or declared the task impossible. |

## Console

In the evaluator picker, third-party evaluators appear in their own **Third-party evaluators** section, grouped by provider, separate from the built-in evaluator groups. This section is collapsed by default.

To create a custom evaluator derived from a base evaluator, use the existing **Create custom evaluator** flow and choose **Third-party library** as the evaluator definition type. This option removes the instruction and scale sections shown for LLM-as-a-judge, since the base evaluator owns the prompt and scoring. Choose a library and metric, then supply the model and inference parameters. The evaluation level is shown read-only, set by the metric.
