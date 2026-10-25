

# A/B testing
<a name="ab-testing"></a>

A/B testing splits live production traffic between two variants and continuously evaluates performance with statistical significance. The AgentCore Gateway handles traffic routing; your agent code does not change.

A/B testing is the validation step in the [AgentCore optimization improvement loop](optimization-how-it-works.md). After generating a [recommendation](optimization-recommendations.md) and validating it with [offline batch evaluations](dataset-evaluations.md), you run an A/B test to confirm the change improves performance on live traffic before committing to a full rollout. You can route traffic to separate AgentCore Runtimes (target-based) or deliver different configurations to the same AgentCore Runtime (configuration bundles).

## When to use A/B testing
<a name="ab-testing-when-to-use"></a>

Use A/B testing when you need to:
+  **Validate a recommendation** before routing all production traffic to the optimized configuration.
+  **Compare two model versions** (for example, moving from one foundation model to another) on live traffic with statistical rigor.
+  **Measure the impact of a prompt change** across real user sessions rather than a curated test set.
+  **Gradually roll out a new capability** (new tools, updated system prompt) by validating it on a subset of live traffic before full deployment.

## How it works
<a name="ab-testing-how-it-works"></a>

An A/B test follows this flow:

1.  **You initiate an A/B test** with `agentcore eval ab-test config-based run` or `agentcore eval ab-test target-based run`, specifying an already-deployed AgentCore Gateway, two variants (control and treatment), traffic weights, and one or more online evaluation configurations for scoring. The execution role is optional. Each variant references either an AgentCore Gateway target or a configuration bundle version. The test starts by default. To create it paused, pass `--enable-on-create false`.

1.  **The AgentCore Gateway splits traffic.** Once the test is running, the gateway splits incoming traffic between the two variants based on the runtime session ID. Assignment is sticky; a given session ID always routes to the same variant.

1.  **Online evaluation scores each session.** The online evaluation configuration you specified runs evaluators against each session as it completes. The A/B test aggregation pipeline maps scores to variants.

1.  **The service computes statistical significance.** As sample sizes grow, the service calculates per-evaluator metrics for each variant: mean score, absolute and percent change, p-value, confidence interval, and a significance flag. A p-value below 0.05 indicates the difference is statistically significant. Poll results with `agentcore eval ab-test get --id <id>` at any time without affecting statistical validity.

1.  **You route traffic to the winning variant.** Stop the test with `agentcore eval ab-test stop --id <id>`. If the treatment won, create or update a Gateway rule that routes traffic to the treatment target or applies the treatment configuration bundle version. Use the AWS CLI (`aws bedrock-agentcore-control create-gateway-rule` or `update-gateway-rule`) for this step. The rule is not part of the project, and `agentcore deploy` does not manage it.

## A/B test patterns
<a name="ab-testing-patterns"></a>

A/B tests support two variant configuration patterns:

Use when the change includes code changes, a framework upgrade, or when you want to compare entirely different agent implementations. Each variant routes to a different AgentCore Gateway target pointing to a different runtime endpoint.

Use when the change is purely configuration (system prompt, model ID, or tool descriptions). Both variants run on the same AgentCore Runtime with different configuration bundle versions. Your runtime receives the assigned bundle reference through W3C baggage headers, a standard mechanism for passing context between services, and uses the AgentCore SDK to retrieve the configuration.


| Aspect | Target-based variants | Configuration bundle variants | 
| --- | --- | --- | 
| What varies | Entire runtime endpoint (code, framework, model) | System prompt, tool descriptions, model parameters | 
| Routing | Different targets per variant | Same target, different config bundles | 
| Evaluation config | One online eval config per variant endpoint or data source | Single shared online eval config | 
| When to use | Code changes, framework upgrades, comparing different agents | Configuration-only changes on a single AgentCore Runtime | 

**Topics**