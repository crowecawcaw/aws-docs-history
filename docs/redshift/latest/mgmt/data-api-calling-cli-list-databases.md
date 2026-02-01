Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# List databases in a

cluster

To list the databases in a cluster, use the `aws redshift-data
 list-databases` AWS CLI command.

The following AWS CLI command runs a SQL statement against a cluster to list
databases. This example uses the AWS Secrets Manager authentication method.

```

aws redshift-data list-databases

    --secret-arn arn:aws:secretsmanager:us-west-2:123456789012:secret:myuser-secret-hKgPWn
    --cluster-identifier mycluster-test
    --database dev

```

The following is an example of the response.

```
{
    "Databases": [
        "dev"
    ]
}
```

The following AWS CLI command runs a SQL statement against a cluster to list
databases. This example uses the temporary credentials authentication method.

```

aws redshift-data list-databases
    --db-user myuser
    --cluster-identifier mycluster-test
    --database dev

```

The following is an example of the response.

```
{
    "Databases": [
        "dev"
    ]
}
```
