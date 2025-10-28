# Amazon EMR 7.10.0 - Flink release notes

**Amazon EMR 7.10.0 - Flink Changes**

| Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Feature | Starting with Amazon EMR version 7.10.0, you can enable Kafka and Kinesis Flink connectors more easily by using configuration settings. Add either `kafka.enabled: true` or `kinesis.enabled: true` in the `flink-conf` classification during cluster creation to automatically configure the respective connector. This streamlined approach eliminates the manual configuration steps that were previously required. |
