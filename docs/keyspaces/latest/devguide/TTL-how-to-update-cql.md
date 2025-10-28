# Use the `UPDATE` statement to edit custom Time to Live (TTL)

settings for rows and columns

###### Note

Before you can set custom TTL values for rows and columns, you must enable TTL on the
table first. For more information, see [Update table with custom Time to Live (TTL)](TTL-how-to-enable-custom-alter.md "TTL-how-to-enable-custom-alter.md").

You can use the `UPDATE` statement to overwrite a table's default TTL value by setting the expiration date for individual
rows and columns:

- Rows – You can update an existing row of data with a custom TTL value.
- Columns – You can update a subset of columns within existing rows with a custom TTL value.
  Setting TTL values for rows and columns takes precedence over the default TTL setting for the
  table.

To change the TTL settings of the 'subject' column inserted earlier from 259,200
seconds (3 days) to 86,400 seconds (one day), use the following statement.

```
UPDATE `my_table` USING TTL 86400 set subject = 'Updated Message' WHERE userid = B79CB3BA-745E-5D9A-8903-4A02327A7E09 and time = 96a29100-5e25-11ec-90d7-b5d91eceda0a;
```

You can run a simple select query to see the updated record before the expiration
time.

```
SELECT * from `my_table`;
```

The query shows the following output.

```
`userid | time | body | subject | user
--------------------------------------+--------------------------------------+-------+-----------------+-----------------
b79cb3ba-745e-5d9a-8903-4a02327a7e09 | 96a29100-5e25-11ec-90d7-b5d91eceda0a | Hello | Updated Message | 205.212.123.123
50554d6e-29bb-11e5-b345-feff819cdc9f | cf03fb21-59b5-11ec-b371-dff626ab9620 | Hello | Message | 205.212.123.123`
```

To confirm that the expiration was successful, run the same query again after the configured expiration time.

```
SELECT * from `my_table`;
```

The query shows the following output after the 'subject' column has expired.

```
`userid | time | body | subject | user
--------------------------------------+--------------------------------------+-------+---------+-----------------
b79cb3ba-745e-5d9a-8903-4a02327a7e09 | 96a29100-5e25-11ec-90d7-b5d91eceda0a | Hello | null | 205.212.123.123
50554d6e-29bb-11e5-b345-feff819cdc9f | cf03fb21-59b5-11ec-b371-dff626ab9620 | Hello | Message | 205.212.123.123`
```
