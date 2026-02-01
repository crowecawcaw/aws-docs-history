• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Controlling access to

Fleet Manager

To use Fleet Manager, a tool in AWS Systems Manager, your AWS Identity and Access Management (IAM) user or role must
have the required permissions. You can create an IAM policy that provides access
to all Fleet Manager features, or modify your policy to grant access to the features you
choose. You then grant these permissions to users, or identities, in your
account.

**Task 1: Create IAM policies to define access
permissions**

Follow one of the methods provided in the followig topic in the
_IAM User Guide_ to create an IAM to provide
identities (users, roles, or user groupss) with access to
Fleet Manager:

- [Define custom IAM permissions with customer managed
  policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md")

You can use one of the sample policies we provide below, or modify
them according to the permissions you want to grant. We provide sample
policies for full Fleet Manager access and read-only access.

**Task 2: Attach the IAM policies to users to grant
permissions**

After you have created the IAM policy or policies that define access
permissions to Fleet Manager, use one of the following procedures in the
_IAM User Guide_ to grant these permissions to
identities in your account:

- [Adding IAM identity permissions (console)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console")
- [Adding IAM identity permissions (AWS CLI)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policy-cli "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policy-cli")
- [Adding IAM identity permissions (AWS
  API)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policy-api "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policy-api")

###### Topics

- [Sample policy for Fleet Manager administrator
  access](#admin-policy-sample "#admin-policy-sample")
- [Sample policy for Fleet Manager read-only
  access](#read-only-policy-sample "#read-only-policy-sample")

## Sample policy for Fleet Manager administrator

access

The following policy provides permissions to all Fleet Manager features. This means
a user can create and delete local users and groups, modify group membership for
any local group, and modify Windows Server registry keys or values. Replace each
`example resource placeholder` with your own
information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EC2",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags",
 "ec2:DeleteTags",
 "ec2:DescribeInstances",
 "ec2:DescribeTags"
 ],
 "Resource": "*"
 },
 {
 "Sid": "General",
 "Effect": "Allow",
 "Action": [
 "ssm:AddTagsToResource",
 "ssm:DescribeInstanceAssociationsStatus",
 "ssm:DescribeInstancePatches",
 "ssm:DescribeInstancePatchStates",
 "ssm:DescribeInstanceProperties",
 "ssm:GetCommandInvocation",
 "ssm:GetServiceSetting",
 "ssm:GetInventorySchema",
 "ssm:ListComplianceItems",
 "ssm:ListInventoryEntries",
 "ssm:ListTagsForResource",
 "ssm:ListCommandInvocations",
 "ssm:ListAssociations",
 "ssm:RemoveTagsFromResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DefaultHostManagement",
 "Effect": "Allow",
 "Action": [
 "ssm:ResetServiceSetting",
 "ssm:UpdateServiceSetting"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/`service-role/AWSSystemsManagerDefaultEC2InstanceManagementRole`",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "ssm.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "SendCommand",
 "Effect": "Allow",
 "Action": [
 "ssm:GetDocument",
 "ssm:SendCommand",
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ec2:*:`111122223333`:instance/*",
 "arn:aws:ssm:*:`111122223333`:managed-instance/*",
 "arn:aws:ssm:*:`111122223333`:document/SSM-SessionManagerRunShell",
 "arn:aws:ssm:*:*:document/AWS-PasswordReset",
 "arn:aws:ssm:*:*:document/AWSFleetManager-AddUsersToGroups",
 "arn:aws:ssm:*:*:document/AWSFleetManager-CopyFileSystemItem",
 "arn:aws:ssm:*:*:document/AWSFleetManager-CreateDirectory",
 "arn:aws:ssm:*:*:document/AWSFleetManager-CreateGroup",
 "arn:aws:ssm:*:*:document/AWSFleetManager-CreateUser",
 "arn:aws:ssm:*:*:document/AWSFleetManager-CreateUserInteractive",
 "arn:aws:ssm:*:*:document/AWSFleetManager-CreateWindowsRegistryKey",
 "arn:aws:ssm:*:*:document/AWSFleetManager-DeleteFileSystemItem",
 "arn:aws:ssm:*:*:document/AWSFleetManager-DeleteGroup",
 "arn:aws:ssm:*:*:document/AWSFleetManager-DeleteUser",
 "arn:aws:ssm:*:*:document/AWSFleetManager-DeleteWindowsRegistryKey",
 "arn:aws:ssm:*:*:document/AWSFleetManager-DeleteWindowsRegistryValue",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetDiskInformation",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetFileContent",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetFileSystemContent",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetGroups",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetPerformanceCounters",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetProcessDetails",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetUsers",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetWindowsEvents",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetWindowsRegistryContent",
 "arn:aws:ssm:*:*:document/AWSFleetManager-MountVolume",
 "arn:aws:ssm:*:*:document/AWSFleetManager-MoveFileSystemItem",
 "arn:aws:ssm:*:*:document/AWSFleetManager-RemoveUsersFromGroups",
 "arn:aws:ssm:*:*:document/AWSFleetManager-RenameFileSystemItem",
 "arn:aws:ssm:*:*:document/AWSFleetManager-SetWindowsRegistryValue",
 "arn:aws:ssm:*:*:document/AWSFleetManager-StartProcess",
 "arn:aws:ssm:*:*:document/AWSFleetManager-TerminateProcess"
 ]
 },
 {
 "Sid": "TerminateSession",
 "Effect": "Allow",
 "Action": [
 "ssm:TerminateSession"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "ssm:resourceTag/aws:ssmmessages:session-id": [
 "${aws:userid}"
 ]
 }
 }
 }
 ]
}`

```

## Sample policy for Fleet Manager read-only

access

The following policy provides permissions to read-only Fleet Manager features.
Replace each `example resource placeholder` with
your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EC2",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeTags"
 ],
 "Resource": "*"
 },
 {
 "Sid": "General",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeInstanceAssociationsStatus",
 "ssm:DescribeInstancePatches",
 "ssm:DescribeInstancePatchStates",
 "ssm:DescribeInstanceProperties",
 "ssm:GetCommandInvocation",
 "ssm:GetServiceSetting",
 "ssm:GetInventorySchema",
 "ssm:ListComplianceItems",
 "ssm:ListInventoryEntries",
 "ssm:ListTagsForResource",
 "ssm:ListCommandInvocations",
 "ssm:ListAssociations"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SendCommand",
 "Effect": "Allow",
 "Action": [
 "ssm:GetDocument",
 "ssm:SendCommand",
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ec2:*:`111122223333`:instance/*",
 "arn:aws:ssm:*:`111122223333`:managed-instance/*",
 "arn:aws:ssm:*:`111122223333`:document/SSM-SessionManagerRunShell",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetDiskInformation",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetFileContent",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetFileSystemContent",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetGroups",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetPerformanceCounters",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetProcessDetails",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetUsers",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetWindowsEvents",
 "arn:aws:ssm:*:*:document/AWSFleetManager-GetWindowsRegistryContent"
 ]
 },
 {
 "Sid": "TerminateSession",
 "Effect": "Allow",
 "Action": [
 "ssm:TerminateSession"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "ssm:resourceTag/aws:ssmmessages:session-id": [
 "${aws:userid}"
 ]
 }
 }
 }
 ]
}`

```
