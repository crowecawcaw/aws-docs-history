# Security in AWS Secrets Manager

Security at AWS is the highest priority. As an AWS customer, you benefit from a data
center and network architecture built to meet the requirements of the most security-sensitive
organizations.

You and AWS share the responsibility for security. The [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security of the cloud and security in the cloud:

- **Security of the cloud** – AWS is responsible for
  protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides
  you with services you can use securely. Third-party auditors regularly test and verify the
  effectiveness of our security as part of the [AWS Compliance Programs.](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/") To
  learn about the compliance programs that apply to AWS Secrets Manager, see [AWS Services in Scope by
  Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your AWS service determines
  your responsibility. You are also responsible for other factors including the sensitivity of
  your data, your company’s requirements, and applicable laws and regulations.
  For more resources, see [Security Pillar – AWS
  Well-Architected Framework](../../../wellarchitected/latest/security-pillar/welcome.md "../../../wellarchitected/latest/security-pillar/welcome.md").

###### Topics

- [Mitigate the risks of using the AWS CLI
  to store your AWS Secrets Manager secrets](security_cli-exposure-risks.md "security_cli-exposure-risks.md")
- [Authentication and access control for AWS Secrets Manager](auth-and-access.md "auth-and-access.md")
- [Data protection in AWS Secrets Manager](data-protection.md "data-protection.md")
- [Secret encryption and decryption in AWS Secrets Manager](security-encryption.md "security-encryption.md")
- [Infrastructure security in AWS Secrets Manager](infrastructure-security.md "infrastructure-security.md")
- [Using an AWS Secrets Manager VPC endpoint](vpc-endpoint-overview.md "vpc-endpoint-overview.md")
- [Control API access with IAM policies](ip-access.md "ip-access.md")
- [Resiliency in AWS Secrets Manager](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Post-quantum TLS](pqtls.md "pqtls.md")
