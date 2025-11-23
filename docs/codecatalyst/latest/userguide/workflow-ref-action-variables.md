Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# List of predefined variables

Consult the following sections to view the predefined variables produced automatically by
CodeCatalyst actions as part of a workflow run.

For more information about predefined variables, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").

###### Note

This list only includes predefined variables emitted by the CodeCatalyst source and [CodeCatalyst actions](workflows-actions.md#workflows-actions-types "workflows-actions.md#workflows-actions-types"). If you're using other types
of actions, such as GitHub Actions or CodeCatalyst Labs actions, see instead [Determining
which predefined variables your workflow emits](workflows-working-with-variables-determine-output-vars.md "workflows-working-with-variables-determine-output-vars.md").

**List**

###### Note

Not all CodeCatalyst actions produce predefined variables. If the action is not in the list,
then it does not produce variables.

- ['BranchName' and 'CommitId'
  variables](workflows-sources-variables.md "workflows-sources-variables.md")
- ['Deploy CloudFormation stack' variables](deploy-action-cfn-variables.md "deploy-action-cfn-variables.md")
- ['Deploy to Amazon ECS' variables](deploy-action-ecs-variables.md "deploy-action-ecs-variables.md")
- ['Deploy to Kubernetes
  cluster' variables](deploy-action-eks-variables.md "deploy-action-eks-variables.md")
- ['AWS CDK deploy' variables](cdk-dep-action-variables.md "cdk-dep-action-variables.md")
- ['AWS CDK bootstrap' variables](cdk-boot-action-variables.md "cdk-boot-action-variables.md")
- ['AWS Lambda invoke' variables](lam-invoke-action-variables.md "lam-invoke-action-variables.md")
- ['Render Amazon ECS task definition' variables](render-ecs-action-variables.md "render-ecs-action-variables.md")
