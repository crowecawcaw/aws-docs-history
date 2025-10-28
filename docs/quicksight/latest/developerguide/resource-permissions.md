# Permissions for Quick Sight resources

If you're not sure what the necessary permission is, you can attempt to make a call.
The client then tells you what the missing permission is. You can use asterisk
(`*`) in the Resource field of your permission policy instead of
specifying explicit resources. However, we highly recommend that you restrict each
permission as much as possible. You can restrict user access by specifying or excluding
resources in the policy, using their Quick Sight ARN. To retrieve the ARN of an Quick Sight resource,
use the `Describe` operation on the relevant resource.

Before you can call the Quick Sight API operations, you need the
`quicksight:*operation-name*` permission in a
policy attached to your IAM identity. For example, to call `list-users`,
you need the permission `quicksight:ListUsers`. The same pattern applies to
all operations. If you attempt to make the call you don't have permissions to call, the
resulting error shows you what the missing permission is. We highly recommend that you
restrict each permission as much as possible.

You can add conditions in IAM to further restrict access to an API in some scenarios. For
example, when you add `User1` to `Group1`, the main resource is
`Group1`. You can allow or deny access to certain groups. Or you can also
edit the Quick Sight IAM key `quicksight:UserName` to add a condition to allow or
prevent certain users from being added to that group.

For more information, see the following:

- [Actions, Resources, and Condition Keys](../../../IAM/latest/UserGuide/list_amazonquicksight.md "../../../IAM/latest/UserGuide/list_amazonquicksight.md")
- [IAM
  JSON Policy Elements](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md")

## Best practices

By working with Quick Sight, you can share analyses, dashboards, templates, and themes with up to
100 principals. A _principal_ can be one of the following:

- The Amazon Resource Name (ARN) of an Quick Sight user or group associated with a data source or dataset. (This is common.)
- The ARN of an Quick Sight user, group, or namespace associated with an analysis, dashboard, template, or theme. (This is common.)
- The ARN of an AWS account root: This is an IAM ARN rather than a Quick Sight ARN. Use this option only to share resources (templates) across AWS accounts. (This is less common.)

To share these resources with more principals, consider assigning resource permissions at
the group or namespace level. For example, if you add users into a group and share a
resource to the group, the group counts as one principal. This is true even though
it's shared to everyone in the group.
