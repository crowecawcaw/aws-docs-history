# Replicating EFS file systems across AWS

accounts

You can replicate EFS file systems across AWS accounts. Replicating across
accounts enhances the overall resilience and reliability of your disaster recovery (DR)
strategies and can help you meet corporate compliance mandates.

For example, you might be required by compliance policies to use different accounts for
different environments (such as production, staging, and disaster recovery (DR)). Or you may
find that replication across different AWS accounts provides stronger isolation, more granular
control over permissions and access policies, and more straightforward auditing of resources. If
the production account is compromised (such as by security breaches, misconfiguration, or
insider threats), having the DR servers in a separate account can prevent the attacker from
accessing them, reduce the blast radius of security incidents, and minimize the risk of
unauthorized changes.

Replicating across AWS accounts requires additional security and policy setup. Instead of
using service-linked roles to perform cross-account replication, you must create an IAM role
that gives Amazon EFS permission to perform replication in the destination account. You also need to
create policies on the file systems that you want to share across accounts. After the IAM role
and file system policies are created, you create the replication configuration.

###### Topics

- [Create an IAM role with a custom trust
  policy](#replication-create-iam-role "#replication-create-iam-role")
- [Create policies on the source and destination
  file systems](#replication-assign-fs-policies "#replication-assign-fs-policies")
- [Create the replication configuration](#xar-create-replication-configuration "#xar-create-replication-configuration")

## Create an IAM role with a custom trust

policy

For Amazon EFS to perform cross-account replication on the source account’s behalf, an IAM
role must be created on the source account. The role must have the
`elasticfilesystem.amazonaws.com` trust policy to allow Amazon EFS to assume the role
and act as the service principal. The role must contain all of the IAM permissions required
to perform replication (see [Required IAM permissions](efs-replication.md#efs-replication-permissions "efs-replication.md#efs-replication-permissions")) and grant explicit permission to replicate to
the file system in the destination account.

### Prerequisites

You must create both the source file system and the destination file system in the
replication configuration before you can create the IAM role for the source account. Amazon EFS
cannot create the destination file system for you during replication. Additionally, you must
know and provide the Amazon Resource Name (ARN) for each file system.

###### To create the IAM role

for cross-account replication

The following are the general steps for creating an IAM role with custom trust
policies for cross-account replication with Amazon EFS. For step-by-step instructions for
creating an IAM role, see [Create a role using custom
trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the _AWS Identity and Access Management User Guide_.

1. In the AWS Identity and Access Management console for the source account, create an IAM role that uses the following
   trust policy. For instructions, see [Create a role using custom
   trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the _AWS Identity and Access Management User
   Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "elasticfilesystem.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. After you create the role, assign the following permissions for the role. Replace
   `arn:aws:elasticfilesystem:`us-east-1`:`111122223333`:file-system/fs-0123456789abcdef1`
   with the ARN of the destination file system and replace
   `arn:aws:elasticfilesystem:`us-east-1`:`444455556666`:file-system/fs-5678910112hijkqr1`
   with the ARN of the source file system. For instructions on assigning
   permissions to the role, see [Creating policies using the JSON editor](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action":[
 "elasticfilesystem:DescribeFileSystems",
 "elasticfilesystem:CreateReplicationConfiguration",
 "elasticfilesystem:DescribeReplicationConfigurations",
 "elasticfilesystem:DeleteReplicationConfiguration",
 "elasticfilesystem:ReplicationWrite"
 ],
 "Resource": "arn:aws:elasticfilesystem:`us-east-1`:`111122223333`:file-system/fs-0123456789abcdef1"
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticfilesystem:ReplicationRead",
 "elasticfilesystem:DescribeFileSystems"
 ],
 "Resource": "arn:aws:elasticfilesystem:`us-east-1`:`444455556666`:file-system/fs-5678910112hijkqr1"
 }
 ]
}`

```

3. Copy or write down the ARN for the IAM role. You need to provide the ARN
   when you create the replication configuration.

## Create policies on the source and destination

file systems

To share file systems cross-account in Amazon EFS, you must assign policies to both the
destination and source file systems. The policies grant or restrict access across accounts to
the file system to which they are applied. Only account owners with permission to edit file
systems can assign policies to the file system in their account.

In addition to granting or restricting access across accounts, the policies need to grant
other permissions required for clients to work with the file systems, such as
`elasticfilesystem:ClientMount`. Otherwise, the file system might be inaccessible
to clients.

###### Important

You cannot restrict access to resources over TLS connection. If you include the
`"aws:SecureTransport": "false"` condition in your statement, the NFS client
connection will fail.

#### Policy for the destination file

system

To allow the source account permission to replicate to the destination file system and
to delete the replication configuration from the destination account, the following policy
must be created on the destination file system. Replace
`arn:aws:iam::`444455556666`:root` with
the ID of the account that owns the source file system. Replace
`arn:aws:elasticfilesystem:`us-east-1`:`111122223333`:file-system/fs-0123456789abcdef1`
with the ARN of the destination file system

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSourceAccountReplicationActions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`444455556666`:root"
 },
 "Action": [
 "elasticfilesystem:DescribeFileSystems",
 "elasticfilesystem:CreateReplicationConfiguration",
 "elasticfilesystem:DescribeReplicationConfigurations",
 "elasticfilesystem:DeleteReplicationConfiguration",
 "elasticfilesystem:ReplicationWrite"
 ],
 "Resource": "arn:aws:elasticfilesystem:`us-east-1`:`111122223333`:file-system/fs-0123456789abcdef1"
 },
 {
 "Sid": "AllowReadOnlyClientAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`arn:aws:iam::111122223333:role/EfsReadOnly`"
 },
 "Action": [
 "elasticfilesystem:ClientMount"
 ],
 "Resource": "arn:aws:elasticfilesystem:`us-east-1`:`111122223333`:file-system/fs-0123456789abcdef1"
 }
 ]
}`

```

#### Policy for the source file

system

To allow the destination account permission to delete the replication configuration
from the source account, you must assign the following policy to the source file system.
Replace `arn:aws:iam::`111122223333`:root`
with the ID of the account that owns the destination file system. Replace `arn:aws:elasticfilesystem:`us-east-1`:`444455556666`:file-system/fs-5678910112hijkqr1`
with the ARN of the source file system.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "efs-policy-wizard-15ad9567-2546-4bbb-8168-5541b6fc0e55",
 "Statement": [
 {
 "Sid": "AllowDestinationAccountToDeleteReplication",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "elasticfilesystem:DeleteReplicationConfiguration",
 "Resource": "arn:aws:elasticfilesystem:`us-east-1`:`444455556666`:file-system/fs-5678910112hijkqr1"
 },
 {
 "Sid": "AllowClientAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`arn:aws:iam::111122223333:role/EfsReadOnly`"
 },
 "Action": [
 "elasticfilesystem:ClientMount",
 "elasticfilesystem:ClientWrite",
 "elasticfilesystem:ClientRootAccess"
 ],
 "Resource": "arn:aws:elasticfilesystem:`us-east-1`:`444455556666`:file-system/fs-5678910112hijkqr1",
 "Condition": {
 "Bool": {
 "elasticfilesystem:AccessedViaMountTarget": "true"
 }
 }
 }
 ]
}`

```

###### To create the file system policy

Perform the following steps for both the destination and source file system, using the
policies in the previous section.

1. Sign in to the AWS Management Console with the account that owns the file system, and then open the
   Amazon EFS console at [Amazon EFS Console](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. Open the file system:
   1. In the left navigation pane, choose **File systems**.
   2. In the **File systems** list, choose the file system.

3. On the **File system policy** tab, choose
   **Edit**.
4. Paste the policy in **Policy editor {Json}** and then choose
   **Save**.

## Create the replication configuration

After you have created the IAM role and added the file system policies to the source
and destination file systems, follow the instructions in [Configuring replication to an existing
EFS file system](replicate-existing-destination.md "replicate-existing-destination.md") to
create the replication configuration.
