# Compute environment considerations for MNP with AWS Batch

There are several things to consider when configuring compute environments to run multi-node parallel jobs with
AWS Batch.

- Multi-node parallel jobs aren't supported on `UNMANAGED` compute
  environments.
- If you want to submit multi-node parallel jobs to a compute environment, create a
  _cluster_ placement group in a single Availability Zone and associate it
  with your compute resources. This keeps your multi-node parallel jobs on a logical grouping of
  instances close with high network flow potential. For more information, see [Placement Groups](../../../AWSEC2/latest/UserGuide/placement-groups.md "../../../AWSEC2/latest/UserGuide/placement-groups.md") in the
  _Amazon EC2 User Guide_.
- Multi-node parallel jobs aren't supported on compute environments that use Spot
  Instances.
- AWS Batch multi-node parallel jobs use the Amazon ECS `awsvpc` network mode, which
  gives your multi-node parallel job containers the same networking properties as Amazon EC2
  instances. Each multi-node parallel job container gets its own elastic network interface, a
  primary private IP address, and an internal DNS hostname. The network interface is created in
  the same VPC subnet as its host compute resource.
- Your compute environment might have no more than five security groups associated with it.
  The elastic network interfaces that are created and attached to an MNP task will use the
  security groups specified in your compute environment, If you don't specify a security group,
  the default security group for the VPC is used.
- The `awsvpc` network mode doesn't provide the elastic network interfaces for
  multi-node parallel jobs with public IP addresses. To access the internet, your compute
  resources must be launched in a private subnet that is configured to use a NAT gateway. For
  more information, see [NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in
  the _Amazon VPC User Guide_. Inter-node communication must use the private IP
  address or DNS hostname for the node. Multi-node parallel jobs that run on compute resources
  within public subnets don't have outbound network access. To create a VPC with private subnets
  and a NAT gateway, see [Create a virtual private cloud](create-public-private-vpc.md "create-public-private-vpc.md") .
- The elastic network interfaces that are created and attached to your compute resources
  can't be detached manually or modified by your account. This is to prevent the accidental
  deletion of an elastic network interface that's associated with a running job. To release the
  elastic network interfaces for a task, terminate the job.
- Your compute environment must have enough maximum vCPUs to support your multi-node parallel job.
- Your Amazon EC2 instance quota include the number of instances that's required to run your job.
  For example, suppose that your job requires 30 instances, but your account can only run 20
  instances in a Region. Then, your job will get stuck in `RUNNABLE` status.
- If you specify an instance type for a node group in a multi-node parallel job, your
  compute environment must launch that instance type.
