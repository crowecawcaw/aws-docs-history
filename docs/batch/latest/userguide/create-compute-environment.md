# Create a compute environment

Before you can run jobs in AWS Batch, you need to create a compute environment. You can create
a managed compute environment where AWS Batch manages the Amazon EC2 instances or AWS Fargate resources
within the environment based on your specifications. Or, alternatively, you can create an
unmanaged compute environment where you handle the Amazon EC2 instance configuration within the
environment.

###### Important

Fargate Spot instances are not supported in the following scenarios:

- Windows containers on AWS Fargate
  A job queue will be blocked in these scenarios if a job is submitted to a job queue that
  only uses Fargate Spot compute environments.

###### Topics

- [Tutorial: Create a managed compute
  environment using Fargate resources](create-compute-environment-fargate.md "create-compute-environment-fargate.md")
- [Tutorial: Create a managed compute
  environment using Amazon EC2 resources](create-compute-environment-managed-ec2.md "create-compute-environment-managed-ec2.md")
- [Tutorial: Create an unmanaged
  compute environment using Amazon EC2 resources](create-compute-environment-unmanaged-ec2.md "create-compute-environment-unmanaged-ec2.md")
- [Tutorial: Create a managed compute
  environment using Amazon EKS resources](create-compute-environment-managed-eks.md "create-compute-environment-managed-eks.md")
- [Resource: Compute environment template](compute-environment-template.md "compute-environment-template.md")
- [Instance type compute table](instance-type-compute-table.md "instance-type-compute-table.md")
