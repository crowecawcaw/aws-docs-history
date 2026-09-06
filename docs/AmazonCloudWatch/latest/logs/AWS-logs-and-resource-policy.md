

# Enable logging from AWS services
<a name="AWS-logs-and-resource-policy"></a>

While many services publish logs only to CloudWatch Logs, some AWS services can publish logs directly to Amazon Simple Storage Service or Amazon Data Firehose. If your main requirement for logs is storage or processing in one of these services, you can easily have the service that produces the logs send them directly to Amazon S3 or Firehose without additional setup.

Even when you publish logs directly to Amazon S3 or Firehose, CloudWatch delivery charges apply. If you send logs to Amazon S3, then `{{AWS_REGION}}-S3-Egress-Bytes` charges appear in Cost Explorer or on your bill. If you send logs to Firehose, then `{{AWS_REGION}}-FH-Egress-Bytes` charges appear. For more information about vended logs pricing, see the **Logs** tab at [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

Some AWS services use a common infrastructure to send their logs. To enable logging from these services, you must be logged in as a user that has certain permissions. Additionally, you must grant permissions to AWS to enable the logs to be sent.

For services that require these permissions, there are two versions of the permissions needed. The services that require these extra permissions are noted as **Supported (V1 permissions)** and **Supported (V2 permissions)** in the [Supported log destinations](AWS-logs-destinations-table.md). For information about these required permissions, see the sections after the table.
| Service | Guide |
| --- | --- |
| Amazon API Gateway | [Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html) |
| Application Load Balancer | [Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) |
| AWS AppSync | [Guide](https://docs.aws.amazon.com/appsync/latest/devguide/monitoring.html) |
| Amazon Aurora MySQL | [Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.CloudWatch.html) |
| Amazon Bedrock Knowledge Bases | [Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html) |
| Amazon Bedrock Agents | [Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) |
| Amazon Bedrock AgentCore Runtime | [Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) |
| Amazon Bedrock AgentCore Gateway | [Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) |
| Amazon Bedrock AgentCore Identity | [Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) |
| Amazon Bedrock AgentCore Memory | [Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) |
| Amazon Bedrock AgentCore Payments | [Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments.html) |
| Amazon Bedrock AgentCore Tools | [Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-tools.html) |
| Amazon Chime | [Guide](https://docs.aws.amazon.com/chime/latest/ag/monitoring-cloudwatch.html#cw-logs) |
| Amazon CloudFront | [Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) |
| AWS CloudHSM | [Guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-hsm-audit-logs-using-cloudwatch.html) |
| CloudWatch Evidently | [Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-datastorage.html#CloudWatch-Evidently-datastorage-logformat) |
| CloudWatch Internet Monitor | [Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools.S3_athena.html) |
| AWS CloudTrail | [Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html) |
| AWS CodeBuild | [Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/getting-started-build-log-console.html) |
| Amazon CodeWhisperer | [Guide](https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-codewhisperer.html) |
| Amazon Cognito | [Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) |
| Amazon Connect | [Guide](https://docs.aws.amazon.com/connect/latest/adminguide/logging-and-monitoring.html) |
| AWS DataSync | [Guide](https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#cloudwatchlogs) |
| AWS DevOps Agent | [Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-vended-logs-and-metrics.html) |
| Amazon ElastiCache (Redis OSS) | [Guide](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Log_Delivery.html) |
| AWS Elastic Beanstalk | [Guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudwatchlogs.html) |
| Amazon ECS | [Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_cloudwatch_logs.html) |
| Amazon EKS Auto Mode | [Guide](https://docs.aws.amazon.com/eks/latest/userguide/auto-managed-component-logs.html) |
| Amazon EKS Capability Logs | [Guide](https://docs.aws.amazon.com/eks/latest/userguide/capabilities-controller-logs.html) |
| Amazon EKS Control Plane | [Guide](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) |
| AWS Elemental MediaPackage | [Guide](https://docs.aws.amazon.com/mediapackage/latest/ug/access-logging.html) |
| AWS Elemental MediaTailor | [Guide](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-cw-logs.html) |
| AWS Entity Resolution | [Guide](https://docs.aws.amazon.com/entityresolution/latest/userguide/what-is-service.html) |
| Amazon EventBridge Pipes | [Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html) |
| Amazon EventBridge Event Buses | [Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html) |
| AWS Fargate | [Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html) |
| AWS Fault Injection Service | [Guide](https://docs.aws.amazon.com/fis/latest/userguide/monitoring-logging.html) |
| Amazon FinSpace | [Guide](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html) |
| AWS Global Accelerator | [Guide](https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html) |
| AWS Glue | [Guide](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging.html) |
| IAM Identity Center | [Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/logging-ad-sync-errors.html) |
| Amazon IVS Chat | [Guide](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/chat-logging.html) |
| AWS IoT | [Guide](https://docs.aws.amazon.com/iot/latest/developerguide/cloud-watch-logs.html) |
| AWS IoT FleetWise | [Guide](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/logging-cw.html) |
| AWS Lambda | [Guide](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html) |
| Amazon Macie | [Guide](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-monitor-cw-logs.html) |
| Amazon SES | [Guide](https://docs.aws.amazon.com/ses/latest/dg/eb-logging.html) |
| AWS Mainframe Modernization | [Guide](https://docs.aws.amazon.com/m2/latest/userguide/what-is-m2.html) |
| Amazon Managed Service for Prometheus | [Guide](https://docs.aws.amazon.com/prometheus/latest/userguide/CW-logs.html) |
| Amazon MSK | [Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-logging.html) |
| Amazon MSK Connect | [Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-logging.html) |
| Amazon MQ | [Guide](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.html) |
| AWS Network Firewall | [Guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging.html) |
| AWS Network Firewall Proxy | [Guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/proxy-logging-and-monitoring.html) |
| Network Load Balancer | [Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html) |
| Amazon OpenSearch Service | [Guide](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html) |
| Amazon OpenSearch Ingestion | [Guide](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-pipeline-logs.html) |
| AWS PCS | [Guide](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring-overview.html) |
| Amazon Q Business Connectors | [Guide](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connectors-list.html) |
| Amazon Q Business Conversations | [Guide](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cw-logs-enable-logging.html) |
| Amazon Quick Chat and Feedback | [Guide](https://docs.aws.amazon.com/quicksuite/latest/userguide/monitoring-quicksuite-chat-feedback-cloudwatch.html) |
| Amazon RDS PostgreSQL | [Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.html#USER_LogAccess.PostgreSQL.PublishtoCloudWatchLogs) |
| AWS RTB Fabric | [Guide](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/what-is-rtb-fabric.html) |
| AWS Security Hub CSPM | [Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) |
| AWS Security Hub | [Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) |
| Amazon Route 53 Public DNS | [Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/logging-monitoring.html) |
| Amazon Route 53 Resolver | [Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs-choosing-target-resource.html) |
| Amazon S3 | [Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) |
| Amazon SageMaker AI Events | [Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html) |
| Amazon SageMaker AI Worker Events | [Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/workteam-private-tracking.html) |
| AWS Site-to-Site VPN | [Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-logs.html) |
| Amazon SES | [Guide](https://docs.aws.amazon.com/ses/latest/dg/eb-logging.html) |
| Amazon SNS | [Guide](https://docs.aws.amazon.com/sns/latest/dg/sms_stats_cloudwatch.html#sns-viewing-cloudwatch-logs) |
| Amazon SNS Data Protection | [Guide](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-operations.html) |
| EC2 Spot Instance | [Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html) |
| AWS Step Functions | [Guide](https://docs.aws.amazon.com/step-functions/latest/dg/cw-logs.html) |
| AWS Storage Gateway | [Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html) |
| AWS Transfer Family | [Guide](https://docs.aws.amazon.com/transfer/latest/userguide/structured-logging.html) |
| AWS Verified Access | [Guide](https://docs.aws.amazon.com/verified-access/latest/ug/access-logs.html) |
| Amazon VPC Flow Logs | [Guide](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3.html) |
| Amazon VPC Lattice | [Guide](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html) |
| Amazon VPC Route Server | [Guide](https://docs.aws.amazon.com/vpc/latest/userguide/dynamic-routing-route-server.html) |
| AWS WAF | [Guide](https://docs.aws.amazon.com/waf/latest/developerguide/logging-destinations.html) |
| Amazon WorkMail | [Guide](https://docs.aws.amazon.com/workmail/latest/adminguide/monitoring-audit-logging.html) |

