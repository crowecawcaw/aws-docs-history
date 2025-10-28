# Using service-linked roles for Amazon EMR on EKS

Amazon EMR on EKS uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon EMR on EKS. Service-linked roles are predefined by Amazon EMR on EKS and include all
the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Amazon EMR on EKS easier because you don’t have to manually
add the necessary permissions. Amazon EMR on EKS defines the permissions of its service-linked roles,
and unless defined otherwise, only Amazon EMR on EKS can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions policy cannot be
attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your Amazon EMR on EKS resources because you can't inadvertently remove permission to access
the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for Amazon EMR on EKS

Amazon EMR on EKS uses the service-linked role named
**AWSServiceRoleForAmazonEMRContainers**.

The `AWSServiceRoleForAmazonEMRContainers` service-linked role trusts the
following services to assume the role:

- `emr-containers.amazonaws.com`

The role permissions policy `AmazonEMRContainersServiceRolePolicy` allows
Amazon EMR on EKS to complete a set of actions on the specified resources, as the following policy
statement demonstrates.

###### Note

Managed policy contents change, so the policy shown here may be out-of-date. View the
most up-to-date policy documentation at [AmazonEMRContainersServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEMRContainersServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonEMRContainersServiceRolePolicy.md") in the _AWS Managed Policy
Reference Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "eks:DescribeCluster",
 "eks:ListNodeGroups",
 "eks:DescribeNodeGroup",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "elasticloadbalancing:DescribeInstanceHealth",
 "elasticloadbalancing:DescribeLoadBalancers",
 "elasticloadbalancing:DescribeTargetGroups",
 "elasticloadbalancing:DescribeTargetHealth",
 "eks:ListPodIdentityAssociations",
 "eks:DescribePodIdentityAssociation"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowEKSDescribecluster"
 },
 {
 "Effect": "Allow",
 "Action": [
 "acm:ImportCertificate",
 "acm:AddTagsToCertificate"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/emr-container:endpoint:managed-certificate": "true"
 }
 },
 "Sid": "AllowACMImportcertificate"
 },
 {
 "Effect": "Allow",
 "Action": [
 "acm:DeleteCertificate"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/emr-container:endpoint:managed-certificate": "true"
 }
 },
 "Sid": "AllowACMDeletecertificate"
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for Amazon EMR on EKS

You don't need to manually create a service-linked role. When you create a virtual
cluster, Amazon EMR on EKS creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create a virtual cluster,
Amazon EMR on EKS creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**Amazon EMR on EKS** use case. In the AWS CLI or the AWS API, create a
service-linked role with the `emr-containers.amazonaws.com` service name. For more
information, see [Creating a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for Amazon EMR on EKS

Amazon EMR on EKS does not allow you to edit the `AWSServiceRoleForAmazonEMRContainers`
service-linked role. After you create a service-linked role, you cannot change the name of the
role because various entities might reference the role. However, you can edit the description
of the role using IAM. For more information, see [Editing
a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for Amazon EMR on EKS

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the Amazon EMR on EKS service is using the role when you try to delete the resources, then
the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete Amazon EMR on EKS resources used by the

`AWSServiceRoleForAmazonEMRContainers`

1. Open the Amazon EMR console.
2. Choose a virtual cluster.
3. On the `Virtual Cluster` page choose **Delete**.
4. Repeat this procedure for any other virtual clusters in your account.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForAmazonEMRContainers` service-linked role. For more information,
see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for Amazon EMR on EKS service-linked roles

Amazon EMR on EKS supports using service-linked roles in all of the Regions where the service is
available. For more information, see [Amazon EMR on EKS service endpoints and quotas](service-quotas.md "service-quotas.md").
