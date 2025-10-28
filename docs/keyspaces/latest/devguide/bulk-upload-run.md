# Step 5: Run the `cqlsh COPY FROM` command to upload data from the CSV file to the target table

To run the `cqlsh COPY FROM` command, complete the following steps.

1. Connect to Amazon Keyspaces using cqlsh.
2. Choose your keyspace with the following code.

```
USE `catalog`;
```

3. Set write consistency to `LOCAL_QUORUM`. To ensure data durability,
   Amazon Keyspaces doesn’t allow other write consistency settings. See the following
   code.

```
CONSISTENCY LOCAL_QUORUM;
```

4. Prepare your `cqlsh COPY FROM` syntax using the following code
   example.

```
COPY `book_awards` FROM './keyspace.table.csv' WITH HEADER=true
AND INGESTRATE=`calculated ingestrate`
AND NUMPROCESSES=`calculated numprocess`
AND MAXBATCHSIZE=20
AND CHUNKSIZE=`calculated chunksize`;
```

5.  Run the statement prepared in the previous step. cqlsh echoes back all the
    settings that you've configured.

        1. Make sure that the settings match your input. See the following
         example.



        ```
        `Reading options from the command line: {'chunksize': '120', 'header': 'true', 'ingestrate': '36000', 'numprocesses': '15', 'maxbatchsize': '20'}
        Using 15 child processes`
        ```
        2. Review the number of rows transferred and the current average rate, as
         shown in the following example.



        ```
        `Processed: 57834 rows; Rate: 6561 rows/s; Avg. rate: 31751 rows/s`
        ```
        3. When cqlsh has finished uploading the data, review the summary of the
         data load statistics (the number of files read, runtime, and skipped
         rows) as shown in the following example.



        ```
        `15556824 rows imported from 1 files in 8 minutes and 8.321 seconds (0 skipped).`
        ```

    In this final step of the tutorial, you have uploaded the data to Amazon Keyspaces.

###### Important

Now that you have transferred your data, adjust the capacity mode settings of your
target table to match your application’s regular traffic patterns. You incur charges
at the hourly rate for your provisioned capacity until you change it.
