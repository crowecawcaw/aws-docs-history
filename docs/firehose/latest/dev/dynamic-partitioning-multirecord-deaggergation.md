# Apply dynamic partitioning to

aggregated data

You can apply dynamic partitioning to aggregated data (for example, multiple events,
logs, or records aggregated into a single `PutRecord` and
`PutRecordBatch` API call) but this data must first be deaggregated. You
can deaggregate your data by enabling multi record deaggregation - the process of
parsing through the records in the Firehose stream and separating them.

Multi record deaggregation can either be of `JSON` type, meaning that the
separation of records is based on consecutive JSON objects. Deaggregation can also be of
the type `Delimited`, meaning that the separation of records is performed
based on a specified custom delimiter. This custom delimiter must be a base-64 encoded
string. For example, if you want to use the following string as your custom delimiter
`####`, you must specify it in the base-64 encoded format, which
translates it to `IyMjIw==`. Record deaggregation by JSON or by delimiter is
capped at 500 per record.

###### Note

When deaggregating JSON records, make sure
that your input is still presented in the supported JSON format. JSON objects must be on a single line with no delimiter or newline-delimited (JSONL) only.
An array of
JSON objects is not a valid input.

These are examples of correct input: `{"a":1}{"a":2} and {"a":1}\n{"a":2}`

This is an example of the incorrect input: `[{"a":1}, {"a":2}]`

With aggregated data, when you enable dynamic partitioning, Firehose parses the records
and looks for either valid JSON objects or delimited records within each API call based
on the specified multi record deaggregation type.

###### Important

If your data is aggregated, dynamic partitioning can be only be applied if your
data is first deaggregated.

###### Important

When you use Data Transformation feature in Firehose, the deaggregation will be applied before
the Data Transformation. Data coming into Firehose will be processed in the following
order: Deaggregation → Data Transformation via Lambda → Partitioning Keys.
