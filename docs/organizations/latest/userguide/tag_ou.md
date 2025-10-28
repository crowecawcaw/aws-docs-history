# Tagging an organizational unit (OU) with AWS Organizations

When you sign in to your organization's management account, you can add or remove the
tags attached to an OU. To do this, complete the following steps.

###### Minimum permissions

To edit the tags attached to an OU within a root in your organization, you
must have the following permissions:

- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:DescribeOrganizationalUnit`– required only when using the Organizations console
- `organizations:TagResource`
- `organizations:UntagResource`

AWS Management Console

###### To edit the tags attached to an OU

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, [navigate to
   and choose the name of the OU](navigate_tree.md "navigate_tree.md") whose tags you want to
   edit.
3. On the OU's details page, choose the **Tags**
   tab, and then choose **Manage tags**.
4. You can perform any of these actions on this tab:
   - Edit the value for any tag by entering a new value over
     the old one. You can't modify the tag key. To change a key,
     you must delete the tag with the old key and add a tag with
     the new key.
   - Remove an existing tag by choosing
     **Remove** next to the tag you want to
     remive.
   - Add a new tag key and value pair. Choose **Add
     tag**, then enter the new key name and optional
     value in the provided boxes. If you leave the
     **Value** box empty, the value is an
     empty string; it isn't `null`.

5. Choose **Save changes** after you've made all the
   additions, removals, and edits you want to make.

AWS CLI & AWS SDKs

###### To edit the tags attached to an OU

You can use one of the following commands to change the tags attached
to an OU:

- AWS CLI: [tag-resource](../../../cli/latest/reference/organizations/tag-resource.md "../../../cli/latest/reference/organizations/tag-resource.md") and [untag-resource](../../../cli/latest/reference/organizations/untag-resource.md "../../../cli/latest/reference/organizations/untag-resource.md")

The following example attaches the tag
`"Department"="12345"` to an OU. Note that
`Key` and `Value` are case
sensitive.

```
`$` **aws organizations tag-resource \
 --resource-id ou-a1b2-f6g7h222 \
 --tags Key=Department,Value=12345**
```

This command produces no output when successful.

The following example removes the `Department` tag from
an OU.

```
`$` **aws organizations untag-resource \
 --resource-id ou-a1b2-f6g7h222 \
 --tag-keys Department**
```

This command produces no output when successful.

- AWS SDKs: [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
