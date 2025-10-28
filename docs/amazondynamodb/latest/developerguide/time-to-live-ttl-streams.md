# DynamoDB Streams and Time to Live

You can back up, or otherwise process, items that are deleted by [Time to Live](TTL.md "TTL.md") (TTL) by enabling Amazon DynamoDB Streams on the table and processing the streams records
of the expired items. For more information, see [Reading and processing a stream](Streams.md#Streams.Processing "Streams.md#Streams.Processing").

The streams record contains a user identity field
`Records[`<index>`].userIdentity`.

Items that are deleted by the Time to Live process after expiration have the following
fields:

- `Records[`<index>`].userIdentity.type`

`"Service"`

- `Records[`<index>`].userIdentity.principalId`

`"dynamodb.amazonaws.com"`

###### Note

When you use TTL in a global table, the region the TTL was performed in will have the `userIdentity` field set. This field won't be set in other regions when the delete is replicated.

The following JSON shows the relevant portion of a single streams record.

```
"Records": [
    {
        ...

        "userIdentity": {
            "type": "Service",
            "principalId": "dynamodb.amazonaws.com"
        }

        ...

    }
]
```

## Using DynamoDB Streams and Lambda to archive TTL

deleted items

Combining [DynamoDB Time to Live (TTL)](TTL.md "TTL.md"),
[DynamoDB Streams](Streams.md "Streams.md"), and [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") can
help simplify archiving data, reduce DynamoDB storage costs, and reduce code complexity.
Using Lambda as the stream consumer provides many advantages, most notably the cost
reduction compared to other consumers such as Kinesis Client Library (KCL). You aren’t
charged for `GetRecords` API calls on your DynamoDB stream when using Lambda to
consume events, and Lambda can provide event filtering by identifying JSON patterns in a
stream event. With event-pattern content filtering, you can define up to five different
filters to control which events are sent to Lambda for processing. This helps reduce
invocations of your Lambda functions, simplifies code, and reduces overall cost.

While DynamoDB Streams contains all data modifications, such as `Create`,
`Modify`, and `Remove` actions, this can result in unwanted
invocations of your archive Lambda function. For example, say you have a table with 2
million data modifications per hour flowing into the stream, but less than 5 percent of
these are item deletes that will expire through the TTL process and need to be archived.
With [Lambda event source filters](../../../lambda/latest/dg/invocation-eventfiltering.md "../../../lambda/latest/dg/invocation-eventfiltering.md"), the Lambda function will only invoke 100,000
times per hour. The result with event filtering is that you’re charged only for the
needed invocations instead of the 2 million invocations you would have without event
filtering.

Event filtering is applied to the [Lambda event source
mapping](../../../lambda/latest/dg/invocation-eventsourcemapping.md "../../../lambda/latest/dg/invocation-eventsourcemapping.md"), which is a resource that reads from a chosen event—the DynamoDB
stream—and invokes a Lambda function. In the following diagram, you can see how a Time to Live
deleted item is consumed by a Lambda function using streams and event filters.

![An item deleted through TTL process starts a Lambda function that uses streams and event filters.](images/streams-lambda-ttl.png)

### DynamoDB Time to Live event filter pattern

Adding the following JSON to your event source mapping [filter criteria](../../../lambda/latest/dg/API_FilterCriteria.md "../../../lambda/latest/dg/API_FilterCriteria.md") allows
invocation of your Lambda function only for TTL deleted items:

```
{
    "Filters": [
        {
            "Pattern": { "userIdentity": { "type": ["Service"], "principalId": ["dynamodb.amazonaws.com"] } }
        }
    ]
}

```

### Create an AWS Lambda event source

mapping

Use the following code snippets to create a filtered event source mapping which
you can connect to a table's DynamoDB stream. Each code block includes the event filter
pattern.

AWS CLI

```
aws lambda create-event-source-mapping \
--event-source-arn 'arn:aws:dynamodb:eu-west-1:012345678910:table/test/stream/2021-12-10T00:00:00.000' \
--batch-size 10 \
--enabled \
--function-name test_func \
--starting-position LATEST \
--filter-criteria '{"Filters": [{"Pattern": "{\"userIdentity\":{\"type\":[\"Service\"],\"principalId\":[\"dynamodb.amazonaws.com\"]}}"}]}'

```

Java

```
LambdaClient client = LambdaClient.builder()
        .region(Region.EU_WEST_1)
        .build();

Filter userIdentity = Filter.builder()
        .pattern("{\"userIdentity\":{\"type\":[\"Service\"],\"principalId\":[\"dynamodb.amazonaws.com\"]}}")
        .build();

FilterCriteria filterCriteria = FilterCriteria.builder()
        .filters(userIdentity)
        .build();

CreateEventSourceMappingRequest mappingRequest = CreateEventSourceMappingRequest.builder()
        .eventSourceArn("arn:aws:dynamodb:eu-west-1:012345678910:table/test/stream/2021-12-10T00:00:00.000")
        .batchSize(10)
        .enabled(Boolean.TRUE)
        .functionName("test_func")
        .startingPosition("LATEST")
        .filterCriteria(filterCriteria)
        .build();

try{
    CreateEventSourceMappingResponse eventSourceMappingResponse = client.createEventSourceMapping(mappingRequest);
    System.out.println("The mapping ARN is "+eventSourceMappingResponse.eventSourceArn());

}catch (ServiceException e){
    System.out.println(e.getMessage());
}


```

Node

```
const client = new LambdaClient({ region: "eu-west-1" });

const input = {
    EventSourceArn: "arn:aws:dynamodb:eu-west-1:012345678910:table/test/stream/2021-12-10T00:00:00.000",
    BatchSize: 10,
    Enabled: true,
    FunctionName: "test_func",
    StartingPosition: "LATEST",
    FilterCriteria: { "Filters": [{ "Pattern": "{\"userIdentity\":{\"type\":[\"Service\"],\"principalId\":[\"dynamodb.amazonaws.com\"]}}" }] }
}

const command = new CreateEventSourceMappingCommand(input);

try {
    const results = await client.send(command);
    console.log(results);
} catch (err) {
    console.error(err);
}

```

Python

```
session = boto3.session.Session(region_name = 'eu-west-1')
client = session.client('lambda')

try:
    response = client.create_event_source_mapping(
        EventSourceArn='arn:aws:dynamodb:eu-west-1:012345678910:table/test/stream/2021-12-10T00:00:00.000',
        BatchSize=10,
        Enabled=True,
        FunctionName='test_func',
        StartingPosition='LATEST',
        FilterCriteria={
            'Filters': [
                {
                    'Pattern': "{\"userIdentity\":{\"type\":[\"Service\"],\"principalId\":[\"dynamodb.amazonaws.com\"]}}"
                },
            ]
        }
    )
    print(response)
except Exception as e:
    print(e)

```

JSON

```
{
  "userIdentity": {
     "type": ["Service"],
     "principalId": ["dynamodb.amazonaws.com"]
   }
}

```
