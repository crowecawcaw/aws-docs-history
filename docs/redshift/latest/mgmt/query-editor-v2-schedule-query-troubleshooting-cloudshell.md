Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing the

results of a scheduled query with AWS CloudShell

You can use AWS CloudShell to find out details about a schedule query. You must have the
proper permissions to run the AWS CLI commands shown in the following procedure.

###### To view the results of a scheduled query

1. On the AWS console, open the AWS CloudShell command prompt. For more information
   about AWS CloudShell, see [What is AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") in
   the _AWS CloudShell User Guide_.
2. Assume the IAM role of the scheduled query. To assume the role, find the
   IAM role associated with the scheduled query in query editor v2 and use it in the AWS CLI
   command in AWS CloudShell. For example, for the role `scheduler` enter an
   AWS STS command to assume the role used by the scheduled query.

```
aws sts assume-role --role-arn "arn:aws:iam::`123456789012`:role/scheduler" --role-session-name "scheduler-test"
```

The credentials returned are similar to the following.

```
"Credentials": {
"AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
"SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
"SessionToken": "je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY...",
"Expiration": "2023-08-18T18:19:44+00:00"
},
"AssumedRoleUser": {
"AssumedRoleId": "AROA35B2NH6WBTP7ONL4E:scheduler-test",
"Arn": "arn:aws:sts::`123456789012`:assumed-role/scheduler/scheduler-test"
}
}

```

3. Create environmental variables in the AWS CLI using the credentials displayed
   from assuming the IAM role. You must use these tokens before their expiration
   time. For example, you enter the following in AWS CloudShell.

```

export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_SESSION_TOKEN=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY...

```

4. To view the error of a failed query, run the AWS CLI command to describe a
   statement. The id of the SQL statement is from the **ID** shown
   in the **Schedule history** section of a scheduled query in the
   query editor v2.

```
aws redshift-data describe-statement --id `130d2620-05d2-439c-b7cf-815d9767f513`
```

In this example, the scheduled SQL `select * from users limit 100`
results in a SQL error that the `users` table does not exist.

```
{
"CreatedAt": "2023-08-18T17:39:15.563000+00:00",
"Duration": -1,
"Error": "ERROR: relation \"users\" does not exist",
"HasResultSet": false,
"Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"QueryString": "select * from users limit 100\n—RequestID=a1b2c3d4-5678-90ab-cdef-EXAMPLE22222; TraceID=1-633c5642-4039308d03f3a0ba53dbdf6f",
"RedshiftPid": 1073766651,
"RedshiftQueryId": 0,
"ResultRows": -1,
"ResultSize": -1,
"Status": "FAILED",
"UpdatedAt": "2023-08-18T17:39:16.116000+00:00",
"WorkgroupName": "default"
}
```
