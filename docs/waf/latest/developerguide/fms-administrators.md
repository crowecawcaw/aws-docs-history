**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using AWS Firewall Manager administrators

This page explains what Firewall Manager administrators are and defines related terms.

With AWS Firewall Manager you can have one or multiple administrators who can manage the firewall
resources of your organization. If you want to use multiple Firewall Manager administrators in your
organization, you can apply administrative scope conditions to each administrator to define
the resources that they can manage. This gives you the flexibility to have different
administrator roles within your organization, and helps you maintain the principal of least
privileged access. For example, you can have one administrator manage a set of
organizational units (OUs) for your organization, while delegating another administrator to
manage only specific Firewall Manager policy types. For more information about Organizations and
management accounts, see [Managing the AWS Accounts in Your Organization](../../../organizations/latest/userguide/orgs_manage_accounts.md "../../../organizations/latest/userguide/orgs_manage_accounts.md").

For the maximum number of administrators that you can have per organization, see
[AWS Firewall Manager quotas](fms-limits.md "fms-limits.md")

###### Getting started using Firewall Manager administrators

Before you begin using Firewall Manager administrators, you must complete the prerequisites listed in
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). In the prerequisites,
you'll onboard an AWS Organizations organization to Firewall Manager and create a default administrator
account for Firewall Manager. A default administrator account has the ability to manage third-party
firewalls and has full administrative scope.

###### Administrative scope

_Administrative scope_ defines the resources that the Firewall Manager administrator
can manage. After an AWS Organizations management account onboards an organization to Firewall Manager, the
management account can create additional Firewall Manager administrators with different
administrative scopes. An AWS Organizations management account can either grant the administrator
**full** or **restricted** administrative scope.
Full scope gives the administrator full access to all of the preceding resource types.
Restricted scope refers to granting administrative permission to only a subset of the
preceding resources. We recommend that you only grant administrators the permissions
they need to perform the duties of their role. You can apply any combination of these
administrative scope conditions to an administrator:

- Accounts or OUs in your organization that the administrator can apply policies to.
- Regions that the administrator can perform actions in.
- Firewall Manager policy types that the administrator can manage.

###### Administrator roles

There are two types of administrator roles in Firewall Manager: a default administrator, and Firewall Manager
administrators.

- Default administrator - The organization's management account creates a Firewall Manager
  _default administrator_ account when they onboard their
  organization to Firewall Manager while completing the [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). The default administrator can manage third-party
  firewalls and has full administrative scope, but is otherwise at the same peer level
  as other administrators, if you choose to have multiple administrators.
- Firewall Manager administrators - A Firewall Manager administrator can manage the resources that the AWS Organizations
  management account designates for them in their administrative scope configuration.
  For the maximum number of administrators that you can have per organization, see
  [AWS Firewall Manager quotas](fms-limits.md "fms-limits.md"). Upon creation of a
  Firewall Manager administrator account, the service checks with AWS Organizations to see if the account
  is already a delegated administrator for Firewall Manager within the organization. If not, then
  Firewall Manager calls Organizations to set the account as a delegated administrator for Firewall Manager. For
  information about Organizations delegated administrators, see [AWS Organizations
  terminology and concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the
  _AWS Organizations User Guide_.

###### Existing administrators

If you are an existing Firewall Manager customer and have set already set an administrator, then this
existing administrator will be the Firewall Manager default administrator. There should be no
impacts to your existing flow. If you wish to add more administrators, you can do so by
following the procedures in this chapter.
