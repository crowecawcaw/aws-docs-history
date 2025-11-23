# Security in AWS Backup

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that is built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes
this as security _of_ the cloud and security _in_ the
cloud:

- **Security of the cloud** – AWS is responsible for
  protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also
  provides you with services that you can use securely. Third-party auditors regularly test
  and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the
  compliance programs that apply to AWS Backup, see [AWS Services in Scope by Compliance
  Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility for
  AWS Backup includes, but is not limited to, the following. You are also responsible for other
  factors including the sensitivity of your data, your organization's requirements, and
  applicable laws and regulations.

      + Responding to communications you receive from AWS.
      + Managing the credentials you and your team use. For more information, see [Identity and
       access management in AWS Backup](backup-iam.md "backup-iam.md").
      + Configuring your backup plans and resource assignments to reflect your
       organization’s data protection policies. For more information, see [Managing
       backup plans](getting-started.md "getting-started.md").
      + Regularly testing your ability to find certain recovery points and restore them. For
       more information, see [Working with
       backups](recovery-points.md "recovery-points.md").
      + Incorporating AWS Backup procedures in your organization’s disaster recovery and business
       continuity written procedures. For a start point, see [Getting started with
       AWS Backup](getting-started.md "getting-started.md").
      + Ensuring that your employees are familiar with and have practiced using AWS Backup along
       with your organizational procedures in the event of an emergency. For more information,
       see the [AWS Well-Architected Framework](../../../wellarchitected/latest/framework/welcome.md "../../../wellarchitected/latest/framework/welcome.md").

  This documentation helps you understand how to apply the shared responsibility model when
  using AWS Backup. The following topics show you how to configure AWS Backup to meet your
  security and compliance objectives. You also learn how to use other AWS services that help you
  monitor and secure your AWS Backup resources.

###### Topics

- [Compliance validation](backup-compliance.md "backup-compliance.md")
- [Data protection](data-protection.md "data-protection.md")
- [Identity and access management](backup-iam.md "backup-iam.md")
- [Infrastructure security](infrastructure-security.md "infrastructure-security.md")
- [Integrity](backup-integrity.md "backup-integrity.md")
- [Legal holds](legalhold.md "legalhold.md")
- [Malware protection](malware-protection.md "malware-protection.md")
- [Resilience](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
