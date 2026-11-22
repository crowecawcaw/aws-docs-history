

# Dataset schema

A dataset contains one or more scenarios. Each scenario represents a conversation (session) with the agent. The [AgentCore-run dataset evaluation](batch-evaluations-dataset.md), [SDK on-demand runner](dataset-evaluations-on-demand.md), and [SDK batch runner](dataset-evaluations-batch.md) use the same dataset format.

A dataset doesn’t declare a schema type. It holds two kinds of scenarios, and a single dataset can mix both:
+  **Fixed scenarios** use a fixed sequence of turns that you author by hand. The runner replays the turns exactly as written.
+  **Dynamic scenarios** use a large language model (LLM)-backed actor to generate turns dynamically based on a persona and goal. See [User simulation](user-simulation.md) for details on actor profiles and simulation configuration.

The fields in each scenario determine how it runs. A scenario with a `turns` field is a fixed scenario. A scenario without `turns` is a dynamic scenario, and you must give it `input`, `actor_profile`, or both. `FileDatasetProvider` uses the same rules when it loads a dataset for an SDK runner, and loads fixed scenarios as `PredefinedScenario` and dynamic scenarios as `SimulatedScenario`.

Every example requires a non-empty string `scenario_id`, which is the **unique identifier** of the scenario within the dataset. AgentCore rejects an example that contains none of `turns`, `input`, or `actor_profile` with the error `A scenario must include 'turns', 'input' or 'actor_profile'`. AgentCore validates an example that contains `turns` together with `input`, `actor_profile`, or both against the rules for both fixed and dynamic scenarios.

## Fixed scenarios
<a name="dataset-schema-predefined"></a>

A fixed scenario specifies a fixed sequence of turns with known inputs and optional expected outputs. The `turns` field is a non-empty list of 1–100 turns.

**Note**  
A fixed scenario (an example that contains only `turns`) cannot include `reward_function`.

### Single-turn example
<a name="dataset-schema-predefined-single-turn"></a>

Each scenario sends one prompt and checks the response:

```json
{
  "scenarios": [
    {
      "scenario_id": "math-question",
      "turns": [
        {
          "input": "What is 15 + 27?",
          "expected_response": "15 + 27 = 42"
        }
      ],
      "expected_trajectory": ["calculator"],
      "assertions": ["Agent used the calculator tool to compute the result"]
    },
    {
      "scenario_id": "weather-check",
      "turns": [
        {
          "input": "What's the weather?",
          "expected_response": "The weather is sunny"
        }
      ],
      "expected_trajectory": ["weather"],
      "assertions": ["Agent used the weather tool"]
    }
  ]
}
```

### Multi-turn example
<a name="dataset-schema-predefined-multi-turn"></a>

Multi-turn scenarios have multiple turns per scenario. Turns execute sequentially within the same session, maintaining conversation context. Each turn can have its own `expected_response`, while `assertions` and `expected_trajectory` apply to the entire session:

```json
{
  "scenarios": [
    {
      "scenario_id": "math-follow-up",
      "turns": [
        {
          "input": "What is 15 + 27?",
          "expected_response": "15 + 27 = 42"
        },
        {
          "input": "Now multiply that result by 2.",
          "expected_response": "42 × 2 = 84"
        }
      ],
      "expected_trajectory": ["calculator", "calculator"],
      "assertions": [
        "Agent used the calculator tool for both calculations",
        "Agent used the result of the first turn (42) in the second calculation"
      ]
    }
  ]
}
```

### Scenario fields
<a name="dataset-schema-predefined-fields"></a>


| Field | Required | Type | Constraints | Description | 
| --- | --- | --- | --- | --- | 
|  `scenario_id`  | Yes | String | Non-empty |  **The unique identifier for the scenario.** Use a different `scenario_id` for each scenario in the dataset. A request that contains duplicate `scenario_id` values is rejected. | 
|  `turns`  | Yes | List of objects | Non-empty list of 1–100 turns | List of turns in the conversation. Each turn has `input` (required) and `expected_response` (optional). | 
|  `expected_trajectory`  | No | List of strings |  | Expected sequence of tool names. Used by trajectory evaluators (`Builtin.TrajectoryExactOrderMatch`, `Builtin.TrajectoryInOrderMatch`, `Builtin.TrajectoryAnyOrderMatch`). | 
|  `assertions`  | No | List of strings |  | Natural language assertions about expected behavior. Used by `Builtin.GoalSuccessRate`. | 
|  `scenario_description`  | No | String |  | Optional metadata describing the scenario. Useful for organizing and identifying scenarios in results. | 
|  `metadata`  | No | Object | Up to 2 KB when serialized as compact UTF-8 JSON | Your key-value metadata for the scenario. AgentCore-added metadata keys don’t count toward the limit. | 

### Turn fields
<a name="dataset-schema-turn-fields"></a>

The following table lists the fields of a turn object.


| Field | Required | Type | Constraints | Description | 
| --- | --- | --- | --- | --- | 
|  `input`  | Yes | String or Object | Non-empty | The prompt sent to the agent for this turn. Can be a plain string (for example, `"What is the weather in Seattle today?"`) or a structured object (for example, `{"role": "user", "content": "What is the weather in Seattle today?"}`). | 
|  `expected_response`  | No | String |  | The expected agent response for this turn. Used by `Builtin.Correctness`. Mapped positionally to the trace produced by this turn; turn 0 maps to trace 0, turn 1 maps to trace 1. | 

## Dynamic scenarios
<a name="dataset-schema-simulated"></a>

A dynamic scenario provides an `input`, an `actor_profile`, or both. When an `actor_profile` is present, the actor generates subsequent turns dynamically:

```json
{
  "scenarios": [
    {
      "scenario_id": "geography-student",
      "scenario_description": "A curious student asks geography questions",
      "actor_profile": {
        "traits": {"expertise": "novice", "tone": "curious"},
        "context": "A student studying world geography who wants to learn about capitals",
        "goal": "Find out the capital cities of at least two different countries"
      },
      "input": "Hi! I'm studying geography. Can you help me learn about world capitals?",
      "max_turns": 5,
      "assertions": [
        "Agent provides accurate capital city information",
        "Agent is helpful and encouraging to the student"
      ]
    }
  ]
}
```

### Scenario fields
<a name="dataset-schema-simulated-fields"></a>


| Field | Required | Type | Constraints | Description | 
| --- | --- | --- | --- | --- | 
|  `scenario_id`  | Yes | String | Non-empty |  **The unique identifier for the scenario.** Use a different `scenario_id` for each scenario in the dataset. A request that contains duplicate `scenario_id` values is rejected. | 
|  `input`  | Conditional | String, object, or list | Non-empty | The first message sent to your agent to start the conversation. Can be a plain string, a structured object, or a list of role/content messages with the roles `user`, `assistant`, or `tool`. Provide `input`, `actor_profile`, or both. A scenario with `input` and no `actor_profile` runs as a single turn. | 
|  `actor_profile`  | Conditional | Object | Must contain `context` and `goal`  | The actor’s identity and objective. For the fields of this object, see [Actor profile fields](#dataset-schema-actor-profile-fields). Provide `input`, `actor_profile`, or both. See [User simulation](user-simulation.md). | 
|  `scenario_description`  | No | String |  | Optional metadata describing the scenario. Useful for organizing and identifying scenarios in results. | 
|  `max_turns`  | No | Integer | 1 or greater | Maximum number of turns before the conversation stops. Default: 30. Used only when `actor_profile` is present. | 
|  `expected_trajectory`  | No | List of strings |  | Expected sequence of tool names. Supported for dynamic scenarios because it applies to the completed session rather than to predetermined turns. | 
|  `assertions`  | No | List of strings |  | Natural language assertions about expected behavior. Used by `Builtin.GoalSuccessRate`. | 
|  `metadata`  | No | Object | Up to 2 KB when serialized as compact UTF-8 JSON | Your key-value metadata for the scenario. AgentCore-added metadata keys don’t count toward the limit. | 
|  `agent_invocation_headers`  | No | Object |  | Optional headers to include when AgentCore invokes the agent. | 
|  `reward_function`  | No | String | Non-empty | A reward function used to score the conversation. When present, `ground_truth_response` is also required. | 
|  `ground_truth_response`  | No | String | Non-empty | The reference response used by `reward_function`. Required when `reward_function` is present. | 

You must provide at least one of `input` or `actor_profile`. Dynamic scenarios support session-level `expected_trajectory` and `assertions`. They don’t support per-turn `expected_response` because the actor writes the user turns during the run.

### Actor profile fields
<a name="dataset-schema-actor-profile-fields"></a>

The `actor_profile` object describes the actor that drives the conversation. The following table lists its fields.


| Field | Required | Type | Constraints | Description | 
| --- | --- | --- | --- | --- | 
|  `context`  | Yes | String |  | The actor’s background and situation. | 
|  `goal`  | Yes | String |  | What the actor is trying to accomplish in the conversation. | 
|  `known_info`  | No | String |  | Information the actor already knows. | 
|  `unknown_info`  | No | String |  | Information the actor does not know. | 
|  `traits`  | No | Object |  | Optional personality traits that shape how the actor communicates. | 

## Ground truth mapping
<a name="dataset-schema-ground-truth"></a>

The service and the SDK runners map dataset fields to the evaluators that use them:


| Evaluator | Ground truth field | Level | Description | 
| --- | --- | --- | --- | 
|  `Builtin.Correctness`  |  `turns[].expected_response`  | Trace | Measures how accurately the agent’s response matches the expected answer. | 
|  `Builtin.GoalSuccessRate`  |  `assertions`  | Session | Validates whether the agent’s behavior satisfies natural language assertions. | 
|  `Builtin.TrajectoryExactOrderMatch`  |  `expected_trajectory`  | Session | Checks that the actual tool call sequence matches exactly. | 
|  `Builtin.TrajectoryInOrderMatch`  |  `expected_trajectory`  | Session | Checks that expected tools appear in order, allowing extras between them. | 
|  `Builtin.TrajectoryAnyOrderMatch`  |  `expected_trajectory`  | Session | Checks that all expected tools are present, regardless of order. | 
+ Ground truth fields are optional. Evaluators that do not use ground truth (for example, `Builtin.Helpfulness`, `Builtin.Faithfulness`) evaluate based on session content alone.
+ You can include all ground truth fields in a single dataset. Each runner routes the relevant fields to the appropriate evaluators.
+ If you select a trajectory evaluator, every fixed and dynamic scenario must have a non-empty `expected_trajectory`. This means a mixed dataset can use trajectory evaluators when every scenario supplies that field.
+ If no ground truth fields are present, evaluators fall back to their ground truth-free mode.

For more details on ground truth fields and how they work with the Evaluate API, see [Ground truth evaluations](ground-truth-evaluations.md).

## Inline dataset construction
<a name="dataset-schema-inline-construction"></a>

Instead of loading from a JSON file, you can construct datasets directly in Python. In the AgentCore SDK, the `PredefinedScenario` class represents a fixed scenario and the `SimulatedScenario` class represents a dynamic scenario. The following example constructs a dataset of fixed scenarios:

```python
from bedrock_agentcore.evaluation import Dataset, PredefinedScenario, Turn

dataset = Dataset(
    scenarios=[
        PredefinedScenario(
            scenario_id="math-question",
            turns=[
                Turn(
                    input="What is 15 + 27?",
                    expected_response="15 + 27 = 42",
                ),
            ],
            expected_trajectory=["calculator"],
            assertions=["Agent used the calculator tool"],
        ),
        PredefinedScenario(
            scenario_id="weather-check",
            turns=[
                Turn(input="What's the weather?"),
            ],
            expected_trajectory=["weather"],
        ),
    ]
)
```

Or load from a JSON file:

```python
from bedrock_agentcore.evaluation import FileDatasetProvider

dataset = FileDatasetProvider("dataset.json").get_dataset()
```