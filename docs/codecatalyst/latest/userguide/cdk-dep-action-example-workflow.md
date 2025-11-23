Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Example: Deploying an AWS CDK app

The following example workflow includes the **AWS CDK deploy** action,
along with the **AWS CDK bootstrap** action. The workflow consists of the
following building blocks that run sequentially:

- A **trigger** – This trigger starts the workflow run
  automatically when you push a change to your source repository. This repository contains
  your AWS CDK app. For more information about triggers, see [Starting a workflow run automatically using
  triggers](workflows-add-trigger.md "workflows-add-trigger.md").
- An **AWS CDK bootstrap** action (`CDKBootstrap`)
  – On trigger, the action deploys the `CDKToolkit` bootstrap stack
  into AWS. If the `CDKToolkit` stack already exists in the environment,
  it will be upgraded if necessary; otherwise, nothing happens, and the action is marked as
  succeeded.
- An **AWS CDK deploy** action (`AWS CDKDeploy`) – On
  completion of the **AWS CDK bootstrap** action, the **AWS CDK
  deploy** action synthesizes your AWS CDK app code into an CloudFormation template and
  deploys the stack defined in the template into AWS.

###### Note

The following workflow example is for illustrative purposes, and will not work without
additional configuration.

###### Note

In the YAML code that follows, you can omit the `Connections:` sections if
you want. If you omit these sections, you must ensure that the role specified in the
**Default IAM role** field in your environment includes the permissions
and trust policies required by the **AWS CDK bootstrap** and **AWS CDK
deploy** actions. For more information about setting up an environment with a
default IAM role, see [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md"). For more information about the
permissions and trust policies required by the **AWS CDK bootstrap** and
**AWS CDK deploy** actions, see the description of the `Role`
property in the ['AWS CDK bootstrap' action YAML](cdk-boot-action-ref.md "cdk-boot-action-ref.md")
and ['AWS CDK deploy' action YAML](cdk-dep-action-ref.md "cdk-dep-action-ref.md").

```
Name: codecatalyst-cdk-deploy-workflow
SchemaVersion: 1.0

Triggers:
  - Type: PUSH
    Branches:
      - main
Actions:
  CDKBootstrap:
    Identifier: aws/cdk-bootstrap@v2
    Inputs:
      Sources:
        - WorkflowSource
    Environment:
      Name: codecatalyst-cdk-deploy-environment
      Connections:
        - Name: codecatalyst-account-connection
          Role: codecatalyst-cdk-bootstrap-role
    Configuration:
      Region: us-west-2

  CDKDeploy:
    Identifier: aws/cdk-deploy@v2
    DependsOn:
      - CDKBootstrap
    Environment:
      Name: codecatalyst-cdk-deploy-environment
      Connections:
        - Name: codecatalyst-account-connection
          Role: codecatalyst-cdk-deploy-role
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      StackName: my-app-stack
      Region: us-west-2
```
