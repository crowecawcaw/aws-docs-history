# Use the `INSERT` statement to set custom Time to Live (TTL) values for new rows

###### Note

Before you can set custom TTL values for rows using the `INSERT` statement, you must first enable custom TTL on the
table. For more information, see [Update table with custom Time to Live (TTL)](TTL-how-to-enable-custom-alter.md "TTL-how-to-enable-custom-alter.md").

To overwrite a table's default TTL value by setting expiration dates for individual
rows, you can use the `INSERT` statement:

- `INSERT` – Insert a new row of data with a TTL value
  set.
  Setting TTL values for new rows using the `INSERT` statement takes precedence over the default TTL setting of the
  table.

The following CQL statement inserts a row of data into the table and changes the
default TTL setting to 259,200 seconds (which is equivalent to 3 days).

```
INSERT INTO `my_table` (userid, time, subject, body, user)
        VALUES (B79CB3BA-745E-5D9A-8903-4A02327A7E09, 96a29100-5e25-11ec-90d7-b5d91eceda0a, 'Message', 'Hello','205.212.123.123')
        USING TTL 259200;
```

To confirm the TTL settings for the inserted row, use the following statement.

```
SELECT TTL (subject) from `my_table`;
```
