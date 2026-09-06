

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CREATE MASKING POLICY
<a name="r_CREATE_MASKING_POLICY"></a>

Creates a new dynamic data masking policy to obfuscate data of a given format. For more information on dynamic data masking, see [Dynamic data masking](t_ddm.md).

Superusers and users or roles that have the sys:secadmin role can create a masking policy.

## Syntax
<a name="r_CREATE_MASKING_POLICY-synopsis"></a>

```
CREATE MASKING POLICY 
   { policy_name | database_name.policy_name } [IF NOT EXISTS]
   WITH (input_columns)
   USING (masking_expression);
```

## Parameters
<a name="r_CREATE_MASKING_POLICY-parameters"></a>

 *policy\_name*   
The name of the masking policy. The masking policy can't have the same name as another masking policy that already exists in the database.

database\_name  
The name of the database where the policy will be created. Policy can be created on the connected database or on Amazon Redshift Federated Permissions Catalog.

*input\_columns*   
A tuple of column names in the format (col1 type, col2 type ...).  
Column names are used as the input for the masking expression. Column names don't have to match the names of the columns being masked, but the input and output data types must match.

*masking\_expression*  
The SQL expression used to transform the target columns. It can be written using data manipulation functions such as String manipulation functions, or in conjunction with user-defined functions written in SQL, Python, or with AWS Lambda. You can include a tuple of column expressions for masking policies that have multiple outputs. If you use a constant as your masking expression, you must explicitly cast it to a type that matches the input type.  
 You must have the USAGE permission on any user-defined functions that you use in the masking expression. 

For the usage of CREATE MASKING POLICY on Amazon Redshift Federated Permissions Catalog, see [ Managing access control with Amazon Redshift federated permissions](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-managing-access.html).