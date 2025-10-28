# Architect your application for Amazon ECS

You architect your application by creating a task definition for your application. The
task definition contains the parameters that define information about the application,
including:

- The capacity to use, which determines the infrastructure that your tasks are
  hosted on.

When you use the EC2 capacity provider, you also choose the instance
type. When you use the Amazon ECS Managed Instances capacity provider, you can provide
instance requirements for Amazon ECS to manage compute capacity. For some instance types, such as
GPU, you need to set specific parameters. For more information, see [Amazon ECS task definition use cases](use-cases.md "use-cases.md").

- The container image, which holds your application code and all the dependencies
  that your application code requires to run.
- The networking mode to use for the containers in your task.

The networking mode determines how your task communicates over the network.

For tasks that run on EC2 instances and Amazon ECS Managed Instances, there are multiple options, but
we recommend that you use the `awsvpc` network mode. The
`awsvpc` network mode simplifies container networking by giving you
more control over how your applications communicate with each other and other
services within your VPCs.

For tasks that run on Fargate, you must use the `awsvpc` network
mode.

- The logging configuration to use for your tasks.
- Any data volumes that are used with the containers in the task.
  For a complete list of task definition parameters, see [Amazon ECS task definition parameters for Fargate](task_definition_parameters.md "task_definition_parameters.md").

Use the following guidelines when you create your task definitions:

- Use each task definition family for only one business purpose.

If you group multiple types of application containers together in the same task
definition, you can't independently scale those containers. For example, a website
and an API typically require different scaling patterns. As traffic increases, you
might need a different number of web containers than API containers. If these two
containers are deployed in the same task definition, every task runs the same number
of web containers and API containers.

- Match each application version with a task definition revision within a task
  definition family.

Within a task definition family, each task definition revision represents a
point-in-time snapshot of the settings for a particular container image. This is
similar to how the container is a snapshot of all the components needed to run a
particular version of your application code.

Create a one-to-one mapping between a version of application code, a container
image tag, and a task definition revision. A typical release process involves a git
commit that gets turned into a container image that's tagged with the git commit
SHA. Then, that container image tag gets its own Amazon ECS task definition revision.
Last, the Amazon ECS service is updated to deploy the new task definition
revision.

- Use different IAM roles for each task definition family.

Define each task definition with its own IAM role. Implement this practice along
with providing each business component its own task definition family. By
implementing both of these best practices, you can limit how much access each
service has to resources in your AWS account. For example, you can give your
authentication service access to connect to your passwords database. At the same
time, you can ensure that only your order service has access to the credit card
payment information.
