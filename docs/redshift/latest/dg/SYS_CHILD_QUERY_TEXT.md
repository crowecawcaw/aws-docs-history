Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_CHILD_QUERY_TEXT

Returns the SQL text of a child query.

## Table columns

| Column name          | Data type      | Description                                                |
| -------------------- | -------------- | ---------------------------------------------------------- |
| user_id              | integer        | The identifier of the user who submitted the query.        |
| query_id             | bigint         | The user query ID                                          |
| child_query_sequence | integer        | The sequence of the rewritten user query, starting with 1. |
| sequence             | integer        | The sequence number for this query piece.                  |
| text                 | character(200) | The first 200 characters of the text of the SQL query.     |

## Sample

queries

In the following example, the rows in the result show actions taken by Amazon Redshift.

```
`SELECT * from sys_child_query_text where query_id = '34487366' order by child_query_sequence asc, sequence asc;`

`user_id | query_id | child_query_sequence | sequence | text
--------|----------|----------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
100 | 34899339 | 1 | 0 | /* RQEV2-aY6ZZ1ZpQK */\nwith venue as (\n select venueid,\n venuename,\n venuestate\n from venue\n), event as (\n select eventid,\n venueid,\n date
100 | 34899339 | 1 | 1 | id,\n eventname\n from event\n where eventname like '3 Doors Down'\n), users as (\n select userid\n from users\n), sales as (\n select salesid,\n pricepaid,
100 | 34899339 | 1 | 2 | \n eventid,\n buyerid\n from sales\n)\nselect e.eventname,\n v.venuename,\n count(distinct(u.userid)) as unique_customers,\n sum(s.pricepaid) as total_sal
100 | 34899339 | 1 | 3 | es\nfrom venue as v inner join event e on v.venueid = e.venueid\ninner join sales s on e.eventid = s.eventid inner join users u on s.buyerid = u.userid\ngroup by 1,2\norder by 4 desc limit 100`
```
