# Monitor Kinesis Data Streams Agent health with Amazon CloudWatch

The agent publishes custom CloudWatch metrics with a namespace of
**AWSKinesisAgent**. These metrics help you assess whether the
agent is submitting data into Kinesis Data Streams as specified, and whether it is healthy and
consuming the appropriate amount of CPU and memory resources on the data producer.
Metrics such as the number of records and bytes sent are useful to understand the rate
at which the agent is submitting data to the stream. When these metrics fall below
expected thresholds by some percentage or drop to zero, it could indicate configuration
issues, network errors, or agent health issues. Metrics such as on-host CPU and memory
consumption and agent error counters indicate data producer resource usage, and provide
insights into potential configuration or host errors. Finally, the agent also logs
service exceptions to help investigate agent issues. These metrics are reported in the
Region specified in the agent configuration setting `cloudwatch.endpoint`.
CloudWatch metrics published from multiple Kinesis agents are aggregated or combined. For more
information about agent configuration, see [Specify the agent configuration settings](writing-with-agents.md#agent-config-settings "writing-with-agents.md#agent-config-settings").

## Monitor with CloudWatch

The Kinesis Data Streams agent sends the following metrics to CloudWatch.

| Metric               | Description                                                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BytesSent`          | The number of bytes sent to Kinesis Data Streams over the specified time<br>period.<br>Units: Bytes                                                        |
| `RecordSendAttempts` | The number of records attempted (either first time, or as a<br>retry) in a call to `PutRecords` over the specified<br>time period.<br>Units: Count         |
| `RecordSendErrors`   | The number of records that returned failure status in a call<br>to `PutRecords`, including retries, over the<br>specified time period.<br>Units: Count     |
| `ServiceErrors`      | The number of calls to `PutRecords` that resulted<br>in a service error (other than a throttling error) over the<br>specified time period.<br>Units: Count |
