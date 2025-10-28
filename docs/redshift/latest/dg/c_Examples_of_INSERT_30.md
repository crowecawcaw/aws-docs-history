Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# INSERT examples

The CATEGORY table in the TICKIT database contains the following rows:

```
 catid | catgroup |  catname  |                  catdesc
-------+----------+-----------+--------------------------------------------
     1 | Sports   | MLB       | Major League Baseball
     2 | Sports   | NHL       | National Hockey League
     3 | Sports   | NFL       | National Football League
     4 | Sports   | NBA       | National Basketball Association
     5 | Sports   | MLS       | Major League Soccer
     6 | Shows    | Musicals  | Musical theatre
     7 | Shows    | Plays     | All non-musical theatre
     8 | Shows    | Opera     | All opera and light opera
     9 | Concerts | Pop       | All rock and pop music concerts
    10 | Concerts | Jazz      | All jazz singers and bands
    11 | Concerts | Classical | All symphony, concerto, and choir concerts
(11 rows)
```

Create a CATEGORY_STAGE table with a similar schema to the CATEGORY table but define
default values for the columns:

```
create table category_stage
(catid smallint default 0,
catgroup varchar(10) default 'General',
catname varchar(10) default 'General',
catdesc varchar(50) default 'General');
```

The following INSERT statement selects all of the rows from the CATEGORY table and
inserts them into the CATEGORY_STAGE table.

```
insert into category_stage
(select * from category);
```

The parentheses around the query are optional.

This command inserts a new row into the CATEGORY_STAGE table with a value specified
for each column in order:

```
insert into category_stage values
(12, 'Concerts', 'Comedy', 'All stand-up comedy performances');
```

You can also insert a new row that combines specific values and default values:

```
insert into category_stage values
(13, 'Concerts', 'Other', default);
```

Run the following query to return the inserted rows:

```
select * from category_stage
where catid in(12,13) order by 1;

 catid | catgroup | catname |             catdesc
-------+----------+---------+----------------------------------
    12 | Concerts | Comedy  | All stand-up comedy performances
    13 | Concerts | Other   | General
(2 rows)
```

The following examples show some multiple-row INSERT VALUES statements. The first
example inserts specific CATID values for two rows and default values for the other
columns in both rows.

```
insert into category_stage values
(14, default, default, default),
(15, default, default, default);

select * from category_stage where catid in(14,15) order by 1;
 catid | catgroup | catname | catdesc
-------+----------+---------+---------
    14 | General  | General | General
    15 | General  | General | General
(2 rows)
```

The next example inserts three rows with various combinations of specific and default
values:

```
insert into category_stage values
(default, default, default, default),
(20, default, 'Country', default),
(21, 'Concerts', 'Rock', default);

select * from category_stage where catid in(0,20,21) order by 1;
 catid | catgroup | catname | catdesc
-------+----------+---------+---------
     0 | General  | General | General
    20 | General  | Country | General
    21 | Concerts | Rock    | General
(3 rows)
```

The first set of VALUES in this example produces the same results as specifying
DEFAULT VALUES for a single-row INSERT statement.

The following examples show INSERT behavior when a table has an IDENTITY column.
First, create a new version of the CATEGORY table, then insert rows into it from
CATEGORY:

```
create table category_ident
(catid int identity not null,
catgroup varchar(10) default 'General',
catname varchar(10) default 'General',
catdesc varchar(50) default 'General');


insert into category_ident(catgroup,catname,catdesc)
select catgroup,catname,catdesc from category;

```

Note that you can't insert specific integer values into the CATID IDENTITY
column. IDENTITY column values are automatically generated.

The following example demonstrates that subqueries can't be used as expressions
in multiple-row INSERT VALUES statements:

```
insert into category(catid) values
((select max(catid)+1 from category)),
((select max(catid)+2 from category));

ERROR: can't use subqueries in multi-row VALUES
```

The following example shows an insert into a temporary table populated with data from
the `venue` table using the `WITH SELECT` clause. For more
information about the `venue` table, see [Sample database](c_sampledb.md "c_sampledb.md").

First, create the temporary table `#venuetemp`.

```
CREATE TABLE #venuetemp AS SELECT * FROM venue;
```

List the rows in the `#venuetemp` table.

```
`SELECT * FROM #venuetemp ORDER BY venueid;`
         `venueid | venuename | venuecity | venuestate| venueseats
--------+--------------------------+------------+-----------+------------
1 Toyota Park Bridgeview IL 0
2 Columbus Crew Stadium Columbus OH 0
3 RFK Stadium Washington DC 0
4 CommunityAmerica Ballpark Kansas City KS 0
5 Gillette Stadium Foxborough MA 68756
...`
```

Insert 10 duplicate rows in the `#venuetemp` table using the `WITH
 SELECT` clause.

```
INSERT INTO #venuetemp (WITH venuecopy AS (SELECT * FROM venue) SELECT * FROM venuecopy ORDER BY 1 LIMIT 10);
```

List the rows in the `#venuetemp` table.

```
`SELECT * FROM #venuetemp ORDER BY venueid;`
         `venueid | venuename | venuecity | venuestate| venueseats
--------+--------------------------+------------+-----------+------------
1 Toyota Park Bridgeview IL 0
1 Toyota Park Bridgeview IL 0
2 Columbus Crew Stadium Columbus OH 0
2 Columbus Crew Stadium Columbus OH 0
3 RFK Stadium Washington DC 0
3 RFK Stadium Washington DC 0
4 CommunityAmerica Ballpark Kansas City KS 0
4 CommunityAmerica Ballpark Kansas City KS 0
5 Gillette Stadium Foxborough MA 68756
5 Gillette Stadium Foxborough MA 68756
...`
```
