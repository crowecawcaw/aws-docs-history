# AWS: Allows

enabling and disabling AWS Regions

This example shows how you might create an identity-based policy that allows an administrator to enable and disable the Asia Pacific
(Hong Kong) Region (ap-east-1). This policy defines permissions for programmatic and console access. This setting appears in the
**Account settings** page in the AWS Management Console. This page includes
sensitive account-level information that should be viewed and managed only by account
administrators. To use this policy, replace the `italicized placeholder text` in the example policy with your own information.
Then, follow the directions in [create a policy](access_policies_create.md "access_policies_create.md") or [edit a policy](access_policies_manage-edit.md "access_policies_manage-edit.md").

###### Important

You cannot enable or disable regions that are enabled by default. You can only include
regions that are _disabled_ by default. For more
information, see [Managing AWS
Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in the _AWS General Reference_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnableDisableHongKong",
 "Effect": "Allow",
 "Action": [
 "account:EnableRegion",
 "account:DisableRegion"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {"account:TargetRegion": "`ap-east-1`"}
 }
 },
 {
 "Sid": "ViewConsole",
 "Effect": "Allow",
 "Action": [
 "account:ListRegions"
 ],
 "Resource": "*"
 }
 ]
}`

```
