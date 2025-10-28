Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP DATASHARE

Drops a datashare. This command isn't reversible.

Only a superuser or the datashare owner can drop a datashare.

## Required privileges

Following are required privileges for DROP DATASHARE:

- Superuser
- Users with the DROP DATASHARE privilege
- Datashare owner

## Syntax

```
DROP DATASHARE *datashare\_name*;
```

## Parameters

_datashare_name_

The name of the datashare to be dropped.

## DROP DATASHARE usage notes

When using the DROP DATASHARE statement, consider the following:

- In general, we recommend that you don't drop an AWS Data Exchange datashare using
  the DROP DATASHARE statement. If you do, the AWS accounts that have access to
  the datashare lose access. Performing this type of alteration can breach data
  product terms in AWS Data Exchange.

The following example shows an error when an AWS Data Exchange datashare is dropped.

```
DROP DATASHARE salesshare;
ERROR:  Drop of ADX-managed datashare salesshare requires session variable datashare_break_glass_session_var to be set to value '620c871f890c49'
```

To allow dropping an AWS Data Exchange datashare, set the following variable and run the
DROP DATASHARE statement again.

```
SET datashare_break_glass_session_var to '620c871f890c49';
```

```
DROP DATASHARE salesshare;
```

In this case, Amazon Redshift generates a random one-time value to set the session
variable to allow DROP DATASHARE for an AWS Data Exchange datashare.

## Examples

The following example drops a datashare named `salesshare`.

```
DROP DATASHARE salesshare;
```
