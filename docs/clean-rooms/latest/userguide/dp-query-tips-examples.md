# Differential Privacy query tips and examples

AWS Clean Rooms Differential Privacy uses a [general-purpose query structure](dp-sql-capabilities.md "dp-sql-capabilities.md") to support a wide
variety of SQL constructs such as Common Table Expressions (CTEs) for data preparation and
commonly used aggregate functions such as `COUNT`, or `SUM`. In order to
obfuscate the contribution of any possible user in your data by adding noise to aggregate
query results at run-time, AWS Clean Rooms Differential Privacy requires that aggregate functions in the
final `SELECT statement` are run on user-level data.

The following example uses two tables named `socialco_impressions` and
`socialco_users` from a media publisher who wants to protect data using
differential privacy while collaborating with an athletic brand with
`athletic_brand_sales` data. The media publisher has configured the
`user_id` column as the user identifier column while enabling differential
privacy in AWS Clean Rooms. The advertiser does not need differential privacy protection and wants to
run a query using CTEs on combined data. Since their CTE uses differential privacy protected
tables, the advertiser includes the user identifier column from those protected tables in the
list of CTE columns and joins the protected tables on the user identifier column.

```
WITH matches_table AS(
     SELECT **si.user\_id**, si.campaign_id, s.sale_id, s.sale_price
     FROM socialco_impressions si
     JOIN socialco_users su
         ON **su.user\_id = si.user\_id**
     JOIN athletic_brand_sales s
         ON s.emailsha256 = su.emailsha256
     WHERE s.timestamp > si.timestamp

UNION ALL

     SELECT **si.user\_id**, si.campaign_id, s.sale_id, s.sale_price
     FROM socialco_impressions si
     JOIN socialco_users su
         ON **su.user\_id = si.user\_id**
     JOIN athletic_brand_sales s
         ON s.phonesha256 = su.phonesha256
     WHERE s.timestamp > si.timestamp
)

SELECT COUNT (DISTINCT user_id) as unique_users
FROM matches_table
GROUP BY campaign_id
ORDER BY COUNT (DISTINCT user_id) DESC
LIMIT 5
```

Similarly, if you want to run window functions on differential privacy protected data
tables, you must include the user identifier column in the `PARTITION BY`
clause.

```
ROW_NUMBER() OVER (PARTITION BY conversion_id, **user\_id** ORDER BY match_type, match_age) AS row
```
