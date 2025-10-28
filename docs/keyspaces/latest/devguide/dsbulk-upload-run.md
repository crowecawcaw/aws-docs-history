# Step 5: Run the DSBulk `load`

command to upload data from the CSV file to the target table

In the final step of this tutorial, you upload the data into Amazon Keyspaces.

To run the DSBulk `load` command, complete the following steps.

1. Run the following code to upload the data from your csv file to your Amazon Keyspaces
   table. Make sure to update the path to the application configuration file you
   created earlier.

```
dsbulk load -f `./dsbulk_keyspaces.conf`  --connector.csv.url keyspace.table.csv -header true --batch.mode DISABLED --executor.maxPerSecond `5` --driver.basic.request.timeout `"5 minutes"` --driver.advanced.retry-policy.max-retries `10` -k catalog -t book_awards
```

2. The output includes the location of a log file that details successful and
   unsuccessful operations. The file is stored in the following directory.

```
`Operation directory: /home/user_name/logs/UNLOAD_20210308-202317-801911`
```

3. The log file entries will include metrics, as in the following example. Check
   to make sure that the number of rows is consistent with the number of rows in
   your csv file.

```
`total | failed | rows/s | p50ms | p99ms | p999ms
 200 | 0 | 200 | 21.63 | 21.89 | 21.89`
```

###### Important

Now that you have transferred your data, adjust the capacity mode settings of your
target table to match your application’s regular traffic patterns. You incur charges
at the hourly rate for your provisioned capacity until you change it. For more
information, see [Configure read/write capacity modes in Amazon Keyspaces](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md").
