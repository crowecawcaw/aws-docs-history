Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using Data API with trusted

identity propagation

As an Amazon Redshift account administrator, you can integrate your Amazon Redshift cluster or workgroup
with AWS IAM Identity Center, which helps manage your workforce access to Amazon Redshift with single sign-on.
For more information, see [Setting up AWS IAM Identity Center
integration with Amazon Redshift](redshift-iam-access-control-idp-connect-console.md "redshift-iam-access-control-idp-connect-console.md"). The
Amazon Redshift Data API supports propagating IAM Identity Center user identities to an Amazon Redshift cluster or
workgroup, and to other services, such as, AWS Lake Formation, down the chain. You can set up and
query using the Data API by following the steps in [Access AWS services programmatically using trusted identity
propagation](https://aws.amazon.com/blogs/security/access-aws-services-programmatically-using-trusted-identity-propagation/ "https://aws.amazon.com/blogs/security/access-aws-services-programmatically-using-trusted-identity-propagation/").

When you call the Data API using an IAM Identity Center user identity from an identity-enhanced
IAM role session, you can only access the resulting statement and statement result
using the same IAM Identity Center user. For example, the following AWS CLI command calls the
`execute-statement` operation to
run a SQL command with trusted identity propagation.

```
aws redshift-data execute-statement
--sql "`select current_user;`"
--cluster-id `mycluster`
--database `dev`

```

The following AWS CLI command calls the `batch-execute-statement` operation
to run two SQL commands.

```
aws redshift-data batch-execute-statement
--sqls  "`select current_user;`"  "`select current_date;`"
--cluster-id `mycluster`
--database `dev`

```

To access statements with `cancel-statement`,
`describe-statement`, `get-statement-result`, and
`get-statement-result-v2` submitted by identity-enhanced IAM role
sessions, the IAM Identity Center user and IAM role must match the credentials used
to run `execute-statment` or `batch-execute-statement`. For
example, the following AWS CLI command gets the results of a SQL statement.

```
aws redshift-data get-statement-result
--id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`

```

To list statements, a `cluster-identifier` or `workgroup-name`
parameter must be provided to ensure that the IAM Identity Center user only has access the Amazon Redshift IAM Identity Center
applications they are assigned to. For example, the following AWS CLI command lists
statements for a specific cluster.

```
aws redshift-data list-statements
--cluster-identifier `mycluster`

```

You can also invoke the Data API operations that access database objects in a
cluster or workgroup using trusted identity propagation. This includes the
`list-databases`, `list-schemas`, `list-tables`,
and `describe-table` operations.

API calls made by the IAM Identity Center user can be tracked in AWS CloudTrail. A `onBehalfOf`
section of the CloudTrail event shows the IAM Identity Center user id and the identity store ARN. The
following example shows a snippet of a CloudTrail event showing the `onBehalfOf`
section with the IAM Identity Center user ID of
`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` and the Identity store ARN of
`arn:aws:identitystore::123456789012:identitystore/d-9067bc44d2`.

```
{
            "eventVersion":"1.10",
            "userIdentity":{
            "type":"AssumedRole",
            ...
            },
            "onBehalfOf":{
            "userId":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "identityStoreArn":"arn:aws:identitystore::123456789012:identitystore/d-9067bc44d2"
            }
            },
            "eventTime":"2025-01-13T04:46:27Z",
            "eventSource":"redshift-data.amazonaws.com",
            "eventName":"ExecuteStatement",
            "awsRegion":"us-east-1"
            }
```

You can run the following SQL command to check the query submitted by the IAM
Identity Center user. In this example, the email registered in Identity Center is
`username@example.com`.

```
SELECT
    h.query_id,
    h.database_name,
    h.status,
    h.query_text,
    u.usename,
    h.start_time,
    h.end_time
FROM
    sys_query_history h
LEFT JOIN
    pg_user u
ON
    h.user_id = u.usesysid
where u.usename='awsidc:`username@example.com`'
ORDER BY
    h.start_time DESC;
```
