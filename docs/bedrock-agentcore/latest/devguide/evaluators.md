# Evaluators

Evaluators are the core components that assess your agent's performance across
different dimensions. They analyze agent traces and provide quantitative scores based on
specific criteria such as helpfulness, accuracy, or custom business metrics.
AgentCore Evaluations offers both built-in evaluators for common use cases and the flexibility
to create custom evaluators tailored to your specific requirements.

###### Topics

- [Built-in evaluators](#built-in-evaluators "#built-in-evaluators")
- [Custom evaluators](#custom-evaluators-hiw "#custom-evaluators-hiw")

## Built-in evaluators

Built-in evaluators are pre-configured solutions that use Large Language Models
(LLMs) as judges to evaluate agent performance. These evaluators come with
predefined configurations, including carefully crafted prompt templates, selected
evaluator models, and standardized scoring criteria.

Built-in evaluators are designed to address common evaluation needs while ensuring
consistency and reliability across assessments. Because they are part of our fully
managed offering, you can use them immediately without any additional configuration,
and we will continue improving their quality and adding new evaluators over time. To
preserve consistency and reliability, the configurations of built-in evaluators
cannot be modified.

## Custom evaluators

Custom evaluators offer more flexibility by allowing you to define all aspects of
your evaluation process, while still using LLMs as the underlying judges. You can
tailor the evaluation to your specific needs by selecting the evaluator model,
crafting custom evaluation instructions, defining specific evaluation criteria, and
designing your own scoring schema. This level of customization is particularly
valuable when you need to evaluate domain-specific agents, apply unique quality
standards, or implement specialized scoring systems.

For example, you might create custom evaluation criteria for specific industries
like healthcare or finance, or design scoring schemas that align with your
organization's quality metrics. Custom evaluators give you complete control over how
your agents are evaluated while leveraging LLMs to make objective judgments.
