# Example Service Control Policies for

AWS Trusted Advisor

AWS Trusted Advisor supports service control policies (SCPs). SCPs are policies that you attach to elements
in an organization to manage permissions within that organization. An SCP applies to all AWS accounts
[under the element to which you attach the SCP](../../../organizations/latest/userguide/orgs_manage_policies_inheritance_auth.md "../../../organizations/latest/userguide/orgs_manage_policies_inheritance_auth.md"). SCPs offer central control over the maximum available permissions
for all accounts in your organization. They can help you to ensure your AWS accounts stay within your
organization’s access control guidelines. For more information, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the
_AWS Organizations User Guide_.

###### Topics

- [Prerequisites](#prerequisites-trusted-advisor-scps "#prerequisites-trusted-advisor-scps")
- [Example Service Control Policies](#example-service-control-policies "#example-service-control-policies")

## Prerequisites

To use SCPs, you must first do the following:

- Enable all features in your organization. For more information, see [Enabling all features
  in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") in the _AWS Organizations User Guide_.
- Enable SCPs for use within your organization. For more information, see [Enabling and disabling
  policy types](../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md "../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md") in the _AWS Organizations User Guide_.
- Create the SCPs that you need. For more information about creating SCPs, see [Creating, updating, and deleting
  service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md") in the _AWS Organizations User Guide_.

## Example Service Control Policies

The following examples show how you can control various aspects of resource sharing in an organization.

###### Example: Prevent users from creating or editing engagements in Trusted Advisor Engage

The following SCP prevents users from creating new engagements or editing existing engagements.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "trustedadvisor:CreateEngagement",
 "trustedadvisor:UpdateEngagement*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

###### Example: Deny Trusted Advisor Engage and Trusted Advisor Priority Access

The following SCP prevents users from accessing or performing any actions within Trusted Advisor Engage and Trusted Advisor Priority.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "trustedadvisor:ListEngagement*",
 "trustedadvisor:GetEngagement*",
 "trustedadvisor:CreateEngagement*",
 "trustedadvisor:UpdateEngagement*",
 "trustedadvisor:DescribeRisk*",
 "trustedadvisor:UpdateRisk*",
 "trustedadvisor:DownloadRisk"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
