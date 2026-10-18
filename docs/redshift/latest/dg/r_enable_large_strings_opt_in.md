

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# enable\_large\_strings\_opt\_in
<a name="r_enable_large_strings_opt_in"></a>

## Values (default in bold)
<a name="r_enable_large_strings_opt_in-values"></a>

Yes, No, **not set** (preserves existing cluster behavior)

## Description
<a name="r_enable_large_strings_opt_in-description"></a>

Determines whether Amazon Redshift supports individual strings up to 16,000,000 bytes in the SUPER data type and in-memory string operations.

When set to `Yes`:
+ Individual strings that you store in the SUPER data type can be up to 16,000,000 bytes.
+ In-memory string functions can process `VARCHAR` values up to 16,000,000 bytes.
+ `VARCHAR(MAX)` resolves to `VARCHAR(16000000)` in expression contexts, such as `CAST` expressions, views, user-defined functions (UDFs), and stored procedures.
+ `CREATE TABLE` with `VARCHAR(MAX)` continues to create `VARCHAR(65535)` columns.

When set to `No`:
+ Individual strings in SUPER columns have a limit of 65,535 bytes.
+ String functions can process `VARCHAR` values up to 65,535 bytes.

When this parameter is not set, Amazon Redshift preserves the existing behavior of your cluster.

For a provisioned cluster, you must reboot the cluster to apply this parameter. To check the current state of your cluster, run the following command:

```
SELECT is_large_string_enabled();
```

When you reset `enable_large_strings_opt_in` through `ResetClusterParameterGroup`, Amazon Redshift preserves the original value of the parameter. After you set `enable_large_strings_opt_in` to `Yes` or `No`, you can't reset it to the default value.