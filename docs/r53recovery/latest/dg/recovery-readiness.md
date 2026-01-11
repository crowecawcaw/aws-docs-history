# Readiness rules descriptions in ARC

This section lists the readiness rules descriptions for all the types of resources supported by Amazon Application Recovery Controller (ARC). To see a list of the resource types
supported by ARC, see [Resource types and ARN formats
in ARC](recovery-readiness.md "recovery-readiness.md").

You can also view the readiness rules descriptions on the ARC console or by using an API operation, by doing the following:

- To view readiness rules in the console, follow the steps in the following procedure:
  [View readiness rules on the console](#recovery-readiness.list-rules-console "#recovery-readiness.list-rules-console").
- To view readiness rules by using the API, see the [ListRules](../../../recovery-readiness/latest/api/rules.md "../../../recovery-readiness/latest/api/rules.md") operation.

###### Topics

- [Readiness rules in ARC](#recovery-readiness.list-rules "#recovery-readiness.list-rules")
- [View readiness rules on the console](#recovery-readiness.list-rules-console "#recovery-readiness.list-rules-console")

## Readiness rules in ARC

This section lists the set of readiness rules for each resource type that is supported by ARC.

As you look through the rule descriptions, you can see that most of them include the terms **Inspects all**
or **Inspects each**. To understand how these terms explain how a rule works in the context of a readiness
check, and other details about how ARC sets readiness status, see [How readiness rules
determine readiness status](recovery-readiness.md "recovery-readiness.md").

### Readiness rules

ARC audits resources by using the following readiness rules.

**Amazon API Gateway Version 1 stages**

- **ApiGwV1ApiKeyCount**: Inspects all API Gateway stages
  to ensure that they have the same number of API Keys linked
  to them.
- **ApiGwV1ApiKeySource**: Inspects all API Gateway stages
  to ensure that they have the same value for `API Key
Source`.
- **ApiGwV1BasePath**: Inspects all API Gateway stages to ensure that they are linked to the same base path.
- **ApiGwV1BinaryMediaTypes**: Inspects all API Gateway stages to ensure that they support the same binary media types.
- **ApiGwV1CacheClusterEnabled**: Inspects all API Gateway
  stages to ensure that either all have `Cache
Cluster` enabled, or none do.
- **ApiGwV1CacheClusterSize**: Inspects all API Gateway
  stages to ensure that they have the same `Cache Cluster
Size`. If one has a greater value, the others are
  marked NOT READY.
- **ApiGwV1CacheClusterStatus**: Inspects all API Gateway
  stages to ensure that the `Cache Cluster` is in
  the AVAILABLE state.
- **ApiGwV1DisableExecuteApiEndpoint**: Inspects all
  API Gateway stages to ensure that either all have `Execute
API Endpoint` disabled, or none do.
- **ApiGwV1DomainName**: Inspects all API Gateway stages to ensure that they are linked to the same domain name.
- **ApiGwV1EndpointConfiguration**: Inspects all
  API Gateway stages to ensure that they are linked to a domain with
  the same endpoint configuration.
- **ApiGwV1EndpointDomainNameStatus**: Inspects all API Gateway stages to ensure that the domain name that they are linked to is in the AVAILABLE state.
- **ApiGwV1MethodSettings**: Inspects all API Gateway
  stages to ensure that they have the same value for
  `Method Settings`.
- **ApiGwV1MutualTlsAuthentication**: Inspects all
  API Gateway stages to ensure that they have the same value for
  `Mutual TLS Authentication`.
- **ApiGwV1Policy**: Inspects all API Gateway stages to ensure that either all use API level policies, or none do.
- **ApiGwV1RegionalDomainName**: Inspects all API Gateway stages to ensure that they are linked to
  the same Regional domain name. Note: This rule does not affect readiness status.
- **ApiGwV1ResourceMethodConfigs**: Inspects all API Gateway stages to ensure that they have a similar resource hierarchy, including the related configurations.
- **ApiGwV1SecurityPolicy**: Inspects all API Gateway
  stages to ensure that they have the same value for
  `Security Policy`.
- **ApiGwV1Quotas**: Inspects all API Gateway groups to ensure that they conform to quotas (limits) that are managed by Service Quotas.
- **ApiGwV1UsagePlans**: Inspects all API Gateway stages to ensure that they are linked to `Usage Plans` with the same configuration.

**Amazon API Gateway Version 2 stages**

- **ApiGwV2ApiKeySelectionExpression**: Inspects all
  API Gateway stages ensure that they have the same value for
  `API Key Selection Expression`.
- **ApiGwV2ApiMappingSelectionExpression**: Inspects
  all API Gateway stages to ensure that they have the same value for
  `API Mapping Selection Expression`.
- **ApiGwV2CorsConfiguration**: Inspects all API Gateway
  stages to ensure that they have the same CORS related
  configuration.
- **ApiGwV2DomainName**: Inspects all API Gateway stages to ensure that they are linked to the same domain name.
- **ApiGwV2DomainNameStatus**: Inspects all API Gateway stages to ensure that the domain name is in the AVAILABLE state.
- **ApiGwV2EndpointType**: Inspects all API Gateway stages
  to ensure that they have the same value for
  `Endpoint Type`.
- **ApiGwV2Quotas**: Inspects all API Gateway groups to ensure that they conform to quotas (limits) that are managed by Service Quotas.
- **ApiGwV2MutualTlsAuthentication**: Inspects all
  API Gateway stages to ensure that they have the same value for
  `Mutual TLS Authentication`.
- **ApiGwV2ProtocolType**: Inspects all API Gateway stages
  to ensure that they have the same value for `Protocol
Type`.
- **ApiGwV2RouteConfigs**: Inspects all API Gateway stages
  to ensure that they have the same hierarchy of routes with
  the same configuration.
- **ApiGwV2RouteSelectionExpression**: Inspects all
  API Gateway stages to ensure that they have the same value for
  `Route Selection Expression`.
- **ApiGwV2RouteSettings**: Inspects all API Gateway
  stages to ensure that they have the same value for
  `Default Route Settings`.
- **ApiGwV2SecurityPolicy**: Inspects all API Gateway
  stages to ensure that they have the same value for
  `Security Policy`.
- **ApiGwV2StageVariables**: Inspects all API Gateway
  stages to ensure that they all have the same `Stage
Variables` as the other stages.
- **ApiGwV2ThrottlingBurstLimit**: Inspects all
  API Gateway stages to ensure that they have the same value for
  `Throttling Burst Limit`.
- **ApiGwV2ThrottlingRateLimit**: Inspects all API Gateway
  stages to ensure that they have the same value for
  `Throttling Rate Limit`.

**Amazon Aurora clusters**

- **RdsClusterStatus**: Inspects each Aurora cluster to ensure that it has a status of either `AVAILABLE` or `BACKING-UP`.
- **RdsEngineMode**: Inspects all Aurora clusters to
  ensure that they have the same value for `Engine
Mode`.
- **RdsEngineVersion**: Inspects all Aurora clusters
  to ensure that they have the same value for `Major
Version`.
- **RdsGlobalReplicaLag**: Inspects each Aurora
  cluster to ensure that it has a `Global Replica
Lag` of less than 30 seconds.
- **RdsNormalizedCapacity**: Inspects all Aurora clusters to ensure that they have a normalized capacity within 15% of the maximum in the resource set.
- **RdsInstanceType**: Inspects all Aurora clusters to ensure that they have the same instance types.
- **RdsQuotas**: Inspects all Aurora clusters to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Auto Scaling groups**

- **AsgMinSizeAndMaxSize**: Inspects all Auto Scaling groups to ensure that they have the same minimum and maximum group sizes.
- **AsgAZCount**: Inspects all Auto Scaling groups to ensure that they have the same number of Availability Zones.
- **AsgInstanceTypes**: Inspects all Auto Scaling groups to ensure that they have the same instance
  types. Note: This rule does not affect readiness status.
- **AsgInstanceSizes**: Inspects all Auto Scaling groups to ensure that they have the same instance sizes.
- **AsgNormalizedCapacity**: Inspects all Auto Scaling groups to ensure that they have a normalized capacity within 15% of the maximum in the resource set.
- **AsgQuotas**: Inspects all Auto Scaling groups to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**CloudWatch alarms**

- **CloudWatchAlarmState**: Inspects CloudWatch alarms to ensure that each is not in the `ALARM` or `INSUFFICIENT_DATA` state.

**Customer gateways**

- **CustomerGatewayIpAddress**: Inspects all customer gateways to ensure that they have the same IP address.
- **CustomerGatewayState**: Inspects customer gateways to ensure that each is in the `AVAILABLE` state.
- **CustomerGatewayVPNType**: Inspects all customer gateways to ensure that they have the same VPN type.

**DNS target resources**

- **DnsTargetResourceHostedZoneConfigurationRule**: Inspects all DNS target resources to ensure that they have the same Amazon Route 53 hosted zone ID and that
  each hosted zone is not private. Note: This rule does not affect readiness status.
- **DnsTargetResourceRecordSetConfigurationRule**: Inspects all DNS target resources to ensure that they have the same resource record cache time to
  live (TTL) and that the TTLs are less than or equal to 300.
- **DnsTargetResourceRoutingRule**: Inspects each DNS target resource associated with an alias resource record set to ensure that it routes
  traffic to the DNS name configured on the target resource. Note: This rule does not affect readiness status.
- **DnsTargetResourceHealthCheckRule**: Inspects all DNS target resources to ensure that health checks are associated with their resource record sets
  when appropriate and not otherwise. Note: This rule does not affect readiness status.

**Amazon DynamoDB tables**

- **DynamoConfiguration**: Inspects all DynamoDB tables to ensure that they have the same keys, attributes, server-side encryption, and streams configurations.
- **DynamoTableStatus**: Inspects each DynamoDB table
  to ensure that it has a status of ACTIVE.
- **DynamoCapacity**: Inspects all DynamoDB tables to ensure that their provisioned read capacities and write capacities are within 20% of the maximum capacities in the resource set.
- **DynamoPeakRcuWcu**: Inspects each DynamoDB table to ensure that it has had similar peak traffic to the other tables, to assure provisioned capacity.
- **DynamoGsiPeakRcuWcu**: Inspects each DynamoDB table to ensure that it has had similar maximum read and write capacity to the other tables, to assure provisioned capacity.
- **DynamoGsiConfig**: Inspects all DynamoDB tables that have global secondary indexes to ensure that the tables use the same index, key schema, and projection.
- **DynamoGsiStatus**: Inspects all DynamoDB tables that have global secondary indexes to ensure that the global secondary indexes have an ACTIVE status.
- **DynamoGsiCapacity**: Inspects all DynamoDB tables that have global secondary indexes to ensure that the tables have provisioned GSI read capacities and GSI write capacities within 20% of the maximum capacities in the resource set.
- **DynamoReplicationLatency**: Inspects all DynamoDB tables that are global tables to ensure that they have the same replication latency.
- **DynamoAutoScalingConfiguration**: Inspects all DynamoDB tables that have Auto Scaling enabled to ensure that they have the same minimum, maximum, and target read and write capacities.
- **DynamoQuotas**: Inspects all DynamoDB tables to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**ELB (Classic Load Balancers)**

- **ElbV1CheckAzCount**: Inspects each Classic Load Balancer to ensure that it is attached to only one Availability Zone. Note: This rule does not affect readiness status.
- **ElbV1AnyInstances**: Inspects all Classic Load Balancers to ensure that they have at least one EC2 instance.
- **ElbV1AnyInstancesHealthy**: Inspects all Classic Load Balancers to ensure that they have at least one healthy EC2 instance.
- **ElbV1Scheme**: Inspects all Classic Load Balancers to ensure that they have the same load balancer scheme.
- **ElbV1HealthCheckThreshold**: Inspects all Classic Load Balancers to ensure that they have the same health check threshold value.
- **ElbV1HealthCheckInterval**: Inspects all Classic Load Balancers to ensure that they have the same health check interval value.
- **ElbV1CrossZoneRoutingEnabled**: Inspects all Classic Load Balancers to ensure that they have the same value for cross-zone load balancing (ENABLED or DISABLED).
- **ElbV1AccessLogsEnabledAttribute**: Inspects all Classic Load Balancers to ensure that they have the same value for access logs (ENABLED or DISABLED).
- **ElbV1ConnectionDrainingEnabledAttribute**: Inspects all Classic Load Balancers to ensure that they have the same value for connection draining (ENABLED or DISABLED).
- **ElbV1ConnectionDrainingTimeoutAttribute**: Inspects all Classic Load Balancers to ensure that they have the same connection draining timeout value.
- **ElbV1IdleTimeoutAttribute**: Inspects all Classic Load Balancers to ensure that they have the same value for idle timeout.
- **ElbV1ProvisionedCapacityLcuCount**: Inspects all
  Classic Load Balancers with a provisioned LCU greater than
  10 to ensure that they are within 20% of the highest
  provisioned LCU in the resource set.
- **ElbV1ProvisionedCapacityStatus**: Inspects the provisioned capacity status on each Classic Load Balancer to ensure that it does not have a value of DISABLED or PENDING.

**Amazon EBS volumes**

- **EbsVolumeEncryption**: Inspects all EBS volumes to ensure that they have the same value for encryption (ENABLED or DISABLED).
- **EbsVolumeEncryptionDefault**: Inspects all EBS volumes to ensure that they have the same value for encryption by default (ENABLED or DISABLED).
- **EbsVolumeIops**: Inspects all EBS volumes to ensure that they have the same input/output operations per second (IOPS).
- **EbsVolumeKmsKeyId**: Inspects all EBS volumes to ensure that they have the same default AWS KMS key ID.
- **EbsVolumeMultiAttach**: Inspects all EBS volumes to ensure that they have the same value for multi-attach (ENABLED or DISABLED).
- **EbsVolumeQuotas**: Inspects all EBS volumes to ensure that they conform to quotas (limits) that are set by Service Quotas.
- **EbsVolumeSize**: Inspects all EBS volumes to ensure that they have the same readable size.
- **EbsVolumeState**: Inspects all EBS volumes to ensure that they have the same volume state.
- **EbsVolumeType**: Inspects all EBS volumes to ensure that they have the same volume type.

**AWS Lambda functions**

- **LambdaMemorySize**: Inspects all Lambda functions to ensure that they have the same memory size. If one has more memory, the others are marked `NOT READY`.
- **LambdaFunctionTimeout**: Inspects all Lambda functions to ensure that they have the same timeout value. If one has a greater value, the others are marked `NOT READY`.
- **LambdaFunctionRuntime**: Inspects all Lambda
  functions to ensure that they all have the same
  runtime.
- **LambdaFunctionReservedConcurrentExecutions**:
  Inspects all Lambda functions to ensure that they all have
  the same value for `Reserved Concurrent
Executions`. If one has a greater value, the
  others are marked `NOT READY`.
- **LambdaFunctionDeadLetterConfig**: Inspects all
  Lambda functions to ensure that they either all have a
  `Dead Letter Config` defined, or that none of
  them do.
- **LambdaFunctionProvisionedConcurrencyConfig**:
  Inspects all Lambda functions to ensure that they have the
  same value for `Provisioned Concurrency`.
- **LambdaFunctionSecurityGroupCount**: Inspects all
  Lambda functions to ensure that they have the same value for
  `Security Groups`.
- **LambdaFunctionSubnetIdCount**: Inspects all
  Lambda functions to ensure that they have the same value for
  `Subnet Ids`.
- **LambdaFunctionEventSourceMappingMatch**:
  Inspects all Lambda functions to ensure that all of the
  chosen `Event Source Mapping` properties match
  between them.
- **LambdaFunctionLimitsRule**: Inspects all Lambda functions to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Network Load Balancers and Application Load Balancers**

- **ElbV2CheckAzCount**: Inspects each Network Load Balancer to ensure that it is attached to only one
  Availability Zone. Note: This rule does not affect readiness status.
- **ElbV2TargetGroupsCanServeTraffic**: Inspects each Network Load Balancer and Application Load Balancer to ensure that it has at least one healthy Amazon EC2 instance.
- **ElbV2State**: Inspects each Network Load Balancer and Application Load Balancer to
  ensure that it is in the `ACTIVE` state.
- **ElbV2IpAddressType**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same IP address types.
- **ElbV2Scheme**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same scheme.
- **ElbV2Type**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same type.
- **ElbV2S3LogsEnabled**: Inspects all Network Load Balancers and
  Application Load Balancers to ensure that they have the same value for Amazon S3
  server access logs (ENABLED or DISABLED).
- **ElbV2DeletionProtection**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for deletion protection (ENABLED or DISABLED).
- **ElbV2IdleTimeoutSeconds**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for idle time seconds.
- **ElbV2HttpDropInvalidHeaders**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for HTTP drop invalid headers.
- **ElbV2Http2Enabled**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for HTTP2 (ENABLED or DISABLED).
- **ElbV2CrossZoneEnabled**: Inspects all Network Load Balancers and Application Load Balancers to ensure that they have the same value for cross-zone load balancing (ENABLED or DISABLED).
- **ElbV2ProvisionedCapacityLcuCount**: Inspects all Network Load Balancers and Application Load Balancers with a provisioned LCU greater than 10 to ensure that they are within 20% of the highest provisioned LCU in the resource set.
- **ElbV2ProvisionedCapacityEnabled**: Inspects all Network Load Balancers and Application Load Balancers provisioned capacity status to ensure that it does not have a value of DISABLED or PENDING.

**Amazon MSK clusters**

- **MskClusterClientSubnet**: Inspects each MSK cluster to ensure that it has only two or only three client subnets.
- **MskClusterInstanceType**: Inspects all MSK clusters to ensure that they have the same Amazon EC2 instance type.
- **MskClusterSecurityGroups**: Inspects all MSK clusters to ensure that they have the same security groups.
- **MskClusterStorageInfo**: Inspects all MSK clusters to ensure that they have the same EBS storage volume size. If one has a greater value, the others are marked NOT READY.
- **MskClusterACMCertificate**: Inspects all MSK clusters to ensure that they have the same list of client authorization certificate ARNs.
- **MskClusterServerProperties**: Inspects all MSK
  clusters to ensure that they have the same value for
  `Current Broker Software Info`.
- **MskClusterKafkaVersion**: Inspects all MSK clusters to ensure that they have the same Kafka version.
- **MskClusterEncryptionInTransitInCluster**:
  Inspects all MSK clusters to ensure that they have the same
  value for `Encryption In Transit In
Cluster`.
- **MskClusterEncryptionInClientBroker**: Inspects
  all MSK clusters to ensure that they have the same value for
  `Encryption In Transit Client Broker`.
- **MskClusterEnhancedMonitoring**: Inspects all MSK
  clusters to ensure that they have the same value for
  `Enhanced Monitoring`.
- **MskClusterOpenMonitoringInJmx**: Inspects all
  MSK clusters to ensure that they have the same value for
  `Open Monitoring JMX Exporter`.
- **MskClusterOpenMonitoringInNode**: Inspects all
  MSK clusters to ensure that they have the same value for
  `Open Monitoring Not Exporter.`
- **MskClusterLoggingInS3**: Inspects all MSK
  clusters to ensure that they have the same value for
  `Is Logging in S3`.
- **MskClusterLoggingInFirehose**: Inspects all MSK
  clusters to ensure that they have the same value for
  `Is Logging In Firehose`.
- **MskClusterLoggingInCloudWatch**: Inspects all
  MSK clusters to ensure that they have the same value for
  `Is Logging Available In CloudWatch
Logs`.
- **MskClusterNumberOfBrokerNodes**: Inspects all
  MSK clusters to ensure they have the same value for
  `Number of Broker Nodes`. If one has a
  greater value, the others are marked NOT READY.
- **MskClusterState**: Inspects each MSK cluster to ensure that it is in an ACTIVE state.
- **MskClusterLimitsRule**: Inspects all Lambda functions to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Amazon Route 53 health checks**

- **R53HealthCheckType**: Inspects each Route 53 health check to ensure that it is not of type CALCULATED and that all checks are of the same type.
- **R53HealthCheckDisabled**: Inspects each Route 53
  health check to ensure that it does not have a DISABLED
  state.
- **R53HealthCheckStatus**: Inspects each Route 53 health check to ensure that it has a SUCCESS status.
- **R53HealthCheckRequestInterval**: Inspects all
  Route 53 health checks to ensure that they all have the same
  value for `Request Interval`.
- **R53HealthCheckFailureThreshold**: Inspects all
  Route 53 health checks to ensure that they all have the same
  value for `Failure Threshold.`
- **R53HealthCheckEnableSNI**: Inspects all Route 53
  health checks to ensure that they all have the same value
  for `Enable SNI.`
- **R53HealthCheckSearchString**: Inspects all Route
  53 health checks to ensure that they all have the same value
  for `Search String.`
- **R53HealthCheckRegions**: Inspects all Route 53
  health checks to ensure that they all have the same list of
  AWS Regions.
- **R53HealthCheckMeasureLatency**: Inspects all
  Route 53 health checks to ensure that they all have the same
  value for `Measure Latency`.
- **R53HealthCheckInsufficientDataHealthStatus**:
  Inspects all Route 53 health checks to ensure that they all
  have the same value for `Insufficient Data Health
Status`.
- **R53HealthCheckInverted**: Inspects all Route 53
  health checks to ensure that they are all Inverted, or are
  all not Inverted.
- **R53HealthCheckResourcePath**: Inspects all Route
  53 health checks to ensure that they all have the same value
  for `Resource Path`.
- **R53HealthCheckCloudWatchAlarm**: Inspects all Route 53 health checks to ensure that the CloudWatch alarms associated with them have the same settings and configurations.

**Amazon SNS subscriptions**

- **SnsSubscriptionProtocol**: Inspects all SNS subscriptions to ensure that they have the same protocol.
- **SnsSubscriptionSqsLambdaEndpoint**: Inspects all SNS subscriptions that have Lambda or SQS endpoints to ensure that they have different endpoints.
- **SnsSubscriptionNonAwsEndpoint**: Inspects all SNS subscriptions that have a non-AWS service endpoint type, for example, email, to ensure that the
  subscriptions have the same endpoint.
- **SnsSubscriptionPendingConfirmation**: Inspects all SNS subscriptions to ensure that they have the same value for 'Pending Confirmations'.
- **SnsSubscriptionDeliveryPolicy**: Inspects all SNS subscriptions that use HTTP/S to ensure that they have the same value for 'Effective Delivery Period'.
- **SnsSubscriptionRawMessageDelivery**: Inspects all SNS subscriptions to ensure that they have the same value for 'Raw Message Delivery'.
- **SnsSubscriptionFilter**: Inspects all SNS subscriptions to ensure that they have the same value for 'Filter Policy'.
- **SnsSubscriptionRedrivePolicy**: Inspects all SNS subscriptions to ensure that they have the same value for 'Redrive Policy'.
- **SnsSubscriptionEndpointEnabled**: Inspects all SNS subscriptions to ensure that they have the same value for 'Endpoint Enabled'.
- **SnsSubscriptionLambdaEndpointValid**: Inspects all SNS subscriptions that have Lambda endpoints to ensure that they have valid Lambda endpoints.
- **SnsSubscriptionSqsEndpointValidRule**: Inspects all SNS subscriptions that use SQS endpoints to ensure that they have valid SQS endpoints.
- **SnsSubscriptionQuotas**: Inspects all SNS subscriptions to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Amazon SNS topics**

- **SnsTopicDisplayName**: Inspects all SNS topics
  to ensure that they have the same value for `Display
Name`.
- **SnsTopicDeliveryPolicy**: Inspects all SNS topics that have HTTPS subscribers to ensure that they have the same `EffectiveDeliveryPolicy`.
- **SnsTopicSubscription**: Inspects all SNS topics to ensure that they have the same number of subscribers for each of their protocols.
- **SnsTopicAwsKmsKey**: Inspects all SNS topics to
  ensure that all of the topics or none of the topics have an
  AWS KMS key.
- **SnsTopicQuotas**: Inspects all SNS topics to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Amazon SQS queues**

- **SqsQueueType**: Inspects all SQS queues to
  ensure that they are all the same value for
  `Type`.
- **SqsQueueDelaySeconds**: Inspects all SQS queues
  to ensure that they all have the same value for `Delay
Seconds`.
- **SqsQueueMaximumMessageSize**: Inspects all SQS
  queues to ensure that they all have the same value for
  `Maximum Message Size`.
- **SqsQueueMessageRetentionPeriod**: Inspects all
  SQS queues to ensure that they all have the same value for
  `Message Retention Period`.
- **SqsQueueReceiveMessageWaitTimeSeconds**:
  Inspects all SQS queues to ensure that they all have the
  same value for `Receive Message Wait Time
Seconds`.
- **SqsQueueRedrivePolicyMaxReceiveCount**: Inspects
  all SQS queues to ensure that they all have the same value
  for `Redrive Policy Max Receive Count`.
- **SqsQueueVisibilityTimeout**: Inspects all SQS
  queues to ensure that they all have the same value for
  `Visibility Timeout`.
- **SqsQueueContentBasedDeduplication**: Inspects
  all SQS queues to ensure that they all have the same value
  for `Content-Based Deduplication`.
- **SqsQueueQuotas**: Inspects all SQS queues to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Amazon VPCs**

- **VpcCidrBlock**: Inspects all VPCs to ensure that they all have the same value for CIDR block network size.
- **VpcCidrBlocksSameProtocolVersion**: Inspects all VPCs that have the same CIDR blocks to ensure that they have the same value for Internet Stream Protocol version number.
- **VpcCidrBlocksStateInAssociationSets**: Inspects all CIDR block association sets for all VPCs to ensure that they all have CIDR blocks that are in an `ASSOCIATED` state.
- **VpcIpv6CidrBlocksStateInAssociationSets**: Inspects all CIDR block association sets for all VPCs to ensure that they all have CIDR blocks with the same number of addresses.
- **VpcCidrBlocksInAssociationSets**: Inspects all CIDR block association sets for all VPCs to ensure that they all have the same size.
- **VpcIpv6CidrBlocksInAssociationSets**: Inspects all IPv6 CIDR block association sets for all VPCs to ensure that they have the same size.
- **VpcState**: Inspects each VPC to ensure that it is in an `AVAILABLE` state.
- **VpcInstanceTenancy**: Inspects all VPCs to
  ensure that they all have the same value for `Instance
Tenancy`.
- **VpcIsDefault**: Inspects all VPCs to ensure that
  they have the same value for `Is Default.`
- **VpcSubnetState**: Inspects each VPC subnet to ensure that it is in an AVAILABLE state.
- **VpcSubnetAvailableIpAddressCount**: Inspects
  each VPC subnet to ensure that it has an available IP
  address count greater than zero.
- **VpcSubnetCount**: Inspects all VPC subnets to ensure that they have the same number of subnets.
- **VpcQuotas**: Inspects all VPC subnets to ensure that they conform to quotas (limits) that are managed by Service Quotas.

**Site-to-Site VPN connections**

- **VpnConnectionsRouteCount**: Inspects all VPN connections to ensure that they have at least one route, and also the same number of routes.
- **VpnConnectionsEnableAcceleration**: Inspects all
  VPN connections to ensure that they have the same value for
  `Enable Accelerations`.
- **VpnConnectionsStaticRoutesOnly**: Inspects all
  VPN connections to ensure that they have the same value for
  `Static Routes Only.`
- **VpnConnectionsCategory**: Inspects all VPN
  connections to ensure that they have a category of
  `VPN`.
- **VpnConnectionsCustomerConfiguration**: Inspects
  all VPN connections to ensure that they have the same value
  for `Customer Gateway Configuration`.
- **VpnConnectionsCustomerGatewayId**: Inspects each VPN connection to ensure that it has a customer gateway attached.
- **VpnConnectionsRoutesState**: Inspects all VPN connections to ensure that they are in an `AVAILABLE` state.
- **VpnConnectionsVgwTelemetryStatus**: Inspects each VPN connection to ensure that it has a VGW status of `UP`.
- **VpnConnectionsVgwTelemetryIpAddress**: Inspects each VPN connection to ensure that it has a different outside IP address for each VGW telemetry.
- **VpnConnectionsTunnelOptions**: Inspects all VPN connections to ensure that they have the same tunnel options.
- **VpnConnectionsRoutesCidr**: Inspects all VPN connections to ensure that they have the same destination CIDR blocks.
- **VpnConnectionsInstanceType**: Inspects all VPN
  connections to ensure that they have the same `Instance
Type`.

**Site-to-Site VPN gateways**

- **VpnGatewayState**: Inspects all VPN gateways to ensure that they are in an AVAILABLE state.
- **VpnGatewayAsn**: Inspects all VPN gateways to ensure that they have the same ASN.
- **VpnGatewayType**: Inspects all VPN gateways to ensure that they have the same type.
- **VpnGatewayAttachment**: Inspects all VPN gateways to ensure that they have the same attachment configurations.

## View readiness rules on the console

You can view readiness rules on the AWS Management Console, listed by each resource type.

## To view readiness rules on the console

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Readiness check**.
3. Under **Resource type**, choose the resource type that you want to view the rules for.
