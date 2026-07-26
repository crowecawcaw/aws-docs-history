Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# List sessions

To list the sessions that you created in the last 24 hours, use the `aws
 redshift-data list-sessions` AWS CLI command. By default, the command returns
only sessions with a status of `AVAILABLE` or `BUSY`. You can
filter the results by session status, compute target (cluster or serverless
workgroup), or database. Your IAM permissions determine whether you can run this
command. For more information about sessions, see [Running SQL statements with session reuse when calling the Amazon Redshift Data API](data-api.md#data-api-calling-considerations-session-reuse "data-api.md#data-api-calling-considerations-session-reuse").

The following AWS CLI command lists the sessions that ran on a cluster:

```

 aws redshift-data list-sessions
    --cluster-identifier mycluster-test

```

The following is an example of the response:

```
{
    "Sessions": [
        {
            "SessionId": "5a254dc6-4fc2-4203-87a8-551155432ee4",
            "Status": "AVAILABLE",
            "CreatedAt": 1703022996.436,
            "UpdatedAt": 1703023010.221,
            "Database": "dev",
            "DbUser": "awsuser",
            "ClusterIdentifier": "mycluster-test",
            "SessionAliveSeconds": 10,
            "SessionTtl": 1703023020.436
        },
        {
            "SessionId": "8b365ed7-5gd7-5314-98b9-662266543ff5",
            "Status": "BUSY",
            "CreatedAt": 1703023100.512,
            "UpdatedAt": 1703023150.874,
            "Database": "dev",
            "DbUser": "awsuser",
            "ClusterIdentifier": "mycluster-test",
            "SessionAliveSeconds": 60,
            "SessionTtl": 1703023210.512,
            "CurrentStatementId": "c016234e-5c6c-4bc5-bb16-2c5b8ff61814"
        }
    ]
}
```

The following AWS CLI command lists the `CLOSED` sessions on a serverless
workgroup by filtering on session status:

```

aws redshift-data list-sessions
    --workgroup-name myworkgroup
    --status CLOSED

```

The following is an example of the response:

```
{
    "Sessions": [
        {
            "SessionId": "07c5ffea-76d6-4786-b62c-4fe3ef529680",
            "Status": "CLOSED",
            "CreatedAt": 1703019996.436,
            "UpdatedAt": 1703020056.436,
            "Database": "dev",
            "DbUser": "IAMR:RoleName",
            "WorkgroupName": "myworkgroup",
            "SessionAliveSeconds": 60,
            "SessionTtl": 1703020056.436
        }
    ]
}
```

###### Note

If you use identity-enhanced IAM role sessions, then you must provide either
the `cluster-identifier` or `workgroup-name` parameter.
With this parameter, you ensure that the AWS IAM Identity Center user can access only the Amazon Redshift IAM Identity Center applications
that they are assigned to. For more information, see [Using Data API with trusted identity propagation](data-api-trusted-identity-propagation.md "data-api-trusted-identity-propagation.md").
