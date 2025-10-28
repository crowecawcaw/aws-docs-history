# Amazon EC2: Attach or detach Amazon EBS

volumes to EC2 instances based on tags

This example shows how you might create an identity-based policy that allows EBS volume owners to attach or detach their EBS volumes
defined using the tag `VolumeUser` to EC2 instances that are tagged as
development instances (`Department=Development`). This policy grants the permissions necessary to complete this action programmatically from the AWS API or AWS CLI.
To use this policy, replace the `italicized placeholder text` in the example policy with your own information.
Then, follow the directions in [create a policy](access_policies_create.md "access_policies_create.md") or [edit a policy](access_policies_manage-edit.md "access_policies_manage-edit.md").

For more information about creating IAM
policies to control access to Amazon EC2 resources, see [Controlling Access to Amazon EC2 Resources](../../../AWSEC2/latest/UserGuide/UsingIAM.md "../../../AWSEC2/latest/UserGuide/UsingIAM.md") in the
_Amazon EC2 User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AttachVolume",
 "ec2:DetachVolume"
 ],
 "Resource": "arn:aws:ec2:*:*:instance/*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/`Department`": "`Development`"}
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AttachVolume",
 "ec2:DetachVolume"
 ],
 "Resource": "arn:aws:ec2:*:*:volume/*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/`VolumeUser`": "${aws:username}"}
 }
 }
 ]
}`

```
