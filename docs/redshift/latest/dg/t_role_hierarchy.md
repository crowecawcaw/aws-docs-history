Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Role hierarchy

_Roles_ are collections of permissions that you can
assign to a user or another role. You can assign system or database permissions to a
role. A user inherits permissions from an assigned role.

In RBAC, users can have nested roles. You can grant roles to both users and roles.
When granting a role to a user, you authorize the user with all the permissions
that this role includes. When granting a role r1 to a user, you
authorize the user with permissions from r1. The user now has permissions from r1 and
also any existing permissions they already have.

When granting a role (r1) to another role (r2), you authorize r2 with all the
permissions from r1. Also, when granting r2 to another role (r3), the permissions of r3
are the combination of the permissions from r1 and r2. Role hierarchy has r2 inherit
permissions from r1. Amazon Redshift propagates permissions with each role authorization.
Granting r1 to r2 and then r2 to r3 authorizes r3 with all the permissions from the
three roles. Thus, by granting r3 to a user, the user has all the permissions from the
three roles.

Amazon Redshift doesn't allow the creation of a role authorization cycle. A role
authorization cycle happens when a nested role is assigned back to a role earlier in the
role hierarchy, such as r3 being assigned back to r1. For more information about how to create roles and manage role assignments, see [Managing roles in RBAC](r_roles-managing.md "r_roles-managing.md").
