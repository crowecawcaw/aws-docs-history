# Using PL/Rust to write PostgreSQL

functions in the Rust language

PL/Rust is a trusted Rust language extension for PostgreSQL. You can use it for stored
procedures, functions, and other procedural code that's callable from SQL. The PL/Rust
language extension is available in the following versions:

- RDS for PostgreSQL 17.1 and higher 17 versions
- RDS for PostgreSQL 16.1 and higher 16 versions
- RDS for PostgreSQL 15.2-R2 and higher 15 versions
- RDS for PostgreSQL 14.9 and higher 14 versions
- RDS for PostgreSQL 13.12 and higher 13 versions
  For more information, see [PL/Rust](https://github.com/tcdi/plrust#readme "https://github.com/tcdi/plrust#readme") on GitHub.

###### Topics

- [Setting up PL/Rust](#PL_Rust-setting-up "#PL_Rust-setting-up")
- [Creating functions with PL/Rust](#PL_Rust-create-function "#PL_Rust-create-function")
- [Using crates with PL/Rust](#PL_Rust-crates "#PL_Rust-crates")
- [PL/Rust limitations](#PL_Rust-limitations "#PL_Rust-limitations")

## Setting up PL/Rust

To install the plrust extension on your DB instance, add plrust to the
`shared_preload_libraries` parameter in the DB parameter group associated with
your DB instance. With the plrust extension installed, you can create functions.

To modify the `shared_preload_libraries` parameter, your DB instance must be
associated with a custom parameter group. For information about creating a custom DB
parameter group, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

You can install the plrust extension using the AWS Management Console or the AWS CLI.

The following steps assume that your DB instance is associated with a custom DB
parameter group.

###### Install the plrust extension in the `shared_preload_libraries`

parameter

Complete the following steps using an account that is a member of the
`rds_superuser` group (role).

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the name of your DB instance to display its details.
4. Open the **Configuration** tab for your DB instance and find
   the DB instance parameter group link.
5. Choose the link to open the custom parameters associated with your DB instance.
6. In the **Parameters** search field, type
   `shared_pre` to find the
   **`shared_preload_libraries`** parameter.
7. Choose **Edit parameters** to access the property
   values.
8. Add plrust to the list in the **Values** field. Use a comma to
   separate items in the list of values.
9. Reboot the DB instance so that your change to the
   `shared_preload_libraries` parameter takes effect. The initial reboot
   may require additional time to complete.
10. When the instance is available, verify that plrust has been initialized. Use
    `psql` to connect to the DB
    instance, and then run the following command.

```
`SHOW shared_preload_libraries;`
```

Your output should look similar to the following:

```
`shared_preload_libraries
--------------------------
rdsutils,plrust
(1 row)`
```

###### Install the plrust extension in the shared_preload_libraries parameter

Complete the following steps using an account that is a member of the
`rds_superuser` group (role).

1. Use the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md") AWS CLI command to add plrust to the
   `shared_preload_libraries` parameter.

```
aws rds modify-db-parameter-group \
   --db-parameter-group-name `custom-param-group-name` \
   --parameters "ParameterName=shared_preload_libraries,ParameterValue=plrust,ApplyMethod=pending-reboot" \
   --region `aws-region`
```

2. Use the [reboot-db-instance](../../../cli/latest/reference/rds/reboot-db-instance.md "../../../cli/latest/reference/rds/reboot-db-instance.md") AWS CLI command to reboot the DB instance and initialize the plrust library. The
   initial reboot may require additional time to complete.

```
aws rds reboot-db-instance \
    --db-instance-identifier `your-instance` \
    --region `aws-region`
```

3. When the instance is available, you can verify that plrust has been initialized.
   Use `psql` to connect to the DB
   instance, and then run the following command.

```
`SHOW shared_preload_libraries;`
```

Your output should look similar to the following:

```
`shared_preload_libraries
--------------------------
rdsutils,plrust
(1 row)`
```

## Creating functions with PL/Rust

PL/Rust will compile the function as a dynamic library, load it, and execute it.

The following Rust function filters multiples out of an array.

```
postgres=> CREATE LANGUAGE plrust;
CREATE EXTENSION
```

```
CREATE OR REPLACE FUNCTION filter_multiples(a BIGINT[], multiple BIGINT) RETURNS BIGINT[]
    IMMUTABLE STRICT
    LANGUAGE PLRUST AS
$$
    Ok(Some(a.into_iter().filter(|x| x.unwrap() % multiple != 0).collect()))
$$;

WITH gen_values AS (
SELECT ARRAY(SELECT * FROM generate_series(1,100)) as arr)
SELECT filter_multiples(arr, 3)
from gen_values;
```

## Using crates with PL/Rust

In RDS for PostgreSQL versions 16.3-R2 and higher, 15.7-R2 and higher 15 versions, 14.12-R2
and higher 14 versions, and 13.15-R2 and higher 13 versions, PL/Rust supports additional
crates:

- `url`
- `regex`
- `serde`
- `serde_json`

In RDS for PostgreSQL versions 15.5-R2 and higher, 14.10-R2 and higher 14 versions, and
13.13-R2 and higher 13 versions, PL/Rust supports two additional crates:

- `croaring-rs`
- `num-bigint`

Starting with Amazon RDS for PostgreSQL versions 15.4, 14.9, and 13.12, PL/Rust supports the
following crates:

- `aes`
- `ctr`
- `rand`

Only the default features are supported for these crates. New RDS for PostgreSQL versions
might contain updated versions of crates, and older versions of crates may no longer be
supported.

Follow the best practices for performing a major version upgrade to test whether your
PL/Rust functions are compatible with the new major version. For more information, see the
blog [Best practices for upgrading Amazon RDS to major and minor versions of PostgreSQL](https://aws.amazon.com/blogs/database/best-practices-for-upgrading-amazon-rds-to-major-and-minor-versions-of-postgresql/ "https://aws.amazon.com/blogs/database/best-practices-for-upgrading-amazon-rds-to-major-and-minor-versions-of-postgresql/")
and [Upgrading the
PostgreSQL DB engine for Amazon RDS](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md") in the Amazon RDS User Guide.

Examples of using dependencies when creating a PL/Rust function are available at [Use
dependencies](https://tcdi.github.io/plrust/use-plrust.html#use-dependencies "https://tcdi.github.io/plrust/use-plrust.html#use-dependencies").

## PL/Rust limitations

By default, database users can't use PL/Rust. To provide access to PL/Rust, connect as a
user with rds_superuser privilege, and run the following command:

```
postgres=> GRANT USAGE ON LANGUAGE PLRUST TO `user`;
```
