After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# In-Application Streams and Pumps

When you configure [application input](how-it-works-input.md "how-it-works-input.md"),
you map a streaming source to an in-application stream
that is created. Data continuously flows from the streaming source into the
in-application stream. An in-application stream works like a table that you can query using
SQL statements, but it's called a stream because it represents continuous data flow.

###### Note

Do not confuse in-application streams with Amazon Kinesis data streams and Firehose
delivery streams. In-application streams exist only in the context of an Amazon Kinesis Data Analytics
application. Kinesis data streams and Firehose delivery streams exist independent of your
application. You can configure them as a streaming source in your application input
configuration or as a destination in output configuration.

You can also create more in-application streams as needed to store intermediate query
results. Creating an in-application stream is a two-step process. First, you create an
in-application stream, and then you pump data into it. For example, suppose that the input
configuration of your application creates an in-application stream named
`INPUTSTREAM`. In the following example, you create another stream
(`TEMPSTREAM`), and then you pump data from `INPUTSTREAM` into it.

1. Create an in-application stream (`TEMPSTREAM`) with three
   columns, as shown following:

```
CREATE OR REPLACE STREAM "TEMPSTREAM" (
   "column1" BIGINT NOT NULL,
   "column2" INTEGER,
   "column3" VARCHAR(64));
```

The column names are specified in quotes, making them case sensitive. For more
information, see [Identifiers](../sqlref/sql-reference-identifiers.md "../sqlref/sql-reference-identifiers.md") in the _Amazon Kinesis Data Analytics SQL Reference_. 2. Insert data into the stream using a pump. A pump is a continuous insert query running that inserts data from one in-application stream to another in-application stream. The following statement creates a
pump (`SAMPLEPUMP`) and inserts data into the `TEMPSTREAM` by selecting
records from another stream (`INPUTSTREAM`).

```
CREATE OR REPLACE PUMP "SAMPLEPUMP" AS
INSERT INTO "TEMPSTREAM" ("column1",
                          "column2",
                          "column3")
SELECT STREAM inputcolumn1,
              inputcolumn2,
              inputcolumn3
FROM "INPUTSTREAM";
```

You can have multiple writers insert into an in-application stream, and there can be
multiple readers selected from the stream. Think of an in-application stream as
implementing a publish/subscribe messaging paradigm. In this paradigm, the data row,
including the time of creation and time of receipt, can be processed, interpreted, and
forwarded by a cascade of streaming SQL statements, without having to be stored in a
traditional RDBMS.

After an in-application stream is created, you can perform normal SQL queries.

###### Note

When you query streams, most SQL statements are bound using a row-based or
time-based window. For more information, see [Windowed Queries](windowed-sql.md "windowed-sql.md").

You can also join streams. For examples of joining streams, see [Streaming Data Operations: Stream Joins](stream-joins-concepts.md "stream-joins-concepts.md").
