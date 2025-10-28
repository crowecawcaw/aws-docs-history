# Use tags with IAM policies

Use resource tags in your IAM policies to control user access and permissions. For
example, policies can allow users to only create resources that have a specific tag attached.
Policies can also restrict users from creating or modifying resources that have certain
tags.

###### Note

If you use tags to allow or deny users' access to resources, you should deny users the
ability to add or remove those tags for the same resources. Otherwise, a user could bypass
your restrictions and gain access to a resource by modifying its tags.

You can use the following condition context keys and values in the `Condition`
element (also called the `Condition` block) of a policy statement.

`aws:ResourceTag/`tag-key`:
 `tag-value``

Allow or deny actions on resources with specific tags.

`aws:RequestTag/`tag-key`:
 `tag-value``

Require that a specific tag be used (or not used) when creating or modifying a
taggable resource.

`aws:TagKeys: [`tag-key`, ...]`

Require that a specific set of tag keys be used (or not used) when creating or
modifying a taggable resource.

###### Note

The condition context keys and values in an IAM policy apply only to actions that have
a taggable resource as a required parameter. For example, you can set tag-based conditional
access for [ListAssets](../APIReference/API_ListAssets.md "../APIReference/API_ListAssets.md").
You can't set tag-based conditional access on [PutLoggingOptions](../APIReference/API_PutLoggingOptions.md "../APIReference/API_PutLoggingOptions.md") because no taggable
resource is referenced in the request.

For more information, see [Controlling access
to AWS resources using resource tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") and [IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the
_IAM User Guide_.

**Example IAM policies using tags**

- [View AWS IoT SiteWise assets
  based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-asset-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-asset-tags")
