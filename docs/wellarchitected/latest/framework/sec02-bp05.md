

# SEC02-BP05 Audit and rotate credentials periodically

 Some credentials cannot be made temporary, and every long-term credential is a standing risk. The longer it lives, the more chances it has to be inadvertently disclosed, and the longer that disclosure stays useful. Regular auditing confirms that the right controls are in place, and regular rotation caps how long any single credential is valid. 

 **Desired outcome:** 
+  You audit your identities and credentials on a schedule and remediate anything that violates policy. 
+  Your long-term credentials are rotated on a defined maximum interval. 
+  Your required controls, such as multi-factor authentication, are enforced and monitored automatically. 
+  You detect and remove unused identities, permissions, and cross-account roles. 

 **Common anti-patterns:** 
+  Teams never audit how credentials are used. 
+  Teams keep long-term credentials in cases where temporary credentials would work. 
+  Teams hold long-term credentials without rotating them on any schedule. 
+  Teams enforce multi-factor authentication once and never verify that it stays in place. 

 **Benefits of establishing this best practice:** 
+  Rotation limits how long a credential that was inadvertently disclosed but not yet detected remains usable. 
+  Scheduled audits catch stale accounts, unused permissions, and missing controls before they are misused. 
+  Automated MFA checks keep a required control from lapsing. 
+  Credential reports and access analysis give you evidence for compliance reviews. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 This practice applies to the credentials that remain after you have moved as much access as possible to temporary credentials. For credentials that stay, auditing verifies that a credential still has an owner, needs its permissions, and meets required controls such as [multi-factor authentication](https://aws.amazon.com/iam/features/mfa/). Rotation replaces the secret material on a schedule so that an old value, even one that was inadvertently disclosed, stops working. You need both because even well-controlled and freshly rotated credentials can still be exposed or over-permissioned. 

 Manual auditing does not keep pace with change, so automate the checks. A [credential report](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) inventories every IAM user and the state of their passwords and access keys. Use it as a baseline while you migrate users to centralized identities. Rule-based evaluation catches drift as it happens (for example, [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-5) can flag users without MFA). 

 Machine identities are the hardest to rotate, because a static key on an on-premises server has no runtime to refresh it. [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) removes the standing key entirely by exchanging a trusted X.509 certificate for temporary credentials. This shifts the rotation burden from the access key to the certificate, which you still must monitor and renew before it expires. Where even that is not possible, audit and rotate keys frequently. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Audit identities and credentials regularly:** Review the identities in your identity provider and IAM so that only authorized principals retain access, and remove leavers and cross-account roles that are no longer needed. Use credential reports and [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to review credentials and permissions. Add [Amazon CloudWatch alarms for specific API calls](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html), and use [Amazon GuardDuty IAM findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html) to surface unexpected credential activity. 

1.  **Rotate long-term credentials on a schedule:** Where temporary credentials are not an option, [rotate long-term access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) at a maximum interval, such as every 90 days, so an undisclosed exposure has a bounded lifetime. 

1.  **Review IAM permissions against least privilege:** Regularly review each IAM policy and confirm that it grants only the permissions the principal needs. 

1.  **Automate identity resource creation:** Use [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) to automate role and policy management, or define IAM resources in AWS CloudFormation templates that you version-control and review to reduce human error. 

1.  **Replace machine-identity keys with roles:** Use [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) so that on-premises and other external systems authenticate with a trusted [X.509 certificate](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/trust-model.html#signature-verification) and receive temporary credentials. Monitor and renew that certificate before it expires. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC02-BP02 Use temporary credentials](sec02-bp02.md) 
+  [SEC02-BP03 Store and use secrets securely](sec02-bp03.md) 
+  [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md) 

 **Related documents:** 
+  [Getting started with AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) 
+  [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 
+  [IAM identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) 
+  [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) 
+  [Getting credential reports for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) 
+  [Security partner solutions](https://aws.amazon.com/security/partner-solutions/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - A proactive approach to secrets management at scale (SEC234)](https://www.youtube.com/watch?v=vMGYf09XBek) 