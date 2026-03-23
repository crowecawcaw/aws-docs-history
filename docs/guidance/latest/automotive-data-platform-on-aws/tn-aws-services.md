# AWS services used

| Service                                         | Purpose                                                                                         |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Amazon Managed Streaming for Apache Kafka (MSK) | Message bus for telemetry ingestion, normalization, and per-fleet distribution                  |
| Amazon Managed Service for Apache Flink         | Stream processing for normalization (preprocessors) and routing (EventDrivenTelemetryProcessor) |
| Amazon ElastiCache (Redis)                      | Latest vehicle state cache, signal catalog cache, fleet enrollment cache                        |
| Amazon API Gateway (WebSocket)                  | Real-time telemetry push to external consumers                                                  |
| Amazon API Gateway (REST)                       | Fleet Management API with Cognito authorization                                                 |
| Amazon ECS (Fargate)                            | OEM streaming connectors and WebSocket fanout consumer                                          |
| Amazon DynamoDB                                 | Signal catalog, fleet enrollment, vehicles, trips, WebSocket connections                        |
| Amazon S3                                       | Transform manifests, Iceberg data lake                                                          |
| Apache Iceberg (via AWS Glue)                   | Historical telemetry tables partitioned by fleet                                                |
| Amazon Athena                                   | SQL analytics over normalized telemetry                                                         |
| AWS Lake Formation                              | Row-level security by fleet on Iceberg tables                                                   |
| Amazon Cognito                                  | User authentication with group-based access control                                             |
| AWS IoT Core                                    | MQTT broker for direct vehicle connections and FleetWise Edge                                   |
| AWS Lambda                                      | API handlers, OEM polling connectors, command processing                                        |
