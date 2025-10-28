# Security Hub recommendations

###### Note

Security Hub is in preview release and is subject to change.

The following security services in AWS send findings to Security Hub in the OCSF format.
After you enable Security Hub, we recommend enabling these AWS services for additional security.

######

Security Hub CSPM

When you [enable Security Hub CSPM](securityhub-settingup.md "securityhub-settingup.md"), you get a comprehensive view of your security state in AWS.
This helps you assess your environment against security industry standards and best practices.
Although you can get started with Security Hub without enabling Security Hub CSPM, we recommend enabling Security Hub CSPM because Security Hub correlates security signals from Security Hub CSPM to improve your posture management.

If you [enable Security Hub CSPM](securityhub-settingup.md "securityhub-settingup.md"), we also recommend [enabling the AWS Foundational Security Best Practices standard](enable-standards.md "enable-standards.md") for your account.
This standard consists of a set of controls that detect when your AWS accounts and resources deviate from security best practices.
When you enable the AWS Foundational Security Best Practices standard for your account, AWS Security Hub CSPM automatically enables all of its controls, including controls for the following resource types:

- Account controls
- Amazon DynamoDB controls
- Amazon Elastic Compute Cloud controls
- AWS Identity and Access Management (IAM) controls
- AWS Lambda controls
- Amazon Relational Database Service (Amazon RDS) controls
- Amazon Simple Storage Service controls

You can disable any of the controls in this list.
However, if you disable any of these controls, you cannot receive exposure findings for supported resources.
For information about controls that apply to the AWS Foundational Security Best Practices standard, see [AWS Foundational Security Best Practices v1.0.0 (FSBP) standard](fsbp-standard.md "fsbp-standard.md").

######

GuardDuty

When you [enable GuardDuty](../../../guardduty/latest/ug/guardduty_settingup.md "../../../guardduty/latest/ug/guardduty_settingup.md"), you can view all of your threats and security coverage findings in the dashboard of the Security Hub console.
If you enable GuardDuty, GuardDuty automatically begins sending data to Security Hub in the OCSF format.

######

Amazon Inspector

When you [enable Amazon Inspector](../../../inspector/latest/user/getting_started_tutorial.md "../../../inspector/latest/user/getting_started_tutorial.md"), you can view all of your exposures and security coverage findings in the dashboard of the Security Hub console.
If you enable Amazon Inspector, Amazon Inspector automatically begins sending data to Security Hub in the OCSF format.

We recommend activating Amazon EC2 scanning and Lambda standard scanning.
When you activate Amazon EC2 scanning, Amazon Inspector scans Amazon EC2 instances in your account for package vulnerabilities and network reachability issues.
When you activate Lambda standard scanning, Amazon Inspector scans Lambda functions for software vulnerabilities in package dependencies.
For more information, see [Activating a scan type](../../../inspector/latest/user/activate-scans.md "../../../inspector/latest/user/activate-scans.md") in the _Amazon Inspector User Guide_.

######

Macie

When you [enable Macie](../../../macie/latest/user/getting-started.md "../../../macie/latest/user/getting-started.md"), you can detect additional exposures for your Amazon S3 buckets.
We recommend configuring [automated sensitive data discovery](../../../macie/latest/user/discovery-asdd-account-enable.md "../../../macie/latest/user/discovery-asdd-account-enable.md"), so Macie can evaluate your Amazon S3 bucket inventory on a daily basis.
