Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# UNLOAD examples

These examples demonstrate various parameters of the UNLOAD command.
The TICKIT sample data is used in many of the examples. For more information, see
[Sample database](c_sampledb.md "c_sampledb.md").

###### Note

These examples contain line breaks for readability. Do not include line breaks
or spaces in your _credentials-args_ string.

## Unload VENUE to a pipe-delimited file

(default delimiter)

The following example unloads the VENUE table and writes the data to
`s3://amzn-s3-demo-bucket/unload/`:

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/unload/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
```

By default, UNLOAD writes one or more files per slice. Assuming a two-node cluster
with two slices per node, the previous example creates these files in
`amzn-s3-demo-bucket`:

```
unload/0000_part_00
unload/0001_part_00
unload/0002_part_00
unload/0003_part_00
```

To better differentiate the output files, you can include a prefix in the
location. The following example unloads the VENUE table and writes the data to
`s3://amzn-s3-demo-bucket/unload/venue_pipe_`:

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/unload/venue_pipe_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
```

The result is these four files in the `unload` folder, again assuming
four slices.

```
venue_pipe_0000_part_00
venue_pipe_0001_part_00
venue_pipe_0002_part_00
venue_pipe_0003_part_00
```

## Unload LINEITEM table to

partitioned Parquet files

The following example unloads the LINEITEM table in Parquet format, partitioned by
the `l_shipdate` column.

```
unload ('select * from lineitem')
to 's3://amzn-s3-demo-bucket/lineitem/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
PARQUET
PARTITION BY (l_shipdate);

```

Assuming four slices, the resulting Parquet files are dynamically partitioned into
various folders.

```

s3://amzn-s3-demo-bucket/lineitem/l_shipdate=1992-01-02/0000_part_00.parquet
                                             0001_part_00.parquet
                                             0002_part_00.parquet
                                             0003_part_00.parquet
s3://amzn-s3-demo-bucket/lineitem/l_shipdate=1992-01-03/0000_part_00.parquet
                                             0001_part_00.parquet
                                             0002_part_00.parquet
                                             0003_part_00.parquet
s3://amzn-s3-demo-bucket/lineitem/l_shipdate=1992-01-04/0000_part_00.parquet
                                             0001_part_00.parquet
                                             0002_part_00.parquet
                                             0003_part_00.parquet
...

```

###### Note

In some cases, the UNLOAD command used the INCLUDE option as shown in the
following SQL statement.

```
unload ('select * from lineitem')
to 's3://amzn-s3-demo-bucket/lineitem/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
PARQUET
PARTITION BY (l_shipdate) INCLUDE;

```

In these cases, the `l_shipdate` column is also in the data in the
Parquet files. Otherwise, the `l_shipdate` column data isn't in
the Parquet files.

## Unload the VENUE table to a JSON file

The following example unloads the VENUE table and writes the data in JSON format to `s3://amzn-s3-demo-bucket/unload/`.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/unload/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
JSON;
```

Following are sample rows from the VENUE table.

```
venueid | venuename                  | venuecity       | venuestate | venueseats
--------+----------------------------+-----------------+------------+-----------
      1 | Pinewood Racetrack         | Akron           | OH         | 0
      2 | Columbus "Crew" Stadium    | Columbus        | OH         | 0
      4 | Community, Ballpark, Arena | Kansas City     | KS         | 0
```

After unloading to JSON, the format of the file is similar to the following.

```
{"venueid":1,"venuename":"Pinewood Racetrack","venuecity":"Akron","venuestate":"OH","venueseats":0}
{"venueid":2,"venuename":"Columbus \"Crew\" Stadium ","venuecity":"Columbus","venuestate":"OH","venueseats":0}
{"venueid":4,"venuename":"Community, Ballpark, Arena","venuecity":"Kansas City","venuestate":"KS","venueseats":0}
```

## Unload VENUE to a CSV file

The following example unloads the VENUE table and writes the data in CSV format to
`s3://amzn-s3-demo-bucket/unload/`.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/unload/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
CSV;
```

Suppose that the VENUE table contains the following rows.

```

venueid | venuename                  | venuecity       | venuestate | venueseats
--------+----------------------------+-----------------+------------+-----------
      1 | Pinewood Racetrack         | Akron           | OH         | 0
      2 | Columbus "Crew" Stadium    | Columbus        | OH         | 0
      4 | Community, Ballpark, Arena | Kansas City     | KS         | 0

```

The unload file looks similar to the following.

```
1,Pinewood Racetrack,Akron,OH,0
2,"Columbus ""Crew"" Stadium",Columbus,OH,0
4,"Community, Ballpark, Arena",Kansas City,KS,0
```

## Unload VENUE to a CSV file using a

delimiter

The following example unloads the VENUE table and writes the data in CSV format
using the pipe character (|) as the delimiter. The unloaded file is written to
`s3://amzn-s3-demo-bucket/unload/`. The VENUE table in this example contains the
pipe character in the value of the first row (`Pinewood Race|track`). It
does this to show that the value in the result is enclosed in double quotation marks.
A double quotation mark is escaped by a double quotation mark, and the entire field
is enclosed in double quotation marks.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/unload/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
CSV DELIMITER AS '|';
```

Suppose that the VENUE table contains the following rows.

```

venueid | venuename                  | venuecity       | venuestate | venueseats
--------+----------------------------+-----------------+------------+-------------
      1 | Pinewood Race|track        | Akron           | OH         | 0
      2 | Columbus "Crew" Stadium    | Columbus        | OH         | 0
      4 | Community, Ballpark, Arena | Kansas City     | KS         | 0

```

The unload file looks similar to the following.

```
1|"Pinewood Race|track"|Akron|OH|0
2|"Columbus ""Crew"" Stadium"|Columbus|OH|0
4|Community, Ballpark, Arena|Kansas City|KS|0

```

## Unload VENUE with a manifest file

To create a manifest file, include the MANIFEST option. The following example
unloads the VENUE table and writes a manifest file along with the data files to
s3://amzn-s3-demo-bucket/venue_pipe\_:

###### Important

If you unload files with the MANIFEST option, you should use the MANIFEST
option with the COPY command when you load the files. If you use the same prefix
to load the files and don't specify the MANIFEST option, COPY fails because
it assumes the manifest file is a data file.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/venue_pipe_' iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
manifest;
```

The result is these five files:

```
s3://amzn-s3-demo-bucket/venue_pipe_0000_part_00
s3://amzn-s3-demo-bucket/venue_pipe_0001_part_00
s3://amzn-s3-demo-bucket/venue_pipe_0002_part_00
s3://amzn-s3-demo-bucket/venue_pipe_0003_part_00
s3://amzn-s3-demo-bucket/venue_pipe_manifest
```

The following shows the contents of the manifest file.

```
{
  "entries": [
    {"url":"s3://amzn-s3-demo-bucket/tickit/venue_0000_part_00"},
    {"url":"s3://amzn-s3-demo-bucket/tickit/venue_0001_part_00"},
    {"url":"s3://amzn-s3-demo-bucket/tickit/venue_0002_part_00"},
    {"url":"s3://amzn-s3-demo-bucket/tickit/venue_0003_part_00"}
  ]
}
```

## Unload VENUE with MANIFEST

VERBOSE

When you specify the MANIFEST VERBOSE option, the manifest file includes the
following sections:

- The `entries` section lists Amazon S3 path, file size, and row
  count for each file.
- The `schema` section lists the column names, data types, and
  dimension for each column.
- The `meta` section shows the total file size and row count for
  all files.

The following example unloads the VENUE table using the MANIFEST VERBOSE option.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/unload_venue_folder/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
manifest verbose;
```

The following shows the contents of the manifest file.

```
{
  "entries": [
    {"url":"s3://amzn-s3-demo-bucket/venue_pipe_0000_part_00", "meta": { "content_length": 32295, "record_count": 10 }},
    {"url":"s3://amzn-s3-demo-bucket/venue_pipe_0001_part_00", "meta": { "content_length": 32771, "record_count": 20 }},
    {"url":"s3://amzn-s3-demo-bucket/venue_pipe_0002_part_00", "meta": { "content_length": 32302, "record_count": 10 }},
    {"url":"s3://amzn-s3-demo-bucket/venue_pipe_0003_part_00", "meta": { "content_length": 31810, "record_count": 15 }}
  ],
  "schema": {
    "elements": [
      {"name": "venueid", "type": { "base": "integer" }},
      {"name": "venuename", "type": { "base": "character varying", 25 }},
      {"name": "venuecity", "type": { "base": "character varying", 25 }},
      {"name": "venuestate", "type": { "base": "character varying", 25 }},
      {"name": "venueseats", "type": { "base": "character varying", 25 }}
    ]
  },
  "meta": {
    "content_length": 129178,
    "record_count": 55
  },
  "author": {
    "name": "Amazon Redshift",
    "version": "1.0.0"
  }
}
```

## Unload VENUE with a header

The following example unloads VENUE with a header row.

```
unload ('select * from venue where venueseats > 75000')
to 's3://amzn-s3-demo-bucket/unload/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
header
parallel off;
```

The following shows the contents of the output file with a header row.

```
venueid|venuename|venuecity|venuestate|venueseats
6|New York Giants Stadium|East Rutherford|NJ|80242
78|INVESCO Field|Denver|CO|76125
83|FedExField|Landover|MD|91704
79|Arrowhead Stadium|Kansas City|MO|79451
```

## Unload VENUE to smaller files

By default, the maximum file size is 6.2 GB. If the unload data is larger than 6.2
GB, UNLOAD creates a new file for each 6.2 GB data segment. To create smaller files,
include the MAXFILESIZE parameter. Assuming the size of the data in the previous
example was 20 GB, the following UNLOAD command creates 20 files, each 1 GB in
size.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/unload/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
maxfilesize 1 gb;

```

## Unload VENUE serially

To unload serially, specify PARALLEL OFF. UNLOAD then writes one file at a time,
up to a maximum of 6.2 GB per file.

The following example unloads the VENUE table and writes the data serially to
`s3://amzn-s3-demo-bucket/unload/`.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/unload/venue_serial_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
parallel off;
```

The result is one file named venue_serial_000.

If the unload data is larger than 6.2 GB, UNLOAD creates a new file for each 6.2
GB data segment. The following example unloads the LINEORDER table and writes the
data serially to `s3://amzn-s3-demo-bucket/unload/`.

```
unload ('select * from lineorder')
to 's3://amzn-s3-demo-bucket/unload/lineorder_serial_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
parallel off gzip;
```

The result is the following series of files.

```
lineorder_serial_0000.gz
lineorder_serial_0001.gz
lineorder_serial_0002.gz
lineorder_serial_0003.gz
```

To better differentiate the output files, you can include a prefix in the
location. The following example unloads the VENUE table and writes the data to
`s3://amzn-s3-demo-bucket/venue_pipe_`:

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/unload/venue_pipe_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
```

The result is these four files in the `unload` folder, again assuming
four slices.

```
venue_pipe_0000_part_00
venue_pipe_0001_part_00
venue_pipe_0002_part_00
venue_pipe_0003_part_00
```

## Load VENUE from unload files

To load a table from a set of unload files, simply reverse the process by using a
COPY command. The following example creates a new table, LOADVENUE, and loads the
table from the data files created in the previous example.

```
create table loadvenue (like venue);

copy loadvenue from 's3://amzn-s3-demo-bucket/venue_pipe_' iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
```

If you used the MANIFEST option to create a manifest file with your unload files,
you can load the data using the same manifest file. You do so with a COPY command
with the MANIFEST option. The following example loads data using a manifest
file.

```
copy loadvenue
from 's3://amzn-s3-demo-bucket/venue_pipe_manifest' iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
manifest;

```

## Unload VENUE to encrypted

files

The following example unloads the VENUE table to a set of encrypted files using an AWS KMS key.
If you specify a manifest file with the ENCRYPTED option, the manifest file
is also encrypted. For more information, see [Unloading encrypted data files](t_unloading_encrypted_files.md "t_unloading_encrypted_files.md").

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/venue_encrypt_kms'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
kms_key_id '1234abcd-12ab-34cd-56ef-1234567890ab'
manifest
encrypted;
```

The following example unloads the VENUE table to a set of encrypted files using a
root symmetric key.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/venue_encrypt_cmk'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
master_symmetric_key 'EXAMPLEMASTERKEYtkbjk/OpCwtYSx/M4/t7DMCDIK722'
encrypted;
```

## Load VENUE from encrypted

files

To load tables from a set of files that were created by using UNLOAD with the
ENCRYPT option, reverse the process by using a COPY command. With that command, use
the ENCRYPTED option and specify the same root symmetric key that was used for the
UNLOAD command. The following example loads the LOADVENUE table from the encrypted
data files created in the previous example.

```
create table loadvenue (like venue);

copy loadvenue
from 's3://amzn-s3-demo-bucket/venue_encrypt_manifest'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
master_symmetric_key 'EXAMPLEMASTERKEYtkbjk/OpCwtYSx/M4/t7DMCDIK722'
manifest
encrypted;
```

## Unload VENUE data to a tab-delimited

file

```
unload ('select venueid, venuename, venueseats from venue')
to 's3://amzn-s3-demo-bucket/venue_tab_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
delimiter as '\t';
```

The output data files look like this:

```
1	Toyota Park	Bridgeview	IL	0
2	Columbus Crew Stadium	Columbus	OH	0
3	RFK Stadium	Washington	DC	0
4	CommunityAmerica Ballpark	Kansas City	KS	0
5	Gillette Stadium	Foxborough	MA	68756
...
```

## Unload VENUE to a fixed-width data

file

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/venue_fw_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
fixedwidth as 'venueid:3,venuename:39,venuecity:16,venuestate:2,venueseats:6';
```

The output data files look like the following.

```
1  Toyota Park              Bridgeview  IL0
2  Columbus Crew Stadium    Columbus    OH0
3  RFK Stadium              Washington  DC0
4  CommunityAmerica BallparkKansas City KS0
5  Gillette Stadium         Foxborough  MA68756
...
```

## Unload VENUE to a set of tab-delimited

GZIP-compressed files

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/venue_tab_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
delimiter as '\t'
gzip;
```

## Unload VENUE to a GZIP-compressed text file

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/venue_tab_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
extension 'txt.gz'
gzip;

```

## Unload data that contains a

delimiter

This example uses the ADDQUOTES option to unload comma-delimited data where some
of the actual data fields contain a comma.

First, create a table that contains quotation marks.

```
create table location (id int, location char(64));

insert into location values (1,'Phoenix, AZ'),(2,'San Diego, CA'),(3,'Chicago, IL');
```

Then, unload the data using the ADDQUOTES option.

```
unload ('select id, location from location')
to 's3://amzn-s3-demo-bucket/location_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
delimiter ',' addquotes;
```

The unloaded data files look like this:

```
1,"Phoenix, AZ"
2,"San Diego, CA"
3,"Chicago, IL"
...
```

## Unload the results of a join query

The following example unloads the results of a join query that contains a window
function.

```
unload ('select venuecity, venuestate, caldate, pricepaid,
sum(pricepaid) over(partition by venuecity, venuestate
order by caldate rows between 3 preceding and 3 following) as winsum
from sales join date on sales.dateid=date.dateid
join event on event.eventid=sales.eventid
join venue on event.venueid=venue.venueid
order by 1,2')
to 's3://amzn-s3-demo-bucket/tickit/winsum'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
```

The output files look like this:

```
Atlanta|GA|2008-01-04|363.00|1362.00
Atlanta|GA|2008-01-05|233.00|2030.00
Atlanta|GA|2008-01-06|310.00|3135.00
Atlanta|GA|2008-01-08|166.00|8338.00
Atlanta|GA|2008-01-11|268.00|7630.00
...
```

## Unload using NULL AS

UNLOAD outputs null values as empty strings by default. The following examples
show how to use NULL AS to substitute a text string for nulls.

For these examples, we add some null values to the VENUE table.

```
update venue set venuestate = NULL
where venuecity = 'Cleveland';
```

Select from VENUE where VENUESTATE is null to verify that the columns contain
NULL.

```
`select * from venue where venuestate is null;`
`venueid | venuename | venuecity | venuestate | venueseats
---------+--------------------------+-----------+------------+------------
 22 | Quicken Loans Arena | Cleveland | | 0
 101 | Progressive Field | Cleveland | | 43345
 72 | Cleveland Browns Stadium | Cleveland | | 73200`
```

Now, UNLOAD the VENUE table using the NULL AS option to replace null values with
the character string '`fred`'.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/nulls/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
null as 'fred';
```

The following sample from the unload file shows that null values were replaced
with `fred`. It turns out that some values for VENUESEATS were also null
and were replaced with `fred`. Even though the data type for VENUESEATS is
integer, UNLOAD converts the values to text in the unload files, and then COPY
converts them back to integer. If you are unloading to a fixed-width file, the NULL
AS string must not be larger than the field width.

```
248|Charles Playhouse|Boston|MA|0
251|Paris Hotel|Las Vegas|NV|fred
258|Tropicana Hotel|Las Vegas|NV|fred
300|Kennedy Center Opera House|Washington|DC|0
306|Lyric Opera House|Baltimore|MD|0
308|Metropolitan Opera|New York City|NY|0
  5|Gillette Stadium|Foxborough|MA|5
 22|Quicken Loans Arena|Cleveland|fred|0
101|Progressive Field|Cleveland|fred|43345
...
```

To load a table from the unload files, use a COPY command with the same NULL AS
option.

###### Note

If you attempt to load nulls into a column defined as NOT NULL, the COPY
command fails.

```
create table loadvenuenulls (like venue);

copy loadvenuenulls from 's3://amzn-s3-demo-bucket/nulls/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
null as 'fred';
```

To verify that the columns contain null, not just empty strings, select from
LOADVENUENULLS and filter for null.

```
`select * from loadvenuenulls where venuestate is null or venueseats is null;`
`venueid | venuename | venuecity | venuestate | venueseats
---------+--------------------------+-----------+------------+------------
 72 | Cleveland Browns Stadium | Cleveland | | 73200
 253 | Mirage Hotel | Las Vegas | NV |
 255 | Venetian Hotel | Las Vegas | NV |
 22 | Quicken Loans Arena | Cleveland | | 0
 101 | Progressive Field | Cleveland | | 43345
 251 | Paris Hotel | Las Vegas | NV |

...`
```

You can UNLOAD a table that contains nulls using the default NULL AS behavior and
then COPY the data back into a table using the default NULL AS behavior; however, any
non-numeric fields in the target table contain empty strings, not nulls. By default
UNLOAD converts nulls to empty strings (white space or zero-length). COPY converts
empty strings to NULL for numeric columns, but inserts empty strings into non-numeric
columns. The following example shows how to perform an UNLOAD followed by a COPY
using the default NULL AS behavior.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/nulls/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole' allowoverwrite;

truncate loadvenuenulls;
copy loadvenuenulls from 's3://amzn-s3-demo-bucket/nulls/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
```

In this case, when you filter for nulls, only the rows where VENUESEATS contained
nulls. Where VENUESTATE contained nulls in the table (VENUE), VENUESTATE in the
target table (LOADVENUENULLS) contains empty strings.

```
`select * from loadvenuenulls where venuestate is null or venueseats is null;`
`venueid | venuename | venuecity | venuestate | venueseats
---------+--------------------------+-----------+------------+------------
 253 | Mirage Hotel | Las Vegas | NV |
 255 | Venetian Hotel | Las Vegas | NV |
 251 | Paris Hotel | Las Vegas | NV |
...`
```

To load empty strings to non-numeric columns as NULL, include the EMPTYASNULL or
BLANKSASNULL options. It's OK to use both.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/nulls/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole' allowoverwrite;

truncate loadvenuenulls;
copy loadvenuenulls from 's3://amzn-s3-demo-bucket/nulls/'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole' EMPTYASNULL;
```

To verify that the columns contain NULL, not just whitespace or empty strings,
select from LOADVENUENULLS and filter for null.

```
`select * from loadvenuenulls where venuestate is null or venueseats is null;`
`venueid | venuename | venuecity | venuestate | venueseats
---------+--------------------------+-----------+------------+------------
 72 | Cleveland Browns Stadium | Cleveland | | 73200
 253 | Mirage Hotel | Las Vegas | NV |
 255 | Venetian Hotel | Las Vegas | NV |
 22 | Quicken Loans Arena | Cleveland | | 0
 101 | Progressive Field | Cleveland | | 43345
 251 | Paris Hotel | Las Vegas | NV |
 ...`
```

## Unload using ALLOWOVERWRITE parameter

By default, UNLOAD doesn't overwrite existing files in the destination
bucket. For example, if you run the same UNLOAD statement twice without modifying the
files in the destination bucket, the second UNLOAD fails. To overwrite the existing
files, including the manifest file, specify the ALLOWOVERWRITE option.

```
unload ('select * from venue')
to 's3://amzn-s3-demo-bucket/venue_pipe_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
manifest allowoverwrite;
```

## Unload EVENT table using PARALLEL and MANIFEST parameters

You can UNLOAD a table in parallel and generate a manifest file.
The Amazon S3 data files are all created at the same level and names are suffixed with the pattern `0000_part_00`.
The manifest file is at the same folder level as the data files and suffixed with the text `manifest`.
The following SQL unloads the EVENT table and creates files with the base name `parallel`

```
unload ('select * from mytickit1.event')
to 's3://amzn-s3-demo-bucket/parallel'
iam_role 'arn:aws:iam::123456789012:role/MyRedshiftRole'
parallel on
manifest;
```

The Amazon S3 files listing is similar to the following.

```

 Name                       Last modified                        Size
 parallel0000_part_00	-   August 2, 2023, 14:54:39 (UTC-07:00) 52.1 KB
 parallel0001_part_00	-   August 2, 2023, 14:54:39 (UTC-07:00) 53.4 KB
 parallel0002_part_00	-   August 2, 2023, 14:54:39 (UTC-07:00) 52.1 KB
 parallel0003_part_00	-   August 2, 2023, 14:54:39 (UTC-07:00) 51.1 KB
 parallel0004_part_00	-   August 2, 2023, 14:54:39 (UTC-07:00) 54.6 KB
 parallel0005_part_00	-   August 2, 2023, 14:54:39 (UTC-07:00) 53.4 KB
 parallel0006_part_00	-   August 2, 2023, 14:54:39 (UTC-07:00) 54.1 KB
 parallel0007_part_00	-   August 2, 2023, 14:54:39 (UTC-07:00) 55.9 KB
 parallelmanifest       -   August 2, 2023, 14:54:39 (UTC-07:00) 886.0 B

```

The `parallelmanifest` file content is similar to the following.

```

{
  "entries": [
    {"url":"s3://amzn-s3-demo-bucket/parallel0000_part_00", "meta": { "content_length": 53316 }},
    {"url":"s3://amzn-s3-demo-bucket/parallel0001_part_00", "meta": { "content_length": 54704 }},
    {"url":"s3://amzn-s3-demo-bucket/parallel0002_part_00", "meta": { "content_length": 53326 }},
    {"url":"s3://amzn-s3-demo-bucket/parallel0003_part_00", "meta": { "content_length": 52356 }},
    {"url":"s3://amzn-s3-demo-bucket/parallel0004_part_00", "meta": { "content_length": 55933 }},
    {"url":"s3://amzn-s3-demo-bucket/parallel0005_part_00", "meta": { "content_length": 54648 }},
    {"url":"s3://amzn-s3-demo-bucket/parallel0006_part_00", "meta": { "content_length": 55436 }},
    {"url":"s3://amzn-s3-demo-bucket/parallel0007_part_00", "meta": { "content_length": 57272 }}
  ]
}

```

## Unload EVENT table using PARALLEL OFF and MANIFEST parameters

You can UNLOAD a table serially (PARALLEL OFF) and generate a manifest file.
The Amazon S3 data files are all created at the same level and names are suffixed with the pattern `0000`.
The manifest file is at the same folder level as the data files and suffixed with the text `manifest`.

```
unload ('select * from mytickit1.event')
to 's3://amzn-s3-demo-bucket/serial'
iam_role 'arn:aws:iam::123456789012:role/MyRedshiftRole'
parallel off
manifest;
```

The Amazon S3 files listing is similar to the following.

```

 Name                       Last modified                        Size
 serial0000             -   August 2, 2023, 15:54:39 (UTC-07:00) 426.7 KB
 serialmanifest         -   August 2, 2023, 15:54:39 (UTC-07:00) 120.0 B

```

The `serialmanifest` file content is similar to the following.

```

{
  "entries": [
    {"url":"s3://amzn-s3-demo-bucket/serial000", "meta": { "content_length": 436991 }}
  ]
}

```

## Unload EVENT table using PARTITION BY and MANIFEST parameters

You can UNLOAD a table by partition and generate a manifest file.
A new folder is created in Amazon S3 with child partition folders, and the data files in the child folders with a name pattern similar to `0000_par_00`.
The manifest file is at the same folder level as the child folders with the name `manifest`.

```
unload ('select * from mytickit1.event')
to 's3://amzn-s3-demo-bucket/partition'
iam_role 'arn:aws:iam::123456789012:role/MyRedshiftRole'
partition by (eventname)
manifest;
```

The Amazon S3 files listing is similar to the following.

```

 Name                   Type     Last modified                        Size
 partition           	Folder

```

In the `partition` folder are child folders with the partition name and the manifest file.
Shown following is the bottom of the list of folders in the `partition` folder, similar to the following.

```

 Name                   Type      Last modified                        Size
 ...
 eventname=Zucchero/    Folder
 eventname=Zumanity/    Folder
 eventname=ZZ Top/      Folder
 manifest          	    -	    August 2, 2023, 15:54:39 (UTC-07:00) 467.6 KB

```

In the `eventname=Zucchero/` folder are the data files similar to the following.

```

 Name               Last modified                        Size
 0000_part_00	-   August 2, 2023, 15:59:19 (UTC-07:00) 70.0 B
 0001_part_00	-   August 2, 2023, 15:59:16 (UTC-07:00) 106.0 B
 0002_part_00	-   August 2, 2023, 15:59:15 (UTC-07:00) 70.0 B
 0004_part_00	-   August 2, 2023, 15:59:17 (UTC-07:00) 141.0 B
 0006_part_00	-   August 2, 2023, 15:59:16 (UTC-07:00) 35.0 B
 0007_part_00	-   August 2, 2023, 15:59:19 (UTC-07:00) 108.0 B

```

The bottom of the `manifest` file content is similar to the following.

```

{
  "entries": [
    ...
    {"url":"s3://amzn-s3-demo-bucket/partition/eventname=Zucchero/007_part_00", "meta": { "content_length": 108 }},
    {"url":"s3://amzn-s3-demo-bucket/partition/eventname=Zumanity/007_part_00", "meta": { "content_length": 72 }}
  ]
}

```

## Unload EVENT table using MAXFILESIZE, ROWGROUPSIZE, and MANIFEST parameters

You can UNLOAD a table in parallel and generate a manifest file.
The Amazon S3 data files are all created at the same level and names are suffixed with the pattern `0000_part_00`.
The generated Parquet data files are limited to 256 MB and row group size 128 MB.
The manifest file is at the same folder level as the data files and suffixed with `manifest`.

```
unload ('select * from mytickit1.event')
to 's3://amzn-s3-demo-bucket/eventsize'
iam_role 'arn:aws:iam::123456789012:role/MyRedshiftRole'
maxfilesize 256 MB
rowgroupsize 128 MB
parallel on
parquet
manifest;
```

The Amazon S3 files listing is similar to the following.

```

 Name                            Type      Last modified                        Size
 eventsize0000_part_00.parquet	parquet	August 2, 2023, 17:35:21 (UTC-07:00) 24.5 KB
 eventsize0001_part_00.parquet	parquet	August 2, 2023, 17:35:21 (UTC-07:00) 24.8 KB
 eventsize0002_part_00.parquet	parquet	August 2, 2023, 17:35:21 (UTC-07:00) 24.4 KB
 eventsize0003_part_00.parquet	parquet	August 2, 2023, 17:35:21 (UTC-07:00) 24.0 KB
 eventsize0004_part_00.parquet	parquet	August 2, 2023, 17:35:21 (UTC-07:00) 25.3 KB
 eventsize0005_part_00.parquet	parquet	August 2, 2023, 17:35:21 (UTC-07:00) 24.8 KB
 eventsize0006_part_00.parquet	parquet	August 2, 2023, 17:35:21 (UTC-07:00) 25.0 KB
 eventsize0007_part_00.parquet	parquet	August 2, 2023, 17:35:21 (UTC-07:00) 25.6 KB
 eventsizemanifest                 -       August 2, 2023, 17:35:21 (UTC-07:00) 958.0 B

```

The `eventsizemanifest` file content is similar to the following.

```

{
  "entries": [
    {"url":"s3://amzn-s3-demo-bucket/eventsize0000_part_00.parquet", "meta": { "content_length": 25130 }},
    {"url":"s3://amzn-s3-demo-bucket/eventsize0001_part_00.parquet", "meta": { "content_length": 25428 }},
    {"url":"s3://amzn-s3-demo-bucket/eventsize0002_part_00.parquet", "meta": { "content_length": 25025 }},
    {"url":"s3://amzn-s3-demo-bucket/eventsize0003_part_00.parquet", "meta": { "content_length": 24554 }},
    {"url":"s3://amzn-s3-demo-bucket/eventsize0004_part_00.parquet", "meta": { "content_length": 25918 }},
    {"url":"s3://amzn-s3-demo-bucket/eventsize0005_part_00.parquet", "meta": { "content_length": 25362 }},
    {"url":"s3://amzn-s3-demo-bucket/eventsize0006_part_00.parquet", "meta": { "content_length": 25647 }},
    {"url":"s3://amzn-s3-demo-bucket/eventsize0007_part_00.parquet", "meta": { "content_length": 26256 }}
  ]
}

```
