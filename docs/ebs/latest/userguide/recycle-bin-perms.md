

# Control access to Recycle Bin with IAM
<a name="recycle-bin-perms"></a>

By default, users don't have permission to work with Recycle Bin, retention rules, or with resources that are in the Recycle Bin. To allow users to work with these resources, you must create IAM policies that grant permission to use specific resources and API actions. After the policies are created, you must add permissions to your users, groups, or roles.

**Topics**
+ [Permissions for working with Recycle Bin and retention rules](#rule-perms)
+ [Permissions for working with resources in the Recycle Bin](#resource-perms)
+ [Condition keys for Recycle Bin](#rbin-condition-keys)

## Permissions for working with Recycle Bin and retention rules
<a name="rule-perms"></a>

To work with Recycle Bin and retention rules, users need the following permissions.
+ `rbin:CreateRule`
+ `rbin:UpdateRule`
+ `rbin:GetRule`
+ `rbin:ListRules`
+ `rbin:DeleteRule`
+ `rbin:TagResource`
+ `rbin:UntagResource`
+ `rbin:ListTagsForResource`
+ `rbin:LockRule`
+ `rbin:UnlockRule`

To use the Recycle Bin console, users need the `tag:GetResources` permission.

The following is an example IAM policy that includes the `tag:GetResources` permission for console users. If some permissions are not needed, you can remove them from the policy.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rbin:CreateRule",
                "rbin:UpdateRule",
                "rbin:GetRule",
                "rbin:ListRules",
                "rbin:DeleteRule",
                "rbin:TagResource",
                "rbin:UntagResource",
                "rbin:ListTagsForResource",
                "rbin:LockRule",
                "rbin:UnlockRule",
                "tag:GetResources"
            ],
            "Resource": "*"
        }
    ]
}
```

------

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

## Permissions for working with resources in the Recycle Bin
<a name="resource-perms"></a>

For more information about the IAM permissions needed to work with resources in the Recycle Bin, see the following:
+ [Permissions for working with volumes in the Recycle Bin](recycle-bin-working-with-volumes.md#volume-perms)
+ [Permissions for working with snapshots in the Recycle Bin](recycle-bin-working-with-snaps.md#snap-perms)
+ [Permissions for working with AMIs in the Recycle Bin](recycle-bin-working-with-amis.md#ami-perms)

## Condition keys for Recycle Bin
<a name="rbin-condition-keys"></a>

Recycle Bin defines the following condition keys that you can use in the `Condition` element of an IAM policy to control the conditions under which the policy statement applies. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.

**Topics**
+ [`rbin:Request/ResourceType` condition key](#resource-type-parameter)
+ [`rbin:Attribute/ResourceType` condition key](#resource-type-attribute)

### `rbin:Request/ResourceType` condition key
<a name="resource-type-parameter"></a>

The `rbin:Request/ResourceType` condition key can be used to filter access on [ CreateRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_CreateRule.html) and [ ListRules](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_ListRules.html) requests based on the value specified for the `ResourceType` request parameter.

**Example 1 - CreateRule**  
The following sample IAM policy allows IAM principals to make **CreateRule** requests only if the value specified for the `ResourceType` request parameter is `EBS_SNAPSHOT` or `EC2_IMAGE`. This allows the principal to create new retention rules for snapshots and AMIs only.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement" : [
        {
            "Effect" : "Allow",
            "Action" :[
                "rbin:CreateRule"
            ],
            "Resource" : "*",
            "Condition" : {
                "StringEquals" : {
                    "rbin:Request/ResourceType" : ["EBS_SNAPSHOT", "EC2_IMAGE"]
                }
            }
        }
    ]
}
```

------

**Example 2 - ListRules**  
The following sample IAM policy allows IAM principals to make **ListRules** requests only if the value specified for the `ResourceType` request parameter is `EBS_SNAPSHOT`. This allows the principal to list retention rules for snapshots only, and it prevents them from listing retention rules for any other resource type.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement" : [
        {
            "Effect" : "Allow",
            "Action" :[
                "rbin:ListRules"
            ],
            "Resource" : "*",
            "Condition" : {
                "StringEquals" : {
                    "rbin:Request/ResourceType" : "EBS_SNAPSHOT"
                }
            }
        }
    ]
}
```

------

### `rbin:Attribute/ResourceType` condition key
<a name="resource-type-attribute"></a>

The `rbin:Attribute/ResourceType` condition key can be used to filter access on [DeleteRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_DeleteRule.html), [GetRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_GetRule.html), [UpdateRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UpdateRule.html), [LockRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_LockRule.html), [UnlockRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UnlockRule.html), [TagResource](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UntagResource.html), and [ ListTagsForResource](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_ListTagsForResource.html) requests based on the value of the retention rule's `ResourceType` attribute.

**Example 1 - UpdateRule**  
The following sample IAM policy allows IAM principals to make **UpdateRule** requests only if the `ResourceType` attribute of the requested retention rule is `EBS_SNAPSHOT` or `EC2_IMAGE`. This allows the principal to update retention rules for snapshots and AMIs only.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement" : [
        {
            "Effect" : "Allow",
            "Action" :[
                "rbin:UpdateRule"
            ],
            "Resource" : "*",
            "Condition" : {
                "StringEquals" : {
                    "rbin:Attribute/ResourceType" : ["EBS_SNAPSHOT", "EC2_IMAGE"]
                }
            }
        }
    ]
}
```

------

**Example 2 - DeleteRule**  
The following sample IAM policy allows IAM principals to make **DeleteRule** requests only if the `ResourceType` attribute of the requested retention rule is `EBS_SNAPSHOT`. This allows the principal to delete retention rules for snapshots only.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement" : [
        {
            "Effect" : "Allow",
            "Action" :[
                "rbin:DeleteRule"
            ],
            "Resource" : "*",
            "Condition" : {
                "StringEquals" : {
                    "rbin:Attribute/ResourceType" : "EBS_SNAPSHOT"
                }
            }
        }
    ]
}
```

------