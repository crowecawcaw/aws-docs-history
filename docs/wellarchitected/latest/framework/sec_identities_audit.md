# SEC02-BP05 Audit and rotate credentials periodically

Audit and rotate credentials periodically to limit how long the
credentials can be used to access your resources. Long-term
credentials create many risks, and these risks can be reduced by
rotating long-term credentials regularly.

**Desired outcome:** Implement
credential rotation to help reduce the risks associated with
long-term credential usage. Regularly audit and remediate
non-compliance with credential rotation policies.

**Common anti-patterns:**

- Not auditing credential use.
- Using long-term credentials unnecessarily.
- Using long-term credentials and not rotating them regularly.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When you cannot rely on temporary credentials and require
long-term credentials, audit credentials to verify that defined
controls like
[multi-factor
authentication](https://aws.amazon.com/iam/features/mfa/ "https://aws.amazon.com/iam/features/mfa/") (MFA) are enforced, rotated regularly, and
have the appropriate access level.

Periodic validation, preferably through an automated tool, is
necessary to verify that the correct controls are enforced. For
human identities, you should require users to change their
passwords periodically and retire access keys in favor of
temporary credentials. As you move from AWS Identity and Access Management (IAM) users to centralized identities, you can
[generate
a credential report](../../../IAM/latest/UserGuide/id_credentials_getting-report.md "../../../IAM/latest/UserGuide/id_credentials_getting-report.md") to audit your users.

We also recommend that you enforce and monitor MFA in your
identity provider. You can set up
[AWS Config Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md"), or use
[AWS Security Hub CSPM Security Standards](../../../securityhub/latest/userguide/securityhub-standards-fsbp-controls.md#fsbp-iam-3 "../../../securityhub/latest/userguide/securityhub-standards-fsbp-controls.md#fsbp-iam-3"), to monitor if users have
configured MFA. Consider using
[IAM
Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md") to provide temporary credentials for machine
identities. In situations when using IAM roles and temporary
credentials is not possible, frequent auditing and rotating access
keys is necessary.

### Implementation steps

- **Regularly audit
  credentials:** Auditing the identities that are
  configured in your identity provider and IAM helps verify
  that only authorized identities have access to your
  workload. Such identities can include, but are not limited
  to, IAM users, AWS IAM Identity Center users, Active
  Directory users, or users in a different upstream identity
  provider. For example, remove people that leave the
  organization, and remove cross-account roles that are no
  longer required. Have a process in place to periodically
  audit permissions to the services accessed by an IAM entity.
  This helps you identify the policies you need to modify to
  remove any unused permissions. Use credential reports and
  [AWS Identity and Access Management Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") to
  audit IAM credentials and permissions. You can use
  [Amazon CloudWatch to set up alarms for specific API calls](../../../awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.md")
  called within your AWS environment.
  [Amazon GuardDuty can also alert you to unexpected activity](../../../guardduty/latest/ug/guardduty_finding-types-iam.md "../../../guardduty/latest/ug/guardduty_finding-types-iam.md"),
  which might indicate overly permissive access or unintended
  access to IAM credentials.
- **Rotate credentials
  regularly:** When you are unable to use temporary
  credentials, rotate long-term IAM access keys regularly
  (maximum every 90 days). If an access key is unintentionally
  disclosed without your knowledge, this limits how long the
  credentials can be used to access your resources. For
  information about rotating access keys for IAM users, see
  [Rotating
  access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey").
- **Review IAM permissions:**
  To improve the security of your AWS account, regularly
  review and monitor each of your IAM policies. Verify that
  policies adhere to the principle of least privilege.
- **Consider automating IAM resource
  creation and updates:**
  [IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") automates many IAM tasks, such as
  role and policy management. Alternatively, AWS CloudFormation can be used to automate the deployment of IAM
  resources, including roles and policies, to reduce the
  chance of human error because the templates can be verified
  and version controlled.
- **Use IAM Roles Anywhere to replace
  IAM users for machine identities:**
  [IAM
  Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md") allows you to use roles in areas that
  you traditionally could not, such as on-premise servers. IAM
  Roles Anywhere uses a trusted
  [X.509
  certificate](../../../rolesanywhere/latest/userguide/trust-model.md#signature-verification "../../../rolesanywhere/latest/userguide/trust-model.md#signature-verification") to authenticate to AWS and receive
  temporary credentials. Using IAM Roles Anywhere avoids the
  need to rotate these credentials, as long-term credentials
  are no longer stored in your on-premises environment. Please
  note that you will need to monitor and rotate the X.509
  certificate as it approaches expiration.

## Resources

**Related best practices:**

- [SEC02-BP02 Use temporary
  credentials](../security-pillar/sec_identities_unique.md "../security-pillar/sec_identities_unique.md")
- [SEC02-BP03 Store and use
  secrets securely](../security-pillar/sec_identities_secrets.md "../security-pillar/sec_identities_secrets.md")

**Related documents:**

- [Getting
  Started with AWS Secrets Manager](../../../secretsmanager/latest/userguide/getting-started.md "../../../secretsmanager/latest/userguide/getting-started.md")
- [IAM
  Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [Identity
  Providers and Federation](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md")
- [Security
  Partner Solutions: Access and Access Control](https://aws.amazon.com/security/partner-solutions/#access-control "https://aws.amazon.com/security/partner-solutions/#access-control")
- [Temporary
  Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md")
- [Getting
  credential reports for your AWS account](../../../IAM/latest/UserGuide/id_credentials_getting-report.md "../../../IAM/latest/UserGuide/id_credentials_getting-report.md")

**Related videos:**

- [Best Practices
  for Managing, Retrieving, and Rotating Secrets at Scale](https://youtu.be/qoxxRlwJKZ4 "https://youtu.be/qoxxRlwJKZ4")
- [Managing user
  permissions at scale with AWS IAM Identity Center](https://youtu.be/aEIqeFCcK7E "https://youtu.be/aEIqeFCcK7E")
- [Mastering
  identity at every layer of the cake](https://www.youtube.com/watch?v=vbjFjMNVEpc "https://www.youtube.com/watch?v=vbjFjMNVEpc")
