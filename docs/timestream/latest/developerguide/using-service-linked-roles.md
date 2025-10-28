For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Using service-linked roles for

Amazon Timestream for InfluxDB

Amazon Timestream for InfluxDB uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to an AWS service, such as Amazon Timestream for InfluxDB. Amazon Timestream for InfluxDB service-linked roles are
predefined by Amazon Timestream for InfluxDB. They include all the permissions that the service requires to call
AWS services on behalf of your dbinstances.

A service-linked role makes setting up Amazon Timestream for InfluxDB easier because you don’t have to
manually add the necessary permissions. The roles already exist within your AWS account but
are linked to Amazon Timestream for InfluxDB use cases and have predefined permissions. Only Amazon Timestream for InfluxDB can
assume these roles, and only these roles can use the predefined permissions policy. You can
delete the roles only after first deleting their related resources. This protects your
Amazon Timestream for InfluxDB resources because you can't inadvertently remove necessary permissions to access
the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that
have **Yes** in the **Service-Linked
Role** column. Choose a **Yes** with a link to view the
service-linked role documentation for that service.

###### Contents

- [Service-Linked Role Permissions](using-service-linked-roles.md#service-linked-role-permissions "using-service-linked-roles.md#service-linked-role-permissions")
- [Creating a Service-Linked Role (IAM)](using-service-linked-roles.md#create-service-linked-role-iam "using-service-linked-roles.md#create-service-linked-role-iam")
- [Editing a Service-Linked Role Description](using-service-linked-roles.md#edit-service-linked-role "using-service-linked-roles.md#edit-service-linked-role")
  - [Using the IAM Console](using-service-linked-roles.md#edit-service-linked-role-iam-console "using-service-linked-roles.md#edit-service-linked-role-iam-console")
  - [Using the IAM CLI](using-service-linked-roles.md#edit-service-linked-role-iam-cli "using-service-linked-roles.md#edit-service-linked-role-iam-cli")
  - [Using the IAM API](using-service-linked-roles.md#edit-service-linked-role-iam-api "using-service-linked-roles.md#edit-service-linked-role-iam-api")

- [Deleting a Service-Linked Role for Amazon Timestream for InfluxDB](using-service-linked-roles.md#delete-service-linked-role "using-service-linked-roles.md#delete-service-linked-role")
  - [Cleaning Up a Service-Linked Role](using-service-linked-roles.md#service-linked-role-review-before-delete "using-service-linked-roles.md#service-linked-role-review-before-delete")
  - [Deleting a Service-Linked Role (IAM Console)](using-service-linked-roles.md#delete-service-linked-role-iam-console "using-service-linked-roles.md#delete-service-linked-role-iam-console")
  - [Deleting a Service-Linked Role (IAM CLI)](using-service-linked-roles.md#delete-service-linked-role-iam-cli "using-service-linked-roles.md#delete-service-linked-role-iam-cli")
  - [Deleting a Service-Linked Role (IAM API)](using-service-linked-roles.md#delete-service-linked-role-iam-api "using-service-linked-roles.md#delete-service-linked-role-iam-api")

- [Supported Regions for Amazon Timestream for InfluxDB Service-Linked Roles](using-service-linked-roles.md#supported-regions "using-service-linked-roles.md#supported-regions")

## Service-Linked Role Permissions for Amazon Timestream for InfluxDB

Amazon Timestream for InfluxDB uses the service-linked role named **AmazonTimestreamInfluxDBServiceRolePolicy** –
This policy allows Timestream for InfluxDB to manage AWS resources on your behalf as necessary for managing your clusters.

The AmazonTimestreamInfluxDBServiceRolePolicy service-linked role permissions policy allows Amazon Timestream for InfluxDB to complete the
following actions on the specified resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DescribeNetworkStatement",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeNetworkInterfaces"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CreateEniInSubnetStatement",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*"
 ]
 },
 {
 "Sid": "CreateEniStatement",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "Null": {
 "aws:RequestTag/AmazonTimestreamInfluxDBManaged": "false"
 }
 }
 },
 {
 "Sid": "CreateTagWithEniStatement",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "Null": {
 "aws:RequestTag/AmazonTimestreamInfluxDBManaged": "false"
 },
 "StringEquals": {
 "ec2:CreateAction": [
 "CreateNetworkInterface"
 ]
 }
 }
 },
 {
 "Sid": "ManageEniStatement",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "Null": {
 "aws:ResourceTag/AmazonTimestreamInfluxDBManaged": "false"
 }
 }
 },
 {
 "Sid": "PutCloudWatchMetricsStatement",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/Timestream/InfluxDB",
 "AWS/Usage"
 ]
 }
 },
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ManageSecretStatement",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:CreateSecret",
 "secretsmanager:DeleteSecret"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:READONLY-InfluxDB-auth-parameters-*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

**To allow an IAM entity to create AmazonTimestreamInfluxDBServiceRolePolicy service-linked
roles**

Add the following policy statement to the permissions for that IAM entity:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:CreateServiceLinkedRole",
        "iam:PutRolePolicy"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/timestreamforinfluxdb.amazonaws.com/AmazonTimestreamInfluxDBServiceRolePolicy*",
    "Condition": {"StringLike": {"iam:AWSServiceName": "timestreamforinfluxdb.amazonaws.com"}}
}
```

**To allow an IAM entity to delete AmazonTimestreamInfluxDBServiceRolePolicy service-linked
roles**

Add the following policy statement to the permissions for that IAM entity:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:DeleteServiceLinkedRole",
        "iam:GetServiceLinkedRoleDeletionStatus"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/timestreamforinfluxdb.amazonaws.com/AmazonTimestreamInfluxDBServiceRolePolicy*",
    "Condition": {"StringLike": {"iam:AWSServiceName": "timestreamforinfluxdb.amazonaws.com"}}
}
```

Alternatively, you can use an AWS managed policy to provide full access to
Amazon Timestream for InfluxDB.

## Creating a Service-Linked Role (IAM)

You don't need to manually create a service-linked role. When you create a DB instance, Amazon Timestream for InfluxDB creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create a DB instance, Amazon Timestream for InfluxDB creates the service-linked role for you again.

## Editing the Description of a Service-Linked Role for Amazon Timestream for InfluxDB

Amazon Timestream for InfluxDB does not allow you to edit the AmazonTimestreamInfluxDBServiceRolePolicy service-linked role. After you
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

1. (Optional) To view the current description for a role, use the AWS CLI for IAM
   operation `get-role`.

```
`$` `aws iam get-role --role-name AmazonTimestreamInfluxDBServiceRolePolicy`
```

Use the role name, not the ARN, to refer to roles with the CLI operations. For
example, if a role has the following ARN:
`arn:aws:iam::123456789012:role/myrole`, refer to the role as `myrole`. 2. To update a service-linked role's description, use the AWS CLI for IAM operation `update-role-description`.

**Linux and MacOS**

```
`$` `aws iam update-role-description \
 --role-name AmazonTimestreamInfluxDBServiceRolePolicy \
 --description "`new description`"`
```

**Windows**

```
`$` `aws iam update-role-description ^
 --role-name AmazonTimestreamInfluxDBServiceRolePolicy ^
 --description "`new description`"`
```

### Editing a Service-Linked Role Description (IAM API)

You can use the IAM API to edit a service-linked role description.

###### To change the description of a service-linked role (API)

1. (Optional) To view the current description for a role, use the IAM API operation GetRole.

```
https://iam.amazonaws.com/
   ?Action=GetRole
   &RoleName=AmazonTimestreamInfluxDBServiceRolePolicy
   &Version=2010-05-08
   &AUTHPARAMS
```

2. To update a role's description, use the IAM API operation UpdateRoleDescription.

```
https://iam.amazonaws.com/
   ?Action=UpdateRoleDescription
   &RoleName=AmazonTimestreamInfluxDBServiceRolePolicy
   &Version=2010-05-08
   &Description="`New description`"
```

## Deleting a Service-Linked Role for Amazon Timestream for InfluxDB

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up your service-linked role before
you can delete it.

Amazon Timestream for InfluxDB does not delete the service-linked role for you.

### Cleaning Up a Service-Linked Role

Before you can use IAM to delete a service-linked role, first
confirm that the role has no resources (clusters) associated with
it.

###### To check whether the service-linked role has an active session in the IAM console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane of the IAM console, choose **Roles**. Then
   choose the name (not the check box) of the AmazonTimestreamInfluxDBServiceRolePolicy role.
3. On the **Summary** page for the selected role, choose the
   **Access Advisor** tab.
4. On the **Access Advisor** tab, review recent activity for the
   service-linked role.

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
associated resources, you must submit a deletion request with the
[delete-service-linked-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-linked-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-linked-role.html")
command. That request can be denied if these conditions are not met. You must capture
the `deletion-task-id` from the response to check the status of the deletion
task. Enter the following to submit a service-linked role deletion request.

```
`$` `aws iam delete-service-linked-role --role-name `role-name``
```

3. Run the [get-service-linked-role-deletion-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-linked-role-deletion-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-linked-role-deletion-status.html")
   command to check the status of the deletion task.

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

## Supported Regions for Amazon Timestream for InfluxDB Service-Linked Roles

Amazon Timestream for InfluxDB supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS service endpoints](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md").
