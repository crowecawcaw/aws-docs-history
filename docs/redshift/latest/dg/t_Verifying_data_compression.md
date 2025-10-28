Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Testing compression encodings

If you decide to manually specify column encodings, you might want to test
different encodings with your data.

###### Note

We recommend that you use the COPY command to load data whenever possible, and
allow the COPY command to choose the optimal encodings based on your data. Or
you can use the [ANALYZE COMPRESSION](r_ANALYZE_COMPRESSION.md "r_ANALYZE_COMPRESSION.md") command to view the suggested
encodings for existing data. For details about applying automatic compression,
see [Loading tables with automatic
compression](c_Loading_tables_auto_compress.md "c_Loading_tables_auto_compress.md").

To perform a meaningful test of data compression, you must have a large number of
rows. For this example, we create a table and insert rows by using a statement that
selects from two tables; VENUE and LISTING. We leave out the WHERE clause that would
normally join the two tables. The result is that _each_ row in
the VENUE table is joined to _all_ of the rows in the LISTING
table, for a total of over 32 million rows. This is known as a Cartesian join and
normally is not recommended. However, for this purpose, it's a convenient
method of creating many rows. If you have an existing table with data that you want
to test, you can skip this step.

After we have a table with sample data, we create a table with seven columns. Each
has a different compression encoding: raw, bytedict, lzo, run length, text255,
text32k, and zstd. We populate each column with exactly the same data by running an
INSERT command that selects the data from the first table.

To test compression encodings, do the following:

1. (Optional) First, use a Cartesian join to create a table with a
   large number of rows. Skip this step if you want to test an existing
   table.

```
create table cartesian_venue(
venueid smallint not null distkey sortkey,
venuename varchar(100),
venuecity varchar(30),
venuestate char(2),
venueseats integer);

insert into cartesian_venue
select venueid, venuename, venuecity, venuestate, venueseats
from venue, listing;
```

2. Next, create a table with the encodings that you want to compare.

```
create table encodingvenue (
venueraw varchar(100) encode raw,
venuebytedict varchar(100) encode bytedict,
venuelzo varchar(100) encode lzo,
venuerunlength varchar(100) encode runlength,
venuetext255 varchar(100) encode text255,
venuetext32k varchar(100) encode text32k,
venuezstd varchar(100) encode zstd);
```

3. Insert the same data into all of the columns using an INSERT
   statement with a SELECT clause.

```
insert into encodingvenue
select venuename as venueraw, venuename as venuebytedict, venuename as venuelzo, venuename as venuerunlength, venuename as  venuetext32k, venuename as  venuetext255, venuename as venuezstd
from cartesian_venue;
```

4. Verify the number of rows in the new table.

```
select count(*) from encodingvenue

  count
----------
 38884394
(1 row)
```

5. Query the [STV_BLOCKLIST](r_STV_BLOCKLIST.md "r_STV_BLOCKLIST.md") system table to compare the number
   of 1 MB disk blocks used by each column.

The MAX aggregate function returns the highest block number for each
column. The STV_BLOCKLIST table includes details for three system-generated
columns. This example uses `col < 6` in the WHERE clause to
exclude the system-generated columns.

```
select col, max(blocknum)
from stv_blocklist b, stv_tbl_perm p
where (b.tbl=p.id) and name ='encodingvenue'
and col < 7
group by name, col
order by col;
```

The query returns the following results. The columns are numbered
beginning with zero. Depending on how your cluster is configured, your
result might have different numbers, but the relative sizes should be
similar. You can see that BYTEDICT encoding on the second column produced
the best results for this dataset. This approach has a compression ratio of
better than 20:1. LZO and ZSTD encoding also produced excellent results.
Different datasets produce different results, of course. When a column
contains longer text strings, LZO often produces the best compression
results.

```
 col | max
-----+-----
   0 | 203
   1 |  10
   2 |  22
   3 | 204
   4 |  56
   5 |  72
   6 |  20
(7 rows)
```

If you have data in an existing table, you can use the [ANALYZE COMPRESSION](r_ANALYZE_COMPRESSION.md "r_ANALYZE_COMPRESSION.md") command
to view the suggested encodings for the table. For example, the following example
shows the recommended encoding for a copy of the VENUE table, CARTESIAN_VENUE, that
contains 38 million rows. Notice that ANALYZE COMPRESSION recommends LZO encoding
for the VENUENAME column. ANALYZE COMPRESSION chooses optimal compression based on
multiple factors, which include percent of reduction. In this specific case,
BYTEDICT provides better compression, but LZO also produces greater than 90 percent
compression.

```
analyze compression cartesian_venue;

Table          | Column     | Encoding | Est_reduction_pct
---------------+------------+----------+------------------
reallybigvenue | venueid    | lzo      | 97.54
reallybigvenue | venuename  | lzo      | 91.71
reallybigvenue | venuecity  | lzo      | 96.01
reallybigvenue | venuestate | lzo      | 97.68
reallybigvenue | venueseats | lzo      | 98.21
```

## Example

The following example creates a CUSTOMER table that has columns with various
data types. This CREATE TABLE statement shows one of many possible combinations of
compression encodings for these columns.

```
create table customer(
custkey int encode delta,
custname varchar(30) encode raw,
gender varchar(7) encode text255,
address varchar(200) encode text255,
city varchar(30) encode text255,
state char(2) encode raw,
zipcode char(5) encode bytedict,
start_date date encode delta32k);
```

The following table shows the column encodings that were chosen for the CUSTOMER
table and gives an explanation for the choices:

| Column     | Data type    | Encoding | Explanation                                                                                                                                                                                                                                                            |
| ---------- | ------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CUSTKEY    | int          | delta    | CUSTKEY consists of unique, consecutive integer values. Because the differences are one byte, DELTA is a good choice.                                                                                                                                                  |
| CUSTNAME   | varchar(30)  | raw      | CUSTNAME has a large domain with few repeated values. Any compression encoding would probably be ineffective.                                                                                                                                                          |
| GENDER     | varchar(7)   | text255  | GENDER is very small domain with many repeated values. Text255 works well with VARCHAR columns in which the same words recur.                                                                                                                                          |
| ADDRESS    | varchar(200) | text255  | ADDRESS is a large domain, but contains many repeated words, such as Street, Avenue, North, South, and so on. Text 255 and text 32k are useful for compressing VARCHAR columns in which the same words recur. The column length is short, so text255 is a good choice. |
| CITY       | varchar(30)  | text255  | CITY is a large domain, with some repeated values. Certain city names are used much more commonly than others. Text255 is a good choice for the same reasons as ADDRESS.                                                                                               |
| STATE      | char(2)      | raw      | In the United States, STATE is a precise domain of 50 two-character values. Bytedict encoding would yield some compression, but because the column size is only two characters, compression might not be worth the overhead of uncompressing the data.                 |
| ZIPCODE    | char(5)      | bytedict | ZIPCODE is a known domain of fewer than 50,000 unique values. Certain zip codes occur much more commonly than others. Bytedict encoding is very effective when a column contains a limited number of unique values.                                                    |
| START_DATE | date         | delta32k | Delta encodings are very useful for date time columns, especially if the rows are loaded in date order.                                                                                                                                                                |
