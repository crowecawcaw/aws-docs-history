# CodeCommit source actions and EventBridge

To add a CodeCommit source action in CodePipeline, you can choose either to:

- Use the CodePipeline console **Create pipeline** wizard ([Create a custom pipeline (console)](pipelines-create.md#pipelines-create-console "pipelines-create.md#pipelines-create-console")) or **Edit action** page to choose the
  **CodeCommit** provider option. The console creates an EventBridge
  rule that starts your pipeline when the source changes.
- Use the AWS CLI to add the action configuration for the `CodeCommit`
  action and create additional resources as follows:
  - Use the `CodeCommit` example action configuration in [CodeCommit source action reference](action-reference-CodeCommit.md "action-reference-CodeCommit.md") to create your action
    as shown in [Create a pipeline (CLI)](pipelines-create.md#pipelines-create-cli "pipelines-create.md#pipelines-create-cli").
  - The change detection method defaults to starting the pipeline by
    polling the source. You should disable periodic checks and create the
    change detection rule manually. Use one of the following methods: [Create an EventBridge rule
    for a CodeCommit source (console)](pipelines-trigger-source-repo-changes-console.md "pipelines-trigger-source-repo-changes-console.md"),
    [Create an EventBridge rule for
    a CodeCommit source (CLI)](pipelines-trigger-source-repo-changes-cli.md "pipelines-trigger-source-repo-changes-cli.md"), or
    [Create an EventBridge rule for
    a CodeCommit source (CloudFormation template)](pipelines-trigger-source-repo-changes-cfn.md "pipelines-trigger-source-repo-changes-cfn.md") .

###### Topics

- [Create an EventBridge rule
  for a CodeCommit source (console)](pipelines-trigger-source-repo-changes-console.md "pipelines-trigger-source-repo-changes-console.md")
- [Create an EventBridge rule for
  a CodeCommit source (CLI)](pipelines-trigger-source-repo-changes-cli.md "pipelines-trigger-source-repo-changes-cli.md")
- [Create an EventBridge rule for
  a CodeCommit source (CloudFormation template)](pipelines-trigger-source-repo-changes-cfn.md "pipelines-trigger-source-repo-changes-cfn.md")
