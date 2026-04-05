# Dataset evaluations

Dataset evaluations let you run your agent against a predefined set of scenarios and
automatically evaluate the results. Instead of manually invoking your agent and collecting
spans, the `OnDemandEvaluationDatasetRunner` from the AgentCore SDK orchestrates the
entire lifecycle — invoke the agent, wait for telemetry ingestion, collect spans, and call
the Evaluate API — in a single `run()` call.

This is useful for regression testing, benchmark datasets, and CI/CD pipelines where you
want to evaluate agent quality across many scenarios automatically.

###### Note

Dataset evaluations support all AgentCore evaluators — all built-in evaluators
across session, trace, and tool-call levels, as well as custom evaluators. The runner
automatically handles level-aware request construction, batching, and ground truth
mapping for whichever evaluators you configure.

###### Topics

- [How it works](#ds-how-it-works "#ds-how-it-works")
- [Prerequisites](#ds-prerequisites "#ds-prerequisites")
- [Dataset schema](#ds-dataset-schema "#ds-dataset-schema")
- [Single-turn example](#ds-single-turn "#ds-single-turn")
- [Multi-turn example](#ds-multi-turn "#ds-multi-turn")
- [Inline dataset construction](#ds-inline-construction "#ds-inline-construction")
- [Components reference](#ds-components-reference "#ds-components-reference")
- [Result structure](#ds-result-structure "#ds-result-structure")

## How it works

The runner processes scenarios in three phases:

1. **Invoke** — All scenarios run concurrently using a thread pool. Each scenario gets a
   unique session ID, and turns within a scenario execute sequentially to maintain
   conversation context.
2. **Wait** — A configurable delay (default: 180 seconds) allows CloudWatch to ingest
   the telemetry data. This delay is paid once, not per-scenario.
3. **Evaluate** — Spans are collected from CloudWatch and evaluation requests are built
   for each evaluator. Ground truth fields from the dataset (`expected_response`,
   `assertions`, `expected_trajectory`) are automatically mapped to the correct API
   reference inputs.

## Prerequisites

- Python 3.10+
- An agent deployed on AgentCore Runtime with observability enabled, or an agent built
  with a supported framework configured with
  [AgentCore Observability](observability-configure.md#observability-configure-3p "observability-configure.md#observability-configure-3p").
  Supported frameworks:
  - Strands Agents
  - LangGraph with `opentelemetry-instrumentation-langchain` or
    `openinference-instrumentation-langchain`

- Transaction Search enabled in CloudWatch — see
  [Enable Transaction Search](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-getting-started.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-getting-started.md")
- The AgentCore SDK installed: `pip install bedrock-agentcore`
- AWS credentials configured with permissions for `bedrock-agentcore`,
  `bedrock-agentcore-control`, and `logs` (CloudWatch)

The following constants are used throughout the examples. Replace them with your own values:

```
REGION    = "<region-code>"
AGENT_ARN = "arn:aws:bedrock-agentcore:<region-code>:<account-id>:runtime/<agent-id>"
LOG_GROUP = "/aws/bedrock-agentcore/runtimes/<agent-id>-DEFAULT"
```

## Dataset schema

A dataset contains one or more scenarios. Each scenario represents a conversation
(session) with the agent. Scenarios can be single-turn or multi-turn.

```
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
    }
  ]
}
```

| Scenario fields       | Field | Required | Scope                                                                                                   | Description |
| --------------------- | ----- | -------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| `scenario_id`         | Yes   | —        | Unique identifier for the scenario.                                                                     |
| `turns`               | Yes   | —        | List of turns in the conversation. Each turn has `input` (required) and `expected_response` (optional). |
| `expected_trajectory` | No    | Session  | Expected sequence of tool names. Used by trajectory evaluators.                                         |
| `assertions`          | No    | Session  | Natural language assertions about expected behavior. Used by `Builtin.GoalSuccessRate`.                 |

| Turn fields         | Field | Required                                                                                           | Description |
| ------------------- | ----- | -------------------------------------------------------------------------------------------------- | ----------- |
| `input`             | Yes   | The prompt sent to the agent for this turn. Can be a string or a dict.                             |
| `expected_response` | No    | The expected agent response for this turn. Mapped positionally to the trace produced by this turn. |

The runner automatically maps dataset fields to the Evaluate API's
`evaluationReferenceInputs`:

- `expected_response` on each turn maps positionally to traces — turn 0 → trace 0,
  turn 1 → trace 1, and so on.
- `assertions` and `expected_trajectory` are scoped to the session level.
- If no ground truth fields are present, `evaluationReferenceInputs` is omitted from
  the API request.

## Single-turn example

A single-turn dataset has one turn per scenario. This is the simplest form — each
scenario sends one prompt and checks the response.

Save the following as `dataset.json`:

```
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

Run the evaluation:

```
import json
import boto3
from bedrock_agentcore.evaluation import (
    OnDemandEvaluationDatasetRunner,
    EvaluationRunConfig,
    EvaluatorConfig,
    FileDatasetProvider,
    CloudWatchAgentSpanCollector,
    AgentInvokerInput,
    AgentInvokerOutput,
)

# Load dataset
dataset = FileDatasetProvider("dataset.json").get_dataset()

# Define the agent invoker
agentcore_client = boto3.client("bedrock-agentcore", region_name=REGION)

def agent_invoker(invoker_input: AgentInvokerInput) -> AgentInvokerOutput:
    payload = invoker_input.payload
    if isinstance(payload, str):
        payload = json.dumps({"prompt": payload}).encode()
    elif isinstance(payload, dict):
        payload = json.dumps(payload).encode()

    response = agentcore_client.invoke_agent_runtime(
        agentRuntimeArn=AGENT_ARN,
        runtimeSessionId=invoker_input.session_id,
        payload=payload,
    )
    response_body = response["response"].read()
    return AgentInvokerOutput(agent_output=json.loads(response_body))

# Create span collector
span_collector = CloudWatchAgentSpanCollector(
    log_group_name=LOG_GROUP,
    region=REGION,
)

# Configure evaluators
config = EvaluationRunConfig(
    evaluator_config=EvaluatorConfig(
        evaluator_ids=[
            "Builtin.GoalSuccessRate",
            "Builtin.TrajectoryExactOrderMatch",
            "Builtin.TrajectoryInOrderMatch",
            "Builtin.TrajectoryAnyOrderMatch",
            "Builtin.Correctness",
            "Builtin.Helpfulness",
            "Builtin.ToolSelectionAccuracy"
        ],
    ),
    evaluation_delay_seconds=180,
    max_concurrent_scenarios=5,
)

# Run
runner = OnDemandEvaluationDatasetRunner(region=REGION)
result = runner.run(
    agent_invoker=agent_invoker,
    dataset=dataset,
    span_collector=span_collector,
    config=config,
)

print(f"Completed: {len(result.scenario_results)} scenario(s)")
```

Process results:

```
for scenario in result.scenario_results:
    print(f"\nScenario: {scenario.scenario_id} ({scenario.status})")
    if scenario.error:
        print(f"  Error: {scenario.error}")
        continue
    for evaluator in scenario.evaluator_results:
        print(f"  {evaluator.evaluator_id}:")
        for r in evaluator.results:
            print(f"    Score: {r.get('value')}, Label: {r.get('label')}")
            ignored = r.get("ignoredReferenceInputFields", [])
            if ignored:
                print(f"    Ignored fields: {ignored}")
```

To save results to a file:

```
with open("results.json", "w") as f:
    f.write(result.model_dump_json(indent=2))
```

## Multi-turn example

Multi-turn scenarios have multiple turns per scenario. Turns execute sequentially within
the same session, maintaining conversation context. Each turn can have its own
`expected_response`, while `assertions` and `expected_trajectory` apply to the entire
session.

Save the following as `multi_turn_dataset.json`:

```
{
  "scenarios": [
    {
      "scenario_id": "math-then-weather",
      "turns": [
        {
          "input": "What is 15 + 27?",
          "expected_response": "15 + 27 = 42"
        },
        {
          "input": "What's the weather?",
          "expected_response": "The weather is sunny"
        }
      ],
      "expected_trajectory": ["calculator", "weather"],
      "assertions": [
        "Agent used the calculator tool for the math question",
        "Agent used the weather tool when asked about weather"
      ]
    }
  ]
}
```

Run the evaluation:

```
dataset = FileDatasetProvider("multi_turn_dataset.json").get_dataset()

result = runner.run(
    agent_invoker=agent_invoker,
    dataset=dataset,
    span_collector=span_collector,
    config=config,
)

for scenario in result.scenario_results:
    print(f"Scenario: {scenario.scenario_id} ({scenario.status})")
    for evaluator in scenario.evaluator_results:
        for r in evaluator.results:
            trace = r.get("context", {}).get("spanContext", {}).get("traceId", "session")
            print(f"  {evaluator.evaluator_id} [{trace}]: {r.get('value')} ({r.get('label')})")
```

## Inline dataset construction

Instead of loading from a JSON file, you can construct datasets directly in Python:

```
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

## Components reference

The runner requires four components:

**Agent invoker**

A `Callable[[AgentInvokerInput], AgentInvokerOutput]` that invokes your agent for a
single turn. The runner calls this once per turn in each scenario.

| Agent invoker fields              | Field           | Type                                                                                             | Description |
| --------------------------------- | --------------- | ------------------------------------------------------------------------------------------------ | ----------- |
| `AgentInvokerInput.payload`       | `str` or `dict` | The turn input from the dataset.                                                                 |
| `AgentInvokerInput.session_id`    | `str`           | Stable across all turns in a scenario. Pass this to your agent to maintain conversation context. |
| `AgentInvokerOutput.agent_output` | `Any`           | The agent's response.                                                                            |

The invoker is framework-agnostic — you can call your agent via boto3
`invoke_agent_runtime`, a direct function call, HTTP request, or any other method.

**Span collector**

An `AgentSpanCollector` that retrieves telemetry spans after agent invocation. The SDK
ships `CloudWatchAgentSpanCollector`:

```
from bedrock_agentcore.evaluation import CloudWatchAgentSpanCollector

span_collector = CloudWatchAgentSpanCollector(
    log_group_name="/aws/bedrock-agentcore/runtimes/<agent-id>-DEFAULT",
    region=REGION,
)
```

The collector queries two CloudWatch log groups (`aws/spans` for structural spans and the
agent's log group for conversation content), polls until spans appear, and returns them as
a flat list.

**Evaluation config**

```
from bedrock_agentcore.evaluation import EvaluationRunConfig, EvaluatorConfig

config = EvaluationRunConfig(
    evaluator_config=EvaluatorConfig(
        evaluator_ids=["Builtin.Correctness", "Builtin.GoalSuccessRate"],
    ),
    evaluation_delay_seconds=180,  # Wait for CloudWatch ingestion (default: 180)
    max_concurrent_scenarios=5,    # Thread pool size (default: 5)
)
```

| Evaluation config fields         | Field | Default                                                                                                        | Description |
| -------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| `evaluator_config.evaluator_ids` | —     | List of evaluator IDs (built-in names or custom evaluator IDs).                                                |
| `evaluation_delay_seconds`       | 180   | Seconds to wait after invocation for CloudWatch to ingest spans. Set to 0 if using a non-CloudWatch collector. |
| `max_concurrent_scenarios`       | 5     | Maximum number of scenarios to invoke and evaluate in parallel.                                                |

**Dataset**

A `Dataset` loaded from a JSON file via `FileDatasetProvider` or constructed inline.
See [Dataset schema](#ds-dataset-schema "#ds-dataset-schema") for the full field reference.

## Result structure

The runner returns an `EvaluationResult` with the following structure:

```
EvaluationResult
  └── scenario_results: List[ScenarioResult]
        ├── scenario_id: str
        ├── session_id: str
        ├── status: "COMPLETED" | "FAILED"
        ├── error: Optional[str]
        └── evaluator_results: List[EvaluatorResult]
              ├── evaluator_id: str
              └── results: List[Dict]   # Raw API responses
```

Each entry in `results` is a raw response dict from the Evaluate API, containing fields
like `value`, `label`, `explanation`, `context`, `tokenUsage`, and
`ignoredReferenceInputFields`. See
[Getting started with on-demand evaluation](getting-started-on-demand.md "getting-started-on-demand.md")
for the full response format.

A scenario with status `FAILED` means a structural problem occurred (agent invocation
error, span collection failure). Individual evaluator errors within a `COMPLETED` scenario
are recorded in the evaluator's `results` list with `errorCode` and `errorMessage` fields.
