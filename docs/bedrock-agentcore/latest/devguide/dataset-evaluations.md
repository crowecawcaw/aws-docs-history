# Dataset evaluation

###### Note

Dataset evaluation is in public preview. Features and APIs may change before general availability.

Dataset evaluations let you run your agent against a set of scenarios and automatically evaluate the results. Instead of manually invoking your agent, collecting spans, and calling the Evaluate API, a dataset runner orchestrates the entire lifecycle in a single call: invoke the agent, wait for telemetry ingestion, and evaluate.

This is useful for regression testing, benchmark datasets, CI/CD pipelines, baseline measurement, and pre/post comparison after configuration changes.

The AgentCore SDK provides two dataset runners that share the same [dataset schema](dataset-evaluations-schema.md "dataset-evaluations-schema.md") and ground truth format but differ in where evaluation happens:

- **On-demand dataset runner** (`OnDemandEvaluationDatasetRunner`) — Collects spans and calls the Evaluate API client-side. Best for dev-time iteration and small datasets.
- **Batch dataset runner** (`BatchEvaluationRunner`) — Delegates span collection and evaluation to the service via the batch evaluation API. Best for large datasets and production baselines.

**Choosing a runner**

| Aspect             | On-demand runner                                                                         | Batch runner                                                                                          |
| ------------------ | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Span collection    | SDK-side via `AgentSpanCollector`                                                        | Server-side; service reads from CloudWatch directly                                                   |
| Evaluate API calls | SDK calls `evaluate()` per evaluator per scenario                                        | SDK calls `startBatchEvaluation()` once                                                               |
| Execution model    | Synchronous three-phase pipeline (invoke, wait, evaluate)                                | Asynchronous four-phase pipeline (invoke, wait, submit, poll)                                         |
| Results            | Structured `EvaluationResult` with per-scenario, per-evaluator detail                    | Aggregate `BatchEvaluationSummary` with per-evaluator averages, plus per-session detail in CloudWatch |
| Best for           | Dev-time iteration, CI/CD, small datasets, when you need per-scenario detail immediately | Baseline measurement, large datasets, pre/post comparison, when aggregate scores are sufficient       |

**Prerequisites**

Both runners require:

- Python 3.10+
- An agent built with a supported framework and instrumentation library. For more information about supported frameworks and instrumentation libraries, see [Supported agent frameworks](supported-frameworks.md "supported-frameworks.md").
- An agent deployed on AgentCore Runtime with observability enabled, or an agent built with a supported framework configured with [AgentCore Observability](observability.md "observability.md"), including Transaction Search. For more information about telemetry setup, see [Telemetry setup and delivery](supported-frameworks-telemetry.md "supported-frameworks-telemetry.md").
- The AgentCore SDK installed: `pip install bedrock-agentcore`
- AWS credentials configured with permissions for `bedrock-agentcore`, `bedrock-agentcore-control`, and `logs` (CloudWatch)

###### Topics

- [Prerequisites](datasets-prereqs.md "datasets-prereqs.md")
- [Getting started](datasets-getting-started.md "datasets-getting-started.md")
- [Dataset schema](dataset-evaluations-schema.md "dataset-evaluations-schema.md")
- [Manage datasets](datasets-manage.md "datasets-manage.md")
- [Manage dataset examples](datasets-examples.md "datasets-examples.md")
- [Manage dataset versions](datasets-versions.md "datasets-versions.md")
- [Dataset encryption](datasets-encryption.md "datasets-encryption.md")
- [On-demand dataset runner](dataset-evaluations-on-demand.md "dataset-evaluations-on-demand.md")
- [Batch dataset runner](dataset-evaluations-batch.md "dataset-evaluations-batch.md")
