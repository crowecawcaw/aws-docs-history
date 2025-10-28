# AWS managed policies for Amazon One Enterprise

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AmazonOneEnterpriseFullAccess

This policy grants administrative permissions that allow access to all Amazon One Enterprise resources and operations.

`one:*` Lets you perform all Amazon One Enterprise actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "FullAccessStatementID",
 "Effect": "Allow",
 "Action": [
 "one:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AmazonOneEnterpriseReadOnlyAccess

This policy grants read only permissions to all Amazon One Enterprise resources and operations.

`one:Get*` Gets the Amazon One Enterprise resources.

`one:List*` Lists the Amazon One Enterprise resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadOnlyAccessStatementID",
 "Effect": "Allow",
 "Action": [
 "one:Get*",
 "one:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AmazonOneEnterpriseInstallerAccess

This policy grants limited read and write permissions that allow you to create activation QR code for any configured device
instance to activate device at any site.

`one:CreateDeviceActivationQrCode` Let you create QR code to activate device.

`one:GetDeviceInstance` Let you fetch the information about an Amazon One device instance.

`one:GetSite` Let you fetch the information about an Amazon One Enterprise site.

`one:GetSiteAddress` Let you fetch the physical address of an Amazon One Enterprise site.

`one:ListDeviceInstances` Let you list the Amazon One device instances.

`one:ListSites` Let you list the Amazon One Enterprise sites.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "InstallerAccessStatementID",
 "Effect": "Allow",
 "Action": [
 "one:CreateDeviceActivationQrCode",
 "one:GetDeviceInstance",
 "one:GetSite",
 "one:GetSiteAddress",
 "one:ListDeviceInstances",
 "one:ListSites"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Amazon One Enterprise updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon One Enterprise that have been made
since this service began tracking these changes. For automatic alerts about changes to this
page, subscribe to the RSS feed on the Amazon One Enterprise Document history page.

| Change                                                   | Description                                                                                                                                                            | Date             |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Amazon One Enterprise added AmazonOneMetricPublishAccess | The role permissions policy named AmazonOneMetricPublishAccess allows Amazon One Enterprise to perform CloudWatch:PutMetricData on CloudWatch Namespace AWS/AmazonOne. | February 6, 2025 |
| Amazon One Enterprise started tracking changes           | Amazon One Enterprise started tracking changes for its AWS managed policies.                                                                                           | December 1, 2023 |
