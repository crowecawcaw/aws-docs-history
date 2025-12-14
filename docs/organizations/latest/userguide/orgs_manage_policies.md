# Managing organization policies with AWS Organizations

Policies in AWS Organizations enable you to apply additional types of management to the
AWS accounts in your organization. You can use policies when [all features are enabled](orgs_manage_org_support-all-features.md "orgs_manage_org_support-all-features.md") in your
organization.

The AWS Organizations console displays the enabled or disabled status for each policy type. On the
**Organize accounts** tab, choose the `Root` in the left
navigation pane. The details pane on the right side of the screen shows all of the available
policy types. The list indicates which are enabled and which are disabled in that
organization root. If the option to **Enable** a type is present, that type
is currently disabled. If the option to **Disable** a type is present, that
type is currently enabled.

###### Topics

- [Policy types](#orgs-policy-types "#orgs-policy-types")
- [Authorization policies](orgs_manage_policies_authorization_policies.md "orgs_manage_policies_authorization_policies.md")
- [Management policies](orgs_manage_policies_management_policies.md "orgs_manage_policies_management_policies.md")
- [Delegated administrator for AWS Organizations](orgs_delegate_policies.md "orgs_delegate_policies.md")
- [Enabling a policy type](enable-policy-type.md "enable-policy-type.md")
- [Disabling a policy type](disable-policy-type.md "disable-policy-type.md")
- [Creating policies](orgs_policies_create.md "orgs_policies_create.md")
- [Updating policies](orgs_policies_update.md "orgs_policies_update.md")
- [Editing tags attached to policies](orgs_policies_edit.md "orgs_policies_edit.md")
- [Attaching policies](orgs_policies_attach.md "orgs_policies_attach.md")
- [Detaching policies](orgs_policies_detach.md "orgs_policies_detach.md")
- [Getting policy details](orgs_manage_policies_info-operations.md "orgs_manage_policies_info-operations.md")
- [Deleting policies](orgs_policies_delete.md "orgs_policies_delete.md")

## Policy types

Organizations offers policy types in the following two broad categories:

### Authorization

policies

Authorization policies help you to centrally manage the security of AWS accounts
across an organization.

- **[Service
  control policies (SCPs)](orgs_manage_policies_scps.md "orgs_manage_policies_scps.md")** offer central control over
  the maximum available permissions for IAM users and IAM roles in an
  organization.
- **[Resource
  control policies (RCPs)](orgs_manage_policies_rcps.md "orgs_manage_policies_rcps.md")** offer central control over
  the maximum available permissions for resources in an organization.

### Management policies

Management policies help you centrally configure and manage AWS services and
their features across an organization.

- **[Declarative policies](orgs_manage_policies_declarative.md "orgs_manage_policies_declarative.md")** allow you to centrally
  declare and enforce desired configurations for a given AWS service at
  scale across an organization. Once attached, the configuration is always
  maintained when the service adds new features or APIs.
- **[Backup
  policies](orgs_manage_policies_backup.md "orgs_manage_policies_backup.md")** allow you to centrally manage and apply
  backup plans to the AWS resources across an organization's
  accounts.
- **[Tag policies](orgs_manage_policies_tag-policies.md "orgs_manage_policies_tag-policies.md")** allow you to standardize the tags
  attached to the AWS resources in an organization's accounts.
- **[Chat
  applications policies](orgs_manage_policies_chatbot.md "orgs_manage_policies_chatbot.md")** allow you to control access
  to an organization's accounts from chat applications such as Slack and
  Microsoft Teams.
- **[AI
  services opt-out policies](orgs_manage_policies_ai-opt-out.md "orgs_manage_policies_ai-opt-out.md")** allow you to control
  data collection for AWS AI services for all the accounts in an
  organization.
- **[Security Hub CSPM policies](orgs_manage_policies_security_hub.md "orgs_manage_policies_security_hub.md")** allow you to address security
  coverage gaps that align with your organization's security requirements and
  centrally applying them across an organization.
- **[Amazon Inspector policies](orgs_manage_policies_inspector.md "orgs_manage_policies_inspector.md")** allow you to centrally enable and manage Amazon Inspector across accounts in your AWS organization.
- **[Amazon Bedrock policies](orgs_manage_policies_bedrock.md "orgs_manage_policies_bedrock.md")** allow you to enforce safeguards configured in Amazon Bedrock Guardrails automatically across any element in your organization structure for all model inference calls to Amazon Bedrock.
- **[Upgrade rollout policies](orgs_manage_policies_upgrade_rollout.md "orgs_manage_policies_upgrade_rollout.md")** allow you to centrally manage and stagger automatic upgrades across multiple AWS resources and accounts in your organization.
- **[Amazon S3 policies](orgs_manage_policies_s3.md "orgs_manage_policies_s3.md")** allow you to centrally manage configurations for Amazon S3 resources at scale across the accounts in an organization.

The following table summarizes some of the characteristics of each policy type. For
additional characteristics about these policy types, see [Quotas and service limits for AWS Organizations](orgs_reference_limits.md "orgs_reference_limits.md").

| Policy type                | Policy category | Affects management account | Maximum number you can attach to a root, OU, or account | Maximum size      | Supports viewing effective policy for OU or account |
| -------------------------- | --------------- | -------------------------- | ------------------------------------------------------- | ----------------- | --------------------------------------------------- |
| SCP                        | Authorization   | No                         | 5                                                       | 5120 characters   | No                                                  |
| RCP                        | Authorization   | No                         | 5                                                       | 5120 characters   | No                                                  |
| Declarative policy         | Management      | Yes                        | 10                                                      | 10,000 characters | Yes                                                 |
| Backup policy              | Management      | Yes                        | 10                                                      | 10,000 characters | Yes                                                 |
| Tag policy                 | Management      | Yes                        | 10                                                      | 10,000 characters | Yes                                                 |
| Chat applications policy   | Management      | Yes                        | 5                                                       | 10,000 characters | Yes                                                 |
| AI services opt-out policy | Management      | Yes                        | 5                                                       | 2500 characters   | Yes                                                 |
| Security Hub CSPM policy   | Management      | Yes                        | 10                                                      | 10,000 characters | Yes                                                 |
| Amazon Inspector policy    | Management      | Yes                        | 10                                                      | 10,000 characters | Yes                                                 |
| Amazon Bedrock policy      | Management      | Yes                        | 10                                                      | 10,000 characters | Yes                                                 |
| Upgrade rollout policy     | Management      | Yes                        | 10                                                      | 10,000 characters | Yes                                                 |
| S3 policy                  | Management      | Yes                        | 10                                                      | 10,000 characters | Yes                                                 |
