AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Setting up

just-in-time access with Systems Manager

Setting up just-in-time node access with Systems Manager involved multiple steps. First, you
choose the _targets_ where you want to set up just-in-time node
access. Targets consist of AWS Organizations organizational units (OUs) and AWS Regions. By
default, the same targets you chose when setting up the unified Systems Manager console are
selected for just-in-time node access. You can choose to set up just-in-time node access
for all of the same targets, or a subset of the targets you specified when setting up
the unified Systems Manager console. Adding new targets that weren't selected when you set up the
unified Systems Manager console isn't supported.

Next you'll create _approval policies_ to determine when node
connections require manual approval and are automatically approved. Approval policies
are managed by each account in your organization. You can also share a policy from the
delegated administrator account to explicitly deny the automatic approval of connections
to specific nodes.

###### Note

Setting up just-in-time node access doesn't affect existing IAM policies or
preferences you've configured for Session Manager. You must remove permission to the
`StartSession` API action from your IAM policies to ensure that only
just-in-time node access is used when users attempt to connect to your nodes. After
you set up just-in-time node access, we recommend testing your approval policies
with a subset of users and nodes to verify your policies are working as desired
before removing permissions to Session Manager.

###### Authentication support

Note the following details about authentication support used for just-in-time node
access:

- Just-in-time node access doesn't support the Single Sign-On authentication
  type when connecting to Windows Server instances with Remote Desktop.
- Only AWS Security Token Service (AWS STS) `AssumeRole` temporary security credentials
  are supported. For more information, see the following topics in the
  _IAM User Guide_:
- - [Temporary
    security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") + [Comparing AWS STS credentials](../../../IAM/latest/UserGuide/id_credentials_sts-comparison.md "../../../IAM/latest/UserGuide/id_credentials_sts-comparison.md") + [Requesting temporary security credentials](../../../IAM/latest/UserGuide/id_credentials_temp_request.md "../../../IAM/latest/UserGuide/id_credentials_temp_request.md")
    The following IAM policies outline the permissions needed to administer and allow
    users to create just-in-time node access requests to nodes with Systems Manager. After verifying
    you have the required permissions to use just-in-time node access with Systems Manager, you can
    continue the setting up process. Replace each `example resource
 placeholder` with your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QuickSetupConfigurationManagers",
 "Effect": "Allow",
 "Action": [
 "ssm-quicksetup:CreateConfigurationManager",
 "ssm-quicksetup:DeleteConfigurationManager",
 "ssm-quicksetup:GetConfiguration",
 "ssm-quicksetup:GetConfigurationManager",
 "ssm-quicksetup:GetServiceSettings",
 "ssm-quicksetup:ListConfigurationManagers",
 "ssm-quicksetup:ListConfigurations",
 "ssm-quicksetup:ListQuickSetupTypes",
 "ssm-quicksetup:ListTagsForResource",
 "ssm-quicksetup:TagResource",
 "ssm-quicksetup:UntagResource",
 "ssm-quicksetup:UpdateConfigurationDefinition",
 "ssm-quicksetup:UpdateConfigurationManager",
 "ssm-quicksetup:UpdateServiceSettings"
 ],
 "Resource": "*"
 },
 {
 "Sid": "QuickSetupDeployments",
 "Effect": "Allow",
 "Action": [
 "cloudformation:DescribeStackSetOperation",
 "cloudformation:ListStacks",
 "cloudformation:DescribeStacks",
 "cloudformation:DescribeStackResources",
 "cloudformation:ListStackSetOperations",
 "cloudformation:ListStackInstances",
 "cloudformation:DescribeStackSet",
 "cloudformation:ListStackSets",
 "cloudformation:DescribeStackInstance",
 "cloudformation:DescribeOrganizationsAccess",
 "cloudformation:ActivateOrganizationsAccess",
 "cloudformation:GetTemplate",
 "cloudformation:ListStackSetOperationResults",
 "cloudformation:DescribeStackEvents",
 "cloudformation:UntagResource",
 "ssm:DescribeAutomationExecutions",
 "ssm:GetAutomationExecution",
 "ssm:ListAssociations",
 "ssm:DescribeAssociation",
 "ssm:GetDocument",
 "ssm:ListDocuments",
 "ssm:DescribeDocument",
 "ssm:GetOpsSummary",
 "organizations:DeregisterDelegatedAdministrator",
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListRoots",
 "organizations:ListParents",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:DescribeOrganizationalUnit",
 "organizations:ListAWSServiceAccessForOrganization",
 "iam:ListRoles",
 "iam:ListRolePolicies",
 "iam:GetRole",
 "iam:CreatePolicy",
 "cloudformation:TagResource"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:RollbackStack",
 "cloudformation:CreateStack",
 "cloudformation:UpdateStack",
 "cloudformation:DeleteStack"
 ],
 "Resource": [
 "arn:aws:cloudformation:*:*:stack/StackSet-AWS-QuickSetup-JITNA*",
 "arn:aws:cloudformation:*:*:stack/AWS-QuickSetup-*",
 "arn:aws:cloudformation:*:*:type/resource/*",
 "arn:aws:cloudformation:*:*:stack/StackSet-SSMQuickSetup"
 ]
 },
 {
 "Sid": "StackSetOperations",
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStackSet",
 "cloudformation:UpdateStackSet",
 "cloudformation:DeleteStackSet",
 "cloudformation:DeleteStackInstances",
 "cloudformation:CreateStackInstances",
 "cloudformation:StopStackSetOperation"
 ],
 "Resource": [
 "arn:aws:cloudformation:*:*:stackset/AWS-QuickSetup-JITNA*",
 "arn:aws:cloudformation:*:*:type/resource/*",
 "arn:aws:cloudformation:*:*:stackset-target/AWS-QuickSetup-JITNA*:*"
 ]
 },
 {
 "Sid": "IamRolesMgmt",
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:DeleteRole",
 "iam:GetRole",
 "iam:AttachRolePolicy",
 "iam:PutRolePolicy",
 "iam:DetachRolePolicy",
 "iam:GetRolePolicy",
 "iam:ListRolePolicies"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AWS-QuickSetup-JITNA*",
 "arn:aws:iam::*:role/service-role/AWS-QuickSetup-JITNA*"
 ]
 },
 {
 "Sid": "IamPassRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AWS-QuickSetup-JITNA*",
 "arn:aws:iam::*:role/service-role/AWS-QuickSetup-JITNA*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "ssm.amazonaws.com",
 "ssm-quicksetup.amazonaws.com",
 "cloudformation.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "SSMAutomationExecution",
 "Effect": "Allow",
 "Action": "ssm:StartAutomationExecution",
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:automation-definition/AWS-EnableExplorer:*"
 },
 {
 "Sid": "SSMAssociationPermissions",
 "Effect": "Allow",
 "Action": [
 "ssm:DeleteAssociation",
 "ssm:CreateAssociation",
 "ssm:StartAssociationsOnce"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:association/*"
 },
 {
 "Sid": "SSMResourceDataSync",
 "Effect": "Allow",
 "Action": [
 "ssm:CreateResourceDataSync",
 "ssm:UpdateResourceDataSync"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:resource-data-sync/AWS-QuickSetup-*"
 },
 {
 "Sid": "ListResourceDataSync",
 "Effect": "Allow",
 "Action": [
 "ssm:ListResourceDataSync"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CreateServiceLinkedRoles",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "accountdiscovery.ssm.amazonaws.com",
 "ssm.amazonaws.com",
 "ssm-quicksetup.amazonaws.com",
 "stacksets.cloudformation.amazonaws.com"
 ]
 }
 },
 "Resource": "*"
 },
 {
 "Sid": "CreateStackSetsServiceLinkedRole",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/stacksets.cloudformation.amazonaws.com/AWSServiceRoleForCloudFormationStackSetsOrgAdmin"
 },
 {
 "Sid": "AllowSsmJitnaPoliciesCrudOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:CreateDocument",
 "ssm:UpdateDocument",
 "ssm:UpdateDocumentDefaultVersion",
 "ssm:GetDocument",
 "ssm:DescribeDocument",
 "ssm:DeleteDocument"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-JustInTimeAccessDenyAccessOrgPolicy"
 ],
 "Condition": {
 "StringEquals": {
 "ssm:DocumentType": [
 "AutoApprovalPolicy"
 ]
 }
 }
 },
 {
 "Sid": "AllowAccessRequestOpsItemOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsItem",
 "ssm:DescribeOpsItems",
 "ssm:GetOpsSummary",
 "ssm:DeleteOpsItem",
 "ssm:ListOpsItemEvents"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IdentityCenterPermissions",
 "Effect": "Allow",
 "Action": [
 "sso:DescribeRegisteredRegions",
 "sso:ListDirectoryAssociations",
 "identitystore:GetUserId",
 "identitystore:DescribeUser",
 "identitystore:DescribeGroup",
 "identitystore:ListGroupMembershipsForMember"
 ],
 "Resource": "*"
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSsmJitnaPoliciesCrudOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:CreateDocument",
 "ssm:UpdateDocument",
 "ssm:UpdateDocumentDefaultVersion",
 "ssm:GetDocument",
 "ssm:DescribeDocument",
 "ssm:DeleteDocument"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/*"
 ],
 "Condition": {
 "StringEquals": {
 "ssm:DocumentType": [
 "ManualApprovalPolicy",
 "AutoApprovalPolicy"
 ]
 }
 }
 },
 {
 "Sid": "AllowSsmJitnaPoliciesListOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:ListDocuments",
 "ssm:ListDocumentVersions"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/SSM-JustInTimeAccessTokenRole",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "justintimeaccess.ssm.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AllowAccessRequestOpsItemOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsItem",
 "ssm:DescribeOpsItems",
 "ssm:GetOpsSummary",
 "ssm:DeleteOpsItem",
 "ssm:ListOpsItemEvents"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSessionManagerPreferencesOperation",
 "Effect": "Allow",
 "Action": [
 "ssm:CreateDocument",
 "ssm:GetDocument",
 "ssm:DescribeDocument",
 "ssm:UpdateDocument",
 "ssm:DeleteDocument"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-SessionManagerRunShell",
 "Condition": {
 "StringEquals": {
 "ssm:DocumentType": "Session"
 }
 }
 },
 {
 "Sid": "AllowSessionManagerOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeSessions",
 "ssm:GetConnectionStatus",
 "ssm:TerminateSession"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowRDPConnectionRecordingOperations",
 "Effect": "Allow",
 "Action": [
 "ssm-guiconnect:UpdateConnectionRecordingPreferences",
 "ssm-guiconnect:GetConnectionRecordingPreferences",
 "ssm-guiconnect:DeleteConnectionRecordingPreferences"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowRDPConnectionRecordingKmsOperation",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/SystemsManagerJustInTimeNodeAccessManaged": "true"
 },
 "StringLike": {
 "kms:ViaService": "ssm-guiconnect.*.amazonaws.com"
 },
 "Bool": {
 "aws:ViaAWSService": "true"
 }
 }
 },
 {
 "Sid": "AllowFleetManagerOperations",
 "Effect": "Allow",
 "Action": [
 "ssm-guiconnect:GetConnection",
 "ssm-guiconnect:ListConnections"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SNSTopicManagement",
 "Effect": "Allow",
 "Action": [
 "sns:CreateTopic",
 "sns:SetTopicAttributes"
 ],
 "Resource": [
 "arn:aws:sns:`us-east-1`:`111122223333`:SSM-JITNA*"
 ]
 },
 {
 "Sid": "SNSListTopics",
 "Effect": "Allow",
 "Action": [
 "sns:ListTopics"
 ],
 "Resource": "*"
 },
 {
 "Sid": "EventBridgeRuleManagement",
 "Effect": "Allow",
 "Action": [
 "events:PutRule",
 "events:PutTargets"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`::rule/SSM-JITNA*"
 ]
 },
 {
 "Sid": "ChatbotSlackManagement",
 "Effect": "Allow",
 "Action": [
 "chatbot:CreateSlackChannelConfiguration",
 "chatbot:UpdateSlackChannelConfiguration",
 "chatbot:DescribeSlackChannelConfigurations",
 "chatbot:DescribeSlackWorkspaces",
 "chatbot:DeleteSlackChannelConfiguration",
 "chatbot:RedeemSlackOauthCode",
 "chatbot:DeleteSlackWorkspaceAuthorization",
 "chatbot:GetSlackOauthParameters"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ChatbotTeamsManagement",
 "Effect": "Allow",
 "Action": [
 "chatbot:ListMicrosoftTeamsChannelConfigurations",
 "chatbot:CreateMicrosoftTeamsChannelConfiguration",
 "chatbot:UpdateMicrosoftTeamsChannelConfiguration",
 "chatbot:ListMicrosoftTeamsConfiguredTeams",
 "chatbot:DeleteMicrosoftTeamsChannelConfiguration",
 "chatbot:RedeemMicrosoftTeamsOauthCode",
 "chatbot:DeleteMicrosoftTeamsConfiguredTeam",
 "chatbot:GetMicrosoftTeamsOauthParameters",
 "chatbot:TagResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SSMEmailSettings",
 "Effect": "Allow",
 "Action": [
 "ssm:UpdateServiceSetting",
 "ssm:GetServiceSetting"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:servicesetting/ssm/access-request/email-role-mapping",
 "arn:aws:ssm:`us-east-1`:`111122223333`:servicesetting/ssm/access-request/enabled-email-notifications"
 ]
 },
 {
 "Sid": "AllowViewingJitnaCloudWatchMetrics",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/SSM/JustInTimeAccess"
 }
 }
 },
 {
 "Sid": "QuickSetupConfigurationManagers",
 "Effect": "Allow",
 "Action": [
 "ssm-quicksetup:ListConfigurationManagers",
 "ssm-quicksetup:ListConfigurations",
 "ssm-quicksetup:ListQuickSetupTypes",
 "ssm-quicksetup:GetConfiguration",
 "ssm-quicksetup:GetConfigurationManager"
 ],
 "Resource": "*"
 },
 {
 "Sid": "QuickSetupDeployments",
 "Effect": "Allow",
 "Action": [
 "cloudformation:ListStacks",
 "cloudformation:DescribeStacks",
 "organizations:DescribeOrganization",
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ManualPolicy",
 "Effect": "Allow",
 "Action": [
 "sso:DescribeRegisteredRegions",
 "ssm:GetServiceSetting",
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SessionPreference",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowIamListForKMS",
 "Effect": "Allow",
 "Action": [
 "iam:ListUsers"
 ],
 "Resource": "arn:aws:iam::`111122223333`:user/*"
 },
 {
 "Sid": "KMSPermission",
 "Effect": "Allow",
 "Action": [
 "kms:TagResource",
 "kms:ListAliases",
 "kms:CreateAlias"
 ],
 "Resource": "*"
 },
 {
 "Sid": "KMSCreateKey",
 "Effect": "Allow",
 "Action": [
 "kms:CreateKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/SystemsManagerJustInTimeNodeAccessManaged": "true"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "SystemsManagerJustInTimeNodeAccessManaged"
 ]
 }
 }
 },
 {
 "Sid": "AllowIamRoleForChatbotAction",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/`role name`",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "chatbot.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AllowIamServiceRoleForChat",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/management.chatbot.amazonaws.com/AWSServiceRoleForAWSChatbot"
 },
 {
 "Sid": "CloudWatchLogs",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": "arn:aws:logs:*:`111122223333`:log-group::log-stream:"
 },
 {
 "Sid": "IdentityStorePermissions",
 "Effect": "Allow",
 "Action": [
 "sso:ListDirectoryAssociations",
 "identitystore:GetUserId",
 "sso-directory:SearchUsers",
 "sso-directory:SearchGroups",
 "identitystore:DescribeGroup",
 "identitystore:DescribeUser"
 ],
 "Resource": "*"
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAccessRequestDescriptions",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeOpsItems",
 "ssm:GetOpsSummary",
 "ssm:ListOpsItemEvents"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowGetSpecificAccessRequest",
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsItem"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:opsitem/*"
 },
 {
 "Sid": "AllowApprovalRejectionSignal",
 "Effect": "Allow",
 "Action": [
 "ssm:SendAutomationSignal"
 ],
 "Resource": "arn:aws:ssm:*:*:automation-execution/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/SystemsManagerJustInTimeNodeAccessManaged": "true"
 }
 }
 },
 {
 "Sid": "QuickSetupConfigurationManagers",
 "Effect": "Allow",
 "Action": [
 "ssm-quicksetup:ListConfigurationManagers",
 "ssm-quicksetup:ListConfigurations",
 "ssm-quicksetup:GetConfigurationManager",
 "ssm-quicksetup:ListQuickSetupTypes",
 "ssm-quicksetup:GetConfiguration"
 ],
 "Resource": "*"
 },
 {
 "Sid": "QuickSetupDeployments",
 "Effect": "Allow",
 "Action": [
 "cloudformation:ListStacks",
 "cloudformation:DescribeStacks",
 "organizations:DescribeOrganization",
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSsmJitnaPoliciesCrudOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:GetDocument",
 "ssm:DescribeDocument"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/*"
 ],
 "Condition": {
 "StringEquals": {
 "ssm:DocumentType": [
 "ManualApprovalPolicy",
 "AutoApprovalPolicy"
 ]
 }
 }
 },
 {
 "Sid": "AllowSsmJitnaPoliciesListOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:ListDocuments",
 "ssm:ListDocumentVersions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IDCPermissions",
 "Effect": "Allow",
 "Action": [
 "sso:DescribeRegisteredRegions",
 "sso:ListDirectoryAssociations",
 "identitystore:GetUserId",
 "identitystore:DescribeUser",
 "identitystore:DescribeGroup",
 "identitystore:ListGroupMembershipsForMember"
 ],
 "Resource": "*"
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowJITNAOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:StartAccessRequest",
 "ssm:GetAccessToken"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowOpsItemCreationAndRetrieval",
 "Effect": "Allow",
 "Action": [
 "ssm:CreateOpsItem",
 "ssm:GetOpsItem"
 ],
 "Resource": "arn:aws:ssm:*:*:opsitem/*"
 },
 {
 "Sid": "AllowListAccessRequests",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeOpsItems",
 "ssm:GetOpsSummary",
 "ssm:ListOpsItemEvents",
 "ssm:DescribeSessions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "RequestManualApprovals",
 "Action": "ssm:StartAutomationExecution",
 "Effect": "Allow",
 "Resource": "arn:aws:ssm:*:*:document/*",
 "Condition": {
 "StringEquals": {
 "ssm:DocumentType": "ManualApprovalPolicy"
 }
 }
 },
 {
 "Sid": "StartManualApprovalsAutomationExecution",
 "Effect": "Allow",
 "Action": "ssm:StartAutomationExecution",
 "Resource": "arn:aws:ssm:*:*:automation-execution/*"
 },
 {
 "Sid": "CancelAccessRequestManualApproval",
 "Effect": "Allow",
 "Action": "ssm:StopAutomationExecution",
 "Resource": "arn:aws:ssm:*:*:automation-execution/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/SystemsManagerJustInTimeNodeAccessManaged": "true"
 }
 }
 },
 {
 "Sid": "DescribeEC2Instances",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeTags",
 "ec2:GetPasswordData"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowListSSMManagedNodesAndTags",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeInstanceInformation",
 "ssm:ListTagsForResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "QuickSetupConfigurationManagers",
 "Effect": "Allow",
 "Action": [
 "ssm-quicksetup:ListConfigurationManagers",
 "ssm-quicksetup:GetConfigurationManager",
 "ssm-quicksetup:ListConfigurations",
 "ssm-quicksetup:ListQuickSetupTypes",
 "ssm-quicksetup:GetConfiguration"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSessionManagerOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeSessions",
 "ssm:GetConnectionStatus"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowRDPOperations",
 "Effect": "Allow",
 "Action": [
 "ssm-guiconnect:ListConnections",
 "ssm:GetConnectionStatus"
 ],
 "Resource": "*"
 },
 {
 "Sid": "QuickSetupDeployments",
 "Effect": "Allow",
 "Action": [
 "cloudformation:ListStacks",
 "cloudformation:DescribeStacks",
 "organizations:DescribeOrganization",
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSsmJitnaPoliciesReadOnly",
 "Effect": "Allow",
 "Action": [
 "ssm:GetDocument",
 "ssm:DescribeDocument"
 ],
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:document/*"
 ],
 "Condition": {
 "StringEquals": {
 "ssm:DocumentType": [
 "ManualApprovalPolicy",
 "AutoApprovalPolicy"
 ]
 }
 }
 },
 {
 "Sid": "AllowSsmJitnaPoliciesListOperations",
 "Effect": "Allow",
 "Action": [
 "ssm:ListDocuments",
 "ssm:ListDocumentVersions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ExploreNodes",
 "Effect": "Allow",
 "Action": [
 "ssm:ListNodesSummary",
 "ssm:ListNodes",
 "ssm:DescribeInstanceProperties"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IdentityStorePermissions",
 "Effect": "Allow",
 "Action": [
 "sso:DescribeRegisteredRegions",
 "sso:ListDirectoryAssociations",
 "identitystore:GetUserId",
 "identitystore:DescribeUser",
 "identitystore:DescribeGroup"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

To restrict access to API operations that create, update, or delete approval
policies, use the `ssm:DocumentType` condition key for the
`AutoApprovalPolicy` and `ManualApprovalPolicy` document
types. The `StartAccessRequest` and `GetAccessToken` API
operations don't support the following global context keys:

- `aws:SourceVpc`
- `aws:SourceVpce`
- `aws:VpcSourceIp`
- `aws:UserAgent`
- `aws:MultiFactorAuthPresent`
  For more information about condition context keys for Systems Manager, see [Condition keys for AWS Systems Manager](../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-policy-keys "../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-policy-keys") in the _Service Authorization
  Reference_.

The following procedure describes how to complete the first set up step for
just-in-time node access.

###### To set up just-in-time node access

1. Log in to the Systems Manager delegated administrator account for your
   organization.
2. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
3. Select **Just-in-time node access** in the navigation
   pane.
4. Select **Enable the new experience**.
5. Choose the Regions where you want to enable just-in-time node access. By
   default, the same Regions you chose when setting up the unified Systems Manager console
   are selected for just-in-time node access. Choosing new Regions that weren't
   selected when you set up the unified Systems Manager console isn't supported.
6. Select **Enable just-in-time node access**.
   There is no charge to use just-in-time node access for 30 days after enabling the
   feature. After the 30 day trial period, there is a charge to use just-in-time node
   access. For more information, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").
