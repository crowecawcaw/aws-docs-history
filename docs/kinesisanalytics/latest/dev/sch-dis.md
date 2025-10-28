After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Using the Schema Discovery Feature on Streaming Data

###### Note

After September 12, 2023, you will not able to create new applications using Kinesis Data Firehose as a source if you do not already use Kinesis Data Analytics for SQL. For more information, see [Limits](limits.md "limits.md").

Providing an input schema that describes how records on the streaming input map to an
in-application stream can be cumbersome and error prone. You can use the [DiscoverInputSchema](API_DiscoverInputSchema.md "API_DiscoverInputSchema.md") API
(called the _discovery API_) to infer a schema. Using random samples
of records on the streaming source, the API can infer a schema (that is, column names,
data types, and position of the data element in the incoming data).

###### Note

To use the Discovery API to generate a schema from a file stored in Amazon S3, see
[Using the Schema Discovery Feature on Static Data](sch-dis-ref.md "sch-dis-ref.md").

The console uses the Discovery API to generate a schema for a specified streaming
source. Using the console, you can also update the schema, including adding or removing
columns, changing column names or data types, and so on. However, make changes carefully
to ensure that you do not create an invalid schema.

After you finalize a schema for your in-application stream, there are functions you
can use to manipulate string and datetime values. You can use these functions in your
application code when working with rows in the resulting in-application stream. For more
information, see [Example: Transforming
DateTime Values](app-string-datetime-manipulation.md "app-string-datetime-manipulation.md").

## Column Naming During Schema Discovery

During schema discovery, Amazon Kinesis Data Analytics tries to retain as much of the original column
name as possible from the streaming input source, except in the following
cases:

- The source stream column name is a reserved SQL keyword, such as
  `TIMESTAMP`, `USER`, `VALUES`, or
  `YEAR`.
- The source stream column name contains unsupported characters. Only
  letters, numbers, and the underscore character ( \_ ) are supported.
- The source stream column name begins with a number.
- The source stream column name is longer than 100 characters.

If a column is renamed, the renamed schema column name begins with
`COL_`. In some cases, none of the original column name can be
retained—for example, if the entire name is unsupported characters. In such a
case, the column is named `COL_#`, with # being a number indicating the
column's place in the column order.

After discovery completes, you can update the schema using the console to add or
remove columns, or change column names, data types, or data size.

### Examples of Discovery-Suggested

Column Names

| Source Stream Column Name | Discovery-Suggested Column Name |
| ------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| USER                      | COL_USER                        |
| USER@DOMAIN               | COL_USERDOMAIN                  |
| @@                        | COL_0                           | ## Schema Discovery Issues What happens if Kinesis Data Analytics does not infer a schema for a given streaming source? Kinesis Data Analytics infers your schema for common formats, such as CSV and JSON, which are UTF-8 encoded. Kinesis Data Analytics supports any UTF-8 encoded records (including raw text like application logs and records) with a custom column and row delimiter. If Kinesis Data Analytics doesn't infer a schema, you can define a schema manually using the schema editor on the console (or using the API). If your data does not follow a pattern (which you can specify using the schema editor), you can define a schema as a single column of type VARCHAR(N), where N is the largest number of characters you expect your record to include. From there, you can use string and date-time manipulation to structure your data after it is in an in-application stream. For examples, see [Example: Transforming DateTime Values](app-string-datetime-manipulation.md "app-string-datetime-manipulation.md"). |
