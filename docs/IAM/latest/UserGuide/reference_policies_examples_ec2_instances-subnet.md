# Amazon EC2: Allows launching EC2

instances in a specific subnet, programmatically and in the console

This example shows how you might create an identity-based policy that allows listing information for all EC2 objects and launching EC2
instances in a specific subnet. This policy defines permissions for programmatic and console access. To use this policy, replace the `italicized placeholder text` in the example policy with your own information.
Then, follow the directions in [create a policy](access_policies_create.md "access_policies_create.md") or [edit a policy](access_policies_manage-edit.md "access_policies_manage-edit.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:Describe*",
 "ec2:GetConsole*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`*`:`*`:subnet/subnet-`subnet-id`",
 "arn:aws:ec2:`*`:`*`:network-interface/*",
 "arn:aws:ec2:`*`:`*`:instance/*",
 "arn:aws:ec2:`*`:`*`:volume/*",
 "arn:aws:ec2:`*`::image/ami-*",
 "arn:aws:ec2:`*`:`*`:key-pair/*",
 "arn:aws:ec2:`*`:`*`:security-group/*"
 ]
 }
 ]
}`

```
