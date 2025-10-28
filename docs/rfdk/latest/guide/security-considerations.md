# Security in the RFDK

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

Cloud security at Amazon Web Services (AWS) is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to
meet the requirements of the most security-sensitive organizations. Security is a shared responsibility between AWS and you. The
[Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as Security of the Cloud and Security in the Cloud.

**Security of the Cloud** – AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud and providing you with services that
you can use securely. Our security responsibility is the highest priority at AWS, and the effectiveness of our security is regularly tested and verified by third-party auditors
as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").

**Security in the Cloud** – Your responsibility is determined by the AWS service you are using, and other factors including the sensitivity of your data, your organization’s
requirements, and applicable laws and regulations.

The RFDK follows the shared responsibility model and compliance is shared between AWS and you. RFDK is designed and developed with a security-first approach. Ultimately, the
CDK and RFDK are both SDKs which are intended to be used as building blocks for deploying infrastructure that meets a range of diverse requirements. When building an RFDK
application, it is up to you to follow security best practices to ensure that the resulting deployed render farm is secure.

###### Important

It is highly recommended that you read and familiarize yourself with the
[Security Pillar of the AWS Well-Architected Framework](https://d1.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf "https://d1.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf"). This article contains key principles to securing
your AWS infrastructure.

###### In this section:

- [Additional Readings](#additional-readings "#additional-readings")
- [Data protection in the RFDK](security-data-protection.md "security-data-protection.md")
- [Identity and access management in the RFDK](security-iam.md "security-iam.md")
- [Infrastructure security in the RFDK](security-infrastructure.md "security-infrastructure.md")
- [Deadline Secrets Management in the RFDK](deadline-secrets-management-rfdk.md "deadline-secrets-management-rfdk.md")
- [Security best practices for the RFDK](security-best-practice.md "security-best-practice.md")

## Additional Readings

- [Security Pillar - AWS Well-Architected Framework](https://d1.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf "https://d1.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf")
- [Security for the AWS Cloud Development Kit (AWS CDK)](../../../cdk/latest/guide/security.md "../../../cdk/latest/guide/security.md")
- [Security in Amazon Virtual Private Cloud](../../../vpc/latest/userguide/security.md "../../../vpc/latest/userguide/security.md")
- [AWS security credentials](../../../general/latest/gr/aws-security-credentials.md "../../../general/latest/gr/aws-security-credentials.md")
- Security in Amazon EC2
  - [Linux](../../../AWSEC2/latest/UserGuide/ec2-security.md "../../../AWSEC2/latest/UserGuide/ec2-security.md")
  - [Windows](../../../AWSEC2/latest/WindowsGuide/ec2-security.md "../../../AWSEC2/latest/WindowsGuide/ec2-security.md")
