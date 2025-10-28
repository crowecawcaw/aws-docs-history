# Use AMS SSP to provision AWS License Manager in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS License Manager capabilities directly in your AMS managed account. AWS License Manager integrates with AWS services to simplify the management of licenses across multiple AWS accounts, IT
catalogs, and on-premises, through a single AWS account.
AWS License Manager lets administrators create customized licensing rules that emulate the terms of their licensing agreements,
and then enforces these rules when an instance of Amazon EC2 gets launched.
The rules in AWS License Manager enable you to limit a licensing breach by physically stopping the instance from launching or by
notifying administrators about the infringement.
To learn more, see [AWS License Manager](https://aws.amazon.com/license-manager/ "https://aws.amazon.com/license-manager/").

## License Manager in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request AWS License Manager to be set up in my AMS account?**

Request access to AWS License Manager by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account: `customer_license_manager_role`.
Once the License Manager IAM role is provisioned in your account, you must onboard the role in your federation
solution.

**Q: What are the restrictions to using AWS License Manager in my AMS account?**

You're able to associate AWS License Manager rules to the AMIs you own (filtered
under "Owned by me"). If you choose to enforce a limit association to an AMI
(example: can only support 100 vCPU of this AMI) and exhaust the limit,
future launches with that AMI are blocked and return an error stating "No
licenses available." This is the intended behavior of this service (not
allowing license exhaustion). In the event you exhaust the limit but need to
launch the AMI again, you must modify the rule configured in
AWS License Manager.

**Q: What are the prerequisites or dependencies to using AWS License Manager in my AMS account?**

There are no prerequisites or dependencies to use AWS License Manager in your AMS account.
