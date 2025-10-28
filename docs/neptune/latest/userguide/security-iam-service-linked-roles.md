# Using service-linked roles for Amazon Neptune

Amazon Neptune uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Neptune. Service-linked roles are predefined by Neptune and
include all the permissions that the service requires to call other AWS services on your
behalf.

###### Important

For certain management features, Amazon Neptune uses operational technology
that is shared with Amazon RDS. This includes the _service-linked role_ and
management API permissions.

A service-linked role makes using Neptune easier because you don’t have to manually
add the necessary permissions. Neptune defines the permissions of its service-linked
roles, and unless defined otherwise, only Neptune can assume its roles. The defined
permissions include the trust policy and the permissions policy, and that permissions policy
cannot be attached to any other IAM entity.

You can delete the roles only after first deleting their related resources. This protects
your Neptune resources because you can't inadvertently remove permission to access the
resources.

For information about other services that support service-linked roles, see [AWS Services That Work
with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"), and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

## Service-Linked Role Permissions for

Neptune

Neptune uses the `AWSServiceRoleForRDS` service-linked role to allow
Neptune and Amazon RDS to call AWS services on behalf of your database instances. The
`AWSServiceRoleForRDS` service-linked role trusts the
`rds.amazonaws.com` service to assume the role.

The role permissions policy allows Neptune to complete the following actions on
the specified resources:

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

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. You might encounter the following error
message:

**`Unable to create the resource. Verify that you have permission to create
 service linked role. Otherwise wait and try again later.`**

If you see this message, make sure that you have the following permissions enabled:

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

## Creating a Service-Linked Role for Neptune

You don't need to manually create a service-linked role. When you create an
instance or a cluster, Neptune creates the service-linked role for you.

###### Important

To learn more, see [A New
Role Appeared in My IAM Account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared") in the _IAM User Guide_.

If you delete this service-linked role and then need to create it again, you can use the
same process to re-create the role in your account. When you create an instance or a cluster,
Neptune creates the service-linked role for you again.

## Editing a Service-Linked Role for Neptune

Neptune does not allow you to edit the `AWSServiceRoleForRDS` service-linked
role. After you create a service-linked role, you cannot change the name of the role because
various entities might reference the role. However, you can edit the description of the role
using IAM. For more information, see [Editing a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a Service-Linked Role for Neptune

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must delete all of your instances and
clusters before you can delete the associated service-linked role.

### Cleaning Up a Service-Linked Role Before Deleting

Before you can use IAM to delete a service-linked role, you must first confirm that
the role has no active sessions and remove any resources used by the role.

###### To check whether the service-linked role has an active session in the IAM

console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**. Then choose
   the name (not the check box) of the `AWSServiceRoleForRDS` role.
3. On the **Summary** page for the selected role, choose the
   **Access Advisor** tab.
4. On the **Access Advisor** tab, review recent activity for the
   service-linked role.

###### Note

If you are unsure whether Neptune is using the `AWSServiceRoleForRDS` role, you
can try to delete the role. If the service is using the role, then the deletion fails
and you can view the Regions where the role is being used. If the role is being used,
then you must wait for the session to end before you can delete the role. You cannot
revoke the session for a service-linked role.

If you want to remove the `AWSServiceRoleForRDS` role, you must first
delete _all_ of your instances and clusters.

#### Deleting All of Your Instances

Use one of these procedures to delete each of your instances.

###### To delete an instance (console)

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Instances**.
3. In the **Instances** list, choose the instance that you want to
   delete.
4. Choose **Instance actions**, and then choose
   **Delete**.
5. If you are prompted for **Create final Snapshot?**, choose
   **Yes** or **No**.
6. If you chose **Yes** in the previous step, for **Final snapshot
   name** enter the name of your final snapshot.
7. Choose **Delete**.

###### To delete an instance (AWS CLI)

See `delete-db-instance` in the _AWS CLI Command Reference_.

###### To delete an instance (API)

See `DeleteDBInstance`.

#### Deleting All of Your Clusters

Use one of the following procedures to delete a single cluster, and then repeat the
procedure for each of your clusters.

###### To delete a cluster (console)

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the **Clusters** list, choose the cluster that you want to
   delete.
3. Choose **Cluster Actions**, and then choose
   **Delete**.
4. Choose **Delete**.

###### To delete a cluster (CLI)

See `delete-db-cluster` in the _AWS CLI Command Reference_.

###### To delete a cluster (API)

See `DeleteDBCluster`

You can use the IAM console, the IAM CLI, or the IAM API to delete the
`AWSServiceRoleForRDS` service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
