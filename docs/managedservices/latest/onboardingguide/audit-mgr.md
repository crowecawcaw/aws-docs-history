# Use AMS SSP to provision AWS Audit Manager in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Audit Manager capabilities directly in your AMS managed account. Audit Manager helps you continuously audit your AWS usage to simplify how you assess risk and
compliance with regulations and industry standards. Audit Manager automates evidence collection to
make it easier to assess if your policies, procedures, and activities are operating effectively.
When it is time for an audit, Audit Manager helps you manage stakeholder reviews of your controls and
helps you build audit-ready reports with significantly less manual effort.
To learn more, see [Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/").

## AWS Audit Manager in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS Audit Manager in my AMS account?**

You can request access through the submission of the AWS Services RFC
Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny). This RFC provisions the following IAM role
in your account: `customer-audit-manager-admin-Role`.
After provisioned in your account, you must onboard the role in your federation
solution.

**Q: What are the restrictions to using AWS Audit Manager?**

There are no restrictions for the use of AWS Audit Manager in your AMS account. Full functionality
for AWS Audit Manager is provided.

**Q: What are the prerequisites or dependencies to using AWS Audit Manager?**

1. You need to provide AMS with the s3 bucket where you want reports/assessments
   to reside.
2. If you want to have encryption with the service, you need to provide AMS with the
   KMS CMK ARN to use.
3. If you want to send an SNS notifications to a Topic, you must provide the name of
   the topic or arn.
4. **(Optional)** There is an additional prerequisite if you want to
   enable Organizations as part of your multi-account landing zone in Audit Manager and you want a delegated
   administrator account: In the description field for RFC (Management | AWS service |
   Compatible Service| Add), mention that you want to use the delegated administrator account
   as part of Audit Manager Setup and provide the below details:
   - KMS CMK ARN (used to set up Audit Manager, initially)
   - Delegated administrator account ID for Audit Manager to use as part of this multi-account landing zone (can be a
     MALZ application account)
