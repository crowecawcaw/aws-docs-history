# Managed compute environments

You can use a managed compute environment to have AWS Batch manage the capacity and instance
types of the compute resources within the environment. This is based on the compute resource
specifications that you define when you create the compute environment. You can choose either to
use Amazon EC2 On-Demand Instances and Amazon EC2 Spot Instances. Or, you can alternatively use Fargate
and Fargate Spot capacity in your managed compute environment. When using Spot Instances, you
can optionally set a maximum price. This way, Spot Instances only launch when the Spot Instance
price is under a specified percentage of the On-Demand price.

###### Important

Fargate Spot instances are not supported on Windows containers on AWS Fargate. A job queue will be blocked
if a FargateWindows job is submitted to a job queue that only uses Fargate Spot compute
environments.

###### Important

AWS Batch creates and manages multiple AWS resources on your behalf and within your
account, including Amazon EC2 Launch Templates, Amazon EC2 Auto Scaling Groups, Amazon EC2 Spot Fleets, and Amazon ECS
Clusters. These managed resources are configured specifically to ensure optimal AWS Batch
operation. Manually modifying these Batch-managed resources, unless explicitly stated in AWS Batch
documentation, may result in unexpected behavior resulting in `INVALID` Compute Environment,
suboptimal instance scaling behavior, delayed workload processing, or unexpected costs. These
manual modifications can not be deterministically supported by the AWS Batch service. Always use
the supported Batch APIs or the Batch console to manage your Compute Environments.

Managed compute environments launch Amazon EC2 instances into the VPC and subnets that you
specify and then registers them with an Amazon ECS cluster. The Amazon EC2 instances need external network
access to communicate with the Amazon ECS service endpoint. Some subnets don't provide Amazon EC2 instances
with public IP addresses. If your Amazon EC2 instances don't have a public IP address, they must use
network address translation (NAT) to gain this access. For more information, see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
_Amazon VPC User Guide_. For more information about how to create a VPC, see [Create a virtual private cloud](create-public-private-vpc.md "create-public-private-vpc.md") .

By default, AWS Batch managed compute environments use a recent, approved version of the Amazon ECS
optimized AMI for compute resources. However, you might want to create your own AMI to use
for your managed compute environments for various reasons. For more information, see [Compute resource AMIs](compute_resource_AMIs.md "compute_resource_AMIs.md").

###### Note

AWS Batch doesn't automatically upgrade the AMIs in a compute environment after it's created.
For example, it doesn't update the AMIs in your compute environment when a newer version of the
Amazon ECS optimized AMI is released. You're responsible for the management of the guest operating
system. This includes any updates and security patches. You're also responsible for any
additional application software or utilities that you install on the compute resources. There
are two ways to use a new AMI for your AWS Batch jobs. The original method is to complete these
steps:

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
  `SPOT_CAPACITY_OPTIMIZED` or `SPOT_PRICE_CAPACITY_OPTIMIZED`.
- Set the update to latest image version ([`updateToLatestImageVersion`](../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-updateToLatestImageVersion "../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-updateToLatestImageVersion")) parameter to `true`.
- Don't specify an AMI ID in [`imageId`](../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-imageId "../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-imageId"), [`imageIdOverride`](../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageIdOverride "../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageIdOverride") (in [`ec2Configuration`](../APIReference/API_Ec2Configuration.md "../APIReference/API_Ec2Configuration.md")), or in the launch template ([`launchTemplate`](../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate "../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate")). In that case, AWS Batch selects the latest Amazon ECS
  optimized AMI that's supported by AWS Batch at the time the infrastructure update is initiated.
  Alternatively, you can specify the AMI ID in the `imageId` or
  `imageIdOverride` parameters, or the launch template identified by the
  `LaunchTemplate` properties. Changing any of these properties starts an
  infrastructure update. If the AMI ID is specified in the launch template, it can't be replaced
  by specifying an AMI ID in either the `imageId` or `imageIdOverride`
  parameters. It can only be replaced by specifying a different launch template. Or, if the
  launch template version is set to `$Default` or `$Latest`, by setting
  either a new default version for the launch template (if it's `$Default`) or by
  adding a new version to the launch template (if it's `$Latest`).
  If these rules are followed, any update that starts an infrastructure update will cause the
  AMI ID to be re-selected. If the [`version`](../APIReference/API_LaunchTemplateSpecification.md#Batch-Type-LaunchTemplateSpecification-version "../APIReference/API_LaunchTemplateSpecification.md#Batch-Type-LaunchTemplateSpecification-version") setting in the launch template ([`launchTemplate`](../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate "../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate")) is set to `$Latest` or `$Default`,
  the latest or default version of the launch template are evaluated up at the time of the
  infrastructure update, even if the [`launchTemplate`](../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate "../APIReference/API_ComputeResourceUpdate.md#Batch-Type-ComputeResourceUpdate-launchTemplate") was not updated.

## Consideration when creating multi-node

parallel jobs

AWS Batch recommends creating dedicated compute environments for running multi-node parallel
(MNP) jobs and non-MNP jobs. This is due to the way compute capacity is created in your managed
compute environment. When creating a new managed compute environment, if you specify a
`minvCpu` value greater than zero then AWS Batch creates an instance pool for use with
non-MNP jobs only. If a multi-node parallel job is submitted, AWS Batch creates new instance
capacity to run the multi-node parallel jobs. In cases where there are both single-node and
multi-node parallel jobs running in the same compute environment where either a
`minvCpus` or `maxvCpus` value is set, if the required compute resources
are unavailable AWS Batch will wait for the current jobs to finish before creating the compute
resources necessary to run the new jobs.
