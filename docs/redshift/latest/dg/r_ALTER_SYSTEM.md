Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER SYSTEM

Changes a system-level configuration option for the Amazon Redshift cluster or Redshift Serverless
workgroup.

## Required privileges

One of the following user types can run the ALTER SYSTEM command:

- Superuser
- Admin user

## Syntax

```
ALTER SYSTEM SET *system-level-configuration* = {true| t | on | false | f | off}
```

## Parameters

_system-level-configuration_

A system-level configuration. Valid value:
`data_catalog_auto_mount` and
`metadata_security`.

{true| t | on | false | f | off}

A value to activate or deactivate the system-level configuration. A
`true`, `t`, or `on` indicates to activate
the configuration. A `false`, `f`, or `off`
indicates to deactivate the configuration.

## Usage notes

For a provisioned cluster, changes to `data_catalog_auto_mount` take
effect on the next reboot of the cluster. For more information, see [Rebooting a
cluster](../mgmt/managing-clusters-console.md#reboot-cluster "../mgmt/managing-clusters-console.md#reboot-cluster") in the _Amazon Redshift Management Guide_.

For a serverliess workgroup, changes to `data_catalog_auto_mount` do not
take effect immediately.

## Examples

The following example turns on automounting the AWS Glue Data Catalog.

```
ALTER SYSTEM SET data_catalog_auto_mount = true;
```

The following example turns on metadata security.

```
ALTER SYSTEM SET metadata_security = true;
```

### Setting a default identity

namespace

This example is specific to working with an identity provider. You can integrate
Redshift with IAM Identity Center and an identity provider to centralize identity management for
Redshift and other AWS services.

The following sample shows how to set the default identity namespace for the
system. Doing this subsequently makes it more simple to run GRANT and CREATE
statements, because you don't have to include the namespace as a prefix for each
identity.

```
ALTER SYSTEM SET default_identity_namespace = 'MYCO';
```

After running the command, you can run statements like the following:

```
GRANT SELECT ON TABLE mytable TO alice;

GRANT UPDATE ON TABLE mytable TO salesrole;

CREATE USER bob password 'md50c983d1a624280812631c5389e60d48c';
```

The effect of setting the default identity namespace is that each identity doesn't
require it as a prefix. In this example, `alice` is replaced with
`MYCO:alice`. This happens with any identity included. For more
information about using an identity provider with Redshift, see [Connect Redshift
with IAM Identity Center to give users a single sign-on experience](../mgmt/redshift-iam-access-control-idp-connect.md "../mgmt/redshift-iam-access-control-idp-connect.md").

For more information about settings that pertain to Redshift configuration with
IAM Identity Center, see [SET](r_SET.md "r_SET.md") and [ALTER IDENTITY PROVIDER](r_ALTER_IDENTITY_PROVIDER.md "r_ALTER_IDENTITY_PROVIDER.md").
