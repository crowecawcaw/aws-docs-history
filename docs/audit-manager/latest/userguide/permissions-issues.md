# Troubleshooting permission and access

issues

You can use the information on this page to resolve common permission issues in
Audit Manager.

###### Topics

- [I followed the Audit Manager setup procedure,
  but I don't have enough IAM privileges](#insufficient-iam-privileges "#insufficient-iam-privileges")
- [I specified someone as an audit owner,
  but they still don’t have full access to the assessment. Why is this?](#audit-owner-missing-access "#audit-owner-missing-access")
- [I can't perform an action in Audit Manager](#cannot-perform-action "#cannot-perform-action")
- [I want to allow people outside
  of my AWS account to access my Audit Manager resources](#want-to-allow-access-to-resources "#want-to-allow-access-to-resources")
- [I see an Access Denied error, despite
  having the required Audit Manager permissions](#access-denied-due-to-scp "#access-denied-due-to-scp")
- [Additional resources](#permissions-see-also "#permissions-see-also")

## I followed the Audit Manager setup procedure,

but I don't have enough IAM privileges

The user, role, or group that you use to access Audit Manager must have the required
permissions. Moreover, your identity-based policy shouldn't be too restrictive.
Otherwise, the console won't function as intended. This guide provides an example
policy that you can use to [Allow the minimum
permissions required to enable Audit Manager](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console"). Depending on
your use case, you might need broader, less restrictive permissions. For example, we
recommend that audit owners have [administrator access](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md"). This is so that they can modify Audit Manager settings and
manage resources such as assessments, frameworks, controls, and assessment reports.
Other users, such as delegates, might only need [management access](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access") or [read-only](security_iam_id-based-policy-examples.md#read-only "security_iam_id-based-policy-examples.md#read-only") access.

Make sure that you add the appropriate permissions for your user, role, or group.
For audit owners, the recommended policy is [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md"). For delegates, you can use [the management access example policy](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access") that's provided on the [IAM policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md") page. You can use these example policies as a
starting point, and make changes as necessary to fit your requirements.

We recommend that you take time to customize your permissions to meet your
specific requirements. If you need help with IAM permissions, contact your
administrator or [AWS
Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## I specified someone as an audit owner,

but they still don’t have full access to the assessment. Why is this?

Specifying someone as an audit owner alone doesn't provide them with full access
to an assessment. Audit owners must also have the necessary IAM permissions to
access and manage Audit Manager resources. In other words, in addition to [specifying a user as an audit owner](create-assessments.md#choose-audit-owners "create-assessments.md#choose-audit-owners"), you must also attach the [necessary IAM policies](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-personas "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-personas") to that user. The idea behind this is that, by
requiring both, Audit Manager ensures that you have full control over all of the specifics of
each assessment.

###### Note

For audit owners, we recommend that you use the [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") policy. For more information,
see [Recommended policies for user personas in AWS Audit Manager](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-personas "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-personas").

## I can't perform an action in Audit Manager

If you don't have the necessary permissions to use the AWS Audit Manager console or Audit Manager
API operations, you will likely encounter an `AccessDeniedException`
error.

To resolve this issue, you must contact your administrator for assistance. Your
administrator is the person that provided you with your sign-in credentials.

## I want to allow people outside

of my AWS account to access my Audit Manager resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who
is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant
people access to your resources.

To learn more, consult the following:

- To learn whether Audit Manager supports these features, see [How AWS Audit Manager works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you
  own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
  _IAM User Guide_.

## I see an Access Denied error, despite

having the required Audit Manager permissions

If your account is a part of an organization, it’s possible that the `Access
 Denied` error is caused by a [service
control policy (SCP)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md"). SCPs are policies that are used to manage
permissions for an organization. When an SCP is in place, it can deny specific
permissions to all member accounts, including the delegated administrator account
that you use in Audit Manager.

For example, if your organization has an SCP in place that denies permissions for
AWS Control Catalog APIs, you can't view the resources that are provided by
Control Catalog. This is true even if you otherwise have the required permissions
for Audit Manager, such as the [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") policy. The SCP overrides the
managed policy permissions by explicitly denying access to the Control Catalog
APIs.

Here’s an example of such an SCP. With this SCP in place, your delegated
administrator account is denied access to the common controls, control objectives,
and control domains that are needed to use the common controls feature in Audit Manager.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "controlcatalog:ListCommonControls",
 "controlcatalog:ListObjectives",
 "controlcatalog:ListDomains"
 ],
 "Resource": "*"
 }
 ]
}`

```

To resolve this issue, we recommend that you take the following steps:

1. Confirm if an SCP is attached to your organization. For instructions, see
   [Getting information about your organization's policies](../../../organizations/latest/userguide/orgs_manage_policies_info-operations.md "../../../organizations/latest/userguide/orgs_manage_policies_info-operations.md") in the
   _AWS Organizations User Guide_.
2. Identify if the SCP is causing the `Access Denied`
   error.
3. Update the SCP to ensure that your delegated administrator account has the
   necessary access for Audit Manager. For instructions, see [Updating an SCP](../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md#update_policy "../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md#update_policy") in the _AWS
   Organizations User Guide_.

## Additional resources

The following pages contain troubleshooting guidance for other issues that can be
caused by missing permissions:

- [I can’t see any
  controls or control sets in my assessment](control-issues.md#cannot-view-controls "control-issues.md#cannot-view-controls")
- [The
  custom rule option is unavailable when I’m configuring a control data
  source](control-issues.md#custom-rule-option-unavailable "control-issues.md#custom-rule-option-unavailable")
- [I get an access denied error when I try to generate a
  report](assessment-report-issues.md#assessment-report-access-denied-error "assessment-report-issues.md#assessment-report-access-denied-error")
- [I get an access denied error when I try to generate an
  assessment report using my delegated administrator account](delegated-admin-issues.md#delegated-admin-access-denied-error "delegated-admin-issues.md#delegated-admin-access-denied-error")
- [I can't
  enable evidence finder](evidence-finder-issues.md#cannot-enable-evidence-finder "evidence-finder-issues.md#cannot-enable-evidence-finder")
- [I can't
  disable evidence finder](evidence-finder-issues.md#cannot-disable-evidence-finder "evidence-finder-issues.md#cannot-disable-evidence-finder")
- [My search query
  fails](evidence-finder-issues.md#cannot-start-query "evidence-finder-issues.md#cannot-start-query")
- [I specified an Amazon SNS topic in Audit Manager, but I'm
  not receiving any notifications](notification-issues.md#missing-notifications "notification-issues.md#missing-notifications")
