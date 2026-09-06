

# Required permissions for using custom IAM policies to manage access to the Connect Customer console
<a name="security-iam-amazon-connect-permissions"></a>

If you're using custom [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) policies to manage access to the Connect Customer console, your users need some or all of the permissions listed in this article, depending on the tasks they need to do. 

**Note**  
Using `connect:*` in a custom IAM policy grants your users all of the Connect Customer permissions listed in this article.

**Note**  
Certain pages on the Connect Customer console, such as [Tasks](#tasks-page) and [Customer Profiles](#customer-profiles-page), require that you add permissions to your inline policies. 

**Topics**
+ [AmazonConnect\_FullAccess policy](#amazonconnectfullaccesspolicy)
+ [AmazonConnectReadOnlyAccess policy](#amazonconnectreadonlyaccesspolicy)
+ [Home page](#console-home-page-permissions)
+ [Detail pages](#detail-pages)
+ [Overview page](#overview-page)
+ [Telephony page](#telephony-page)
+ [Data storage page](#data-storage-page)
+ [Data streaming page](#data-streaming-page)
+ [Flows page](#contact-flows-page)
+ [Conversational analytics connectors page](#contactlensconnectors-page)
+ [Voice transfer integrations page](#voice-transfer-integrations-page)
+ [Application integration page](#application-integration-page)
+ [Customer Profiles page](#customer-profiles-page)
+ [Tasks page](#tasks-page)
+ [Email page](#email-page)
+ [Cases page](#cases-page)
+ [Customer authentication page](#customer-authentication-page)
+ [Outbound campaigns page](#outbound-campaigns-page)
+ [agent assist page](#wisdom-page)
+ [Voice ID page](#voiceid-page)
+ [Forecasting & agent scheduling page](#forecasting-page)
+ [Federations](#federations)

## AWS managed policy: AmazonConnect\_FullAccess policy
<a name="amazonconnectfullaccesspolicy"></a>

To allow full read/write access to Connect Customer, you must attach two policies to your users, groups, or roles. Attach the `AmazonConnect_FullAccess` policy and a custom policy with the following contents:

------
#### [ JSON ]

****  

```
{ 
    "Version":"2012-10-17",		 	 	  
    "Statement": [ 
        { 
            "Sid": "AttachAnyPolicyToAmazonConnectRole", 
            "Effect": "Allow", 
            "Action": "iam:PutRolePolicy", 
            "Resource": "arn:aws:iam::*:role/aws-service-role/connect.amazonaws.com/AWSServiceRoleForAmazonConnect*" 
        } 
    ] 
}
```

------

To allow a user to create an instance, make sure that they have the permissions granted by the `AmazonConnect_FullAccess` policy.

When you use `AmazonConnect_FullAccess` policy, note the following:
+ Additional privileges are required to create an Amazon S3 bucket with a name of your choosing, or to use an existing bucket while creating or updating an instance from the Connect Customer admin website. If you choose default storage locations for your call recordings, chat transcripts, email messages, attachments, call transcripts, and other data, the system prepends `"amazon-connect-"` to those objects.
+ The `aws/connect` KMS key is available to use as a default encryption option. To use a custom encryption key, assign users additional KMS privileges.
+ Assign users additional privileges to attach other AWS resources like Amazon Polly, Live Media Streaming, Data Streaming, and Lex bots to their Connect Customer instances. 

## AWS managed policy: AmazonConnectReadOnlyAccess policy
<a name="amazonconnectreadonlyaccesspolicy"></a>

To allow read-only access, you need to attach only the `AmazonConnectReadOnlyAccess` policy.

## Connect Customer console home page
<a name="console-home-page-permissions"></a>

The following image shows a sample Connect Customer console home page, with an arrow pointing to the instance alias. Choose the instance alias to navigate to the detailed instance pages.

![The Connect Customer virtual contact center instances page, the instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)


Use the permissions listed in the following table to manage access to this page.


| Action/Use case | Permissions needed | 
| --- | --- | 
| List instance | `connect:ListInstances`<br />`ds:DescribeDirectories` | 
| Describe instance: View the details of the instance/ current settings | `connect:DescribeInstance`<br />`connect:ListLambdaFunctions`<br />`connect:ListLexBots`<br />`connect:ListInstanceStorageConfigs`<br />`connect:ListApprovedOrigins`<br />`connect:ListSecurityKeys`<br />`connect:DescribeInstanceAttributes`<br />`connect:DescribeInstanceStorageConfig`<br />`ds:DescribeDirectories` | 
| Create instance | `connect:AssociateCustomerProfilesDomain`<br />`connect:CreateInstance`<br />`connect:DescribeInstance`<br />`connect:ListInstances`<br />`connect:AssociateInstanceStorageConfig`<br />`connect:UpdateInstanceAttribute`<br />`ds:CheckAlias`<br />`ds:CreateAlias`<br />`ds:AuthorizeApplication`<br />`ds:UnauthorizeApplication`<br />`ds:CreateIdentityPoolDirectory`<br />`ds:DescribeDirectories`<br />`iam:CreateServiceLinkedRole`<br />`iam:PutRolePolicy`<br />`kms:CreateGrant`<br />`kms:DescribeKey`<br />`kms:ListAliases`<br />`kms:RetireGrant`<br />`logs:CreateLogGroup`<br />`s3:CreateBucket`<br />`s3:GetBucketLocation`<br />`s3:ListAllMyBuckets`<br />`servicequotas:GetServiceQuota`<br />`profile:CreateDomain`<br />`profile:GetDomain`<br />`profile:GetProfileObjectType`<br />`profile:ListAccountIntegrations`<br />`profile:ListDomains`<br />`profile:ListProfileObjectTypeTemplates`<br />`profile:PutIntegration` | 
| Create a replica instance (Connect Customer Global Resiliency): Replicate an instance in another AWS Region with the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API | `connect:ReplicateInstance`<br />Because this action creates a new instance in the replica AWS Region, you also need the permissions listed for **Create instance** in the preceding rows. | 
| Delete instance | `connect:DescribeInstance`<br />`connect:DeleteInstance`<br />`connect:ListInstances`<br />`ds:DescribeDirectories`<br />`ds:DeleteDirectory`<br />`ds:UnauthorizeApplication` | 

## Detailed instance pages
<a name="detail-pages"></a>

The following image shows the navigation menu you use to access each of the detailed instance pages.

![The navigation menu on the Connect Customer instances page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/iam-custom-permissions-admin-console-telephony-page.png)


To access the detailed instance pages, you need permissions to the Connect Customer console home page (describe/list). Or, use the `AmazonConnectReadOnlyAccess` policy.

The following tables list the granular permissions for each detailed instance page.

**Note**  
To perform `Edit` actions, users also need `List` and `Describe` permissions.

## Overview page
<a name="overview-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| Create service-linked role | `connect:DescribeInstance`<br />`connect:ListInstances`<br />`connect:DescribeInstanceAttribute`<br />`connect:UpdateInstanceAttribute`<br />`connect:ListIntegrationAssociations`<br />`profile:ListAccountIntegrations`<br />`ds:DescribeDirectories`<br />`iam:CreateServiceLinkedRole`<br />`iam:PutRolePolicy` | 

## Telephony page
<a name="telephony-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View telephony options | `connect:DescribeInstance` | 
| Enable/Disable telephony options  | `connect:UpdateInstanceAttribute` | 
| View outbound campaigns | `connect-campaigns:GetConnectInstanceConfig`<br />`connect-campaigns:GetInstanceOnboardingJobStatus`<br />`connect:DescribeInstance`<br />`connect:DescribeInstanceAttribute`<br />`kms:DescribeKey` | 
| Enable/disable outbound campaigns | `connect-campaigns:GetConnectInstanceConfig`<br />`connect-campaigns:GetInstanceOnboardingJobStatus`<br />`connect-campaigns:StartInstanceOnboardingJob`<br />`connect-campaigns:DeleteInstanceOnboardingJob`<br />`connect-campaigns:DeleteConnectInstanceConfig`<br />`connect:DescribeInstance`<br />`connect:DescribeInstanceAttribute`<br />`connect:UpdateInstanceAttribute`<br />`iam:CreateServiceLinkedRole`<br />`iam:DeleteServiceLinkedRole`<br />`iam:AttachRolePolicy`<br />`iam:PutRolePolicy`<br />`iam:DeleteRolePolicy`<br />`events:PutRule`<br />`events:PutTargets`<br />`events:DeleteRule`<br />`events:RemoveTargets`<br />`events:DescribeRule`<br />`events:ListTargetsByRule`<br />`ds:DescribeDirectories`<br />`kms:DescribeKey`<br />`kms:ListKeys`<br />`kms:CreateGrant`<br />`kms:RetireGrant` | 

## Data storage page
<a name="data-storage-page"></a>

### Call recording section
<a name="call-recording-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View call recording | `connect:DescribeInstance`<br />`connect:ListInstanceStorageConfigs`<br />`connect:DescribeInstanceStorageConfig` | 
| Edit call recording | `connect:AssociateInstanceStorageConfig`<br />`connect:UpdateInstanceStorageConfig`<br />`connect:DisassociateInstanceStorageConfig`<br />`s3:ListAllMyBuckets`<br />`s3:GetBucketLocation`<br />`s3:GetBucketAcl`<br />`s3:CreateBucket`<br />`kms:CreateGrant`<br />`kms:DescribeKey`<br />`kms:ListAliases`<br />`kms:RetireGrant`<br />`iam:PutRolePolicy` | 

### Screen recording section
<a name="screen-recording-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View screen recording | `connect:DescribeInstance`<br />`connect:ListInstanceStorageConfigs`<br />`connect:DescribeInstanceStorageConfig` | 
| Edit screen recording | `connect:AssociateInstanceStorageConfig`<br />`connect:UpdateInstanceStorageConfig`<br />`connect:DisassociateInstanceStorageConfig`<br />`s3:ListAllMyBuckets`<br />`s3:GetBucketLocation`<br />`s3:GetBucketAcl`<br />`s3:CreateBucket`<br />`iam:PutRolePolicy`<br />`kms:CreateGrant`<br />`kms:DescribeKey`<br />`kms:ListAliases`<br />`kms:RetireGrant` | 

### Chat transcripts section
<a name="chat-transcripts-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View chat transcripts | `connect:DescribeInstance`<br />`connect:DescribeInstanceStorageConfig`<br />`connect:ListInstanceStorageConfigs` | 
| Edit chat transcripts | `connect:AssociateInstanceStorageConfig`<br />`connect:UpdateInstanceStorageConfig`<br />`connect:DisassociateInstanceStorageConfig`<br />`s3:ListAllMyBuckets`<br />`s3:GetBucketLocation`<br />`s3:GetBucketAcl`<br />`s3:CreateBucket`<br />`kms:CreateGrant`<br />`kms:DescribeKey`<br />`kms:ListAliases`<br />`kms:RetireGrant`<br />`iam:PutRolePolicy` | 

### Attachments section
<a name="attachments-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View attachments | `connect:DescribeInstance`<br />`connect:DescribeInstanceStorageConfig`<br />`connect:ListInstanceStorageConfigs` | 
| Edit attachments | `connect:AssociateInstanceStorageConfig`<br />`connect:UpdateInstanceStorageConfig`<br />`connect:DisassociateInstanceStorageConfig`<br />`s3:ListAllMyBuckets`<br />`s3:GetBucketLocation`<br />`s3:CreateBucket`<br />`s3:GetBucketAcl`<br />`kms:CreateGrant`<br />`kms:DescribeKey`<br />`kms:ListAliases`<br />`kms:RetireGrant`<br />`iam:PutRolePolicy` | 

### Live media streaming section
<a name="live-media-streaming-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View live media streaming | `connect:DescribeInstance`<br />`connect:ListInstanceStorageConfigs`<br />`connect:DescribeInstanceStorageConfig` | 
| Edit live media streaming | `connect:AssociateInstanceStorageConfig`<br />`connect:UpdateInstanceStorageConfig`<br />`connect:DisassociateInstanceStorageConfig`<br />`kms:CreateGrant`<br />`kms:DescribeKey`<br />`kms:RetireGrant`<br />`iam:PutRolePolicy` | 

### Exported reports section
<a name="exported-reports-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View exported reports | `connect:DescribeInstance`<br />`connect:ListInstanceStorageConfigs`<br />`connect:DescribeInstanceStorageConfig` | 
| Edit exported reports | `connect:AssociateInstanceStorageConfig`<br />`connect:UpdateInstanceStorageConfig`<br />`connect: DisassociateInstanceStorageConfig`<br />`s3:ListAllMyBuckets`<br />`s3:GetBucketLocation`<br />`s3:CreateBucket`<br />`kms:DescribeKey`<br />`kms:ListAliases`<br />`kms:RetireGrant`<br />`kms:CreateGrant`<br />`iam:PutRolePolicy` | 

## Data streaming page
<a name="data-streaming-page"></a>

### Contact records section
<a name="ctr-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View data streaming - Contact records | `connect:DescribeInstance`<br />`connect:ListInstanceStorageConfigs`<br />`connect:DescribeInstanceStorageConfig` | 
| Edit contact record | `connect:AssociateInstanceStorageConfig`<br />`connect:UpdateInstanceStorageConfig`<br />`connect:DisassociateInstanceStorageConfig`<br />`firehose:ListDeliveryStreams`<br />`firehose:DescribeDeliveryStream`<br />`kinesis:ListStreams`<br />`kinesis:DescribeStream`<br />`iam:PutRolePolicy` | 

### Agent events section
<a name="agent-events-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View data streaming - Agent events | `connect:DescribeInstance`<br />`connect:ListInstanceStorageConfigs`<br />`connect:DescribeInstanceStorageConfig` | 
| Edit agent events | `connect:AssociateInstanceStorageConfig`<br />`connect:UpdateInstanceStorageConfig`<br />`connect:DisassociateInstanceStorageConfig`<br />`kinesis:ListStreams`<br />`kinesis: DescribeStream`<br />`iam:PutRolePolicy` | 

## Flows page
<a name="contact-flows-page"></a>

### Flows security keys section
<a name="security-keys-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View flow security keys | `connect:DescribeInstance`<br />`connect:ListSecurityKeys` | 
| Add/remove flow security keys | `connect:AssociateSecurityKey`<br />`connect:DisassociateSecurityKey` | 

### Lex bots section
<a name="lex-bots-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View Lex bots | `connect:ListLexBots`<br />`connect:ListBots` | 
| Add/remove Lex bots | `lex:GetBots`<br />`lex:GetBot`<br />`lex:CreateResourcePolicy`<br />`lex:DeleteResourcePolicy`<br />`lex:UpdateResourcePolicy`<br />`lex:DescribeBotAlias`<br />`lex:ListBotAliases`<br />`lex:ListBots`<br />`connect:AssociateBot`<br />`connect:DisassociateBot`<br />`connect:ListBots`<br />`connect:AssociateLexBot`<br />`connect:DisassociateLexBot`<br />`connect:ListLexBots`<br />`iam:PutRolePolicy` | 

### Lambda functions section
<a name="lambda-functions-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View Lambda functions | `connect:ListLambdaFunctions` | 
| Add/remove Lambda functions | `connect:ListLambdaFunctions`<br />`connect:AssociateLambdaFunction`<br />`connect:DisassociateLambdaFunction`<br />`iam:PutRolePolicy`<br />`lambda:ListFunctions`<br />`lambda:AddPermission`<br />`lambda:RemovePermission` | 

### Flow logs section
<a name="contact-flow-logs-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View flow log config | `connect:DescribeInstance`<br />`connect:DescribeInstanceAttribute` | 
| Enable/disable flow log | `logs:CreateLogGroup` | 

### Amazon Polly section
<a name="amazon-polly-section"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View Amazon Polly option | `connect:DescribeInstance`<br />`connect:DescribeInstanceAttribute` | 
| Update Amazon Polly option | `connect:UpdateInstanceAttribute` | 

## Conversational analytics connectors page
<a name="contactlensconnectors-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View conversational analytics connectors | `connect:ListIntegrationAssociations`<br />`chime:GetVoiceConnector`<br />`chime:GetVoiceConnectorLoggingConfiguration`<br />`chime:GetVoiceConnectorTermination`<br />`chime:GetVoiceConnectorTerminationHealth`<br />`chime:ListVoiceConnectors`<br />`chime:ListVoiceConnectorTerminationCredentials`<br />`chime:GetVoiceConnectorExternalSystemsConfiguration` | 
| Add/Update/Remove conversational analytics connectors | `chime:CreateVoiceConnector`<br />`chime:DeleteVoiceConnector`<br />`chime:DeleteVoiceConnectorTermination`<br />`chime:DeleteVoiceConnectorTerminationCredentials`<br />`chime:GetVoiceConnector`<br />`chime:GetVoiceConnectorLoggingConfiguration`<br />`chime:GetVoiceConnectorTermination`<br />`chime:GetVoiceConnectorTerminationHealth`<br />`chime:ListVoiceConnectors`<br />`chime:ListVoiceConnectorTerminationCredentials`<br />`chime:PutVoiceConnectorLoggingConfiguration`<br />`chime:PutVoiceConnectorTermination`<br />`chime:PutVoiceConnectorTerminationCredentials`<br />`chime:UpdateVoiceConnector`<br />`chime:CreateConnectAnalyticsConnector`<br />`chime:PutVoiceConnectorExternalSystemsConfiguration`<br />`chime:GetVoiceConnectorExternalSystemsConfiguration`<br />`chime:DeleteVoiceConnectorExternalSystemsConfiguration`<br />`chime:AssociateVoiceConnectorConnect`<br />`chime:DisassociateVoiceConnectorConnect`<br />`chime:TagResources`<br />`chime:UntagResources`<br />`chime:ListTagsForResource` | 

## Voice transfer integrations page
<a name="voice-transfer-integrations-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View external voice transfer connectors | `connect:ListIntegrationAssociations`<br />`chime:GetVoiceConnector`<br />`chime:GetVoiceConnectorLoggingConfiguration`<br />`chime:GetVoiceConnectorOrigination`<br />`chime:GetVoiceConnectorTermination`<br />`chime:GetVoiceConnectorTerminationHealth`<br />`chime:ListVoiceConnectors`<br />`chime:ListVoiceConnectorTerminationCredentials`<br />`chime:GetVoiceConnectorExternalSystemsConfiguration`<br />`servicequotas:GetServiceQuota` | 
| Add/Update/Remove external voice transfer connectors | `connect:CreateIntegrationAssociation`<br />`connect:DeleteIntegrationAssociation`<br />`connect:ListIntegrationAssociations`<br />`chime:CreateConnectCallTransferConnector`<br />`chime:CreateVoiceConnector`<br />`chime:DeleteVoiceConnector`<br />`chime:DeleteVoiceConnectorTermination`<br />`chime:DeleteVoiceConnectorTerminationCredentials`<br />`chime:GetVoiceConnector`<br />`chime:GetVoiceConnectorLoggingConfiguration`<br />`chime:GetVoiceConnectorOrigination`<br />`chime:GetVoiceConnectorTermination`<br />`chime:GetVoiceConnectorTerminationHealth`<br />`chime:ListVoiceConnectors`<br />`chime:ListVoiceConnectorTerminationCredentials`<br />`chime:PutVoiceConnectorLoggingConfiguration`<br />`chime:PutVoiceConnectorOrigination`<br />`chime:PutVoiceConnectorTermination`<br />`chime:PutVoiceConnectorTerminationCredentials`<br />`chime:UpdateVoiceConnector`<br />`chime:CreateConnectAnalyticsConnector`<br />`chime:PutVoiceConnectorExternalSystemsConfiguration`<br />`chime:GetVoiceConnectorExternalSystemsConfiguration`<br />`chime:DeleteVoiceConnectorExternalSystemsConfiguration`<br />`chime:AssociateVoiceConnectorConnect`<br />`chime:DisassociateVoiceConnectorConnect`<br />`chime:TagResources`<br />`chime:UntagResources`<br />`chime:ListTagsForResource`<br />`servicequotas:GetServiceQuota` | 

## Application integration page
<a name="application-integration-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View approved origins | `connect:DescribeInstance`<br />`connect:ListApprovedOrigins` | 
| Edit approved origins | `connect: AssociateApprovedOrigin`<br />`connect:ListApprovedOrigins`<br />`connect:DisassociateApprovedOrigin` | 

## Customer Profiles page
<a name="customer-profiles-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View customer profiles | `app-integrations:ListEventIntegrations`<br />`appflow:DescribeConnectorEntity`<br />`appflow:DescribeConnectorProfiles`<br />`appflow:DescribeFlow`<br />`appflow:ListFlows`<br />`appflow:ListConnectorEntities`<br />`appflow:ListConnectorProfiles`<br />`cloudwatch:GetMetricData`<br />`connect:DescribeInstance`<br />`connect:ListInstances`<br />`ds:DescribeDirectories`<br />`iam:ListRoles`<br />`kinesis:DescribeStreamSummary`<br />`kms:Decrypt`<br />`kms:DescribeKey`<br />`kms:GenerateDataKey`<br />`kms:ListKeys`<br />`profile:GetCalculatedAttributeDefinition`<br />`profile:GetDomain`<br />`profile:GetEventStream`<br />`profile:GetIdentityResolutionJob`<br />`profile:GetIntegration`<br />`profile:GetProfileObjectType`<br />`profile:GetProfileObjectTypeTemplate`<br />`profile:GetWorkflow`<br />`profile:ListAccountIntegrations`<br />`profile:ListCalculatedAttributeDefinitions`<br />`profile:ListDomains`<br />`profile:ListDomainLayouts`<br />`profile:ListEventStreams`<br />`profile:ListIdentityResolutionJobs`<br />`profile:ListIntegrations`<br />`profile:ListProfileObjectTypes`<br />`profile:ListProfileObjectTypeTemplates`<br />`profile:ListRecommenders`<br />`profile:ListSegmentDefinitions`<br />`sqs:ListQueues` | 
| Edit customer profiles | `app-integrations:CreateEventIntegration`<br />`app-integrations:ListEventIntegrations`<br />`appflow:CreateFlow`<br />`appflow:CreateConnectorProfile`<br />`appflow:DescribeFlow`<br />`appflow:DeleteFlow`<br />`appflow:DescribeConnectorEntity`<br />`appflow:DescribeConnectorProfiles`<br />`appflow:ListFlows`<br />`appflow:ListConnectorEntities`<br />`appflow:ListConnectorProfiles`<br />`appflow:StartFlow`<br />`cloudwatch:GetMetricData`<br />`connect:DescribeInstance`<br />`connect:ListInstances`<br />`ds:DescribeDirectories`<br />`events:CreateEventBus`<br />`events:DescribeEventBus`<br />`events:DescribeEventSource`<br />`events:ListEventSources`<br />`iam:CreateRole`<br />`iam:CreatePolicy`<br />`iam:AttachRolePolicy`<br />`iam:ListRoles`<br />`iam:PutRolePolicy`<br />`kinesis:DescribeStreamSummary`<br />`kinesis:ListStreams`<br />`kms:CreateGrant`<br />`kms:Decrypt`<br />`kms:DescribeKey`<br />`kms:GenerateDataKey`<br />`kms:ListAliases`<br />`kms:ListKeys`<br />`kms:ListGrants`<br />`profile:CreateCalculatedAttributeDefinition`<br />`profile:CreateDomain`<br />`profile:CreateDomainLayout`<br />`profile:CreateEventStream`<br />`profile:CreateIntegrationWorkflow`<br />`profile:CreateSegmentDefinition`<br />`profile:DeleteEventStream`<br />`profile:DeleteIntegration`<br />`profile:DeleteDomain`<br />`profile:DeleteProfileObjectType`<br />`profile:DetectProfileObjectType`<br />`profile:GetCalculatedAttributeDefinition`<br />`profile:GetDomain`<br />`profile:GetEventStream`<br />`profile:GetIdentityResolutionJob`<br />`profile:GetIntegration`<br />`profile:GetProfileObjectType`<br />`profile:GetProfileObjectTypeTemplate`<br />`profile:GetWorkflow`<br />`profile:ListAccountIntegrations`<br />`profile:ListCalculatedAttributeDefinitions`<br />`profile:ListDomains`<br />`profile:ListDomainLayouts`<br />`profile:ListEventStreams`<br />`profile:ListIdentityResolutionJobs`<br />`profile:ListIntegrations`<br />`profile:ListProfileObjectTypes`<br />`profile:ListProfileObjectTypeTemplates`<br />`profile:ListSegmentDefinitions`<br />`profile:PutIntegration`<br />`profile:PutProfileObjectType`<br />`profile:TagResource`<br />`profile:UntagResource`<br />`profile:UpdateDomain`<br />`s3:GetBucketLocation`<br />`s3:GetBucketPolicy`<br />`s3:GetObject`<br />`s3:HeadBucket`<br />`s3:ListAllMyBuckets`<br />`s3:ListBucket`<br />`s3:ListObjectsV2`<br />`s3:PutBucketPolicy`<br />`s3:SelectObjectContent`<br />`sqs:ListQueues` | 

## Tasks page
<a name="tasks-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View Tasks integrations | `app-integrations:GetEventIntegration`<br />`connect:ListIntegrationAssociations` | 
| Edit Tasks integrations | `app-integrations:CreateEventIntegration`<br />`app-integrations:GetEventIntegration`<br />`app-integrations:ListEventIntegrations`<br />`app-integrations:DeleteEventIntegrationAssociation`<br />`app-integrations:CreateEventIntegrationAssociation`<br />`appflow:CreateFlow`<br />`appflow:CreateConnectorProfile`<br />`appflow:DescribeFlow`<br />`appflow:DeleteFlow`<br />`appflow:DeleteConnectorProfile`<br />`appflow:DescribeConnectorEntity`<br />`appflow:ListFlows`<br />`appflow:ListConnectorEntities`<br />`appflow:StartFlow`<br />`connect:ListIntegrationAssociations`<br />`connect:DeleteIntegrationAssociation`<br />`connect:ListUseCases`<br />`connect:DeleteUseCase`<br />`events:ActivateEventSource`<br />`events:CreateEventBus`<br />`events:DescribeEventBus`<br />`events:DescribeEventSource`<br />`events:ListEventSources`<br />`events:ListTargetsByRule`<br />`events:PutRule`<br />`events:PutTargets`<br />`events:DeleteRule`<br />`events:RemoveTargets`<br />`kms:CreateGrant`<br />`kms:DescribeKey`<br />`kms:ListAliases`<br />`kms:ListKeys`<br />`kms:ListGrants` | 

## Email page
<a name="email-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View email domains and addresses | `ses:GetIdentityVerificationAttributes`<br />`ses:DescribeReceiptRule`<br />`ses:DescribeActiveReceiptRuleSet`<br />`ses:GetEmailIdentity`<br />`ses:DescribeReceiptRuleSet`<br />`ses:GetConfigurationSetEventDestinations`<br />`ses:GetConfigurationSet` | 
| Edit email domains and addresses | `ses:CreateReceiptRule`<br />`ses:UpdateReceiptRule`<br />`ses:SetActiveReceiptRuleSet`<br />`ses:CreateReceiptRuleSet`<br />`ses:CreateEmailIdentity`<br />`ses:TagResource`<br />`ses:UntagResource`<br />`ses:DeleteReceiptRule`<br />`ses:DeleteReceiptRuleSet`<br />`ses:CloneReceiptRuleSet`<br />`ses:CreateConfigurationSet`<br />`ses:CreateConfigurationSetEventDestination`<br />`ses:PutEmailIdentityConfigurationSetAttributes`<br />`ses:CreateEmailIdentityPolicy`<br />`ses:UpdateEmailIdentityPolicy`<br />`ses:DeleteEmailIdentityPolicy`<br />`iam:CreateServiceLinkedRole`<br />`iam:PassRole`<br />`iam:CreateRole`<br />`iam:CreatePolicy` | 

## Cases page
<a name="cases-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View Cases domain details | `connect:ListInstances`<br />`ds:DescribeDirectories`<br />`connect:ListIntegrationAssociations`<br />`cases:GetDomain` | 
| Onboard to Cases | `connect:ListInstances`<br />`connect:ListIntegrationAssociations`<br />`cases:GetDomain`<br />`cases:CreateDomain`<br />`connect:CreateIntegrationAssociation`<br />`connect:DescribeInstance`<br />`iam:PutRolePolicy` | 

## Customer authentication page
<a name="customer-authentication-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View customer authentication | `connect:ListIntegrationAssociations`<br />`cognito-idp:ListUserPools`<br />`cognito-idp:DescribeUserPool` | 
| Onboard to customer authentication | `connect:CreateIntegrationAssociation`<br />`connect:DeleteIntegrationAssociation`<br />`connect:ListIntegrationAssociations`<br />`cognito-idp:ListUserPools`<br />`cognito-idp:DescribeUserPool`<br />`cognito-idp:ListUserPoolClients`<br />`cognito-idp:TagResource`<br />`cognito-idp:CreateUserPool` | 

## Outbound campaigns page
<a name="outbound-campaigns-page"></a>


|  Action / Use case  |  Permissions needed  | 
| --- | --- | 
|  View outbound campaigns  | `connect:ListIntegrationAssociations`<br />`connect:ListPhoneNumbersV2`<br />`connect:SearchEmailAddresses`<br />`connect:DescribeInstance`<br />`connect:DescribeInstanceAttribute`<br />`kms:DescribeKey`<br />`kms:ListKeys`<br />`profile:ListAccountIntegrations`<br />`profile:ListIntegrations`<br />`profile:ListDomains`<br />`profile:GetDomain`<br />`wisdom:ListKnowledgeBases`<br />`wisdom:GetKnowledgeBase`<br />`connect-campaigns:GetInstanceOnboardingJobStatus`<br />`connect-campaigns:GetConnectInstanceConfig`<br />`connect-campaigns:ListConnectInstanceIntegrations` | 
|  Create outbound campaigns  | `connect-campaigns:StartInstanceOnboardingJob`<br />`connect-campaigns:DeleteInstanceOnboardingJob`<br />`connect-campaigns:GetConnectInstanceConfig`<br />`connect-campaigns:GetInstanceOnboardingJobStatus`<br />`connect-campaigns:DeleteConnectInstanceConfig`<br />`connect:DescribeInstance`<br />`connect:DescribeInstanceAttribute`<br />`connect:UpdateInstanceAttribute`<br />`iam:CreateServiceLinkedRole`<br />`iam:DeleteServiceLinkedRole`<br />`iam:AttachRolePolicy`<br />`iam:PutRolePolicy`<br />`iam:DeleteRolePolicy`<br />`events:PutRule`<br />`events:PutTargets`<br />`events:DeleteRule`<br />`events:RemoveTargets`<br />`events:DescribeRule`<br />`events:ListTargetsByRule`<br />`ds:DescribeDirectories`<br />`kms:DescribeKey`<br />`kms:ListKeys`<br />`kms:CreateGrant`<br />`kms:RetireGrant`<br />`profile:CreateDomain`<br />`profile:ListAccountIntegrations`<br />`profile:ListIntegrations`<br />`profile:PutIntegration`<br />`profile:PutProfileObjectType`<br />`connect:CreateIntegrationAssociation`<br />`connect:ListIntegrationAssociations`<br />`connect:UpdateInstanceAttribute`<br />`connect:AssociateCustomerProfilesDomain`<br />`connect-campaigns:ListConnectInstanceIntegrations`<br />`connect-campaigns:PutConnectInstanceIntegration`<br />`wisdom:CreateKnowledgeBase`<br />`wisdom:ListKnowledgeBases` | 

## agent assist page
<a name="wisdom-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View domains and integrations | `wisdom:ListAssistantAssociations`<br />`appflow:DescribeConnectorProfiles`<br />`app-integrations:GetDataIntegration`<br />`connect:DescribeInstance`<br />`connect:DescribeInstanceAttribute`<br />`connect:ListIntegrationAssociations`<br />`kms:DescribeKey`<br />`kms:ListGrants`<br />`wisdom:GetAssistant`<br />`wisdom:GetKnowledgeBase`<br />`wisdom:ListAssistantAssociations` | 
| Add or remove domains | `connect:CreateIntegrationAssociation`<br />`connect:DeleteIntegrationAssociation`<br />`connect:ListIntegrationAssociations`<br />`iam:DeleteRolePolicy`<br />`iam:PutRolePolicy`<br />`kms:CreateGrant`<br />`kms:DescribeKey`<br />`kms:ListAliases`<br />`wisdom:CreateAssistant`<br />`wisdom:DeleteAssistant`<br />`wisdom:GetAssistant`<br />`wisdom:ListAssistantAssociations`<br />`wisdom:ListAssistants`<br />`wisdom:TagResource` | 
| Add or remove integrations | `wisdom:ListAssistantAssociations`<br />`app-integrations:CreateDataIntegration`<br />`app-integrations:CreateDataIntegrationAssociation`<br />`app-integrations:DeleteDataIntegrationAssociation`<br />`app-integrations:GetDataIntegration`<br />`app-integrations:ListDataIntegrations`<br />`appflow:CreateConnectorProfile`<br />`appflow:CreateFlow`<br />`appflow:DeleteFlow`<br />`appflow:DescribeConnector`<br />`appflow:DescribeConnectorEntity`<br />`appflow:DescribeConnectorProfiles`<br />`appflow:DescribeConnectors`<br />`appflow:DescribeFlow`<br />`appflow:ListConnectorEntities`<br />`appflow:StartFlow`<br />`appflow:StopFlow`<br />`appflow:TagResource`<br />`appflow:UseConnectorProfile`<br />`connect:CreateIntegrationAssociation`<br />`connect:DeleteIntegrationAssociation`<br />`connect:ListIntegrationAssociations`<br />`iam:DeleteRolePolicy`<br />`iam:PutRolePolicy`<br />`kms:CreateGrant`<br />`kms:Decrypt`<br />`kms:DescribeKey`<br />`kms:GenerateDataKey`<br />`kms:ListAliases`<br />`kms:ListGrants`<br />`secretsmanager:CreateSecret`<br />`secretsmanager:PutResourcePolicy`<br />`wisdom:CreateAssistantAssociation`<br />`wisdom:CreateKnowledgeBase`<br />`wisdom:DeleteAssistantAssociation`<br />`wisdom:DeleteKnowledgeBase`<br />`wisdom:GetAssistant`<br />`wisdom:GetKnowledgeBase`<br />`wisdom:ListAssistantAssociations`<br />`wisdom:ListKnowledgeBases`<br />`wisdom:TagResource` | 

## Voice ID page
<a name="voiceid-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View Voice ID integrations | `voiceid:DescribeDomain`<br />`voiceid:ListDomains`<br />`voiceid:RegisterComplianceConsent`<br />`voiceid:DescribeComplianceConsent`<br />`connect:ListIntegrationAssociations` | 
| Edit Voice ID integrations | `voiceid:DescribeDomain`<br />`voiceid:ListDomains`<br />`voiceid:RegisterComplianceConsent`<br />`voiceid:DescribeComplianceConsent`<br />`voiceid:UpdateDomain`<br />`voiceid:CreateDomain`<br />`connect:ListIntegrationAssociations`<br />`connect:CreateIntegrationAssociation`<br />`connect:DeleteIntegrationAssociation`<br />`events:PutRule`<br />`events:DeleteRule`<br />`events:PutTargets`<br />`events:RemoveTargets`<br />`iam:PutRolePolicy` | 

## Forecasting & agent scheduling page
<a name="forecasting-page"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| View forecasting & agent scheduling | `connect:DescribeForecastingPlanningSchedulingIntegration` | 
| Enable forecasting & agent scheduling | `connect:UpdateInstanceAttribute`<br />`connect:StartForecastingPlanningSchedulingIntegration` | 
| Disable forecasting & agent scheduling | `connect:UpdateInstanceAttribute`<br />`connect:StopForecastingPlanningSchedulingIntegration` | 

## Federations
<a name="federations"></a>

### SAML federation
<a name="saml-federation"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| SAML federation | `connect:GetFederationToken` | 

### Admin/Emergency federation
<a name="admin-emergency-federation"></a>


| Action/Use case | Permissions needed | 
| --- | --- | 
| Admin/Emergency federation | `connect:AdminGetEmergencyAccessToken` | 