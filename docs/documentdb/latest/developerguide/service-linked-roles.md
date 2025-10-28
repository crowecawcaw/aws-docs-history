# Understanding service-linked roles

Amazon DocumentDB (with MongoDB compatibility) uses AWS Identity and Access Management (IAM) service-linked roles. A [service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") is a unique type
of IAM role that is linked directly to Amazon DocumentDB. Service-linked roles are predefined by Amazon DocumentDB and include all the permissions that the service requires
to call other AWS services on your behalf.

A service-linked role makes using Amazon DocumentDB easier because you don’t have to manually add the necessary permissions. Amazon DocumentDB defines the permissions of
its service-linked roles, and unless defined otherwise, only Amazon DocumentDB can assume its roles. The defined permissions include the trust policy and the
permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete the roles only after first deleting their related resources. This protects your Amazon DocumentDB resources because you can't inadvertently remove
permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the
services that have **Yes** in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Amazon DocumentDB service-linked role permissions

Amazon DocumentDB (with MongoDB compatibility) uses the service-linked role named **AWSServiceRoleForRDS** to allow Amazon DocumentDB to call AWS services on behalf of your clusters.

The AWSServiceRoleForRDS service-linked role trusts the following services to assume the role:

- `docdb.amazonaws.com`

The role permissions policy allows Amazon DocumentDB to complete the following actions on the specified resources:

- Actions on `ec2`:
  - `AssignPrivateIpAddresses`
  - `AuthorizeSecurityGroupIngress`
  - `CreateNetworkInterface`
  - `CreateSecurityGroup`
  - `DeleteNetworkInterface`
  - `DeleteSecurityGroup`
  - `DescribeAvailabilityZones`
  - `DescribeInternetGateways`
  - `DescribeSecurityGroups`
  - `DescribeSubnets`
  - `DescribeVpcAttribute`
  - `DescribeVpcs`
  - `ModifyNetworkInterfaceAttribute`
  - `RevokeSecurityGroupIngress`
  - `UnassignPrivateIpAddresses`

- Actions on `sns`:
  - `ListTopic`
  - `Publish`

- Actions on `cloudwatch`:
  - `PutMetricData`
  - `GetMetricData`
  - `CreateLogStream`
  - `PullLogEvents`
  - `DescribeLogStreams`
  - `CreateLogGroup`

###### Note

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. You
might encounter the following error message:

**Unable to create the resource. Verify that you have permission to create service linked role. Otherwise wait and try again
later.**

If you see this error, ensure that you have the following permissions enabled:

```
{
    "Action": "iam:CreateServiceLinkedRole",
    "Effect": "Allow",
    "Resource": "arn:aws:iam::*:role/aws-service-role/rds.amazonaws.com/AWSServiceRoleForRDS",
    "Condition": {
        "StringLike": {
            "iam:AWSServiceName":"rds.amazonaws.com"
        }
    }
}
```

For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating an Amazon DocumentDB service-linked role

You don't need to manually create a service-linked role. When you create a cluster, Amazon DocumentDB creates the service-linked role for you.

If you delete this service-linked role and then need to create it again, you can use the same process to re-create the role in your account. When
you create a cluster, Amazon DocumentDB creates the service-linked role for you again.

## Modifying an Amazon DocumentDB service-linked role

Amazon DocumentDB does not allow you to modify the AWSServiceRoleForRDS service-linked role. After you create a service-linked role, you cannot change the name of the
role because various entities might reference the role. However, you can modify the description of the role using IAM. For more information, see
[Editing a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in
the _IAM User Guide_.

## Deleting an Amazon DocumentDB service-linked role

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t
have an unused entity that is not actively monitored or maintained. However, you must delete all of your clusters before you can delete the
service-linked role.

### Cleaning up an Amazon DocumentDB service-linked role

Before you can use IAM to delete a service-linked role, you must first confirm that the role has no active sessions and remove any resources used
by the role.

###### To check whether the service-linked role has an active session using the console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**, and then choose the name (not the check box) of the
   **AWSServiceRoleForRDS** role.
3. On the **Summary** page for the selected role, choose the **Access Advisor** tab.
4. On the **Access Advisor** tab, review the recent activity for the service-linked role.

###### Note

If you are unsure whether Amazon DocumentDB is using the AWSServiceRoleForRDS role, you can try to delete the role. If the service is using the role, then
the deletion fails and you can view the Regions where the role is being used. If the role is being used, then you must wait for the session
to end before you can delete the role. You cannot revoke the session for a service-linked role.

If you want to remove the AWSServiceRoleForRDS role, you must first delete _all_ your instances and clusters. For information about
deleting instances and clusters, see the following topics:

- [Deleting an Amazon DocumentDB instance](db-instance-delete.md "db-instance-delete.md")
- [Deleting an Amazon DocumentDB cluster](db-cluster-delete.md "db-cluster-delete.md")

## Supported regions for Amazon DocumentDB service-linked roles

Amazon DocumentDB supports using service-linked roles in all of the Regions where the service is available. For more information, see [https://docs.aws.amazon.com/documentdb/latest/developerguide/regions-and-azs.html#regions-and-azs-availability](regions-and-azs.md#regions-and-azs-availability "regions-and-azs.md#regions-and-azs-availability").
