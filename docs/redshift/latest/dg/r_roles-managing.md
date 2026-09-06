

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Managing roles in RBAC
<a name="r_roles-managing"></a>

To perform the following actions, use the following commands:
+ To create a role, use the [CREATE ROLE](r_CREATE_ROLE.md) command.
+ To rename a role or change the owner of the role, use the [ALTER ROLE](r_ALTER_ROLE.md) command.
+ To delete a role, use the [DROP ROLE](r_DROP_ROLE.md) command. 
+ To grant a role to a user, use the [GRANT](r_GRANT.md) command. 
+ To revoke a role from a user, use the [REVOKE](r_REVOKE.md) command. 
+ To grant system permissions to a role, use the [GRANT](r_GRANT.md) command. 
+ To revoke system permissions from a role, use the [REVOKE](r_REVOKE.md) command. 

To view a list of roles in your cluster or workgroup, see [SVV\_ROLES](r_SVV_ROLES.md).