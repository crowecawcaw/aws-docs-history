Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Verifying that the data loaded

correctly

After the load operation is complete, query the [STL_LOAD_COMMITS](r_STL_LOAD_COMMITS.md "r_STL_LOAD_COMMITS.md") system table to verify that the expected files
were loaded. Run the COPY command and load verification within the same transaction
so that if there is problem with the load you can roll back the entire
transaction.

The following query returns entries for loading the tables in the TICKIT
database:

```
`SELECT query, trim(filename) AS filename, curtime, status
FROM stl_load_commits
WHERE filename like '%tickit%' order by query;`
`query | filename | curtime | status
-------+---------------------------+----------------------------+--------
 22475 | tickit/allusers_pipe.txt | 2013-02-08 20:58:23.274186 | 1
 22478 | tickit/venue_pipe.txt | 2013-02-08 20:58:25.070604 | 1
 22480 | tickit/category_pipe.txt | 2013-02-08 20:58:27.333472 | 1
 22482 | tickit/date2008_pipe.txt | 2013-02-08 20:58:28.608305 | 1
 22485 | tickit/allevents_pipe.txt | 2013-02-08 20:58:29.99489 | 1
 22487 | tickit/listings_pipe.txt | 2013-02-08 20:58:37.632939 | 1
 22489 | tickit/sales_tab.txt | 2013-02-08 20:58:37.632939 | 1
(6 rows)`
```
