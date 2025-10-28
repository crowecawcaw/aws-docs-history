# Step 2: Prepare the data to upload using DSBulk

Preparing the source data for an efficient transfer is a two-step process. First, you
randomize the data. In the second step, you analyze the data to determine the
appropriate `dsbulk` parameter values and required table settings.

###### Randomize the data

The `dsbulk` command reads and writes data in the same order that it
appears in the CSV file. If you use the `dsbulk` command to create the
source file, the data is written in key-sorted order in the CSV. Internally, Amazon Keyspaces
partitions data using partition keys. Although Amazon Keyspaces has built-in logic to help load
balance requests for the same partition key, loading the data is faster and more
efficient if you randomize the order. This is because you can take advantage of the
built-in load balancing that occurs when Amazon Keyspaces is writing to different
partitions.

To spread the writes across the partitions evenly, you must randomize the data in the
source file. You can write an application to do this or use an open-source tool, such as
[Shuf](https://en.wikipedia.org/wiki/Shuf "https://en.wikipedia.org/wiki/Shuf"). Shuf is freely
available on Linux distributions, on macOS (by installing coreutils in [homebrew](https://brew.sh "https://brew.sh")), and on Windows (by using Windows Subsystem
for Linux (WSL)). One extra step is required to prevent the header row with the column
names to get shuffled in this step.

To randomize the source file while preserving the header, enter the following
code.

```
tail -n +2 `keyspaces_sample_table.csv` | shuf -o `keyspace.table.csv` && (head -1 `keyspaces_sample_table.csv` && cat keyspace.table.csv ) > `keyspace.table.csv1` && mv `keyspace.table.csv1` `keyspace.table.csv`
```

Shuf rewrites the data to a new CSV file called
`keyspace.table.csv`. You can now delete the
`keyspaces_sample_table.csv` file—you no longer need
it.

###### Analyze the data

Determine the average and maximum row size by analyzing the data.

You do this for the following reasons:

- The average row size helps to estimate the total amount of data to be
  transferred.
- You need the average row size to provision the write capacity needed for the data upload.
- You can make sure that each row is less than 1 MB in size, which is the
  maximum row size in Amazon Keyspaces.

###### Note

This quota refers to row size, not partition size. Unlike Apache Cassandra
partitions, Amazon Keyspaces partitions can be virtually unbound in size. Partition keys and
clustering columns require additional storage for metadata, which you must add to
the raw size of rows. For more information, see [Estimate row size in Amazon Keyspaces](calculating-row-size.md "calculating-row-size.md").

The following code uses [AWK](https://en.wikipedia.org/wiki/AWK "https://en.wikipedia.org/wiki/AWK") to
analyze a CSV file and print the average and maximum row size.

```
awk -F, 'BEGIN {samp=10000;max=-1;}{if(NR>1){len=length($0);t+=len;avg=t/NR;max=(len>max ? len : max)}}NR==samp{exit}END{printf("{lines: %d, average: %d bytes, max: %d bytes}\n",NR,avg,max);}' `keyspace.table.csv`
```

Running this code results in the following output.

```
using 10,000 samples:
{lines: 10000, avg: 123 bytes, max: 225 bytes}
```

Make sure that your maximum row size doesn't exceed 1 MB. If it does, you have to
break up the row or compress the data to bring the row size below 1 MB. In the next step
of this tutorial, you use the average row size to provision the write capacity for the
table.
