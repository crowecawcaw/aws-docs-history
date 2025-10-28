Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'Deploy to Amazon ECS' variables

The **Deploy to Amazon ECS** action produces and sets the following variables
at run time. These are known as _predefined variables_.

For information about referencing these variables in a workflow, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").

| Key                 | Value                                                                                                                                                                                                                                                                                        |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cluster             | The name of the Amazon ECS cluster that was deployed to during the workflow run. Example: `codecatalyst-ecs-cluster`                                                                                                                                                                         |
| deployment-platform | The name of the deployment platform. Hardcoded to `AWS:ECS`.                                                                                                                                                                                                                                 |
| service             | The name of the Amazon ECS service that was deployed to during the workflow run. Example: `codecatalyst-ecs-service`                                                                                                                                                                         |
| task-definition-arn | The Amazon Resource Name (ARN) of the task definition that was registered during the workflow run. Example: `arn:aws:ecs:us-west-2:111122223333:task-definition/codecatalyst-task-def:8`The `:8` in the preceding example indicates the revision that was registered.                        |
| deployment-url      | A link to the Amazon ECS console's **Events** tab, where you can view details of the Amazon ECS deployment associated with the workflow run. Example: `https://console.aws.amazon.com/ecs/home?region=us-west-2#/clusters/codecatalyst-ecs-cluster/services/codecatalyst-ecs-service/events` |
| region              | The region code of the AWS Region that was deployed to during the workflow run. Example: `us-west-2`                                                                                                                                                                                         |
