

# Evaluate agent quality
<a name="omni-agents-evaluate"></a>

Agents fail in ways that do not show up as errors: the run completes, but the answer is wrong, incomplete, or against your policies. Evaluation is how you measure response quality, so you can catch these failures and tell whether a change to a prompt, a model, or a tool made your agent better or worse.

**How evaluation fits together**

The evaluation workflow builds from your real traffic:

1. **Curate test cases from real traces.** Your traces already contain real requests and the behavior that needs to improve. You collect representative runs (common requests, edge cases, known failures) into a **dataset**, a fixed test set you can run against repeatedly. See [Datasets](omni-agents-datasets.md).

1. **Score responses with evaluators.** An **evaluator** reads a trace (the input, the response, and the steps in between) and returns a score against a criterion such as correctness or relevance. The scores from running one or more evaluators are an **evaluation**, the record you compare against later runs. You can score a single trace as you debug, or score your agent's outputs across a whole dataset. See [Evaluators and evaluations](omni-agents-evaluators.md).

1. **Compare versions with experiments.** An **experiment** runs two or more agent versions against the same dataset with the same evaluators, so a score difference can only come from the change you made. See [Experiments](omni-agents-experiments.md).

The **playground** sits alongside this loop for interactive iteration: try a prompt or an agent change and see the effect immediately, then formalize what worked into a dataset and an experiment. See [Prompt playground](omni-prompt-playground.md).

![The agent evaluation workflow: a development loop of curate, score, and compare, with the playground alongside for interactive iteration, and an online evaluation in production scoring a sample of live traffic whose failing traces feed back into the loop as new test cases.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-agents-evaluation-workflow.png)


**Where evaluators come from**

Every evaluator runs through Amazon Bedrock AgentCore Evaluations, so one catalog covers three kinds:
+ **Built-in** — ready-made checks for common criteria such as correctness, helpfulness, and tool-use quality. Start here.
+ **Third-party** — metrics from the DeepEval and AutoEval open-source libraries, run for you, so you can use familiar metrics without hosting them.
+ **Custom** — evaluators you write yourself, including one that reuses a built-in or third-party evaluator's scoring on a judge model you choose.

Choose an evaluator by the criterion you want to check; you can mix kinds in the same evaluation. For the full catalog and more on how to write your own evaluators, see [Evaluators and evaluations](omni-agents-evaluators.md). To understand how Amazon Bedrock AgentCore evaluates agent performance, see [Evaluate agent performance](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) and [Third-party evaluators](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/third-party-evaluators.html) in the *Amazon Bedrock AgentCore Developer Guide*.

**Evaluation during development and in production**

The same pieces serve two workflows. During development, you run the loop deliberately: build a dataset, score a change in the playground, confirm it with an experiment before you deploy. In production, evaluation runs unattended: an **online evaluation** is a configuration that continuously scores a sample of your live traffic with the evaluators you choose (see [Online evaluations](omni-agents-online-evaluations.md)), and a declining pass rate shows that quality regressed. When production evaluation catches a regression, the development loop is how you fix it. See [Tutorial: Fix a production quality regression](omni-agents-close-the-loop.md) for the end-to-end workflow.

Evaluators read trace content, so your agent must send traces that include input and output. See [Send AI agent telemetry](omni-send-ai-agent-telemetry.md). For the trace, span, and session vocabulary these pages build on, see [Monitor AI agents](omni-monitor-ai-agents.md). To monitor quality signals across your agents in production, see [Monitor agents in the web UI](omni-monitor-agents-in-the-web-ui.md).