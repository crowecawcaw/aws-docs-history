Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring compute and runtime images

In a CodeCatalyst workflow, you can specify the compute and runtime environment image that
CodeCatalyst uses to run workflow actions.

_Compute_ refers to the computing engine (the CPU, memory, and operating
system) managed and maintained by CodeCatalyst to run workflow actions.

###### Note

If compute is defined as a property of the workflow, then it can't be defined as a
property of any action in that workflow. Similarly, if compute is defined as a property
of any action, it can't be defined in the workflow.

A _runtime environment image_ is a Docker container within which CodeCatalyst
runs workflow actions. The Docker container runs on top of your chosen compute platform, and includes
an operating system and extra tools that a workflow action might need, such as the AWS CLI,
Node.js, and .tar.

###### Topics

- [Compute types](#compute.types "#compute.types")
- [Compute fleets](#compute.fleets "#compute.fleets")
- [On-demand fleet properties](#compute.on-demand "#compute.on-demand")
- [Provisioned fleet properties](#compute.provisioned-fleets "#compute.provisioned-fleets")
- [Creating a provisioned fleet](projects-create-compute-resource.md "projects-create-compute-resource.md")
- [Editing a provisioned fleet](edit-compute-resource.md "edit-compute-resource.md")
- [Deleting a provisioned fleet](delete-compute-resource.md "delete-compute-resource.md")
- [Assigning a fleet or compute to an
  action](workflows-assign-compute-resource.md "workflows-assign-compute-resource.md")
- [Sharing compute across actions](compute-sharing.md "compute-sharing.md")
- [Specifying runtime environment images](build-images.md "build-images.md")

## Compute types

CodeCatalyst offers the following compute types:

- Amazon EC2
- AWS Lambda

Amazon EC2 offers optimized flexibility during action runs and Lambda offers optimized
action start-up speeds. Lambda supports faster workflow action runs due to a lower
start-up latency. Lambda allows you to run basic workflows that can build, test, and
deploy serverless applications with common runtimes. These runtimes include Node.js,
Python, Java, .NET, and Go. However, there are some use-cases which Lambda does not
support, and if they impact you, use the Amazon EC2 compute type:

- Lambda doesn't support runtime environment images from a specified
  registry.
- Lambda doesn't support tools that require root permissions. For tools such as
  `yum` or `rpm`, use the Amazon EC2 compute type or other
  tools that don't require root permissions.
- Lambda doesn't support Docker builds or runs. The following actions that use
  Docker images are not supported: Deploy AWS CloudFormation stack, Deploy to Amazon ECS, Amazon S3
  publish, AWS CDK bootstrap, AWS CDK deploy, AWS Lambda invoke , and GitHub Actions.
  Docker-based GitHub Actions that are running within CodeCatalyst GitHub Actions action
  are also not supported with Lambda compute. You can use alternatives that don’t
  require root permissions, such as Podman.
- Lambda doesn't support writing to files outside `/tmp`. When
  configuring your workflow actions, you can reconfigure your tools to install or
  write to `/tmp`. If you have a build action that installs
  `npm`, make sure you configure it to install to
  `/tmp`.
- Lambda doesn't support runtimes longer than 15 minutes.

## Compute fleets

CodeCatalyst offers the following compute fleets:

- On-demand fleets
- Provisioned fleets

With on-demand fleets, when a workflow action starts, the workflow provisions the
resources it needs. The machines are destroyed when the action finishes. You only pay
for the number of minutes that you're running your actions. On-demand fleets are fully
managed, and includes automatic scaling capabilities to handle spikes in demand.

CodeCatalyst also offers provisioned fleets which contain machines powered by Amazon EC2 that are
maintained by CodeCatalyst. With provisioned fleets, you configure a set of dedicated machines
to run your workflow actions. These machines remain idle, ready to process actions
immediately. With provisioned fleets, your machines are always running and will incur
costs as long they're provisioned.

In order to create, update, or delete a fleet, you must have the
**Space administrator** role or the
**Project administrator** role.

## On-demand fleet properties

CodeCatalyst provides the following on-demand fleets:

| Name                   | Operating system | Architecture | vCPUs            | Memory (GiB) | Disk space     | Supported compute types |
| ---------------------- | ---------------- | ------------ | ---------------- | ------------ | -------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Linux.Arm64.Large`    | Amazon Linux 2   | Arm64        | 2                | 4            | 64 GB          | Amazon EC2              |
| 10 GB                  | Lambda           |
| `Linux.Arm64.XLarge`   | Amazon Linux 2   | Arm64        | 4                | 8            | 128 GB         | Amazon EC2              |
| 10 GB                  | Lambda           |
| `Linux.Arm64.2XLarge`  | Amazon Linux 2   | Arm64        | 8                | 16           | 128 GB         | Amazon EC2              |
| `Linux.x86-64.Large`   | Amazon Linux 2   | x86-64       | 2                | 4            | 64 GB          | Amazon EC2              |
| 10 GB                  | Lambda           |
| `Linux.x86-64.XLarge`  | Amazon Linux 2   | x86-64       | 4                | 8            | 128 GB         | Amazon EC2              |
| 10 GB                  | Lambda           |
| `Linux.x86-64.2XLarge` | Amazon Linux 2   | x86-64       | 8                | 16           | 128 GB         | Amazon EC2              | ###### Note The specifications for on-demand fleets will vary depending on your billing tier. For more information, see [Pricing](https://codecatalyst.aws/explore/pricing "https://codecatalyst.aws/explore/pricing"). If no fleet is selected, CodeCatalyst uses `Linux.x86-64.Large`. ## Provisioned fleet properties A provisioned fleet contains the following properties: **Operating system** The operating system. The following operating systems are available: <br>• Amazon Linux 2 <br>• Windows Server 2022 ###### Note Windows fleets are only supported in the build action. Other actions do not currently support Windows. **Architecture** The processor architecture. The following architectures are available: <br>• x86_64 <br>• Arm64 **Machine type** The machine type for each instance. The following machine types are available: |
| vCPUs                  | Memory (GiB)     | Disk space   | Operating system |              | ---            | ---                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 2                      | 4                | 64 GB        | Amazon Linux 2   |              | 4              | 8                       | 128 GB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Amazon Linux 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Windows Server 2022    |                  | 8            | 16               | 128 GB       | Amazon Linux 2 |                         | Windows Server 2022                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Capacity** The initial number of machines allocated to the fleet, which defines the number of actions that can run in parallel. **Scaling mode** Defines the behavior when the number of actions exceeds the fleet capacity. **Provision additional capacity on demand** Additional machines are set up on demand which automatically scale up in response to new actions running, and then scale down to the base capacity as actions finish. This can incur additional costs, since you pay by the minute for each machine running. **Wait until additional fleet capacity is available** Action runs are placed in a queue until a machine is available. This limits additional costs because no additional machines are allocated. |
