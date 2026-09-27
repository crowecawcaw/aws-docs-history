

# Online evaluations
<a name="omni-agents-online-evaluations"></a>

On-demand evaluation scores a trace when you ask. An **online evaluation** scores your traffic continuously: you choose the agents to watch, the evaluators to run, and how much traffic to sample, and CloudWatch Omni evaluates matching traces as they arrive. Quality regressions surface in your evaluation trends without anyone running a check. Online evaluation is the continuous-monitoring stage of the evaluation workflow described in [Evaluate agent quality](omni-agents-evaluate.md).

**How an online evaluation works**

An online evaluation is a configuration that you create, and then enable:
+ **Agents to evaluate** — chosen by service name from the agents seen in your space's telemetry.
+ **Evaluators to run** — one or more evaluators from the catalog described below.
+ **Sampling percentage** — how much of the matching traffic is evaluated. Sampling is your cost control: judge-based evaluators invoke a judge model for every sampled trace, so evaluate a fraction of high-volume traffic.
+ **Session settings (optional)** — a session timeout that determines when a conversation is considered complete, so session-level evaluators can score the full exchange. The timeout is measured from a session's last activity: a session is evaluated only after it has been idle for this long. A session that never goes idle — for example a long-running or continuously reused session that always has recent activity — is never treated as complete, so it is never evaluated and produces no results. Set the timeout shorter than the typical gap between turns in your sessions so they finalize and are scored.

While the configuration is enabled, CloudWatch Omni evaluates sampled traces continuously. Scores appear alongside the traces and feed the trends in the Evaluation dashboard. Each configuration also gets a dedicated CloudWatch log group holding its results in JSON, and publishes each score as a CloudWatch metric, so you can query results with CloudWatch Logs Insights and alarm on a score the same way you alarm on any other metric. Results follow the OpenTelemetry semantic conventions for generative AI evaluation events, and each result references the trace and session it came from, so you can go from a score back to the run that produced it.

To change an enabled configuration's evaluators, disable it first. The evaluator list is locked while the evaluation runs. A running evaluation also locks the custom evaluators it uses, so that scores stay comparable over time: you cannot edit or delete one while an evaluation is using it. To change a custom evaluator's criteria, clone it, edit the copy, and point the configuration at the copy. The original keeps the scoring history it already produced.

**Where evaluators come from**

An online evaluation runs the same catalog as on-demand evaluation (built-in, third-party, and custom evaluators, all through Amazon Bedrock AgentCore Evaluations), and you can mix kinds in one configuration. For what each kind covers and how to write your own, see [Evaluators and evaluations](omni-agents-evaluators.md).

The judge model depends on the evaluator kind, and that determines what you pay for. For built-in and third-party evaluators, the service selects and runs the judge model on its own capacity. There is nothing to configure. For custom evaluators, including one derived from a built-in or third-party evaluator, the judge model is the one you chose, and it is invoked with the permissions you grant the evaluation, so those model invocations run in your account. For the online-evaluation reference, see [Evaluate agent performance](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html), [Online evaluation configurations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/online-evaluations.html), [Prerequisites](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-prerequisites.html), and [Results and output](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/results-and-output.html) in the *Amazon Bedrock AgentCore Developer Guide*.

**Permissions for custom evaluators**

Built-in and third-party evaluators run on service-managed capacity — you grant nothing extra. A custom evaluator invokes the judge you chose, using the online evaluation's execution role, so that role must be allowed to invoke it. The permission depends on the judge:
+ Amazon Bedrock foundation model or inference profile — `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` on that model's or inference profile's ARN.
+ A model served through the `bedrock-mantle` endpoint in Amazon Bedrock — `bedrock-mantle:CreateInference` on the project and `bedrock-mantle:CallWithBearerToken`.
+ Lambda (code) evaluator — `lambda:InvokeFunction` and `lambda:GetFunction` on your evaluator function.

The default execution role created for you covers built-in and third-party evaluators. When you add a custom evaluator, add the matching permission above to the execution role before you enable the evaluation; otherwise enabling fails with a permissions error (for example, "the execution role does not have permissions to invoke the specified Bedrock models"). For the managed policies that carry these actions and the conditions on them, see [IAM policies to use CloudWatch Omni](omni-iam-policies-to-use-cloudwatch-omni.md). For the execution-role policy reference, see [Prerequisites](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-prerequisites.html).

**To create an online evaluation**

1. In your space, under `Evaluate`, choose `Online evaluations`, and then choose `New evaluation`.

1. Select the agents to evaluate, the evaluators to run, and the sampling percentage.

1. Grant the permissions the evaluation needs. Every online evaluation needs permission to write its results (CloudWatch Logs and metrics). If you include a custom evaluator, the evaluation's execution role must also be allowed to invoke that evaluator's judge — the exact permission depends on the judge's type (see **Permissions for custom evaluators**). Built-in and third-party evaluators need no additional permissions.

1. Enable the evaluation, and confirm its status shows as enabled. Scores from sampled traffic appear in the Evaluation dashboard as they accumulate.

**Cost and data considerations**
+ Judge-based evaluators invoke a model for every sampled trace. Tune the sampling percentage to match your traffic volume and budget.
+ Evaluators that use a judge model send the sampled trace content to that model. If your traces can contain sensitive data, see [Protect sensitive data](omni-data-protection.md).

For scoring a specific trace or dataset on demand, see [Evaluators and evaluations](omni-agents-evaluators.md). When an online evaluation surfaces a regression, follow [Tutorial: Fix a production quality regression](omni-agents-close-the-loop.md) to fix and verify it.