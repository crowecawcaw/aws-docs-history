# Create a role to delegate permissions to an

AWS service

Many AWS services require that you
use roles to allow the service to access resources in other services on your behalf. A role that
a service assumes to perform actions on your behalf is called a [service role](id_roles.md#iam-term-service-role "id_roles.md#iam-term-service-role"). When a role serves a specialized purpose
for a service, it is categorized as a [service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role"). To see what services support using service-linked roles, or
whether a service supports any form of temporary credentials, see [AWS services that work with
IAM](reference_aws-services-that-work-with-iam.md "reference_aws-services-that-work-with-iam.md"). To learn how an individual
service uses roles, choose the service name in the table to view the documentation for that
service.

When setting the `PassRole` permission, you should make sure that a user doesn’t
pass a role where the role has more permissions than you want the user to have. For example,
Alice might not be allowed to perform any Amazon S3 actions. If Alice could pass a role to a service
that allows Amazon S3 actions, the service could perform Amazon S3 actions on behalf of Alice when
executing the job.

For information about how roles help you to delegate permissions, see [Roles terms and concepts](id_roles.md#id_roles_terms-and-concepts "id_roles.md#id_roles_terms-and-concepts").

## Service role permissions

You must configure permissions to allow an IAM entity (user or role) to create or edit a
service role.

###### Note

The ARN for a service-linked role includes a service principal, which is indicated in
the following policies as
``SERVICE-NAME`.amazonaws.com`. Do not try to guess the
service principal, because it is case-sensitive and the format can vary across AWS
services. To view the service principal for a service, see its service-linked role
documentation.

**To allow an IAM entity to create a specific service
role**

Add the following policy to the IAM entity that needs to create the service role. This
policy allows you to create a service role for the specified service and with a specific name.
You can then attach managed or inline policies to that role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreateRole",
 "iam:PutRolePolicy"
 ],
 "Resource": "arn:aws:iam::*:role/`SERVICE-ROLE-NAME`"
 }
 ]
}`

```

**To allow an IAM entity to create any service
role**

AWS recommends that you allow only administrative users to create any service role. A
person with permissions to create a role and attach any policy can escalate their own
permissions. Instead, create a policy that allows them to create only the roles that they need
or have an administrator create the service role on their behalf.

To attach a policy that allows an administrator to access your entire AWS account, use
the [AdministratorAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AdministratorAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AdministratorAccess") AWS managed policy.

**To allow an IAM entity to edit a service role**

Add the following policy to the IAM entity that needs to edit the service role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EditSpecificServiceRole",
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:DeleteRolePolicy",
 "iam:DetachRolePolicy",
 "iam:GetRole",
 "iam:GetRolePolicy",
 "iam:ListAttachedRolePolicies",
 "iam:ListRolePolicies",
 "iam:PutRolePolicy",
 "iam:UpdateRole",
 "iam:UpdateRoleDescription"
 ],
 "Resource": "arn:aws:iam::*:role/`SERVICE-ROLE-NAME`"
 },
 {
 "Sid": "ViewRolesAndPolicies",
 "Effect": "Allow",
 "Action": [
 "iam:GetPolicy",
 "iam:ListRoles"
 ],
 "Resource": "*"
 }
 ]
}`

```

**To allow an IAM entity to delete a specific service
role**

Add the following statement to the permissions policy for the IAM entity that needs to
delete the specified service role.

```
{
    "Effect": "Allow",
    "Action": "iam:DeleteRole",
    "Resource": "arn:aws:iam::*:role/`SERVICE-ROLE-NAME`"
}
```

**To allow an IAM entity to delete any service
role**

AWS recommends that you allow only administrative users to delete any service role.
Instead, create a policy that allows them to delete only the roles that they need or have an
administrator delete the service role on their behalf.

To attach a policy that allows an administrator to access your entire AWS account, use
the [AdministratorAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AdministratorAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AdministratorAccess") AWS managed policy.

## Creating a role for an AWS service

(console)

You can use the AWS Management Console to create a role for a service. Because some services support
more than one service role, see the [AWS documentation](../../../index.md "../../../index.md")
for your service to see which use case to choose. You can learn how to assign the necessary
trust and permissions policies to the role so that the service can assume the role on your
behalf. The steps that you can use to control the permissions for your role can vary,
depending on how the service defines the use cases, and whether or not you create a
service-linked role.

Console

###### To create a role for an AWS service (IAM console)

1.  Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane of the IAM console, choose **Roles**, and
    then choose **Create role**.
3.  For **Trusted entity type**, choose **AWS service**.
4.  For **Service or use case**, choose a service, and then choose the use case. Use cases are defined by the service to include the trust policy
    that the service requires.
5.  Choose **Next**.
6.  For **Permissions policies**, the options depend on the use case that you selected:
    - If the service defines the permissions for the role, you can't select permissions policies.
    - Select from a limited set of permission polices.
    - Select from all permission policies.
    - Select no permissions policies, create the policies after the role is created, and then attach the policies to the role.

7.  (Optional) Set a [permissions
    boundary](access_policies_boundaries.md "access_policies_boundaries.md"). This is an advanced feature that is available for service roles, but
    not service-linked roles.
    1. Open the **Set permissions boundary** section, and then choose
       **Use a permissions boundary to control the maximum role
       permissions**.

    IAM includes a list of the AWS managed and customer-managed policies in your account. 2. Select the policy to use for the permissions boundary.

8.  Choose **Next**.
9.  For **Role name**, the options depend on the service:
    - If the service defines the role name, you can't edit the role name.
    - If the service defines a prefix for the role name, you can enter an optional suffix.
    - If the service doesn't define the role name, you can name the role.

    ###### Important

    When you name a role, note the following:

        + Role names must be unique within your AWS account, and can't be made unique by case.


        For example, don't create roles named both `PRODROLE` and
         `prodrole`. When a role name is used in a policy or as part of an ARN, the role name is case sensitive, however when a role name appears to customers in the console, such as during the sign-in process, the role name is case insensitive.
        + You can't edit the name of the role after it's created because other entities might reference the role.

10. (Optional) For **Description**, enter a description for the role.
11. (Optional) To edit
    the use cases and permissions for the role, in the **Step 1: Select trusted
    entities** or **Step 2: Add permissions** sections, choose **Edit**.
12. (Optional) To help identify, organize, or search for the role, add tags as key-value pairs. For more
    information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](id_tags.md "id_tags.md") in the _IAM User Guide_.
13. Review the role, and then choose **Create role**.

## Creating a role for a service (AWS CLI)

Creating a role from the AWS CLI involves multiple steps. When you use the console to create
a role, many of the steps are done for you, but with the AWS CLI you must explicitly perform
each step yourself. You must create the role and then assign a permissions policy to the role.
If the service you are working with is Amazon EC2, then you must also create an instance profile
and add the role to it. Optionally, you can also set the [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md") for your role.

###### To create a role for an AWS service from the AWS CLI

1. The following `create-role` command creates a role named _Test-Role_
   and attaches a trust policy to it:

`aws iam create-role --role-name Test-Role --assume-role-policy-document
 file://Test-Role-Trust-Policy.json` 2. Attach a managed permissions policy to the role: [aws iam
attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md").

For example, the following `attach-role-policy` command attaches the AWS
managed policy named `ReadOnlyAccess` to the IAM role named
`ReadOnlyRole`:

`aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess
 --role-name ReadOnlyRole`

or

Create an inline permissions policy for the role: [aws iam put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md")

To add an inline permissions policy, see the following example:

`aws iam put-role-policy --role-name Test-Role --policy-name ExamplePolicy
 --policy-document file://AdminPolicy.json` 3. (Optional) Add custom attributes to the role by attaching tags: [aws iam tag-role](../../../cli/latest/reference/iam/tag-role.md "../../../cli/latest/reference/iam/tag-role.md")

For more information, see [Managing tags on IAM roles (AWS CLI or
AWS API)](id_tags_roles.md#id_tags_roles_procs-cli-api "id_tags_roles.md#id_tags_roles_procs-cli-api"). 4. (Optional) Set the [permissions
boundary](access_policies_boundaries.md "access_policies_boundaries.md") for the role: [aws iam
put-role-permissions-boundary](../../../cli/latest/reference/iam/put-role-permissions-boundary.md "../../../cli/latest/reference/iam/put-role-permissions-boundary.md")

A permissions boundary controls the maximum permissions that a role can have.
Permissions boundaries are an advanced AWS feature.

If you are going to use the role with Amazon EC2 or another AWS service that uses Amazon EC2, you
must store the role in an instance profile. An instance profile is a container for a role that
can be attached to an Amazon EC2 instance when launched. An instance profile can contain only one
role, and that limit cannot be increased. If you create the role using the AWS Management Console, the
instance profile is created for you with the same name as the role. For more information about
instance profiles, see [Use instance profiles](id_roles_use_switch-role-ec2_instance-profiles.md "id_roles_use_switch-role-ec2_instance-profiles.md"). For information about how
to launch an EC2 instance with a role, see [Controlling Access to
Amazon EC2 Resources](../../../AWSEC2/latest/UserGuide/UsingIAM.md#UsingIAMrolesWithAmazonEC2Instances "../../../AWSEC2/latest/UserGuide/UsingIAM.md#UsingIAMrolesWithAmazonEC2Instances") in the _Amazon EC2 User Guide_.

###### To create an instance profile and store the role in it (AWS CLI)

1. Create an instance profile: [aws iam create-instance-profile](../../../cli/latest/reference/iam/create-instance-profile.md "../../../cli/latest/reference/iam/create-instance-profile.md")
2. Add the role to the instance profile: [aws iam
   add-role-to-instance-profile](../../../cli/latest/reference/iam/add-role-to-instance-profile.md "../../../cli/latest/reference/iam/add-role-to-instance-profile.md")

The AWS CLI example command set below demonstrates the first two steps for creating a role
and attaching permissions. It also shows the two steps for creating an instance profile and
adding the role to the profile. This example trust policy allows the Amazon EC2 service to assume
the role and view the `example_bucket` Amazon S3 bucket. The example also assumes that
you are running on a client computer running Windows and have already configured your command
line interface with your account credentials and Region. For more information, see [Configuring the AWS Command Line
Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").

In this example, include the following trust policy in the first command when you create
the role. This trust policy allows the Amazon EC2 service to assume the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {"Service": "ec2.amazonaws.com"},
 "Action": "sts:AssumeRole"
 }
}`

```

When you use the second command, you must attach a permissions policy to the role. The
following example permissions policy allows the role to perform only the
`ListBucket` action on the `example_bucket` Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::example_bucket"
 }
}`

```

To create this `Test-Role-for-EC2` role, you must first save the previous trust
policy with the name `trustpolicyforec2.json` and the previous permissions policy
with the name `permissionspolicyforec2.json` to the `policies` directory
in your local `C:` drive. You can then use the following commands to create the
role, attach the policy, create the instance profile, and add the role to the instance
profile.

```
`# Create the role and attach the trust policy that allows EC2 to assume this role.
$` `aws iam create-role --role-name Test-Role-for-EC2 --assume-role-policy-document file://C:\policies\trustpolicyforec2.json`

`# Embed the permissions policy (in this example an inline policy) to the role to specify what it is allowed to do.
$` `aws iam put-role-policy --role-name Test-Role-for-EC2 --policy-name Permissions-Policy-For-Ec2 --policy-document file://C:\policies\permissionspolicyforec2.json`

`# Create the instance profile required by EC2 to contain the role
$` `aws iam create-instance-profile --instance-profile-name EC2-ListBucket-S3`

`# Finally, add the role to the instance profile
$` `aws iam add-role-to-instance-profile --instance-profile-name EC2-ListBucket-S3 --role-name Test-Role-for-EC2`
```

When you launch the EC2 instance, specify the instance profile name in the
**Configure Instance Details** page if you use the AWS console. If you
use the `aws ec2 run-instances` CLI command, specify the
`--iam-instance-profile` parameter.

## Creating a role for a service (AWS

API)

Creating a role from the AWS API involves multiple steps. When you use the console to
create a role, many of the steps are done for you, but with the API you must explicitly
perform each step yourself. You must create the role and then assign a permissions policy to
the role. If the service you are working with is Amazon EC2, then you must also create an
instance profile and add the role to it. Optionally, you can also set the [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md") for your role.

###### To create a role for an AWS service (AWS API)

1. Create a role: [CreateRole](../APIReference/API_CreateRole.md "../APIReference/API_CreateRole.md")

For the role's trust policy, you can specify a file location. 2. Attach a managed permissions policy to the role: [AttachRolePolicy](../APIReference/API_AttachRolePolicy.md "../APIReference/API_AttachRolePolicy.md")

or

Create an inline permissions policy for the role: [PutRolePolicy](../APIReference/API_PutRolePolicy.md "../APIReference/API_PutRolePolicy.md") 3. (Optional) Add custom attributes to the user by attaching tags: [TagRole](../APIReference/API_TagRole.md "../APIReference/API_TagRole.md")

For more information, see [Managing tags on IAM users (AWS CLI or
AWS API)](id_tags_users.md#id_tags_users_procs-cli-api "id_tags_users.md#id_tags_users_procs-cli-api"). 4. (Optional) Set the [permissions
boundary](access_policies_boundaries.md "access_policies_boundaries.md") for the role: [PutRolePermissionsBoundary](../APIReference/API_PutRolePermissionsBoundary.md "../APIReference/API_PutRolePermissionsBoundary.md")

A permissions boundary controls the maximum permissions that a role can have.
Permissions boundaries are an advanced AWS feature.

If you are going to use the role with Amazon EC2 or another AWS service that uses Amazon EC2,
you must store the role in an instance profile. An instance profile is a container for a
role. Each instance profile can contain only one role, and that limit cannot be increased.
If you create the role in the AWS Management Console, the instance profile is created for you with the
same name as the role. For more information about instance profiles, see [Use instance profiles](id_roles_use_switch-role-ec2_instance-profiles.md "id_roles_use_switch-role-ec2_instance-profiles.md"). For information about
how to launch an Amazon EC2 instance with a role, see [Controlling Access
to Amazon EC2 Resources](../../../AWSEC2/latest/UserGuide/UsingIAM.md#UsingIAMrolesWithAmazonEC2Instances "../../../AWSEC2/latest/UserGuide/UsingIAM.md#UsingIAMrolesWithAmazonEC2Instances") in the _Amazon EC2 User Guide_.

###### To create an instance profile and store the role in it (AWS API)

1. Create an instance profile: [CreateInstanceProfile](../APIReference/API_CreateInstanceProfile.md "../APIReference/API_CreateInstanceProfile.md")
2. Add the role to the instance profile: [AddRoleToInstanceProfile](../APIReference/API_AddRoleToInstanceProfile.md "../APIReference/API_AddRoleToInstanceProfile.md")
