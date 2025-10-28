# Use AMS SSP to provision AWS Resilience Hub in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Resilience Hub capabilities directly in your AMS managed account. AWS Resilience Hub helps you proactively prepare and protect your AWS applications from disruptions. The Resilience Hub offers resiliency assessment and validation that integrate into your software development lifecycle to uncover resiliency weaknesses. Resilience Hub helps you estimate whether or not your applications can meet the recovery time objective (RTO) and recovery point objective (RPO) targets, and helps resolve issues before they are released into production.
After you deploy an AWS application into production, you can use Resilience Hub to continue tracking the resiliency posture of your application. If an outage occurs, Resilience Hub sends a notification to the operator to launch the associated recovery process.

## AWS Resilience Hub in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS Resilience Hub in my AMS account?**

Request access to Resilience Hub by submitting an RFC with the Management | AWS service | Self-provisioned
service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM roles and policies to your account:

###### IAM roles

- `customer_resiliencehub_console_role`
- `customer_resiliencehub_service_role`

###### Policies

- `customer_resiliencehub_console_policy`
- `customer_resiliencehub_service_policy`

After the role is provisioned in your account, you must onboard the role `customer_resiliencehub_console_role` in your
federation solution.

**Q: What are the restrictions to using AWS Resilience Hub in my AMS account?**

There are no restrictions. Full functionality of Resilience Hub is available in your AMS acount.

**Q: What are the prerequisites or dependencies to using AWS Resilience Hub in my AMS account?**

There are no prerequisites or dependencies to use Resilience Hub in your AMS account.
