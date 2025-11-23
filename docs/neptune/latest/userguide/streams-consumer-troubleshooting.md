# Troubleshooting Neptune full-text search

###### Note

If you have enabled [fine-grained access
control](../../../opensearch-service/latest/developerguide/fgac.md "../../../opensearch-service/latest/developerguide/fgac.md") on your OpenSearch cluster, you need to [enable
IAM authentication](iam-auth-enable.md "iam-auth-enable.md") in your Neptune database as well.

To diagnose issues with replication from Neptune to OpenSearch, consult the CloudWatch Logs for
your poller Lambda function. These logs provide details about the number of records read from
the stream and the number of records replicated successfully to OpenSearch.

You can also change the LOGGING level for your Lambda function by changing the
`LoggingLevel`environment variable.

###### Note

With `LoggingLevel` set to `DEBUG`, you can view additional
details, such as dropped stream records and the reason why each was dropped, while replicating
data by StreamPoller from Neptune to OpenSearch. This can be useful if you find you are
missing records.

The Neptune streams consumer application publishes two metrics on CloudWatch that can also
help you diagnose problems:

- `StreamRecordsProcessed` – The number of records processed by the
  application per unit of time. Helpful in tracking the application run rate.
- `StreamLagTime` – The time difference in milliseconds between the
  current time and the commit time of a stream record being processed. This metric shows how
  much the consumer application is lagging behind.
  In addition, all the metrics related to the replication process are exposed in a dashboard
  in CloudWatch under the same name same as the `ApplicationName` provided when you
  instantiated the application using the CloudWatch template.

You can also choose to create a CloudWatch alarm that is triggered whenever polling fails more
than twice in a row. Do this by setting the `CreateCloudWatchAlarm` field to
`true` when you instantiate the application. Then specify the email addresses
that you want to be notified when the alarm is triggered.

## Troubleshooting a process that fails while reading records from the stream

If a process fails while reading records from the stream, make sure that you have the
following:

- The stream is enabled on your cluster.
- The Neptune stream endpoint is in the correct format:
  - For Gremlin or openCypher: `https://`your cluster endpoint`:`your cluster port`/propertygraph/stream`
    or its alias, `https://`your cluster endpoint`:`your cluster port`/pg/stream`
  - For SPARQL: `https://`your cluster endpoint`:`your cluster port`/sparql/stream`

- The DynamoDB endpoint is configured for your VPC.
- The monitoring endpoint is configured for your VPC subnets.

## Troubleshooting a process that fails while writing data to OpenSearch

If a process fails while writing records to OpenSearch, make sure that you have the
following:

- Your Elasticsearch version is 7.1 or higher, or Opensearch 2.3 and above.
- OpenSearch can be accessed from the poller Lambda function in your VPC.
- The security policy attached to OpenSearch allows inbound HTTP/HTTPS requests.

## Fixing out-of-sync

issues between Neptune and OpenSearch on an existing replication setup

You can use the steps below to get a Neptune database and OpenSearch domain back
in sync with the latest data in case of out-of-sync issues between them resulting from
an `ExpiredStreamException` or data corruption.

Note that this approach deletes all the data in the OpenSearch domain and re-syncs
it from the current state of the Neptune database, so no data needs to be reloaded
in the Neptune database.

1. Disable the replication process as described in [Disabling (pausing) the stream poller
   process](full-text-search-pause-poller.md "full-text-search-pause-poller.md").
2. Delete the Neptune index on the OpenSearch domain using the following command:

```
curl -X DELETE "`(your OpenSearch endpoint)`/amazon_neptune"
```

3. Create a clone of the database (see [Database
   Cloning in Neptune](manage-console-cloning.md "manage-console-cloning.md")).
4. Get the latest `eventID` for the streams on the cloned database by
   executing a command of this kind against the Streams API endpoint (see [Calling the Neptune Streams REST API](streams-using-api-call.md "streams-using-api-call.md") for
   more information):

```
curl "https://`(your neptune endpoint)`:`(port)`/`(propertygraph or sparql)`/stream?iteratorType=LATEST"
```

Make a note of the values in the `commitNum` and `opNum` fields
in the `lastEventId` object in the response. 5. Use the [export-neptune-to-elasticsearch](https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch "https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch")
tool on github to perform a one-time synchronization from the cloned database to the OpenSearch
domain. 6. Go to the DynamoDB table for the replication stack. The name of the table will be
the **Application Name** you specified in the CloudFormation template (the default
is `NeptuneStream`) with a `-LeaseTable` suffix. In other words,
the default table name is `NeptuneStream-LeaseTable`.

You can explore table rows by scanning because there should only be one row in the
table. Make the following changes using the `commitNum` and `opNum`
values you recorded above:

    * Change the value for the `checkpoint` field in the table to
     the value you noted for `commitNum`.
    * Change the value for `checkpointSubSequenceNumber` field
     in the table to the value you noted for `opNum`.

7. Re-enable the replication process as described in [Re-enabling the stream poller
   process](full-text-search-re-enable-poller.md "full-text-search-re-enable-poller.md").
8. Delete the cloned database and the CloudFormation stack created for the
   `export-neptune-to-elasticsearch` tool.
