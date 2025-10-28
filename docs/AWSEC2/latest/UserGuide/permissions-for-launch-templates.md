# IAM permissions required for Amazon EC2

launch templates

You can use IAM permissions to control whether users can list, view, create, or
delete launch templates or launch template versions.

###### Important

You can't use resource-level permissions to restrict the resources that users can
specify in a launch template when they create a launch template or launch template
version. Therefore, make sure that only trusted administrators are granted
permission to create launch templates and launch template versions.

You must grant anyone that will use a launch template the permissions required to
create and access the resources that are specified in the launch template. For
example:

- To launch an instance from a shared private Amazon Machine Image (AMI), the user must
  have launch permission for the AMI.
- To create EBS volumes with tags from existing snapshots, the user must have
  read access to the snapshots, and permissions to create and tag volumes.

###### Contents

- [ec2:CreateLaunchTemplate](#permissions-for-launch-templates-create "#permissions-for-launch-templates-create")
- [ec2:DescribeLaunchTemplates](#permissions-for-launch-templates-view "#permissions-for-launch-templates-view")
- [ec2:DescribeLaunchTemplateVersions](#permissions-for-launch-template-versions-view "#permissions-for-launch-template-versions-view")
- [ec2:DeleteLaunchTemplate](#permissions-for-launch-templates-delete "#permissions-for-launch-templates-delete")
- [Control versioning
  permissions](#permissions-for-launch-template-versions "#permissions-for-launch-template-versions")
- [Control access to tags on
  launch templates](#permissions-for-launch-templates-tags "#permissions-for-launch-templates-tags")

## ec2:CreateLaunchTemplate

To create a launch template in the console or by using the APIs, the principal
must have the `ec2:CreateLaunchTemplate` permission in an IAM policy.
Whenever possible, use tags to help you control access to the launch templates in
your account.

For example, the following IAM policy statement gives the principal permission
to create launch templates only if the template uses the specified tag
(`purpose`=`testing`).

```
{
    "Sid": "IAMPolicyForCreatingTaggedLaunchTemplates",
    "Action": "ec2:CreateLaunchTemplate",
    "Effect": "Allow",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceTag/`purpose`": "`testing`"
        }
    }
}
```

Principals who create launch templates might need some related permissions, such
as:

- **ec2:CreateTags** – To add tags to
  the launch template during the `CreateLaunchTemplate` operation,
  the `CreateLaunchTemplate` caller must have the
  `ec2:CreateTags` permission in an IAM policy.
- **ec2:RunInstances** – To launch EC2
  instances from the launch template that they created, the principal must
  also have the `ec2:RunInstances` permission in an IAM
  policy.

For resource-creating actions that apply tags, users must have the
`ec2:CreateTags` permission. The following IAM policy statement
uses the `ec2:CreateAction` condition key to allow users to create tags
only in the context of `CreateLaunchTemplate`. Users cannot tag existing
launch templates or any other resources. For more information, see [Grant permission to tag Amazon EC2 resources during creation](supported-iam-actions-tagging.md "supported-iam-actions-tagging.md").

```
{
    "Sid": "IAMPolicyForTaggingLaunchTemplatesOnCreation",
    "Action": "ec2:CreateTags",
    "Effect": "Allow",
    "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/*",
    "Condition": {
        "StringEquals": {
            "ec2:CreateAction": "CreateLaunchTemplate"
        }
    }
}
```

The IAM user who creates a launch template doesn't automatically have permission
to use the launch template that they created. Like any other principal, the launch
template creator needs to get permission through an IAM policy. If an IAM user
wants to launch an EC2 instance from a launch template, they must have the
`ec2:RunInstances` permission. When granting these permissions, you
can specify that users can only use launch templates with specific tags or specific
IDs. You can also control the AMI and other resources that anyone using launch
templates can reference and use when launching instances by specifying
resource-level permissions for the `RunInstances` call. For example
policies, see [Launch templates](ExamplePolicies_EC2.md#iam-example-runinstances-launch-templates "ExamplePolicies_EC2.md#iam-example-runinstances-launch-templates").

## ec2:DescribeLaunchTemplates

To list and view launch templates in the account, the principal must have the
`ec2:DescribeLaunchTemplates` permission in an IAM policy. Because
`Describe` actions do not support resource-level permissions, you
must specify them without conditions and the value of the resource element in the
policy must be `"*"`.

For example, the following IAM policy statement gives the principal permission
to list and view all launch templates in the account.

```
{
    "Sid": "IAMPolicyForDescribingLaunchTemplates",
    "Action": "ec2:DescribeLaunchTemplates",
    "Effect": "Allow",
    "Resource": "*"
}
```

## ec2:DescribeLaunchTemplateVersions

Principals who list and view launch templates should also have the
`ec2:DescribeLaunchTemplateVersions` permission to retrieve the
entire set of attributes that make up the launch templates.

To list and view launch template versions in the account, the principal must have
the `ec2:DescribeLaunchTemplateVersions` permission in an IAM policy.
Because `Describe` actions do not support resource-level permissions, you
must specify them without conditions and the value of the resource element in the
policy must be `"*"`.

For example, the following IAM policy statement gives the principal permission
to list and view all launch template versions in the account.

```
{
    "Sid": "IAMPolicyForDescribingLaunchTemplateVersions",
    "Effect": "Allow",
    "Action": "ec2:DescribeLaunchTemplateVersions",
    "Resource": "*"
}
```

## ec2:DeleteLaunchTemplate

###### Important

Use caution when giving principals permission to delete a resource. Deleting a
launch template might cause a failure in an AWS resource that relies on the
launch template.

To delete a launch template, the principal must have the
`ec2:DeleteLaunchTemplate` permission in an IAM policy. Whenever
possible, use tag-based condition keys to limit the permissions.

For example, the following IAM policy statement gives the principal permission
to delete launch templates only if the template has the specified tag
(`purpose`=`testing`).

```
{
    "Sid": "IAMPolicyForDeletingLaunchTemplates",
    "Action": "ec2:DeleteLaunchTemplate",
    "Effect": "Allow",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceTag/`purpose`": "`testing`"
        }
    }
}
```

Alternatively, you can use ARNs to identify the launch template that the IAM
policy applies to.

A launch template has the following ARN.

```
"Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/`lt-09477bcd97b0d310e`"
```

You can specify multiple ARNs by enclosing them in a list, or you can specify a
`Resource` value of `"*"` without the
`Condition` element to allow the principal to delete any launch
template in the account.

## Control versioning

permissions

For trusted administrators, you can grant access for creating and deleting
versions of a launch template, and for changing the default version of a launch
template, by using IAM policies similar to the following examples.

###### Important

Be cautious when giving principals permission to create launch template
versions or modify launch templates.

- When you create a launch template version, you affect any AWS
  resources that allow Amazon EC2 to launch instances on your behalf with the
  `Latest` version.
- When you modify a launch template, you can change which version is the
  `Default` and therefore affect any AWS resources that
  allow Amazon EC2 to launch instances on your behalf with this modified
  version.
  You also need to be cautious in how you handle AWS resources that interact
  with the `Latest` or `Default` launch template version,
  such as EC2 Fleet and Spot Fleet. When a different launch template version is used for
  `Latest` or `Default`, Amazon EC2 does not re-check user
  permissions for actions to be completed when launching new instances to fulfil
  the fleet’s target capacity because there is no user interaction with the AWS
  resource. By granting a user permission to call the
  `CreateLaunchTemplateVersion` and
  `ModifyLaunchTemplate` APIs, the user is effectively also granted
  the `iam:PassRole` permission if they point the fleet to a different
  launch template version that contains an instance profile (a container for an
  IAM role). It means that a user can potentially update a launch template to
  pass an IAM role to an instance even if they don’t have the
  `iam:PassRole` permission. You can manage this risk by being
  careful when granting permissions to who can create and manage launch template
  versions.

### ec2:CreateLaunchTemplateVersion

To create a new version of a launch template, the principal must have the
`ec2:CreateLaunchTemplateVersion` permission for the launch
template in an IAM policy.

For example, the following IAM policy statement gives the principal
permission to create launch template versions only if the version uses the
specified tag
(`environment`=`production`).
Alternatively, you can specify one or multiple launch template ARNs, or you can
specify a `Resource` value of `"*"` without the
`Condition` element to allow the principal to create versions of
any launch template in the account.

```
{
    "Sid": "IAMPolicyForCreatingLaunchTemplateVersions",
    "Action": "ec2:CreateLaunchTemplateVersion",
    "Effect": "Allow",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceTag/`environment`": "`production`"
        }
    }
}
```

### ec2:DeleteLaunchTemplateVersion

###### Important

As always, you should exercise caution when giving principals permission
to delete a resource. Deleting a launch template version might cause a
failure in an AWS resource that relies on the launch template
version.

To delete a launch template version, the principal must have the
`ec2:DeleteLaunchTemplateVersion` permission for the launch
template in an IAM policy.

For example, the following IAM policy statement gives the principal
permission to delete launch template versions only if the version uses the
specified tag
(`environment`=`production`).
Alternatively, you can specify one or multiple launch template ARNs, or you can
specify a `Resource` value of `"*"` without the
`Condition` element to allow the principal to delete versions of
any launch template in the account.

```
{
    "Sid": "IAMPolicyForDeletingLaunchTemplateVersions",
    "Action": "ec2:DeleteLaunchTemplateVersion",
    "Effect": "Allow",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceTag/`environment`": "`production`"
        }
    }
}
```

### ec2:ModifyLaunchTemplate

To change the `Default` version that is associated with a launch
template, the principal must have the `ec2:ModifyLaunchTemplate`
permission for the launch template in an IAM policy.

For example, the following IAM policy statement gives the principal
permission to modify launch templates only if the launch template uses the
specified tag
(`environment`=`production`).
Alternatively, you can specify one or multiple launch template ARNs, or you can
specify a `Resource` value of `"*"` without the
`Condition` element to allow the principal to modify any launch
template in the account.

```
{
    "Sid": "IAMPolicyForModifyingLaunchTemplates",
    "Action": "ec2:ModifyLaunchTemplate",
    "Effect": "Allow",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceTag/`environment`": "`production`"
        }
    }
}
```

## Control access to tags on

launch templates

You can use condition keys to limit tagging permissions when the resource is a
launch template. For example, the following IAM policy allows removing only the
tag with the `temporary` key from launch
templates in the specified account and Region.

```
{
    "Sid": "IAMPolicyForDeletingTagsOnLaunchTemplates",
    "Action": "ec2:DeleteTags",
    "Effect": "Allow",
    "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:launch-template/*",
    "Condition": {
        "ForAllValues:StringEquals": {
            "aws:TagKeys": ["`temporary`"]
        }
    }
}
```

For more information about conditions keys that you can use to control the tag
keys and values that can be applied to Amazon EC2 resources, see [Control access to specific tags](supported-iam-actions-tagging.md#control-tagging "supported-iam-actions-tagging.md#control-tagging").
