

# Example service control policies for AWS Organizations and Resource Explorer
<a name="security_iam_scp"></a>

AWS Resource Explorer supports service control policies (SCPs). SCPs are policies that you attach to elements in an organization to manage permissions within that organization. An SCP applies to all AWS accounts in an organization [under the element to which you attach the SCP](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_evaluation.html). SCPs offer central control over the maximum available permissions for all accounts in your organization. They can help you to ensure your AWS accounts stay within your organization’s access control guidelines. For more information, see [ Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_type-auth.html) in the *AWS Organizations User Guide*.

## Prerequisites
<a name="scp-prereqs"></a>

To use SCPs, you must first do the following:
+ Enable all features in your organization. For more information, see [Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *AWS Organizations User Guide*.
+ Enable SCPs for use within your organization. For more information, see [Enabling and disabling policy types](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_enable-disable.html) in the *AWS Organizations User Guide*.
+ Create the SCPs that you need. For more information about creating SCPs, see [ Creating and updating SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp-create.html) in the *AWS Organizations User Guide*.

## Example service control policies
<a name="scp-examples"></a>

The following example shows how you can use [attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) to control access to the administrative operations of Resource Explorer. This example policy denies access to all Resource Explorer operations except the two permissions required to search, `resource-explorer-2:Search` and `resource-explorer-2:GetView`, unless the IAM principal making the request is tagged `ResourceExplorerAdmin=TRUE`. For a more complete discussion of using ABAC with Resource Explorer, see [Using tag-based authorization to control access to your views](configure-views-grant-access.md#configure-views-grant-access-abac).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
    {
    "Effect": "Deny",
    "Action": [
    "resource-explorer-2:AssociateDefaultView",
    "resource-explorer-2:BatchGetView",
    "resource-explorer-2:CreateIndex",
    "resource-explorer-2:CreateView",
    "resource-explorer-2:DeleteIndex",
    "resource-explorer-2:DeleteView",
    "resource-explorer-2:DisassociateDefaultView",
    "resource-explorer-2:GetDefaultView",
    "resource-explorer-2:GetIndex",
    "resource-explorer-2:ListIndexes",
    "resource-explorer-2:ListSupportedResourceTypes",
    "resource-explorer-2:ListTagsForResource",
    "resource-explorer-2:ListViews",
    "resource-explorer-2:TagResource",
    "resource-explorer-2:UntagResource",
    "resource-explorer-2:UpdateIndexType",
    "resource-explorer-2:UpdateView"
    ],
    "Resource": [
    "*"
    ],
    "Condition": {
    "StringNotEqualsIgnoreCase": {"aws:PrincipalTag/ResourceExplorerAdmin": "TRUE"}
    }
    }
    ]
    }
```

------