Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'Deploy to Amazon ECS' variables

The **Deploy to Amazon ECS** action produces and sets the following variables
at run time. These are known as _predefined variables_.

For information about referencing these variables in a workflow, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").

| Key                 | Value                                                                                                                                                                                                                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cluster             | The name of the Amazon ECS cluster that was deployed to during the workflow<br>run.<br>Example: `codecatalyst-ecs-cluster`                                                                                                                                                                                 |
| deployment-platform | The name of the deployment platform.<br>Hardcoded to `AWS:ECS`.                                                                                                                                                                                                                                            |
| service             | The name of the Amazon ECS service that was deployed to during the workflow<br>run.<br>Example: `codecatalyst-ecs-service`                                                                                                                                                                                 |
| task-definition-arn | The Amazon Resource Name (ARN) of the task definition that was registered during<br>the workflow run.<br>Example:<br>`arn:aws:ecs:us-west-2:111122223333:task-definition/codecatalyst-task-def:8`The<br>`:8` in the preceding example indicates the revision that was<br>registered.                       |
| deployment-url      | A link to the Amazon ECS console's \*_Events_<br>• tab, where you can<br>view details of the Amazon ECS deployment associated with the workflow run.<br>Example:<br>`https://console.aws.amazon.com/ecs/home?region=us-west-2#/clusters/codecatalyst-ecs-cluster/services/codecatalyst-ecs-service/events` |
| region              | The region code of the AWS Region that was deployed to during the workflow<br>run.<br>Example: `us-west-2`                                                                                                                                                                                                 |
