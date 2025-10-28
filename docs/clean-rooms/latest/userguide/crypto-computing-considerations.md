# Considerations when using Cryptographic Computing for Clean Rooms

Cryptographic Computing for Clean Rooms (C3R) seeks to maximize data protection. However, some use cases might
benefit from lower levels of data protection in exchange for additional functionality. You can
make these specific tradeoffs by modifying C3R from its most secure configuration. As
the customer, you should be aware of these tradeoffs and determine if they are appropriate for
your use case. Tradeoffs to consider include the following:

###### Topics

- [Allowing mixed cleartext and encrypted
  data in your tables](#allow-mixed-plaintext-and-encrypted-data "#allow-mixed-plaintext-and-encrypted-data")
- [Allowing repeated values in fingerprint
  columns](#allow-repeated-values "#allow-repeated-values")
- [Loosening restrictions on how
  fingerprint columns are named](#loose-restrictions-on-join-column-names "#loose-restrictions-on-join-column-names")
- [Determining how NULL values are
  represented](#determine-null-values "#determine-null-values")
  For more information about how to set parameters for these scenarios, see [Cryptographic computing parameters](crypto-computing-parameters.md "crypto-computing-parameters.md").

## Allowing mixed cleartext and encrypted

data in your tables

Having all data be client-side encrypted provides maximum data protection. However, this
limits certain kinds of queries (for example, the SUM aggregate function). The
risk of allowing cleartext data is that it's feasible that anyone with access to
the encrypted tables could infer some information about encrypted values. This could be done by
performing a statistical analysis on the cleartext and associated data.

For example, imagine you had the columns of `City` and `State`. The
`City` column is cleartext and the `State` column is
encrypted. When you see the value `Chicago` in the `City` column, that
helps you determine with high probability that the `State` is `Illinois`.
In contrast, if one column is `City` and the other column is
`EmailAddress`, a cleartext
`City` is unlikely to reveal anything about an encrypted `EmailAddress`.

For more information about the parameter for this scenario, see [Allow cleartext columns
parameter](crypto-computing-parameters.md#parameter-allowcleartext "crypto-computing-parameters.md#parameter-allowcleartext").

## Allowing repeated values in fingerprint

columns

For the most secure approach, we assume that any fingerprint column contains
exactly one instance of a variable. No item can be repeated in a fingerprint
column. The C3R encryption client maps these cleartext values into unique values that are
indistinguishable from random values. Therefore, it's impossible to infer information about the
cleartext from these random values.

The risk of repeated values in a fingerprint column is that repeated values
will result in repeated random-looking values. Thus, anyone who has access to the encrypted
tables could, in theory, perform a statistical analysis of the fingerprint columns
that might reveal information about cleartext values.

Again, suppose the fingerprint column is `State`, and every row of
the table corresponds to a US household. By doing a frequency analysis, one could infer which
state is `California` and which is `Wyoming` with high probability. This
inference is possible because `California` has many more residents than
`Wyoming`. In contrast, say the fingerprint column is on a household
identifier and each household appeared in the database between 1 and 4 times in a database of
millions of entries. It's unlikely that a frequency analysis would reveal any useful
information.

For more information about the parameter for this scenario, see [Allow duplicates parameter](crypto-computing-parameters.md#parameter-allowduplicates "crypto-computing-parameters.md#parameter-allowduplicates").

## Loosening restrictions on how

fingerprint columns are named

By default, we assume that when two tables are joined using encrypted
fingerprint columns, those columns have the same name in each table. The
technical reason for this result is that, by default, we derive a different cryptographic key for
encrypting each fingerprint column. That key is derived from a combination of the
shared secret key for the collaboration and the column name. If we try to join two columns with
different column names, we derive different keys and we can't compute a valid join.

To address this issue, you can turn off the feature that derives keys from each column name.
Then, the C3R encryption client uses a single derived key for all fingerprint columns.
The risk is that another kind of frequency analysis can be done that might reveal information.

Let’s use the `City` and `State` example again. If we derive the same
random values for each fingerprint column (by not incorporating the column name).
`New York` has the same random value in the `City` and `State`
columns. New York is one of a few cities in the US where the `City` name is the same
as the `State` name. In contrast, if your dataset has completely different values in
each column, no information is leaked.

For more information about the parameter for this scenario, see [Allow JOIN of columns with different
names parameter](crypto-computing-parameters.md#parameter-allowjoin "crypto-computing-parameters.md#parameter-allowjoin").

## Determining how NULL values are

represented

The option available to you is whether to process cryptographically (encrypt and HMAC)
NULL values like any other value. If you don't process NULL values
like any other value, information might be revealed.

For example, suppose that NULL in the `Middle Name` column in the
cleartext indicates people without middle names. If you don't encrypt those
values, you leak which rows in the encrypted table are used for people without middle names. That
information might be an identifying signal for some people in some populations. But if you do
cryptographically process NULL values, certain SQL queries act differently. For
example, GROUP BY clauses will not group fingerprint
NULL values in fingerprint columns together.

For more information about the parameter for this scenario, see [Preserve NULL values
parameter](crypto-computing-parameters.md#parameter-preservenulls "crypto-computing-parameters.md#parameter-preservenulls").
