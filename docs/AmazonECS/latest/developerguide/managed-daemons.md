# Amazon ECS Managed Daemons

Amazon ECS Managed Daemons enable you to deploy and manage software agents, such as
security, observability, and networking agents, across your container infrastructure on
Amazon ECS Managed Instances. Managed Daemons decouple daemon lifecycle management from
application operations. You can deploy, update, and monitor agents independently, without
redeploying workloads or coordinating changes across services.

## How Managed Daemons work

To use Managed Daemons, first register a daemon task definition. A daemon task
definition is a template that describes the containers that form a daemon. After you
register a daemon task definition, create a daemon and associate it with a cluster and
one or more Amazon ECS Managed Instances capacity providers. Amazon ECS then ensures that exactly one
daemon task runs on every Amazon EC2 instance provisioned through those capacity
providers.

Daemons do not launch instances independently. When you run an application task on a
Amazon ECS Managed Instances capacity provider, Amazon ECS provisions an Amazon EC2 instance, starts the
daemon task first, and only then transitions the application task to
`RUNNING`. This ordering guarantees that cross-cutting functions like
logging, tracing, and metrics collection are operational before your application begins
processing requests.

Daemons are essential for instance health. If a daemon task stops, Amazon ECS automatically
drains and replaces that container instance. This auto-repair behavior ensures reliable
daemon coverage across all instances without manual intervention.

When you update a daemon to a new task definition revision, Amazon ECS performs a rolling
deployment across all instances in the associated capacity providers. During the
deployment, Amazon ECS drains a configurable percentage of instances simultaneously,
provisions replacement instances with the updated daemon, and replaces your Amazon ECS
service tasks automatically. Amazon ECS provides built-in circuit breaker protection. You
can configure a bake time and CloudWatch alarms so that Amazon ECS monitors the deployment after
it updates all instances and automatically rolls back if issues arise.

## Key benefits

- **Decoupled lifecycle management** - Update
  daemons independently from application deployments.
- **Guaranteed coverage** - Amazon ECS ensures
  daemon tasks start before application tasks on every instance, so cross-cutting
  functions are always available.
- **Reliable version updates** - When you
  update a daemon version, Amazon ECS rolls it out across all instances in the
  associated capacity providers, with built-in circuit breaker protection and
  automatic rollback to ensure every instance runs the target revision.
- **Improved resource utilization** - Running
  a single daemon task per instance eliminates the sidecar-per-task model,
  reducing resource overhead across your cluster.
- **Automatic instance repair** - If a daemon
  task stops or becomes unhealthy, Amazon ECS automatically drains and replaces that
  container instance. This maintains reliable daemon coverage without manual
  intervention.

###### Note

Amazon ECS offers a DAEMON scheduling strategy for Amazon ECS services for the Amazon EC2 launch
type. Managed Daemons is a new capability built for Amazon ECS Managed Instances to
simplify daemon deployments and provide stronger daemon coverage guarantees.

## Getting started

To get started, register a daemon task definition specifying your container image,
then create a daemon with associated capacity providers in your cluster. You can use the
AWS Management Console, AWS CLI, CloudFormation, or AWS SDKs. For step-by-step instructions, see [Creating and managing daemons](managed-daemons-create-manage.md "managed-daemons-create-manage.md").
