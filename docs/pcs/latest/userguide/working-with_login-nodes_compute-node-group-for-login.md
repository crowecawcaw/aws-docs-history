# Using an AWS PCS

compute node group to provide login nodes

This topic provides an overview of suggested configuration options and describes what to
consider when you use an AWS PCS compute node group to provide persistent, interactive access to
your cluster.

## Creating an

AWS PCS compute node group for login nodes

Operationally, this is not much different from creating a regular compute node group.
However, there are some key configuration choices make:

- Set a static scaling configuration of at least one EC2 instance in the compute node
  group.
- Choose on-demand purchase option to avoid having your instance(s) reclaimed.
- Choose an informative name for the compute node group, such as login.
- If you want the login node instance(s) to be accessible outside your VPC, consider using
  a public subnet.
- If you intend to allow SSH access, the launch template will need have a security group
  that exposes the SSH port to your choice of IP addresses.
- The IAM instance profile should have only the AWS permissions you want your end users to
  have. See [IAM instance profiles for AWS Parallel Computing Service](security-instance-profiles.md "security-instance-profiles.md") for details.
- Consider allowing AWS Systems Manager Session Manager to manage your login instances.
- Consider restricting access to the instance AWS credentials to only administrative users
- Select less expensive instance types than for regular compute node groups, since the
  login node(s) will be running continuously.
- Use the same (or a derivative) AMI as for your other compute node groups to help ensure
  all instances have the same software installed. For more information about customizing AMIs,
  see [Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md "working-with_ami.md")
- Configure the same network file system (Amazon EFS, Amazon FSx for Lustre, etc.) mounts
  on your login nodes as on your compute instances. For more information, see [Using network file systems with AWS PCS](working-with_file-systems.md "working-with_file-systems.md").

###### Access your login nodes

Once your new compute node group reaches ACTIVE status, you can find the EC2 instance(s)
it has created and log into them. For more information, see [Finding compute node group instances in
AWS PCS](working-with_compute-instances.md "working-with_compute-instances.md").

## Updating an

AWS PCS compute node group for login nodes

You can update a login node group using UpdateComputeNodeGroup. As part of the node group
update process, running instances will be replaced. Note that this will interrupt any active
user sessions or processes on the instance. Running or queued Slurm jobs will be unaffected. For
more information, see [Updating an AWS PCS compute node group](working-with_cng_update.md "working-with_cng_update.md").

You can also edit the launch template used by your compute node group. You must use
UpdateComputeNodeGroup to apply the updated launch template to the compute node group.
New EC2 instances launched in the compute node group use the updated launch template.
For more information, see [Using Amazon EC2 launch templates
with AWS PCS](working-with_launch-templates.md "working-with_launch-templates.md").

## Deleting an

AWS PCS compute node group for login nodes

You can update a login node group using the **delete compute node
group** mechanism in AWS PCS. Running instances will be terminated as part of node
group deletion. Please note that this will interrupt any active user sessions or processes on
the instance. Running or queued Slurm jobs will be unaffected. For more information, see [Deleting a compute node group in AWS PCS](working-with_cng_delete.md "working-with_cng_delete.md").
