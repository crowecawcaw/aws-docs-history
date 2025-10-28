# Control access to Amazon Data Lifecycle Manager using IAM

Access to Amazon Data Lifecycle Manager requires credentials. Those credentials must have permissions to access
AWS resources, such as instances, volumes, snapshots, and AMIs.

The following IAM permissions are required to use Amazon Data Lifecycle Manager.

###### Note

- The `ec2:DescribeAvailabilityZones`, `ec2:DescribeRegions`,
  `kms:ListAliases`, and `kms:DescribeKey` permissions are
  required for console users only. If console access is not required, you can remove
  the permissions.
- The ARN format of the _AWSDataLifecycleManagerDefaultRole_ role
  differs depending on whether it was created using the console or the AWS CLI. If the
  role was created using the console, the ARN format is
  `arn:aws:iam::`account_id`:role/service-role/AWSDataLifecycleManagerDefaultRole`.
  If the role was created using the AWS CLI, the ARN format is
  `arn:aws:iam::`account_id`:role/AWSDataLifecycleManagerDefaultRole`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "dlm:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::`111122223333`:role/AWSDataLifecycleManagerDefaultRole",
 "arn:aws:iam::`111122223333`:role/AWSDataLifecycleManagerDefaultRoleForAMIManagement",
 "arn:aws:iam::`111122223333`:role/service-role/AWSDataLifecycleManagerDefaultRole",
 "arn:aws:iam::`111122223333`:role/service-role/AWSDataLifecycleManagerDefaultRoleForAMIManagement"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeRegions",
 "kms:ListAliases",
 "kms:DescribeKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Permissions for encryption

Consider the following when working with Amazon Data Lifecycle Manager and encrypted resources.

- If the source volume is encrypted, ensure that the Amazon Data Lifecycle Manager default roles
  (**AWSDataLifecycleManagerDefaultRole** and
  **AWSDataLifecycleManagerDefaultRoleForAMIManagement**)
  have permission to use the KMS keys used to encrypt the volume.
- If you enable **Cross Region copy** for
  unencrypted snapshots or AMIs backed by unencrypted snapshots, and choose
  to enable encryption in the destination Region, ensure that the default
  roles have permission to use the KMS key needed to perform the encryption
  in the destination Region.
- If you enable **Cross Region copy** for
  encrypted snapshots or AMIs backed by encrypted snapshots, ensure that the
  default roles have permission to use both the source and destination
  KMS keys.
- If you enable snapshot archiving for encrypted snapshots, ensure that
  the Amazon Data Lifecycle Manager default role (**AWSDataLifecycleManagerDefaultRole**
  has permission to use the KMS key used to encrypt the snapshot.
  For more information, see [Allowing users
  in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the _AWS Key Management Service Developer Guide_.

For more information, see [Changing
permissions for a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") in the _IAM User Guide_.
