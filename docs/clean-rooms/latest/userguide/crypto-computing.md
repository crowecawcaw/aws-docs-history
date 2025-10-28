# Cryptographic Computing for Clean Rooms

Cryptographic Computing for Clean Rooms (C3R) is a capability in AWS Clean Rooms that can be used in addition to
[analysis rules](analysis-rules.md "analysis-rules.md"). With C3R, organizations can
bring sensitive data together to derive new insights from data analytics while cryptographically
limiting what can be learned by any party in the process. C3R can be used by two or
more parties that want to collaborate with their sensitive data but are required to only use
encrypted data in the cloud.

The C3R encryption client is a client-side encryption tool that you can use to [encrypt](glossary.md#glossary-encryption "glossary.md#glossary-encryption") your data for
use with AWS Clean Rooms. When you use the C3R encryption client, data remains cryptographically protected
while in use in an AWS Clean Rooms collaboration. As with a regular AWS Clean Rooms collaboration, the input
data is relational database tables, and the computation is expressed as a SQL query. However,
C3R only supports a limited subset of SQL queries on encrypted data.

Specifically, C3R supports SQL JOIN and SELECT
statements on cryptographically protected data. Each column in the input table can be used in
exactly one of the following SQL statement types:

- Columns that are cryptographically protected for use in JOIN statements
  are called **fingerprint columns**.
- Columns that are cryptographically protected for use in SELECT statements
  are called **sealed columns**.
- Columns that are not cryptographically protected for use in JOIN or
  SELECT statements are called **cleartext
  columns**.
  In some cases, GROUP BY statements are supported on
  fingerprint columns. For more information, see [Fingerprint columns](crypto-computing-column-types.md#fingerprint-columns "crypto-computing-column-types.md#fingerprint-columns"). Currently,
  C3R doesn't support the use of other SQL constructs on encrypted data, such as
  WHERE clauses or aggregate functions like SUM and
  AVERAGE, even if they would otherwise be allowed by the relevant analysis
  rules.

C3R is designed to protect data in individual cells of a table. Using the
default configuration for C3R, the underlying data that a customer makes available
to third parties through a collaboration remains encrypted while the content is in use within
AWS Clean Rooms. C3R uses industry standard AES-GCM encryption for all
sealed columns and an industry standard pseudorandom function, known as a
Hash-based Message Authentication Code (HMAC), for protecting fingerprint
columns.

Although C3R encrypts the data in your tables, the following information might
still be able to be inferred:

- Information about the tables themselves, including the number of columns, column names,
  and the number of rows in your table.
- As with most standard forms of encryption, C3R doesn't try to hide the
  length of encrypted values. C3R does offer the ability to pad encrypted values
  to hide the exact length of cleartexts. However, an upper bound on the length of the
  cleartexts in each column could still be revealed to another party.
- Logging-level information, such as when a particular row was added to an encrypted
  C3R table.
  For more information about C3R, see the following topics.

###### Topics

- [Considerations when using Cryptographic Computing for Clean Rooms](crypto-computing-considerations.md "crypto-computing-considerations.md")
- [Supported file and data types in Cryptographic Computing for Clean Rooms](crypto-computing-file-types.md "crypto-computing-file-types.md")
- [Column names in Cryptographic Computing for Clean Rooms](crypto-computing-column-names.md "crypto-computing-column-names.md")
- [Column types in Cryptographic Computing for Clean Rooms](crypto-computing-column-types.md "crypto-computing-column-types.md")
- [Cryptographic computing parameters](crypto-computing-parameters.md "crypto-computing-parameters.md")
- [Optional flags in Cryptographic Computing for Clean Rooms](crypto-computing-optional-flags.md "crypto-computing-optional-flags.md")
- [Queries with Cryptographic Computing for Clean Rooms](crypto-computing-queries.md "crypto-computing-queries.md")
- [Guidelines for the C3R encryption client](crypto-computing-guidelines.md "crypto-computing-guidelines.md")
