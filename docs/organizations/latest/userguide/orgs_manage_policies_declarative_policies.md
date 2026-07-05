# Declarative policies in AWS Organizations

Declarative policies enable you to centrally configure and manage AWS services and their
features. How those policies affect the OUs and accounts that inherit them depends on the
type of declarative policy you apply in AWS Organizations. Review the topics in this section to
understand relevant terms and concepts about declarative policies.

Declarative policies allow you to centrally declare and enforce your desired configuration
for a given AWS service at scale across an organization. Once attached, the configuration
is always maintained when the service adds new features or APIs. Use declarative policies to
prevent noncompliant actions. For example, you can block public internet access to Amazon VPC
resources, or enforce encryption in transit for VPC traffic, across your organization.

The key benefits of using declarative policies are:

- **Ease of use**: You can enforce the baseline
  configuration for an AWS service with a few selections in the AWS Organizations and
  AWS Control Tower consoles or with a few commands using the AWS CLI & AWS SDKs.
- **Set once and forget**: The baseline configuration
  for an AWS service is always maintained, even when the service introduces new
  features or APIs. The baseline configuration is also maintained when new accounts
  are added to an organization or when new principals and resources are
  created.
- **Transparency**: The account status report allows
  you to review the current status of all attributes supported by declarative policies
  for the accounts in scope. You can also create customizable error messages, which
  can help administrators redirect end users to internal wiki pages or provide a
  descriptive message that can help end users understand why an action failed.

## How declarative policies work

Declarative policies are enforced in the service's control plane, which is an
important distinction from [authorization policies such as service control policies (SCPs) and resource control
policies (RCPs)](orgs_manage_policies_authorization_policies.md "orgs_manage_policies_authorization_policies.md"). While authorization policies regulate access to APIs,
declarative policies are applied directly at the service level to enforce durable
intent. This ensures that the baseline configuration is always enforced, even when new
features or APIs are introduced by the service.

The following table helps illustrate this distinction and provides some use
cases.

|                               | Service control policies                                                                                                                                                                                                                                                                                                                                                                  | Resource control policies                                                                                                                                                                                                                                                                                                                                                                                                  | Declarative policies                                                                                                                                                      |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Why?                          | To centrally define and enforce consistent access controls on<br>principals (such as IAM users and IAM roles) at scale.                                                                                                                                                                                                                                                                   | To centrally define and enforce consistent access controls on<br>resources at scale                                                                                                                                                                                                                                                                                                                                        | To centrally define and enforce the baseline configuration for<br>AWS services at scale.                                                                                  |
| How?                          | By controlling the maximum available access permissions of<br>principals at an API level.                                                                                                                                                                                                                                                                                                 | By controlling the maximum available access permissions for<br>resources at an API level.                                                                                                                                                                                                                                                                                                                                  | By enforcing the desired configuration of an AWS service without<br>using API actions.                                                                                    |
| Governs service-linked roles? | No                                                                                                                                                                                                                                                                                                                                                                                        | No                                                                                                                                                                                                                                                                                                                                                                                                                         | Yes                                                                                                                                                                       |
| Example policy                | [Deny member accounts from leaving the organization](https://github.com/aws-samples/service-control-policy-examples/blob/main/Privileged-access-controls/Deny-member-accounts-from-leaving-your-AWS-organization.json "https://github.com/aws-samples/service-control-policy-examples/blob/main/Privileged-access-controls/Deny-member-accounts-from-leaving-your-AWS-organization.json") | [Restrict access to only HTTPS connections to your resources](https://github.com/aws-samples/resource-control-policy-examples/blob/main/Restrict-resource-access-patterns/Restrict-access-to-only-HTTPS-connections-to-your-resources.json "https://github.com/aws-samples/resource-control-policy-examples/blob/main/Restrict-resource-access-patterns/Restrict-access-to-only-HTTPS-connections-to-your-resources.json") | [Allowed<br>Images Settings](orgs_manage_policies_ec2_syntax.md#ec2-policy-ec2-ami-allowed-images "orgs_manage_policies_ec2_syntax.md#ec2-policy-ec2-ami-allowed-images") |

After you have [created](orgs_policies_create.md#create-declarative-policy-procedure "orgs_policies_create.md#create-declarative-policy-procedure") and [attached](orgs_policies_attach.md "orgs_policies_attach.md") a
declarative policy, it is applied and enforced across your organization. Declarative
policies can be applied to an entire organization, organizational units (OUs), or
accounts. Accounts joining an organization will automatically inherit the declarative
policy in the organization. For more information, see [Understanding declarative policy inheritance](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md").

The _effective policy_ is the set of rules that are
inherited from the organization root and OUs along with those directly attached to the
account. The effective policy specifies the final set of rules that apply to the
account. For more information, see [Viewing effective declarative policies](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md").

If a declarative policy is [detached](orgs_policies_detach.md "orgs_policies_detach.md"), the
attribute state will roll back to its previous state before the declarative policy was
attached.

###### Topics

- [Prerequisites and permissions](orgs_manage_policies_prereqs.md "orgs_manage_policies_prereqs.md")
- [Understanding policy inheritance](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md")
- [Viewing effective policies](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md")
- [Invalid policy alerts](invalid-policy-alerts.md "invalid-policy-alerts.md")
- [EC2 policies](orgs_manage_policies_ec2.md "orgs_manage_policies_ec2.md")
- [Backup policies](orgs_manage_policies_backup.md "orgs_manage_policies_backup.md")
- [Tag policies](orgs_manage_policies_tag-policies.md "orgs_manage_policies_tag-policies.md")
- [Chat applications policies](orgs_manage_policies_chatbot.md "orgs_manage_policies_chatbot.md")
- [AI services opt-out policies](orgs_manage_policies_ai-opt-out.md "orgs_manage_policies_ai-opt-out.md")
- [Security Hub policies](orgs_manage_policies_security_hub.md "orgs_manage_policies_security_hub.md")
- [Amazon Bedrock policies](orgs_manage_policies_bedrock.md "orgs_manage_policies_bedrock.md")
- [Amazon Inspector policies](orgs_manage_policies_inspector.md "orgs_manage_policies_inspector.md")
- [Upgrade rollout policies](orgs_manage_policies_upgrade_rollout.md "orgs_manage_policies_upgrade_rollout.md")
- [Amazon S3 policies](orgs_manage_policies_s3.md "orgs_manage_policies_s3.md")
- [AWS Shield Network Security Director policies](orgs_manage_policies_network_security_director.md "orgs_manage_policies_network_security_director.md")
