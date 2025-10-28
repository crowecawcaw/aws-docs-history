Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Tutorial: Using Amazon Q

generative SQL capability with the TICKIT data

To author efficient prompts to generate SQL, you must learn about your database schema
and your data. The TICKIT data consists of seven tables: two fact tables and five
dimensions. The sample data contains records about sales to attendants of entertainment
events that occurred in 2008. For more information about the TICKIT data schema, see
[Sample
database](../dg/c_sampledb.md "../dg/c_sampledb.md") in the _Amazon Redshift Database Developer Guide_. You can load the TICKIT
data into a database by various methods in both the Amazon Redshift console and the query editor v2. The
query editor v2 provides a method to load TICKIT data into database `sample_data_dev`.
For information, see [Loading data into a database](query-editor-v2-loading.md "query-editor-v2-loading.md"). The query editor v2 also provides
example prompts for the TICKIT data. The following scenario describes a conversation
with generative SQL to generate SQL about the TICKIT sample data. In this
scenario, the TICKIT sample data is already created in a `dev` database in an
Amazon Redshift cluster.

###### Note

This example is to illustrate a conversation.
The responses from generative SQL might not match your results using the same prompts.

###### Example conversation with Amazon Q generative SQL

1. In the **Editor**, connect to a cluster or workgroup that contains the TICKIT
   sample data.
2. Create an empty notebook and choose the
   ![Generative SQL](images/qev2-amazon-q.png)
   Generative SQL icon to open the chat panel.
3. Enter the following prompt to generate SQL to verify the number of records in
   the `VENUE` table:

```
How many venues are there?
```

```

SELECT
  COUNT(*) AS num_venues
FROM
  tickit.venue
```

Choose **Add to notebook** to add two cells to the open
notebook. One Markdown cell "How many venues are there?" and one containing the
generated SQL.

In the SQL cell, choose **Run** to receive the result:

```
`count
------
202`
```

4. To ask for another version of SQL, choose **Regenerate SQL**
   and receive the following answer:

```
`SELECT
 venuestate,
 COUNT(*) AS num_venues
FROM
 tickit.venue
GROUP BY
 venuestate`
```

Choose **Add to notebook** to add two more cells to the open
notebook. One Markdown cell "How many venues are there?" and one containing the
generated SQL.

In the SQL cell, choose **Run** to receive the result listing
venue state's by number:

```
`venuestate num_venues
----------------------
MA 4
OH 8
MI 5
...`
```

5. The generative SQL assistant can make assumptions about what you're asking.
   Although there are no widgets in the database, you can still ask. In this case,
   it gives you a message that it was not able to generate SQL.

```
How many widgets are there?
```

```

I was not able to generate any SQL
```

6. As you learn more about your database, you can ask more specific questions to
   generate SQL. For example, you're aware that the database contains sales data
   for several months in 2008. Enter the following prompt to generate SQL to find
   the number of sales in November 2008:

```
How many sales were there in November 2008?
```

```

SELECT
  COUNT(*) AS num_sales
FROM
  tickit.sales s
  JOIN tickit.date d ON s.dateid = d.dateid
WHERE
  d.month = 'November'
  AND d.year = 2008
```

Choose **Add to notebook** to add two cells to the open
notebook. One Markdown cell "How many sales were there in November 2008?" and
one containing the generated SQL.

In the SQL cell, choose **Run** to receive the result:

```
`num_sales
-----
0`
```

You realize this is not the result you were expecting. 7. You notice that the predicate `date.month='November'` expects the
month in the DATE table to be represented by an abbreviation of month name. You
change the predicate to `d.month='NOV'` and rerun the SQL.

```
`SELECT
 COUNT(*)
FROM
 sales
 JOIN date ON sales.dateid = date.dateid
WHERE
 date.month = 'NOV'
 AND date.year = 2008`
```

In the SQL cell, choose **Run** to get new results.

```
`count
-----
14261`
```

8. If you ask a question that tries to change the connected database, a warning
   message is returned along with any recommended SQL. Enter the following prompt
   to generate SQL to inset data into a table:

```
Insert 1 into the venue table.
```

```

INSERT
,
UPDATE
  OR delete data
FROM
  the database AS that could potentially change the data.Please provide a query that ONLY selects data
```

```


I was not able to generate the correct SQL code. I generated SQL, but you'll have to edit it to work with your database.
```

If you choose **Add to notebook** to add two cells to the
open notebook and run the SQL, then the SQL fails.

```
`ERROR: syntax error at or near "," Position: 132 [ErrorId: 1-6546764a-011df2691778846219ce6ec2]`
```

This scenario only illustrated some basic ways to interact with the Amazon Q generative
SQL. You can experiment even more with this generative AI technology to help you start
authoring SQL to query your database.
