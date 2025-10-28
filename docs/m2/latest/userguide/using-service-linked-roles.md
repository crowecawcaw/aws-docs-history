AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Using service-linked roles for

AWS Mainframe Modernization

AWS Mainframe Modernization uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Mainframe Modernization. Service-linked roles are predefined by AWS Mainframe Modernization and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS Mainframe Modernization easier because you don’t have to
manually add the necessary permissions. AWS Mainframe Modernization defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS Mainframe Modernization can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your AWS Mainframe Modernization resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the
**Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for

AWS Mainframe Modernization

AWS Mainframe Modernization uses the service-linked role named **AWSServiceRoleForAWSM2** –
configure the network to connect to your VPC and access resources such as file systems.

The AWSServiceRoleForAWSM2 service-linked role trusts the following services to assume the
role:

- `m2.amazonaws.com`

The role permissions policy named AWSM2ServicePolicy allows AWS Mainframe Modernization to complete the following actions on the
specified resources:

- Create, delete, describe, and attach permissions to Amazon EC2 network interfaces for the AWS Mainframe Modernization environment to establish connectivity to the customer VPC.
- Register or de-register entries from Elastic Load Balancing, which is how customers connect to the AWS Mainframe Modernization environment.
- Describe the Amazon EFS or Amazon FSx file system, if used.
- Emit metrics to the customer's CloudWatch from the runtime environment.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSubnets",
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticfilesystem:DescribeMountTargets"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticloadbalancing:RegisterTargets",
 "elasticloadbalancing:DeregisterTargets"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "fsx:DescribeFileSystems"
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
 "cloudwatch:namespace": [
 "AWS/M2"
 ]
 }
 }
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for

AWS Mainframe Modernization

You don't need to manually create a service-linked role. When you
create a runtime environment in the AWS Management Console, the AWS CLI, or the AWS API, AWS Mainframe Modernization
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create a runtime environment,
AWS Mainframe Modernization creates the service-linked role for you again.

## Editing a service-linked role for

AWS Mainframe Modernization

AWS Mainframe Modernization does not allow you to edit the AWSServiceRoleForAWSM2 service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for

AWS Mainframe Modernization

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the AWS Mainframe Modernization service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete AWS Mainframe Modernization resources used by the AWSServiceRoleForAWSM2

- Delete the runtime environments in AWS Mainframe Modernization. Make sure to delete applications from an environment before deleting the environment itself.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAWSM2
service-linked role. For more information, see [Deleting a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported regions for

AWS Mainframe Modernization service-linked roles

AWS Mainframe Modernization supports using service-linked roles in all of the regions where the service is available. For more information, see [AWS regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
