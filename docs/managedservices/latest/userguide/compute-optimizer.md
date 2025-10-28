# Use AMS SSP to provision AWS Compute Optimizer in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Compute Optimizer capabilities directly in your AMS managed account. AWS Compute Optimizer recommends optimal AWS Compute resources for your workloads to reduce costs and improve performance
by using machine learning to analyze historical utilization metrics.
Over-provisioning compute (Amazon EC2 and ASGs) can lead to unnecessary infrastructure cost and under-provisioning
compute can lead to poor application performance. Compute Optimizer helps you choose
the optimal Amazon EC2 instance types, including those that are part of an Amazon EC2 Auto Scaling group,
based on your utilization data.
To learn more, see [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/").

## Compute Optimizer in AWS Managed Services FAQ

**Q: How do I request access to Compute Optimizer in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account:
`customer_compute_optimizer_readonly_role`. After it's
provisioned in your account, you must onboard the role in your federation
solution.

**Q: What are the restrictions to using Compute Optimizer in my AMS account?**

There are no restrictions. Full functionality of AWS Compute Optimizer is available in your AMS account.

**Q: What are the prerequisites or dependencies to using Compute Optimizer in my AMS account?**

- You must submit an RFC (Management | Other | Other | Update) authorizing AMS Ops to enable the
  service in the account. During deployment, a service linked role (SLR) is created to allow metrics gathering
  and report generation. The SLR is labeled "AWSServiceRoleForComputeOptimizer". For more information, see
  [Using Service-Linked Roles for AWS Compute Optimizer](../../../compute-optimizer/latest/ug/using-service-linked-roles.md "../../../compute-optimizer/latest/ug/using-service-linked-roles.md")
- CloudWatch metrics must be enabled for the following metrics:
  - **CPU utilization**: The percentage of allocated Amazon EC2 compute units that are in use on
    the instance. This metric identiﬁes the processing power
    required to run an application upon a selected instance.
  - **Memory utilization**: The amount of memory that has been used in some way during the
    sample period. This metric identiﬁes the memory required
    to run an application upon a selected instance. Memory utilization is analyzed only for
    resources that have the uniﬁed CloudWatch agent installed on them.
    For more information, see Enabling Memory Utilization with the CloudWatch Agent (p. 10).
  - **Network in**: The number of bytes received on all network
    interfaces by the instance. This metric identiﬁes the volume of incoming network
    traﬃc to a single instance.
  - **Network out**: The number of bytes sent out on all network
    interfaces by the
    instance. This metric identiﬁes the volume of outgoing network
    traﬃc from a single instance.
  - **Local disk input/output (I/O)**: The number of input/output
    operations for the local disk. This metric identiﬁes the performance of the root
    volume of an instance
