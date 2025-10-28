# Compute resource AMIs

By default, AWS Batch managed compute environments use a recent, approved version of the Amazon ECS
optimized AMI for compute resources. However, you might want to create your own AMI to use for
your managed and unmanaged compute environments. If you require any of the following, we recommend
you create your own AMI:

- Increasing the storage size of your AMI root or data volumes
- Adding instance storage volumes for supported Amazon EC2 instance types
- Customizing the Amazon ECS container agent
- Customizing Docker
- Configuring a GPU workload AMI to allow containers to access GPU hardware on supported
  Amazon EC2 instance types

###### Note

After a compute environment is created, AWS Batch doesn't upgrade the AMIs in the compute
environment. AWS Batch also doesn't update the AMIs in your compute environment when a newer
version of the Amazon ECS optimized AMI is available. You're responsible for the management of the
guest operating system. This includes any updates and security patches. You're also responsible
for any additional application software or utilities that you install on the compute resources.
To use a new AMI for your AWS Batch jobs, do the following:

1. Create a new compute environment with the new AMI.
2. Add the compute environment to an existing job queue.
3. Remove the earlier compute environment from your job queue.
4. Delete the earlier compute environment.
   In April 2022, AWS Batch added enhanced support for updating compute environments. For more
   information, see [Update a compute environment in
   AWS Batch](updating-compute-environments.md "updating-compute-environments.md"). To use the enhanced updating of compute environments
   to update AMIs, follow these rules:

- Either don't set the service role ([`serviceRole`](../APIReference/API_CreateComputeEnvironment.md#Batch-CreateComputeEnvironment-request-serviceRole "../APIReference/API_CreateComputeEnvironment.md#Batch-CreateComputeEnvironment-request-serviceRole")) parameter or set it to the **AWSServiceRoleForBatch** service-linked role.
- Set the allocation strategy ([`allocationStrategy`](../APIReference/API_ComputeResource.md#Batch-Type-ComputeResource-allocationStrategy "../APIReference/API_ComputeResource.md#Batch-Type-ComputeResource-allocationStrategy")) parameter to `BEST_FIT_PROGRESSIVE`,
  `SPOT_CAPACITY_OPTIMIZED`, or `SPOT_PRICE_CAPACITY_OPTIMIZED`.
- Set the update to latest image version ([`updateToLatestImageVersion`](../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-updateToLatestImageVersion "../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-updateToLatestImageVersion")) parameter to `true`.
- Don't specify an AMI ID in [`imageId`](../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-imageId "../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-imageId"), [`imageIdOverride`](../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageIdOverride "../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageIdOverride") (in [`ec2Configuration`](../APIReference/API_Ec2Configuration.md "../APIReference/API_Ec2Configuration.md")), or in the launch template ([`launchTemplate`](../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate "../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate")). When you don't specify an AMI ID, AWS Batch selects
  the latest Amazon ECS optimized AMI that AWS Batch supports at the time the infrastructure update is
  initiated. Alternatively, you can specify the AMI ID in the `imageId` or
  `imageIdOverride` parameters. Or, you can specify the launch template that's
  identified by the `LaunchTemplate` properties. Changing any of these properties
  starts an infrastructure update. If the AMI ID is specified in the launch template, the AMI
  ID can't be replaced by specifying an AMI ID in either the `imageId` or
  `imageIdOverride` parameters. The AMI ID can only be replaced by specifying a
  different launch template. If the launch template version is set to `$Default` or
  `$Latest`, the AMI ID can be replaced by setting either a new default version for
  the launch template (if `$Default`) or by adding a new version to the launch
  template (if `$Latest`).
  If these rules are followed, any update that starts an infrastructure update causes the AMI
  ID to be re-selected. If the [`version`](../APIReference/API_LaunchTemplateSpecification.md#Batch-Type-LaunchTemplateSpecification-version "../APIReference/API_LaunchTemplateSpecification.md#Batch-Type-LaunchTemplateSpecification-version") setting in the launch template ([`launchTemplate`](../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate "../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate")) is set to `$Latest` or `$Default`,
  the latest or default version of the launch template is evaluated up at the time of the
  infrastructure update, even if the [`launchTemplate`](../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate "../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate") wasn't updated.

###### Topics

- [Compute resource AMI specification](batch-ami-spec.md "batch-ami-spec.md")
- [Tutorial: Create a compute resource AMI](create-batch-ami.md "create-batch-ami.md")
- [Use a GPU workload AMI](batch-gpu-ami.md "batch-gpu-ami.md")
- [Amazon Linux deprecation](al1-ami-deprecation.md "al1-ami-deprecation.md")
- [Amazon EKS Amazon Linux 2 AMI deprecation](eks-al2-ami-deprecation.md "eks-al2-ami-deprecation.md")
- [Amazon ECS Amazon Linux 2 AMI deprecation](ecs-al2-ami-deprecation.md "ecs-al2-ami-deprecation.md")
