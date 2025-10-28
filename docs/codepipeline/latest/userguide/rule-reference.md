# Rule structure reference

This section is a reference for rule configuration only. For a conceptual overview of the
pipeline structure, see [CodePipeline pipeline structure reference](reference-pipeline-structure.md "reference-pipeline-structure.md").

Each rule provider in CodePipeline uses a set of required and optional configuration fields in the
pipeline structure. This section provides the following reference information by rule
provider:

- Valid values for the `RuleType` fields included in the pipeline structure
  rule block, such as `Owner` and `Provider`.
- Descriptions and other reference information for the `Configuration`
  parameters (required and optional) included in the pipeline structure rule section.
- Valid example JSON and YAML rule configuration fields.
  Reference information is available for the following rule providers:

###### Topics

- [CloudWatchAlarm](rule-reference-CloudWatchAlarm.md "rule-reference-CloudWatchAlarm.md")
- [CodeBuild rule](rule-reference-CodeBuild.md "rule-reference-CodeBuild.md")
- [Commands](rule-reference-Commands.md "rule-reference-Commands.md")
- [DeploymentWindow](rule-reference-DeploymentWindow.md "rule-reference-DeploymentWindow.md")
- [LambdaInvoke](rule-reference-LambdaInvoke.md "rule-reference-LambdaInvoke.md")
- [VariableCheck](rule-reference-VariableCheck.md "rule-reference-VariableCheck.md")
