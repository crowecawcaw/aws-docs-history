# Use action types, custom actions, and approval actions

In AWS CodePipeline, an action is part of the sequence in a stage of a pipeline. It is a task performed
on the artifact in that stage. Pipeline actions occur in a specified order, in sequence or in
parallel, as determined in the configuration of the stage.

CodePipeline provides support for six types of actions:

- Source
- Build
- Test
- Deploy
- Approval
- Invoke
  For information about the AWS service and partner products and services you can integrate
  into your pipeline based on action type, see [Integrations with CodePipeline action types](integrations-action-type.md "integrations-action-type.md").

###### Topics

- [Working with action types](action-types.md "action-types.md")
- [Create a custom action for a pipeline](actions-create-custom-action.md "actions-create-custom-action.md")
- [Tag a custom action in CodePipeline](customactions-tag.md "customactions-tag.md")
- [Invoke a Lambda function in a pipeline](actions-invoke-lambda-function.md "actions-invoke-lambda-function.md")
- [Add a manual approval action to a stage](approvals.md "approvals.md")
- [Add a cross-Region action to a pipeline](actions-create-cross-region.md "actions-create-cross-region.md")
- [Working with variables](actions-variables.md "actions-variables.md")
