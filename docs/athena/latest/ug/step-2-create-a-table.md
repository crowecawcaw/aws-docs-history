# Step 2: Create a table

Now that you have a database, you can create an Athena table for it. The table that you
create will be based on sample Amazon CloudFront log data in the location
`s3://athena-examples-`myregion`/cloudfront/plaintext/`,
where `myregion` is your current AWS Region.

The sample log data is in tab-separated values (TSV) format, which means that a tab
character is used as a delimiter to separate the fields. The data looks like the
following example. For readability, the tabs in the excerpt have been converted to
spaces and the final field shortened.

```
2014-07-05 20:00:09 DFW3 4260 10.0.0.15 GET eabcd12345678.cloudfront.net /test-image-1.jpeg 200 - Mozilla/5.0[...]
2014-07-05 20:00:09 DFW3 4252 10.0.0.15 GET eabcd12345678.cloudfront.net /test-image-2.jpeg 200 - Mozilla/5.0[...]
2014-07-05 20:00:10 AMS1 4261 10.0.0.15 GET eabcd12345678.cloudfront.net /test-image-3.jpeg 200 - Mozilla/5.0[...]
```

To enable Athena to read this data, you could create a straightforward `CREATE
 EXTERNAL TABLE` statement like the following. The statement that creates the
table defines columns that map to the data, specifies how the data is delimited, and
specifies the Amazon S3 location that contains the sample data. Note that because Athena
expects to scan all of the files in a folder, the `LOCATION` clause specifies
an Amazon S3 folder location, not a specific file.

Do not use this example just yet as it has an important limitation that will be
explained shortly.

```
CREATE EXTERNAL TABLE IF NOT EXISTS cloudfront_logs (
  `Date` DATE,
  Time STRING,
  Location STRING,
  Bytes INT,
  RequestIP STRING,
  Method STRING,
  Host STRING,
  Uri STRING,
  Status INT,
  Referrer STRING,
  ClientInfo STRING
  )
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY '\t'
  LINES TERMINATED BY '\n'
  LOCATION 's3://athena-examples-`my-region`/cloudfront/plaintext/';
```

The example creates a table called `cloudfront_logs` and specifies a name
and data type for each field. These fields become the columns in the table. Because
`date` is a [reserved word](reserved-words.md#list-of-ddl-reserved-words "reserved-words.md#list-of-ddl-reserved-words"), it is escaped with
backtick (`) characters. `ROW FORMAT DELIMITED` means that Athena will use a
 default library called [LazySimpleSerDe](lazy-simple-serde.md "lazy-simple-serde.md") to do the actual work of
 parsing the data. The example also specifies that the fields are tab separated
 (`FIELDS TERMINATED BY '\t'`) and that each record in the file ends in a
 newline character (`LINES TERMINATED BY '\n`). Finally, the
 `LOCATION` clause specifies the path in Amazon S3 where the actual data to be
read is located.

If you have your own tab or comma-separated data, you can use a `CREATE
 TABLE` statement like the example just presented—as long as your fields
do not contain nested information. However, if you have a column like
`ClientInfo` that contains nested information that uses a different
delimiter, a different approach is required.

###### Extracting data from the ClientInfo field

Looking at the sample data, here is a full example of the final field
`ClientInfo`:

```
Mozilla/5.0%20(Android;%20U;%20Windows%20NT%205.1;%20en-US;%20rv:1.9.0.9)%20Gecko/2009040821%20IE/3.0.9
```

As you can see, this field is multivalued. Because the example `CREATE
 TABLE` statement just presented specifies tabs as field delimiters, it can't
break out the separate components inside the `ClientInfo` field into separate
columns. So, a new `CREATE TABLE` statement is required.

To create columns from the values inside the `ClientInfo` field, you can
use a [regular
expression](https://en.wikipedia.org/wiki/Regular_expression "https://en.wikipedia.org/wiki/Regular_expression") (regex) that contains regex groups. The regex groups that you
specify become separate table columns. To use a regex in your `CREATE TABLE`
statement, use syntax like the following. This syntax instructs Athena to use the [Regex SerDe](regex-serde.md "regex-serde.md") library and the regular
expression that you specify.

```
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
  WITH SERDEPROPERTIES ("input.regex" = "`regular_expression`")
```

Regular expressions can be useful for creating tables from complex CSV or TSV data but
can be difficult to write and maintain. Fortunately, there are other libraries that you
can use for formats like JSON, Parquet, and ORC. For more information, see [Choose a SerDe for your data](supported-serdes.md "supported-serdes.md").

Now you are ready to create the table in the Athena query editor. The `CREATE
 TABLE` statement and regex are provided for you.

###### To create a table in Athena

1. In the navigation pane, for **Database**, make sure that
   `mydatabase` is selected.
2. To give yourself more room in the query editor, you can choose the arrow icon
   to collapse the navigation pane.

![Choose the arrow to collapse the navigation pane.](images/getting-started-collapse-nav-pane.png) 3. To create a tab for a new query, choose the plus (**+**) sign
in the query editor. You can have up to ten query tabs open at once.

![Choose the plus icon to create a new query.](images/getting-started-new-query-tab.png) 4. To close one or more query tabs, choose the arrow next to the plus sign. To
close all tabs at once, choose the arrow, and then choose **Close all
tabs**.

![Choose the arrow icon to close one or more query tabs.](images/close-all-query-editor-tabs.png) 5. In the query pane, enter the following `CREATE EXTERNAL TABLE`
statement. The regex breaks out the operating system, browser, and browser
version information from the `ClientInfo` field in the log
data.

###### Note

The regex used in the following example is designed to work with the
publicly available sample CloudFront log data in the
`athena-examples` Amazon S3 location and is illustrative
only. For more up-to-date regexes that query both standard and real-time
CloudFront log files, see [Query Amazon CloudFront logs](cloudfront-logs.md "cloudfront-logs.md").

```
CREATE EXTERNAL TABLE IF NOT EXISTS cloudfront_logs (
  `Date` DATE,
  Time STRING,
  Location STRING,
  Bytes INT,
  RequestIP STRING,
  Method STRING,
  Host STRING,
  Uri STRING,
  Status INT,
  Referrer STRING,
  os STRING,
  Browser STRING,
  BrowserVersion STRING
  )
  ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
  WITH SERDEPROPERTIES (
  "input.regex" = "^(?!#)([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+[^\(]+[\(]([^\;]+).*\%20([^\/]+)[\/](.*)$"
  ) LOCATION 's3://athena-examples-`myregion`/cloudfront/plaintext/';
```

6. In the `LOCATION` statement, replace
   `myregion` with the AWS Region that you are
   currently using (for example, `us-west-1`).
7. Choose **Run**.

The table `cloudfront_logs` is created and appears under the list
of **Tables** for the `mydatabase` database.
