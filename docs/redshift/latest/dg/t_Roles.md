Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Role-based access control (RBAC)

By using role-based access control (RBAC) to manage database permissions in Amazon Redshift,
you can simplify the management of security permissions in Amazon Redshift. You can secure the
access to sensitive data by controlling what users can do both at a broad or fine level.
You can also control user access to tasks that are normally restricted to superusers. By
assigning different permissions to different roles and assigning them to different users,
you can have more granular control of user access.

Users with an assigned role can perform only the tasks that are specified by the
assigned role that they are authorized with. For example, a user with the assigned role
that has the CREATE TABLE and DROP TABLE permissions is only authorized to perform those
tasks. You can control user access by granting different levels of security permissions to
different users to access the data they require for their work.

RBAC applies the principle of least permissions to users based on their role
requirements, regardless of the types of objects that are involved. Granting and revoking
of permissions is performed at the role level, without the need to update permissions on
individual database objects.

With RBAC, you can create roles with permissions to run commands that used to require
superuser permissions. Users can run these commands, as long as they are authorized with a
role that includes these permissions. Similarly, you can also create roles to limit the
access to certain commands, and assign the role to either superusers or users that have
been authorized with the role.

To learn how Amazon Redshift RBAC works, watch the following video.
