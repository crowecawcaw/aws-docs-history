# IAM: View

service last accessed information for an AWS Organizations policy

This example shows how you might create an identity-based policy that allows viewing service last accessed information for a specific
AWS Organizations policy. This policy allows retrieving data for the service control policy (SCP) with
the `p-policy123` ID. The person who generates and views the report must be
authenticated using AWS Organizations management account credentials. This policy allows the requester
to retrieve the data for any AWS Organizations entity in their
organization. This policy defines permissions for programmatic and console access. To use this policy, replace the `italicized placeholder text` in the example policy with your own information.
Then, follow the directions in [create a policy](access_policies_create.md "access_policies_create.md") or [edit a policy](access_policies_manage-edit.md "access_policies_manage-edit.md").

For important information about last accessed information, including permissions required,
troubleshooting, and supported Regions, see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowOrgsReadOnlyAndIamGetReport",
 "Effect": "Allow",
 "Action": [
 "iam:GetOrganizationsAccessReport",
 "organizations:Describe*",
 "organizations:List*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowGenerateReportOnlyForThePolicy",
 "Effect": "Allow",
 "Action": "iam:GenerateOrganizationsAccessReport",
 "Resource": "*",
 "Condition": {
 "StringEquals": {"iam:OrganizationsPolicyId": "`p-policy123`"}
 }
 }
 ]
}`

```
