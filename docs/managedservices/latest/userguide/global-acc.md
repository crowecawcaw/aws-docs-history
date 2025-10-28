# Use AMS SSP to provision AWS Global Accelerator in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Global Accelerator capabilities directly in your AMS managed account. Global Accelerator is a network layer service in which you create accelerators to improve availability
and performance for internet applications used by a global audience. To learn more, see
[Global Accelerator](https://aws.amazon.com/global-accelerator/ "https://aws.amazon.com/global-accelerator/").

## Global Accelerator in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request Global Accelerator to be set up in my AMS account?**

Request access through the submission of the AWS Services RFC (Management |
AWS service | Self-provisioned Service). Through this RFC, the following IAM roles will be
provisioned in your account: `customer_global_accelerator_console_role`.
Once provisioned in your account you must onboard the console role in your federation
solution.

**Q: What are the restrictions to using Global Accelerator in my AMS account?**

Global Accelerator is a global service that supports endpoints in multiple AWS Regions, which
are listed in the
[AWS Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

**Q: What are the prerequisites or dependencies to using Global Accelerator in my AMS account?**

When you set up your accelerator with Global Accelerator, you associate the static IP addresses
to regional endpoints in one or more AWS Regions. For standard accelerators, the endpoints
are Network Load Balancers, Application Load Balancers, Amazon EC2 instances, or Elastic
IP addresses. For custom routing accelerators, endpoints are virtual private cloud (VPC)
subnets with one or more EC2 instances.
