

# Supported metrics for resource tags for telemetry
<a name="SupportedMetricsForResourceTagsForTelemetry"></a>

The following sections list the metrics that CloudWatch enriches with AWS resource tags, grouped by namespace. For each namespace, the supported resource types are listed, with a table of metrics and the dimensions you can use with each.

CloudWatch treats each unique combination of dimensions as a separate metric. In the following tables, each bullet in the Dimensions column is a combination of dimensions that are published together.

## AWS/AOSS
<a name="supported-metrics-ns-aws-aoss"></a>

The `AWS/AOSS` namespace includes enriched metrics for the following resource types.
+ [AWS::OpenSearchServerless::Collection](#supported-metrics-aws-aoss-aws-opensearchserverless-collection)

### AWS::OpenSearchServerless::Collection
<a name="supported-metrics-aws-aoss-aws-opensearchserverless-collection"></a>


| Metric | Dimensions | 
| --- | --- | 
| 2xx | + `ClientId`, `CollectionId`, `CollectionName` | 
| 3xx | + `ClientId`, `CollectionId`, `CollectionName` | 
| 4xx | + `ClientId`, `CollectionId`, `CollectionName` | 
| 5xx | + `ClientId`, `CollectionId`, `CollectionName` | 
| ActiveCollection | + `ClientId`, `CollectionId`, `CollectionName` | 
| ActiveCollection-Shadow | + `ClientId`, `CollectionId`, `CollectionName` | 
| AutoOptimizeJob | + `ClientId`, `CollectionId`, `CollectionName` | 
| IngestionDataRate-Shadow | + `ClientId`, `CollectionId`, `CollectionName` | 
| IngestionDocumentErrors-Shadow | + `ClientId`, `CollectionId`, `CollectionName` | 
| IngestionDocumentRate-Shadow | + `ClientId`, `CollectionId`, `CollectionName` | 
| IngestionRequestErrors | + `ClientId`, `CollectionId`, `CollectionName` | 
| IngestionRequestErrors-Shadow | + `ClientId`, `CollectionId`, `CollectionName` | 
| IngestionRequestLatency | + `ClientId`, `CollectionId`, `CollectionName` | 
| IngestionRequestRate | + `ClientId`, `CollectionId`, `CollectionName` | 
| IngestionRequestRate-Shadow | + `ClientId`, `CollectionId`, `CollectionName` | 
| IngestionRequestSuccess | + `ClientId`, `CollectionId`, `CollectionName` | 
| IngestionRequestSuccess-Shadow | + `ClientId`, `CollectionId`, `CollectionName` | 
| KNNRemoteIndexBuildFailureCount | + `ClientId`, `CollectionId`, `CollectionName` | 
| KNNRemoteIndexBuildSuccessCount | + `ClientId`, `CollectionId`, `CollectionName` | 
| KNNRemoteIndexBuildTime | + `ClientId`, `CollectionId`, `CollectionName` | 
| SearchRequestErrors-Shadow | + `ClientId`, `CollectionId`, `CollectionName` | 
| SearchRequestLatency | + `ClientId`, `CollectionId`, `CollectionName` | 
| SearchRequestRate | + `ClientId`, `CollectionId`, `CollectionName` | 
| SearchRequestRate-Shadow | + `ClientId`, `CollectionId`, `CollectionName` | 
| SemanticSearchOCU | + `AwsAccountId`, `CollectionId`<br />+ `ClientId`, `CollectionId`, `CollectionName` | 

## AWS/ApiGateway
<a name="supported-metrics-ns-aws-apigateway"></a>

The `AWS/ApiGateway` namespace includes enriched metrics for the following resource types.
+ [AWS::ApiGatewayV2::Api](#supported-metrics-aws-apigateway-aws-apigatewayv2-api)

### AWS::ApiGatewayV2::Api
<a name="supported-metrics-aws-apigateway-aws-apigatewayv2-api"></a>


| Metric | Dimensions | 
| --- | --- | 
| 4xx | + `ApiId`<br />+ `ApiId`, `Method`, `Resource`, `Stage` | 
| 5xx | + `ApiId`<br />+ `ApiId`, `Method`, `Resource`, `Stage` | 
| ClientError | + `ApiId`<br />+ `ApiId`, `Route`, `Stage` | 
| ConnectCount | + `ApiId`<br />+ `ApiId`, `Route`, `Stage` | 
| Count | + `ApiId`<br />+ `ApiId`, `Method`, `Resource`, `Stage` | 
| DataProcessed | + `ApiId`<br />+ `ApiId`, `Method`, `Resource`, `Stage` | 
| ExecutionError | + `ApiId`<br />+ `ApiId`, `Route`, `Stage` | 
| IntegrationError | + `ApiId`<br />+ `ApiId`, `Route`, `Stage` | 
| IntegrationLatency | + `ApiId`<br />+ `ApiId`, `Method`, `Resource`, `Stage`<br />+ `ApiId`, `Route`, `Stage` | 
| Latency | + `ApiId`<br />+ `ApiId`, `Method`, `Resource`, `Stage` | 
| MessageCount | + `ApiId`<br />+ `ApiId`, `Route`, `Stage` | 

## AWS/AppFlow
<a name="supported-metrics-ns-aws-appflow"></a>

The `AWS/AppFlow` namespace includes enriched metrics for the following resource types.
+ [AWS::AppFlow::Flow](#supported-metrics-aws-appflow-aws-appflow-flow)

### AWS::AppFlow::Flow
<a name="supported-metrics-aws-appflow-aws-appflow-flow"></a>


| Metric | Dimensions | 
| --- | --- | 
| FlowExecutionRecordsProcessed | + `FlowName` | 
| FlowExecutionTime | + `FlowName` | 
| FlowExecutionsFailed | + `FlowName` | 
| FlowExecutionsStarted | + `FlowName` | 
| FlowExecutionsSucceeded | + `FlowName` | 

## AWS/AppSync
<a name="supported-metrics-ns-aws-appsync"></a>

The `AWS/AppSync` namespace includes enriched metrics for the following resource types.
+ [AWS::AppSync::GraphQLApi](#supported-metrics-aws-appsync-aws-appsync-graphqlapi)

### AWS::AppSync::GraphQLApi
<a name="supported-metrics-aws-appsync-aws-appsync-graphqlapi"></a>


| Metric | Dimensions | 
| --- | --- | 
| 4XXError | + `GraphQLAPIId` | 
| 5XXError | + `GraphQLAPIId` | 
| ActiveConnections | + `GraphQLAPIId` | 
| ActiveSubscriptions | + `GraphQLAPIId` | 
| CacheHit | + `GraphQLAPIId`, `Resolver` | 
| CacheMiss | + `GraphQLAPIId`, `Resolver` | 
| ConnectClientError | + `GraphQLAPIId` | 
| ConnectRequests | + `GraphQLAPIId` | 
| ConnectServerError | + `GraphQLAPIId` | 
| ConnectSuccess | + `GraphQLAPIId` | 
| ConnectionDuration | + `GraphQLAPIId` | 
| DisconnectClientError | + `GraphQLAPIId` | 
| DisconnectServerError | + `GraphQLAPIId` | 
| DisconnectSuccess | + `GraphQLAPIId` | 
| GraphQLError | + `DataSource`, `GraphQLAPIId`<br />+ `GraphQLAPIId`, `Operation`<br />+ `GraphQLAPIId`, `Resolver` | 
| InboundMessageDelayed | + `GraphQLAPIId` | 
| InboundMessageDropped | + `GraphQLAPIId` | 
| InboundMessageError | + `GraphQLAPIId` | 
| InboundMessageFailure | + `GraphQLAPIId` | 
| InboundMessageSuccess | + `GraphQLAPIId` | 
| InvalidationRequestDropped | + `GraphQLAPIId` | 
| InvalidationRequestError | + `GraphQLAPIId` | 
| InvalidationRequestFailure | + `GraphQLAPIId` | 
| InvalidationRequestSuccess | + `GraphQLAPIId` | 
| InvalidationSuccess | + `GraphQLAPIId` | 
| Latency | + `DataSource`, `GraphQLAPIId`<br />+ `GraphQLAPIId`<br />+ `GraphQLAPIId`, `Resolver` | 
| OutboundMessages | + `GraphQLAPIId` | 
| PublishDataMessageClientError | + `GraphQLAPIId` | 
| PublishDataMessageServerError | + `GraphQLAPIId` | 
| PublishDataMessageSize | + `GraphQLAPIId` | 
| PublishDataMessageSuccess | + `GraphQLAPIId` | 
| Requests | + `DataSource`, `GraphQLAPIId`<br />+ `GraphQLAPIId`, `Operation`<br />+ `GraphQLAPIId`, `Resolver` | 
| SubscribeClientError | + `GraphQLAPIId` | 
| SubscribeServerError | + `GraphQLAPIId` | 
| SubscribeSuccess | + `GraphQLAPIId` | 
| UnsubscribeClientError | + `GraphQLAPIId` | 
| UnsubscribeServerError | + `GraphQLAPIId` | 
| UnsubscribeSuccess | + `GraphQLAPIId` | 

## AWS/ApplicationELB
<a name="supported-metrics-ns-aws-applicationelb"></a>

The `AWS/ApplicationELB` namespace includes enriched metrics for the following resource types.
+ [AWS::ElasticLoadBalancingV2::LoadBalancer](#supported-metrics-aws-applicationelb-aws-elasticloadbalancingv2-loadbalancer)
+ [AWS::ElasticLoadBalancingV2::TargetGroup](#supported-metrics-aws-applicationelb-aws-elasticloadbalancingv2-targetgroup)

### AWS::ElasticLoadBalancingV2::LoadBalancer
<a name="supported-metrics-aws-applicationelb-aws-elasticloadbalancingv2-loadbalancer"></a>


| Metric | Dimensions | 
| --- | --- | 
| ActiveConnectionCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ActiveZonalShiftHostCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| AnomalousHostCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| AppCookieNonStickinessCount | + `LoadBalancer` | 
| ClientTLSNegotiationErrorCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ConsumedLCUs | + `LoadBalancer` | 
| DesyncMitigationMode\_NonCompliant\_Request\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| DroppedInvalidHeaderRequestCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ELBAuthError | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ELBAuthFailure | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ELBAuthLatency | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ELBAuthRefreshTokenSuccess | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ELBAuthSuccess | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ELBAuthUserClaimsSizeExceeded | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ExcessiveLowReputationPackets | + `LoadBalancer` | 
| ForwardedInvalidHeaderRequestCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| GrpcRequestCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| HTTPCode\_ELB\_3XX\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| HTTPCode\_ELB\_4XX\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| HTTPCode\_ELB\_500\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| HTTPCode\_ELB\_502\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| HTTPCode\_ELB\_503\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| HTTPCode\_ELB\_504\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| HTTPCode\_ELB\_5XX\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| HTTPCode\_Target\_2XX\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| HTTPCode\_Target\_3XX\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| HTTPCode\_Target\_4XX\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| HTTPCode\_Target\_5XX\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| HTTP\_Fixed\_Response\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| HTTP\_Redirect\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| HTTP\_Redirect\_Url\_Limit\_Exceeded\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| HealthyHostCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| HealthyStateDNS | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| HealthyStateRouting | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| IPv6ProcessedBytes | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| IPv6RequestCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| LambdaTargetProcessedBytes | + `LoadBalancer` | 
| LambdaUserError | + `LoadBalancer`, `TargetGroup` | 
| LowReputationPacketsDropped | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| LowReputationRequestsDenied | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| MitigatedHostCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| NewConnectionCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| NonStickyRequestCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| PeakLCUs | + `LoadBalancer` | 
| ProcessedBytes | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| RejectedConnectionCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| RequestCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| RequestCountPerTarget | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| ReservedLCUs | + `LoadBalancer` | 
| RuleEvaluations | + `LoadBalancer` | 
| TargetConnectionErrorCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| TargetControlActiveChannelCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TargetControlChannelErrorCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TargetControlNewChannelCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TargetControlProcessedBytes | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TargetControlRequestCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TargetControlRequestRejectCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TargetControlWorkQueueLength | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TargetResponseTime | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| TargetTLSNegotiationErrorCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| UnHealthyHostCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| UnhealthyRoutingRequestCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| UnhealthyStateDNS | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| UnhealthyStateRouting | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 

### AWS::ElasticLoadBalancingV2::TargetGroup
<a name="supported-metrics-aws-applicationelb-aws-elasticloadbalancingv2-targetgroup"></a>


| Metric | Dimensions | 
| --- | --- | 
| GrpcRequestCount | + `AvailabilityZone`, `TargetGroup`<br />+ `TargetGroup` | 
| LambdaInternalError | + `TargetGroup` | 
| LambdaUserError | + `TargetGroup` | 
| RequestCountPerTarget | + `AvailabilityZone`, `TargetGroup`<br />+ `TargetGroup` | 

## AWS/Athena
<a name="supported-metrics-ns-aws-athena"></a>

The `AWS/Athena` namespace includes enriched metrics for the following resource types.
+ [AWS::Athena::WorkGroup](#supported-metrics-aws-athena-aws-athena-workgroup)

### AWS::Athena::WorkGroup
<a name="supported-metrics-aws-athena-aws-athena-workgroup"></a>


| Metric | Dimensions | 
| --- | --- | 
| DPUConsumed | + `WorkGroup` | 
| DPUCount | + `QueryState`, `QueryType`, `WorkGroup` | 
| EngineExecutionTime | + `QueryState`, `QueryType`, `WorkGroup` | 
| ProcessedBytes | + `QueryState`, `QueryType`, `WorkGroup`<br />+ `WorkGroup` | 
| QueryPlanningTime | + `QueryState`, `QueryType`, `WorkGroup` | 
| QueryQueueTime | + `QueryState`, `QueryType`, `WorkGroup` | 
| ServicePreProcessingTime | + `QueryState`, `QueryType`, `WorkGroup` | 
| ServiceProcessingTime | + `QueryState`, `QueryType`, `WorkGroup` | 
| TotalExecutionTime | + `QueryState`, `QueryType`, `WorkGroup` | 

## AWS/ClientVPN
<a name="supported-metrics-ns-aws-clientvpn"></a>

The `AWS/ClientVPN` namespace includes enriched metrics for the following resource types.
+ [AWS::EC2::ClientVpnEndpoint](#supported-metrics-aws-clientvpn-aws-ec2-clientvpnendpoint)

### AWS::EC2::ClientVpnEndpoint
<a name="supported-metrics-aws-clientvpn-aws-ec2-clientvpnendpoint"></a>


| Metric | Dimensions | 
| --- | --- | 
| ActiveConnectionsCount | + `Endpoint` | 
| AuthenticationFailures | + `Endpoint` | 
| ClientConnectHandlerDeniedConnections | + `Endpoint` | 
| ClientConnectHandlerFailedServiceErrors | + `Endpoint` | 
| ClientConnectHandlerInvalidResponses | + `Endpoint` | 
| ClientConnectHandlerOtherExecutionErrors | + `Endpoint` | 
| ClientConnectHandlerThrottlingErrors | + `Endpoint` | 
| ClientConnectHandlerTimeouts | + `Endpoint` | 
| CrlDaysToExpiry | + `Endpoint` | 
| EgressBytes | + `Endpoint` | 
| EgressPackets | + `Endpoint` | 
| IngressBytes | + `Endpoint` | 
| IngressPackets | + `Endpoint` | 
| SelfServicePortalClientConfigurationDownloads | + `Endpoint` | 
| ZeroHealthItemsCount | + `Endpoint` | 

## AWS/CloudFront
<a name="supported-metrics-ns-aws-cloudfront"></a>

The `AWS/CloudFront` namespace includes enriched metrics for the following resource types.
+ [AWS::CloudFront::Distribution](#supported-metrics-aws-cloudfront-aws-cloudfront-distribution)
+ [AWS::CloudFront::Function](#supported-metrics-aws-cloudfront-aws-cloudfront-function)

### AWS::CloudFront::Distribution
<a name="supported-metrics-aws-cloudfront-aws-cloudfront-distribution"></a>


| Metric | Dimensions | 
| --- | --- | 
| 4xxErrorRate | + `DistributionId`, `Region` | 
| 5xxErrorRate | + `DistributionId`, `Region` | 
| BytesDownloaded | + `DistributionId`, `Region` | 
| BytesUploaded | + `DistributionId`, `Region` | 
| Requests | + `DistributionId`, `Region` | 
| TotalErrorRate | + `DistributionId`, `Region` | 

### AWS::CloudFront::Function
<a name="supported-metrics-aws-cloudfront-aws-cloudfront-function"></a>


| Metric | Dimensions | 
| --- | --- | 
| FunctionComputeUtilization | + `DistributionId`, `FunctionName`, `Region` | 
| FunctionExecutionErrors | + `DistributionId`, `FunctionName`, `Region` | 
| FunctionInvocations | + `DistributionId`, `FunctionName`, `Region` | 
| FunctionThrottles | + `DistributionId`, `FunctionName`, `Region` | 
| FunctionValidationErrors | + `DistributionId`, `FunctionName`, `Region` | 
| KvsReadErrors | + `DistributionId`, `FunctionName`, `Region` | 
| KvsReadRequests | + `DistributionId`, `FunctionName`, `Region` | 

## AWS/CloudWatch/MetricStreams
<a name="supported-metrics-ns-aws-cloudwatch-metricstreams"></a>

The `AWS/CloudWatch/MetricStreams` namespace includes enriched metrics for the following resource types.
+ [AWS::CloudWatch::MetricStream](#supported-metrics-aws-cloudwatch-metricstreams-aws-cloudwatch-metricstream)

### AWS::CloudWatch::MetricStream
<a name="supported-metrics-aws-cloudwatch-metricstreams-aws-cloudwatch-metricstream"></a>


| Metric | Dimensions | 
| --- | --- | 
| MetricUpdate | + `MetricStreamName` | 
| PublishErrorRate | + `MetricStreamName` | 
| TotalMetricUpdate | + `MetricStreamName` | 

## AWS/CodeGuruProfiler
<a name="supported-metrics-ns-aws-codeguruprofiler"></a>

The `AWS/CodeGuruProfiler` namespace includes enriched metrics for the following resource types.
+ [AWS::CodeGuruProfiler::ProfilingGroup](#supported-metrics-aws-codeguruprofiler-aws-codeguruprofiler-profilinggroup)

### AWS::CodeGuruProfiler::ProfilingGroup
<a name="supported-metrics-aws-codeguruprofiler-aws-codeguruprofiler-profilinggroup"></a>


| Metric | Dimensions | 
| --- | --- | 
| Recommendations | + `ProfilingGroupName` | 

## AWS/Cognito
<a name="supported-metrics-ns-aws-cognito"></a>

The `AWS/Cognito` namespace includes enriched metrics for the following resource types.
+ [AWS::Cognito::UserPool](#supported-metrics-aws-cognito-aws-cognito-userpool)

### AWS::Cognito::UserPool
<a name="supported-metrics-aws-cognito-aws-cognito-userpool"></a>


| Metric | Dimensions | 
| --- | --- | 
| AccountTakeoverRisk | + `Operation`, `RiskLevel`, `UserPoolId` | 
| CompromisedCredentialRisk | + `Operation`, `RiskLevel`, `UserPoolId` | 
| FederationSuccesses | + `IdentityProvider`, `UserPool`, `UserPoolClient` | 
| FederationThrottles | + `IdentityProvider`, `UserPool`, `UserPoolClient` | 
| NoRisk | + `Operation`, `UserPoolId` | 
| Risk | + `Operation`, `UserPoolId` | 
| SignInSuccesses | + `UserPool`, `UserPoolClient` | 
| SignInThrottles | + `UserPool`, `UserPoolClient` | 
| SignUpSuccesses | + `UserPool`, `UserPoolClient` | 
| SignUpThrottles | + `UserPool`, `UserPoolClient` | 
| TokenRefreshSuccesses | + `UserPool`, `UserPoolClient` | 
| TokenRefreshThrottles | + `UserPool`, `UserPoolClient` | 

## AWS/Connect
<a name="supported-metrics-ns-aws-connect"></a>

The `AWS/Connect` namespace includes enriched metrics for the following resource types.
+ [AWS::Connect::Instance](#supported-metrics-aws-connect-aws-connect-instance)

### AWS::Connect::Instance
<a name="supported-metrics-aws-connect-aws-connect-instance"></a>


| Metric | Dimensions | 
| --- | --- | 
| CallRecordingUploadError | + `InstanceId`, `MetricGroup` | 
| CallsBreachingConcurrencyQuota | + `InstanceId`, `MetricGroup` | 
| CallsPerInterval | + `InstanceId`, `MetricGroup` | 
| ChatsBreachingActiveChatQuota | + `InstanceId`, `MetricGroup` | 
| ConcurrentActiveChats | + `InstanceId`, `MetricGroup` | 
| ConcurrentActiveChatsPercentage | + `InstanceId`, `MetricGroup` | 
| ConcurrentCalls | + `InstanceId`, `MetricGroup` | 
| ConcurrentCallsPercentage | + `InstanceId`, `MetricGroup` | 
| ConcurrentTasks | + `InstanceId`, `MetricGroup` | 
| ConcurrentTasksPercentage | + `InstanceId`, `MetricGroup` | 
| ContactFlowErrors | + `ContactFlowName`, `InstanceId`, `MetricGroup` | 
| LongestQueueWaitTime | + `InstanceId`, `MetricGroup`, `QueueName` | 
| MisconfiguredPhoneNumbers | + `InstanceId`, `MetricGroup` | 
| MissedCalls | + `InstanceId`, `MetricGroup` | 
| PublicSigningKeyUsage | + `InstanceId`, `SigningKeyId` | 
| QueueCapacityExceededError | + `InstanceId`, `MetricGroup`, `QueueName` | 
| QueueSize | + `InstanceId`, `MetricGroup`, `QueueName` | 
| SuccessfulChatsPerInterval | + `InstanceId`, `MetricGroup` | 
| TasksBreachingConcurrencyQuota | + `InstanceId`, `MetricGroup` | 
| ToInstancePacketLossRate | + `InstanceId`, `Participant`, `Stream Type`, `Type of Connection` | 

## AWS/DAX
<a name="supported-metrics-ns-aws-dax"></a>

The `AWS/DAX` namespace includes enriched metrics for the following resource types.
+ [AWS::DAX::Cluster](#supported-metrics-aws-dax-aws-dax-cluster)

### AWS::DAX::Cluster
<a name="supported-metrics-aws-dax-aws-dax-cluster"></a>


| Metric | Dimensions | 
| --- | --- | 
| BaselineNetworkBytesInUtilization | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| BaselineNetworkBytesOutUtilization | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| BatchGetItemRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| BatchWriteItemRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| CPUCreditBalance | + `ClusterId`, `NodeId` | 
| CPUCreditUsage | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| CPUSurplusCreditBalance | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| CPUSurplusCreditsCharged | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| CPUUtilization | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| CacheMemoryUtilization | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| ClientConnections | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| DeleteItemRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| ErrorRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| EstimatedDbSize | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| EvictedSize | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| FailedRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| FaultRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| GetItemRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| ItemCacheHits | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| ItemCacheMisses | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| NetworkBytesIn | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| NetworkBytesOut | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| NetworkMaxBytesIn | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| NetworkMaxBytesOut | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| NetworkMaxPacketsIn | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| NetworkMaxPacketsOut | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| NetworkPacketsIn | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| NetworkPacketsOut | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| PutItemRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| QueryCacheHits | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| QueryCacheMisses | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| QueryRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| ScanCacheHits | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| ScanCacheMisses | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| ScanRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| ThrottledRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| TotalRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| TransactGetItemsCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| TransactWriteItemsCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 
| UpdateItemRequestCount | + `ClusterId`<br />+ `ClusterId`, `NodeId` | 

## AWS/DataSync
<a name="supported-metrics-ns-aws-datasync"></a>

The `AWS/DataSync` namespace includes enriched metrics for the following resource types.
+ [AWS::DataSync::Task](#supported-metrics-aws-datasync-aws-datasync-task)

### AWS::DataSync::Task
<a name="supported-metrics-aws-datasync-aws-datasync-task"></a>


| Metric | Dimensions | 
| --- | --- | 
| BytesCompressed | + `TaskId` | 
| BytesPreparedDestination | + `TaskId` | 
| BytesPreparedSource | + `TaskId` | 
| BytesTransferred | + `TaskId` | 
| BytesVerifiedDestination | + `TaskId` | 
| BytesVerifiedSource | + `TaskId` | 
| BytesWritten | + `TaskId` | 
| FilesDeleted | + `TaskId` | 
| FilesListedSource | + `TaskId` | 
| FilesPrepared | + `TaskId` | 
| FilesPreparedDestination | + `TaskId` | 
| FilesPreparedSource | + `TaskId` | 
| FilesSkipped | + `TaskId` | 
| FilesTransferred | + `TaskId` | 
| FilesVerified | + `TaskId` | 
| FilesVerifiedDestination | + `TaskId` | 
| FilesVerifiedSource | + `TaskId` | 

## AWS/DynamoDB
<a name="supported-metrics-ns-aws-dynamodb"></a>

The `AWS/DynamoDB` namespace includes enriched metrics for the following resource types.
+ [AWS::DynamoDB::Table](#supported-metrics-aws-dynamodb-aws-dynamodb-table)

### AWS::DynamoDB::Table
<a name="supported-metrics-aws-dynamodb-aws-dynamodb-table"></a>


| Metric | Dimensions | 
| --- | --- | 
| AgeOfOldestUnreplicatedRecord | + `DelegatedOperation`, `TableName` | 
| ConditionalCheckFailedRequests | + `TableName` | 
| ConsumedChangeDataCaptureUnits | + `DelegatedOperation`, `TableName` | 
| ConsumedReadCapacityUnits | + `TableName` | 
| ConsumedWriteCapacityUnits | + `GlobalSecondaryIndexName`, `Source`, `TableName`<br />+ `Source`, `TableName`<br />+ `TableName` | 
| ProvisionedReadCapacityUnits | + `TableName` | 
| ProvisionedWriteCapacityUnits | + `TableName` | 
| ReadThrottleEvents | + `TableName` | 
| ReturnedItemCount | + `Operation`, `TableName`<br />+ `Operation`, `TableName`, `Verb` | 
| SuccessfulRequestLatency | + `Operation`, `OperationType`, `TableName`<br />+ `Operation`, `TableName`<br />+ `Operation`, `TableName`, `Verb` | 
| SystemErrors | + `Operation`, `TableName` | 
| ThrottledPutRecordCount | + `DelegatedOperation`, `TableName` | 
| ThrottledRequests | + `Operation`, `TableName`<br />+ `Operation`, `TableName`, `Verb` | 
| TimeToLiveDeletedItemCount | + `TableName` | 
| TransactionConflict | + `TableName` | 
| WriteThrottleEvents | + `TableName` | 

## AWS/EBS
<a name="supported-metrics-ns-aws-ebs"></a>

The `AWS/EBS` namespace includes enriched metrics for the following resource types.
+ [AWS::EC2::Volume](#supported-metrics-aws-ebs-aws-ec2-volume)

### AWS::EC2::Volume
<a name="supported-metrics-aws-ebs-aws-ec2-volume"></a>


| Metric | Dimensions | 
| --- | --- | 
| BurstBalance | + `VolumeId` | 
| VolumeAvgIOPS | + `InstanceId`, `VolumeId` | 
| VolumeAvgReadLatency | + `InstanceId`, `VolumeId` | 
| VolumeAvgThroughput | + `InstanceId`, `VolumeId` | 
| VolumeAvgWriteLatency | + `InstanceId`, `VolumeId` | 
| VolumeConsumedReadWriteOps | + `VolumeId` | 
| VolumeIOPSExceededCheck | + `InstanceId`, `VolumeId` | 
| VolumeIdleTime | + `VolumeId` | 
| VolumeQueueLength | + `VolumeId` | 
| VolumeReadBytes | + `VolumeId` | 
| VolumeReadOps | + `VolumeId` | 
| VolumeStalledIOCheck | + `InstanceId`, `VolumeId` | 
| VolumeThroughputExceededCheck | + `InstanceId`, `VolumeId` | 
| VolumeThroughputPercentage | + `VolumeId` | 
| VolumeTotalReadTime | + `VolumeId` | 
| VolumeTotalWriteTime | + `VolumeId` | 
| VolumeWriteBytes | + `VolumeId` | 
| VolumeWriteOps | + `VolumeId` | 

## AWS/EC2
<a name="supported-metrics-ns-aws-ec2"></a>

The `AWS/EC2` namespace includes enriched metrics for the following resource types.
+ [AWS::EC2::Host](#supported-metrics-aws-ec2-aws-ec2-host)
+ [AWS::EC2::Instance](#supported-metrics-aws-ec2-aws-ec2-instance)
+ [AWS::EC2::VPC](#supported-metrics-aws-ec2-aws-ec2-vpc)

### AWS::EC2::Host
<a name="supported-metrics-aws-ec2-aws-ec2-host"></a>


| Metric | Dimensions | 
| --- | --- | 
| DedicatedHostCPUUtilization | + `HostId` | 

### AWS::EC2::Instance
<a name="supported-metrics-aws-ec2-aws-ec2-instance"></a>


| Metric | Dimensions | 
| --- | --- | 
| CPUCreditBalance | + `InstanceId` | 
| CPUCreditUsage | + `InstanceId` | 
| CPUSurplusCreditBalance | + `InstanceId` | 
| CPUSurplusCreditsCharged | + `InstanceId` | 
| CPUUtilization | + `InstanceId` | 
| DiskReadBytes | + `InstanceId` | 
| DiskReadOps | + `InstanceId` | 
| DiskWriteBytes | + `InstanceId` | 
| DiskWriteOps | + `InstanceId` | 
| EBSByteBalance% | + `InstanceId` | 
| EBSIOBalance% | + `InstanceId` | 
| EBSReadBytes | + `InstanceId` | 
| EBSReadOps | + `InstanceId` | 
| EBSWriteBytes | + `InstanceId` | 
| EBSWriteOps | + `InstanceId` | 
| GPUPowerUtilization | + `InstanceId` | 
| InstanceEBSIOPSExceededCheck | + `InstanceId` | 
| InstanceEBSThroughputExceededCheck | + `InstanceId` | 
| MetadataNoToken | + `InstanceId` | 
| MetadataNoTokenRejected | + `InstanceId` | 
| NetworkIn | + `InstanceId` | 
| NetworkMirrorIn | + `InstanceId` | 
| NetworkMirrorOut | + `InstanceId` | 
| NetworkOut | + `InstanceId` | 
| NetworkPacketsIn | + `InstanceId` | 
| NetworkPacketsMirrorIn | + `InstanceId` | 
| NetworkPacketsMirrorOut | + `InstanceId` | 
| NetworkPacketsOut | + `InstanceId` | 
| NetworkPacketsSkipMirrorIn | + `InstanceId` | 
| NetworkPacketsSkipMirrorOut | + `InstanceId` | 
| NetworkSkipMirrorIn | + `InstanceId` | 
| NetworkSkipMirrorOut | + `InstanceId` | 
| StatusCheckFailed | + `InstanceId` | 
| StatusCheckFailed\_Application | + `InstanceId` | 
| StatusCheckFailed\_AttachedEBS | + `InstanceId` | 
| StatusCheckFailed\_Instance | + `InstanceId` | 
| StatusCheckFailed\_System | + `InstanceId` | 

### AWS::EC2::VPC
<a name="supported-metrics-aws-ec2-aws-ec2-vpc"></a>


| Metric | Dimensions | 
| --- | --- | 
| NetworkAddressUsage | + `Per-VPC Metrics` | 
| NetworkAddressUsagePeered | + `Per-VPC Metrics` | 

## AWS/EC2CapacityReservations
<a name="supported-metrics-ns-aws-ec2capacityreservations"></a>

The `AWS/EC2CapacityReservations` namespace includes enriched metrics for the following resource types.
+ [AWS::EC2::CapacityReservation](#supported-metrics-aws-ec2capacityreservations-aws-ec2-capacityreservation)

### AWS::EC2::CapacityReservation
<a name="supported-metrics-aws-ec2capacityreservations-aws-ec2-capacityreservation"></a>


| Metric | Dimensions | 
| --- | --- | 
| AvailableInstanceCount | + `CapacityReservationId` | 
| InstanceUtilization | + `CapacityReservationId` | 
| TotalInstanceCount | + `CapacityReservationId` | 
| UsedInstanceCount | + `CapacityReservationId` | 

## AWS/ECS
<a name="supported-metrics-ns-aws-ecs"></a>

The `AWS/ECS` namespace includes enriched metrics for the following resource types.
+ [AWS::ECS::Cluster](#supported-metrics-aws-ecs-aws-ecs-cluster)
+ [AWS::ECS::Service](#supported-metrics-aws-ecs-aws-ecs-service)

### AWS::ECS::Cluster
<a name="supported-metrics-aws-ecs-aws-ecs-cluster"></a>


| Metric | Dimensions | 
| --- | --- | 
| CPUReservation | + `ClusterName` | 
| CPUUtilization | + `ClusterName` | 
| GPUReservation | + `ClusterName` | 
| MemoryReservation | + `ClusterName` | 
| MemoryUtilization | + `ClusterName` | 

### AWS::ECS::Service
<a name="supported-metrics-aws-ecs-aws-ecs-service"></a>


| Metric | Dimensions | 
| --- | --- | 
| CPUUtilization | + `ClusterName`, `ServiceName` | 
| MemoryUtilization | + `ClusterName`, `ServiceName` | 

## AWS/EFS
<a name="supported-metrics-ns-aws-efs"></a>

The `AWS/EFS` namespace includes enriched metrics for the following resource types.
+ [AWS::EFS::FileSystem](#supported-metrics-aws-efs-aws-efs-filesystem)

### AWS::EFS::FileSystem
<a name="supported-metrics-aws-efs-aws-efs-filesystem"></a>


| Metric | Dimensions | 
| --- | --- | 
| BurstCreditBalance | + `FileSystemId` | 
| ClientConnections | + `FileSystemId` | 
| DataReadIOBytes | + `FileSystemId` | 
| DataWriteIOBytes | + `FileSystemId` | 
| MetadataIOBytes | + `FileSystemId` | 
| MeteredIOBytes | + `FileSystemId` | 
| PercentIOLimit | + `FileSystemId` | 
| PermittedThroughput | + `FileSystemId` | 
| StorageBytes | + `FileSystemId`, `StorageClass` | 
| TimeSinceLastSync | + `DestinationFileSystemId`, `FileSystemId` | 
| TotalIOBytes | + `FileSystemId` | 

## AWS/EKS
<a name="supported-metrics-ns-aws-eks"></a>

The `AWS/EKS` namespace includes enriched metrics for the following resource types.
+ [AWS::EKS::Cluster](#supported-metrics-aws-eks-aws-eks-cluster)

### AWS::EKS::Cluster
<a name="supported-metrics-aws-eks-aws-eks-cluster"></a>


| Metric | Dimensions | 
| --- | --- | 
| apiserver\_admission\_webhook\_rejection\_count\_ADMIT | + `ClusterName` | 
| apiserver\_admission\_webhook\_rejection\_count\_VALIDATING | + `ClusterName` | 
| apiserver\_admission\_webhook\_request\_total | + `ClusterName` | 
| apiserver\_admission\_webhook\_request\_total\_ADMIT | + `ClusterName` | 
| apiserver\_admission\_webhook\_request\_total\_VALIDATING | + `ClusterName` | 
| apiserver\_current\_inflight\_requests\_MUTATING | + `ClusterName` | 
| apiserver\_current\_inflight\_requests\_READONLY | + `ClusterName` | 
| apiserver\_flowcontrol\_current\_executing\_seats | + `ClusterName` | 
| apiserver\_request\_duration\_seconds\_DELETE\_P99 | + `ClusterName` | 
| apiserver\_request\_duration\_seconds\_GET\_P99 | + `ClusterName` | 
| apiserver\_request\_duration\_seconds\_LIST\_P99 | + `ClusterName` | 
| apiserver\_request\_duration\_seconds\_PATCH\_P99 | + `ClusterName` | 
| apiserver\_request\_duration\_seconds\_POST\_P99 | + `ClusterName` | 
| apiserver\_request\_duration\_seconds\_PUT\_P99 | + `ClusterName` | 
| apiserver\_request\_total | + `ClusterName` | 
| apiserver\_request\_total\_429 | + `ClusterName` | 
| apiserver\_request\_total\_4XX | + `ClusterName` | 
| apiserver\_request\_total\_5XX | + `ClusterName` | 
| apiserver\_request\_total\_LIST\_PODS | + `ClusterName` | 
| apiserver\_storage\_size\_bytes | + `ClusterName` | 
| etcd\_mvcc\_db\_total\_size\_in\_use\_in\_bytes | + `ClusterName` | 
| scheduler\_pending\_pods | + `ClusterName` | 
| scheduler\_pending\_pods\_ACTIVEQ | + `ClusterName` | 
| scheduler\_pending\_pods\_BACKOFF | + `ClusterName` | 
| scheduler\_pending\_pods\_GATED | + `ClusterName` | 
| scheduler\_pending\_pods\_UNSCHEDULABLE | + `ClusterName` | 
| scheduler\_schedule\_attempts\_ERROR | + `ClusterName` | 
| scheduler\_schedule\_attempts\_SCHEDULED | + `ClusterName` | 
| scheduler\_schedule\_attempts\_UNSCHEDULABLE | + `ClusterName` | 
| scheduler\_schedule\_attempts\_total | + `ClusterName` | 

## AWS/ELB
<a name="supported-metrics-ns-aws-elb"></a>

The `AWS/ELB` namespace includes enriched metrics for the following resource types.
+ [AWS::ElasticLoadBalancing::LoadBalancer](#supported-metrics-aws-elb-aws-elasticloadbalancing-loadbalancer)

### AWS::ElasticLoadBalancing::LoadBalancer
<a name="supported-metrics-aws-elb-aws-elasticloadbalancing-loadbalancer"></a>


| Metric | Dimensions | 
| --- | --- | 
| BackendConnectionErrors | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| DesyncMitigationMode\_NonCompliant\_Request\_Count | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| HTTPCode\_Backend\_2XX | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| HTTPCode\_Backend\_3XX | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| HTTPCode\_Backend\_4XX | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| HTTPCode\_Backend\_5XX | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| HTTPCode\_ELB\_4XX | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| HTTPCode\_ELB\_5XX | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| HealthyHostCount | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| Latency | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| RequestCount | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| SpilloverCount | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| SurgeQueueLength | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 
| UnHealthyHostCount | + `AvailabilityZone`, `LoadBalancerName`<br />+ `LoadBalancerName` | 

## AWS/EMRServerless
<a name="supported-metrics-ns-aws-emrserverless"></a>

The `AWS/EMRServerless` namespace includes enriched metrics for the following resource types.
+ [AWS::EMRServerless::Application](#supported-metrics-aws-emrserverless-aws-emrserverless-application)

### AWS::EMRServerless::Application
<a name="supported-metrics-aws-emrserverless-aws-emrserverless-application"></a>


| Metric | Dimensions | 
| --- | --- | 
| CPUAllocated | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName`<br />+ `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `WorkerType` | 
| CancelledJobs | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| CancellingJobs | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| FailedJobs | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| IdleWorkerCount | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName`<br />+ `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `WorkerType` | 
| MaxCPUAllowed | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| MaxMemoryAllowed | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| MaxStorageAllowed | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| MemoryAllocated | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName`<br />+ `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `WorkerType` | 
| PendingCreationWorkerCount | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName`<br />+ `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `WorkerType` | 
| PendingJobs | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| RunningJobs | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| RunningWorkerCount | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName`<br />+ `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `WorkerType` | 
| ScheduledJobs | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| StorageAllocated | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName`<br />+ `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `WorkerType` | 
| SubmittedJobs | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| SuccessJobs | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName` | 
| TotalWorkerCount | + `ApplicationId`<br />+ `ApplicationId`, `ApplicationName`<br />+ `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `WorkerType` | 
| WorkerCpuAllocated | + `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `JobId`, `WorkerType` | 
| WorkerCpuUsed | + `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `JobId`, `WorkerType` | 
| WorkerEphemeralStorageAllocated | + `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `JobId`, `WorkerType` | 
| WorkerEphemeralStorageUsed | + `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `JobId`, `WorkerType` | 
| WorkerMemoryAllocated | + `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `JobId`, `WorkerType` | 
| WorkerMemoryUsed | + `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `JobId`, `WorkerType` | 
| WorkerStorageReadBytes | + `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `JobId`, `WorkerType` | 
| WorkerStorageWriteBytes | + `ApplicationId`, `ApplicationName`, `CapacityAllocationType`, `JobId`, `JobName`, `WorkerType`<br />+ `ApplicationId`, `CapacityAllocationType`, `JobId`, `WorkerType` | 

## AWS/ES
<a name="supported-metrics-ns-aws-es"></a>

The `AWS/ES` namespace includes enriched metrics for the following resource types.
+ [AWS::OpenSearchService::Domain](#supported-metrics-aws-es-aws-opensearchservice-domain)

### AWS::OpenSearchService::Domain
<a name="supported-metrics-aws-es-aws-opensearchservice-domain"></a>


| Metric | Dimensions | 
| --- | --- | 
| 2xx | + `ClientId`, `DomainName` | 
| 3xx | + `ClientId`, `DomainName` | 
| 4xx | + `ClientId`, `DomainName` | 
| 5xx | + `ClientId`, `DomainName` | 
| ADAnomalyDetectorsIndexStatus.red | + `ClientId`, `DomainName` | 
| ADAnomalyDetectorsIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| ADAnomalyResultsIndexStatus.red | + `ClientId`, `DomainName` | 
| ADAnomalyResultsIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| ADExecuteFailureCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ADExecuteRequestCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ADHCExecuteFailureCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ADHCExecuteRequestCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ADModelsCheckpointIndexStatus.red | + `ClientId`, `DomainName` | 
| ADModelsCheckpointIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| ADPluginUnhealthy | + `ClientId`, `DomainName` | 
| ActiveDataNode | + `ClientId`, `DomainName`, `NodeId` | 
| AlertingDegraded | + `ClientId`, `DomainName` | 
| AlertingIndexExists | + `ClientId`, `DomainName` | 
| AlertingIndexStatus.green | + `ClientId`, `DomainName` | 
| AlertingIndexStatus.red | + `ClientId`, `DomainName` | 
| AlertingIndexStatus.yellow | + `ClientId`, `DomainName` | 
| AlertingNodesNotOnSchedule | + `ClientId`, `DomainName` | 
| AlertingNodesOnSchedule | + `ClientId`, `DomainName` | 
| AlertingScheduledJobEnabled | + `ClientId`, `DomainName` | 
| AsyncQueryCancelApiFailedRequestCusErrCount | + `ClientId`, `DomainName` | 
| AsyncQueryCancelApiFailedRequestSysErrCount | + `ClientId`, `DomainName` | 
| AsyncQueryCancelApiRequestCount | + `ClientId`, `DomainName` | 
| AsyncQueryCreateApiFailedRequestCusErrCount | + `ClientId`, `DomainName` | 
| AsyncQueryCreateApiFailedRequestSysErrCount | + `ClientId`, `DomainName` | 
| AsyncQueryCreateApiRequestCount | + `ClientId`, `DomainName` | 
| AsyncQueryGetApiFailedRequestCusErrCount | + `ClientId`, `DomainName` | 
| AsyncQueryGetApiFailedRequestSysErrCount | + `ClientId`, `DomainName` | 
| AsyncQueryGetApiRequestCount | + `ClientId`, `DomainName` | 
| AsynchronousSearchCancelled | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| AsynchronousSearchCompletionRate | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| AsynchronousSearchFailureRate | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| AsynchronousSearchInitializedRate | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| AsynchronousSearchPersistFailedRate | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| AsynchronousSearchPersistRate | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| AsynchronousSearchRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| AsynchronousSearchRunningCurrent | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| AsynchronousSearchStoreHealthRed | + `ClientId`, `DomainName` | 
| AsynchronousSearchStoreSize | + `ClientId`, `DomainName` | 
| AsynchronousSearchStoredResponseCount | + `ClientId`, `DomainName` | 
| AsynchronousSearchSubmissionRate | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| AutoFollowLeaderCallFailure | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `LeaderAlias` | 
| AutoFollowNumFailedStartReplication | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `LeaderAlias` | 
| AutoFollowNumSuccessStartReplication | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `LeaderAlias` | 
| AutoTuneChangesHistoryHeapSize | + `AutotuningType`, `ClientId`, `DomainName`, `TargetId` | 
| AutoTuneFailed | + `AutotuningType`, `ClientId`, `DomainName`, `TargetId` | 
| AutoTuneSucceeded | + `AutotuningType`, `ClientId`, `DomainName`, `TargetId` | 
| AutoTuneValue | + `AutotuningType`, `ClientId`, `DomainName`, `TargetId` | 
| AutomatedSnapshotFailure | + `ClientId`, `DomainName` | 
| AvgPointInTimeAliveTime | + `ClientId`, `DomainName` | 
| BurstBalance | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CPUCreditBalance | + `ClientId`, `DomainName` | 
| CPUUtilization | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CanMatchCurrent | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CanMatchTimeInMillis | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CanMatchTotal | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ClusterIndexWritesBlocked | + `ClientId`, `DomainName` | 
| ClusterStatus.green | + `ClientId`, `DomainName` | 
| ClusterStatus.red | + `ClientId`, `DomainName` | 
| ClusterStatus.yellow | + `ClientId`, `DomainName` | 
| ClusterUsedSpace | + `ClientId`, `DomainName` | 
| ColdStorageSpaceUtilization | + `ClientId`, `DomainName` | 
| ColdToWarmMigrationFailureCount | + `ClientId`, `DomainName` | 
| ColdToWarmMigrationLatency | + `ClientId`, `DomainName` | 
| ColdToWarmMigrationQueueSize | + `ClientId`, `DomainName` | 
| ColdToWarmMigrationSuccessCount | + `ClientId`, `DomainName` | 
| ComponentTemplateCount | + `ClientId`, `DomainName` | 
| ConcurrentSearchLatency | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ConcurrentSearchRate | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatingWriteRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorCPUUtilization | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorFreeStorageSpace | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorJVMGCOldCollectionCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorJVMGCOldCollectionTime | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorJVMGCYoungCollectionCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorJVMGCYoungCollectionTime | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorJVMMemoryPressure | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorOldGenJVMMemoryPressure | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorSysMemoryUtilization | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolForce\_mergeQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolForce\_mergeRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolForce\_mergeThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolIndexQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolIndexRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolIndexThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolOpendistro\_monitor\_runnerQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolOpendistro\_monitor\_runnerRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolOpendistro\_monitor\_runnerThreads | + `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolSearchQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolSearchRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolSearchThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolWriteQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolWriteRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolWriteThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolsql-workerQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolsql-workerRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CoordinatorThreadpoolsql-workerThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| CrossClusterInboundReplicationRequests | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName` | 
| CrossClusterInboundRequests | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName` | 
| CrossClusterInboundSearchRequests | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName` | 
| CrossClusterOutboundConnections | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName` | 
| CrossClusterOutboundReplicationRequests | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName` | 
| CrossClusterOutboundRequests | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName` | 
| CrossClusterOutboundSearchRequests | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName` | 
| CurrentPointInTime | + `ClientId`, `DomainName`, `NodeId` | 
| DataNodes | + `ActiveAZ`, `ClientId`, `DomainName` | 
| DataNodesShards.active | + `ActiveAZ`, `ClientId`, `DomainName` | 
| DataNodesShards.initialising | + `ActiveAZ`, `ClientId`, `DomainName` | 
| DataNodesShards.relocating | + `ActiveAZ`, `ClientId`, `DomainName` | 
| DataNodesShards.unassigned | + `ActiveAZ`, `ClientId`, `DomainName` | 
| DeletedDocuments | + `ClientId`, `DomainName` | 
| DfsPreQueryCurrent | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| DfsPreQueryTimeInMillis | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| DfsPreQueryTotal | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| DfsQueryCurrent | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| DfsQueryTimeInMillis | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| DfsQueryTotal | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| DiskQueueDepth | + `ClientId`, `DomainName` | 
| ESReportingFailedRequestSysErrCount | + `ClientId`, `DomainName` | 
| ESReportingFailedRequestUserErrCount | + `ClientId`, `DomainName` | 
| ESReportingRequestCount | + `ClientId`, `DomainName` | 
| ESReportingSuccessCount | + `ClientId`, `DomainName` | 
| ElasticsearchRequests | + `ClientId`, `DomainName` | 
| EnforcedWorkloadGroupCount | + `ClientId`, `DomainName` | 
| ExpandCurrent | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ExpandTimeInMillis | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ExpandTotal | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| FetchCurrent | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| FetchTimeInMillis | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| FetchTotal | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| FollowerCheckPoint | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName`, `LeaderAlias` | 
| ForecastCheckpointIndexStatus.red | + `ClientId`, `DomainName` | 
| ForecastCheckpointIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| ForecastConfigIndexStatus.red | + `ClientId`, `DomainName` | 
| ForecastConfigIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| ForecastExecuteFailureCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ForecastExecuteRequestCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ForecastHCExecuteFailureCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ForecastHCExecuteRequestCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ForecastModelCorruptionCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ForecastResultsIndexStatus.red | + `ClientId`, `DomainName` | 
| ForecastResultsIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| ForecastStateIndexStatus.red | + `ClientId`, `DomainName` | 
| ForecastStateIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| ForecastUnhealthy | + `ClientId`, `DomainName` | 
| ForecasterCount | + `ClientId`, `DomainName` | 
| FreeStorageSpace | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| HCForecasterCount | + `ClientId`, `DomainName` | 
| HasActivePointInTime | + `ClientId`, `DomainName` | 
| HasUsedPointInTime | + `ClientId`, `DomainName` | 
| HighSwapUsage | + `ClientId`, `DomainName`, `NodeId` | 
| HotStorageSpaceUtilization | + `ClientId`, `DomainName` | 
| HotToWarmMigrationFailureCount | + `ClientId`, `DomainName` | 
| HotToWarmMigrationForceMergeLatency | + `ClientId`, `DomainName` | 
| HotToWarmMigrationProcessingLatency | + `ClientId`, `DomainName` | 
| HotToWarmMigrationQueueSize | + `ClientId`, `DomainName` | 
| HotToWarmMigrationSnapshotLatency | + `ClientId`, `DomainName` | 
| HotToWarmMigrationSuccessCount | + `ClientId`, `DomainName` | 
| HotToWarmMigrationSuccessLatency | + `ClientId`, `DomainName` | 
| ISMPolicyCount | + `ClientId`, `DomainName` | 
| InFlightFetches | + `ClientId`, `DomainName` | 
| IndexingLatency | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| IndexingRate | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| InvalidHostHeaderRequests | + `ClientId`, `DomainName` | 
| IopsThrottle | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| JVMGCOldCollectionCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| JVMGCOldCollectionTime | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| JVMGCYoungCollectionCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| JVMGCYoungCollectionTime | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| JVMMemoryPressure | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KMSKeyError | + `ClientId`, `DomainName` | 
| KMSKeyInaccessible | + `ClientId`, `DomainName` | 
| KNNCacheCapacityReached | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNCircuitBreakerTriggered | + `ClientId`, `DomainName` | 
| KNNEvictionCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNFaissInitialized | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNGraphIndexErrors | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNGraphIndexRequests | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNGraphMemoryUsage | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNGraphMemoryUsagePercentage | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNGraphQueryErrors | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNGraphQueryRequests | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNHitCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNLoadExceptionCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNLoadSuccessCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNLuceneInitialized | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNMissCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNNmslibInitialized | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNQueryRequests | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNRemoteBuildEnabled | + `ClientId`, `DomainName` | 
| KNNRemoteIndexBuildFailureCount | + `ClientId`, `DomainName` | 
| KNNRemoteIndexBuildSuccessCount | + `ClientId`, `DomainName` | 
| KNNScriptCompilationErrors | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNScriptCompilations | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNScriptQueryErrors | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNScriptQueryRequests | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNTotalLoadTime | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNTrainingErrors | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNTrainingMemoryUsage | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNTrainingMemoryUsagePercentage | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KNNTrainingRequests | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| KibanaConcurrentConnections | + `ClientId`, `DomainName`, `NodeId` | 
| KibanaHealthyNode | + `ClientId`, `DomainName`, `NodeId` | 
| KibanaHealthyNodes | + `ClientId`, `DomainName` | 
| KibanaHeapTotal | + `ClientId`, `DomainName`, `NodeId` | 
| KibanaHeapUsed | + `ClientId`, `DomainName`, `NodeId` | 
| KibanaHeapUtilization | + `ClientId`, `DomainName`, `NodeId` | 
| KibanaIndexMigrationFailed | + `ClientId`, `DomainName` | 
| KibanaOS1MinuteLoad | + `ClientId`, `DomainName`, `NodeId` | 
| KibanaRequestTotal | + `ClientId`, `DomainName`, `NodeId` | 
| KibanaResponseTimesMaxInMillis | + `ClientId`, `DomainName`, `NodeId` | 
| LTRFeatureMemoryUsageInBytes | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| LTRFeaturesetMemoryUsageInBytes | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| LTRModelMemoryUsageInBytes | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| LTRPluginUnhealthy | + `ClientId`, `DomainName` | 
| LTRRequestErrorCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| LTRRequestTotalCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| LTRStatus.red | + `ClientId`, `DomainName` | 
| LeaderCheckPoint | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName`, `LeaderAlias` | 
| MLCircuitBreakerTriggerCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MLCommonsPluginUnhealthy | + `ClientId`, `DomainName` | 
| MLConnectorCount | + `ClientId`, `DomainName` | 
| MLConnectorIndexStatus.red | + `ClientId`, `DomainName` | 
| MLConnectorIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| MLDeployedModelCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MLExecutingTaskCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MLFailureCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MLModelCount | + `ClientId`, `DomainName` | 
| MLModelIndexStatus.red | + `ClientId`, `DomainName` | 
| MLModelIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| MLRequestCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MLTaskIndexStatus.red | + `ClientId`, `DomainName` | 
| MLTaskIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| MasterCPUCreditBalance | + `ClientId`, `DomainName` | 
| MasterCPUUtilization | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MasterFreeStorageSpace | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MasterJVMMemoryPressure | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MasterOldGenJVMMemoryPressure | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MasterReachableFromNode | + `ClientId`, `DomainName` | 
| MasterSysMemoryUtilization | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MaxProvisionedThroughput | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MlCircuitBreakerTriggerCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MlConnectorCount | + `ClientId`, `DomainName` | 
| MlConnectorIndexStatus.red | + `ClientId`, `DomainName` | 
| MlConnectorIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| MlDeployedModelCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MlExecutingTaskCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MlFailureCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MlModelCount | + `ClientId`, `DomainName` | 
| MlModelIndexStatus.red | + `ClientId`, `DomainName` | 
| MlModelIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| MlNodeExecutingTaskCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MlNodeTotalCircuitBreakerTriggerCount | + `ClientId`, `DomainName`, `NodeId` | 
| MlNodeTotalFailureCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MlNodeTotalModelCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MlNodeTotalRequestCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MlRequestCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| MlTaskIndexStatus.red | + `ClientId`, `DomainName` | 
| MlTaskIndexStatusIndexExists | + `ClientId`, `DomainName` | 
| Nodes | + `ClientId`, `DomainName` | 
| OldGenJVMMemoryPressure | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| OpenContexts | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| OpenContexts-BeagleStone | + `ClientId`, `DomainName` | 
| OpenSearchDashboardsConcurrentConnections | + `ClientId`, `DomainName`, `NodeId` | 
| OpenSearchDashboardsHealthyNode | + `ClientId`, `DomainName`, `NodeId` | 
| OpenSearchDashboardsHealthyNodes | + `ClientId`, `DomainName` | 
| OpenSearchDashboardsHeapTotal | + `ClientId`, `DomainName`, `NodeId` | 
| OpenSearchDashboardsHeapUsed | + `ClientId`, `DomainName`, `NodeId` | 
| OpenSearchDashboardsHeapUtilization | + `ClientId`, `DomainName`, `NodeId` | 
| OpenSearchDashboardsIndexMigrationFailed | + `ClientId`, `DomainName` | 
| OpenSearchDashboardsOS1MinuteLoad | + `ClientId`, `DomainName`, `NodeId` | 
| OpenSearchDashboardsRequestTotal | + `ClientId`, `DomainName`, `NodeId` | 
| OpenSearchDashboardsResponseTimesMaxInMillis | + `ClientId`, `DomainName`, `NodeId` | 
| OpenSearchRequests | + `ClientId`, `DomainName` | 
| OpensearchDashboardsReportingFailedRequestSysErrCount | + `ClientId`, `DomainName` | 
| OpensearchDashboardsReportingFailedRequestUserErrCount | + `ClientId`, `DomainName` | 
| OpensearchDashboardsReportingRequestCount | + `ClientId`, `DomainName` | 
| OpensearchDashboardsReportingSuccessCount | + `ClientId`, `DomainName` | 
| PPLFailedRequestCountByCusErr | + `ClientId`, `DomainName` | 
| PPLFailedRequestCountBySysErr | + `ClientId`, `DomainName` | 
| PPLRequestCount | + `ClientId`, `DomainName` | 
| PrimaryWriteRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| QueryCurrent | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| QueryFailure | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| QueryFailure-BeagleStone | + `ClientId`, `DomainName` | 
| QuerySuccess | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| QuerySuccess-BeagleStone | + `ClientId`, `DomainName` | 
| QueryTimeInMillis | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| QueryTotal | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ReadIOPS | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ReadIOPSMicroBursting | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ReadLatency | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ReadThroughput | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ReadThroughputMicroBursting | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| RemoteStorageUsedSpace | + `ClientId`, `DomainName` | 
| RemoteStorageWriteRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ReplicaWriteRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ReplicationLagMaxTime | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ReplicationNumBootstrappingIndices | + `ClientId`, `DomainName` | 
| ReplicationNumFailedIndices | + `ClientId`, `DomainName` | 
| ReplicationNumIndexTasks | + `ClientId`, `DomainName` | 
| ReplicationNumPausedIndices | + `ClientId`, `DomainName` | 
| ReplicationNumShardTasks | + `ClientId`, `DomainName` | 
| ReplicationNumSyncingIndices | + `ClientId`, `DomainName` | 
| ReplicationRate | + `ClientId`, `ConnectionId`, `DomainName`<br />+ `ClientId`, `DomainName`, `LeaderAlias` | 
| SQLDefaultCursorRequestCount | + `ClientId`, `DomainName` | 
| SQLFailedRequestCountByCusErr | + `ClientId`, `DomainName` | 
| SQLFailedRequestCountBySysErr | + `ClientId`, `DomainName` | 
| SQLRequestCount | + `ClientId`, `DomainName` | 
| SQLUnhealthy | + `ClientId`, `DomainName` | 
| ScrollCurrent | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ScrollCurrent-BeagleStone | + `ClientId`, `DomainName` | 
| ScrollTotal | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ScrollTotal-BeagleStone | + `ClientId`, `DomainName` | 
| SearchIdleReactivateCountTotal | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| SearchLatency | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| SearchPipelineRequestFailure | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `Processor` | 
| SearchPipelineRequestTime | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `Processor` | 
| SearchPipelineUnhealthy | + `ClientId`, `DomainName` | 
| SearchRate | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| SearchShardTaskCancelled | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| SearchTaskCancelled | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| SearchableDocuments | + `ClientId`, `DomainName` | 
| SegmentCount | + `ClientId`, `DomainName`, `NodeId` | 
| ShardCount | + `ActiveAZ`, `ClientId`, `DomainName`, `NodeId`, `ShardRole`<br />+ `ActiveAZ`, `ClientId`, `DomainName`, `ShardRole`<br />+ `ClientId`, `DomainName`, `NodeId`, `ShardRole` | 
| Shards.active | + `ClientId`, `DomainName` | 
| Shards.activePrimary | + `ClientId`, `DomainName` | 
| Shards.delayedUnassigned | + `ClientId`, `DomainName` | 
| Shards.initializing | + `ClientId`, `DomainName` | 
| Shards.relocating | + `ClientId`, `DomainName` | 
| Shards.unassigned | + `ClientId`, `DomainName` | 
| SingleStreamForecasterCount | + `ClientId`, `DomainName` | 
| SnapshotCount | + `ClientId`, `DomainName`, `Repository` | 
| SnapshotFailures | + `ClientId`, `DomainName`, `Repository` | 
| SoftWorkloadGroupCount | + `ClientId`, `DomainName` | 
| SysMemoryUtilization | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| TLSNegotiationError | + `ClientId`, `DomainName` | 
| ThreadCount | + `ClientId`, `DomainName` | 
| ThreadpoolBulkQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolBulkRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolBulkThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolForce\_mergeQueue | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolForce\_mergeRejected | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolForce\_mergeThreads | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolIndexQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolIndexRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolIndexSearcherQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolIndexSearcherRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolIndexSearcherThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolIndexThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolMergeQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolMergeRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolMergeThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolOpendistro\_monitor\_runnerQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolOpendistro\_monitor\_runnerRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolOpendistro\_monitor\_runnerThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolSearchQueue | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolSearchRejected | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolSearchThreads | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolWriteQueue | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolWriteRejected | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThreadpoolWriteThreads | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| Threadpoolsql-workerQueue | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| Threadpoolsql-workerRejected | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| Threadpoolsql-workerThreads | + `ActiveAZ`, `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| ThroughputThrottle | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| TookCurrent | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| TookTimeInMillis | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| TookTotal | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `InstanceId`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| TotalPointInTime | + `ClientId`, `DomainName`, `NodeId` | 
| TotalRemoteReindexCallsFailed | + `ClientId`, `DomainName`, `RemoteDomain` | 
| TotalRemoteReindexCallsSucceeded | + `ClientId`, `DomainName`, `RemoteDomain` | 
| VolumeStalledIOCheck | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmCPUUtilization | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmConcurrentSearchLatency | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmConcurrentSearchRate | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmFreeStorageSpace | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmJVMGCOldCollectionCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmJVMGCOldCollectionTime | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmJVMGCYoungCollectionCount | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmJVMGCYoungCollectionTime | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmJVMMemoryPressure | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmNodes | + `ClientId`, `DomainName` | 
| WarmOldGenJVMMemoryPressure | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmSearchLatency | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmSearchRate | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmSearchableDocuments | + `ClientId`, `DomainName` | 
| WarmStorageSpaceUtilization | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmSysMemoryUtilization | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmThreadpoolIndexSearcherQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmThreadpoolIndexSearcherRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmThreadpoolIndexSearcherThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmThreadpoolSearchQueue | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmThreadpoolSearchRejected | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmThreadpoolSearchThreads | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WarmToColdMigrationFailureCount | + `ClientId`, `DomainName` | 
| WarmToColdMigrationLatency | + `ClientId`, `DomainName` | 
| WarmToColdMigrationQueueSize | + `ClientId`, `DomainName` | 
| WarmToColdMigrationSuccessCount | + `ClientId`, `DomainName` | 
| WarmToHotMigrationQueueSize | + `ClientId`, `DomainName` | 
| WorkloadCPUCancellations | + `ClientId`, `DomainName` | 
| WorkloadCPURejections | + `ClientId`, `DomainName` | 
| WorkloadManagementEnabled | + `ClientId`, `DomainName` | 
| WorkloadMemoryCancellations | + `ClientId`, `DomainName` | 
| WorkloadQueryCompletions | + `ClientId`, `DomainName` | 
| WriteIOPS | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WriteIOPSMicroBursting | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WriteLatency | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WriteThroughput | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| WriteThroughputMicroBursting | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| warmQueryFailure | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 
| warmQuerySuccess | + `ClientId`, `DomainName`<br />+ `ClientId`, `DomainName`, `NodeId` | 

## AWS/ElastiCache
<a name="supported-metrics-ns-aws-elasticache"></a>

The `AWS/ElastiCache` namespace includes enriched metrics for the following resource types.
+ [AWS::ElastiCache::CacheCluster](#supported-metrics-aws-elasticache-aws-elasticache-cachecluster)
+ [AWS::ElastiCache::ReplicationGroup](#supported-metrics-aws-elasticache-aws-elasticache-replicationgroup)

### AWS::ElastiCache::CacheCluster
<a name="supported-metrics-aws-elasticache-aws-elasticache-cachecluster"></a>


| Metric | Dimensions | 
| --- | --- | 
| ActiveDefragHits | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| AllocatorFragmentationBytes | + `CacheClusterId`, `CacheNodeId` | 
| AllocatorFragmentationRatio | + `CacheClusterId`, `CacheNodeId` | 
| AuthenticationFailures | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| BlockedConnections | + `CacheClusterId`, `CacheNodeId` | 
| BytesReadFromDisk | + `CacheClusterId`, `CacheNodeId` | 
| BytesReadIntoMemcached | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| BytesUsedForCache | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId`<br />+ `CacheClusterId`, `CacheNodeId`, `Tier` | 
| BytesUsedForCacheItems | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| BytesUsedForHash | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| BytesWrittenOutFromMemcached | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| BytesWrittenToDisk | + `CacheClusterId`, `CacheNodeId` | 
| CPUCreditBalance | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CPUCreditUsage | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CPUUtilization | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CacheHitRate | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CacheHits | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CacheMisses | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CasBadval | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CasHits | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CasMisses | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| ChannelAuthorizationFailures | + `CacheClusterId`, `CacheNodeId` | 
| ClusterBasedCmds | + `CacheClusterId`, `CacheNodeId` | 
| ClusterBasedCmdsLatency | + `CacheClusterId`, `CacheNodeId` | 
| CmdConfigGet | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CmdConfigSet | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CmdFlush | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CmdGet | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CmdSet | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CmdTouch | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CommandAuthorizationFailures | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CurrConfig | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CurrConnections | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| CurrItems | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId`<br />+ `CacheClusterId`, `CacheNodeId`, `Tier` | 
| CurrItemsWithVolatileFields | + `CacheClusterId`, `CacheNodeId` | 
| CurrVolatileItems | + `CacheClusterId`, `CacheNodeId` | 
| DB0AverageTTL | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| DatabaseAuthorizationFailures | + `CacheClusterId`, `CacheNodeId` | 
| DatabaseCapacityUsageCountedForEvictPercentage | + `CacheClusterId`, `CacheNodeId` | 
| DatabaseCapacityUsagePercentage | + `CacheClusterId`, `CacheNodeId` | 
| DatabaseMemoryUsageCountedForEvictPercentage | + `CacheClusterId`, `CacheNodeId` | 
| DatabaseMemoryUsagePercentage | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| DecrHits | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| DecrMisses | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| DeleteHits | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| DeleteMisses | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| DurabilityBufferExceededErrorCount | + `CacheClusterId`, `CacheNodeId` | 
| DurabilityLag | + `CacheClusterId`, `CacheNodeId` | 
| EngineCPUUtilization | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| ErrorCount | + `CacheClusterId`, `CacheNodeId` | 
| EvalBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| EvalBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| EvictedUnfetched | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| Evictions | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| ExpiredUnfetched | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| FreeableMemory | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| GeoSpatialBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| GeoSpatialBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| GetHits | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| GetMisses | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| GetTypeCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| GetTypeCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| HashBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| HashBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| HyperLogLogBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| HyperLogLogBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| IamAuthenticationExpirations | + `CacheClusterId`, `CacheNodeId` | 
| IamAuthenticationThrottling | + `CacheClusterId`, `CacheNodeId` | 
| IncrHits | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| IncrMisses | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| IsMaster | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| JsonBasedCmds | + `CacheClusterId`, `CacheNodeId` | 
| JsonBasedCmdsLatency | + `CacheClusterId`, `CacheNodeId` | 
| JsonBasedGetCmds | + `CacheClusterId`, `CacheNodeId` | 
| JsonBasedGetCmdsLatency | + `CacheClusterId`, `CacheNodeId` | 
| JsonBasedSetCmds | + `CacheClusterId`, `CacheNodeId` | 
| JsonBasedSetCmdsLatency | + `CacheClusterId`, `CacheNodeId` | 
| KeyAuthorizationFailures | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| KeyBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| KeyBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| KeysTracked | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| ListBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| ListBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| MajorPageFaults | + `CacheClusterId`, `CacheNodeId` | 
| MasterLinkHealthStatus | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| MemoryFragmentationRatio | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NetworkBandwidthInAllowanceExceeded | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NetworkBandwidthOutAllowanceExceeded | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NetworkBaselineMaxUsageInPercentage | + `CacheClusterId`, `CacheNodeId` | 
| NetworkBaselineMaxUsageOutPercentage | + `CacheClusterId`, `CacheNodeId` | 
| NetworkBaselineUsageInPercentage | + `CacheClusterId`, `CacheNodeId` | 
| NetworkBaselineUsageOutPercentage | + `CacheClusterId`, `CacheNodeId` | 
| NetworkBytesIn | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NetworkBytesOut | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NetworkConntrackAllowanceExceeded | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NetworkLinkLocalAllowanceExceeded | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NetworkMaxBytesIn | + `CacheClusterId`, `CacheNodeId` | 
| NetworkMaxBytesOut | + `CacheClusterId`, `CacheNodeId` | 
| NetworkMaxPacketsIn | + `CacheClusterId`, `CacheNodeId` | 
| NetworkMaxPacketsOut | + `CacheClusterId`, `CacheNodeId` | 
| NetworkPacketsIn | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NetworkPacketsOut | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NetworkPacketsPerSecondAllowanceExceeded | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NewConnections | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NewItems | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| NonKeyTypeCmds | + `CacheClusterId`, `CacheNodeId` | 
| NonKeyTypeCmdsLatency | + `CacheClusterId`, `CacheNodeId` | 
| NumItemsReadFromDisk | + `CacheClusterId`, `CacheNodeId` | 
| NumItemsWrittenToDisk | + `CacheClusterId`, `CacheNodeId` | 
| ProcessedCommands | + `CacheClusterId`, `CacheNodeId` | 
| PubSubBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| PubSubBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| PubSubChannels | + `CacheClusterId`, `CacheNodeId` | 
| PubSubShardChannels | + `CacheClusterId`, `CacheNodeId` | 
| Reclaimed | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| ReclaimedFields | + `CacheClusterId`, `CacheNodeId` | 
| RejectedConnections | + `CacheClusterId`, `CacheNodeId` | 
| ReplicationBytes | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| ReplicationLag | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| SaveInProgress | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| SearchBasedCmds | + `CacheClusterId`, `CacheNodeId` | 
| SearchBasedCmdsLatency | + `CacheClusterId`, `CacheNodeId` | 
| SearchBasedGetCmds | + `CacheClusterId`, `CacheNodeId` | 
| SearchBasedGetCmdsLatency | + `CacheClusterId`, `CacheNodeId` | 
| SearchBasedSetCmds | + `CacheClusterId`, `CacheNodeId` | 
| SearchBasedSetCmdsLatency | + `CacheClusterId`, `CacheNodeId` | 
| SearchNumberOfIndexes | + `CacheClusterId`, `CacheNodeId` | 
| SearchTotalIndexedDocuments | + `CacheClusterId`, `CacheNodeId` | 
| SearchUsedMemoryBytes | + `CacheClusterId`, `CacheNodeId` | 
| SetBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| SetBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| SetTypeCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| SetTypeCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| SlabsMoved | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| SortedSetBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| SortedSetBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| StreamBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| StreamBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| StringBasedCmds | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| StringBasedCmdsLatency | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| SuccessfulReadRequestLatency | + `CacheClusterId`, `CacheNodeId` | 
| SuccessfulWriteRequestLatency | + `CacheClusterId`, `CacheNodeId` | 
| SwapUsage | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| TouchHits | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| TouchMisses | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| TrafficManagementActive | + `CacheClusterId`, `CacheNodeId` | 
| UnusedMemory | + `CacheClusterId`<br />+ `CacheClusterId`, `CacheNodeId` | 
| UsedMemoryDataset | + `CacheClusterId`, `CacheNodeId` | 

### AWS::ElastiCache::ReplicationGroup
<a name="supported-metrics-aws-elasticache-aws-elasticache-replicationgroup"></a>


| Metric | Dimensions | 
| --- | --- | 
| DatabaseCapacityUsageCountedForEvictPercentage | + `NodeGroupId`, `ReplicationGroupId`<br />+ `ReplicationGroupId` | 
| DatabaseMemoryUsageCountedForEvictPercentage | + `NodeGroupId`, `ReplicationGroupId`<br />+ `ReplicationGroupId` | 
| EngineCPUUtilization | + `NodeGroupId`, `ReplicationGroupId`<br />+ `ReplicationGroupId`<br />+ `ReplicationGroupId`, `Role` | 

## AWS/ElasticBeanstalk
<a name="supported-metrics-ns-aws-elasticbeanstalk"></a>

The `AWS/ElasticBeanstalk` namespace includes enriched metrics for the following resource types.
+ [AWS::ElasticBeanstalk::Environment](#supported-metrics-aws-elasticbeanstalk-aws-elasticbeanstalk-environment)

### AWS::ElasticBeanstalk::Environment
<a name="supported-metrics-aws-elasticbeanstalk-aws-elasticbeanstalk-environment"></a>


| Metric | Dimensions | 
| --- | --- | 
| ApplicationLatencyP10 | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationLatencyP50 | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationLatencyP75 | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationLatencyP85 | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationLatencyP90 | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationLatencyP95 | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationLatencyP99 | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationLatencyP99.9 | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationRequests2xx | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationRequests3xx | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationRequests4xx | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationRequests5xx | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| ApplicationRequestsTotal | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 
| CPUIdle | + `EnvironmentName`, `InstanceId` | 
| CPUIowait | + `EnvironmentName`, `InstanceId` | 
| CPUIrq | + `EnvironmentName`, `InstanceId` | 
| CPUNice | + `EnvironmentName`, `InstanceId` | 
| CPUPrivileged | + `EnvironmentName`, `InstanceId` | 
| CPUSoftirq | + `EnvironmentName`, `InstanceId` | 
| CPUSystem | + `EnvironmentName`, `InstanceId` | 
| CPUUser | + `EnvironmentName`, `InstanceId` | 
| EnvironmentHealth | + `EnvironmentName` | 
| InstanceHealth | + `EnvironmentName`, `InstanceId` | 
| InstancesDegraded | + `EnvironmentName` | 
| InstancesInfo | + `EnvironmentName` | 
| InstancesNoData | + `EnvironmentName` | 
| InstancesOk | + `EnvironmentName` | 
| InstancesPending | + `EnvironmentName` | 
| InstancesSevere | + `EnvironmentName` | 
| InstancesUnknown | + `EnvironmentName` | 
| InstancesWarning | + `EnvironmentName` | 
| LoadAverage1min | + `EnvironmentName`, `InstanceId` | 
| LoadAverage5min | + `EnvironmentName`, `InstanceId` | 
| RootFilesystemUtil | + `EnvironmentName`<br />+ `EnvironmentName`, `InstanceId` | 

## AWS/ElasticMapReduce
<a name="supported-metrics-ns-aws-elasticmapreduce"></a>

The `AWS/ElasticMapReduce` namespace includes enriched metrics for the following resource types.
+ [AWS::EMR::Cluster](#supported-metrics-aws-elasticmapreduce-aws-emr-cluster)

### AWS::EMR::Cluster
<a name="supported-metrics-aws-elasticmapreduce-aws-emr-cluster"></a>


| Metric | Dimensions | 
| --- | --- | 
| AppsCompleted | + `JobFlowId` | 
| AppsFailed | + `JobFlowId` | 
| AppsKilled | + `JobFlowId` | 
| AppsPending | + `JobFlowId` | 
| AppsRunning | + `JobFlowId` | 
| AppsSubmitted | + `JobFlowId` | 
| AutoTerminationIsClusterIdle | + `JobFlowId` | 
| ContainerAllocated | + `JobFlowId` | 
| ContainerPending | + `JobFlowId` | 
| ContainerPendingRatio | + `JobFlowId` | 
| ContainerReserved | + `JobFlowId` | 
| CoreNodesPending | + `JobFlowId` | 
| CoreNodesRequested | + `JobFlowId` | 
| CoreNodesRunning | + `JobFlowId` | 
| CoreUnitsRequested | + `JobFlowId` | 
| CoreUnitsRunning | + `JobFlowId` | 
| CoreVCPURequested | + `JobFlowId` | 
| CoreVCPURunning | + `JobFlowId` | 
| HDFSBytesRead | + `JobFlowId`<br />+ `JobFlowId`, `JobId` | 
| HDFSBytesWritten | + `JobFlowId`<br />+ `JobFlowId`, `JobId` | 
| HDFSUtilization | + `JobFlowId` | 
| IsIdle | + `JobFlowId` | 
| JobsFailed | + `JobFlowId` | 
| JobsRunning | + `JobFlowId` | 
| LiveDataNodes | + `JobFlowId` | 
| LiveTaskTrackers | + `JobFlowId` | 
| MRActiveNodes | + `JobFlowId` | 
| MRDecommissionedNodes | + `JobFlowId` | 
| MRLostNodes | + `JobFlowId` | 
| MRTotalNodes | + `JobFlowId` | 
| MRUnhealthyNodes | + `JobFlowId` | 
| MapSlotsOpen | + `JobFlowId` | 
| MapTasksRemaining | + `JobFlowId` | 
| MapTasksRunning | + `JobFlowId` | 
| MissingBlocks | + `JobFlowId` | 
| ReduceSlotsOpen | + `JobFlowId` | 
| ReduceTasksRemaining | + `JobFlowId` | 
| ReduceTasksRunning | + `JobFlowId` | 
| RemainingMapTasksPerSlot | + `JobFlowId` | 
| S3BytesRead | + `JobFlowId`<br />+ `JobFlowId`, `JobId` | 
| S3BytesWritten | + `JobFlowId`<br />+ `JobFlowId`, `JobId` | 
| TaskNodesPending | + `JobFlowId` | 
| TaskNodesRequested | + `JobFlowId` | 
| TaskNodesRunning | + `JobFlowId` | 
| TaskUnitsRequested | + `JobFlowId` | 
| TaskUnitsRunning | + `JobFlowId` | 
| TaskVCPURequested | + `JobFlowId` | 
| TaskVCPURunning | + `JobFlowId` | 
| TotalLoad | + `JobFlowId` | 
| TotalNodesRequested | + `JobFlowId` | 
| TotalNodesRunning | + `JobFlowId` | 
| TotalNotebookKernels | + `JobFlowId` | 
| TotalUnitsRequested | + `JobFlowId` | 
| TotalUnitsRunning | + `JobFlowId` | 
| TotalVCPURequested | + `JobFlowId` | 
| TotalVCPURunning | + `JobFlowId` | 

## AWS/EventBridge/Pipes
<a name="supported-metrics-ns-aws-eventbridge-pipes"></a>

The `AWS/EventBridge/Pipes` namespace includes enriched metrics for the following resource types.
+ [AWS::Pipes::Pipe](#supported-metrics-aws-eventbridge-pipes-aws-pipes-pipe)

### AWS::Pipes::Pipe
<a name="supported-metrics-aws-eventbridge-pipes-aws-pipes-pipe"></a>


| Metric | Dimensions | 
| --- | --- | 
| Duration | + `PipeName` | 
| EnrichmentStageDuration | + `PipeName` | 
| EnrichmentStageFailed | + `PipeName` | 
| EventCount | + `PipeName` | 
| EventSize | + `PipeName` | 
| ExecutionFailed | + `PipeName` | 
| ExecutionPartiallyFailed | + `PipeName` | 
| ExecutionTimeout | + `PipeName` | 
| TargetStageDuration | + `PipeName` | 
| TargetStageFailed | + `PipeName` | 
| TargetStagePartiallyFailed | + `PipeName` | 
| TargetStageSkipped | + `PipeName` | 

## AWS/Events
<a name="supported-metrics-ns-aws-events"></a>

The `AWS/Events` namespace includes enriched metrics for the following resource types.
+ [AWS::Events::Rule](#supported-metrics-aws-events-aws-events-rule)

### AWS::Events::Rule
<a name="supported-metrics-aws-events-aws-events-rule"></a>


| Metric | Dimensions | 
| --- | --- | 
| DeadLetterInvocations | + `EventBusName`, `RuleName`<br />+ `RuleName` | 
| FailedInvocations | + `EventBusName`, `RuleName`<br />+ `RuleName` | 
| IngestiontoInvocationCompleteLatency | + `EventBusName`, `RuleName` | 
| IngestiontoInvocationStartLatency | + `EventBusName`, `RuleName` | 
| Invocations | + `EventBusName`, `RuleName`<br />+ `RuleName` | 
| InvocationsFailedToBeSentToDlq | + `EventBusName`, `RuleName`<br />+ `RuleName` | 
| InvocationsSentToDlq | + `EventBusName`, `RuleName`<br />+ `RuleName` | 
| ThrottledRules | + `EventBusName`, `RuleName`<br />+ `RuleName` | 
| TriggeredRules | + `EventBusName`, `RuleName`<br />+ `RuleName` | 

## AWS/FSx
<a name="supported-metrics-ns-aws-fsx"></a>

The `AWS/FSx` namespace includes enriched metrics for the following resource types.
+ [AWS::FSx::FileSystem](#supported-metrics-aws-fsx-aws-fsx-filesystem)

### AWS::FSx::FileSystem
<a name="supported-metrics-aws-fsx-aws-fsx-filesystem"></a>


| Metric | Dimensions | 
| --- | --- | 
| AgeOfOldestQueuedMessage | + `FileSystemId`, `Publisher` | 
| CPUUtilization | + `FileServer`, `FileSystemId`<br />+ `FileSystemId` | 
| CapacityPoolReadBytes | + `FileSystemId`, `VolumeId` | 
| CapacityPoolReadOperations | + `FileSystemId`, `VolumeId` | 
| CapacityPoolWriteBytes | + `FileSystemId`, `VolumeId` | 
| CapacityPoolWriteOperations | + `FileSystemId`, `VolumeId` | 
| ClientConnections | + `FileSystemId` | 
| CompressionRatio | + `FileSystemId`, `VolumeId` | 
| DataReadBytes | + `FileSystemId`<br />+ `FileSystemId`, `VolumeId` | 
| DataReadOperationTime | + `FileSystemId`, `VolumeId` | 
| DataReadOperations | + `FileSystemId`<br />+ `FileSystemId`, `VolumeId` | 
| DataWriteBytes | + `FileSystemId`<br />+ `FileSystemId`, `VolumeId` | 
| DataWriteLatency | + `FileSystemId`, `StorageTargetId` | 
| DataWriteOperationTime | + `FileSystemId`, `VolumeId` | 
| DataWriteOperations | + `FileSystemId`<br />+ `FileSystemId`, `VolumeId` | 
| DirectoryCreateOperations | + `FileSystemId`, `JobId`, `StorageTargetId`<br />+ `FileSystemId`, `StorageTargetId` | 
| DirectoryDeleteOperations | + `FileSystemId`, `JobId`, `StorageTargetId`<br />+ `FileSystemId`, `StorageTargetId` | 
| DiskIopsExceededCheck | + `FileSystemId`, `StorageTargetId` | 
| DiskIopsUtilization | + `Aggregate`, `FileSystemId`<br />+ `FileSystemId`, `StorageTargetId` | 
| DiskReadBytes | + `Aggregate`, `FileSystemId`<br />+ `FileSystemId`, `StorageTargetId` | 
| DiskReadOperations | + `Aggregate`, `FileSystemId`<br />+ `FileSystemId`, `StorageTargetId` | 
| DiskThroughputBalance | + `FileSystemId` | 
| DiskThroughputExceededCheck | + `FileSystemId`, `StorageTargetId` | 
| DiskThroughputUtilization | + `FileSystemId` | 
| DiskWriteBytes | + `Aggregate`, `FileSystemId`<br />+ `FileSystemId`, `StorageTargetId` | 
| DiskWriteOperations | + `Aggregate`, `FileSystemId`<br />+ `FileSystemId`, `StorageTargetId` | 
| FileCreateOperations | + `FileSystemId`, `JobId`, `StorageTargetId`<br />+ `FileSystemId`, `StorageTargetId` | 
| FileDeleteOperations | + `FileSystemId`, `JobId`, `StorageTargetId`<br />+ `FileSystemId`, `StorageTargetId` | 
| FileOpenOperations | + `FileSystemId`, `JobId`, `StorageTargetId`<br />+ `FileSystemId`, `StorageTargetId` | 
| FileServerCacheHitRatio | + `CacheType`, `FileSystemId`<br />+ `FileServer`, `FileSystemId` | 
| FileServerDiskIopsBalance | + `FileServer`, `FileSystemId`<br />+ `FileSystemId` | 
| FileServerDiskIopsUtilization | + `FileServer`, `FileSystemId`<br />+ `FileSystemId` | 
| FileServerDiskThroughputBalance | + `FileServer`, `FileSystemId` | 
| FileServerDiskThroughputUtilization | + `FileServer`, `FileSystemId`<br />+ `FileSystemId` | 
| FilesCapacity | + `FileSystemId`, `VolumeId` | 
| FilesUsed | + `FileSystemId`, `VolumeId` | 
| FreeDataStorageCapacity | + `FileSystemId`<br />+ `FileSystemId`, `StorageTargetId` | 
| FreeStorageCapacity | + `FileSystemId` | 
| MemoryUtilization | + `FileSystemId` | 
| MetadataOperationTime | + `FileSystemId`, `VolumeId` | 
| MetadataOperations | + `FileSystemId`<br />+ `FileSystemId`, `VolumeId` | 
| NetworkReceivedBytes | + `FileServer`, `FileSystemId` | 
| NetworkSentBytes | + `FileServer`, `FileSystemId` | 
| NetworkThroughputUtilization | + `FileServer`, `FileSystemId`<br />+ `FileSystemId` | 
| RenameOperations | + `FileSystemId`, `JobId`, `StorageTargetId` | 
| RepositoryRenameOperations | + `FileSystemId`, `Publisher` | 
| StatOperations | + `FileSystemId`, `JobId`, `StorageTargetId` | 
| StorageCapacity | + `Aggregate`, `DataType`, `FileSystemId`, `StorageTier`<br />+ `DataType`, `FileSystemId`, `StorageTier`<br />+ `FileSystemId`, `VolumeId` | 
| StorageCapacityUtilization | + `Aggregate`, `DataType`, `FileSystemId`, `StorageTier`<br />+ `DataType`, `FileSystemId`, `StorageTier`<br />+ `DataType`, `FileSystemId`, `StorageTier`, `VolumeId`<br />+ `FileSystemId`, `StorageTargetId`<br />+ `FileSystemId`, `VolumeId` | 
| StorageUsed | + `Aggregate`, `DataType`, `FileSystemId`, `StorageTier`<br />+ `DataType`, `FileSystemId`, `StorageTier`<br />+ `DataType`, `FileSystemId`, `StorageTier`, `VolumeId`<br />+ `FileSystemId`, `VolumeId` | 
| UsedStorageCapacity | + `DataType`, `FileSystemId`, `StorageTier`<br />+ `DataType`, `FileSystemId`, `StorageTier`, `VolumeId`<br />+ `FileSystemId`, `VolumeId` | 

## AWS/Firehose
<a name="supported-metrics-ns-aws-firehose"></a>

The `AWS/Firehose` namespace includes enriched metrics for the following resource types.
+ [AWS::KinesisFirehose::DeliveryStream](#supported-metrics-aws-firehose-aws-kinesisfirehose-deliverystream)

### AWS::KinesisFirehose::DeliveryStream
<a name="supported-metrics-aws-firehose-aws-kinesisfirehose-deliverystream"></a>


| Metric | Dimensions | 
| --- | --- | 
| BackupToS3.Bytes | + `DeliveryStreamName` | 
| BackupToS3.DataFreshness | + `DeliveryStreamName` | 
| BackupToS3.Records | + `DeliveryStreamName` | 
| BackupToS3.Success | + `DeliveryStreamName` | 
| BytesPerSecondLimit | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| DataReadFromKinesisStream.Bytes | + `DeliveryStreamName` | 
| DataReadFromKinesisStream.Records | + `DeliveryStreamName` | 
| DataReadFromSource.Backpressured | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| DataReadFromSource.Bytes | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| DataReadFromSource.Records | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| DeliveryToAmazonOpenSearchServerless.AuthFailure | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchServerless.Bytes | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchServerless.DataFreshness | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchServerless.DeliveryRejected | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchServerless.Records | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchServerless.Success | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchService.AuthFailure | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchService.Bytes | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchService.DataFreshness | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchService.DeliveryRejected | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchService.Records | + `DeliveryStreamName` | 
| DeliveryToAmazonOpenSearchService.Success | + `DeliveryStreamName` | 
| DeliveryToHttpEndpoint.Bytes | + `DeliveryStreamName` | 
| DeliveryToHttpEndpoint.DataFreshness | + `DeliveryStreamName` | 
| DeliveryToHttpEndpoint.ProcessedBytes | + `DeliveryStreamName` | 
| DeliveryToHttpEndpoint.ProcessedRecords | + `DeliveryStreamName` | 
| DeliveryToHttpEndpoint.Records | + `DeliveryStreamName` | 
| DeliveryToHttpEndpoint.Success | + `DeliveryStreamName` | 
| DeliveryToIceberg.Bytes | + `DeliveryStreamName`, `IcebergTableName` | 
| DeliveryToIceberg.DataFreshness | + `DeliveryStreamName`, `IcebergTableName` | 
| DeliveryToIceberg.Success | + `DeliveryStreamName`, `IcebergTableName` | 
| DeliveryToIceberg.SuccessfulRowCount | + `DeliveryStreamName`, `IcebergTableName` | 
| DeliveryToRedshift.Bytes | + `DeliveryStreamName` | 
| DeliveryToRedshift.Records | + `DeliveryStreamName` | 
| DeliveryToRedshift.Success | + `DeliveryStreamName` | 
| DeliveryToS3.Bytes | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| DeliveryToS3.DataFreshness | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| DeliveryToS3.Records | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| DeliveryToS3.Success | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| DeliveryToSnowflake.Bytes | + `DeliveryStreamName` | 
| DeliveryToSnowflake.DataCommitLatency | + `DeliveryStreamName` | 
| DeliveryToSnowflake.DataFreshness | + `DeliveryStreamName` | 
| DeliveryToSnowflake.Records | + `DeliveryStreamName` | 
| DeliveryToSnowflake.Success | + `DeliveryStreamName` | 
| DeliveryToSplunk.Bytes | + `DeliveryStreamName` | 
| DeliveryToSplunk.DataAckLatency | + `DeliveryStreamName` | 
| DeliveryToSplunk.DataFreshness | + `DeliveryStreamName` | 
| DeliveryToSplunk.Records | + `DeliveryStreamName` | 
| DeliveryToSplunk.Success | + `DeliveryStreamName` | 
| DescribeDeliveryStream.Latency | + `DeliveryStreamName` | 
| DescribeDeliveryStream.Requests | + `DeliveryStreamName` | 
| ExecuteProcessing.Duration | + `DeliveryStreamName` | 
| ExecuteProcessing.Success | + `DeliveryStreamName` | 
| FailedConversion.Bytes | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| FailedConversion.Records | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| FailedValidation.Bytes | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| FailedValidation.Records | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| IncomingBytes | + `DeliveryStreamName` | 
| IncomingPutRequests | + `DeliveryStreamName` | 
| IncomingRecords | + `DeliveryStreamName` | 
| KMSKeyAccessDenied | + `DeliveryStreamName` | 
| KMSKeyDisabled | + `DeliveryStreamName` | 
| KMSKeyInvalidState | + `DeliveryStreamName` | 
| KMSKeyNotFound | + `DeliveryStreamName` | 
| KafkaOffsetLag | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| KinesisMillisBehindLatest | + `DeliveryStreamName` | 
| ListDeliveryStreams.Latency | + `DeliveryStreamName` | 
| ListDeliveryStreams.Requests | + `DeliveryStreamName` | 
| OutputDecompressedBytes.Failed | + `DeliveryStreamName` | 
| OutputDecompressedBytes.Success | + `DeliveryStreamName` | 
| OutputDecompressedRecords.Failed | + `DeliveryStreamName` | 
| OutputDecompressedRecords.Success | + `DeliveryStreamName` | 
| PutRecord.Bytes | + `DeliveryStreamName` | 
| PutRecord.Latency | + `DeliveryStreamName` | 
| PutRecord.Requests | + `DeliveryStreamName` | 
| PutRecordBatch.Bytes | + `DeliveryStreamName` | 
| PutRecordBatch.Latency | + `DeliveryStreamName` | 
| PutRecordBatch.Records | + `DeliveryStreamName` | 
| PutRecordBatch.Requests | + `DeliveryStreamName` | 
| PutRequestsPerSecondLimit | + `DeliveryStreamName` | 
| RecordsPerSecondLimit | + `DeliveryStreamName` | 
| SourceThrottled.Delay | + `DeliveryStreamName` | 
| SourceToDelivery.DataFreshness | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| SucceedConversion.Bytes | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| SucceedConversion.Records | + `DeliveryStreamName`<br />+ `DeliveryStreamName`, `SourcePartitionId` | 
| SucceedProcessing.Bytes | + `DeliveryStreamName` | 
| SucceedProcessing.Records | + `DeliveryStreamName` | 
| ThrottledDescribeStream | + `DeliveryStreamName` | 
| ThrottledGetRecords | + `DeliveryStreamName` | 
| ThrottledGetShardIterator | + `DeliveryStreamName` | 
| ThrottledRecords | + `DeliveryStreamName` | 
| UpdateDeliveryStream.Latency | + `DeliveryStreamName` | 
| UpdateDeliveryStream.Requests | + `DeliveryStreamName` | 

## AWS/FraudDetector
<a name="supported-metrics-ns-aws-frauddetector"></a>

The `AWS/FraudDetector` namespace includes enriched metrics for the following resource types.
+ [AWS::FraudDetector::Detector](#supported-metrics-aws-frauddetector-aws-frauddetector-detector)

### AWS::FraudDetector::Detector
<a name="supported-metrics-aws-frauddetector-aws-frauddetector-detector"></a>


| Metric | Dimensions | 
| --- | --- | 
| GetEventPrediction | + `DetectorID` | 
| GetEventPrediction4xxError | + `DetectorID` | 
| GetEventPrediction5xxError | + `DetectorID` | 
| GetEventPredictionLatency | + `DetectorID` | 
| ModelInvocation | + `DetectorID`, `DetectorVersionID`, `ModelEndpoint`<br />+ `DetectorID`, `DetectorVersionID`, `ModelID`, `ModelType`, `ModelVersionNumber` | 
| ModelInvocationError | + `DetectorID`, `DetectorVersionID`, `ModelEndpoint`<br />+ `DetectorID`, `DetectorVersionID`, `ModelID`, `ModelType`, `ModelVersionNumber` | 
| ModelInvocationLatency | + `DetectorID`, `DetectorVersionID`, `ModelEndpoint`<br />+ `DetectorID`, `DetectorVersionID`, `ModelID`, `ModelType`, `ModelVersionNumber` | 
| OutcomeReturned | + `DetectorID`, `DetectorVersionID`, `OutcomeName`<br />+ `DetectorID`, `OutcomeName` | 
| Prediction | + `DetectorID`, `DetectorVersionID` | 
| PredictionError | + `DetectorID`, `DetectorVersionID` | 
| PredictionLatency | + `DetectorID`, `DetectorVersionID` | 
| RuleEvaluateFalse | + `DetectorID`, `DetectorVersionID`, `RuleID` | 
| RuleEvaluateTrue | + `DetectorID`, `DetectorVersionID`, `RuleID` | 
| RuleNotEvaluated | + `DetectorID`, `DetectorVersionID`, `RuleID` | 
| VariableUsed | + `DetectorID`, `DetectorVersionID`, `VariableName` | 

## AWS/GameLift
<a name="supported-metrics-ns-aws-gamelift"></a>

The `AWS/GameLift` namespace includes enriched metrics for the following resource types.
+ [AWS::GameLift::GameSessionQueue](#supported-metrics-aws-gamelift-aws-gamelift-gamesessionqueue)
+ [AWS::GameLift::MatchmakingConfiguration](#supported-metrics-aws-gamelift-aws-gamelift-matchmakingconfiguration)

### AWS::GameLift::GameSessionQueue
<a name="supported-metrics-aws-gamelift-aws-gamelift-gamesessionqueue"></a>


| Metric | Dimensions | 
| --- | --- | 
| AverageWaitTime | + `Location`, `QueueName`<br />+ `QueueName` | 
| FirstChoiceNotViable | + `QueueName` | 
| FirstChoiceOutOfCapacity | + `QueueName` | 
| GameSessionPlaced | + `LocationName`, `QueueName` | 
| LowestLatencyPlacement | + `QueueName` | 
| LowestPricePlacement | + `QueueName` | 
| PlacementApNortheast1 | + `QueueName` | 
| PlacementApNortheast2 | + `QueueName` | 
| PlacementApSouth1 | + `QueueName` | 
| PlacementApSoutheast2 | + `QueueName` | 
| PlacementEuCentral1 | + `QueueName` | 
| PlacementEuNorth1 | + `QueueName` | 
| PlacementEuWest1 | + `QueueName` | 
| PlacementEuWest2 | + `QueueName` | 
| PlacementMeSouth1 | + `QueueName` | 
| PlacementSaEast1 | + `QueueName` | 
| PlacementUsEast1 | + `QueueName` | 
| PlacementUsEast2 | + `QueueName` | 
| PlacementUsWest1 | + `QueueName` | 
| PlacementUsWest2 | + `QueueName` | 
| PlacementsCanceled | + `QueueName` | 
| PlacementsStarted | + `QueueName` | 
| PlacementsSucceeded | + `QueueName` | 
| PlacementsTimedOut | + `QueueName` | 
| QueueDepth | + `Location`, `QueueName`<br />+ `QueueName` | 

### AWS::GameLift::MatchmakingConfiguration
<a name="supported-metrics-aws-gamelift-aws-gamelift-matchmakingconfiguration"></a>


| Metric | Dimensions | 
| --- | --- | 
| CurrentTickets | + `ConfigurationName` | 
| MatchesAccepted | + `ConfigurationName` | 
| MatchesCreated | + `ConfigurationName` | 
| MatchesPlaced | + `ConfigurationName` | 
| MatchesRejected | + `ConfigurationName` | 
| MatchmakingSearchTime | + `ConfigurationName` | 
| PlayersStarted | + `ConfigurationName` | 
| TicketsStarted | + `ConfigurationName` | 
| TicketsTimedOut | + `ConfigurationName` | 
| TimeToMatch | + `ConfigurationName` | 
| TimeToTicketCancel | + `ConfigurationName` | 
| TimeToTicketSuccess | + `ConfigurationName` | 

## AWS/GatewayELB
<a name="supported-metrics-ns-aws-gatewayelb"></a>

The `AWS/GatewayELB` namespace includes enriched metrics for the following resource types.
+ [AWS::ElasticLoadBalancingV2::LoadBalancer](#supported-metrics-aws-gatewayelb-aws-elasticloadbalancingv2-loadbalancer)

### AWS::ElasticLoadBalancingV2::LoadBalancer
<a name="supported-metrics-aws-gatewayelb-aws-elasticloadbalancingv2-loadbalancer"></a>


| Metric | Dimensions | 
| --- | --- | 
| ActiveFlowCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ConsumedLCUs | + `LoadBalancer` | 
| HealthyHostCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| NewFlowCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ProcessedBytes | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| UnHealthyHostCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 

## AWS/IVSChat
<a name="supported-metrics-ns-aws-ivschat"></a>

The `AWS/IVSChat` namespace includes enriched metrics for the following resource types.
+ [AWS::IVSChat::LoggingConfiguration](#supported-metrics-aws-ivschat-aws-ivschat-loggingconfiguration)

### AWS::IVSChat::LoggingConfiguration
<a name="supported-metrics-aws-ivschat-aws-ivschat-loggingconfiguration"></a>


| Metric | Dimensions | 
| --- | --- | 
| LogDestinationAccessDeniedError | + `LoggingConfiguration` | 
| LogDestinationErrors | + `LoggingConfiguration` | 
| LogDestinationResourceNotFoundErrors | + `LoggingConfiguration` | 

## AWS/IoT
<a name="supported-metrics-ns-aws-iot"></a>

The `AWS/IoT` namespace includes enriched metrics for the following resource types.
+ [AWS::IoT::CACertificate](#supported-metrics-aws-iot-aws-iot-cacertificate)
+ [AWS::IoT::ScheduledAudit](#supported-metrics-aws-iot-aws-iot-scheduledaudit)
+ [AWS::IoT::SecurityProfile](#supported-metrics-aws-iot-aws-iot-securityprofile)
+ [AWS::IoT::TopicRule](#supported-metrics-aws-iot-aws-iot-topicrule)

### AWS::IoT::CACertificate
<a name="supported-metrics-aws-iot-aws-iot-cacertificate"></a>


| Metric | Dimensions | 
| --- | --- | 
| ProvisionThing.ClientError | + `CaCertificateId` | 
| ProvisionThing.ServerError | + `CaCertificateId` | 
| ProvisionThing.Success | + `CaCertificateId` | 

### AWS::IoT::ScheduledAudit
<a name="supported-metrics-aws-iot-aws-iot-scheduledaudit"></a>


| Metric | Dimensions | 
| --- | --- | 
| MisconfiguredDeviceDefenderNotification | + `CheckName`, `ScheduledAuditName` | 
| NonCompliantResources | + `CheckName`, `ScheduledAuditName` | 
| ResourcesEvaluated | + `CheckName`, `ScheduledAuditName` | 

### AWS::IoT::SecurityProfile
<a name="supported-metrics-aws-iot-aws-iot-securityprofile"></a>


| Metric | Dimensions | 
| --- | --- | 
| BehaviorEvaluationCompleted | + `BehaviorName`, `SecurityProfileName` | 
| BehaviorEvaluationSkipped | + `BehaviorName`, `SecurityProfileName` | 
| MisconfiguredDeviceDefenderNotification | + `BehaviorName`, `SecurityProfileName` | 
| NumOfMetricsExceedingSizeLimit | + `BehaviorName`, `SecurityProfileName` | 
| NumOfMetricsExported | + `BehaviorName`, `SecurityProfileName` | 
| NumOfMetricsSkipped | + `BehaviorName`, `SecurityProfileName` | 
| Violations | + `BehaviorName`, `SecurityProfileName`<br />+ `SecurityProfileName` | 
| ViolationsCleared | + `BehaviorName`, `SecurityProfileName`<br />+ `SecurityProfileName` | 
| ViolationsInvalidated | + `BehaviorName`, `SecurityProfileName`<br />+ `SecurityProfileName` | 

### AWS::IoT::TopicRule
<a name="supported-metrics-aws-iot-aws-iot-topicrule"></a>


| Metric | Dimensions | 
| --- | --- | 
| ErrorActionFailure | + `ActionType`, `RuleName` | 
| ErrorActionHttpDestinationNotEnabled | + `ActionType`, `RuleName` | 
| ErrorActionSuccess | + `ActionType`, `RuleName` | 
| Failure | + `ActionType`, `RuleName` | 
| HttpCode\_4XX | + `ActionType`, `RuleName` | 
| HttpCode\_5XX | + `ActionType`, `RuleName` | 
| HttpCode\_Other | + `ActionType`, `RuleName` | 
| HttpInvalidUrl | + `ActionType`, `RuleName` | 
| HttpRequestTimeout | + `ActionType`, `RuleName` | 
| HttpUnknownHost | + `ActionType`, `RuleName` | 
| ParseError | + `RuleName` | 
| RequestTimeout | + `ActionType`, `RuleName` | 
| RuleMessageThrottled | + `RuleName` | 
| RuleNotFound | + `RuleName` | 
| RulesExecuted | + `RuleName` | 
| SaslAuthFailed | + `ActionType`, `RuleName` | 
| Success | + `ActionType`, `RuleName` | 
| TopicMatch | + `RuleName` | 

## AWS/KMS
<a name="supported-metrics-ns-aws-kms"></a>

The `AWS/KMS` namespace includes enriched metrics for the following resource types.
+ [AWS::KMS::Key](#supported-metrics-aws-kms-aws-kms-key)

### AWS::KMS::Key
<a name="supported-metrics-aws-kms-aws-kms-key"></a>


| Metric | Dimensions | 
| --- | --- | 
| SecondsUntilKeyMaterialExpiration | + `KeyId` | 

## AWS/Kendra
<a name="supported-metrics-ns-aws-kendra"></a>

The `AWS/Kendra` namespace includes enriched metrics for the following resource types.
+ [AWS::Kendra::DataSource](#supported-metrics-aws-kendra-aws-kendra-datasource)
+ [AWS::Kendra::Index](#supported-metrics-aws-kendra-aws-kendra-index)

### AWS::Kendra::DataSource
<a name="supported-metrics-aws-kendra-aws-kendra-datasource"></a>


| Metric | Dimensions | 
| --- | --- | 
| DataSourceDocumentCount | + `DataSourceId`, `IndexId` | 
| DataSourceSyncRuntime | + `DataSourceId`, `IndexId` | 
| DocumentsCrawled | + `AwsAccountId`, `DataSourceId`, `DataSourceType`, `IndexId`<br />+ `DataSourceId`, `IndexId` | 
| DocumentsFailedToIndex | + `DataSourceId`, `IndexId` | 
| DocumentsIndexed | + `DataSourceId`, `IndexId` | 
| DocumentsSkippedInvalidMetadata | + `DataSourceId`, `IndexId` | 
| DocumentsSkippedNoChange | + `DataSourceId`, `IndexId` | 
| DocumentsSubmittedForDeletion | + `AwsAccountId`, `DataSourceId`, `DataSourceType`, `IndexId`<br />+ `DataSourceId`, `IndexId` | 
| DocumentsSubmittedForDeletionFailed | + `AwsAccountId`, `DataSourceId`, `DataSourceType`, `IndexId`<br />+ `DataSourceId`, `IndexId` | 
| DocumentsSubmittedForIndexing | + `AwsAccountId`, `DataSourceId`, `DataSourceType`, `IndexId`<br />+ `DataSourceId`, `IndexId` | 
| DocumentsSubmittedForIndexingFailed | + `AwsAccountId`, `DataSourceId`, `DataSourceType`, `IndexId`<br />+ `DataSourceId`, `IndexId` | 
| DocumentsWithoutAcl | + `AwsAccountId`, `DataSourceId`, `DataSourceType`, `IndexId` | 
| MetadataFilesCrawled | + `DataSourceId`, `IndexId` | 
| PrincipalGroupsScanned | + `DataSourceId`, `IndexId` | 

### AWS::Kendra::Index
<a name="supported-metrics-aws-kendra-aws-kendra-index"></a>


| Metric | Dimensions | 
| --- | --- | 
| ClickFeedbackSubmittedCount | + `IndexId` | 
| DocumentsFailedToIndex | + `IndexId` | 
| DocumentsIndexed | + `IndexId` | 
| GroupProcessed | + `IndexId` | 
| GroupProcessedButNotPersistent | + `IndexId` | 
| GroupReceived | + `IndexId` | 
| GroupUpdateLatencyInMilliSeconds | + `IndexId` | 
| GroupWithOlderOrderingIdSkipped | + `IndexId` | 
| IndexDocumentCount | + `IndexId` | 
| IndexDocumentStorageSize | + `IndexId` | 
| IndexQueryCount | + `IndexId` | 
| ProvisionedIndexDocumentCount | + `IndexId` | 
| ProvisionedIndexStorageSize | + `IndexId` | 
| RelevantFeedbackSubmittedCount | + `IndexId` | 

## AWS/Kinesis
<a name="supported-metrics-ns-aws-kinesis"></a>

The `AWS/Kinesis` namespace includes enriched metrics for the following resource types.
+ [AWS::Kinesis::Stream](#supported-metrics-aws-kinesis-aws-kinesis-stream)

### AWS::Kinesis::Stream
<a name="supported-metrics-aws-kinesis-aws-kinesis-stream"></a>


| Metric | Dimensions | 
| --- | --- | 
| GetRecords.Bytes | + `StreamName` | 
| GetRecords.IteratorAgeMilliseconds | + `StreamName` | 
| GetRecords.Latency | + `StreamName` | 
| GetRecords.Records | + `StreamName` | 
| GetRecords.Success | + `StreamName` | 
| IncomingBytes | + `ShardId`, `StreamName`<br />+ `StreamName` | 
| IncomingRecords | + `ShardId`, `StreamName`<br />+ `StreamName` | 
| IteratorAgeMilliseconds | + `ShardId`, `StreamName` | 
| OutgoingBytes | + `ShardId`, `StreamName` | 
| OutgoingRecords | + `ShardId`, `StreamName` | 
| PutRecord.Success | + `StreamName` | 
| PutRecords.Bytes | + `StreamName` | 
| PutRecords.Success | + `StreamName` | 
| ReadProvisionedThroughputExceeded | + `ShardId`, `StreamName`<br />+ `StreamName` | 
| SubscribeToShard.RateExceeded | + `ConsumerName`, `StreamName` | 
| SubscribeToShard.Success | + `ConsumerName`, `StreamName` | 
| SubscribeToShardEvent.Bytes | + `ConsumerName`, `StreamName` | 
| SubscribeToShardEvent.MillisBehindLatest | + `ConsumerName`, `StreamName` | 
| SubscribeToShardEvent.Records | + `ConsumerName`, `StreamName` | 
| SubscribeToShardEvent.Success | + `ConsumerName`, `StreamName` | 
| WriteProvisionedThroughputExceeded | + `ShardId`, `StreamName`<br />+ `StreamName` | 

## AWS/KinesisAnalytics
<a name="supported-metrics-ns-aws-kinesisanalytics"></a>

The `AWS/KinesisAnalytics` namespace includes enriched metrics for the following resource types.
+ [AWS::KinesisAnalyticsV2::Application](#supported-metrics-aws-kinesisanalytics-aws-kinesisanalyticsv2-application)

### AWS::KinesisAnalyticsV2::Application
<a name="supported-metrics-aws-kinesisanalytics-aws-kinesisanalyticsv2-application"></a>


| Metric | Dimensions | 
| --- | --- | 
| KPUs | + `Application` | 
| KPUs-Interactive | + `Application` | 
| backPressuredTimeMsPerSecond | + `Application`<br />+ `Application`, `Task`<br />+ `Application`, `Task`, `TaskParallelismIndex` | 
| busyTimeMsPerSecond | + `Application`<br />+ `Application`, `Task`<br />+ `Application`, `Task`, `TaskParallelismIndex` | 
| bytesRequestedPerFetch | + `Application`, `Flow`, `Id`<br />+ `Application`, `Flow`, `Id`, `ShardId` | 
| committedOffsets | + `Application`, `Flow`, `Topic` | 
| containerCPUUtilization | + `Application` | 
| containerDiskUtilization | + `Application` | 
| containerMemoryUtilization | + `Application` | 
| cpuUtilization | + `Application` | 
| currentInputWatermark | + `Application`<br />+ `Application`, `Task`<br />+ `Application`, `Task`, `TaskOperator`<br />+ `Application`, `Task`, `TaskOperator`, `TaskOperatorParallelismIndex`<br />+ `Application`, `Task`, `TaskParallelismIndex` | 
| currentOffsets | + `Application`, `Flow`, `Topic` | 
| currentOutputWatermark | + `Application`<br />+ `Application`, `Task`<br />+ `Application`, `Task`, `TaskOperator`<br />+ `Application`, `Task`, `TaskOperator`, `TaskOperatorParallelismIndex` | 
| downtime | + `Application` | 
| fullRestarts | + `Application` | 
| heapMemoryUtilization | + `Application` | 
| idleTimeMsPerSecond | + `Application`<br />+ `Application`, `Task`<br />+ `Application`, `Task`, `TaskParallelismIndex` | 
| jobmanagerFileDescriptorsMax | + `Application` | 
| jobmanagerFileDescriptorsOpen | + `Application` | 
| jobmanagerHeapMemoryUtilization | + `Application` | 
| jobmanagerMetaspaceMemoryUtilization | + `Application` | 
| lastCheckpointDuration | + `Application` | 
| lastCheckpointSize | + `Application` | 
| managedMemoryTotal | + `Application` | 
| managedMemoryUsed | + `Application` | 
| managedMemoryUtilization | + `Application` | 
| metaspaceMemoryUtilization | + `Application` | 
| millisBehindLatest | + `Application`, `Flow`, `Id`<br />+ `Application`, `Flow`, `Id`, `ShardId` | 
| numLateRecordsDropped | + `Application`<br />+ `Application`, `Task`<br />+ `Application`, `Task`, `TaskOperator`<br />+ `Application`, `Task`, `TaskOperator`, `TaskOperatorParallelismIndex` | 
| numRecordsIn | + `Application`<br />+ `Application`, `Task`<br />+ `Application`, `Task`, `TaskOperator`<br />+ `Application`, `Task`, `TaskOperator`, `TaskOperatorParallelismIndex`<br />+ `Application`, `Task`, `TaskParallelismIndex` | 
| numRecordsInPerSecond | + `Application`<br />+ `Application`, `Task`<br />+ `Application`, `Task`, `TaskOperator`<br />+ `Application`, `Task`, `TaskOperator`, `TaskOperatorParallelismIndex`<br />+ `Application`, `Task`, `TaskParallelismIndex` | 
| numRecordsOut | + `Application`<br />+ `Application`, `Task`<br />+ `Application`, `Task`, `TaskOperator`<br />+ `Application`, `Task`, `TaskOperator`, `TaskOperatorParallelismIndex`<br />+ `Application`, `Task`, `TaskParallelismIndex` | 
| numRecordsOutPerSecond | + `Application`<br />+ `Application`, `Task`<br />+ `Application`, `Task`, `TaskOperator`<br />+ `Application`, `Task`, `TaskOperator`, `TaskOperatorParallelismIndex`<br />+ `Application`, `Task`, `TaskParallelismIndex` | 
| numRestarts | + `Application` | 
| numberOfFailedCheckpoints | + `Application` | 
| oldGenerationGCCount | + `Application` | 
| oldGenerationGCTime | + `Application` | 
| taskmanagerFileDescriptorsMax | + `Application` | 
| taskmanagerFileDescriptorsOpen | + `Application` | 
| threadCount | + `Application` | 
| threadsCount | + `Application` | 
| uptime | + `Application` | 
| zeppelinCpuUtilization | + `Application` | 
| zeppelinHeapMemoryUtilization | + `Application` | 
| zeppelinServerUptime | + `Application` | 
| zeppelinThreadCount | + `Application` | 
| zeppelinWaitingJobs | + `Application` | 

## AWS/Lambda
<a name="supported-metrics-ns-aws-lambda"></a>

The `AWS/Lambda` namespace includes enriched metrics for the following resource types.
+ [AWS::Lambda::EventSourceMapping](#supported-metrics-aws-lambda-aws-lambda-eventsourcemapping)
+ [AWS::Lambda::Function](#supported-metrics-aws-lambda-aws-lambda-function)

### AWS::Lambda::EventSourceMapping
<a name="supported-metrics-aws-lambda-aws-lambda-eventsourcemapping"></a>


| Metric | Dimensions | 
| --- | --- | 
| CommittedEventCount | + `EventSourceMappingUUID` | 
| DeletedEventCount | + `EventSourceMappingUUID` | 
| DroppedEventCount | + `EventSourceMappingUUID` | 
| EventPollerThroughputInBytes | + `EventSourceMappingUUID` | 
| EventPollerUnit | + `EventSourceMappingUUID` | 
| FailedInvokeEventCount | + `EventSourceMappingUUID` | 
| FilteredOutEventCount | + `EventSourceMappingUUID` | 
| InvokedEventCount | + `EventSourceMappingUUID` | 
| IteratorAge | + `EventSourceMappingUUID` | 
| MaxOffsetLag | + `EventSourceMappingUUID` | 
| OnFailureDestinationDeliveredEventCount | + `EventSourceMappingUUID` | 
| PolledEventCount | + `EventSourceMappingUUID` | 
| ProvisionedPollers | + `EventSourceMappingUUID` | 
| SumOffsetLag | + `EventSourceMappingUUID` | 

### AWS::Lambda::Function
<a name="supported-metrics-aws-lambda-aws-lambda-function"></a>


| Metric | Dimensions | 
| --- | --- | 
| AsyncEventAge | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| AsyncEventsDropped | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| AsyncEventsReceived | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| CPUThrottles | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| ConcurrencyThrottles | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| ConcurrentExecutions | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DeadLetterErrors | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DestinationDeliveryFailures | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DiskThrottles | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DurableExecutionDuration | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DurableExecutionFailed | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DurableExecutionOperations | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DurableExecutionStarted | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DurableExecutionStopped | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DurableExecutionStorageWrittenBytes | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DurableExecutionSucceeded | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| DurableExecutionTimedOut | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| Duration | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| Errors | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| Invocations | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| IteratorAge | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| MemoryThrottles | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| OffsetLag | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| PostRuntimeExtensionsDuration | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| ProvisionedConcurrencyInvocations | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| ProvisionedConcurrencySpilloverInvocations | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| ProvisionedConcurrencyUtilization | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| ProvisionedConcurrentExecutions | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| RecursiveInvocationsDropped | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| SignatureValidationErrors | + `FunctionName`<br />+ `FunctionName`, `Resource` | 
| StreamedOutboundBytes | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| StreamedOutboundThroughput | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| Throttles | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| TimeToFirstByteLatency | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| TimeToLastByteLatency | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| Url4xxCount | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| Url5xxCount | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| UrlRequestCount | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 
| UrlRequestLatency | + `ExecutedVersion`, `FunctionName`, `Resource`<br />+ `FunctionName`<br />+ `FunctionName`, `Resource` | 

## AWS/MediaTailor
<a name="supported-metrics-ns-aws-mediatailor"></a>

The `AWS/MediaTailor` namespace includes enriched metrics for the following resource types.
+ [AWS::MediaTailor::Channel](#supported-metrics-aws-mediatailor-aws-mediatailor-channel)

### AWS::MediaTailor::Channel
<a name="supported-metrics-aws-mediatailor-aws-mediatailor-channel"></a>


| Metric | Dimensions | 
| --- | --- | 
| 4xxErrorCount | + `Channel`<br />+ `Channel`, `Output` | 
| 5xxErrorCount | + `Channel`<br />+ `Channel`, `Output` | 
| RequestCount | + `Channel`<br />+ `Channel`, `Output` | 
| TotalTime | + `Channel`<br />+ `Channel`, `Output` | 

## AWS/MemoryDB
<a name="supported-metrics-ns-aws-memorydb"></a>

The `AWS/MemoryDB` namespace includes enriched metrics for the following resource types.
+ [AWS::MemoryDB::Cluster](#supported-metrics-aws-memorydb-aws-memorydb-cluster)

### AWS::MemoryDB::Cluster
<a name="supported-metrics-aws-memorydb-aws-memorydb-cluster"></a>


| Metric | Dimensions | 
| --- | --- | 
| ActiveDefragHits | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| AuthenticationFailures | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| BytesReadFromDisk | + `ClusterName`, `NodeName` | 
| BytesUsedForMemoryDB | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| BytesWrittenToDisk | + `ClusterName`, `NodeName` | 
| CPUUtilization | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| ChannelAuthorizationFailures | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| CommandAuthorizationFailures | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| CurrConnections | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| CurrItems | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| DB0AverageTTL | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| DatabaseCapacityUsagePercentage | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| DatabaseMemoryUsagePercentage | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| EngineCPUUtilization | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| ErrorCount | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| EvalBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| Evictions | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| FreeableMemory | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| GetTypeCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| HashBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| IamAuthenticationExpirations | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| IamAuthenticationThrottling | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| IsPrimary | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| JsonBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| JsonBasedGetCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| JsonBasedSetCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| KeyAuthorizationFailures | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| KeyBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| KeysTracked | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| KeyspaceHits | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| KeyspaceMisses | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| ListBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| MaxReplicationThroughput | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| MemoryFragmentationRatio | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkBandwidthInAllowanceExceeded | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkBandwidthOutAllowanceExceeded | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkBytesIn | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkBytesOut | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkConntrackAllowanceExceeded | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkMaxBytesIn | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkMaxBytesOut | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkMaxPacketsIn | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkMaxPacketsOut | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkPacketsIn | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkPacketsOut | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NetworkPacketsPerSecondAllowanceExceeded | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NewConnections | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NonKeyTypeCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NumItemsReadFromDisk | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| NumItemsWrittenToDisk | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| PrimaryLinkHealthStatus | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| PubSubBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| Reclaimed | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| ReplicationBytes | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| ReplicationDelayedWriteCommands | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| ReplicationLag | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SearchBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SearchBasedGetCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SearchBasedSetCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SearchNumberOfIndexedKeys | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SearchNumberOfIndexes | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SearchTotalIndexSize | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SetBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SetTypeCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SortedSetBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| StreamBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| StringBasedCmds | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SuccessfulReadRequestLatency | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SuccessfulWriteRequestLatency | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 
| SwapUsage | + `ClusterName`<br />+ `ClusterName`, `NodeName` | 

## AWS/NATGateway
<a name="supported-metrics-ns-aws-natgateway"></a>

The `AWS/NATGateway` namespace includes enriched metrics for the following resource types.
+ [AWS::EC2::NatGateway](#supported-metrics-aws-natgateway-aws-ec2-natgateway)

### AWS::EC2::NatGateway
<a name="supported-metrics-aws-natgateway-aws-ec2-natgateway"></a>


| Metric | Dimensions | 
| --- | --- | 
| ActiveConnectionCount | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| BytesInFromDestination | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| BytesInFromSource | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| BytesOutToDestination | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| BytesOutToSource | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| ConnectionAttemptCount | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| ConnectionEstablishedCount | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| ErrorPortAllocation | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| IdleTimeoutCount | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| PacketsDropCount | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| PacketsInFromDestination | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| PacketsInFromSource | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| PacketsOutToDestination | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| PacketsOutToSource | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| PeakBytesPerSecond | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 
| PeakPacketsPerSecond | + `AvailabilityZone`, `NatGatewayId`<br />+ `NatGatewayId` | 

## AWS/NetworkELB
<a name="supported-metrics-ns-aws-networkelb"></a>

The `AWS/NetworkELB` namespace includes enriched metrics for the following resource types.
+ [AWS::ElasticLoadBalancingV2::LoadBalancer](#supported-metrics-aws-networkelb-aws-elasticloadbalancingv2-loadbalancer)

### AWS::ElasticLoadBalancingV2::LoadBalancer
<a name="supported-metrics-aws-networkelb-aws-elasticloadbalancingv2-loadbalancer"></a>


| Metric | Dimensions | 
| --- | --- | 
| ActiveFlowCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| ActiveFlowCount\_TCP | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| ActiveFlowCount\_TLS | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer` | 
| ActiveFlowCount\_UDP | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| ActiveZonalShiftHostCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| ClientTLSNegotiationErrorCount | + `LoadBalancer` | 
| ConsumedLCUs | + `LoadBalancer` | 
| ConsumedLCUs\_TCP | + `LoadBalancer` | 
| ConsumedLCUs\_TLS | + `LoadBalancer` | 
| ConsumedLCUs\_UDP | + `LoadBalancer` | 
| HealthyHostCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 
| NewFlowCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| NewFlowCount\_TCP | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| NewFlowCount\_TLS | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer` | 
| NewFlowCount\_UDP | + `AvailabilityZone`, `LoadBalancer`<br />+ `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`<br />+ `LoadBalancer`, `TargetGroup` | 
| PeakPacketsPerSecond | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| PortAllocationErrorCount | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ProcessedBytes | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ProcessedBytes\_TCP | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ProcessedBytes\_TLS | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ProcessedBytes\_UDP | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| ProcessedPackets | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TCP\_Client\_Reset\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TCP\_ELB\_Reset\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TCP\_Target\_Reset\_Count | + `AvailabilityZone`, `LoadBalancer`<br />+ `LoadBalancer` | 
| TargetTLSNegotiationErrorCount | + `LoadBalancer` | 
| UnHealthyHostCount | + `AvailabilityZone`, `LoadBalancer`, `TargetGroup`<br />+ `LoadBalancer`, `TargetGroup` | 

## AWS/NetworkFirewall
<a name="supported-metrics-ns-aws-networkfirewall"></a>

The `AWS/NetworkFirewall` namespace includes enriched metrics for the following resource types.
+ [AWS::NetworkFirewall::Firewall](#supported-metrics-aws-networkfirewall-aws-networkfirewall-firewall)

### AWS::NetworkFirewall::Firewall
<a name="supported-metrics-aws-networkfirewall-aws-networkfirewall-firewall"></a>


| Metric | Dimensions | 
| --- | --- | 
| DroppedPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| InvalidDroppedPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| OtherDroppedPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| Packets | + `AvailabilityZone`, `CustomAction`, `Engine`, `FirewallName` | 
| PassedPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| ReceivedPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| RejectedPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| StreamExceptionPolicyPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| TLSDroppedPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| TLSErrors | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| TLSPassedPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| TLSReceivedPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| TLSRejectedPackets | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| TLSRevocationStatusOKConnections | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| TLSRevocationStatusRevokedConnections | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| TLSRevocationStatusUnknownConnections | + `AvailabilityZone`, `Engine`, `FirewallName` | 
| TLSTimedOutConnections | + `AvailabilityZone`, `Engine`, `FirewallName` | 

## AWS/Prometheus
<a name="supported-metrics-ns-aws-prometheus"></a>

The `AWS/Prometheus` namespace includes enriched metrics for the following resource types.
+ [AWS::APS::RuleGroupsNamespace](#supported-metrics-aws-prometheus-aws-aps-rulegroupsnamespace)
+ [AWS::APS::Workspace](#supported-metrics-aws-prometheus-aws-aps-workspace)

### AWS::APS::RuleGroupsNamespace
<a name="supported-metrics-aws-prometheus-aws-aps-rulegroupsnamespace"></a>


| Metric | Dimensions | 
| --- | --- | 
| RuleEvaluationFailures | + `RuleGroup`, `Workspace` | 
| RuleEvaluations | + `RuleGroup`, `Workspace` | 
| RuleGroupIterationsMissed | + `RuleGroup`, `Workspace` | 
| RuleGroupLastEvaluationDuration | + `RuleGroup`, `Workspace` | 

### AWS::APS::Workspace
<a name="supported-metrics-aws-prometheus-aws-aps-workspace"></a>


| Metric | Dimensions | 
| --- | --- | 
| ActiveSeriesLimitPerLabelSet | + `LabelSet`, `Workspace` | 
| ActiveSeriesPerLabelSet | + `LabelSet`, `Workspace` | 
| AlertManagerAlertsReceived | + `Workspace` | 
| AlertManagerNotificationsFailed | + `Workspace` | 
| AlertManagerNotificationsFailedByIntegration | + `Workspace` | 
| AlertManagerNotificationsThrottled | + `Workspace` | 
| AlertManagerNotificationsThrottledByIntegration | + `Workspace` | 
| DiscardedSamples | + `Reason`, `Workspace` | 
| DiscardedSamplesPerLabelSet | + `LabelSet`, `Reason`, `Workspace` | 
| DiscardedSeries | + `Reason`, `Workspace` | 
| DiscardedSeriesPerLabelSet | + `LabelSet`, `Reason`, `Workspace` | 
| IngestionRatePerLabelSet | + `LabelSet`, `Workspace` | 
| QuerySamplesProcessed | + `Workspace` | 
| SecretFetchFailure | + `Workspace` | 

## AWS/RDS
<a name="supported-metrics-ns-aws-rds"></a>

The `AWS/RDS` namespace includes enriched metrics for the following resource types.
+ [AWS::RDS::DBCluster](#supported-metrics-aws-rds-aws-rds-dbcluster)
+ [AWS::RDS::DBInstance](#supported-metrics-aws-rds-aws-rds-dbinstance)

### AWS::RDS::DBCluster
<a name="supported-metrics-aws-rds-aws-rds-dbcluster"></a>


| Metric | Dimensions | 
| --- | --- | 
| AbortedClients | + `DBClusterIdentifier`, `Role` | 
| ActiveTransactions | + `DBClusterIdentifier`, `Role` | 
| AuroraBinlogReplicaLag | + `DBClusterIdentifier`, `Role` | 
| AuroraDMLRejectedMasterFull | + `DBClusterIdentifier`, `Role` | 
| AuroraReplicaLagMaximum | + `DBClusterIdentifier`, `Role` | 
| AuroraReplicaLagMinimum | + `DBClusterIdentifier`, `Role` | 
| AuroraVolumeBytesLeftTotal | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_attempted | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_executed | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_failed | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_in\_progress | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_column\_bit | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_column\_geometry | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_column\_lob | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_column\_virtual | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_custom\_charset | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_fast\_ddl | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_index\_hint | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_long\_trx | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_range\_scan | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_small\_table | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_temporary\_table | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts | + `DBClusterIdentifier`, `Role` | 
| Aurora\_pq\_request\_throttled | + `DBClusterIdentifier`, `Role` | 
| BlockedTransactions | + `DBClusterIdentifier`, `Role` | 
| BufferCacheHitRatio | + `DBClusterIdentifier`, `Role` | 
| CPUUtilization | + `DBClusterIdentifier`<br />+ `DBClusterIdentifier`, `Role` | 
| CommitLatency | + `DBClusterIdentifier`, `Role` | 
| CommitThroughput | + `DBClusterIdentifier`, `Role` | 
| ConnectionAttempts | + `DBClusterIdentifier`, `Role` | 
| DDLLatency | + `DBClusterIdentifier`, `Role` | 
| DDLThroughput | + `DBClusterIdentifier`, `Role` | 
| DMLLatency | + `DBClusterIdentifier`, `Role` | 
| DMLThroughput | + `DBClusterIdentifier`, `Role` | 
| DatabaseConnections | + `DBClusterIdentifier`<br />+ `DBClusterIdentifier`, `Role` | 
| Deadlocks | + `DBClusterIdentifier`, `Role` | 
| DeleteLatency | + `DBClusterIdentifier`, `Role` | 
| DeleteThroughput | + `DBClusterIdentifier`, `Role` | 
| DiskQueueDepth | + `DBClusterIdentifier`, `Role` | 
| EBSByteBalance% | + `DBClusterIdentifier`, `Role` | 
| EBSIOBalance% | + `DBClusterIdentifier`, `Role` | 
| EngineUptime | + `DBClusterIdentifier`, `Role` | 
| ForwardingMasterDMLLatency | + `DBClusterIdentifier`, `Role` | 
| ForwardingMasterDMLThroughput | + `DBClusterIdentifier`, `Role` | 
| ForwardingMasterOpenSessions | + `DBClusterIdentifier`, `Role` | 
| ForwardingReplicaDMLLatency | + `DBClusterIdentifier`, `Role` | 
| ForwardingReplicaDMLThroughput | + `DBClusterIdentifier`, `Role` | 
| ForwardingReplicaOpenSessions | + `DBClusterIdentifier`, `Role` | 
| ForwardingReplicaReadWaitLatency | + `DBClusterIdentifier`, `Role` | 
| ForwardingReplicaReadWaitThroughput | + `DBClusterIdentifier`, `Role` | 
| ForwardingReplicaSelectLatency | + `DBClusterIdentifier`, `Role` | 
| ForwardingReplicaSelectThroughput | + `DBClusterIdentifier`, `Role` | 
| FreeLocalStorage | + `DBClusterIdentifier`, `Role` | 
| FreeStorageSpace | + `DBClusterIdentifier` | 
| FreeableMemory | + `DBClusterIdentifier`<br />+ `DBClusterIdentifier`, `Role` | 
| InsertLatency | + `DBClusterIdentifier`, `Role` | 
| InsertThroughput | + `DBClusterIdentifier`, `Role` | 
| LoginFailures | + `DBClusterIdentifier`, `Role` | 
| NetworkReceiveThroughput | + `DBClusterIdentifier`, `Role` | 
| NetworkThroughput | + `DBClusterIdentifier`, `Role` | 
| NetworkTransmitThroughput | + `DBClusterIdentifier`, `Role` | 
| NumBinaryLogFiles | + `DBClusterIdentifier`, `Role` | 
| PurgeBoundary | + `DBClusterIdentifier`, `Role` | 
| PurgeFinishedPoint | + `DBClusterIdentifier`, `Role` | 
| Queries | + `DBClusterIdentifier`, `Role` | 
| ReadIOPS | + `DBClusterIdentifier`<br />+ `DBClusterIdentifier`, `Role` | 
| ReadLatency | + `DBClusterIdentifier`<br />+ `DBClusterIdentifier`, `Role` | 
| ReadThroughput | + `DBClusterIdentifier`<br />+ `DBClusterIdentifier`, `Role` | 
| ResultSetCacheHitRatio | + `DBClusterIdentifier`, `Role` | 
| RollbackSegmentHistoryListLength | + `DBClusterIdentifier`, `Role` | 
| RowLockTime | + `DBClusterIdentifier`, `Role` | 
| SelectLatency | + `DBClusterIdentifier`, `Role` | 
| SelectThroughput | + `DBClusterIdentifier`, `Role` | 
| StorageNetworkReceiveThroughput | + `DBClusterIdentifier`, `Role` | 
| StorageNetworkThroughput | + `DBClusterIdentifier`, `Role` | 
| StorageNetworkTransmitThroughput | + `DBClusterIdentifier`, `Role` | 
| SumBinaryLogSize | + `DBClusterIdentifier`, `Role` | 
| SwapUsage | + `DBClusterIdentifier`, `Role` | 
| TruncateFinishedPoint | + `DBClusterIdentifier`, `Role` | 
| UpdateLatency | + `DBClusterIdentifier`, `Role` | 
| UpdateThroughput | + `DBClusterIdentifier`, `Role` | 
| VolumeBytesUsed | + `DbClusterIdentifier`, `EngineName` | 
| VolumeReadIOPs | + `DbClusterIdentifier`, `EngineName` | 
| VolumeWriteIOPs | + `DbClusterIdentifier`, `EngineName` | 
| WriteIOPS | + `DBClusterIdentifier`<br />+ `DBClusterIdentifier`, `Role` | 
| WriteLatency | + `DBClusterIdentifier`<br />+ `DBClusterIdentifier`, `Role` | 
| WriteThroughput | + `DBClusterIdentifier`<br />+ `DBClusterIdentifier`, `Role` | 

### AWS::RDS::DBInstance
<a name="supported-metrics-aws-rds-aws-rds-dbinstance"></a>


| Metric | Dimensions | 
| --- | --- | 
| CPUUtilization | + `DBInstanceIdentifier` | 
| DatabaseConnections | + `DBInstanceIdentifier` | 
| FreeStorageSpace | + `DBInstanceIdentifier` | 
| FreeableMemory | + `DBInstanceIdentifier` | 
| ReadIOPS | + `DBInstanceIdentifier` | 
| ReadLatency | + `DBInstanceIdentifier` | 
| ReadThroughput | + `DBInstanceIdentifier` | 
| WriteIOPS | + `DBInstanceIdentifier` | 
| WriteLatency | + `DBInstanceIdentifier` | 
| WriteThroughput | + `DBInstanceIdentifier` | 

## AWS/RUM
<a name="supported-metrics-ns-aws-rum"></a>

The `AWS/RUM` namespace includes enriched metrics for the following resource types.
+ [AWS::RUM::AppMonitor](#supported-metrics-aws-rum-aws-rum-appmonitor)

### AWS::RUM::AppMonitor
<a name="supported-metrics-aws-rum-aws-rum-appmonitor"></a>


| Metric | Dimensions | 
| --- | --- | 
| Http4xxCount | + `application_name` | 
| Http5xxCount | + `application_name` | 
| HttpStatusCodeCount | + `application_name`, `event_details.response.status`, `event_type` | 
| JsErrorCount | + `application_name` | 
| NavigationFrustratedTransaction | + `application_name` | 
| NavigationSatisfiedTransaction | + `application_name` | 
| NavigationToleratedTransaction | + `application_name` | 
| PageViewCount | + `application_name` | 
| PerformanceNavigationDuration | + `application_name` | 
| PerformanceResourceDuration | + `application_name`, `event_details.file.type`, `event_type` | 
| RumEventPayloadSize | + `application_name` | 
| SessionCount | + `application_name` | 
| WebVitalsCumulativeLayoutShift | + `application_name` | 
| WebVitalsFirstInputDelay | + `application_name` | 
| WebVitalsLargestContentfulPaint | + `application_name` | 

## AWS/Redshift
<a name="supported-metrics-ns-aws-redshift"></a>

The `AWS/Redshift` namespace includes enriched metrics for the following resource types.
+ [AWS::Redshift::Cluster](#supported-metrics-aws-redshift-aws-redshift-cluster)

### AWS::Redshift::Cluster
<a name="supported-metrics-aws-redshift-aws-redshift-cluster"></a>


| Metric | Dimensions | 
| --- | --- | 
| CPUUtilization | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| CommitQueueLength | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| ConcurrencyScalingActiveClusters | + `ClusterIdentifier` | 
| ConcurrencyScalingSeconds | + `ClusterIdentifier` | 
| DatabaseConnections | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| HealthStatus | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| MaintenanceMode | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| MaxConfiguredConcurrencyScalingClusters | + `ClusterIdentifier` | 
| NetworkReceiveThroughput | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| NetworkTransmitThroughput | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| NumExceededSchemaQuotas | + `ClusterIdentifier` | 
| PercentageDiskSpaceUsed | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| QueriesCompletedPerSecond | + `ClusterIdentifier`, `NodeID`, `latency`<br />+ `ClusterIdentifier`, `latency` | 
| QueryDuration | + `ClusterIdentifier`, `NodeID`, `latency`<br />+ `ClusterIdentifier`, `latency` | 
| QueryRuntimeBreakdown | + `ClusterIdentifier`, `NodeID`, `stage`<br />+ `ClusterIdentifier`, `stage` | 
| ReadIOPS | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| ReadLatency | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| ReadThroughput | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| RedshiftManagedStorageTotalCapacity | + `ClusterIdentifier` | 
| TotalTableCount | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| WLMQueriesCompletedPerSecond | + `ClusterIdentifier`, `NodeID`, `wlmid`<br />+ `ClusterIdentifier`, `QueueName`<br />+ `ClusterIdentifier`, `wlmid` | 
| WLMQueryDuration | + `ClusterIdentifier`, `NodeID`, `wlmid`<br />+ `ClusterIdentifier`, `QueueName`<br />+ `ClusterIdentifier`, `wlmid` | 
| WLMQueueLength | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID`<br />+ `ClusterIdentifier`, `NodeID`, `QueueName`<br />+ `ClusterIdentifier`, `NodeID`, `service class`<br />+ `ClusterIdentifier`, `QueueName`<br />+ `ClusterIdentifier`, `service class` | 
| WLMQueueWaitTime | + `ClusterIdentifier`, `QueryPriority`<br />+ `ClusterIdentifier`, `QueueName`<br />+ `ClusterIdentifier`, `wlmid` | 
| WLMRunningQueries | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `QueueName`<br />+ `ClusterIdentifier`, `wlmid` | 
| WriteIOPS | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| WriteLatency | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 
| WriteThroughput | + `ClusterIdentifier`<br />+ `ClusterIdentifier`, `NodeID` | 

## AWS/Route53
<a name="supported-metrics-ns-aws-route53"></a>

The `AWS/Route53` namespace includes enriched metrics for the following resource types.
+ [AWS::Route53::HealthCheck](#supported-metrics-aws-route53-aws-route53-healthcheck)

### AWS::Route53::HealthCheck
<a name="supported-metrics-aws-route53-aws-route53-healthcheck"></a>


| Metric | Dimensions | 
| --- | --- | 
| ChildHealthCheckHealthyCount | + `HealthCheckId` | 
| ConnectionTime | + `HealthCheckId`<br />+ `HealthCheckId`, `Region` | 
| HealthCheckPercentageHealthy | + `HealthCheckId` | 
| HealthCheckStatus | + `HealthCheckId` | 
| SSLHandshakeTime | + `HealthCheckId`<br />+ `HealthCheckId`, `Region` | 
| TimeToFirstByte | + `HealthCheckId`<br />+ `HealthCheckId`, `Region` | 

## AWS/Route53Resolver
<a name="supported-metrics-ns-aws-route53resolver"></a>

The `AWS/Route53Resolver` namespace includes enriched metrics for the following resource types.
+ [AWS::Route53Resolver::FirewallRuleGroup](#supported-metrics-aws-route53resolver-aws-route53resolver-firewallrulegroup)
+ [AWS::Route53Resolver::ResolverEndpoint](#supported-metrics-aws-route53resolver-aws-route53resolver-resolverendpoint)

### AWS::Route53Resolver::FirewallRuleGroup
<a name="supported-metrics-aws-route53resolver-aws-route53resolver-firewallrulegroup"></a>


| Metric | Dimensions | 
| --- | --- | 
| FirewallRuleGroupQueryVolume | + `FirewallRuleGroupId` | 
| FirewallRuleGroupVpcQueryVolume | + `FirewallRuleGroupId`, `VpcId` | 

### AWS::Route53Resolver::ResolverEndpoint
<a name="supported-metrics-aws-route53resolver-aws-route53resolver-resolverendpoint"></a>


| Metric | Dimensions | 
| --- | --- | 
| AverageResponseTime | + `EndpointId`, `RniId` | 
| CapacityUsage\_BETA | + `EndpointId`, `RniId` | 
| ConntrackUtilization | + `EndpointId`, `RniId` | 
| EndpointHealthyENICount | + `EndpointId` | 
| EndpointUnhealthyENICount | + `EndpointId` | 
| FormErrCount | + `EndpointId`, `RniId` | 
| FormErrorQueries | + `EndpointId`, `RniId` | 
| InboundQueryVolume | + `EndpointId` | 
| NXDomainCount | + `EndpointId`, `RniId` | 
| NoErrorCount | + `EndpointId`, `RniId` | 
| NxDomainQueries | + `EndpointId`, `RniId` | 
| OutboundQueryAggregateVolume | + `EndpointId` | 
| OutboundQueryVolume | + `EndpointId` | 
| P90ResponseTime | + `EndpointID`, `TargetNameServerIP`<br />+ `EndpointId`, `RniId` | 
| RefusedCount | + `EndpointId`, `RniId` | 
| RefusedQueries | + `EndpointId`, `RniId` | 
| ReplyCount | + `EndpointId`, `RniId` | 
| RequestQueries | + `EndpointID`, `TargetNameServerIP` | 
| ResolverEndpointCapacityStatus | + `EndpointId` | 
| ServFailQueries | + `EndpointId`, `RniId` | 
| ServfailCount | + `EndpointId`, `RniId` | 
| TimeoutCount | + `EndpointId`, `RniId` | 
| TimeoutQueries | + `EndpointID`, `TargetNameServerIP`<br />+ `EndpointId`, `RniId` | 
| tcpRequestCount | + `EndpointId`, `RniId` | 
| udpRequestCount | + `EndpointId`, `RniId` | 

## AWS/S3
<a name="supported-metrics-ns-aws-s3"></a>

The `AWS/S3` namespace includes enriched metrics for the following resource types.
+ [AWS::S3::Bucket](#supported-metrics-aws-s3-aws-s3-bucket)

### AWS::S3::Bucket
<a name="supported-metrics-aws-s3-aws-s3-bucket"></a>


| Metric | Dimensions | 
| --- | --- | 
| 4xxErrors | + `BucketName`, `FilterId` | 
| 5xxErrors | + `BucketName`, `FilterId` | 
| AllRequests | + `BucketName`, `FilterId` | 
| BucketSizeBytes | + `BucketName`, `StorageType` | 
| BytesDownloaded | + `BucketName`, `FilterId` | 
| BytesUploaded | + `BucketName`, `FilterId` | 
| DeleteRequests | + `BucketName`, `FilterId` | 
| FirstByteLatency | + `BucketName`, `FilterId` | 
| GetRequests | + `BucketName`, `FilterId` | 
| HeadRequests | + `BucketName`, `FilterId` | 
| ListRequests | + `BucketName`, `FilterId` | 
| NumberOfObjects | + `BucketName`, `StorageType` | 
| PostRequests | + `BucketName`, `FilterId` | 
| PutRequests | + `BucketName`, `FilterId` | 
| TotalRequestLatency | + `BucketName`, `FilterId` | 

## AWS/SNS
<a name="supported-metrics-ns-aws-sns"></a>

The `AWS/SNS` namespace includes enriched metrics for the following resource types.
+ [AWS::SNS::Topic](#supported-metrics-aws-sns-aws-sns-topic)

### AWS::SNS::Topic
<a name="supported-metrics-aws-sns-aws-sns-topic"></a>


| Metric | Dimensions | 
| --- | --- | 
| NumberOfMessagesPublished | + `TopicName` | 
| NumberOfNotificationsDelivered | + `TopicName` | 
| NumberOfNotificationsFailed | + `TopicName` | 
| PublishSize | + `TopicName` | 

## AWS/SQS
<a name="supported-metrics-ns-aws-sqs"></a>

The `AWS/SQS` namespace includes enriched metrics for the following resource types.
+ [AWS::SQS::Queue](#supported-metrics-aws-sqs-aws-sqs-queue)

### AWS::SQS::Queue
<a name="supported-metrics-aws-sqs-aws-sqs-queue"></a>


| Metric | Dimensions | 
| --- | --- | 
| ApproximateAgeOfOldestMessage | + `QueueName` | 
| ApproximateAgeOfOldestMessageInQuietGroups | + `QueueName` | 
| ApproximateNumberOfGroupsWithInflightMessages | + `QueueName` | 
| ApproximateNumberOfMessagesDelayed | + `QueueName` | 
| ApproximateNumberOfMessagesDelayedInQuietGroups | + `QueueName` | 
| ApproximateNumberOfMessagesNotVisible | + `QueueName` | 
| ApproximateNumberOfMessagesNotVisibleInQuietGroups | + `QueueName` | 
| ApproximateNumberOfMessagesVisible | + `QueueName` | 
| ApproximateNumberOfMessagesVisibleInQuietGroups | + `QueueName` | 
| ApproximateNumberOfNoisyGroups | + `QueueName` | 
| NumberOfDeduplicatedSentMessages | + `QueueName` | 
| NumberOfEmptyReceives | + `QueueName` | 
| NumberOfMessagesDeleted | + `QueueName` | 
| NumberOfMessagesReceived | + `QueueName` | 
| NumberOfMessagesSent | + `QueueName` | 
| SentMessageSize | + `QueueName` | 

## AWS/SageMaker
<a name="supported-metrics-ns-aws-sagemaker"></a>

The `AWS/SageMaker` namespace includes enriched metrics for the following resource types.
+ [AWS::SageMaker::Endpoint](#supported-metrics-aws-sagemaker-aws-sagemaker-endpoint)
+ [AWS::SageMaker::InferenceComponent](#supported-metrics-aws-sagemaker-aws-sagemaker-inferencecomponent)

### AWS::SageMaker::Endpoint
<a name="supported-metrics-aws-sagemaker-aws-sagemaker-endpoint"></a>


| Metric | Dimensions | 
| --- | --- | 
| ConcurrentRequestsPerCopy | + `EndpointName`, `VariantName` | 
| ConcurrentRequestsPerModel | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `EndpointName`, `VariantName` | 
| FirstChunkLatency | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `EndpointName`, `VariantName` | 
| FirstChunkModelLatency | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `EndpointName`, `VariantName` | 
| FirstChunkOverheadLatency | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `EndpointName`, `VariantName` | 
| Invocation4XXErrors | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `VariantName` | 
| Invocation5XXErrors | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `VariantName` | 
| InvocationModelErrors | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `VariantName` | 
| Invocations | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `VariantName` | 
| InvocationsPerCopy | + `EndpointName`, `VariantName` | 
| InvocationsPerInstance | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `EndpointName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `VariantName` | 
| MidStreamErrors | + `EndpointName`, `VariantName` | 
| ModelCacheHit | + `EndpointName`, `VariantName` | 
| ModelDownloadingTime | + `EndpointName`, `VariantName` | 
| ModelLatency | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `VariantName` | 
| ModelLoadingTime | + `EndpointName`, `VariantName` | 
| ModelLoadingWaitTime | + `EndpointName`, `VariantName` | 
| ModelSetupTime | + `EndpointName`, `VariantName` | 
| ModelUnloadingTime | + `EndpointName`, `VariantName` | 
| OverheadLatency | + `AvailabilityZone`, `EndpointName`, `InstanceType`, `Region`, `VariantName`<br />+ `ContainerId`, `EndpointName`, `InferenceComponentName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `InstanceId`, `VariantName`<br />+ `EndpointName`, `VariantName` | 

### AWS::SageMaker::InferenceComponent
<a name="supported-metrics-aws-sagemaker-aws-sagemaker-inferencecomponent"></a>


| Metric | Dimensions | 
| --- | --- | 
| ConcurrentRequestsPerCopy | + `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region`<br />+ `InferenceComponentName` | 
| ConcurrentRequestsPerModel | + `InferenceComponentName` | 
| Invocation4XXErrors | + `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region`<br />+ `InferenceComponentName` | 
| Invocation5XXErrors | + `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region`<br />+ `InferenceComponentName` | 
| InvocationModelErrors | + `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region`<br />+ `InferenceComponentName` | 
| Invocations | + `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region`<br />+ `InferenceComponentName` | 
| InvocationsPerCopy | + `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region`<br />+ `InferenceComponentName` | 
| InvocationsPerInstance | + `InferenceComponentName` | 
| ModelLatency | + `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region`<br />+ `InferenceComponentName` | 
| ModelSetupTime | + `InferenceComponentName` | 
| OverheadLatency | + `AvailabilityZone`, `InferenceComponentName`, `InstanceType`, `Region`<br />+ `InferenceComponentName` | 

## AWS/Scheduler
<a name="supported-metrics-ns-aws-scheduler"></a>

The `AWS/Scheduler` namespace includes enriched metrics for the following resource types.
+ [AWS::Scheduler::ScheduleGroup](#supported-metrics-aws-scheduler-aws-scheduler-schedulegroup)

### AWS::Scheduler::ScheduleGroup
<a name="supported-metrics-aws-scheduler-aws-scheduler-schedulegroup"></a>


| Metric | Dimensions | 
| --- | --- | 
| InvocationAttemptCount | + `ScheduleGroup` | 
| InvocationDroppedCount | + `ScheduleGroup` | 
| InvocationThrottleCount | + `ScheduleGroup` | 
| InvocationsFailedToBeSentToDeadLetterCount | + `ScheduleGroup` | 
| InvocationsFailedToBeSentToDeadLetterCount\_AWS.SimpleQueueService.NonExistentQueue | + `ScheduleGroup` | 
| InvocationsFailedToBeSentToDeadLetterCount\_AccessDenied | + `ScheduleGroup` | 
| InvocationsFailedToBeSentToDeadLetterCount\_KMS.AccessDeniedException | + `ScheduleGroup` | 
| InvocationsSentToDeadLetterCount | + `ScheduleGroup` | 
| TargetErrorCount | + `ScheduleGroup` | 
| TargetErrorThrottledCount | + `ScheduleGroup` | 

## AWS/Transfer
<a name="supported-metrics-ns-aws-transfer"></a>

The `AWS/Transfer` namespace includes enriched metrics for the following resource types.
+ [AWS::Transfer::Connector](#supported-metrics-aws-transfer-aws-transfer-connector)
+ [AWS::Transfer::Server](#supported-metrics-aws-transfer-aws-transfer-server)

### AWS::Transfer::Connector
<a name="supported-metrics-aws-transfer-aws-transfer-connector"></a>


| Metric | Dimensions | 
| --- | --- | 
| OutboundFailedMessage | + `ConnectorId` | 
| OutboundMessage | + `ConnectorId` | 

### AWS::Transfer::Server
<a name="supported-metrics-aws-transfer-aws-transfer-server"></a>


| Metric | Dimensions | 
| --- | --- | 
| BytesIn | + `ServerId` | 
| BytesOut | + `ServerId` | 
| ConcurrentSessions | + `ServerId` | 
| FilesIn | + `ServerId` | 
| FilesOut | + `ServerId` | 
| InboundFailedMessage | + `ServerId` | 
| InboundMessage | + `ServerId` | 
| OnUploadExecutionsFailed | + `ServerId` | 
| OnUploadExecutionsStarted | + `ServerId` | 
| OnUploadExecutionsSuccess | + `ServerId` | 
| OutboundFailedMessage | + `ServerId` | 

## AWS/TransitGateway
<a name="supported-metrics-ns-aws-transitgateway"></a>

The `AWS/TransitGateway` namespace includes enriched metrics for the following resource types.
+ [AWS::EC2::TransitGateway](#supported-metrics-aws-transitgateway-aws-ec2-transitgateway)

### AWS::EC2::TransitGateway
<a name="supported-metrics-aws-transitgateway-aws-ec2-transitgateway"></a>


| Metric | Dimensions | 
| --- | --- | 
| BytesDropCountBlackhole | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| BytesDropCountInternalError | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| BytesDropCountNoPolicy | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| BytesDropCountNoRoute | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| BytesIn | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| BytesOut | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| PacketDropCountBlackhole | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| PacketDropCountInternalError | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| PacketDropCountNoPolicy | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| PacketDropCountNoRoute | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| PacketDropCountTTLExpired | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| PacketsIn | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 
| PacketsOut | + `AvailabilityZone`, `TransitGateway`<br />+ `AvailabilityZone`, `TransitGateway`, `TransitGatewayAttachment`<br />+ `TransitGateway`<br />+ `TransitGateway`, `TransitGatewayAttachment` | 

## AWS/VPN
<a name="supported-metrics-ns-aws-vpn"></a>

The `AWS/VPN` namespace includes enriched metrics for the following resource types.
+ [AWS::EC2::VPNConnection](#supported-metrics-aws-vpn-aws-ec2-vpnconnection)

### AWS::EC2::VPNConnection
<a name="supported-metrics-aws-vpn-aws-ec2-vpnconnection"></a>


| Metric | Dimensions | 
| --- | --- | 
| TunnelDataIn | + `VpnId` | 
| TunnelDataOut | + `VpnId` | 
| TunnelState | + `VpnId` | 

## AWS/VpcLattice
<a name="supported-metrics-ns-aws-vpclattice"></a>

The `AWS/VpcLattice` namespace includes enriched metrics for the following resource types.
+ [AWS::VpcLattice::Service](#supported-metrics-aws-vpclattice-aws-vpclattice-service)

### AWS::VpcLattice::Service
<a name="supported-metrics-aws-vpclattice-aws-vpclattice-service"></a>


| Metric | Dimensions | 
| --- | --- | 
| HTTPCode\_2XX\_Count | + `AvailabilityZone`, `Service` | 
| HTTPCode\_3XX\_Count | + `AvailabilityZone`, `Service` | 
| HTTPCode\_4XX\_Count | + `AvailabilityZone`, `Service` | 
| HTTPCode\_5XX\_Count | + `AvailabilityZone`, `Service` | 
| RequestTime | + `AvailabilityZone`, `Service` | 
| RequestTimeoutCount | + `AvailabilityZone`, `Service` | 
| TotalRequestCount | + `AvailabilityZone`, `Service` | 

## AWS/WorkSpaces
<a name="supported-metrics-ns-aws-workspaces"></a>

The `AWS/WorkSpaces` namespace includes enriched metrics for the following resource types.
+ [AWS::WorkSpaces::Workspace](#supported-metrics-aws-workspaces-aws-workspaces-workspace)

### AWS::WorkSpaces::Workspace
<a name="supported-metrics-aws-workspaces-aws-workspaces-workspace"></a>


| Metric | Dimensions | 
| --- | --- | 
| Available | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| CPUUsage | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| ConnectionAttempt | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| ConnectionFailure | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| ConnectionSuccess | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| InSessionLatency | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| Maintenance | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| MemoryUsage | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| Restoring | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| RootVolumeDiskUsage | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| SessionDisconnect | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| SessionLaunchTime | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| Stopped | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| UDPPacketLossRate | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| Unhealthy | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| UpTime | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| UserConnected | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 
| UserVolumeDiskUsage | + `AwsAccountId`, `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `AwsAccountId`, `WorkspaceId`<br />+ `BundleId`, `ComputeType`, `Protocol`, `RunningMode`, `WorkspaceId`<br />+ `WorkspaceId` | 

## CloudWatchSynthetics
<a name="supported-metrics-ns-cloudwatchsynthetics"></a>

The `CloudWatchSynthetics` namespace includes enriched metrics for the following resource types.
+ [AWS::Synthetics::Canary](#supported-metrics-cloudwatchsynthetics-aws-synthetics-canary)

### AWS::Synthetics::Canary
<a name="supported-metrics-cloudwatchsynthetics-aws-synthetics-canary"></a>


| Metric | Dimensions | 
| --- | --- | 
| 2xx | + `CanaryName` | 
| 4xx | + `CanaryName` | 
| 5xx | + `CanaryName` | 
| Duration | + `CanaryName` | 
| Error | + `CanaryName` | 
| Failed | + `CanaryName` | 
| Failed requests | + `CanaryName` | 
| SuccessPercent | + `CanaryName` | 
| VisualMonitoringSuccessPercent | + `CanaryName` | 
| VisualMonitoringTotalComparisons | + `CanaryName` | 

## ContainerInsights
<a name="supported-metrics-ns-containerinsights"></a>

The `ContainerInsights` namespace includes enriched metrics for the following resource types.
+ [AWS::EKS::Cluster](#supported-metrics-containerinsights-aws-eks-cluster)

### AWS::EKS::Cluster
<a name="supported-metrics-containerinsights-aws-eks-cluster"></a>


| Metric | Dimensions | 
| --- | --- | 
| cluster\_failed\_node\_count | + `ClusterName` | 
| cluster\_node\_count | + `ClusterName` | 
| node\_cpu\_limit | + `ClusterName` | 
| node\_cpu\_usage\_total | + `ClusterName` | 
| node\_filesystem\_utilization | + `ClusterName` | 
| node\_memory\_limit | + `ClusterName` | 
| node\_memory\_working\_set | + `ClusterName` | 
| node\_network\_total\_bytes | + `ClusterName` | 
| pod\_cpu\_utilization | + `ClusterName` | 
| pod\_network\_rx\_bytes | + `ClusterName` | 
| pod\_network\_tx\_bytes | + `ClusterName` | 

## ECS/ContainerInsights
<a name="supported-metrics-ns-ecs-containerinsights"></a>

The `ECS/ContainerInsights` namespace includes enriched metrics for the following resource types.
+ [AWS::ECS::Cluster](#supported-metrics-ecs-containerinsights-aws-ecs-cluster)
+ [AWS::ECS::Service](#supported-metrics-ecs-containerinsights-aws-ecs-service)

### AWS::ECS::Cluster
<a name="supported-metrics-ecs-containerinsights-aws-ecs-cluster"></a>


| Metric | Dimensions | 
| --- | --- | 
| ContainerInstanceCount | + `ClusterName` | 
| CpuReserved | + `ClusterName`<br />+ `ClusterName`, `TaskDefinitionFamily` | 
| CpuUtilized | + `ClusterName`<br />+ `ClusterName`, `TaskDefinitionFamily` | 
| EphemeralStorageReserved | + `ClusterName`<br />+ `ClusterName`, `TaskDefinitionFamily` | 
| EphemeralStorageUtilized | + `ClusterName`<br />+ `ClusterName`, `TaskDefinitionFamily` | 
| MemoryReserved | + `ClusterName`<br />+ `ClusterName`, `TaskDefinitionFamily` | 
| MemoryUtilized | + `ClusterName`<br />+ `ClusterName`, `TaskDefinitionFamily` | 
| NetworkRxBytes | + `ClusterName`<br />+ `ClusterName`, `TaskDefinitionFamily` | 
| NetworkTxBytes | + `ClusterName`<br />+ `ClusterName`, `TaskDefinitionFamily` | 
| ServiceCount | + `ClusterName` | 
| StorageReadBytes | + `ClusterName`, `TaskDefinitionFamily` | 
| StorageWriteBytes | + `ClusterName`, `TaskDefinitionFamily` | 
| TaskCount | + `ClusterName` | 

### AWS::ECS::Service
<a name="supported-metrics-ecs-containerinsights-aws-ecs-service"></a>


| Metric | Dimensions | 
| --- | --- | 
| CpuReserved | + `ClusterName`, `ServiceName` | 
| CpuUtilized | + `ClusterName`, `ServiceName` | 
| DeploymentCount | + `ClusterName`, `ServiceName` | 
| DesiredTaskCount | + `ClusterName`, `ServiceName` | 
| EphemeralStorageReserved | + `ClusterName`, `ServiceName` | 
| EphemeralStorageUtilized | + `ClusterName`, `ServiceName` | 
| MemoryReserved | + `ClusterName`, `ServiceName` | 
| MemoryUtilized | + `ClusterName`, `ServiceName` | 
| NetworkRxBytes | + `ClusterName`, `ServiceName` | 
| NetworkTxBytes | + `ClusterName`, `ServiceName` | 
| PendingTaskCount | + `ClusterName`, `ServiceName` | 
| RunningTaskCount | + `ClusterName`, `ServiceName` | 
| TaskSetCount | + `ClusterName`, `ServiceName` | 

## Glue
<a name="supported-metrics-ns-glue"></a>

The `Glue` namespace includes enriched metrics for the following resource types.
+ [AWS::Glue::Job](#supported-metrics-glue-aws-glue-job)

### AWS::Glue::Job
<a name="supported-metrics-glue-aws-glue-job"></a>


| Metric | Dimensions | 
| --- | --- | 
| glue.ALL.jvm.heap.usage | + `JobName`, `JobRunId`, `Type` | 
| glue.ALL.jvm.heap.used | + `JobName`, `JobRunId`, `Type` | 
| glue.ALL.s3.filesystem.read\_bytes | + `JobName`, `JobRunId`, `Type` | 
| glue.ALL.s3.filesystem.write\_bytes | + `JobName`, `JobRunId`, `Type` | 
| glue.ALL.system.cpuSystemLoad | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.BlockManager.disk.diskSpaceUsed\_MB | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.ExecutorAllocationManager.executors.numberAllExecutors | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.ExecutorAllocationManager.executors.numberMaxNeededExecutors | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.aggregate.bytesRead | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.aggregate.elapsedTime | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.aggregate.numCompletedStages | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.aggregate.numCompletedTasks | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.aggregate.numFailedTasks | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.aggregate.numKilledTasks | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.aggregate.recordsRead | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.aggregate.shuffleBytesWritten | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.aggregate.shuffleLocalBytesRead | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.jvm.heap.usage | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.jvm.heap.used | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.s3.filesystem.read\_bytes | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.s3.filesystem.write\_bytes | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.streaming.batchProcessingTimeInMs | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.streaming.numRecords | + `JobName`, `JobRunId`, `Type` | 
| glue.driver.system.cpuSystemLoad | + `JobName`, `JobRunId`, `Type` | 

## LambdaInsights
<a name="supported-metrics-ns-lambdainsights"></a>

The `LambdaInsights` namespace includes enriched metrics for the following resource types.
+ [AWS::Lambda::Function](#supported-metrics-lambdainsights-aws-lambda-function)

### AWS::Lambda::Function
<a name="supported-metrics-lambdainsights-aws-lambda-function"></a>


| Metric | Dimensions | 
| --- | --- | 
| cpu\_total\_time | + `function_name` | 
| init\_duration | + `function_name` | 
| memory\_utilization | + `function_name` | 
| rx\_bytes | + `function_name` | 
| total\_memory | + `function_name` | 
| total\_network | + `function_name` | 
| tx\_bytes | + `function_name` | 
| used\_memory\_max | + `function_name` | 