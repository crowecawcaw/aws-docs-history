Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deploying with workflows

Using [CodeCatalyst workflows](workflow.md "workflow.md"), you can deploy applications and
other resources to various targets such as Amazon ECS, AWS Lambda, and more.

## How do I deploy an application?

To deploy an application or resource through CodeCatalyst, you first create a workflow, and then
specify a deploy action inside of it. A _deploy action_ is a workflow
building block that defines _what_ you want to deploy,
_where_ you want to deploy it, and _how_ you want to
deploy it (for example, using a blue/green scheme). You add a deploy action to your workflow
using the CodeCatalyst console's visual editor, or YAML editor.

The high-level steps to deploy an application or resource are as follows.

###### To deploy an application (high-level tasks)

1. In your CodeCatalyst project, you **add source code** for an
   application you want to deploy. For more information, see [Storing source code in repositories for a project in
   CodeCatalyst](source-repositories.md "source-repositories.md").
2. In your CodeCatalyst project, you **add an environment** that
   defines the target AWS account and optional Amazon Virtual Private Cloud (VPC) that you want to deploy to.
   For more information, see [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md").
3. In your CodeCatalyst project, you **create a workflow**. The
   workflow is where you define how to build, test, and deploy your application. For more
   information, see [Getting started with workflows](workflows-getting-started.md "workflows-getting-started.md").
4. In the workflow, you **add a trigger**, a **build action**, and optionally, a **test
   action**. For more information, see [Starting a workflow run automatically using
   triggers](workflows-add-trigger.md "workflows-add-trigger.md"), [Adding the build action](build-add-action.md "build-add-action.md"), and [Adding the test action](test-add-action.md "test-add-action.md").
5. In the workflow, you **add a deploy action**. You can
   choose from several CodeCatalyst-provided deploy actions to your application to different
   targets, such as Amazon ECS. (You can also use a build action or a GitHub Action to deploy your
   application. For more information about the build action and GitHub Actions, see [Alternatives to deploy actions](#deploy-concepts-alternatives "#deploy-concepts-alternatives").)
6. You **start the workflow** either manually or
   automatically through a trigger. The workflow runs the build, test, and deploy actions in
   sequence to deploy your application and resources to the target. For more information, see
   [Starting a workflow run manually](workflows-manually-start.md "workflows-manually-start.md").

## List of deploy actions

The following deploy actions are available:

- Deploy AWS CloudFormation stack – This action creates a CloudFormation stack in AWS based on
  an [AWS CloudFormation
  template](../../../serverless-application-model/latest/developerguide/sam-specification.md "../../../serverless-application-model/latest/developerguide/sam-specification.md") or [AWS Serverless Application Model template](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md")
  that you provide. For more information, see [Deploying an AWS CloudFormation stack](deploy-action-cfn.md "deploy-action-cfn.md").
- Deploy to Amazon ECS – This action registers a [task
  definition](../../../AmazonECS/latest/developerguide/Welcome.md#welcome-task-definitions "../../../AmazonECS/latest/developerguide/Welcome.md#welcome-task-definitions") file that you provide. For more information, see [Deploying to Amazon ECS with a workflow](deploy-action-ecs.md "deploy-action-ecs.md").
- Deploy to Kubernetes cluster – This action deploys an application to an Amazon Elastic Kubernetes Service
  cluster. For more information, see [Deploying to Amazon EKS with a
  workflow](deploy-action-eks.md "deploy-action-eks.md").
- AWS CDK deploy – This action deploys an [AWS CDK app](../../../cdk/v2/guide/getting_started.md#getting_started_concepts "../../../cdk/v2/guide/getting_started.md#getting_started_concepts") into
  AWS. For more information, see [Deploying an AWS CDK app with a workflow](cdk-dep-action.md "cdk-dep-action.md").

###### Note

There are other CodeCatalyst actions that can deploy resources; however, they are not
considered _deploy_ actions because their deployment information doesn't
appear on the **Environments** page. To learn more about the
**Environments** page and viewing deployments, see [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md") and [Viewing deployment information](deploy-view-deployment-info.md "deploy-view-deployment-info.md").

## Benefits of deploy actions

Using deploy actions within a workflow has the following benefits:

- **Deployment history** – View a history of your
  deployments to help manage and communicate changes in your deployed software.
- **Traceability** – Track the status of your
  deployments through the CodeCatalyst console, and see when and where each application revision
  was deployed.
- **Rollbacks** – Roll back deployments
  automatically if there are errors. You can also configure alarms to activate deployment
  rollbacks.
- **Monitoring** – Watch your deployment as it
  progresses through the various stages of your workflow.
- **Integration with other CodeCatalyst features** – Store
  source code and then build, test, and deploy it, all from one application.

## Alternatives to deploy actions

You don't have to use deploy actions, although they are recommended because they offer the
benefits outlined in the preceding section. Instead, you can use the following [CodeCatalyst actions](workflows-actions.md#workflows-actions-types-cc "workflows-actions.md#workflows-actions-types-cc") :

- A **build** action.

Typically, you use build actions if you want to deploy to a target for which a
corresponding deploy action does not exist, or if you want more control over the
deployment procedure. For more information about using build actions to deploy resources,
see [Building with workflows](build-workflow-actions.md "build-workflow-actions.md").

- A **GitHub Action**.

You can use a [GitHub Action](workflows-actions.md#workflows-actions-types-github "workflows-actions.md#workflows-actions-types-github")
inside a CodeCatalyst workflow to deploy applications and resources (instead of a CodeCatalyst
action). For information about how to use GitHub Actions inside a CodeCatalyst workflow, see
[Integrating with GitHub Actions](integrations-github-actions.md "integrations-github-actions.md")

You can also use the following AWS services to deploy your application, if you don't
want to use a CodeCatalyst workflow to do so:

- AWS CodeDeploy – see [What is CodeDeploy?](../../../codedeploy/latest/userguide/welcome.md "../../../codedeploy/latest/userguide/welcome.md")
- AWS CodeBuild and AWS CodePipeline – see [What is AWS CodeBuild?](../../../codebuild/latest/userguide/welcome.md "../../../codebuild/latest/userguide/welcome.md") and [What is
  AWS CodePipeline?](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md")
- AWS CloudFormation – see [What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")

Use CodeDeploy, CodeBuild, CodePipeline, and CloudFormation services for complex, enterprise
deployments.

###### Topics

- [Deploying to Amazon ECS with a workflow](deploy-action-ecs.md "deploy-action-ecs.md")
- [Deploying to Amazon EKS with a
  workflow](deploy-action-eks.md "deploy-action-eks.md")
- [Deploying an AWS CloudFormation stack](deploy-action-cfn.md "deploy-action-cfn.md")
- [Deploying an AWS CDK app with a workflow](cdk-dep-action.md "cdk-dep-action.md")
- [Bootstrapping an AWS CDK app with a workflow](cdk-boot-action.md "cdk-boot-action.md")
- [Publishing files to Amazon S3 with a workflow](s3-pub-action.md "s3-pub-action.md")
- [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md")
- [Displaying the app URL in the workflow diagram](deploy-app-url.md "deploy-app-url.md")
- [Removing a deployment target](deploy-remove-target.md "deploy-remove-target.md")
- [Tracking deployment status by commit](track-changes.md "track-changes.md")
- [Viewing the deployment logs](deploy-deployment-logs.md "deploy-deployment-logs.md")
- [Viewing deployment information](deploy-view-deployment-info.md "deploy-view-deployment-info.md")
