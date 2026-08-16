Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SYS\_CHILD\_QUERY\_TEXT

Returns the SQL text of a child query.

## Table columns

| Column name            | Data type      | Description                                                |
| ---------------------- | -------------- | ---------------------------------------------------------- |
| user\_id               | integer        | The identifier of the user who submitted the query.        |
| query\_id              | bigint         | The user query ID                                          |
| child\_query\_sequence | integer        | The sequence of the rewritten user query, starting with 1. |
| sequence               | integer        | The sequence number for this query piece.                  |
| text                   | character(200) | The first 200 characters of the text of the SQL query.     |
| query\_uuid            | character(36)  | A globally unique identifier (UUID) of the query.          |

## Sample queries

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
