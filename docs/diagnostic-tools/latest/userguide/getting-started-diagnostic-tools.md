

# Get started with AWS Diagnostic Tools
<a name="getting-started-diagnostic-tools"></a>

**Topics**
+ [Overview](#getting-started-overview)
+ [Enabling Diagnostic Tools on your account](#create-policy-snippet)
+ [Partner training for Diagnostic Tools](#partner-training-overview)

## Overview
<a name="getting-started-overview"></a>

To access the AWS Diagnostic Tools service, your account must be managed by a Partner-Led Support (PLS) program partner. 

**Tip**  
Learn more about the [Partner-Led Support program](https://aws.amazon.com/premiumsupport/partner-led-support/).

Your partners use a role with read-only IAM permissions that you create to run Diagnostic Tools, which perform read-only operations on your AWS account. This helps your partners quickly investigate issues with your AWS services or applications deployed on your AWS account.

**Note**  
Diagnostic Tools is only visible on your account if your account is managed by an AWS Partner that is a part of the AWS Partner-Led Support program. If your account is managed by an AWS Partner under the [Partner-Led Support program](https://aws.amazon.com/premiumsupport/partner-led-support/), and you don't see Diagnostic Tools, please contact your partner to investigate.

## Enabling Diagnostic Tools on your account
<a name="create-policy-snippet"></a>

Before you can enable the AWS Diagnostic Tools service on your account, you must meet the following prerequisites:

1. Your partner must be in the [Partner-Led Support program](https://aws.amazon.com/premiumsupport/partner-led-support/).

1. Your partner should enlist your account as a managed account based on your support plan with your partner.

1. For each account managed by your partner, you must create the read-only IAM role with the permission policy attached to the trust policy that can execute Diagnostic Tools on your account.

1. Your partner must use the IAM role you create to federate into the account to use Diagnostic Tools.

Follow these instructions to create the read-only IAM role for Diagnostic Tools on your account:

### Step 1: Create a permission policy
<a name="collapsible-create-iam-role"></a>

**Create a permission policy with the correct API permissions**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Policy**, then choose **JSON**.

1. Copy and paste the following policy.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "acm-pca:ListCertificateAuthorities",
           "acm-pca:describeCertificateAuthority",
           "acm-pca:describeCertificateAuthorityAuditReport",
           "acm-pca:getCertificateAuthorityCertificate",
           "acm-pca:getCertificateAuthorityCsr",
           "acm-pca:listTags",
           "acm:describeCertificate",
           "acm:getCertificate",
           "acm:listCertificates",
           "acm:listTagsForCertificate",
           "cloudfront:listDistributionsByWebACLId",
           "cloudtrail:describeTrails",
           "cloudtrail:getEventSelectors",
           "cloudtrail:lookupEvents",
           "cloudwatch:getMetricData",
           "cloudwatch:listDashboards",
           "cloudwatch:getDashboard",
           "cloudwatch:listMetrics",
           "codepipeline:getPipeline",
           "codepipeline:getPipelineState",
           "codepipeline:listActionTypes",
           "codepipeline:listPipelineExecutions",
           "codepipeline:listPipelines",
           "ec2:describeCapacityReservations",
           "ec2:describeByoipCidrs",
           "ec2:describeDhcpOptions",
           "ec2:describeNatGateways",
           "ec2:describeNetworkAcls",
           "ec2:describeNetworkInterfaces",
           "ec2:describePublicIpv4Pools",
           "ec2:describeRouteTables",
           "ec2:describeSecurityGroups",
           "ec2:describeSpotFleetRequests",
           "ec2:describeSpotInstanceRequests",
           "ec2:describeSubnets",
           "ec2:describeVpcs",
           "elasticfilesystem:describeAccessPoints",
           "elasticfilesystem:describeFileSystemPolicy",
           "elasticfilesystem:describeFileSystems",
           "elasticfilesystem:describeLifecycleConfiguration",
           "elasticfilesystem:describeMountTargets",
           "elasticfilesystem:listTagsForResource",
           "elasticloadbalancing:describeListeners",
           "elasticloadbalancing:describeLoadBalancers",
           "elasticloadbalancing:describeTags",
           "elasticloadbalancing:describeTargetGroups",
           "elasticloadbalancing:describeTargetHealth",
           "events:describeRule",
           "events:listApiDestinations",
           "events:listConnections",
           "events:listEventBuses",
           "events:listEventSources",
           "events:listRules",
           "events:listTargetsByRule",
           "guardduty:getFindings",
           "guardduty:listDetectors",
           "guardduty:listFindings",
           "guardduty:listIPSets",
           "guardduty:listThreatIntelSets",
           "iam:getAccessKeyLastUsed",
           "iam:getGroupPolicy",
           "iam:getPolicy",
           "iam:getPolicyVersion",
           "iam:getRole",
           "iam:getRolePolicy",
           "iam:getServerCertificate",
           "iam:getUser",
           "iam:getUserPolicy",
           "iam:listAccessKeys",
           "iam:listAttachedGroupPolicies",
           "iam:listAttachedRolePolicies",
           "iam:listAttachedUserPolicies",
           "iam:listGroupPolicies",
           "iam:listGroupsForUser",
           "iam:listInstanceProfiles",
           "iam:listMFADevices",
           "iam:listPolicies",
           "iam:listPolicyVersions",
           "iam:listRolePolicies",
           "iam:listRoles",
           "iam:listSSHPublicKeys",
           "iam:listServerCertificates",
           "iam:listUserPolicies",
           "iam:listUsers",
           "iam:listVirtualMFADevices",
           "lambda:getAccountSettings",
           "lambda:listEventSourceMappings",
           "lambda:listFunctions",
           "lambda:listLayers",
           "lambda:getFunction",
           "lambda:getPolicy",
           "lambda:listAliases",
           "lambda:listProvisionedConcurrencyConfigs",
           "lambda:listVersionsByFunction",
           "logs:describeExportTasks",
           "logs:describeLogGroups",
           "logs:describeLogStreams",
           "logs:describeMetricFilters",
           "logs:describeSubscriptionFilters",
           "medialive:listChannels",
           "medialive:listInputSecurityGroups",
           "medialive:listInputs",
           "mobiletargeting:getAdmChannel",
           "mobiletargeting:getApnsChannel",
           "mobiletargeting:getApnsSandboxChannel",
           "mobiletargeting:getApnsVoipChannel",
           "mobiletargeting:getApnsVoipSandboxChannel",
           "mobiletargeting:getApplicationSettings",
           "mobiletargeting:getApps",
           "mobiletargeting:getBaiduChannel",
           "mobiletargeting:getCampaign",
           "mobiletargeting:getCampaignActivities",
           "mobiletargeting:getCampaignVersions",
           "mobiletargeting:getCampaigns",
           "mobiletargeting:getEmailChannel",
           "mobiletargeting:getEventStream",
           "mobiletargeting:getExportJobs",
           "mobiletargeting:getGcmChannel",
           "mobiletargeting:getImportJobs",
           "mobiletargeting:getJourney",
           "mobiletargeting:getJourneyExecutionActivityMetrics",
           "mobiletargeting:getJourneyExecutionMetrics",
           "mobiletargeting:getJourneyRunExecutionActivityMetrics",
           "mobiletargeting:getJourneyRuns",
           "mobiletargeting:getSegment",
           "mobiletargeting:getSegmentImportJobs",
           "mobiletargeting:getSegmentVersions",
           "mobiletargeting:getSegments",
           "mobiletargeting:getSmsChannel",
           "mobiletargeting:listJourneys",
           "pipes:listPipes",
           "polly:describeVoices",
           "polly:listLexicons",
           "rds:describeDBClusterParameterGroups",
           "rds:describeDBClusterParameters",
           "rds:describeDBClusterSnapshots",
           "rds:describeDBClusters",
           "rds:describeDBInstances",
           "rds:describeDBParameterGroups",
           "rds:describeDBParameters",
           "rds:describeDBSecurityGroups",
           "rds:describeDBSnapshots",
           "rds:describeDBSubnetGroups",
           "rds:describeEvents",
           "rds:describePendingMaintenanceActions",
           "rds:listTagsForResource",
           "redshift:describeClusterParameterGroups",
           "redshift:describeClusterParameters",
           "redshift:describeClusterSnapshots",
           "redshift:describeClusterSubnetGroups",
           "redshift:describeClusters",
           "redshift:describeEventSubscriptions",
           "redshift:describeEvents",
           "redshift:describeLoggingStatus",
           "redshift:describeReservedNodes",
           "redshift:describeResize",
           "route53domains:getDomainDetail",
           "route53domains:getOperationDetail",
           "route53domains:listDomains",
           "route53domains:listOperations",
           "scheduler:listScheduleGroups",
           "scheduler:listSchedules",
           "servicequotas:listAWSDefaultServiceQuotas",
           "servicequotas:listServiceQuotas",
           "ssm:describeActivations",
           "ssm:describeAutomationExecutions",
           "ssm:describeInstanceInformation",
           "ssm:describeMaintenanceWindows",
           "ssm:describeParameters",
           "ssm:describePatchBaselines",
           "ssm:describePatchGroups",
           "ssm:listDocuments",
           "swf:describeActivityType",
           "swf:describeDomain",
           "swf:describeWorkflowExecution",
           "swf:describeWorkflowType",
           "swf:getWorkflowExecutionHistory",
           "swf:listActivityTypes",
           "swf:listClosedWorkflowExecutions",
           "swf:listDomains",
           "swf:listOpenWorkflowExecutions",
           "swf:listWorkflowTypes",
           "waf-regional:getWebACL",
           "waf-regional:listResourcesForWebACL",
           "waf-regional:listWebACLs",
           "waf:getWebACL",
           "waf:listWebACLs"
        ],
         "Resource": "*"
       }
     ]
   }
   ```

------

1. Give the policy a name. Note this name. You will need it in a later step. 

1. Add a description.

### Step 2: Create a trust policy and add permissions
<a name="collapsible-trust-policy"></a>

1. In the IAM dashboard, choose **Roles** on the left panel.

1. Choose **Create role**.

1. Select the **Custom trust policy** option.

1. Copy and paste the following into the **Custom trust policy** panel.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [{
           "Effect": "Allow",
           "Principal": {
               "Service": [
                   "ts.amazonaws.com"
               ]
           },
           "Action": "sts:AssumeRole"
       }]
   }
   ```

------

1. Choose **Next**. Select **Add permissions**, then select **Attach policies**. 

1. Search for the permission policy you created and select it.

1. Choose **Next**, then enter a name and description. 
**Note**  
You share this permission with your partner. Enter a name you can use to recognize this role.

1. Create the IAM role. Share the name of this IAM role with your partner.

## Partner training for Diagnostic Tools
<a name="partner-training-overview"></a>

As a part of your partner's participation in the Partner-Led Support program, we provide training on how to use Diagnostic Tools and when to use them.

**Tip**  
Your partners can access their training content at the [AWS Skill Builder](https://explore.skillbuilder.aws/learn/signin) site. 