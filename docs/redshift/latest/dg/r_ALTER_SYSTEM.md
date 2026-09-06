

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ALTER SYSTEM
<a name="r_ALTER_SYSTEM"></a>

Changes a system-level configuration option for the Amazon Redshift cluster or Redshift Serverless workgroup.

## Required privileges
<a name="r_ALTER_SYSTEM-privileges"></a>

One of the following user types can run the ALTER SYSTEM command:
+ Superuser
+ Admin user

## Syntax
<a name="r_ALTER_SYSTEM-synopsis"></a>

```
ALTER SYSTEM SET system-level-configuration = {true| t | on | false | f | off}
```

## Parameters
<a name="r_ALTER_SYSTEM-parameters"></a>

 *system-level-configuration*   
A system-level configuration. Valid value: `data_catalog_auto_mount` and `metadata_security`.

{true\| t \| on \| false \| f \| off}   
A value to activate or deactivate the system-level configuration. A `true`, `t`, or `on` indicates to activate the configuration. A `false`, `f`, or `off` indicates to deactivate the configuration.

## Usage notes
<a name="r_ALTER_SYSTEM-usage-notes"></a>

For a provisioned cluster, changes to `data_catalog_auto_mount` take effect on the next reboot of the cluster. For more information, see [Rebooting a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html#reboot-cluster) in the *Amazon Redshift Management Guide*.

For a serverliess workgroup, changes to `data_catalog_auto_mount` do not take effect immediately.

## Examples
<a name="r_ALTER_SYSTEM-examples"></a>

The following example turns on automounting the AWS Glue Data Catalog.

```
ALTER SYSTEM SET data_catalog_auto_mount = true;
```

The following example turns on metadata security.

```
ALTER SYSTEM SET metadata_security = true;
```

### Setting a default identity namespace
<a name="r_ALTER_SYSTEM-identity"></a>

This example is specific to working with an identity provider. You can integrate Redshift with IAM Identity Center and an identity provider to centralize identity management for Redshift and other AWS services.

The following sample shows how to set the default identity namespace for the system. Doing this subsequently makes it more simple to run GRANT and CREATE statements, because you don't have to include the namespace as a prefix for each identity.

```
ALTER SYSTEM SET default_identity_namespace = 'MYCO';
```

After running the command, you can run statements like the following:

```
GRANT SELECT ON TABLE mytable TO alice;

GRANT UPDATE ON TABLE mytable TO salesrole;
               
CREATE USER bob password 'md50c983d1a624280812631c5389e60d48c';
```

The effect of setting the default identity namespace is that each identity doesn't require it as a prefix. In this example, `alice` is replaced with `MYCO:alice`. This happens with any identity included. For more information about using an identity provider with Redshift, see [Connect Redshift with IAM Identity Center to give users a single sign-on experience](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html).

For more information about settings that pertain to Redshift configuration with IAM Identity Center, see [SET](r_SET.md) and [ALTER IDENTITY PROVIDER](r_ALTER_IDENTITY_PROVIDER.md).