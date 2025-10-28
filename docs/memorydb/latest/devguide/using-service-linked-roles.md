# Using Service-Linked Roles for

MemoryDB

MemoryDB uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to an AWS service, such as MemoryDB. MemoryDB service-linked roles are
predefined by MemoryDB. They include all the permissions that the service requires to call
AWS services on behalf of your clusters.

A service-linked role makes setting up MemoryDB easier because you don’t have to
manually add the necessary permissions. The roles already exist within your AWS account but
are linked to MemoryDB use cases and have predefined permissions. Only MemoryDB can
assume these roles, and only these roles can use the predefined permissions policy. You can
delete the roles only after first deleting their related resources. This protects your
MemoryDB resources because you can't inadvertently remove necessary permissions to access
the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that
have **Yes** in the **Service-Linked
Role** column. Choose a **Yes** with a link to view the
service-linked role documentation for that service.

###### Contents

- [Service-Linked Role Permissions](using-service-linked-roles.md#service-linked-role-permissions "using-service-linked-roles.md#service-linked-role-permissions")
- [Creating a Service-Linked Role (IAM)](using-service-linked-roles.md#create-service-linked-role-iam "using-service-linked-roles.md#create-service-linked-role-iam")
  - [Using the IAM Console](using-service-linked-roles.md#create-service-linked-role-iam-console "using-service-linked-roles.md#create-service-linked-role-iam-console")
  - [Using the IAM CLI](using-service-linked-roles.md#create-service-linked-role-iam-cli "using-service-linked-roles.md#create-service-linked-role-iam-cli")
  - [Using the IAM API](using-service-linked-roles.md#create-service-linked-role-iam-api "using-service-linked-roles.md#create-service-linked-role-iam-api")

- [Editing a Service-Linked Role Description](using-service-linked-roles.md#edit-service-linked-role "using-service-linked-roles.md#edit-service-linked-role")
  - [Using the IAM Console](using-service-linked-roles.md#edit-service-linked-role-iam-console "using-service-linked-roles.md#edit-service-linked-role-iam-console")
  - [Using the IAM CLI](using-service-linked-roles.md#edit-service-linked-role-iam-cli "using-service-linked-roles.md#edit-service-linked-role-iam-cli")
  - [Using the IAM API](using-service-linked-roles.md#edit-service-linked-role-iam-api "using-service-linked-roles.md#edit-service-linked-role-iam-api")

- [Deleting a Service-Linked Role for MemoryDB](using-service-linked-roles.md#delete-service-linked-role "using-service-linked-roles.md#delete-service-linked-role")
  - [Cleaning Up a Service-Linked Role](using-service-linked-roles.md#service-linked-role-review-before-delete "using-service-linked-roles.md#service-linked-role-review-before-delete")
  - [Deleting a Service-Linked Role (IAM Console)](using-service-linked-roles.md#delete-service-linked-role-iam-console "using-service-linked-roles.md#delete-service-linked-role-iam-console")
  - [Deleting a Service-Linked Role (IAM CLI)](using-service-linked-roles.md#delete-service-linked-role-iam-cli "using-service-linked-roles.md#delete-service-linked-role-iam-cli")
  - [Deleting a Service-Linked Role (IAM API)](using-service-linked-roles.md#delete-service-linked-role-iam-api "using-service-linked-roles.md#delete-service-linked-role-iam-api")

## Service-Linked Role Permissions for MemoryDB

MemoryDB uses the service-linked role named **AWSServiceRoleForMemoryDB** –
This policy allows MemoryDB to manage AWS resources on your behalf as necessary for managing your clusters.

The AWSServiceRoleForMemoryDB service-linked role permissions policy allows MemoryDB to complete the
following actions on the specified resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws-cn:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateNetworkInterface"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "AmazonMemoryDBManaged"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws-cn:ec2:*:*:network-interface/*",
 "arn:aws-cn:ec2:*:*:subnet/*",
 "arn:aws-cn:ec2:*:*:security-group/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteNetworkInterface",
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": "arn:aws-cn:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/AmazonMemoryDBManaged": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteNetworkInterface",
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": "arn:aws-cn:ec2:*:*:security-group/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/MemoryDB"
 }
 }
 }
 ]
}`

```

For more information, see [AWS managed policy: MemoryDBServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-memorydbServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-memorydbServiceRolePolicy").

**To allow an IAM entity to create AWSServiceRoleForMemoryDB service-linked
roles**

Add the following policy statement to the permissions for that IAM entity:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:CreateServiceLinkedRole",
        "iam:PutRolePolicy"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/memorydb.amazonaws.com/AWSServiceRoleForMemoryDB*",
    "Condition": {"StringLike": {"iam:AWSServiceName": "memorydb.amazonaws.com"}}
}
```

**To allow an IAM entity to delete AWSServiceRoleForMemoryDB service-linked
roles**

Add the following policy statement to the permissions for that IAM entity:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:DeleteServiceLinkedRole",
        "iam:GetServiceLinkedRoleDeletionStatus"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/memorydb.amazonaws.com/AWSServiceRoleForMemoryDB*",
    "Condition": {"StringLike": {"iam:AWSServiceName": "memorydb.amazonaws.com"}}
}
```

Alternatively, you can use an AWS managed policy to provide full access to
MemoryDB.

## Creating a Service-Linked Role (IAM)

You can create a service-linked role using the IAM console, CLI, or API.

### Creating a Service-Linked Role (IAM Console)

You can use the IAM console to create a service-linked role.

###### To create a service-linked role (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane of the IAM console, choose **Roles**. Then
   choose **Create new role**.
3. Under **Select type of trusted entity** choose **AWS Service**.
4. Under **Or select a service to view its use cases**, choose **MemoryDB**.
5. Choose **Next: Permissions**.
6. Under **Policy name**, note that the `MemoryDBServiceRolePolicy` is required for this role. Choose **Next:Tags**.
7. Note that tags are not supported for Service-Linked roles. Choose **Next:Review**.
8. (Optional) For **Role description**, edit the description for the
   new service-linked role.
9. Review the role and then choose **Create role**.

### Creating a Service-Linked Role (IAM CLI)

You can use IAM operations from the AWS Command Line Interface to create a service-linked role. This
role can include the trust policy and inline policies that the service needs to assume the
role.

**To create a service-linked role (CLI)**

Use the following operation:

```
`$` `aws iam create-service-linked-role --aws-service-name `memorydb.amazonaws.com``
```

### Creating a Service-Linked Role (IAM API)

You can use the IAM API to create a service-linked role. This role can contain the
trust policy and inline policies that the service needs to assume the role.

**To create a service-linked role (API)**

Use the CreateServiceLinkedRole API call.
In the request, specify a service name of `memorydb.amazonaws.com`.

## Editing the Description of a Service-Linked Role for MemoryDB

MemoryDB does not allow you to edit the AWSServiceRoleForMemoryDB service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using
IAM.

### Editing a Service-Linked Role Description (IAM Console)

You can use the IAM console to edit a service-linked role description.

###### To edit the description of a service-linked role (console)

1. In the left navigation pane of the IAM console, choose
   **Roles**.
2. Choose the name of the role to modify.
3. To the far right of **Role description**, choose
   **Edit**.
4. Enter a new description in the box and choose **Save**.

### Editing a Service-Linked Role Description (IAM CLI)

You can use IAM operations from the AWS Command Line Interface to edit a service-linked role description.

###### To change the description of a service-linked role (CLI)

1. (Optional) To view the current description for a role, use the AWS CLI for IAM operation `get-role`.

```
`$` `aws iam get-role --role-name AWSServiceRoleForMemoryDB`
```

Use the role name, not the ARN, to refer to roles with the CLI operations. For
example, if a role has the following ARN:
`arn:aws:iam::123456789012:role/myrole`, refer to the role as `myrole`. 2. To update a service-linked role's description, use the AWS CLI for IAM operation `update-role-description`.

For Linux, macOS, or Unix:

```
`$` `aws iam update-role-description \
 --role-name AWSServiceRoleForMemoryDB \
 --description "`new description`"`
```

For Windows:

```
`$` `aws iam update-role-description ^
 --role-name AWSServiceRoleForMemoryDB ^
 --description "`new description`"`
```

### Editing a Service-Linked Role Description (IAM API)

You can use the IAM API to edit a service-linked role description.

###### To change the description of a service-linked role (API)

1. (Optional) To view the current description for a role, use the IAM API operation GetRole.

```
https://iam.amazonaws.com/
   ?Action=GetRole
   &RoleName=`AWSServiceRoleForMemoryDB`
   &Version=2010-05-08
   &AUTHPARAMS
```

2. To update a role's description, use the IAM API operation UpdateRoleDescription.

```
https://iam.amazonaws.com/
   ?Action=UpdateRoleDescription
   &RoleName=`AWSServiceRoleForMemoryDB`
   &Version=2010-05-08
   &Description="`New description`"
```

## Deleting a Service-Linked Role for MemoryDB

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up your service-linked role before
you can delete it.

MemoryDB does not delete the service-linked role for you.

### Cleaning Up a Service-Linked Role

Before you can use IAM to delete a service-linked role, first
confirm that the role has no resources (clusters) associated with
it.

###### To check whether the service-linked role has an active session in the IAM console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane of the IAM console, choose **Roles**. Then
   choose the name (not the check box) of the AWSServiceRoleForMemoryDB role.
3. On the **Summary** page for the selected role, choose the
   **Access Advisor** tab.
4. On the **Access Advisor** tab, review recent activity for the
   service-linked role.

###### To delete MemoryDB resources that require AWSServiceRoleForMemoryDB (console)

- To delete a cluster, see the following:
  - [Using the AWS Management Console](getting-started.md#clusters.deleteclusters.viewdetails "getting-started.md#clusters.deleteclusters.viewdetails")
  - [Using the AWS CLI](getting-started.md#clusters.delete.cli "getting-started.md#clusters.delete.cli")
  - [Using the MemoryDB API](getting-started.md#clusters.delete.api "getting-started.md#clusters.delete.api")

### Deleting a Service-Linked Role (IAM Console)

You can use the IAM console to delete a service-linked role.

###### To delete a service-linked role (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane of the IAM console, choose **Roles**. Then
   select the check box next to the role name that you want to delete, not the name or row
   itself.
3. For **Role actions** at the top of the page, choose
   **Delete role**.
4. In the confirmation page, review the service last accessed data, which shows
   when each of the selected roles last accessed an AWS service. This helps you to
   confirm whether the role is currently active. If you want to proceed, choose
   **Yes, Delete** to submit the service-linked role for
   deletion.
5. Watch the IAM console notifications to monitor the progress of the service-linked
   role deletion. Because the IAM service-linked role deletion is asynchronous, after you
   submit the role for deletion, the deletion task can succeed or fail. If the task fails,
   you can choose **View details** or **View Resources**
   from the notifications to learn why the deletion failed.

### Deleting a Service-Linked Role (IAM CLI)

You can use IAM operations from the AWS Command Line Interface to delete a service-linked role.

###### To delete a service-linked role (CLI)

1. If you don't know the name of the service-linked role that you want to delete, enter
   the following command. This command lists the roles and their Amazon Resource Names
   (ARNs) in your account.

```
`$` `aws iam get-role --role-name `role-name``
```

Use the role name, not the ARN, to refer to roles with the CLI operations. For
example, if a role has the ARN `arn:aws:iam::123456789012:role/myrole`,
you refer to the role as `myrole`. 2. Because a service-linked role cannot be deleted if it is being used or has
associated resources, you must submit a deletion request. That request can be denied if
these conditions are not met. You must capture the `deletion-task-id` from
the response to check the status of the deletion task. Enter the following to submit a
service-linked role deletion request.

```
`$` `aws iam delete-service-linked-role --role-name `role-name``
```

3. Enter the following to check the status of the deletion task.

```
`$` `aws iam get-service-linked-role-deletion-status --deletion-task-id `deletion-task-id``
```

The status of the deletion task can be `NOT_STARTED`,
`IN_PROGRESS`, `SUCCEEDED`, or `FAILED`. If the
deletion fails, the call returns the reason that it failed so that you can
troubleshoot.

### Deleting a Service-Linked Role (IAM API)

You can use the IAM API to delete a service-linked role.

###### To delete a service-linked role (API)

1. To submit a deletion request for a service-linked roll, call DeleteServiceLinkedRole.
   In the request, specify a role name.

Because a service-linked role cannot be deleted if it is being used or has
associated resources, you must submit a deletion request. That request can be denied if
these conditions are not met. You must capture the `DeletionTaskId` from the
response to check the status of the deletion task. 2. To check the status of the deletion, call GetServiceLinkedRoleDeletionStatus.
In the request, specify the `DeletionTaskId`.

The status of the deletion task can be `NOT_STARTED`,
`IN_PROGRESS`, `SUCCEEDED`, or `FAILED`. If the
deletion fails, the call returns the reason that it failed so that you can
troubleshoot.
