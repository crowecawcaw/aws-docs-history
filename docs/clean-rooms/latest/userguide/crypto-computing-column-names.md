# Column names in Cryptographic Computing for Clean Rooms

By default, the names of columns are important in Cryptographic Computing for Clean Rooms.

If the value of the **Allow JOIN of columns with different
names** parameter is **false**, column names are used during the
encryption of fingerprint columns. For this reason, by default, collaborators must
coordinate in advance and use the same target column names for data that will use
JOIN statements in queries. By default, columns encrypted for JOIN
with different names don't successfully JOIN on any values.

If the value of the **Allow JOIN of columns with different
names** parameter is **true**, JOIN statements across
columns encrypted as fingerprint columns succeed. Encrypting data with this
parameter might allow some inference of the cleartext values. For example, if a row
has the same Hash-based Message Authentication Code (HMAC) value in both the `City`
column and `State` column, the value might be `New York`.

## Normalization of column header names

Column header names are normalized by the C3R encryption client. Any leading and trailing white
space is removed, and the column name is made lowercase for the transformed output.

Normalization is applied before all other computations, calculations, or other operations
which could possibly be impacted by column names. The emitted output file only contains the
normalized names.
