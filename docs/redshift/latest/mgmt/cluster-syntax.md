Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Connecting to Amazon Redshift

You can connect to your database using the following syntax.

```
`cluster-name`.`account-number`.`aws-region`.redshift.amazonaws.com/`database-name`
```

The syntax elements are defined as follows.

- `cluster-name`

Your cluster's name.

- `account-number`

The unique identifier associated with your AWS account number in a given
AWS Region. All clusters created by a given account in a given AWS Region
have the same `account-number`.

- `aws-region`

The code for the AWS Region that the cluster is in.

- `database-name`

Your database's name.
For example, the following connection string specifies the `my-db` database
in the `my-cluster` cluster in the us-east-1 AWS Region.

```
my-cluster.123456789012.us-east-1.redshift.amazonaws.com/my-db
```
