

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ALTER MASKING POLICY
<a name="r_ALTER_MASKING_POLICY"></a>

Alters an existing dynamic data masking policy. For more information on dynamic data masking, see [Dynamic data masking](t_ddm.md).

Superusers and users or roles that have the sys:secadmin role can alter a masking policy.

## Syntax
<a name="r_ALTER_MASKING_POLICY-synopsis"></a>

```
ALTER MASKING POLICY
{ policy_name | database_name.policy_name }
USING (masking_expression);
```

## Parameters
<a name="r_ALTER_MASKING_POLICY-parameters"></a>

*policy\_name*   
 The name of the masking policy. This must be the name of a masking policy that already exists in the database. 

database\_name  
The name of the database from where the policy is created. The database can be the connected database or a database that supports Amazon Redshift federated permissions.

*masking\_expression*  
The SQL expression used to transform the target columns. It can be written using data manipulation functions such as String manipulation functions, or in conjunction with user-defined functions written in SQL, Python, or with AWS Lambda.   
 The expression must match the original expression's input columns and data types. For example, if the original masking policy's input columns were `sample_1 FLOAT` and `sample_2 VARCHAR(10)`, you wouldn't be able to alter the masking policy to take a third column, or make the policy take a FLOAT and a BOOLEAN. If you use a constant as your masking expression, you must explicitly cast it to a type that matches the input type.  
 You must have the USAGE permission on any user-defined functions that you use in the masking expression. 

For the usage of ALTER MASKING POLICY on Amazon Redshift Federated Permissions Catalog, see [ Managing access control with Amazon Redshift federated permissions](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-managing-access.html).