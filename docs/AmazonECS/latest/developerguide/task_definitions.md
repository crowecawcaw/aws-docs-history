# Amazon ECS task definitions

A _task definition_ is a blueprint for your application. It is a text
file in JSON format that describes the parameters and one or more containers that form your
application.

The following are some of the parameters that you can specify in a task definition:

- The capacity to use, which determines the infrastructure that your tasks are
  hosted on
- The Docker image to use with each container in your task
- How much CPU and memory to use with each task or each container within a
  task
- The memory and CPU requirements
- The operating system of the container that the task runs on
- The Docker networking mode to use for the containers in your task
- The logging configuration to use for your tasks
- Whether the task continues to run if the container finishes or fails
- The command that the container runs when it's started
- Any data volumes that are used with the containers in the task
- The IAM role that your tasks use
  For a complete list of task definition parameters, see [Amazon ECS task definition parameters for Fargate](task_definition_parameters.md "task_definition_parameters.md").

After you create a task definition, you can run the task definition as a task or a
service.

- A _task_ is the instantiation of a task definition within a
  cluster. After you create a task definition for your application within Amazon ECS, you
  can specify the number of tasks to run on your cluster.
- An Amazon ECS _service_ runs and maintains your
  desired number of tasks simultaneously in an Amazon ECS cluster. How it works is that, if
  any of your tasks fail or stop for any reason, the Amazon ECS service scheduler launches
  another instance based on your task definition. It does this to replace it and
  thereby maintain your desired number of tasks in the service.

###### Topics

- [Amazon ECS task definition states](task-definition-state.md "task-definition-state.md")
- [Architect your application for Amazon ECS](application_architecture.md "application_architecture.md")
- [Creating an Amazon ECS task definition using the
  console](create-task-definition.md "create-task-definition.md")
- [Using Amazon Q Developer to provide task definition recommendations in the Amazon ECS console](using-amazon-q.md "using-amazon-q.md")
- [Updating an Amazon ECS task definition using
  the console](update-task-definition-console-v2.md "update-task-definition-console-v2.md")
- [Deregistering an Amazon ECS task definition revision
  using the console](deregister-task-definition-v2.md "deregister-task-definition-v2.md")
- [Deleting an Amazon ECS task definition revision using the
  console](delete-task-definition-v2.md "delete-task-definition-v2.md")
- [Amazon ECS task definition use cases](use-cases.md "use-cases.md")
- [Amazon ECS task definition
  parameters for Amazon ECS Managed Instances](task_definition_parameters-managed-instances.md "task_definition_parameters-managed-instances.md")
- [Amazon ECS task definition parameters for Fargate](task_definition_parameters.md "task_definition_parameters.md")
- [Amazon ECS task definition parameters for
  Amazon EC2](task_definition_parameters_ec2.md "task_definition_parameters_ec2.md")
- [Amazon ECS task definition template](task-definition-template.md "task-definition-template.md")
- [Example Amazon ECS task definitions](example_task_definitions.md "example_task_definitions.md")
