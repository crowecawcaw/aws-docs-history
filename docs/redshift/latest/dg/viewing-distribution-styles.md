Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing distribution styles

To view the distribution style of a table, query the PG_CLASS_INFO view or the
SVV_TABLE_INFO view.

The RELEFFECTIVEDISTSTYLE column in PG_CLASS_INFO indicates the current
distribution style for the table. If the table uses automatic distribution,
RELEFFECTIVEDISTSTYLE is 10, 11, or 12, which indicates whether the effective
distribution style is AUTO (ALL), AUTO (EVEN), or AUTO (KEY). If the table uses
automatic distribution, the distribution style might initially show AUTO (ALL), then
change to AUTO (EVEN) or AUTO (KEY) when the table grows.

The following table gives the distribution style for each value in RELEFFECTIVEDISTSTYLE column:

| RELEFFECTIVEDISTSTYLE | Current distribution style |
| --------------------- | -------------------------- |
| 0                     | EVEN                       |
| 1                     | KEY                        |
| 8                     | ALL                        |
| 10                    | AUTO (ALL)                 |
| 11                    | AUTO (EVEN)                |
| 12                    | AUTO (KEY)                 |

The DISTSTYLE column in SVV_TABLE_INFO indicates the current
distribution style for the table. If the table uses automatic distribution,
DISTSTYLE is AUTO (ALL), AUTO (EVEN), or AUTO (KEY).

The following example creates four tables using the three distribution styles and automatic distribution,
then queries SVV_TABLE_INFO to view the distribution styles.

```

create table public.dist_key (col1 int)
diststyle key distkey (col1);

insert into public.dist_key values (1);

create table public.dist_even (col1 int)
diststyle even;

insert into public.dist_even values (1);

create table public.dist_all (col1 int)
diststyle all;

insert into public.dist_all values (1);

create table public.dist_auto (col1 int);

insert into public.dist_auto values (1);

select "schema", "table", diststyle from SVV_TABLE_INFO
where "table" like 'dist%';

        schema   |    table        | diststyle
     ------------+-----------------+------------
      public     | dist_key        | KEY(col1)
      public     | dist_even       | EVEN
      public     | dist_all        | ALL
      public     | dist_auto       | AUTO(ALL)
```
