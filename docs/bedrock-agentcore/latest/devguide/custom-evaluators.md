# Custom evaluators

Custom evaluators in AgentCore Evaluations allow you to define your own evaluator model, evaluation instruction and scoring schemas. You can create custom evaluators that are tailored to your specific use cases and evaluation requirements.

You can use custom evaluators with both online and on-demand evaluations. To specify a custom evaluator, use its Amazon Resource Name (ARN) in the following format:

```
arn:aws:bedrock-agentcore:region:account:evaluator/evaluator-id
```

You can also create a custom evaluator that runs an existing built-in or third-party evaluator’s logic on your own model. With this approach, you skip writing your own instructions and rating scale. For more information, see [Third-party evaluators](third-party-evaluators.md "third-party-evaluators.md").

###### Topics

- [Create evaluator](create-evaluator.md "create-evaluator.md")
- [List evaluators](list-evaluators.md "list-evaluators.md")
- [Update evaluator](update-evaluator.md "update-evaluator.md")
- [Get evaluator](get-evaluator.md "get-evaluator.md")
- [Delete evaluator](delete-evaluator.md "delete-evaluator.md")
- [Custom code-based evaluator](code-based-evaluators.md "code-based-evaluators.md")
