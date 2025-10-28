# Amazon Elastic Kubernetes Service and

AWS Organizations

The Amazon Elastic Kubernetes Service Dashboard is a consolidated dashboard that you can use to monitor,
manage, and gain visibility into your Kubernetes clusters across multiple AWS Regions and
AWS Accounts. The EKS Dashboard provides you with comprehensive control and insights for
your Amazon EKS infrastructure through a centralized interface.

The Amazon Elastic Kubernetes Service Dashboard enables you to track clusters scheduled for upgrades, project
control plane costs, review cluster insights, and monitor node group distributions across
your organization. Your AWS administrators can view aggregated data about cluster
resources, including health status, version distribution, and add-on configurations through
different visualization options including graphs, resource lists, and geographic maps. The
dashboard integrates with AWS Organizations to provide secure cross-account and
cross-region visibility of your EKS resources.

Use the following information to help you integrate
Amazon Elastic Kubernetes Service with AWS Organizations.

## Service-linked roles created when

you enable integration

The following service-linked role is automatically created in your organization's
management account when you enable trusted access using the Amazon Elastic Kubernetes Service console. This
role allows Amazon EKS to perform supported operations within your
organization's accounts in your organization. You can delete or modify this role only if
you disable trusted access between Amazon Elastic Kubernetes Service and Organizations.

If you enable trusted access directly from the Organizations console, CLI or SDK, the
service-linked role is not created automatically.

- `AWSServiceRoleForAmazonEKSDashboard`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Amazon EKS grant access to the following service
principals:

- `dashboard.eks.amazonaws.com`

## Enabling trusted access with

Amazon EKS

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

###### To enable trusted access using the Amazon EKS console

See [Enable trusted access](../../../eks/latest/userguide/cluster-dashboard-orgs.md#_enable_trusted_access "../../../eks/latest/userguide/cluster-dashboard-orgs.md#_enable_trusted_access") in the _Amazon EKS User
Guide_.

## Disabling trusted access with

Amazon EKS

###### To disable trusted access using the Amazon EKS console

See [Disable trusted access](../../../eks/latest/userguide/cluster-dashboard-orgs.md#_disable_trusted_access "../../../eks/latest/userguide/cluster-dashboard-orgs.md#_disable_trusted_access") in the _Amazon EKS User
Guide_.

## Enabling a delegated administrator

account for Amazon EKS

The management account administrator can delegate Amazon EKS administrative
permissions to a designated member account known as delegated administrator.

Management accounts and delegated administrator accounts can view the Amazon EKS
Dashboard.

###### To enable a delegated administrator account

See [Enable a delegated administrator account](../../../eks/latest/userguide/cluster-dashboard-orgs.md#_enable_a_delegated_administrator_account "../../../eks/latest/userguide/cluster-dashboard-orgs.md#_enable_a_delegated_administrator_account") in the _Amazon EKS
User Guide_.

## Disabling a delegated administrator

for Amazon EKS

Only an administrator in the organization management account can configure a delegated
administrator for Amazon EKS.

###### To disable a delegated administrator account

See [Disable a delegated administrator account](../../../eks/latest/userguide/cluster-dashboard-orgs.md#_disable_a_delegated_administrator_account "../../../eks/latest/userguide/cluster-dashboard-orgs.md#_disable_a_delegated_administrator_account") in the _Amazon EKS
User Guide_.
