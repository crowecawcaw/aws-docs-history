# Using service-linked roles (SLRs) in Neptune Analytics

Neptune Analytics graphs use AWS Identity and Access Management (IAM) [service-linked
roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly
to Neptune Analytics graphs. Service-linked roles are predefined by Neptune Analytics graphs and include all the
permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes using Neptune Analytics graphs easier because you don't have to
add the necessary permissions manually. Neptune Analytics defines the permissions in its service-linked
roles, and unless defined otherwise, only Neptune Analytics graphs can assume its roles. The defined
permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity. You can delete the roles only after
first deleting their related resources. This protects your Neptune Analytics graph resources because
you can't inadvertently remove the permissions to access the resources.

For information about other services that support service-linked roles, see
[AWS
services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that are marked
with **Yes** in the **Service-Linked Role**
column. Choose a **Yes** with a link to view the service-linked
role documentation for that service.

## Service-linked role permissions for Neptune Analytics Graphs

Neptune Analytics graphs uses the service-linked role named `AWSServiceRoleForNeptuneGraph`
to allow them to call AWS services on behalf of your DB clusters.

This service-linked role has an IAM managed permissions policy attached to it named [AWSServiceRoleForNeptuneGraphPolicy](../../../neptune/latest/userguide/aws-service-role-for-neptune-graph-policy.md "../../../neptune/latest/userguide/aws-service-role-for-neptune-graph-policy.md")
that grants it permissions to operate in your account. See [AWS managed policies for Amazon Neptune](../../../neptune/latest/userguide/security-iam-access-managed-policies.md "../../../neptune/latest/userguide/security-iam-access-managed-policies.md").
This policy provides read-only access to all Amazon Neptune Analytics resources along with
read-only permissions for dependent services, as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GraphMetrics",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/Neptune",
 "AWS/Usage"
 ]
 }
 }
 },
 {
 "Sid": "GraphLogGroup",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/neptune/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "GraphLogEvents",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/neptune/*:log-stream:*"
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

###### Note

To allow an IAM entity such as a user, group, or role to be able to
create, edit, or delete a service-linked role, you must set the appropriate
permissions, like this:

```
{
  "Action": "iam:CreateServiceLinkedRole",
  "Effect": "Allow",
  "Resource": "arn:aws:iam::*:role/aws-service-role/neptune-graph.amazonaws.com/AWSServiceRoleForNeptuneGraph",
  "Condition": {
    "StringLike": {
        "iam:AWSServiceName":"neptune-graph.amazonaws.com"
    }
}
```

If those permissions have not been set, or have not yet propagated, you
may receive the following error message when you try to create a service-linked role:

```
Unable to create the resource. Verify that you have permission
to create service linked role. Otherwise wait and try again later.
```

For more information, see [Service-linked
role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

## Creating a service-linked role for Neptune Analytics

You don't have to create a service-linked role manually for Neptune Analytics. When you create
a graph, Neptune Analytics automatically creates the service-linked role for you.

## Editing a service-linked role for Neptune Analytics

Neptune Analytics doesn't allow you to edit the `AWSServiceRoleForNeptuneGraph`
service-linked role. After you create a service-linked role, you cannot change the
name of the role because various entities might reference it. However, you can edi
t the description of the role using IAM. For more information, see
[Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

## Deleting a service-linked role

If you no longer need to use a feature or service that requires a service-linked
role, it's best to delete that role so you don't have an unused entity that is not
actively monitored or maintained.

However, before you can delete the service-linked role, you must first confirm that
the role has no active sessions, and remove any resources that it uses.

###### To check whether a service-linked role has an active session in the IAM console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   `Roles`. Then choose the name (not the check box) of
   the `AWSServiceRoleForNeptuneGraph` role.
3. On the **Summary** page for the chosen role, choose
   the **Access Advisor** tab.

###### Note

If you are unsure whether Neptune Analytics is using the `AWSServiceRoleForNeptuneGraph`
role, you can try to delete the role. If the service is using the role, then the deletion
fails and you can view the AWS Regions where the role is being used. If the role is
being used, then you must wait for the session to end before you can delete the role.
You cannot revoke the session for a service-linked role.

###### To delete your clusters so that you can delete `AWSServiceRoleForNeptuneGraph`

1. Open the Neptune console at [https://console.aws.amazon.com/neptune/](https://console.aws.amazon.com/neptune/ "https://console.aws.amazon.com/neptune/").
2. In the navigation pane, choose **Graphs**.
3. Choose a cluster that you want to delete.
4. For **Actions**, choose **Delete**.
5. If you are prompted to **Create final Snapshot?**, choose
   **Yes** or **No**. If you choose **Yes**
   enter the name of your final snapshot for **Final snapshot name**.
6. Choose **Delete**.

You can use the IAM console, the IAM CLI, or the IAM API to delete the
`AWSServiceRoleForNeptuneGraph` service-linked role. For more information,
see [Deleting
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").
