# Use AMS SSP to provision AWS Security Hub CSPM in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Security Hub CSPM capabilities directly in your AMS managed account. AWS Security Hub CSPM provides you with a comprehensive view of your security state within AWS and your compliance with
security industry standards and best practices.
Security Hub CSPM centralizes and prioritizes security and compliance findings from across AWS accounts, services, and supported
third-party partners to help you
analyze your security trends and identify the highest priority security issues.
To learn more, see [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/").

## Security Hub CSPM in AWS Managed Services FAQ

**Q: How do I request access to AWS Security Hub CSPM in my AMS account?**

Request access to Security Hub CSPM by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account:
`customer_securityhub_role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Security Hub CSPM in my AMS account?**

Archiving functionality has been noted as a potential security and operational risk and
has been restricted as a part of the self-provisioned service Security role.

**Q: What are the prerequisites or dependencies to using AWS Security Hub CSPM in my AMS account?**

There are no prerequisites or dependencies to use AWS Security Hub CSPM in your AMS account.
