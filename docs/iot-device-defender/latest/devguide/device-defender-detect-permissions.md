# Permissions

This section contains information about how to set up the IAM roles and policies
required to manage AWS IoT Device Defender Detect. For more information, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

## Give AWS IoT Device Defender detect

permission to publish alarms to an SNS topic

If you use the `alertTargets` parameter in [CreateSecurityProfile](../../../iot/latest/apireference/API_CreateSecurityProfile.md "../../../iot/latest/apireference/API_CreateSecurityProfile.md"), you must specify an IAM role with
two policies: a permissions policy and a trust policy. The permissions policy grants
permission to AWS IoT Device Defender to publish notifications to your SNS topic. The trust policy grants
AWS IoT Device Defender permission to assume the required role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sns:Publish"
 ],
 "Resource": [
 "arn:aws:sns:us-east-1:111122223333:`your-topic-name`"
 ]
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "iot.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

You also need an IAM permissions policy attached to the IAM user that allows the
user to pass roles. See [Granting a User
Permissions to Pass a Role to an AWS Service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::111122223333:role/Role_To_Pass"
 }
 ]
}`

```
