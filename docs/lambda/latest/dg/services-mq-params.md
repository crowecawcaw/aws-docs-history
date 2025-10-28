# Event source mapping parameters

All Lambda event source types share the same [CreateEventSourceMapping](../api/API_CreateEventSourceMapping.md "../api/API_CreateEventSourceMapping.md") and [UpdateEventSourceMapping](../api/API_UpdateEventSourceMapping.md "../api/API_UpdateEventSourceMapping.md")
API operations. However, only some of the parameters apply to Amazon MQ and RabbitMQ.

| Parameter                      | Required | Default | Notes                                                                                                                                                                  |
| ------------------------------ | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BatchSize                      | N        | 100     | Maximum: 10,000                                                                                                                                                        |
| Enabled                        | N        | true    | none                                                                                                                                                                   |
| FunctionName                   | Y        | N/A     | none                                                                                                                                                                   |
| FilterCriteria                 | N        | N/A     | [Control which events Lambda sends to your function](invocation-eventfiltering.md "invocation-eventfiltering.md")                                                      |
| MaximumBatchingWindowInSeconds | N        | 500 ms  | [Batching behavior](invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching "invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching") |
| Queues                         | N        | N/A     | The name of the Amazon MQ broker destination queue to consume.                                                                                                         |
| SourceAccessConfigurations     | N        | N/A     | For ActiveMQ, BASIC_AUTH credentials. For RabbitMQ, can contain both BASIC_AUTH credentials and VIRTUAL_HOST information.                                              |
