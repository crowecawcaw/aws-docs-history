# Delegated administrator for AWS services that work with Organizations

We recommend that you use the AWS Organizations management account and its users and roles only for
tasks that must be performed by that account. We also recommend that you store your AWS resources in other
member accounts in the organization and keep them out of the management account. This is because security features
like Organizations service control policies (SCPs) do not restrict users or roles in the management account.
Separating your resources from your management account can also help you understand the charges on your invoices.

Many AWS services that integrate with Organizations enable you to reduce the usage of the
management account. These services enable you to register one or more member accounts as
administrators that can manage all of the organization's accounts used in the service. These
accounts are called _delegated administrators_ for that
specific service. By registering a member account as a delegated administrator for an AWS
service you enable that account to have some administrative permissions for that service, as
well as permissions for Organizations read-only actions.

Before you register an account as a delegated administrator for a service:

- Confirm that the service supports delegated administrators. See the table in [AWS services that you can use with
  AWS Organizations](orgs_integrate_services_list.md "orgs_integrate_services_list.md") to learn which services support delegated administrators.
- Enable trusted access for that service.

###### Note

To learn how to enable a delegated administrator a service, reference the table in [AWS services that you can use with
AWS Organizations](orgs_integrate_services_list.md "orgs_integrate_services_list.md") and select the **Learn more** link in the **Supports Delegated Administrator** column for that service.

## Permissions granted to delegated administrator accounts

Each service-specific delegated administrator account has permissions granted by that service. To learn more, reference the table in [AWS services that you can use with
AWS Organizations](orgs_integrate_services_list.md "orgs_integrate_services_list.md") and select the **Learn more** link in the **Supports Delegated Administrator** column for that service.

A delegated administrator account also has these read-only permissions:

- `DescribeAccount`
- `DescribeCreateAccountStatus`
- `DescribeEffectivePolicy`
- `DescribeHandshake`
- `DescribeOrganization`
- `DescribeOrganizationalUnit`
- `DescribePolicy`
- `DescribeResourcePolicy`
- `ListAccounts`
- `ListAccountsForParent`
- `ListAWSServiceAccessForOrganization`
- `ListChildren`
- `ListCreateAccountStatus`
- `ListDelegatedAdministrators`
- `ListDelegatedServicesForAccount`
- `ListHandshakesForAccount`
- `ListHandshakesForOrganization`
- `ListOrganizationalUnitsForParent`
- `ListParents`
- `ListPolicies`
- `ListPoliciesForTarget`
- `ListRoots`
- `ListTagsForResource`
- `ListTargetsForPolicy`

These permissions enable you to view, but not change these console items:

- Organization structure, all accounts and OUs, and organizational policies
- Memberships
- All accounts and OUs.
- Organizational policies
