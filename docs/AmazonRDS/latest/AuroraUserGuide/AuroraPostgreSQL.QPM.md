# Supporting table partition

Aurora PostgreSQL Query Plan Management (QPM) supports declarative table partitioning in the following versions:

- 15.3 and higher 15 versions
- 14.8 and higher 14 versions
- 13.11 and higher 13 versions
  For more information, see [Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html "https://www.postgresql.org/docs/current/ddl-partitioning.html").

###### Topics

- [Setting up table partition](#AuroraPostgreSQL.QPM.Partitiontable.setup "#AuroraPostgreSQL.QPM.Partitiontable.setup")
- [Capturing plans for table partition](#AuroraPostgreSQL.QPM.Partitiontable.capture "#AuroraPostgreSQL.QPM.Partitiontable.capture")
- [Enforcing a table partition plan](#AuroraPostgreSQL.QPM.Partitiontable.enforcement "#AuroraPostgreSQL.QPM.Partitiontable.enforcement")
- [Naming Convention](#AuroraPostgreSQL.QPM.Partitiontable.naming.convention "#AuroraPostgreSQL.QPM.Partitiontable.naming.convention")

## Setting up table partition

To set up table partition in Aurora PostgreSQL QPM, do as follows:

1. Set `apg_plan_mgmt.plan_hash_version` to 3 or more in the DB cluster parameter group.
2. Navigate to a database that uses Query Plan Management and has entries in `apg_plan_mgmt.dba_plans` view.
3. Call `apg_plan_mgmt.validate_plans('update_plan_hash')` to update the `plan_hash` value in the plans table.
4. Repeat steps 2-3 for all databases with Query Plan Management enabled that have entries in `apg_plan_mgmt.dba_plans` view.

For more information on these parameters, see [Parameter reference for
Aurora PostgreSQL query plan management](AuroraPostgreSQL.Optimize.md "AuroraPostgreSQL.Optimize.md").

## Capturing plans for table partition

In QPM, different plans are distinguished by their `plan_hash` value. To understand how the `plan_hash` changes, you must first understand
similar kind of plans.

The combination of access methods, digit-stripped index names and digit-stripped partition names, accumulated at the Append node
level must be constant for plans to be considered the same. The specific partitions accessed in the plans are not significant.
In the following example, a table `tbl_a` is created with 4 partitions.

```
`postgres=>`create table tbl_a(i int, j int, k int, l int, m int) partition by range(i);
`CREATE TABLE`
`postgres=>`create table tbl_a1 partition of tbl_a for values from (0) to (1000);
`CREATE TABLE`
`postgres=>`create table tbl_a2 partition of tbl_a for values from (1001) to (2000);
`CREATE TABLE`
`postgres=>`create table tbl_a3 partition of tbl_a for values from (2001) to (3000);
`CREATE TABLE`
`postgres=>`create table tbl_a4 partition of tbl_a for values from (3001) to (4000);
`CREATE TABLE`
`postgres=>`create index t_i on tbl_a using btree (i);
`CREATE INDEX`
`postgres=>`create index t_j on tbl_a using btree (j);
`CREATE INDEX`
`postgres=>`create index t_k on tbl_a using btree (k);
`CREATE INDEX`
```

The following plans are considered the same because a single scan method is being used to scan `tbl_a` irrespective
of the number of partitions that the query looks up.

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 999 and j < 9910 and k > 50;
            `QUERY PLAN
-------------------------------------------------------------------
Seq Scan on tbl_a1 tbl_a
 Filter: ((i >= 990) AND (i <= 999) AND (j < 9910) AND (k > 50))
SQL Hash: 1553185667, Plan Hash: -694232056
(3 rows)`
```

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 1100 and j < 9910 and k > 50;
            `QUERY PLAN
-------------------------------------------------------------------
Append
 -> Seq Scan on tbl_a1 tbl_a_1
 Filter: ((i >= 990) AND (i <= 1100) AND (j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 1100) AND (j < 9910) AND (k > 50))
 SQL Hash: 1553185667, Plan Hash: -694232056
 (6 rows)`
```

```
`postgres=>explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 2100 and j < 9910 and k > 50;`
            `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Seq Scan on tbl_a1 tbl_a_1
 Filter: ((i >= 990) AND (i <= 2100) AND (j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 2100) AND (j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a3 tbl_a_3
 Filter: ((i >= 990) AND (i <= 2100) AND (j < 9910) AND (k > 50))
 SQL Hash: 1553185667, Plan Hash: -694232056
(8 rows)`
```

The following 3 plans are also considered the same because at the parent level, the access methods, digit-stripped index names and digit-stripped partition names are `SeqScan tbl_a`, `IndexScan (i_idx) tbl_a`.

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 1100 and j < 9910 and k > 50;
            `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Seq Scan on tbl_a1 tbl_a_1
 Filter: ((i >= 990) AND (i <= 1100) AND (j < 9910) AND (k > 50))
 -> Index Scan using tbl_a2_i_idx on tbl_a2 tbl_a_2
 Index Cond: ((i >= 990) AND (i <= 1100))
 Filter: ((j < 9910) AND (k > 50))
 SQL Hash: 1553185667, Plan Hash: -993736942
(7 rows)`
```

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 2100 and j < 9910 and k > 50;
            `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Index Scan using tbl_a1_i_idx on tbl_a1 tbl_a_1
 Index Cond: ((i >= 990) AND (i <= 2100))
 Filter: ((j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 2100) AND (j < 9910) AND (k > 50))
 -> Index Scan using tbl_a3_i_idx on tbl_a3 tbl_a_3
 Index Cond: ((i >= 990) AND (i <= 2100))
 Filter: ((j < 9910) AND (k > 50))
 SQL Hash: 1553185667, Plan Hash: -993736942
(10 rows)`
```

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 3100 and j < 9910 and k > 50;
            `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Seq Scan on tbl_a1 tbl_a_1
 Filter: ((i >= 990) AND (i <= 3100) AND (j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 3100) AND (j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a3 tbl_a_3
 Filter: ((i >= 990) AND (i <= 3100) AND (j < 9910) AND (k > 50))
 -> Index Scan using tbl_a4_i_idx on tbl_a4 tbl_a_4
 Index Cond: ((i >= 990) AND (i <= 3100))
 Filter: ((j < 9910) AND (k > 50))
 SQL Hash: 1553185667, Plan Hash: -993736942
(11 rows)`
```

Irrespective of different order and number of occurrences in child partitions, the access methods, digit-stripped index names and digit-stripped partition names are constant at the parent level for each of the above plans.

However, the plans would be considered different if any of the following conditions are met:

- Any additional access methods are used in the plan.

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 2100 and j < 9910 and k > 50;
                    `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Seq Scan on tbl_a1 tbl_a_1
 Filter: ((i >= 990) AND (i <= 2100) AND (j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 2100) AND (j < 9910) AND (k > 50))
 -> Bitmap Heap Scan on tbl\_a3 tbl\_a\_3
 Recheck Cond: ((i >= 990) AND (i <= 2100))
 Filter: ((j < 9910) AND (k > 50))
 -> Bitmap Index Scan on tbl\_a3\_i\_idx
 Index Cond: ((i >= 990) AND (i <= 2100))
 SQL Hash: 1553185667, Plan Hash: 1134525070
(11 rows)`
```

- Any of the access methods in the plan are not used anymore.

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 1100 and j < 9910 and k > 50;
                    `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Seq Scan on tbl_a1 tbl_a_1
 Filter: ((i >= 990) AND (i <= 1100) AND (j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 1100) AND (j < 9910) AND (k > 50))
 SQL Hash: 1553185667, Plan Hash: -694232056
(6 rows)`
```

- The index associated with an index method is changed.

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 1100 and j < 9910 and k > 50;
                    `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Seq Scan on tbl_a1 tbl_a_1
 Filter: ((i >= 990) AND (i <= 1100) AND (j < 9910) AND (k > 50))
 -> Index Scan using tbl\_a2\_j\_idx on tbl_a2 tbl_a_2
 Index Cond: (j < 9910)
 Filter: ((i >= 990) AND (i <= 1100) AND (k > 50))
 SQL Hash: 1553185667, Plan Hash: -993343726
(7 rows)`
```

## Enforcing a table partition plan

Approved plans for partitioned tables are enforced with positional correspondence. The plans are not specific to the partitions, and can be enforced
on partitions other than the plans referenced in the original query. Plans also have the capability of being enforced for queries accessing a different
number of partitions than the original approved outline.

For example, if the approved outline is for the following plan:

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 2100 and j < 9910 and k > 50;
            `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Index Scan using tbl_a1_i_idx on tbl_a1 tbl_a_1
 Index Cond: ((i >= 990) AND (i <= 2100))
 Filter: ((j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 2100) AND (j < 9910) AND (k > 50))
 -> Index Scan using tbl_a3_i_idx on tbl_a3 tbl_a_3
 Index Cond: ((i >= 990) AND (i <= 2100))
 Filter: ((j < 9910) AND (k > 50))
 SQL Hash: 1553185667, Plan Hash: -993736942
(10 rows)`
```

Then, this plan can be enforced on SQL queries referencing 2, 4, or more partitions as well. The possible plans that could arise from these scenarios for 2 and 4 partition access are:

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 1100 and j < 9910 and k > 50;
            `QUERY PLAN
----------------------------------------------------------------------------------
 Append
 -> Index Scan using tbl_a1_i_idx on tbl_a1 tbl_a_1
 Index Cond: ((i >= 990) AND (i <= 1100))
 Filter: ((j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 1100) AND (j < 9910) AND (k > 50))
 Note: An Approved plan was used instead of the minimum cost plan.
 SQL Hash: 1553185667, Plan Hash: -993736942, Minimum Cost Plan Hash: -1873216041
(8 rows)`
```

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 3100 and j < 9910 and k > 50;
            `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Index Scan using tbl_a1_i_idx on tbl_a1 tbl_a_1
 Index Cond: ((i >= 990) AND (i <= 3100))
 Filter: ((j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 3100) AND (j < 9910) AND (k > 50))
 -> Index Scan using tbl_a3_i_idx on tbl_a3 tbl_a_3
 Index Cond: ((i >= 990) AND (i <= 3100))
 Filter: ((j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a4 tbl_a_4
 Filter: ((i >= 990) AND (i <= 3100) AND (j < 9910) AND (k > 50))
 Note: An Approved plan was used instead of the minimum cost plan.
 SQL Hash: 1553185667, Plan Hash: -993736942, Minimum Cost Plan Hash: -1873216041
(12 rows)`
```

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 3100 and j < 9910 and k > 50;
            `QUERY PLAN
----------------------------------------------------------------------------------
 Append
 -> Index Scan using tbl_a1_i_idx on tbl_a1 tbl_a_1
 Index Cond: ((i >= 990) AND (i <= 3100))
 Filter: ((j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 3100) AND (j < 9910) AND (k > 50))
 -> Index Scan using tbl_a3_i_idx on tbl_a3 tbl_a_3
 Index Cond: ((i >= 990) AND (i <= 3100))
 Filter: ((j < 9910) AND (k > 50))
 -> Index Scan using tbl_a4_i_idx on tbl_a4 tbl_a_4
 Index Cond: ((i >= 990) AND (i <= 3100))
 Filter: ((j < 9910) AND (k > 50))
 Note: An Approved plan was used instead of the minimum cost plan.
 SQL Hash: 1553185667, Plan Hash: -993736942, Minimum Cost Plan Hash: -1873216041
(14 rows)`
```

Consider another approved plan with different access methods for each partition:

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 2100 and j < 9910 and k > 50;
            `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Index Scan using tbl_a1_i_idx on tbl_a1 tbl_a_1
 Index Cond: ((i >= 990) AND (i <= 2100))
 Filter: ((j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 2100) AND (j < 9910) AND (k > 50))
 -> Bitmap Heap Scan on tbl_a3 tbl_a_3
 Recheck Cond: ((i >= 990) AND (i <= 2100))
 Filter: ((j < 9910) AND (k > 50))
 -> Bitmap Index Scan on tbl_a3_i_idx
 Index Cond: ((i >= 990) AND (i <= 2100))
 SQL Hash: 1553185667, Plan Hash: 2032136998
(12 rows)`
```

In this case, any plan that reads from two partitions would fail to be enforced. Unless all of the (access method, index name) combinations from the
approved plan are usable, the plan cannot be enforced. For example, the following plans have different plan hashes and the approved plan can't be
enforced in these cases:

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 1900 and j < 9910 and k > 50;
            `QUERY PLAN
-------------------------------------------------------------------------
 Append
 -> Bitmap Heap Scan on tbl_a1 tbl_a_1
 Recheck Cond: ((i >= 990) AND (i <= 1900))
 Filter: ((j < 9910) AND (k > 50))
 -> Bitmap Index Scan on tbl_a1_i_idx
 Index Cond: ((i >= 990) AND (i <= 1900))
 -> Bitmap Heap Scan on tbl_a2 tbl_a_2
 Recheck Cond: ((i >= 990) AND (i <= 1900))
 Filter: ((j < 9910) AND (k > 50))
 -> Bitmap Index Scan on tbl_a2_i_idx
 Index Cond: ((i >= 990) AND (i <= 1900))
 Note: This is not an Approved plan. No usable Approved plan was found.
 SQL Hash: 1553185667, Plan Hash: -568647260
(13 rows)`
```

```
`postgres=>`explain (hashes true, costs false) select j, k from tbl_a where i between 990 and 1900 and j < 9910 and k > 50;
            `QUERY PLAN
--------------------------------------------------------------------------
 Append
 -> Index Scan using tbl_a1_i_idx on tbl_a1 tbl_a_1
 Index Cond: ((i >= 990) AND (i <= 1900))
 Filter: ((j < 9910) AND (k > 50))
 -> Seq Scan on tbl_a2 tbl_a_2
 Filter: ((i >= 990) AND (i <= 1900) AND (j < 9910) AND (k > 50))
 Note: This is not an Approved plan. No usable Approved plan was found.
 SQL Hash: 1553185667, Plan Hash: -496793743
(8 rows)`
```

##

Naming Convention

For QPM to enforce a plan with declarative partitioned tables, you must follow specific naming rules for parent tables, table partitions, and indexes:

- Parent table names – These names must differ by alphabets or special characters, and not by just digits. For example, tA, tB, and tC are acceptable
  names for separate parent tables while t1, t2, and t3 are not.
- Individual partition table names – Partitions of the same parent should differ from one another by digits only. For example, acceptable partition names
  of tA could be tA1, tA2 or t1A, t2A or even multiple digits.

Any other differences (letters, special characters) will not guarantee plan enforcement.

- Index names – In partition table hierarchy, make sure that all indexes have unique names. This means that the non-numeric parts of the names must be different.
  For example, if you have a partitioned table named `tA` with an index named `tA_col1_idx1`, you can't have another index named `tA_col1_idx2`. However, you can have an index called `tA_a_col1_idx2` because the
  non-numeric part of the name is unique. This rule applies to indexes created on both the parent table and individual partition tables.

Failure to adhere to the above naming conventions may result in failure of approved plans enforcement. The following example illustrates such a failed enforcement:

```
`postgres=>`create table t1(i int, j int, k int, l int, m int) partition by range(i);
`CREATE TABLE`
`postgres=>`create table t1a partition of t1 for values from (0) to (1000);
`CREATE TABLE`
`postgres=>`create table t1b partition of t1 for values from (1001) to (2000);
`CREATE TABLE`
`postgres=>`SET apg_plan_mgmt.capture_plan_baselines TO 'manual';
`SET`
`postgres=>`explain (hashes true, costs false) select count(*) from t1 where i > 0;
`QUERY PLAN
--------------------------------------------------------------------------
 Aggregate
 -> Append
 -> Seq Scan on t1a t1_1
 Filter: (i > 0)
 -> Seq Scan on t1b t1_2
 Filter: (i > 0)
 SQL Hash: -1720232281, Plan Hash: -1010664377
(7 rows)`
```

```
`postgres=>`SET apg_plan_mgmt.use_plan_baselines TO 'on';
`SET`
`postgres=>`explain (hashes true, costs false) select count(*) from t1 where i > 1000;
`QUERY PLAN
-------------------------------------------------------------------------
 Aggregate
 -> Seq Scan on t1b t1
 Filter: (i > 1000)
 Note: This is not an Approved plan. No usable Approved plan was found.
 SQL Hash: -1720232281, Plan Hash: 335531806
(5 rows)`
```

Even though the two plans might appear identical, their `Plan Hash` values are different due to the names of the
child tables. The table names vary by alpha characters instead of just digits leading to an enforcement failure.
