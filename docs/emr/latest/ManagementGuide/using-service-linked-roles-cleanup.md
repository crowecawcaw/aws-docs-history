# Using service-linked roles for Amazon EMR for

cleanup

Amazon EMR uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon EMR. Service-linked roles are predefined by Amazon EMR and
include all the permissions that the service requires to call other AWS services on your
behalf.

Service-linked roles work together with the Amazon EMR service role and Amazon EC2 instance profile
for Amazon EMR. For more information about the service role and instance profile, see [Configure IAM service roles for Amazon EMR permissions to AWS
services and resources](emr-iam-roles.md "emr-iam-roles.md").

A service-linked role makes setting up Amazon EMR easier because you don’t have to
manually add the necessary permissions. Amazon EMR defines the permissions of its
service-linked roles, and unless defined otherwise, only Amazon EMR can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete this service-linked role for Amazon EMR only after you delete any related
resources and terminate all EMR clusters in the account. This protects your Amazon EMR
resources so that you can't inadvertently remove permission to access the resources.

## Using service-linked roles

for cleanup

Amazon EMR uses the service-based **AWSServiceRoleForEMRCleanup** role to grant Amazon EMR
permission to terminate and delete Amazon EC2 resources on your behalf if the Amazon EMR
service-linked role loses that capability. Amazon EMR creates the service-linked role
automatically during cluster creation if it doesn't already exist.

The AWSServiceRoleForEMRCleanup service-linked role trusts the following services to assume the
role:

- `elasticmapreduce.amazonaws.com`

The AWSServiceRoleForEMRCleanup service-linked role permissions policy allows Amazon EMR to complete
the following actions on the specified resources:

- Action: `DescribeInstances` on `ec2`
- Action: `DescribeLaunchTemplates` on
  `ec2`
- Action: `DeleteLaunchTemplate` on
  `ec2`
- Action: `DescribeSpotInstanceRequests` on
  `ec2`
- Action: `ModifyInstanceAttribute` on
  `ec2`
- Action: `TerminateInstances` on
  `ec2`
- Action: `CancelSpotInstanceRequests` on
  `ec2`
- Action: `DeleteNetworkInterface` on
  `ec2`
- Action: `DescribeInstanceAttribute` on
  `ec2`
- Action: `DescribeVolumeStatus` on
  `ec2`
- Action: `DescribeVolumes` on `ec2`
- Action: `DetachVolume` on `ec2`
- Action: `DeleteVolume` on `ec2`
- Action: `DescribePlacementGroups` on `ec2`
- Action: `DeletePlacementGroup` on `ec2`

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role.

## Creating a service-linked role for

Amazon EMR

You don't need to manually create the AWSServiceRoleForEMRCleanup role. When you launch a cluster, either
for the first time or when the AWSServiceRoleForEMRCleanup service-linked role is not present, Amazon EMR
creates the AWSServiceRoleForEMRCleanup service-linked role for you. You must have permissions to create a
service-linked role. For an example statement that adds this capability to the permissions
policy of an IAM entity (such as a user, group, or role):

Add the following statement to the permissions policy for the IAM entity that needs to
create the service-linked role.

```
{
             "Sid": "ElasticMapReduceServiceLinkedRole",
             "Effect": "Allow",
             "Action": "iam:CreateServiceLinkedRole",
             "Resource": "arn:aws:iam::*:role/aws-service-role/elasticmapreduce.amazonaws.com*/AWSServiceRoleForEMRCleanup*",
             "Condition": {
                 "StringEquals": {
                     "iam:AWSServiceName": [
                         "elasticmapreduce.amazonaws.com",
                         "elasticmapreduce.amazonaws.com.cn"
                     ]
                 }
             }
 }
```

###### Important

If you used Amazon EMR before October 24, 2017, when service-linked roles weren't
supported, then Amazon EMR created the AWSServiceRoleForEMRCleanup service-linked role in your account.
For more information, see [A new
role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

## Editing a service-linked role for

Amazon EMR

Amazon EMR doesn't allow you to edit the AWSServiceRoleForEMRCleanup service-linked role. After you
create a service-linked role, you can't change the name of the service-linked role because
various entities might reference the service-linked role. However, you can edit the
description of the service-linked role using IAM.

### Editing a service-linked role

description (IAM console)

You can use the IAM console to edit the description of a service-linked role.

###### To edit the description of a service-linked role (console)

1. In the navigation pane of the IAM console, choose
   **Roles**.
2. Choose the name of the role to modify.
3. To the right of the **Role description**, choose
   **Edit**.
4. Enter a new description in the box and choose **Save changes**.

### Editing a service-linked role

description (IAM CLI)

You can use IAM commands from the AWS Command Line Interface to edit the description of a
service-linked role.

###### To change the description of a service-linked role (CLI)

1. (Optional) To view the current description for a role, use the following
   commands:

```
`$` `aws iam get-role --role-name `role-name``
```

Use the role name, not the ARN, to refer to roles with the CLI commands. For
example, if a role has the following ARN:
`arn:aws:iam::123456789012:role/myrole`, you refer to the role as
`myrole`. 2. To update a service-linked role's description, use one of the following
commands:

```
`$` `aws iam update-role-description --role-name `role-name` --description `description``
```

### Editing a service-linked role

description (IAM API)

You can use the IAM API to edit the description of a service-linked role.

###### To change the description of a service-linked role (API)

1. (Optional) To view the current description for a role, use the following
   command:

IAM API: [GetRole](../../../IAM/latest/APIReference/API_GetRole.md "../../../IAM/latest/APIReference/API_GetRole.md") 2. To update a role's description, use the following command:

IAM API: [UpdateRoleDescription](../../../IAM/latest/APIReference/API_UpdateRoleDescription.md "../../../IAM/latest/APIReference/API_UpdateRoleDescription.md")

## Deleting a service-linked role for

Amazon EMR

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that service-linked role. That way, you don't have an unused
entity that is not being actively monitored or maintained. However, you must clean up your
service-linked role before you can delete it.

### Cleaning up a service-linked

role

Before you can use IAM to delete a service-linked role, you must first confirm that
the service-linked role has no active sessions and remove any resources used by the
service-linked role.

###### To check whether the service-linked role has an active session in the IAM

console

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**. Select the name (not
   the check box) of the AWSServiceRoleForEMRCleanup service-linked role.
3. On the **Summary** page for the selected service-linked role,
   choose **Access Advisor**.
4. On the **Access Advisor** tab, review the recent activity for the
   service-linked role.

###### Note

If you are unsure whether Amazon EMR is using the AWSServiceRoleForEMRCleanup service-linked
role, you can try to delete the service-linked role. If the service is using the
service-linked role, then the deletion fails and you can view the Regions where the
service-linked role is being used. If the service-linked role is being used, then
you must wait for the session to end before you can delete the service-linked role.
You cannot revoke the session for a service-linked role.

###### To remove Amazon EMR resources used by the AWSServiceRoleForEMRCleanup

- Terminate all clusters in your account. For more information, see [Terminate an Amazon EMR cluster in the starting, running, or waiting states](UsingEMR_TerminateJobFlow.md "UsingEMR_TerminateJobFlow.md").

### Deleting a service-linked role

(IAM console)

You can use the IAM console to delete a service-linked role.

###### To delete a service-linked role (console)

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**. Select the check box
   next to AWSServiceRoleForEMRCleanup, not the name or row itself.
3. For **Role actions** at the top of the page, choose
   **Delete role**.
4. In the confirmation dialog box, review the service last accessed data, which shows
   when each of the selected roles last accessed an AWS service. This helps you to
   confirm whether the role is currently active. To proceed, choose **Yes,
   Delete**.
5. Watch the IAM console notifications to monitor the progress of the
   service-linked role deletion. Because the IAM service-linked role deletion is
   asynchronous, after you submit the service-linked role for deletion, the deletion task
   can succeed or fail. If the task fails, you can choose **View
   details** or **View Resources** from the notifications to
   learn why the deletion failed. If the deletion fails because there are resources in
   the service that are being used by the role, then the reason for the failure includes
   a list of resources.

### Deleting a service-linked role (IAM

CLI)

You can use IAM commands from the AWS Command Line Interface to delete a service-linked role. Because
a service-linked role cannot be deleted if it is being used or has associated resources,
you must submit a deletion request. If these conditions are not met, that request can be
denied.

###### To delete a service-linked role (CLI)

1. To check the status of the deletion task, you must capture the
   `deletion-task-id` from the response. Type the following command to
   submit a service-linked role deletion request:

```
`$` `aws iam delete-service-linked-role --role-name AWSServiceRoleForEMRCleanup`
```

2. Type the following command to check the status of the deletion task:

```
`$` `aws iam get-service-linked-role-deletion-status --deletion-task-id `deletion-task-id``
```

The status of the deletion task can be `NOT_STARTED`,
`IN_PROGRESS`, `SUCCEEDED`, or `FAILED`. If the
deletion fails, the call returns the reason that it failed so that you can
troubleshoot.

### Deleting a service-linked role (IAM

API)

You can use the IAM API to delete a service-linked role. Because a service-linked
role cannot be deleted if it is being used or has associated resources, you must submit a
deletion request. If these conditions are not met, that request can be denied.

###### To delete a service-linked role (API)

1. To submit a deletion request for a service-linked role, call [DeleteServiceLinkedRole](../../../IAM/latest/APIReference/API_DeleteServiceLinkedRole.md "../../../IAM/latest/APIReference/API_DeleteServiceLinkedRole.md").
   In the request, specify the AWSServiceRoleForEMRCleanup role name.

To check the status of the deletion task, you must capture the
`DeletionTaskId` from the response. 2. To check the status of the deletion, call [GetServiceLinkedRoleDeletionStatus](../../../IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.md "../../../IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.md"). In the request, specify the
`DeletionTaskId`.

The status of the deletion task can be `NOT_STARTED`,
`IN_PROGRESS`, `SUCCEEDED`, or `FAILED`. If the
deletion fails, the call returns the reason that it failed so that you can
troubleshoot.

## Supported Regions for AWSServiceRoleForEMRCleanup

Amazon EMR supports using the AWSServiceRoleForEMRCleanup service-linked role in the following
Regions.

| Region name               | Region identity | Support in Amazon EMR |
| ------------------------- | --------------- | --------------------- |
| US East (N. Virginia)     | us-east-1       | Yes                   |
| US East (Ohio)            | us-east-2       | Yes                   |
| US West (N. California)   | us-west-1       | Yes                   |
| US West (Oregon)          | us-west-2       | Yes                   |
| Asia Pacific (Mumbai)     | ap-south-1      | Yes                   |
| Asia Pacific (Osaka)      | ap-northeast-3  | Yes                   |
| Asia Pacific (Seoul)      | ap-northeast-2  | Yes                   |
| Asia Pacific (Singapore)  | ap-southeast-1  | Yes                   |
| Asia Pacific (Sydney)     | ap-southeast-2  | Yes                   |
| Asia Pacific (Tokyo)      | ap-northeast-1  | Yes                   |
| Canada (Central)          | ca-central-1    | Yes                   |
| Europe (Frankfurt)        | eu-central-1    | Yes                   |
| Europe (Ireland)          | eu-west-1       | Yes                   |
| Europe (London)           | eu-west-2       | Yes                   |
| Europe (Paris)            | eu-west-3       | Yes                   |
| South America (São Paulo) | sa-east-1       | Yes                   |
