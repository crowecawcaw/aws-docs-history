

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ATTACH MASKING POLICY
<a name="r_ATTACH_MASKING_POLICY"></a>

Attaches an existing dynamic data masking policy to a column. For more information on dynamic data masking, see [Dynamic data masking](t_ddm.md).

Superusers and users or roles that have the sys:secadmin role can attach a masking policy.

## Syntax
<a name="r_ATTACH_MASKING_POLICY-synopsis"></a>

```
ATTACH MASKING POLICY 
{
  policy_name ON relation_name
  | database_name.policy_name ON database_name.schema_name.relation_name
}
( { output_column_names | output_path } )
[ USING ( { input_column_names | input_path } ) ]
TO { user_name | ROLE role_name | PUBLIC }
[ PRIORITY priority ];
```

## Parameters
<a name="r_ATTACH_MASKING_POLICY-parameters"></a>

*policy\_name*   
The name of the masking policy to attach.

database\_name  
The name of the database where the policy and the relation are created. The policy and the relation needs to be on the same database. The database can be the connected database or a database that supports Amazon Redshift federated permissions.

schema\_name  
The name of the schema the relation belongs to.

 *relation\_name*   
The name of the relation to attach the masking policy to.

*output\_column\_names*   
The names of the columns that the masking policy will apply to.

*output\_paths*   
The full path of the SUPER object that the masking policy will apply to, including the column name. For example, for a relation with a SUPER type column named `person`, *output\_path* might be `person.name.first_name`. 

*input\_column\_names*   
The names of the columns that the masking policy will take as input. This parameter is optional. If not specified, the masking policy uses *output\_column\_names* as inputs.

*input\_paths*   
The full path of the SUPER object that the masking policy will take as input. This parameter is optional. If not specified, the masking policy uses *output\_path* for inputs.

*user\_name*   
The name of the user to whom the masking policy will attach. You can't attach two policies to the same combination of user and column or role and column. You can attach a policy to a user and another policy to the user's role. In this case, the policy with the higher priority applies.  
You can only set one of user\_name, role\_name, and PUBLIC in a single ATTACH MASKING POLICY command. 

*role\_name*   
The name of the role to which the masking policy will attach. You can't attach two policies to the same column/role pair. You can attach a policy to a user and another policy to the user's role. In this case, the policy with the higher priority applies.  
You can only set one of user\_name, role\_name, and PUBLIC in a single ATTACH MASKING POLICY command. 

*PUBLIC*   
Attaches the masking policy to all users accessing the table. You must give other masking policies attached to specific column/user or column/role pairs a higher priority than the PUBLIC policy for them to apply.  
You can only set one of user\_name, role\_name, and PUBLIC in a single ATTACH MASKING POLICY command. 

*priority*   
The priority of the masking policy. When multiple masking policies apply to a given user's query, the highest priority policy applies.  
You can't attach two different policies to the same column with equal priority, even if the two policies are attached to different users or roles. You can attach the same policy multiple times to the same set of table, output column, input column, and priority parameters, as long as the user or role the policy attaches to is different each time.   
You can't apply a policy to a column with the same priority as another policy attached to that column, even if they're for different roles. This field is optional. If you don't specify a priority, the masking policy defaults to attaching with a priority of 0.

For the usage of ATTACH MASKING POLICY on Amazon Redshift Federated Permissions Catalog, see [ Managing access control with Amazon Redshift federated permissions](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-managing-access.html).