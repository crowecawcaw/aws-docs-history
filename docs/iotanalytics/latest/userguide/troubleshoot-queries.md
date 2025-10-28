End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Troubleshoot common issues with SQL queries in

AWS IoT Analytics

Use the following information to help troubleshoot issues with your SQL queries in
AWS IoT Analytics.

- To escape a single
  quote, precede it with another single quote. Don't confuse this with a
  double quote.

###### Example

```
SELECT 'O''Reilly'
```

- To escape
  underscores, use backticks to enclose data store column names that
  begin with an underscore.

###### Example

```
SELECT `_myMessageAttribute` FROM myDataStore

```

- To escape names with
  numbers, enclose data store names that include numbers in double
  quotes.

###### Example

```
SELECT * FROM "myDataStore123"
```

- To escape reserved
  keywords, enclose reserved keywords in double quotes. For more
  information, see [List of Reserved Keywords](../../../athena/latest/ug/reserved-words.md#list-of-reserved-words-sql-select "../../../athena/latest/ug/reserved-words.md#list-of-reserved-words-sql-select") in _SQL SELECT
  Statements_.
