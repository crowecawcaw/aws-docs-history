Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE DATASHARE

Creates a new datashare in the current database. The owner of this datashare is the
issuer of the CREATE DATASHARE command.

Amazon Redshift associates each datashare with a single Amazon Redshift database. You can only add objects from the
associated database to a datashare. You can create multiple datashares on the same Amazon Redshift
database.

For information about datashares, see [Data sharing in Amazon Redshift](datashare-overview.md "datashare-overview.md").

To view information about the datashares, use [SHOW DATASHARES](r_SHOW_DATASHARES.md "r_SHOW_DATASHARES.md").

## Required privileges

Following are required privileges for CREATE DATASHARE:

- Superuser
- Users with the CREATE DATASHARE privilege
- Database owner

## Syntax

```
CREATE DATASHARE *datashare\_name*
[[SET] PUBLICACCESSIBLE [=] TRUE | FALSE ];
```

## Parameters

_datashare_name_

The name of the datashare. The datashare name must be unique in the cluster
namespace.

[[SET] PUBLICACCESSIBLE]

A clause that specifies whether the datashare can be shared to clusters that
are publicly accessible.

The default value for `SET PUBLICACCESSIBLE` is
`FALSE`.

## Usage notes

By default, the owner of the datashare only owns the share but not objects within the
share.

Only superusers and the database owner can use CREATE DATASHARE and delegate ALTER
privileges to other users or groups.

## Examples

The following example creates the datashare `salesshare`.

```
CREATE DATASHARE salesshare;
```

The following example creates the datashare `demoshare` that AWS Data Exchange
manages.

```
CREATE DATASHARE demoshare SET PUBLICACCESSIBLE TRUE, MANAGEDBY ADX;
```
