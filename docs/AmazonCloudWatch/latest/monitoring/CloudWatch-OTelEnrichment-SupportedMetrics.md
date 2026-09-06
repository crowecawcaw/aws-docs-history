# Supported AWS resources and metrics for OpenTelemetry enrichment

When you enable OTel enrichment, CloudWatch republishes selected metrics from the following AWS services as OpenTelemetry time series. Each CloudWatch namespace maps to an OpenTelemetry instrumentation scope named `cloudwatch.aws/`service`` — for example, the `AWS/EC2` namespace maps to the scope `cloudwatch.aws/ec2`. All enriched instruments use Delta temporality.

Depending on the resource, enriched metrics can also carry the following resource context:

- `cloud.resource_id` — the resource ARN, added when the metric can be resolved to a specific resource.
- `tag.*` — the resource's AWS tags, added when the resource is supported for [Using resource tags for telemetry](UsingResourceTagsForTelemetry.md "UsingResourceTagsForTelemetry.md").
  The following tables list, per namespace, the supported resources and their enriched metrics. For each metric, the OpenTelemetry metric name matches the CloudWatch metric name unless a rewritten name is shown, and the instrument type is either `Sum` or `Histogram`. The metric's CloudWatch dimensions are emitted verbatim as OpenTelemetry data point attributes (the attribute key is the dimension name); the _Data point attributes_ column lists the dimension sets each metric is published with.

###### Topics

- [AWS/AIDevOps](#otel-enrichment-ns-aws-aidevops "#otel-enrichment-ns-aws-aidevops")
- [AWS/AOSS](#otel-enrichment-ns-aws-aoss "#otel-enrichment-ns-aws-aoss")
- [AWS/ApiGateway](#otel-enrichment-ns-aws-apigateway "#otel-enrichment-ns-aws-apigateway")
- [AWS/AppFlow](#otel-enrichment-ns-aws-appflow "#otel-enrichment-ns-aws-appflow")
- [AWS/AppStream](#otel-enrichment-ns-aws-appstream "#otel-enrichment-ns-aws-appstream")
- [AWS/AppSync](#otel-enrichment-ns-aws-appsync "#otel-enrichment-ns-aws-appsync")
- [AWS/ApplicationELB](#otel-enrichment-ns-aws-applicationelb "#otel-enrichment-ns-aws-applicationelb")
- [AWS/Athena](#otel-enrichment-ns-aws-athena "#otel-enrichment-ns-aws-athena")
- [AWS/AutoScaling](#otel-enrichment-ns-aws-autoscaling "#otel-enrichment-ns-aws-autoscaling")
- [AWS/Backup](#otel-enrichment-ns-aws-backup "#otel-enrichment-ns-aws-backup")
- [AWS/Bedrock](#otel-enrichment-ns-aws-bedrock "#otel-enrichment-ns-aws-bedrock")
- [AWS/BedrockMantle](#otel-enrichment-ns-aws-bedrockmantle "#otel-enrichment-ns-aws-bedrockmantle")
- [AWS/ClientVPN](#otel-enrichment-ns-aws-clientvpn "#otel-enrichment-ns-aws-clientvpn")
- [AWS/CloudFront](#otel-enrichment-ns-aws-cloudfront "#otel-enrichment-ns-aws-cloudfront")
- [AWS/CloudWatch/MetricStreams](#otel-enrichment-ns-aws-cloudwatch-metricstreams "#otel-enrichment-ns-aws-cloudwatch-metricstreams")
- [AWS/CodeGuruProfiler](#otel-enrichment-ns-aws-codeguruprofiler "#otel-enrichment-ns-aws-codeguruprofiler")
- [AWS/Cognito](#otel-enrichment-ns-aws-cognito "#otel-enrichment-ns-aws-cognito")
- [AWS/Connect](#otel-enrichment-ns-aws-connect "#otel-enrichment-ns-aws-connect")
- [AWS/DAX](#otel-enrichment-ns-aws-dax "#otel-enrichment-ns-aws-dax")
- [AWS/DX](#otel-enrichment-ns-aws-dx "#otel-enrichment-ns-aws-dx")
- [AWS/DataSync](#otel-enrichment-ns-aws-datasync "#otel-enrichment-ns-aws-datasync")
- [AWS/DocDB](#otel-enrichment-ns-aws-docdb "#otel-enrichment-ns-aws-docdb")
- [AWS/DocDB-Elastic](#otel-enrichment-ns-aws-docdb-elastic "#otel-enrichment-ns-aws-docdb-elastic")
- [AWS/DynamoDB](#otel-enrichment-ns-aws-dynamodb "#otel-enrichment-ns-aws-dynamodb")
- [AWS/EBS](#otel-enrichment-ns-aws-ebs "#otel-enrichment-ns-aws-ebs")
- [AWS/EC2](#otel-enrichment-ns-aws-ec2 "#otel-enrichment-ns-aws-ec2")
- [AWS/EC2CapacityReservations](#otel-enrichment-ns-aws-ec2capacityreservations "#otel-enrichment-ns-aws-ec2capacityreservations")
- [AWS/EFS](#otel-enrichment-ns-aws-efs "#otel-enrichment-ns-aws-efs")
- [AWS/EKS](#otel-enrichment-ns-aws-eks "#otel-enrichment-ns-aws-eks")
- [AWS/ELB](#otel-enrichment-ns-aws-elb "#otel-enrichment-ns-aws-elb")
- [AWS/EMRServerless](#otel-enrichment-ns-aws-emrserverless "#otel-enrichment-ns-aws-emrserverless")
- [AWS/ES](#otel-enrichment-ns-aws-es "#otel-enrichment-ns-aws-es")
- [AWS/ElastiCache](#otel-enrichment-ns-aws-elasticache "#otel-enrichment-ns-aws-elasticache")
- [AWS/ElasticBeanstalk](#otel-enrichment-ns-aws-elasticbeanstalk "#otel-enrichment-ns-aws-elasticbeanstalk")
- [AWS/ElasticMapReduce](#otel-enrichment-ns-aws-elasticmapreduce "#otel-enrichment-ns-aws-elasticmapreduce")
- [AWS/EventBridge/Pipes](#otel-enrichment-ns-aws-eventbridge-pipes "#otel-enrichment-ns-aws-eventbridge-pipes")
- [AWS/Events](#otel-enrichment-ns-aws-events "#otel-enrichment-ns-aws-events")
- [AWS/FSx](#otel-enrichment-ns-aws-fsx "#otel-enrichment-ns-aws-fsx")
- [AWS/Firehose](#otel-enrichment-ns-aws-firehose "#otel-enrichment-ns-aws-firehose")
- [AWS/FraudDetector](#otel-enrichment-ns-aws-frauddetector "#otel-enrichment-ns-aws-frauddetector")
- [AWS/GameLift](#otel-enrichment-ns-aws-gamelift "#otel-enrichment-ns-aws-gamelift")
- [AWS/GatewayELB](#otel-enrichment-ns-aws-gatewayelb "#otel-enrichment-ns-aws-gatewayelb")
- [AWS/IVSChat](#otel-enrichment-ns-aws-ivschat "#otel-enrichment-ns-aws-ivschat")
- [AWS/IoT](#otel-enrichment-ns-aws-iot "#otel-enrichment-ns-aws-iot")
- [AWS/KMS](#otel-enrichment-ns-aws-kms "#otel-enrichment-ns-aws-kms")
- [AWS/Kafka](#otel-enrichment-ns-aws-kafka "#otel-enrichment-ns-aws-kafka")
- [AWS/Kendra](#otel-enrichment-ns-aws-kendra "#otel-enrichment-ns-aws-kendra")
- [AWS/Kinesis](#otel-enrichment-ns-aws-kinesis "#otel-enrichment-ns-aws-kinesis")
- [AWS/KinesisAnalytics](#otel-enrichment-ns-aws-kinesisanalytics "#otel-enrichment-ns-aws-kinesisanalytics")
- [AWS/Lambda](#otel-enrichment-ns-aws-lambda "#otel-enrichment-ns-aws-lambda")
- [AWS/M2](#otel-enrichment-ns-aws-m2 "#otel-enrichment-ns-aws-m2")
- [AWS/MWAA](#otel-enrichment-ns-aws-mwaa "#otel-enrichment-ns-aws-mwaa")
- [AWS/MediaTailor](#otel-enrichment-ns-aws-mediatailor "#otel-enrichment-ns-aws-mediatailor")
- [AWS/MemoryDB](#otel-enrichment-ns-aws-memorydb "#otel-enrichment-ns-aws-memorydb")
- [AWS/NATGateway](#otel-enrichment-ns-aws-natgateway "#otel-enrichment-ns-aws-natgateway")
- [AWS/NetworkELB](#otel-enrichment-ns-aws-networkelb "#otel-enrichment-ns-aws-networkelb")
- [AWS/NetworkFirewall](#otel-enrichment-ns-aws-networkfirewall "#otel-enrichment-ns-aws-networkfirewall")
- [AWS/Pinpoint](#otel-enrichment-ns-aws-pinpoint "#otel-enrichment-ns-aws-pinpoint")
- [AWS/Prometheus](#otel-enrichment-ns-aws-prometheus "#otel-enrichment-ns-aws-prometheus")
- [AWS/RDS](#otel-enrichment-ns-aws-rds "#otel-enrichment-ns-aws-rds")
- [AWS/RUM](#otel-enrichment-ns-aws-rum "#otel-enrichment-ns-aws-rum")
- [AWS/Redshift](#otel-enrichment-ns-aws-redshift "#otel-enrichment-ns-aws-redshift")
- [AWS/Redshift-Serverless](#otel-enrichment-ns-aws-redshift-serverless "#otel-enrichment-ns-aws-redshift-serverless")
- [AWS/Route53](#otel-enrichment-ns-aws-route53 "#otel-enrichment-ns-aws-route53")
- [AWS/Route53Resolver](#otel-enrichment-ns-aws-route53resolver "#otel-enrichment-ns-aws-route53resolver")
- [AWS/S3](#otel-enrichment-ns-aws-s3 "#otel-enrichment-ns-aws-s3")
- [AWS/SNS](#otel-enrichment-ns-aws-sns "#otel-enrichment-ns-aws-sns")
- [AWS/SQS](#otel-enrichment-ns-aws-sqs "#otel-enrichment-ns-aws-sqs")
- [AWS/SageMaker](#otel-enrichment-ns-aws-sagemaker "#otel-enrichment-ns-aws-sagemaker")
- [AWS/Scheduler](#otel-enrichment-ns-aws-scheduler "#otel-enrichment-ns-aws-scheduler")
- [AWS/Transfer](#otel-enrichment-ns-aws-transfer "#otel-enrichment-ns-aws-transfer")
- [AWS/TransitGateway](#otel-enrichment-ns-aws-transitgateway "#otel-enrichment-ns-aws-transitgateway")
- [AWS/VPN](#otel-enrichment-ns-aws-vpn "#otel-enrichment-ns-aws-vpn")
- [AWS/VpcLattice](#otel-enrichment-ns-aws-vpclattice "#otel-enrichment-ns-aws-vpclattice")
- [AWS/WorkSpaces](#otel-enrichment-ns-aws-workspaces "#otel-enrichment-ns-aws-workspaces")

## AWS/AIDevOps

The `AWS/AIDevOps` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/aidevops`. All enriched instruments use Delta temporality.

- [AWS::DevOpsAgent::AgentSpace](#otel-enrichment-aws-aidevops-aws-devopsagent-agentspace "#otel-enrichment-aws-aidevops-aws-devopsagent-agentspace")

### AWS::DevOpsAgent::AgentSpace

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                               | OpenTelemetry metric                 | Instrument type | Data point attributes |
| ------------------------------------ | ------------------------------------ | --------------- | --------------------- |
| `ConsumedChatRequests`               | `ConsumedChatRequests`               | Sum             | `AgentSpaceUUID`      |
| `ConsumedEvaluationTime`             | `ConsumedEvaluationTime`             | Histogram       | `AgentSpaceUUID`      |
| `ConsumedInvestigationTime`          | `ConsumedInvestigationTime`          | Histogram       | `AgentSpaceUUID`      |
| `ConsumedOnDemandTime`               | `ConsumedOnDemandTime`               | Histogram       | `AgentSpaceUUID`      |
| `ConsumedReleaseAPITestingTime`      | `ConsumedReleaseAPITestingTime`      | Histogram       | `AgentSpaceUUID`      |
| `ConsumedReleaseReadinessReviewTime` | `ConsumedReleaseReadinessReviewTime` | Histogram       | `AgentSpaceUUID`      |
| `ConsumedReleaseShepherdTime`        | `ConsumedReleaseShepherdTime`        | Histogram       | `AgentSpaceUUID`      |
| `ConsumedReleaseUITestingTime`       | `ConsumedReleaseUITestingTime`       | Histogram       | `AgentSpaceUUID`      |
| `TopologyCompletionCount`            | `TopologyCompletionCount`            | Sum             | `AgentSpaceUUID`      |

## AWS/AOSS

The `AWS/AOSS` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/aoss`. All enriched instruments use Delta temporality.

- [AWS::OpenSearchServerless::Collection](#otel-enrichment-aws-aoss-aws-opensearchserverless-collection "#otel-enrichment-aws-aoss-aws-opensearchserverless-collection")
- [AWS::OpenSearchServerless::CollectionGroup](#otel-enrichment-aws-aoss-aws-opensearchserverless-collectiongroup "#otel-enrichment-aws-aoss-aws-opensearchserverless-collectiongroup")

### AWS::OpenSearchServerless::Collection

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                            | OpenTelemetry metric              | Instrument type | Data point attributes                        |
| --------------------------------- | --------------------------------- | --------------- | -------------------------------------------- |
| `2xx`                             | `2xx`                             | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `3xx`                             | `3xx`                             | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `4xx`                             | `4xx`                             | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `5xx`                             | `5xx`                             | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `ActiveCollection`                | `ActiveCollection`                | Histogram       | `ClientId`, `CollectionId`, `CollectionName` |
| `ActiveCollection-Shadow`         | `ActiveCollection-Shadow`         | Histogram       | `ClientId`, `CollectionId`, `CollectionName` |
| `AutoOptimizeJob`                 | `AutoOptimizeJob`                 | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `IngestionDataRate-Shadow`        | `IngestionDataRate-Shadow`        | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `IngestionDocumentErrors-Shadow`  | `IngestionDocumentErrors-Shadow`  | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `IngestionDocumentRate-Shadow`    | `IngestionDocumentRate-Shadow`    | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `IngestionRequestErrors`          | `IngestionRequestErrors`          | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `IngestionRequestErrors-Shadow`   | `IngestionRequestErrors-Shadow`   | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `IngestionRequestLatency`         | `IngestionRequestLatency`         | Histogram       | `ClientId`, `CollectionId`, `CollectionName` |
| `IngestionRequestRate`            | `IngestionRequestRate`            | Histogram       | `ClientId`, `CollectionId`, `CollectionName` |
| `IngestionRequestRate-Shadow`     | `IngestionRequestRate-Shadow`     | Histogram       | `ClientId`, `CollectionId`, `CollectionName` |
| `IngestionRequestSuccess`         | `IngestionRequestSuccess`         | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `IngestionRequestSuccess-Shadow`  | `IngestionRequestSuccess-Shadow`  | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `KNNRemoteIndexBuildFailureCount` | `KNNRemoteIndexBuildFailureCount` | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `KNNRemoteIndexBuildSuccessCount` | `KNNRemoteIndexBuildSuccessCount` | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `KNNRemoteIndexBuildTime`         | `KNNRemoteIndexBuildTime`         | Histogram       | `ClientId`, `CollectionId`, `CollectionName` |
| `SearchRequestErrors-Shadow`      | `SearchRequestErrors-Shadow`      | Sum             | `ClientId`, `CollectionId`, `CollectionName` |
| `SearchRequestLatency`            | `SearchRequestLatency`            | Histogram       | `ClientId`, `CollectionId`, `CollectionName` |
| `SearchRequestRate`               | `SearchRequestRate`               | Histogram       | `ClientId`, `CollectionId`, `CollectionName` |
| `SearchRequestRate-Shadow`        | `SearchRequestRate-Shadow`        | Histogram       | `ClientId`, `CollectionId`, `CollectionName` |
| `SemanticSearchOCU`               | `SemanticSearchOCU`               | Histogram       | `ClientId`, `CollectionId`, `CollectionName` |

### AWS::OpenSearchServerless::CollectionGroup

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric        | OpenTelemetry metric | Instrument type | Data point attributes                                  |
| ------------- | -------------------- | --------------- | ------------------------------------------------------ |
| `IndexingOCU` | `IndexingOCU`        | Histogram       | `ClientId`, `CollectionGroupId`, `CollectionGroupName` |
| `SearchOCU`   | `SearchOCU`          | Histogram       | `ClientId`, `CollectionGroupId`, `CollectionGroupName` |

## AWS/ApiGateway

The `AWS/ApiGateway` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/apigateway`. All enriched instruments use Delta temporality.

- [AWS::ApiGateway::Stage](#otel-enrichment-aws-apigateway-aws-apigateway-stage "#otel-enrichment-aws-apigateway-aws-apigateway-stage")
- [stage](#otel-enrichment-aws-apigateway-stage "#otel-enrichment-aws-apigateway-stage")

### AWS::ApiGateway::Stage

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric               | OpenTelemetry metric         | Instrument type | Data point attributes                    |
| -------------------- | ---------------------------- | --------------- | ---------------------------------------- |
| `4XXError`           | `4XXError`                   | Sum             | `ApiName`, `Stage`                       |
| `4XXError`           | `4XXErrorByMethod`           | Sum             | `ApiName`, `Method`, `Resource`, `Stage` |
| `5XXError`           | `5XXError`                   | Sum             | `ApiName`, `Stage`                       |
| `5XXError`           | `5XXErrorByMethod`           | Sum             | `ApiName`, `Method`, `Resource`, `Stage` |
| `CacheHitCount`      | `CacheHitCount`              | Sum             | `ApiName`, `Stage`                       |
| `CacheHitCount`      | `CacheHitCountByMethod`      | Sum             | `ApiName`, `Method`, `Resource`, `Stage` |
| `CacheMissCount`     | `CacheMissCount`             | Sum             | `ApiName`, `Stage`                       |
| `CacheMissCount`     | `CacheMissCountByMethod`     | Sum             | `ApiName`, `Method`, `Resource`, `Stage` |
| `Count`              | `Count`                      | Sum             | `ApiName`, `Stage`                       |
| `Count`              | `CountByMethod`              | Sum             | `ApiName`, `Method`, `Resource`, `Stage` |
| `IntegrationLatency` | `IntegrationLatency`         | Histogram       | `ApiName`, `Stage`                       |
| `IntegrationLatency` | `IntegrationLatencyByMethod` | Histogram       | `ApiName`, `Method`, `Resource`, `Stage` |
| `Latency`            | `Latency`                    | Histogram       | `ApiName`, `Stage`                       |
| `Latency`            | `LatencyByMethod`            | Histogram       | `ApiName`, `Method`, `Resource`, `Stage` |

### `stage`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric               | OpenTelemetry metric | Instrument type | Data point attributes |
| -------------------- | -------------------- | --------------- | --------------------- |
| `4xx`                | `4xx`                | Sum             | `ApiId`, `Stage`      |
| `5xx`                | `5xx`                | Sum             | `ApiId`, `Stage`      |
| `ClientError`        | `ClientError`        | Sum             | `ApiId`, `Stage`      |
| `ConnectCount`       | `ConnectCount`       | Sum             | `ApiId`, `Stage`      |
| `Count`              | `Count`              | Sum             | `ApiId`, `Stage`      |
| `DataProcessed`      | `DataProcessed`      | Histogram       | `ApiId`, `Stage`      |
| `ExecutionError`     | `ExecutionError`     | Sum             | `ApiId`, `Stage`      |
| `IntegrationError`   | `IntegrationError`   | Sum             | `ApiId`, `Stage`      |
| `IntegrationLatency` | `IntegrationLatency` | Histogram       | `ApiId`, `Stage`      |
| `Latency`            | `Latency`            | Histogram       | `ApiId`, `Stage`      |
| `MessageCount`       | `MessageCount`       | Sum             | `ApiId`, `Stage`      |

## AWS/AppFlow

The `AWS/AppFlow` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/appflow`. All enriched instruments use Delta temporality.

- [AWS::AppFlow::Flow](#otel-enrichment-aws-appflow-aws-appflow-flow "#otel-enrichment-aws-appflow-aws-appflow-flow")

### AWS::AppFlow::Flow

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                          | OpenTelemetry metric            | Instrument type | Data point attributes |
| ------------------------------- | ------------------------------- | --------------- | --------------------- |
| `FlowExecutionRecordsProcessed` | `FlowExecutionRecordsProcessed` | Sum             | `FlowName`            |
| `FlowExecutionTime`             | `FlowExecutionTime`             | Histogram       | `FlowName`            |
| `FlowExecutionsFailed`          | `FlowExecutionsFailed`          | Sum             | `FlowName`            |
| `FlowExecutionsStarted`         | `FlowExecutionsStarted`         | Sum             | `FlowName`            |
| `FlowExecutionsSucceeded`       | `FlowExecutionsSucceeded`       | Sum             | `FlowName`            |

## AWS/AppStream

The `AWS/AppStream` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/appstream`. All enriched instruments use Delta temporality.

- [fleet](#otel-enrichment-aws-appstream-fleet "#otel-enrichment-aws-appstream-fleet")

### `fleet`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                              | OpenTelemetry metric                | Instrument type | Data point attributes |
| ----------------------------------- | ----------------------------------- | --------------- | --------------------- |
| `ActiveUserSessionCapacity`         | `ActiveUserSessionCapacity`         | Histogram       | `Fleet`               |
| `ActualCapacity`                    | `ActualCapacity`                    | Histogram       | `Fleet`               |
| `ActualUserSessionCapacity`         | `ActualUserSessionCapacity`         | Histogram       | `Fleet`               |
| `AvailableCapacity`                 | `AvailableCapacity`                 | Histogram       | `Fleet`               |
| `AvailableUserSessionCapacity`      | `AvailableUserSessionCapacity`      | Histogram       | `Fleet`               |
| `CapacityUtilization`               | `CapacityUtilization`               | Histogram       | `Fleet`               |
| `DesiredCapacity`                   | `DesiredCapacity`                   | Histogram       | `Fleet`               |
| `DesiredUserSessionCapacity`        | `DesiredUserSessionCapacity`        | Histogram       | `Fleet`               |
| `InUseCapacity`                     | `InUseCapacity`                     | Histogram       | `Fleet`               |
| `InsufficientCapacityError`         | `InsufficientCapacityError`         | Sum             | `Fleet`               |
| `InsufficientConcurrencyLimitError` | `InsufficientConcurrencyLimitError` | Sum             | `Fleet`               |
| `PendingCapacity`                   | `PendingCapacity`                   | Histogram       | `Fleet`               |
| `PendingUserSessionCapacity`        | `PendingUserSessionCapacity`        | Histogram       | `Fleet`               |
| `ReservedCapacity`                  | `ReservedCapacity`                  | Histogram       | `Fleet`               |
| `RunningCapacity`                   | `RunningCapacity`                   | Histogram       | `Fleet`               |
| `RunningUserSessionCapacity`        | `RunningUserSessionCapacity`        | Histogram       | `Fleet`               |

## AWS/AppSync

The `AWS/AppSync` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/appsync`. All enriched instruments use Delta temporality.

- [AWS::AppSync::GraphQLApi](#otel-enrichment-aws-appsync-aws-appsync-graphqlapi "#otel-enrichment-aws-appsync-aws-appsync-graphqlapi")

### AWS::AppSync::GraphQLApi

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                          | OpenTelemetry metric            | Instrument type | Data point attributes      |
| ------------------------------- | ------------------------------- | --------------- | -------------------------- |
| `4XXError`                      | `4XXError`                      | Sum             | `GraphQLAPIId`             |
| `5XXError`                      | `5XXError`                      | Sum             | `GraphQLAPIId`             |
| `ActiveConnections`             | `ActiveConnections`             | Histogram       | `GraphQLAPIId`             |
| `ActiveSubscriptions`           | `ActiveSubscriptions`           | Histogram       | `GraphQLAPIId`             |
| `CacheHit`                      | `CacheHit`                      | Sum             | `GraphQLAPIId`, `Resolver` |
| `CacheMiss`                     | `CacheMiss`                     | Sum             | `GraphQLAPIId`, `Resolver` |
| `ConnectClientError`            | `ConnectClientError`            | Sum             | `GraphQLAPIId`             |
| `ConnectRequests`               | `ConnectRequests`               | Sum             | `GraphQLAPIId`             |
| `ConnectServerError`            | `ConnectServerError`            | Sum             | `GraphQLAPIId`             |
| `ConnectSuccess`                | `ConnectSuccess`                | Sum             | `GraphQLAPIId`             |
| `ConnectionDuration`            | `ConnectionDuration`            | Histogram       | `GraphQLAPIId`             |
| `DisconnectClientError`         | `DisconnectClientError`         | Sum             | `GraphQLAPIId`             |
| `DisconnectServerError`         | `DisconnectServerError`         | Sum             | `GraphQLAPIId`             |
| `DisconnectSuccess`             | `DisconnectSuccess`             | Sum             | `GraphQLAPIId`             |
| `InboundMessageDelayed`         | `InboundMessageDelayed`         | Sum             | `GraphQLAPIId`             |
| `InboundMessageDropped`         | `InboundMessageDropped`         | Sum             | `GraphQLAPIId`             |
| `InboundMessageError`           | `InboundMessageError`           | Sum             | `GraphQLAPIId`             |
| `InboundMessageFailure`         | `InboundMessageFailure`         | Sum             | `GraphQLAPIId`             |
| `InboundMessageSuccess`         | `InboundMessageSuccess`         | Sum             | `GraphQLAPIId`             |
| `InvalidationRequestDropped`    | `InvalidationRequestDropped`    | Sum             | `GraphQLAPIId`             |
| `InvalidationRequestError`      | `InvalidationRequestError`      | Sum             | `GraphQLAPIId`             |
| `InvalidationRequestFailure`    | `InvalidationRequestFailure`    | Sum             | `GraphQLAPIId`             |
| `InvalidationRequestSuccess`    | `InvalidationRequestSuccess`    | Sum             | `GraphQLAPIId`             |
| `InvalidationSuccess`           | `InvalidationSuccess`           | Sum             | `GraphQLAPIId`             |
| `OutboundMessages`              | `OutboundMessages`              | Sum             | `GraphQLAPIId`             |
| `PublishDataMessageClientError` | `PublishDataMessageClientError` | Sum             | `GraphQLAPIId`             |
| `PublishDataMessageServerError` | `PublishDataMessageServerError` | Sum             | `GraphQLAPIId`             |
| `PublishDataMessageSize`        | `PublishDataMessageSize`        | Histogram       | `GraphQLAPIId`             |
| `PublishDataMessageSuccess`     | `PublishDataMessageSuccess`     | Sum             | `GraphQLAPIId`             |
| `SubscribeClientError`          | `SubscribeClientError`          | Sum             | `GraphQLAPIId`             |
| `SubscribeServerError`          | `SubscribeServerError`          | Sum             | `GraphQLAPIId`             |
| `SubscribeSuccess`              | `SubscribeSuccess`              | Sum             | `GraphQLAPIId`             |
| `UnsubscribeClientError`        | `UnsubscribeClientError`        | Sum             | `GraphQLAPIId`             |
| `UnsubscribeServerError`        | `UnsubscribeServerError`        | Sum             | `GraphQLAPIId`             |
| `UnsubscribeSuccess`            | `UnsubscribeSuccess`            | Sum             | `GraphQLAPIId`             |

## AWS/ApplicationELB

The `AWS/ApplicationELB` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/elasticloadbalancing`. All enriched instruments use Delta temporality.

- [AWS::ElasticLoadBalancingV2::LoadBalancer](#otel-enrichment-aws-applicationelb-aws-elasticloadbalancingv2-loadbalancer "#otel-enrichment-aws-applicationelb-aws-elasticloadbalancingv2-loadbalancer")
- [AWS::ElasticLoadBalancingV2::TargetGroup](#otel-enrichment-aws-applicationelb-aws-elasticloadbalancingv2-targetgroup "#otel-enrichment-aws-applicationelb-aws-elasticloadbalancingv2-targetgroup")

### AWS::ElasticLoadBalancingV2::LoadBalancer

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                            | OpenTelemetry metric                              | Instrument type | Data point attributes                             |
| ------------------------------------------------- | ------------------------------------------------- | --------------- | ------------------------------------------------- |
| `ActiveConnectionCount`                           | `ActiveConnectionCount`                           | Histogram       | `AvailabilityZone`, `LoadBalancer`                |
| `ActiveZonalShiftHostCount`                       | `ActiveZonalShiftHostCount`                       | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `AnomalousHostCount`                              | `AnomalousHostCount`                              | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `AppCookieNonStickinessCount`                     | `AppCookieNonStickinessCount`                     | Sum             | `LoadBalancer`                                    |
| `ClientTLSNegotiationErrorCount`                  | `ClientTLSNegotiationErrorCount`                  | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ConsumedLCUs`                                    | `ConsumedLCUs`                                    | Histogram       | `LoadBalancer`                                    |
| `DesyncMitigationMode_NonCompliant_Request_Count` | `DesyncMitigationMode_NonCompliant_Request_Count` | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `DroppedInvalidHeaderRequestCount`                | `DroppedInvalidHeaderRequestCount`                | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ELBAuthError`                                    | `ELBAuthError`                                    | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ELBAuthFailure`                                  | `ELBAuthFailure`                                  | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ELBAuthLatency`                                  | `ELBAuthLatency`                                  | Histogram       | `AvailabilityZone`, `LoadBalancer`                |
| `ELBAuthRefreshTokenSuccess`                      | `ELBAuthRefreshTokenSuccess`                      | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ELBAuthSuccess`                                  | `ELBAuthSuccess`                                  | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ELBAuthUserClaimsSizeExceeded`                   | `ELBAuthUserClaimsSizeExceeded`                   | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ExcessiveLowReputationPackets`                   | `ExcessiveLowReputationPackets`                   | Sum             | `LoadBalancer`                                    |
| `ForwardedInvalidHeaderRequestCount`              | `ForwardedInvalidHeaderRequestCount`              | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `GrpcRequestCount`                                | `GrpcRequestCount`                                | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `HTTPCode_ELB_3XX_Count`                          | `HTTPCode_ELB_3XX_Count`                          | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `HTTPCode_ELB_4XX_Count`                          | `HTTPCode_ELB_4XX_Count`                          | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `HTTPCode_ELB_500_Count`                          | `HTTPCode_ELB_500_Count`                          | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `HTTPCode_ELB_502_Count`                          | `HTTPCode_ELB_502_Count`                          | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `HTTPCode_ELB_503_Count`                          | `HTTPCode_ELB_503_Count`                          | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `HTTPCode_ELB_504_Count`                          | `HTTPCode_ELB_504_Count`                          | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `HTTPCode_ELB_5XX_Count`                          | `HTTPCode_ELB_5XX_Count`                          | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `HTTPCode_Target_2XX_Count`                       | `HTTPCode_Target_2XX_Count`                       | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `HTTPCode_Target_3XX_Count`                       | `HTTPCode_Target_3XX_Count`                       | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `HTTPCode_Target_4XX_Count`                       | `HTTPCode_Target_4XX_Count`                       | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `HTTPCode_Target_5XX_Count`                       | `HTTPCode_Target_5XX_Count`                       | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `HTTP_Fixed_Response_Count`                       | `HTTP_Fixed_Response_Count`                       | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `HTTP_Redirect_Count`                             | `HTTP_Redirect_Count`                             | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `HTTP_Redirect_Url_Limit_Exceeded_Count`          | `HTTP_Redirect_Url_Limit_Exceeded_Count`          | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `HealthyHostCount`                                | `HealthyHostCount`                                | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `HealthyStateDNS`                                 | `HealthyStateDNS`                                 | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `HealthyStateRouting`                             | `HealthyStateRouting`                             | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `IPv6ProcessedBytes`                              | `IPv6ProcessedBytes`                              | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `IPv6RequestCount`                                | `IPv6RequestCount`                                | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `LambdaTargetProcessedBytes`                      | `LambdaTargetProcessedBytes`                      | Sum             | `LoadBalancer`                                    |
| `LowReputationPacketsDropped`                     | `LowReputationPacketsDropped`                     | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `LowReputationRequestsDenied`                     | `LowReputationRequestsDenied`                     | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `MitigatedHostCount`                              | `MitigatedHostCount`                              | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `NewConnectionCount`                              | `NewConnectionCount`                              | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `NonStickyRequestCount`                           | `NonStickyRequestCount`                           | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `PeakLCUs`                                        | `PeakLCUs`                                        | Histogram       | `LoadBalancer`                                    |
| `ProcessedBytes`                                  | `ProcessedBytes`                                  | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `RejectedConnectionCount`                         | `RejectedConnectionCount`                         | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `RequestCount`                                    | `RequestCount`                                    | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `RequestCountPerTarget`                           | `RequestCountPerTarget`                           | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `ReservedLCUs`                                    | `ReservedLCUs`                                    | Histogram       | `LoadBalancer`                                    |
| `RuleEvaluations`                                 | `RuleEvaluations`                                 | Sum             | `LoadBalancer`                                    |
| `TargetConnectionErrorCount`                      | `TargetConnectionErrorCount`                      | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `TargetControlActiveChannelCount`                 | `TargetControlActiveChannelCount`                 | Histogram       | `AvailabilityZone`, `LoadBalancer`                |
| `TargetControlChannelErrorCount`                  | `TargetControlChannelErrorCount`                  | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `TargetControlNewChannelCount`                    | `TargetControlNewChannelCount`                    | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `TargetControlProcessedBytes`                     | `TargetControlProcessedBytes`                     | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `TargetControlRequestCount`                       | `TargetControlRequestCount`                       | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `TargetControlRequestRejectCount`                 | `TargetControlRequestRejectCount`                 | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `TargetControlWorkQueueLength`                    | `TargetControlWorkQueueLength`                    | Histogram       | `AvailabilityZone`, `LoadBalancer`                |
| `TargetResponseTime`                              | `TargetResponseTime`                              | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `TargetTLSNegotiationErrorCount`                  | `TargetTLSNegotiationErrorCount`                  | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `UnHealthyHostCount`                              | `UnHealthyHostCount`                              | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `UnhealthyRoutingRequestCount`                    | `UnhealthyRoutingRequestCount`                    | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `UnhealthyStateDNS`                               | `UnhealthyStateDNS`                               | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `UnhealthyStateRouting`                           | `UnhealthyStateRouting`                           | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |

### AWS::ElasticLoadBalancingV2::TargetGroup

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                | OpenTelemetry metric  | Instrument type | Data point attributes |
| --------------------- | --------------------- | --------------- | --------------------- |
| `LambdaInternalError` | `LambdaInternalError` | Sum             | `TargetGroup`         |
| `LambdaUserError`     | `LambdaUserError`     | Sum             | `TargetGroup`         |

## AWS/Athena

The `AWS/Athena` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/athena`. All enriched instruments use Delta temporality.

- [AWS::Athena::CapacityReservation](#otel-enrichment-aws-athena-aws-athena-capacityreservation "#otel-enrichment-aws-athena-aws-athena-capacityreservation")

### AWS::Athena::CapacityReservation

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric        | OpenTelemetry metric | Instrument type | Data point attributes               |
| ------------- | -------------------- | --------------- | ----------------------------------- |
| `DPUConsumed` | `DPUConsumed`        | Histogram       | `Capacity Reservation`, `WorkGroup` |

## AWS/AutoScaling

The `AWS/AutoScaling` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/autoscaling`. All enriched instruments use Delta temporality.

- [AWS::AutoScaling::AutoScalingGroup](#otel-enrichment-aws-autoscaling-aws-autoscaling-autoscalinggroup "#otel-enrichment-aws-autoscaling-aws-autoscaling-autoscalinggroup")

### AWS::AutoScaling::AutoScalingGroup

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric                            | OpenTelemetry metric              | Instrument type | Data point attributes  |
| --------------------------------- | --------------------------------- | --------------- | ---------------------- |
| `GroupAndWarmPoolDesiredCapacity` | `GroupAndWarmPoolDesiredCapacity` | Histogram       | `AutoScalingGroupName` |
| `GroupAndWarmPoolTotalCapacity`   | `GroupAndWarmPoolTotalCapacity`   | Histogram       | `AutoScalingGroupName` |
| `GroupDesiredCapacity`            | `GroupDesiredCapacity`            | Histogram       | `AutoScalingGroupName` |
| `GroupInServiceCapacity`          | `GroupInServiceCapacity`          | Histogram       | `AutoScalingGroupName` |
| `GroupInServiceInstances`         | `GroupInServiceInstances`         | Histogram       | `AutoScalingGroupName` |
| `GroupMaxSize`                    | `GroupMaxSize`                    | Histogram       | `AutoScalingGroupName` |
| `GroupMinSize`                    | `GroupMinSize`                    | Histogram       | `AutoScalingGroupName` |
| `GroupPendingCapacity`            | `GroupPendingCapacity`            | Histogram       | `AutoScalingGroupName` |
| `GroupPendingInstances`           | `GroupPendingInstances`           | Histogram       | `AutoScalingGroupName` |
| `GroupStandbyCapacity`            | `GroupStandbyCapacity`            | Histogram       | `AutoScalingGroupName` |
| `GroupStandbyInstances`           | `GroupStandbyInstances`           | Histogram       | `AutoScalingGroupName` |
| `GroupTerminatingCapacity`        | `GroupTerminatingCapacity`        | Histogram       | `AutoScalingGroupName` |
| `GroupTerminatingInstances`       | `GroupTerminatingInstances`       | Histogram       | `AutoScalingGroupName` |
| `GroupTotalCapacity`              | `GroupTotalCapacity`              | Histogram       | `AutoScalingGroupName` |
| `GroupTotalInstances`             | `GroupTotalInstances`             | Histogram       | `AutoScalingGroupName` |
| `WarmPoolDesiredCapacity`         | `WarmPoolDesiredCapacity`         | Histogram       | `AutoScalingGroupName` |
| `WarmPoolMinSize`                 | `WarmPoolMinSize`                 | Histogram       | `AutoScalingGroupName` |
| `WarmPoolPendingCapacity`         | `WarmPoolPendingCapacity`         | Histogram       | `AutoScalingGroupName` |
| `WarmPoolTerminatingCapacity`     | `WarmPoolTerminatingCapacity`     | Histogram       | `AutoScalingGroupName` |
| `WarmPoolTotalCapacity`           | `WarmPoolTotalCapacity`           | Histogram       | `AutoScalingGroupName` |
| `WarmPoolWarmedCapacity`          | `WarmPoolWarmedCapacity`          | Histogram       | `AutoScalingGroupName` |

## AWS/Backup

The `AWS/Backup` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/backup`. All enriched instruments use Delta temporality.

- [AWS::Backup::BackupVault](#otel-enrichment-aws-backup-aws-backup-backupvault "#otel-enrichment-aws-backup-aws-backup-backupvault")

### AWS::Backup::BackupVault

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                            | OpenTelemetry metric              | Instrument type | Data point attributes             |
| --------------------------------- | --------------------------------- | --------------- | --------------------------------- |
| `NumberOfBackupJobsCompleted`     | `NumberOfBackupJobsCompleted`     | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfBackupJobsCreated`       | `NumberOfBackupJobsCreated`       | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfBackupJobsExpired`       | `NumberOfBackupJobsExpired`       | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfBackupJobsFailed`        | `NumberOfBackupJobsFailed`        | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfBackupJobsPartial`       | `NumberOfBackupJobsPartial`       | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfBackupJobsPending`       | `NumberOfBackupJobsPending`       | Histogram       | `BackupVaultName`, `ResourceType` |
| `NumberOfBackupJobsRunning`       | `NumberOfBackupJobsRunning`       | Histogram       | `BackupVaultName`, `ResourceType` |
| `NumberOfCopyJobsCompleted`       | `NumberOfCopyJobsCompleted`       | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfCopyJobsCreated`         | `NumberOfCopyJobsCreated`         | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfCopyJobsFailed`          | `NumberOfCopyJobsFailed`          | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfCopyJobsRunning`         | `NumberOfCopyJobsRunning`         | Histogram       | `BackupVaultName`, `ResourceType` |
| `NumberOfRecoveryPointsCold`      | `NumberOfRecoveryPointsCold`      | Histogram       | `BackupVaultName`, `ResourceType` |
| `NumberOfRecoveryPointsCompleted` | `NumberOfRecoveryPointsCompleted` | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfRecoveryPointsCreating`  | `NumberOfRecoveryPointsCreating`  | Histogram       | `BackupVaultName`, `ResourceType` |
| `NumberOfRecoveryPointsDeleting`  | `NumberOfRecoveryPointsDeleting`  | Histogram       | `BackupVaultName`, `ResourceType` |
| `NumberOfRecoveryPointsExpired`   | `NumberOfRecoveryPointsExpired`   | Histogram       | `BackupVaultName`, `ResourceType` |
| `NumberOfRecoveryPointsPartial`   | `NumberOfRecoveryPointsPartial`   | Histogram       | `BackupVaultName`, `ResourceType` |
| `NumberOfRestoreJobsCompleted`    | `NumberOfRestoreJobsCompleted`    | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfRestoreJobsFailed`       | `NumberOfRestoreJobsFailed`       | Sum             | `BackupVaultName`, `ResourceType` |
| `NumberOfRestoreJobsPending`      | `NumberOfRestoreJobsPending`      | Histogram       | `BackupVaultName`, `ResourceType` |
| `NumberOfRestoreJobsRunning`      | `NumberOfRestoreJobsRunning`      | Histogram       | `BackupVaultName`, `ResourceType` |

## AWS/Bedrock

The `AWS/Bedrock` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/bedrock`. All enriched instruments use Delta temporality.

- [model](#otel-enrichment-aws-bedrock-model "#otel-enrichment-aws-bedrock-model")

### `model`

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric                   | OpenTelemetry metric     | Instrument type | Data point attributes                      |
| ------------------------ | ------------------------ | --------------- | ------------------------------------------ |
| `CacheReadInputTokens`   | `CacheReadInputTokens`   | Sum             | `ModelId`                                  |
| `CacheWriteInputTokens`  | `CacheWriteInputTokens`  | Sum             | `ModelId`                                  |
| `EstimatedTPMQuotaUsage` | `EstimatedTPMQuotaUsage` | Histogram       | `ModelId`                                  |
| `InputTokenCount`        | `InputTokenCount`        | Sum             | `ModelId`                                  |
| `InvocationClientErrors` | `InvocationClientErrors` | Sum             | `ModelId`                                  |
| `InvocationLatency`      | `InvocationLatency`      | Histogram       | `ModelId`                                  |
| `InvocationServerErrors` | `InvocationServerErrors` | Sum             | `ModelId`                                  |
| `InvocationThrottles`    | `InvocationThrottles`    | Sum             | `ModelId`                                  |
| `Invocations`            | `Invocations`            | Sum             | `ModelId`                                  |
| `LegacyModelInvocations` | `LegacyModelInvocations` | Sum             | `ModelId`                                  |
| `OutputImageCount`       | `OutputImageCount`       | Sum             | `BucketedStepSize`, `ImageSize`, `ModelId` |
| `OutputTokenCount`       | `OutputTokenCount`       | Sum             | `ModelId`                                  |
| `TimeToFirstToken`       | `TimeToFirstToken`       | Histogram       | `ModelId`                                  |

## AWS/BedrockMantle

The `AWS/BedrockMantle` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/bedrock-mantle`. All enriched instruments use Delta temporality.

- [AWS::BedrockMantle::Project](#otel-enrichment-aws-bedrockmantle-aws-bedrockmantle-project "#otel-enrichment-aws-bedrockmantle-aws-bedrockmantle-project")

### AWS::BedrockMantle::Project

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                  | OpenTelemetry metric    | Instrument type | Data point attributes |
| ----------------------- | ----------------------- | --------------- | --------------------- |
| `InferenceClientErrors` | `InferenceClientErrors` | Sum             | `Model`, `Project`    |
| `Inferences`            | `Inferences`            | Sum             | `Model`, `Project`    |
| `InputTokens`           | `InputTokens`           | Histogram       | `Model`, `Project`    |
| `OutputTokens`          | `OutputTokens`          | Histogram       | `Model`, `Project`    |
| `TotalInputTokens`      | `TotalInputTokens`      | Sum             | `Project`             |
| `TotalOutputTokens`     | `TotalOutputTokens`     | Sum             | `Project`             |

## AWS/ClientVPN

The `AWS/ClientVPN` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/ec2`. All enriched instruments use Delta temporality.

- [AWS::EC2::ClientVpnEndpoint](#otel-enrichment-aws-clientvpn-aws-ec2-clientvpnendpoint "#otel-enrichment-aws-clientvpn-aws-ec2-clientvpnendpoint")

### AWS::EC2::ClientVpnEndpoint

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                          | OpenTelemetry metric                            | Instrument type | Data point attributes |
| ----------------------------------------------- | ----------------------------------------------- | --------------- | --------------------- |
| `ActiveConnectionsCount`                        | `ActiveConnectionsCount`                        | Histogram       | `Endpoint`            |
| `AuthenticationFailures`                        | `AuthenticationFailures`                        | Sum             | `Endpoint`            |
| `ClientConnectHandlerDeniedConnections`         | `ClientConnectHandlerDeniedConnections`         | Sum             | `Endpoint`            |
| `ClientConnectHandlerFailedServiceErrors`       | `ClientConnectHandlerFailedServiceErrors`       | Sum             | `Endpoint`            |
| `ClientConnectHandlerInvalidResponses`          | `ClientConnectHandlerInvalidResponses`          | Sum             | `Endpoint`            |
| `ClientConnectHandlerOtherExecutionErrors`      | `ClientConnectHandlerOtherExecutionErrors`      | Sum             | `Endpoint`            |
| `ClientConnectHandlerThrottlingErrors`          | `ClientConnectHandlerThrottlingErrors`          | Sum             | `Endpoint`            |
| `ClientConnectHandlerTimeouts`                  | `ClientConnectHandlerTimeouts`                  | Sum             | `Endpoint`            |
| `CrlDaysToExpiry`                               | `CrlDaysToExpiry`                               | Histogram       | `Endpoint`            |
| `EgressBytes`                                   | `EgressBytes`                                   | Sum             | `Endpoint`            |
| `EgressPackets`                                 | `EgressPackets`                                 | Sum             | `Endpoint`            |
| `IngressBytes`                                  | `IngressBytes`                                  | Sum             | `Endpoint`            |
| `IngressPackets`                                | `IngressPackets`                                | Sum             | `Endpoint`            |
| `SelfServicePortalClientConfigurationDownloads` | `SelfServicePortalClientConfigurationDownloads` | Sum             | `Endpoint`            |
| `ZeroHealthItemsCount`                          | `ZeroHealthItemsCount`                          | Histogram       | `Endpoint`            |

## AWS/CloudFront

The `AWS/CloudFront` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/cloudfront`. All enriched instruments use Delta temporality.

- [AWS::CloudFront::Function](#otel-enrichment-aws-cloudfront-aws-cloudfront-function "#otel-enrichment-aws-cloudfront-aws-cloudfront-function")

### AWS::CloudFront::Function

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                       | OpenTelemetry metric         | Instrument type | Data point attributes                      |
| ---------------------------- | ---------------------------- | --------------- | ------------------------------------------ |
| `FunctionComputeUtilization` | `FunctionComputeUtilization` | Histogram       | `DistributionId`, `FunctionName`, `Region` |
| `FunctionExecutionErrors`    | `FunctionExecutionErrors`    | Sum             | `DistributionId`, `FunctionName`, `Region` |
| `FunctionInvocations`        | `FunctionInvocations`        | Sum             | `DistributionId`, `FunctionName`, `Region` |
| `FunctionThrottles`          | `FunctionThrottles`          | Sum             | `DistributionId`, `FunctionName`, `Region` |
| `FunctionValidationErrors`   | `FunctionValidationErrors`   | Sum             | `DistributionId`, `FunctionName`, `Region` |
| `KvsReadErrors`              | `KvsReadErrors`              | Sum             | `DistributionId`, `FunctionName`, `Region` |
| `KvsReadRequests`            | `KvsReadRequests`            | Sum             | `DistributionId`, `FunctionName`, `Region` |

## AWS/CloudWatch/MetricStreams

The `AWS/CloudWatch/MetricStreams` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/cloudwatch`. All enriched instruments use Delta temporality.

- [AWS::CloudWatch::MetricStream](#otel-enrichment-aws-cloudwatch-metricstreams-aws-cloudwatch-metricstream "#otel-enrichment-aws-cloudwatch-metricstreams-aws-cloudwatch-metricstream")

### AWS::CloudWatch::MetricStream

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric              | OpenTelemetry metric | Instrument type | Data point attributes |
| ------------------- | -------------------- | --------------- | --------------------- |
| `MetricUpdate`      | `MetricUpdate`       | Sum             | `MetricStreamName`    |
| `PublishErrorRate`  | `PublishErrorRate`   | Histogram       | `MetricStreamName`    |
| `TotalMetricUpdate` | `TotalMetricUpdate`  | Sum             | `MetricStreamName`    |

## AWS/CodeGuruProfiler

The `AWS/CodeGuruProfiler` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/codeguru-profiler`. All enriched instruments use Delta temporality.

- [AWS::CodeGuruProfiler::ProfilingGroup](#otel-enrichment-aws-codeguruprofiler-aws-codeguruprofiler-profilinggroup "#otel-enrichment-aws-codeguruprofiler-aws-codeguruprofiler-profilinggroup")

### AWS::CodeGuruProfiler::ProfilingGroup

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric            | OpenTelemetry metric | Instrument type | Data point attributes |
| ----------------- | -------------------- | --------------- | --------------------- |
| `Recommendations` | `Recommendations`    | Histogram       | `ProfilingGroupName`  |

## AWS/Cognito

The `AWS/Cognito` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/cognito-idp`. All enriched instruments use Delta temporality.

- [AWS::Cognito::UserPool](#otel-enrichment-aws-cognito-aws-cognito-userpool "#otel-enrichment-aws-cognito-aws-cognito-userpool")

### AWS::Cognito::UserPool

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                      | OpenTelemetry metric        | Instrument type | Data point attributes                            |
| --------------------------- | --------------------------- | --------------- | ------------------------------------------------ |
| `AccountTakeoverRisk`       | `AccountTakeoverRisk`       | Sum             | `Operation`, `RiskLevel`, `UserPoolId`           |
| `CompromisedCredentialRisk` | `CompromisedCredentialRisk` | Sum             | `Operation`, `RiskLevel`, `UserPoolId`           |
| `FederationSuccesses`       | `FederationSuccesses`       | Sum             | `IdentityProvider`, `UserPool`, `UserPoolClient` |
| `FederationThrottles`       | `FederationThrottles`       | Sum             | `IdentityProvider`, `UserPool`, `UserPoolClient` |
| `NoRisk`                    | `NoRisk`                    | Sum             | `Operation`, `UserPoolId`                        |
| `Risk`                      | `Risk`                      | Sum             | `Operation`, `UserPoolId`                        |
| `SignInSuccesses`           | `SignInSuccesses`           | Sum             | `UserPool`, `UserPoolClient`                     |
| `SignInThrottles`           | `SignInThrottles`           | Sum             | `UserPool`, `UserPoolClient`                     |
| `SignUpSuccesses`           | `SignUpSuccesses`           | Sum             | `UserPool`, `UserPoolClient`                     |
| `SignUpThrottles`           | `SignUpThrottles`           | Sum             | `UserPool`, `UserPoolClient`                     |
| `TokenRefreshSuccesses`     | `TokenRefreshSuccesses`     | Sum             | `UserPool`, `UserPoolClient`                     |
| `TokenRefreshThrottles`     | `TokenRefreshThrottles`     | Sum             | `UserPool`, `UserPoolClient`                     |

## AWS/Connect

The `AWS/Connect` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/connect`. All enriched instruments use Delta temporality.

- [AWS::Connect::Instance](#otel-enrichment-aws-connect-aws-connect-instance "#otel-enrichment-aws-connect-aws-connect-instance")
- [contact](#otel-enrichment-aws-connect-contact "#otel-enrichment-aws-connect-contact")

### AWS::Connect::Instance

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                            | OpenTelemetry metric              | Instrument type | Data point attributes                                            |
| --------------------------------- | --------------------------------- | --------------- | ---------------------------------------------------------------- |
| `CallRecordingUploadError`        | `CallRecordingUploadError`        | Sum             | `InstanceId`, `MetricGroup`                                      |
| `CallsBreachingConcurrencyQuota`  | `CallsBreachingConcurrencyQuota`  | Sum             | `InstanceId`, `MetricGroup`                                      |
| `CallsPerInterval`                | `CallsPerInterval`                | Sum             | `InstanceId`, `MetricGroup`                                      |
| `ChatsBreachingActiveChatQuota`   | `ChatsBreachingActiveChatQuota`   | Sum             | `InstanceId`, `MetricGroup`                                      |
| `ConcurrentActiveChats`           | `ConcurrentActiveChats`           | Histogram       | `InstanceId`, `MetricGroup`                                      |
| `ConcurrentActiveChatsPercentage` | `ConcurrentActiveChatsPercentage` | Histogram       | `InstanceId`, `MetricGroup`                                      |
| `ConcurrentCalls`                 | `ConcurrentCalls`                 | Histogram       | `InstanceId`, `MetricGroup`                                      |
| `ConcurrentCallsPercentage`       | `ConcurrentCallsPercentage`       | Histogram       | `InstanceId`, `MetricGroup`                                      |
| `ConcurrentTasks`                 | `ConcurrentTasks`                 | Histogram       | `InstanceId`, `MetricGroup`                                      |
| `ConcurrentTasksPercentage`       | `ConcurrentTasksPercentage`       | Histogram       | `InstanceId`, `MetricGroup`                                      |
| `ContactFlowErrors`               | `ContactFlowErrors`               | Sum             | `ContactFlowName`, `InstanceId`, `MetricGroup`                   |
| `LongestQueueWaitTime`            | `LongestQueueWaitTime`            | Histogram       | `InstanceId`, `MetricGroup`, `QueueName`                         |
| `MisconfiguredPhoneNumbers`       | `MisconfiguredPhoneNumbers`       | Sum             | `InstanceId`, `MetricGroup`                                      |
| `MissedCalls`                     | `MissedCalls`                     | Sum             | `InstanceId`, `MetricGroup`                                      |
| `PublicSigningKeyUsage`           | `PublicSigningKeyUsage`           | Sum             | `InstanceId`, `SigningKeyId`                                     |
| `QueueCapacityExceededError`      | `QueueCapacityExceededError`      | Sum             | `InstanceId`, `MetricGroup`, `QueueName`                         |
| `QueueSize`                       | `QueueSize`                       | Histogram       | `InstanceId`, `MetricGroup`, `QueueName`                         |
| `SuccessfulChatsPerInterval`      | `SuccessfulChatsPerInterval`      | Sum             | `InstanceId`, `MetricGroup`                                      |
| `TasksBreachingConcurrencyQuota`  | `TasksBreachingConcurrencyQuota`  | Sum             | `InstanceId`, `MetricGroup`                                      |
| `ToInstancePacketLossRate`        | `ToInstancePacketLossRate`        | Histogram       | `InstanceId`, `Participant`, `Stream Type`, `Type of Connection` |

### `contact`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                      | OpenTelemetry metric        | Instrument type | Data point attributes                    |
| --------------------------- | --------------------------- | --------------- | ---------------------------------------- |
| `TasksExpired`              | `TasksExpired`              | Sum             | `ContactId`, `InstanceId`, `MetricGroup` |
| `TasksExpiryWarningReached` | `TasksExpiryWarningReached` | Sum             | `ContactId`, `InstanceId`, `MetricGroup` |

## AWS/DAX

The `AWS/DAX` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/dax`. All enriched instruments use Delta temporality.

- [AWS::DAX::Cluster](#otel-enrichment-aws-dax-aws-dax-cluster "#otel-enrichment-aws-dax-aws-dax-cluster")

### AWS::DAX::Cluster

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                               | OpenTelemetry metric                 | Instrument type | Data point attributes |
| ------------------------------------ | ------------------------------------ | --------------- | --------------------- |
| `BaselineNetworkBytesInUtilization`  | `BaselineNetworkBytesInUtilization`  | Histogram       | `ClusterId`, `NodeId` |
| `BaselineNetworkBytesOutUtilization` | `BaselineNetworkBytesOutUtilization` | Histogram       | `ClusterId`, `NodeId` |
| `BatchGetItemRequestCount`           | `BatchGetItemRequestCount`           | Sum             | `ClusterId`, `NodeId` |
| `BatchWriteItemRequestCount`         | `BatchWriteItemRequestCount`         | Sum             | `ClusterId`, `NodeId` |
| `CPUCreditBalance`                   | `CPUCreditBalance`                   | Histogram       | `ClusterId`, `NodeId` |
| `CPUCreditUsage`                     | `CPUCreditUsage`                     | Histogram       | `ClusterId`, `NodeId` |
| `CPUSurplusCreditBalance`            | `CPUSurplusCreditBalance`            | Histogram       | `ClusterId`, `NodeId` |
| `CPUSurplusCreditsCharged`           | `CPUSurplusCreditsCharged`           | Sum             | `ClusterId`, `NodeId` |
| `CPUUtilization`                     | `CPUUtilization`                     | Histogram       | `ClusterId`, `NodeId` |
| `CacheMemoryUtilization`             | `CacheMemoryUtilization`             | Histogram       | `ClusterId`, `NodeId` |
| `ClientConnections`                  | `ClientConnections`                  | Histogram       | `ClusterId`, `NodeId` |
| `DeleteItemRequestCount`             | `DeleteItemRequestCount`             | Sum             | `ClusterId`, `NodeId` |
| `ErrorRequestCount`                  | `ErrorRequestCount`                  | Sum             | `ClusterId`, `NodeId` |
| `EstimatedDbSize`                    | `EstimatedDbSize`                    | Histogram       | `ClusterId`, `NodeId` |
| `EvictedSize`                        | `EvictedSize`                        | Histogram       | `ClusterId`, `NodeId` |
| `FailedRequestCount`                 | `FailedRequestCount`                 | Sum             | `ClusterId`, `NodeId` |
| `FaultRequestCount`                  | `FaultRequestCount`                  | Sum             | `ClusterId`, `NodeId` |
| `GetItemRequestCount`                | `GetItemRequestCount`                | Sum             | `ClusterId`, `NodeId` |
| `ItemCacheHits`                      | `ItemCacheHits`                      | Sum             | `ClusterId`, `NodeId` |
| `ItemCacheMisses`                    | `ItemCacheMisses`                    | Sum             | `ClusterId`, `NodeId` |
| `NetworkBytesIn`                     | `NetworkBytesIn`                     | Sum             | `ClusterId`, `NodeId` |
| `NetworkBytesOut`                    | `NetworkBytesOut`                    | Sum             | `ClusterId`, `NodeId` |
| `NetworkMaxBytesIn`                  | `NetworkMaxBytesIn`                  | Histogram       | `ClusterId`, `NodeId` |
| `NetworkMaxBytesOut`                 | `NetworkMaxBytesOut`                 | Histogram       | `ClusterId`, `NodeId` |
| `NetworkMaxPacketsIn`                | `NetworkMaxPacketsIn`                | Histogram       | `ClusterId`, `NodeId` |
| `NetworkMaxPacketsOut`               | `NetworkMaxPacketsOut`               | Histogram       | `ClusterId`, `NodeId` |
| `NetworkPacketsIn`                   | `NetworkPacketsIn`                   | Sum             | `ClusterId`, `NodeId` |
| `NetworkPacketsOut`                  | `NetworkPacketsOut`                  | Sum             | `ClusterId`, `NodeId` |
| `PutItemRequestCount`                | `PutItemRequestCount`                | Sum             | `ClusterId`, `NodeId` |
| `QueryCacheHits`                     | `QueryCacheHits`                     | Sum             | `ClusterId`, `NodeId` |
| `QueryCacheMisses`                   | `QueryCacheMisses`                   | Sum             | `ClusterId`, `NodeId` |
| `QueryRequestCount`                  | `QueryRequestCount`                  | Sum             | `ClusterId`, `NodeId` |
| `ScanCacheHits`                      | `ScanCacheHits`                      | Sum             | `ClusterId`, `NodeId` |
| `ScanCacheMisses`                    | `ScanCacheMisses`                    | Sum             | `ClusterId`, `NodeId` |
| `ScanRequestCount`                   | `ScanRequestCount`                   | Sum             | `ClusterId`, `NodeId` |
| `ThrottledRequestCount`              | `ThrottledRequestCount`              | Sum             | `ClusterId`, `NodeId` |
| `TotalRequestCount`                  | `TotalRequestCount`                  | Sum             | `ClusterId`, `NodeId` |
| `TransactGetItemsCount`              | `TransactGetItemsCount`              | Sum             | `ClusterId`, `NodeId` |
| `TransactWriteItemsCount`            | `TransactWriteItemsCount`            | Sum             | `ClusterId`, `NodeId` |
| `UpdateItemRequestCount`             | `UpdateItemRequestCount`             | Sum             | `ClusterId`, `NodeId` |

## AWS/DX

The `AWS/DX` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/directconnect`. All enriched instruments use Delta temporality.

- [AWS::DirectConnect::VirtualInterface](#otel-enrichment-aws-dx-aws-directconnect-virtualinterface "#otel-enrichment-aws-dx-aws-directconnect-virtualinterface")
- [dxcon](#otel-enrichment-aws-dx-dxcon "#otel-enrichment-aws-dx-dxcon")

### AWS::DirectConnect::VirtualInterface

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                                  | OpenTelemetry metric                    | Instrument type | Data point attributes                                   |
| --------------------------------------- | --------------------------------------- | --------------- | ------------------------------------------------------- |
| `VirtualInterfaceBgpPrefixesAccepted`   | `VirtualInterfaceBgpPrefixesAccepted`   | Histogram       | `ConnectionId`, `IpAddressFamily`, `VirtualInterfaceId` |
| `VirtualInterfaceBgpPrefixesAdvertised` | `VirtualInterfaceBgpPrefixesAdvertised` | Histogram       | `ConnectionId`, `IpAddressFamily`, `VirtualInterfaceId` |
| `VirtualInterfaceBgpStatus`             | `VirtualInterfaceBgpStatus`             | Histogram       | `ConnectionId`, `IpAddressFamily`, `VirtualInterfaceId` |
| `VirtualInterfaceBpsEgress`             | `VirtualInterfaceBpsEgress`             | Histogram       | `ConnectionId`, `VirtualInterfaceId`                    |
| `VirtualInterfaceBpsIngress`            | `VirtualInterfaceBpsIngress`            | Histogram       | `ConnectionId`, `VirtualInterfaceId`                    |
| `VirtualInterfacePpsEgress`             | `VirtualInterfacePpsEgress`             | Histogram       | `ConnectionId`, `VirtualInterfaceId`                    |
| `VirtualInterfacePpsIngress`            | `VirtualInterfacePpsIngress`            | Histogram       | `ConnectionId`, `VirtualInterfaceId`                    |

### `dxcon`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                      | OpenTelemetry metric        | Instrument type | Data point attributes               |
| --------------------------- | --------------------------- | --------------- | ----------------------------------- |
| `ConnectionBpsEgress`       | `ConnectionBpsEgress`       | Histogram       | `ConnectionId`                      |
| `ConnectionBpsIngress`      | `ConnectionBpsIngress`      | Histogram       | `ConnectionId`                      |
| `ConnectionCRCErrorCount`   | `ConnectionCRCErrorCount`   | Sum             | `ConnectionId`                      |
| `ConnectionEncryptionState` | `ConnectionEncryptionState` | Histogram       | `ConnectionId`                      |
| `ConnectionErrorCount`      | `ConnectionErrorCount`      | Sum             | `ConnectionId`                      |
| `ConnectionLightLevelRx`    | `ConnectionLightLevelRx`    | Histogram       | `ConnectionId`, `OpticalLaneNumber` |
| `ConnectionLightLevelTx`    | `ConnectionLightLevelTx`    | Histogram       | `ConnectionId`, `OpticalLaneNumber` |
| `ConnectionPpsEgress`       | `ConnectionPpsEgress`       | Histogram       | `ConnectionId`                      |
| `ConnectionPpsIngress`      | `ConnectionPpsIngress`      | Histogram       | `ConnectionId`                      |
| `ConnectionState`           | `ConnectionState`           | Histogram       | `ConnectionId`                      |

## AWS/DataSync

The `AWS/DataSync` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/datasync`. All enriched instruments use Delta temporality.

- [AWS::DataSync::Agent](#otel-enrichment-aws-datasync-aws-datasync-agent "#otel-enrichment-aws-datasync-aws-datasync-agent")
- [AWS::DataSync::Task](#otel-enrichment-aws-datasync-aws-datasync-task "#otel-enrichment-aws-datasync-aws-datasync-task")

### AWS::DataSync::Agent

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric             | OpenTelemetry metric | Instrument type | Data point attributes |
| ------------------ | -------------------- | --------------- | --------------------- |
| `BytesCompressed`  | `BytesCompressed`    | Sum             | `AgentId`             |
| `BytesTransferred` | `BytesTransferred`   | Sum             | `AgentId`             |
| `BytesWritten`     | `BytesWritten`       | Sum             | `AgentId`             |
| `FilesTransferred` | `FilesTransferred`   | Sum             | `AgentId`             |

### AWS::DataSync::Task

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                     | OpenTelemetry metric       | Instrument type | Data point attributes |
| -------------------------- | -------------------------- | --------------- | --------------------- |
| `BytesCompressed`          | `BytesCompressed`          | Sum             | `TaskId`              |
| `BytesPreparedDestination` | `BytesPreparedDestination` | Sum             | `TaskId`              |
| `BytesPreparedSource`      | `BytesPreparedSource`      | Sum             | `TaskId`              |
| `BytesTransferred`         | `BytesTransferred`         | Sum             | `TaskId`              |
| `BytesVerifiedDestination` | `BytesVerifiedDestination` | Sum             | `TaskId`              |
| `BytesVerifiedSource`      | `BytesVerifiedSource`      | Sum             | `TaskId`              |
| `BytesWritten`             | `BytesWritten`             | Sum             | `TaskId`              |
| `FilesDeleted`             | `FilesDeleted`             | Sum             | `TaskId`              |
| `FilesListedSource`        | `FilesListedSource`        | Sum             | `TaskId`              |
| `FilesPrepared`            | `FilesPrepared`            | Sum             | `TaskId`              |
| `FilesPreparedDestination` | `FilesPreparedDestination` | Sum             | `TaskId`              |
| `FilesPreparedSource`      | `FilesPreparedSource`      | Sum             | `TaskId`              |
| `FilesSkipped`             | `FilesSkipped`             | Sum             | `TaskId`              |
| `FilesTransferred`         | `FilesTransferred`         | Sum             | `TaskId`              |
| `FilesVerified`            | `FilesVerified`            | Sum             | `TaskId`              |
| `FilesVerifiedDestination` | `FilesVerifiedDestination` | Sum             | `TaskId`              |
| `FilesVerifiedSource`      | `FilesVerifiedSource`      | Sum             | `TaskId`              |

## AWS/DocDB

The `AWS/DocDB` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/rds`. All enriched instruments use Delta temporality.

- [cluster](#otel-enrichment-aws-docdb-cluster "#otel-enrichment-aws-docdb-cluster")
- [instance](#otel-enrichment-aws-docdb-instance "#otel-enrichment-aws-docdb-instance")

### `cluster`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                             | OpenTelemetry metric                     | Instrument type | Data point attributes         |
| ---------------------------------- | ---------------------------------------- | --------------- | ----------------------------- |
| `AvailableMVCCIds`                 | `AvailableMVCCIds`                       | Histogram       | `DBClusterIdentifier`         |
| `AvailableMVCCIds`                 | `AvailableMVCCIdsByRole`                 | Histogram       | `DBClusterIdentifier`, `Role` |
| `BackupRetentionPeriodStorageUsed` | `BackupRetentionPeriodStorageUsed`       | Histogram       | `DBClusterIdentifier`         |
| `BufferCacheHitRatio`              | `BufferCacheHitRatio`                    | Histogram       | `DBClusterIdentifier`         |
| `BufferCacheHitRatio`              | `BufferCacheHitRatioByRole`              | Histogram       | `DBClusterIdentifier`, `Role` |
| `CPUCreditBalance`                 | `CPUCreditBalance`                       | Histogram       | `DBClusterIdentifier`         |
| `CPUCreditBalance`                 | `CPUCreditBalanceByRole`                 | Histogram       | `DBClusterIdentifier`, `Role` |
| `CPUCreditUsage`                   | `CPUCreditUsage`                         | Histogram       | `DBClusterIdentifier`         |
| `CPUCreditUsage`                   | `CPUCreditUsageByRole`                   | Histogram       | `DBClusterIdentifier`, `Role` |
| `CPUSurplusCreditBalance`          | `CPUSurplusCreditBalance`                | Histogram       | `DBClusterIdentifier`         |
| `CPUSurplusCreditBalance`          | `CPUSurplusCreditBalanceByRole`          | Histogram       | `DBClusterIdentifier`, `Role` |
| `CPUSurplusCreditsCharged`         | `CPUSurplusCreditsCharged`               | Sum             | `DBClusterIdentifier`         |
| `CPUSurplusCreditsCharged`         | `CPUSurplusCreditsChargedByRole`         | Sum             | `DBClusterIdentifier`, `Role` |
| `CPUUtilization`                   | `CPUUtilization`                         | Histogram       | `DBClusterIdentifier`         |
| `CPUUtilization`                   | `CPUUtilizationByRole`                   | Histogram       | `DBClusterIdentifier`, `Role` |
| `ChangeStreamLogSize`              | `ChangeStreamLogSize`                    | Histogram       | `DBClusterIdentifier`         |
| `DBClusterReplicaLagMaximum`       | `DBClusterReplicaLagMaximum`             | Histogram       | `DBClusterIdentifier`         |
| `DBClusterReplicaLagMinimum`       | `DBClusterReplicaLagMinimum`             | Histogram       | `DBClusterIdentifier`         |
| `DBInstanceReplicaLag`             | `DBInstanceReplicaLag`                   | Histogram       | `DBClusterIdentifier`         |
| `DBInstanceReplicaLag`             | `DBInstanceReplicaLagByRole`             | Histogram       | `DBClusterIdentifier`, `Role` |
| `DatabaseConnections`              | `DatabaseConnections`                    | Histogram       | `DBClusterIdentifier`         |
| `DatabaseConnections`              | `DatabaseConnectionsByRole`              | Histogram       | `DBClusterIdentifier`, `Role` |
| `DatabaseConnectionsActiveMax`     | `DatabaseConnectionsActiveMax`           | Histogram       | `DBClusterIdentifier`         |
| `DatabaseConnectionsActiveMax`     | `DatabaseConnectionsActiveMaxByRole`     | Histogram       | `DBClusterIdentifier`, `Role` |
| `DatabaseConnectionsLimit`         | `DatabaseConnectionsLimit`               | Histogram       | `DBClusterIdentifier`         |
| `DatabaseConnectionsLimit`         | `DatabaseConnectionsLimitByRole`         | Histogram       | `DBClusterIdentifier`, `Role` |
| `DatabaseConnectionsMax`           | `DatabaseConnectionsMax`                 | Histogram       | `DBClusterIdentifier`         |
| `DatabaseConnectionsMax`           | `DatabaseConnectionsMaxByRole`           | Histogram       | `DBClusterIdentifier`, `Role` |
| `DatabaseCursors`                  | `DatabaseCursors`                        | Histogram       | `DBClusterIdentifier`         |
| `DatabaseCursors`                  | `DatabaseCursorsByRole`                  | Histogram       | `DBClusterIdentifier`, `Role` |
| `DatabaseCursorsLimit`             | `DatabaseCursorsLimit`                   | Histogram       | `DBClusterIdentifier`         |
| `DatabaseCursorsLimit`             | `DatabaseCursorsLimitByRole`             | Histogram       | `DBClusterIdentifier`, `Role` |
| `DatabaseCursorsMax`               | `DatabaseCursorsMax`                     | Histogram       | `DBClusterIdentifier`         |
| `DatabaseCursorsMax`               | `DatabaseCursorsMaxByRole`               | Histogram       | `DBClusterIdentifier`, `Role` |
| `DatabaseCursorsTimedOut`          | `DatabaseCursorsTimedOut`                | Sum             | `DBClusterIdentifier`         |
| `DatabaseCursorsTimedOut`          | `DatabaseCursorsTimedOutByRole`          | Sum             | `DBClusterIdentifier`, `Role` |
| `DiagnosticAlertCount`             | `DiagnosticAlertCount`                   | Histogram       | `DBClusterIdentifier`         |
| `DiagnosticAlertCount`             | `DiagnosticAlertCountByRole`             | Histogram       | `DBClusterIdentifier`, `Role` |
| `DiskQueueDepth`                   | `DiskQueueDepth`                         | Histogram       | `DBClusterIdentifier`         |
| `DiskQueueDepth`                   | `DiskQueueDepthByRole`                   | Histogram       | `DBClusterIdentifier`, `Role` |
| `DocumentsDeleted`                 | `DocumentsDeleted`                       | Sum             | `DBClusterIdentifier`         |
| `DocumentsDeleted`                 | `DocumentsDeletedByRole`                 | Sum             | `DBClusterIdentifier`, `Role` |
| `DocumentsInserted`                | `DocumentsInserted`                      | Sum             | `DBClusterIdentifier`         |
| `DocumentsInserted`                | `DocumentsInsertedByRole`                | Sum             | `DBClusterIdentifier`, `Role` |
| `DocumentsReturned`                | `DocumentsReturned`                      | Sum             | `DBClusterIdentifier`         |
| `DocumentsReturned`                | `DocumentsReturnedByRole`                | Sum             | `DBClusterIdentifier`, `Role` |
| `DocumentsUpdated`                 | `DocumentsUpdated`                       | Sum             | `DBClusterIdentifier`         |
| `DocumentsUpdated`                 | `DocumentsUpdatedByRole`                 | Sum             | `DBClusterIdentifier`, `Role` |
| `EBSByteBalance%`                  | `EBSByteBalance%`                        | Histogram       | `DBClusterIdentifier`         |
| `EBSByteBalance%`                  | `EBSByteBalancePercentByRole`            | Histogram       | `DBClusterIdentifier`, `Role` |
| `EBSIOBalance%`                    | `EBSIOBalance%`                          | Histogram       | `DBClusterIdentifier`         |
| `EBSIOBalance%`                    | `EBSIOBalancePercentByRole`              | Histogram       | `DBClusterIdentifier`, `Role` |
| `EngineUptime`                     | `EngineUptime`                           | Histogram       | `DBClusterIdentifier`         |
| `EngineUptime`                     | `EngineUptimeByRole`                     | Histogram       | `DBClusterIdentifier`, `Role` |
| `FreeLocalStorage`                 | `FreeLocalStorage`                       | Histogram       | `DBClusterIdentifier`         |
| `FreeLocalStorage`                 | `FreeLocalStorageByRole`                 | Histogram       | `DBClusterIdentifier`, `Role` |
| `FreeNVMeStorage`                  | `FreeNVMeStorageByRole`                  | Histogram       | `DBClusterIdentifier`, `Role` |
| `FreeableMemory`                   | `FreeableMemory`                         | Histogram       | `DBClusterIdentifier`         |
| `FreeableMemory`                   | `FreeableMemoryByRole`                   | Histogram       | `DBClusterIdentifier`, `Role` |
| `IndexBufferCacheHitRatio`         | `IndexBufferCacheHitRatio`               | Histogram       | `DBClusterIdentifier`         |
| `IndexBufferCacheHitRatio`         | `IndexBufferCacheHitRatioByRole`         | Histogram       | `DBClusterIdentifier`, `Role` |
| `LongestActiveGCRuntime`           | `LongestActiveGCRuntime`                 | Histogram       | `DBClusterIdentifier`         |
| `LongestActiveGCRuntime`           | `LongestActiveGCRuntimeByRole`           | Histogram       | `DBClusterIdentifier`, `Role` |
| `LowMemNumOperationsThrottled`     | `LowMemNumOperationsThrottled`           | Sum             | `DBClusterIdentifier`         |
| `LowMemNumOperationsThrottled`     | `LowMemNumOperationsThrottledByRole`     | Sum             | `DBClusterIdentifier`, `Role` |
| `LowMemNumOperationsTimedOut`      | `LowMemNumOperationsTimedOut`            | Sum             | `DBClusterIdentifier`         |
| `LowMemNumOperationsTimedOut`      | `LowMemNumOperationsTimedOutByRole`      | Sum             | `DBClusterIdentifier`, `Role` |
| `LowMemThrottleMaxQueueDepth`      | `LowMemThrottleMaxQueueDepth`            | Histogram       | `DBClusterIdentifier`         |
| `LowMemThrottleMaxQueueDepth`      | `LowMemThrottleMaxQueueDepthByRole`      | Histogram       | `DBClusterIdentifier`, `Role` |
| `LowMemThrottleQueueDepth`         | `LowMemThrottleQueueDepth`               | Histogram       | `DBClusterIdentifier`         |
| `LowMemThrottleQueueDepth`         | `LowMemThrottleQueueDepthByRole`         | Histogram       | `DBClusterIdentifier`, `Role` |
| `NVMeStorageCacheHitRatio`         | `NVMeStorageCacheHitRatioByRole`         | Histogram       | `DBClusterIdentifier`, `Role` |
| `NetworkReceiveThroughput`         | `NetworkReceiveThroughput`               | Histogram       | `DBClusterIdentifier`         |
| `NetworkReceiveThroughput`         | `NetworkReceiveThroughputByRole`         | Histogram       | `DBClusterIdentifier`, `Role` |
| `NetworkThroughput`                | `NetworkThroughput`                      | Histogram       | `DBClusterIdentifier`         |
| `NetworkThroughput`                | `NetworkThroughputByRole`                | Histogram       | `DBClusterIdentifier`, `Role` |
| `NetworkTransmitThroughput`        | `NetworkTransmitThroughput`              | Histogram       | `DBClusterIdentifier`         |
| `NetworkTransmitThroughput`        | `NetworkTransmitThroughputByRole`        | Histogram       | `DBClusterIdentifier`, `Role` |
| `OpcountersCommand`                | `OpcountersCommand`                      | Sum             | `DBClusterIdentifier`         |
| `OpcountersCommand`                | `OpcountersCommandByRole`                | Sum             | `DBClusterIdentifier`, `Role` |
| `OpcountersDelete`                 | `OpcountersDelete`                       | Sum             | `DBClusterIdentifier`         |
| `OpcountersDelete`                 | `OpcountersDeleteByRole`                 | Sum             | `DBClusterIdentifier`, `Role` |
| `OpcountersGetmore`                | `OpcountersGetmore`                      | Sum             | `DBClusterIdentifier`         |
| `OpcountersGetmore`                | `OpcountersGetmoreByRole`                | Sum             | `DBClusterIdentifier`, `Role` |
| `OpcountersInsert`                 | `OpcountersInsert`                       | Sum             | `DBClusterIdentifier`         |
| `OpcountersInsert`                 | `OpcountersInsertByRole`                 | Sum             | `DBClusterIdentifier`, `Role` |
| `OpcountersQuery`                  | `OpcountersQuery`                        | Sum             | `DBClusterIdentifier`         |
| `OpcountersQuery`                  | `OpcountersQueryByRole`                  | Sum             | `DBClusterIdentifier`, `Role` |
| `OpcountersUpdate`                 | `OpcountersUpdate`                       | Sum             | `DBClusterIdentifier`         |
| `OpcountersUpdate`                 | `OpcountersUpdateByRole`                 | Sum             | `DBClusterIdentifier`, `Role` |
| `ReadIOPS`                         | `ReadIOPS`                               | Histogram       | `DBClusterIdentifier`         |
| `ReadIOPS`                         | `ReadIOPSByRole`                         | Histogram       | `DBClusterIdentifier`, `Role` |
| `ReadIOPSNVMeStorage`              | `ReadIOPSNVMeStorageByRole`              | Histogram       | `DBClusterIdentifier`, `Role` |
| `ReadLatency`                      | `ReadLatency`                            | Histogram       | `DBClusterIdentifier`         |
| `ReadLatency`                      | `ReadLatencyByRole`                      | Histogram       | `DBClusterIdentifier`, `Role` |
| `ReadLatencyNVMeStorage`           | `ReadLatencyNVMeStorageByRole`           | Histogram       | `DBClusterIdentifier`, `Role` |
| `ReadThroughput`                   | `ReadThroughput`                         | Histogram       | `DBClusterIdentifier`         |
| `ReadThroughput`                   | `ReadThroughputByRole`                   | Histogram       | `DBClusterIdentifier`, `Role` |
| `ReadThroughputNVMeStorage`        | `ReadThroughputNVMeStorageByRole`        | Histogram       | `DBClusterIdentifier`, `Role` |
| `SnapshotStorageUsed`              | `SnapshotStorageUsed`                    | Histogram       | `DBClusterIdentifier`         |
| `StorageNetworkReceiveThroughput`  | `StorageNetworkReceiveThroughput`        | Histogram       | `DBClusterIdentifier`         |
| `StorageNetworkReceiveThroughput`  | `StorageNetworkReceiveThroughputByRole`  | Histogram       | `DBClusterIdentifier`, `Role` |
| `StorageNetworkThroughput`         | `StorageNetworkThroughput`               | Histogram       | `DBClusterIdentifier`         |
| `StorageNetworkThroughput`         | `StorageNetworkThroughputByRole`         | Histogram       | `DBClusterIdentifier`, `Role` |
| `StorageNetworkTransmitThroughput` | `StorageNetworkTransmitThroughput`       | Histogram       | `DBClusterIdentifier`         |
| `StorageNetworkTransmitThroughput` | `StorageNetworkTransmitThroughputByRole` | Histogram       | `DBClusterIdentifier`, `Role` |
| `StsGetCallerIdentityCalls`        | `StsGetCallerIdentityCalls`              | Histogram       | `DBClusterIdentifier`         |
| `StsGetCallerIdentityCalls`        | `StsGetCallerIdentityCallsByRole`        | Histogram       | `DBClusterIdentifier`, `Role` |
| `StsMaxConcurrentRequests`         | `StsMaxConcurrentRequests`               | Histogram       | `DBClusterIdentifier`         |
| `StsMaxConcurrentRequests`         | `StsMaxConcurrentRequestsByRole`         | Histogram       | `DBClusterIdentifier`, `Role` |
| `SwapUsage`                        | `SwapUsage`                              | Histogram       | `DBClusterIdentifier`         |
| `SwapUsage`                        | `SwapUsageByRole`                        | Histogram       | `DBClusterIdentifier`, `Role` |
| `TTLDeletedDocuments`              | `TTLDeletedDocuments`                    | Sum             | `DBClusterIdentifier`         |
| `TTLDeletedDocuments`              | `TTLDeletedDocumentsByRole`              | Sum             | `DBClusterIdentifier`, `Role` |
| `TotalBackupStorageBilled`         | `TotalBackupStorageBilled`               | Histogram       | `DBClusterIdentifier`         |
| `TransactionsAborted`              | `TransactionsAborted`                    | Sum             | `DBClusterIdentifier`         |
| `TransactionsAborted`              | `TransactionsAbortedByRole`              | Sum             | `DBClusterIdentifier`, `Role` |
| `TransactionsCommitted`            | `TransactionsCommitted`                  | Sum             | `DBClusterIdentifier`         |
| `TransactionsCommitted`            | `TransactionsCommittedByRole`            | Sum             | `DBClusterIdentifier`, `Role` |
| `TransactionsOpen`                 | `TransactionsOpen`                       | Histogram       | `DBClusterIdentifier`         |
| `TransactionsOpen`                 | `TransactionsOpenByRole`                 | Histogram       | `DBClusterIdentifier`, `Role` |
| `TransactionsOpenLimit`            | `TransactionsOpenLimit`                  | Histogram       | `DBClusterIdentifier`         |
| `TransactionsOpenLimit`            | `TransactionsOpenLimitByRole`            | Histogram       | `DBClusterIdentifier`, `Role` |
| `TransactionsOpenMax`              | `TransactionsOpenMax`                    | Histogram       | `DBClusterIdentifier`         |
| `TransactionsOpenMax`              | `TransactionsOpenMaxByRole`              | Histogram       | `DBClusterIdentifier`, `Role` |
| `TransactionsStarted`              | `TransactionsStarted`                    | Sum             | `DBClusterIdentifier`         |
| `TransactionsStarted`              | `TransactionsStartedByRole`              | Sum             | `DBClusterIdentifier`, `Role` |
| `VolumeBytesUsed`                  | `VolumeBytesUsed`                        | Histogram       | `DBClusterIdentifier`         |
| `VolumeReadIOPs`                   | `VolumeReadIOPs`                         | Histogram       | `DBClusterIdentifier`         |
| `VolumeWriteIOPs`                  | `VolumeWriteIOPs`                        | Histogram       | `DBClusterIdentifier`         |
| `WriteIOPS`                        | `WriteIOPS`                              | Histogram       | `DBClusterIdentifier`         |
| `WriteIOPS`                        | `WriteIOPSByRole`                        | Histogram       | `DBClusterIdentifier`, `Role` |
| `WriteIOPSNVMeStorage`             | `WriteIOPSNVMeStorageByRole`             | Histogram       | `DBClusterIdentifier`, `Role` |
| `WriteLatency`                     | `WriteLatency`                           | Histogram       | `DBClusterIdentifier`         |
| `WriteLatency`                     | `WriteLatencyByRole`                     | Histogram       | `DBClusterIdentifier`, `Role` |
| `WriteLatencyNVMeStorage`          | `WriteLatencyNVMeStorageByRole`          | Histogram       | `DBClusterIdentifier`, `Role` |
| `WriteThroughput`                  | `WriteThroughput`                        | Histogram       | `DBClusterIdentifier`         |
| `WriteThroughput`                  | `WriteThroughputByRole`                  | Histogram       | `DBClusterIdentifier`, `Role` |
| `WriteThroughputNVMeStorage`       | `WriteThroughputNVMeStorageByRole`       | Histogram       | `DBClusterIdentifier`, `Role` |

### `instance`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                             | OpenTelemetry metric                         | Instrument type | Data point attributes  |
| ---------------------------------- | -------------------------------------------- | --------------- | ---------------------- |
| `AvailableMVCCIds`                 | `AvailableMVCCIdsByInstance`                 | Histogram       | `DBInstanceIdentifier` |
| `BufferCacheHitRatio`              | `BufferCacheHitRatioByInstance`              | Histogram       | `DBInstanceIdentifier` |
| `CPUCreditBalance`                 | `CPUCreditBalanceByInstance`                 | Histogram       | `DBInstanceIdentifier` |
| `CPUCreditUsage`                   | `CPUCreditUsageByInstance`                   | Histogram       | `DBInstanceIdentifier` |
| `CPUSurplusCreditBalance`          | `CPUSurplusCreditBalanceByInstance`          | Histogram       | `DBInstanceIdentifier` |
| `CPUSurplusCreditsCharged`         | `CPUSurplusCreditsChargedByInstance`         | Sum             | `DBInstanceIdentifier` |
| `CPUUtilization`                   | `CPUUtilizationByInstance`                   | Histogram       | `DBInstanceIdentifier` |
| `DBInstanceReplicaLag`             | `DBInstanceReplicaLagByInstance`             | Histogram       | `DBInstanceIdentifier` |
| `DatabaseConnections`              | `DatabaseConnectionsByInstance`              | Histogram       | `DBInstanceIdentifier` |
| `DatabaseConnectionsActiveMax`     | `DatabaseConnectionsActiveMaxByInstance`     | Histogram       | `DBInstanceIdentifier` |
| `DatabaseConnectionsLimit`         | `DatabaseConnectionsLimitByInstance`         | Histogram       | `DBInstanceIdentifier` |
| `DatabaseConnectionsMax`           | `DatabaseConnectionsMaxByInstance`           | Histogram       | `DBInstanceIdentifier` |
| `DatabaseCursors`                  | `DatabaseCursorsByInstance`                  | Histogram       | `DBInstanceIdentifier` |
| `DatabaseCursorsLimit`             | `DatabaseCursorsLimitByInstance`             | Histogram       | `DBInstanceIdentifier` |
| `DatabaseCursorsMax`               | `DatabaseCursorsMaxByInstance`               | Histogram       | `DBInstanceIdentifier` |
| `DatabaseCursorsTimedOut`          | `DatabaseCursorsTimedOutByInstance`          | Sum             | `DBInstanceIdentifier` |
| `DiagnosticAlertCount`             | `DiagnosticAlertCountByInstance`             | Histogram       | `DBInstanceIdentifier` |
| `DiskQueueDepth`                   | `DiskQueueDepthByInstance`                   | Histogram       | `DBInstanceIdentifier` |
| `DocumentsDeleted`                 | `DocumentsDeletedByInstance`                 | Sum             | `DBInstanceIdentifier` |
| `DocumentsInserted`                | `DocumentsInsertedByInstance`                | Sum             | `DBInstanceIdentifier` |
| `DocumentsReturned`                | `DocumentsReturnedByInstance`                | Sum             | `DBInstanceIdentifier` |
| `DocumentsUpdated`                 | `DocumentsUpdatedByInstance`                 | Sum             | `DBInstanceIdentifier` |
| `EBSByteBalance%`                  | `EBSByteBalancePercentByInstance`            | Histogram       | `DBInstanceIdentifier` |
| `EBSIOBalance%`                    | `EBSIOBalancePercentByInstance`              | Histogram       | `DBInstanceIdentifier` |
| `EngineUptime`                     | `EngineUptimeByInstance`                     | Histogram       | `DBInstanceIdentifier` |
| `FreeLocalStorage`                 | `FreeLocalStorageByInstance`                 | Histogram       | `DBInstanceIdentifier` |
| `FreeNVMeStorage`                  | `FreeNVMeStorageByInstance`                  | Histogram       | `DBInstanceIdentifier` |
| `FreeableMemory`                   | `FreeableMemoryByInstance`                   | Histogram       | `DBInstanceIdentifier` |
| `IndexBufferCacheHitRatio`         | `IndexBufferCacheHitRatioByInstance`         | Histogram       | `DBInstanceIdentifier` |
| `LongestActiveGCRuntime`           | `LongestActiveGCRuntimeByInstance`           | Histogram       | `DBInstanceIdentifier` |
| `LowMemNumOperationsThrottled`     | `LowMemNumOperationsThrottledByInstance`     | Sum             | `DBInstanceIdentifier` |
| `LowMemNumOperationsTimedOut`      | `LowMemNumOperationsTimedOutByInstance`      | Sum             | `DBInstanceIdentifier` |
| `LowMemThrottleMaxQueueDepth`      | `LowMemThrottleMaxQueueDepthByInstance`      | Histogram       | `DBInstanceIdentifier` |
| `LowMemThrottleQueueDepth`         | `LowMemThrottleQueueDepthByInstance`         | Histogram       | `DBInstanceIdentifier` |
| `NVMeStorageCacheHitRatio`         | `NVMeStorageCacheHitRatioByInstance`         | Histogram       | `DBInstanceIdentifier` |
| `NetworkReceiveThroughput`         | `NetworkReceiveThroughputByInstance`         | Histogram       | `DBInstanceIdentifier` |
| `NetworkThroughput`                | `NetworkThroughputByInstance`                | Histogram       | `DBInstanceIdentifier` |
| `NetworkTransmitThroughput`        | `NetworkTransmitThroughputByInstance`        | Histogram       | `DBInstanceIdentifier` |
| `OpcountersCommand`                | `OpcountersCommandByInstance`                | Sum             | `DBInstanceIdentifier` |
| `OpcountersDelete`                 | `OpcountersDeleteByInstance`                 | Sum             | `DBInstanceIdentifier` |
| `OpcountersGetmore`                | `OpcountersGetmoreByInstance`                | Sum             | `DBInstanceIdentifier` |
| `OpcountersInsert`                 | `OpcountersInsertByInstance`                 | Sum             | `DBInstanceIdentifier` |
| `OpcountersQuery`                  | `OpcountersQueryByInstance`                  | Sum             | `DBInstanceIdentifier` |
| `OpcountersUpdate`                 | `OpcountersUpdateByInstance`                 | Sum             | `DBInstanceIdentifier` |
| `ReadIOPS`                         | `ReadIOPSByInstance`                         | Histogram       | `DBInstanceIdentifier` |
| `ReadIOPSNVMeStorage`              | `ReadIOPSNVMeStorageByInstance`              | Histogram       | `DBInstanceIdentifier` |
| `ReadLatency`                      | `ReadLatencyByInstance`                      | Histogram       | `DBInstanceIdentifier` |
| `ReadLatencyNVMeStorage`           | `ReadLatencyNVMeStorageByInstance`           | Histogram       | `DBInstanceIdentifier` |
| `ReadThroughput`                   | `ReadThroughputByInstance`                   | Histogram       | `DBInstanceIdentifier` |
| `ReadThroughputNVMeStorage`        | `ReadThroughputNVMeStorageByInstance`        | Histogram       | `DBInstanceIdentifier` |
| `StorageNetworkReceiveThroughput`  | `StorageNetworkReceiveThroughputByInstance`  | Histogram       | `DBInstanceIdentifier` |
| `StorageNetworkThroughput`         | `StorageNetworkThroughputByInstance`         | Histogram       | `DBInstanceIdentifier` |
| `StorageNetworkTransmitThroughput` | `StorageNetworkTransmitThroughputByInstance` | Histogram       | `DBInstanceIdentifier` |
| `StsGetCallerIdentityCalls`        | `StsGetCallerIdentityCallsByInstance`        | Histogram       | `DBInstanceIdentifier` |
| `StsMaxConcurrentRequests`         | `StsMaxConcurrentRequestsByInstance`         | Histogram       | `DBInstanceIdentifier` |
| `SwapUsage`                        | `SwapUsageByInstance`                        | Histogram       | `DBInstanceIdentifier` |
| `TTLDeletedDocuments`              | `TTLDeletedDocumentsByInstance`              | Sum             | `DBInstanceIdentifier` |
| `TransactionsAborted`              | `TransactionsAbortedByInstance`              | Sum             | `DBInstanceIdentifier` |
| `TransactionsCommitted`            | `TransactionsCommittedByInstance`            | Sum             | `DBInstanceIdentifier` |
| `TransactionsOpen`                 | `TransactionsOpenByInstance`                 | Histogram       | `DBInstanceIdentifier` |
| `TransactionsOpenLimit`            | `TransactionsOpenLimitByInstance`            | Histogram       | `DBInstanceIdentifier` |
| `TransactionsOpenMax`              | `TransactionsOpenMaxByInstance`              | Histogram       | `DBInstanceIdentifier` |
| `TransactionsStarted`              | `TransactionsStartedByInstance`              | Sum             | `DBInstanceIdentifier` |
| `WriteIOPS`                        | `WriteIOPSByInstance`                        | Histogram       | `DBInstanceIdentifier` |
| `WriteIOPSNVMeStorage`             | `WriteIOPSNVMeStorageByInstance`             | Histogram       | `DBInstanceIdentifier` |
| `WriteLatency`                     | `WriteLatencyByInstance`                     | Histogram       | `DBInstanceIdentifier` |
| `WriteLatencyNVMeStorage`          | `WriteLatencyNVMeStorageByInstance`          | Histogram       | `DBInstanceIdentifier` |
| `WriteThroughput`                  | `WriteThroughputByInstance`                  | Histogram       | `DBInstanceIdentifier` |
| `WriteThroughputNVMeStorage`       | `WriteThroughputNVMeStorageByInstance`       | Histogram       | `DBInstanceIdentifier` |

## AWS/DocDB-Elastic

The `AWS/DocDB-Elastic` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/docdb-elastic`. All enriched instruments use Delta temporality.

- [AWS::DocDBElastic::Cluster](#otel-enrichment-aws-docdb-elastic-aws-docdbelastic-cluster "#otel-enrichment-aws-docdb-elastic-aws-docdbelastic-cluster")

### AWS::DocDBElastic::Cluster

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                          | OpenTelemetry metric                   | Instrument type | Data point attributes                 |
| ------------------------------- | -------------------------------------- | --------------- | ------------------------------------- |
| `BufferCacheHitRatio`           | `BufferCacheHitRatio`                  | Histogram       | `ClusterId`, `ClusterName`            |
| `BufferCacheHitRatio`           | `BufferCacheHitRatioByShard`           | Histogram       | `ClusterId`, `ClusterName`, `ShardId` |
| `DatabaseConnections`           | `DatabaseConnections`                  | Histogram       | `ClusterId`, `ClusterName`            |
| `DatabaseConnections`           | `DatabaseConnectionsByShard`           | Histogram       | `ClusterId`, `ClusterName`, `ShardId` |
| `DatabaseCursorsMax`            | `DatabaseCursorsMax`                   | Histogram       | `ClusterId`, `ClusterName`            |
| `DatabaseCursorsMax`            | `DatabaseCursorsMaxByShard`            | Histogram       | `ClusterId`, `ClusterName`, `ShardId` |
| `DatabaseCursorsTimedOut`       | `DatabaseCursorsTimedOut`              | Sum             | `ClusterId`, `ClusterName`            |
| `DatabaseCursorsTimedOut`       | `DatabaseCursorsTimedOutByShard`       | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `DocumentsDeleted`              | `DocumentsDeleted`                     | Sum             | `ClusterId`, `ClusterName`            |
| `DocumentsDeleted`              | `DocumentsDeletedByShard`              | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `DocumentsInserted`             | `DocumentsInserted`                    | Sum             | `ClusterId`, `ClusterName`            |
| `DocumentsInserted`             | `DocumentsInsertedByShard`             | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `DocumentsReturned`             | `DocumentsReturned`                    | Sum             | `ClusterId`, `ClusterName`            |
| `DocumentsReturned`             | `DocumentsReturnedByShard`             | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `DocumentsUpdated`              | `DocumentsUpdated`                     | Sum             | `ClusterId`, `ClusterName`            |
| `DocumentsUpdated`              | `DocumentsUpdatedByShard`              | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `OpcountersCommand`             | `OpcountersCommand`                    | Sum             | `ClusterId`, `ClusterName`            |
| `OpcountersCommand`             | `OpcountersCommandByShard`             | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `OpcountersDelete`              | `OpcountersDelete`                     | Sum             | `ClusterId`, `ClusterName`            |
| `OpcountersDelete`              | `OpcountersDeleteByShard`              | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `OpcountersGetmore`             | `OpcountersGetmore`                    | Sum             | `ClusterId`, `ClusterName`            |
| `OpcountersGetmore`             | `OpcountersGetmoreByShard`             | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `OpcountersInsert`              | `OpcountersInsert`                     | Sum             | `ClusterId`, `ClusterName`            |
| `OpcountersInsert`              | `OpcountersInsertByShard`              | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `OpcountersQuery`               | `OpcountersQuery`                      | Sum             | `ClusterId`, `ClusterName`            |
| `OpcountersQuery`               | `OpcountersQueryByShard`               | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `OpcountersUpdate`              | `OpcountersUpdate`                     | Sum             | `ClusterId`, `ClusterName`            |
| `OpcountersUpdate`              | `OpcountersUpdateByShard`              | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `PrimaryInstanceCPUUtilization` | `PrimaryInstanceCPUUtilization`        | Histogram       | `ClusterId`, `ClusterName`            |
| `PrimaryInstanceCPUUtilization` | `PrimaryInstanceCPUUtilizationByShard` | Histogram       | `ClusterId`, `ClusterName`, `ShardId` |
| `PrimaryInstanceFreeableMemory` | `PrimaryInstanceFreeableMemory`        | Histogram       | `ClusterId`, `ClusterName`            |
| `PrimaryInstanceFreeableMemory` | `PrimaryInstanceFreeableMemoryByShard` | Histogram       | `ClusterId`, `ClusterName`, `ShardId` |
| `ReadThroughput`                | `ReadThroughput`                       | Histogram       | `ClusterId`, `ClusterName`            |
| `ReadThroughput`                | `ReadThroughputByShard`                | Histogram       | `ClusterId`, `ClusterName`, `ShardId` |
| `TTLDeletedDocuments`           | `TTLDeletedDocuments`                  | Sum             | `ClusterId`, `ClusterName`            |
| `TTLDeletedDocuments`           | `TTLDeletedDocumentsByShard`           | Sum             | `ClusterId`, `ClusterName`, `ShardId` |
| `VolumeBytesUsed`               | `VolumeBytesUsed`                      | Histogram       | `ClusterId`, `ClusterName`            |
| `VolumeBytesUsed`               | `VolumeBytesUsedByShard`               | Histogram       | `ClusterId`, `ClusterName`, `ShardId` |
| `VolumeReadIOPs`                | `VolumeReadIOPs`                       | Histogram       | `ClusterId`, `ClusterName`            |
| `VolumeReadIOPs`                | `VolumeReadIOPsByShard`                | Histogram       | `ClusterId`, `ClusterName`, `ShardId` |
| `VolumeWriteIOPs`               | `VolumeWriteIOPs`                      | Histogram       | `ClusterId`, `ClusterName`            |
| `VolumeWriteIOPs`               | `VolumeWriteIOPsByShard`               | Histogram       | `ClusterId`, `ClusterName`, `ShardId` |
| `WriteThroughput`               | `WriteThroughput`                      | Histogram       | `ClusterId`, `ClusterName`            |
| `WriteThroughput`               | `WriteThroughputByShard`               | Histogram       | `ClusterId`, `ClusterName`, `ShardId` |

## AWS/DynamoDB

The `AWS/DynamoDB` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/dynamodb`. All enriched instruments use Delta temporality.

- [AWS::DynamoDB::GlobalTable](#otel-enrichment-aws-dynamodb-aws-dynamodb-globaltable "#otel-enrichment-aws-dynamodb-aws-dynamodb-globaltable")
- [AWS::DynamoDB::Table](#otel-enrichment-aws-dynamodb-aws-dynamodb-table "#otel-enrichment-aws-dynamodb-aws-dynamodb-table")
- [index](#otel-enrichment-aws-dynamodb-index "#otel-enrichment-aws-dynamodb-index")
- [stream](#otel-enrichment-aws-dynamodb-stream "#otel-enrichment-aws-dynamodb-stream")

### AWS::DynamoDB::GlobalTable

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                    | OpenTelemetry metric      | Instrument type | Data point attributes                          |
| ------------------------- | ------------------------- | --------------- | ---------------------------------------------- |
| `PendingReplicationCount` | `PendingReplicationCount` | Histogram       | `ReceivingRegion`, `TableName`                 |
| `ReplicationLag`          | `ReplicationLag`          | Histogram       | `ReceivingRegion`, `SourceRegion`, `TableName` |
| `ReplicationLatency`      | `ReplicationLatency`      | Histogram       | `ReceivingRegion`, `TableName`                 |

### AWS::DynamoDB::Table

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                           | OpenTelemetry metric             | Instrument type | Data point attributes             |
| -------------------------------- | -------------------------------- | --------------- | --------------------------------- |
| `AgeOfOldestUnreplicatedRecord`  | `AgeOfOldestUnreplicatedRecord`  | Histogram       | `DelegatedOperation`, `TableName` |
| `ConditionalCheckFailedRequests` | `ConditionalCheckFailedRequests` | Sum             | `TableName`                       |
| `ConsumedChangeDataCaptureUnits` | `ConsumedChangeDataCaptureUnits` | Sum             | `DelegatedOperation`, `TableName` |
| `ConsumedReadCapacityUnits`      | `ConsumedReadCapacityUnits`      | Sum             | `TableName`                       |
| `ConsumedWriteCapacityUnits`     | `ConsumedWriteCapacityUnits`     | Sum             | `TableName`                       |
| `ProvisionedReadCapacityUnits`   | `ProvisionedReadCapacityUnits`   | Histogram       | `TableName`                       |
| `ProvisionedWriteCapacityUnits`  | `ProvisionedWriteCapacityUnits`  | Histogram       | `TableName`                       |
| `ReadThrottleEvents`             | `ReadThrottleEvents`             | Sum             | `TableName`                       |
| `ReturnedItemCount`              | `ReturnedItemCount`              | Histogram       | `Operation`, `TableName`          |
| `SuccessfulRequestLatency`       | `SuccessfulRequestLatency`       | Histogram       | `Operation`, `TableName`          |
| `SystemErrors`                   | `SystemErrors`                   | Sum             | `Operation`, `TableName`          |
| `ThrottledPutRecordCount`        | `ThrottledPutRecordCount`        | Sum             | `DelegatedOperation`, `TableName` |
| `ThrottledRequests`              | `ThrottledRequests`              | Sum             | `Operation`, `TableName`          |
| `TimeToLiveDeletedItemCount`     | `TimeToLiveDeletedItemCount`     | Sum             | `TableName`                       |
| `TransactionConflict`            | `TransactionConflict`            | Sum             | `TableName`                       |
| `WriteThrottleEvents`            | `WriteThrottleEvents`            | Sum             | `TableName`                       |

### `index`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                             | OpenTelemetry metric               | Instrument type | Data point attributes                   |
| ---------------------------------- | ---------------------------------- | --------------- | --------------------------------------- |
| `OnlineIndexConsumedWriteCapacity` | `OnlineIndexConsumedWriteCapacity` | Sum             | `GlobalSecondaryIndexName`, `TableName` |
| `OnlineIndexPercentageProgress`    | `OnlineIndexPercentageProgress`    | Histogram       | `GlobalSecondaryIndexName`, `TableName` |
| `OnlineIndexThrottleEvents`        | `OnlineIndexThrottleEvents`        | Sum             | `GlobalSecondaryIndexName`, `TableName` |

### `stream`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                 | OpenTelemetry metric   | Instrument type | Data point attributes                   |
| ---------------------- | ---------------------- | --------------- | --------------------------------------- |
| `ReturnedBytes`        | `ReturnedBytes`        | Histogram       | `Operation`, `StreamLabel`, `TableName` |
| `ReturnedRecordsCount` | `ReturnedRecordsCount` | Histogram       | `Operation`, `StreamLabel`, `TableName` |

## AWS/EBS

The `AWS/EBS` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/ec2`. All enriched instruments use Delta temporality.

- [AWS::EC2::Volume](#otel-enrichment-aws-ebs-aws-ec2-volume "#otel-enrichment-aws-ebs-aws-ec2-volume")
- [snapshot](#otel-enrichment-aws-ebs-snapshot "#otel-enrichment-aws-ebs-snapshot")

### AWS::EC2::Volume

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                          | OpenTelemetry metric            | Instrument type | Data point attributes    |
| ------------------------------- | ------------------------------- | --------------- | ------------------------ |
| `BurstBalance`                  | `BurstBalance`                  | Histogram       | `VolumeId`               |
| `VolumeAvgIOPS`                 | `VolumeAvgIOPS`                 | Histogram       | `InstanceId`, `VolumeId` |
| `VolumeAvgReadLatency`          | `VolumeAvgReadLatency`          | Histogram       | `InstanceId`, `VolumeId` |
| `VolumeAvgThroughput`           | `VolumeAvgThroughput`           | Histogram       | `InstanceId`, `VolumeId` |
| `VolumeAvgWriteLatency`         | `VolumeAvgWriteLatency`         | Histogram       | `InstanceId`, `VolumeId` |
| `VolumeConsumedReadWriteOps`    | `VolumeConsumedReadWriteOps`    | Sum             | `VolumeId`               |
| `VolumeIOPSExceededCheck`       | `VolumeIOPSExceededCheck`       | Histogram       | `InstanceId`, `VolumeId` |
| `VolumeIdleTime`                | `VolumeIdleTime`                | Sum             | `VolumeId`               |
| `VolumeQueueLength`             | `VolumeQueueLength`             | Histogram       | `VolumeId`               |
| `VolumeReadBytes`               | `VolumeReadBytes`               | Sum             | `VolumeId`               |
| `VolumeReadOps`                 | `VolumeReadOps`                 | Sum             | `VolumeId`               |
| `VolumeStalledIOCheck`          | `VolumeStalledIOCheck`          | Histogram       | `InstanceId`, `VolumeId` |
| `VolumeThroughputExceededCheck` | `VolumeThroughputExceededCheck` | Histogram       | `InstanceId`, `VolumeId` |
| `VolumeThroughputPercentage`    | `VolumeThroughputPercentage`    | Histogram       | `VolumeId`               |
| `VolumeTotalReadTime`           | `VolumeTotalReadTime`           | Sum             | `VolumeId`               |
| `VolumeTotalWriteTime`          | `VolumeTotalWriteTime`          | Sum             | `VolumeId`               |
| `VolumeWriteBytes`              | `VolumeWriteBytes`              | Sum             | `VolumeId`               |
| `VolumeWriteOps`                | `VolumeWriteOps`                | Sum             | `VolumeId`               |

### `snapshot`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                                 | OpenTelemetry metric                   | Instrument type | Data point attributes            |
| -------------------------------------- | -------------------------------------- | --------------- | -------------------------------- |
| `FastSnapshotRestoreCreditsBalance`    | `FastSnapshotRestoreCreditsBalance`    | Histogram       | `AvailabilityZone`, `SnapshotId` |
| `FastSnapshotRestoreCreditsBucketSize` | `FastSnapshotRestoreCreditsBucketSize` | Histogram       | `AvailabilityZone`, `SnapshotId` |

## AWS/EC2

The `AWS/EC2` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/ec2`. All enriched instruments use Delta temporality.

- [AWS::EC2::Host](#otel-enrichment-aws-ec2-aws-ec2-host "#otel-enrichment-aws-ec2-aws-ec2-host")
- [AWS::EC2::Instance](#otel-enrichment-aws-ec2-aws-ec2-instance "#otel-enrichment-aws-ec2-aws-ec2-instance")
- [AWS::EC2::VPC](#otel-enrichment-aws-ec2-aws-ec2-vpc "#otel-enrichment-aws-ec2-aws-ec2-vpc")
- [image](#otel-enrichment-aws-ec2-image "#otel-enrichment-aws-ec2-image")

### AWS::EC2::Host

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                        | OpenTelemetry metric          | Instrument type | Data point attributes |
| ----------------------------- | ----------------------------- | --------------- | --------------------- |
| `DedicatedHostCPUUtilization` | `DedicatedHostCPUUtilization` | Histogram       | `HostId`              |

### AWS::EC2::Instance

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                               | OpenTelemetry metric                 | Instrument type | Data point attributes                                                                                                                                                      |
| ------------------------------------ | ------------------------------------ | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CPUCreditBalance`                   | `CPUCreditBalance`                   | Histogram       | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `CPUCreditUsage`                     | `CPUCreditUsage`                     | Histogram       | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `CPUSurplusCreditBalance`            | `CPUSurplusCreditBalance`            | Histogram       | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `CPUSurplusCreditsCharged`           | `CPUSurplusCreditsCharged`           | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `CPUUtilization`                     | `CPUUtilization`                     | Histogram       | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `DiskReadBytes`                      | `DiskReadBytes`                      | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `DiskReadOps`                        | `DiskReadOps`                        | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `DiskWriteBytes`                     | `DiskWriteBytes`                     | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `DiskWriteOps`                       | `DiskWriteOps`                       | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `EBSByteBalance%`                    | `EBSByteBalance%`                    | Histogram       | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `EBSIOBalance%`                      | `EBSIOBalance%`                      | Histogram       | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `EBSReadBytes`                       | `EBSReadBytes`                       | Sum             | `InstanceId`                                                                                                                                                               |
| `EBSReadOps`                         | `EBSReadOps`                         | Sum             | `InstanceId`                                                                                                                                                               |
| `EBSWriteBytes`                      | `EBSWriteBytes`                      | Sum             | `InstanceId`                                                                                                                                                               |
| `EBSWriteOps`                        | `EBSWriteOps`                        | Sum             | `InstanceId`                                                                                                                                                               |
| `GPUPowerUtilization`                | `GPUPowerUtilization`                | Histogram       | `InstanceId`                                                                                                                                                               |
| `InstanceEBSIOPSExceededCheck`       | `InstanceEBSIOPSExceededCheck`       | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `InstanceEBSThroughputExceededCheck` | `InstanceEBSThroughputExceededCheck` | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `MetadataNoToken`                    | `MetadataNoToken`                    | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `MetadataNoTokenRejected`            | `MetadataNoTokenRejected`            | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `NetworkIn`                          | `NetworkIn`                          | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `NetworkMirrorIn`                    | `NetworkMirrorIn`                    | Sum             | `InstanceId`                                                                                                                                                               |
| `NetworkMirrorOut`                   | `NetworkMirrorOut`                   | Sum             | `InstanceId`                                                                                                                                                               |
| `NetworkOut`                         | `NetworkOut`                         | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `NetworkPacketsIn`                   | `NetworkPacketsIn`                   | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `NetworkPacketsMirrorIn`             | `NetworkPacketsMirrorIn`             | Sum             | `InstanceId`                                                                                                                                                               |
| `NetworkPacketsMirrorOut`            | `NetworkPacketsMirrorOut`            | Sum             | `InstanceId`                                                                                                                                                               |
| `NetworkPacketsOut`                  | `NetworkPacketsOut`                  | Sum             | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `NetworkPacketsSkipMirrorIn`         | `NetworkPacketsSkipMirrorIn`         | Sum             | `InstanceId`                                                                                                                                                               |
| `NetworkPacketsSkipMirrorOut`        | `NetworkPacketsSkipMirrorOut`        | Sum             | `InstanceId`                                                                                                                                                               |
| `NetworkSkipMirrorIn`                | `NetworkSkipMirrorIn`                | Sum             | `InstanceId`                                                                                                                                                               |
| `NetworkSkipMirrorOut`               | `NetworkSkipMirrorOut`               | Sum             | `InstanceId`                                                                                                                                                               |
| `StatusCheckFailed`                  | `StatusCheckFailed`                  | Histogram       | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `StatusCheckFailed_Application`      | `StatusCheckFailed_Application`      | Histogram       | `InstanceId`                                                                                                                                                               |
| `StatusCheckFailed_AttachedEBS`      | `StatusCheckFailed_AttachedEBS`      | Histogram       | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `StatusCheckFailed_Instance`         | `StatusCheckFailed_Instance`         | Histogram       | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |
| `StatusCheckFailed_System`           | `StatusCheckFailed_System`           | Histogram       | • `AutoScalingGroupName`, `ImageId`, `InstanceId`, `InstanceType`<br>• `AutoScalingGroupName`, `InstanceId`<br>• `ImageId`, `InstanceId`, `InstanceType`<br>• `InstanceId` |

### AWS::EC2::VPC

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                      | OpenTelemetry metric        | Instrument type | Data point attributes |
| --------------------------- | --------------------------- | --------------- | --------------------- |
| `NetworkAddressUsage`       | `NetworkAddressUsage`       | Histogram       | `Per-VPC Metrics`     |
| `NetworkAddressUsagePeered` | `NetworkAddressUsagePeered` | Histogram       | `Per-VPC Metrics`     |

### `image`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                                 | OpenTelemetry metric                   | Instrument type | Data point attributes  |
| -------------------------------------- | -------------------------------------- | --------------- | ---------------------- |
| `CPUUtilization`                       | `CPUUtilization`                       | Histogram       | `ImageId`              |
| `DiskReadBytes`                        | `DiskReadBytes`                        | Sum             | `ImageId`              |
| `DiskReadOps`                          | `DiskReadOps`                          | Sum             | `ImageId`              |
| `DiskWriteBytes`                       | `DiskWriteBytes`                       | Sum             | `ImageId`              |
| `DiskWriteOps`                         | `DiskWriteOps`                         | Sum             | `ImageId`              |
| `NetworkIn`                            | `NetworkIn`                            | Sum             | `ImageId`              |
| `NetworkOut`                           | `NetworkOut`                           | Sum             | `ImageId`              |
| `NumberOfAvailableFastLaunchSnapshots` | `NumberOfAvailableFastLaunchSnapshots` | Histogram       | `ImageId`, `ImageName` |

## AWS/EC2CapacityReservations

The `AWS/EC2CapacityReservations` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/ec2`. All enriched instruments use Delta temporality.

- [AWS::EC2::CapacityReservation](#otel-enrichment-aws-ec2capacityreservations-aws-ec2-capacityreservation "#otel-enrichment-aws-ec2capacityreservations-aws-ec2-capacityreservation")

### AWS::EC2::CapacityReservation

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                   | OpenTelemetry metric     | Instrument type | Data point attributes   |
| ------------------------ | ------------------------ | --------------- | ----------------------- |
| `AvailableInstanceCount` | `AvailableInstanceCount` | Histogram       | `CapacityReservationId` |
| `InstanceUtilization`    | `InstanceUtilization`    | Histogram       | `CapacityReservationId` |
| `TotalInstanceCount`     | `TotalInstanceCount`     | Histogram       | `CapacityReservationId` |
| `UsedInstanceCount`      | `UsedInstanceCount`      | Histogram       | `CapacityReservationId` |

## AWS/EFS

The `AWS/EFS` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/elasticfilesystem`. All enriched instruments use Delta temporality.

- [AWS::EFS::FileSystem](#otel-enrichment-aws-efs-aws-efs-filesystem "#otel-enrichment-aws-efs-aws-efs-filesystem")

### AWS::EFS::FileSystem

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                | OpenTelemetry metric  | Instrument type | Data point attributes                     |
| --------------------- | --------------------- | --------------- | ----------------------------------------- |
| `BurstCreditBalance`  | `BurstCreditBalance`  | Histogram       | `FileSystemId`                            |
| `ClientConnections`   | `ClientConnections`   | Histogram       | `FileSystemId`                            |
| `DataReadIOBytes`     | `DataReadIOBytes`     | Sum             | `FileSystemId`                            |
| `DataWriteIOBytes`    | `DataWriteIOBytes`    | Sum             | `FileSystemId`                            |
| `MetadataIOBytes`     | `MetadataIOBytes`     | Sum             | `FileSystemId`                            |
| `MeteredIOBytes`      | `MeteredIOBytes`      | Sum             | `FileSystemId`                            |
| `PercentIOLimit`      | `PercentIOLimit`      | Histogram       | `FileSystemId`                            |
| `PermittedThroughput` | `PermittedThroughput` | Histogram       | `FileSystemId`                            |
| `StorageBytes`        | `StorageBytes`        | Histogram       | `FileSystemId`, `StorageClass`            |
| `TimeSinceLastSync`   | `TimeSinceLastSync`   | Histogram       | `DestinationFileSystemId`, `FileSystemId` |
| `TotalIOBytes`        | `TotalIOBytes`        | Sum             | `FileSystemId`                            |

## AWS/EKS

The `AWS/EKS` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/eks`. All enriched instruments use Delta temporality.

- [AWS::EKS::Cluster](#otel-enrichment-aws-eks-aws-eks-cluster "#otel-enrichment-aws-eks-aws-eks-cluster")

### AWS::EKS::Cluster

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                                   | OpenTelemetry metric                                     | Instrument type | Data point attributes |
| -------------------------------------------------------- | -------------------------------------------------------- | --------------- | --------------------- |
| `apiserver_admission_webhook_rejection_count_ADMIT`      | `apiserver_admission_webhook_rejection_count_ADMIT`      | Sum             | `ClusterName`         |
| `apiserver_admission_webhook_rejection_count_VALIDATING` | `apiserver_admission_webhook_rejection_count_VALIDATING` | Sum             | `ClusterName`         |
| `apiserver_admission_webhook_request_total`              | `apiserver_admission_webhook_request_total`              | Sum             | `ClusterName`         |
| `apiserver_admission_webhook_request_total_ADMIT`        | `apiserver_admission_webhook_request_total_ADMIT`        | Sum             | `ClusterName`         |
| `apiserver_admission_webhook_request_total_VALIDATING`   | `apiserver_admission_webhook_request_total_VALIDATING`   | Sum             | `ClusterName`         |
| `apiserver_current_inflight_requests_MUTATING`           | `apiserver_current_inflight_requests_MUTATING`           | Histogram       | `ClusterName`         |
| `apiserver_current_inflight_requests_READONLY`           | `apiserver_current_inflight_requests_READONLY`           | Histogram       | `ClusterName`         |
| `apiserver_flowcontrol_current_executing_seats`          | `apiserver_flowcontrol_current_executing_seats`          | Histogram       | `ClusterName`         |
| `apiserver_request_duration_seconds_DELETE_P99`          | `apiserver_request_duration_seconds_DELETE_P99`          | Histogram       | `ClusterName`         |
| `apiserver_request_duration_seconds_GET_P99`             | `apiserver_request_duration_seconds_GET_P99`             | Histogram       | `ClusterName`         |
| `apiserver_request_duration_seconds_LIST_P99`            | `apiserver_request_duration_seconds_LIST_P99`            | Histogram       | `ClusterName`         |
| `apiserver_request_duration_seconds_PATCH_P99`           | `apiserver_request_duration_seconds_PATCH_P99`           | Histogram       | `ClusterName`         |
| `apiserver_request_duration_seconds_POST_P99`            | `apiserver_request_duration_seconds_POST_P99`            | Histogram       | `ClusterName`         |
| `apiserver_request_duration_seconds_PUT_P99`             | `apiserver_request_duration_seconds_PUT_P99`             | Histogram       | `ClusterName`         |
| `apiserver_request_total`                                | `apiserver_request_total`                                | Sum             | `ClusterName`         |
| `apiserver_request_total_429`                            | `apiserver_request_total_429`                            | Sum             | `ClusterName`         |
| `apiserver_request_total_4XX`                            | `apiserver_request_total_4XX`                            | Sum             | `ClusterName`         |
| `apiserver_request_total_5XX`                            | `apiserver_request_total_5XX`                            | Sum             | `ClusterName`         |
| `apiserver_request_total_LIST_PODS`                      | `apiserver_request_total_LIST_PODS`                      | Sum             | `ClusterName`         |
| `apiserver_storage_size_bytes`                           | `apiserver_storage_size_bytes`                           | Histogram       | `ClusterName`         |
| `etcd_mvcc_db_total_size_in_use_in_bytes`                | `etcd_mvcc_db_total_size_in_use_in_bytes`                | Histogram       | `ClusterName`         |
| `scheduler_pending_pods`                                 | `scheduler_pending_pods`                                 | Histogram       | `ClusterName`         |
| `scheduler_pending_pods_ACTIVEQ`                         | `scheduler_pending_pods_ACTIVEQ`                         | Histogram       | `ClusterName`         |
| `scheduler_pending_pods_BACKOFF`                         | `scheduler_pending_pods_BACKOFF`                         | Histogram       | `ClusterName`         |
| `scheduler_pending_pods_GATED`                           | `scheduler_pending_pods_GATED`                           | Histogram       | `ClusterName`         |
| `scheduler_pending_pods_UNSCHEDULABLE`                   | `scheduler_pending_pods_UNSCHEDULABLE`                   | Histogram       | `ClusterName`         |
| `scheduler_schedule_attempts_ERROR`                      | `scheduler_schedule_attempts_ERROR`                      | Sum             | `ClusterName`         |
| `scheduler_schedule_attempts_SCHEDULED`                  | `scheduler_schedule_attempts_SCHEDULED`                  | Sum             | `ClusterName`         |
| `scheduler_schedule_attempts_UNSCHEDULABLE`              | `scheduler_schedule_attempts_UNSCHEDULABLE`              | Sum             | `ClusterName`         |
| `scheduler_schedule_attempts_total`                      | `scheduler_schedule_attempts_total`                      | Sum             | `ClusterName`         |

## AWS/ELB

The `AWS/ELB` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/elasticloadbalancing`. All enriched instruments use Delta temporality.

- [AWS::ElasticLoadBalancing::LoadBalancer](#otel-enrichment-aws-elb-aws-elasticloadbalancing-loadbalancer "#otel-enrichment-aws-elb-aws-elasticloadbalancing-loadbalancer")

### AWS::ElasticLoadBalancing::LoadBalancer

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                            | OpenTelemetry metric                              | Instrument type | Data point attributes                  |
| ------------------------------------------------- | ------------------------------------------------- | --------------- | -------------------------------------- |
| `BackendConnectionErrors`                         | `BackendConnectionErrors`                         | Sum             | `AvailabilityZone`, `LoadBalancerName` |
| `DesyncMitigationMode_NonCompliant_Request_Count` | `DesyncMitigationMode_NonCompliant_Request_Count` | Sum             | `AvailabilityZone`, `LoadBalancerName` |
| `HTTPCode_Backend_2XX`                            | `HTTPCode_Backend_2XX`                            | Sum             | `AvailabilityZone`, `LoadBalancerName` |
| `HTTPCode_Backend_3XX`                            | `HTTPCode_Backend_3XX`                            | Sum             | `AvailabilityZone`, `LoadBalancerName` |
| `HTTPCode_Backend_4XX`                            | `HTTPCode_Backend_4XX`                            | Sum             | `AvailabilityZone`, `LoadBalancerName` |
| `HTTPCode_Backend_5XX`                            | `HTTPCode_Backend_5XX`                            | Sum             | `AvailabilityZone`, `LoadBalancerName` |
| `HTTPCode_ELB_4XX`                                | `HTTPCode_ELB_4XX`                                | Sum             | `AvailabilityZone`, `LoadBalancerName` |
| `HTTPCode_ELB_5XX`                                | `HTTPCode_ELB_5XX`                                | Sum             | `AvailabilityZone`, `LoadBalancerName` |
| `HealthyHostCount`                                | `HealthyHostCount`                                | Histogram       | `AvailabilityZone`, `LoadBalancerName` |
| `Latency`                                         | `Latency`                                         | Histogram       | `AvailabilityZone`, `LoadBalancerName` |
| `RequestCount`                                    | `RequestCount`                                    | Sum             | `AvailabilityZone`, `LoadBalancerName` |
| `SpilloverCount`                                  | `SpilloverCount`                                  | Sum             | `AvailabilityZone`, `LoadBalancerName` |
| `SurgeQueueLength`                                | `SurgeQueueLength`                                | Histogram       | `AvailabilityZone`, `LoadBalancerName` |
| `UnHealthyHostCount`                              | `UnHealthyHostCount`                              | Histogram       | `AvailabilityZone`, `LoadBalancerName` |

## AWS/EMRServerless

The `AWS/EMRServerless` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/emr-serverless`. All enriched instruments use Delta temporality.

- [AWS::EMRServerless::Application](#otel-enrichment-aws-emrserverless-aws-emrserverless-application "#otel-enrichment-aws-emrserverless-aws-emrserverless-application")

### AWS::EMRServerless::Application

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                            | OpenTelemetry metric              | Instrument type | Data point attributes                                                                          |
| --------------------------------- | --------------------------------- | --------------- | ---------------------------------------------------------------------------------------------- |
| `CPUAllocated`                    | `CPUAllocated`                    | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`                     |
| `CancelledJobs`                   | `CancelledJobs`                   | Sum             | `ApplicationId`, `ApplicationName`                                                             |
| `CancellingJobs`                  | `CancellingJobs`                  | Histogram       | `ApplicationId`, `ApplicationName`                                                             |
| `FailedJobs`                      | `FailedJobs`                      | Sum             | `ApplicationId`, `ApplicationName`                                                             |
| `IdleWorkerCount`                 | `IdleWorkerCount`                 | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`                     |
| `MaxCPUAllowed`                   | `MaxCPUAllowed`                   | Histogram       | `ApplicationId`, `ApplicationName`                                                             |
| `MaxMemoryAllowed`                | `MaxMemoryAllowed`                | Histogram       | `ApplicationId`, `ApplicationName`                                                             |
| `MaxStorageAllowed`               | `MaxStorageAllowed`               | Histogram       | `ApplicationId`, `ApplicationName`                                                             |
| `MemoryAllocated`                 | `MemoryAllocated`                 | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`                     |
| `PendingCreationWorkerCount`      | `PendingCreationWorkerCount`      | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`                     |
| `PendingJobs`                     | `PendingJobs`                     | Histogram       | `ApplicationId`, `ApplicationName`                                                             |
| `RunningJobs`                     | `RunningJobs`                     | Histogram       | `ApplicationId`, `ApplicationName`                                                             |
| `RunningWorkerCount`              | `RunningWorkerCount`              | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`                     |
| `ScheduledJobs`                   | `ScheduledJobs`                   | Histogram       | `ApplicationId`, `ApplicationName`                                                             |
| `StorageAllocated`                | `StorageAllocated`                | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`                     |
| `SubmittedJobs`                   | `SubmittedJobs`                   | Sum             | `ApplicationId`, `ApplicationName`                                                             |
| `SuccessJobs`                     | `SuccessJobs`                     | Sum             | `ApplicationId`, `ApplicationName`                                                             |
| `TotalWorkerCount`                | `TotalWorkerCount`                | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`                     |
| `WorkerCpuAllocated`              | `WorkerCpuAllocated`              | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType` |
| `WorkerCpuUsed`                   | `WorkerCpuUsed`                   | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType` |
| `WorkerEphemeralStorageAllocated` | `WorkerEphemeralStorageAllocated` | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType` |
| `WorkerEphemeralStorageUsed`      | `WorkerEphemeralStorageUsed`      | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType` |
| `WorkerMemoryAllocated`           | `WorkerMemoryAllocated`           | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType` |
| `WorkerMemoryUsed`                | `WorkerMemoryUsed`                | Histogram       | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType` |
| `WorkerStorageReadBytes`          | `WorkerStorageReadBytes`          | Sum             | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType` |
| `WorkerStorageWriteBytes`         | `WorkerStorageWriteBytes`         | Sum             | `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType` |

## AWS/ES

The `AWS/ES` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/es`. All enriched instruments use Delta temporality.

- [AWS::OpenSearchService::Domain](#otel-enrichment-aws-es-aws-opensearchservice-domain "#otel-enrichment-aws-es-aws-opensearchservice-domain")

### AWS::OpenSearchService::Domain

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                                   | OpenTelemetry metric                                     | Instrument type | Data point attributes                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | --------------- | ------------------------------------------------------ |
| `2xx`                                                    | `2xx`                                                    | Sum             | `ClientId`, `DomainName`                               |
| `3xx`                                                    | `3xx`                                                    | Sum             | `ClientId`, `DomainName`                               |
| `4xx`                                                    | `4xx`                                                    | Sum             | `ClientId`, `DomainName`                               |
| `5xx`                                                    | `5xx`                                                    | Sum             | `ClientId`, `DomainName`                               |
| `ADAnomalyDetectorsIndexStatus.red`                      | `ADAnomalyDetectorsIndexStatus.red`                      | Histogram       | `ClientId`, `DomainName`                               |
| `ADAnomalyDetectorsIndexStatusIndexExists`               | `ADAnomalyDetectorsIndexStatusIndexExists`               | Histogram       | `ClientId`, `DomainName`                               |
| `ADAnomalyResultsIndexStatus.red`                        | `ADAnomalyResultsIndexStatus.red`                        | Histogram       | `ClientId`, `DomainName`                               |
| `ADAnomalyResultsIndexStatusIndexExists`                 | `ADAnomalyResultsIndexStatusIndexExists`                 | Histogram       | `ClientId`, `DomainName`                               |
| `ADExecuteFailureCount`                                  | `ADExecuteFailureCount`                                  | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ADExecuteRequestCount`                                  | `ADExecuteRequestCount`                                  | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ADHCExecuteFailureCount`                                | `ADHCExecuteFailureCount`                                | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ADHCExecuteRequestCount`                                | `ADHCExecuteRequestCount`                                | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ADModelsCheckpointIndexStatus.red`                      | `ADModelsCheckpointIndexStatus.red`                      | Histogram       | `ClientId`, `DomainName`                               |
| `ADModelsCheckpointIndexStatusIndexExists`               | `ADModelsCheckpointIndexStatusIndexExists`               | Histogram       | `ClientId`, `DomainName`                               |
| `ADPluginUnhealthy`                                      | `ADPluginUnhealthy`                                      | Histogram       | `ClientId`, `DomainName`                               |
| `ActiveDataNode`                                         | `ActiveDataNode`                                         | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `AlertingDegraded`                                       | `AlertingDegraded`                                       | Histogram       | `ClientId`, `DomainName`                               |
| `AlertingIndexExists`                                    | `AlertingIndexExists`                                    | Histogram       | `ClientId`, `DomainName`                               |
| `AlertingIndexStatus.green`                              | `AlertingIndexStatus.green`                              | Histogram       | `ClientId`, `DomainName`                               |
| `AlertingIndexStatus.red`                                | `AlertingIndexStatus.red`                                | Histogram       | `ClientId`, `DomainName`                               |
| `AlertingIndexStatus.yellow`                             | `AlertingIndexStatus.yellow`                             | Histogram       | `ClientId`, `DomainName`                               |
| `AlertingNodesNotOnSchedule`                             | `AlertingNodesNotOnSchedule`                             | Histogram       | `ClientId`, `DomainName`                               |
| `AlertingNodesOnSchedule`                                | `AlertingNodesOnSchedule`                                | Histogram       | `ClientId`, `DomainName`                               |
| `AlertingScheduledJobEnabled`                            | `AlertingScheduledJobEnabled`                            | Histogram       | `ClientId`, `DomainName`                               |
| `AsyncQueryCancelApiFailedRequestCusErrCount`            | `AsyncQueryCancelApiFailedRequestCusErrCount`            | Sum             | `ClientId`, `DomainName`                               |
| `AsyncQueryCancelApiFailedRequestSysErrCount`            | `AsyncQueryCancelApiFailedRequestSysErrCount`            | Sum             | `ClientId`, `DomainName`                               |
| `AsyncQueryCancelApiRequestCount`                        | `AsyncQueryCancelApiRequestCount`                        | Sum             | `ClientId`, `DomainName`                               |
| `AsyncQueryCreateApiFailedRequestCusErrCount`            | `AsyncQueryCreateApiFailedRequestCusErrCount`            | Sum             | `ClientId`, `DomainName`                               |
| `AsyncQueryCreateApiFailedRequestSysErrCount`            | `AsyncQueryCreateApiFailedRequestSysErrCount`            | Sum             | `ClientId`, `DomainName`                               |
| `AsyncQueryCreateApiRequestCount`                        | `AsyncQueryCreateApiRequestCount`                        | Sum             | `ClientId`, `DomainName`                               |
| `AsyncQueryGetApiFailedRequestCusErrCount`               | `AsyncQueryGetApiFailedRequestCusErrCount`               | Sum             | `ClientId`, `DomainName`                               |
| `AsyncQueryGetApiFailedRequestSysErrCount`               | `AsyncQueryGetApiFailedRequestSysErrCount`               | Sum             | `ClientId`, `DomainName`                               |
| `AsyncQueryGetApiRequestCount`                           | `AsyncQueryGetApiRequestCount`                           | Sum             | `ClientId`, `DomainName`                               |
| `AsynchronousSearchCancelled`                            | `AsynchronousSearchCancelled`                            | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `AsynchronousSearchCompletionRate`                       | `AsynchronousSearchCompletionRate`                       | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `AsynchronousSearchFailureRate`                          | `AsynchronousSearchFailureRate`                          | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `AsynchronousSearchInitializedRate`                      | `AsynchronousSearchInitializedRate`                      | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `AsynchronousSearchPersistFailedRate`                    | `AsynchronousSearchPersistFailedRate`                    | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `AsynchronousSearchPersistRate`                          | `AsynchronousSearchPersistRate`                          | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `AsynchronousSearchRejected`                             | `AsynchronousSearchRejected`                             | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `AsynchronousSearchRunningCurrent`                       | `AsynchronousSearchRunningCurrent`                       | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `AsynchronousSearchStoreHealthRed`                       | `AsynchronousSearchStoreHealthRed`                       | Histogram       | `ClientId`, `DomainName`                               |
| `AsynchronousSearchStoreSize`                            | `AsynchronousSearchStoreSize`                            | Histogram       | `ClientId`, `DomainName`                               |
| `AsynchronousSearchStoredResponseCount`                  | `AsynchronousSearchStoredResponseCount`                  | Histogram       | `ClientId`, `DomainName`                               |
| `AsynchronousSearchSubmissionRate`                       | `AsynchronousSearchSubmissionRate`                       | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `AutoFollowLeaderCallFailure`                            | `AutoFollowLeaderCallFailure`                            | Histogram       | `ClientId`, `DomainName`, `LeaderAlias`                |
| `AutoFollowNumFailedStartReplication`                    | `AutoFollowNumFailedStartReplication`                    | Sum             | `ClientId`, `DomainName`, `LeaderAlias`                |
| `AutoFollowNumSuccessStartReplication`                   | `AutoFollowNumSuccessStartReplication`                   | Sum             | `ClientId`, `DomainName`                               |
| `AutoTuneChangesHistoryHeapSize`                         | `AutoTuneChangesHistoryHeapSize`                         | Histogram       | `AutotuningType`, `ClientId`, `DomainName`, `TargetId` |
| `AutoTuneFailed`                                         | `AutoTuneFailed`                                         | Sum             | `AutotuningType`, `ClientId`, `DomainName`, `TargetId` |
| `AutoTuneSucceeded`                                      | `AutoTuneSucceeded`                                      | Sum             | `AutotuningType`, `ClientId`, `DomainName`, `TargetId` |
| `AutoTuneValue`                                          | `AutoTuneValue`                                          | Histogram       | `AutotuningType`, `ClientId`, `DomainName`, `TargetId` |
| `AutomatedSnapshotFailure`                               | `AutomatedSnapshotFailure`                               | Histogram       | `ClientId`, `DomainName`                               |
| `AvgPointInTimeAliveTime`                                | `AvgPointInTimeAliveTime`                                | Histogram       | `ClientId`, `DomainName`                               |
| `BurstBalance`                                           | `BurstBalance`                                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CPUCreditBalance`                                       | `CPUCreditBalance`                                       | Histogram       | `ClientId`, `DomainName`                               |
| `CPUUtilization`                                         | `CPUUtilization`                                         | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CanMatchCurrent`                                        | `CanMatchCurrent`                                        | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CanMatchTimeInMillis`                                   | `CanMatchTimeInMillis`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CanMatchTotal`                                          | `CanMatchTotal`                                          | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ClusterIndexWritesBlocked`                              | `ClusterIndexWritesBlocked`                              | Histogram       | `ClientId`, `DomainName`                               |
| `ClusterStatus.green`                                    | `ClusterStatus.green`                                    | Histogram       | `ClientId`, `DomainName`                               |
| `ClusterStatus.red`                                      | `ClusterStatus.red`                                      | Histogram       | `ClientId`, `DomainName`                               |
| `ClusterStatus.yellow`                                   | `ClusterStatus.yellow`                                   | Histogram       | `ClientId`, `DomainName`                               |
| `ClusterUsedSpace`                                       | `ClusterUsedSpace`                                       | Histogram       | `ClientId`, `DomainName`                               |
| `ColdStorageSpaceUtilization`                            | `ColdStorageSpaceUtilization`                            | Histogram       | `ClientId`, `DomainName`                               |
| `ColdToWarmMigrationFailureCount`                        | `ColdToWarmMigrationFailureCount`                        | Sum             | `ClientId`, `DomainName`                               |
| `ColdToWarmMigrationLatency`                             | `ColdToWarmMigrationLatency`                             | Histogram       | `ClientId`, `DomainName`                               |
| `ColdToWarmMigrationQueueSize`                           | `ColdToWarmMigrationQueueSize`                           | Histogram       | `ClientId`, `DomainName`                               |
| `ColdToWarmMigrationSuccessCount`                        | `ColdToWarmMigrationSuccessCount`                        | Sum             | `ClientId`, `DomainName`                               |
| `ComponentTemplateCount`                                 | `ComponentTemplateCount`                                 | Histogram       | `ClientId`, `DomainName`                               |
| `ConcurrentSearchLatency`                                | `ConcurrentSearchLatency`                                | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ConcurrentSearchRate`                                   | `ConcurrentSearchRate`                                   | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatingWriteRejected`                              | `CoordinatingWriteRejected`                              | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorCPUUtilization`                              | `CoordinatorCPUUtilization`                              | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorFreeStorageSpace`                            | `CoordinatorFreeStorageSpace`                            | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorJVMGCOldCollectionCount`                     | `CoordinatorJVMGCOldCollectionCount`                     | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorJVMGCOldCollectionTime`                      | `CoordinatorJVMGCOldCollectionTime`                      | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorJVMGCYoungCollectionCount`                   | `CoordinatorJVMGCYoungCollectionCount`                   | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorJVMGCYoungCollectionTime`                    | `CoordinatorJVMGCYoungCollectionTime`                    | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorJVMMemoryPressure`                           | `CoordinatorJVMMemoryPressure`                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorOldGenJVMMemoryPressure`                     | `CoordinatorOldGenJVMMemoryPressure`                     | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorSysMemoryUtilization`                        | `CoordinatorSysMemoryUtilization`                        | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolForce_mergeQueue`                  | `CoordinatorThreadpoolForce_mergeQueue`                  | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolForce_mergeRejected`               | `CoordinatorThreadpoolForce_mergeRejected`               | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolForce_mergeThreads`                | `CoordinatorThreadpoolForce_mergeThreads`                | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolIndexQueue`                        | `CoordinatorThreadpoolIndexQueue`                        | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolIndexRejected`                     | `CoordinatorThreadpoolIndexRejected`                     | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolIndexThreads`                      | `CoordinatorThreadpoolIndexThreads`                      | Histogram       | `ClientId`, `DomainName`                               |
| `CoordinatorThreadpoolOpendistro_monitor_runnerQueue`    | `CoordinatorThreadpoolOpendistro_monitor_runnerQueue`    | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolOpendistro_monitor_runnerRejected` | `CoordinatorThreadpoolOpendistro_monitor_runnerRejected` | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolOpendistro_monitor_runnerThreads`  | `CoordinatorThreadpoolOpendistro_monitor_runnerThreads`  | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolSearchQueue`                       | `CoordinatorThreadpoolSearchQueue`                       | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolSearchRejected`                    | `CoordinatorThreadpoolSearchRejected`                    | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolSearchThreads`                     | `CoordinatorThreadpoolSearchThreads`                     | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolWriteQueue`                        | `CoordinatorThreadpoolWriteQueue`                        | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolWriteRejected`                     | `CoordinatorThreadpoolWriteRejected`                     | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolWriteThreads`                      | `CoordinatorThreadpoolWriteThreads`                      | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolsql-workerQueue`                   | `CoordinatorThreadpoolsql-workerQueue`                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolsql-workerRejected`                | `CoordinatorThreadpoolsql-workerRejected`                | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `CoordinatorThreadpoolsql-workerThreads`                 | `CoordinatorThreadpoolsql-workerThreads`                 | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `CrossClusterInboundReplicationRequests`                 | `CrossClusterInboundReplicationRequests`                 | Sum             | `ClientId`, `ConnectionId`, `DomainName`               |
| `CrossClusterInboundRequests`                            | `CrossClusterInboundRequests`                            | Sum             | `ClientId`, `ConnectionId`, `DomainName`               |
| `CrossClusterInboundSearchRequests`                      | `CrossClusterInboundSearchRequests`                      | Sum             | `ClientId`, `ConnectionId`, `DomainName`               |
| `CrossClusterOutboundConnections`                        | `CrossClusterOutboundConnections`                        | Histogram       | `ClientId`, `ConnectionId`, `DomainName`               |
| `CrossClusterOutboundReplicationRequests`                | `CrossClusterOutboundReplicationRequests`                | Sum             | `ClientId`, `ConnectionId`, `DomainName`               |
| `CrossClusterOutboundRequests`                           | `CrossClusterOutboundRequests`                           | Sum             | `ClientId`, `ConnectionId`, `DomainName`               |
| `CrossClusterOutboundSearchRequests`                     | `CrossClusterOutboundSearchRequests`                     | Sum             | `ClientId`, `ConnectionId`, `DomainName`               |
| `CurrentPointInTime`                                     | `CurrentPointInTime`                                     | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `DataNodes`                                              | `DataNodes`                                              | Histogram       | `ActiveAZ`, `ClientId`, `DomainName`                   |
| `DataNodesShards.active`                                 | `DataNodesShards.active`                                 | Histogram       | `ActiveAZ`, `ClientId`, `DomainName`                   |
| `DataNodesShards.initialising`                           | `DataNodesShards.initialising`                           | Histogram       | `ActiveAZ`, `ClientId`, `DomainName`                   |
| `DataNodesShards.relocating`                             | `DataNodesShards.relocating`                             | Histogram       | `ActiveAZ`, `ClientId`, `DomainName`                   |
| `DataNodesShards.unassigned`                             | `DataNodesShards.unassigned`                             | Histogram       | `ActiveAZ`, `ClientId`, `DomainName`                   |
| `DeletedDocuments`                                       | `DeletedDocuments`                                       | Histogram       | `ClientId`, `DomainName`                               |
| `DfsPreQueryCurrent`                                     | `DfsPreQueryCurrent`                                     | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `DfsPreQueryTimeInMillis`                                | `DfsPreQueryTimeInMillis`                                | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `DfsPreQueryTotal`                                       | `DfsPreQueryTotal`                                       | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `DfsQueryCurrent`                                        | `DfsQueryCurrent`                                        | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `DfsQueryTimeInMillis`                                   | `DfsQueryTimeInMillis`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `DfsQueryTotal`                                          | `DfsQueryTotal`                                          | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `DiskQueueDepth`                                         | `DiskQueueDepth`                                         | Histogram       | `ClientId`, `DomainName`                               |
| `ESReportingFailedRequestSysErrCount`                    | `ESReportingFailedRequestSysErrCount`                    | Sum             | `ClientId`, `DomainName`                               |
| `ESReportingFailedRequestUserErrCount`                   | `ESReportingFailedRequestUserErrCount`                   | Sum             | `ClientId`, `DomainName`                               |
| `ESReportingRequestCount`                                | `ESReportingRequestCount`                                | Sum             | `ClientId`, `DomainName`                               |
| `ESReportingSuccessCount`                                | `ESReportingSuccessCount`                                | Sum             | `ClientId`, `DomainName`                               |
| `ElasticsearchRequests`                                  | `ElasticsearchRequests`                                  | Sum             | `ClientId`, `DomainName`                               |
| `EnforcedWorkloadGroupCount`                             | `EnforcedWorkloadGroupCount`                             | Histogram       | `ClientId`, `DomainName`                               |
| `ExpandCurrent`                                          | `ExpandCurrent`                                          | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ExpandTimeInMillis`                                     | `ExpandTimeInMillis`                                     | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ExpandTotal`                                            | `ExpandTotal`                                            | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `FetchCurrent`                                           | `FetchCurrent`                                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `FetchTimeInMillis`                                      | `FetchTimeInMillis`                                      | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `FetchTotal`                                             | `FetchTotal`                                             | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `FollowerCheckPoint`                                     | `FollowerCheckPoint`                                     | Histogram       | `ClientId`, `ConnectionId`, `DomainName`               |
| `ForecastCheckpointIndexStatus.red`                      | `ForecastCheckpointIndexStatus.red`                      | Histogram       | `ClientId`, `DomainName`                               |
| `ForecastCheckpointIndexStatusIndexExists`               | `ForecastCheckpointIndexStatusIndexExists`               | Histogram       | `ClientId`, `DomainName`                               |
| `ForecastConfigIndexStatus.red`                          | `ForecastConfigIndexStatus.red`                          | Histogram       | `ClientId`, `DomainName`                               |
| `ForecastConfigIndexStatusIndexExists`                   | `ForecastConfigIndexStatusIndexExists`                   | Histogram       | `ClientId`, `DomainName`                               |
| `ForecastExecuteFailureCount`                            | `ForecastExecuteFailureCount`                            | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ForecastExecuteRequestCount`                            | `ForecastExecuteRequestCount`                            | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ForecastHCExecuteFailureCount`                          | `ForecastHCExecuteFailureCount`                          | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ForecastHCExecuteRequestCount`                          | `ForecastHCExecuteRequestCount`                          | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ForecastModelCorruptionCount`                           | `ForecastModelCorruptionCount`                           | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ForecastResultsIndexStatus.red`                         | `ForecastResultsIndexStatus.red`                         | Histogram       | `ClientId`, `DomainName`                               |
| `ForecastResultsIndexStatusIndexExists`                  | `ForecastResultsIndexStatusIndexExists`                  | Histogram       | `ClientId`, `DomainName`                               |
| `ForecastStateIndexStatus.red`                           | `ForecastStateIndexStatus.red`                           | Histogram       | `ClientId`, `DomainName`                               |
| `ForecastStateIndexStatusIndexExists`                    | `ForecastStateIndexStatusIndexExists`                    | Histogram       | `ClientId`, `DomainName`                               |
| `ForecastUnhealthy`                                      | `ForecastUnhealthy`                                      | Histogram       | `ClientId`, `DomainName`                               |
| `ForecasterCount`                                        | `ForecasterCount`                                        | Histogram       | `ClientId`, `DomainName`                               |
| `FreeStorageSpace`                                       | `FreeStorageSpace`                                       | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `HCForecasterCount`                                      | `HCForecasterCount`                                      | Histogram       | `ClientId`, `DomainName`                               |
| `HasActivePointInTime`                                   | `HasActivePointInTime`                                   | Histogram       | `ClientId`, `DomainName`                               |
| `HasUsedPointInTime`                                     | `HasUsedPointInTime`                                     | Histogram       | `ClientId`, `DomainName`                               |
| `HighSwapUsage`                                          | `HighSwapUsage`                                          | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `HotStorageSpaceUtilization`                             | `HotStorageSpaceUtilization`                             | Histogram       | `ClientId`, `DomainName`                               |
| `HotToWarmMigrationFailureCount`                         | `HotToWarmMigrationFailureCount`                         | Sum             | `ClientId`, `DomainName`                               |
| `HotToWarmMigrationForceMergeLatency`                    | `HotToWarmMigrationForceMergeLatency`                    | Histogram       | `ClientId`, `DomainName`                               |
| `HotToWarmMigrationProcessingLatency`                    | `HotToWarmMigrationProcessingLatency`                    | Histogram       | `ClientId`, `DomainName`                               |
| `HotToWarmMigrationQueueSize`                            | `HotToWarmMigrationQueueSize`                            | Histogram       | `ClientId`, `DomainName`                               |
| `HotToWarmMigrationSnapshotLatency`                      | `HotToWarmMigrationSnapshotLatency`                      | Histogram       | `ClientId`, `DomainName`                               |
| `HotToWarmMigrationSuccessCount`                         | `HotToWarmMigrationSuccessCount`                         | Sum             | `ClientId`, `DomainName`                               |
| `HotToWarmMigrationSuccessLatency`                       | `HotToWarmMigrationSuccessLatency`                       | Histogram       | `ClientId`, `DomainName`                               |
| `ISMPolicyCount`                                         | `ISMPolicyCount`                                         | Histogram       | `ClientId`, `DomainName`                               |
| `InFlightFetches`                                        | `InFlightFetches`                                        | Histogram       | `ClientId`, `DomainName`                               |
| `IndexingLatency`                                        | `IndexingLatency`                                        | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `IndexingRate`                                           | `IndexingRate`                                           | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `InvalidHostHeaderRequests`                              | `InvalidHostHeaderRequests`                              | Sum             | `ClientId`, `DomainName`                               |
| `IopsThrottle`                                           | `IopsThrottle`                                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `JVMGCOldCollectionCount`                                | `JVMGCOldCollectionCount`                                | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `JVMGCOldCollectionTime`                                 | `JVMGCOldCollectionTime`                                 | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `JVMGCYoungCollectionCount`                              | `JVMGCYoungCollectionCount`                              | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `JVMGCYoungCollectionTime`                               | `JVMGCYoungCollectionTime`                               | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `JVMMemoryPressure`                                      | `JVMMemoryPressure`                                      | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KMSKeyError`                                            | `KMSKeyError`                                            | Histogram       | `ClientId`, `DomainName`                               |
| `KMSKeyInaccessible`                                     | `KMSKeyInaccessible`                                     | Histogram       | `ClientId`, `DomainName`                               |
| `KNNCacheCapacityReached`                                | `KNNCacheCapacityReached`                                | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNCircuitBreakerTriggered`                             | `KNNCircuitBreakerTriggered`                             | Histogram       | `ClientId`, `DomainName`                               |
| `KNNEvictionCount`                                       | `KNNEvictionCount`                                       | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNFaissInitialized`                                    | `KNNFaissInitialized`                                    | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNGraphIndexErrors`                                    | `KNNGraphIndexErrors`                                    | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNGraphIndexRequests`                                  | `KNNGraphIndexRequests`                                  | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNGraphMemoryUsage`                                    | `KNNGraphMemoryUsage`                                    | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNGraphMemoryUsagePercentage`                          | `KNNGraphMemoryUsagePercentage`                          | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNGraphQueryErrors`                                    | `KNNGraphQueryErrors`                                    | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNGraphQueryRequests`                                  | `KNNGraphQueryRequests`                                  | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNHitCount`                                            | `KNNHitCount`                                            | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNLoadExceptionCount`                                  | `KNNLoadExceptionCount`                                  | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNLoadSuccessCount`                                    | `KNNLoadSuccessCount`                                    | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNLuceneInitialized`                                   | `KNNLuceneInitialized`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNMissCount`                                           | `KNNMissCount`                                           | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNNmslibInitialized`                                   | `KNNNmslibInitialized`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNQueryRequests`                                       | `KNNQueryRequests`                                       | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNRemoteBuildEnabled`                                  | `KNNRemoteBuildEnabled`                                  | Histogram       | `ClientId`, `DomainName`                               |
| `KNNRemoteIndexBuildFailureCount`                        | `KNNRemoteIndexBuildFailureCount`                        | Sum             | `ClientId`, `DomainName`                               |
| `KNNRemoteIndexBuildSuccessCount`                        | `KNNRemoteIndexBuildSuccessCount`                        | Sum             | `ClientId`, `DomainName`                               |
| `KNNScriptCompilationErrors`                             | `KNNScriptCompilationErrors`                             | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNScriptCompilations`                                  | `KNNScriptCompilations`                                  | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNScriptQueryErrors`                                   | `KNNScriptQueryErrors`                                   | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNScriptQueryRequests`                                 | `KNNScriptQueryRequests`                                 | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNTotalLoadTime`                                       | `KNNTotalLoadTime`                                       | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNTrainingErrors`                                      | `KNNTrainingErrors`                                      | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNTrainingMemoryUsage`                                 | `KNNTrainingMemoryUsage`                                 | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNTrainingMemoryUsagePercentage`                       | `KNNTrainingMemoryUsagePercentage`                       | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KNNTrainingRequests`                                    | `KNNTrainingRequests`                                    | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KibanaConcurrentConnections`                            | `KibanaConcurrentConnections`                            | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KibanaHealthyNode`                                      | `KibanaHealthyNode`                                      | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KibanaHealthyNodes`                                     | `KibanaHealthyNodes`                                     | Histogram       | `ClientId`, `DomainName`                               |
| `KibanaHeapTotal`                                        | `KibanaHeapTotal`                                        | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KibanaHeapUsed`                                         | `KibanaHeapUsed`                                         | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KibanaHeapUtilization`                                  | `KibanaHeapUtilization`                                  | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KibanaIndexMigrationFailed`                             | `KibanaIndexMigrationFailed`                             | Histogram       | `ClientId`, `DomainName`                               |
| `KibanaOS1MinuteLoad`                                    | `KibanaOS1MinuteLoad`                                    | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `KibanaRequestTotal`                                     | `KibanaRequestTotal`                                     | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `KibanaResponseTimesMaxInMillis`                         | `KibanaResponseTimesMaxInMillis`                         | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `LTRFeatureMemoryUsageInBytes`                           | `LTRFeatureMemoryUsageInBytes`                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `LTRFeaturesetMemoryUsageInBytes`                        | `LTRFeaturesetMemoryUsageInBytes`                        | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `LTRModelMemoryUsageInBytes`                             | `LTRModelMemoryUsageInBytes`                             | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `LTRPluginUnhealthy`                                     | `LTRPluginUnhealthy`                                     | Histogram       | `ClientId`, `DomainName`                               |
| `LTRRequestErrorCount`                                   | `LTRRequestErrorCount`                                   | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `LTRRequestTotalCount`                                   | `LTRRequestTotalCount`                                   | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `LTRStatus.red`                                          | `LTRStatus.red`                                          | Histogram       | `ClientId`, `DomainName`                               |
| `LeaderCheckPoint`                                       | `LeaderCheckPoint`                                       | Histogram       | `ClientId`, `DomainName`, `LeaderAlias`                |
| `MLCircuitBreakerTriggerCount`                           | `MLCircuitBreakerTriggerCount`                           | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `MLCommonsPluginUnhealthy`                               | `MLCommonsPluginUnhealthy`                               | Histogram       | `ClientId`, `DomainName`                               |
| `MLConnectorCount`                                       | `MLConnectorCount`                                       | Histogram       | `ClientId`, `DomainName`                               |
| `MLConnectorIndexStatus.red`                             | `MLConnectorIndexStatus.red`                             | Histogram       | `ClientId`, `DomainName`                               |
| `MLConnectorIndexStatusIndexExists`                      | `MLConnectorIndexStatusIndexExists`                      | Histogram       | `ClientId`, `DomainName`                               |
| `MLDeployedModelCount`                                   | `MLDeployedModelCount`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MLExecutingTaskCount`                                   | `MLExecutingTaskCount`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MLFailureCount`                                         | `MLFailureCount`                                         | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `MLModelCount`                                           | `MLModelCount`                                           | Histogram       | `ClientId`, `DomainName`                               |
| `MLModelIndexStatus.red`                                 | `MLModelIndexStatus.red`                                 | Histogram       | `ClientId`, `DomainName`                               |
| `MLModelIndexStatusIndexExists`                          | `MLModelIndexStatusIndexExists`                          | Histogram       | `ClientId`, `DomainName`                               |
| `MLRequestCount`                                         | `MLRequestCount`                                         | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `MLTaskIndexStatus.red`                                  | `MLTaskIndexStatus.red`                                  | Histogram       | `ClientId`, `DomainName`                               |
| `MLTaskIndexStatusIndexExists`                           | `MLTaskIndexStatusIndexExists`                           | Histogram       | `ClientId`, `DomainName`                               |
| `MasterCPUCreditBalance`                                 | `MasterCPUCreditBalance`                                 | Histogram       | `ClientId`, `DomainName`                               |
| `MasterCPUUtilization`                                   | `MasterCPUUtilization`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MasterFreeStorageSpace`                                 | `MasterFreeStorageSpace`                                 | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MasterJVMMemoryPressure`                                | `MasterJVMMemoryPressure`                                | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MasterOldGenJVMMemoryPressure`                          | `MasterOldGenJVMMemoryPressure`                          | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MasterReachableFromNode`                                | `MasterReachableFromNode`                                | Histogram       | `ClientId`, `DomainName`                               |
| `MasterSysMemoryUtilization`                             | `MasterSysMemoryUtilization`                             | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MaxProvisionedThroughput`                               | `MaxProvisionedThroughput`                               | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MlCircuitBreakerTriggerCount`                           | `MlCircuitBreakerTriggerCount`                           | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `MlConnectorCount`                                       | `MlConnectorCount`                                       | Histogram       | `ClientId`, `DomainName`                               |
| `MlConnectorIndexStatus.red`                             | `MlConnectorIndexStatus.red`                             | Histogram       | `ClientId`, `DomainName`                               |
| `MlConnectorIndexStatusIndexExists`                      | `MlConnectorIndexStatusIndexExists`                      | Histogram       | `ClientId`, `DomainName`                               |
| `MlDeployedModelCount`                                   | `MlDeployedModelCount`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MlExecutingTaskCount`                                   | `MlExecutingTaskCount`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MlFailureCount`                                         | `MlFailureCount`                                         | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `MlModelCount`                                           | `MlModelCount`                                           | Histogram       | `ClientId`, `DomainName`                               |
| `MlModelIndexStatus.red`                                 | `MlModelIndexStatus.red`                                 | Histogram       | `ClientId`, `DomainName`                               |
| `MlModelIndexStatusIndexExists`                          | `MlModelIndexStatusIndexExists`                          | Histogram       | `ClientId`, `DomainName`                               |
| `MlNodeExecutingTaskCount`                               | `MlNodeExecutingTaskCount`                               | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MlNodeTotalCircuitBreakerTriggerCount`                  | `MlNodeTotalCircuitBreakerTriggerCount`                  | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `MlNodeTotalFailureCount`                                | `MlNodeTotalFailureCount`                                | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `MlNodeTotalModelCount`                                  | `MlNodeTotalModelCount`                                  | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `MlNodeTotalRequestCount`                                | `MlNodeTotalRequestCount`                                | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `MlRequestCount`                                         | `MlRequestCount`                                         | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `MlTaskIndexStatus.red`                                  | `MlTaskIndexStatus.red`                                  | Histogram       | `ClientId`, `DomainName`                               |
| `MlTaskIndexStatusIndexExists`                           | `MlTaskIndexStatusIndexExists`                           | Histogram       | `ClientId`, `DomainName`                               |
| `Nodes`                                                  | `Nodes`                                                  | Histogram       | `ClientId`, `DomainName`                               |
| `OldGenJVMMemoryPressure`                                | `OldGenJVMMemoryPressure`                                | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `OpenContexts`                                           | `OpenContexts`                                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `OpenContexts-BeagleStone`                               | `OpenContexts-BeagleStone`                               | Histogram       | `ClientId`, `DomainName`                               |
| `OpenSearchDashboardsConcurrentConnections`              | `OpenSearchDashboardsConcurrentConnections`              | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `OpenSearchDashboardsHealthyNode`                        | `OpenSearchDashboardsHealthyNode`                        | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `OpenSearchDashboardsHealthyNodes`                       | `OpenSearchDashboardsHealthyNodes`                       | Histogram       | `ClientId`, `DomainName`                               |
| `OpenSearchDashboardsHeapTotal`                          | `OpenSearchDashboardsHeapTotal`                          | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `OpenSearchDashboardsHeapUsed`                           | `OpenSearchDashboardsHeapUsed`                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `OpenSearchDashboardsHeapUtilization`                    | `OpenSearchDashboardsHeapUtilization`                    | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `OpenSearchDashboardsIndexMigrationFailed`               | `OpenSearchDashboardsIndexMigrationFailed`               | Histogram       | `ClientId`, `DomainName`                               |
| `OpenSearchDashboardsOS1MinuteLoad`                      | `OpenSearchDashboardsOS1MinuteLoad`                      | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `OpenSearchDashboardsRequestTotal`                       | `OpenSearchDashboardsRequestTotal`                       | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `OpenSearchDashboardsResponseTimesMaxInMillis`           | `OpenSearchDashboardsResponseTimesMaxInMillis`           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `OpenSearchRequests`                                     | `OpenSearchRequests`                                     | Sum             | `ClientId`, `DomainName`                               |
| `OpensearchDashboardsReportingFailedRequestSysErrCount`  | `OpensearchDashboardsReportingFailedRequestSysErrCount`  | Sum             | `ClientId`, `DomainName`                               |
| `OpensearchDashboardsReportingFailedRequestUserErrCount` | `OpensearchDashboardsReportingFailedRequestUserErrCount` | Sum             | `ClientId`, `DomainName`                               |
| `OpensearchDashboardsReportingRequestCount`              | `OpensearchDashboardsReportingRequestCount`              | Sum             | `ClientId`, `DomainName`                               |
| `OpensearchDashboardsReportingSuccessCount`              | `OpensearchDashboardsReportingSuccessCount`              | Sum             | `ClientId`, `DomainName`                               |
| `PPLFailedRequestCountByCusErr`                          | `PPLFailedRequestCountByCusErr`                          | Sum             | `ClientId`, `DomainName`                               |
| `PPLFailedRequestCountBySysErr`                          | `PPLFailedRequestCountBySysErr`                          | Sum             | `ClientId`, `DomainName`                               |
| `PPLRequestCount`                                        | `PPLRequestCount`                                        | Sum             | `ClientId`, `DomainName`                               |
| `PrimaryWriteRejected`                                   | `PrimaryWriteRejected`                                   | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `QueryCurrent`                                           | `QueryCurrent`                                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `QueryFailure`                                           | `QueryFailure`                                           | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `QueryFailure-BeagleStone`                               | `QueryFailure-BeagleStone`                               | Sum             | `ClientId`, `DomainName`                               |
| `QuerySuccess`                                           | `QuerySuccess`                                           | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `QuerySuccess-BeagleStone`                               | `QuerySuccess-BeagleStone`                               | Sum             | `ClientId`, `DomainName`                               |
| `QueryTimeInMillis`                                      | `QueryTimeInMillis`                                      | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `QueryTotal`                                             | `QueryTotal`                                             | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ReadIOPS`                                               | `ReadIOPS`                                               | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ReadIOPSMicroBursting`                                  | `ReadIOPSMicroBursting`                                  | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ReadLatency`                                            | `ReadLatency`                                            | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ReadThroughput`                                         | `ReadThroughput`                                         | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ReadThroughputMicroBursting`                            | `ReadThroughputMicroBursting`                            | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `RemoteStorageUsedSpace`                                 | `RemoteStorageUsedSpace`                                 | Histogram       | `ClientId`, `DomainName`                               |
| `RemoteStorageWriteRejected`                             | `RemoteStorageWriteRejected`                             | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ReplicaWriteRejected`                                   | `ReplicaWriteRejected`                                   | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ReplicationLagMaxTime`                                  | `ReplicationLagMaxTime`                                  | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ReplicationNumBootstrappingIndices`                     | `ReplicationNumBootstrappingIndices`                     | Histogram       | `ClientId`, `DomainName`                               |
| `ReplicationNumFailedIndices`                            | `ReplicationNumFailedIndices`                            | Histogram       | `ClientId`, `DomainName`                               |
| `ReplicationNumIndexTasks`                               | `ReplicationNumIndexTasks`                               | Histogram       | `ClientId`, `DomainName`                               |
| `ReplicationNumPausedIndices`                            | `ReplicationNumPausedIndices`                            | Histogram       | `ClientId`, `DomainName`                               |
| `ReplicationNumShardTasks`                               | `ReplicationNumShardTasks`                               | Histogram       | `ClientId`, `DomainName`                               |
| `ReplicationNumSyncingIndices`                           | `ReplicationNumSyncingIndices`                           | Histogram       | `ClientId`, `DomainName`                               |
| `ReplicationRate`                                        | `ReplicationRate`                                        | Histogram       | `ClientId`, `DomainName`, `LeaderAlias`                |
| `SQLDefaultCursorRequestCount`                           | `SQLDefaultCursorRequestCount`                           | Sum             | `ClientId`, `DomainName`                               |
| `SQLFailedRequestCountByCusErr`                          | `SQLFailedRequestCountByCusErr`                          | Sum             | `ClientId`, `DomainName`                               |
| `SQLFailedRequestCountBySysErr`                          | `SQLFailedRequestCountBySysErr`                          | Sum             | `ClientId`, `DomainName`                               |
| `SQLRequestCount`                                        | `SQLRequestCount`                                        | Sum             | `ClientId`, `DomainName`                               |
| `SQLUnhealthy`                                           | `SQLUnhealthy`                                           | Histogram       | `ClientId`, `DomainName`                               |
| `ScrollCurrent`                                          | `ScrollCurrent`                                          | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ScrollCurrent-BeagleStone`                              | `ScrollCurrent-BeagleStone`                              | Histogram       | `ClientId`, `DomainName`                               |
| `ScrollTotal`                                            | `ScrollTotal`                                            | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ScrollTotal-BeagleStone`                                | `ScrollTotal-BeagleStone`                                | Sum             | `ClientId`, `DomainName`                               |
| `SearchIdleReactivateCountTotal`                         | `SearchIdleReactivateCountTotal`                         | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `SearchLatency`                                          | `SearchLatency`                                          | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `SearchPipelineRequestFailure`                           | `SearchPipelineRequestFailure`                           | Sum             | `ClientId`, `DomainName`, `Processor`                  |
| `SearchPipelineRequestTime`                              | `SearchPipelineRequestTime`                              | Histogram       | `ClientId`, `DomainName`                               |
| `SearchPipelineUnhealthy`                                | `SearchPipelineUnhealthy`                                | Histogram       | `ClientId`, `DomainName`                               |
| `SearchRate`                                             | `SearchRate`                                             | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `SearchShardTaskCancelled`                               | `SearchShardTaskCancelled`                               | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `SearchTaskCancelled`                                    | `SearchTaskCancelled`                                    | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `SearchableDocuments`                                    | `SearchableDocuments`                                    | Histogram       | `ClientId`, `DomainName`                               |
| `SegmentCount`                                           | `SegmentCount`                                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ShardCount`                                             | `ShardCount`                                             | Histogram       | `ClientId`, `DomainName`, `NodeId`, `ShardRole`        |
| `Shards.active`                                          | `Shards.active`                                          | Histogram       | `ClientId`, `DomainName`                               |
| `Shards.activePrimary`                                   | `Shards.activePrimary`                                   | Histogram       | `ClientId`, `DomainName`                               |
| `Shards.delayedUnassigned`                               | `Shards.delayedUnassigned`                               | Histogram       | `ClientId`, `DomainName`                               |
| `Shards.initializing`                                    | `Shards.initializing`                                    | Histogram       | `ClientId`, `DomainName`                               |
| `Shards.relocating`                                      | `Shards.relocating`                                      | Histogram       | `ClientId`, `DomainName`                               |
| `Shards.unassigned`                                      | `Shards.unassigned`                                      | Histogram       | `ClientId`, `DomainName`                               |
| `SingleStreamForecasterCount`                            | `SingleStreamForecasterCount`                            | Histogram       | `ClientId`, `DomainName`                               |
| `SnapshotCount`                                          | `SnapshotCount`                                          | Histogram       | `ClientId`, `DomainName`, `Repository`                 |
| `SnapshotFailures`                                       | `SnapshotFailures`                                       | Sum             | `ClientId`, `DomainName`, `Repository`                 |
| `SoftWorkloadGroupCount`                                 | `SoftWorkloadGroupCount`                                 | Histogram       | `ClientId`, `DomainName`                               |
| `SysMemoryUtilization`                                   | `SysMemoryUtilization`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `TLSNegotiationError`                                    | `TLSNegotiationError`                                    | Sum             | `ClientId`, `DomainName`                               |
| `ThreadCount`                                            | `ThreadCount`                                            | Histogram       | `ClientId`, `DomainName`                               |
| `ThreadpoolBulkQueue`                                    | `ThreadpoolBulkQueue`                                    | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolBulkRejected`                                 | `ThreadpoolBulkRejected`                                 | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolBulkThreads`                                  | `ThreadpoolBulkThreads`                                  | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolForce_mergeQueue`                             | `ThreadpoolForce_mergeQueue`                             | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolForce_mergeRejected`                          | `ThreadpoolForce_mergeRejected`                          | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolForce_mergeThreads`                           | `ThreadpoolForce_mergeThreads`                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolIndexQueue`                                   | `ThreadpoolIndexQueue`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolIndexRejected`                                | `ThreadpoolIndexRejected`                                | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolIndexSearcherQueue`                           | `ThreadpoolIndexSearcherQueue`                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolIndexSearcherRejected`                        | `ThreadpoolIndexSearcherRejected`                        | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolIndexSearcherThreads`                         | `ThreadpoolIndexSearcherThreads`                         | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolIndexThreads`                                 | `ThreadpoolIndexThreads`                                 | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolMergeQueue`                                   | `ThreadpoolMergeQueue`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolMergeRejected`                                | `ThreadpoolMergeRejected`                                | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolMergeThreads`                                 | `ThreadpoolMergeThreads`                                 | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolOpendistro_monitor_runnerQueue`               | `ThreadpoolOpendistro_monitor_runnerQueue`               | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolOpendistro_monitor_runnerRejected`            | `ThreadpoolOpendistro_monitor_runnerRejected`            | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolOpendistro_monitor_runnerThreads`             | `ThreadpoolOpendistro_monitor_runnerThreads`             | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolSearchQueue`                                  | `ThreadpoolSearchQueue`                                  | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolSearchRejected`                               | `ThreadpoolSearchRejected`                               | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolSearchThreads`                                | `ThreadpoolSearchThreads`                                | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolWriteQueue`                                   | `ThreadpoolWriteQueue`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolWriteRejected`                                | `ThreadpoolWriteRejected`                                | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `ThreadpoolWriteThreads`                                 | `ThreadpoolWriteThreads`                                 | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `Threadpoolsql-workerQueue`                              | `Threadpoolsql-workerQueue`                              | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `Threadpoolsql-workerRejected`                           | `Threadpoolsql-workerRejected`                           | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `Threadpoolsql-workerThreads`                            | `Threadpoolsql-workerThreads`                            | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `ThroughputThrottle`                                     | `ThroughputThrottle`                                     | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `TookCurrent`                                            | `TookCurrent`                                            | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `TookTimeInMillis`                                       | `TookTimeInMillis`                                       | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `TookTotal`                                              | `TookTotal`                                              | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `TotalPointInTime`                                       | `TotalPointInTime`                                       | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `TotalRemoteReindexCallsFailed`                          | `TotalRemoteReindexCallsFailed`                          | Sum             | `ClientId`, `DomainName`, `RemoteDomain`               |
| `TotalRemoteReindexCallsSucceeded`                       | `TotalRemoteReindexCallsSucceeded`                       | Sum             | `ClientId`, `DomainName`, `RemoteDomain`               |
| `VolumeStalledIOCheck`                                   | `VolumeStalledIOCheck`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmCPUUtilization`                                     | `WarmCPUUtilization`                                     | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmConcurrentSearchLatency`                            | `WarmConcurrentSearchLatency`                            | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmConcurrentSearchRate`                               | `WarmConcurrentSearchRate`                               | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmFreeStorageSpace`                                   | `WarmFreeStorageSpace`                                   | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmJVMGCOldCollectionCount`                            | `WarmJVMGCOldCollectionCount`                            | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmJVMGCOldCollectionTime`                             | `WarmJVMGCOldCollectionTime`                             | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmJVMGCYoungCollectionCount`                          | `WarmJVMGCYoungCollectionCount`                          | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmJVMGCYoungCollectionTime`                           | `WarmJVMGCYoungCollectionTime`                           | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmJVMMemoryPressure`                                  | `WarmJVMMemoryPressure`                                  | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmNodes`                                              | `WarmNodes`                                              | Histogram       | `ClientId`, `DomainName`                               |
| `WarmOldGenJVMMemoryPressure`                            | `WarmOldGenJVMMemoryPressure`                            | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmSearchLatency`                                      | `WarmSearchLatency`                                      | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmSearchRate`                                         | `WarmSearchRate`                                         | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmSearchableDocuments`                                | `WarmSearchableDocuments`                                | Histogram       | `ClientId`, `DomainName`                               |
| `WarmStorageSpaceUtilization`                            | `WarmStorageSpaceUtilization`                            | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmSysMemoryUtilization`                               | `WarmSysMemoryUtilization`                               | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmThreadpoolIndexSearcherQueue`                       | `WarmThreadpoolIndexSearcherQueue`                       | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmThreadpoolIndexSearcherRejected`                    | `WarmThreadpoolIndexSearcherRejected`                    | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmThreadpoolIndexSearcherThreads`                     | `WarmThreadpoolIndexSearcherThreads`                     | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmThreadpoolSearchQueue`                              | `WarmThreadpoolSearchQueue`                              | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmThreadpoolSearchRejected`                           | `WarmThreadpoolSearchRejected`                           | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmThreadpoolSearchThreads`                            | `WarmThreadpoolSearchThreads`                            | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WarmToColdMigrationFailureCount`                        | `WarmToColdMigrationFailureCount`                        | Sum             | `ClientId`, `DomainName`                               |
| `WarmToColdMigrationLatency`                             | `WarmToColdMigrationLatency`                             | Histogram       | `ClientId`, `DomainName`                               |
| `WarmToColdMigrationQueueSize`                           | `WarmToColdMigrationQueueSize`                           | Histogram       | `ClientId`, `DomainName`                               |
| `WarmToColdMigrationSuccessCount`                        | `WarmToColdMigrationSuccessCount`                        | Sum             | `ClientId`, `DomainName`                               |
| `WarmToHotMigrationQueueSize`                            | `WarmToHotMigrationQueueSize`                            | Histogram       | `ClientId`, `DomainName`                               |
| `WorkloadCPUCancellations`                               | `WorkloadCPUCancellations`                               | Sum             | `ClientId`, `DomainName`                               |
| `WorkloadCPURejections`                                  | `WorkloadCPURejections`                                  | Sum             | `ClientId`, `DomainName`                               |
| `WorkloadManagementEnabled`                              | `WorkloadManagementEnabled`                              | Histogram       | `ClientId`, `DomainName`                               |
| `WorkloadMemoryCancellations`                            | `WorkloadMemoryCancellations`                            | Sum             | `ClientId`, `DomainName`                               |
| `WorkloadQueryCompletions`                               | `WorkloadQueryCompletions`                               | Sum             | `ClientId`, `DomainName`                               |
| `WriteIOPS`                                              | `WriteIOPS`                                              | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WriteIOPSMicroBursting`                                 | `WriteIOPSMicroBursting`                                 | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WriteLatency`                                           | `WriteLatency`                                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WriteThroughput`                                        | `WriteThroughput`                                        | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `WriteThroughputMicroBursting`                           | `WriteThroughputMicroBursting`                           | Histogram       | `ClientId`, `DomainName`, `NodeId`                     |
| `warmQueryFailure`                                       | `warmQueryFailure`                                       | Sum             | `ClientId`, `DomainName`, `NodeId`                     |
| `warmQuerySuccess`                                       | `warmQuerySuccess`                                       | Sum             | `ClientId`, `DomainName`, `NodeId`                     |

## AWS/ElastiCache

The `AWS/ElastiCache` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/elasticache`. All enriched instruments use Delta temporality.

- [AWS::ElastiCache::CacheCluster](#otel-enrichment-aws-elasticache-aws-elasticache-cachecluster "#otel-enrichment-aws-elasticache-aws-elasticache-cachecluster")
- [AWS::ElastiCache::ReplicationGroup](#otel-enrichment-aws-elasticache-aws-elasticache-replicationgroup "#otel-enrichment-aws-elasticache-aws-elasticache-replicationgroup")
- [AWS::ElastiCache::ServerlessCache](#otel-enrichment-aws-elasticache-aws-elasticache-serverlesscache "#otel-enrichment-aws-elasticache-aws-elasticache-serverlesscache")

### AWS::ElastiCache::CacheCluster

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                           | OpenTelemetry metric                             | Instrument type | Data point attributes           |
| ------------------------------------------------ | ------------------------------------------------ | --------------- | ------------------------------- |
| `ActiveDefragHits`                               | `ActiveDefragHits`                               | Sum             | `CacheClusterId`, `CacheNodeId` |
| `AllocatorFragmentationBytes`                    | `AllocatorFragmentationBytes`                    | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `AllocatorFragmentationRatio`                    | `AllocatorFragmentationRatio`                    | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `AuthenticationFailures`                         | `AuthenticationFailures`                         | Sum             | `CacheClusterId`, `CacheNodeId` |
| `BlockedConnections`                             | `BlockedConnections`                             | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `BytesReadFromDisk`                              | `BytesReadFromDisk`                              | Sum             | `CacheClusterId`, `CacheNodeId` |
| `BytesReadIntoMemcached`                         | `BytesReadIntoMemcached`                         | Sum             | `CacheClusterId`, `CacheNodeId` |
| `BytesUsedForCache`                              | `BytesUsedForCache`                              | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `BytesUsedForCacheItems`                         | `BytesUsedForCacheItems`                         | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `BytesUsedForHash`                               | `BytesUsedForHash`                               | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `BytesWrittenOutFromMemcached`                   | `BytesWrittenOutFromMemcached`                   | Sum             | `CacheClusterId`, `CacheNodeId` |
| `BytesWrittenToDisk`                             | `BytesWrittenToDisk`                             | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CPUCreditBalance`                               | `CPUCreditBalance`                               | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `CPUCreditUsage`                                 | `CPUCreditUsage`                                 | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CPUUtilization`                                 | `CPUUtilization`                                 | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `CacheHitRate`                                   | `CacheHitRate`                                   | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `CacheHits`                                      | `CacheHits`                                      | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CacheMisses`                                    | `CacheMisses`                                    | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CasBadval`                                      | `CasBadval`                                      | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CasHits`                                        | `CasHits`                                        | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CasMisses`                                      | `CasMisses`                                      | Sum             | `CacheClusterId`, `CacheNodeId` |
| `ChannelAuthorizationFailures`                   | `ChannelAuthorizationFailures`                   | Sum             | `CacheClusterId`, `CacheNodeId` |
| `ClusterBasedCmds`                               | `ClusterBasedCmds`                               | Sum             | `CacheClusterId`, `CacheNodeId` |
| `ClusterBasedCmdsLatency`                        | `ClusterBasedCmdsLatency`                        | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `CmdConfigGet`                                   | `CmdConfigGet`                                   | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CmdConfigSet`                                   | `CmdConfigSet`                                   | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CmdFlush`                                       | `CmdFlush`                                       | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CmdGet`                                         | `CmdGet`                                         | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CmdSet`                                         | `CmdSet`                                         | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CmdTouch`                                       | `CmdTouch`                                       | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CommandAuthorizationFailures`                   | `CommandAuthorizationFailures`                   | Sum             | `CacheClusterId`, `CacheNodeId` |
| `CurrConfig`                                     | `CurrConfig`                                     | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `CurrConnections`                                | `CurrConnections`                                | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `CurrItems`                                      | `CurrItems`                                      | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `CurrItemsWithVolatileFields`                    | `CurrItemsWithVolatileFields`                    | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `CurrVolatileItems`                              | `CurrVolatileItems`                              | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `DB0AverageTTL`                                  | `DB0AverageTTL`                                  | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `DatabaseAuthorizationFailures`                  | `DatabaseAuthorizationFailures`                  | Sum             | `CacheClusterId`, `CacheNodeId` |
| `DatabaseCapacityUsageCountedForEvictPercentage` | `DatabaseCapacityUsageCountedForEvictPercentage` | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `DatabaseCapacityUsagePercentage`                | `DatabaseCapacityUsagePercentage`                | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `DatabaseMemoryUsageCountedForEvictPercentage`   | `DatabaseMemoryUsageCountedForEvictPercentage`   | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `DatabaseMemoryUsagePercentage`                  | `DatabaseMemoryUsagePercentage`                  | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `DecrHits`                                       | `DecrHits`                                       | Sum             | `CacheClusterId`, `CacheNodeId` |
| `DecrMisses`                                     | `DecrMisses`                                     | Sum             | `CacheClusterId`, `CacheNodeId` |
| `DeleteHits`                                     | `DeleteHits`                                     | Sum             | `CacheClusterId`, `CacheNodeId` |
| `DeleteMisses`                                   | `DeleteMisses`                                   | Sum             | `CacheClusterId`, `CacheNodeId` |
| `DurabilityBufferExceededErrorCount`             | `DurabilityBufferExceededErrorCount`             | Sum             | `CacheClusterId`, `CacheNodeId` |
| `DurabilityLag`                                  | `DurabilityLag`                                  | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `EngineCPUUtilization`                           | `EngineCPUUtilization`                           | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `ErrorCount`                                     | `ErrorCount`                                     | Sum             | `CacheClusterId`, `CacheNodeId` |
| `EvalBasedCmds`                                  | `EvalBasedCmds`                                  | Sum             | `CacheClusterId`, `CacheNodeId` |
| `EvalBasedCmdsLatency`                           | `EvalBasedCmdsLatency`                           | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `EvictedUnfetched`                               | `EvictedUnfetched`                               | Sum             | `CacheClusterId`, `CacheNodeId` |
| `Evictions`                                      | `Evictions`                                      | Sum             | `CacheClusterId`, `CacheNodeId` |
| `ExpiredUnfetched`                               | `ExpiredUnfetched`                               | Sum             | `CacheClusterId`, `CacheNodeId` |
| `FreeableMemory`                                 | `FreeableMemory`                                 | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `GeoSpatialBasedCmds`                            | `GeoSpatialBasedCmds`                            | Sum             | `CacheClusterId`, `CacheNodeId` |
| `GeoSpatialBasedCmdsLatency`                     | `GeoSpatialBasedCmdsLatency`                     | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `GetHits`                                        | `GetHits`                                        | Sum             | `CacheClusterId`, `CacheNodeId` |
| `GetMisses`                                      | `GetMisses`                                      | Sum             | `CacheClusterId`, `CacheNodeId` |
| `GetTypeCmds`                                    | `GetTypeCmds`                                    | Sum             | `CacheClusterId`, `CacheNodeId` |
| `GetTypeCmdsLatency`                             | `GetTypeCmdsLatency`                             | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `HashBasedCmds`                                  | `HashBasedCmds`                                  | Sum             | `CacheClusterId`, `CacheNodeId` |
| `HashBasedCmdsLatency`                           | `HashBasedCmdsLatency`                           | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `HyperLogLogBasedCmds`                           | `HyperLogLogBasedCmds`                           | Sum             | `CacheClusterId`, `CacheNodeId` |
| `HyperLogLogBasedCmdsLatency`                    | `HyperLogLogBasedCmdsLatency`                    | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `IamAuthenticationExpirations`                   | `IamAuthenticationExpirations`                   | Sum             | `CacheClusterId`, `CacheNodeId` |
| `IamAuthenticationThrottling`                    | `IamAuthenticationThrottling`                    | Sum             | `CacheClusterId`, `CacheNodeId` |
| `IncrHits`                                       | `IncrHits`                                       | Sum             | `CacheClusterId`, `CacheNodeId` |
| `IncrMisses`                                     | `IncrMisses`                                     | Sum             | `CacheClusterId`, `CacheNodeId` |
| `IsMaster`                                       | `IsMaster`                                       | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `JsonBasedCmds`                                  | `JsonBasedCmds`                                  | Sum             | `CacheClusterId`, `CacheNodeId` |
| `JsonBasedCmdsLatency`                           | `JsonBasedCmdsLatency`                           | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `JsonBasedGetCmds`                               | `JsonBasedGetCmds`                               | Sum             | `CacheClusterId`, `CacheNodeId` |
| `JsonBasedGetCmdsLatency`                        | `JsonBasedGetCmdsLatency`                        | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `JsonBasedSetCmds`                               | `JsonBasedSetCmds`                               | Sum             | `CacheClusterId`, `CacheNodeId` |
| `JsonBasedSetCmdsLatency`                        | `JsonBasedSetCmdsLatency`                        | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `KeyAuthorizationFailures`                       | `KeyAuthorizationFailures`                       | Sum             | `CacheClusterId`, `CacheNodeId` |
| `KeyBasedCmds`                                   | `KeyBasedCmds`                                   | Sum             | `CacheClusterId`, `CacheNodeId` |
| `KeyBasedCmdsLatency`                            | `KeyBasedCmdsLatency`                            | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `KeysTracked`                                    | `KeysTracked`                                    | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `ListBasedCmds`                                  | `ListBasedCmds`                                  | Sum             | `CacheClusterId`, `CacheNodeId` |
| `ListBasedCmdsLatency`                           | `ListBasedCmdsLatency`                           | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `MajorPageFaults`                                | `MajorPageFaults`                                | Sum             | `CacheClusterId`, `CacheNodeId` |
| `MasterLinkHealthStatus`                         | `MasterLinkHealthStatus`                         | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `MemoryFragmentationRatio`                       | `MemoryFragmentationRatio`                       | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `NetworkBandwidthInAllowanceExceeded`            | `NetworkBandwidthInAllowanceExceeded`            | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NetworkBandwidthOutAllowanceExceeded`           | `NetworkBandwidthOutAllowanceExceeded`           | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NetworkBaselineMaxUsageInPercentage`            | `NetworkBaselineMaxUsageInPercentage`            | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `NetworkBaselineMaxUsageOutPercentage`           | `NetworkBaselineMaxUsageOutPercentage`           | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `NetworkBaselineUsageInPercentage`               | `NetworkBaselineUsageInPercentage`               | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `NetworkBaselineUsageOutPercentage`              | `NetworkBaselineUsageOutPercentage`              | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `NetworkBytesIn`                                 | `NetworkBytesIn`                                 | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NetworkBytesOut`                                | `NetworkBytesOut`                                | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NetworkConntrackAllowanceExceeded`              | `NetworkConntrackAllowanceExceeded`              | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NetworkLinkLocalAllowanceExceeded`              | `NetworkLinkLocalAllowanceExceeded`              | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NetworkMaxBytesIn`                              | `NetworkMaxBytesIn`                              | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `NetworkMaxBytesOut`                             | `NetworkMaxBytesOut`                             | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `NetworkMaxPacketsIn`                            | `NetworkMaxPacketsIn`                            | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `NetworkMaxPacketsOut`                           | `NetworkMaxPacketsOut`                           | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `NetworkPacketsIn`                               | `NetworkPacketsIn`                               | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NetworkPacketsOut`                              | `NetworkPacketsOut`                              | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NetworkPacketsPerSecondAllowanceExceeded`       | `NetworkPacketsPerSecondAllowanceExceeded`       | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NewConnections`                                 | `NewConnections`                                 | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NewItems`                                       | `NewItems`                                       | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NonKeyTypeCmds`                                 | `NonKeyTypeCmds`                                 | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NonKeyTypeCmdsLatency`                          | `NonKeyTypeCmdsLatency`                          | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `NumItemsReadFromDisk`                           | `NumItemsReadFromDisk`                           | Sum             | `CacheClusterId`, `CacheNodeId` |
| `NumItemsWrittenToDisk`                          | `NumItemsWrittenToDisk`                          | Sum             | `CacheClusterId`, `CacheNodeId` |
| `ProcessedCommands`                              | `ProcessedCommands`                              | Sum             | `CacheClusterId`, `CacheNodeId` |
| `PubSubBasedCmds`                                | `PubSubBasedCmds`                                | Sum             | `CacheClusterId`, `CacheNodeId` |
| `PubSubBasedCmdsLatency`                         | `PubSubBasedCmdsLatency`                         | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `PubSubChannels`                                 | `PubSubChannels`                                 | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `PubSubShardChannels`                            | `PubSubShardChannels`                            | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `Reclaimed`                                      | `Reclaimed`                                      | Sum             | `CacheClusterId`, `CacheNodeId` |
| `ReclaimedFields`                                | `ReclaimedFields`                                | Sum             | `CacheClusterId`, `CacheNodeId` |
| `RejectedConnections`                            | `RejectedConnections`                            | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `ReplicationBytes`                               | `ReplicationBytes`                               | Sum             | `CacheClusterId`, `CacheNodeId` |
| `ReplicationLag`                                 | `ReplicationLag`                                 | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SaveInProgress`                                 | `SaveInProgress`                                 | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SearchBasedCmds`                                | `SearchBasedCmds`                                | Sum             | `CacheClusterId`, `CacheNodeId` |
| `SearchBasedCmdsLatency`                         | `SearchBasedCmdsLatency`                         | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SearchBasedGetCmds`                             | `SearchBasedGetCmds`                             | Sum             | `CacheClusterId`, `CacheNodeId` |
| `SearchBasedGetCmdsLatency`                      | `SearchBasedGetCmdsLatency`                      | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SearchBasedSetCmds`                             | `SearchBasedSetCmds`                             | Sum             | `CacheClusterId`, `CacheNodeId` |
| `SearchBasedSetCmdsLatency`                      | `SearchBasedSetCmdsLatency`                      | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SearchNumberOfIndexes`                          | `SearchNumberOfIndexes`                          | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SearchTotalIndexedDocuments`                    | `SearchTotalIndexedDocuments`                    | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SearchUsedMemoryBytes`                          | `SearchUsedMemoryBytes`                          | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SetBasedCmds`                                   | `SetBasedCmds`                                   | Sum             | `CacheClusterId`, `CacheNodeId` |
| `SetBasedCmdsLatency`                            | `SetBasedCmdsLatency`                            | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SetTypeCmds`                                    | `SetTypeCmds`                                    | Sum             | `CacheClusterId`, `CacheNodeId` |
| `SetTypeCmdsLatency`                             | `SetTypeCmdsLatency`                             | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SlabsMoved`                                     | `SlabsMoved`                                     | Sum             | `CacheClusterId`, `CacheNodeId` |
| `SortedSetBasedCmds`                             | `SortedSetBasedCmds`                             | Sum             | `CacheClusterId`, `CacheNodeId` |
| `SortedSetBasedCmdsLatency`                      | `SortedSetBasedCmdsLatency`                      | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `StreamBasedCmds`                                | `StreamBasedCmds`                                | Sum             | `CacheClusterId`, `CacheNodeId` |
| `StreamBasedCmdsLatency`                         | `StreamBasedCmdsLatency`                         | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `StringBasedCmds`                                | `StringBasedCmds`                                | Sum             | `CacheClusterId`, `CacheNodeId` |
| `StringBasedCmdsLatency`                         | `StringBasedCmdsLatency`                         | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SuccessfulReadRequestLatency`                   | `SuccessfulReadRequestLatency`                   | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SuccessfulWriteRequestLatency`                  | `SuccessfulWriteRequestLatency`                  | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `SwapUsage`                                      | `SwapUsage`                                      | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `TouchHits`                                      | `TouchHits`                                      | Sum             | `CacheClusterId`, `CacheNodeId` |
| `TouchMisses`                                    | `TouchMisses`                                    | Sum             | `CacheClusterId`, `CacheNodeId` |
| `TrafficManagementActive`                        | `TrafficManagementActive`                        | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `UnusedMemory`                                   | `UnusedMemory`                                   | Histogram       | `CacheClusterId`, `CacheNodeId` |
| `UsedMemoryDataset`                              | `UsedMemoryDataset`                              | Histogram       | `CacheClusterId`, `CacheNodeId` |

### AWS::ElastiCache::ReplicationGroup

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                           | OpenTelemetry metric                             | Instrument type | Data point attributes               |
| ------------------------------------------------ | ------------------------------------------------ | --------------- | ----------------------------------- |
| `DatabaseCapacityUsageCountedForEvictPercentage` | `DatabaseCapacityUsageCountedForEvictPercentage` | Histogram       | `NodeGroupId`, `ReplicationGroupId` |
| `DatabaseMemoryUsageCountedForEvictPercentage`   | `DatabaseMemoryUsageCountedForEvictPercentage`   | Histogram       | `NodeGroupId`, `ReplicationGroupId` |

### AWS::ElastiCache::ServerlessCache

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                       | OpenTelemetry metric         | Instrument type | Data point attributes |
| ---------------------------- | ---------------------------- | --------------- | --------------------- |
| `ClusterBasedCmdsECPUs`      | `ClusterBasedCmdsECPUs`      | Sum             | `clusterId`           |
| `ElastiCacheProcessingUnits` | `ElastiCacheProcessingUnits` | Sum             | `clusterId`           |
| `EvalBasedCmdsECPUs`         | `EvalBasedCmdsECPUs`         | Sum             | `clusterId`           |
| `GeoSpatialBasedCmdsECPUs`   | `GeoSpatialBasedCmdsECPUs`   | Sum             | `clusterId`           |
| `GetTypeCmdsECPUs`           | `GetTypeCmdsECPUs`           | Sum             | `clusterId`           |
| `HashBasedCmdsECPUs`         | `HashBasedCmdsECPUs`         | Sum             | `clusterId`           |
| `HyperLogLogBasedCmdsECPUs`  | `HyperLogLogBasedCmdsECPUs`  | Sum             | `clusterId`           |
| `JsonBasedCmdsECPUs`         | `JsonBasedCmdsECPUs`         | Sum             | `clusterId`           |
| `KeyBasedCmdsECPUs`          | `KeyBasedCmdsECPUs`          | Sum             | `clusterId`           |
| `ListBasedCmdsECPUs`         | `ListBasedCmdsECPUs`         | Sum             | `clusterId`           |
| `NonKeyTypeCmdsECPUs`        | `NonKeyTypeCmdsECPUs`        | Sum             | `clusterId`           |
| `PubSubBasedCmdsECPUs`       | `PubSubBasedCmdsECPUs`       | Sum             | `clusterId`           |
| `SetBasedCmdsECPUs`          | `SetBasedCmdsECPUs`          | Sum             | `clusterId`           |
| `SetTypeCmdsECPUs`           | `SetTypeCmdsECPUs`           | Sum             | `clusterId`           |
| `SortedSetBasedCmdsECPUs`    | `SortedSetBasedCmdsECPUs`    | Sum             | `clusterId`           |
| `StreamBasedCmdsECPUs`       | `StreamBasedCmdsECPUs`       | Sum             | `clusterId`           |
| `StringBasedCmdsECPUs`       | `StringBasedCmdsECPUs`       | Sum             | `clusterId`           |
| `ThrottledCmds`              | `ThrottledCmds`              | Sum             | `clusterId`           |
| `TotalCmdsCount`             | `TotalCmdsCount`             | Sum             | `clusterId`           |

## AWS/ElasticBeanstalk

The `AWS/ElasticBeanstalk` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/elasticbeanstalk`. All enriched instruments use Delta temporality.

- [AWS::ElasticBeanstalk::Environment](#otel-enrichment-aws-elasticbeanstalk-aws-elasticbeanstalk-environment "#otel-enrichment-aws-elasticbeanstalk-aws-elasticbeanstalk-environment")

### AWS::ElasticBeanstalk::Environment

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Supported

| Metric                     | OpenTelemetry metric       | Instrument type | Data point attributes           |
| -------------------------- | -------------------------- | --------------- | ------------------------------- |
| `ApplicationLatencyP10`    | `ApplicationLatencyP10`    | Histogram       | `EnvironmentName`, `InstanceId` |
| `ApplicationLatencyP50`    | `ApplicationLatencyP50`    | Histogram       | `EnvironmentName`, `InstanceId` |
| `ApplicationLatencyP75`    | `ApplicationLatencyP75`    | Histogram       | `EnvironmentName`, `InstanceId` |
| `ApplicationLatencyP85`    | `ApplicationLatencyP85`    | Histogram       | `EnvironmentName`, `InstanceId` |
| `ApplicationLatencyP90`    | `ApplicationLatencyP90`    | Histogram       | `EnvironmentName`, `InstanceId` |
| `ApplicationLatencyP95`    | `ApplicationLatencyP95`    | Histogram       | `EnvironmentName`, `InstanceId` |
| `ApplicationLatencyP99`    | `ApplicationLatencyP99`    | Histogram       | `EnvironmentName`, `InstanceId` |
| `ApplicationLatencyP99.9`  | `ApplicationLatencyP99.9`  | Histogram       | `EnvironmentName`, `InstanceId` |
| `ApplicationRequests2xx`   | `ApplicationRequests2xx`   | Sum             | `EnvironmentName`, `InstanceId` |
| `ApplicationRequests3xx`   | `ApplicationRequests3xx`   | Sum             | `EnvironmentName`, `InstanceId` |
| `ApplicationRequests4xx`   | `ApplicationRequests4xx`   | Sum             | `EnvironmentName`, `InstanceId` |
| `ApplicationRequests5xx`   | `ApplicationRequests5xx`   | Sum             | `EnvironmentName`, `InstanceId` |
| `ApplicationRequestsTotal` | `ApplicationRequestsTotal` | Sum             | `EnvironmentName`, `InstanceId` |
| `CPUIdle`                  | `CPUIdle`                  | Histogram       | `EnvironmentName`, `InstanceId` |
| `CPUIowait`                | `CPUIowait`                | Histogram       | `EnvironmentName`, `InstanceId` |
| `CPUIrq`                   | `CPUIrq`                   | Histogram       | `EnvironmentName`, `InstanceId` |
| `CPUNice`                  | `CPUNice`                  | Histogram       | `EnvironmentName`, `InstanceId` |
| `CPUPrivileged`            | `CPUPrivileged`            | Histogram       | `EnvironmentName`, `InstanceId` |
| `CPUSoftirq`               | `CPUSoftirq`               | Histogram       | `EnvironmentName`, `InstanceId` |
| `CPUSystem`                | `CPUSystem`                | Histogram       | `EnvironmentName`, `InstanceId` |
| `CPUUser`                  | `CPUUser`                  | Histogram       | `EnvironmentName`, `InstanceId` |
| `InstanceHealth`           | `InstanceHealth`           | Histogram       | `EnvironmentName`, `InstanceId` |
| `LoadAverage1min`          | `LoadAverage1min`          | Histogram       | `EnvironmentName`, `InstanceId` |
| `LoadAverage5min`          | `LoadAverage5min`          | Histogram       | `EnvironmentName`, `InstanceId` |
| `RootFilesystemUtil`       | `RootFilesystemUtil`       | Histogram       | `EnvironmentName`, `InstanceId` |

## AWS/ElasticMapReduce

The `AWS/ElasticMapReduce` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/elasticmapreduce`. All enriched instruments use Delta temporality.

- [AWS::EMR::Cluster](#otel-enrichment-aws-elasticmapreduce-aws-emr-cluster "#otel-enrichment-aws-elasticmapreduce-aws-emr-cluster")

### AWS::EMR::Cluster

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                         | OpenTelemetry metric           | Instrument type | Data point attributes |
| ------------------------------ | ------------------------------ | --------------- | --------------------- |
| `AppsCompleted`                | `AppsCompleted`                | Sum             | `JobFlowId`           |
| `AppsFailed`                   | `AppsFailed`                   | Sum             | `JobFlowId`           |
| `AppsKilled`                   | `AppsKilled`                   | Sum             | `JobFlowId`           |
| `AppsPending`                  | `AppsPending`                  | Histogram       | `JobFlowId`           |
| `AppsRunning`                  | `AppsRunning`                  | Histogram       | `JobFlowId`           |
| `AppsSubmitted`                | `AppsSubmitted`                | Sum             | `JobFlowId`           |
| `AutoTerminationIsClusterIdle` | `AutoTerminationIsClusterIdle` | Histogram       | `JobFlowId`           |
| `ContainerAllocated`           | `ContainerAllocated`           | Histogram       | `JobFlowId`           |
| `ContainerPending`             | `ContainerPending`             | Histogram       | `JobFlowId`           |
| `ContainerPendingRatio`        | `ContainerPendingRatio`        | Histogram       | `JobFlowId`           |
| `ContainerReserved`            | `ContainerReserved`            | Histogram       | `JobFlowId`           |
| `CoreNodesPending`             | `CoreNodesPending`             | Histogram       | `JobFlowId`           |
| `CoreNodesRequested`           | `CoreNodesRequested`           | Histogram       | `JobFlowId`           |
| `CoreNodesRunning`             | `CoreNodesRunning`             | Histogram       | `JobFlowId`           |
| `CoreUnitsRequested`           | `CoreUnitsRequested`           | Histogram       | `JobFlowId`           |
| `CoreUnitsRunning`             | `CoreUnitsRunning`             | Histogram       | `JobFlowId`           |
| `CoreVCPURequested`            | `CoreVCPURequested`            | Histogram       | `JobFlowId`           |
| `CoreVCPURunning`              | `CoreVCPURunning`              | Histogram       | `JobFlowId`           |
| `HDFSBytesRead`                | `HDFSBytesRead`                | Sum             | `JobFlowId`           |
| `HDFSBytesWritten`             | `HDFSBytesWritten`             | Sum             | `JobFlowId`           |
| `HDFSUtilization`              | `HDFSUtilization`              | Histogram       | `JobFlowId`           |
| `IsIdle`                       | `IsIdle`                       | Histogram       | `JobFlowId`           |
| `JobsFailed`                   | `JobsFailed`                   | Sum             | `JobFlowId`           |
| `JobsRunning`                  | `JobsRunning`                  | Histogram       | `JobFlowId`           |
| `LiveDataNodes`                | `LiveDataNodes`                | Histogram       | `JobFlowId`           |
| `LiveTaskTrackers`             | `LiveTaskTrackers`             | Histogram       | `JobFlowId`           |
| `MRActiveNodes`                | `MRActiveNodes`                | Histogram       | `JobFlowId`           |
| `MRDecommissionedNodes`        | `MRDecommissionedNodes`        | Histogram       | `JobFlowId`           |
| `MRLostNodes`                  | `MRLostNodes`                  | Histogram       | `JobFlowId`           |
| `MRTotalNodes`                 | `MRTotalNodes`                 | Histogram       | `JobFlowId`           |
| `MRUnhealthyNodes`             | `MRUnhealthyNodes`             | Histogram       | `JobFlowId`           |
| `MapSlotsOpen`                 | `MapSlotsOpen`                 | Histogram       | `JobFlowId`           |
| `MapTasksRemaining`            | `MapTasksRemaining`            | Histogram       | `JobFlowId`           |
| `MapTasksRunning`              | `MapTasksRunning`              | Histogram       | `JobFlowId`           |
| `MissingBlocks`                | `MissingBlocks`                | Histogram       | `JobFlowId`           |
| `ReduceSlotsOpen`              | `ReduceSlotsOpen`              | Histogram       | `JobFlowId`           |
| `ReduceTasksRemaining`         | `ReduceTasksRemaining`         | Histogram       | `JobFlowId`           |
| `ReduceTasksRunning`           | `ReduceTasksRunning`           | Histogram       | `JobFlowId`           |
| `RemainingMapTasksPerSlot`     | `RemainingMapTasksPerSlot`     | Histogram       | `JobFlowId`           |
| `S3BytesRead`                  | `S3BytesRead`                  | Sum             | `JobFlowId`           |
| `S3BytesWritten`               | `S3BytesWritten`               | Sum             | `JobFlowId`           |
| `TaskNodesPending`             | `TaskNodesPending`             | Histogram       | `JobFlowId`           |
| `TaskNodesRequested`           | `TaskNodesRequested`           | Histogram       | `JobFlowId`           |
| `TaskNodesRunning`             | `TaskNodesRunning`             | Histogram       | `JobFlowId`           |
| `TaskUnitsRequested`           | `TaskUnitsRequested`           | Histogram       | `JobFlowId`           |
| `TaskUnitsRunning`             | `TaskUnitsRunning`             | Histogram       | `JobFlowId`           |
| `TaskVCPURequested`            | `TaskVCPURequested`            | Histogram       | `JobFlowId`           |
| `TaskVCPURunning`              | `TaskVCPURunning`              | Histogram       | `JobFlowId`           |
| `TotalLoad`                    | `TotalLoad`                    | Histogram       | `JobFlowId`           |
| `TotalNodesRequested`          | `TotalNodesRequested`          | Histogram       | `JobFlowId`           |
| `TotalNodesRunning`            | `TotalNodesRunning`            | Histogram       | `JobFlowId`           |
| `TotalNotebookKernels`         | `TotalNotebookKernels`         | Histogram       | `JobFlowId`           |
| `TotalUnitsRequested`          | `TotalUnitsRequested`          | Histogram       | `JobFlowId`           |
| `TotalUnitsRunning`            | `TotalUnitsRunning`            | Histogram       | `JobFlowId`           |
| `TotalVCPURequested`           | `TotalVCPURequested`           | Histogram       | `JobFlowId`           |
| `TotalVCPURunning`             | `TotalVCPURunning`             | Histogram       | `JobFlowId`           |

## AWS/EventBridge/Pipes

The `AWS/EventBridge/Pipes` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/pipes`. All enriched instruments use Delta temporality.

- [AWS::Pipes::Pipe](#otel-enrichment-aws-eventbridge-pipes-aws-pipes-pipe "#otel-enrichment-aws-eventbridge-pipes-aws-pipes-pipe")

### AWS::Pipes::Pipe

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                       | OpenTelemetry metric         | Instrument type | Data point attributes |
| ---------------------------- | ---------------------------- | --------------- | --------------------- |
| `Duration`                   | `Duration`                   | Histogram       | `PipeName`            |
| `EnrichmentStageDuration`    | `EnrichmentStageDuration`    | Histogram       | `PipeName`            |
| `EnrichmentStageFailed`      | `EnrichmentStageFailed`      | Sum             | `PipeName`            |
| `EventCount`                 | `EventCount`                 | Sum             | `PipeName`            |
| `EventSize`                  | `EventSize`                  | Histogram       | `PipeName`            |
| `ExecutionFailed`            | `ExecutionFailed`            | Sum             | `PipeName`            |
| `ExecutionPartiallyFailed`   | `ExecutionPartiallyFailed`   | Sum             | `PipeName`            |
| `ExecutionTimeout`           | `ExecutionTimeout`           | Sum             | `PipeName`            |
| `TargetStageDuration`        | `TargetStageDuration`        | Histogram       | `PipeName`            |
| `TargetStageFailed`          | `TargetStageFailed`          | Sum             | `PipeName`            |
| `TargetStagePartiallyFailed` | `TargetStagePartiallyFailed` | Sum             | `PipeName`            |
| `TargetStageSkipped`         | `TargetStageSkipped`         | Sum             | `PipeName`            |

## AWS/Events

The `AWS/Events` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/events`. All enriched instruments use Delta temporality.

- [AWS::Events::Rule](#otel-enrichment-aws-events-aws-events-rule "#otel-enrichment-aws-events-aws-events-rule")
- [event-source](#otel-enrichment-aws-events-event-source "#otel-enrichment-aws-events-event-source")

### AWS::Events::Rule

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                 | OpenTelemetry metric                   | Instrument type | Data point attributes      |
| -------------------------------------- | -------------------------------------- | --------------- | -------------------------- |
| `FailedInvocations`                    | `FailedInvocations`                    | Sum             | `EventBusName`, `RuleName` |
| `IngestiontoInvocationCompleteLatency` | `IngestiontoInvocationCompleteLatency` | Histogram       | `EventBusName`, `RuleName` |
| `IngestiontoInvocationStartLatency`    | `IngestiontoInvocationStartLatency`    | Histogram       | `EventBusName`, `RuleName` |
| `Invocations`                          | `Invocations`                          | Sum             | `EventBusName`, `RuleName` |
| `InvocationsSentToDlq`                 | `InvocationsSentToDlq`                 | Sum             | `EventBusName`, `RuleName` |
| `ThrottledRules`                       | `ThrottledRules`                       | Sum             | `EventBusName`, `RuleName` |
| `TriggeredRules`                       | `TriggeredRules`                       | Sum             | `EventBusName`, `RuleName` |

### `event-source`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric   | OpenTelemetry metric | Instrument type | Data point attributes |
| -------- | -------------------- | --------------- | --------------------- |
| `Events` | `Events`             | Sum             | `EventSourceName`     |

## AWS/FSx

The `AWS/FSx` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/fsx`. All enriched instruments use Delta temporality.

- [AWS::FSx::FileSystem](#otel-enrichment-aws-fsx-aws-fsx-filesystem "#otel-enrichment-aws-fsx-aws-fsx-filesystem")

### AWS::FSx::FileSystem

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                | OpenTelemetry metric                  | Instrument type | Data point attributes                      |
| ------------------------------------- | ------------------------------------- | --------------- | ------------------------------------------ |
| `AgeOfOldestQueuedMessage`            | `AgeOfOldestQueuedMessage`            | Histogram       | `FileSystemId`, `Publisher`                |
| `CPUUtilization`                      | `CPUUtilization`                      | Histogram       | `FileSystemId`                             |
| `CapacityPoolReadBytes`               | `CapacityPoolReadBytes`               | Sum             | `FileSystemId`, `VolumeId`                 |
| `CapacityPoolReadOperations`          | `CapacityPoolReadOperations`          | Sum             | `FileSystemId`, `VolumeId`                 |
| `CapacityPoolWriteBytes`              | `CapacityPoolWriteBytes`              | Sum             | `FileSystemId`, `VolumeId`                 |
| `CapacityPoolWriteOperations`         | `CapacityPoolWriteOperations`         | Sum             | `FileSystemId`, `VolumeId`                 |
| `ClientConnections`                   | `ClientConnections`                   | Histogram       | `FileSystemId`                             |
| `CompressionRatio`                    | `CompressionRatio`                    | Histogram       | `FileSystemId`, `VolumeId`                 |
| `DataReadBytes`                       | `DataReadBytes`                       | Sum             | `FileSystemId`, `VolumeId`                 |
| `DataReadOperationTime`               | `DataReadOperationTime`               | Sum             | `FileSystemId`, `VolumeId`                 |
| `DataReadOperations`                  | `DataReadOperations`                  | Sum             | `FileSystemId`, `VolumeId`                 |
| `DataWriteBytes`                      | `DataWriteBytes`                      | Sum             | `FileSystemId`, `VolumeId`                 |
| `DataWriteLatency`                    | `DataWriteLatency`                    | Histogram       | `FileSystemId`, `StorageTargetId`          |
| `DataWriteOperationTime`              | `DataWriteOperationTime`              | Sum             | `FileSystemId`, `VolumeId`                 |
| `DataWriteOperations`                 | `DataWriteOperations`                 | Sum             | `FileSystemId`, `VolumeId`                 |
| `DirectoryCreateOperations`           | `DirectoryCreateOperations`           | Sum             | `FileSystemId`, `StorageTargetId`          |
| `DirectoryCreateOperations`           | `DirectoryCreateOperationsByJob`      | Sum             | `FileSystemId`, `JobId`, `StorageTargetId` |
| `DirectoryDeleteOperations`           | `DirectoryDeleteOperations`           | Sum             | `FileSystemId`, `StorageTargetId`          |
| `DirectoryDeleteOperations`           | `DirectoryDeleteOperationsByJob`      | Sum             | `FileSystemId`, `JobId`, `StorageTargetId` |
| `DiskIopsExceededCheck`               | `DiskIopsExceededCheck`               | Histogram       | `FileSystemId`, `StorageTargetId`          |
| `DiskThroughputBalance`               | `DiskThroughputBalance`               | Histogram       | `FileSystemId`                             |
| `DiskThroughputExceededCheck`         | `DiskThroughputExceededCheck`         | Histogram       | `FileSystemId`, `StorageTargetId`          |
| `DiskThroughputUtilization`           | `DiskThroughputUtilization`           | Histogram       | `FileSystemId`                             |
| `FileCreateOperations`                | `FileCreateOperations`                | Sum             | `FileSystemId`, `StorageTargetId`          |
| `FileCreateOperations`                | `FileCreateOperationsByJob`           | Sum             | `FileSystemId`, `JobId`, `StorageTargetId` |
| `FileDeleteOperations`                | `FileDeleteOperations`                | Sum             | `FileSystemId`, `StorageTargetId`          |
| `FileDeleteOperations`                | `FileDeleteOperationsByJob`           | Sum             | `FileSystemId`, `JobId`, `StorageTargetId` |
| `FileOpenOperations`                  | `FileOpenOperations`                  | Sum             | `FileSystemId`, `StorageTargetId`          |
| `FileOpenOperations`                  | `FileOpenOperationsByJob`             | Sum             | `FileSystemId`, `JobId`, `StorageTargetId` |
| `FileServerDiskIopsBalance`           | `FileServerDiskIopsBalance`           | Histogram       | `FileSystemId`                             |
| `FileServerDiskIopsUtilization`       | `FileServerDiskIopsUtilization`       | Histogram       | `FileSystemId`                             |
| `FileServerDiskThroughputBalance`     | `FileServerDiskThroughputBalance`     | Histogram       | `FileServer`, `FileSystemId`               |
| `FileServerDiskThroughputUtilization` | `FileServerDiskThroughputUtilization` | Histogram       | `FileSystemId`                             |
| `FilesCapacity`                       | `FilesCapacity`                       | Histogram       | `FileSystemId`, `VolumeId`                 |
| `FilesUsed`                           | `FilesUsed`                           | Histogram       | `FileSystemId`, `VolumeId`                 |
| `FreeDataStorageCapacity`             | `FreeDataStorageCapacity`             | Histogram       | `FileSystemId`                             |
| `FreeStorageCapacity`                 | `FreeStorageCapacity`                 | Histogram       | `FileSystemId`                             |
| `MemoryUtilization`                   | `MemoryUtilization`                   | Histogram       | `FileSystemId`                             |
| `MetadataOperationTime`               | `MetadataOperationTime`               | Sum             | `FileSystemId`, `VolumeId`                 |
| `MetadataOperations`                  | `MetadataOperations`                  | Sum             | `FileSystemId`, `VolumeId`                 |
| `NetworkReceivedBytes`                | `NetworkReceivedBytes`                | Sum             | `FileServer`, `FileSystemId`               |
| `NetworkSentBytes`                    | `NetworkSentBytes`                    | Sum             | `FileServer`, `FileSystemId`               |
| `NetworkThroughputUtilization`        | `NetworkThroughputUtilization`        | Histogram       | `FileSystemId`                             |
| `RenameOperations`                    | `RenameOperationsByJob`               | Sum             | `FileSystemId`, `JobId`, `StorageTargetId` |
| `RepositoryRenameOperations`          | `RepositoryRenameOperations`          | Sum             | `FileSystemId`, `Publisher`                |
| `StatOperations`                      | `StatOperationsByJob`                 | Sum             | `FileSystemId`, `JobId`, `StorageTargetId` |

## AWS/Firehose

The `AWS/Firehose` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/firehose`. All enriched instruments use Delta temporality.

- [AWS::KinesisFirehose::DeliveryStream](#otel-enrichment-aws-firehose-aws-kinesisfirehose-deliverystream "#otel-enrichment-aws-firehose-aws-kinesisfirehose-deliverystream")

### AWS::KinesisFirehose::DeliveryStream

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                                  | OpenTelemetry metric                                    | Instrument type | Data point attributes                    |
| ------------------------------------------------------- | ------------------------------------------------------- | --------------- | ---------------------------------------- |
| `BackupToS3.Bytes`                                      | `BackupToS3.Bytes`                                      | Sum             | `DeliveryStreamName`                     |
| `BackupToS3.DataFreshness`                              | `BackupToS3.DataFreshness`                              | Histogram       | `DeliveryStreamName`                     |
| `BackupToS3.Records`                                    | `BackupToS3.Records`                                    | Sum             | `DeliveryStreamName`                     |
| `BackupToS3.Success`                                    | `BackupToS3.Success`                                    | Sum             | `DeliveryStreamName`                     |
| `BytesPerSecondLimit`                                   | `BytesPerSecondLimit`                                   | Histogram       | `DeliveryStreamName`                     |
| `DataReadFromKinesisStream.Bytes`                       | `DataReadFromKinesisStream.Bytes`                       | Sum             | `DeliveryStreamName`                     |
| `DataReadFromKinesisStream.Records`                     | `DataReadFromKinesisStream.Records`                     | Sum             | `DeliveryStreamName`                     |
| `DataReadFromSource.Backpressured`                      | `DataReadFromSource.Backpressured`                      | Sum             | `DeliveryStreamName`                     |
| `DataReadFromSource.Bytes`                              | `DataReadFromSource.Bytes`                              | Sum             | `DeliveryStreamName`                     |
| `DataReadFromSource.Records`                            | `DataReadFromSource.Records`                            | Sum             | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchServerless.AuthFailure`      | `DeliveryToAmazonOpenSearchServerless.AuthFailure`      | Sum             | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchServerless.Bytes`            | `DeliveryToAmazonOpenSearchServerless.Bytes`            | Sum             | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchServerless.DataFreshness`    | `DeliveryToAmazonOpenSearchServerless.DataFreshness`    | Histogram       | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchServerless.DeliveryRejected` | `DeliveryToAmazonOpenSearchServerless.DeliveryRejected` | Sum             | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchServerless.Records`          | `DeliveryToAmazonOpenSearchServerless.Records`          | Sum             | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchServerless.Success`          | `DeliveryToAmazonOpenSearchServerless.Success`          | Sum             | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchService.AuthFailure`         | `DeliveryToAmazonOpenSearchService.AuthFailure`         | Sum             | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchService.Bytes`               | `DeliveryToAmazonOpenSearchService.Bytes`               | Sum             | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchService.DataFreshness`       | `DeliveryToAmazonOpenSearchService.DataFreshness`       | Histogram       | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchService.DeliveryRejected`    | `DeliveryToAmazonOpenSearchService.DeliveryRejected`    | Sum             | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchService.Records`             | `DeliveryToAmazonOpenSearchService.Records`             | Sum             | `DeliveryStreamName`                     |
| `DeliveryToAmazonOpenSearchService.Success`             | `DeliveryToAmazonOpenSearchService.Success`             | Sum             | `DeliveryStreamName`                     |
| `DeliveryToHttpEndpoint.Bytes`                          | `DeliveryToHttpEndpoint.Bytes`                          | Sum             | `DeliveryStreamName`                     |
| `DeliveryToHttpEndpoint.DataFreshness`                  | `DeliveryToHttpEndpoint.DataFreshness`                  | Histogram       | `DeliveryStreamName`                     |
| `DeliveryToHttpEndpoint.ProcessedBytes`                 | `DeliveryToHttpEndpoint.ProcessedBytes`                 | Sum             | `DeliveryStreamName`                     |
| `DeliveryToHttpEndpoint.ProcessedRecords`               | `DeliveryToHttpEndpoint.ProcessedRecords`               | Sum             | `DeliveryStreamName`                     |
| `DeliveryToHttpEndpoint.Records`                        | `DeliveryToHttpEndpoint.Records`                        | Sum             | `DeliveryStreamName`                     |
| `DeliveryToHttpEndpoint.Success`                        | `DeliveryToHttpEndpoint.Success`                        | Sum             | `DeliveryStreamName`                     |
| `DeliveryToIceberg.Bytes`                               | `DeliveryToIceberg.Bytes`                               | Sum             | `DeliveryStreamName`, `IcebergTableName` |
| `DeliveryToIceberg.DataFreshness`                       | `DeliveryToIceberg.DataFreshness`                       | Histogram       | `DeliveryStreamName`, `IcebergTableName` |
| `DeliveryToIceberg.Success`                             | `DeliveryToIceberg.Success`                             | Sum             | `DeliveryStreamName`, `IcebergTableName` |
| `DeliveryToIceberg.SuccessfulRowCount`                  | `DeliveryToIceberg.SuccessfulRowCount`                  | Sum             | `DeliveryStreamName`, `IcebergTableName` |
| `DeliveryToRedshift.Bytes`                              | `DeliveryToRedshift.Bytes`                              | Sum             | `DeliveryStreamName`                     |
| `DeliveryToRedshift.Records`                            | `DeliveryToRedshift.Records`                            | Sum             | `DeliveryStreamName`                     |
| `DeliveryToRedshift.Success`                            | `DeliveryToRedshift.Success`                            | Sum             | `DeliveryStreamName`                     |
| `DeliveryToS3.Bytes`                                    | `DeliveryToS3.Bytes`                                    | Sum             | `DeliveryStreamName`                     |
| `DeliveryToS3.DataFreshness`                            | `DeliveryToS3.DataFreshness`                            | Histogram       | `DeliveryStreamName`                     |
| `DeliveryToS3.Records`                                  | `DeliveryToS3.Records`                                  | Sum             | `DeliveryStreamName`                     |
| `DeliveryToS3.Success`                                  | `DeliveryToS3.Success`                                  | Sum             | `DeliveryStreamName`                     |
| `DeliveryToSnowflake.Bytes`                             | `DeliveryToSnowflake.Bytes`                             | Sum             | `DeliveryStreamName`                     |
| `DeliveryToSnowflake.DataCommitLatency`                 | `DeliveryToSnowflake.DataCommitLatency`                 | Histogram       | `DeliveryStreamName`                     |
| `DeliveryToSnowflake.DataFreshness`                     | `DeliveryToSnowflake.DataFreshness`                     | Histogram       | `DeliveryStreamName`                     |
| `DeliveryToSnowflake.Records`                           | `DeliveryToSnowflake.Records`                           | Sum             | `DeliveryStreamName`                     |
| `DeliveryToSnowflake.Success`                           | `DeliveryToSnowflake.Success`                           | Sum             | `DeliveryStreamName`                     |
| `DeliveryToSplunk.Bytes`                                | `DeliveryToSplunk.Bytes`                                | Sum             | `DeliveryStreamName`                     |
| `DeliveryToSplunk.DataAckLatency`                       | `DeliveryToSplunk.DataAckLatency`                       | Histogram       | `DeliveryStreamName`                     |
| `DeliveryToSplunk.DataFreshness`                        | `DeliveryToSplunk.DataFreshness`                        | Histogram       | `DeliveryStreamName`                     |
| `DeliveryToSplunk.Records`                              | `DeliveryToSplunk.Records`                              | Sum             | `DeliveryStreamName`                     |
| `DeliveryToSplunk.Success`                              | `DeliveryToSplunk.Success`                              | Sum             | `DeliveryStreamName`                     |
| `DescribeDeliveryStream.Latency`                        | `DescribeDeliveryStream.Latency`                        | Histogram       | `DeliveryStreamName`                     |
| `DescribeDeliveryStream.Requests`                       | `DescribeDeliveryStream.Requests`                       | Sum             | `DeliveryStreamName`                     |
| `ExecuteProcessing.Duration`                            | `ExecuteProcessing.Duration`                            | Histogram       | `DeliveryStreamName`                     |
| `ExecuteProcessing.Success`                             | `ExecuteProcessing.Success`                             | Sum             | `DeliveryStreamName`                     |
| `FailedConversion.Bytes`                                | `FailedConversion.Bytes`                                | Sum             | `DeliveryStreamName`                     |
| `FailedConversion.Records`                              | `FailedConversion.Records`                              | Sum             | `DeliveryStreamName`                     |
| `FailedValidation.Bytes`                                | `FailedValidation.Bytes`                                | Sum             | `DeliveryStreamName`                     |
| `FailedValidation.Records`                              | `FailedValidation.Records`                              | Sum             | `DeliveryStreamName`                     |
| `IncomingBytes`                                         | `IncomingBytes`                                         | Sum             | `DeliveryStreamName`                     |
| `IncomingPutRequests`                                   | `IncomingPutRequests`                                   | Sum             | `DeliveryStreamName`                     |
| `IncomingRecords`                                       | `IncomingRecords`                                       | Sum             | `DeliveryStreamName`                     |
| `KMSKeyAccessDenied`                                    | `KMSKeyAccessDenied`                                    | Sum             | `DeliveryStreamName`                     |
| `KMSKeyDisabled`                                        | `KMSKeyDisabled`                                        | Sum             | `DeliveryStreamName`                     |
| `KMSKeyInvalidState`                                    | `KMSKeyInvalidState`                                    | Sum             | `DeliveryStreamName`                     |
| `KMSKeyNotFound`                                        | `KMSKeyNotFound`                                        | Sum             | `DeliveryStreamName`                     |
| `KafkaOffsetLag`                                        | `KafkaOffsetLag`                                        | Histogram       | `DeliveryStreamName`                     |
| `KinesisMillisBehindLatest`                             | `KinesisMillisBehindLatest`                             | Histogram       | `DeliveryStreamName`                     |
| `ListDeliveryStreams.Latency`                           | `ListDeliveryStreams.Latency`                           | Histogram       | `DeliveryStreamName`                     |
| `ListDeliveryStreams.Requests`                          | `ListDeliveryStreams.Requests`                          | Sum             | `DeliveryStreamName`                     |
| `OutputDecompressedBytes.Failed`                        | `OutputDecompressedBytes.Failed`                        | Sum             | `DeliveryStreamName`                     |
| `OutputDecompressedBytes.Success`                       | `OutputDecompressedBytes.Success`                       | Sum             | `DeliveryStreamName`                     |
| `OutputDecompressedRecords.Failed`                      | `OutputDecompressedRecords.Failed`                      | Sum             | `DeliveryStreamName`                     |
| `OutputDecompressedRecords.Success`                     | `OutputDecompressedRecords.Success`                     | Sum             | `DeliveryStreamName`                     |
| `PutRecord.Bytes`                                       | `PutRecord.Bytes`                                       | Histogram       | `DeliveryStreamName`                     |
| `PutRecord.Latency`                                     | `PutRecord.Latency`                                     | Histogram       | `DeliveryStreamName`                     |
| `PutRecord.Requests`                                    | `PutRecord.Requests`                                    | Sum             | `DeliveryStreamName`                     |
| `PutRecordBatch.Bytes`                                  | `PutRecordBatch.Bytes`                                  | Histogram       | `DeliveryStreamName`                     |
| `PutRecordBatch.Latency`                                | `PutRecordBatch.Latency`                                | Histogram       | `DeliveryStreamName`                     |
| `PutRecordBatch.Records`                                | `PutRecordBatch.Records`                                | Histogram       | `DeliveryStreamName`                     |
| `PutRecordBatch.Requests`                               | `PutRecordBatch.Requests`                               | Sum             | `DeliveryStreamName`                     |
| `PutRequestsPerSecondLimit`                             | `PutRequestsPerSecondLimit`                             | Histogram       | `DeliveryStreamName`                     |
| `RecordsPerSecondLimit`                                 | `RecordsPerSecondLimit`                                 | Histogram       | `DeliveryStreamName`                     |
| `SourceThrottled.Delay`                                 | `SourceThrottled.Delay`                                 | Histogram       | `DeliveryStreamName`                     |
| `SourceToDelivery.DataFreshness`                        | `SourceToDelivery.DataFreshness`                        | Histogram       | `DeliveryStreamName`                     |
| `SucceedConversion.Bytes`                               | `SucceedConversion.Bytes`                               | Sum             | `DeliveryStreamName`                     |
| `SucceedConversion.Records`                             | `SucceedConversion.Records`                             | Sum             | `DeliveryStreamName`                     |
| `SucceedProcessing.Bytes`                               | `SucceedProcessing.Bytes`                               | Sum             | `DeliveryStreamName`                     |
| `SucceedProcessing.Records`                             | `SucceedProcessing.Records`                             | Sum             | `DeliveryStreamName`                     |
| `ThrottledDescribeStream`                               | `ThrottledDescribeStream`                               | Sum             | `DeliveryStreamName`                     |
| `ThrottledGetRecords`                                   | `ThrottledGetRecords`                                   | Sum             | `DeliveryStreamName`                     |
| `ThrottledGetShardIterator`                             | `ThrottledGetShardIterator`                             | Sum             | `DeliveryStreamName`                     |
| `ThrottledRecords`                                      | `ThrottledRecords`                                      | Sum             | `DeliveryStreamName`                     |
| `UpdateDeliveryStream.Latency`                          | `UpdateDeliveryStream.Latency`                          | Histogram       | `DeliveryStreamName`                     |
| `UpdateDeliveryStream.Requests`                         | `UpdateDeliveryStream.Requests`                         | Sum             | `DeliveryStreamName`                     |

## AWS/FraudDetector

The `AWS/FraudDetector` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/frauddetector`. All enriched instruments use Delta temporality.

- [AWS::FraudDetector::Detector](#otel-enrichment-aws-frauddetector-aws-frauddetector-detector "#otel-enrichment-aws-frauddetector-aws-frauddetector-detector")

### AWS::FraudDetector::Detector

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                       | OpenTelemetry metric         | Instrument type | Data point attributes                                                           |
| ---------------------------- | ---------------------------- | --------------- | ------------------------------------------------------------------------------- |
| `GetEventPrediction`         | `GetEventPrediction`         | Sum             | `DetectorID`                                                                    |
| `GetEventPrediction4xxError` | `GetEventPrediction4xxError` | Sum             | `DetectorID`                                                                    |
| `GetEventPrediction5xxError` | `GetEventPrediction5xxError` | Sum             | `DetectorID`                                                                    |
| `GetEventPredictionLatency`  | `GetEventPredictionLatency`  | Histogram       | `DetectorID`                                                                    |
| `ModelInvocation`            | `ModelInvocation`            | Sum             | `DetectorID`, `DetectorVersionID`, `ModelID`, `ModelType`, `ModelVersionNumber` |
| `ModelInvocationError`       | `ModelInvocationError`       | Sum             | `DetectorID`, `DetectorVersionID`, `ModelID`, `ModelType`, `ModelVersionNumber` |
| `ModelInvocationLatency`     | `ModelInvocationLatency`     | Histogram       | `DetectorID`, `DetectorVersionID`, `ModelID`, `ModelType`, `ModelVersionNumber` |
| `OutcomeReturned`            | `OutcomeReturned`            | Sum             | `DetectorID`, `DetectorVersionID`, `OutcomeName`                                |
| `Prediction`                 | `Prediction`                 | Sum             | `DetectorID`, `DetectorVersionID`                                               |
| `PredictionError`            | `PredictionError`            | Sum             | `DetectorID`, `DetectorVersionID`                                               |
| `PredictionLatency`          | `PredictionLatency`          | Histogram       | `DetectorID`, `DetectorVersionID`                                               |
| `RuleEvaluateFalse`          | `RuleEvaluateFalse`          | Sum             | `DetectorID`, `DetectorVersionID`, `RuleID`                                     |
| `RuleEvaluateTrue`           | `RuleEvaluateTrue`           | Sum             | `DetectorID`, `DetectorVersionID`, `RuleID`                                     |
| `RuleNotEvaluated`           | `RuleNotEvaluated`           | Sum             | `DetectorID`, `DetectorVersionID`, `RuleID`                                     |
| `VariableUsed`               | `VariableUsed`               | Sum             | `DetectorID`, `DetectorVersionID`, `VariableName`                               |

## AWS/GameLift

The `AWS/GameLift` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/gamelift`. All enriched instruments use Delta temporality.

- [AWS::GameLift::Fleet](#otel-enrichment-aws-gamelift-aws-gamelift-fleet "#otel-enrichment-aws-gamelift-aws-gamelift-fleet")
- [AWS::GameLift::GameSessionQueue](#otel-enrichment-aws-gamelift-aws-gamelift-gamesessionqueue "#otel-enrichment-aws-gamelift-aws-gamelift-gamesessionqueue")
- [AWS::GameLift::MatchmakingConfiguration](#otel-enrichment-aws-gamelift-aws-gamelift-matchmakingconfiguration "#otel-enrichment-aws-gamelift-aws-gamelift-matchmakingconfiguration")

### AWS::GameLift::Fleet

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                                       | OpenTelemetry metric                         | Instrument type | Data point attributes                       |
| -------------------------------------------- | -------------------------------------------- | --------------- | ------------------------------------------- |
| `ActivatingGameSessions`                     | `ActivatingGameSessions`                     | Histogram       | `FleetId`, `Location`                       |
| `ActiveGameServerContainerGroups`            | `ActiveGameServerContainerGroups`            | Histogram       | `FleetId`, `Location`                       |
| `ActiveGameSessions`                         | `ActiveGameSessions`                         | Histogram       | `FleetId`, `Location`                       |
| `ActiveInstances`                            | `ActiveInstances`                            | Histogram       | `FleetId`, `Location`                       |
| `ActiveServerProcesses`                      | `ActiveServerProcesses`                      | Histogram       | `FleetId`, `Location`                       |
| `AvailableGameSessions`                      | `AvailableGameSessions`                      | Histogram       | `FleetId`, `Location`                       |
| `AvailablePlayerSessions`                    | `AvailablePlayerSessions`                    | Histogram       | `FleetId`, `Location`                       |
| `CPUUtilization`                             | `CPUUtilization`                             | Histogram       | `FleetId`, `Location`                       |
| `ConcurrentActivatableGameSessions`          | `ConcurrentActivatableGameSessions`          | Histogram       | `FleetId`, `Location`                       |
| `ContainerCPUReservation`                    | `ContainerCPUReservation`                    | Histogram       | `FleetId`, `Location`                       |
| `ContainerCPUUtilizationPerInstance`         | `ContainerCPUUtilizationPerInstance`         | Histogram       | `FleetId`, `Location`                       |
| `ContainerMemoryReservation`                 | `ContainerMemoryReservation`                 | Histogram       | `FleetId`, `Location`                       |
| `ContainerMemoryUtilization`                 | `ContainerMemoryUtilization`                 | Histogram       | `FleetId`, `Location`                       |
| `ContainerNetworkIn`                         | `ContainerNetworkIn`                         | Sum             | `ContainerGroupType`, `FleetId`, `Location` |
| `ContainerNetworkOut`                        | `ContainerNetworkOut`                        | Sum             | `ContainerGroupType`, `FleetId`, `Location` |
| `ContainerStorageReadBytes`                  | `ContainerStorageReadBytes`                  | Sum             | `ContainerGroupType`, `FleetId`, `Location` |
| `ContainerStorageWriteBytes`                 | `ContainerStorageWriteBytes`                 | Sum             | `ContainerGroupType`, `FleetId`, `Location` |
| `CurrentPlayerSessions`                      | `CurrentPlayerSessions`                      | Histogram       | `FleetId`, `Location`                       |
| `DesiredInstances`                           | `DesiredInstances`                           | Histogram       | `FleetId`, `Location`                       |
| `DiskReadBytes`                              | `DiskReadBytes`                              | Sum             | `FleetId`, `Location`                       |
| `DiskReadOps`                                | `DiskReadOps`                                | Sum             | `FleetId`, `Location`                       |
| `DiskWriteBytes`                             | `DiskWriteBytes`                             | Sum             | `FleetId`, `Location`                       |
| `DiskWriteOps`                               | `DiskWriteOps`                               | Sum             | `FleetId`, `Location`                       |
| `GameSessionInterruptions`                   | `GameSessionInterruptions`                   | Sum             | `FleetId`, `Location`                       |
| `HealthyServerProcesses`                     | `HealthyServerProcesses`                     | Histogram       | `FleetId`, `Location`                       |
| `IdleGameServerContainerGroups`              | `IdleGameServerContainerGroups`              | Histogram       | `FleetId`, `Location`                       |
| `IdleInstances`                              | `IdleInstances`                              | Histogram       | `FleetId`, `Location`                       |
| `InstanceCPUUtilization`                     | `InstanceCPUUtilization`                     | Histogram       | `FleetId`, `Location`                       |
| `InstanceInterruptions`                      | `InstanceInterruptions`                      | Sum             | `FleetId`, `Location`                       |
| `InstanceNetworkIn`                          | `InstanceNetworkIn`                          | Sum             | `FleetId`, `Location`                       |
| `InstanceNetworkOut`                         | `InstanceNetworkOut`                         | Sum             | `FleetId`, `Location`                       |
| `InstanceStorageReadBytes`                   | `InstanceStorageReadBytes`                   | Sum             | `FleetId`, `Location`                       |
| `InstanceStorageReadOps`                     | `InstanceStorageReadOps`                     | Sum             | `FleetId`, `Location`                       |
| `InstanceStorageWriteBytes`                  | `InstanceStorageWriteBytes`                  | Sum             | `FleetId`, `Location`                       |
| `InstanceStorageWriteOps`                    | `InstanceStorageWriteOps`                    | Sum             | `FleetId`, `Location`                       |
| `MaxInstances`                               | `MaxInstances`                               | Histogram       | `FleetId`, `Location`                       |
| `MinInstances`                               | `MinInstances`                               | Histogram       | `FleetId`, `Location`                       |
| `NetworkIn`                                  | `NetworkIn`                                  | Sum             | `FleetId`, `Location`                       |
| `NetworkOut`                                 | `NetworkOut`                                 | Sum             | `FleetId`, `Location`                       |
| `PendingGameServerContainerGroups`           | `PendingGameServerContainerGroups`           | Histogram       | `FleetId`, `Location`                       |
| `PendingInstances`                           | `PendingInstances`                           | Histogram       | `FleetId`, `Location`                       |
| `PercentAvailableGameSessions`               | `PercentAvailableGameSessions`               | Histogram       | `FleetId`, `Location`                       |
| `PercentHealthyServerProcesses`              | `PercentHealthyServerProcesses`              | Histogram       | `FleetId`, `Location`                       |
| `PercentIdleInstances`                       | `PercentIdleInstances`                       | Histogram       | `FleetId`, `Location`                       |
| `PlayerGatewayBytesIn`                       | `PlayerGatewayBytesIn`                       | Sum             | `FleetId`                                   |
| `PlayerGatewayBytesOut`                      | `PlayerGatewayBytesOut`                      | Sum             | `FleetId`, `Location`                       |
| `PlayerGatewayBytesThrottled`                | `PlayerGatewayBytesThrottled`                | Sum             | `FleetId`, `Location`                       |
| `PlayerGatewayPacketsIn`                     | `PlayerGatewayPacketsIn`                     | Sum             | `FleetId`, `Location`                       |
| `PlayerGatewayPacketsOut`                    | `PlayerGatewayPacketsOut`                    | Sum             | `FleetId`, `Location`                       |
| `PlayerGatewayPacketsThrottled`              | `PlayerGatewayPacketsThrottled`              | Sum             | `FleetId`, `Location`                       |
| `PlayerGatewayPlayerSessions`                | `PlayerGatewayPlayerSessions`                | Sum             | `FleetId`, `Location`                       |
| `PlayerSessionActivations`                   | `PlayerSessionActivations`                   | Sum             | `FleetId`, `Location`                       |
| `RecycledInstances`                          | `RecycledInstances`                          | Sum             | `FleetId`, `Location`                       |
| `ServerProcessAbnormalTerminations`          | `ServerProcessAbnormalTerminations`          | Sum             | `FleetId`, `Location`                       |
| `ServerProcessActivations`                   | `ServerProcessActivations`                   | Sum             | `FleetId`, `Location`                       |
| `ServerProcessTerminations`                  | `ServerProcessTerminations`                  | Sum             | `FleetId`, `Location`                       |
| `TerminatingGameServerContainerGroups`       | `TerminatingGameServerContainerGroups`       | Histogram       | `FleetId`, `Location`                       |
| `TerminatingInstances`                       | `TerminatingInstances`                       | Histogram       | `FleetId`, `Location`                       |
| `UnhealthyGameServerContainerGroupsReplaced` | `UnhealthyGameServerContainerGroupsReplaced` | Sum             | `FleetId`, `Location`                       |
| `UnhealthyInstancesReplaced`                 | `UnhealthyInstancesReplaced`                 | Sum             | `FleetId`, `Location`                       |

### AWS::GameLift::GameSessionQueue

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                     | OpenTelemetry metric       | Instrument type | Data point attributes       |
| -------------------------- | -------------------------- | --------------- | --------------------------- |
| `AverageWaitTime`          | `AverageWaitTime`          | Histogram       | `Location`, `QueueName`     |
| `FirstChoiceNotViable`     | `FirstChoiceNotViable`     | Sum             | `QueueName`                 |
| `FirstChoiceOutOfCapacity` | `FirstChoiceOutOfCapacity` | Sum             | `QueueName`                 |
| `GameSessionPlaced`        | `GameSessionPlaced`        | Sum             | `LocationName`, `QueueName` |
| `LowestLatencyPlacement`   | `LowestLatencyPlacement`   | Sum             | `QueueName`                 |
| `LowestPricePlacement`     | `LowestPricePlacement`     | Sum             | `QueueName`                 |
| `PlacementApNortheast1`    | `PlacementApNortheast1`    | Sum             | `QueueName`                 |
| `PlacementApNortheast2`    | `PlacementApNortheast2`    | Sum             | `QueueName`                 |
| `PlacementApSouth1`        | `PlacementApSouth1`        | Sum             | `QueueName`                 |
| `PlacementApSoutheast2`    | `PlacementApSoutheast2`    | Sum             | `QueueName`                 |
| `PlacementEuCentral1`      | `PlacementEuCentral1`      | Sum             | `QueueName`                 |
| `PlacementEuNorth1`        | `PlacementEuNorth1`        | Sum             | `QueueName`                 |
| `PlacementEuWest1`         | `PlacementEuWest1`         | Sum             | `QueueName`                 |
| `PlacementEuWest2`         | `PlacementEuWest2`         | Sum             | `QueueName`                 |
| `PlacementMeSouth1`        | `PlacementMeSouth1`        | Sum             | `QueueName`                 |
| `PlacementSaEast1`         | `PlacementSaEast1`         | Sum             | `QueueName`                 |
| `PlacementUsEast1`         | `PlacementUsEast1`         | Sum             | `QueueName`                 |
| `PlacementUsEast2`         | `PlacementUsEast2`         | Sum             | `QueueName`                 |
| `PlacementUsWest1`         | `PlacementUsWest1`         | Sum             | `QueueName`                 |
| `PlacementUsWest2`         | `PlacementUsWest2`         | Sum             | `QueueName`                 |
| `PlacementsCanceled`       | `PlacementsCanceled`       | Sum             | `QueueName`                 |
| `PlacementsStarted`        | `PlacementsStarted`        | Sum             | `QueueName`                 |
| `PlacementsSucceeded`      | `PlacementsSucceeded`      | Sum             | `QueueName`                 |
| `PlacementsTimedOut`       | `PlacementsTimedOut`       | Sum             | `QueueName`                 |
| `QueueDepth`               | `QueueDepth`               | Histogram       | `Location`, `QueueName`     |

### AWS::GameLift::MatchmakingConfiguration

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                  | OpenTelemetry metric    | Instrument type | Data point attributes |
| ----------------------- | ----------------------- | --------------- | --------------------- |
| `CurrentTickets`        | `CurrentTickets`        | Histogram       | `ConfigurationName`   |
| `MatchesAccepted`       | `MatchesAccepted`       | Sum             | `ConfigurationName`   |
| `MatchesCreated`        | `MatchesCreated`        | Sum             | `ConfigurationName`   |
| `MatchesPlaced`         | `MatchesPlaced`         | Sum             | `ConfigurationName`   |
| `MatchesRejected`       | `MatchesRejected`       | Sum             | `ConfigurationName`   |
| `MatchmakingSearchTime` | `MatchmakingSearchTime` | Histogram       | `ConfigurationName`   |
| `PlayersStarted`        | `PlayersStarted`        | Sum             | `ConfigurationName`   |
| `TicketsStarted`        | `TicketsStarted`        | Sum             | `ConfigurationName`   |
| `TicketsTimedOut`       | `TicketsTimedOut`       | Sum             | `ConfigurationName`   |
| `TimeToMatch`           | `TimeToMatch`           | Histogram       | `ConfigurationName`   |
| `TimeToTicketCancel`    | `TimeToTicketCancel`    | Histogram       | `ConfigurationName`   |
| `TimeToTicketSuccess`   | `TimeToTicketSuccess`   | Histogram       | `ConfigurationName`   |

## AWS/GatewayELB

The `AWS/GatewayELB` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/elasticloadbalancing`. All enriched instruments use Delta temporality.

- [AWS::ElasticLoadBalancingV2::LoadBalancer](#otel-enrichment-aws-gatewayelb-aws-elasticloadbalancingv2-loadbalancer "#otel-enrichment-aws-gatewayelb-aws-elasticloadbalancingv2-loadbalancer")

### AWS::ElasticLoadBalancingV2::LoadBalancer

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric               | OpenTelemetry metric | Instrument type | Data point attributes                             |
| -------------------- | -------------------- | --------------- | ------------------------------------------------- |
| `ActiveFlowCount`    | `ActiveFlowCount`    | Histogram       | `AvailabilityZone`, `LoadBalancer`                |
| `HealthyHostCount`   | `HealthyHostCount`   | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `NewFlowCount`       | `NewFlowCount`       | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ProcessedBytes`     | `ProcessedBytes`     | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `UnHealthyHostCount` | `UnHealthyHostCount` | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |

## AWS/IVSChat

The `AWS/IVSChat` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/ivschat`. All enriched instruments use Delta temporality.

- [AWS::IVSChat::LoggingConfiguration](#otel-enrichment-aws-ivschat-aws-ivschat-loggingconfiguration "#otel-enrichment-aws-ivschat-aws-ivschat-loggingconfiguration")

### AWS::IVSChat::LoggingConfiguration

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                 | OpenTelemetry metric                   | Instrument type | Data point attributes  |
| -------------------------------------- | -------------------------------------- | --------------- | ---------------------- |
| `LogDestinationAccessDeniedError`      | `LogDestinationAccessDeniedError`      | Sum             | `LoggingConfiguration` |
| `LogDestinationErrors`                 | `LogDestinationErrors`                 | Sum             | `LoggingConfiguration` |
| `LogDestinationResourceNotFoundErrors` | `LogDestinationResourceNotFoundErrors` | Sum             | `LoggingConfiguration` |

## AWS/IoT

The `AWS/IoT` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/iot`. All enriched instruments use Delta temporality.

- [AWS::IoT::CACertificate](#otel-enrichment-aws-iot-aws-iot-cacertificate "#otel-enrichment-aws-iot-aws-iot-cacertificate")
- [AWS::IoT::ScheduledAudit](#otel-enrichment-aws-iot-aws-iot-scheduledaudit "#otel-enrichment-aws-iot-aws-iot-scheduledaudit")
- [AWS::IoT::SecurityProfile](#otel-enrichment-aws-iot-aws-iot-securityprofile "#otel-enrichment-aws-iot-aws-iot-securityprofile")
- [AWS::IoT::TopicRule](#otel-enrichment-aws-iot-aws-iot-topicrule "#otel-enrichment-aws-iot-aws-iot-topicrule")
- [job](#otel-enrichment-aws-iot-job "#otel-enrichment-aws-iot-job")

### AWS::IoT::CACertificate

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                       | OpenTelemetry metric         | Instrument type | Data point attributes |
| ---------------------------- | ---------------------------- | --------------- | --------------------- |
| `ProvisionThing.ClientError` | `ProvisionThing.ClientError` | Sum             | `CaCertificateId`     |
| `ProvisionThing.ServerError` | `ProvisionThing.ServerError` | Sum             | `CaCertificateId`     |
| `ProvisionThing.Success`     | `ProvisionThing.Success`     | Sum             | `CaCertificateId`     |

### AWS::IoT::ScheduledAudit

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                    | OpenTelemetry metric                      | Instrument type | Data point attributes             |
| ----------------------------------------- | ----------------------------------------- | --------------- | --------------------------------- |
| `MisconfiguredDeviceDefenderNotification` | `MisconfiguredDeviceDefenderNotification` | Sum             | `CheckName`, `ScheduledAuditName` |
| `NonCompliantResources`                   | `NonCompliantResources`                   | Sum             | `CheckName`, `ScheduledAuditName` |
| `ResourcesEvaluated`                      | `ResourcesEvaluated`                      | Sum             | `CheckName`, `ScheduledAuditName` |

### AWS::IoT::SecurityProfile

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                    | OpenTelemetry metric                      | Instrument type | Data point attributes                 |
| ----------------------------------------- | ----------------------------------------- | --------------- | ------------------------------------- |
| `BehaviorEvaluationCompleted`             | `BehaviorEvaluationCompleted`             | Sum             | `BehaviorName`, `SecurityProfileName` |
| `BehaviorEvaluationSkipped`               | `BehaviorEvaluationSkipped`               | Sum             | `BehaviorName`, `SecurityProfileName` |
| `MisconfiguredDeviceDefenderNotification` | `MisconfiguredDeviceDefenderNotification` | Sum             | `BehaviorName`, `SecurityProfileName` |
| `NumOfMetricsExceedingSizeLimit`          | `NumOfMetricsExceedingSizeLimit`          | Sum             | `BehaviorName`, `SecurityProfileName` |
| `NumOfMetricsExported`                    | `NumOfMetricsExported`                    | Sum             | `BehaviorName`, `SecurityProfileName` |
| `NumOfMetricsSkipped`                     | `NumOfMetricsSkipped`                     | Sum             | `BehaviorName`, `SecurityProfileName` |
| `Violations`                              | `Violations`                              | Sum             | `BehaviorName`, `SecurityProfileName` |
| `ViolationsCleared`                       | `ViolationsCleared`                       | Sum             | `BehaviorName`, `SecurityProfileName` |
| `ViolationsInvalidated`                   | `ViolationsInvalidated`                   | Sum             | `BehaviorName`, `SecurityProfileName` |

### AWS::IoT::TopicRule

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                 | OpenTelemetry metric                   | Instrument type | Data point attributes    |
| -------------------------------------- | -------------------------------------- | --------------- | ------------------------ |
| `ErrorActionFailure`                   | `ErrorActionFailure`                   | Sum             | `ActionType`, `RuleName` |
| `ErrorActionHttpDestinationNotEnabled` | `ErrorActionHttpDestinationNotEnabled` | Sum             | `ActionType`, `RuleName` |
| `ErrorActionSuccess`                   | `ErrorActionSuccess`                   | Sum             | `ActionType`, `RuleName` |
| `Failure`                              | `Failure`                              | Sum             | `ActionType`, `RuleName` |
| `HttpCode_4XX`                         | `HttpCode_4XX`                         | Sum             | `ActionType`, `RuleName` |
| `HttpCode_5XX`                         | `HttpCode_5XX`                         | Sum             | `ActionType`, `RuleName` |
| `HttpCode_Other`                       | `HttpCode_Other`                       | Sum             | `ActionType`, `RuleName` |
| `HttpInvalidUrl`                       | `HttpInvalidUrl`                       | Sum             | `ActionType`, `RuleName` |
| `HttpRequestTimeout`                   | `HttpRequestTimeout`                   | Sum             | `ActionType`, `RuleName` |
| `HttpUnknownHost`                      | `HttpUnknownHost`                      | Sum             | `ActionType`, `RuleName` |
| `ParseError`                           | `ParseError`                           | Sum             | `RuleName`               |
| `RequestTimeout`                       | `RequestTimeout`                       | Sum             | `ActionType`, `RuleName` |
| `RuleMessageThrottled`                 | `RuleMessageThrottled`                 | Sum             | `RuleName`               |
| `RuleNotFound`                         | `RuleNotFound`                         | Sum             | `RuleName`               |
| `RulesExecuted`                        | `RulesExecuted`                        | Sum             | `RuleName`               |
| `SaslAuthFailed`                       | `SaslAuthFailed`                       | Sum             | `ActionType`, `RuleName` |
| `Success`                              | `Success`                              | Sum             | `ActionType`, `RuleName` |
| `TopicMatch`                           | `TopicMatch`                           | Sum             | `RuleName`               |

### `job`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                             | OpenTelemetry metric               | Instrument type | Data point attributes |
| ---------------------------------- | ---------------------------------- | --------------- | --------------------- |
| `CanceledJobExecutionCount`        | `CanceledJobExecutionCount`        | Sum             | `JobId`               |
| `CanceledJobExecutionTotalCount`   | `CanceledJobExecutionTotalCount`   | Histogram       | `JobId`               |
| `ClientErrorCount`                 | `ClientErrorCount`                 | Sum             | `JobId`               |
| `FailedJobExecutionCount`          | `FailedJobExecutionCount`          | Sum             | `JobId`               |
| `FailedJobExecutionTotalCount`     | `FailedJobExecutionTotalCount`     | Histogram       | `JobId`               |
| `InProgressJobExecutionCount`      | `InProgressJobExecutionCount`      | Sum             | `JobId`               |
| `InProgressJobExecutionTotalCount` | `InProgressJobExecutionTotalCount` | Histogram       | `JobId`               |
| `QueuedJobExecutionCount`          | `QueuedJobExecutionCount`          | Sum             | `JobId`               |
| `QueuedJobExecutionTotalCount`     | `QueuedJobExecutionTotalCount`     | Histogram       | `JobId`               |
| `RejectedJobExecutionCount`        | `RejectedJobExecutionCount`        | Sum             | `JobId`               |
| `RejectedJobExecutionTotalCount`   | `RejectedJobExecutionTotalCount`   | Histogram       | `JobId`               |
| `RemovedJobExecutionCount`         | `RemovedJobExecutionCount`         | Sum             | `JobId`               |
| `RemovedJobExecutionTotalCount`    | `RemovedJobExecutionTotalCount`    | Histogram       | `JobId`               |
| `ServerErrorCount`                 | `ServerErrorCount`                 | Sum             | `JobId`               |
| `SuccededJobExecutionCount`        | `SuccededJobExecutionCount`        | Sum             | `JobId`               |
| `SuccededJobExecutionTotalCount`   | `SuccededJobExecutionTotalCount`   | Histogram       | `JobId`               |
| `SucceededJobExecutionCount`       | `SucceededJobExecutionCount`       | Sum             | `JobId`               |
| `SucceededJobExecutionTotalCount`  | `SucceededJobExecutionTotalCount`  | Histogram       | `JobId`               |
| `TimedOutJobExecutionTotalCount`   | `TimedOutJobExecutionTotalCount`   | Histogram       | `JobId`               |

## AWS/KMS

The `AWS/KMS` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/kms`. All enriched instruments use Delta temporality.

- [AWS::KMS::Key](#otel-enrichment-aws-kms-aws-kms-key "#otel-enrichment-aws-kms-aws-kms-key")

### AWS::KMS::Key

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                              | OpenTelemetry metric                | Instrument type | Data point attributes |
| ----------------------------------- | ----------------------------------- | --------------- | --------------------- |
| `SecondsUntilKeyMaterialExpiration` | `SecondsUntilKeyMaterialExpiration` | Histogram       | `KeyId`               |

## AWS/Kafka

The `AWS/Kafka` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/kafka`. All enriched instruments use Delta temporality.

- [broker](#otel-enrichment-aws-kafka-broker "#otel-enrichment-aws-kafka-broker")
- [broker-client-auth](#otel-enrichment-aws-kafka-broker-client-auth "#otel-enrichment-aws-kafka-broker-client-auth")
- [cluster](#otel-enrichment-aws-kafka-cluster "#otel-enrichment-aws-kafka-cluster")
- [consumer-group](#otel-enrichment-aws-kafka-consumer-group "#otel-enrichment-aws-kafka-consumer-group")
- [consumer-group-partition](#otel-enrichment-aws-kafka-consumer-group-partition "#otel-enrichment-aws-kafka-consumer-group-partition")
- [replicator](#otel-enrichment-aws-kafka-replicator "#otel-enrichment-aws-kafka-replicator")
- [replicator-topic](#otel-enrichment-aws-kafka-replicator-topic "#otel-enrichment-aws-kafka-replicator-topic")
- [topic](#otel-enrichment-aws-kafka-topic "#otel-enrichment-aws-kafka-topic")

### `broker`

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric                                 | OpenTelemetry metric                   | Instrument type | Data point attributes       |
| -------------------------------------- | -------------------------------------- | --------------- | --------------------------- |
| `BurstBalance`                         | `BurstBalance`                         | Histogram       | `Broker ID`, `Cluster Name` |
| `BwInAllowanceExceeded`                | `BwInAllowanceExceeded`                | Sum             | `Broker ID`, `Cluster Name` |
| `BwOutAllowanceExceeded`               | `BwOutAllowanceExceeded`               | Sum             | `Broker ID`, `Cluster Name` |
| `CPUCreditBalance`                     | `CPUCreditBalance`                     | Histogram       | `Broker ID`, `Cluster Name` |
| `CPUCreditUsage`                       | `CPUCreditUsage`                       | Sum             | `Broker ID`, `Cluster Name` |
| `ConnectionCloseRate`                  | `ConnectionCloseRate`                  | Histogram       | `Broker ID`, `Cluster Name` |
| `ConnectionCount`                      | `ConnectionCount`                      | Histogram       | `Broker ID`, `Cluster Name` |
| `ConnectionCreationRate`               | `ConnectionCreationRate`               | Histogram       | `Broker ID`, `Cluster Name` |
| `ConntrackAllowanceExceeded`           | `ConntrackAllowanceExceeded`           | Sum             | `Broker ID`, `Cluster Name` |
| `CpuIdle`                              | `CpuIdle`                              | Histogram       | `Broker ID`, `Cluster Name` |
| `CpuIoWait`                            | `CpuIoWait`                            | Histogram       | `Broker ID`, `Cluster Name` |
| `CpuSystem`                            | `CpuSystem`                            | Histogram       | `Broker ID`, `Cluster Name` |
| `CpuUser`                              | `CpuUser`                              | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchConsumerLocalTimeMsMean`         | `FetchConsumerLocalTimeMsMean`         | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchConsumerRequestQueueTimeMsMean`  | `FetchConsumerRequestQueueTimeMsMean`  | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchConsumerResponseQueueTimeMsMean` | `FetchConsumerResponseQueueTimeMsMean` | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchConsumerResponseSendTimeMsMean`  | `FetchConsumerResponseSendTimeMsMean`  | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchConsumerTotalTimeMsMean`         | `FetchConsumerTotalTimeMsMean`         | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchFollowerLocalTimeMsMean`         | `FetchFollowerLocalTimeMsMean`         | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchFollowerRequestQueueTimeMsMean`  | `FetchFollowerRequestQueueTimeMsMean`  | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchFollowerResponseQueueTimeMsMean` | `FetchFollowerResponseQueueTimeMsMean` | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchFollowerResponseSendTimeMsMean`  | `FetchFollowerResponseSendTimeMsMean`  | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchFollowerTotalTimeMsMean`         | `FetchFollowerTotalTimeMsMean`         | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchMessageConversionsPerSec`        | `FetchMessageConversionsPerSec`        | Sum             | `Broker ID`, `Cluster Name` |
| `FetchThrottleByteRate`                | `FetchThrottleByteRate`                | Sum             | `Broker ID`, `Cluster Name` |
| `FetchThrottleQueueSize`               | `FetchThrottleQueueSize`               | Histogram       | `Broker ID`, `Cluster Name` |
| `FetchThrottleTime`                    | `FetchThrottleTime`                    | Histogram       | `Broker ID`, `Cluster Name` |
| `HeapMemoryAfterGC`                    | `HeapMemoryAfterGC`                    | Histogram       | `Broker ID`, `Cluster Name` |
| `IAMNumberOfConnectionRequests`        | `IAMNumberOfConnectionRequests`        | Sum             | `Broker ID`, `Cluster Name` |
| `IAMTooManyConnections`                | `IAMTooManyConnections`                | Sum             | `Broker ID`, `Cluster Name` |
| `KafkaAppLogsDiskUsed`                 | `KafkaAppLogsDiskUsed`                 | Histogram       | `Broker ID`, `Cluster Name` |
| `KafkaDataLogsDiskUsed`                | `KafkaDataLogsDiskUsed`                | Histogram       | `Broker ID`, `Cluster Name` |
| `LeaderCount`                          | `LeaderCount`                          | Histogram       | `Broker ID`, `Cluster Name` |
| `LinklocalAllowanceExceeded`           | `LinklocalAllowanceExceeded`           | Sum             | `Broker ID`, `Cluster Name` |
| `MemoryBuffered`                       | `MemoryBuffered`                       | Histogram       | `Broker ID`, `Cluster Name` |
| `MemoryCached`                         | `MemoryCached`                         | Histogram       | `Broker ID`, `Cluster Name` |
| `MemoryFree`                           | `MemoryFree`                           | Histogram       | `Broker ID`, `Cluster Name` |
| `MemoryUsed`                           | `MemoryUsed`                           | Histogram       | `Broker ID`, `Cluster Name` |
| `MessagesInPerSec`                     | `MessagesInPerSec`                     | Sum             | `Broker ID`, `Cluster Name` |
| `NetworkProcessorAvgIdlePercent`       | `NetworkProcessorAvgIdlePercent`       | Histogram       | `Broker ID`, `Cluster Name` |
| `NetworkRxDropped`                     | `NetworkRxDropped`                     | Sum             | `Broker ID`, `Cluster Name` |
| `NetworkRxErrors`                      | `NetworkRxErrors`                      | Sum             | `Broker ID`, `Cluster Name` |
| `NetworkRxPackets`                     | `NetworkRxPackets`                     | Sum             | `Broker ID`, `Cluster Name` |
| `NetworkTxDropped`                     | `NetworkTxDropped`                     | Sum             | `Broker ID`, `Cluster Name` |
| `NetworkTxErrors`                      | `NetworkTxErrors`                      | Sum             | `Broker ID`, `Cluster Name` |
| `NetworkTxPackets`                     | `NetworkTxPackets`                     | Sum             | `Broker ID`, `Cluster Name` |
| `PartitionCount`                       | `PartitionCount`                       | Histogram       | `Broker ID`, `Cluster Name` |
| `PpsAllowanceExceeded`                 | `PpsAllowanceExceeded`                 | Sum             | `Broker ID`, `Cluster Name` |
| `ProduceLocalTimeMsMean`               | `ProduceLocalTimeMsMean`               | Histogram       | `Broker ID`, `Cluster Name` |
| `ProduceMessageConversionsPerSec`      | `ProduceMessageConversionsPerSec`      | Sum             | `Broker ID`, `Cluster Name` |
| `ProduceMessageConversionsTimeMsMean`  | `ProduceMessageConversionsTimeMsMean`  | Histogram       | `Broker ID`, `Cluster Name` |
| `ProduceRequestQueueTimeMsMean`        | `ProduceRequestQueueTimeMsMean`        | Histogram       | `Broker ID`, `Cluster Name` |
| `ProduceResponseQueueTimeMsMean`       | `ProduceResponseQueueTimeMsMean`       | Histogram       | `Broker ID`, `Cluster Name` |
| `ProduceResponseSendTimeMsMean`        | `ProduceResponseSendTimeMsMean`        | Histogram       | `Broker ID`, `Cluster Name` |
| `ProduceThrottleByteRate`              | `ProduceThrottleByteRate`              | Sum             | `Broker ID`, `Cluster Name` |
| `ProduceThrottleQueueSize`             | `ProduceThrottleQueueSize`             | Histogram       | `Broker ID`, `Cluster Name` |
| `ProduceThrottleTime`                  | `ProduceThrottleTime`                  | Histogram       | `Broker ID`, `Cluster Name` |
| `ProduceTotalTimeMsMean`               | `ProduceTotalTimeMsMean`               | Histogram       | `Broker ID`, `Cluster Name` |
| `RemoteCopyBytesPerSec`                | `RemoteCopyBytesPerSec`                | Sum             | `Broker ID`, `Cluster Name` |
| `RemoteCopyErrorsPerSec`               | `RemoteCopyErrorsPerSec`               | Sum             | `Broker ID`, `Cluster Name` |
| `RemoteCopyLagBytes`                   | `RemoteCopyLagBytes`                   | Histogram       | `Broker ID`, `Cluster Name` |
| `RemoteFetchBytesPerSec`               | `RemoteFetchBytesPerSec`               | Sum             | `Broker ID`, `Cluster Name` |
| `RemoteFetchErrorsPerSec`              | `RemoteFetchErrorsPerSec`              | Sum             | `Broker ID`, `Cluster Name` |
| `RemoteFetchRequestsPerSec`            | `RemoteFetchRequestsPerSec`            | Sum             | `Broker ID`, `Cluster Name` |
| `RemoteLogManagerTasksAvgIdlePercent`  | `RemoteLogManagerTasksAvgIdlePercent`  | Histogram       | `Broker ID`, `Cluster Name` |
| `RemoteLogReaderAvgIdlePercent`        | `RemoteLogReaderAvgIdlePercent`        | Histogram       | `Broker ID`, `Cluster Name` |
| `RemoteLogReaderTaskQueueSize`         | `RemoteLogReaderTaskQueueSize`         | Histogram       | `Broker ID`, `Cluster Name` |
| `RemoteLogSizeBytes`                   | `RemoteLogSizeBytes`                   | Histogram       | `Broker ID`, `Cluster Name` |
| `ReplicationBytesInPerSec`             | `ReplicationBytesInPerSec`             | Sum             | `Broker ID`, `Cluster Name` |
| `ReplicationBytesOutPerSec`            | `ReplicationBytesOutPerSec`            | Sum             | `Broker ID`, `Cluster Name` |
| `RequestBytesMean`                     | `RequestBytesMean`                     | Histogram       | `Broker ID`, `Cluster Name` |
| `RequestExemptFromThrottleTime`        | `RequestExemptFromThrottleTime`        | Histogram       | `Broker ID`, `Cluster Name` |
| `RequestHandlerAvgIdlePercent`         | `RequestHandlerAvgIdlePercent`         | Histogram       | `Broker ID`, `Cluster Name` |
| `RequestThrottleQueueSize`             | `RequestThrottleQueueSize`             | Histogram       | `Broker ID`, `Cluster Name` |
| `RequestThrottleTime`                  | `RequestThrottleTime`                  | Histogram       | `Broker ID`, `Cluster Name` |
| `RequestTime`                          | `RequestTime`                          | Histogram       | `Broker ID`, `Cluster Name` |
| `RootDiskUsed`                         | `RootDiskUsed`                         | Histogram       | `Broker ID`, `Cluster Name` |
| `SwapFree`                             | `SwapFree`                             | Histogram       | `Broker ID`, `Cluster Name` |
| `SwapUsed`                             | `SwapUsed`                             | Histogram       | `Broker ID`, `Cluster Name` |
| `TCPConnections`                       | `TCPConnections`                       | Sum             | `Broker ID`, `Cluster Name` |
| `TrafficBytes`                         | `TrafficBytes`                         | Sum             | `Broker ID`, `Cluster Name` |
| `TrafficShaping`                       | `TrafficShaping`                       | Sum             | `Broker ID`, `Cluster Name` |
| `UnderMinIsrPartitionCount`            | `UnderMinIsrPartitionCount`            | Histogram       | `Broker ID`, `Cluster Name` |
| `UnderReplicatedPartitions`            | `UnderReplicatedPartitions`            | Histogram       | `Broker ID`, `Cluster Name` |
| `UserPartitionExists`                  | `UserPartitionExists`                  | Histogram       | `Broker ID`, `Cluster Name` |
| `VolumeQueueLength`                    | `VolumeQueueLength`                    | Histogram       | `Broker ID`, `Cluster Name` |
| `VolumeReadBytes`                      | `VolumeReadBytes`                      | Sum             | `Broker ID`, `Cluster Name` |
| `VolumeReadOps`                        | `VolumeReadOps`                        | Sum             | `Broker ID`, `Cluster Name` |
| `VolumeTotalReadTime`                  | `VolumeTotalReadTime`                  | Sum             | `Broker ID`, `Cluster Name` |
| `VolumeTotalWriteTime`                 | `VolumeTotalWriteTime`                 | Sum             | `Broker ID`, `Cluster Name` |
| `VolumeWriteBytes`                     | `VolumeWriteBytes`                     | Sum             | `Broker ID`, `Cluster Name` |
| `VolumeWriteOps`                       | `VolumeWriteOps`                       | Sum             | `Broker ID`, `Cluster Name` |
| `ZooKeeperRequestLatencyMsMean`        | `ZooKeeperRequestLatencyMsMean`        | Histogram       | `Broker ID`, `Cluster Name` |
| `ZooKeeperSessionState`                | `ZooKeeperSessionState`                | Histogram       | `Broker ID`, `Cluster Name` |

### `broker-client-auth`

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric                  | OpenTelemetry metric    | Instrument type | Data point attributes                                |
| ----------------------- | ----------------------- | --------------- | ---------------------------------------------------- |
| `ClientConnectionCount` | `ClientConnectionCount` | Histogram       | `Broker ID`, `Client Authentication`, `Cluster Name` |

### `cluster`

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric                   | OpenTelemetry metric     | Instrument type | Data point attributes |
| ------------------------ | ------------------------ | --------------- | --------------------- |
| `ActiveControllerCount`  | `ActiveControllerCount`  | Histogram       | `Cluster Name`        |
| `GlobalPartitionCount`   | `GlobalPartitionCount`   | Histogram       | `Cluster Name`        |
| `GlobalTopicCount`       | `GlobalTopicCount`       | Histogram       | `Cluster Name`        |
| `OfflinePartitionsCount` | `OfflinePartitionsCount` | Histogram       | `Cluster Name`        |

### `consumer-group`

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric                       | OpenTelemetry metric         | Instrument type | Data point attributes                     |
| ---------------------------- | ---------------------------- | --------------- | ----------------------------------------- |
| `EstimatedMaxTimeLag`        | `EstimatedMaxTimeLag`        | Histogram       | `Cluster Name`, `Consumer Group`, `Topic` |
| `MaxOffsetLag`               | `MaxOffsetLag`               | Histogram       | `Cluster Name`, `Consumer Group`, `Topic` |
| `RollingEstimatedTimeLagMax` | `RollingEstimatedTimeLagMax` | Histogram       | `Cluster Name`, `Consumer Group`, `Topic` |
| `SumOffsetLag`               | `SumOffsetLag`               | Histogram       | `Cluster Name`, `Consumer Group`, `Topic` |

### `consumer-group-partition`

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric                    | OpenTelemetry metric      | Instrument type | Data point attributes                  |
| ------------------------- | ------------------------- | --------------- | -------------------------------------- |
| `EstimatedTimeLag`        | `EstimatedTimeLag`        | Histogram       | `Consumer Group`, `Partition`, `Topic` |
| `OffsetLag`               | `OffsetLag`               | Histogram       | `Consumer Group`, `Partition`, `Topic` |
| `RollingEstimatedTimeLag` | `RollingEstimatedTimeLag` | Histogram       | `Consumer Group`, `Partition`, `Topic` |

### `replicator`

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric                           | OpenTelemetry metric             | Instrument type | Data point attributes |
| -------------------------------- | -------------------------------- | --------------- | --------------------- |
| `ConsumerGroupCount`             | `ConsumerGroupCount`             | Histogram       | `ReplicatorName`      |
| `ConsumerGroupOffsetSyncFailure` | `ConsumerGroupOffsetSyncFailure` | Sum             | `ReplicatorName`      |
| `MessageLag`                     | `MessageLag`                     | Histogram       | `ReplicatorName`      |
| `ReplicationLatency`             | `ReplicationLatency`             | Histogram       | `ReplicatorName`      |
| `ReplicatorBytesInPerSec`        | `ReplicatorBytesInPerSec`        | Sum             | `ReplicatorName`      |
| `ReplicatorBytesOutPerSec`       | `ReplicatorBytesOutPerSec`       | Sum             | `ReplicatorName`      |
| `ReplicatorFailure`              | `ReplicatorFailure`              | Sum             | `ReplicatorName`      |
| `ReplicatorThroughput`           | `ReplicatorThroughput`           | Sum             | `ReplicatorName`      |
| `TopicCount`                     | `TopicCount`                     | Histogram       | `ReplicatorName`      |

### `replicator-topic`

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric                 | OpenTelemetry metric           | Instrument type | Data point attributes     |
| ---------------------- | ------------------------------ | --------------- | ------------------------- |
| `MessageLag`           | `MessageLagPerTopic`           | Histogram       | `ReplicatorName`, `Topic` |
| `ReplicationLatency`   | `ReplicationLatencyPerTopic`   | Histogram       | `ReplicatorName`, `Topic` |
| `ReplicatorThroughput` | `ReplicatorThroughputPerTopic` | Sum             | `ReplicatorName`, `Topic` |

### `topic`

- `cloud.resource_id` enrichment: Not supported
- `tag.*` enrichment: Not supported

| Metric                            | OpenTelemetry metric                      | Instrument type | Data point attributes                |
| --------------------------------- | ----------------------------------------- | --------------- | ------------------------------------ |
| `BytesInPerSec`                   | `BytesInPerSec`                           | Sum             | `Broker ID`, `Cluster Name`, `Topic` |
| `BytesOutPerSec`                  | `BytesOutPerSec`                          | Sum             | `Broker ID`, `Cluster Name`, `Topic` |
| `FetchMessageConversionsPerSec`   | `FetchMessageConversionsPerSecPerTopic`   | Sum             | `Broker ID`, `Cluster Name`, `Topic` |
| `MessagesInPerSec`                | `MessagesInPerSecPerTopic`                | Sum             | `Broker ID`, `Cluster Name`, `Topic` |
| `ProduceMessageConversionsPerSec` | `ProduceMessageConversionsPerSecPerTopic` | Sum             | `Broker ID`, `Cluster Name`, `Topic` |
| `RemoteCopyBytesPerSec`           | `RemoteCopyBytesPerSecPerTopic`           | Sum             | `Broker ID`, `Cluster Name`, `Topic` |
| `RemoteCopyErrorsPerSec`          | `RemoteCopyErrorsPerSecPerTopic`          | Sum             | `Broker ID`, `Cluster Name`, `Topic` |
| `RemoteFetchBytesPerSec`          | `RemoteFetchBytesPerSecPerTopic`          | Sum             | `Broker ID`, `Cluster Name`, `Topic` |
| `RemoteFetchErrorsPerSec`         | `RemoteFetchErrorsPerSecPerTopic`         | Sum             | `Broker ID`, `Cluster Name`, `Topic` |
| `RemoteFetchRequestsPerSec`       | `RemoteFetchRequestsPerSecPerTopic`       | Sum             | `Broker ID`, `Cluster Name`, `Topic` |
| `RemoteLogSizeBytes`              | `RemoteLogSizeBytesPerTopic`              | Histogram       | `Broker ID`, `Cluster Name`, `Topic` |

## AWS/Kendra

The `AWS/Kendra` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/kendra`. All enriched instruments use Delta temporality.

- [AWS::Kendra::DataSource](#otel-enrichment-aws-kendra-aws-kendra-datasource "#otel-enrichment-aws-kendra-aws-kendra-datasource")
- [AWS::Kendra::Index](#otel-enrichment-aws-kendra-aws-kendra-index "#otel-enrichment-aws-kendra-aws-kendra-index")

### AWS::Kendra::DataSource

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                | OpenTelemetry metric                  | Instrument type | Data point attributes                                       |
| ------------------------------------- | ------------------------------------- | --------------- | ----------------------------------------------------------- |
| `DataSourceDocumentCount`             | `DataSourceDocumentCount`             | Histogram       | `DataSourceId`, `IndexId`                                   |
| `DataSourceSyncRuntime`               | `DataSourceSyncRuntime`               | Histogram       | `DataSourceId`, `IndexId`                                   |
| `DocumentsCrawled`                    | `DocumentsCrawled`                    | Sum             | `DataSourceId`, `IndexId`                                   |
| `DocumentsFailedToIndex`              | `DocumentsFailedToIndex`              | Sum             | `DataSourceId`, `IndexId`                                   |
| `DocumentsIndexed`                    | `DocumentsIndexed`                    | Sum             | `DataSourceId`, `IndexId`                                   |
| `DocumentsSkippedInvalidMetadata`     | `DocumentsSkippedInvalidMetadata`     | Sum             | `DataSourceId`, `IndexId`                                   |
| `DocumentsSkippedNoChange`            | `DocumentsSkippedNoChange`            | Sum             | `DataSourceId`, `IndexId`                                   |
| `DocumentsSubmittedForDeletion`       | `DocumentsSubmittedForDeletion`       | Sum             | `DataSourceId`, `IndexId`                                   |
| `DocumentsSubmittedForDeletionFailed` | `DocumentsSubmittedForDeletionFailed` | Sum             | `DataSourceId`, `IndexId`                                   |
| `DocumentsSubmittedForIndexing`       | `DocumentsSubmittedForIndexing`       | Sum             | `DataSourceId`, `IndexId`                                   |
| `DocumentsSubmittedForIndexingFailed` | `DocumentsSubmittedForIndexingFailed` | Sum             | `DataSourceId`, `IndexId`                                   |
| `DocumentsWithoutAcl`                 | `DocumentsWithoutAcl`                 | Sum             | `AwsAccountId`, `DataSourceId`, `DataSourceType`, `IndexId` |
| `MetadataFilesCrawled`                | `MetadataFilesCrawled`                | Sum             | `DataSourceId`, `IndexId`                                   |
| `PrincipalGroupsScanned`              | `PrincipalGroupsScanned`              | Sum             | `DataSourceId`, `IndexId`                                   |

### AWS::Kendra::Index

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                             | OpenTelemetry metric               | Instrument type | Data point attributes |
| ---------------------------------- | ---------------------------------- | --------------- | --------------------- |
| `ClickFeedbackSubmittedCount`      | `ClickFeedbackSubmittedCount`      | Sum             | `IndexId`             |
| `GroupProcessed`                   | `GroupProcessed`                   | Sum             | `IndexId`             |
| `GroupProcessedButNotPersistent`   | `GroupProcessedButNotPersistent`   | Sum             | `IndexId`             |
| `GroupReceived`                    | `GroupReceived`                    | Sum             | `IndexId`             |
| `GroupUpdateLatencyInMilliSeconds` | `GroupUpdateLatencyInMilliSeconds` | Histogram       | `IndexId`             |
| `GroupWithOlderOrderingIdSkipped`  | `GroupWithOlderOrderingIdSkipped`  | Sum             | `IndexId`             |
| `IndexDocumentCount`               | `IndexDocumentCount`               | Histogram       | `IndexId`             |
| `IndexDocumentStorageSize`         | `IndexDocumentStorageSize`         | Histogram       | `IndexId`             |
| `IndexQueryCount`                  | `IndexQueryCount`                  | Sum             | `IndexId`             |
| `ProvisionedIndexDocumentCount`    | `ProvisionedIndexDocumentCount`    | Histogram       | `IndexId`             |
| `ProvisionedIndexStorageSize`      | `ProvisionedIndexStorageSize`      | Histogram       | `IndexId`             |
| `RelevantFeedbackSubmittedCount`   | `RelevantFeedbackSubmittedCount`   | Sum             | `IndexId`             |

## AWS/Kinesis

The `AWS/Kinesis` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/kinesis`. All enriched instruments use Delta temporality.

- [AWS::Kinesis::Stream](#otel-enrichment-aws-kinesis-aws-kinesis-stream "#otel-enrichment-aws-kinesis-aws-kinesis-stream")

### AWS::Kinesis::Stream

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                     | OpenTelemetry metric                       | Instrument type | Data point attributes        |
| ------------------------------------------ | ------------------------------------------ | --------------- | ---------------------------- |
| `GetRecords.Bytes`                         | `GetRecords.Bytes`                         | Sum             | `StreamName`                 |
| `GetRecords.IteratorAgeMilliseconds`       | `GetRecords.IteratorAgeMilliseconds`       | Histogram       | `StreamName`                 |
| `GetRecords.Latency`                       | `GetRecords.Latency`                       | Histogram       | `StreamName`                 |
| `GetRecords.Records`                       | `GetRecords.Records`                       | Sum             | `StreamName`                 |
| `GetRecords.Success`                       | `GetRecords.Success`                       | Sum             | `StreamName`                 |
| `IncomingBytes`                            | `IncomingBytes`                            | Sum             | `StreamName`                 |
| `IncomingRecords`                          | `IncomingRecords`                          | Sum             | `StreamName`                 |
| `IteratorAgeMilliseconds`                  | `IteratorAgeMilliseconds`                  | Histogram       | `ShardId`, `StreamName`      |
| `OutgoingBytes`                            | `OutgoingBytes`                            | Sum             | `ShardId`, `StreamName`      |
| `OutgoingRecords`                          | `OutgoingRecords`                          | Sum             | `ShardId`, `StreamName`      |
| `PutRecord.Success`                        | `PutRecord.Success`                        | Sum             | `StreamName`                 |
| `PutRecords.Bytes`                         | `PutRecords.Bytes`                         | Sum             | `StreamName`                 |
| `PutRecords.Success`                       | `PutRecords.Success`                       | Sum             | `StreamName`                 |
| `ReadProvisionedThroughputExceeded`        | `ReadProvisionedThroughputExceeded`        | Sum             | `StreamName`                 |
| `SubscribeToShard.RateExceeded`            | `SubscribeToShard.RateExceeded`            | Sum             | `ConsumerName`, `StreamName` |
| `SubscribeToShard.Success`                 | `SubscribeToShard.Success`                 | Sum             | `ConsumerName`, `StreamName` |
| `SubscribeToShardEvent.Bytes`              | `SubscribeToShardEvent.Bytes`              | Sum             | `ConsumerName`, `StreamName` |
| `SubscribeToShardEvent.MillisBehindLatest` | `SubscribeToShardEvent.MillisBehindLatest` | Histogram       | `ConsumerName`, `StreamName` |
| `SubscribeToShardEvent.Records`            | `SubscribeToShardEvent.Records`            | Sum             | `ConsumerName`, `StreamName` |
| `SubscribeToShardEvent.Success`            | `SubscribeToShardEvent.Success`            | Sum             | `ConsumerName`, `StreamName` |
| `WriteProvisionedThroughputExceeded`       | `WriteProvisionedThroughputExceeded`       | Sum             | `StreamName`                 |

## AWS/KinesisAnalytics

The `AWS/KinesisAnalytics` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/kinesisanalytics`. All enriched instruments use Delta temporality.

- [AWS::KinesisAnalyticsV2::Application](#otel-enrichment-aws-kinesisanalytics-aws-kinesisanalyticsv2-application "#otel-enrichment-aws-kinesisanalytics-aws-kinesisanalyticsv2-application")

### AWS::KinesisAnalyticsV2::Application

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                 | OpenTelemetry metric                   | Instrument type | Data point attributes          |
| -------------------------------------- | -------------------------------------- | --------------- | ------------------------------ |
| `KPUs`                                 | `KPUs`                                 | Histogram       | `Application`                  |
| `KPUs-Interactive`                     | `KPUs-Interactive`                     | Histogram       | `Application`                  |
| `backPressuredTimeMsPerSecond`         | `backPressuredTimeMsPerSecond`         | Histogram       | `Application`                  |
| `busyTimeMsPerSecond`                  | `busyTimeMsPerSecond`                  | Histogram       | `Application`                  |
| `bytesRequestedPerFetch`               | `bytesRequestedPerFetch`               | Histogram       | `Application`, `Flow`, `Id`    |
| `committedOffsets`                     | `committedOffsets`                     | Histogram       | `Application`, `Flow`, `Topic` |
| `containerCPUUtilization`              | `containerCPUUtilization`              | Histogram       | `Application`                  |
| `containerDiskUtilization`             | `containerDiskUtilization`             | Histogram       | `Application`                  |
| `containerMemoryUtilization`           | `containerMemoryUtilization`           | Histogram       | `Application`                  |
| `cpuUtilization`                       | `cpuUtilization`                       | Histogram       | `Application`                  |
| `currentInputWatermark`                | `currentInputWatermark`                | Histogram       | `Application`                  |
| `currentOffsets`                       | `currentOffsets`                       | Histogram       | `Application`, `Flow`, `Topic` |
| `currentOutputWatermark`               | `currentOutputWatermark`               | Histogram       | `Application`                  |
| `downtime`                             | `downtime`                             | Histogram       | `Application`                  |
| `fullRestarts`                         | `fullRestarts`                         | Sum             | `Application`                  |
| `heapMemoryUtilization`                | `heapMemoryUtilization`                | Histogram       | `Application`                  |
| `idleTimeMsPerSecond`                  | `idleTimeMsPerSecond`                  | Histogram       | `Application`                  |
| `jobmanagerFileDescriptorsMax`         | `jobmanagerFileDescriptorsMax`         | Histogram       | `Application`                  |
| `jobmanagerFileDescriptorsOpen`        | `jobmanagerFileDescriptorsOpen`        | Histogram       | `Application`                  |
| `jobmanagerHeapMemoryUtilization`      | `jobmanagerHeapMemoryUtilization`      | Histogram       | `Application`                  |
| `jobmanagerMetaspaceMemoryUtilization` | `jobmanagerMetaspaceMemoryUtilization` | Histogram       | `Application`                  |
| `lastCheckpointDuration`               | `lastCheckpointDuration`               | Histogram       | `Application`                  |
| `lastCheckpointSize`                   | `lastCheckpointSize`                   | Histogram       | `Application`                  |
| `managedMemoryTotal`                   | `managedMemoryTotal`                   | Histogram       | `Application`                  |
| `managedMemoryUsed`                    | `managedMemoryUsed`                    | Histogram       | `Application`                  |
| `managedMemoryUtilization`             | `managedMemoryUtilization`             | Histogram       | `Application`                  |
| `metaspaceMemoryUtilization`           | `metaspaceMemoryUtilization`           | Histogram       | `Application`                  |
| `millisBehindLatest`                   | `millisBehindLatest`                   | Histogram       | `Application`, `Flow`, `Id`    |
| `numLateRecordsDropped`                | `numLateRecordsDropped`                | Sum             | `Application`                  |
| `numRecordsIn`                         | `numRecordsIn`                         | Sum             | `Application`                  |
| `numRecordsInPerSecond`                | `numRecordsInPerSecond`                | Histogram       | `Application`                  |
| `numRecordsOut`                        | `numRecordsOut`                        | Sum             | `Application`                  |
| `numRecordsOutPerSecond`               | `numRecordsOutPerSecond`               | Histogram       | `Application`                  |
| `numRestarts`                          | `numRestarts`                          | Sum             | `Application`                  |
| `numberOfFailedCheckpoints`            | `numberOfFailedCheckpoints`            | Sum             | `Application`                  |
| `oldGenerationGCCount`                 | `oldGenerationGCCount`                 | Sum             | `Application`                  |
| `oldGenerationGCTime`                  | `oldGenerationGCTime`                  | Sum             | `Application`                  |
| `taskmanagerFileDescriptorsMax`        | `taskmanagerFileDescriptorsMax`        | Histogram       | `Application`                  |
| `taskmanagerFileDescriptorsOpen`       | `taskmanagerFileDescriptorsOpen`       | Histogram       | `Application`                  |
| `threadCount`                          | `threadCount`                          | Histogram       | `Application`                  |
| `threadsCount`                         | `threadsCount`                         | Histogram       | `Application`                  |
| `uptime`                               | `uptime`                               | Histogram       | `Application`                  |
| `zeppelinCpuUtilization`               | `zeppelinCpuUtilization`               | Histogram       | `Application`                  |
| `zeppelinHeapMemoryUtilization`        | `zeppelinHeapMemoryUtilization`        | Histogram       | `Application`                  |
| `zeppelinServerUptime`                 | `zeppelinServerUptime`                 | Histogram       | `Application`                  |
| `zeppelinThreadCount`                  | `zeppelinThreadCount`                  | Histogram       | `Application`                  |
| `zeppelinWaitingJobs`                  | `zeppelinWaitingJobs`                  | Histogram       | `Application`                  |

## AWS/Lambda

The `AWS/Lambda` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/lambda`. All enriched instruments use Delta temporality.

- [AWS::Lambda::CapacityProvider](#otel-enrichment-aws-lambda-aws-lambda-capacityprovider "#otel-enrichment-aws-lambda-aws-lambda-capacityprovider")
- [AWS::Lambda::EventSourceMapping](#otel-enrichment-aws-lambda-aws-lambda-eventsourcemapping "#otel-enrichment-aws-lambda-aws-lambda-eventsourcemapping")
- [AWS::Lambda::Function](#otel-enrichment-aws-lambda-aws-lambda-function "#otel-enrichment-aws-lambda-aws-lambda-function")

### AWS::Lambda::CapacityProvider

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                                  | OpenTelemetry metric                    | Instrument type | Data point attributes                              |
| --------------------------------------- | --------------------------------------- | --------------- | -------------------------------------------------- |
| `ExecutionEnvironmentCPUUtilization`    | `ExecutionEnvironmentCPUUtilization`    | Histogram       | `CapacityProviderName`, `FunctionName`, `Resource` |
| `ExecutionEnvironmentConcurrency`       | `ExecutionEnvironmentConcurrency`       | Histogram       | `CapacityProviderName`, `FunctionName`, `Resource` |
| `ExecutionEnvironmentConcurrencyLimit`  | `ExecutionEnvironmentConcurrencyLimit`  | Histogram       | `CapacityProviderName`, `FunctionName`, `Resource` |
| `ExecutionEnvironmentMemoryUtilization` | `ExecutionEnvironmentMemoryUtilization` | Histogram       | `CapacityProviderName`, `FunctionName`, `Resource` |

### AWS::Lambda::EventSourceMapping

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                    | OpenTelemetry metric                      | Instrument type | Data point attributes    |
| ----------------------------------------- | ----------------------------------------- | --------------- | ------------------------ |
| `CommittedEventCount`                     | `CommittedEventCount`                     | Sum             | `EventSourceMappingUUID` |
| `DeletedEventCount`                       | `DeletedEventCount`                       | Sum             | `EventSourceMappingUUID` |
| `DroppedEventCount`                       | `DroppedEventCount`                       | Sum             | `EventSourceMappingUUID` |
| `EventPollerThroughputInBytes`            | `EventPollerThroughputInBytes`            | Sum             | `EventSourceMappingUUID` |
| `EventPollerUnit`                         | `EventPollerUnit`                         | Histogram       | `EventSourceMappingUUID` |
| `FailedInvokeEventCount`                  | `FailedInvokeEventCount`                  | Sum             | `EventSourceMappingUUID` |
| `FilteredOutEventCount`                   | `FilteredOutEventCount`                   | Sum             | `EventSourceMappingUUID` |
| `InvokedEventCount`                       | `InvokedEventCount`                       | Sum             | `EventSourceMappingUUID` |
| `IteratorAge`                             | `IteratorAge`                             | Histogram       | `EventSourceMappingUUID` |
| `MaxOffsetLag`                            | `MaxOffsetLag`                            | Histogram       | `EventSourceMappingUUID` |
| `OnFailureDestinationDeliveredEventCount` | `OnFailureDestinationDeliveredEventCount` | Sum             | `EventSourceMappingUUID` |
| `PolledEventCount`                        | `PolledEventCount`                        | Sum             | `EventSourceMappingUUID` |
| `ProvisionedPollers`                      | `ProvisionedPollers`                      | Histogram       | `EventSourceMappingUUID` |
| `SumOffsetLag`                            | `SumOffsetLag`                            | Histogram       | `EventSourceMappingUUID` |

### AWS::Lambda::Function

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                       | OpenTelemetry metric                         | Instrument type | Data point attributes      |
| -------------------------------------------- | -------------------------------------------- | --------------- | -------------------------- |
| `AsyncEventAge`                              | `AsyncEventAge`                              | Histogram       | `FunctionName`, `Resource` |
| `AsyncEventsDropped`                         | `AsyncEventsDropped`                         | Sum             | `FunctionName`, `Resource` |
| `AsyncEventsReceived`                        | `AsyncEventsReceived`                        | Sum             | `FunctionName`, `Resource` |
| `CPUThrottles`                               | `CPUThrottles`                               | Sum             | `FunctionName`, `Resource` |
| `ConcurrencyThrottles`                       | `ConcurrencyThrottles`                       | Sum             | `FunctionName`, `Resource` |
| `ConcurrentExecutions`                       | `ConcurrentExecutions`                       | Histogram       | `FunctionName`, `Resource` |
| `DeadLetterErrors`                           | `DeadLetterErrors`                           | Sum             | `FunctionName`, `Resource` |
| `DestinationDeliveryFailures`                | `DestinationDeliveryFailures`                | Sum             | `FunctionName`, `Resource` |
| `DiskThrottles`                              | `DiskThrottles`                              | Sum             | `FunctionName`, `Resource` |
| `DurableExecutionDuration`                   | `DurableExecutionDuration`                   | Histogram       | `FunctionName`, `Resource` |
| `DurableExecutionFailed`                     | `DurableExecutionFailed`                     | Sum             | `FunctionName`, `Resource` |
| `DurableExecutionOperations`                 | `DurableExecutionOperations`                 | Sum             | `FunctionName`, `Resource` |
| `DurableExecutionStarted`                    | `DurableExecutionStarted`                    | Sum             | `FunctionName`, `Resource` |
| `DurableExecutionStopped`                    | `DurableExecutionStopped`                    | Sum             | `FunctionName`, `Resource` |
| `DurableExecutionStorageWrittenBytes`        | `DurableExecutionStorageWrittenBytes`        | Sum             | `FunctionName`, `Resource` |
| `DurableExecutionSucceeded`                  | `DurableExecutionSucceeded`                  | Sum             | `FunctionName`, `Resource` |
| `DurableExecutionTimedOut`                   | `DurableExecutionTimedOut`                   | Sum             | `FunctionName`, `Resource` |
| `Duration`                                   | `Duration`                                   | Histogram       | `FunctionName`, `Resource` |
| `Errors`                                     | `Errors`                                     | Sum             | `FunctionName`, `Resource` |
| `Invocations`                                | `Invocations`                                | Sum             | `FunctionName`, `Resource` |
| `IteratorAge`                                | `IteratorAge`                                | Histogram       | `FunctionName`, `Resource` |
| `MemoryThrottles`                            | `MemoryThrottles`                            | Sum             | `FunctionName`, `Resource` |
| `OffsetLag`                                  | `OffsetLag`                                  | Histogram       | `FunctionName`, `Resource` |
| `PostRuntimeExtensionsDuration`              | `PostRuntimeExtensionsDuration`              | Histogram       | `FunctionName`, `Resource` |
| `ProvisionedConcurrencyInvocations`          | `ProvisionedConcurrencyInvocations`          | Sum             | `FunctionName`, `Resource` |
| `ProvisionedConcurrencySpilloverInvocations` | `ProvisionedConcurrencySpilloverInvocations` | Sum             | `FunctionName`, `Resource` |
| `ProvisionedConcurrencyUtilization`          | `ProvisionedConcurrencyUtilization`          | Histogram       | `FunctionName`, `Resource` |
| `ProvisionedConcurrentExecutions`            | `ProvisionedConcurrentExecutions`            | Histogram       | `FunctionName`, `Resource` |
| `RecursiveInvocationsDropped`                | `RecursiveInvocationsDropped`                | Sum             | `FunctionName`, `Resource` |
| `SignatureValidationErrors`                  | `SignatureValidationErrors`                  | Sum             | `FunctionName`, `Resource` |
| `StreamedOutboundBytes`                      | `StreamedOutboundBytes`                      | Sum             | `FunctionName`, `Resource` |
| `StreamedOutboundThroughput`                 | `StreamedOutboundThroughput`                 | Histogram       | `FunctionName`, `Resource` |
| `Throttles`                                  | `Throttles`                                  | Sum             | `FunctionName`, `Resource` |
| `TimeToFirstByteLatency`                     | `TimeToFirstByteLatency`                     | Histogram       | `FunctionName`, `Resource` |
| `TimeToLastByteLatency`                      | `TimeToLastByteLatency`                      | Histogram       | `FunctionName`, `Resource` |
| `Url4xxCount`                                | `Url4xxCount`                                | Sum             | `FunctionName`, `Resource` |
| `Url5xxCount`                                | `Url5xxCount`                                | Sum             | `FunctionName`, `Resource` |
| `UrlRequestCount`                            | `UrlRequestCount`                            | Sum             | `FunctionName`, `Resource` |
| `UrlRequestLatency`                          | `UrlRequestLatency`                          | Histogram       | `FunctionName`, `Resource` |

## AWS/M2

The `AWS/M2` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/m2`. All enriched instruments use Delta temporality.

- [AWS::M2::Application](#otel-enrichment-aws-m2-aws-m2-application "#otel-enrichment-aws-m2-aws-m2-application")

### AWS::M2::Application

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                      | OpenTelemetry metric        | Instrument type | Data point attributes |
| --------------------------- | --------------------------- | --------------- | --------------------- |
| `BatchJobCompletedCount`    | `BatchJobCompletedCount`    | Sum             | `ApplicationId`       |
| `BatchJobFailedCount`       | `BatchJobFailedCount`       | Sum             | `ApplicationId`       |
| `JvmMemoryFree`             | `JvmMemoryFree`             | Histogram       | `ApplicationId`       |
| `JvmMemoryMax`              | `JvmMemoryMax`              | Histogram       | `ApplicationId`       |
| `JvmMemoryUsed`             | `JvmMemoryUsed`             | Histogram       | `ApplicationId`       |
| `ProcessesActiveCount`      | `ProcessesActiveCount`      | Sum             | `ApplicationId`       |
| `SessionCount`              | `SessionCount`              | Histogram       | `ApplicationId`       |
| `SharedMemoryFree`          | `SharedMemoryFree`          | Histogram       | `ApplicationId`       |
| `SharedMemoryTotal`         | `SharedMemoryTotal`         | Histogram       | `ApplicationId`       |
| `ThreadActiveCount`         | `ThreadActiveCount`         | Histogram       | `ApplicationId`       |
| `TransactionCompletedCount` | `TransactionCompletedCount` | Sum             | `ApplicationId`       |
| `TransactionFailedCount`    | `TransactionFailedCount`    | Sum             | `ApplicationId`       |
| `TransactionResponseTime`   | `TransactionResponseTime`   | Histogram       | `ApplicationId`       |

## AWS/MWAA

The `AWS/MWAA` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/airflow`. All enriched instruments use Delta temporality.

- [environment](#otel-enrichment-aws-mwaa-environment "#otel-enrichment-aws-mwaa-environment")
- [rbac-role](#otel-enrichment-aws-mwaa-rbac-role "#otel-enrichment-aws-mwaa-rbac-role")

### `environment`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                       | OpenTelemetry metric         | Instrument type | Data point attributes    |
| ---------------------------- | ---------------------------- | --------------- | ------------------------ |
| `ActiveConnectionCount`      | `ActiveConnectionCount`      | Histogram       | `Environment`            |
| `ApproximateAgeOfOldestTask` | `ApproximateAgeOfOldestTask` | Histogram       | `Environment`            |
| `CPUUtilization`             | `CPUUtilization`             | Histogram       | `Cluster`, `Environment` |
| `MemoryUtilization`          | `MemoryUtilization`          | Histogram       | `Cluster`, `Environment` |
| `QueuedTasks`                | `QueuedTasks`                | Histogram       | `Environment`            |
| `RunningTasks`               | `RunningTasks`               | Histogram       | `Environment`            |

### `rbac-role`

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                      | OpenTelemetry metric        | Instrument type | Data point attributes         |
| --------------------------- | --------------------------- | --------------- | ----------------------------- |
| `DatabaseConnections`       | `DatabaseConnections`       | Histogram       | `DatabaseRole`, `Environment` |
| `DiskQueueDepth`            | `DiskQueueDepth`            | Histogram       | `DatabaseRole`, `Environment` |
| `FreeableMemory`            | `FreeableMemory`            | Histogram       | `DatabaseRole`, `Environment` |
| `NetworkReceiveThroughput`  | `NetworkReceiveThroughput`  | Histogram       | `DatabaseRole`, `Environment` |
| `NetworkTransmitThroughput` | `NetworkTransmitThroughput` | Histogram       | `DatabaseRole`, `Environment` |
| `ReadIOPS`                  | `ReadIOPS`                  | Histogram       | `DatabaseRole`, `Environment` |
| `ReadLatency`               | `ReadLatency`               | Histogram       | `DatabaseRole`, `Environment` |
| `ReadThroughput`            | `ReadThroughput`            | Histogram       | `DatabaseRole`, `Environment` |
| `WriteIOPS`                 | `WriteIOPS`                 | Histogram       | `DatabaseRole`, `Environment` |
| `WriteLatency`              | `WriteLatency`              | Histogram       | `DatabaseRole`, `Environment` |
| `WriteThroughput`           | `WriteThroughput`           | Histogram       | `DatabaseRole`, `Environment` |

## AWS/MediaTailor

The `AWS/MediaTailor` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/mediatailor`. All enriched instruments use Delta temporality.

- [AWS::MediaTailor::Channel](#otel-enrichment-aws-mediatailor-aws-mediatailor-channel "#otel-enrichment-aws-mediatailor-aws-mediatailor-channel")

### AWS::MediaTailor::Channel

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric          | OpenTelemetry metric | Instrument type | Data point attributes |
| --------------- | -------------------- | --------------- | --------------------- |
| `4xxErrorCount` | `4xxErrorCount`      | Sum             | `Channel`, `Output`   |
| `5xxErrorCount` | `5xxErrorCount`      | Sum             | `Channel`, `Output`   |
| `RequestCount`  | `RequestCount`       | Sum             | `Channel`, `Output`   |
| `TotalTime`     | `TotalTime`          | Histogram       | `Channel`, `Output`   |

## AWS/MemoryDB

The `AWS/MemoryDB` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/memorydb`. All enriched instruments use Delta temporality.

- [AWS::MemoryDB::Cluster](#otel-enrichment-aws-memorydb-aws-memorydb-cluster "#otel-enrichment-aws-memorydb-aws-memorydb-cluster")

### AWS::MemoryDB::Cluster

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                     | OpenTelemetry metric                       | Instrument type | Data point attributes     |
| ------------------------------------------ | ------------------------------------------ | --------------- | ------------------------- |
| `ActiveDefragHits`                         | `ActiveDefragHits`                         | Sum             | `ClusterName`, `NodeName` |
| `AuthenticationFailures`                   | `AuthenticationFailures`                   | Sum             | `ClusterName`, `NodeName` |
| `BytesReadFromDisk`                        | `BytesReadFromDisk`                        | Sum             | `ClusterName`, `NodeName` |
| `BytesUsedForMemoryDB`                     | `BytesUsedForMemoryDB`                     | Histogram       | `ClusterName`, `NodeName` |
| `BytesWrittenToDisk`                       | `BytesWrittenToDisk`                       | Sum             | `ClusterName`, `NodeName` |
| `CPUUtilization`                           | `CPUUtilization`                           | Histogram       | `ClusterName`, `NodeName` |
| `ChannelAuthorizationFailures`             | `ChannelAuthorizationFailures`             | Sum             | `ClusterName`, `NodeName` |
| `CommandAuthorizationFailures`             | `CommandAuthorizationFailures`             | Sum             | `ClusterName`, `NodeName` |
| `CurrConnections`                          | `CurrConnections`                          | Histogram       | `ClusterName`, `NodeName` |
| `CurrItems`                                | `CurrItems`                                | Histogram       | `ClusterName`, `NodeName` |
| `DB0AverageTTL`                            | `DB0AverageTTL`                            | Histogram       | `ClusterName`, `NodeName` |
| `DatabaseCapacityUsagePercentage`          | `DatabaseCapacityUsagePercentage`          | Histogram       | `ClusterName`, `NodeName` |
| `DatabaseMemoryUsagePercentage`            | `DatabaseMemoryUsagePercentage`            | Histogram       | `ClusterName`, `NodeName` |
| `EngineCPUUtilization`                     | `EngineCPUUtilization`                     | Histogram       | `ClusterName`, `NodeName` |
| `ErrorCount`                               | `ErrorCount`                               | Sum             | `ClusterName`, `NodeName` |
| `EvalBasedCmds`                            | `EvalBasedCmds`                            | Sum             | `ClusterName`, `NodeName` |
| `Evictions`                                | `Evictions`                                | Sum             | `ClusterName`, `NodeName` |
| `FreeableMemory`                           | `FreeableMemory`                           | Histogram       | `ClusterName`, `NodeName` |
| `GetTypeCmds`                              | `GetTypeCmds`                              | Sum             | `ClusterName`, `NodeName` |
| `HashBasedCmds`                            | `HashBasedCmds`                            | Sum             | `ClusterName`, `NodeName` |
| `IamAuthenticationExpirations`             | `IamAuthenticationExpirations`             | Sum             | `ClusterName`, `NodeName` |
| `IamAuthenticationThrottling`              | `IamAuthenticationThrottling`              | Sum             | `ClusterName`, `NodeName` |
| `IsPrimary`                                | `IsPrimary`                                | Histogram       | `ClusterName`, `NodeName` |
| `JsonBasedCmds`                            | `JsonBasedCmds`                            | Sum             | `ClusterName`, `NodeName` |
| `JsonBasedGetCmds`                         | `JsonBasedGetCmds`                         | Sum             | `ClusterName`, `NodeName` |
| `JsonBasedSetCmds`                         | `JsonBasedSetCmds`                         | Sum             | `ClusterName`, `NodeName` |
| `KeyAuthorizationFailures`                 | `KeyAuthorizationFailures`                 | Sum             | `ClusterName`, `NodeName` |
| `KeyBasedCmds`                             | `KeyBasedCmds`                             | Sum             | `ClusterName`, `NodeName` |
| `KeysTracked`                              | `KeysTracked`                              | Histogram       | `ClusterName`, `NodeName` |
| `KeyspaceHits`                             | `KeyspaceHits`                             | Sum             | `ClusterName`, `NodeName` |
| `KeyspaceMisses`                           | `KeyspaceMisses`                           | Sum             | `ClusterName`, `NodeName` |
| `ListBasedCmds`                            | `ListBasedCmds`                            | Sum             | `ClusterName`, `NodeName` |
| `MaxReplicationThroughput`                 | `MaxReplicationThroughput`                 | Histogram       | `ClusterName`, `NodeName` |
| `MemoryFragmentationRatio`                 | `MemoryFragmentationRatio`                 | Histogram       | `ClusterName`, `NodeName` |
| `NetworkBandwidthInAllowanceExceeded`      | `NetworkBandwidthInAllowanceExceeded`      | Sum             | `ClusterName`, `NodeName` |
| `NetworkBandwidthOutAllowanceExceeded`     | `NetworkBandwidthOutAllowanceExceeded`     | Sum             | `ClusterName`, `NodeName` |
| `NetworkBytesIn`                           | `NetworkBytesIn`                           | Sum             | `ClusterName`, `NodeName` |
| `NetworkBytesOut`                          | `NetworkBytesOut`                          | Sum             | `ClusterName`, `NodeName` |
| `NetworkConntrackAllowanceExceeded`        | `NetworkConntrackAllowanceExceeded`        | Sum             | `ClusterName`, `NodeName` |
| `NetworkMaxBytesIn`                        | `NetworkMaxBytesIn`                        | Histogram       | `ClusterName`, `NodeName` |
| `NetworkMaxBytesOut`                       | `NetworkMaxBytesOut`                       | Histogram       | `ClusterName`, `NodeName` |
| `NetworkMaxPacketsIn`                      | `NetworkMaxPacketsIn`                      | Histogram       | `ClusterName`, `NodeName` |
| `NetworkMaxPacketsOut`                     | `NetworkMaxPacketsOut`                     | Histogram       | `ClusterName`, `NodeName` |
| `NetworkPacketsIn`                         | `NetworkPacketsIn`                         | Sum             | `ClusterName`, `NodeName` |
| `NetworkPacketsOut`                        | `NetworkPacketsOut`                        | Sum             | `ClusterName`, `NodeName` |
| `NetworkPacketsPerSecondAllowanceExceeded` | `NetworkPacketsPerSecondAllowanceExceeded` | Sum             | `ClusterName`, `NodeName` |
| `NewConnections`                           | `NewConnections`                           | Sum             | `ClusterName`, `NodeName` |
| `NonKeyTypeCmds`                           | `NonKeyTypeCmds`                           | Sum             | `ClusterName`, `NodeName` |
| `NumItemsReadFromDisk`                     | `NumItemsReadFromDisk`                     | Sum             | `ClusterName`, `NodeName` |
| `NumItemsWrittenToDisk`                    | `NumItemsWrittenToDisk`                    | Sum             | `ClusterName`, `NodeName` |
| `PrimaryLinkHealthStatus`                  | `PrimaryLinkHealthStatus`                  | Histogram       | `ClusterName`, `NodeName` |
| `PubSubBasedCmds`                          | `PubSubBasedCmds`                          | Sum             | `ClusterName`, `NodeName` |
| `Reclaimed`                                | `Reclaimed`                                | Sum             | `ClusterName`, `NodeName` |
| `ReplicationBytes`                         | `ReplicationBytes`                         | Sum             | `ClusterName`, `NodeName` |
| `ReplicationDelayedWriteCommands`          | `ReplicationDelayedWriteCommands`          | Sum             | `ClusterName`, `NodeName` |
| `ReplicationLag`                           | `ReplicationLag`                           | Histogram       | `ClusterName`, `NodeName` |
| `SearchBasedCmds`                          | `SearchBasedCmds`                          | Sum             | `ClusterName`, `NodeName` |
| `SearchBasedGetCmds`                       | `SearchBasedGetCmds`                       | Sum             | `ClusterName`, `NodeName` |
| `SearchBasedSetCmds`                       | `SearchBasedSetCmds`                       | Sum             | `ClusterName`, `NodeName` |
| `SearchNumberOfIndexedKeys`                | `SearchNumberOfIndexedKeys`                | Histogram       | `ClusterName`, `NodeName` |
| `SearchNumberOfIndexes`                    | `SearchNumberOfIndexes`                    | Histogram       | `ClusterName`, `NodeName` |
| `SearchTotalIndexSize`                     | `SearchTotalIndexSize`                     | Histogram       | `ClusterName`, `NodeName` |
| `SetBasedCmds`                             | `SetBasedCmds`                             | Sum             | `ClusterName`, `NodeName` |
| `SetTypeCmds`                              | `SetTypeCmds`                              | Sum             | `ClusterName`, `NodeName` |
| `SortedSetBasedCmds`                       | `SortedSetBasedCmds`                       | Sum             | `ClusterName`, `NodeName` |
| `StreamBasedCmds`                          | `StreamBasedCmds`                          | Sum             | `ClusterName`, `NodeName` |
| `StringBasedCmds`                          | `StringBasedCmds`                          | Sum             | `ClusterName`, `NodeName` |
| `SuccessfulReadRequestLatency`             | `SuccessfulReadRequestLatency`             | Histogram       | `ClusterName`, `NodeName` |
| `SuccessfulWriteRequestLatency`            | `SuccessfulWriteRequestLatency`            | Histogram       | `ClusterName`, `NodeName` |
| `SwapUsage`                                | `SwapUsage`                                | Histogram       | `ClusterName`, `NodeName` |

## AWS/NATGateway

The `AWS/NATGateway` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/ec2`. All enriched instruments use Delta temporality.

- [AWS::EC2::NatGateway](#otel-enrichment-aws-natgateway-aws-ec2-natgateway "#otel-enrichment-aws-natgateway-aws-ec2-natgateway")

### AWS::EC2::NatGateway

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                       | OpenTelemetry metric         | Instrument type | Data point attributes |
| ---------------------------- | ---------------------------- | --------------- | --------------------- |
| `ActiveConnectionCount`      | `ActiveConnectionCount`      | Histogram       | `NatGatewayId`        |
| `BytesInFromDestination`     | `BytesInFromDestination`     | Sum             | `NatGatewayId`        |
| `BytesInFromSource`          | `BytesInFromSource`          | Sum             | `NatGatewayId`        |
| `BytesOutToDestination`      | `BytesOutToDestination`      | Sum             | `NatGatewayId`        |
| `BytesOutToSource`           | `BytesOutToSource`           | Sum             | `NatGatewayId`        |
| `ConnectionAttemptCount`     | `ConnectionAttemptCount`     | Sum             | `NatGatewayId`        |
| `ConnectionEstablishedCount` | `ConnectionEstablishedCount` | Sum             | `NatGatewayId`        |
| `ErrorPortAllocation`        | `ErrorPortAllocation`        | Sum             | `NatGatewayId`        |
| `IdleTimeoutCount`           | `IdleTimeoutCount`           | Sum             | `NatGatewayId`        |
| `PacketsDropCount`           | `PacketsDropCount`           | Sum             | `NatGatewayId`        |
| `PacketsInFromDestination`   | `PacketsInFromDestination`   | Sum             | `NatGatewayId`        |
| `PacketsInFromSource`        | `PacketsInFromSource`        | Sum             | `NatGatewayId`        |
| `PacketsOutToDestination`    | `PacketsOutToDestination`    | Sum             | `NatGatewayId`        |
| `PacketsOutToSource`         | `PacketsOutToSource`         | Sum             | `NatGatewayId`        |
| `PeakBytesPerSecond`         | `PeakBytesPerSecond`         | Histogram       | `NatGatewayId`        |
| `PeakPacketsPerSecond`       | `PeakPacketsPerSecond`       | Histogram       | `NatGatewayId`        |

## AWS/NetworkELB

The `AWS/NetworkELB` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/elasticloadbalancing`. All enriched instruments use Delta temporality.

- [AWS::ElasticLoadBalancingV2::LoadBalancer](#otel-enrichment-aws-networkelb-aws-elasticloadbalancingv2-loadbalancer "#otel-enrichment-aws-networkelb-aws-elasticloadbalancingv2-loadbalancer")

### AWS::ElasticLoadBalancingV2::LoadBalancer

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                      | OpenTelemetry metric        | Instrument type | Data point attributes                             |
| --------------------------- | --------------------------- | --------------- | ------------------------------------------------- |
| `ActiveFlowCount`           | `ActiveFlowCount`           | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `ActiveFlowCount_TCP`       | `ActiveFlowCount_TCP`       | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `ActiveFlowCount_TLS`       | `ActiveFlowCount_TLS`       | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `ActiveFlowCount_UDP`       | `ActiveFlowCount_UDP`       | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `ActiveZonalShiftHostCount` | `ActiveZonalShiftHostCount` | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `HealthyHostCount`          | `HealthyHostCount`          | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `NewFlowCount`              | `NewFlowCount`              | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `NewFlowCount_TCP`          | `NewFlowCount_TCP`          | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `NewFlowCount_TLS`          | `NewFlowCount_TLS`          | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `NewFlowCount_UDP`          | `NewFlowCount_UDP`          | Sum             | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |
| `PeakPacketsPerSecond`      | `PeakPacketsPerSecond`      | Histogram       | `AvailabilityZone`, `LoadBalancer`                |
| `PortAllocationErrorCount`  | `PortAllocationErrorCount`  | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ProcessedBytes`            | `ProcessedBytes`            | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ProcessedBytes_TCP`        | `ProcessedBytes_TCP`        | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ProcessedBytes_TLS`        | `ProcessedBytes_TLS`        | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ProcessedBytes_UDP`        | `ProcessedBytes_UDP`        | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `ProcessedPackets`          | `ProcessedPackets`          | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `TCP_Client_Reset_Count`    | `TCP_Client_Reset_Count`    | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `TCP_ELB_Reset_Count`       | `TCP_ELB_Reset_Count`       | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `TCP_Target_Reset_Count`    | `TCP_Target_Reset_Count`    | Sum             | `AvailabilityZone`, `LoadBalancer`                |
| `UnHealthyHostCount`        | `UnHealthyHostCount`        | Histogram       | `AvailabilityZone`, `LoadBalancer`, `TargetGroup` |

## AWS/NetworkFirewall

The `AWS/NetworkFirewall` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/network-firewall`. All enriched instruments use Delta temporality.

- [AWS::NetworkFirewall::Firewall](#otel-enrichment-aws-networkfirewall-aws-networkfirewall-firewall "#otel-enrichment-aws-networkfirewall-aws-networkfirewall-firewall")

### AWS::NetworkFirewall::Firewall

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                  | OpenTelemetry metric                    | Instrument type | Data point attributes                                        |
| --------------------------------------- | --------------------------------------- | --------------- | ------------------------------------------------------------ |
| `DroppedPackets`                        | `DroppedPackets`                        | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `InvalidDroppedPackets`                 | `InvalidDroppedPackets`                 | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `OtherDroppedPackets`                   | `OtherDroppedPackets`                   | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `Packets`                               | `Packets`                               | Sum             | `AvailabilityZone`, `CustomAction`, `Engine`, `FirewallName` |
| `PassedPackets`                         | `PassedPackets`                         | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `ReceivedPackets`                       | `ReceivedPackets`                       | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `RejectedPackets`                       | `RejectedPackets`                       | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `StreamExceptionPolicyPackets`          | `StreamExceptionPolicyPackets`          | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `TLSDroppedPackets`                     | `TLSDroppedPackets`                     | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `TLSErrors`                             | `TLSErrors`                             | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `TLSPassedPackets`                      | `TLSPassedPackets`                      | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `TLSReceivedPackets`                    | `TLSReceivedPackets`                    | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `TLSRejectedPackets`                    | `TLSRejectedPackets`                    | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `TLSRevocationStatusOKConnections`      | `TLSRevocationStatusOKConnections`      | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `TLSRevocationStatusRevokedConnections` | `TLSRevocationStatusRevokedConnections` | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `TLSRevocationStatusUnknownConnections` | `TLSRevocationStatusUnknownConnections` | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |
| `TLSTimedOutConnections`                | `TLSTimedOutConnections`                | Sum             | `AvailabilityZone`, `Engine`, `FirewallName`                 |

## AWS/Pinpoint

The `AWS/Pinpoint` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/mobiletargeting`. All enriched instruments use Delta temporality.

- [AWS::Pinpoint::App](#otel-enrichment-aws-pinpoint-aws-pinpoint-app "#otel-enrichment-aws-pinpoint-aws-pinpoint-app")

### AWS::Pinpoint::App

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                                | OpenTelemetry metric                  | Instrument type | Data point attributes             |
| ------------------------------------- | ------------------------------------- | --------------- | --------------------------------- |
| `CampaignSendMessageLatency`          | `CampaignSendMessageLatency`          | Histogram       | `ApplicationId`, `Channel`        |
| `CampaignSendMessagePermanentFailure` | `CampaignSendMessagePermanentFailure` | Sum             | `ApplicationId`, `Channel`        |
| `CampaignSendMessageSuccess`          | `CampaignSendMessageSuccess`          | Sum             | `ApplicationId`, `Channel`        |
| `CampaignSendMessageTemporaryFailure` | `CampaignSendMessageTemporaryFailure` | Sum             | `ApplicationId`, `Channel`        |
| `CampaignSendMessageThrottled`        | `CampaignSendMessageThrottled`        | Sum             | `ApplicationId`, `Channel`        |
| `DLRFailure`                          | `DLRFailure`                          | Sum             | `ApplicationId`, `IsoCountryCode` |
| `DLRSuccess`                          | `DLRSuccess`                          | Sum             | `ApplicationId`, `IsoCountryCode` |
| `DestinationChannelCount`             | `DestinationChannelCount`             | Histogram       | `ApplicationId`, `Channel`        |
| `DirectSendMessageLatency`            | `DirectSendMessageLatency`            | Histogram       | `ApplicationId`, `Channel`        |
| `DirectSendMessagePermanentFailure`   | `DirectSendMessagePermanentFailure`   | Sum             | `ApplicationId`, `Channel`        |
| `DirectSendMessageSuccess`            | `DirectSendMessageSuccess`            | Sum             | `ApplicationId`, `Channel`        |
| `DirectSendMessageTemporaryFailure`   | `DirectSendMessageTemporaryFailure`   | Sum             | `ApplicationId`, `Channel`        |
| `DirectSendMessageThrottled`          | `DirectSendMessageThrottled`          | Sum             | `ApplicationId`, `Channel`        |
| `EndpointRegistrationFailure`         | `EndpointRegistrationFailure`         | Sum             | `ApplicationId`                   |
| `ExportEventErrors`                   | `ExportEventErrors`                   | Sum             | `ApplicationId`, `ErrorCode`      |
| `ExportedEvents`                      | `ExportedEvents`                      | Sum             | `ApplicationId`                   |
| `ImportJobDuration`                   | `ImportJobDuration`                   | Histogram       | `ApplicationId`                   |
| `ImportJobFailure`                    | `ImportJobFailure`                    | Sum             | `ApplicationId`                   |
| `ImportedEndpointFailure`             | `ImportedEndpointFailure`             | Sum             | `ApplicationId`                   |
| `JourneySendMessageLatency`           | `JourneySendMessageLatency`           | Histogram       | `ApplicationId`, `Channel`        |
| `JourneySendMessagePermanentFailure`  | `JourneySendMessagePermanentFailure`  | Sum             | `ApplicationId`, `Channel`        |
| `JourneySendMessageSuccess`           | `JourneySendMessageSuccess`           | Sum             | `ApplicationId`, `Channel`        |
| `OTPSendMessageLatency`               | `OTPSendMessageLatency`               | Histogram       | `ApplicationId`, `Channel`        |
| `OTPSendMessageSuccess`               | `OTPSendMessageSuccess`               | Sum             | `ApplicationId`, `Channel`        |
| `OTPVerificationAttempt`              | `OTPVerificationAttempt`              | Sum             | `ApplicationId`, `Channel`        |
| `OTPVerificationFailure`              | `OTPVerificationFailure`              | Sum             | `ApplicationId`, `Channel`        |
| `OTPVerificationFailureFinalAttempt`  | `OTPVerificationFailureFinalAttempt`  | Sum             | `ApplicationId`                   |
| `OTPVerificationSuccess`              | `OTPVerificationSuccess`              | Sum             | `ApplicationId`, `Channel`        |
| `TotalEvents`                         | `TotalEvents`                         | Sum             | `ApplicationId`                   |

## AWS/Prometheus

The `AWS/Prometheus` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/aps`. All enriched instruments use Delta temporality.

- [AWS::APS::AnomalyDetector](#otel-enrichment-aws-prometheus-aws-aps-anomalydetector "#otel-enrichment-aws-prometheus-aws-aps-anomalydetector")
- [AWS::APS::RuleGroupsNamespace](#otel-enrichment-aws-prometheus-aws-aps-rulegroupsnamespace "#otel-enrichment-aws-prometheus-aws-aps-rulegroupsnamespace")
- [AWS::APS::Workspace](#otel-enrichment-aws-prometheus-aws-aps-workspace "#otel-enrichment-aws-prometheus-aws-aps-workspace")

### AWS::APS::AnomalyDetector

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                                  | OpenTelemetry metric                    | Instrument type | Data point attributes            |
| --------------------------------------- | --------------------------------------- | --------------- | -------------------------------- |
| `AnomalyDetectorEvaluationFailures`     | `AnomalyDetectorEvaluationFailures`     | Sum             | `AnomalyDetectorId`, `Workspace` |
| `AnomalyDetectorEvaluations`            | `AnomalyDetectorEvaluations`            | Sum             | `AnomalyDetectorId`, `Workspace` |
| `AnomalyDetectorLastEvaluationDuration` | `AnomalyDetectorLastEvaluationDuration` | Histogram       | `AnomalyDetectorId`, `Workspace` |

### AWS::APS::RuleGroupsNamespace

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                            | OpenTelemetry metric              | Instrument type | Data point attributes    |
| --------------------------------- | --------------------------------- | --------------- | ------------------------ |
| `RuleEvaluationFailures`          | `RuleEvaluationFailures`          | Sum             | `RuleGroup`, `Workspace` |
| `RuleEvaluations`                 | `RuleEvaluations`                 | Sum             | `RuleGroup`, `Workspace` |
| `RuleGroupIterationsMissed`       | `RuleGroupIterationsMissed`       | Sum             | `RuleGroup`, `Workspace` |
| `RuleGroupLastEvaluationDuration` | `RuleGroupLastEvaluationDuration` | Histogram       | `RuleGroup`, `Workspace` |

### AWS::APS::Workspace

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                            | OpenTelemetry metric                              | Instrument type | Data point attributes             |
| ------------------------------------------------- | ------------------------------------------------- | --------------- | --------------------------------- |
| `ActiveSeriesLimitPerLabelSet`                    | `ActiveSeriesLimitPerLabelSet`                    | Histogram       | `LabelSet`, `Workspace`           |
| `ActiveSeriesPerLabelSet`                         | `ActiveSeriesPerLabelSet`                         | Histogram       | `LabelSet`, `Workspace`           |
| `AlertManagerAlertsReceived`                      | `AlertManagerAlertsReceived`                      | Sum             | `Workspace`                       |
| `AlertManagerNotificationsFailed`                 | `AlertManagerNotificationsFailed`                 | Sum             | `Workspace`                       |
| `AlertManagerNotificationsFailedByIntegration`    | `AlertManagerNotificationsFailedByIntegration`    | Sum             | `Workspace`                       |
| `AlertManagerNotificationsThrottled`              | `AlertManagerNotificationsThrottled`              | Sum             | `Workspace`                       |
| `AlertManagerNotificationsThrottledByIntegration` | `AlertManagerNotificationsThrottledByIntegration` | Sum             | `Workspace`                       |
| `DiscardedSamples`                                | `DiscardedSamples`                                | Sum             | `Reason`, `Workspace`             |
| `DiscardedSamplesPerLabelSet`                     | `DiscardedSamplesPerLabelSet`                     | Sum             | `LabelSet`, `Reason`, `Workspace` |
| `DiscardedSeries`                                 | `DiscardedSeries`                                 | Sum             | `Reason`, `Workspace`             |
| `DiscardedSeriesPerLabelSet`                      | `DiscardedSeriesPerLabelSet`                      | Sum             | `LabelSet`, `Reason`, `Workspace` |
| `IngestionRatePerLabelSet`                        | `IngestionRatePerLabelSet`                        | Histogram       | `LabelSet`, `Workspace`           |
| `QuerySamplesProcessed`                           | `QuerySamplesProcessed`                           | Sum             | `Workspace`                       |
| `SecretFetchFailure`                              | `SecretFetchFailure`                              | Sum             | `Workspace`                       |

## AWS/RDS

The `AWS/RDS` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/rds`. All enriched instruments use Delta temporality.

- [AWS::RDS::DBCluster](#otel-enrichment-aws-rds-aws-rds-dbcluster "#otel-enrichment-aws-rds-aws-rds-dbcluster")
- [AWS::RDS::DBInstance](#otel-enrichment-aws-rds-aws-rds-dbinstance "#otel-enrichment-aws-rds-aws-rds-dbinstance")

### AWS::RDS::DBCluster

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                                       | OpenTelemetry metric                                         | Instrument type | Data point attributes               |
| ------------------------------------------------------------ | ------------------------------------------------------------ | --------------- | ----------------------------------- |
| `AbortedClients`                                             | `AbortedClients`                                             | Sum             | `DBClusterIdentifier`, `Role`       |
| `ActiveTransactions`                                         | `ActiveTransactions`                                         | Histogram       | `DBClusterIdentifier`, `Role`       |
| `AuroraBinlogReplicaLag`                                     | `AuroraBinlogReplicaLag`                                     | Histogram       | `DBClusterIdentifier`, `Role`       |
| `AuroraDMLRejectedMasterFull`                                | `AuroraDMLRejectedMasterFull`                                | Sum             | `DBClusterIdentifier`, `Role`       |
| `AuroraReplicaLagMaximum`                                    | `AuroraReplicaLagMaximum`                                    | Histogram       | `DBClusterIdentifier`, `Role`       |
| `AuroraReplicaLagMinimum`                                    | `AuroraReplicaLagMinimum`                                    | Histogram       | `DBClusterIdentifier`, `Role`       |
| `AuroraVolumeBytesLeftTotal`                                 | `AuroraVolumeBytesLeftTotal`                                 | Histogram       | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_attempted`                                | `Aurora_pq_request_attempted`                                | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_executed`                                 | `Aurora_pq_request_executed`                                 | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_failed`                                   | `Aurora_pq_request_failed`                                   | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_in_progress`                              | `Aurora_pq_request_in_progress`                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen`                               | `Aurora_pq_request_not_chosen`                               | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_below_min_rows`                | `Aurora_pq_request_not_chosen_below_min_rows`                | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_column_bit`                    | `Aurora_pq_request_not_chosen_column_bit`                    | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_column_geometry`               | `Aurora_pq_request_not_chosen_column_geometry`               | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_column_lob`                    | `Aurora_pq_request_not_chosen_column_lob`                    | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_column_virtual`                | `Aurora_pq_request_not_chosen_column_virtual`                | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_custom_charset`                | `Aurora_pq_request_not_chosen_custom_charset`                | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_fast_ddl`                      | `Aurora_pq_request_not_chosen_fast_ddl`                      | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_few_pages_outside_buffer_pool` | `Aurora_pq_request_not_chosen_few_pages_outside_buffer_pool` | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_full_text_index`               | `Aurora_pq_request_not_chosen_full_text_index`               | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_high_buffer_pool_pct`          | `Aurora_pq_request_not_chosen_high_buffer_pool_pct`          | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_index_hint`                    | `Aurora_pq_request_not_chosen_index_hint`                    | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_innodb_table_format`           | `Aurora_pq_request_not_chosen_innodb_table_format`           | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_long_trx`                      | `Aurora_pq_request_not_chosen_long_trx`                      | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_no_where_clause`               | `Aurora_pq_request_not_chosen_no_where_clause`               | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_range_scan`                    | `Aurora_pq_request_not_chosen_range_scan`                    | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_row_length_too_long`           | `Aurora_pq_request_not_chosen_row_length_too_long`           | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_small_table`                   | `Aurora_pq_request_not_chosen_small_table`                   | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_temporary_table`               | `Aurora_pq_request_not_chosen_temporary_table`               | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_tx_isolation`                  | `Aurora_pq_request_not_chosen_tx_isolation`                  | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_unsupported_access`            | `Aurora_pq_request_not_chosen_unsupported_access`            | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_not_chosen_update_delete_stmts`           | `Aurora_pq_request_not_chosen_update_delete_stmts`           | Sum             | `DBClusterIdentifier`, `Role`       |
| `Aurora_pq_request_throttled`                                | `Aurora_pq_request_throttled`                                | Sum             | `DBClusterIdentifier`, `Role`       |
| `BlockedTransactions`                                        | `BlockedTransactions`                                        | Histogram       | `DBClusterIdentifier`, `Role`       |
| `BufferCacheHitRatio`                                        | `BufferCacheHitRatio`                                        | Histogram       | `DBClusterIdentifier`, `Role`       |
| `CPUUtilization`                                             | `CPUUtilization`                                             | Histogram       | `DBClusterIdentifier`, `Role`       |
| `CommitLatency`                                              | `CommitLatency`                                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `CommitThroughput`                                           | `CommitThroughput`                                           | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ConnectionAttempts`                                         | `ConnectionAttempts`                                         | Sum             | `DBClusterIdentifier`, `Role`       |
| `DDLLatency`                                                 | `DDLLatency`                                                 | Histogram       | `DBClusterIdentifier`, `Role`       |
| `DDLThroughput`                                              | `DDLThroughput`                                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `DMLLatency`                                                 | `DMLLatency`                                                 | Histogram       | `DBClusterIdentifier`, `Role`       |
| `DMLThroughput`                                              | `DMLThroughput`                                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `DatabaseConnections`                                        | `DatabaseConnections`                                        | Histogram       | `DBClusterIdentifier`, `Role`       |
| `Deadlocks`                                                  | `Deadlocks`                                                  | Histogram       | `DBClusterIdentifier`, `Role`       |
| `DeleteLatency`                                              | `DeleteLatency`                                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `DeleteThroughput`                                           | `DeleteThroughput`                                           | Histogram       | `DBClusterIdentifier`, `Role`       |
| `DiskQueueDepth`                                             | `DiskQueueDepth`                                             | Histogram       | `DBClusterIdentifier`, `Role`       |
| `EBSByteBalance%`                                            | `EBSByteBalance%`                                            | Histogram       | `DBClusterIdentifier`, `Role`       |
| `EBSIOBalance%`                                              | `EBSIOBalance%`                                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `EngineUptime`                                               | `EngineUptime`                                               | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ForwardingMasterDMLLatency`                                 | `ForwardingMasterDMLLatency`                                 | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ForwardingMasterDMLThroughput`                              | `ForwardingMasterDMLThroughput`                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ForwardingMasterOpenSessions`                               | `ForwardingMasterOpenSessions`                               | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ForwardingReplicaDMLLatency`                                | `ForwardingReplicaDMLLatency`                                | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ForwardingReplicaDMLThroughput`                             | `ForwardingReplicaDMLThroughput`                             | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ForwardingReplicaOpenSessions`                              | `ForwardingReplicaOpenSessions`                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ForwardingReplicaReadWaitLatency`                           | `ForwardingReplicaReadWaitLatency`                           | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ForwardingReplicaReadWaitThroughput`                        | `ForwardingReplicaReadWaitThroughput`                        | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ForwardingReplicaSelectLatency`                             | `ForwardingReplicaSelectLatency`                             | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ForwardingReplicaSelectThroughput`                          | `ForwardingReplicaSelectThroughput`                          | Histogram       | `DBClusterIdentifier`, `Role`       |
| `FreeLocalStorage`                                           | `FreeLocalStorage`                                           | Histogram       | `DBClusterIdentifier`, `Role`       |
| `FreeableMemory`                                             | `FreeableMemory`                                             | Histogram       | `DBClusterIdentifier`, `Role`       |
| `InsertLatency`                                              | `InsertLatency`                                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `InsertThroughput`                                           | `InsertThroughput`                                           | Histogram       | `DBClusterIdentifier`, `Role`       |
| `LoginFailures`                                              | `LoginFailures`                                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `NetworkReceiveThroughput`                                   | `NetworkReceiveThroughput`                                   | Histogram       | `DBClusterIdentifier`, `Role`       |
| `NetworkThroughput`                                          | `NetworkThroughput`                                          | Histogram       | `DBClusterIdentifier`, `Role`       |
| `NetworkTransmitThroughput`                                  | `NetworkTransmitThroughput`                                  | Histogram       | `DBClusterIdentifier`, `Role`       |
| `NumBinaryLogFiles`                                          | `NumBinaryLogFiles`                                          | Histogram       | `DBClusterIdentifier`, `Role`       |
| `PurgeBoundary`                                              | `PurgeBoundary`                                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `PurgeFinishedPoint`                                         | `PurgeFinishedPoint`                                         | Histogram       | `DBClusterIdentifier`, `Role`       |
| `Queries`                                                    | `Queries`                                                    | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ReadIOPS`                                                   | `ReadIOPS`                                                   | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ReadLatency`                                                | `ReadLatency`                                                | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ReadThroughput`                                             | `ReadThroughput`                                             | Histogram       | `DBClusterIdentifier`, `Role`       |
| `ResultSetCacheHitRatio`                                     | `ResultSetCacheHitRatio`                                     | Histogram       | `DBClusterIdentifier`, `Role`       |
| `RollbackSegmentHistoryListLength`                           | `RollbackSegmentHistoryListLength`                           | Histogram       | `DBClusterIdentifier`, `Role`       |
| `RowLockTime`                                                | `RowLockTime`                                                | Sum             | `DBClusterIdentifier`, `Role`       |
| `SelectLatency`                                              | `SelectLatency`                                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `SelectThroughput`                                           | `SelectThroughput`                                           | Histogram       | `DBClusterIdentifier`, `Role`       |
| `StorageNetworkReceiveThroughput`                            | `StorageNetworkReceiveThroughput`                            | Histogram       | `DBClusterIdentifier`, `Role`       |
| `StorageNetworkThroughput`                                   | `StorageNetworkThroughput`                                   | Histogram       | `DBClusterIdentifier`, `Role`       |
| `StorageNetworkTransmitThroughput`                           | `StorageNetworkTransmitThroughput`                           | Histogram       | `DBClusterIdentifier`, `Role`       |
| `SumBinaryLogSize`                                           | `SumBinaryLogSize`                                           | Histogram       | `DBClusterIdentifier`, `Role`       |
| `SwapUsage`                                                  | `SwapUsage`                                                  | Histogram       | `DBClusterIdentifier`, `Role`       |
| `TruncateFinishedPoint`                                      | `TruncateFinishedPoint`                                      | Histogram       | `DBClusterIdentifier`, `Role`       |
| `UpdateLatency`                                              | `UpdateLatency`                                              | Histogram       | `DBClusterIdentifier`, `Role`       |
| `UpdateThroughput`                                           | `UpdateThroughput`                                           | Histogram       | `DBClusterIdentifier`, `Role`       |
| `VolumeBytesUsed`                                            | `VolumeBytesUsed`                                            | Histogram       | `DbClusterIdentifier`, `EngineName` |
| `VolumeReadIOPs`                                             | `VolumeReadIOPs`                                             | Histogram       | `DbClusterIdentifier`, `EngineName` |
| `VolumeWriteIOPs`                                            | `VolumeWriteIOPs`                                            | Histogram       | `DbClusterIdentifier`, `EngineName` |
| `WriteIOPS`                                                  | `WriteIOPS`                                                  | Histogram       | `DBClusterIdentifier`, `Role`       |
| `WriteLatency`                                               | `WriteLatency`                                               | Histogram       | `DBClusterIdentifier`, `Role`       |
| `WriteThroughput`                                            | `WriteThroughput`                                            | Histogram       | `DBClusterIdentifier`, `Role`       |

### AWS::RDS::DBInstance

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                | OpenTelemetry metric  | Instrument type | Data point attributes  |
| --------------------- | --------------------- | --------------- | ---------------------- |
| `CPUUtilization`      | `CPUUtilization`      | Histogram       | `DBInstanceIdentifier` |
| `DatabaseConnections` | `DatabaseConnections` | Histogram       | `DBInstanceIdentifier` |
| `FreeStorageSpace`    | `FreeStorageSpace`    | Histogram       | `DBInstanceIdentifier` |
| `FreeableMemory`      | `FreeableMemory`      | Histogram       | `DBInstanceIdentifier` |
| `ReadIOPS`            | `ReadIOPS`            | Histogram       | `DBInstanceIdentifier` |
| `ReadLatency`         | `ReadLatency`         | Histogram       | `DBInstanceIdentifier` |
| `ReadThroughput`      | `ReadThroughput`      | Histogram       | `DBInstanceIdentifier` |
| `WriteIOPS`           | `WriteIOPS`           | Histogram       | `DBInstanceIdentifier` |
| `WriteLatency`        | `WriteLatency`        | Histogram       | `DBInstanceIdentifier` |
| `WriteThroughput`     | `WriteThroughput`     | Histogram       | `DBInstanceIdentifier` |

## AWS/RUM

The `AWS/RUM` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/rum`. All enriched instruments use Delta temporality.

- [AWS::RUM::AppMonitor](#otel-enrichment-aws-rum-aws-rum-appmonitor "#otel-enrichment-aws-rum-aws-rum-appmonitor")

### AWS::RUM::AppMonitor

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                            | OpenTelemetry metric              | Instrument type | Data point attributes                                             |
| --------------------------------- | --------------------------------- | --------------- | ----------------------------------------------------------------- |
| `Http4xxCount`                    | `Http4xxCount`                    | Sum             | `application_name`                                                |
| `Http5xxCount`                    | `Http5xxCount`                    | Sum             | `application_name`                                                |
| `HttpStatusCodeCount`             | `HttpStatusCodeCount`             | Sum             | `application_name`, `event_details.response.status`, `event_type` |
| `JsErrorCount`                    | `JsErrorCount`                    | Sum             | `application_name`                                                |
| `NavigationFrustratedTransaction` | `NavigationFrustratedTransaction` | Sum             | `application_name`                                                |
| `NavigationSatisfiedTransaction`  | `NavigationSatisfiedTransaction`  | Sum             | `application_name`                                                |
| `NavigationToleratedTransaction`  | `NavigationToleratedTransaction`  | Sum             | `application_name`                                                |
| `PageViewCount`                   | `PageViewCount`                   | Sum             | `application_name`                                                |
| `PerformanceNavigationDuration`   | `PerformanceNavigationDuration`   | Histogram       | `application_name`                                                |
| `PerformanceResourceDuration`     | `PerformanceResourceDuration`     | Histogram       | `application_name`, `event_details.file.type`, `event_type`       |
| `RumEventPayloadSize`             | `RumEventPayloadSize`             | Histogram       | `application_name`                                                |
| `SessionCount`                    | `SessionCount`                    | Sum             | `application_name`                                                |
| `WebVitalsCumulativeLayoutShift`  | `WebVitalsCumulativeLayoutShift`  | Histogram       | `application_name`                                                |
| `WebVitalsFirstInputDelay`        | `WebVitalsFirstInputDelay`        | Histogram       | `application_name`                                                |
| `WebVitalsLargestContentfulPaint` | `WebVitalsLargestContentfulPaint` | Histogram       | `application_name`                                                |

## AWS/Redshift

The `AWS/Redshift` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/redshift`. All enriched instruments use Delta temporality.

- [AWS::Redshift::Cluster](#otel-enrichment-aws-redshift-aws-redshift-cluster "#otel-enrichment-aws-redshift-aws-redshift-cluster")

### AWS::Redshift::Cluster

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                    | OpenTelemetry metric                      | Instrument type | Data point attributes                    |
| ----------------------------------------- | ----------------------------------------- | --------------- | ---------------------------------------- |
| `CPUUtilization`                          | `CPUUtilization`                          | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `CommitQueueLength`                       | `CommitQueueLength`                       | Histogram       | `ClusterIdentifier`                      |
| `ConcurrencyScalingActiveClusters`        | `ConcurrencyScalingActiveClusters`        | Histogram       | `ClusterIdentifier`                      |
| `ConcurrencyScalingSeconds`               | `ConcurrencyScalingSeconds`               | Sum             | `ClusterIdentifier`                      |
| `DatabaseConnections`                     | `DatabaseConnections`                     | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `HealthStatus`                            | `HealthStatus`                            | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `MaintenanceMode`                         | `MaintenanceMode`                         | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `MaxConfiguredConcurrencyScalingClusters` | `MaxConfiguredConcurrencyScalingClusters` | Histogram       | `ClusterIdentifier`                      |
| `NetworkReceiveThroughput`                | `NetworkReceiveThroughput`                | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `NetworkTransmitThroughput`               | `NetworkTransmitThroughput`               | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `NumExceededSchemaQuotas`                 | `NumExceededSchemaQuotas`                 | Histogram       | `ClusterIdentifier`                      |
| `PercentageDiskSpaceUsed`                 | `PercentageDiskSpaceUsed`                 | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `QueriesCompletedPerSecond`               | `QueriesCompletedPerSecond`               | Histogram       | `ClusterIdentifier`, `NodeID`, `latency` |
| `QueryDuration`                           | `QueryDuration`                           | Histogram       | `ClusterIdentifier`, `NodeID`, `latency` |
| `QueryRuntimeBreakdown`                   | `QueryRuntimeBreakdown`                   | Histogram       | `ClusterIdentifier`, `NodeID`, `stage`   |
| `ReadIOPS`                                | `ReadIOPS`                                | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `ReadLatency`                             | `ReadLatency`                             | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `ReadThroughput`                          | `ReadThroughput`                          | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `RedshiftManagedStorageTotalCapacity`     | `RedshiftManagedStorageTotalCapacity`     | Histogram       | `ClusterIdentifier`                      |
| `TotalTableCount`                         | `TotalTableCount`                         | Histogram       | `ClusterIdentifier`                      |
| `WLMQueriesCompletedPerSecond`            | `WLMQueriesCompletedPerSecond`            | Histogram       | `ClusterIdentifier`, `wlmid`             |
| `WLMQueryDuration`                        | `WLMQueryDuration`                        | Histogram       | `ClusterIdentifier`, `NodeID`, `wlmid`   |
| `WLMQueueLength`                          | `WLMQueueLength`                          | Histogram       | `ClusterIdentifier`, `QueueName`         |
| `WLMQueueWaitTime`                        | `WLMQueueWaitTime`                        | Histogram       | `ClusterIdentifier`, `wlmid`             |
| `WLMRunningQueries`                       | `WLMRunningQueries`                       | Histogram       | `ClusterIdentifier`, `QueueName`         |
| `WriteIOPS`                               | `WriteIOPS`                               | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `WriteLatency`                            | `WriteLatency`                            | Histogram       | `ClusterIdentifier`, `NodeID`            |
| `WriteThroughput`                         | `WriteThroughput`                         | Histogram       | `ClusterIdentifier`, `NodeID`            |

## AWS/Redshift-Serverless

The `AWS/Redshift-Serverless` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/redshift-serverless`. All enriched instruments use Delta temporality.

- [AWS::RedshiftServerless::Namespace](#otel-enrichment-aws-redshift-serverless-aws-redshiftserverless-namespace "#otel-enrichment-aws-redshift-serverless-aws-redshiftserverless-namespace")
- [AWS::RedshiftServerless::Workgroup](#otel-enrichment-aws-redshift-serverless-aws-redshiftserverless-workgroup "#otel-enrichment-aws-redshift-serverless-aws-redshiftserverless-workgroup")

### AWS::RedshiftServerless::Namespace

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric            | OpenTelemetry metric | Instrument type | Data point attributes       |
| ----------------- | -------------------- | --------------- | --------------------------- |
| `DataStorage`     | `DataStorage`        | Histogram       | `Namespace`                 |
| `TotalTableCount` | `TotalTableCount`    | Histogram       | `DatabaseName`, `Namespace` |

### AWS::RedshiftServerless::Workgroup

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                      | OpenTelemetry metric        | Instrument type | Data point attributes                       |
| --------------------------- | --------------------------- | --------------- | ------------------------------------------- |
| `ComputeCapacity`           | `ComputeCapacity`           | Histogram       | `Workgroup`                                 |
| `ComputeSeconds`            | `ComputeSeconds`            | Sum             | `Workgroup`                                 |
| `DatabaseConnections`       | `DatabaseConnections`       | Histogram       | `DatabaseName`, `Workgroup`                 |
| `QueriesCompletedPerSecond` | `QueriesCompletedPerSecond` | Histogram       | `DatabaseName`, `LatencyRange`, `Workgroup` |
| `QueriesFailed`             | `QueriesFailed`             | Sum             | `DatabaseName`, `QueryType`, `Workgroup`    |
| `QueriesQueued`             | `QueriesQueued`             | Histogram       | `DatabaseName`, `QueryType`, `Workgroup`    |
| `QueriesRunning`            | `QueriesRunning`            | Histogram       | `DatabaseName`, `QueryType`, `Workgroup`    |
| `QueriesSucceeded`          | `QueriesSucceeded`          | Sum             | `DatabaseName`, `QueryType`, `Workgroup`    |
| `QueryDuration`             | `QueryDuration`             | Histogram       | `DatabaseName`, `LatencyRange`, `Workgroup` |
| `QueryRuntimeBreakdown`     | `QueryRuntimeBreakdown`     | Sum             | `DatabaseName`, `Workgroup`, `stage`        |
| `UsageLimitAvailable`       | `UsageLimitAvailable`       | Histogram       | `UsageLimitId`, `UsageType`, `Workgroup`    |
| `UsageLimitConsumed`        | `UsageLimitConsumed`        | Histogram       | `UsageLimitId`, `UsageType`, `Workgroup`    |

## AWS/Route53

The `AWS/Route53` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/route53`. All enriched instruments use Delta temporality.

- [AWS::Route53::HealthCheck](#otel-enrichment-aws-route53-aws-route53-healthcheck "#otel-enrichment-aws-route53-aws-route53-healthcheck")

### AWS::Route53::HealthCheck

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                         | OpenTelemetry metric           | Instrument type | Data point attributes     |
| ------------------------------ | ------------------------------ | --------------- | ------------------------- |
| `ChildHealthCheckHealthyCount` | `ChildHealthCheckHealthyCount` | Histogram       | `HealthCheckId`           |
| `ConnectionTime`               | `ConnectionTime`               | Histogram       | `HealthCheckId`, `Region` |
| `HealthCheckPercentageHealthy` | `HealthCheckPercentageHealthy` | Histogram       | `HealthCheckId`           |
| `HealthCheckStatus`            | `HealthCheckStatus`            | Histogram       | `HealthCheckId`           |
| `SSLHandshakeTime`             | `SSLHandshakeTime`             | Histogram       | `HealthCheckId`, `Region` |
| `TimeToFirstByte`              | `TimeToFirstByte`              | Histogram       | `HealthCheckId`, `Region` |

## AWS/Route53Resolver

The `AWS/Route53Resolver` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/route53resolver`. All enriched instruments use Delta temporality.

- [AWS::Route53Resolver::FirewallRuleGroup](#otel-enrichment-aws-route53resolver-aws-route53resolver-firewallrulegroup "#otel-enrichment-aws-route53resolver-aws-route53resolver-firewallrulegroup")
- [AWS::Route53Resolver::ResolverEndpoint](#otel-enrichment-aws-route53resolver-aws-route53resolver-resolverendpoint "#otel-enrichment-aws-route53resolver-aws-route53resolver-resolverendpoint")

### AWS::Route53Resolver::FirewallRuleGroup

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                            | OpenTelemetry metric              | Instrument type | Data point attributes          |
| --------------------------------- | --------------------------------- | --------------- | ------------------------------ |
| `FirewallRuleGroupQueryVolume`    | `FirewallRuleGroupQueryVolume`    | Sum             | `FirewallRuleGroupId`          |
| `FirewallRuleGroupVpcQueryVolume` | `FirewallRuleGroupVpcQueryVolume` | Sum             | `FirewallRuleGroupId`, `VpcId` |

### AWS::Route53Resolver::ResolverEndpoint

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                           | OpenTelemetry metric             | Instrument type | Data point attributes                                           |
| -------------------------------- | -------------------------------- | --------------- | --------------------------------------------------------------- |
| `AverageResponseTime`            | `AverageResponseTime`            | Histogram       | `EndpointId`, `RniId`                                           |
| `CapacityUsage_BETA`             | `CapacityUsage_BETA`             | Histogram       | `EndpointId`, `RniId`                                           |
| `ConntrackUtilization`           | `ConntrackUtilization`           | Histogram       | `EndpointId`, `RniId`                                           |
| `EndpointHealthyENICount`        | `EndpointHealthyENICount`        | Histogram       | `EndpointId`                                                    |
| `EndpointUnhealthyENICount`      | `EndpointUnhealthyENICount`      | Histogram       | `EndpointId`                                                    |
| `FormErrCount`                   | `FormErrCount`                   | Sum             | `EndpointId`, `RniId`                                           |
| `FormErrorQueries`               | `FormErrorQueries`               | Sum             | `EndpointId`, `RniId`                                           |
| `InboundQueryVolume`             | `InboundQueryVolume`             | Sum             | `EndpointId`                                                    |
| `NXDomainCount`                  | `NXDomainCount`                  | Sum             | `EndpointId`, `RniId`                                           |
| `NoErrorCount`                   | `NoErrorCount`                   | Sum             | `EndpointId`, `RniId`                                           |
| `NxDomainQueries`                | `NxDomainQueries`                | Sum             | `EndpointId`, `RniId`                                           |
| `OutboundQueryAggregateVolume`   | `OutboundQueryAggregateVolume`   | Sum             | `EndpointId`                                                    |
| `OutboundQueryVolume`            | `OutboundQueryVolume`            | Sum             | `EndpointId`                                                    |
| `P90ResponseTime`                | `P90ResponseTime`                | Histogram       | • `EndpointID`, `TargetNameServerIP`<br>• `EndpointId`, `RniId` |
| `RefusedCount`                   | `RefusedCount`                   | Sum             | `EndpointId`, `RniId`                                           |
| `RefusedQueries`                 | `RefusedQueries`                 | Sum             | `EndpointId`, `RniId`                                           |
| `ReplyCount`                     | `ReplyCount`                     | Sum             | `EndpointId`, `RniId`                                           |
| `RequestQueries`                 | `RequestQueries`                 | Sum             | `EndpointID`, `TargetNameServerIP`                              |
| `ResolverEndpointCapacityStatus` | `ResolverEndpointCapacityStatus` | Histogram       | `EndpointId`                                                    |
| `ServFailQueries`                | `ServFailQueries`                | Sum             | `EndpointId`, `RniId`                                           |
| `ServfailCount`                  | `ServfailCount`                  | Sum             | `EndpointId`, `RniId`                                           |
| `TimeoutCount`                   | `TimeoutCount`                   | Sum             | `EndpointId`, `RniId`                                           |
| `TimeoutQueries`                 | `TimeoutQueries`                 | Sum             | • `EndpointID`, `TargetNameServerIP`<br>• `EndpointId`, `RniId` |
| `tcpRequestCount`                | `tcpRequestCount`                | Sum             | `EndpointId`, `RniId`                                           |
| `udpRequestCount`                | `udpRequestCount`                | Sum             | `EndpointId`, `RniId`                                           |

## AWS/S3

The `AWS/S3` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/s3`. All enriched instruments use Delta temporality.

- [AWS::S3::Bucket](#otel-enrichment-aws-s3-aws-s3-bucket "#otel-enrichment-aws-s3-aws-s3-bucket")

### AWS::S3::Bucket

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                | OpenTelemetry metric  | Instrument type | Data point attributes       |
| --------------------- | --------------------- | --------------- | --------------------------- |
| `4xxErrors`           | `4xxErrors`           | Sum             | `BucketName`, `FilterId`    |
| `5xxErrors`           | `5xxErrors`           | Sum             | `BucketName`, `FilterId`    |
| `AllRequests`         | `AllRequests`         | Sum             | `BucketName`, `FilterId`    |
| `BucketSizeBytes`     | `BucketSizeBytes`     | Histogram       | `BucketName`, `StorageType` |
| `BytesDownloaded`     | `BytesDownloaded`     | Sum             | `BucketName`, `FilterId`    |
| `BytesUploaded`       | `BytesUploaded`       | Sum             | `BucketName`, `FilterId`    |
| `DeleteRequests`      | `DeleteRequests`      | Sum             | `BucketName`, `FilterId`    |
| `FirstByteLatency`    | `FirstByteLatency`    | Histogram       | `BucketName`, `FilterId`    |
| `GetRequests`         | `GetRequests`         | Sum             | `BucketName`, `FilterId`    |
| `HeadRequests`        | `HeadRequests`        | Sum             | `BucketName`, `FilterId`    |
| `ListRequests`        | `ListRequests`        | Sum             | `BucketName`, `FilterId`    |
| `NumberOfObjects`     | `NumberOfObjects`     | Histogram       | `BucketName`, `StorageType` |
| `PostRequests`        | `PostRequests`        | Sum             | `BucketName`, `FilterId`    |
| `PutRequests`         | `PutRequests`         | Sum             | `BucketName`, `FilterId`    |
| `TotalRequestLatency` | `TotalRequestLatency` | Histogram       | `BucketName`, `FilterId`    |

## AWS/SNS

The `AWS/SNS` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/sns`. All enriched instruments use Delta temporality.

- [AWS::SNS::Topic](#otel-enrichment-aws-sns-aws-sns-topic "#otel-enrichment-aws-sns-aws-sns-topic")

### AWS::SNS::Topic

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                           | OpenTelemetry metric             | Instrument type | Data point attributes |
| -------------------------------- | -------------------------------- | --------------- | --------------------- |
| `NumberOfMessagesPublished`      | `NumberOfMessagesPublished`      | Sum             | `TopicName`           |
| `NumberOfNotificationsDelivered` | `NumberOfNotificationsDelivered` | Sum             | `TopicName`           |
| `NumberOfNotificationsFailed`    | `NumberOfNotificationsFailed`    | Sum             | `TopicName`           |
| `PublishSize`                    | `PublishSize`                    | Histogram       | `TopicName`           |

## AWS/SQS

The `AWS/SQS` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/sqs`. All enriched instruments use Delta temporality.

- [AWS::SQS::Queue](#otel-enrichment-aws-sqs-aws-sqs-queue "#otel-enrichment-aws-sqs-aws-sqs-queue")

### AWS::SQS::Queue

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                               | OpenTelemetry metric                                 | Instrument type | Data point attributes |
| ---------------------------------------------------- | ---------------------------------------------------- | --------------- | --------------------- |
| `ApproximateAgeOfOldestMessage`                      | `ApproximateAgeOfOldestMessage`                      | Histogram       | `QueueName`           |
| `ApproximateAgeOfOldestMessageInQuietGroups`         | `ApproximateAgeOfOldestMessageInQuietGroups`         | Histogram       | `QueueName`           |
| `ApproximateNumberOfGroupsWithInflightMessages`      | `ApproximateNumberOfGroupsWithInflightMessages`      | Histogram       | `QueueName`           |
| `ApproximateNumberOfMessagesDelayed`                 | `ApproximateNumberOfMessagesDelayed`                 | Histogram       | `QueueName`           |
| `ApproximateNumberOfMessagesDelayedInQuietGroups`    | `ApproximateNumberOfMessagesDelayedInQuietGroups`    | Histogram       | `QueueName`           |
| `ApproximateNumberOfMessagesNotVisible`              | `ApproximateNumberOfMessagesNotVisible`              | Histogram       | `QueueName`           |
| `ApproximateNumberOfMessagesNotVisibleInQuietGroups` | `ApproximateNumberOfMessagesNotVisibleInQuietGroups` | Histogram       | `QueueName`           |
| `ApproximateNumberOfMessagesVisible`                 | `ApproximateNumberOfMessagesVisible`                 | Histogram       | `QueueName`           |
| `ApproximateNumberOfMessagesVisibleInQuietGroups`    | `ApproximateNumberOfMessagesVisibleInQuietGroups`    | Histogram       | `QueueName`           |
| `ApproximateNumberOfNoisyGroups`                     | `ApproximateNumberOfNoisyGroups`                     | Histogram       | `QueueName`           |
| `NumberOfDeduplicatedSentMessages`                   | `NumberOfDeduplicatedSentMessages`                   | Sum             | `QueueName`           |
| `NumberOfEmptyReceives`                              | `NumberOfEmptyReceives`                              | Sum             | `QueueName`           |
| `NumberOfMessagesDeleted`                            | `NumberOfMessagesDeleted`                            | Sum             | `QueueName`           |
| `NumberOfMessagesReceived`                           | `NumberOfMessagesReceived`                           | Sum             | `QueueName`           |
| `NumberOfMessagesSent`                               | `NumberOfMessagesSent`                               | Sum             | `QueueName`           |
| `SentMessageSize`                                    | `SentMessageSize`                                    | Histogram       | `QueueName`           |

## AWS/SageMaker

The `AWS/SageMaker` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/sagemaker`. All enriched instruments use Delta temporality.

- [AWS::SageMaker::Endpoint](#otel-enrichment-aws-sagemaker-aws-sagemaker-endpoint "#otel-enrichment-aws-sagemaker-aws-sagemaker-endpoint")
- [AWS::SageMaker::InferenceComponent](#otel-enrichment-aws-sagemaker-aws-sagemaker-inferencecomponent "#otel-enrichment-aws-sagemaker-aws-sagemaker-inferencecomponent")

### AWS::SageMaker::Endpoint

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                       | OpenTelemetry metric                                  | Instrument type | Data point attributes                                                                |
| ---------------------------- | ----------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------ |
| `ConcurrentRequestsPerModel` | `ConcurrentRequestsPerModel`                          | Histogram       | `EndpointName`, `VariantName`                                                        |
| `ConcurrentRequestsPerModel` | `ConcurrentRequestsPerModelByAzByInstanceType`        | Histogram       | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `FirstChunkLatency`          | `FirstChunkLatency`                                   | Histogram       | `EndpointName`, `VariantName`                                                        |
| `FirstChunkLatency`          | `FirstChunkLatencyByAzByInstanceType`                 | Histogram       | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `FirstChunkModelLatency`     | `FirstChunkModelLatency`                              | Histogram       | `EndpointName`, `VariantName`                                                        |
| `FirstChunkModelLatency`     | `FirstChunkModelLatencyByAzByInstanceType`            | Histogram       | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `FirstChunkOverheadLatency`  | `FirstChunkOverheadLatency`                           | Histogram       | `EndpointName`, `VariantName`                                                        |
| `FirstChunkOverheadLatency`  | `FirstChunkOverheadLatencyByAzByInstanceType`         | Histogram       | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `Invocation4XXErrors`        | `Invocation4XXErrors`                                 | Sum             | `EndpointName`, `VariantName`                                                        |
| `Invocation4XXErrors`        | `Invocation4XXErrorsByAzByInstanceType`               | Sum             | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `Invocation4XXErrors`        | `Invocation4XXErrorsByInstanceId`                     | Sum             | `EndpointName`, `InstanceId`, `VariantName`                                          |
| `Invocation4XXErrors`        | `Invocation4XXErrorsForIcByInstanceIdByContainerId`   | Sum             | `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName` |
| `Invocation5XXErrors`        | `Invocation5XXErrors`                                 | Sum             | `EndpointName`, `VariantName`                                                        |
| `Invocation5XXErrors`        | `Invocation5XXErrorsByAzByInstanceType`               | Sum             | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `Invocation5XXErrors`        | `Invocation5XXErrorsByInstanceId`                     | Sum             | `EndpointName`, `InstanceId`, `VariantName`                                          |
| `Invocation5XXErrors`        | `Invocation5XXErrorsForIcByInstanceIdByContainerId`   | Sum             | `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName` |
| `InvocationModelErrors`      | `InvocationModelErrors`                               | Sum             | `EndpointName`, `VariantName`                                                        |
| `InvocationModelErrors`      | `InvocationModelErrorsByAzByInstanceType`             | Sum             | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `InvocationModelErrors`      | `InvocationModelErrorsByInstanceId`                   | Sum             | `EndpointName`, `InstanceId`, `VariantName`                                          |
| `InvocationModelErrors`      | `InvocationModelErrorsForIcByInstanceIdByContainerId` | Sum             | `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName` |
| `Invocations`                | `Invocations`                                         | Sum             | `EndpointName`, `VariantName`                                                        |
| `Invocations`                | `InvocationsByAzByInstanceType`                       | Sum             | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `Invocations`                | `InvocationsByInstanceId`                             | Sum             | `EndpointName`, `InstanceId`, `VariantName`                                          |
| `Invocations`                | `InvocationsForIcByInstanceIdByContainerId`           | Sum             | `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName` |
| `InvocationsPerInstance`     | `InvocationsPerInstance`                              | Sum             | `EndpointName`, `VariantName`                                                        |
| `InvocationsPerInstance`     | `InvocationsPerInstanceByAzByInstanceType`            | Sum             | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `InvocationsPerInstance`     | `InvocationsPerInstanceByInstanceId`                  | Sum             | `EndpointName`, `InstanceId`, `VariantName`                                          |
| `MidStreamErrors`            | `MidStreamErrors`                                     | Sum             | `EndpointName`, `VariantName`                                                        |
| `ModelLatency`               | `ModelLatency`                                        | Histogram       | `EndpointName`, `VariantName`                                                        |
| `ModelLatency`               | `ModelLatencyByAzByInstanceType`                      | Histogram       | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `ModelLatency`               | `ModelLatencyByInstanceId`                            | Histogram       | `EndpointName`, `InstanceId`, `VariantName`                                          |
| `ModelLatency`               | `ModelLatencyForIcByInstanceIdByContainerId`          | Histogram       | `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName` |
| `OverheadLatency`            | `OverheadLatency`                                     | Histogram       | `EndpointName`, `VariantName`                                                        |
| `OverheadLatency`            | `OverheadLatencyByAzByInstanceType`                   | Histogram       | `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`          |
| `OverheadLatency`            | `OverheadLatencyByInstanceId`                         | Histogram       | `EndpointName`, `InstanceId`, `VariantName`                                          |
| `OverheadLatency`            | `OverheadLatencyForIcByInstanceIdByContainerId`       | Histogram       | `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName` |

### AWS::SageMaker::InferenceComponent

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                      | OpenTelemetry metric                           | Instrument type | Data point attributes                                                  |
| --------------------------- | ---------------------------------------------- | --------------- | ---------------------------------------------------------------------- |
| `ConcurrentRequestsPerCopy` | `ConcurrentRequestsPerCopy`                    | Histogram       | `InferenceComponentName`                                               |
| `ConcurrentRequestsPerCopy` | `ConcurrentRequestsPerCopyByAzByInstanceType`  | Histogram       | `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region` |
| `Invocation4XXErrors`       | `Invocation4XXErrorsForIc`                     | Sum             | `InferenceComponentName`                                               |
| `Invocation4XXErrors`       | `Invocation4XXErrorsForIcByAzByInstanceType`   | Sum             | `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region` |
| `Invocation5XXErrors`       | `Invocation5XXErrorsForIc`                     | Sum             | `InferenceComponentName`                                               |
| `Invocation5XXErrors`       | `Invocation5XXErrorsForIcByAzByInstanceType`   | Sum             | `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region` |
| `InvocationModelErrors`     | `InvocationModelErrorsForIc`                   | Sum             | `InferenceComponentName`                                               |
| `InvocationModelErrors`     | `InvocationModelErrorsForIcByAzByInstanceType` | Sum             | `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region` |
| `Invocations`               | `InvocationsForIc`                             | Sum             | `InferenceComponentName`                                               |
| `Invocations`               | `InvocationsForIcByAzByInstanceType`           | Sum             | `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region` |
| `InvocationsPerCopy`        | `InvocationsPerCopy`                           | Sum             | `InferenceComponentName`                                               |
| `InvocationsPerCopy`        | `InvocationsPerCopyByAzByInstanceType`         | Sum             | `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region` |
| `ModelLatency`              | `ModelLatencyForIc`                            | Histogram       | `InferenceComponentName`                                               |
| `ModelLatency`              | `ModelLatencyForIcByAzByInstanceType`          | Histogram       | `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region` |
| `OverheadLatency`           | `OverheadLatencyForIc`                         | Histogram       | `InferenceComponentName`                                               |
| `OverheadLatency`           | `OverheadLatencyForIcByAzByInstanceType`       | Histogram       | `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region` |

## AWS/Scheduler

The `AWS/Scheduler` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/scheduler`. All enriched instruments use Delta temporality.

- [AWS::Scheduler::ScheduleGroup](#otel-enrichment-aws-scheduler-aws-scheduler-schedulegroup "#otel-enrichment-aws-scheduler-aws-scheduler-schedulegroup")

### AWS::Scheduler::ScheduleGroup

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                                                                               | OpenTelemetry metric                                                                 | Instrument type | Data point attributes |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | --------------- | --------------------- |
| `InvocationAttemptCount`                                                             | `InvocationAttemptCount`                                                             | Sum             | `ScheduleGroup`       |
| `InvocationDroppedCount`                                                             | `InvocationDroppedCount`                                                             | Sum             | `ScheduleGroup`       |
| `InvocationThrottleCount`                                                            | `InvocationThrottleCount`                                                            | Sum             | `ScheduleGroup`       |
| `InvocationsFailedToBeSentToDeadLetterCount`                                         | `InvocationsFailedToBeSentToDeadLetterCount`                                         | Sum             | `ScheduleGroup`       |
| `InvocationsFailedToBeSentToDeadLetterCount_AWS.SimpleQueueService.NonExistentQueue` | `InvocationsFailedToBeSentToDeadLetterCount_AWS.SimpleQueueService.NonExistentQueue` | Sum             | `ScheduleGroup`       |
| `InvocationsFailedToBeSentToDeadLetterCount_AccessDenied`                            | `InvocationsFailedToBeSentToDeadLetterCount_AccessDenied`                            | Sum             | `ScheduleGroup`       |
| `InvocationsFailedToBeSentToDeadLetterCount_KMS.AccessDeniedException`               | `InvocationsFailedToBeSentToDeadLetterCount_KMS.AccessDeniedException`               | Sum             | `ScheduleGroup`       |
| `InvocationsSentToDeadLetterCount`                                                   | `InvocationsSentToDeadLetterCount`                                                   | Sum             | `ScheduleGroup`       |
| `TargetErrorCount`                                                                   | `TargetErrorCount`                                                                   | Sum             | `ScheduleGroup`       |
| `TargetErrorThrottledCount`                                                          | `TargetErrorThrottledCount`                                                          | Sum             | `ScheduleGroup`       |

## AWS/Transfer

The `AWS/Transfer` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/transfer`. All enriched instruments use Delta temporality.

- [AWS::Transfer::Connector](#otel-enrichment-aws-transfer-aws-transfer-connector "#otel-enrichment-aws-transfer-aws-transfer-connector")
- [AWS::Transfer::Server](#otel-enrichment-aws-transfer-aws-transfer-server "#otel-enrichment-aws-transfer-aws-transfer-server")

### AWS::Transfer::Connector

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                  | OpenTelemetry metric    | Instrument type | Data point attributes |
| ----------------------- | ----------------------- | --------------- | --------------------- |
| `OutboundFailedMessage` | `OutboundFailedMessage` | Sum             | `ConnectorId`         |
| `OutboundMessage`       | `OutboundMessage`       | Sum             | `ConnectorId`         |

### AWS::Transfer::Server

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                      | OpenTelemetry metric        | Instrument type | Data point attributes |
| --------------------------- | --------------------------- | --------------- | --------------------- |
| `BytesIn`                   | `BytesIn`                   | Sum             | `ServerId`            |
| `BytesOut`                  | `BytesOut`                  | Sum             | `ServerId`            |
| `ConcurrentSessions`        | `ConcurrentSessions`        | Histogram       | `ServerId`            |
| `FilesIn`                   | `FilesIn`                   | Sum             | `ServerId`            |
| `FilesOut`                  | `FilesOut`                  | Sum             | `ServerId`            |
| `InboundFailedMessage`      | `InboundFailedMessage`      | Sum             | `ServerId`            |
| `InboundMessage`            | `InboundMessage`            | Sum             | `ServerId`            |
| `OnUploadExecutionsFailed`  | `OnUploadExecutionsFailed`  | Sum             | `ServerId`            |
| `OnUploadExecutionsStarted` | `OnUploadExecutionsStarted` | Sum             | `ServerId`            |
| `OnUploadExecutionsSuccess` | `OnUploadExecutionsSuccess` | Sum             | `ServerId`            |
| `OutboundFailedMessage`     | `OutboundFailedMessage`     | Sum             | `ServerId`            |

## AWS/TransitGateway

The `AWS/TransitGateway` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/ec2`. All enriched instruments use Delta temporality.

- [AWS::EC2::TransitGateway](#otel-enrichment-aws-transitgateway-aws-ec2-transitgateway "#otel-enrichment-aws-transitgateway-aws-ec2-transitgateway")

### AWS::EC2::TransitGateway

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                         | OpenTelemetry metric           | Instrument type | Data point attributes                                            |
| ------------------------------ | ------------------------------ | --------------- | ---------------------------------------------------------------- |
| `BytesDropCountBlackhole`      | `BytesDropCountBlackhole`      | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `BytesDropCountInternalError`  | `BytesDropCountInternalError`  | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `BytesDropCountNoPolicy`       | `BytesDropCountNoPolicy`       | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `BytesDropCountNoRoute`        | `BytesDropCountNoRoute`        | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `BytesIn`                      | `BytesIn`                      | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `BytesOut`                     | `BytesOut`                     | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `PacketDropCountBlackhole`     | `PacketDropCountBlackhole`     | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `PacketDropCountInternalError` | `PacketDropCountInternalError` | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `PacketDropCountNoPolicy`      | `PacketDropCountNoPolicy`      | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `PacketDropCountNoRoute`       | `PacketDropCountNoRoute`       | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `PacketDropCountTTLExpired`    | `PacketDropCountTTLExpired`    | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `PacketsIn`                    | `PacketsIn`                    | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |
| `PacketsOut`                   | `PacketsOut`                   | Sum             | `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment` |

## AWS/VPN

The `AWS/VPN` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/ec2`. All enriched instruments use Delta temporality.

- [AWS::EC2::VPNConnection](#otel-enrichment-aws-vpn-aws-ec2-vpnconnection "#otel-enrichment-aws-vpn-aws-ec2-vpnconnection")

### AWS::EC2::VPNConnection

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric          | OpenTelemetry metric | Instrument type | Data point attributes |
| --------------- | -------------------- | --------------- | --------------------- |
| `TunnelDataIn`  | `TunnelDataIn`       | Sum             | `VpnId`               |
| `TunnelDataOut` | `TunnelDataOut`      | Sum             | `VpnId`               |
| `TunnelState`   | `TunnelState`        | Histogram       | `VpnId`               |

## AWS/VpcLattice

The `AWS/VpcLattice` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/vpc-lattice`. All enriched instruments use Delta temporality.

- [AWS::VpcLattice::Service](#otel-enrichment-aws-vpclattice-aws-vpclattice-service "#otel-enrichment-aws-vpclattice-aws-vpclattice-service")

### AWS::VpcLattice::Service

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                | OpenTelemetry metric  | Instrument type | Data point attributes         |
| --------------------- | --------------------- | --------------- | ----------------------------- |
| `HTTPCode_2XX_Count`  | `HTTPCode_2XX_Count`  | Sum             | `AvailabilityZone`, `Service` |
| `HTTPCode_3XX_Count`  | `HTTPCode_3XX_Count`  | Sum             | `AvailabilityZone`, `Service` |
| `HTTPCode_4XX_Count`  | `HTTPCode_4XX_Count`  | Sum             | `AvailabilityZone`, `Service` |
| `HTTPCode_5XX_Count`  | `HTTPCode_5XX_Count`  | Sum             | `AvailabilityZone`, `Service` |
| `RequestTime`         | `RequestTime`         | Histogram       | `AvailabilityZone`, `Service` |
| `RequestTimeoutCount` | `RequestTimeoutCount` | Sum             | `AvailabilityZone`, `Service` |
| `TotalRequestCount`   | `TotalRequestCount`   | Sum             | `AvailabilityZone`, `Service` |

## AWS/WorkSpaces

The `AWS/WorkSpaces` namespace is published under the OpenTelemetry instrumentation scope `cloudwatch.aws/workspaces`. All enriched instruments use Delta temporality.

- [AWS::WorkSpaces::Workspace](#otel-enrichment-aws-workspaces-aws-workspaces-workspace "#otel-enrichment-aws-workspaces-aws-workspaces-workspace")
- [AWS::WorkSpaces::WorkspacesPool](#otel-enrichment-aws-workspaces-aws-workspaces-workspacespool "#otel-enrichment-aws-workspaces-aws-workspaces-workspacespool")

### AWS::WorkSpaces::Workspace

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Supported

| Metric                | OpenTelemetry metric  | Instrument type | Data point attributes                                                               |
| --------------------- | --------------------- | --------------- | ----------------------------------------------------------------------------------- |
| `Available`           | `Available`           | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `CPUUsage`            | `CPUUsage`            | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `ConnectionAttempt`   | `ConnectionAttempt`   | Sum             | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `ConnectionFailure`   | `ConnectionFailure`   | Sum             | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `ConnectionSuccess`   | `ConnectionSuccess`   | Sum             | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `InSessionLatency`    | `InSessionLatency`    | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `Maintenance`         | `Maintenance`         | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `MemoryUsage`         | `MemoryUsage`         | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `Restoring`           | `Restoring`           | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `RootVolumeDiskUsage` | `RootVolumeDiskUsage` | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `SessionDisconnect`   | `SessionDisconnect`   | Sum             | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `SessionLaunchTime`   | `SessionLaunchTime`   | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `Stopped`             | `Stopped`             | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `UDPPacketLossRate`   | `UDPPacketLossRate`   | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `Unhealthy`           | `Unhealthy`           | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `UpTime`              | `UpTime`              | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `UserConnected`       | `UserConnected`       | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |
| `UserVolumeDiskUsage` | `UserVolumeDiskUsage` | Histogram       | `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId` |

### AWS::WorkSpaces::WorkspacesPool

- `cloud.resource_id` enrichment: Supported
- `tag.*` enrichment: Not supported

| Metric                            | OpenTelemetry metric              | Instrument type | Data point attributes |
| --------------------------------- | --------------------------------- | --------------- | --------------------- |
| `ActiveUserSessionCapacity`       | `ActiveUserSessionCapacity`       | Histogram       | `WorkSpaces pool ID`  |
| `ActualUserSessionCapacity`       | `ActualUserSessionCapacity`       | Histogram       | `WorkSpaces pool ID`  |
| `AvailableUserSessionCapacity`    | `AvailableUserSessionCapacity`    | Histogram       | `WorkSpaces pool ID`  |
| `DesiredUserSessionCapacity`      | `DesiredUserSessionCapacity`      | Histogram       | `WorkSpaces pool ID`  |
| `InsufficientCapacityError`       | `InsufficientCapacityError`       | Sum             | `WorkSpaces pool ID`  |
| `PendingUserSessionCapacity`      | `PendingUserSessionCapacity`      | Histogram       | `WorkSpaces pool ID`  |
| `UserSessionsCapacityUtilization` | `UserSessionsCapacityUtilization` | Histogram       | `WorkSpaces pool ID`  |
