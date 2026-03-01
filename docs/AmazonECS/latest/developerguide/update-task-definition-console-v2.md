# Updating an Amazon ECS task definition using the console

A _task definition revision_ is a copy of the current task definition
with the new parameter values replacing the existing ones. All parameters that you do not
modify are in the new revision.

To update a task definition, create a task definition revision. If the task definition is
used in a service, you must update that service to use the updated task definition.

When you create a revision, you can modify the following container properties and
environment properties.

- Container image URI
- Port mappings
- Environment variables
- Infrastructure requirements
- Task size
- Container size
- Task role
- Task execution role
- Volumes and container mount points
- Private registry
  You can have Amazon Q provide recommendations when you use the JSON editor. For more
  information, see [Using Amazon Q Developer to provide task definition recommendations in the Amazon ECS console](using-amazon-q.md "using-amazon-q.md")

## JSON validation

The Amazon ECS console JSON editor validates the following in the JSON file:

- The file is a valid JSON file
- The file does not contain any extraneous keys
- The file contains the `familyName` parameter
- There is at least one entry under `containerDefinitions`

## Procedure

Amazon ECS console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, choose the Region that contains your task
   definition.
3. In the navigation pane, choose **Task
   definitions**.
4. Choose the task definition.
5. Select the task definition revision, and then choose
   **Create new revision**, **Create new
   revision**.
6. On the **Create new task definition revision**
   page, make changes. For example, to change the existing container
   definitions (such as the container image, memory limits, or port
   mappings), select the container, and then make the changes. You can
   update task definition compatibility to one of **AWS
   Fargate**, **Managed Instances**,
   **Amazon EC2 instances**.
7. Verify the information, and then choose
   **Update**.
8. If your task definition is used in a service, update your service
   with the updated task definition. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").

Amazon ECS console JSON editor

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task
   definitions**.
3. Choose **Create new revision**, **Create
   new revision with JSON**.
4. In the JSON editor box, edit your JSON file,

The JSON must pass the validation checks specified in [JSON validation](#json-validate-for-update "#json-validate-for-update"). 5. Choose **Create**.
