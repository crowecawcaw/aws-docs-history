# Using the COPY command with Aurora PostgreSQL Limitless Database

You can use the [\copy](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMANDS-COPY "https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMANDS-COPY") functionality in the
`psql` utility for importing data into and exporting data from Aurora PostgreSQL Limitless Database

## Using the COPY command to load data into Aurora PostgreSQL Limitless Database

Aurora PostgreSQL Limitless Database is compatible with the [\copy](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMANDS-COPY "https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMANDS-COPY")
functionality in the `psql` utility for importing data.

In Limitless Database as in Aurora PostgreSQL, the following aren't supported:

- Direct SSH access to DB instances – You can't copy a data file (such as in .csv format) to the DB instance host and run
  `COPY` from the file.
- Using local files on the DB instance – Use `COPY ... FROM STDIN` and `COPY ... TO STDOUT`.

The `COPY` command in PostgreSQL has options for working with local files (`FROM/TO`) and transmitting data using a
connection between the client and the server (`STDIN/STDOUT`). For more information, see [COPY](https://www.postgresql.org/docs/current/sql-copy.html "https://www.postgresql.org/docs/current/sql-copy.html") in the PostgreSQL documentation.

The `\copy` command in the PostgreSQL `psql` utility works with local files on the computer where you run the
`psql` client. It invokes the respective `COPY ... FROM STDIN` or `COPY ... FROM STDOUT` command on the
remote (for example, Limitless Database) server to which you connect. It reads data from the local file to `STDIN` or writes to it from
`STDOUT`.

### Splitting data into multiple files

Data is stored on multiple shards in Aurora PostgreSQL Limitless Database. To speed up data loading using `\copy`, you can split your data into multiple
files. Then import independently for each data file by running separate `\copy` commands in parallel.

For example, you have an input data file in CSV format with 3 million rows to import. You can split the file into chunks each holding
200,000 rows (15 chunks):

```
split -l200000 data.csv data_ --additional-suffix=.csv -d
```

This results in files `data_00.csv` through `data_14.csv`. You can then import data using 15
parallel `\copy` commands, for example:

```
psql -h dbcluster.limitless-111122223333.aws-region.rds.amazonaws.com -U username -c "\copy test_table from '/tmp/data_00.csv';" postgres_limitless &
psql -h dbcluster.limitless-111122223333.aws-region.rds.amazonaws.com -U username -c "\copy test_table FROM '/tmp/data_01.csv';" postgres_limitless &
...
psql -h dbcluster.limitless-111122223333.aws-region.rds.amazonaws.com -U username -c "\copy test_table FROM '/tmp/data_13.csv';" postgres_limitless &
psql -h dbcluster.limitless-111122223333.aws-region.rds.amazonaws.com -U username -c "\copy test_table FROM '/tmp/data_14.csv';" postgres_limitless
```

Using this technique, the same amount of data is imported approximately 10 times faster than using a single `\copy`
command.

## Using the COPY command to copy Limitless Database data to a file

You can use the [\copy](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMANDS-COPY "https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMANDS-COPY") command to copy
data from a limitless table to a file, as shown in the following example:

```
postgres_limitless=> \copy test_table TO '/tmp/test_table.csv' DELIMITER ',' CSV HEADER;
```
