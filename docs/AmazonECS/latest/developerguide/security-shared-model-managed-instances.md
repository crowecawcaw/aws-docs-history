

# Shared responsibility model for Amazon ECS Managed Instances
<a name="security-shared-model-managed-instances"></a>

Amazon ECS Managed Instances provides a managed solution for containerized workloads that combines the operational simplicity of Fargate with access to the full range of Amazon EC2 instance types and capabilities. AWS handles infrastructure provisioning, patching, scaling, and maintenance while customers retain control over their applications and specific configurations.

Unlike Fargate, containerized workloads running on Amazon ECS Managed Instances share the operating system, Linux kernel, network interface, ephemeral storage, CPU, memory, and GPU resources with other tasks on the same instance. Amazon ECS optimizes infrastructure utilization by placing multiple tasks on larger instances to minimize unused capacity.

## AWS responsibilities
<a name="managed-instances-aws-responsibilities"></a>

When using Amazon ECS Managed Instances, AWS is responsible for:
+ Instance provisioning and lifecycle management
+ Operating system patching and security updates
+ Infrastructure scaling and optimization
+ Instance replacement and maintenance (maximum 21-day instance lifetime)
+ Access control restrictions (no SSH access, no SSM Session Manager access)
+ Amazon EC2 Instance Storage encryption, which is storage directly attached to the instance. For more information, see [Data protection in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html).
+ Amazon ECS manages the volumes attached to Amazon EC2 instances at creation time, including root and data volumes.
+ Amazon ECS uses Amazon EC2 managed instances under-the-hood. For more information about Amazon EC2 managed instances, see [Security in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html).

## Customer responsibilities
<a name="managed-instances-customer-responsibilities"></a>

You are responsible for managing the following resources:
+ Network configuration including VPC, NACLs, security groups, and route tables
+ Client and service storage encryption. For more information, see [Storage options for Amazon ECS tasks](using_data_volumes.md).
+ Container images. For more information, see [Amazon ECS task and container security best practices](security-tasks-containers.md).
+ IAM permissions for the applications by using the task role. For more information, see [Amazon ECS task IAM role](task-iam-roles.md).
+ Application-level configuration and monitoring
+ Security monitoring of your containers
+ Task and service definitions
+ Security considerations for co-located workloads. Unlike Fargate, there is no task isolation on Amazon ECS Managed Instances. Containers can potentially access credentials, environment variables, and temporary files from other tasks on the same instance, including data left behind by previously running tasks.
+ Privileged container configurations and enhanced Linux capabilities (CAP\_NET\_ADMIN, CAP\_BPF, CAP\_PERFMON, etc.) when enabled
+ Management operations through Amazon ECS API (direct instance access via SSH or SSM is not available)

For information about AWS and customer responsibilities for Amazon ECS Managed Instances security, see [Security considerations for Amazon ECS Managed Instances](managed-instances-security.md).

The following diagram illustrates the shared responsibility model for Amazon ECS Managed Instances, showing which security responsibilities are managed by AWS and which are yours.

![Diagram showing the shared responsibility model for Amazon ECS Managed Instances on Amazon ECS.](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/images/managed-instances-shared-responsibility.png)
