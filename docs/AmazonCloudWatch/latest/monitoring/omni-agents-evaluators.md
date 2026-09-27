

# Evaluators and evaluations
<a name="omni-agents-evaluators"></a>

An evaluator scores agent behavior against a criterion (for example, whether the response was correct, relevant, or grounded in the retrieved context). An evaluation is the result of running one or more evaluators over a trace, or over the outputs your agent produces from a dataset's test cases. Because evaluators are automated, you can score hundreds of runs the way you would review one by hand. This page covers scoring on demand. To score production traffic continuously, see [Online evaluations](omni-agents-online-evaluations.md).

**What an evaluator reads**

An evaluator reads the full trace — the user's input, the agent's response, and depending on the evaluator, the steps in between: which tools the agent called and in what order, and what context it retrieved (for the trace and session vocabulary, see [Monitor AI agents](omni-monitor-ai-agents.md)). Each evaluator scores at one of three levels: a **trace** (one request and response), a **session** (a whole conversation), or a **tool call** (one tool invocation). Traces must therefore show input and output. If your evaluators return blank results, check the content-extraction settings in [Send AI agent telemetry](omni-send-ai-agent-telemetry.md).

**Where evaluators come from**

Every evaluator runs through Amazon Bedrock AgentCore Evaluations, and the catalog covers three kinds. For the full evaluator reference, see [Evaluate agent performance](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) in the *Amazon Bedrock AgentCore Developer Guide*.
+ **Built-in** — ready-made checks for common criteria such as correctness, helpfulness, and tool-use quality. Start here: they cover the criteria most agents need, without setup. Some built-in evaluators use a judge model internally; others are rule-based checks.
+ **Third-party** — metrics from the DeepEval and AutoEval open-source evaluation libraries. If you already use these libraries, you can run the same metrics here without hosting them: the service runs the evaluator, selects the judge model, and manages the library version, the same way it does for a built-in evaluator. To run one of these metrics on a judge model you choose, create a derived custom evaluator instead. DeepEval covers task completion, tool use, and summarization; multi-turn behavior such as knowledge retention, turn relevancy, and goal accuracy; and safety checks for bias, toxicity, and PII leakage. AutoEval covers whether a response is malicious, whether it is humorous, and whether the agent attempted the task or declared it impossible. AWS tests and benchmarks the built-in evaluators but makes no quality claims about these libraries, so validate a metric against your own traces before you rely on its scores. For the metric-by-metric list, see [Third-party evaluators](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/third-party-evaluators.html) in the *Amazon Bedrock AgentCore Developer Guide*.
+ **Custom** — evaluators you create, in three forms. A **model-as-judge** evaluator scores trace content against criteria you write in natural language, with your choice of judge model. Use it for criteria that need judgment ("is the tone appropriate for a support agent?") that no fixed rule can check, and spot-check its scores against your own judgment before trusting it at scale. A **derived** evaluator runs an existing built-in or third-party evaluator's logic on the judge model you choose, so you skip writing instructions and a rating scale. A **code-based** evaluator is your own AWS Lambda function that receives the trace content and returns a score. Use it for deterministic, domain-specific checks (the response parses as valid JSON, cites a real order ID, stays under a length limit) where a rule is cheaper and more reliable than a model.

**Important**  
**Judge-based evaluators send trace content to the judge model.** Both the evaluator prompt and the trace content it scores go to the model for inference. This applies to judge-based built-in and third-party evaluators as well as custom model-as-judge evaluators. If your traces can contain sensitive data, see [Protect sensitive data](omni-data-protection.md).

**Permissions for custom evaluators**

Built-in and third-party evaluators run on service-managed capacity — there is nothing to grant. A custom evaluator invokes its judge using your space's permissions, so the Space Access role must be allowed to invoke it, and the permission depends on the judge:
+ Amazon Bedrock foundation model or inference profile — `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` on that model or inference profile.
+ A model served through the `bedrock-mantle` endpoint in Amazon Bedrock — `bedrock-mantle:CreateInference` on the project and `bedrock-mantle:CallWithBearerToken`.
+ Lambda (code) evaluator — `lambda:InvokeFunction` and `lambda:GetFunction` on your evaluator function.

Without the matching permission, on-demand scoring with that custom evaluator fails; built-in and third-party evaluators are unaffected. For the managed policies that carry these actions and the conditions on them, see [IAM policies to use CloudWatch Omni](omni-iam-policies-to-use-cloudwatch-omni.md). For online evaluations, grant them to the evaluation's execution role instead — see [Online evaluations](omni-agents-online-evaluations.md).

**Built-in evaluators miss domain-specific failures**

Built-in evaluators score general criteria, and an agent can pass all of them while doing the wrong thing for your domain. Consider a customer support agent that answers an off-topic question, such as providing a recipe: a helpfulness evaluator scores it high (it answered well), and a policy-compliance evaluator scores it high (nothing harmful). Every score is high, yet the agent has left its designated scope. No general-purpose criterion knows what your agent's scope is.

Use built-in evaluators for universal criteria, and write a custom evaluator for every rule that is specific to your agent: permitted topics, required behaviors, forbidden actions. If you can state the rule in a sentence, you can usually write it as a model-as-judge evaluator; if it is mechanically checkable, write it as a code-based evaluator.

**Write a custom model-as-judge evaluator**

A model-as-judge evaluator is a prompt to the judge model plus a rating scale. The judge reads the conversation and the response, applies your rubric, and returns one of the scale's values. A well-specified evaluator has three parts:

1. **State what the agent is, and what is in scope.** Enumerate the permitted topics or behaviors explicitly. The judge cannot infer your product's boundaries. For example: "The agent is an e-commerce customer support agent. Its only permitted topics are returns and refunds, product inquiries, and account management."

1. **Write the rubric as decidable cases.** Define each score with the specific conditions that earn it, including the edge cases. For a scope evaluator: "a response that acknowledges the request is off-topic but still answers it is off-topic." Vague rubrics ("score how appropriate the response is") produce inconsistent judgments.

1. **Match the rating scale to the criterion.** A rule the agent either follows or breaks should be binary: two values, pass and fail, each with a one-line definition. Remove middle values; a 0.5 on "did the agent stay in scope?" has no meaning, and evaluators default to it when the rubric leaves room for doubt. Reserve graded scales for criteria that are genuinely graded, such as completeness.

The evaluator's instructions include placeholders that are filled with trace content for each run it scores. For a trace-level evaluator, these are `{context}` (the conversation so far) and `{assistant_turn}` (the response under evaluation). Each evaluation level has its own placeholder set; for the full list, see [Create evaluator](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/create-evaluator.html) in the *Amazon Bedrock AgentCore Developer Guide*. The rating scale can be numerical (each value has a number, a label, and a definition) or categorical (the label is the value). Test the evaluator on a known-bad and a known-good trace before relying on it: the known-bad trace should score fail, and the known-good one should score pass. If either misses, tighten the rubric.

**To evaluate a response**

1. Open a trace in [Agent traces](omni-agent-traces.md) to score a single run, select sessions in [Agent sessions](omni-agent-sessions.md) to score whole conversations, or run your agent against a dataset's test cases, for example in an experiment, and score the outputs. See [Experiments](omni-agents-experiments.md).

1. Choose the evaluators that match what you want to check: one criterion per evaluator, and typically several evaluators per run.

1. Run them, and review the scores. Each score links back to the trace it came from, so you can open a low-scoring run and see exactly what the agent did.

**Interpret scores as comparisons**

A single absolute score rarely means much on its own. A 0.8 correctness score is only good or bad relative to something. Scores become useful when you compare: the same dataset before and after a change (see [Experiments](omni-agents-experiments.md)), the same evaluator across agents, or a trend over time.

**Review evaluation results over time**

The **Evaluation dashboard** aggregates your evaluation results: score trends, score distributions, pass rates, and a comparison across evaluators. Use it to watch for drift after individual runs are scored: a pass rate that declines over days signals a regression even when every individual score looks reasonable in isolation. From a declining trend, open the low-scoring traces to see what changed. If the drop follows a deployment or a prompt change, check that change first. To respond to a regression you find here, see [Tutorial: Fix a production quality regression](omni-agents-close-the-loop.md).

![The evaluation dashboard showing a pass-rate trend declining over several days and a score distribution across evaluators.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-evaluation-dashboard.png)
