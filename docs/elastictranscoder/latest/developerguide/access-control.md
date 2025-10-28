End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Controlling Access to Elastic Transcoder

Amazon Elastic Transcoder lets you use AWS Identity and Access Management (IAM) to control what users can do with Elastic Transcoder, and to
control Elastic Transcoder's access to other AWS services that Elastic Transcoder requires. You control access using
IAM policies, which are a collection of permissions that can be associated with an
IAM user, an IAM group, or a role.

###### Topics

- [Controlling Access to Elastic Transcoder](#access-control-users "#access-control-users")
- [Service Roles for Elastic Transcoder Pipelines](#access-control-roles "#access-control-roles")

## Controlling Access to Elastic Transcoder

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

To control Elastic Transcoder's access to other AWS services, you can create service roles. These
are IAM roles that you assign when you create a pipeline, and that give Elastic Transcoder itself
permissions to perform the tasks associated with transcoding.

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
    boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"). This is an advanced feature that is available for service roles, but
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
    information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.
13. Review the role, and then choose **Create role**.

As an example of how user and service roles are both important during the transcoding
process, Elastic Transcoder needs a service role in order to get files from an Amazon S3 bucket and store
the transcoded files in another Amazon S3 bucket, while a user needs an IAM role that
allows them to create a job in Elastic Transcoder.

For more information about IAM, see the _[IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")_. For more information about service roles,
see [Creating a Role for an AWS
Service](../../../IAM/latest/UserGuide/create-role-xacct.md "../../../IAM/latest/UserGuide/create-role-xacct.md").

### Example Policies for Elastic Transcoder

To allow users to perform Elastic Transcoder administrative functions, such as creating
pipelines and running jobs, you must have a policy that you can associate with the
user. This section shows how to create a policy, and also shows three policies for
controlling access to Elastic Transcoder operations and to the operations of related services that
Elastic Transcoder relies on. You can give users of your AWS account access to all Elastic Transcoder
operations or to only a subset of them.

For more information on managing policies, see [Managing IAM Policies](../../../IAM/latest/UserGuide/ManagingPolicies.md "../../../IAM/latest/UserGuide/ManagingPolicies.md") in the
_IAM User Guide_.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter or paste a JSON policy document. For details about the IAM policy language, see
[IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md"). 6. Resolve any security warnings, errors, or general warnings generated during [policy validation](../../../IAM/latest/UserGuide/access_policies_policy-validator.md "../../../IAM/latest/UserGuide/access_policies_policy-validator.md"), and then choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. (Optional) When you create or edit a policy in the AWS Management Console, you can generate a JSON
or YAML policy template that you can use in AWS CloudFormation templates.

To do this, in the **Policy editor** choose
**Actions**, and then choose **Generate CloudFormation
template**. To learn more about AWS CloudFormation, see [AWS Identity and Access Management resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md "../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md") in the
_AWS CloudFormation User Guide_. 8. When you are finished adding permissions to the policy, choose
**Next**. 9. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 10. (Optional) Add metadata to the policy by attaching tags as key-value pairs. For more
information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_. 11. Choose **Create policy** to save your new policy.

#### Give Read-only Access to Elastic Transcoder and

Amazon S3

The following policy grants read-only access to Elastic Transcoder resources and access to
the list operation of Amazon S3. This policy is useful for permissions to find and
watch transcoded files and to see what buckets are available to the IAM
account, but who don't need the ability to update, create, or delete resources
or files. This policy also allows listing all available pipelines, presets, and
jobs for the IAM account. To restrict access to a particular bucket, see [Restricting Access to Certain
Resources](#access-control-resources "#access-control-resources").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elastictranscoder:Read*",
 "elastictranscoder:List*",
 "s3:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

#### Give Permission to Create

Jobs

The following policy grants the permissions to list and get all Elastic Transcoder resources
associated with the account, create or modify jobs and presets, and use the list
operations of Amazon S3 and Amazon SNS.

This policy is useful to modify transcoding settings, and the ability to
create or delete presets or jobs. It does not allow create, update, or delete of
pipelines, Amazon S3 buckets, or Amazon SNS notifications.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elastictranscoder:Read*",
 "elastictranscoder:List*",
 "elastictranscoder:*Job",
 "elastictranscoder:*Preset",
 "s3:List*",
 "sns:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

#### Elastic Transcoder Operations with Controllable

Access

The following is the full list of Elastic Transcoder operations.

```

    elastictranscoder:CancelJob
    elastictranscoder:CreateJob
    elastictranscoder:CreatePipeline
    elastictranscoder:CreatePreset
    elastictranscoder:DeletePipeline
    elastictranscoder:DeletePreset
    elastictranscoder:ListJobsByPipeline
    elastictranscoder:ListJobsByStatus
    elastictranscoder:ListPipelines
    elastictranscoder:ListPresets
    elastictranscoder:ReadJob
    elastictranscoder:ReadPipeline
    elastictranscoder:ReadPreset
    elastictranscoder:TestRole
    elastictranscoder:UpdatePipeline
    elastictranscoder:UpdatePipelineNotifications
    elastictranscoder:UpdatePipelineStatus

```

### Restricting Access to Certain

Resources

In addition to restricting access to operations (actions), you can further
restrict access to specific jobs, pipelines, and presets, which is referred to as
granting resource-level permissions.

To restrict or grant access to a subset of Elastic Transcoder resources, put the ARN of the
resource in the resource element of your policy. Elastic Transcoder ARNs have the following
general format:

```
arn:aws:elastictranscoder:`region`:`account`:`resource`/`ID`
```

Replace the `region`, `account`,
`resource`, and `ID` variables
with valid values. Valid values can be the following:

- `region`: The name of the region. A list of
  regions is available [here](../../../general/latest/gr/rande.md#elastictranscoder_region "../../../general/latest/gr/rande.md#elastictranscoder_region"). To
  indicate all regions, use a wildcard (\*). You must specify a value.
- `account`: The ID of the AWS account. You must
  specify a value.
- `resource`: The type of Elastic Transcoder resource;
  `preset`, `pipeline`, or `job`.
- `ID`: The ID of the specific preset, pipeline, or
  job, or \* to indicate all resources of the specified type that are
  associated with the current AWS account.

For example, the following ARN specifies all preset resources in the
`us-east-2` region for the account
`111122223333`:

```
arn:aws:elastictranscoder:us-east-2:111122223333:preset/*
```

You can find the ARN of a resource by clicking the magnifying-glass icon (
![Magnifying glass icon with a plus sign, representing a search or zoom function.](images/magnifying-glass-icon.png)
) next to the resource name in the pipeline, preset, or job
console pages.

For more information, see [Resources](../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#Resource "../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#Resource") in the _IAM User Guide_.

#### Example Policy for

Restricting Resources

The following policy grants permissions to the bucket named
`amzn-s3-demo-bucket` in Amazon S3, list and read permissions for
everything in Elastic Transcoder, and permission to create jobs in the pipeline named
`example_pipeline`.

This policy is useful for SDK and CLI users who need to be able to see what
files and resources are available, and use those resources to create their own
transcoding jobs. It does not allow for updating or deleting resources, creating
resources other than jobs, or for working with resources other than the ones
specified here, and will not work for console users.

## Service Roles for Elastic Transcoder Pipelines

When you create a pipeline that manages your transcoding jobs, you must specify an
IAM service role. The IAM service role has a policy that specifies the permissions used
by that pipeline for transcoding.

You have two options when you specify a role for a pipeline:

- Use the default role, which includes only the
  permissions that Elastic Transcoder needs for transcoding. If you use the Elastic Transcoder console to
  create your pipelines, when you create your first pipeline the console gives
  you the option to create the default role automatically. You must have administrative
  permissions to create IAM service roles, including the default role.
- Choose an existing role. In this case, you must have previously
  created the role in IAM and attached a policy
  to the role that gives Elastic Transcoder sufficient permissions to transcode your
  files. This is useful if you want to use the role for other AWS
  services as well.

### The Default IAM Role for Pipelines

The default role created by Elastic Transcoder lets Elastic Transcoder perform the following operations:

- Get a file from an Amazon S3 bucket for transcoding.
- List the contents of any Amazon S3 bucket.
- Save a transcoded file to an Amazon S3 bucket.
- Create an Amazon S3 multipart upload.
- Publish notification to any SNS topic.

The policy prevents Elastic Transcoder from performing any of the following operations:

- Perform any Amazon SNS delete operations, or add or remove a policy statement in a topic.
- Perform any Amazon S3 bucket or item delete operations, or add, remove, or
  modify a bucket policy.

The access (permission) policy definition for the default role looks like:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"1",
 "Effect":"Allow",
 "Action":[
 "s3:Get*",
 "s3:ListBucket",
 "s3:Put*",
 "s3:*MultipartUpload*"
 ],
 "Resource":"*"
 },
 {
 "Sid":"2",
 "Effect":"Allow",
 "Action":"sns:Publish",
 "Resource":"*"
 },
 {
 "Sid":"3",
 "Effect":"Deny",
 "Action":[
 "sns:*Permission*",
 "sns:*Delete*",
 "sns:*Remove*",
 "s3:*Policy*",
 "s3:*Delete*"
 ],
 "Resource":"*"
 }
 ]
}`

```

#### Supported Regions for

Elastic Transcoder Service-Linked Roles

Elastic Transcoder supports using service-linked roles in the following regions.

| Region Name               | Region Identity | Support in Elastic Transcoder |
| ------------------------- | --------------- | ----------------------------- |
| US East (N. Virginia)     | us-east-1       | Yes                           |
| US East (Ohio)            | us-east-2       | No                            |
| US West (N. California)   | us-west-1       | Yes                           |
| US West (Oregon)          | us-west-2       | Yes                           |
| Asia Pacific (Mumbai)     | ap-south-1      | Yes                           |
| Asia Pacific (Osaka)      | ap-northeast-3  | No                            |
| Asia Pacific (Seoul)      | ap-northeast-2  | No                            |
| Asia Pacific (Singapore)  | ap-southeast-1  | Yes                           |
| Asia Pacific (Sydney)     | ap-southeast-2  | Yes                           |
| Asia Pacific (Tokyo)      | ap-northeast-1  | Yes                           |
| Canada (Central)          | ca-central-1    | No                            |
| Europe (Frankfurt)        | eu-central-1    | No                            |
| Europe (Ireland)          | eu-west-1       | Yes                           |
| Europe (London)           | eu-west-2       | No                            |
| Europe (Paris)            | eu-west-3       | No                            |
| South America (São Paulo) | sa-east-1       | No                            |
