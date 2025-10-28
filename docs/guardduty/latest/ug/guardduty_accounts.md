# Multiple accounts in Amazon GuardDuty

When your AWS environment has multiple accounts, you can manage them by designating one
AWS account as the administrator account. You can then associate the multiple AWS accounts with this
administrator account as its member accounts. With this configuration, a designated GuardDuty administrator account can
assess and monitor the overall security of your organization. The administrator account can also perform
account management tasks, such as reviewing all generated findings and configuring
protection plans within GuardDuty.

In GuardDuty, an organization consists of a delegated GuardDuty administrator account and one or more associated member
accounts. You can associate the accounts in two ways – by integrating with AWS Organizations,
or by using a legacy method of sending and accepting membership invitations in the GuardDuty
console. GuardDuty recommends that you integrate with AWS Organizations.

AWS Organizations is a global account management service that enables AWS administrators to
consolidate and centrally manage multiple AWS accounts. It provides account management and
consolidated billing features that are designed to support budgetary, security, and
compliance needs. It’s offered at no additional charge and it integrates with multiple
AWS services, including Macie, AWS Security Hub, and Amazon GuardDuty. For more information, see the
[AWS Organizations User Guide](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

###### Contents

- [Understanding the relationship
  between GuardDuty administrator account and member accounts](administrator_member_relationships.md "administrator_member_relationships.md")
- [Managing GuardDuty accounts with AWS Organizations](guardduty_organizations.md "guardduty_organizations.md")
- [Managing GuardDuty accounts by invitation](guardduty_invitations.md "guardduty_invitations.md")
- [GuardDuty considerations for
  exporting member account details in CSV format](exporting-guardduty-accounts-data-to-csv.md "exporting-guardduty-accounts-data-to-csv.md")
