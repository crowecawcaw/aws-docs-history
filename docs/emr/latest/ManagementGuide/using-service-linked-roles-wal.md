# Using service-linked roles with Amazon EMR for write-ahead

logging

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

You can delete this service-linked role for Amazon EMR only after you delete their related
resources and terminate all EMR clusters in the account. This protects your Amazon EMR
resources so that you can't inadvertently remove permission to access the resources.

## Service-linked role permissions

for write-ahead logging (WAL)

Amazon EMR uses the service-linked role **AWSServiceRoleForEMRWAL** to retrieve
a cluster status.

The AWSServiceRoleForEMRWAL service-linked role trusts the following services to assume the
role:

- `emrwal.amazonaws.com`

The [EMRDescribeClusterPolicyForEMRWAL](EMRDescribeClusterPolicyForEMRWAL.md "EMRDescribeClusterPolicyForEMRWAL.md") permissions policy for the
service-linked role allows Amazon EMR to complete the following actions on the specified
resources:

- Action: `DescribeCluster` on `*`

You must configure permissions to allow an IAM entity (in this case, Amazon EMR WAL) to
create, edit, or delete a service-linked role. Add the following statements as needed to the
permissions policy for your instance profile:

**To allow an IAM entity to create the AWSServiceRoleForEMRWAL
service-linked role**

Add the following statement to the permissions policy for the IAM entity that needs
to create the service-linked role:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:CreateServiceLinkedRole",
        "iam:PutRolePolicy"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/emrwal.amazonaws.com*/AWSServiceRoleForEMRWAL*",
    "Condition": {
        "StringLike": {
            "iam:AWSServiceName": [
                "emrwal.amazonaws.com",
                "elasticmapreduce.amazonaws.com.cn"
            ]
        }
    }
}
```

**To allow an IAM entity to edit the description of the
AWSServiceRoleForEMRWAL service-linked role**

Add the following statement to the permissions policy for the IAM entity that needs
to edit the description of a service-linked role:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:UpdateRoleDescription"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/emrwal.amazonaws.com*/AWSServiceRoleForEMRWAL*",
    "Condition": {
        "StringLike": {
            "iam:AWSServiceName": [
                "emrwal.amazonaws.com",
                "elasticmapreduce.amazonaws.com.cn"
            ]
        }
    }
}
```

**To allow an IAM entity to delete the AWSServiceRoleForEMRWAL
service-linked role**

Add the following statement to the permissions policy for the IAM entity that needs
to delete a service-linked role:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:DeleteServiceLinkedRole",
        "iam:GetServiceLinkedRoleDeletionStatus"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/elasticmapreduce.amazonaws.com*/AWSServiceRoleForEMRCleanup*",
    "Condition": {
        "StringLike": {
            "iam:AWSServiceName": [
                "emrwal.amazonaws.com",
                "elasticmapreduce.amazonaws.com.cn"
            ]
        }
    }
}
```

## Creating a service-linked role for

Amazon EMR

You don't need to manually create the AWSServiceRoleForEMRWAL role. Amazon EMR creates this
service-linked role automatically when you create a WAL workspace with the EMRWAL CLI or
from AWS CloudFormation, or HBase will create the service-linked role when you configure a workspace
for Amazon EMR WAL and the service-linked role doesn't yet exist. You must have permissions to
create a service-linked role. For example statements that add this capability to the
permissions policy of an IAM entity (such as a user, group, or role), see the prior
section, [Service-linked role permissions
for write-ahead logging (WAL)](#using-service-linked-roles-permissions-wal "#using-service-linked-roles-permissions-wal").

## Editing a service-linked role for

Amazon EMR

Amazon EMR doesn't allow you to edit the AWSServiceRoleForEMRWAL service-linked role. After you
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

###### Note

The write-ahead logging operation isn't affected if you delete the AWSServiceRoleForEMRWAL role,
but Amazon EMR won't auto-delete the logs that it created once your EMR cluster terminates.
Therefore, you'll need to manually delete the Amazon EMR WAL logs if you delete the
service-linked role.

### Cleaning up a service-linked

role

Before you can use IAM to delete a service-linked role, you must first confirm that
the role has no active sessions and remove any resources used by the role.

###### To check whether the service-linked role has an active session in the IAM

console

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**. Select the name (not
   the check box) of the AWSServiceRoleForEMRWAL role.
3. On the **Summary** page for the selected role, choose
   **Access Advisor**.
4. On the **Access Advisor** tab, review the recent activity for the
   service-linked role.

###### Note

If you are unsure whether Amazon EMR is using the AWSServiceRoleForEMRWAL role, you can
try to delete the service-linked role. If the service is using the role, then the
deletion fails and you can view the Regions where the service-linked role is being
used. If the service-linked role is being used, then you must wait for the session
to end before you can delete the service-linked role. You cannot revoke the session
for a service-linked role.

###### To remove Amazon EMR resources used by the AWSServiceRoleForEMRWAL

- Terminate all clusters in your account. For more information, see [Terminate an Amazon EMR cluster in the starting, running, or waiting states](UsingEMR_TerminateJobFlow.md "UsingEMR_TerminateJobFlow.md").

### Deleting a service-linked role

(IAM console)

You can use the IAM console to delete a service-linked role.

###### To delete a service-linked role (console)

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**. Select the check box
   next to AWSServiceRoleForEMRWAL, not the name or row itself.
3. For **Role actions** at the top of the page, choose
   **Delete role**.
4. In the confirmation dialog box, review the service last accessed data, which shows
   when each of the selected roles last accessed an AWS service. This helps you to
   confirm whether the role is currently active. To proceed, choose **Yes,
   Delete**.
5. Watch the IAM console notifications to monitor the progress of the
   service-linked role deletion. Because the IAM service-linked role deletion is
   asynchronous, after you submit the role for deletion, the deletion task can succeed or
   fail. If the task fails, you can choose **View details** or
   **View Resources** from the notifications to learn why the deletion
   failed. If the deletion fails because there are resources in the service that are
   being used by the role, then the reason for the failure includes a list of
   resources.

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
`$` `aws iam delete-service-linked-role --role-name AWSServiceRoleForEMRWAL`
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
   In the request, specify the AWSServiceRoleForEMRWAL role name.

To check the status of the deletion task, you must capture the
`DeletionTaskId` from the response. 2. To check the status of the deletion, call [GetServiceLinkedRoleDeletionStatus](../../../IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.md "../../../IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.md"). In the request, specify the
`DeletionTaskId`.

The status of the deletion task can be `NOT_STARTED`,
`IN_PROGRESS`, `SUCCEEDED`, or `FAILED`. If the
deletion fails, the call returns the reason that it failed so that you can
troubleshoot.

## Supported Regions for AWSServiceRoleForEMRWAL

Amazon EMR supports using the AWSServiceRoleForEMRWAL service-linked role in the following
Regions.

| Region name              | Region identity | Support in Amazon EMR |
| ------------------------ | --------------- | --------------------- |
| US East (N. Virginia)    | us-east-1       | Yes                   |
| US East (Ohio)           | us-east-2       | Yes                   |
| US West (N. California)  | us-west-1       | Yes                   |
| US West (Oregon)         | us-west-2       | Yes                   |
| Asia Pacific (Mumbai)    | ap-south-1      | Yes                   |
| Asia Pacific (Singapore) | ap-southeast-1  | Yes                   |
| Asia Pacific (Sydney)    | ap-southeast-2  | Yes                   |
| Asia Pacific (Tokyo)     | ap-northeast-1  | Yes                   |
| Europe (Frankfurt)       | eu-central-1    | Yes                   |
| Europe (Ireland)         | eu-west-1       | Yes                   |
