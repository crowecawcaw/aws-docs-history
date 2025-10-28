# Use AMS SSP to provision AWS Batch in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Batch capabilities directly in your AMS managed account. AWS Batch enables developers, scientists, and engineers to easily and efficiently run hundreds
of thousands of batch computing jobs on AWS. AWS Batch dynamically provisions the optimal
quantity and type of compute resources (such as CPU or memory optimized instances) based on
the volume and specific resource requirements of the batch jobs submitted. With AWS Batch, there
is no need to install and manage batch computing software or server clusters that you use to run
your jobs, allowing you to focus on analyzing results and solving problems.
To learn more, see [AWS Batch](https://aws.amazon.com/batch/ "https://aws.amazon.com/batch/").

## AWS Batch in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS Batch in my AMS account?**

1.

To request access to AWS Batch, submit the RFC
Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct). This RFC provisions the following IAM roles
and policies in your account:

IAM roles:

- `customer_batch_console_role`
- `customer_batch_ecs_instance_role`
- `customer_batch_events_service_role`
- `customer_batch_service_role`
- `customer_batch_ecs_task_role`

Policies:

- `customer_batch_console_role_policy`
- `customer_batch_service_role_policy`
- `customer_batch_events_service_role_policy`

2. After provisioned in your account, you must onboard the role
   `customer_batch_console_role` in your federation solution.

**Q: What are the restrictions to using AWS Batch?**

When creating the Compute Environment, you should tag EC2 instances as
"customer_batch" or "customer-batch". If the instances are not tagged, instances will not be
terminated by batch when the job completes.

**Q: What are the prerequisites or dependencies to using AWS Batch?**

There are no prerequisites or dependencies to use AWS Batch in your AMS account.
