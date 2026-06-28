# Monitor `bedrock-mantle` inference using CloudWatch metrics

The Amazon Bedrock OpenAI-compatible endpoint
(`bedrock-mantle.`region`.api.aws`) publishes customer-facing
metrics to Amazon CloudWatch under the `AWS/BedrockMantle` namespace. Use these metrics to
monitor inference volume, token consumption, and error rates across your AWS account, projects,
and models.

If your application calls inference through
`bedrock-runtime.`region`.amazonaws.com` using [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md"),
[ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md"), [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md"), or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md"), see [Amazon Bedrock runtime metrics](monitoring-runtime-metrics.md#runtime-cloudwatch-metrics "monitoring-runtime-metrics.md#runtime-cloudwatch-metrics") instead.
`bedrock-mantle` metrics cover only inference issued through the Responses API, Chat
Completions API, and Anthropic Messages API on the `bedrock-mantle` endpoint.

`bedrock-mantle` publishes metrics at four levels of granularity. Each level uses a
different combination of CloudWatch dimensions, described in [Dimensions](#mantle-metrics-dimensions "#mantle-metrics-dimensions").
All metrics are scoped to your AWS account.

## Inference metrics

Inference metrics| Metric name | Unit | Description |
| --- | --- | --- |
| `Inferences` | Count | Total number of completed inference requests across the Responses, Chat Completions, and<br>Messages APIs. Published at Account, Project, Model, and Project+Model levels. |
| `InferenceClientErrors` | Count | Number of inference requests that failed with a client-side (4xx) error. Published at<br>Account, Project, Model, and Project+Model levels. |

## Token metrics

Token metrics| Metric name | Unit | Description |
| --- | --- | --- |
| `TotalInputTokens` | Count | Aggregate billable input tokens processed within the publish interval. Published at<br>Account, Project, and Model levels. Use for sums and rate calculations. |
| `TotalOutputTokens` | Count | Aggregate billable output tokens generated within the publish interval. Published at<br>Account, Project, and Model levels. |
| `InputTokens` | Count | Per-inference billable input tokens. Each completed inference emits one datum. Published<br>at the Project+Model level only. Use this when you need percentile statistics (p50/p90/p99)<br>of per-request token counts. |
| `OutputTokens` | Count | Per-inference billable output tokens. Each completed inference emits one datum.<br>Published at the Project+Model level only. |

## Dimensions

Dimensions| Dimension name | Values | Applies to |
| --- | --- | --- |
| `Project` | The project ID associated with the inference request. | Project, Project+Model |
| `Model` | The model identifier (for example, `anthropic.claude-opus-4-7`). | Model, Project+Model |

Account-level metrics are scoped to your AWS account and have no additional dimensions.
Each level of granularity emits independently, so a single inference contributes to all four
levels when both the project and the model can be resolved.

## Choosing the right granularity level

- **Account level** – overall usage, error rate, and
  aggregate token volume. Suitable for high-level dashboards and account-wide alarms. Not
  suitable for cost analysis, because pricing varies by model.
- **Project level** – per-project rollups for chargeback
  and team-level dashboards.
- **Model level** – per-model usage and error rates,
  suitable for migrating dashboards built against the existing `bedrock-runtime`
  `ModelId` dimension.
- **Project+Model level** – primary level for cost
  analysis, and percentile latency and token analysis. Use this when you need both project
  attribution and model attribution on the same datum.

## Differences from `bedrock-runtime` metrics

- **Separate namespace.** `bedrock-mantle` metrics
  publish to `AWS/BedrockMantle`. Existing dashboards and alarms built against
  `AWS/Bedrock` will not pick up `bedrock-mantle` traffic.
- **Naming.** `bedrock-mantle` uses
  `Inferences` rather than `Invocations`, `TotalInputTokens` and
  `TotalOutputTokens` rather than `InputTokenCount` and
  `OutputTokenCount`, and `InferenceClientErrors` rather than
  `InvocationClientErrors`.
- **Project dimension.** `bedrock-mantle` metrics
  carry a `Project` dimension that `bedrock-runtime` metrics do not,
  enabling per-project cost attribution.
- **Cross-region inference.** `bedrock-mantle` is
  in-region only. Metrics are emitted in the Region that handled the request and are not
  aggregated across Regions the way cross-Region inference (CRIS) traffic is on
  `bedrock-runtime`.
- **Latency metrics.** `InvocationLatency` and
  `TimeToFirstToken` equivalents are not yet published by
  `bedrock-mantle`.

## Viewing `bedrock-mantle` metrics

To view `bedrock-mantle` metrics in the CloudWatch console:

1. Open the CloudWatch console.
2. In the navigation pane, choose **Metrics**, **All
   metrics**.
3. Choose the `AWS/BedrockMantle` namespace.
4. Select a granularity level by choosing the dimension set that matches your query (for
   example, `Project, Model` for project-and-model breakdowns).

You must have appropriate CloudWatch permissions to read `bedrock-mantle` metrics. For
more information, see [Authentication
and access control for Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md") in the _Amazon CloudWatch User Guide_.
