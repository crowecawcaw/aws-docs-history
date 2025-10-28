# Use AMS SSP to provision AWS Outposts in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Outposts capabilities directly in your AMS managed account. AWS Outposts is a fully managed service that extends AWS infrastructure, AWS services, APIs, and tools to virtually
any datacenter, co-location space, or on-premises facility for a consistent hybrid experience.
AWS Outposts is good for workloads that require low latency access to on-premises systems, local data processing,
or local data storage.
To learn more, see [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

## AWS Outposts in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request AWS Outposts to be set up in my AMS account?**

Request access to AWS Outposts by submitting an RFC with the Management | AWS service | Self-provisioned
service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account: `customer_outposts_role`.
Once the role is provisioned in your account, you must onboard it in your
federation solution.

**Q: What are the restrictions to using AWS Outposts in my AMS account?**

There are no restrictions for the use of AWS Outposts in your AMS account.

**Q: What are the prerequisites or dependencies to using AWS Outposts in my AMS account?**

There are no prerequisites or dependencies to use AWS Outposts in your AMS account.
