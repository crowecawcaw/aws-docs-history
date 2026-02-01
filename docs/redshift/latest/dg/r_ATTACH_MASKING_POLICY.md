Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ATTACH MASKING POLICY

Attaches an existing dynamic data masking policy to a column. For more information on
dynamic data masking, see [Dynamic data masking](t_ddm.md "t_ddm.md").

Superusers and users or roles that have the sys:secadmin role can attach a masking
policy.

## Syntax

```
ATTACH MASKING POLICY
{
  *policy\_name* ON *relation\_name*
  | *database\_name*.*policy\_name* ON *database\_name*.*schema\_name*.*relation\_name*
}
( { output_column_names | output_path } )
[ USING ( { input_column_names | input_path } ) ]
TO { user_name | ROLE role_name | PUBLIC }
[ PRIORITY priority ];

```

## Parameters

_policy_name_

The name of the masking policy to attach.

database_name

The name of the database where the policy and the relation are created. The policy and the
relation needs to be on the same database. The database can be the connected database or a
database that supports Amazon Redshift federated permissions.

schema_name

The name of the schema the relation belongs to.

_relation_name_

The name of the relation to attach the masking policy to.

_output_column_names_

The names of the columns that the masking policy will apply to.

_output_paths_

The full path of the SUPER object that the masking policy will apply to,
including the column name. For example, for a relation with a SUPER type column
named `person`, _output_path_ might be
`person.name.first_name`.

_input_column_names_

The names of the columns that the masking policy will take as input. This
parameter is optional. If not specified, the masking policy uses
_output_column_names_ as inputs.

_input_paths_

The full path of the SUPER object that the masking policy will take as
input. This parameter is optional. If not specified, the masking policy uses
_output_path_ for inputs.

_user_name_

The name of the user to whom the masking policy will attach. You can't
attach two policies to the same combination of user and column or role and
column. You can attach a policy to a user and another policy to the user's
role. In this case, the policy with the higher priority applies.

You can only set one of user_name, role_name, and PUBLIC in a single ATTACH
MASKING POLICY command.

_role_name_

The name of the role to which the masking policy will attach. You can't
attach two policies to the same column/role pair. You can attach a policy to a
user and another policy to the user's role. In this case, the policy with the
higher priority applies.

You can only set one of user_name, role_name, and PUBLIC in a single ATTACH
MASKING POLICY command.

_PUBLIC_

Attaches the masking policy to all users accessing the table. You must give
other masking policies attached to specific column/user or column/role pairs a
higher priority than the PUBLIC policy for them to apply.

You can only set one of user_name, role_name, and PUBLIC in a single ATTACH
MASKING POLICY command.

_priority_

The priority of the masking policy. When multiple masking policies apply to
a given user's query, the highest priority policy applies.

You can't attach two different policies to the same column with equal
priority, even if the two policies are attached to different users or roles.
You can attach the same policy multiple times to the same set of table, output
column, input column, and priority parameters, as long as the user or role the
policy attaches to is different each time.

You can't apply a policy to a column with the same priority as another
policy attached to that column, even if they're for different roles. This field
is optional. If you don't specify a priority, the masking policy defaults to
attaching with a priority of 0.

For the usage of ATTACH MASKING POLICY on Amazon Redshift Federated Permissions Catalog, see [Managing access control with Amazon Redshift federated permissions](federated-permissions-managing-access.md "federated-permissions-managing-access.md").
