# Savings Plans types

AWS offers three types of Savings Plans: Compute Savings Plans, EC2 Instance Savings Plans, and SageMaker AI Savings Plans.

- **Compute Savings Plans** provide the most flexibility and prices that are up to
  66 percent off of On-Demand rates. These plans automatically apply to your EC2 instance usage,
  regardless of instance family (for example, m5, c5, etc.), instance size (for example,
  c5.large, c5.xlarge, etc.), Region (for example, us-east-1, us-east-2, etc.), operating system
  (for example, Windows, Linux, etc.), or tenancy (for example, Dedicated, default, Dedicated
  Host). They also apply to your Fargate and Lambda usage. With Compute Savings Plans, you can move a
  workload from c5 to m5, shift your usage from EU (Ireland) to EU (London), or migrate your
  application from Amazon EC2 to Amazon ECS using Fargate at any time. You can continue to benefit from
  the low prices provided by Compute Savings Plans as you make these changes.
- **EC2 Instance Savings Plans** provide savings up to 72 percent off
  On-Demand, in exchange for a commitment to a specific instance family in a chosen AWS Region
  (for example, m5 in Virginia). These plans automatically apply to usage regardless of instance
  size (for example, m5.xlarge, m5.2xlarge, etc.), OS (for example, Windows, Linux, etc.), and
  tenancy (Host, Dedicated, Default) within the specified family in a Region.

With an EC2 Instance Savings Plan, you can change your instance size within the instance
type (for example, from c5.xlarge to c5.2xlarge) or the operating system (for example, from
Windows to Linux), or move from Dedicated tenancy to Default and continue to receive the
discounted rate provided by your EC2 Instance Savings Plan.

- **SageMaker AI Savings Plans** provide savings up to 64 percent off of On-Demand rates.
  These plans automatically apply to your SageMaker AI instance usage regardless of instance family (for
  example, ml.m5, ml.c5, etc.), instance sizes (for example ml.c5.large, ml.c5.xlarge, etc.),
  Region (for example, us-east-1, us-east-2, etc.), and component (for example, Notebook,
  Training, etc.).

With SageMaker AI Savings Plans, you can move a workload from ml.c5 to ml.m5, shift your usage from
Europe (Ireland) to Europe (London), or migrate your usage from Training to Inference at
any time and continue to receive benefits.

###### Note

Savings Plans provides low prices in exchange for commitment. The terms of the commitment can't
be changed after purchase. As your usage changes, you can sign up for additional Savings Plans.

Dedicated Instances are charged $2/hour in every Region you have at least
one Dedicated Instance running. These dedicated fees are not discounted by Savings Plans.

Both Compute and EC2 Instance plan types apply to EC2 instances that are a part of Amazon EMR,
Amazon EKS, and Amazon ECS clusters. Amazon EKS charges will not be covered by Savings Plans, but the underlying EC2
instances will be.
