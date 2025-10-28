Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Evaluating the query plan

You can use query plans to identify candidates for optimizing the distribution
style.

After making your initial design decisions, create your tables, load them with
data, and test them. Use a test dataset that is as close as possible to the real
data. Measure load times to use as a baseline for comparisons.

Evaluate queries that are representative of the most costly queries you expect to
run, specifically queries that use joins and aggregations. Compare runtimes for
various design options. When you compare runtimes, don't count the first time
the query is run, because the first runtime includes the compilation time.

**DS_DIST_NONE**

No redistribution is required, because corresponding slices are
collocated on the compute nodes. You typically have only one
DS_DIST_NONE step, the join between the fact table and one dimension
table.

**DS_DIST_ALL_NONE**

No redistribution is required, because the inner join table used
DISTSTYLE ALL. The entire table is located on every node.

**DS_DIST_INNER**

The inner table is redistributed.

**DS_DIST_OUTER**

The outer table is redistributed.

**DS_BCAST_INNER**

A copy of the entire inner table is broadcast to all the compute
nodes.

**DS_DIST_ALL_INNER**

The entire inner table is redistributed to a single slice because the
outer table uses DISTSTYLE ALL.

**DS_DIST_BOTH**

Both tables are redistributed.

**DS_DIST_ERR**

When the table doesn't have a distribution style selected.

DS_DIST_NONE and DS_DIST_ALL_NONE are good. They indicate that no distribution was
required for that step because all of the joins are collocated.

DS_DIST_INNER means that the step probably has a relatively high cost because the
inner table is being redistributed to the nodes. DS_DIST_INNER indicates that the
outer table is already properly distributed on the join key. Set the inner
table's distribution key to the join key to convert this to DS_DIST_NONE. In
some cases, distributing the inner table on the join key isn't possible because
the outer table isn't distributed on the join key. If this is the case,
evaluate whether to use ALL distribution for the inner table. If the table isn't
updated frequently or extensively, and it's large enough to carry a high
redistribution cost, change the distribution style to ALL and test again. ALL
distribution causes increased load times, so when you retest, include the load time
in your evaluation factors.

DS_DIST_ALL_INNER is not good. It means that the entire inner table is
redistributed to a single slice because the outer table uses DISTSTYLE ALL, so that
a copy of the entire outer table is located on each node. This results in
inefficient serial runtime of the join on a single node, instead taking advantage of
parallel runtime using all of the nodes. DISTSTYLE ALL is meant to be used only for
the inner join table. Instead, specify a distribution key or use even distribution
for the outer table.

DS_BCAST_INNER and DS_DIST_BOTH are not good. Usually these redistributions occur
because the tables are not joined on their distribution keys. If the fact table does
not already have a distribution key, specify the joining column as the distribution
key for both tables. If the fact table already has a distribution key on another
column, evaluate whether changing the distribution key to collocate this join
improve overall performance. If changing the distribution key of the outer table
isn't an optimal choice, you can achieve collocation by specifying DISTSTYLE
ALL for the inner table.

The following example shows a portion of a query plan with DS_BCAST_INNER and
DS_DIST_NONE labels.

```
->  XN Hash Join DS_BCAST_INNER  (cost=112.50..3272334142.59 rows=170771 width=84)
        Hash Cond: ("outer".venueid = "inner".venueid)
        ->  XN Hash Join DS_BCAST_INNER  (cost=109.98..3167290276.71 rows=172456 width=47)
              Hash Cond: ("outer".eventid = "inner".eventid)
              ->  XN Merge Join DS_DIST_NONE  (cost=0.00..6286.47 rows=172456 width=30)
                    Merge Cond: ("outer".listid = "inner".listid)
                    ->  XN Seq Scan on listing  (cost=0.00..1924.97 rows=192497 width=14)
                    ->  XN Seq Scan on sales  (cost=0.00..1724.56 rows=172456 width=24)
```

After changing the dimension tables to use DISTSTYLE ALL, the query plan for the
same query shows DS_DIST_ALL_NONE in place of DS_BCAST_INNER. Also, there is a
dramatic change in the relative cost for the join steps. The total cost is `14142.59` compared to `3272334142.59` in the previous query.

```
->  XN Hash Join DS_DIST_ALL_NONE  (cost=112.50..14142.59 rows=170771 width=84)
        Hash Cond: ("outer".venueid = "inner".venueid)
        ->  XN Hash Join DS_DIST_ALL_NONE  (cost=109.98..10276.71 rows=172456 width=47)
              Hash Cond: ("outer".eventid = "inner".eventid)
              ->  XN Merge Join DS_DIST_NONE  (cost=0.00..6286.47 rows=172456 width=30)
                    Merge Cond: ("outer".listid = "inner".listid)
                    ->  XN Seq Scan on listing  (cost=0.00..1924.97 rows=192497 width=14)
                    ->  XN Seq Scan on sales  (cost=0.00..1724.56 rows=172456 width=24)
```
