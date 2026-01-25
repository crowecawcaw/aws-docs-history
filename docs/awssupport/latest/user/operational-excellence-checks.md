# Operational Excellence

You can use the following checks for the operational excellence category.

###### Check names

- [Amazon API Gateway Not Logging Execution Logs](operational-excellence-checks.md#api-gw-execution-logging-enabled "operational-excellence-checks.md#api-gw-execution-logging-enabled")
- [Amazon API Gateway REST APIs Without X-Ray Tracing Enabled](operational-excellence-checks.md#api-gw-xray-enabled "operational-excellence-checks.md#api-gw-xray-enabled")
- [Amazon CloudFront Access Log Configured](operational-excellence-checks.md#cloudfront-access-log-configured "operational-excellence-checks.md#cloudfront-access-log-configured")
- [Amazon CloudWatch Alarm Action is Disabled](operational-excellence-checks.md#cloudwatch-alarm-action-disabled "operational-excellence-checks.md#cloudwatch-alarm-action-disabled")
- [Amazon EC2 Instance Not Managed by AWS Systems Manager](operational-excellence-checks.md#ec2-instance-managed-ssm "operational-excellence-checks.md#ec2-instance-managed-ssm")
- [Amazon ECR Repository With Tag Immutability Disabled](operational-excellence-checks.md#ecr-private-tag-immutability-enabled "operational-excellence-checks.md#ecr-private-tag-immutability-enabled")
- [Amazon ECS clusters with Container Insights disabled](operational-excellence-checks.md#ecs-container-insights-enabled "operational-excellence-checks.md#ecs-container-insights-enabled")
- [Amazon ECS task logging not enabled](operational-excellence-checks.md#ecs-task-definition-log-configuration "operational-excellence-checks.md#ecs-task-definition-log-configuration")
- [Amazon OpenSearch Service logging CloudWatch not configured](operational-excellence-checks.md#opensearch-logs-to-cloudwatch "operational-excellence-checks.md#opensearch-logs-to-cloudwatch")
- [Amazon RDS DB instances in the clusters with heterogeneous parameter groups](operational-excellence-checks.md#rds-db-instances-heterogeneous-parameter-groups "operational-excellence-checks.md#rds-db-instances-heterogeneous-parameter-groups")
- [Amazon RDS Enhanced Monitoring is turned off](operational-excellence-checks.md#rds-enhanced-monitoring-off "operational-excellence-checks.md#rds-enhanced-monitoring-off")
- [Amazon RDS Performance Insights is turned off](operational-excellence-checks.md#rds-performance-insights-off "operational-excellence-checks.md#rds-performance-insights-off")
- [Amazon RDS track_counts parameter is turned off](operational-excellence-checks.md#rds-track-counts-parameters-off "operational-excellence-checks.md#rds-track-counts-parameters-off")
- [Amazon Redshift cluster audit logging](operational-excellence-checks.md#redshift-audit-logging-enabled "operational-excellence-checks.md#redshift-audit-logging-enabled")
- [Amazon S3 Access Logs Enabled](operational-excellence-checks.md#Amazon-S3-Server-Access-Logs-Enabled "operational-excellence-checks.md#Amazon-S3-Server-Access-Logs-Enabled")
- [Amazon S3 does not have Event Notifications enabled](operational-excellence-checks.md#s3-event-notification-enabled "operational-excellence-checks.md#s3-event-notification-enabled")
- [Amazon SNS Topics Not Logging Message Delivery Status](operational-excellence-checks.md#sns-topics-not-logging-message-delivery-status "operational-excellence-checks.md#sns-topics-not-logging-message-delivery-status")
- [Amazon VPC Without Flow Logs](operational-excellence-checks.md#vpc-flow-logs-enabled "operational-excellence-checks.md#vpc-flow-logs-enabled")
- [Application Load Balancers and Classic Load Balancers Without Access Logs Enabled](operational-excellence-checks.md#elb-logging-enabled "operational-excellence-checks.md#elb-logging-enabled")
- [CloudFormation Stack Notification](operational-excellence-checks.md#cloudformation-stack-notification "operational-excellence-checks.md#cloudformation-stack-notification")
- [AWS CloudTrail data events logging for objects in an S3 bucket](operational-excellence-checks.md#cloudtrail-s3-dataevents-enabled "operational-excellence-checks.md#cloudtrail-s3-dataevents-enabled")
- [AWS CodeBuild Project Logging](operational-excellence-checks.md#codebuild-project-logging-enabled "operational-excellence-checks.md#codebuild-project-logging-enabled")
- [AWS CodeDeploy Auto Rollback and Monitor Enabled](operational-excellence-checks.md#codedeploy-auto-rollback-monitor-enabled "operational-excellence-checks.md#codedeploy-auto-rollback-monitor-enabled")
- [AWS CodeDeploy Lambda is using all-at-once deployment configuration](operational-excellence-checks.md#codedeploy-lambda-allatonce-traffic-shift-disabled "operational-excellence-checks.md#codedeploy-lambda-allatonce-traffic-shift-disabled")
- [AWS Elastic Beanstalk Enhanced Health Reporting is not Configured](operational-excellence-checks.md#elastic-beanstalk-enhanced-health-reporting-not-enabled "operational-excellence-checks.md#elastic-beanstalk-enhanced-health-reporting-not-enabled")
- [AWS Elastic Beanstalk with Managed Platform Updates Disabled](operational-excellence-checks.md#elastic-beanstalk-managed-updates-enabled "operational-excellence-checks.md#elastic-beanstalk-managed-updates-enabled")
- [AWS Fargate platform version is not latest](operational-excellence-checks.md#ecs-fargate-latest-platform-version "operational-excellence-checks.md#ecs-fargate-latest-platform-version")
- [AWS Systems Manager State Manager Association in Non-compliant Status](operational-excellence-checks.md#ec2-managedinstance-association-compliance-status-check "operational-excellence-checks.md#ec2-managedinstance-association-compliance-status-check")
- [CloudTrail trails are not configured with Amazon CloudWatch Logs](operational-excellence-checks.md#cloudtrail-cloudwatch-logs-enabled "operational-excellence-checks.md#cloudtrail-cloudwatch-logs-enabled")
- [Elastic Load Balancing Deletion Protection Not Enabled for Load Balancers](operational-excellence-checks.md#elb-deletion-protection-enabled "operational-excellence-checks.md#elb-deletion-protection-enabled")
- [RDS DB Cluster Deletion Protection Check](operational-excellence-checks.md#rds-db-cluster-deletion-protection "operational-excellence-checks.md#rds-db-cluster-deletion-protection")
- [RDS DB Instance Automatic Minor Version Upgrade Check](operational-excellence-checks.md#rds-automatic-minor-version-upgrade-enabled "operational-excellence-checks.md#rds-automatic-minor-version-upgrade-enabled")

## Amazon API Gateway Not Logging Execution Logs

**Description**

Checks if Amazon API Gateway has CloudWatch Logs turned on at the desired logging level.

Turn on CloudWatch logging for REST API methods or WebSocket API routes in Amazon API Gateway to collect execution logs in CloudWatch Logs for requests received by your APIs. The information contained in the execution logs helps identify and troubleshoot issues related to your API.

You can specify the logging level (ERROR, INFO) ID in the **loggingLevel** parameter in the AWS Config rules.

Refer to the REST API or WebSocket API documentation for more information about CloudWatch logging in Amazon API Gateway.

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz125`

**Source**

`AWS Config Managed Rule: api-gw-execution-logging-enabled`

**Alert Criteria**

Yellow: The CloudWatch logging setting for execution log collection isn't enabled at the desired logging level for an Amazon API Gateway.

**Recommended Action**

Turn on CloudWatch logging for execution logs for your Amazon API Gateway [REST APIs](../../../apigateway/latest/developerguide/set-up-logging.md#set-up-access-logging-using-console "../../../apigateway/latest/developerguide/set-up-logging.md#set-up-access-logging-using-console") or [WebSocket APIs](../../../apigateway/latest/developerguide/websocket-api-logging.md "../../../apigateway/latest/developerguide/websocket-api-logging.md") with the appropriate logging level (ERROR, INFO).

For more information, see [Create a flow log](../../../vpc/latest/userguide/working-with-flow-logs.md#create-flow-log "../../../vpc/latest/userguide/working-with-flow-logs.md#create-flow-log")

**Additional Resources**

- [Setting up CloudWatch logging for a REST API in API Gateway](../../../apigateway/latest/developerguide/set-up-logging.md "../../../apigateway/latest/developerguide/set-up-logging.md")
- [Configuring logging for a WebSocket API](../../../apigateway/latest/developerguide/websocket-api-logging.md "../../../apigateway/latest/developerguide/websocket-api-logging.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon API Gateway REST APIs Without X-Ray Tracing Enabled

**Description**

Checks if Amazon API Gateway REST APIs have AWS X-Ray tracing turned on.

Turn on X-Ray tracing for your REST APIs to allow API Gateway to sample API invocation requests with trace information. This allows you to take advantage of AWS X-Ray to trace and analyze requests as they travel through your API Gateway REST APIs to the downstream services.

For more information, see [Tracing user requests to REST APIs using X-Ray](../../../apigateway/latest/developerguide/apigateway-xray.md "../../../apigateway/latest/developerguide/apigateway-xray.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz126`

**Source**

`AWS Config Managed Rule: api-gw-xray-enabled`

**Alert Criteria**

Yellow: X-Ray tracing is not turned on for an API Gateway REST API.

**Recommended Action**

Turn on X-Ray tracing for your API Gateway REST APIs.

For more information, see [Setting up AWS X-Ray with API Gateway REST APIs](../../../apigateway/latest/developerguide/apigateway-enabling-xray.md "../../../apigateway/latest/developerguide/apigateway-enabling-xray.md").

**Additional Resources**

- [Tracing user requests to REST APIs using X-Ray](../../../apigateway/latest/developerguide/apigateway-xray.md "../../../apigateway/latest/developerguide/apigateway-xray.md")
- [What is AWS X-Ray?](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon CloudFront Access Log Configured

**Description**

Checks if Amazon CloudFront distributions are configured to capture information from Amazon S3 server access logs. Amazon S3 server access logs contain detailed information about every user request that CloudFront receives.

You can adjust the the name of the Amazon S3 bucket for storing server access logs, using the **S3BucketName** parameter in your AWS Config rules.

For more information, see [Configuring and using standard logs (access logs)](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz110`

**Source**

`AWS Config Managed Rule: cloudfront-accesslogs-enabled`

**Alert Criteria**

Yellow: Amazon CloudFront access logging is not enabled

**Recommended Action**

Make sure that you turn on CloudFront access logging to capture detailed information about every user request that CloudFront receives.

You can turn on standard logs when you create or update a distribution.

For more information, see [Values that you specify when you create or update a distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md").

**Additional Resources**

- [Values that you specify when you create or update a distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md")
- [Configuring and using standard logs (access logs)](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon CloudWatch Alarm Action is Disabled

**Description**

Checks if your Amazon CloudWatch alarm action is in a disabled state.

You can use the AWS CLI to enable or disable the action feature in your alarm. Or, you can programatically disable or enable the action feature using the AWS SDK. When the alarm action feature is turned off, CloudWatch doesn't perform any defined action in any state (OK, INSUFFICIENT_DATA, ALARM).

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz109`

**Source**

`AWS Config Managed Rule: cloudwatch-alarm-action-enabled-check`

**Alert Criteria**

Yellow: Amazon CloudWatch alarm action is not enabled. No action is performed in any alarm state.

**Recommended Action**

Enable actions in your CloudWatch alarms unless you have a valid reason to disable them, such as for testing purposes.

If the CloudWatch alarm is no longer needed, delete it to avoid incurring unnecessary costs.

For more information, see [enable-alarm-actions](../../../cli/latest/reference/cloudwatch/enable-alarm-actions.md "../../../cli/latest/reference/cloudwatch/enable-alarm-actions.md") in the AWS CLI Command Reference and [func (\*CloudWatch) EnableAlarmActions](../../../sdk-for-go/api/service/cloudwatch.md#CloudWatch.EnableAlarmActions "../../../sdk-for-go/api/service/cloudwatch.md#CloudWatch.EnableAlarmActions") in the AWS SDK for Go API Reference.

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon EC2 Instance Not Managed by AWS Systems Manager

**Description**

Checks if the Amazon EC2 instances in your account are managed by AWS Systems Manager.

Systems Manager helps you understand and control the current state of your Amazon EC2 instance and OS configurations. With Systems Manager, you can collect software configuration and inventory information about your fleet of instances, including the software installed on them. This allows you to track detailed system configuration, OS patch levels, application configurations, and other details about your deployment.

For more information, see [Setting up Systems Manager for EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz145`

**Source**

`AWS Config Managed Rule: ec2-instance-managed-by-systems-manager`

**Alert Criteria**

Yellow: The Amazon EC2 instances are not managed by Systems Manager.

**Recommended Action**

Configure your Amazon EC2 instance to be managed by Systems Manager.

This check can't be excluded from view in the Trusted Advisor console.

For more information, see [Why is my EC2 instance not displaying as a managed node or showing a "Connection lost" status in Systems Manager?](https://repost.aws/knowledge-center/systems-manager-ec2-instance-not-appear "https://repost.aws/knowledge-center/systems-manager-ec2-instance-not-appear").

**Additional Resources**

[Setting up Systems Manager for EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon ECR Repository With Tag Immutability Disabled

**Description**

Checks if a private Amazon ECR repository has image tag immutability turned on.

Turn on image tag immutability for a private Amazon ECR repository to prevent image tags from being overwritten. This allows you to rely on descriptive tags as a reliable mechanism to track and uniquely identify images.For example, if image tag immutability is turned on, then users can reliably use an image tag to correlate a deployed image version with the build that produced such image.

For more information, see [Image tag mutability](../../../AmazonECR/latest/userguide/image-tag-mutability.md "../../../AmazonECR/latest/userguide/image-tag-mutability.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz129`

**Source**

`AWS Config Managed Rule: ecr-private-tag-immutability-enabled`

**Alert Criteria**

Yellow: An Amazon ECR private repository doesn’t have tag immutability turned on.

**Recommended Action**

Turn on image tag immutability for your Amazon ECR private repositories.

For more information, see [Image tag mutability](../../../AmazonECR/latest/userguide/image-tag-mutability.md "../../../AmazonECR/latest/userguide/image-tag-mutability.md").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon ECS clusters with Container Insights disabled

**Description**

Checks if Amazon CloudWatch Container Insights is turned on for your Amazon ECS clusters.

CloudWatch Container Insights collects, aggregates, and summarizes metrics and logs from your containerized applications and microservices. The metrics include utilization for resources such as CPU, memory, disk, and network.

For more information, see [Amazon ECS CloudWatch Container Insights](../../../AmazonECS/latest/developerguide/cloudwatch-container-insights.md "../../../AmazonECS/latest/developerguide/cloudwatch-container-insights.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz173`

**Source**

`AWS Config Managed Rule: ecs-container-insights-enabled`

**Alert Criteria**

Yellow: Amazon ECS cluster does not have container insights enabled.

**Recommended Action**

Turn on CloudWatch Container Insights on your Amazon ECS clusters.

For more information, see [Using Container Insights](../../../AmazonCloudWatch/latest/monitoring/ContainerInsights.md "../../../AmazonCloudWatch/latest/monitoring/ContainerInsights.md").

**Additional Resources**

[Amazon ECS CloudWatch Container Insights](../../../AmazonECS/latest/developerguide/cloudwatch-container-insights.md "../../../AmazonECS/latest/developerguide/cloudwatch-container-insights.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon ECS task logging not enabled

**Description**

Checks if log configuration is set on active Amazon ECS task definitions.

Checking the log configuration in your Amazon ECS task definitions makes sure that logs generated by containers are properly configured and stored. This helps identify and troubleshoot issues more quickly, optimize performance, and meet compliance requirements.

By default, the logs that are captured show the command output that you typically see in an interactive terminal if you ran the container locally. The awslogs driver passes these logs from Docker to Amazon CloudWatch Logs.

For more information, see [Using the awslogs log driver](../../../AmazonECS/latest/developerguide/using_awslogs.md "../../../AmazonECS/latest/developerguide/using_awslogs.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz175`

**Source**

`AWS Config Managed Rule: ecs-task-definition-log-configuration`

**Alert Criteria**

Yellow: Amazon ECS task definition does not have a logging configuration.

**Recommended Action**

Consider specifying the log driver configuration in container definition to send log information to CloudWatch Logs or a different logging driver.

For more information, see [LogConfiguration](../../../AmazonECS/latest/APIReference/API_LogConfiguration.md "../../../AmazonECS/latest/APIReference/API_LogConfiguration.md").

**Additional Resources**

Consider specifying the log driver configuration in container definition to send log information to CloudWatch Logs or a different logging driver.

For more information, see [Example task definitions](../../../AmazonECS/latest/developerguide/example_task_definitions.md "../../../AmazonECS/latest/developerguide/example_task_definitions.md").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon OpenSearch Service logging CloudWatch not configured

**Description**

Checks if Amazon OpenSearch Service domains are configured to send logs to Amazon CloudWatch Logs.

Monitoring logs is crucial for maintaining the reliability, availability, and performance of OpenSearch Service.

Search slow logs, indexing slow logs, and error logs are useful for troubleshooting performance and stability issues your workload. These logs need to be enabled to capture data.

You can specify which log types that you want to filter (error, search, index) using the **logTypes** parameter in your AWS Config rules.

For more information, see [Monitoring Amazon OpenSearch Service domains](../../../opensearch-service/latest/developerguide/monitoring.md "../../../opensearch-service/latest/developerguide/monitoring.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz184`

**Source**

`AWS Config Managed Rule: opensearch-logs-to-cloudwatch`

**Alert Criteria**

Yellow: Amazon OpenSearch Service does not have a logging configuration with Amazon CloudWatch Logs

**Recommended Action**

Configure OpenSearch Service domains to publish logs to CloudWatch Logs.

For more information, see [Enabling log publishing (console)](../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md#createdomain-configure-slow-logs-console "../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md#createdomain-configure-slow-logs-console").

**Additional Resources**

- [Monitoring OpenSearch Service cluster metrics with Amazon CloudWatch](../../../opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.md "../../../opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon RDS DB instances in the clusters with heterogeneous parameter groups

**Description**

We recommend that all of the DB instances in the DB cluster use the same DB parameter group.

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

###### Note

When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.

If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**

`c1qf5bt010`

**Alert Criteria**

Yellow: DB clusters have the DB instances with heterogeneous parameter groups.

**Recommended Action**

Associate the DB instance with the DB parameter group associated with the writer instance in your DB cluster.

**Additional Resources**

When the DB instances in your DB cluster use different DB parameter groups, there can be an inconsistent behavior during a failover or compatibility issues between the DB instances in your DB cluster.

For more information, see [Working with parameter groups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.md").

**Report columns**

- Status
- Region
- Resource
- Recommended Value
- Engine Name
- Last Updated Time

## Amazon RDS Enhanced Monitoring is turned off

**Description**

Your database resources don't have Enhanced Monitoring turned on. Enhanced Monitoring provides real-time operating system metrics for monitoring and troubleshooting.

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

###### Note

When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.

If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**

`c1qf5bt004`

**Alert Criteria**

Yellow: Amazon RDS resources don't have Enhanced Monitoring turned on.

**Recommended Action**

Turn on Enhanced Monitoring.

**Additional Resources**

Enhanced Monitoring for Amazon RDS provides additional visibility on the health of your DB instances. We recommend that you turn on Enhanced Monitoring. When the Enhanced Monitoring option is turned on for your DB instance, it collects vital operating system metrics and process information.

For more information, see [Monitoring OS metrics with Enhanced Monitoring](../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md "../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md").

**Report columns**

- Status
- Region
- Resource
- Recommended Value
- Engine Name
- Last Updated Time

## Amazon RDS Performance Insights is turned off

**Description**

Amazon RDS Performance Insights monitors your DB instance load to help you analyze and resolve database performance issues. We recommend that you turn on Performance Insights.

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

###### Note

When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.

If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**

`c1qf5bt012`

**Alert Criteria**

Yellow: Amazon RDS resources don't have Performance Insights turned on.

**Recommended Action**

Turn on Performance Insights.

**Additional Resources**

Performance Insights uses a lightweight data collection method that doesn't impact the performance of your applications. Performance Insights helps you assess the database load quickly.

For more information, see [Monitoring DB load with Performance Insights on Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md").

**Report columns**

- Status
- Region
- Resource
- Recommended Value
- Engine Name
- Last Updated Time

## Amazon RDS track_counts parameter is turned off

**Description**

When the **track_counts** parameter is turned off, the database doesn't collect the database activity statistics. Autovacuum requires these statistics to work correctly.

We recommend that you set **track_counts** parameter to 1

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

###### Note

When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.

If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**

`c1qf5bt027`

**Alert Criteria**

Yellow: DB parameter groups have **track_counts** parameter turned off.

**Recommended Action**

Set **track_counts** parameter to 1

**Additional Resources**

When **track_counts** parameter is turned off, it disables the collection of database activity statistics. The autovacuum daemon requires the collected statistics to identify the tables for autovacuum and autoanalyze.

For more information, see [Run-time Statistics for PostgreSQL](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-COUNTS "https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-COUNTS") on the PostgreSQL documentation website.

**Report columns**

- Status
- Region
- Resource
- Parameter Value
- Recommended Value
- Last Updated Time

## Amazon Redshift cluster audit logging

**Description**

Checks if your Amazon Redshift clusters have database audit logging turned on. Amazon Redshift logs information about connections and user activities in your database.

You can specify your desired logging Amazon S3 bucket name to match in the **bucketNames** parameter of your AWS Config rules.

For more information, see [Database audit logging](../../../redshift/latest/mgmt/db-auditing.md "../../../redshift/latest/mgmt/db-auditing.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz134`

**Source**

`AWS Config Managed Rule: redshift-audit-logging-enabled`

**Alert Criteria**

Yellow: An Amazon Redshift cluster has database audit logging disabled

**Recommended Action**

Turn on logging and monitoring for your Amazon Redshift clusters.

For more information, see [Configuring auditing using the console](../../../redshift/latest/mgmt/db-auditing-console.md "../../../redshift/latest/mgmt/db-auditing-console.md").

**Additional Resources**

[Logging and monitoring in Amazon Redshift](../../../redshift/latest/mgmt/security-incident-response.md "../../../redshift/latest/mgmt/security-incident-response.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

##

Amazon S3 Access Logs Enabled

**Description**

Checks the logging configuration of
Amazon Simple Storage Service
buckets.

Activating
server access logging delivers detailed hourly access logs to a specified
Amazon S3 bucket. Access logs contain request details including type, specified
resources, and processing time/date. Logging is turned off by default.
Customers should activate access logging to perform security audits or
analyze user behavior and usage patterns.

When logging is initially
activated,
the configuration is automatically validated. However, future modifications
can result in logging failures.
Note
that currently this check doesn’t examine Amazon S3 bucket write
permissions.

**Check ID**

`c1fd6b96l4`

**Alert Criteria**

- Yellow: The bucket does not have server access logging
  enabled.
- Yellow: The target bucket permissions do not include the root
  account, so
  Trusted Advisor
  cannot check it.
- Red: The target bucket does not exist.
- Red: The target bucket and the source bucket have different
  owners.
- Green: Bucket has server access logging enabled, the target
  exists, and permissions to write to target exists

**Recommended Action**

Activate
server access logging for all relevant Amazon S3 buckets. Server access logs
provide an audit trail that can be used to understand bucket access patterns
and investigate suspicious activity. Activating logging on all applicable
buckets will improve visibility into access events across your Amazon S3
environment. See [Enabling Logging Using
the Console](../../../AmazonS3/latest/userguide/ServerLogs.md "../../../AmazonS3/latest/userguide/ServerLogs.md") and [Enabling Logging Programmatically](../../../AmazonS3/latest/userguide/enable-server-access-logging.md "../../../AmazonS3/latest/userguide/enable-server-access-logging.md").

If the target bucket permissions do not include the root account and you
want
Trusted Advisor
to check the logging status, add the root account as a grantee. See [Editing Bucket Permissions](../../../AmazonS3/latest/userguide/security-iam.md "../../../AmazonS3/latest/userguide/security-iam.md").

If the target bucket does not exist, select an existing bucket as a target
or create a new one and select it. See [Managing Bucket
Logging](../../../AmazonS3/latest/userguide/ServerLogs.md "../../../AmazonS3/latest/userguide/ServerLogs.md").

If the target and source have different owners, change the target bucket
to one that has the same owner as the source bucket. See [Managing Bucket Logging](../../../AmazonS3/latest/userguide/ServerLogs.md "../../../AmazonS3/latest/userguide/ServerLogs.md").

**Additional Resources**

[Working with buckets](../../../AmazonS3/latest/userguide/creating-buckets-s3.md "../../../AmazonS3/latest/userguide/creating-buckets-s3.md")

[Server access logging](../../../AmazonS3/latest/userguide/ServerLogs.md "../../../AmazonS3/latest/userguide/ServerLogs.md")

[Server access log format](../../../AmazonS3/latest/userguide/LogFormat.md "../../../AmazonS3/latest/userguide/LogFormat.md")

[Deleting log files](../../../AmazonS3/latest/userguide/deleting-log-files-lifecycle.md "../../../AmazonS3/latest/userguide/deleting-log-files-lifecycle.md")

**Report columns**

- Status
- Region
- Resource ARN
- Bucket Name
- Target Name
- Target Exists
- Same Owner
- Write Enabled
- Reason
- Last Updated Time

## Amazon S3 does not have Event Notifications enabled

**Description**

Checks if Amazon S3 Event Notifications is enabled or is correctly configured with the desired destination or types.

The Amazon S3 Event Notifications feature sends notifications when certain events happen in your Amazon S3 buckets. Amazon S3 can send notification messages to Amazon SQS queues, Amazon SNS topics, and AWS Lambda functions.

You can specify your desired destination and event types using the **destinationArn** and **eventTypes** parameters of your AWS Config rules.

For more information, see [Amazon S3 Event Notifications](../../../AmazonS3/latest/userguide/EventNotifications.md "../../../AmazonS3/latest/userguide/EventNotifications.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz163`

**Source**

`AWS Config Managed Rule: s3-event-notifications-enabled`

**Alert Criteria**

Yellow: Amazon S3 does not have Event Notifications enabled, or not configured with the desired destination or types.

**Recommended Action**

Configure Amazon S3 Event Notfiications for object and bucket events.

For more information, see [Enabling and configuring event notifications using the Amazon S3 console](../../../AmazonS3/latest/userguide/enable-event-notifications.md "../../../AmazonS3/latest/userguide/enable-event-notifications.md").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon SNS Topics Not Logging Message Delivery Status

**Description**

Checks if Amazon SNS topics have message delivery status logging turned on.

Configure Amazon SNS topics for logging message delivery status to help provide better operational insights. For example, message delivery logging verifies if a message was delivered to a particular Amazon SNS endpoint. And, it also helps identify the response sent from the endpoint.

For more information, see [Amazon SNS message delivery status](../../../sns/latest/dg/sns-topic-attributes.md "../../../sns/latest/dg/sns-topic-attributes.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz121`

**Source**

`AWS Config Managed Rule: sns-topic-message-delivery-notification-enabled`

**Alert Criteria**

Yellow: Message delivery status logging is not turned on for an Amazon SNS topic.

**Recommended Action**

Turn on message delivery status logging for your SNS topics.

For more information, see [Configuring delivery status logging using the AWS Management Console](../../../sns/latest/dg/sns-topic-attributes.md#topics-attrib "../../../sns/latest/dg/sns-topic-attributes.md#topics-attrib").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Amazon VPC Without Flow Logs

**Description**

Checks if Amazon Virtual Private Cloud Flow Logs are created for a VPC.

You can specify the traffic type using the **trafficType** parameter in your AWS Config rules.

For more information, see [Logging IP traffic using VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz122`

**Source**

`AWS Config Managed Rule: vpc-flow-logs-enabled`

**Alert Criteria**

Yellow: VPCs do not have Amazon VPC Flow Logs.

**Recommended Action**

Create VPC Flow Logs for each of your VPCs.

For more information, see [Create a flow log](../../../vpc/latest/userguide/working-with-flow-logs.md#create-flow-log "../../../vpc/latest/userguide/working-with-flow-logs.md#create-flow-log")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Application Load Balancers and Classic Load Balancers Without Access Logs Enabled

**Description**

Checks if Application Load Balancers and Classic Load Balancers have access logging enabled.

Elastic Load Balancing provides access logs that capture detailed information about requests sent to your load balancer. Each log contains information such as the time the request was received, the client's IP address, latencies, request paths, and server responses. You can use these access logs to analyze traffic patterns and troubleshoot issues.

Access logs are an optional feature of Elastic Load Balancing that is disabled by default. After you enable access logs for your load balancer, Elastic Load Balancing captures the logs and stores them in the Amazon S3 bucket that you specify.

You can specify the access log Amazon S3 bucket that you want to check using the **s3BucketNames** parameter in your AWS Config rules.

For more information, see [Access logs for your Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md") or [Access logs for your Classic Load Balancer](../../../elasticloadbalancing/latest/classic/access-log-collection.md "../../../elasticloadbalancing/latest/classic/access-log-collection.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz167`

**Source**

`AWS Config Managed Rule: elb-logging-enabled`

**Alert Criteria**

Yellow: Access logs feature not enabled for an Application Load Balancer or Classic Load Balancer.

**Recommended Action**

Enable access logs for your Application Load Balancers and Classic Load Balancers.

For more information, see [Enable access logs for your Application Load Balancer](../../../elasticloadbalancing/latest/application/enable-access-logging.md "../../../elasticloadbalancing/latest/application/enable-access-logging.md") or [Enable access logs for your Classic Load Balancer](../../../elasticloadbalancing/latest/classic/enable-access-logs.md "../../../elasticloadbalancing/latest/classic/enable-access-logs.md").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## CloudFormation Stack Notification

**Description**

Checks if all of your CloudFormation stacks use Amazon SNS to receive notifications when an event occurs.

You can configure this check to look for specific Amazon SNS topic ARNs using parameters in your AWS Config rules.

For more information, see [Setting CloudFormationstack options](../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz111`

**Source**

`AWS Config Managed Rule: cloudformation-stack-notification-check`

**Alert Criteria**

Yellow: Amazon SNS event notifications for your CloudFormation stacks are not turned on.

**Recommended Action**

Make sure that your CloudFormation stacks use Amazon SNS to receive notifications when an event occurs.

Monitoring stack events helps you to respond quickly to unauthorized actions that might alter your AWS environment.

**Additional Resources**

[How can I receive an email alert when my AWS CloudFormation stack enters ROLLBACK_IN_PROGRESS status?](https://repost.aws/knowledge-center/cloudformation-rollback-email "https://repost.aws/knowledge-center/cloudformation-rollback-email")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## AWS CloudTrail data events logging for objects in an S3 bucket

**Description**

Checks if at least one AWS CloudTrail trail logs Amazon S3 data events for all of your Amazon S3 buckets.

For more information, see [Logging Amazon S3 API calls using AWS CloudTrail](../../../AmazonS3/latest/userguide/cloudtrail-logging.md "../../../AmazonS3/latest/userguide/cloudtrail-logging.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz166`

**Source**

`AWS Config Managed Rule: cloudtrail-s3-dataevents-enabled`

**Alert Criteria**

Yellow: AWS CloudTrail event logging for Amazon S3 buckets is not configured

**Recommended Action**

Enable CloudTrail event logging for Amazon S3 buckets and objects to track requests for target bucket access.

For more information, see [Enabling CloudTrail event logging for S3 buckets and objects](../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md "../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## AWS CodeBuild Project Logging

**Description**

Checks if the AWS CodeBuild project environment uses logging. Logging options can be logs in Amazon CloudWatch Logs, or built in a specified Amazon S3 bucket, or both. Enabling logging in a CodeBuild project can provide several benefits such as debugging and auditing.

You can specify the name of the Amazon S3 bucket or CloudWatch Logs group for storing the logs, using the **s3BucketNames** or **cloudWatchGroupNames** parameter in your AWS Config rules.

For more information, see [Monitoring AWS CodeBuild](../../../codebuild/latest/userguide/monitoring-builds.md "../../../codebuild/latest/userguide/monitoring-builds.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz113`

**Source**

`AWS Config Managed Rule: codebuild-project-logging-enabled`

**Alert Criteria**

Yellow: AWS CodeBuild project logging is not enabled.

**Recommended Action**

Make sure that logging is turned on in your AWS CodeBuild project. This check can't be excluded from view in the AWS Trusted Advisor console.

For more information, see [Logging and monitoring in AWS CodeBuild](../../../codebuild/latest/userguide/logging-monitoring.md "../../../codebuild/latest/userguide/logging-monitoring.md").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## AWS CodeDeploy Auto Rollback and Monitor Enabled

**Description**

Checks if the deployment group is configured with automatic deployment rollback and deployment monitoring with alarms attached. If something goes wrong during a deployment, it is automatically rolled back, and your application remains in a stable state

For more information, see [Redeploy and roll back a deployment with CodeDeploy](../../../codedeploy/latest/userguide/deployments-rollback-and-redeploy.md "../../../codedeploy/latest/userguide/deployments-rollback-and-redeploy.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz114`

**Source**

`AWS Config Managed Rule: codedeploy-auto-rollback-monitor-enabled`

**Alert Criteria**

Yellow: AWS CodeDeploy automatic deployment rollback and deployment monitoring are not enabled.

**Recommended Action**

Configure a deployment group or deployment to automatically roll back when a deployment fails or when a monitoring threshold you specify is met.

Configure alarm to monitor various metrics, such as CPU usage, memory usage, or network traffic, during the deployment process. If any of these metrics exceed certain thresholds, the alarms trigger, and the deployment is stopped or rolled back.

For information on setting up automatic rollbacks and configuring alarms for your deployment groups, see [Configure advanced options for a deployment group](../../../codedeploy/latest/userguide/deployment-groups-configure-advanced-options.md "../../../codedeploy/latest/userguide/deployment-groups-configure-advanced-options.md").

**Additional Resources**
[What is CodeDeploy?](../../../codedeploy/latest/userguide/welcome.md "../../../codedeploy/latest/userguide/welcome.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## AWS CodeDeploy Lambda is using all-at-once deployment configuration

**Description**

Checks if the AWS CodeDeploy deployment group for AWS Lambda compute platform is using all-at-once deployment configuration.

To reduce the risk of deployment failures of your Lambda functions in CodeDeploy, it's a best practice to use the canary or linear deployment configuration instead of the default option where all traffic is shifted from the original Lambda function to the updated function at once.

For more information, see [Lambda function versions](../../../lambda/latest/dg/configuration-versions.md "../../../lambda/latest/dg/configuration-versions.md") and [Deployment configuration](../../../codedeploy/latest/userguide/primary-components.md#primary-components-deployment-configuration "../../../codedeploy/latest/userguide/primary-components.md#primary-components-deployment-configuration").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz115`

**Source**

`AWS Config Managed Rule: codedeploy-lambda-allatonce-traffic-shift-disabled`

**Alert Criteria**

Yellow: AWS CodeDeploy Lambda deployment uses the all-at-once deployment configuration to shift all traffic to the updated Lambda functions at once.

**Recommended Action**

Use the Canary or Linear deployment configuration of CodeDeploy deployment group for the Lambda compute platform.

**Additional Resources**
[Deployment configuration](../../../codedeploy/latest/userguide/primary-components.md#primary-components-deployment-configuration "../../../codedeploy/latest/userguide/primary-components.md#primary-components-deployment-configuration")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## AWS Elastic Beanstalk Enhanced Health Reporting is not Configured

**Description**

Checks if an AWS Elastic Beanstalk environment is configured for enhanced health reporting.

Elastic Beanstalk enhanced health reporting provides detailed performance metrics, such as CPU usage, memory usage, network traffic, and infrastructure health information, such as number of instances and load balancer status.

For more information, see [Enhanced health reporting and monitoring](../../../elasticbeanstalk/latest/dg/health-enhanced.md "../../../elasticbeanstalk/latest/dg/health-enhanced.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz108`

**Source**

`AWS Config Managed Rule: beanstalk-enhanced-health-reporting-enabled`

**Alert Criteria**

Yellow: Elastic Beanstalk environment is not configured for enhanced health reporting

**Recommended Action**

Make sure that an Elastic Beanstalk environment is configured for enhanced health reporting.

For more information, see [Enabling enhanced health reporting using the Elastic Beanstalk console](../../../elasticbeanstalk/latest/dg/health-enhanced-enable.md#health-enhanced-enable-console "../../../elasticbeanstalk/latest/dg/health-enhanced-enable.md#health-enhanced-enable-console").

**Additional Resources**

- [Enabling Elastic Beanstalk enhanced health reporting](../../../elasticbeanstalk/latest/dg/health-enhanced-enable.md "../../../elasticbeanstalk/latest/dg/health-enhanced-enable.md")
- [Enhanced health reporting and monitoring](../../../elasticbeanstalk/latest/dg/health-enhanced.md "../../../elasticbeanstalk/latest/dg/health-enhanced.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## AWS Elastic Beanstalk with Managed Platform Updates Disabled

**Description**

Checks if managed platform updates in Elastic Beanstalk environments and configuration templates are enabled.

AWS Elastic Beanstalk regularly releases platform updates to provide fixes, software updates, and new features. With managed platform updates,Elastic Beanstalk can automatically perform platform updates for new patch and minor platform versions.

You can specify your desired update level in the **UpdateLevel** parameters of your AWS Config rules.

For more information, see [Updating your Elastic Beanstalk environment's platform version](../../../elasticbeanstalk/latest/dg/using-features.platform.md "../../../elasticbeanstalk/latest/dg/using-features.platform.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz177`

**Source**

`AWS Config Managed Rule: elastic-beanstalk-managed-updates-enabled`

**Alert Criteria**

Yellow: AWS Elastic Beanstalk managed platform updates is not configured at all, including at a minor or patch level.

**Recommended Action**

Enable managed platform updates in your Elastic Beanstalk environments, or configure it at a minor or update level.

For more information, see [Managed platform updates](../../../elasticbeanstalk/latest/dg/environment-platform-update-managed.md "../../../elasticbeanstalk/latest/dg/environment-platform-update-managed.md").

**Additional Resources**

- [Enabling Elastic Beanstalk enhanced health reporting](../../../elasticbeanstalk/latest/dg/health-enhanced-enable.md "../../../elasticbeanstalk/latest/dg/health-enhanced-enable.md")
- [Enhanced health reporting and monitoring](../../../elasticbeanstalk/latest/dg/health-enhanced.md "../../../elasticbeanstalk/latest/dg/health-enhanced.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## AWS Fargate platform version is not latest

**Description**

Checks if Amazon ECS is running the latest platform version of AWS Fargate. The Fargate platform version refers to a specific runtime environment for Fargate task infrastructure. It's a combination of the kernel and container runtime versions. New platform versions are released as runtime environment evolves. For example, if there are kernel or operating system updates, new features, bug fixes, or security updates.

For more information, see [Fargate task maintenance](../../../AmazonECS/latest/userguide/task-maintenance.md "../../../AmazonECS/latest/userguide/task-maintenance.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz174`

**Source**

`AWS Config Managed Rule: ecs-fargate-latest-platform-version`

**Alert Criteria**

Yellow: Amazon ECS is not running on the latest version of the Fargate platform.

**Recommended Action**

Update to the latest Fargate platform version.

For more information, see [Fargate task maintenance](../../../AmazonECS/latest/userguide/task-maintenance.md "../../../AmazonECS/latest/userguide/task-maintenance.md").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## AWS Systems Manager State Manager Association in Non-compliant Status

**Description**

Checks if the status of the AWS Systems Manager association compliance is COMPLIANT or NON_COMPLIANT after the association execution on the instance.

State Manager, a capability of AWS Systems Manager, is a secure and scalable configuration management service that automates the process of keeping your managed nodes and other AWS resources in a state that you define. A State Manager association is a configuration that you assign to your AWS resources. The configuration defines the state that you want to maintain on your resources, so it helps you to achieve the target, such as avoidance of configuration drifts across your Amazon EC2 instances.

For more information, see [AWS Systems Manager State Manager](../../../systems-manager/latest/userguide/systems-manager-state.md "../../../systems-manager/latest/userguide/systems-manager-state.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz147`

**Source**

`AWS Config Managed Rule: ec2-managedinstance-association-compliance-status-check`

**Alert Criteria**

Yellow: The status of the AWS Systems Manager association compliance is NON_COMPLIANT.

**Recommended Action**

Validate the status of the State Manager associations, and then take any needed actions to return the status back to COMPLIANT.

For more information, see [About State Manager](../../../systems-manager/latest/userguide/state-manager-about.md "../../../systems-manager/latest/userguide/state-manager-about.md").

**Additional Resources**

[AWS Systems Manager State Manager](../../../systems-manager/latest/userguide/systems-manager-state.md "../../../systems-manager/latest/userguide/systems-manager-state.md")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## CloudTrail trails are not configured with Amazon CloudWatch Logs

**Description**

Checks if AWS CloudTrail trails are configured to send logs to CloudWatch Logs.

Monitor CloudTrail Log files with CloudWatch Logs to trigger an automated response when critical events are captured in AWS CloudTrail.

For more information, see [Monitoring CloudTrail Log Files with CloudWatch Logs](../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md "../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz164`

**Source**

`AWS Config Managed Rule: cloud-trail-cloud-watch-logs-enabled`

**Alert Criteria**

Yellow: AWS CloudTrail is not set up with CloudWatch Logs integration.

**Recommended Action**

Configure CloudTrail trails to send log events to CloudWatch Logs.

For more information, see [Creating CloudWatch alarms for CloudTrail events: examples](../../../awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.md").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## Elastic Load Balancing Deletion Protection Not Enabled for Load Balancers

**Description**

Checks if deletion protection is turned on for your load balancers.

Elastic Load Balancing supports deletion protection for your Application Load Balancers, Network Load Balancers, and Gateway Load Balancers. Turn on deletion protection to prevent your load balancer from accidental deletion. Deletion protection is turned off by default when you create a load balancer. If your load balancers are part of a production environment, then consider turning on deletion protection.

Access logs are an optional feature of Elastic Load Balancing that is disabled by default. After you enable access logs for your load balancer, Elastic Load Balancing captures the logs and stores them in the Amazon S3 bucket that you specify.

For more information, see [Application Load Balancer Deletion protection](../../../elasticloadbalancing/latest/application/application-load-balancers.md#deletion-protection "../../../elasticloadbalancing/latest/application/application-load-balancers.md#deletion-protection"), [Network Load Balancers Deletion protection](../../../elasticloadbalancing/latest/network/network-load-balancers.md#deletion-protection "../../../elasticloadbalancing/latest/network/network-load-balancers.md#deletion-protection"), or [Gateway Load Balancers Deletion protection](../../../elasticloadbalancing/latest/gateway/gateway-load-balancers.md#deletion-protection "../../../elasticloadbalancing/latest/gateway/gateway-load-balancers.md#deletion-protection").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz168`

**Source**

`AWS Config Managed Rule: elb-deletion-protection-enabled`

**Alert Criteria**

Yellow: Deletion protection is not enabled for a load balancer.

**Recommended Action**

Turn on deletion protection for your Application Load Balancers, Network Load Balancers, and Gateway Load Balancers.

For more information, see [Application Load Balancer Deletion protection](../../../elasticloadbalancing/latest/application/application-load-balancers.md#deletion-protection "../../../elasticloadbalancing/latest/application/application-load-balancers.md#deletion-protection"), [Network Load Balancers Deletion protection](../../../elasticloadbalancing/latest/network/network-load-balancers.md#deletion-protection "../../../elasticloadbalancing/latest/network/network-load-balancers.md#deletion-protection"), or [Gateway Load Balancers Deletion protection](../../../elasticloadbalancing/latest/gateway/gateway-load-balancers.md#deletion-protection "../../../elasticloadbalancing/latest/gateway/gateway-load-balancers.md#deletion-protection").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## RDS DB Cluster Deletion Protection Check

**Description**

Checks if your Amazon RDS DB clusters have deletion protection enabled.

When a cluster is configured with deletion protection, the database cannot be deleted by any user.

Deletion protection is available for Amazon Aurora and RDS for MySQL, RDS for MariaDB, RDS for Oracle, RDS for PostgreSQL, and RDS for SQL Server database instances in all AWS Regions.

For more information, see [Deletion protection for Aurora clusters](../../../AmazonRDS/latest/AuroraUserGuide/USER_DeleteCluster.md#USER_DeletionProtection "../../../AmazonRDS/latest/AuroraUserGuide/USER_DeleteCluster.md#USER_DeletionProtection").

**Check ID**

`c18d2gz160`

**Source**

`AWS Config Managed Rule: rds-cluster-deletion-protection-enabled`

**Alert Criteria**

Yellow: You have Amazon RDS DB clusters that don't have deletion protection enabled.

**Recommended Action**

Turn on deletion protection when you create an Amazon RDS DB cluster.

You can only delete clusters that don't have deletion protection enabled. Enabling deletion protection adds an extra layer of protection and avoids data loss from accidental or non-accidental deletion of a database instance. Deletion protection also helps meet regulatory compliance requirements and ensure business continuity.

For more information, see [Deletion protection for Aurora clusters](../../../AmazonRDS/latest/AuroraUserGuide/USER_DeleteCluster.md#USER_DeletionProtection "../../../AmazonRDS/latest/AuroraUserGuide/USER_DeleteCluster.md#USER_DeletionProtection").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Additional Resources**

[Deletion protection for Aurora clusters](../../../AmazonRDS/latest/AuroraUserGuide/USER_DeleteCluster.md#USER_DeletionProtection "../../../AmazonRDS/latest/AuroraUserGuide/USER_DeleteCluster.md#USER_DeletionProtection")

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time

## RDS DB Instance Automatic Minor Version Upgrade Check

**Description**

Checks if Amazon RDS DB instances have automatic minor version upgrades configured.

Turn on automatic minor version upgrades for an Amazon RDS instance to make sure that the database is always running the latest secure and stable version. Minor upgrades provide security updates, bug fixes, performance improvements, and maintain compatibility with existing applications.

For more information, see [Upgrading a DB instance engine version](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades. "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades.").

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c18d2gz155`

**Source**

`AWS Config Managed Rule: rds-automatic-minor-version-upgrade-enabled`

**Alert Criteria**

Yellow: RDS DB instance does not have automatic minor version upgrades turned on.

**Recommended Action**

Turn on automatic minor version upgrades when you create a Amazon RDS DB instance.

When you turn on minor version upgrade, the database version automatically upgrades if it is running a minor version of the DB engine that is lower than the [Manually upgrading the engine version](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades").

**Report columns**

- Status
- Region
- Resource
- AWS Config Rule
- Input Parameters
- Last Updated Time
