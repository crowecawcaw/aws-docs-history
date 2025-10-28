Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deploying to Amazon ECS with a workflow

This section describes how to deploy a containerized application into an Amazon Elastic Container Service cluster
using a CodeCatalyst workflow. To accomplish this, you must add the **Deploy to
Amazon ECS** action to your workflow. This action registers a [task
definition](../../../AmazonECS/latest/developerguide/Welcome.md#welcome-task-definitions "../../../AmazonECS/latest/developerguide/Welcome.md#welcome-task-definitions") file that you provide. Upon registration, the task definition is
instantiated by your [Amazon ECS service](../../../AmazonECS/latest/developerguide/ecs_services.md "../../../AmazonECS/latest/developerguide/ecs_services.md") running in your
[Amazon ECS cluster](../../../AmazonECS/latest/developerguide/Welcome.md#welcome-clusters "../../../AmazonECS/latest/developerguide/Welcome.md#welcome-clusters").
"Instantiating a task definition" is equivalent to deploying an application into Amazon ECS.

To use this action, you must have an Amazon ECS cluster, service, and task definition file
ready.

For more information about Amazon ECS, see the _Amazon Elastic Container Service Developer Guide_.

###### Tip

For a tutorial that shows you how to use the **Deploy to Amazon ECS** action,
see [Tutorial: Deploy an application to Amazon ECS](deploy-tut-ecs.md "deploy-tut-ecs.md").

###### Tip

For a working example of the **Deploy to Amazon ECS** action, create a project
with either the **Node.js API with AWS Fargate** or
**Java API with AWS Fargate** blueprint. For more information, see [Creating a project with a
blueprint](projects-create.md#projects-create-console-template "projects-create.md#projects-create-console-template").

###### Topics

- [Runtime image used by the 'Deploy to Amazon ECS'
  action](#deploy-action-ecs-runtime "#deploy-action-ecs-runtime")
- [Tutorial: Deploy an application to Amazon ECS](deploy-tut-ecs.md "deploy-tut-ecs.md")
- [Adding the 'Deploy to Amazon ECS' action](deploy-action-ecs-adding.md "deploy-action-ecs-adding.md")
- ['Deploy to Amazon ECS' variables](deploy-action-ecs-variables.md "deploy-action-ecs-variables.md")
- ['Deploy to Amazon ECS' action YAML](deploy-action-ref-ecs.md "deploy-action-ref-ecs.md")

## Runtime image used by the 'Deploy to Amazon ECS'

action

The **Deploy to Amazon ECS** action runs on a [November 2022 image](build-images.md#build.previous-image "build-images.md#build.previous-image"). For more information, see [Active images](build-images.md#build-curated-images "build-images.md#build-curated-images").
