

# FND02-BP02 Use strong sign-in mechanisms

 Sign-in credentials are a critical security boundary in any cloud environment. When authentication is weak (missing multi-factor verification, using guessable passwords, or failing to detect suspicious activity), organizations face higher risk of unauthorized access. Strong sign-in mechanisms reduce this risk by requiring multiple forms of verification and enforcing credential quality. 

 **Desired outcome:** 
+  You have implemented multi-factor authentication (MFA) for all human identities accessing AWS, including root users, IAM users, IAM Identity Center users, and any third-party identity provider integrations. 
+  Your organization enforces strong password policies that require sufficient length and complexity while allowing users to manage their own credentials securely. 
+  You have enabled detective controls that identify suspicious sign-in patterns and anomalous authentication behavior across all identity sources. 
+  Your authentication requirements align with established security frameworks such as NIST 800-63 and meet or exceed your organization's security and compliance standards. 

 **Common anti-patterns:** 
+  Allowing human identities to authenticate without multi-factor authentication, creating single points of failure when credentials are exposed. 
+  Enforcing weak password policies that permit short passwords or lack complexity requirements, leaving credentials susceptible to guessing or brute-force attempts. 
+  Sharing credentials among multiple users instead of creating individual identities, which removes accountability and audit capability. 
+  Deploying authentication mechanisms without detective controls to identify suspicious sign-in behavior or credential misuse. 
+  Applying inconsistent authentication standards across different identity sources, creating security gaps where unauthorized parties can target the weakest authentication path. 

 **Benefits of establishing this best practice:** 
+  Multi-factor authentication provides defense-in-depth by requiring an unauthorized party to obtain both the password and a second factor, raising the bar for unauthorized access even when credentials are disclosed. 
+  Individual identities with strong authentication create clear attribution for actions, which supports forensic investigation and compliance requirements for user activity tracking. 
+  Detective controls for anomalous sign-in behavior let security teams identify potential credential exposure before unauthorized parties can act on access, reducing dwell time and limiting impact. 
+  Strong authentication requirements align with security frameworks like NIST 800-63 and industry regulations, simplifying compliance demonstrations and reducing audit findings. 
+  Centralized authentication policies and enforcement mechanisms reduce the operational burden of managing authentication requirements across multiple systems and identity sources. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Authentication is the trust boundary between legitimate users and unauthorized parties. When this boundary is weak, every other security control becomes less effective. An unauthorized user with valid credentials can bypass network controls, assume legitimate roles, and access resources as if they were authorized. No matter how well you design permissions or implement monitoring, weak sign-in mechanisms create gaps other controls cannot close. Strong sign-in mechanisms shift the security posture from "trust the credential" to "trust the credential plus verified possession of a second factor plus behavioral consistency," spanning authentication strength, credential policies, and anomaly detection across all identity sources. 

 AWS environments support multiple authentication paths depending on your organizational structure and use cases. For workforce identities (employees and contractors who operate AWS resources), use centralized identity providers through federation. IAM Identity Center provides native federation with built-in MFA and password policy controls. You can also establish direct SAML 2.0 federation with external identity providers such as Okta, Microsoft Entra ID (formerly Azure AD), or Ping Identity. Centralized authentication applies consistent requirements across all AWS accounts and reduces the burden of managing authentication in each account separately. 

 The AWS account root user has unrestricted permissions and cannot be limited through IAM policies. Protect the root user with phishing-resistant MFA such as passkeys or security keys. Store root credentials in a physically secure location accessible only to a small number of trusted administrators. Reserve the root user for tasks that explicitly require it (account closure, billing contact changes, and a small number of other privileged operations). Use federated identities or IAM roles for day-to-day operations. 

 For application-facing authentication (customers, partners, or external users), Amazon Cognito user pools support configurable password policies, MFA options, and adaptive authentication. Cognito's advanced security features detect anomalous sign-in patterns such as login attempts from unexpected geographic locations or devices. Cognito responds automatically by blocking or challenging the attempt. 

 IAM users (direct users created in AWS IAM rather than federated from an external identity provider) are a legacy authentication pattern. AWS recommends federation for human identities. Where IAM users still exist, enforce mandatory MFA, strong password policies, and individual credentials that are never shared. Attach an IAM policy that denies all actions except credential management until the user configures MFA. This provides a self-service enrollment path and prevents resource access for users without MFA. 

 Context-aware authentication evaluates the sign-in context (device, location, IP address, time of day) and adjusts authentication requirements. IAM Identity Center supports context-aware MFA that can require step-up authentication when it detects high-risk sign-in conditions. This balances security with user experience by requiring additional verification only when the context suggests elevated risk. 

 Detective controls complement preventative authentication by identifying suspicious patterns that indicate credential exposure or abuse. AWS CloudTrail captures authentication events. Amazon GuardDuty detects anomalous authentication patterns: sign-ins from unusual locations, brute-force attempts, and impossible travel (authentication from geographically distant locations in an impossibly short time). Automated responses (for example, disabling a user account when GuardDuty confirms credential exposure) reduce the time between detection and containment. 

 NIST 800-63 emphasizes password length over complexity, because longer passwords provide more entropy than shorter passwords with special character requirements. Rigid composition rules often lead to predictable patterns such as Password1\!. Require at least 14 characters and allow spaces and special characters. Password history prevents reuse of recent passwords. Forcing frequent changes without cause weakens passwords, because users make minimal changes to satisfy the requirement. Configure the settings to follow your company policy or a standard such as [NIST 800-63](https://pages.nist.gov/800-63-3/sp800-63b.html). 

**Important**  
 Do not create long-term access keys (access key ID and secret access key) for the root user. If root user access keys exist in your account, delete them immediately. Root user access keys cannot be restricted by IAM policies and are a significant security risk. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable MFA for the AWS account root user:** Immediately after creating an AWS account, sign in as the root user, navigate to the IAM console security credentials page, and configure MFA. Prefer phishing-resistant factors such as passkeys or security keys. Virtual MFA applications are an acceptable alternative when phishing-resistant factors are not available. Store the hardware device or virtual MFA backup codes in a secure physical location accessible only to designated administrators. Test the MFA configuration by signing out and signing back in. Refer to [Multi-factor authentication for AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html) for detailed instructions. 

1.  **Establish centralized authentication using IAM Identity Center or external federation:** For workforce identities, configure IAM Identity Center as your centralized authentication point for all AWS accounts in your organization. If you use an external identity provider, configure SAML 2.0 federation between the provider and IAM Identity Center or establish direct SAML federation with AWS IAM. Verify that users can authenticate through the centralized identity provider and access AWS resources. See [Getting started with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) and [Enabling and configuring SAML 2.0-based federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html). 

1.  **Configure strong password policies in IAM Identity Center:** If using the IAM Identity Center default directory, review the predefined password policy, which requires a minimum length, complexity requirements, and password history. Adjust these settings to meet your organization's security requirements, at minimum a 14-character password length. If using AWS Managed Microsoft AD or AD Connector as the identity source, configure password policies in the directory service itself. Refer to [Password requirements when managing identities in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/password-requirements.html) and enforce strong passwords following [NIST 800-63: Strength of Memorized Secrets](https://pages.nist.gov/800-63-3/sp800-63b.html#appA). 

1.  **Enable MFA in IAM Identity Center with context-aware authentication:** In the IAM Identity Center console, enable MFA and configure the authentication context to require MFA always or only when sign-in context indicates elevated risk. Permit users to self-register their MFA devices to reduce administrative overhead. Test the configuration by signing in under different conditions and verifying that MFA challenges appear as expected. See [Multi-factor authentication](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-mfa.html) and [How to allow users to register their own MFA devices](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-allow-user-registration.html). 

1.  **Configure Amazon Cognito user pools for application authentication:** For customer-facing applications that require authentication, create an Amazon Cognito user pool and configure password strength requirements including minimum length and character composition rules. Enable MFA for user pool sign-ins, offering TOTP software tokens or SMS as second factors. Activate threat protection to detect and respond to suspicious sign-in attempts. Review [Configure user pool sign-in options](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users-passwords.html) and [Advanced security with threat protection](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.html). 

1.  **Enforce MFA and strong passwords for IAM users if applicable:** If your environment includes IAM users (not recommended for human identities), set an account password policy that requires minimum length, complexity, and password expiration according to your security requirements. Create an IAM policy that enforces MFA by denying all actions except credential management until the user configures MFA. Attach this policy to all IAM users or groups. Instruct users to configure MFA through the IAM console security credentials page. See [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) and [AWS Multi-factor authentication in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html). 

1.  **Monitor authentication events through CloudTrail:** Make sure that AWS CloudTrail is enabled in all AWS accounts and Regions and that you actively monitor IAM and IAM Identity Center authentication events. Configure CloudTrail to deliver logs to a centralized S3 bucket in a log archive account for long-term retention and analysis. Verify that authentication events (ConsoleLogin, AssumeRole, GetSessionToken) appear in CloudTrail logs and feed into your monitoring pipeline. Refer to [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html). 

1.  **Deploy GuardDuty for anomalous authentication detection:** Enable Amazon GuardDuty in all AWS accounts (or centrally through AWS Organizations) to monitor for suspicious authentication patterns including impossible travel, brute-force attempts, and credential exposure. Configure GuardDuty findings to publish to Amazon EventBridge and create automated response workflows for high-severity authentication findings. Test the detection by simulating suspicious authentication patterns in a non-production environment. See [Getting started with GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html) and [GuardDuty findings for IAM](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html). 

1.  **Establish monitoring and alerting for authentication failures:** Create CloudWatch Logs metric filters or EventBridge rules to detect patterns that indicate authentication problems, such as repeated failed login attempts, MFA failures, or authentication from unexpected IP ranges. Route alerts to security operations teams through Amazon SNS or your security information and event management (SIEM) system. Set thresholds that balance signal-to-noise (catching genuine threats without overwhelming operations with false positives). See [Creating CloudWatch alarms for CloudTrail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html). 

1.  **Conduct regular authentication security reviews:** Establish a quarterly review process to audit user accounts, verify MFA enrollment status, identify dormant accounts, check for shared credentials, and validate password policy compliance. Disable or remove accounts that no longer require access. Review authentication logs for unusual patterns that automated detection might have missed. Document findings and remediation actions. Use AWS IAM Access Analyzer or IAM Identity Center reporting features to identify users without MFA enabled or weak password configurations. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND02-BP01 Protect account root users, and establish alternate contacts](fnd02-bp01.md) 
+  [FND02-BP03 Employ a centralized identity provider](fnd02-bp03.md) 
+  [SEC02-BP03 Store and use secrets securely](sec02-bp03.md) 
+  [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md) 
+  [SEC03-BP04 Share resources securely within your organization](sec03-bp04.md) 

 **Related documents:** 
+  [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) 
+  [Getting started with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) 
+  [Password requirements when managing identities in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/password-requirements.html) 
+  [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) 
+  [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) 
+  [Configure user pool sign-in options - Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users-passwords.html) 
+  [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) 
+  [Security best practices in IAM - Require multi-factor authentication (MFA)](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#enable-mfa-for-privileged-users) 
+  [NIST Special Publication 800-63B - Authentication and Lifecycle Management](https://pages.nist.gov/800-63-3/sp800-63b.html) 
+  [Passkeys enhance security and usability as AWS expands MFA requirements](https://aws.amazon.com/blogs/security/passkeys-enhance-security-and-usability-as-aws-expands-mfa-requirements/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Dive deep into IAM Identity Center](https://www.youtube.com/watch?v=3HejqmJcDoQ) 
+  [AWS re:Inforce 2024 - Securing human access to AWS at scale](https://www.youtube.com/watch?v=N82s9TF_b9w) 

 **Related services:** 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) 