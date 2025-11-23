# Amazon ECR source actions and EventBridge resources

To add an Amazon ECR source action in CodePipeline, you can choose either to:

- Use the CodePipeline console **Create pipeline** wizard ([Create a custom pipeline (console)](pipelines-create.md#pipelines-create-console "pipelines-create.md#pipelines-create-console")) or **Edit action** page to choose the **Amazon
  ECR** provider option. The console creates an EventBridge rule that starts
  your pipeline when the source changes.
- Use the CLI to add the action configuration for the `ECR` action
  and create additional resources as follows:
  - Use the `ECR` example action configuration in [Amazon ECR source action reference](action-reference-ECR.md "action-reference-ECR.md") to create your action as shown in [Create a pipeline (CLI)](pipelines-create.md#pipelines-create-cli "pipelines-create.md#pipelines-create-cli").
  - The change detection method defaults to starting the pipeline by
    polling the source. You should disable periodic checks and create the
    change detection rule manually. Use one of the following methods: [Create an EventBridge rule for an Amazon ECR
    source (console)](create-cwe-ecr-source-console.md "create-cwe-ecr-source-console.md"), [Create an EventBridge rule for an Amazon ECR source
    (CLI)](create-cwe-ecr-source-cli.md "create-cwe-ecr-source-cli.md"), or [Create an EventBridge rule for an Amazon ECR source
    (CloudFormation template)](create-cwe-ecr-source-cfn.md "create-cwe-ecr-source-cfn.md") .

###### Topics

- [Create an EventBridge rule for an Amazon ECR
  source (console)](create-cwe-ecr-source-console.md "create-cwe-ecr-source-console.md")
- [Create an EventBridge rule for an Amazon ECR source
  (CLI)](create-cwe-ecr-source-cli.md "create-cwe-ecr-source-cli.md")
- [Create an EventBridge rule for an Amazon ECR source
  (CloudFormation template)](create-cwe-ecr-source-cfn.md "create-cwe-ecr-source-cfn.md")
