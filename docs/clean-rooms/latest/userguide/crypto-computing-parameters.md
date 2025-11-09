# Cryptographic computing parameters

Cryptographic computing parameters are available for collaborations using Cryptographic Computing for Clean Rooms
(C3R) when [creating a collaboration](create-collaboration.md "create-collaboration.md"). You
can create a collaboration using either the AWS Clean Rooms console or the
`CreateCollaboration` API operation. In the console, you can set values for the
parameters in **Cryptographic computing parameters** after you turn on the
**Support cryptographic computing** option. For more information, see the
following topics.

###### Topics

- [Allow cleartext columns
  parameter](#parameter-allowcleartext "#parameter-allowcleartext")
- [Allow duplicates parameter](#parameter-allowduplicates "#parameter-allowduplicates")
- [Allow JOIN of columns with different
  names parameter](#parameter-allowjoin "#parameter-allowjoin")
- [Preserve NULL values
  parameter](#parameter-preservenulls "#parameter-preservenulls")

## Allow cleartext columns

parameter

In the console, you can set the **Allow cleartext
columns** parameter when [creating a
collaboration](create-collaboration.md "create-collaboration.md") to specify if cleartext data is allowed in a table with
encrypted data.

The following table describes the values for the **Allow cleartext
columns** parameter.

| Parameter value | Description                                                                                                                                                                                                                                                                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **No**          | Cleartext columns aren't allowed in the encrypted table. All data<br>is cryptographically protected.                                                                                                                                                                                                                                         |
| **Yes**         | Cleartext columns are allowed in the encrypted table.<br>Cleartext columns are not cryptographically protected and are<br>included as cleartext. You should take note of what your rows’<br>cleartext data might reveal about the other data in the<br>table.<br>To run SUM or AVG on specific columns, the columns<br>must be in cleartext. |

Using the `CreateCollaboration` API operation, for the
`dataEncryptionMetadata` parameter, you can set the value of
`allowCleartext` to `true` or `false`.
For
more information about API operations, see the [AWS Clean Rooms API
Reference](../apireference/Welcome.md "../apireference/Welcome.md").

Cleartext columns correspond to columns that are classified as
cleartext in the table-specific schema. Data in these columns is not
encrypted and can be used in any way. Cleartext columns can be useful if the
data is not sensitive and/or if more flexibility is needed than an encrypted
sealed column or fingerprint column allows.

## Allow duplicates parameter

In the console, you can set the **Allow duplicates** parameter when [creating a collaboration](create-collaboration.md "create-collaboration.md") to specify if columns
encrypted for JOIN queries can contain duplicate non-NULL
values.

###### Important

The **Allow duplicates**, [Allow JOIN of columns with different names](#parameter-allowjoin "#parameter-allowjoin"),
and [Preserve NULL
values](#parameter-preservenulls "#parameter-preservenulls") parameters have separate but related effects.

The following table describes the values for the **Allow duplicates**
parameter.

| Parameter value | Description                                                                                                                                                                                                                                                                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **No**          | Repeated values are not allowed in a fingerprint column. All<br>values in a single fingerprint column must be unique.                                                                                                                                                                                                                        |
| **Yes**         | Repeated values are allowed in a fingerprint column.<br>If you need to join columns with repeated values, set this value to<br>**Yes**. When set to **Yes**, frequency patterns<br>appearing within fingerprint columns in the C3R table or<br>results might imply some additional information about the structure of the<br>cleartext data. |

Using the `CreateCollaboration` API operation, for the
`dataEncryptionMetadata` parameter you can set the value of
`allowDuplicates` to `true` or `false`.
For
more information about API operations, see the [AWS Clean Rooms API Reference](../apireference/Welcome.md "../apireference/Welcome.md").

By default, if encrypted data must be used in JOIN queries, the
C3R encryption client requires that those columns have no duplicate values. This requirement is an
effort to increase data protection. This behavior can help ensure that repeated patterns in
the data are not observable. However, if you want to work with encrypted data in
JOIN queries and aren't concerned about duplicate values, the **Allow
duplicates** parameter can disable this conservative
check.

## Allow JOIN of columns with different

names parameter

In the console, you can set the **Allow JOIN of columns with
different names** parameter when [creating a
collaboration](create-collaboration.md "create-collaboration.md") to specify if JOIN statements between columns with
different names are
supported.

For more information, see [Normalization of column header names](crypto-computing-column-names.md#column-header-names-normalization "crypto-computing-column-names.md#column-header-names-normalization")

The following table describes the values for the **Allow JOIN of
columns with different names** parameter.

| Parameter value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **No**          | Joins of fingerprint columns with different names are not<br>supported. JOIN statements only provide accurate results on columns<br>that have the same name.<br>ImportantThe **No\*<br>• value provides increased information security but<br>requires collaboration participants to agree previously about column names. If two<br>columns have different names when encrypted as fingerprint columns<br>and **Allow JOIN of columns with different names**<br>is set to **No\*\*, JOIN statements on those columns<br>produce no results. This is because no values post-encryption are shared between<br>them.            |
| **Yes**         | Joins of fingerprint columns with different names are supported.<br>For additional flexibility, users can set this value to **Yes**,<br>which allows JOIN statements on columns regardless of their column<br>name.<br>If set to **Yes**, the C3R encryption client doesn't consider the<br>column name when protecting fingerprint columns. As a result, common<br>values across different fingerprint columns are observable in the<br>C3R table.<br>For example, if a row has the same encrypted JOIN value in both a<br>`City` column and a `State` column, it might be reasonable<br>to infer that value is `New York`. |

Using the `CreateCollaboration` API operation, for the
`dataEncryptionMetadata` parameter, you can set the value of
`allowJoinsOnColumnsWithDifferentNames` to `true` or
`false`. For more information about API operations, see the [AWS Clean Rooms API
Reference](../apireference/Welcome.md "../apireference/Welcome.md").

By default, fingerprint column encryption is affected by the
`targetHeader` for that column, set in [Step 4: Generate an encryption schema for a
tabular file](gen-encryption-schema-csv.md "gen-encryption-schema-csv.md") . Therefore, the same cleartext
value has different encrypted representations in each different fingerprint
column that it's encrypted for.

This parameter can be useful at preventing the inference of cleartext
values in some cases. For example, seeing the same encrypted value in
fingerprint columns `City` and `State` might be used to
reasonably infer the value is `New York`. However, this parameter's use requires
additional coordination in advance, so that all columns to be joined in queries have shared
names.

You can use the **Allow JOIN of columns with different
names** parameter to loosen this restriction. When the parameter value is set to
`Yes`, it allows any columns encrypted for JOIN to be used
together regardless of name.

## Preserve NULL values

parameter

In the console, you can set the **Preserve NULL values**
parameter when [creating a collaboration](create-collaboration.md "create-collaboration.md") to
indicate that there is no value present for that column.

The following table describes the values for the **Preserve NULL
values** parameter.

| Parameter value | Description                                                                                                                                                                                                                                                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **No**          | NULL values are not preserved. NULL values don't<br>appear as NULL in an encrypted table. NULL values<br>appear as unique random values in a C3R table.                                                                                                                                                                                                |
| **Yes**         | NULL values are preserved. NULL values appear as<br>NULL in an encrypted table. If you require SQL semantics of<br>NULL values, you can set this value to **Yes**. As a<br>result, NULL entries appear as NULL in the<br>C3R table, regardless of whether the column is encrypted and regardless of<br>the parameter setting for **Allow duplicates**. |

Using the `CreateCollaboration` API operation, for the
`dataEncryptionMetadata` parameter, you can set the value of
`preserveNulls` to `true` or `false`. For more information
about API operations, see the [AWS Clean Rooms API
Reference](../apireference/Welcome.md "../apireference/Welcome.md").

When the **Preserve NULL values** parameter is set to
**No** for the collaboration:

1. NULL entries in `cleartext` columns are unchanged.
2. NULL entries in encrypted `fingerprint` columns are
   encrypted as random values to conceal their contents. Joining on an encrypted column with
   NULL entries in
   the
   cleartextcolumn doesn't produce any matches for any of
   the NULL entries. No matches are made because they each receive their own,
   unique random content.
3. NULL entries in encrypted `sealed` columns are
   encrypted.

When the value of the **Preserve NULL values** parameter
is set to **Yes** for the collaboration, NULL entries from all
columns remain as NULL regardless of whether the column is encrypted.

The **Preserve NULL values** parameter is useful in
scenarios such as data enrichment, where you want to share a lack of information expressed as
NULL. The **Preserve NULL values** parameter
is also useful in fingerprint or HMAC format if you have NULL
values in the column you want to JOIN or GROUP BY.

If the value of the **Allow duplicates** and **Preserve
NULL values** parameters is set to **No**, having
more than one NULL entry in a fingerprint column produces an
error and stops encryption. If the value of either parameter is set to
**Yes**, no such error occurs.
