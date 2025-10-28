# Get started with AWS Parallel Computing Service

This is a tutorial to create a simple cluster that you can use to try AWS PCS.
The following figure shows the design of the cluster.

![An architecture diagram of the tutorial cluster: The 2 compute node groups are resources in your AWS account and connect to the Slurm cluster controller that runs in a service-owned AWS account. The EC2 instances in both compute node groups connect to shared storage in Amazon EFS and Amazon FSx for Lustre.](images/aws-pcs-tutorial-environment-diagram.png)
The tutorial cluster design has the following key components:

- A VPC and subnets that meet [AWS PCS networking requirements](working-with_networking_vpc-requirements.md "working-with_networking_vpc-requirements.md").
- An Amazon EFS file system, which will be used as a shared home directory.
- An Amazon FSx for Lustre file system, which provides a shared high performance
  directory.
- An AWS PCS cluster, which provides a Slurm controller.
- 2 AWS PCS compute node groups.
  - The `login` node group, which provides shell-based interactive access to the system.
  - The `compute-1` node group provides elastically-scaling instances to run jobs.

- 1 queue that sends jobs to EC2 instances in the `compute-1` node group.
  The cluster requires additional AWS resources, such as security groups, IAM roles, and
  EC2 launch templates, which aren't shown in the diagram.

###### Note

We recommend that you complete the command line steps in this topic in a Bash shell. If
you aren't using a Bash shell, some script commands such as line continuation characters and
the way variables are set and used require adjustment for your shell. Additionally, the quoting
and escaping rules for your shell might be different. For more information, see [Quotation marks and literals with strings in the AWS CLI](../../../cli/latest/userguide/cli-usage-parameters-quoting-strings.md "../../../cli/latest/userguide/cli-usage-parameters-quoting-strings.md") in the _AWS Command Line Interface
User Guide for Version 2_.

###### Topics

- [Prerequisites for getting started with AWS PCS](getting-started_prerequisites.md "getting-started_prerequisites.md")
- [Using AWS CloudFormation with the AWS PCS tutorial](getting-started_cfn-note.md "getting-started_cfn-note.md")
- [Create a VPC and subnets for AWS PCS](getting-started_create-vpc.md "getting-started_create-vpc.md")
- [Create security groups for AWS PCS](getting-started_create-sg.md "getting-started_create-sg.md")
- [Create a cluster in AWS PCS](getting-started_create-cluster.md "getting-started_create-cluster.md")
- [Create shared storage for AWS PCS in Amazon Elastic File System](getting-started_create-efs.md "getting-started_create-efs.md")
- [Create shared storage for AWS PCS in Amazon FSx for Lustre](getting-started_create-fsx.md "getting-started_create-fsx.md")
- [Create compute node groups in AWS PCS](getting-started_create-cng.md "getting-started_create-cng.md")
- [Create a queue to manage jobs in AWS PCS](getting-started_create-queue.md "getting-started_create-queue.md")
- [Connect to your AWS PCS cluster](getting-started_connect.md "getting-started_connect.md")
- [Explore the cluster environment in AWS PCS](getting-started_explore.md "getting-started_explore.md")
- [Run a single node job in AWS PCS](getting-started_run-job.md "getting-started_run-job.md")
- [Run a multi-node MPI job with Slurm in AWS PCS](getting-started_run-mpi-job.md "getting-started_run-mpi-job.md")
- [Delete your AWS resources for AWS PCS](getting-started_delete.md "getting-started_delete.md")
