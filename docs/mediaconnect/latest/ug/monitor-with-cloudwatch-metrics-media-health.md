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

| Metric                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ConnectionAttempts`      | The number of reconnection attempts. If the MediaConnect flow or<br>source loses its connection, it will attempt to reconnect<br>automatically.<br>Units: Count<br>Supported protocols:<br>• Zixi<br>• SRT<br>Supported statistics:<br>• Sum<br>Valid dimension sets:<br>• Flow ARN<br>• Source ARN<br>• Availability Zone<br>• All flows                                                                                                                                                  |
| `ConsecutiveDrops`        | The number of data packets that were dropped in a row<br>during transmission of data to or from MediaConnect.<br>Units: Count<br>Supported protocols:<br>• Zixi<br>Supported statistics:<br>• Maximum<br>• Minimum<br>• Average<br>Valid dimension sets:<br>• Flow ARN<br>• Source ARN<br>• Availability Zone<br>• All flows                                                                                                                                                               |
| `ConsecutiveNotRecovered` | The number of data packets that were not recovered in a<br>row. After a data packet is dropped, error correction<br>attempts to recover that packet. This metric helps to<br>identify extended periods of data packets that were dropped<br>and not<br>recovered.<br>Units: Count<br>Supported protocols:<br>• Zixi<br>Supported statistics:<br>• Maximum<br>• Minimum<br>• Average<br>Valid dimension sets:<br>• Flow ARN<br>• Source ARN<br>• Availability Zone<br>• All flows           |
| `SourceJitter`            | The current network jitter, measured in milliseconds.<br>Network jitter is a measurement of changes in<br>latency.<br>An increase in network jitter indicates inconsistency in the<br>latency and can negatively impact quality.<br>Units: milliseconds (ms)<br>Supported protocols:<br>• All Transport Stream (TS) protocols<br>Supported statistics:<br>• Maximum<br>• Minimum<br>• Average<br>Valid dimension sets:<br>• Flow ARN<br>• Source ARN<br>• Availability Zone<br>• All flows |
| `SourceLatency`           | The stream latency of the flow or source. Latency is the<br>time it takes for data packets to travel from your source to<br>MediaConnect.<br>Units: milliseconds (ms)<br>Supported protocols:<br>• All Transport Stream (TS) protocols<br>Supported statistics:<br>• Maximum<br>• Minimum<br>• Average<br>Valid dimension sets:<br>• Flow ARN<br>• Source ARN<br>• Availability Zone<br>• All flows                                                                                        |
| `SourceUptime`            | The number of seconds that the source has been active. If<br>the source is disconnected or has a connection timeout, this<br>metric resets to zero.<br>Units: Count<br>Supported protocols:<br>• All Transport Stream (TS) protocols<br>Supported statistics:<br>• Maximum<br>• Minimum<br>• Average<br>Valid dimension sets:<br>• Flow ARN<br>• Source ARN<br>• Availability Zone<br>• All flows                                                                                          |
