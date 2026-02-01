Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Scalar Lambda UDFs

Amazon Redshift can use custom functions defined in AWS Lambda as part of SQL queries. You can
write scalar Lambda UDFs in any programming languages supported by Lambda, such as Java, Go,
PowerShell, Node.js, C#, Python, and Ruby. Or you can use a custom runtime.

The [CREATE EXTERNAL FUNCTION](r_CREATE_EXTERNAL_FUNCTION.md "r_CREATE_EXTERNAL_FUNCTION.md") command creates the following
parameters:

- (Optional) A list of arguments with data type.
- One return data type.
- One function name of the external function that is called by Amazon Redshift.
- One IAM role that the Amazon Redshift cluster is authorized to assume and call to
  Lambda.
- One Lambda function name that the Lambda UDF invokes.
  For information about CREATE EXTERNAL FUNCTION, see [CREATE EXTERNAL FUNCTION](r_CREATE_EXTERNAL_FUNCTION.md "r_CREATE_EXTERNAL_FUNCTION.md").

The input and return data types for Lambda UDFs can be any of the following types:

- SMALLINT
- INTEGER
- BIGINT
- DECIMAL
- REAL
- DOUBLE PRECISION
- CHAR
- VARCHAR
- BOOLEAN
- DATE
- TIMESTAMP
  The aliases for these types are also valid. For a full list of data types and their aliases,
  see [Data types](c_Supported_data_types.md "c_Supported_data_types.md").

Amazon Redshift ensures that the external function can send and receive batched arguments and
results.

Lambda UDFs are defined and managed in Lambda, and you can control the access privileges
to invoke these UDFs in Amazon Redshift. You can invoke multiple Lambda functions in the same query
or invoke the same function multiple times.

Use Lambda UDFs in any clauses of the SQL statements where scalar functions are
supported. You can also use Lambda UDFs in any SQL statement such as SELECT, UPDATE, INSERT,
or DELETE.

###### Note

Using Lambda UDFs can incur additional charges from the Lambda service. Whether it does so
depends on factors such as the numbers of Lambda requests (UDF invocations) and the total
duration of the Lambda program execution. However, there is no additional charge to use
Lambda UDFs in Amazon Redshift. For information about AWS Lambda pricing, see [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing "https://aws.amazon.com/lambda/pricing").

The number of Lambda requests varies depending on the specific SQL statement clause
where the Lambda UDF is used. For example, suppose the function is used in a WHERE clause
such as the following.

`SELECT a, b FROM t1 WHERE lambda_multiply(a, b) = 64; SELECT a, b FROM t1 WHERE
 a*b = lambda_multiply(2, 32)`

In this case, Amazon Redshift calls the first SELECT statement for each and calls the second
SELECT statement only once.

However, using a UDF in the projection part of the query might only invoke the Lambda
function once for every qualified or aggregated row in the result set.

## UDF security and permissions

To create a Lambda UDF, make sure that you have permissions for usage on the LANGUAGE EXFUNC. You must explicitly grant USAGE ON LANGUAGE EXFUNC or revoke USAGE ON LANGUAGE
EXFUNC to specific users, groups, or public.

The following example grants usage on EXFUNC to PUBLIC.

```
grant usage on language exfunc to PUBLIC;
```

The following example revokes usage on exfunc from PUBLIC and then grants usage to
the user group lambda_udf_devs.

```
revoke usage on language exfunc from PUBLIC;
grant usage on language exfunc to group lambda_udf_devs;
```

To run a Lambda UDF, make sure that you have permission for each function called. By
default, permission to run new Lambda UDFs is granted to PUBLIC. To restrict usage,
revoke this permission from PUBLIC for the function. Then, grant the privilege to
specific users or groups.

The following example revokes execution on the function exfunc_sum from PUBLIC.
Then, it grants usage to the user group lambda_udf_devs.

```
revoke execute on function exfunc_sum(int, int) from PUBLIC;
grant execute on function exfunc_sum(int, int) to group lambda_udf_devs;
```

Superusers have all privileges by default.

For more information about granting and revoking privileges, see [GRANT](r_GRANT.md "r_GRANT.md") and [REVOKE](r_REVOKE.md "r_REVOKE.md").

## Configuring the authorization parameter for

Lambda UDFs

The CREATE EXTERNAL FUNCTION command requires authorization to invoke Lambda functions in AWS Lambda.
To start authorization, specify an AWS Identity and Access Management (IAM) role when you run the CREATE EXTERNAL FUNCTION command. For more information about IAM roles,
see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _IAM User Guide_.

If there is an existing IAM role with permissions to invoke Lambda functions
attached to your cluster, then you can substitute your role Amazon Resource Name (ARN)
in the IAM_ROLE parameter for the command. Following sections describe the steps for
using an IAM role in the CREATE EXTERNAL FUNCTION command.

### Creating an IAM role for Lambda

The IAM role requires permission to invoke Lambda functions. While creating the IAM role, provide the permission in one of the
following ways:

- Attach the `AWSLambdaRole` policy on the **Attach permissions
  policy** page while creating an IAM role. The
  `AWSLambdaRole` policy grants permissions to invoke Lambda
  functions which is the minimal requirement. For more information and other
  policies, see [Identity-based IAM
  policies for AWS Lambda](../../../lambda/latest/dg/access-control-identity-based.md "../../../lambda/latest/dg/access-control-identity-based.md") in the
  _AWS Lambda Developer Guide_.
- Create your own custom policy to attach to your IAM role with the
  `lambda:InvokeFunction` permission of either all resources or a
  particular Lambda function with the ARN of that function. For more information
  on how to create a policy, see [Creating IAM
  policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

The following example policy enables invoking Lambda on a particular
Lambda function.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Invoke",
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-west-2:123456789012:function:my-function"
 }
 ]
}`

```

For more information on resources for Lambda functions, see [Resources and conditions for Lambda actions](../../../lambda/latest/dg/lambda-api-permissions-ref.md "../../../lambda/latest/dg/lambda-api-permissions-ref.md") in the _IAM API Reference_.

After creating your custom policy with the required permissions, you
can attach your policy to the IAM role on the **Attach permissions
policy** page while creating an IAM role.

For steps to create an IAM role, see [Authorizing Amazon Redshift
to access other AWS services on your behalf](../mgmt/authorizing-redshift-service.md "../mgmt/authorizing-redshift-service.md") in the
_Amazon Redshift Management Guide_.

If you don't want to create a new IAM role, you can add the permissions
mentioned previously to your existing IAM role.

### Associating an IAM role with the cluster

Attach the IAM role to your cluster. You can add a
role to a cluster or view the roles associated with a cluster by using the Amazon
Redshift Management Console, CLI, or API. For more information, see [Associating an
IAM Role With a Cluster](../mgmt/copy-unload-iam-role.md "../mgmt/copy-unload-iam-role.md") in
the _Amazon Redshift Management Guide_.

### Including the IAM role in the command

Include the IAM role ARN in the CREATE EXTERNAL FUNCTION command. When you
create an IAM role, IAM returns an Amazon Resource Name (ARN) for the role. To
specify an IAM role, provide the role ARN with the `IAM_ROLE` parameter. The
following shows the syntax for the `IAM_ROLE` parameter.

```
IAM_ROLE 'arn:aws:iam::aws-account-id:role/role-name'
```

To invoke Lambda functions which reside
in other accounts within the same Region, see [Chaining IAM roles in Amazon Redshift](../mgmt/authorizing-redshift-service.md#authorizing-redshift-service-chaining-roles.html "../mgmt/authorizing-redshift-service.md#authorizing-redshift-service-chaining-roles.html").

## Using the JSON interface between Amazon Redshift and

AWS Lambda

Amazon Redshift uses a common interface for all Lambda functions that Amazon Redshift communicates
to.

The following table shows the list of input fields that the designated Lambda
functions that you can expect for the JSON payload.

| Field name        | Description                                                                             | Value range                                                                                                                                                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_id        | A universally unique identifier (UUID) that uniquely identifies each invoke<br>request. | A valid UUID.                                                                                                                                                                                                               |
| cluster           | The full Amazon Resource Name (ARN) of the<br>cluster.                                  | A valid cluster ARN.                                                                                                                                                                                                        |
| user              | The name of the user that makes the call.                                               | A valid user name.                                                                                                                                                                                                          |
| database          | The name of the database that the query is running on.                                  | A valid database name.                                                                                                                                                                                                      |
| external_function | The fully qualified name of the external function that makes the call.                  | A valid fully qualified function name.                                                                                                                                                                                      |
| query_id          | The query ID of the query that is making the call.                                      | A valid query ID.                                                                                                                                                                                                           |
| num_records       | The number of arguments in the payload.                                                 | A value of 1<br>• 2^64.                                                                                                                                                                                                     |
| arguments         | The data payload in the specified format.                                               | The data in array format must be a JSON array. Each element is a record that is an array if the number of arguments is larger than 1. By using an array, Amazon Redshift preserves the order of the records in the payload. |

The order of the JSON array determines the order of batch processing. The Lambda
function must process the arguments iteratively and produce the exact number of
records. The following is an example of a payload.

```
{
  "request_id" : "23FF1F97-F28A-44AA-AB67-266ED976BF40",
  "cluster" : "arn:aws:redshift:xxxx",
  "user" : "adminuser",
  "database" : "db1",
  "external_function": "public.foo",
  "query_id" : 5678234,
  "num_records" : 4,
  "arguments" : [
     [ 1, 2 ],
     [ 3, null],
     null,
     [ 4, 6]
   ]
 }
```

The return output of the Lambda function contains the following fields.

| Field name  | Description                                                                                                          | Value range                       |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| success     | The indication of success or failure for the<br>function.                                                            | A value of `"true"` or `"false"`. |
| error_msg   | The error message if the success value is<br>`"false"` (if the function fails); otherwise, this field is<br>ignored. | A valid message.                  |
| num_records | The number of records in the payload.                                                                                | A value of 1<br>• 2^64.           |
| results     | The results of the call in the specified format.                                                                     | N/A                               |

The following is an example of the Lambda function output.

```
{
  "success": true,   // true indicates the call succeeded
  "error_msg" : "my function isn't working",  // shall only exist when success != true
  "num_records": 4,      // number of records in this payload
  "results" : [
     1,
     4,
     null,
     7
   ]
}
```

When you call Lambda functions from SQL queries, Amazon Redshift ensures the security of the
connection with the following considerations:

- GRANT and REVOKE permissions. For more information about UDF security and permissions, see [UDF security and permissions](udf-security-and-privileges.md "udf-security-and-privileges.md").
- Amazon Redshift only submits the minimum set of data to the designated Lambda function.
- Amazon Redshift only calls the designated Lambda function with the designated IAM role.
