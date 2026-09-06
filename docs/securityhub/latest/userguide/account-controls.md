

# Security Hub CSPM controls for AWS accounts
<a name="account-controls"></a>

These Security Hub CSPM controls evaluate AWS accounts.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [Account.1] Security contact information should be provided for an AWS account
<a name="account-1"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.2, NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2)

**Category:** Identify > Resource Configuration

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`security-account-information-provided`](https://docs.aws.amazon.com/config/latest/developerguide/security-account-information-provided.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks if an Amazon Web Services (AWS) account has security contact information. The control fails if security contact information is not provided for the account.

Alternate security contacts allow AWS to contact another person about issues with your account in case you're unavailable. Notifications can be from Support, or other AWS service teams about security-related topics associated with your AWS account usage.

### Remediation
<a name="account-1-remediation"></a>

To add an alternate contact as a security contact to your AWS account, see [Update the alternate contacts for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html) in the *AWS Account Management Reference Guide*.

## [Account.2] AWS accounts should be part of an AWS Organizations organization
<a name="account-2"></a>

**Category:** Protect > Secure access management > Access control

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Severity:** High

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`account-part-of-organizations`](https://docs.aws.amazon.com/config/latest/developerguide/account-part-of-organizations.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks if an AWS account is part of an organization managed through AWS Organizations. The control fails if the account is not part of an organization.

Organizations helps you centrally manage your environment as you scale your workloads on AWS. You can use multiple AWS accounts to isolate workloads that have specific security requirements, or to comply with frameworks such as HIPAA or PCI. By creating an organization, you can administer multiple accounts as a single unit and centrally manage their access to AWS services, resources, and Regions.

### Remediation
<a name="account-2-remediation"></a>

To create a new organization and automatically add AWS accounts to it, see [Creating an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html) in the *AWS Organizations User Guide*. To add accounts to an existing organization, see [Inviting an AWS account to join your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html) in the *AWS Organizations User Guide*.