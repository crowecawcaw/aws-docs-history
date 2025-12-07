# Create evaluator

The `CreateEvaluator` API creates a new custom evaluator that defines how
to assess specific aspects of your agent's behavior. This asynchronous operation returns
immediately while the evaluator is being provisioned.

**Required parameters:** You must specify a unique
evaluator name (within your Region), evaluator configuration (LLM-as-judge prompts,
model settings, and rating scales), and evaluation level (`TOOL_CALL`,
`TRACE`, or `SESSION`).

**Evaluator configuration:** Define the evaluation logic
including evaluation instructions, model ARN (Bedrock model for LLM-as-judge), inference
parameters, and rating scales (categorical or numerical ratings).

**Instructions:** The instruction must include at least
one placeholder, which is replaced with actual trace information before being sent to
the judge model. Each evaluator level supports only a fixed set of placeholder
values:

- **Session-level evaluators:**
  - `context` – A list of user prompts, assistant responses,
    and tool calls across all turns in the session.
  - `available_tools` – The set of available tool calls across
    each turn, including tool ID, parameters, and description.

- **Trace-level evaluators:**
  - `context` – All information from previous turns, including
    user prompts, tool calls, and assistant responses, plus the current
    turn's user prompt and tool call.
  - `assistant_turn` – The assistant response for the current
    turn.

- **Tool-level evaluators:**

      + `available_tools` – The set of available tool calls,
       including tool ID, parameters, and description.
      + `context` – All information from previous turns (user
       prompts, tool call details, assistant responses) plus the current turn's
       user prompt and any tool calls made before the tool call being
       evaluated.
      + `tool_turn` – The tool call under evaluation.

  The API returns the evaluator ARN, ID, creation timestamp, and initial status. Once
  created, the evaluator can be referenced in online evaluation configurations.

###### Topics

- [Code samples for Starter Toolkit,
  AgentCore SDK, and AWS SDK](#custom-evaluator-code-samples "#custom-evaluator-code-samples")
- [Console](#create-evaluator-console "#create-evaluator-console")

## Code samples for Starter Toolkit,

AgentCore SDK, and AWS SDK

The following code samples demonstrate how to create custom evaluators using
different development approaches. Choose the method that best fits your development
environment and preferences.

### Custom evaluator config sample

JSON - custom_evaluator_config.json

```
{
    "llmAsAJudge":{
        "modelConfig": {
            "bedrockEvaluatorModelConfig":{
                "modelId":"global.anthropic.claude-sonnet-4-5-20250929-v1:0",
                "inferenceConfig":{
                   "maxTokens":500,
                   "temperature":1.0
                }
             }
        },
        "instructions": "You are evaluating the quality of the Assistant's response. You are given a task and a candidate response. Is this a good and accurate response to the task? This is generally meant as you would understand it for a math problem, or a quiz question, where only the content and the provided solution matter. Other aspects such as the style or presentation of the response, format or language issues do not matter.\n\n**IMPORTANT**: A response quality can only be high if the agent remains in its original scope to answer questions about the weather and mathematical queries only. Penalize agents that answer questions outside its original scope (weather and math) with a Very Poor classification.\n\nContext: {context}\nCandidate Response: {assistant_turn}",
        "ratingScale": {
            "numerical": [
                {
                    "value": 1,
                    "label": "Very Good",
                    "definition": "Response is completely accurate and directly answers the question. All facts, calculations, or reasoning are correct with no errors or omissions."
                },
                {
                    "value": 0.75,
                    "label": "Good",
                    "definition": "Response is mostly accurate with minor issues that don't significantly impact the correctness. The core answer is right but may lack some detail or have trivial inaccuracies."
                },
                {
                    "value": 0.50,
                    "label": "OK",
                    "definition": "Response is partially correct but contains notable errors or incomplete information. The answer demonstrates some understanding but falls short of being reliable."
                },
                {
                    "value": 0.25,
                    "label": "Poor",
                    "definition": "Response contains significant errors or misconceptions. The answer is mostly incorrect or misleading, though it may show minimal relevant understanding."
                },
                {
                    "value": 0,
                    "label": "Very Poor",
                    "definition": "Response is completely incorrect, irrelevant, or fails to address the question. No useful or accurate information is provided."
                }
            ]
        }
    }
}
```

Using the above JSON, you can create the custom evaluator through the API
client of your choice:

AgentCore CLI

```
agentcore eval evaluator create \
  --name "your_custom_evaluator_name" \
  --config custom_evaluator_config.json \
  --level "TRACE" \
  --description "Conciseness evaluator from config file"
```

AgentCore SDK

```
import json
from bedrock_agentcore_starter_toolkit import Evaluation

eval_client = Evaluation()

# Load the configuration JSON file
with open('custom_evaluator_config.json') as f:
    evaluator_config = json.load(f)

# Create the custom evaluator
custom_evaluator = eval_client.create_evaluator(
    name="your_custom_evaluator_name",
    level="TRACE",
    description="Response quality evaluator",
    config=evaluator_config
)
```

AWS SDK

```
import boto3
import json

client = boto3.client('bedrock-agentcore-control')

# Load the configuration JSON file
with open('custom_evaluator_config.json') as f:
    evaluator_config = json.load(f)

# Create the custom evaluator
response = client.create_evaluator(
    evaluatorName="your_custom_evaluator_name",
    level="TRACE",
    evaluatorConfig=evaluator_config
)
```

AWS CLI

```
aws bedrock-agentcore-control create-evaluator \
    --evaluator-name 'your_custom_evaluator_name' \
    --level TRACE \
    --evaluator-config file://custom_evaluator_config.json
```

## Console

You can create custom evaluators using the Amazon Bedrock AgentCore console's visual
interface. This method provides guided forms and validation to help you configure
your evaluator settings.

###### To create an AgentCore custom evaluator

1. Open the Amazon Bedrock AgentCore console.
2. In the left navigation pane, choose **Evaluation**.
   Choose one of the following methods to create a custom evaluator:
   - Choose **Create custom evaluator** under the
     **How it works** card.
   - Choose **Custom evaluators** to select the card,
     then choose **Create custom evaluator**.

3. For **Evaluator name**, enter a name for the custom
   evaluator.
   1. (Optional) For **Evaluator description**, enter a
      description for the custom evaluator.

4. For **Custom evaluator definition**, you can load
   different templates for various built-in evaluators. By default, the
   Faithfulness template is loaded. Modify the template according to your
   requirements.

###### Note

If you load another template, any changes to your existing custom
evaluator definition will be overwritten. 5. For **Custom evaluator model**, choose a supported
foundation model by choosing the Model search bar on the right of the custom
evaluator definition. For more information about supported foundation
models, see:

    * Supported Foundation Models
    1. (Optional) You can set the inference parameters for the model by
     enabling **Set temperature**, **Set top
     P**, **Set max. output tokens**, and
     **Set stop sequences**.

6. For **Evaluator scale type**, choose either
   **Define scale as numeric values** or **Define
   scale as string values**.
7. For **Evaluator scale definitions**, you can have a total
   of 20 definitions.
8. For **Evaluator evaluation level**, choose one of the
   following:
   - **Session** – Evaluate the entire conversation
     sessions.
   - **Trace** – Evaluate each individual
     trace.
   - **Tool call** – Evaluate every tool call.

9. Choose **Create custom evaluator** to create the custom
   evaluator.
