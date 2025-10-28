Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Building with workflows

Using [CodeCatalyst workflows](workflow.md "workflow.md"), you can build applications and other
resources.

###### Topics

- [How do I build an application?](#build-how-to "#build-how-to")
- [Benefits of the build action](#build-benefits "#build-benefits")
- [Alternatives to the build action](#build-alternatives "#build-alternatives")
- [Adding the build action](build-add-action.md "build-add-action.md")
- [Viewing the results of a build action](build-view-results.md "build-view-results.md")
- [Tutorial: Upload artifacts to Amazon S3](build-deploy.md "build-deploy.md")
- [Build and test actions YAML](build-action-ref.md "build-action-ref.md")

## How do I build an application?

To build an application or resource in CodeCatalyst, you first create a workflow, and then
specify a build action inside it.

A _build action_ is a workflow building block that compiles your source code, runs unit tests,
and produces artifacts that are ready to deploy.

You add a build action to your workflow using the CodeCatalyst console's visual editor or YAML
editor.

The high-level steps to build an application or resource are as follows.

###### To build an application (high-level tasks)

1. In CodeCatalyst, you **add source code** for an application you
   want to build. For more information, see [Storing source code in repositories for a project in
   CodeCatalyst](source-repositories.md "source-repositories.md").
2. In CodeCatalyst, you **create a workflow**. The workflow is
   where you define how to build, test, and deploy your application. For more information,
   see [Getting started with workflows](workflows-getting-started.md "workflows-getting-started.md").
3. (Optional) In the workflow, you **add a trigger** that
   indicates the events that will cause the workflow to start automatically. For more
   information, see [Starting a workflow run automatically using
   triggers](workflows-add-trigger.md "workflows-add-trigger.md")
4. In the workflow, you add a **build action** that compiles
   and packages your application or resource source code. Optionally, you can also have the
   build action run unit tests, generate reports, and deploy your application if you don't
   want to use a test or deploy action for these purposes. For more on the test and deploy
   actions, see [Adding the build action](build-add-action.md "build-add-action.md").
5. (Optional) In the workflow, you **add a test action** and
   a **deploy action** to test and deploy your application or
   resource. You can choose from several pre-configured actions to deploy your application to
   different targets, such as Amazon ECS. For more information, see [Testing with workflows](test-workflow-actions.md "test-workflow-actions.md"), and [Deploying with workflows](deploy.md "deploy.md").
6. You **start the workflow** either manually or
   automatically through a trigger. The workflow runs the build, test, and deploy actions in
   sequence to build, test, and deploy your application and resources to the target. For more
   information, see [Starting a workflow run manually](workflows-manually-start.md "workflows-manually-start.md").

## Benefits of the build action

Using the build action within a workflow has the following benefits:

- **Fully managed** – The build action eliminates
  the need to set up, patch, update, and manage your own build servers.
- **On demand** – The build action scales on demand
  to meet your build needs. You pay only for the number of build minutes you consume. For
  more information, see [Configuring compute and runtime images](workflows-working-compute.md "workflows-working-compute.md").
- **Out of the box** – CodeCatalyst includes prepackaged
  runtime environment Docker images that are used to run all your workflow actions,
  including build actions. These images come preconfigured with useful tools for building
  applications such as the AWS CLI and Node.js. You can configure CodeCatalyst to use a build image
  that you supply from a public or private registry. For more information, see [Specifying runtime environment images](build-images.md "build-images.md").

## Alternatives to the build action

If you're using a build action to deploy your application, consider using a CodeCatalyst
_deploy action_ instead. Deploy actions perform behind-the-scenes
configuration that you would otherwise have to write manually if you're using a build action.
For more information on the available deploy actions, see [List of deploy actions](deploy.md#deploy-concepts-action-supported "deploy.md#deploy-concepts-action-supported").

You can also use AWS CodeBuild to build your applications. For more information, see [What is
CodeBuild?](../../../codebuild/latest/userguide/welcome.md "../../../codebuild/latest/userguide/welcome.md").
