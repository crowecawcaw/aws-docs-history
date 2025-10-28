Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Example: Invoke a Lambda

function

The following example workflow includes the **AWS Lambda invoke** action, along
with a deploy action. The workflow sends out a Slack notification indicating that a deployment
has started, and then deploys an application into AWS using an AWS CloudFormation template. The workflow
consists of the following building blocks that run sequentially:

- A **trigger** – This trigger starts the workflow run
  automatically when you push a change to your source repository. For more information about
  triggers, see [Starting a workflow run automatically using
  triggers](workflows-add-trigger.md "workflows-add-trigger.md").
- An **AWS Lambda invoke** action (`LambdaNotify`) – On
  trigger, this action invokes the `Notify-Start` Lambda function in the specified
  AWS account and Region (`my-aws-account`, and `us-west-2`). On
  invocation, the Lambda function sends a Slack notification indicating a deployment has
  started.
- A **Deploy AWS CloudFormation stack** action (`Deploy`) – On
  completion of the **AWS Lambda invoke** action, the **Deploy AWS CloudFormation
  stack** action runs the template (`cfn-template.yml`) to deploy your
  application stack. For more information about the **Deploy AWS CloudFormation stack**
  action, see [Deploying an AWS CloudFormation stack](deploy-action-cfn.md "deploy-action-cfn.md").

###### Note

The following workflow example is for illustrative purposes, and will not work without
additional configuration.

###### Note

In the YAML code that follows, you can omit the `Connections:` sections if
you want. If you omit these sections, you must ensure that the role specified in the
**Default IAM role** field in your environment includes the permissions
and trust policies required by the **AWS Lambda invoke** and
**Deploy AWS CloudFormation stack** actions. For more information about setting up an
environment with a default IAM role, see [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md"). For more information about the
permissions and trust policies required by the **AWS Lambda invoke** and
**Deploy AWS CloudFormation stack** actions, see the description of the
`Role` property in the ['AWS Lambda invoke' action YAML](lam-invoke-action-ref.md "lam-invoke-action-ref.md") and ['Deploy AWS CloudFormation stack' action YAML](deploy-action-ref-cfn.md "deploy-action-ref-cfn.md").

```
Name: codecatalyst-lamda-invoke-workflow
SchemaVersion: 1.0

Triggers:
  - Type: PUSH
    Branches:
      - main
Actions:
  LambdaNotify:
    Identifier: aws/lambda-invoke@v1
    Environment:
      Name: my-production-environment
      Connections:
        - Name: my-aws-account
          Role: codecatalyst-lambda-invoke-role
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      Function: Notify-Start
      AWSRegion: us-west-2

  Deploy:
    Identifier: aws/cfn-deploy@v1
    Environment:
      Name: my-production-environment
      Connections:
        - Name: my-aws-account
          Role: codecatalyst-deploy-role
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      name: my-application-stack
      region: us-west-2
      role-arn: arn:aws:iam::111122223333:role/StackRole
      template: ./cfn-template.yml
      capabilities: CAPABILITY_IAM,CAPABILITY_AUTO_EXPAND
```
