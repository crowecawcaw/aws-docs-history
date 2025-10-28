# Service-linked role permissions for Amazon Inspector agentless scans

Amazon Inspector agentless scanning uses the service-linked role named `AWSServiceRoleForAmazonInspector2Agentless`. This SLR allows Amazon Inspector to create an Amazon EBS volume snapshot in your account, and then access the data from that snapshot. This
service-linked role trusts the `agentless.inspector2.amazonaws.com` service to assume the
role.

###### Important

The statements in this service-linked role prevent Amazon Inspector from performing agentless scans on any EC2 instance that you have excluded from scans using the `InspectorEc2Exclusion` tag. Additionally the statements prevent Amazon Inspector from accessing encrypted data from a volume when the KMS key used to encrypt it has the `InspectorEc2Exclusion` tag. For more information, see [Excluding instances from Amazon Inspector scans](scanning-ec2.md#exclude-ec2 "scanning-ec2.md#exclude-ec2").

The permissions policy for the role, which is named `AmazonInspector2AgentlessServiceRolePolicy`, allows
Amazon Inspector to perform tasks such as:

- Use Amazon Elastic Compute Cloud (Amazon EC2) actions to retrieve information about your EC2 instances, volumes, and snapshots.
  - Use Amazon EC2 tagging actions to tag snapshots for scans with the `InspectorScan` tag key.
  - Use Amazon EC2 snapshot actions to create snapshots, tag them with the `InspectorScan` tag key, and then delete snapshots of Amazon EBS volumes that have been tagged with the `InspectorScan` tag key.

- Use Amazon EBS actions to retrieve information from snapshots tagged with the `InspectorScan` tag key.
- Use select AWS KMS decryption actions to decrypt snapshots encrypted with AWS KMS customer managed keys. Amazon Inspector does not decrypt snapshots when the KMS key used to encrypt them is tagged with the `InspectorEc2Exclusion` tag.
  The role is configured with the following permissions policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "InstanceIdentification",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeVolumes",
 "ec2:DescribeSnapshots"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GetSnapshotData",
 "Effect": "Allow",
 "Action": [
 "ebs:ListSnapshotBlocks",
 "ebs:GetSnapshotBlock"
 ],
 "Resource": "arn:aws:ec2:*:*:snapshot/*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/InspectorScan": "*"
 }
 }
 },
 {
 "Sid": "CreateSnapshotsAnyInstanceOrVolume",
 "Effect": "Allow",
 "Action": "ec2:CreateSnapshots",
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ec2:*:*:volume/*"
 ]
 },
 {
 "Sid": "DenyCreateSnapshotsOnExcludedInstances",
 "Effect": "Deny",
 "Action": "ec2:CreateSnapshots",
 "Resource": "arn:aws:ec2:*:*:instance/*",
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/InspectorEc2Exclusion": "true"
 }
 }
 },
 {
 "Sid": "CreateSnapshotsOnAnySnapshotOnlyWithTag",
 "Effect": "Allow",
 "Action": "ec2:CreateSnapshots",
 "Resource": "arn:aws:ec2:*:*:snapshot/*",
 "Condition": {
 "Null": {
 "aws:TagKeys": "false"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "InspectorScan"
 }
 }
 },
 {
 "Sid": "CreateOnlyInspectorScanTagOnlyUsingCreateSnapshots",
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "arn:aws:ec2:*:*:snapshot/*",
 "Condition": {
 "StringLike": {
 "ec2:CreateAction": "CreateSnapshots"
 },
 "Null": {
 "aws:TagKeys": "false"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "InspectorScan"
 }
 }
 },
 {
 "Sid": "DeleteOnlySnapshotsTaggedForScanning",
 "Effect": "Allow",
 "Action": "ec2:DeleteSnapshot",
 "Resource": "arn:aws:ec2:*:*:snapshot/*",
 "Condition": {
 "StringLike": {
 "ec2:ResourceTag/InspectorScan": "*"
 }
 }
 },
 {
 "Sid": "DenyKmsDecryptForExcludedKeys",
 "Effect": "Deny",
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:*:*:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/InspectorEc2Exclusion": "true"
 }
 }
 },
 {
 "Sid": "DecryptSnapshotBlocksVolContext",
 "Effect": "Allow",
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:*:*:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 },
 "StringLike": {
 "kms:ViaService": "ec2.*.amazonaws.com",
 "kms:EncryptionContext:aws:ebs:id": "vol-*"
 }
 }
 },
 {
 "Sid": "DecryptSnapshotBlocksSnapContext",
 "Effect": "Allow",
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:*:*:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 },
 "StringLike": {
 "kms:ViaService": "ec2.*.amazonaws.com",
 "kms:EncryptionContext:aws:ebs:id": "snap-*"
 }
 }
 },
 {
 "Sid": "DescribeKeysForEbsOperations",
 "Effect": "Allow",
 "Action": "kms:DescribeKey",
 "Resource": "arn:aws:kms:*:*:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 },
 "StringLike": {
 "kms:ViaService": "ec2.*.amazonaws.com"
 }
 }
 },
 {
 "Sid": "ListKeyResourceTags",
 "Effect": "Allow",
 "Action": "kms:ListResourceTags",
 "Resource": "arn:aws:kms:*:*:key/*"
 }
 ]
}`

```
