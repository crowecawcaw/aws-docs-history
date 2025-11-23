# Enabling full text search on existing Neptune databases

These are the established approaches to enabling full text search on existing Amazon Neptune databases.
Depending on whether you can pause your write workloads or not, the steps may vary slightly.
This guide outlines the recommended steps for both scenarios - when you can pause writes, and when you cannot.
It covers enabling Neptune streams, creating a database clone, synchronizing data to an OpenSearch domain,
and setting up continuous updates. The guidance leverages AWS services and open-source tools to streamline the
process and minimize downtime.

## If you can pause your write workloads

The best way to enable full text search on an existing Neptune database is
generally as follows, provided you can pause your write workloads. It requires creating
a clone, enabling the streams using a cluster parameter, and restarting all the
instances. Creating a clone is a relatively fast operation, so the downtime
required is limited.

Here are the steps required:

1. Stop all write workloads on the database.
2. Enable streams on the database (see [Enabling
   Neptune Streams](streams-using-enabling.md "streams-using-enabling.md")).
3. Create a clone of the database (see [Database
   Cloning in Neptune](manage-console-cloning.md "manage-console-cloning.md")).
4. Resume the write workloads.
5. Use the [export-neptune-to-elasticsearch](https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch "https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch")
   tool on github to perform a one-time synchronization from the cloned database to the OpenSearch
   domain.
6. Use the [CloudFormation
   template for your region](full-text-search-cfn-create.md#full-text-search-cfn-by-region "full-text-search-cfn-create.md#full-text-search-cfn-by-region") to start synchronization from your original database
   with continuous updating (no configuration change is needed in the template).
7. Delete the cloned database and the CloudFormation stack created for the
   `export-neptune-to-elasticsearch` tool.

###### Note

[export-neptune-to-elasticsearch](https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch "https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch") does not currently support Opensearch serverless. Deployments which require
a one-time synchronization of existing data in Neptune must use Opensearch managed clusters.

## If you cannot pause your write workloads

If you can't afford to suspend write workloads on your database, here is an
approach that requires even less downtime than the recommended approach above,
but it needs to be done carefully:

1. Enable streams on the database (see [Enabling
   Neptune Streams](streams-using-enabling.md "streams-using-enabling.md")).
2. Create a clone of the database (see [Database
   Cloning in Neptune](manage-console-cloning.md "manage-console-cloning.md")).
3. Get the latest `eventID` for the streams on the cloned database by
   executing a command of this kind against the Streams API endpoint (see [Calling the Neptune Streams REST API](streams-using-api-call.md "streams-using-api-call.md") for
   more information):

```
curl "https://`(your neptune endpoint)`:`(port)`/`(propertygraph or sparql)`/stream?iteratorType=LATEST"
```

Make a note of the values in the `commitNum` and `opNum` fields
in the `lastEventId` object in the response. 4. Use the [export-neptune-to-elasticsearch](https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch "https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch")
tool on github to perform a one-time synchronization from the cloned database to the OpenSearch
domain. 5. Use the [CloudFormation
template for your region](full-text-search-cfn-create.md#full-text-search-cfn-by-region "full-text-search-cfn-create.md#full-text-search-cfn-by-region") to start synchronization from your original database
with continuous updating.

Make the following change while creating the stack: on the stack details page,
in the **Parameters** section, set the value of the `StartingCheckpoint`
field to `*commitNum*`:`*opnum*`
using the the `commitNum` and `opNum` values you recorded above. 6. Delete the cloned database and the CloudFormation stack created for the
`export-neptune-to-elasticsearch` tool.
