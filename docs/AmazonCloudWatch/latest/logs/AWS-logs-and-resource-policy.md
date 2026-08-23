# Enable logging from AWS services

While many services publish logs only to CloudWatch Logs, some AWS services can publish logs
directly to Amazon Simple Storage Service or Amazon Data Firehose. If your main requirement for logs is storage or
processing in one of these services, you can easily have the service that produces the logs
send them directly to Amazon S3 or Firehose without additional setup.

Even when you publish logs directly to Amazon S3 or Firehose, CloudWatch delivery charges
apply. If you send logs to Amazon S3, then
``AWS_REGION`-S3-Egress-Bytes` charges appear in Cost
 Explorer or on your bill. If you send logs to Firehose, then
 ``AWS_REGION`-FH-Egress-Bytes` charges appear. For more
information about vended logs pricing, see the **Logs** tab at
[Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

Some AWS services use a common infrastructure to send their logs. To enable logging from
these services, you must be logged in as a user that has certain permissions. Additionally,
you must grant permissions to AWS to enable the logs to be sent.

For services that require these permissions, there are two versions of the permissions
needed. The services that require these extra permissions are noted as **Supported
(V1 permissions)** and **Supported (V2 permissions)** in the
[Supported log destinations](AWS-logs-destinations-table.md "AWS-logs-destinations-table.md"). For information about these required
permissions, see the sections after the table.

- [![Amazon API Gateway logo](images/integration-icons/api-gateway.png)Amazon API Gateway](../../../apigateway/latest/developerguide/set-up-logging.md "../../../apigateway/latest/developerguide/set-up-logging.md")
- [![Application Load Balancer logo](images/integration-icons/alb.png)Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md")
- [![AWS AppSync logo](images/integration-icons/appsync.png)AWS AppSync](../../../appsync/latest/devguide/monitoring.md "../../../appsync/latest/devguide/monitoring.md")
- [![Amazon Aurora MySQL logo](images/integration-icons/aurora.png)Amazon Aurora MySQL](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.CloudWatch.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.CloudWatch.md")
- [![Amazon Bedrock Knowledge Bases logo](images/integration-icons/bedrock.png)Amazon Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-bases-logging.md "../../../bedrock/latest/userguide/knowledge-bases-logging.md")
- [![Amazon Bedrock Agents logo](images/integration-icons/bedrock.png)Amazon Bedrock Agents](../../../bedrock/latest/userguide/model-invocation-logging.md "../../../bedrock/latest/userguide/model-invocation-logging.md")
- [![Amazon Bedrock AgentCore Runtime logo](images/integration-icons/bedrock-agentcore.png)Amazon Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md")
- [![Amazon Bedrock AgentCore Gateway logo](images/integration-icons/bedrock-agentcore.png)Amazon Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md")
- [![Amazon Bedrock AgentCore Identity logo](images/integration-icons/bedrock-agentcore.png)Amazon Bedrock AgentCore Identity](../../../bedrock-agentcore/latest/devguide/identity.md "../../../bedrock-agentcore/latest/devguide/identity.md")
- [![Amazon Bedrock AgentCore Memory logo](images/integration-icons/bedrock-agentcore.png)Amazon Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md")
- [![Amazon Bedrock AgentCore Payments logo](images/integration-icons/bedrock-agentcore.png)Amazon Bedrock AgentCore Payments](../../../bedrock-agentcore/latest/devguide/payments.md "../../../bedrock-agentcore/latest/devguide/payments.md")
- [![Amazon Bedrock AgentCore Tools logo](images/integration-icons/bedrock-agentcore.png)Amazon Bedrock AgentCore Tools](../../../bedrock-agentcore/latest/devguide/built-in-tools.md "../../../bedrock-agentcore/latest/devguide/built-in-tools.md")
- [![Amazon Chime logo](images/integration-icons/chime.png)Amazon Chime](../../../chime/latest/ag/monitoring-cloudwatch.md#cw-logs "../../../chime/latest/ag/monitoring-cloudwatch.md#cw-logs")
- [![Amazon CloudFront logo](images/integration-icons/cloudfront.png)Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md")
- [![AWS CloudHSM logo](images/integration-icons/cloudhsm.png)AWS CloudHSM](../../../cloudhsm/latest/userguide/get-hsm-audit-logs-using-cloudwatch.md "../../../cloudhsm/latest/userguide/get-hsm-audit-logs-using-cloudwatch.md")
- [![CloudWatch Evidently logo](images/integration-icons/cloudwatch.png)CloudWatch Evidently](../monitoring/CloudWatch-Evidently-datastorage.md#CloudWatch-Evidently-datastorage-logformat "../monitoring/CloudWatch-Evidently-datastorage.md#CloudWatch-Evidently-datastorage-logformat")
- [![CloudWatch Internet Monitor logo](images/integration-icons/cloudwatch.png)CloudWatch Internet Monitor](../monitoring/CloudWatch-IM-view-cw-tools.S3_athena.md "../monitoring/CloudWatch-IM-view-cw-tools.S3_athena.md")
- [![AWS CloudTrail logo](images/integration-icons/cloudtrail.png)AWS CloudTrail](../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md "../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md")
- [![AWS CodeBuild logo](images/integration-icons/codebuild.png)AWS CodeBuild](../../../codebuild/latest/userguide/getting-started-build-log-console.md "../../../codebuild/latest/userguide/getting-started-build-log-console.md")
- [![Amazon CodeWhisperer logo](images/integration-icons/codewhisperer.png)Amazon CodeWhisperer](../../../eventbridge/latest/ref/events-ref-codewhisperer.md "../../../eventbridge/latest/ref/events-ref-codewhisperer.md")
- [![Amazon Cognito logo](images/integration-icons/cognito.png)Amazon Cognito](../../../cognito/latest/developerguide/what-is-amazon-cognito.md "../../../cognito/latest/developerguide/what-is-amazon-cognito.md")
- [![Amazon Connect logo](images/integration-icons/connect.png)Amazon Connect](../../../connect/latest/adminguide/logging-and-monitoring.md "../../../connect/latest/adminguide/logging-and-monitoring.md")
- [![AWS DataSync logo](images/integration-icons/datasync.png)AWS DataSync](../../../datasync/latest/userguide/monitor-datasync.md#cloudwatchlogs "../../../datasync/latest/userguide/monitor-datasync.md#cloudwatchlogs")
- [![AWS DevOps Agent logo](images/integration-icons/devops-agent.png)AWS DevOps Agent](../../../devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-vended-logs-and-metrics.md "../../../devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-vended-logs-and-metrics.md")
- [![Amazon ElastiCache (Redis OSS) logo](images/integration-icons/elasticache.png)Amazon ElastiCache (Redis OSS)](../../../AmazonElastiCache/latest/red-ug/Log_Delivery.md "../../../AmazonElastiCache/latest/red-ug/Log_Delivery.md")
- [![AWS Elastic Beanstalk logo](images/integration-icons/elastic-beanstalk.png)AWS Elastic Beanstalk](../../../elasticbeanstalk/latest/dg/AWSHowTo.cloudwatchlogs.md "../../../elasticbeanstalk/latest/dg/AWSHowTo.cloudwatchlogs.md")
- [![Amazon ECS logo](images/integration-icons/ecs.png)Amazon ECS](../../../AmazonECS/latest/developerguide/using_cloudwatch_logs.md "../../../AmazonECS/latest/developerguide/using_cloudwatch_logs.md")
- [![Amazon EKS Auto Mode logo](images/integration-icons/eks.png)Amazon EKS Auto Mode](../../../eks/latest/userguide/auto-managed-component-logs.md "../../../eks/latest/userguide/auto-managed-component-logs.md")
- [![Amazon EKS Capability Logs logo](images/integration-icons/eks.png)Amazon EKS Capability Logs](../../../eks/latest/userguide/capabilities-controller-logs.md "../../../eks/latest/userguide/capabilities-controller-logs.md")
- [![Amazon EKS Control Plane logo](images/integration-icons/eks.png)Amazon EKS Control Plane](../../../eks/latest/userguide/control-plane-logs.md "../../../eks/latest/userguide/control-plane-logs.md")
- [![AWS Elemental MediaPackage logo](images/integration-icons/mediapackage.png)AWS Elemental MediaPackage](../../../mediapackage/latest/ug/access-logging.md "../../../mediapackage/latest/ug/access-logging.md")
- [![AWS Elemental MediaTailor logo](images/integration-icons/mediatailor.png)AWS Elemental MediaTailor](../../../mediatailor/latest/ug/monitoring-cw-logs.md "../../../mediatailor/latest/ug/monitoring-cw-logs.md")
- [![AWS Entity Resolution logo](images/integration-icons/entity-resolution.png)AWS Entity Resolution](../../../entityresolution/latest/userguide/what-is-service.md "../../../entityresolution/latest/userguide/what-is-service.md")
- [![Amazon EventBridge Pipes logo](images/integration-icons/eventbridge.png)Amazon EventBridge Pipes](../../../eventbridge/latest/userguide/eb-pipes-logs.md "../../../eventbridge/latest/userguide/eb-pipes-logs.md")
- [![Amazon EventBridge Event Buses logo](images/integration-icons/eventbridge.png)Amazon EventBridge Event Buses](../../../eventbridge/latest/userguide/eb-pipes-logs.md "../../../eventbridge/latest/userguide/eb-pipes-logs.md")
- [![AWS Fargate logo](images/integration-icons/fargate.png)AWS Fargate](../../../AmazonECS/latest/developerguide/using_awslogs.md "../../../AmazonECS/latest/developerguide/using_awslogs.md")
- [![AWS Fault Injection Service logo](images/integration-icons/fis.png)AWS Fault Injection Service](../../../fis/latest/userguide/monitoring-logging.md "../../../fis/latest/userguide/monitoring-logging.md")
- [![Amazon FinSpace logo](images/integration-icons/finspace.png)Amazon FinSpace](../../../finspace/latest/userguide/finspace-what-is.md "../../../finspace/latest/userguide/finspace-what-is.md")
- [![AWS Global Accelerator logo](images/integration-icons/global-accelerator.png)AWS Global Accelerator](../../../global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.md "../../../global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.md")
- [![AWS Glue logo](images/integration-icons/glue.png)AWS Glue](../../../glue/latest/dg/monitor-continuous-logging.md "../../../glue/latest/dg/monitor-continuous-logging.md")
- [![IAM Identity Center logo](images/integration-icons/iam-identity-center.png)IAM Identity Center](../../../singlesignon/latest/userguide/logging-ad-sync-errors.md "../../../singlesignon/latest/userguide/logging-ad-sync-errors.md")
- [![Amazon IVS Chat logo](images/integration-icons/ivs.png)Amazon IVS Chat](../../../ivs/latest/LowLatencyUserGuide/chat-logging.md "../../../ivs/latest/LowLatencyUserGuide/chat-logging.md")
- [![AWS IoT logo](images/integration-icons/iot.png)AWS IoT](../../../iot/latest/developerguide/cloud-watch-logs.md "../../../iot/latest/developerguide/cloud-watch-logs.md")
- [![AWS IoT FleetWise logo](images/integration-icons/iot-fleetwise.png)AWS IoT FleetWise](../../../iot-fleetwise/latest/developerguide/logging-cw.md "../../../iot-fleetwise/latest/developerguide/logging-cw.md")
- [![AWS Lambda logo](images/integration-icons/lambda.png)AWS Lambda](../../../lambda/latest/dg/monitoring-cloudwatchlogs.md "../../../lambda/latest/dg/monitoring-cloudwatchlogs.md")
- [![Amazon Macie logo](images/integration-icons/macie.png)Amazon Macie](../../../macie/latest/user/discovery-jobs-monitor-cw-logs.md "../../../macie/latest/user/discovery-jobs-monitor-cw-logs.md")
- [![Amazon SES logo](images/integration-icons/ses.png)Amazon SES](../../../ses/latest/dg/eb-logging.md "../../../ses/latest/dg/eb-logging.md")
- [![AWS Mainframe Modernization logo](images/integration-icons/mainframe.png)AWS Mainframe Modernization](../../../m2/latest/userguide/what-is-m2.md "../../../m2/latest/userguide/what-is-m2.md")
- [![Amazon Managed Service for Prometheus logo](images/integration-icons/prometheus.png)Amazon Managed Service for Prometheus](../../../prometheus/latest/userguide/CW-logs.md "../../../prometheus/latest/userguide/CW-logs.md")
- [![Amazon MSK logo](images/integration-icons/msk.png)Amazon MSK](../../../msk/latest/developerguide/msk-logging.md "../../../msk/latest/developerguide/msk-logging.md")
- [![Amazon MSK Connect logo](images/integration-icons/msk-connect.png)Amazon MSK Connect](../../../msk/latest/developerguide/msk-connect-logging.md "../../../msk/latest/developerguide/msk-connect-logging.md")
- [![Amazon MQ logo](images/integration-icons/mq.png)Amazon MQ](../../../amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.md "../../../amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.md")
- [![AWS Network Firewall logo](images/integration-icons/network-firewall.png)AWS Network Firewall](../../../network-firewall/latest/developerguide/firewall-logging.md "../../../network-firewall/latest/developerguide/firewall-logging.md")
- [![AWS Network Firewall Proxy logo](images/integration-icons/network-firewall.png)AWS Network Firewall Proxy](../../../network-firewall/latest/developerguide/proxy-logging-and-monitoring.md "../../../network-firewall/latest/developerguide/proxy-logging-and-monitoring.md")
- [![Network Load Balancer logo](images/integration-icons/nlb.png)Network Load Balancer](../../../elasticloadbalancing/latest/network/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/network/load-balancer-access-logs.md")
- [![Amazon OpenSearch Service logo](images/integration-icons/opensearch.png)Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md "../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md")
- [![Amazon OpenSearch Ingestion logo](images/integration-icons/opensearch-ingestion.png)Amazon OpenSearch Ingestion](../../../opensearch-service/latest/developerguide/monitoring-pipeline-logs.md "../../../opensearch-service/latest/developerguide/monitoring-pipeline-logs.md")
- [![AWS PCS logo](images/integration-icons/pcs.png)AWS PCS](../../../pcs/latest/userguide/monitoring-overview.md "../../../pcs/latest/userguide/monitoring-overview.md")
- [![Amazon Q Business Connectors logo](images/integration-icons/q-business.png)Amazon Q Business Connectors](../../../amazonq/latest/qbusiness-ug/connectors-list.md "../../../amazonq/latest/qbusiness-ug/connectors-list.md")
- [![Amazon Q Business Conversations logo](images/integration-icons/q-business.png)Amazon Q Business Conversations](../../../amazonq/latest/qbusiness-ug/cw-logs-enable-logging.md "../../../amazonq/latest/qbusiness-ug/cw-logs-enable-logging.md")
- [![Amazon Quick Chat and Feedback logo](images/integration-icons/quick-chat.png)Amazon Quick Chat and Feedback](../../../quicksuite/latest/userguide/monitoring-quicksuite-chat-feedback-cloudwatch.md "../../../quicksuite/latest/userguide/monitoring-quicksuite-chat-feedback-cloudwatch.md")
- [![Amazon RDS PostgreSQL logo](images/integration-icons/rds.png)Amazon RDS PostgreSQL](../../../AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.md#USER_LogAccess.PostgreSQL.PublishtoCloudWatchLogs "../../../AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.md#USER_LogAccess.PostgreSQL.PublishtoCloudWatchLogs")
- [![AWS RTB Fabric logo](images/integration-icons/rtb-fabric.png)AWS RTB Fabric](../../../rtb-fabric/latest/userguide/what-is-rtb-fabric.md "../../../rtb-fabric/latest/userguide/what-is-rtb-fabric.md")
- [![AWS Security Hub CSPM logo](images/integration-icons/security-hub.png)AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")
- [![AWS Security Hub logo](images/integration-icons/security-hub.png)AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub-v2.md "../../../securityhub/latest/userguide/what-is-securityhub-v2.md")
- [![Amazon Route 53 Public DNS logo](images/integration-icons/route53.png)Amazon Route 53 Public DNS](../../../Route53/latest/DeveloperGuide/logging-monitoring.md "../../../Route53/latest/DeveloperGuide/logging-monitoring.md")
- [![Amazon Route 53 Resolver logo](images/integration-icons/route53.png)Amazon Route 53 Resolver](../../../Route53/latest/DeveloperGuide/resolver-query-logs-choosing-target-resource.md "../../../Route53/latest/DeveloperGuide/resolver-query-logs-choosing-target-resource.md")
- [![Amazon S3 logo](images/integration-icons/s3.png)Amazon S3](../../../AmazonS3/latest/userguide/ServerLogs.md "../../../AmazonS3/latest/userguide/ServerLogs.md")
- [![Amazon SageMaker AI Events logo](images/integration-icons/sagemaker.png)Amazon SageMaker AI Events](../../../sagemaker/latest/dg/logging-cloudwatch.md "../../../sagemaker/latest/dg/logging-cloudwatch.md")
- [![Amazon SageMaker AI Worker Events logo](images/integration-icons/sagemaker.png)Amazon SageMaker AI Worker Events](../../../sagemaker/latest/dg/workteam-private-tracking.md "../../../sagemaker/latest/dg/workteam-private-tracking.md")
- [![AWS Site-to-Site VPN logo](images/integration-icons/site-to-site-vpn.png)AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/monitoring-logs.md "../../../vpn/latest/s2svpn/monitoring-logs.md")
- [![Amazon SES logo](images/integration-icons/ses.png)Amazon SES](../../../ses/latest/dg/eb-logging.md "../../../ses/latest/dg/eb-logging.md")
- [![Amazon SNS logo](images/integration-icons/sns.png)Amazon SNS](../../../sns/latest/dg/sms_stats_cloudwatch.md#sns-viewing-cloudwatch-logs "../../../sns/latest/dg/sms_stats_cloudwatch.md#sns-viewing-cloudwatch-logs")
- [![Amazon SNS Data Protection logo](images/integration-icons/sns.png)Amazon SNS Data Protection](../../../sns/latest/dg/sns-message-data-protection-operations.md "../../../sns/latest/dg/sns-message-data-protection-operations.md")
- [![EC2 Spot Instance logo](images/integration-icons/ec2.png)EC2 Spot Instance](../../../AWSEC2/latest/UserGuide/spot-data-feeds.md "../../../AWSEC2/latest/UserGuide/spot-data-feeds.md")
- [![AWS Step Functions logo](images/integration-icons/step-functions.png)AWS Step Functions](../../../step-functions/latest/dg/cw-logs.md "../../../step-functions/latest/dg/cw-logs.md")
- [![AWS Storage Gateway logo](images/integration-icons/storage-gateway.png)AWS Storage Gateway](../../../storagegateway/latest/userguide/monitoring-file-gateway.md "../../../storagegateway/latest/userguide/monitoring-file-gateway.md")
- [![AWS Transfer Family logo](images/integration-icons/transfer-family.png)AWS Transfer Family](../../../transfer/latest/userguide/structured-logging.md "../../../transfer/latest/userguide/structured-logging.md")
- [![AWS Verified Access logo](images/integration-icons/verified-access.png)AWS Verified Access](../../../verified-access/latest/ug/access-logs.md "../../../verified-access/latest/ug/access-logs.md")
- [![Amazon VPC Flow Logs logo](images/integration-icons/vpc.png)Amazon VPC Flow Logs](../../../vpc/latest/userguide/flow-logs-s3.md "../../../vpc/latest/userguide/flow-logs-s3.md")
- [![Amazon VPC Lattice logo](images/integration-icons/vpc-lattice.png)Amazon VPC Lattice](../../../vpc-lattice/latest/ug/monitoring-access-logs.md "../../../vpc-lattice/latest/ug/monitoring-access-logs.md")
- [![Amazon VPC Route Server logo](images/integration-icons/vpc-route-server.png)Amazon VPC Route Server](../../../vpc/latest/userguide/dynamic-routing-route-server.md "../../../vpc/latest/userguide/dynamic-routing-route-server.md")
- [![AWS WAF logo](images/integration-icons/waf.png)AWS WAF](../../../waf/latest/developerguide/logging-destinations.md "../../../waf/latest/developerguide/logging-destinations.md")
- [![Amazon WorkMail logo](images/integration-icons/workmail.png)Amazon WorkMail](../../../workmail/latest/adminguide/monitoring-audit-logging.md "../../../workmail/latest/adminguide/monitoring-audit-logging.md")
