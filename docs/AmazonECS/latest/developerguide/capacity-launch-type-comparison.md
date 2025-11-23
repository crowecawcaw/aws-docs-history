# Amazon Amazon ECS launch types and capacity providers

Amazon ECS provides two methods for configuring capacity for workloads. You can use launch
types or capacity providers. Launch types include EC2, Fargate, and External. Capacity
providers offer enhanced flexibility and advanced features for capacity management. You can
run workloads on serverless compute with Fargate and Fargate Spot capacity
providers, on self-managed EC2 instances through Amazon EC2 Auto Scaling group capacity providers, or on
fully-managed compute using Amazon ECS Managed Instances capacity providers that combine the
simplicity of Fargate with the flexibility of EC2 compute. Capacity providers
offer better control over resource allocation and can help optimize both performance and
costs. Capacity providers are the recommended way to configure capacity for workloads compared to
traditional launch types. Use the following to understand the differences between capacity
providers and launch types.

## Best practices

The following are the best practices:

Use launch types to define infrastructure compatibility

Launch types define the infrastructure on which tasks and services
run. When you define tasks, specify `RequiresCompatibilities` to include one
or more launch types that are compatible with tasks. You can use following
launch types: EC2, Fargate, External, and Amazon ECS Managed Instances. While you
can also use launch type to run your tasks or services, we recommend using
the launch type only for defining compatibilities in your task definitions,
and use capacity providers for launching tasks or services. Note that
you can choose one or more launch types to define compatibilities for
tasks.

Use capacity providers to configure compute capacity

When you launch tasks or services, configure a capacity provider
strategy. Amazon ECS supports following capacity providers: Fargate and
FARGATE_SPOT, Amazon EC2 Auto Scaling groups for self-managed EC2 instances, and Amazon ECS Managed Instances.
Note that Spot Fleet is only available as a capacity provider and not as a
launch type. You can create one or more Amazon ECS Managed Instances or Amazon EC2 Auto Scaling groups capacity
providers in a cluster. Fargate and Fargate Spot capacity providers are created and managed
by Amazon ECS on every cluster and you do not need to create them. A cluster can have a mix of all capacity provider types, however, a
capacity provider strategy can't have a mix of different capacity provider types.

Update the capacity for services

You can simply update a capacity provider strategy for a service to move it from one compute type to the other.

## Service mutability

Amazon ECS supports updating services between different capacity providers. This allows
for:

- Seamless update from launch types to capacity providers
- Transitions between different capacity provider types
- Testing different compute options without service recreation

The following is a high-level overview of the process:

1. Update the task definition – Ensure `requiresCompatibilities` includes the target
   capacity provider, for example `MANAGED_INSTANCES`.

###### Note

Task definitions must pass compatibility validation for the target
capacity provider. If the `requiresCompatibilities` check fails
for the task definition version, the `UpdateService` call
fails. 2. Create a capacity provider – If you use custom Amazon EC2 Amazon EC2 Auto Scaling groups, create the capacity
provider. 3. Update the service – Modify the service to use a capacity provider strategy instead of the
launch type. 4. Validate the deployment – Confirm that tasks deploy successfully. 5. Monitor and optimize – Adjust capacity provider settings as needed.

### Capacity provider to

capacity provider

All capacity provider to capacity provider updates are supported:

- Amazon EC2 Amazon EC2 Auto Scaling group capacity provider to Amazon ECS Managed Instances
- Fargate capacity provider to Amazon ECS Managed Instances
- Amazon EC2 Amazon EC2 Auto Scaling group capacity provider to Fargate capacity
  provider
- Amazon ECS Managed Instances to Fargate capacity provider
- Fargate capacity provider to Amazon EC2 Amazon EC2 Auto Scaling group capacity
  provider
- Amazon ECS Managed Instances to Amazon EC2 Amazon EC2 Auto Scaling group capacity provider

### Launch type to capacity

provider

All launch type to capacity provider updates are supported:

- EC2 launch type to Amazon ECS Managed Instances
- Fargate launch type to Amazon ECS Managed Instances
- EC2 launch type to Fargate capacity provider
- EC2 launch type to EC2 Amazon EC2 Auto Scaling group capacity provider
- Fargate launch type to Amazon EC2 Amazon EC2 Auto Scaling group capacity provider
- Fargate launch type to Fargate capacity provider
- External launch type to Amazon ECS Managed Instances
- External launch type to Fargate capacity provider
- External launch type to Amazon EC2 Amazon EC2 Auto Scaling group capacity provider

### Launch type to launch type

Launch type to launch type updates are not supported:

- EC2 launch type to Fargate launch type (use Fargate
  capacity provider instead)
- Fargate launch type to EC2 launch type (use Amazon EC2
  Amazon EC2 Auto Scaling group capacity provider instead)

Instead of migrating between launch types, migrate to the equivalent capacity provider for enhanced functionality and future compatibility.

###### Note

Task definitions must pass compatibility validation for the target capacity provider. If the `requiresCompatibilities` check fails for the task definition version, the `UpdateService` call will fail.
