Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# List schemas in a

database

To list the schemas in a database, use the `aws redshift-data
 list-schemas` AWS CLI command.

The following AWS CLI command runs a SQL statement against a cluster to list schemas
in a database. This example uses the AWS Secrets Manager authentication method.

```

aws redshift-data list-schemas
    --secret-arn arn:aws:secretsmanager:us-west-2:123456789012:secret:myuser-secret-hKgPWn
    --cluster-identifier mycluster-test
    --database dev

```

The following is an example of the response.

```
{
    "Schemas": [
        "information_schema",
        "pg_catalog",
        "pg_internal",
        "public"
    ]
}
```

The following AWS CLI command runs a SQL statement against a cluster to list schemas
in a database. This example uses the temporary credentials authentication
method.

```

aws redshift-data list-schemas
    --db-user mysuser
    --cluster-identifier mycluster-test
    --database dev

```

The following is an example of the response.

```
{
    "Schemas": [
        "information_schema",
        "pg_catalog",
        "pg_internal",
        "public"
    ]
}
```
