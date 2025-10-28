# Define your infrastructure with AWS SAM

Now that you have created your project, you are ready to define your application infrastructure with AWS SAM. Do this by configuring your
AWS SAM template to define your application's resources and properties, which is the `template.yaml` file in your AWS SAM project.

The topics in this section provide content on defining your infrastructure in your AWS SAM template (your `template.yaml` file).
It also contains topics on defining resources for specific use cases, such as working
with Lambda layers, using nested applications, controlling access to API Gateway APIs, orchestrating AWS resources
with Step Functions, code signing your applications, and validating your AWS SAM template.

###### Topics

- [Define application resources in your AWS SAM template](authoring-define-resources.md "authoring-define-resources.md")
- [Set up and manage resource access in your AWS SAM template](sam-permissions.md "sam-permissions.md")
- [Control API access with your AWS SAM template](serverless-controlling-access-to-apis.md "serverless-controlling-access-to-apis.md")
- [Increase efficiency using Lambda layers with AWS SAM](serverless-sam-cli-layers.md "serverless-sam-cli-layers.md")
- [Reuse code and resources using nested applications in AWS SAM](serverless-sam-template-nested-applications.md "serverless-sam-template-nested-applications.md")
- [Manage time-based events with EventBridge
  Scheduler in AWS SAM](using-eventbridge-scheduler.md "using-eventbridge-scheduler.md")
- [Orchestrating AWS SAM resources with
  AWS Step Functions](serverless-step-functions-in-sam.md "serverless-step-functions-in-sam.md")
- [Set up code signing for your AWS SAM application](authoring-codesigning.md "authoring-codesigning.md")
- [Validate AWS SAM template files](serverless-sam-cli-using-validate.md "serverless-sam-cli-using-validate.md")
