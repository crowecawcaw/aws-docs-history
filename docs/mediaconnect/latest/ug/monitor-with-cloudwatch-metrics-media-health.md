# AWS Elemental MediaConnect

metrics to monitor media health

AWS Elemental MediaConnect sends metrics to CloudWatch. You can review specific metrics to
evaluate the health of the media transmitted by MediaConnect. The media health metrics
listed below only apply to Transport Stream (TS) flows. For details about each
metric, see the table in this section.

## Media metrics

The following table lists media metrics that AWS Elemental MediaConnect sends to
CloudWatch.

###### Note

All source-level and output-level metrics are also posted at the flow
level. This allows you to query these metrics using the Flow ARN, Source
ARN, or Output ARN dimensions as appropriate.

| Metric                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ConnectionAttempts`      | The number of reconnection attempts. If the MediaConnect flow or source loses its connection, it will attempt to reconnect automatically. Units: Count Supported protocols: <br>• Zixi <br>• SRT listener <br>• SRT caller Supported statistics: <br>• Sum Valid dimension sets: <br>• Flow ARN <br>• Source ARN <br>• Availability Zone <br>• All flows                                                                                                                   |
| `ConsecutiveDrops`        | The number of data packets that were dropped in a row during transmission of data to or from MediaConnect. Units: Count Supported protocols: <br>• Zixi Supported statistics: <br>• Maximum <br>• Minimum <br>• Average Valid dimension sets: <br>• Flow ARN <br>• Source ARN <br>• Availability Zone <br>• All flows                                                                                                                                                      |
| `ConsecutiveNotRecovered` | The number of data packets that were not recovered in a row. After a data packet is dropped, error correction attempts to recover that packet. This metric helps to identify extended periods of data packets that were dropped and not recovered. Units: Count Supported protocols: <br>• Zixi Supported statistics: <br>• Maximum <br>• Minimum <br>• Average Valid dimension sets: <br>• Flow ARN <br>• Source ARN <br>• Availability Zone <br>• All flows              |
| `SourceJitter`            | The current network jitter, measured in milliseconds. Network jitter is a measurement of changes in latency. An increase in network jitter indicates inconsistency in the latency and can negatively impact quality. Units: milliseconds (ms) Supported protocols: <br>• All Transport Stream (TS) protocols Supported statistics: <br>• Maximum <br>• Minimum <br>• Average Valid dimension sets: <br>• Flow ARN <br>• Source ARN <br>• Availability Zone <br>• All flows |
| `SourceLatency`           | The stream latency of the flow or source. Latency is the time it takes for data packets to travel from your source to MediaConnect. Units: milliseconds (ms) Supported protocols: <br>• All Transport Stream (TS) protocols Supported statistics: <br>• Maximum <br>• Minimum <br>• Average Valid dimension sets: <br>• Flow ARN <br>• Source ARN <br>• Availability Zone <br>• All flows                                                                                  |
| `SourceUptime`            | The number of seconds that the source has been active. If the source is disconnected or has a connection timeout, this metric resets to zero. Units: Count Supported protocols: <br>• All Transport Stream (TS) protocols Supported statistics: <br>• Maximum <br>• Minimum <br>• Average Valid dimension sets: <br>• Flow ARN <br>• Source ARN <br>• Availability Zone <br>• All flows                                                                                    |
