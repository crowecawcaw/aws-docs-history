# Update data in an Amazon Keyspaces

table using CQL

To update the data in your `book_awards` table, use the
`UPDATE` statement.

The general form of the `UPDATE` statement is as follows.

```
UPDATE `table_name` SET `column_name`=`new_value` WHERE `primary_key`=`value` ;
```

###### Tip

- You can update multiple columns by using a comma-separated list of
  `column_names` and values, as in the following example.

```
UPDATE my_table SET col1='new_value_1', col2='new_value2' WHERE col3='1' ;
```

- If the primary key is composed of multiple columns, all primary key columns
  and their values must be included in the `WHERE` clause.
- You cannot update any column in the primary key because that would change the primary
  key for the record.

###### To update a single cell

Using your `book_awards` table, change the name of a publisher the for winner of the non-fiction Wolf awards in 2020.

```
UPDATE book_awards SET publisher='new Books' WHERE year = 2020 AND award='Wolf' AND category='Non-Fiction' AND rank=1;
```

Verify that the publisher is now `new Books`.

```
SELECT * FROM book_awards WHERE year = 2020 AND award='Wolf' AND category='Non-Fiction' AND rank=1;
```

The statement should return the following output.

```
 `year | award | category | rank | author | book_title | publisher
------+-------+-------------+------+-------------+------------------+-----------
 2020 | Wolf | Non-Fiction | 1 | Wang Xiulan | History of Ideas | new Books`
```

## Try it

**Advanced:** The winner of the 2020 fiction "Kwezi Manu Prize" has changed their name. Update this record
to change the name to `'Akua Mansa-House'`.
