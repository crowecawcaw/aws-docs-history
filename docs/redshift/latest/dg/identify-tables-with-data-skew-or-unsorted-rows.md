Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Identifying tables with data skew

or unsorted rows

The following query identifies tables that have uneven data distribution (data
skew) or a high percentage of unsorted rows.

A low `skew` value indicates that table data is properly distributed.
If a table has a `skew` value of 4.00 or higher, consider modifying its
data distribution style. For more information, see [Suboptimal data distribution](query-performance-improvement-opportunities.md#suboptimal-data-distribution "query-performance-improvement-opportunities.md#suboptimal-data-distribution").

If a table has a `pct_unsorted` value greater than 20 percent, consider
running the [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md")
command. For more information, see [Unsorted or missorted rows](query-performance-improvement-opportunities.md#unsorted-or-mis-sorted-rows "query-performance-improvement-opportunities.md#unsorted-or-mis-sorted-rows").

Also review the `mbytes` and `pct_of_total` values for each
table. These columns identify the size of the table and what percentage of raw disk
space the table consumes. The raw disk space includes space that is reserved by
Amazon Redshift for internal use, so it is larger than the nominal disk capacity, which is
the amount of disk space available to the user. Use this information to verify
that you have free disk space equal to at least 2.5 times the size of your largest
table. Having this space available enables the system to write intermediate results
to disk when processing complex queries.

```
select trim(pgn.nspname) as schema,
trim(a.name) as table, id as tableid,
decode(pgc.reldiststyle,0, 'even',1,det.distkey ,8,'all') as distkey, dist_ratio.ratio::decimal(10,4) as skew,
det.head_sort as "sortkey",
det.n_sortkeys as "#sks", b.mbytes,
decode(b.mbytes,0,0,((b.mbytes/part.total::decimal)*100)::decimal(5,2)) as pct_of_total,
decode(det.max_enc,0,'n','y') as enc, a.rows,
decode( det.n_sortkeys, 0, null, a.unsorted_rows ) as unsorted_rows ,
decode( det.n_sortkeys, 0, null, decode( a.rows,0,0, (a.unsorted_rows::decimal(32)/a.rows)*100) )::decimal(5,2) as pct_unsorted
from (select db_id, id, name, sum(rows) as rows,
sum(rows)-sum(sorted_rows) as unsorted_rows
from stv_tbl_perm a
group by db_id, id, name) as a
join pg_class as pgc on pgc.oid = a.id
join pg_namespace as pgn on pgn.oid = pgc.relnamespace
left outer join (select tbl, count(*) as mbytes
from stv_blocklist group by tbl) b on a.id=b.tbl
inner join (select attrelid,
min(case attisdistkey when 't' then attname else null end) as "distkey",
min(case attsortkeyord when 1 then attname  else null end ) as head_sort ,
max(attsortkeyord) as n_sortkeys,
max(attencodingtype) as max_enc
from pg_attribute group by 1) as det
on det.attrelid = a.id
inner join ( select tbl, max(mbytes)::decimal(32)/min(mbytes) as ratio
from (select tbl, trim(name) as name, slice, count(*) as mbytes
from svv_diskusage group by tbl, name, slice )
group by tbl, name ) as dist_ratio on a.id = dist_ratio.tbl
join ( select sum(capacity) as  total
from stv_partitions where part_begin=0 ) as part on 1=1
where mbytes is not null
order by  mbytes desc;
```
