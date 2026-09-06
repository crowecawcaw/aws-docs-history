

# AWS managed policies for Connect Customer
<a name="security_iam_awsmanpol"></a>

To add permissions to users, groups, and roles, it is more efficient to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) policies that provide your team with only the permissions that they need. To get started quickly, you can use AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the ReadOnlyAccess AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AmazonConnect\_FullAccess
<a name="AmazonConnect_FullAccess-policy"></a>

To allow full read/write access to Connect Customer, you must attach two policies to your IAM users, groups, or roles. Attach the `AmazonConnect_FullAccess` policy and a custom policy to have full access to Connect Customer.

To view the permissions for the `AmazonConnect_FullAccess` policy, see [AmazonConnect\_FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnect_FullAccess.html) in the *AWS Managed Policy Reference*.

**Custom Policy**

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
+ The custom policy that contains the `iam:PutRolePolicy` action, allows the user with this policy assigned to configure any resource in the account to work with a Connect Customer instance. Since this added action grants such broad permissions, only assign it when necessary. As an alternative, you can create the service-linked role with access to the necessary resources and let the user have access to pass the service-linked role to Connect Customer (which is granted by the `AmazonConnect_FullAccess` policy). 
+ Additional privileges are required to create a Amazon S3 bucket with a name of your choosing, or use an existing bucket while creating or updating an instance from the Connect Customer admin website. If you choose default storage locations for your call recordings, chat transcripts, call transcripts, and other data, the system prepends "amazon-connect-" to the names of those objects.
+ The aws/connect KMS key is available to use as a default encryption option. To use a custom encryption key, assign users additional KMS privileges.
+ Assign users additional privileges to attach other AWS resources like Amazon Polly, Live Media Streaming, Data Streaming, and Lex bots to their Connect Customer instances. 

For more information and detailed permissions, see [Required permissions for using custom IAM policies to manage access to the Connect Customer console](security-iam-amazon-connect-permissions.md). 

## AWS managed policy: AmazonConnectReadOnlyAccess
<a name="amazonconnectreadonlyaccess-policy"></a>

To allow read-only access, you can attach the `AmazonConnectReadOnlyAccess` policy.

To view the permissions for this policy, see [AmazonConnectReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnectReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonConnectServiceLinkedRolePolicy
<a name="amazonconnectservicelinkedrolepolicy"></a>

This policy is attached to the service-linked role named `AWSServiceRoleForAmazonConnect` to allow Connect Customer to perform various actions on specified resources. As you enable additional features in Connect Customer, additional permissions are added for the [AWSServiceRoleForAmazonConnect](https://docs.aws.amazon.com/connect/latest/adminguide/connect-slr.html#slr-permissions) service-linked role to access the resources associated with those features.

To view the permissions for this policy, see [AmazonConnectServiceLinkedRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnectServiceLinkedRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonConnectCampaignsServiceLinkedRolePolicy
<a name="amazonconnectcampaignsservicelinkedrolepolicy"></a>

The `AmazonConnectCampaignsServiceLinkedRolePolicy` role permissions policy allows Connect Customer outbound campaigns to perform various actions on specified resources. As you enable additional features in Connect Customer, additional permissions are added for the [AWSServiceRoleForConnectCampaigns](https://docs.aws.amazon.com/connect/latest/adminguide/connect-slr-outbound.html#slr-permissions-outbound) service-linked role to access the resources associated with those features.

To view the permissions for this policy, see [AmazonConnectCampaignsServiceLinkedRolePolicy ](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnectCampaignsServiceLinkedRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonConnectVoiceIDFullAccess
<a name="amazonconnectvoiceidfullaccesspolicy"></a>

To allow full access to Connect Customer Voice ID, you must attach two policies to your users, groups, or roles. Attach the `AmazonConnectVoiceIDFullAccess` policy and a custom policy to access Voice ID through the Connect Customer admin website.

To view the permissions for the `AmazonConnectVoiceIDFullAccess` policy, see [AmazonConnectVoiceIDFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnectVoiceIDFullAccess.html) in the *AWS Managed Policy Reference*.

**Custom policy**

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
        },
        {
            "Effect": "Allow",
            "Action": [
                "connect:CreateIntegrationAssociation",
                "connect:DeleteIntegrationAssociation",
                "connect:ListIntegrationAssociations"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "events:DeleteRule",
                "events:PutRule",
                "events:PutTargets",
                "events:RemoveTargets"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "events:ManagedBy": "connect.amazonaws.com"
                }
            }
        }
    ] 
}
```

------

The custom policy configures the following:
+ The `iam:PutRolePolicy` allows the user who gets that policy to configure any resource in the account to work with the Connect Customer instance. Due to its broad scope, grant this permission only when absolutely necessary.
+ Attaching a Voice ID domain to an Connect Customer instance requires additional Connect Customer and Amazon EventBridge permissions. You need permissions to call Connect Customer APIs for creating, deleting, and listing integration associations. Additionally, EventBridge permissions are required to create and delete rules that provide contact records related to Voice ID.

Connect Customer Voice ID does not have a default encryption option, so you must allow the following API operations in the key policy to use your customer-managed key. Additionally, you need to grant these permissions on the relevant key, as they are not included in the managed policy.
+ `kms:Decrypt` - to access or store encrypted data.
+ `kms:CreateGrant` – when creating or updating a domain, used to create a grant to the customer managed key for the Voice ID domain. The grant controls access to the specified KMS key which allows access to [grant operations](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-grant-operations) Connect Customer Voice ID requires. For more information about using grants, see [Using grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the *AWS Key Management Service Developer Guide*.
+ `kms:DescribeKey` – when creating or updating a domain, allows determining the ARN for KMS key you provided.

For more about creating domains and KMS keys, see [Get started enabling Voice ID in Connect Customer](enable-voiceid.md) and [Encryption at rest in Connect Customer](encryption-at-rest.md). 

## AWS managed policy: CustomerProfilesServiceLinkedRolePolicy
<a name="customerprofilesservicelinkedrolepolicy"></a>

The `CustomerProfilesServiceLinkedRolePolicy` role permissions policy allows Connect Customer to perform various actions on specified resources. As you enable additional features in Amazon Connect, additional permissions are added for the [AWSServiceRoleForProfile](customerprofiles-slr.md#slr-permissions-customerprofiles) service-linked role to access the resources associated with those features.

To view the permissions for this policy, see [CustomerProfilesServiceLinkedRolePolicy ](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CustomerProfilesServiceLinkedRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonConnectSynchronizationServiceRolePolicy
<a name="amazonconnectsynchronizationservicerolepolicy"></a>

The `AmazonConnectSynchronizationServiceRolePolicy` permissions policy allows Connect Customer Managed Synchronization to perform various actions on specified resources. As resource synchronization is enabled for more resources, additional permissions are added to the [AWSServiceRoleForAmazonConnectSynchronization](managed-synchronization-slr.md#slr-permissions-managed-synchronization) service-linked role to access these resources.

To view the permissions for this policy, see [AmazonConnectSynchronizationServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnectSynchronizationServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Connect Customer updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Connect Customer since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Connect Customer Document history](doc-history.md) page. 




| Change | Description | Date | 
| --- | --- | --- | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Updated actions for Connect Customer Customer Profiles | Updated the Connect Customer Customer Profiles permissions in the service-linked role policy to `profile:*` on all Connect Customer Customer Profiles resources with the `amazon-connect-` domain prefix and template resources, with an explicit deny for the following actions:+  `profile:CreateDomain` <br />+  `profile:UpdateDomain` <br />+  `profile:DeleteDomain` <br />+  `profile:CreateEventStream` <br />+  `profile:DeleteEventStream` <br />+  `profile:DeleteWorkflow` <br />+  `profile:DeleteProfileKey` <br />+  `profile:UntagResource` <br />+  `profile:TagResource` <br />+  `profile:CreateIntegrationWorkflow` <br />Additionally, the following actions are allowed on all resources: `profile:ListRecommenderRecipes`, `profile:ListAccountIntegrations`, and `profile:ListDomains`. | May 20, 2026 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Updated actions for agent assist | Updated the agent assist permissions in the service-linked role policy to `wisdom:*` on all Connect Customer agent assist resources with resource tag `'AmazonConnectEnabled':'True'`, with an explicit deny for the following actions:+  `wisdom:DeleteAssistant` <br />+  `wisdom:DeleteKnowledgeBase`  | May 18, 2026 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for agent assist | Added the following agent assist actions to the service-linked role policy:+  `wisdom:Retrieve` <br />+  `wisdom:ListAssistantAssociations`  | November 18, 2025 | 
|  [AmazonConnectSynchronizationServiceRolePolicy](#amazonconnectsynchronizationservicerolepolicy) – Added actions for Managed Synchronization | Modified the allowed actions by adding batch and import wildcards. The following actions were added:+  `connect:BatchCreate*` <br />+  `connect:BatchUpdate*` <br />+  `connect:BatchDelete*` <br />+  `connect:BatchDescribe*` <br />+  `connect:Import*`  | November 21, 2025 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for AWS End User Messaging Social | Added AWS End User Messaging Social actions to allow the listing of WhatsApp business accounts and the retrieval of a business account's WhatsApp message templates. The following actions were added:+  `social-messaging:ListLinkedWhatsAppBusinessAccounts` <br />+  `social-messaging:GetWhatsAppMessageTemplate` <br />+  `social-messaging:ListWhatsAppMessageTemplates` <br />The AWS End User Messaging Social template APIs are restricted to WhatsApp business accounts that are tagged `AmazonConnectEnabled : True`. | October 20, 2025 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer Customer Profiles | Added the following Connect Customer Customer Profiles actions to the service-linked role policy below the **AllowCustomerProfilesForConnectDomain** Sid. Also, added support for profile UploadJobs on all amazon-connect-\* resources, and not just “upload-jobs” resources:+  `profile:GetUploadJob` <br />+  `profile:GetUploadJobPath` <br />+  `profile:StartUploadJob` <br />+  `profile:StopUploadJob`  | July 25, 2025 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon Polly | Added the following Amazon Polly actions to the service-linked role policy:+  `polly:ListLexicons` <br />+  `polly:DescribeVoices` <br />+  `polly:SynthesizeSpeech`  | July 9, 2025 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer Customer Profiles | Added the following Connect Customer Customer Profiles actions to the service-linked role policy:+  `profile:GetUploadJob` <br />+  `profile:GetUploadJobPath` <br />+  `profile:StartUploadJob` <br />+  `profile:StopUploadJob` <br />+  `profile:CreateUploadJob` <br />+  `profile:ListUploadJobs` <br />+  `profile:DetectProfileObjectType`  | June 30, 2025 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer Customer Profiles | Added the following Customer Profiles actions to the service-linked role policy:+  `profile:CreateDomainLayout` <br />+  `profile:UpdateDomainLayout` <br />+  `profile:DeleteDomainLayout` <br />+  `profile:GetDomainLayout` <br />+  `profile:ListDomainLayouts` <br />+  `profile:GetSimilarProfiles`  | June 9, 2025 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for agent assist, to support messaging | Added the following agent assist actions to the service-linked role policy to support messaging. These actions allow Connect Customer to send, list, and get the next message by using the agent assist API:+  `wisdom:SendMessage` <br />+  `wisdom:GetNextMessage` <br />+  `wisdom:ListMessages`  | March 14, 2025 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for agent assist | Added the following agent assist actions to the service-linked role policy:+  `wisdom:CreateAIAgent` <br />+  `wisdom:CreateAIAgentVersion` <br />+  `wisdom:DeleteAIAgent` <br />+  `wisdom:DeleteAIAgentVersion` <br />+  `wisdom:UpdateAIAgent` <br />+  `wisdom:UpdateAssistantAIAgent` <br />+  `wisdom:RemoveAssistantAIAgent` <br />+  `wisdom:GetAIAgent` <br />+  `wisdom:ListAIAgents` <br />+  `wisdom:ListAIAgentVersions` <br />+  `wisdom:CreateAIPrompt` <br />+  `wisdom:CreateAIPromptVersion` <br />+  `wisdom:DeleteAIPrompt` <br />+  `wisdom:DeleteAIPromptVersion` <br />+  `wisdom:UpdateAIPrompt` <br />+  `wisdom:GetAIPrompt` <br />+  `wisdom:ListAIPrompts` <br />+  `wisdom:ListAIPromptVersions` <br />+  `wisdom:CreateAIGuardrail` <br />+  `wisdom:CreateAIGuardrailVersion` <br />+  `wisdom:DeleteAIGuardrail` <br />+  `wisdom:DeleteAIGuardrailVersion` <br />+  `wisdom:UpdateAIGuardrail` <br />+  `wisdom:GetAIGuardrail` <br />+  `wisdom:ListAIGuardrails` <br />+  `wisdom:ListAIGuardrailVersions` <br />+  `wisdom:CreateAssistant` <br />+  `wisdom:ListTagsForResource`  | December 31, 2024 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added action for Amazon Pinpoint, to support push notifications | Added the following Amazon Pinpoint action to the service-linked role policy to support push notifications. This action allows Connect Customer to send push notifications by using the Amazon Pinpoint API:+  `mobiletargeting:SendMessages`  | December 10, 2024 | 
| [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for integration with AWS End User Messaging Social | Added the following AWS End User Messaging Social actions to the service-linked role policy. The actions allow Connect Customer to invoke these APIs on End User Messaging Social phone numbers that have the `'AmazonConnectEnabled':'True'` resource tag.+  `social-messaging:SendWhatsAppMessage` <br />+  `social-messaging:PostWhatsAppMessageMedia` <br />+  `social-messaging:GetWhatsAppMessageMedia` <br />+  `social-messaging:GetLinkedWhatsAppBusinessAccountPhoneNumber`  | December 2, 2024 | 
| [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon SES, to support the email channel | Added the following Amazon SES actions to the service-linked role policy to support the email channel. These actions allow Connect Customer send, receive, and manage emails by using the Amazon SES APIs:+  `ses:DescribeReceiptRule` <br />+  `ses:UpdateReceiptRule` <br />+  `ses:DeleteEmailIdentity` <br />+  `ses:SendRawEmail` <br />+  `iam:PassRole`  | November 22, 2024 | 
|  [AmazonConnectServiceLinkedRolePolicy](#amazonconnectservicelinkedrolepolicy) – Added Actions for Connect Customer Customer Profiles | Added the following actions to manage Connect Customer Customer Profiles resources:+   `profile:GetIntegration`  <br />+   `profile:PutIntegration`  <br />+   `profile:DeleteIntegration`  <br />+   `profile:CreateEventTrigger`  <br />+   `profile:GetEventTrigger`  <br />+   `profile:ListEventTriggers`  <br />+   `profile:UpdateEventTrigger`  <br />+   `profile:DeleteEventTrigger`   | November 18, 2024 | 
|  [CustomerProfilesServiceLinkedRolePolicy](#customerprofilesservicelinkedrolepolicy) – Added permissions for managing outbound campaigns | Added the following actions to retrieving profile information and triggering a campaign.+  With `connect-campaigns:PutProfileOutboundRequestBatch`, you can trigger a campaign based on your Customer Profiles Event Trigger Definition. <br />+  With `profile:BatchGetProfile`, you can retrieve profile information necessary for triggering an event.  | December 1, 2024 | 
|  [AmazonConnectServiceLinkedRolePolicy](#amazonconnectservicelinkedrolepolicy) – Added Actions for Connect Customer Customer Profiles and Connect Customer agent assist | Added the following actions to manage Connect Customer Customer Profiles resources:+   `profile:ListObjectTypeAttributes`  <br />+   `profile:ListProfileAttributeValues`  <br />+   `profile:BatchGetProfile`  <br />+   `profile:BatchGetCalculatedAttributeForProfile`  <br />+   `profile:ListSegmentDefinitions`  <br />+   `profile:CreateSegmentDefinition`  <br />+   `profile:GetSegmentDefinition`  <br />+   `profile:DeleteSegmentDefinition`  <br />+   `profile:CreateSegmentEstimate`  <br />+   `profile:GetSegmentEstimate`  <br />+   `profile:CreateSegmentSnapshot`  <br />+   `profile:GetSegmentSnapshot`  <br />+   `profile:GetSegmentMembership`  <br />Added the following actions to manage Connect Customer agent assist resources:+   `wisdom:CreateMessageTemplate`  <br />+   `wisdom:UpdateMessageTemplate`  <br />+   `wisdom:UpdateMessageTemplateMetadata`  <br />+   `wisdom:GetMessageTemplate`  <br />+   `wisdom:DeleteMessageTemplate`  <br />+   `wisdom:ListMessageTemplates`  <br />+   `wisdom:SearchMessageTemplates`  <br />+   `wisdom:ActivateMessageTemplate`  <br />+   `wisdom:DeactivateMessageTemplate`  <br />+   `wisdom:CreateMessageTemplateVersion`  <br />+   `wisdom:ListMessageTemplateVersions`  <br />+   `wisdom:CreateMessageTemplateAttachment`  <br />+   `wisdom:DeleteMessageTemplateAttachment`  <br />+   `wisdom:RenderMessageTemplate`   | November 18, 2024 | 
|  [AmazonConnectCampaignsServiceLinkedRolePolicy](#amazonconnectcampaignsservicelinkedrolepolicy) – Added Actions for Connect Customer Customer Profiles and Connect Customer agent assist | Added the following actions to manage Connect Customer resources:+  `connect:StartOutboundVoiceContact` <br />+  `connect:GetMetricData` <br />+  `connect:GetCurrentMetricData` <br />+  `connect:BatchPutContact` <br />+  `connect:StopContact` <br />+  `connect:GetMetricDataV2` <br />+  `connect:DescribeContactFlow` <br />+  `connect:SendOutboundEmail` <br />Added the following actions to manage EventBridge resources:+  `events:DeleteRule` <br />+  `events:PutRule` <br />+  `events:PutTargets` <br />+  `events:RemoveTargets` <br />+  `events:ListRules` <br />+  `events:ListTargetsByRule` <br />Added the following actions to manage Connect Customer agent assist resources:+   `wisdom:GetMessageTemplate`  <br />+   `wisdom:RenderMessageTemplate`   | November 18, 2024 | 
|  [AmazonConnectSynchronizationServiceRolePolicy](#amazonconnectsynchronizationservicerolepolicy) – Consolidated allowed actions and added a deny-list of actions for Managed Synchronization | Modified the allowed actions by using wildcards and added an explicit deny-list of actions. | November 12, 2024 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon Chime SDK Voice Connector | Added the following Amazon Chime SDK Voice Connector actions to the service-linked role policy. These actions allow Connect Customer to obtain Amazon Chime Voice Connector information by using get and list Amazon Chime SDK Voice Connector APIs:+  `chime:GetVoiceConnector`: Allows Connect Customer to invoke the [GetVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnector.html) API on any Amazon Chime SDK Voice Connectors that have an `'AmazonConnectEnabled':'True'` resource tag. <br />+  `chime:ListVoiceConnectors`: Allows Connect Customer to list all Amazon Chime SDK Voice Connectors created in the account across all Regions.  | October 25, 2024 | 
|  [AmazonConnectSynchronizationServiceRolePolicy](#amazonconnectsynchronizationservicerolepolicy) – Added for Managed Synchronization | Added the following actions to the service-linked role managed policy to support the launch of the `HoursOfOperationOverride` attribute.+  `connect:CreateHoursOfOperationOverride` <br />+  `connect:UpdateHoursOfOperationOverride` <br />+  `connect:DeleteHoursOfOperationOverride` <br />+  `connect:DescribeHoursOfOperationOverride` <br />+  `connect:ListHoursOfOperationOverrides`  | September 25, 2024 | 
|  [AmazonConnectSynchronizationServiceRolePolicy](#amazonconnectsynchronizationservicerolepolicy) – Added for Managed Synchronization | Added the following actions to the service-linked role managed policy for managed synchronization:+  `connect:AssociatePhoneNumberContactFlow` <br />+  `connect:DisassociatePhoneNumberContactFlow` <br />+  `connect:AssociateRoutingProfileQueues` <br />+  `connect:DisassociateQueueQuickConnects` <br />+  `connect:AssociateQueueQuickConnects` <br />+  `connect:DisassociateUserProficiencies` <br />+  `connect:AssociateUserProficiencies` <br />+  `connect:DisassociateRoutingProfileQueues` <br />+  `connect:CreateAuthenticationProfile` <br />+  `connect:UpdateAuthenticationProfile` <br />+  `connect:DescribeAuthenticationProfile` <br />+  `connect:ListAuthenticationProfiles`  | July 5, 2024 | 
|  [AmazonConnectReadOnlyAccess](#amazonconnectreadonlyaccess-policy) – Renamed action `connect:GetFederationTokens` and changed to `connect:AdminGetEmergencyAccessToken` | The AmazonConnectReadOnlyAccess managed policy has been updated due to the renaming of the Connect Customer action `connect:GetFederationTokens` to `connect:AdminGetEmergencyAccessToken`. This change is backwards compatible and the `connect:AdminGetEmergencyAccessToken` action will function in the same way as the `connect:GetFederationTokens` action. If you leave the previously named `connect:GetFederationTokens` action in your policies, they will continue to function as expected. | June 15, 2024 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon Cognito user pools and Connect Customer Customer Profiles | Added the following Amazon Cognito user pools actions to the service-linked role policy to allow select read operations on Cognito User Pool User Pool resources that have an `AmazonConnectEnabled` resource tag. This tag is put on the resource when the `CreateIntegrationAssociations` API is called:+  `cognito-idp:DescribeUserPool` <br />+  `cognito-idp:ListUserPoolClients` <br />Added the following Connect Customer Customer Profiles action to the service-linked role policy to allow permissions to put data into the Connect-adjacent service, Customer Profiles:+  profile:PutProfileObject  | May 23, 2024 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for agent assist | The following action is allowed to be performed on agent assist resources that have the resource tag `'AmazonConnectEnabled':'True'` on agent assist Knowledge Base:+  `wisdom:ListContentAssociations`  | May 20, 2024 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon Pinpoint | Added the following actions to the service-linked role policy to use Amazon Pinpoint phone numbers to allow Connect Customer to send SMS:+  `sms:DescribePhoneNumbers` <br />+  `sms:SendTextMessage`  | November 17, 2023 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer agent assist | The following action is allowed to be performed on agent assist resources that have the resource tag `'AmazonConnectEnabled':'True'` on agent assist Knowledge Base:+  `wisdom:PutFeedback`  | November 15, 2023 | 
|  [AmazonConnectCampaignsServiceLinkedRolePolicy](connect-slr-outbound.md#slr-permissions-outbound) – Added actions for Connect Customer | Connect Customer added new actions to retrieve outbound campaigns:+  `connect:BatchPutContact` <br />+  `connect:StopContact`  | November 8, 2023 | 
|  [AmazonConnectSynchronizationServiceRolePolicy](#amazonconnectsynchronizationservicerolepolicy) – Added new AWS managed policy | Added a new service-linked role managed policy for managed synchronization.<br />The policy provides access to read, create, update, and delete Connect Customer resources and is used to automatically synchronize AWS resources across AWS Regions. | November 3, 2023 | 
|  [AmazonConnectServiceLinkedRolePolicy](#amazonconnectservicelinkedrolepolicy) – Added actions for Customer Profiles | Added the following action to manage Connect Customer Customer Profiles Service Linked Roles:+  `profile:ListCalculatedAttributesForProfile` <br />+  `profile:GetDomain` <br />+  `profile:ListIntegrations` <br />+  `profile:CreateCalculatedAttributeDefinition` <br />+  `profile:DeleteCalculatedAttributeDefinition` <br />+  `profile:GetCalculatedAttributeDefinition` <br />+  `profile:UpdateCalculatedAttributeDefinition`  | October 30, 2023 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer agent assist | The following actions are allowed to be performed on agent assist resources that have the resource tag `'AmazonConnectEnabled':'True'` on agent assist Knowledge Base:+  `wisdom:CreateQuickResponse` <br />+  `wisdom:GetQuickResponse` <br />+  `wisdom:SearchQuickResponses` <br />+  `wisdom:StartImportJob` <br />+  `wisdom:GetImportJob` <br />+  `wisdom:ListImportJobs` <br />+  `wisdom:ListQuickResponses` <br />+  `wisdom:UpdateQuickResponse` <br />+  `wisdom:DeleteQuickResponse`  | October 25, 2023 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Customer Profiles | Added the following action to manage Connect Customer Customer Profiles Service Linked Roles:+  `profile:ListCalculatedAttributeDefinitions` <br />+  `profile:GetCalculatedAttributeForProfile`  | October 6, 2023 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer agent assist | The following actions are allowed to be performed on agent assist resources that have the resource tag `'AmazonConnectEnabled':'True'` on agent assist knowledge bases and assistants:+  `wisdom:CreateContent` <br />+  `wisdom:DeleteContent` <br />+  `wisdom:CreateKnowledgeBase` <br />+  `wisdom:GetAssistant` <br />+  `wisdom:GetKnowledgeBase` <br />+  `wisdom:GetContent` <br />+  `wisdom:GetRecommendations` <br />+  `wisdom:GetSession` <br />+  `wisdom:NotifyRecommendationsReceived` <br />+  `wisdom:QueryAssistant` <br />+  `wisdom:StartContentUpload` <br />+  `wisdom:UntagResource` <br />+  `wisdom:TagResource` <br />+  `wisdom:CreateSession` <br />The following `List` actions are allowed to be performed on all agent assist resources:+  `wisdom:ListAssistants` <br />+  `wisdom:KnowledgeBases`  | September 29, 2023 | 
|  [CustomerProfilesServiceLinkedRolePolicy](#customerprofilesservicelinkedrolepolicy) – Added CustomerProfilesServiceLinkedRolePolicy | New managed policy. | March 7, 2023 | 
|  [AmazonConnect\_FullAccess](#AmazonConnect_FullAccess-policy) – Added permission for managing Connect Customer Customer Profiles Service Linked Roles | Added the following action to manage Connect Customer Customer Profiles Service Linked Roles.+  With `iam:CreateServiceLinkedRole`, you can create a service-linked role for Customer Profiles.  | January 26, 2023 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon CloudWatch | Added the following action to publish usage Connect Customer metrics for an instance to your account.+  `cloudwatch:PutMetricData`  | Februrary 22, 2022 | 
|  [AmazonConnect\_FullAccess](#AmazonConnect_FullAccess-policy) – Added permissions for managing Connect Customer Customer Profiles domains | Added all permissions for managing Connect Customer Customer Profiles domains that are created for new Connect Customer instances.+  `profile:ListAccountIntegrations` - Lists all the integrations associated with a specific URI in the AWS account. <br />+  `profile:ListDomains` - Returns a list of all the domains for an AWS account that have been created. <br />+  `profile:GetDomain` - Returns information about a specific domain. <br />+  `profile:ListProfileObjectTypeTemplates` - Allow the Connect Customer console to display a list of templates that you can use to create your data mappings. <br />+  With `profile:GetObjectTypes`, you can view all the current Object Types (data mappings) that you've created. <br />The following permissions are allowed to be performed on domains with a name that is prefixed with `amazon-connect-`:+  With `profile:AddProfileKey`, you can associate a new key value with a specific profile <br />+  With `profile:CreateDomain`, you can create new domains  <br />+  With `profile:CreateProfile`, you can create new profiles <br />+  With `profile:DeleteDomain`, you can delete domains <br />+  With `profile:DeleteIntegration`, you can delete integrations with a domain <br />+  With `profile:DeleteProfile`, you can delete a profile <br />+  With `profile:DeleteProfileKey`, you can delete a profile key <br />+  With `profile:DeleteProfileObject`, you can delete a profile object <br />+  With `profile:DeleteProfileObjectType`, you can delete a profile object type <br />+  With `profile:GetIntegration`, you can retrieve information about an integration <br />+  With `profile:GetMatches`, you can retrieve possible profile matches <br />+  With `profile:GetProfileObjectType`, you can retrieve profile object types <br />+  With `profile:ListIntegrations`, you can list integrations <br />+  With `profile:ListProfileObjects`, you can list profile objects <br />+  With `profile:ListProfileObjectTypes`, you can list profile object types <br />+  With `profile:ListTagsForResource`, you can list tags for a resource <br />+  With `profile:MergeProfiles`, you can merge profile matches <br />+  With `profile:PutIntegration`, you can add an integration between the service and a third-party service which includes Amazon AppFlow and Connect Customer <br />+  With `profile:PutProfileObject`, you can create and update objects <br />+  With `profile:PutProfileObjectType`, you can create and update object types <br />+  With `profile:SearchProfiles`, you can search profiles <br />+  With `profile:TagResource`, you can tag resources <br />+  With `profile:UntagResource`, you can untag resources <br />+  With `profile:UpdateDomain`, you can update domains <br />+  With `profile:UpdateProfile`, you can update profiles  | November 12, 2021 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer Customer Profiles | Added the following actions so Connect Customer flows and the agent experience can interact with the profiles in your default Customer Profiles domain:+  `profile:SearchProfiles` <br />+  `profile:CreateProfile`  <br />+  `profile:UpdateProfile`  <br />+  `profile:AddProfileKey`  <br />Added the following action so Connect Customer flows and the agent experience can interact with the profile objects in your default Customer Profiles domain: +  `profile:ListProfileObjects ` <br />Added the following action so Connect Customer flows and the agent experience can determine whether Customer Profiles is enabled for your Connect Customer instance: +  `profile:ListAccountIntegrations`   | November 12, 2021 | 
|  [AmazonConnectVoiceIDFullAccess](#amazonconnectvoiceidfullaccesspolicy) – Added new AWS managed policy | Added a new AWS managed policy so you can set up your users to use Connect Customer Voice ID.<br />This policy provides full access to Connect Customer Voice ID through the AWS console, SDK, or other means. | September 27, 2021 | 
|  [AmazonConnectCampaignsServiceLinkedRolePolicy](connect-slr-outbound.md#slr-permissions-outbound) – Added new service-linked role policy | Added a new service-linked role policy for outbound campaigns.<br />The policy provides access to retrieve all the outbound campaigns. | September 27, 2021 | 
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon Lex | Added the following actions for the all bots created in the account across all Regions. These actions were added to support integration with Amazon Lex. +  `lex:ListBots` - Lists all the bots available in a given Region for your account.  <br />+  `lex:ListBotAliases` - Lists all the aliases for a given bot.   | June 15, 2021 | 
| [AmazonConnect\_FullAccess](security-iam-amazon-connect-permissions.md) – Added actions for Amazon Lex  | Added the following actions for the all bots created in the account across all Regions. These actions were added to support integration with Amazon Lex. +  `lex:ListBots` <br />+  `lex:ListBotAliases`  | June 15, 2021 | 
| Connect Customer started tracking changes | Connect Customer started tracking changes for its AWS managed policies. | June 15, 2021 | 