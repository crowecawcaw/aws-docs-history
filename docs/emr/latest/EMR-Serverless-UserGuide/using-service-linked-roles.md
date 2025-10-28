# Using service-linked roles for

EMR Serverless

Amazon EMR Serverless uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to EMR Serverless. Service-linked roles are predefined by EMR Serverless and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up EMR Serverless easier because you don’t have to
manually add the necessary permissions. EMR Serverless defines the permissions of its
service-linked roles, and unless defined otherwise, only EMR Serverless can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your EMR Serverless resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, refer to [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and check for the services that have **Yes** in the **Service-linked roles**
column. Choose a **Yes** with a link to access the service-linked
role documentation for that service.

## Service-linked role permissions for EMR Serverless

EMR Serverless uses the service-linked role named **AWSServiceRoleForAmazonEMRServerless** to enable
it to call AWS APIs on your behalf.

The AWSServiceRoleForAmazonEMRServerless service-linked role trusts the following services to assume the
role:

- `ops.emr-serverless.amazonaws.com`

The role permissions policy named `AmazonEMRServerlessServiceRolePolicy` allows EMR Serverless to
complete the following actions on the specified resources.

###### Note

Managed policy contents change, so the policy shown here might be out of date. View the
most up-to-date policy [AmazonEMRServerlessServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonEMRServerlessServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonEMRServerlessServiceRolePolicy") in the AWS Management Console.

- Action: `ec2:CreateNetworkInterface`
- Action: `ec2:DeleteNetworkInterface`
- Action: `ec2:DescribeNetworkInterfaces`
- Action: `ec2:DescribeSecurityGroups`
- Action: `ec2:DescribeSubnets`
- Action: `ec2:DescribeVpcs`
- Action: `ec2:DescribeDhcpOptions`
- Action: `ec2:DescribeRouteTables`
- Action: `cloudwatch:PutMetricData`

The following is the full `AmazonEMRServerlessServiceRolePolicy` policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EC2PolicyStatement",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeRouteTables"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "CloudWatchPolicyStatement",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/EMRServerless",
 "AWS/Usage"
 ]
 }
 }
 }
 ]
}`

```

The following trust policy is attached to this role to allow the EMR Serverless principal
to assume this role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "arn:aws:iam::123456789012:role/aws-service-role/emr-serverless.amazonaws.com/AWSServiceRoleForEMRServerless",
 "Sid": "AllowSTSAssumerole"
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, refer to [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for EMR Serverless

You don't need to manually create a service-linked role. When you
create a new EMR Serverless application in the AWS Management Console (using EMR Studio), the AWS CLI, or the AWS
API, EMR Serverless creates the service-linked role for you. You must configure permissions to
allow an IAM entity (such as a user, group, or role) to create, edit, or delete a
service-linked role.

**To create the AWSServiceRoleForAmazonEMRServerless service-linked role using
IAM**

Add the following statement to the permissions policy for the IAM entity that needs to
create the service-linked role.

```
{
    "Effect": "Allow",
    "Action": [
        "iam:CreateServiceLinkedRole"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/ops.emr-serverless.amazonaws.com/AWSServiceRoleForAmazonEMRServerless*",
    "Condition": {"StringLike": {"iam:AWSServiceName": "ops.emr-serverless.amazonaws.com"}}
}
```

If you delete this service-linked role, and then need to create it again, use the
same process to recreate the role in your account. When you create a new EMR Serverless application,
EMR Serverless creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**EMR Serverless** use case. In the AWS CLI or the AWS API, create a
service-linked role with the `ops.emr-serverless.amazonaws.com` service name. For more
information, refer to [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, use this same process to create the role
again.

## Editing a service-linked role for EMR Serverless

EMR Serverless does not allow you to edit the AWSServiceRoleForAmazonEMRServerless service-linked role because
various entities might reference the role. You can't edit the AWS-owned IAM policy that
the EMR Serverless service-linked role uses, as it contains all the necessary permissions
EMR Serverless needs. However, you can edit the description of the role using IAM.

**To edit the description of the AWSServiceRoleForAmazonEMRServerless service-linked role using
IAM**

Add the following statement to the permissions policy for the IAM entity that needs to
edit the description of a service-linked role.

```
{
    "Effect": "Allow",
    "Action": [
        "iam: UpdateRoleDescription"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/ops.emr-serverless.amazonaws.com/AWSServiceRoleForAmazonEMRServerless*",
    "Condition": {"StringLike": {"iam:AWSServiceName": "ops.emr-serverless.amazonaws.com"}}
}
```

For more information, refer to [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for EMR Serverless

If you no longer need to use a feature or service that requires a service-linked role, we
suggest that you delete that role. This is so you don’t have an unused entity that is not
actively monitored or maintained. However, delete all EMR Serverless applications in
all Regions before delete the service-linked role.

###### Note

If the EMR Serverless service is using the role when you try to delete the resources
associated with the role, then the deletion might fail. If that happens, wait for a few
minutes and try the operation again.

**To delete the AWSServiceRoleForAmazonEMRServerless service-linked role using
IAM**

Add the following statement to the permissions policy for the IAM entity that needs to
delete a service-linked role.

```
{
    "Effect": "Allow",
    "Action": [
        "iam:DeleteServiceLinkedRole",
        "iam:GetServiceLinkedRoleDeletionStatus"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/ops.emr-serverless.amazonaws.com/AWSServiceRoleForAmazonEMRServerless*",
    "Condition": {"StringLike": {"iam:AWSServiceName": "ops.emr-serverless.amazonaws.com"}}
}
```

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonEMRServerless service-linked
role. For more information, refer to [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for EMR Serverless service-linked roles

EMR Serverless supports using service-linked roles in all of the Regions where the service
is available. For more information, refer to [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
