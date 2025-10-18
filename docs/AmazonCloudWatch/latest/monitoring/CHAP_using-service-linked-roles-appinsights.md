# Using service-linked roles for
 CloudWatch Application Insights

CloudWatch Application Insights uses AWS Identity and Access Management (IAM)[service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
 linked directly to CloudWatch Application Insights. Service-linked roles are predefined by CloudWatch Application Insights and
 include all of the permissions that the service requires to call other AWS services on your
 behalf. 

A service-linked role makes setting up CloudWatch Application Insights easier because you don’t have to
 manually add the necessary permissions. CloudWatch Application Insights defines the permissions of its
 service-linked roles, and unless defined otherwise, only CloudWatch Application Insights can assume its roles. The
 defined permissions include the trust policy and the permissions policy, and that permissions
 policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS Services That Work
 with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html") and look for the services that have **Yes** in
 the **Service-Linked Role** column. Choose a **Yes** link to view the service-linked role documentation for that service.


## Service-linked role permissions for
 CloudWatch Application Insights


CloudWatch Application Insights uses the service-linked role named **AWSServiceRoleForApplicationInsights**.
 Application Insights uses this role to perform operations such as analyzing the resource groups of the customer, creating CloudFormation stacks to create alarms on metrics, and configuring the CloudWatch Agent on EC2 instances. This service-linked role has an IAM policy attached to it named
 `CloudwatchApplicationInsightsServiceLinkedRolePolicy`. For updates to this
 policy, see [Application Insights updates to AWS
 managed policies](security-iam-awsmanpol-appinsights.md#security-iam-awsmanpol-appinsights-updates "security-iam-awsmanpol-appinsights.md#security-iam-awsmanpol-appinsights-updates").


The role permissions policy allows CloudWatch Application Insights to complete the following actions on
 resources.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "CloudWatch",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:DescribeAlarmHistory",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:GetMetricData",
 "cloudwatch:ListMetrics",
 "cloudwatch:PutMetricAlarm",
 "cloudwatch:DeleteAlarms",
 "cloudwatch:PutAnomalyDetector",
 "cloudwatch:DeleteAnomalyDetector",
 "cloudwatch:DescribeAnomalyDetectors"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "CloudWatchLogs",
 "Effect": "Allow",
 "Action": [
 "logs:FilterLogEvents",
 "logs:GetLogEvents",
 "logs:DescribeLogStreams",
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "EventBridge",
 "Effect": "Allow",
 "Action": [
 "events:DescribeRule"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "CloudFormation",
 "Effect": "Allow",
 "Action": [
 "cloudFormation:CreateStack",
 "cloudFormation:UpdateStack",
 "cloudFormation:DeleteStack",
 "cloudFormation:DescribeStackResources",
 "cloudFormation:UpdateTerminationProtection"
 ],
 "Resource": [
 "arn:aws:cloudformation:*:*:stack/ApplicationInsights-*"
 ]
 },
 {
 "Sid": "CloudFormationStacks",
 "Effect": "Allow",
 "Action": [
 "cloudFormation:DescribeStacks",
 "cloudFormation:ListStackResources",
 "cloudFormation:ListStacks"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "Tag",
 "Effect": "Allow",
 "Action": [
 "tag:GetResources"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ResourceGroups",
 "Effect": "Allow",
 "Action": [
 "resource-groups:ListGroupResources",
 "resource-groups:GetGroupQuery",
 "resource-groups:GetGroup"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ApplicationInsightsResourceGroup",
 "Effect": "Allow",
 "Action": [
 "resource-groups:CreateGroup",
 "resource-groups:DeleteGroup"
 ],
 "Resource": [
 "arn:aws:resource-groups:*:*:group/ApplicationInsights-*"
 ]
 },
 {
 "Sid": "ElasticLoadBalancing",
 "Effect": "Allow",
 "Action": [
 "elasticloadbalancing:DescribeLoadBalancers",
 "elasticloadbalancing:DescribeTargetGroups",
 "elasticloadbalancing:DescribeTargetHealth"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AutoScaling",
 "Effect": "Allow",
 "Action": [
 "autoscaling:DescribeAutoScalingGroups"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "SSMParameter",
 "Effect": "Allow",
 "Action": [
 "ssm:PutParameter",
 "ssm:DeleteParameter",
 "ssm:AddTagsToResource",
 "ssm:RemoveTagsFromResource",
 "ssm:GetParameters"
 ],
 "Resource": "arn:aws:ssm:*:*:parameter/AmazonCloudWatch-ApplicationInsights-*"
 },
 {
 "Sid": "SSMAssociation",
 "Effect": "Allow",
 "Action": [
 "ssm:CreateAssociation",
 "ssm:UpdateAssociation",
 "ssm:DeleteAssociation",
 "ssm:DescribeAssociation"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ssm:*:*:association/*",
 "arn:aws:ssm:*:*:managed-instance/*",
 "arn:aws:ssm:*:*:document/AWSEC2-ApplicationInsightsCloudwatchAgentInstallAndConfigure",
 "arn:aws:ssm:*:*:document/AWS-ConfigureAWSPackage",
 "arn:aws:ssm:*:*:document/AmazonCloudWatch-ManageAgent"
 ]
 },
 {
 "Sid": "SSMOpsItem",
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsItem",
 "ssm:CreateOpsItem",
 "ssm:DescribeOpsItems",
 "ssm:UpdateOpsItem",
 "ssm:DescribeInstanceInformation"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "SSMTags",
 "Effect": "Allow",
 "Action": [
 "ssm:AddTagsToResource"
 ],
 "Resource": "arn:aws:ssm:*:*:opsitem/*"
 },
 {
 "Sid": "SSMGetCommandInvocation",
 "Effect": "Allow",
 "Action": [
 "ssm:ListCommandInvocations",
 "ssm:GetCommandInvocation"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "SSMSendCommand",
 "Effect": "Allow",
 "Action": "ssm:SendCommand",
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ssm:*:*:document/AWSEC2-CheckPerformanceCounterSets",
 "arn:aws:ssm:*:*:document/AWS-ConfigureAWSPackage",
 "arn:aws:ssm:*:*:document/AWSEC2-DetectWorkload",
 "arn:aws:ssm:*:*:document/AmazonCloudWatch-ManageAgent"
 ]
 },
 {
 "Sid": "EC2",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeVolumes",
 "ec2:DescribeVolumeStatus",
 "ec2:DescribeVpcs",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeNatGateways"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "RDS",
 "Effect": "Allow",
 "Action": [
 "rds:DescribeDBInstances",
 "rds:DescribeDBClusters"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "Lambda",
 "Effect": "Allow",
 "Action": [
 "lambda:ListFunctions",
 "lambda:GetFunctionConfiguration",
 "lambda:ListEventSourceMappings"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "EventBridgeManagedRule",
 "Effect": "Allow",
 "Action": [
 "events:PutRule",
 "events:PutTargets",
 "events:RemoveTargets",
 "events:DeleteRule"
 ],
 "Resource": [
 "arn:aws:events:*:*:rule/AmazonCloudWatch-ApplicationInsights-*"
 ]
 },
 {
 "Sid": "XRay",
 "Effect": "Allow",
 "Action": [
 "xray:GetServiceGraph",
 "xray:GetTraceSummaries",
 "xray:GetTimeSeriesServiceStatistics",
 "xray:GetTraceGraph"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "DynamoDB",
 "Effect": "Allow",
 "Action": [
 "dynamodb:ListTables",
 "dynamodb:DescribeTable",
 "dynamodb:DescribeContributorInsights",
 "dynamodb:DescribeTimeToLive"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ApplicationAutoscaling",
 "Effect": "Allow",
 "Action": [
 "application-autoscaling:DescribeScalableTargets"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "S3",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets",
 "s3:GetMetricsConfiguration",
 "s3:GetReplicationConfiguration"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "States",
 "Effect": "Allow",
 "Action": [
 "states:ListStateMachines",
 "states:DescribeExecution",
 "states:DescribeStateMachine",
 "states:GetExecutionHistory"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "APIGateway",
 "Effect": "Allow",
 "Action": [
 "apigateway:GET"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ECS",
 "Effect": "Allow",
 "Action": [
 "ecs:DescribeClusters",
 "ecs:DescribeContainerInstances",
 "ecs:DescribeServices",
 "ecs:DescribeTaskDefinition",
 "ecs:DescribeTasks",
 "ecs:DescribeTaskSets",
 "ecs:ListClusters",
 "ecs:ListContainerInstances",
 "ecs:ListServices",
 "ecs:ListTasks"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ECSCluster",
 "Effect": "Allow",
 "Action": [
 "ecs:UpdateClusterSettings"
 ],
 "Resource": [
 "arn:aws:ecs:*:*:cluster/*"
 ]
 },
 {
 "Sid": "EKS",
 "Effect": "Allow",
 "Action": [
 "eks:DescribeCluster",
 "eks:DescribeFargateProfile",
 "eks:DescribeNodegroup",
 "eks:ListClusters",
 "eks:ListFargateProfiles",
 "eks:ListNodegroups",
 "fsx:DescribeFileSystems",
 "fsx:DescribeVolumes"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "SNS",
 "Effect": "Allow",
 "Action": [
 "sns:GetSubscriptionAttributes",
 "sns:GetTopicAttributes",
 "sns:GetSMSAttributes",
 "sns:ListSubscriptionsByTopic",
 "sns:ListTopics"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "SQS",
 "Effect": "Allow",
 "Action": [
 "sqs:ListQueues"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchLogsDeleteSubscriptionFilter",
 "Effect": "Allow",
 "Action": [
 "logs:DeleteSubscriptionFilter"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:*"
 ]
 },
 {
 "Sid": "CloudWatchLogsCreateSubscriptionFilter",
 "Effect": "Allow",
 "Action": [
 "logs:PutSubscriptionFilter"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:*",
 "arn:aws:logs:*:*:destination:AmazonCloudWatch-ApplicationInsights-LogIngestionDestination*"
 ]
 },
 {
 "Sid": "EFS",
 "Effect": "Allow",
 "Action": [
 "elasticfilesystem:DescribeFileSystems"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "Route53",
 "Effect": "Allow",
 "Action": [
 "route53:GetHostedZone",
 "route53:GetHealthCheck",
 "route53:ListHostedZones",
 "route53:ListHealthChecks",
 "route53:ListQueryLoggingConfigs"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "Route53Resolver",
 "Effect": "Allow",
 "Action": [
 "route53resolver:ListFirewallRuleGroupAssociations",
 "route53resolver:GetFirewallRuleGroup",
 "route53resolver:ListFirewallRuleGroups",
 "route53resolver:ListResolverEndpoints",
 "route53resolver:GetResolverQueryLogConfig",
 "route53resolver:ListResolverQueryLogConfigs",
 "route53resolver:ListResolverQueryLogConfigAssociations",
 "route53resolver:GetResolverEndpoint",
 "route53resolver:GetFirewallRuleGroupAssociation"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```





You must configure permissions to allow an IAM entity (such as a user, group, or role)
 to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions") in the
 *IAM User Guide*.


## Creating a service-linked role for
 CloudWatch Application Insights


You don't need to manually create a service-linked role. When you
 create a new Application Insights application in the AWS Management Console, CloudWatch Application Insights creates the service-linked role for
 you. 


If you delete this service-linked role, and then want to create it again, you can use the
 same process to recreate the role in your account. When you create a new Application Insights application,
 CloudWatch Application Insights creates the service-linked role for you again. 


## Editing a service-linked role for CloudWatch Application Insights


CloudWatch Application Insights does not allow you to edit the AWSServiceRoleForApplicationInsights service-linked role. After you
 create a service-linked role, you cannot change the name of the role because various entities
 might reference the role. However, you can edit the description of the role using IAM. For
 more information, see [Editing a
 Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role") in the *IAM User Guide*.


## Deleting a service-linked role for
 CloudWatch Application Insights


If you no longer need to use a feature or service that requires a service-linked role, we
 recommend that you delete that role. That way you avoid having an unused entity that is not
 actively monitored or maintained. However, you must delete all applications in Application
 Insights before you can manually delete the role.


###### Note

If the CloudWatch Application Insights service is using the role when you try to delete the resources, the
 deletion might fail. If that happens, wait for a few minutes and try the operation
 again.


###### To delete CloudWatch Application Insights resources used by the AWSServiceRoleForApplicationInsights

* Delete all of your CloudWatch Application Insights applications. For more information, see "Deleting
 Your Application(s)" in the CloudWatch Application Insights User Guide.

**To manually delete the service-linked role using
 IAM**


Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForApplicationInsights service-linked
 role. For more information, see [Deleting a
 Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role") in the *IAM User Guide*.


## Supported Regions for CloudWatch Application Insights service-linked roles


CloudWatch Application Insights supports using service-linked roles in all of the AWS Regions where the
 service is available. For more information, see [CloudWatch Application Insights Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/applicationinsights.html "https://docs.aws.amazon.com/general/latest/gr/applicationinsights.html").
