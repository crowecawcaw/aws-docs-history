# Step 4: Configure `cqlsh COPY FROM`

settings

This section outlines how to determine the parameter values for `cqlsh COPY
 FROM`. The `cqlsh COPY FROM` command reads the CSV file that you
prepared earlier and inserts the data into Amazon Keyspaces using CQL. The command divides up the
rows and distributes the `INSERT` operations among a set of workers. Each
worker establishes a connection with Amazon Keyspaces and sends `INSERT` requests along
this channel.

The `cqlsh COPY` command doesn’t have internal logic to distribute work
evenly among its workers. However, you can configure it manually to make sure that the
work is distributed evenly. Start by reviewing these key cqlsh parameters:

- DELIMITER – If you used a delimiter other
  than a comma, you can set this parameter, which defaults to comma.
- INGESTRATE – The target number of rows
  that `cqlsh COPY FROM` attempts to process per second. If unset, it
  defaults to 100,000.
- NUMPROCESSES – The number of child worker
  processes that cqlsh creates for `COPY FROM` tasks. The maximum for
  this setting is 16, the default is `num_cores - 1`, where
  `num_cores` is the number of processing cores on the host running
  cqlsh.
- MAXBATCHSIZE – The batch size determines the maximal number of rows
  inserted into the destination table in a single batch.
  If unset, cqlsh uses batches of 20 inserted rows.
- CHUNKSIZE – The size of the work unit
  that passes to the child worker. By default, it is set to 5,000.
- MAXATTEMPTS – The maximum number of times
  to retry a failed worker chunk. After the maximum attempt is reached, the failed
  records are written to a new CSV file that you can run again later after
  investigating the failure.
  Set `INGESTRATE` based on the number of WCUs that you provisioned to the
  target destination table. The `INGESTRATE` of the `cqlsh COPY FROM`
  command isn’t a limit—it’s a target average. This means it can (and often does)
  burst above the number you set. To allow for bursts and make sure that enough capacity
  is in place to handle the data load requests, set `INGESTRATE` to 90% of the
  table’s write capacity.

```
INGESTRATE = WCUs * .90
```

Next, set the `NUMPROCESSES` parameter to equal to one less than the number
of cores on your system. To find out what the number of cores of your system is, you can
run the following code.

```
python -c "import multiprocessing; print(multiprocessing.cpu_count())"
```

For this tutorial, we use the following value.

```
NUMPROCESSES = 4
```

Each process creates a worker, and each worker establishes a connection to Amazon Keyspaces.
Amazon Keyspaces can support up to 3,000 CQL requests per second on every connection. This means
that you have to make sure that each worker is processing fewer than 3,000 requests per
second.

As with `INGESTRATE`, the workers often burst above the number you set and
aren’t limited by clock seconds. Therefore, to account for bursts, set your cqlsh
parameters to target each worker to process 2,500 requests per second. To calculate the
amount of work distributed to a worker, use the following guideline.

- Divide `INGESTRATE` by `NUMPROCESSES`.
- If `INGESTRATE` / `NUMPROCESSES` > 2,500, lower the
  `INGESTRATE` to make this formula true.

```
INGESTRATE / NUMPROCESSES <= 2,500
```

Before you configure the settings to optimize the upload of our sample data, let's
review the `cqlsh` default settings and see how using them impacts the data
upload process. Because `cqlsh COPY FROM` uses the `CHUNKSIZE` to
create chunks of work (`INSERT` statements) to distribute to workers, the
work is not automatically distributed evenly. Some workers might sit idle, depending on
the `INGESTRATE` setting.

To distribute work evenly among the workers and keep each worker at the optimal 2,500
requests per second rate, you must set `CHUNKSIZE`,
`MAXBATCHSIZE`, and `INGESTRATE` by changing the input parameters.
To optimize network traffic utilization during the data load, choose a value for
`MAXBATCHSIZE` that is close to the maximum value of 30. By changing
`CHUNKSIZE` to 100 and `MAXBATCHSIZE` to 25, the 10,000 rows
are spread evenly among the four workers (10,000 / 2500 = 4).

The following code example illustrates this.

```
INGESTRATE = 10,000
NUMPROCESSES = 4
CHUNKSIZE = 100
MAXBATCHSIZE. = 25
Work Distribution:
Connection 1 / Worker 1 : 2,500 Requests per second
Connection 2 / Worker 2 : 2,500 Requests per second
Connection 3 / Worker 3 : 2,500 Requests per second
Connection 4 / Worker 4 : 2,500 Requests per second
```

To summarize, use the following formulas when setting `cqlsh COPY FROM` parameters:

- INGESTRATE = write_capacity_units \* .90
- NUMPROCESSES = num_cores -1
  (default)
- INGESTRATE / NUMPROCESSES = 2,500 (This must be
  a true statement.)
- MAXBATCHSIZE = 30 (Defaults to 20. Amazon Keyspaces
  accepts batches up to 30.)
- CHUNKSIZE = (INGESTRATE / NUMPROCESSES) /
  MAXBATCHSIZE
  Now that you have calculated `NUMPROCESSES`, `INGESTRATE`, and
  `CHUNKSIZE`, you’re ready to load your data.
