

# FND02-BP08 Audit and rotate credentials periodically

 Audit and rotate credentials on a regular schedule to limit how long they can be used to access your resources. Use temporary credentials when possible, and rotate risky long-term credentials regularly. 

 **Desired outcome:** 
+  You have implemented credential rotation to help reduce the risks associated with long-term credential usage. 
+  You regularly audit and remediate non-compliance with credential rotation policies. 
+  Your organization uses temporary credentials by default, with long-term credentials reserved as documented exceptions that have explicit justification. 
+  You have identified and removed unused or unnecessary credentials through periodic audits, reducing the attack surface across your environment. 

 **Common anti-patterns:** 
+  Not auditing credential use. 
+  Using long-term credentials unnecessarily. 
+  Using long-term credentials and not rotating them regularly. 

 **Benefits of establishing this best practice:** 
+  Reduced window of exposure if credentials are disclosed, through regular credential auditing and rotation. 
+  Lower risk of unauthorized access from disclosed credentials by preferring temporary credentials and rotating long-term credentials regularly. 
+  Smaller surface area through periodic audits that identify unused or unnecessary credentials and remove them. 
+  Stronger compliance posture in meeting security standards that mandate regular credential reviews and rotation policies. 
+  Better visibility into credential usage patterns, so teams can detect anomalous behavior. 
+  Lower operational overhead through automated credential management and rotation, which improves consistency and reduces human error in credential lifecycle management. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Long-term credentials (IAM user access keys, passwords, and service account keys) accumulate over time and become difficult to inventory and control. When these credentials are disclosed, they give an unauthorized party persistent access until they are rotated or revoked. The longer a credential exists, the higher the probability it has been disclosed through a security incident, inadvertent disclosure, or insider threat. 

 Remove long-term credentials wherever possible by replacing them with temporary credentials that expire automatically. Temporary credentials reduce risk because they have a built-in expiration: even if disclosed, they become unusable after a short period. AWS provides multiple mechanisms for temporary credentials: [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html), [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html), and [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html). Reserve long-term credentials as documented exceptions with explicit justification, and review the [alternatives to long-term access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html#security-creds-alternatives-to-long-term-access-keys) before accepting the risk of persistent credentials. 

 When long-term credentials cannot be removed (for legacy applications, third-party integrations, or on-premises systems that lack support for temporary credentials), rotate them regularly and audit them continuously. Rotation limits the window of exposure: if a credential is disclosed without your knowledge, rotation makes sure that it becomes invalid within a defined period (typically 90 days or less). Auditing reveals usage patterns, identifies credentials no longer needed, and detects anomalous behavior that might indicate unauthorized use. Long-term credential audits also verify that defined controls (source IP address restrictions, MFA requirements, and organization ID conditions) remain enforced over time. 

 Use automated tooling to validate that credential controls remain enforced. For human identities, rotate passwords and replace access keys with temporary credentials to narrow the window of exposure when credentials are disclosed. As organizations move from IAM users to centralized identities, use a [credential report](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) to audit remaining IAM users. Enforce and monitor MFA in the identity provider, and use [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) or [AWS Security Hub CSPM IAM controls](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html) to catch users who fail to configure MFA even when policy requires it. 

 The most common failure mode is credential sprawl: long-term credentials created for specific purposes but never retired when those purposes end. Developers leave the organization, temporary projects become permanent, and credentials accumulate in CI/CD systems, configuration files, and local machines. Without systematic auditing, these orphaned credentials remain active indefinitely. Another pitfall is completing rotation on schedule but failing to verify that old credentials are invalidated and that dependent systems have updated to the new credentials. 

 For machine identities, use [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) instead of long-term access keys. With X.509 certificates issued by a trusted certificate authority, on-premises servers and workloads outside AWS can obtain temporary credentials without storing long-term secrets. You then manage certificate lifecycle instead of static access keys, using mature PKI tooling and processes. Use [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) to rotate database credentials, API keys, and other secrets without manual intervention. Configure alerts on rotation failures so that operations teams can intervene before credentials exceed policy thresholds. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Regularly audit credentials:** Audit the identities configured in your identity provider and [AWS IAM](https://aws.amazon.com/iam/) to verify that only authorized identities have access to your workload. Remove people that leave the organization, and remove cross-account roles no longer required. Have a process to periodically audit permissions to the services accessed by an IAM entity to identify policies that need modification to remove unused permissions. Use [credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) and [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to audit IAM credentials and permissions. Use [Amazon CloudWatch to set up alarms for specific API calls](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html) and [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html) to alert on unexpected activity that might indicate overly permissive access or unintended access to credentials. 

1.  **Evaluate long-term credentials for migration to temporary credentials:** As part of each audit cycle, evaluate whether existing long-term credentials can be replaced with temporary credentials. Long-term credentials are often introduced for legacy applications or third-party integrations that did not support temporary credentials at initial setup. As these systems are updated or replaced, they might gain support for IAM roles, [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html), or other temporary credential mechanisms. Establish a regular review cadence (for example, quarterly) to reassess each long-term credential and migrate to short-term credentials where possible. 

1.  **Rotate credentials regularly:** When you are unable to use temporary credentials, rotate long-term IAM access keys regularly (maximum every 90 days). If an access key is unintentionally disclosed without your knowledge, this limits how long the credentials can be used. For information about rotating access keys for IAM users, see [Update access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html). 

1.  **Verify that defined controls are enforced:** Use automated tooling to continuously validate that credential hygiene controls remain in place. A one-time configuration is not enough. Deploy [AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) such as iam-user-mfa-enabled and access-keys-rotated to flag non-compliant resources. Enable the relevant [AWS Security Hub CSPM controls for AWS Identity and Access Management](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html) to aggregate findings across accounts. Verify that supplementary controls such as source IP restrictions, MFA requirements, and aws:PrincipalOrgID conditions on long-term credentials remain enforced over time. 

1.  **Automate credential rotation:** Use [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) to automate rotation of database credentials, API keys, and other secrets so that rotation occurs on a defined schedule without manual intervention. Configure alerts on rotation failures so that operations teams can intervene before credentials exceed policy thresholds. 

1.  **Use IAM Roles Anywhere for machine identities:** Use [AWS IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) to provide temporary credentials for machine identities in areas where you traditionally could not use IAM roles, such as on-premises servers. AWS IAM Roles Anywhere uses a trusted [X.509 certificate](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/trust-model.html#signature-verification) to authenticate to AWS and receive temporary credentials, removing the need to store long-term credentials in your on-premises environment. Monitor and rotate the X.509 certificate as it approaches expiration. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND02-BP09 Establish a process to continually review and refine permissions](fnd02-bp09.md) 
+  [FND02-BP10 Establish workload and machine identity federation](fnd02-bp10.md) 
+  [FND05-BP11 Establish encryption and key management standards](fnd05-bp11.md) 
+  [SEC02-BP03 Store and use secrets securely](sec02-bp03.md) 

 **Related documents:** 
+  [Get started with Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html#get-started) 
+  [Security best practices in IAM - Rotate access keys regularly](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials) 
+  [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) 
+  [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) 
+  [Generate credential reports for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) 
+  [Alternatives to long-term access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html#security-creds-alternatives-to-long-term-access-keys) 

 **Related videos:** 
+  [AWS re:Invent 2023 - AWS Secrets Manager: Manage, retrieve, and rotate credentials (SEC235)](https://www.youtube.com/watch?v=3xPOTlHOZKo) 
+  [AWS re:Invent 2023 - Managing identity, access, and authorization with IAM and IAM Identity Center (SEC231)](https://www.youtube.com/watch?v=BqnKSRAZBek) 