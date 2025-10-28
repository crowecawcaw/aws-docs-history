After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Step 4: Verify Output

After configuring the application output in [Step 3: Configure
Application Output](app-anomaly-create-ka-app-config-destination.md "app-anomaly-create-ka-app-config-destination.md"), use the following
AWS CLI commands to read records in the destination stream that is written by the
application:

1. Run the `get-shard-iterator` command to get a pointer to data
   on the output stream.

```
aws kinesis get-shard-iterator \
--shard-id shardId-000000000000 \
--shard-iterator-type TRIM_HORIZON \
--stream-name OutputStreamTestingAnomalyScores \
--region us-east-1 \
--profile adminuser
```

You get a response with a shard iterator value, as shown in the following
example response:

```
  {      
      "ShardIterator":
      "`shard-iterator-value`"   }
```

Copy the shard iterator value. 2. Run the AWS CLI `get-records` command.

```
aws kinesis get-records \
--shard-iterator `shared-iterator-value` \
--region us-east-1 \
--profile adminuser
```

The command returns a page of records and another shard iterator that you
can use in the subsequent `get-records` command to fetch the next
set of records.
