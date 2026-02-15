# Evaluate agent performance with Amazon Bedrock AgentCore Evaluations

###### Preview

This feature is in preview and is not available in all regions.

Amazon Bedrock AgentCore Evaluations provides automated assessment tools to measure how well your
agent or tools perform specific tasks, handle edge cases, and maintain consistency across
different inputs and contexts. The service enables data-driven optimization and ensures your
agents meet quality standards before and after deployment.

AgentCore Evaluations integrates with popular agent frameworks including **Strands** and **LangGraph** with **OpenTelemetry** and **OpenInference** instrumentation
libraries. Under the hood, traces from these agents are converted to a unified format and scored
using LLM-as-a-Judge techniques for both built-in and custom evaluators.

Each evaluator has a unique Amazon Resource Name (ARN) and resource policy attached to it. Evaluator ARNs follow
these formats:

```
arn:aws:bedrock-agentcore:::evaluator/Builtin.Helpfulness (for built-in evaluators)
```

```
arn:aws:bedrock-agentcore:region:account:evaluator/my-evaluator-id (for custom evaluators)
```

Built-in evaluators are public and accessible to all users. Custom evaluation resources are
private and can only be accessed by users who are explicitly granted access. To grant access, you
can use IAM resource-based policies for evaluators and evaluation configurations, and IAM
identity-based policies for users and roles.

By default, you can create up to 1,000 evaluation configurations per AWS Region in an AWS
account, with up to 100 active at any point in time. The service supports up to 1 million input
and output tokens per minute per account for large regions.

###### Topics

- [How it works](how-it-works-evaluations.md "how-it-works-evaluations.md")
- [Built-in evaluators](built-in-evaluators-overview.md "built-in-evaluators-overview.md")
- [Custom evaluators](custom-evaluators.md "custom-evaluators.md")
- [Online evaluation](online-evaluations.md "online-evaluations.md")
- [On-demand evaluation](on-demand-evaluations.md "on-demand-evaluations.md")
