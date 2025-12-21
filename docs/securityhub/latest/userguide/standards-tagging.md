# AWS Resource Tagging standard in Security Hub CSPM

The AWS Resource Tagging standard, developed by AWS Security Hub CSPM, helps you determine whether
your AWS resources are missing tags. _Tags_ are
key‐value pairs that act as metadata for organizing AWS resources. With most AWS
resources, you have the option of adding tags to a resource when you create the resource or
after you create the resource. Examples of resources include Amazon CloudFront distributions,
Amazon Elastic Compute Cloud (Amazon EC2) instances, and secrets in AWS Secrets Manager. Tags can help you manage, identify,
organize, search for, and filter AWS resources.

Each tag has two parts:

- A tag key—for example, `CostCenter`, `Environment`,
  or `Project`. Tag keys are case sensitive.
- A tag value—for example, `111122223333` or
  `Production`. Like tag keys, tag values are case sensitive.
  You can use tags to categorize resources by purpose, owner, environment, or other
  criteria. For information about adding tags to AWS resources, see the [Tagging AWS
  Resources and Tag Editor User Guide](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

For each control that applies to the AWS Resource Tagging standard in Security Hub CSPM, you can
optionally use the supported parameter to specify tag keys that you want the control to
check for. If you don't specify any tag keys, the control checks only for the existence of
at least one tag key, and fails if a resource doesn't have any tag keys.

Before you enable the AWS Resource Tagging standard, it's important to enable and
configure resource recording in AWS Config. When you configure resource recording, also be sure to
enable it for all the types of AWS resources that are checked by controls that apply to
the standard. Otherwise, Security Hub CSPM might not be able to evaluate the appropriate resources, and
generate accurate findings for controls that apply to the standard. For more information,
including a list of the types of resources to record, see [Required AWS Config resources for control findings](controls-config-resources.md "controls-config-resources.md").

After you enable the AWS Resource Tagging standard, you begin receiving findings for
controls that apply to the standard. Note that it can take up to 18 hours for Security Hub CSPM to
generate findings for controls that use the same AWS Config service-linked rule as controls that
apply to other enabled standards. For more information, see [Schedule for running security checks](securityhub-standards-schedule.md "securityhub-standards-schedule.md").

The AWS Resource Tagging standard has the following Amazon Resource Name (ARN):
`arn:aws:securityhub:`region`::standards/aws-resource-tagging-standard/v/1.0.0`,
where `region` is the Region code for the applicable AWS Region.
You can also use the [GetEnabledStandards](../../1.0/APIReference/API_GetEnabledStandards.md "../../1.0/APIReference/API_GetEnabledStandards.md") operation of the Security Hub CSPM API to retrieve the ARN of a
standard that's currently enabled.

###### Note

The AWS Resource Tagging standard isn't
available in the Asia Pacific (New Zealand) and Asia Pacific (Taipei) Regions.

## Controls that apply to the standard

The following list specifies which AWS Security Hub CSPM controls apply to the
AWS Resource Tagging standard (v1.0.0). To review the details of a control, choose the
control.

- [[ACM.3] ACM certificates should be tagged](acm-controls.md#acm-3 "acm-controls.md#acm-3")
- [[Amplify.1] Amplify apps should be tagged](amplify-controls.md#amplify-1 "amplify-controls.md#amplify-1")
- [[Amplify.2] Amplify branches should be tagged](amplify-controls.md#amplify-2 "amplify-controls.md#amplify-2")
- [[AppConfig.1] AWS AppConfig applications should be tagged](appconfig-controls.md#appconfig-1 "appconfig-controls.md#appconfig-1")
- [[AppConfig.2] AWS AppConfig configuration profiles should be tagged](appconfig-controls.md#appconfig-2 "appconfig-controls.md#appconfig-2")
- [[AppConfig.3] AWS AppConfig environments should be tagged](appconfig-controls.md#appconfig-3 "appconfig-controls.md#appconfig-3")
- [[AppConfig.4] AWS AppConfig extension associations should be tagged](appconfig-controls.md#appconfig-4 "appconfig-controls.md#appconfig-4")
- [[AppFlow.1] Amazon AppFlow flows should be tagged](appflow-controls.md#appflow-1 "appflow-controls.md#appflow-1")
- [[AppRunner.1] App Runner services should be tagged](apprunner-controls.md#apprunner-1 "apprunner-controls.md#apprunner-1")
- [[AppRunner.2] App Runner VPC connectors should be tagged](apprunner-controls.md#apprunner-2 "apprunner-controls.md#apprunner-2")
- [[AppSync.4] AWS AppSync GraphQL APIs should be tagged](appsync-controls.md#appsync-4 "appsync-controls.md#appsync-4")
- [[Athena.2] Athena data catalogs should be tagged](athena-controls.md#athena-2 "athena-controls.md#athena-2")
- [[Athena.3] Athena workgroups should be tagged](athena-controls.md#athena-3 "athena-controls.md#athena-3")
- [[AutoScaling.10] EC2 Auto Scaling groups should be tagged](autoscaling-controls.md#autoscaling-10 "autoscaling-controls.md#autoscaling-10")
- [[Backup.2] AWS Backup recovery points should be tagged](backup-controls.md#backup-2 "backup-controls.md#backup-2")
- [[Backup.3] AWS Backup vaults should be tagged](backup-controls.md#backup-3 "backup-controls.md#backup-3")
- [[Backup.4] AWS Backup report plans should be tagged](backup-controls.md#backup-4 "backup-controls.md#backup-4")
- [[Backup.5] AWS Backup backup plans should be tagged](backup-controls.md#backup-5 "backup-controls.md#backup-5")
- [[Batch.1] Batch job queues should be tagged](batch-controls.md#batch-1 "batch-controls.md#batch-1")
- [[Batch.2] Batch scheduling policies should be tagged](batch-controls.md#batch-2 "batch-controls.md#batch-2")
- [[Batch.3] Batch compute environments should be tagged](batch-controls.md#batch-3 "batch-controls.md#batch-3")
- [[Batch.4] Compute resources properties in managed Batch compute environments should be tagged](batch-controls.md#batch-4 "batch-controls.md#batch-4")
- [[CloudFormation.2] CloudFormation stacks should be tagged](cloudformation-controls.md#cloudformation-2 "cloudformation-controls.md#cloudformation-2")
- [[CloudFront.14] CloudFront distributions should be
  tagged](cloudfront-controls.md#cloudfront-14 "cloudfront-controls.md#cloudfront-14")
- [[CloudTrail.9] CloudTrail trails should be tagged](cloudtrail-controls.md#cloudtrail-9 "cloudtrail-controls.md#cloudtrail-9")
- [[CodeArtifact.1]CodeArtifact repositories should be tagged](codeartifact-controls.md#codeartifact-1 "codeartifact-controls.md#codeartifact-1")
- [[CodeGuruProfiler.1] CodeGuru Profiler profiling groups should be
  tagged](codeguruprofiler-controls.md#codeguruprofiler-1 "codeguruprofiler-controls.md#codeguruprofiler-1")
- [[CodeGuruReviewer.1] CodeGuru Reviewer repository associations should be
  tagged](codegurureviewer-controls.md#codegurureviewer-1 "codegurureviewer-controls.md#codegurureviewer-1")
- [[Connect.1] Amazon Connect Customer Profiles object types
  should be tagged](connect-controls.md#connect-1 "connect-controls.md#connect-1")
- [[DataSync.2] DataSync tasks should be tagged](datasync-controls.md#datasync-2 "datasync-controls.md#datasync-2")
- [[Detective.1] Detective behavior graphs should be tagged](detective-controls.md#detective-1 "detective-controls.md#detective-1")
- [[DMS.2] DMS certificates should be tagged](dms-controls.md#dms-2 "dms-controls.md#dms-2")
- [[DMS.3] DMS event subscriptions should be tagged](dms-controls.md#dms-3 "dms-controls.md#dms-3")
- [[DMS.4] DMS replication instances should be tagged](dms-controls.md#dms-4 "dms-controls.md#dms-4")
- [[DMS.5] DMS replication subnet groups should be tagged](dms-controls.md#dms-5 "dms-controls.md#dms-5")
- [[DynamoDB.5] DynamoDB tables should be tagged](dynamodb-controls.md#dynamodb-5 "dynamodb-controls.md#dynamodb-5")
- [[EC2.33] EC2 transit gateway attachments should
  be tagged](ec2-controls.md#ec2-33 "ec2-controls.md#ec2-33")
- [[EC2.34] EC2 transit gateway route tables should
  be tagged](ec2-controls.md#ec2-34 "ec2-controls.md#ec2-34")
- [[EC2.35] EC2 network interfaces should be
  tagged](ec2-controls.md#ec2-35 "ec2-controls.md#ec2-35")
- [[EC2.36] EC2 customer gateways should be
  tagged](ec2-controls.md#ec2-36 "ec2-controls.md#ec2-36")
- [[EC2.37] EC2 Elastic IP addresses should be
  tagged](ec2-controls.md#ec2-37 "ec2-controls.md#ec2-37")
- [[EC2.38] EC2 instances should be tagged](ec2-controls.md#ec2-38 "ec2-controls.md#ec2-38")
- [[EC2.39] EC2 internet gateways should be
  tagged](ec2-controls.md#ec2-39 "ec2-controls.md#ec2-39")
- [[EC2.40] EC2 NAT gateways should be
  tagged](ec2-controls.md#ec2-40 "ec2-controls.md#ec2-40")
- [[EC2.41] EC2 network ACLs should be
  tagged](ec2-controls.md#ec2-41 "ec2-controls.md#ec2-41")
- [[EC2.42] EC2 route tables should be
  tagged](ec2-controls.md#ec2-42 "ec2-controls.md#ec2-42")
- [[EC2.43] EC2 security groups should be
  tagged](ec2-controls.md#ec2-43 "ec2-controls.md#ec2-43")
- [[EC2.44] EC2 subnets should be tagged](ec2-controls.md#ec2-44 "ec2-controls.md#ec2-44")
- [[EC2.45] EC2 volumes should be tagged](ec2-controls.md#ec2-45 "ec2-controls.md#ec2-45")
- [[EC2.46] Amazon VPCs should be tagged](ec2-controls.md#ec2-46 "ec2-controls.md#ec2-46")
- [[EC2.47] Amazon VPC endpoint services should be
  tagged](ec2-controls.md#ec2-47 "ec2-controls.md#ec2-47")
- [[EC2.48] Amazon VPC flow logs should be tagged](ec2-controls.md#ec2-48 "ec2-controls.md#ec2-48")
- [[EC2.49] Amazon VPC peering connections should be
  tagged](ec2-controls.md#ec2-49 "ec2-controls.md#ec2-49")
- [[EC2.50] EC2 VPN gateways should be
  tagged](ec2-controls.md#ec2-50 "ec2-controls.md#ec2-50")
- [[EC2.52] EC2 transit gateways should be
  tagged](ec2-controls.md#ec2-52 "ec2-controls.md#ec2-52")
- [[EC2.174] EC2 DHCP option sets should be tagged](ec2-controls.md#ec2-174 "ec2-controls.md#ec2-174")
- [[EC2.175] EC2 launch templates should be tagged](ec2-controls.md#ec2-175 "ec2-controls.md#ec2-175")
- [[EC2.176] EC2 prefix lists should be tagged](ec2-controls.md#ec2-176 "ec2-controls.md#ec2-176")
- [[EC2.177] EC2 traffic mirror sessions should be
  tagged](ec2-controls.md#ec2-177 "ec2-controls.md#ec2-177")
- [[EC2.178] EC2 traffic mirror filters should be
  tagged](ec2-controls.md#ec2-178 "ec2-controls.md#ec2-178")
- [[EC2.179] EC2 traffic mirror targets should be
  tagged](ec2-controls.md#ec2-179 "ec2-controls.md#ec2-179")
- [[ECR.4] ECR public repositories should be tagged](ecr-controls.md#ecr-4 "ecr-controls.md#ecr-4")
- [[ECS.13] ECS services should be tagged](ecs-controls.md#ecs-13 "ecs-controls.md#ecs-13")
- [[ECS.14] ECS clusters should be tagged](ecs-controls.md#ecs-14 "ecs-controls.md#ecs-14")
- [[ECS.15] ECS task definitions should be tagged](ecs-controls.md#ecs-15 "ecs-controls.md#ecs-15")
- [[EFS.5] EFS access points should be tagged](efs-controls.md#efs-5 "efs-controls.md#efs-5")
- [[EKS.6] EKS clusters should be tagged](eks-controls.md#eks-6 "eks-controls.md#eks-6")
- [[EKS.7] EKS identity provider configurations should be tagged](eks-controls.md#eks-7 "eks-controls.md#eks-7")
- [[ES.9] Elasticsearch domains should be tagged](es-controls.md#es-9 "es-controls.md#es-9")
- [[EventBridge.2] EventBridge event buses should be tagged](eventbridge-controls.md#eventbridge-2 "eventbridge-controls.md#eventbridge-2")
- [[FraudDetector.1] Amazon Fraud Detector entity types should be tagged](frauddetector-controls.md#frauddetector-1 "frauddetector-controls.md#frauddetector-1")
- [[FraudDetector.2] Amazon Fraud Detector labels should be tagged](frauddetector-controls.md#frauddetector-2 "frauddetector-controls.md#frauddetector-2")
- [[FraudDetector.3] Amazon Fraud Detector outcomes should be tagged](frauddetector-controls.md#frauddetector-3 "frauddetector-controls.md#frauddetector-3")
- [[FraudDetector.4] Amazon Fraud Detector variables should be tagged](frauddetector-controls.md#frauddetector-4 "frauddetector-controls.md#frauddetector-4")
- [[GlobalAccelerator.1] Global Accelerator accelerators should be tagged](globalaccelerator-controls.md#globalaccelerator-1 "globalaccelerator-controls.md#globalaccelerator-1")
- [[Glue.1] AWS Glue jobs should be tagged](glue-controls.md#glue-1 "glue-controls.md#glue-1")
- [[GuardDuty.2] GuardDuty filters should be tagged](guardduty-controls.md#guardduty-2 "guardduty-controls.md#guardduty-2")
- [[GuardDuty.3] GuardDuty IPSets should be tagged](guardduty-controls.md#guardduty-3 "guardduty-controls.md#guardduty-3")
- [[GuardDuty.4] GuardDuty detectors should be tagged](guardduty-controls.md#guardduty-4 "guardduty-controls.md#guardduty-4")
- [[IAM.23] IAM Access Analyzer analyzers should be tagged](iam-controls.md#iam-23 "iam-controls.md#iam-23")
- [[IAM.24] IAM roles should be tagged](iam-controls.md#iam-24 "iam-controls.md#iam-24")
- [[IAM.25] IAM users should be tagged](iam-controls.md#iam-25 "iam-controls.md#iam-25")
- [[IoT.1] AWS IoT Device Defender security profiles should be tagged](iot-controls.md#iot-1 "iot-controls.md#iot-1")
- [[IoT.2] AWS IoT Core mitigation actions should be tagged](iot-controls.md#iot-2 "iot-controls.md#iot-2")
- [[IoT.3] AWS IoT Core dimensions should be tagged](iot-controls.md#iot-3 "iot-controls.md#iot-3")
- [[IoT.4] AWS IoT Core authorizers should be tagged](iot-controls.md#iot-4 "iot-controls.md#iot-4")
- [[IoT.5] AWS IoT Core role aliases should be tagged](iot-controls.md#iot-5 "iot-controls.md#iot-5")
- [[IoT.6] AWS IoT Core policies should be tagged](iot-controls.md#iot-6 "iot-controls.md#iot-6")
- [[IoTEvents.1] AWS IoT Events inputs should be tagged](iotevents-controls.md#iotevents-1 "iotevents-controls.md#iotevents-1")
- [[IoTEvents.2] AWS IoT Events detector models should be tagged](iotevents-controls.md#iotevents-2 "iotevents-controls.md#iotevents-2")
- [[IoTEvents.3] AWS IoT Events alarm models should be tagged](iotevents-controls.md#iotevents-3 "iotevents-controls.md#iotevents-3")
- [[IoTSiteWise.1] AWS IoT SiteWise asset models should be tagged](iotsitewise-controls.md#iotsitewise-1 "iotsitewise-controls.md#iotsitewise-1")
- [[IoTSiteWise.2] AWS IoT SiteWise dashboards should be tagged](iotsitewise-controls.md#iotsitewise-2 "iotsitewise-controls.md#iotsitewise-2")
- [[IoTSiteWise.3] AWS IoT SiteWise gateways should be tagged](iotsitewise-controls.md#iotsitewise-3 "iotsitewise-controls.md#iotsitewise-3")
- [[IoTSiteWise.4] AWS IoT SiteWise portals should be tagged](iotsitewise-controls.md#iotsitewise-4 "iotsitewise-controls.md#iotsitewise-4")
- [[IoTSiteWise.5] AWS IoT SiteWise projects should be tagged](iotsitewise-controls.md#iotsitewise-5 "iotsitewise-controls.md#iotsitewise-5")
- [[IoTTwinMaker.1] AWS IoT TwinMaker sync jobs should be tagged](iottwinmaker-controls.md#iottwinmaker-1 "iottwinmaker-controls.md#iottwinmaker-1")
- [[IoTTwinMaker.2] AWS IoT TwinMaker workspaces should be tagged](iottwinmaker-controls.md#iottwinmaker-2 "iottwinmaker-controls.md#iottwinmaker-2")
- [[IoTTwinMaker.3] AWS IoT TwinMaker scenes should be tagged](iottwinmaker-controls.md#iottwinmaker-3 "iottwinmaker-controls.md#iottwinmaker-3")
- [[IoTTwinMaker.4] AWS IoT TwinMaker entities should be tagged](iottwinmaker-controls.md#iottwinmaker-4 "iottwinmaker-controls.md#iottwinmaker-4")
- [[IoTWireless.1] AWS IoT Wireless multicast groups should be tagged](iotwireless-controls.md#iotwireless-1 "iotwireless-controls.md#iotwireless-1")
- [[IoTWireless.2] AWS IoT Wireless service profiles should be tagged](iotwireless-controls.md#iotwireless-2 "iotwireless-controls.md#iotwireless-2")
- [[IoTWireless.3] AWS IoT FUOTA tasks should be tagged](iotwireless-controls.md#iotwireless-3 "iotwireless-controls.md#iotwireless-3")
- [[IVS.1] IVS playback key pairs should be tagged](ivs-controls.md#ivs-1 "ivs-controls.md#ivs-1")
- [[IVS.2] IVS recording configurations should be tagged](ivs-controls.md#ivs-2 "ivs-controls.md#ivs-2")
- [[IVS.3] IVS channels should be tagged](ivs-controls.md#ivs-3 "ivs-controls.md#ivs-3")
- [[Keyspaces.1] Amazon Keyspaces keyspaces should be tagged](keyspaces-controls.md#keyspaces-1 "keyspaces-controls.md#keyspaces-1")
- [[Kinesis.2] Kinesis streams should be tagged](kinesis-controls.md#kinesis-2 "kinesis-controls.md#kinesis-2")
- [[Lambda.6] Lambda functions should be tagged](lambda-controls.md#lambda-6 "lambda-controls.md#lambda-6")
- [[MQ.4] Amazon MQ brokers should be tagged](mq-controls.md#mq-4 "mq-controls.md#mq-4")
- [[NetworkFirewall.7] Network Firewall firewalls should be tagged](networkfirewall-controls.md#networkfirewall-7 "networkfirewall-controls.md#networkfirewall-7")
- [[NetworkFirewall.8] Network Firewall firewall policies should be tagged](networkfirewall-controls.md#networkfirewall-8 "networkfirewall-controls.md#networkfirewall-8")
- [[Opensearch.9] OpenSearch domains should be tagged](opensearch-controls.md#opensearch-9 "opensearch-controls.md#opensearch-9")
- [[PCA.2] AWS Private CA certificate authorities should be tagged](pca-controls.md#pca-2 "pca-controls.md#pca-2")
- [[RDS.28] RDS DB clusters should be tagged](rds-controls.md#rds-28 "rds-controls.md#rds-28")
- [[RDS.29] RDS DB cluster snapshots should be tagged](rds-controls.md#rds-29 "rds-controls.md#rds-29")
- [[RDS.30] RDS DB instances should be tagged](rds-controls.md#rds-30 "rds-controls.md#rds-30")
- [[RDS.31] RDS DB security groups should be tagged](rds-controls.md#rds-31 "rds-controls.md#rds-31")
- [[RDS.32] RDS DB snapshots should be tagged](rds-controls.md#rds-32 "rds-controls.md#rds-32")
- [[RDS.33] RDS DB subnet groups should be tagged](rds-controls.md#rds-33 "rds-controls.md#rds-33")
- [[Redshift.11] Redshift clusters should be tagged](redshift-controls.md#redshift-11 "redshift-controls.md#redshift-11")
- [[Redshift.12] Redshift event notification subscriptions should be tagged](redshift-controls.md#redshift-12 "redshift-controls.md#redshift-12")
- [[Redshift.13] Redshift cluster snapshots should be tagged](redshift-controls.md#redshift-13 "redshift-controls.md#redshift-13")
- [[Redshift.14] Redshift cluster subnet groups should be tagged](redshift-controls.md#redshift-14 "redshift-controls.md#redshift-14")
- [[Redshift.17] Redshift cluster parameter groups should be
  tagged](redshift-controls.md#redshift-17 "redshift-controls.md#redshift-17")
- [[Route53.1] Route 53 health checks should be tagged](route53-controls.md#route53-1 "route53-controls.md#route53-1")
- [[SageMaker.6] SageMaker app image configurations should be
  tagged](sagemaker-controls.md#sagemaker-6 "sagemaker-controls.md#sagemaker-6")
- [[SageMaker.7] SageMaker images should be tagged](sagemaker-controls.md#sagemaker-7 "sagemaker-controls.md#sagemaker-7")
- [[SecretsManager.5] Secrets Manager secrets should be tagged](secretsmanager-controls.md#secretsmanager-5 "secretsmanager-controls.md#secretsmanager-5")
- [[SES.1] SES contact lists should be tagged](ses-controls.md#ses-1 "ses-controls.md#ses-1")
- [[SES.2] SES configuration sets should be tagged](ses-controls.md#ses-2 "ses-controls.md#ses-2")
- [[SNS.3] SNS topics should be tagged](sns-controls.md#sns-3 "sns-controls.md#sns-3")
- [[SQS.2] SQS queues should be tagged](sqs-controls.md#sqs-2 "sqs-controls.md#sqs-2")
- [[SSM.5] SSM documents should be tagged](ssm-controls.md#ssm-5 "ssm-controls.md#ssm-5")
- [[StepFunctions.2] Step Functions activities should be tagged](stepfunctions-controls.md#stepfunctions-2 "stepfunctions-controls.md#stepfunctions-2")
- [[Transfer.1] AWS Transfer Family workflows should be tagged](transfer-controls.md#transfer-1 "transfer-controls.md#transfer-1")
- [[Transfer.4] Transfer Family agreements should be tagged](transfer-controls.md#transfer-4 "transfer-controls.md#transfer-4")
- [[Transfer.5] Transfer Family certificates should be tagged](transfer-controls.md#transfer-5 "transfer-controls.md#transfer-5")
- [[Transfer.6] Transfer Family connectors should be tagged](transfer-controls.md#transfer-6 "transfer-controls.md#transfer-6")
- [[Transfer.7] Transfer Family profiles should be tagged](transfer-controls.md#transfer-7 "transfer-controls.md#transfer-7")
