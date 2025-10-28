# Use AMS SSP to provision Amazon Elastic Container Registry in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Elastic Container Registry (Amazon ECR) capabilities directly in your AMS managed account. Amazon Elastic Container Registry is a fully-managed
[Docker](https://aws.amazon.com/docker/ "https://aws.amazon.com/docker/") container registry that
makes it easy for developers to store, manage, and deploy Docker container images. Amazon ECR is integrated
with [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/"), simplifying your development to production workflow.
Amazon ECR eliminates the need to operate your own container repositories
or worry about scaling the underlying infrastructure. Amazon ECS hosts your images in a highly available and
scalable architecture, allowing you to reliably deploy containers for your applications. Integration with
AWS Identity and Access Management (IAM) provides resource-level control of each repository. With Amazon ECR,
there are no upfront fees or commitments. You pay only for the amount of data you store in your repositories
and data transferred to the Internet.

To learn more, see [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/ "https://aws.amazon.com/ecr/").

## Amazon Elastic Container Registry in AWS Managed Services FAQ

**Q: How do I request access to Amazon ECR in my AMS account?**

Request access to Amazon ECR by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM roles to your account: `customer_ecr_console_role`, and
`customer_ecr_poweruser_instance_profile` with associated IAM policies, `customer_ecr_console_policy` and
`customer_ecr_poweruser_instance_profile_policy`, respectively.
Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon ECR in my AMS account?**

There are restrictions around AMS namespaces for the use of Amazon ECR in your AMS account.
Container images may not be prefixed with "AMS-" or "Sentinel-".

**Q: What are the prerequisites or dependencies to using Amazon ECR in my AMS account?**

There are no prerequisites or dependencies to use Amazon ECR in your AMS account.
