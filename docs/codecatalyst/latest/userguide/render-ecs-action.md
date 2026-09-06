

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Modifying an Amazon ECS task definition
<a name="render-ecs-action"></a>

This section describes how to update the `image` field in an Amazon Elastic Container Service (Amazon ECS) [task definition file](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html#welcome-task-definitions) using a CodeCatalyst workflow. To accomplish this, you must add the **Render Amazon ECS task definition** action to your workflow. This action updates the image field in the task definition file with a Docker image name that is supplied by your workflow at runtime.

**Note**  
You can also use this action to update the task definition’s `environment` field with environment variables.

**Topics**
+ [When to use this action](#render-ecs-action-when-to-use)
+ [How the 'Render Amazon ECS task definition' action works](#render-ecs-action-how-it-works)
+ [Runtime image used by the 'Render Amazon ECS task definition' action](#render-ecs-action-runtime)
+ [Example: Modify an Amazon ECS taskdef](render-ecs-action-example-workflow.md)
+ [Adding the 'Render Amazon ECS task definition' action](render-ecs-action-add.md)
+ [Viewing the updated task definition file](render-ecs-action-view.md)
+ ['Render Amazon ECS task definition' variables](render-ecs-action-variables.md)
+ ['Render Amazon ECS task definition' action YAML](render-ecs-action-ref.md)

## When to use this action
<a name="render-ecs-action-when-to-use"></a>

Use this if you have a workflow that builds and tags a Docker image with dynamic content, such as a commit ID or timestamp. 

Do not use this action if your task definition file contains an image value that always stays the same. In this case, you can manually enter the name of your image into the task definition file.

## How the 'Render Amazon ECS task definition' action works
<a name="render-ecs-action-how-it-works"></a>

You must use the **Render Amazon ECS task definition** action with the **build** and **Deploy to Amazon ECS** actions in your workflow. Together, these actions work as follows:

1. The **build** action builds your Docker image and tags it with a name, a commit ID, timestamp, or other dynamic content. For example, your build action might look like this:

   ```
   MyECSWorkflow
     Actions:
       BuildAction:
         Identifier: aws/build@v1
         ...
         Configuration:
           Steps:
           # Build, tag, and push the Docker image...
             - Run: docker build -t MyDockerImage:${WorkflowSource.CommitId} .
             ...
   ```

   In the preceding code, the `docker build -t` directive indicates to build the Docker image and tag it with the commit ID at action runtime. The generated image name might look like this:

   `MyDockerImage:a37bd7e`

1. The **Render Amazon ECS task definition** action adds the dynamically generated image name, `MyDockerImage:a37bd7e`, to your task definition file, like this:

   ```
   {
       "executionRoleArn": "arn:aws:iam::account_ID:role/codecatalyst-ecs-task-execution-role",
       "containerDefinitions": [
           {
               "name": "codecatalyst-ecs-container",
               "image":  MyDockerImage:a37bd7e, 
               "essential": true,
               ...
               "portMappings": [
                   {
                       "hostPort": 80,
                       "protocol": "tcp",
                       "containerPort": 80
                   }
               ]
           }
       ],
   ...
   }
   ```

   Optionally, you can also have the **Render Amazon ECS task definition** action add environment variables to the task definition, like this:

   ```
   {
     "executionRoleArn": "arn:aws:iam::account_ID:role/codecatalyst-ecs-task-execution-role",
     "containerDefinitions": [
       {
         "name": "codecatalyst-ecs-container",
         "image":  MyDockerImage:a37bd7e,
         ...
         "environment": [
           {
             name": "ECS_LOGLEVEL",
             value": "info"
           }
         ]
       }
     ],
   ...
   }
   ```

   For more information about environment variables, see [Specifying environment variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html) in the *Amazon Elastic Container Service Developer Guide*.

1. The **Deploy to Amazon ECS** action registers the updated task definition file with Amazon ECS. Registering the updated task definition file deploys the new image, `MyDockerImage:a37bd7e` into Amazon ECS.

## Runtime image used by the 'Render Amazon ECS task definition' action
<a name="render-ecs-action-runtime"></a>

The **Render Amazon ECS task definition** action runs on a [November 2022 image](build-images.md#build.previous-image). For more information, see [Active images](build-images.md#build-curated-images).