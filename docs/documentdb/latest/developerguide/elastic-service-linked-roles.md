# Service-linked roles in elastic clusters

Amazon DocumentDB elastic clusters use AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role").
A service-linked role is a unique type of IAM role that is linked directly to Amazon DocumentDB elastic clusters.
Service-linked roles are predefined by Amazon DocumentDB elastic clusters and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes using Amazon DocumentDB elastic clusters easier because you don't have to manually add the necessary permissions.
Amazon DocumentDB elastic clusters defines the permissions of its service-linked roles, and unless defined otherwise, only Amazon DocumentDB elastic clusters can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.
You can delete the roles only after first deleting their related resources.
This protects your Amazon DocumentDB elastic clusters resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that are marked with **Yes** in the **Service-Linked Role** column.
Choose a Yes with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for elastic clusters

Amazon DocumentDB elastic clusters uses the service-linked role named `AWSServiceRoleForDocDB-Elastic` to allow Amazon DocumentDB elastic clusters to call AWS services on behalf of your clusters.

This service-linked role has a permissions policy attached to it called `AmazonDocDB-ElasticServiceRolePolicy` that grants it permissions to operate in your account.
The role permissions policy allows Amazon DocumentDB elastic clusters to complete the following actions on the specified resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/DocDB-Elastic"
 ]
 }
 }
 }
 ]
}`

```

###### Note

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role.
If you encounter the following error message:
**"Unable to create the resource. Verify that you have permission to create service linked role. Otherwise wait and try again later."**, make sure you have the following permissions enabled:

```

{
"Action": "iam:CreateServiceLinkedRole",
    "Effect": "Allow",
    "Resource": "arn:aws:iam::*:role/aws-service-role/docdb-elastic.amazonaws.com/AWSServiceRoleForDocDB-Elastic",
    "Condition": {
"StringLike": {
"iam:AWSServiceName":"docdb-elastic.amazonaws.com"
        }
    }
}

```

For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _AWS Identity and Access Management User Guide_.

### Creating a service-linked role for Amazon DocumentDB elastic clusters

You don't need to manually create a service-linked role.
When you create a DB instance, Amazon DocumentDB elastic clusters creates the service-linked role for you.

### Editing a service-linked role for Amazon DocumentDB elastic clusters

Amazon DocumentDB elastic clusters do not allow you to edit the `AWSServiceRoleForDocDB-Elastic` service-linked role.
After you create a service-linked role, you cannot change the name of the role because various entities might reference the role.
However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _AWS Identity and Access Management User Guide_.

##### Deleting a service-linked role for Amazon DocumentDB elastic clusters

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role.
That way you don't have an unused entity that is not actively monitored or maintained.
However, you must delete all of your clusters before you can delete the service-linked role.

##### Cleaning up a service-linked role

Before you can use IAM to delete a service-linked role, you must first confirm that the role has no active sessions and remove any resources used by the role.

To check whether the service-linked role has an active session in the IAM console:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") and open the IAM console.
2. In the navigation pane of the IAM console, choose **Roles**.
   Then choose the name (not the check box) of the `AWSServiceRoleForDocDB-Elastic` role.
3. On the **Summary** page for the chosen role, choose the **Access Advisor** tab.

###### Note

If you are unsure whether Amazon DocumentDB elastic clusters is using the `AWSServiceRoleForDocDB-Elastic` role, you can try to delete the role.
If the service is using the role, then the deletion fails and you can view the AWS Regions where the role is being used.
If the role is being used, then you must wait for the session to end before you can delete the role.
You cannot revoke the session for a service-linked role.

If you want to remove the `AWSServiceRoleForDocDB-Elastic` role, you must first delete all of your clusters.

##### Deleting all of your clusters

To delete a cluster in the Amazon DocumentDB console:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb") and open the Amazon DocumentDB console.
2. In the navigation pane, choose **Clusters**.
3. Choose the cluster that you want to delete.
4. For **Actions**, choose **Delete**.
5. If you are prompted to **Create final Snapshot?**, choose **Yes** or **No**.
6. If you chose **Yes** in the previous step, for **Final snapshot name** enter the name of your final snapshot.
7. Choose **Delete**.

###### Note

You can use the IAM console, the IAM CLI, or the IAM API to delete the `AWSServiceRoleForDocDB-Elastic` service-linked role.
For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _AWS Identity and Access Management User Guide_.
