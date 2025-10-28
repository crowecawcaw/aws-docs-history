# About member accounts

Member accounts are the accounts through which your users perform their AWS workloads.
AWS Control Tower member accounts can be created and customized by various methods, including automated methods. In some cases, you can bring existing AWS accounts into AWS Control Tower.
When member accounts are created or enrolled, they must exist inside an organizational unit (OU) that was created in the AWS Control Tower
console, or registered with AWS Control Tower. For more information, see these related
topics:

- [Methods of provisioning](methods-of-provisioning.md "methods-of-provisioning.md")
- [Provision and manage accounts with Account Factory](account-factory.md "account-factory.md")
- [Automate tasks in AWS Control Tower](automating-tasks.md "automating-tasks.md")
- [Move and enroll accounts with auto-enrollment](account-auto-enrollment.md "account-auto-enrollment.md")
- [Provision accounts with AWS Control Tower Account Factory
  for Terraform (AFT)](taf-account-provisioning.md "taf-account-provisioning.md")
- [AWS
  Organizations Terminology and Concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the
  _AWS Organizations User Guide_.

###### Accounts and controls

Member accounts can be _enrolled_ in AWS Control Tower, or
they can be _unenrolled_. Controls apply
differently to enrolled and unenrolled accounts, and controls may apply to
accounts in nested OUs based on inheritance.

For information about member account resources that AWS Control Tower allocates, see [Resource Considerations for
Account Factory](account-factory-considerations.md "account-factory-considerations.md").
