# User groups, roles, and permission

sets

User groups manage specialized _roles_ that are
defined within your shared accounts. Roles establish sets of permissions that belong
together. All members of a group inherit the permission sets, or roles, associated with
the group. You can create new groups for the end users of your member accounts, so that
you can custom-assign only the roles that are needed for the specific tasks a group
performs.

The permission sets available cover a broad range of distinct user permission
requirements, such as read-only access, AWS Control Tower administrative access, and Service Catalog access.
These permission sets enable your end users to provision their own AWS accounts in
your landing zone quickly, and in compliance with your enterprise's guidelines.

For tips on planning your allocations of users, groups, and permissions, refer to
[Recommendations for setting up groups, roles, and
policies](roles-recommendations.md "roles-recommendations.md")

For more information on how to use this service in the context of AWS Control Tower, see the
following topics in the _AWS IAM Identity Center User Guide_.

- To add users, see [Add Users](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md").
- To add users to groups, see [Add Users to Groups](../../../singlesignon/latest/userguide/adduserstogroups.md "../../../singlesignon/latest/userguide/adduserstogroups.md").
- To edit user properties, see [Edit
  User Properties](../../../singlesignon/latest/userguide/edituser.md "../../../singlesignon/latest/userguide/edituser.md").
- To add a group, see [Add
  Groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md").

###### Warning

AWS Control Tower sets up your IAM Identity Center directory in your home Region. If you set up your
landing zone in another Region and then navigate to the IAM Identity Center console, you must change
the Region to your home region. Do not delete your IAM Identity Center configuration in your home
Region.
