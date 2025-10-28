# Troubleshooting

After the data upload has completed, check to see if rows were skipped. To do so,
navigate to the source directory of the source CSV file and search for a file with the
following name.

```
import_`yourcsvfilename`.err.timestamp.csv
```

cqlsh writes any skipped rows of data into a file with that name. If the file exists
in your source directory and has data in it, these rows didn't upload to Amazon Keyspaces. To retry
these rows, first check for any errors that were encountered during the upload and
adjust the data accordingly. To retry these rows, you can rerun the process.

###### Common errors

The most common reasons why rows aren’t loaded are capacity errors and parsing
errors.

**Invalid request errors when uploading data to
Amazon Keyspaces**

In the following example, the source table contains a counter column, which results in logged batch calls from the cqlsh `COPY` command.
Logged batch calls are not supported by Amazon Keyspaces.

```
`Failed to import 10 rows: InvalidRequest - Error from server: code=2200 [Invalid query] message=“Only UNLOGGED Batches are supported at this time.“, will retry later, attempt 22 of 25`
```

To resolve this error, use DSBulk to migrate the data. For more information, see [Tutorial: Loading data into Amazon Keyspaces using DSBulk](dsbulk-upload.md "dsbulk-upload.md").

**Parser errors when uploading data to Amazon Keyspaces**

The following example shows a skipped row due to a `ParseError`.

```
`Failed to import 1 rows: ParseError - Invalid ... –`
```

To resolve this error, you need to make sure that the data to be imported matches the
table schema in Amazon Keyspaces. Review the import file for parsing errors. You can try using a
single row of data using an `INSERT` statement to isolate the error.

**Capacity errors when uploading data to Amazon Keyspaces**

```
`Failed to import 1 rows: WriteTimeout - Error from server: code=1100 [Coordinator node timed out waiting for replica nodes' responses]
 message="Operation timed out - received only 0 responses." info={'received_responses': 0, 'required_responses': 2, 'write_type': 'SIMPLE', 'consistency':
 'LOCAL_QUORUM'}, will retry later, attempt 1 of 100`
```

Amazon Keyspaces uses the `ReadTimeout` and `WriteTimeout` exceptions to
indicate when a write request fails due to insufficient throughput capacity. To help
diagnose insufficient capacity exceptions, Amazon Keyspaces publishes
`WriteThrottleEvents` and `ReadThrottledEvents` metrics in
Amazon CloudWatch. For more information, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

**cqlsh errors when uploading data to Amazon Keyspaces**

To help troubleshoot cqlsh errors, rerun the failing command with the `--debug` flag.

When using an incompatible version of cqlsh, you see the following error.

```
AttributeError: 'NoneType' object has no attribute 'is_up'
Failed to import 3 rows: AttributeError - 'NoneType' object has no attribute 'is_up',  given up after 1 attempts
```

Confirm that the correct version of cqlsh is installed by running the following
command.

```
cqlsh --version
```

You should see something like the following for output.

```
cqlsh 5.0.1
```

If you're using Windows, replace all instances of `cqlsh` with
`cqlsh.bat`. For example, to check the version of cqlsh in Windows, run
the following command.

```
cqlsh.bat --version
```

The connection to Amazon Keyspaces fails after the cqlsh client receives three consecutive errors
of any type from the server. The cqlsh client fails with the following message.

```
`Failed to import 1 rows: NoHostAvailable - , will retry later, attempt 3 of 100`
```

To resolve this error, you need to make sure that the data to be imported matches the
table schema in Amazon Keyspaces. Review the import file for parsing errors. You can try using a
single row of data by using an INSERT statement to isolate the error.

The client automatically attempts to reestablish the connection.
