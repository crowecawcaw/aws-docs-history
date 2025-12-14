# Policy syntax and inheritance for management policy

types

Exactly how policies affect the OUs and accounts that inherit them depends on the type
of management policy you choose. Management policy types include:

- [Declarative
  policies](orgs_manage_policies_declarative.md "orgs_manage_policies_declarative.md")
- [Backup policies](orgs_manage_policies_backup.md "orgs_manage_policies_backup.md")
- [Tag policies](orgs_manage_policies_tag-policies.md "orgs_manage_policies_tag-policies.md")
- [Chat applications
  policies](orgs_manage_policies_chatbot.md "orgs_manage_policies_chatbot.md")
- [AI services opt-out
  policies](orgs_manage_policies_ai-opt-out.md "orgs_manage_policies_ai-opt-out.md")
- [Security Hub policies](orgs_manage_policies_security_hub.md "orgs_manage_policies_security_hub.md")
- [Bedrock policies](orgs_manage_policies_bedrock.md "orgs_manage_policies_bedrock.md")
- [Inspector policies](orgs_manage_policies_inspector.md "orgs_manage_policies_inspector.md")
- [Upgrade rollout
  policies](orgs_manage_policies_upgrade_rollout.md "orgs_manage_policies_upgrade_rollout.md")
- [S3 policies](orgs_manage_policies_s3.md "orgs_manage_policies_s3.md")
- [AWS Shield Network Security Director policies](orgs_manage_policies_network_security_director.md "orgs_manage_policies_network_security_director.md")
  The syntax for management policy types includes _[Inheritance operators](policy-operators.md "policy-operators.md")_, which
  enable you to specify with fine granularity what elements from the parent policies are
  applied and what elements can be overridden or modified when inherited by child OUs and
  accounts.

The _effective policy_ is the set of rules that are
inherited from the organization root and OUs along with those directly attached to the
account. The effective policy specifies the final set of rules that apply to the
account. You can view the effective policy for an account that includes the effect of
all of the inheritance operators in the policies applied. For more information, see
[Viewing effective management
policies](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md").
