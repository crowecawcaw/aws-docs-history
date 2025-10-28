# Recording real-time item interaction events

An _item interaction event_ is an interaction between a user and an item in your catalog. For example, a user purchasing
shoes or watching movie.

Record real-time item interaction events as you show your customer item recommendations. This builds out your interactions
data and keeps your data fresh. And it tells Amazon Personalize about the current interests of your user, which can improve recommendation
relevance.

You record item interaction events with the [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") API
operation. Amazon Personalize appends the event data to the _Item interactions dataset_ in your dataset group. If you
record two events with exactly the same timestamp and identical properties, Amazon Personalize keeps only one of the events. You can
record item interaction events using the AWS SDKs, AWS Amplify, or AWS Command Line Interface (AWS CLI).

If you use Apache Kafka, you can use the _Kafka connector for Amazon Personalize_ to stream item interactions in real time to Amazon Personalize.
For information see [Kafka Connector for Amazon Personalize](https://github.com/aws/personalize-kafka-connector/blob/main/README.md "https://github.com/aws/personalize-kafka-connector/blob/main/README.md") in the _personalize-kafka-connector_ Github repository.

AWS Amplify includes a JavaScript library for recording item interaction events from
web client applications, and a library for recording events in server code.
For more information, see [Amplify documentation](https://docs.amplify.aws/ "https://docs.amplify.aws/").

###### Topics

- [Requirements for recording
  item interaction events and training a model](#recording-events-requirements "#recording-events-requirements")
- [Creating an item interaction event tracker](event-get-tracker.md "event-get-tracker.md")
- [Recording a single item interaction event](putevents-example.md "putevents-example.md")
- [Recording multiple item interaction events with event value data](recording-events-example-event-value.md "recording-events-example-event-value.md")
- [Recording
  item interaction events with impressions data](putevents-including-impressions-data.md "putevents-including-impressions-data.md")
- [Event metrics and attribution reports](event-metrics.md "event-metrics.md")

## Requirements for recording

item interaction events and training a model

To record item interaction events, you need the following:

- A dataset group that includes an `Item interactions`
  dataset, which can be empty. If you went through the [Getting started tutorials](getting-started.md "getting-started.md") guide,
  you can use the same dataset group and dataset that you created. For
  information on creating a dataset group and a dataset, see [Importing training data into Amazon Personalize datasets](import-data.md "import-data.md").
- An event tracker.
- A call to the [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") API operation.
- If you use an AWS Lambda function to call the PutEvents operation, your function's execution role must have permission to perform the `personalize:PutEvents`
  action with the wildcard `*` in the `Resource` element.

You can start out with an empty Item interactions dataset and, when you
have recorded enough data, train the model using only new recorded events.
For all use cases (Domain dataset groups) and recipes (Custom dataset groups),
your interactions data must have the following before training:

- At minimum 1000 item interactions records from users interacting with items in your catalog.
  These interactions can be from bulk imports, or streamed events, or both.
- At minimum 25 unique user IDs with at least two item interactions for each.

For quality recommendations, we recommend that you have at minimum 50,000 item interactions from at least 1,000 users with two or more item interactions each.
