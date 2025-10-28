# Lambda-backed custom resources

When you associate a Lambda function with a custom resource, the function is invoked
whenever the custom resource is created, updated, or deleted.

CloudFormation calls a Lambda API to invoke the function and to pass all the request data (such
as the request type and resource properties) to the function. The power and customizability
of Lambda functions in combination with CloudFormation enable a wide range of scenarios, such as
dynamically looking up AMI IDs during stack creation, or implementing and using utility
functions, such as string reversal functions.

For an introduction to custom resources and how they work, see [Create custom provisioning logic with custom
resources](template-custom-resources.md "template-custom-resources.md").

###### Topics

- [Walkthrough: Create a delay
  mechanism with a Lambda-backed custom resource](walkthrough-lambda-backed-custom-resources.md "walkthrough-lambda-backed-custom-resources.md")
- [cfn-response
  module](cfn-lambda-function-code-cfnresponsemodule.md "cfn-lambda-function-code-cfnresponsemodule.md")
