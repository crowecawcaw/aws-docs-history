

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Deploying to Amazon ECS with a workflow
<a name="deploy-action-ecs"></a>

This section describes how to deploy a containerized application into an Amazon Elastic Container Service cluster using a CodeCatalyst workflow. To accomplish this, you must add the **Deploy to Amazon ECS** action to your workflow. This action registers a [task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html#welcome-task-definitions) file that you provide. Upon registration, the task definition is instantiated by your [Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) running in your [Amazon ECS cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html#welcome-clusters). "Instantiating a task definition" is equivalent to deploying an application into Amazon ECS.

To use this action, you must have an Amazon ECS cluster, service, and task definition file ready.

For more information about Amazon ECS, see the *Amazon Elastic Container Service Developer Guide*.

**Tip**  
For a tutorial that shows you how to use the **Deploy to Amazon ECS ** action, see [Tutorial: Deploy an application to Amazon ECS](deploy-tut-ecs.md).

**Tip**  
For a working example of the **Deploy to Amazon ECS** action, create a project with either the **Node.js API with AWS Fargate** or **Java API with AWS Fargate** blueprint. For more information, see [Creating a project with a blueprint](projects-create.md#projects-create-console-template).

**Topics**
+ [Runtime image used by the 'Deploy to Amazon ECS' action](#deploy-action-ecs-runtime)
+ [Tutorial: Deploy an application to Amazon ECS](deploy-tut-ecs.md)
+ [Adding the 'Deploy to Amazon ECS' action](deploy-action-ecs-adding.md)
+ ['Deploy to Amazon ECS' variables](deploy-action-ecs-variables.md)
+ ['Deploy to Amazon ECS' action YAML](deploy-action-ref-ecs.md)

## Runtime image used by the 'Deploy to Amazon ECS' action
<a name="deploy-action-ecs-runtime"></a>

The **Deploy to Amazon ECS** action runs on a [November 2022 image](build-images.md#build.previous-image). For more information, see [Active images](build-images.md#build-curated-images).