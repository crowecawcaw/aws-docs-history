# Amazon EC2: Allows full EC2 access within a

specific Region, programmatically and in the console

This example shows how you might create an identity-based policy that allows full EC2 access within a specific Region.
This policy defines permissions for programmatic and console access. To use this policy, replace the `italicized placeholder text` in the example policy with your own information.
Then, follow the directions in [create a policy](access_policies_create.md "access_policies_create.md") or [edit a policy](access_policies_manage-edit.md "access_policies_manage-edit.md"). For a list of Region codes, see [Available
Regions](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-available-regions "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-available-regions") in the _Amazon EC2 User Guide_.

Alternatively, you can use the global condition key [`aws:RequestedRegion`](reference_policies_condition-keys.md#condition-keys-requestedregion "reference_policies_condition-keys.md#condition-keys-requestedregion"), which is supported by all Amazon EC2 API actions. For
more information, see [Example: Restricting access to a specific Region](../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region "../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region") in the _Amazon EC2 User
Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "ec2:*",
 "Resource": "*",
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "ec2:Region": "`us-east-2`"
 }
 }
 }
 ]
}`

```
