Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# query_group

## Values (default in bold)

No default; the value can be any character string.

## Description

Applies a user-defined label to a group of queries that are run during the same
session. This label is captured in the query logs. You can use it to constrain results
from the STL_QUERY and STV_INFLIGHT tables and the SVL_QLOG view. For example, you can
apply a separate label to every query that you run to uniquely identify queries without
having to look up their IDs.

This parameter doesn't exist in the server configuration file and must be set at
runtime with a SET command. Although you can use a long character string as a label, the
label is truncated to 30 characters in the LABEL column of the STL_QUERY table and the
SVL_QLOG view (and to 15 characters in STV_INFLIGHT).

In the following example, query_group is set to `Monday`, then
several queries are run with that label.

```
set query_group to 'Monday';
SET
select * from category limit 1;
...
...
select query, pid, substring, elapsed, label
from svl_qlog where label ='Monday'
order by query;

query | pid  |        substring                   |  elapsed  | label
------+------+------------------------------------+-----------+--------
789   | 6084 | select * from category limit 1;    | 65468     | Monday
790   | 6084 | select query, trim(label) from ... | 1260327   | Monday
791   | 6084 | select * from svl_qlog where ..    | 2293547   | Monday
792   | 6084 | select count(*) from bigsales;     | 108235617 | Monday
...
```
