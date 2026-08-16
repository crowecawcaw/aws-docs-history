# Recommended PromQL alarms

Use these PromQL alarms as equivalents of the classic recommended alarms. They monitor
the same metrics by using PromQL instant queries that are evaluated against metrics ingested
through the CloudWatch OTLP endpoint.

PromQL alarms use `EvaluationCriteria` with `PromQLCriteria`.
Unlike classic metric alarms, the threshold is embedded directly in the PromQL query
expression.

- **Pending period** – The duration in seconds
  that a time series must continuously breach before the alarm transitions to ALARM
  state.
- **Recovery period** – The duration in seconds
  that all time series must stop breaching before the alarm returns to OK
  state.
- **Evaluation interval** – How often, in
  seconds, CloudWatch runs the PromQL query.

###### Note

These alarms require metrics published through the CloudWatch OTLP endpoint. For more
information, see [PromQL alarms](alarm-promql.md "alarm-promql.md").

You can deploy these alarms by using AWS CloudFormation. Use the
`EvaluationCriteria` and `PromQLCriteria` properties on the
`AWS::CloudWatch::Alarm` resource.

###### Topics

- [API Gateway](#Recommended_PromQL_ApiGateway "#Recommended_PromQL_ApiGateway")
- [Auto Scaling](#Recommended_PromQL_AutoScaling "#Recommended_PromQL_AutoScaling")
- [Certificate Manager](#Recommended_PromQL_CertificateManager "#Recommended_PromQL_CertificateManager")
- [CloudFront](#Recommended_PromQL_CloudFront "#Recommended_PromQL_CloudFront")
- [Cognito](#Recommended_PromQL_Cognito "#Recommended_PromQL_Cognito")
- [DynamoDB](#Recommended_PromQL_DynamoDB "#Recommended_PromQL_DynamoDB")
- [EBS](#Recommended_PromQL_EBS "#Recommended_PromQL_EBS")
- [Amazon Elastic Compute Cloud](#Recommended_PromQL_EC2 "#Recommended_PromQL_EC2")
- [Amazon ECS](#Recommended_PromQL_ECS "#Recommended_PromQL_ECS")
- [Amazon ECS Container Insights](#Recommended_PromQL_ECS_ContainerInsights "#Recommended_PromQL_ECS_ContainerInsights")
- [Amazon ECS Container Insights enhanced observability](#Recommended_PromQL_ECS_ContainerInsights_Enhanced "#Recommended_PromQL_ECS_ContainerInsights_Enhanced")
- [Amazon EFS](#Recommended_PromQL_EFS "#Recommended_PromQL_EFS")
- [Amazon EKS Container Insights](#Recommended_PromQL_EKS "#Recommended_PromQL_EKS")
- [Amazon ElastiCache](#Recommended_PromQL_ElastiCache "#Recommended_PromQL_ElastiCache")
- [Elastic GPUs](#Recommended_PromQL_ElasticGPUs "#Recommended_PromQL_ElasticGPUs")
- [Amazon EventBridge Scheduler](#Recommended_PromQL_Scheduler "#Recommended_PromQL_Scheduler")
- [Amazon Kinesis Data Streams](#Recommended_PromQL_Kinesis "#Recommended_PromQL_Kinesis")
- [AWS Lambda](#Recommended_PromQL_Lambda "#Recommended_PromQL_Lambda")
- [AWS Lambda Insights](#Recommended_PromQL_LambdaInsights "#Recommended_PromQL_LambdaInsights")
- [NAT Gateway](#Recommended_PromQL_NATGateway "#Recommended_PromQL_NATGateway")
- [AWS PrivateLink endpoints](#Recommended_PromQL_PrivateLinkEndpoints "#Recommended_PromQL_PrivateLinkEndpoints")
- [AWS PrivateLink services](#Recommended_PromQL_PrivateLinkServices "#Recommended_PromQL_PrivateLinkServices")
- [RDS](#Recommended_PromQL_RDS "#Recommended_PromQL_RDS")
- [Route 53](#Recommended_PromQL_Route53 "#Recommended_PromQL_Route53")
- [S3](#Recommended_PromQL_S3 "#Recommended_PromQL_S3")
- [S3 Object Lambda](#Recommended_PromQL_S3ObjectLambda "#Recommended_PromQL_S3ObjectLambda")
- [SNS](#Recommended_PromQL_SNS "#Recommended_PromQL_SNS")
- [SQS](#Recommended_PromQL_SQS "#Recommended_PromQL_SQS")
- [VPN](#Recommended_PromQL_VPN "#Recommended_PromQL_VPN")

## API Gateway

**REST API**

**4XXError**

**Labels:** ApiName, Stage

**Alarm description:** Alarm when the
average 4XX error rate exceeds 5% for a REST API stage.

**Intent:** Detect high client error
rate indicating request issues.

**PromQL criteria:** `avg({__name__="4XXError", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiName="`your-api-name`",Stage="`your-stage`"}) > 0.05`

**Recommended threshold:** 0.05 (embedded
in query)

**Threshold justification:** Detects
greater than 5% client error rate, which indicates significant request
failures.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**5XXError**

**Labels:** ApiName, Stage

**Alarm description:** Alarm when the
average 5XX error rate exceeds 5% for a REST API stage.

**Intent:** Detect high server error
rate indicating backend failures.

**PromQL criteria:** `avg({__name__="5XXError", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiName="`your-api-name`",Stage="`your-stage`"}) > 0.05`

**Recommended threshold:** 0.05 (embedded
in query)

**Threshold justification:** Detects
greater than 5% server error rate, which requires immediate
investigation.

**Evaluation interval:** 60

**Pending period:** 180

**Recovery period:** 300

**Latency**

**Labels:** ApiName, Stage

**Alarm description:** Alarm when the p90
latency exceeds 2500 ms for a REST API stage.

**Intent:** Detect high p90 latency
affecting user experience.

**PromQL criteria:** `histogram_quantile(0.9, {__name__="Latency", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiName="`your-api-name`",Stage="`your-stage`"}) > 2500`

**Recommended threshold:** 2500 (embedded
in query)

**Threshold justification:** A p90 latency
above 2500 ms indicates degraded response times for most
requests.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**Count**

**Labels:** ApiName, Stage

**Alarm description:** Alarm when the
total request count drops below the expected baseline for a REST API
stage.

**Intent:** Detect low traffic volume
that might indicate routing or availability issues.

**PromQL criteria:** `sum({__name__="Count", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiName="`your-api-name`",Stage="`your-stage`"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your expected traffic baseline to detect unexpected drops.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 300

**HTTP API**

**4xx**

**Labels:** ApiId, Stage

**Alarm description:** Alarm when the
average 4xx error rate exceeds 5% for an HTTP API stage.

**Intent:** Detect high client error
rate on HTTP API endpoints.

**PromQL criteria:** `avg({__name__="4xx", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiId="`your-api-id`",Stage="`your-stage`"}) > 0.05`

**Recommended threshold:** 0.05 (embedded
in query)

**Threshold justification:** Detects
greater than 5% client error rate.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**5xx**

**Labels:** ApiId, Stage

**Alarm description:** Alarm when the
average 5xx error rate exceeds 5% for an HTTP API stage.

**Intent:** Detect high server error
rate on HTTP API endpoints.

**PromQL criteria:** `avg({__name__="5xx", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiId="`your-api-id`",Stage="`your-stage`"}) > 0.05`

**Recommended threshold:** 0.05 (embedded
in query)

**Threshold justification:** Detects
greater than 5% server error rate requiring investigation.

**Evaluation interval:** 60

**Pending period:** 180

**Recovery period:** 300

**Latency**

**Labels:** ApiId, Stage

**Alarm description:** Alarm when the p90
latency exceeds 2500 ms for an HTTP API stage.

**Intent:** Detect high p90 latency on
HTTP API endpoints.

**PromQL criteria:** `histogram_quantile(0.9, {__name__="Latency", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiId="`your-api-id`",Stage="`your-stage`"}) > 2500`

**Recommended threshold:** 2500 (embedded
in query)

**Threshold justification:** A p90
latency above 2500 ms indicates degraded response times.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**IntegrationLatency**

**Labels:** ApiId, Stage

**Alarm description:** Alarm when the p90
integration latency exceeds 2000 ms for an HTTP API stage.

**Intent:** Detect high backend
integration latency affecting response times.

**PromQL criteria:** `histogram_quantile(0.9, {__name__="IntegrationLatency", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiId="`your-api-id`",Stage="`your-stage`"}) > 2000`

**Recommended threshold:** 2000 (embedded
in query)

**Threshold justification:** A p90
integration latency above 2000 ms indicates backend
slowness.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**Count**

**Labels:** ApiId, Stage

**Alarm description:** Alarm when the
total request count drops below the expected baseline for an HTTP API
stage.

**Intent:** Detect low traffic volume
that might indicate routing or availability issues.

**PromQL criteria:** `sum({__name__="Count", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiId="`your-api-id`",Stage="`your-stage`"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your expected traffic baseline to detect unexpected drops.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 300

**WebSocket API**

**ClientError**

**Labels:** ApiId, Stage

**Alarm description:** Alarm when the
average client error rate exceeds 5% for a WebSocket API
stage.

**Intent:** Detect high client error
rate on WebSocket API connections.

**PromQL criteria:** `avg({__name__="ClientError", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiId="`your-api-id`",Stage="`your-stage`"}) > 0.05`

**Recommended threshold:** 0.05 (embedded
in query)

**Threshold justification:** Detects
greater than 5% client error rate on WebSocket
connections.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**ExecutionError**

**Labels:** ApiId, Stage

**Alarm description:** Alarm when the
average execution error rate exceeds 5% for a WebSocket API
stage.

**Intent:** Detect high server-side
execution error rate on WebSocket APIs.

**PromQL criteria:** `avg({__name__="ExecutionError", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiId="`your-api-id`",Stage="`your-stage`"}) > 0.05`

**Recommended threshold:** 0.05 (embedded
in query)

**Threshold justification:** Detects
greater than 5% execution error rate requiring
investigation.

**Evaluation interval:** 60

**Pending period:** 180

**Recovery period:** 300

**IntegrationLatency**

**Labels:** ApiId, Stage

**Alarm description:** Alarm when the p90
integration latency exceeds 2000 ms for a WebSocket API
stage.

**Intent:** Detect high backend
integration latency on WebSocket API routes.

**PromQL criteria:** `histogram_quantile(0.9, {__name__="IntegrationLatency", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiId="`your-api-id`",Stage="`your-stage`"}) > 2000`

**Recommended threshold:** 2000 (embedded
in query)

**Threshold justification:** A p90
integration latency above 2000 ms indicates backend
slowness.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**MessageCount**

**Labels:** ApiId, Stage

**Alarm description:** Alarm when the
total message count drops below the expected baseline for a WebSocket
API stage.

**Intent:** Detect low message volume
that might indicate connection or routing issues.

**PromQL criteria:** `sum({__name__="MessageCount", "@instrumentation.@name"="cloudwatch.aws/apigateway", ApiId="`your-api-id`",Stage="`your-stage`"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your expected message volume to detect unexpected drops.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 300

## Auto Scaling

**GroupInServiceCapacity**

**Labels:** AutoScalingGroupName

**Alarm description:** Alarm when the
average in-service capacity drops below the expected minimum for an
Auto Scaling group.

**Intent:** Detect low availability due
to launch failures or terminated instances.

**PromQL criteria:** `avg({__name__="GroupInServiceCapacity", "@instrumentation.@name"="cloudwatch.aws/autoscaling", AutoScalingGroupName="`your-auto-scaling-group-name`"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your minimum desired capacity to detect launch failures or
insufficient instances.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

## Certificate Manager

**DaysToExpiry**

**Labels:** CertificateArn

**Alarm description:** Alarm when the
minimum days to certificate expiry drops to 44 days or fewer.

**Intent:** Proactive certificate
expiration alert to allow time for renewal.

**PromQL criteria:** `min({__name__="DaysToExpiry", "@instrumentation.@name"="cloudwatch.aws/certificatemanager", CertificateArn="`your-certificate-arn`"}) <= 44`

**Recommended threshold:** 44 (embedded
in query)

**Threshold justification:** Provides
sufficient lead time before certificate expiration to complete the
renewal process.

**Evaluation interval:** 86400

**Pending period:** 86400

**Recovery period:** 86400

## CloudFront

**5xxErrorRate**

**Labels:** DistributionId

**Alarm description:** Alarm when the
average 5xx error rate exceeds the threshold for a CloudFront
distribution.

**Intent:** Detect high origin or
CloudFront error rate affecting content delivery.

**PromQL criteria:** `avg({__name__="5xxErrorRate", "@instrumentation.@name"="cloudwatch.aws/cloudfront", DistributionId="`your-distribution-id`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable error rate for content delivery.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**OriginLatency**

**Labels:** DistributionId

**Alarm description:** Alarm when the p90
origin latency exceeds the threshold for a CloudFront
distribution.

**Intent:** Detect high origin response
latency affecting content delivery performance.

**PromQL criteria:** `histogram_quantile(0.9, {__name__="OriginLatency", "@instrumentation.@name"="cloudwatch.aws/cloudfront", DistributionId="`your-distribution-id`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your expected origin response time and caching strategy.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**FunctionValidationErrors**

**Labels:** DistributionId,
FunctionName

**Alarm description:** Alarm when any
CloudFront function validation errors occur.

**Intent:** Detect CloudFront function
validation failures that prevent function execution.

**PromQL criteria:** `sum({__name__="FunctionValidationErrors", "@instrumentation.@name"="cloudwatch.aws/cloudfront", DistributionId="`your-distribution-id`",FunctionName="`your-function-name`"}) > 0`

**Recommended threshold:** 0 (embedded
in query)

**Threshold justification:** Any
validation error indicates a function configuration problem that
requires attention.

**Evaluation interval:** 60

**Pending period:** 120

**Recovery period:** 120

**FunctionExecutionErrors**

**Labels:** DistributionId,
FunctionName

**Alarm description:** Alarm when any
CloudFront function execution errors occur.

**Intent:** Detect runtime failures in
CloudFront functions that affect request processing.

**PromQL criteria:** `sum({__name__="FunctionExecutionErrors", "@instrumentation.@name"="cloudwatch.aws/cloudfront", DistributionId="`your-distribution-id`",FunctionName="`your-function-name`"}) > 0`

**Recommended threshold:** 0 (embedded
in query)

**Threshold justification:** Any
execution error indicates a runtime problem in the function
code.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**FunctionThrottles**

**Labels:** DistributionId,
FunctionName

**Alarm description:** Alarm when any
CloudFront function throttling occurs.

**Intent:** Detect CloudFront function
throttling that might degrade request processing.

**PromQL criteria:** `sum({__name__="FunctionThrottles", "@instrumentation.@name"="cloudwatch.aws/cloudfront", DistributionId="`your-distribution-id`",FunctionName="`your-function-name`"}) > 0`

**Recommended threshold:** 0 (embedded
in query)

**Threshold justification:** Any
throttling indicates the function is hitting compute limits.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## Cognito

**SignUpThrottles**

**Labels:** UserPool,
UserPoolClient

**Alarm description:** Alarm when sign-up
throttle events exceed the threshold for a user pool.

**Intent:** Detect sign-up throttling
that prevents new user registrations.

**PromQL criteria:** `sum({__name__="SignUpThrottles", "@instrumentation.@name"="cloudwatch.aws/cognito", UserPool="`your-user-pool`",UserPoolClient="`your-user-pool-client`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable throttle rate for sign-up operations.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**SignInThrottles**

**Labels:** UserPool,
UserPoolClient

**Alarm description:** Alarm when sign-in
throttle events exceed the threshold for a user pool.

**Intent:** Detect sign-in throttling
that prevents user authentication.

**PromQL criteria:** `sum({__name__="SignInThrottles", "@instrumentation.@name"="cloudwatch.aws/cognito", UserPool="`your-user-pool`",UserPoolClient="`your-user-pool-client`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable throttle rate for sign-in operations.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**TokenRefreshThrottles**

**Labels:** UserPool,
UserPoolClient

**Alarm description:** Alarm when token
refresh throttle events exceed the threshold for a user pool.

**Intent:** Detect token refresh
throttling that might cause session interruptions.

**PromQL criteria:** `sum({__name__="TokenRefreshThrottles", "@instrumentation.@name"="cloudwatch.aws/cognito", UserPool="`your-user-pool`",UserPoolClient="`your-user-pool-client`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable throttle rate for token refresh operations.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**FederationThrottles**

**Labels:** UserPool, UserPoolClient,
IdentityProvider

**Alarm description:** Alarm when
federation throttle events exceed the threshold for a user pool identity
provider.

**Intent:** Detect federation throttling
that might prevent federated sign-in.

**PromQL criteria:** `sum({__name__="FederationThrottles", "@instrumentation.@name"="cloudwatch.aws/cognito", UserPool="`your-user-pool`",UserPoolClient="`your-user-pool-client`",IdentityProvider="`your-identity-provider`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable throttle rate for federation operations.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## DynamoDB

**AccountProvisionedReadCapacityUtilization**

**Labels:** None

**Alarm description:** Alarm when the
account-level provisioned read capacity utilization exceeds
80%.

**Intent:** Detect when provisioned read
capacity approaches account limits.

**PromQL criteria:** `max({__name__="AccountProvisionedReadCapacityUtilization", "@instrumentation.@name"="cloudwatch.aws/dynamodb"}) > 80`

**Recommended threshold:** 80 (embedded
in query)

**Threshold justification:** At 80%
utilization, you have limited headroom before reaching account
limits.

**Evaluation interval:** 300

**Pending period:** 600

**Recovery period:** 600

**AccountProvisionedWriteCapacityUtilization**

**Labels:** None

**Alarm description:** Alarm when the
account-level provisioned write capacity utilization exceeds
80%.

**Intent:** Detect when provisioned write
capacity approaches account limits.

**PromQL criteria:** `max({__name__="AccountProvisionedWriteCapacityUtilization", "@instrumentation.@name"="cloudwatch.aws/dynamodb"}) > 80`

**Recommended threshold:** 80 (embedded
in query)

**Threshold justification:** At 80%
utilization, you have limited headroom before reaching account
limits.

**Evaluation interval:** 300

**Pending period:** 600

**Recovery period:** 600

**AgeOfOldestUnreplicatedRecord**

**Labels:** TableName,
DelegatedOperation

**Alarm description:** Alarm when the age
of the oldest unreplicated record exceeds the threshold.

**Intent:** Detect replication lag that
might cause stale data in global tables.

**PromQL criteria:** `max({__name__="AgeOfOldestUnreplicatedRecord", "@instrumentation.@name"="cloudwatch.aws/dynamodb", TableName="`your-table-name`",DelegatedOperation="`your-operation`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your replication freshness requirements.

**Evaluation interval:** 300

**Pending period:** 900

**Recovery period:** 900

**FailedToReplicateRecordCount**

**Labels:** TableName,
DelegatedOperation

**Alarm description:** Alarm when any
records fail to replicate in a global table.

**Intent:** Detect replication failures
that cause data inconsistency across regions.

**PromQL criteria:** `sum({__name__="FailedToReplicateRecordCount", "@instrumentation.@name"="cloudwatch.aws/dynamodb", TableName="`your-table-name`",DelegatedOperation="`your-operation`"}) > 0`

**Recommended threshold:** 0 (embedded
in query)

**Threshold justification:** Any failed
replication indicates data consistency issues requiring immediate
attention.

**Evaluation interval:** 60

**Pending period:** 60

**Recovery period:** 60

**ReadThrottleEvents**

**Labels:** TableName

**Alarm description:** Alarm when read
throttle events exceed the threshold for a table.

**Intent:** Detect read throttling that
indicates insufficient provisioned capacity.

**PromQL criteria:** `sum({__name__="ReadThrottleEvents", "@instrumentation.@name"="cloudwatch.aws/dynamodb", TableName="`your-table-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable throttle count for read operations.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**ReadThrottleEvents (GSI)**

**Labels:** TableName,
GlobalSecondaryIndexName

**Alarm description:** Alarm when read
throttle events exceed the threshold for a global secondary
index.

**Intent:** Detect read throttling on a
GSI that indicates insufficient index capacity.

**PromQL criteria:** `sum({__name__="ReadThrottleEvents", "@instrumentation.@name"="cloudwatch.aws/dynamodb", TableName="`your-table-name`",GlobalSecondaryIndexName="`your-index-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable throttle count for GSI read operations.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**ReplicationLatency**

**Labels:** TableName,
ReceivingRegion

**Alarm description:** Alarm when the
average replication latency exceeds the threshold for a global
table.

**Intent:** Detect high replication
latency that might cause stale reads in replica regions.

**PromQL criteria:** `avg({__name__="ReplicationLatency", "@instrumentation.@name"="cloudwatch.aws/dynamodb", TableName="`your-table-name`",ReceivingRegion="`your-receiving-region`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your data freshness requirements for replica regions.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**SuccessfulRequestLatency**

**Labels:** TableName, Operation

**Alarm description:** Alarm when the
average successful request latency exceeds the threshold for a table
operation.

**Intent:** Detect high latency on
DynamoDB operations affecting application performance.

**PromQL criteria:** `avg({__name__="SuccessfulRequestLatency", "@instrumentation.@name"="cloudwatch.aws/dynamodb", TableName="`your-table-name`",Operation="`your-operation`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your latency SLA for the specific DynamoDB operation.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

**SystemErrors**

**Labels:** TableName

**Alarm description:** Alarm when system
errors exceed the threshold for a table.

**Intent:** Detect DynamoDB service-side
errors that affect table availability.

**PromQL criteria:** `sum({__name__="SystemErrors", "@instrumentation.@name"="cloudwatch.aws/dynamodb", TableName="`your-table-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable system error count for the table.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**ThrottledPutRecordCount**

**Labels:** TableName,
DelegatedOperation

**Alarm description:** Alarm when
throttled put record count exceeds the threshold for a table.

**Intent:** Detect throttled puts that
might cause data loss in streaming operations.

**PromQL criteria:** `max({__name__="ThrottledPutRecordCount", "@instrumentation.@name"="cloudwatch.aws/dynamodb", TableName="`your-table-name`",DelegatedOperation="`your-operation`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable throttle count for streaming put
operations.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

**UserErrors**

**Labels:** None

**Alarm description:** Alarm when user
errors exceed the threshold across the account.

**Intent:** Detect high rates of client
errors such as validation or conditional check failures.

**PromQL criteria:** `sum({__name__="UserErrors", "@instrumentation.@name"="cloudwatch.aws/dynamodb"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable error rate for client-side request
failures.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

**WriteThrottleEvents**

**Labels:** TableName

**Alarm description:** Alarm when write
throttle events exceed the threshold for a table.

**Intent:** Detect write throttling that
indicates insufficient provisioned capacity.

**PromQL criteria:** `sum({__name__="WriteThrottleEvents", "@instrumentation.@name"="cloudwatch.aws/dynamodb", TableName="`your-table-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable throttle count for write operations.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**WriteThrottleEvents (GSI)**

**Labels:** TableName,
GlobalSecondaryIndexName

**Alarm description:** Alarm when write
throttle events exceed the threshold for a global secondary
index.

**Intent:** Detect write throttling on a
GSI that indicates insufficient index capacity.

**PromQL criteria:** `sum({__name__="WriteThrottleEvents", "@instrumentation.@name"="cloudwatch.aws/dynamodb", TableName="`your-table-name`",GlobalSecondaryIndexName="`your-index-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded
in query)

**Threshold justification:** Set based on
your acceptable throttle count for GSI write operations.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## EBS

**VolumeStalledIOCheck**

**Labels:** VolumeId, InstanceId

**Alarm description:** Alarm when an EBS
volume reports a stalled I/O check failure.

**Intent:** Detect stalled I/O on EBS
volumes that indicates volume impairment.

**PromQL criteria:** `max({__name__="VolumeStalledIOCheck", "@instrumentation.@name"="cloudwatch.aws/ebs", VolumeId="`your-volume-id`",InstanceId="`your-instance-id`"}) >= 1`

**Recommended threshold:** 1 (embedded
in query)

**Threshold justification:** A value of 1
or greater indicates the volume has stalled I/O, requiring immediate
investigation.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

## Amazon Elastic Compute Cloud

**CPUUtilization**

**Labels:** InstanceId

**Alarm description:** Alarm when average CPU utilization exceeds 80% for an EC2 instance.

**Intent:** Detect high CPU utilization.

**PromQL criteria:** `avg({__name__="CPUUtilization", "@instrumentation.@name"="cloudwatch.aws/ec2", InstanceId="`your-instance-id`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% threshold gives headroom before saturation.

**Evaluation interval:** 300

**Pending period:** 900

**Recovery period:** 900

**StatusCheckFailed**

**Labels:** InstanceId

**Alarm description:** Alarm when an instance or system health check fails for an EC2 instance.

**Intent:** Detect instance or system health issues.

**PromQL criteria:** `max({__name__="StatusCheckFailed", "@instrumentation.@name"="cloudwatch.aws/ec2", InstanceId="`your-instance-id`"}) >= 1`

**Recommended threshold:** 1 (embedded in query)

**Threshold justification:** Any status check failure requires investigation.

**Evaluation interval:** 300

**Pending period:** 600

**Recovery period:** 600

**StatusCheckFailed\_AttachedEBS**

**Labels:** InstanceId

**Alarm description:** Alarm when an attached EBS volume becomes unreachable for an EC2 instance.

**Intent:** Detect unreachable EBS volumes.

**PromQL criteria:** `max({__name__="StatusCheckFailed_AttachedEBS", "@instrumentation.@name"="cloudwatch.aws/ec2", InstanceId="`your-instance-id`"}) >= 1`

**Recommended threshold:** 1 (embedded in query)

**Threshold justification:** Unreachable volumes cause I/O failures.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

## Amazon ECS

**CPUReservation**

**Labels:** ClusterName

**Alarm description:** Alarm when average CPU reservation exceeds 80% for an ECS cluster.

**Intent:** Detect cluster approaching CPU capacity.

**PromQL criteria:** `avg({__name__="CPUReservation", "@instrumentation.@name"="cloudwatch.aws/ecs", ClusterName="`your-cluster-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% reservation indicates limited headroom for new tasks.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**CPUUtilization**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when average CPU utilization exceeds 80% for an ECS service.

**Intent:** Detect high CPU utilization for ECS service.

**PromQL criteria:** `avg({__name__="CPUUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**EBSFilesystemUtilization**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when average EBS filesystem utilization exceeds 80% for an ECS service.

**Intent:** Detect high EBS storage utilization.

**PromQL criteria:** `avg({__name__="EBSFilesystemUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**MemoryReservation**

**Labels:** ClusterName

**Alarm description:** Alarm when average memory reservation exceeds 80% for an ECS cluster.

**Intent:** Detect cluster approaching memory capacity.

**PromQL criteria:** `avg({__name__="MemoryReservation", "@instrumentation.@name"="cloudwatch.aws/ecs", ClusterName="`your-cluster-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% reservation indicates limited headroom for new tasks.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**MemoryUtilization**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when average memory utilization exceeds 80% for an ECS service.

**Intent:** Detect high memory utilization.

**PromQL criteria:** `avg({__name__="MemoryUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**HTTPCode\_Target\_5XX\_Count**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when the HTTP 5XX error count exceeds the threshold for an ECS service.

**Intent:** Detect high server-side error count.

**PromQL criteria:** `sum({__name__="HTTPCode_Target_5XX_Count", "@instrumentation.@name"="cloudwatch.aws/ecs", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on your application's normal error rate baseline.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**TargetResponseTime**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when average target response time exceeds the threshold for an ECS service.

**Intent:** Detect high target response time.

**PromQL criteria:** `avg({__name__="TargetResponseTime", "@instrumentation.@name"="cloudwatch.aws/ecs", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on your application's acceptable latency requirements.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## Amazon ECS Container Insights

**EphemeralStorageUtilized**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when average ephemeral storage usage exceeds the threshold for Fargate tasks.

**Intent:** Detect high ephemeral storage usage for Fargate tasks.

**PromQL criteria:** `avg({__name__="EphemeralStorageUtilized", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on your task's ephemeral storage allocation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**RunningTaskCount**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when the running task count drops to zero for an ECS service.

**Intent:** Detect when no tasks are running.

**PromQL criteria:** `avg({__name__="RunningTaskCount", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) <= 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Zero running tasks indicates a service outage.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**instance\_filesystem\_utilization**

**Labels:** InstanceId, ContainerInstanceId, ClusterName

**Alarm description:** Alarm when average filesystem utilization exceeds 90% on a container instance.

**Intent:** Detect high filesystem utilization.

**PromQL criteria:** `avg({__name__="instance_filesystem_utilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", InstanceId="`your-instance-id`",ContainerInstanceId="`your-container-instance-id`",ClusterName="`your-cluster-name`"}) > 90`

**Recommended threshold:** 90 (embedded in query)

**Threshold justification:** 90% filesystem utilization leaves minimal space for operations.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## Amazon ECS Container Insights enhanced observability

**TaskCpuUtilization (cluster level)**

**Labels:** ClusterName

**Alarm description:** Alarm when average task CPU utilization exceeds 80% at the cluster level.

**Intent:** Detect high CPU utilization.

**PromQL criteria:** `avg({__name__="TaskCpuUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**TaskCpuUtilization (service level)**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when average task CPU utilization exceeds 80% at the service level.

**Intent:** Detect high CPU utilization.

**PromQL criteria:** `avg({__name__="TaskCpuUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**TaskMemoryUtilization (cluster level)**

**Labels:** ClusterName

**Alarm description:** Alarm when average task memory utilization exceeds 80% at the cluster level.

**Intent:** Detect high memory utilization.

**PromQL criteria:** `avg({__name__="TaskMemoryUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**TaskMemoryUtilization (service level)**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when average task memory utilization exceeds 80% at the service level.

**Intent:** Detect high memory utilization.

**PromQL criteria:** `avg({__name__="TaskMemoryUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**ContainerCpuUtilization (cluster level)**

**Labels:** ClusterName

**Alarm description:** Alarm when average container CPU utilization exceeds 80% at the cluster level.

**Intent:** Detect high CPU utilization.

**PromQL criteria:** `avg({__name__="ContainerCpuUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**ContainerCpuUtilization (container level)**

**Labels:** ContainerName, ClusterName, ServiceName

**Alarm description:** Alarm when average container CPU utilization exceeds 80% at the container level.

**Intent:** Detect high CPU utilization.

**PromQL criteria:** `avg({__name__="ContainerCpuUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ContainerName="`your-container-name`",ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**ContainerMemoryUtilization (cluster level)**

**Labels:** ClusterName

**Alarm description:** Alarm when average container memory utilization exceeds 80% at the cluster level.

**Intent:** Detect high memory utilization.

**PromQL criteria:** `avg({__name__="ContainerMemoryUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**ContainerMemoryUtilization (container level)**

**Labels:** ContainerName, ClusterName, ServiceName

**Alarm description:** Alarm when average container memory utilization exceeds 80% at the container level.

**Intent:** Detect high memory utilization.

**PromQL criteria:** `avg({__name__="ContainerMemoryUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ContainerName="`your-container-name`",ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**TaskEBSfilesystemUtilization**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when average EBS filesystem utilization exceeds 80% for tasks.

**Intent:** Detect high EBS filesystem utilization.

**PromQL criteria:** `avg({__name__="TaskEBSfilesystemUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**TaskEphemeralStorageUtilization (cluster level)**

**Labels:** ClusterName

**Alarm description:** Alarm when average ephemeral storage utilization exceeds 80% at the cluster level.

**Intent:** Detect high ephemeral storage utilization.

**PromQL criteria:** `avg({__name__="TaskEphemeralStorageUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**TaskEphemeralStorageUtilization (service level)**

**Labels:** ClusterName, ServiceName

**Alarm description:** Alarm when average ephemeral storage utilization exceeds 80% at the service level.

**Intent:** Detect high ephemeral storage utilization.

**PromQL criteria:** `avg({__name__="TaskEphemeralStorageUtilization", "@instrumentation.@name"="cloudwatch.aws/ecs-containerinsights", ClusterName="`your-cluster-name`",ServiceName="`your-service-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## Amazon EFS

**PercentIOLimit**

**Labels:** FileSystemId

**Alarm description:** Alarm when an EFS filesystem reaches 100% of its I/O limit.

**Intent:** Detect when filesystem reaches I/O limit.

**PromQL criteria:** `avg({__name__="PercentIOLimit", "@instrumentation.@name"="cloudwatch.aws/efs", FileSystemId="`your-filesystem-id`"}) >= 100`

**Recommended threshold:** 100 (embedded in query)

**Threshold justification:** At 100% the filesystem becomes a bottleneck.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**BurstCreditBalance**

**Labels:** FileSystemId

**Alarm description:** Alarm when burst credit balance drops to zero for an EFS filesystem.

**Intent:** Detect depleted burst credits causing throughput slowdown.

**PromQL criteria:** `avg({__name__="BurstCreditBalance", "@instrumentation.@name"="cloudwatch.aws/efs", FileSystemId="`your-filesystem-id`"}) <= 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Zero credits causes reduced throughput.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

## Amazon EKS Container Insights

**node\_cpu\_utilization**

**Labels:** ClusterName

**Alarm description:** Alarm when maximum CPU utilization exceeds 80% on EKS worker nodes.

**Intent:** Detect high CPU on worker nodes.

**PromQL criteria:** `max({__name__="node_cpu_utilization", "@instrumentation.@name"="cloudwatch.aws/eks-containerinsights", ClusterName="`your-cluster-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**node\_filesystem\_utilization**

**Labels:** ClusterName

**Alarm description:** Alarm when maximum filesystem utilization exceeds the threshold on EKS worker nodes.

**Intent:** Detect high filesystem usage on worker nodes.

**PromQL criteria:** `max({__name__="node_filesystem_utilization", "@instrumentation.@name"="cloudwatch.aws/eks-containerinsights", ClusterName="`your-cluster-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on your node's storage capacity and usage patterns.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**node\_memory\_utilization**

**Labels:** ClusterName

**Alarm description:** Alarm when maximum memory utilization exceeds 80% on EKS worker nodes.

**Intent:** Detect high memory on worker nodes.

**PromQL criteria:** `max({__name__="node_memory_utilization", "@instrumentation.@name"="cloudwatch.aws/eks-containerinsights", ClusterName="`your-cluster-name`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**pod\_cpu\_utilization\_over\_pod\_limit**

**Labels:** ClusterName, Namespace, Service

**Alarm description:** Alarm when pod CPU utilization exceeds 80% of its limit.

**Intent:** Detect pods approaching CPU limits.

**PromQL criteria:** `max({__name__="pod_cpu_utilization_over_pod_limit", "@instrumentation.@name"="cloudwatch.aws/eks-containerinsights", ClusterName="`your-cluster-name`",Namespace="`your-namespace`",Service="`your-service`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before throttling occurs.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**pod\_memory\_utilization\_over\_pod\_limit**

**Labels:** ClusterName, Namespace, Service

**Alarm description:** Alarm when pod memory utilization exceeds 80% of its limit.

**Intent:** Detect pods approaching memory limits.

**PromQL criteria:** `max({__name__="pod_memory_utilization_over_pod_limit", "@instrumentation.@name"="cloudwatch.aws/eks-containerinsights", ClusterName="`your-cluster-name`",Namespace="`your-namespace`",Service="`your-service`"}) > 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** 80% gives headroom before OOMKill occurs.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## Amazon ElastiCache

**CPUUtilization**

**Labels:** CacheClusterId, CacheNodeId

**Alarm description:** Alarm when average CPU utilization exceeds the threshold for an ElastiCache node.

**Intent:** Detect high CPU across the instance.

**PromQL criteria:** `avg({__name__="CPUUtilization", "@instrumentation.@name"="cloudwatch.aws/elasticache", CacheClusterId="`your-cache-cluster-id`",CacheNodeId="`your-cache-node-id`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on your node type and workload characteristics.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**CurrConnections**

**Labels:** CacheClusterId, CacheNodeId

**Alarm description:** Alarm when the connection count exceeds the threshold for an ElastiCache node.

**Intent:** Detect high connection counts.

**PromQL criteria:** `avg({__name__="CurrConnections", "@instrumentation.@name"="cloudwatch.aws/elasticache", CacheClusterId="`your-cache-cluster-id`",CacheNodeId="`your-cache-node-id`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on your expected connection pool size and application needs.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

**DatabaseMemoryUsagePercentage**

**Labels:** CacheClusterId

**Alarm description:** Alarm when database memory usage exceeds the threshold for an ElastiCache cluster.

**Intent:** Detect high memory usage to prevent write failures.

**PromQL criteria:** `avg({__name__="DatabaseMemoryUsagePercentage", "@instrumentation.@name"="cloudwatch.aws/elasticache", CacheClusterId="`your-cache-cluster-id`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on your eviction policy and data criticality.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**EngineCPUUtilization**

**Labels:** CacheClusterId

**Alarm description:** Alarm when Redis engine CPU utilization exceeds 90% for an ElastiCache cluster.

**Intent:** Detect high Redis engine CPU utilization.

**PromQL criteria:** `avg({__name__="EngineCPUUtilization", "@instrumentation.@name"="cloudwatch.aws/elasticache", CacheClusterId="`your-cache-cluster-id`"}) > 90`

**Recommended threshold:** 90 (embedded in query)

**Threshold justification:** Redis is single-threaded; greater than 90% indicates saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**ReplicationLag**

**Labels:** CacheClusterId

**Alarm description:** Alarm when replication lag exceeds the threshold for an ElastiCache cluster.

**Intent:** Detect replication delay affecting data consistency.

**PromQL criteria:** `avg({__name__="ReplicationLag", "@instrumentation.@name"="cloudwatch.aws/elasticache", CacheClusterId="`your-cache-cluster-id`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on your application's tolerance for stale reads.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

## Elastic GPUs

**GPUConnectivityCheckFailed**

**Labels:** InstanceId, EGPUId

**Alarm description:** Alarm when the Elastic Graphics accelerator loses connectivity to the instance.

**Intent:** Detect connectivity issues to Elastic Graphics accelerator.

**PromQL criteria:** `max({__name__="GPUConnectivityCheckFailed", "@instrumentation.@name"="cloudwatch.aws/elasticgpus", InstanceId="`your-instance-id`",EGPUId="`your-egpu-id`"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Any connectivity failure requires investigation.

**Evaluation interval:** 300

**Pending period:** 900

**Recovery period:** 900

**GPUHealthCheckFailed**

**Labels:** InstanceId, EGPUId

**Alarm description:** Alarm when an Elastic Graphics accelerator health check fails.

**Intent:** Detect unhealthy Elastic Graphics accelerator.

**PromQL criteria:** `max({__name__="GPUHealthCheckFailed", "@instrumentation.@name"="cloudwatch.aws/elasticgpus", InstanceId="`your-instance-id`",EGPUId="`your-egpu-id`"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Health check failures indicate accelerator problems.

**Evaluation interval:** 300

**Pending period:** 900

**Recovery period:** 900

## Amazon EventBridge Scheduler

**TargetErrorThrottledCount**

**Alarm description:** Alarm when schedule target invocations are throttled.

**Intent:** Detect target throttling causing schedule delays.

**PromQL criteria:** `sum({__name__="TargetErrorThrottledCount", "@instrumentation.@name"="cloudwatch.aws/scheduler"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Any throttling indicates target capacity issues.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**InvocationThrottleCount**

**Alarm description:** Alarm when Scheduler invocations are throttled.

**Intent:** Detect Scheduler invocation throttling.

**PromQL criteria:** `sum({__name__="InvocationThrottleCount", "@instrumentation.@name"="cloudwatch.aws/scheduler"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Throttling delays scheduled executions.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**InvocationDroppedCount**

**Alarm description:** Alarm when scheduled invocations are dropped.

**Intent:** Detect dropped invocations.

**PromQL criteria:** `sum({__name__="InvocationDroppedCount", "@instrumentation.@name"="cloudwatch.aws/scheduler"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Dropped invocations represent lost scheduled events.

**Evaluation interval:** 60

**Pending period:** 60

**Recovery period:** 60

**InvocationsFailedToBeSentToDeadLetterCount**

**Alarm description:** Alarm when failed invocations cannot be sent to the dead-letter queue.

**Intent:** Detect DLQ delivery failures.

**PromQL criteria:** `sum({__name__="InvocationsFailedToBeSentToDeadLetterCount", "@instrumentation.@name"="cloudwatch.aws/scheduler"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Failed DLQ delivery means lost error information.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

## Amazon Kinesis Data Streams

**GetRecords.IteratorAgeMilliseconds**

**Labels:** StreamName

**Alarm description:** Alarm when consumer iterator age exceeds the threshold for a Kinesis stream.

**Intent:** Detect data falling behind retention period risking data loss.

**PromQL criteria:** `max({__name__="GetRecords.IteratorAgeMilliseconds", "@instrumentation.@name"="cloudwatch.aws/kinesis", StreamName="`your-stream-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on stream retention period percentage.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**GetRecords.Success**

**Labels:** StreamName

**Alarm description:** Alarm when the GetRecords success rate drops below the threshold for a Kinesis stream.

**Intent:** Detect consumer retrieval failures.

**PromQL criteria:** `avg({__name__="GetRecords.Success", "@instrumentation.@name"="cloudwatch.aws/kinesis", StreamName="`your-stream-name`"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on expected success rate.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**PutRecord.Success**

**Labels:** StreamName

**Alarm description:** Alarm when the PutRecord success rate drops below the threshold for a Kinesis stream.

**Intent:** Detect producer ingestion failures.

**PromQL criteria:** `avg({__name__="PutRecord.Success", "@instrumentation.@name"="cloudwatch.aws/kinesis", StreamName="`your-stream-name`"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on expected success rate.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**PutRecords.FailedRecords**

**Labels:** StreamName

**Alarm description:** Alarm when batch put operations produce failed records for a Kinesis stream.

**Intent:** Detect batch put failures.

**PromQL criteria:** `sum({__name__="PutRecords.FailedRecords", "@instrumentation.@name"="cloudwatch.aws/kinesis", StreamName="`your-stream-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable failure count.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**ReadProvisionedThroughputExceeded**

**Labels:** StreamName

**Alarm description:** Alarm when consumer reads exceed provisioned throughput for a Kinesis stream.

**Intent:** Detect consumer read throttling.

**PromQL criteria:** `avg({__name__="ReadProvisionedThroughputExceeded", "@instrumentation.@name"="cloudwatch.aws/kinesis", StreamName="`your-stream-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Any sustained throttling indicates capacity needs.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**SubscribeToShardEvent.MillisBehindLatest**

**Labels:** StreamName, ConsumerName

**Alarm description:** Alarm when an enhanced fan-out consumer falls behind the latest record.

**Intent:** Detect enhanced fan-out consumer processing lag.

**PromQL criteria:** `avg({__name__="SubscribeToShardEvent.MillisBehindLatest", "@instrumentation.@name"="cloudwatch.aws/kinesis", StreamName="`your-stream-name`",ConsumerName="`your-consumer-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable processing delay.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**WriteProvisionedThroughputExceeded**

**Labels:** StreamName

**Alarm description:** Alarm when producer writes exceed provisioned throughput for a Kinesis stream.

**Intent:** Detect producer write throttling.

**PromQL criteria:** `avg({__name__="WriteProvisionedThroughputExceeded", "@instrumentation.@name"="cloudwatch.aws/kinesis", StreamName="`your-stream-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Sustained throttling indicates capacity needs.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## AWS Lambda

**ClaimedAccountConcurrency**

**Alarm description:** Alarm when claimed account concurrency exceeds the threshold.

**Intent:** Detect account approaching concurrency quota.

**PromQL criteria:** `max({__name__="ClaimedAccountConcurrency", "@instrumentation.@name"="cloudwatch.aws/lambda"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set to percentage of regional concurrency limit.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

**Errors**

**Labels:** FunctionName

**Alarm description:** Alarm when function error count exceeds the threshold for a Lambda function.

**Intent:** Detect high function error count.

**PromQL criteria:** `sum({__name__="Errors", "@instrumentation.@name"="cloudwatch.aws/lambda", FunctionName="`your-function-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable error volume.

**Evaluation interval:** 60

**Pending period:** 180

**Recovery period:** 300

**Throttles**

**Labels:** FunctionName

**Alarm description:** Alarm when function invocations are throttled for a Lambda function.

**Intent:** Detect function invocation throttling.

**PromQL criteria:** `sum({__name__="Throttles", "@instrumentation.@name"="cloudwatch.aws/lambda", FunctionName="`your-function-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Throttling indicates concurrency limit reached.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**Duration**

**Labels:** FunctionName

**Alarm description:** Alarm when p90 function duration exceeds the threshold for a Lambda function.

**Intent:** Detect long-running function invocations.

**PromQL criteria:** `histogram_quantile(0.9, {__name__="Duration", "@instrumentation.@name"="cloudwatch.aws/lambda", FunctionName="`your-function-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set relative to function timeout.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**ConcurrentExecutions**

**Labels:** FunctionName

**Alarm description:** Alarm when concurrent executions exceed the threshold for a Lambda function.

**Intent:** Detect function approaching concurrency limits.

**PromQL criteria:** `max({__name__="ConcurrentExecutions", "@instrumentation.@name"="cloudwatch.aws/lambda", FunctionName="`your-function-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set to percentage of reserved concurrency.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

## AWS Lambda Insights

**memory\_utilization**

**Labels:** function\_name

**Alarm description:** Alarm when average memory utilization exceeds 90% for a Lambda function.

**Intent:** Detect function approaching configured memory limit.

**PromQL criteria:** `avg({__name__="memory_utilization", "@instrumentation.@name"="cloudwatch.aws/lambda-insights", function_name="`your-function-name`"}) > 90`

**Recommended threshold:** 90 (embedded in query)

**Threshold justification:** Above 90% risks out-of-memory failures.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

## NAT Gateway

**ErrorPortAllocation**

**Labels:** NatGatewayId

**Alarm description:** Alarm when the NAT gateway fails to allocate a port for new connections.

**Intent:** Detect port allocation failures preventing new connections.

**PromQL criteria:** `sum({__name__="ErrorPortAllocation", "@instrumentation.@name"="cloudwatch.aws/natgateway", NatGatewayId="`your-nat-gateway-id`"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Any allocation failure impacts connectivity.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**PacketsDropCount**

**Labels:** NatGatewayId

**Alarm description:** Alarm when the NAT gateway drops packets exceeding the threshold.

**Intent:** Detect packet drops indicating capacity or connectivity issues.

**PromQL criteria:** `sum({__name__="PacketsDropCount", "@instrumentation.@name"="cloudwatch.aws/natgateway", NatGatewayId="`your-nat-gateway-id`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable drop rate.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## AWS PrivateLink endpoints

**PacketsDropped**

**Labels:** VpcId, VpcEndpointId, EndpointType, SubnetId, ServiceName

**Alarm description:** Alarm when a VPC endpoint drops packets exceeding the threshold.

**Intent:** Detect unhealthy endpoint or endpoint service.

**PromQL criteria:** `sum({__name__="PacketsDropped", "@instrumentation.@name"="cloudwatch.aws/privatelinkendpoints", VpcId="`your-vpc-id`",VpcEndpointId="`your-vpc-endpoint-id`",EndpointType="`your-endpoint-type`",SubnetId="`your-subnet-id`",ServiceName="`your-service-name`"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable drop rate.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## AWS PrivateLink services

**RstPacketsSent**

**Labels:** ServiceId, LoadBalancerArn, Az

**Alarm description:** Alarm when the RST packet rate exceeds the threshold for an endpoint service.

**Intent:** Detect unhealthy targets of endpoint service.

**PromQL criteria:** `sum({__name__="RstPacketsSent", "@instrumentation.@name"="cloudwatch.aws/privatelinkservices", ServiceId="SVC",LoadBalancerArn="LB",Az="AZ"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable RST packet rate.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## RDS

**CPUUtilization**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when average CPU utilization exceeds 90% for an RDS instance.

**Intent:** Detect high CPU preventing performance degradation.

**PromQL criteria:** `avg({__name__="CPUUtilization", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) > 90`

**Recommended threshold:** 90 (embedded in query)

**Threshold justification:** 90% indicates near saturation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**DatabaseConnections**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when database connections exceed the threshold for an RDS instance.

**Intent:** Prevent rejected connections at maximum limit.

**PromQL criteria:** `avg({__name__="DatabaseConnections", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set to percentage of max\_connections parameter.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**EBSByteBalance%**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when EBS byte balance drops below 10% for an RDS instance.

**Intent:** Detect low throughput credits causing bottlenecks.

**PromQL criteria:** `avg({__name__="EBSByteBalance%", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) < 10`

**Recommended threshold:** 10 (embedded in query)

**Threshold justification:** Below 10% risks throughput degradation.

**Evaluation interval:** 60

**Pending period:** 180

**Recovery period:** 180

**EBSIOBalance%**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when EBS IO balance drops below 10% for an RDS instance.

**Intent:** Detect low IOPS credits causing bottlenecks.

**PromQL criteria:** `avg({__name__="EBSIOBalance%", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) < 10`

**Recommended threshold:** 10 (embedded in query)

**Threshold justification:** Below 10% risks IOPS degradation.

**Evaluation interval:** 60

**Pending period:** 180

**Recovery period:** 180

**FreeableMemory**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when freeable memory drops below the threshold for an RDS instance.

**Intent:** Prevent out-of-memory causing rejected connections.

**PromQL criteria:** `avg({__name__="FreeableMemory", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on instance class memory.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**FreeLocalStorage**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when free local storage drops below the threshold for an Aurora instance.

**Intent:** Prevent Aurora local storage exhaustion.

**PromQL criteria:** `avg({__name__="FreeLocalStorage", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on minimum required for operations.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**FreeStorageSpace**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when free storage space drops below the threshold for an RDS instance.

**Intent:** Prevent storage-full downtime.

**PromQL criteria:** `min({__name__="FreeStorageSpace", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on storage growth rate and provisioned size.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**MaximumUsedTransactionIDs**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when maximum used transaction IDs exceed 1 billion for an RDS instance.

**Intent:** Prevent PostgreSQL transaction ID wraparound.

**PromQL criteria:** `avg({__name__="MaximumUsedTransactionIDs", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) > 1000000000`

**Recommended threshold:** 1000000000 (embedded in query)

**Threshold justification:** 1 billion indicates approaching wraparound danger.

**Evaluation interval:** 60

**Pending period:** 60

**Recovery period:** 60

**ReadLatency**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when p90 read latency exceeds the threshold for an RDS instance.

**Intent:** Detect high read latency indicating disk issues.

**PromQL criteria:** `histogram_quantile(0.9, {__name__="ReadLatency", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable application latency.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**ReplicaLag**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when replication lag exceeds 60 seconds for an RDS read replica.

**Intent:** Detect replication delay risking data loss.

**PromQL criteria:** `max({__name__="ReplicaLag", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) > 60`

**Recommended threshold:** 60 (embedded in query)

**Threshold justification:** 60 seconds represents significant lag for most workloads.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

**WriteLatency**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when p90 write latency exceeds the threshold for an RDS instance.

**Intent:** Detect high write latency indicating disk issues.

**PromQL criteria:** `histogram_quantile(0.9, {__name__="WriteLatency", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable application latency.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**DBLoad**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when average database load exceeds the threshold for an RDS instance.

**Intent:** Detect high database load degrading performance.

**PromQL criteria:** `avg({__name__="DBLoad", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set to multiple of vCPU count.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**AuroraVolumeBytesLeftTotal**

**Labels:** DBClusterIdentifier

**Alarm description:** Alarm when Aurora cluster storage bytes remaining drops below the threshold.

**Intent:** Prevent Aurora cluster storage exhaustion.

**PromQL criteria:** `avg({__name__="AuroraVolumeBytesLeftTotal", "@instrumentation.@name"="cloudwatch.aws/rds", DBClusterIdentifier="CLUSTER"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on growth rate.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**AuroraBinlogReplicaLag**

**Labels:** DBClusterIdentifier

**Alarm description:** Alarm when Aurora binlog replica lag indicates an error state.

**Intent:** Detect writer instance replication errors.

**PromQL criteria:** `avg({__name__="AuroraBinlogReplicaLag", "@instrumentation.@name"="cloudwatch.aws/rds", DBClusterIdentifier="CLUSTER"}) <= -1`

**Recommended threshold:** -1 (embedded in query)

**Threshold justification:** -1 indicates error state.

**Evaluation interval:** 60

**Pending period:** 120

**Recovery period:** 120

**BlockedTransactions**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when blocked transaction count exceeds the threshold for an RDS instance.

**Intent:** Detect transaction blocking causing performance degradation.

**PromQL criteria:** `avg({__name__="BlockedTransactions", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable blocked transaction count.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**BufferCacheHitRatio**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when buffer cache hit ratio drops below 80% for an RDS instance.

**Intent:** Detect low cache efficiency causing performance decrease.

**PromQL criteria:** `avg({__name__="BufferCacheHitRatio", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) < 80`

**Recommended threshold:** 80 (embedded in query)

**Threshold justification:** Below 80% indicates excessive disk I/O.

**Evaluation interval:** 60

**Pending period:** 600

**Recovery period:** 600

**EngineUptime**

**Labels:** DBClusterIdentifier

**Alarm description:** Alarm when engine uptime drops to zero indicating an Aurora writer restart.

**Intent:** Detect Aurora writer instance downtime or crash.

**PromQL criteria:** `avg({__name__="EngineUptime", "@instrumentation.@name"="cloudwatch.aws/rds", DBClusterIdentifier="CLUSTER"}) <= 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Zero uptime indicates instance restart.

**Evaluation interval:** 60

**Pending period:** 120

**Recovery period:** 120

**RollbackSegmentHistoryListLength**

**Labels:** DBInstanceIdentifier

**Alarm description:** Alarm when rollback segment history list length exceeds 1 million for an Aurora instance.

**Intent:** Detect high rollback history causing CPU degradation.

**PromQL criteria:** `avg({__name__="RollbackSegmentHistoryListLength", "@instrumentation.@name"="cloudwatch.aws/rds", DBInstanceIdentifier="DB"}) > 1000000`

**Recommended threshold:** 1000000 (embedded in query)

**Threshold justification:** Above 1M causes performance issues.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**StorageNetworkThroughput**

**Labels:** DBClusterIdentifier

**Alarm description:** Alarm when storage network throughput exceeds the threshold for an Aurora cluster.

**Intent:** Detect high throughput risking network packet drops.

**PromQL criteria:** `avg({__name__="StorageNetworkThroughput", "@instrumentation.@name"="cloudwatch.aws/rds", DBClusterIdentifier="CLUSTER"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on instance network capacity.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## Route 53

**HealthCheckStatus**

**Labels:** HealthCheckId

**Alarm description:** Alarm when a Route 53 health check reports an unhealthy endpoint.

**Intent:** Detect unhealthy endpoints by using Route 53 health checkers.

**PromQL criteria:** `avg({__name__="HealthCheckStatus", "@instrumentation.@name"="cloudwatch.aws/route53", HealthCheckId="HC"}) < 1`

**Recommended threshold:** 1 (embedded in query)

**Threshold justification:** Below 1 indicates endpoint is failing health checks.

**Evaluation interval:** 60

**Pending period:** 180

**Recovery period:** 180

## S3

**4xxErrors**

**Labels:** BucketName, FilterId

**Alarm description:** Alarm when the 4xx error rate exceeds 5% for an S3 bucket.

**Intent:** Detect abnormal client error rates.

**PromQL criteria:** `avg({__name__="4xxErrors", "@instrumentation.@name"="cloudwatch.aws/s3", BucketName="BUCKET",FilterId="FILTER"}) > 0.05`

**Recommended threshold:** 0.05 (embedded in query)

**Threshold justification:** Above 5% indicates setup or access issues.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**5xxErrors**

**Labels:** BucketName, FilterId

**Alarm description:** Alarm when the 5xx error rate exceeds 5% for an S3 bucket.

**Intent:** Detect server-side errors affecting application.

**PromQL criteria:** `avg({__name__="5xxErrors", "@instrumentation.@name"="cloudwatch.aws/s3", BucketName="BUCKET",FilterId="FILTER"}) > 0.05`

**Recommended threshold:** 0.05 (embedded in query)

**Threshold justification:** Above 5% indicates S3 service issues.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**OperationsFailedReplication**

**Labels:** SourceBucket, DestinationBucket, RuleId

**Alarm description:** Alarm when S3 replication operations fail for a bucket.

**Intent:** Detect replication failures risking data inconsistency.

**PromQL criteria:** `max({__name__="OperationsFailedReplication", "@instrumentation.@name"="cloudwatch.aws/s3", SourceBucket="SRC",DestinationBucket="DST",RuleId="RULE"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Any failed replication requires investigation.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## S3 Object Lambda

**4xxErrors**

**Labels:** AccessPointName, DataSourceARN

**Alarm description:** Alarm when the 4xx error rate exceeds 5% for an S3 Object Lambda access point.

**Intent:** Detect abnormal client error rates for Object Lambda.

**PromQL criteria:** `avg({__name__="4xxErrors", "@instrumentation.@name"="cloudwatch.aws/s3objectlambda", AccessPointName="AP",DataSourceARN="ARN"}) > 0.05`

**Recommended threshold:** 0.05 (embedded in query)

**Threshold justification:** Above 5% indicates setup issues.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**5xxErrors**

**Labels:** AccessPointName, DataSourceARN

**Alarm description:** Alarm when the 5xx error rate exceeds 5% for an S3 Object Lambda access point.

**Intent:** Detect server-side errors in Object Lambda.

**PromQL criteria:** `avg({__name__="5xxErrors", "@instrumentation.@name"="cloudwatch.aws/s3objectlambda", AccessPointName="AP",DataSourceARN="ARN"}) > 0.05`

**Recommended threshold:** 0.05 (embedded in query)

**Threshold justification:** Above 5% indicates Lambda or S3 issues.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**LambdaResponse4xx**

**Labels:** AccessPointName, DataSourceARN

**Alarm description:** Alarm when the Lambda function 4xx response rate exceeds 5% for an S3 Object Lambda access point.

**Intent:** Detect Lambda function client errors.

**PromQL criteria:** `avg({__name__="LambdaResponse4xx", "@instrumentation.@name"="cloudwatch.aws/s3objectlambda", AccessPointName="AP",DataSourceARN="ARN"}) > 0.05`

**Recommended threshold:** 0.05 (embedded in query)

**Threshold justification:** Above 5% indicates Lambda function issues.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

## SNS

**NumberOfMessagesPublished**

**Labels:** TopicName

**Alarm description:** Alarm when the number of messages published drops below the threshold for an SNS topic.

**Intent:** Detect significant drop in publishing volume.

**PromQL criteria:** `sum({__name__="NumberOfMessagesPublished", "@instrumentation.@name"="cloudwatch.aws/sns", TopicName="TOPIC"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on minimum expected traffic.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**NumberOfNotificationsDelivered**

**Labels:** TopicName

**Alarm description:** Alarm when the number of notifications delivered drops below the threshold for an SNS topic.

**Intent:** Detect drop in notification delivery volume.

**PromQL criteria:** `sum({__name__="NumberOfNotificationsDelivered", "@instrumentation.@name"="cloudwatch.aws/sns", TopicName="TOPIC"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on minimum expected deliveries.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**NumberOfNotificationsFailed**

**Labels:** TopicName

**Alarm description:** Alarm when failed notification delivery count exceeds the threshold for an SNS topic.

**Intent:** Detect delivery failures.

**PromQL criteria:** `sum({__name__="NumberOfNotificationsFailed", "@instrumentation.@name"="cloudwatch.aws/sns", TopicName="TOPIC"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable failure rate.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**NumberOfNotificationsFilteredOut-InvalidAttributes**

**Labels:** TopicName

**Alarm description:** Alarm when notifications are filtered out due to invalid message attributes.

**Intent:** Detect invalid message attributes.

**PromQL criteria:** `sum({__name__="NumberOfNotificationsFilteredOut-InvalidAttributes", "@instrumentation.@name"="cloudwatch.aws/sns", TopicName="TOPIC"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Any invalid filter indicates misconfiguration.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**NumberOfNotificationsFilteredOut-InvalidMessageBody**

**Labels:** TopicName

**Alarm description:** Alarm when notifications are filtered out due to invalid message bodies.

**Intent:** Detect invalid message bodies.

**PromQL criteria:** `sum({__name__="NumberOfNotificationsFilteredOut-InvalidMessageBody", "@instrumentation.@name"="cloudwatch.aws/sns", TopicName="TOPIC"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Any invalid filter indicates misconfiguration.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**NumberOfNotificationsRedrivenToDlq**

**Labels:** TopicName

**Alarm description:** Alarm when notifications are sent to the dead-letter queue for an SNS topic.

**Intent:** Detect messages sent to dead-letter queue.

**PromQL criteria:** `sum({__name__="NumberOfNotificationsRedrivenToDlq", "@instrumentation.@name"="cloudwatch.aws/sns", TopicName="TOPIC"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Any DLQ message indicates delivery issues.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**NumberOfNotificationsFailedToRedriveToDlq**

**Labels:** TopicName

**Alarm description:** Alarm when notifications fail to be sent to the dead-letter queue for an SNS topic.

**Intent:** Detect DLQ delivery failures.

**PromQL criteria:** `sum({__name__="NumberOfNotificationsFailedToRedriveToDlq", "@instrumentation.@name"="cloudwatch.aws/sns", TopicName="TOPIC"}) > 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Failed DLQ means lost error tracking.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**SMSMonthToDateSpentUSD**

**Labels:** TopicName

**Alarm description:** Alarm when SMS spending approaches the account quota for an SNS topic.

**Intent:** Detect SMS spend approaching quota.

**PromQL criteria:** `max({__name__="SMSMonthToDateSpentUSD", "@instrumentation.@name"="cloudwatch.aws/sns", TopicName="TOPIC"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on account SMS quota.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

**SMSSuccessRate**

**Labels:** TopicName

**Alarm description:** Alarm when the SMS delivery success rate drops below the threshold for an SNS topic.

**Intent:** Detect failing SMS deliveries.

**PromQL criteria:** `avg({__name__="SMSSuccessRate", "@instrumentation.@name"="cloudwatch.aws/sns", TopicName="TOPIC"}) < `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable delivery rate.

**Evaluation interval:** 60

**Pending period:** 300

**Recovery period:** 300

## SQS

**ApproximateAgeOfOldestMessage**

**Labels:** QueueName

**Alarm description:** Alarm when the oldest message age exceeds the threshold for an SQS queue.

**Intent:** Detect messages not processed quickly enough.

**PromQL criteria:** `max({__name__="ApproximateAgeOfOldestMessage", "@instrumentation.@name"="cloudwatch.aws/sqs", QueueName="QUEUE"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on acceptable message processing time.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**ApproximateNumberOfMessagesNotVisible**

**Labels:** QueueName

**Alarm description:** Alarm when the number of in-flight messages exceeds the threshold for an SQS queue.

**Intent:** Detect high in-flight messages indicating consumer issues.

**PromQL criteria:** `avg({__name__="ApproximateNumberOfMessagesNotVisible", "@instrumentation.@name"="cloudwatch.aws/sqs", QueueName="QUEUE"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on expected processing volume.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**ApproximateNumberOfMessagesVisible**

**Labels:** QueueName

**Alarm description:** Alarm when the number of visible messages exceeds the threshold for an SQS queue.

**Intent:** Detect message backlog indicating slow consumers.

**PromQL criteria:** `avg({__name__="ApproximateNumberOfMessagesVisible", "@instrumentation.@name"="cloudwatch.aws/sqs", QueueName="QUEUE"}) > `THRESHOLD``

**Recommended threshold:** `THRESHOLD` (embedded in query)

**Threshold justification:** Set based on expected queue depth.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

**NumberOfMessagesSent**

**Labels:** QueueName

**Alarm description:** Alarm when no messages are sent to an SQS queue.

**Intent:** Detect producers stopped sending messages.

**PromQL criteria:** `sum({__name__="NumberOfMessagesSent", "@instrumentation.@name"="cloudwatch.aws/sqs", QueueName="QUEUE"}) <= 0`

**Recommended threshold:** 0 (embedded in query)

**Threshold justification:** Zero messages indicates producer failure.

**Evaluation interval:** 60

**Pending period:** 900

**Recovery period:** 900

## VPN

**TunnelState (VPN level)**

**Labels:** VpnId

**Alarm description:** Alarm when at least one VPN tunnel is in a DOWN state.

**Intent:** Detect at least one tunnel in DOWN state.

**PromQL criteria:** `min({__name__="TunnelState", "@instrumentation.@name"="cloudwatch.aws/vpn", VpnId="VPN"}) < 1`

**Recommended threshold:** 1 (embedded in query)

**Threshold justification:** Below 1 means tunnel is down.

**Evaluation interval:** 300

**Pending period:** 900

**Recovery period:** 900

**TunnelState (Tunnel level)**

**Labels:** TunnelIpAddress

**Alarm description:** Alarm when a specific VPN tunnel is in a DOWN state.

**Intent:** Detect specific tunnel in DOWN state.

**PromQL criteria:** `min({__name__="TunnelState", "@instrumentation.@name"="cloudwatch.aws/vpn", TunnelIpAddress="IP"}) < 1`

**Recommended threshold:** 1 (embedded in query)

**Threshold justification:** Below 1 means tunnel is down.

**Evaluation interval:** 300

**Pending period:** 900

**Recovery period:** 900
