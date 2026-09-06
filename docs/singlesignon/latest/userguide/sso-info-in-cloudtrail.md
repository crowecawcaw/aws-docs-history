

# IAM Identity Center information in CloudTrail
<a name="sso-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in IAM Identity Center, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

**Note**  
For more information about how user identification and tracking of user actions in CloudTrail events is evolving, refer to [Important changes to CloudTrail events for IAM Identity Center](https://aws.amazon.com/blogs/security/modifications-to-aws-cloudtrail-event-data-of-iam-identity-center/) in the *AWS Security Blog*.

For an ongoing record of events in your AWS account, including events for IAM Identity Center, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following topics in the *AWS CloudTrail User Guide*: 
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

When CloudTrail logging is enabled in your AWS account, API calls made to IAM Identity Center actions are tracked in log files. IAM Identity Center records are written together with other AWS service records in a log file. CloudTrail determines when to create and write to a new file based on a time period and file size.

**CloudTrail events for supported IAM Identity Center APIs**  
The following sections provide information about the CloudTrail events associated with the following APIs that IAM Identity Center supports:
+ [IAM Identity Center API](#cloudtrail-events-iam-identity-center-operations)
+ [Identity Store API](#cloudtrail-events-identity-store-operations)
+ [OIDC API](#cloudtrail-events-oidc-operations)
+ [AWS access portal API](#cloudtrail-events-access-portal-operations)
+ [SCIM API](#cloudtrail-events-scim-api-operations)

## CloudTrail events of IAM Identity Center API operations
<a name="cloudtrail-events-iam-identity-center-operations"></a>

The following list contains the CloudTrail events that the public IAM Identity Center operations emit with the `sso.amazonaws.com` event source. For more information about the public IAM Identity Center API operations, see the [IAM Identity Center API Reference](https://docs.aws.amazon.com/singlesignon/latest/APIReference/welcome.html).

 You might find additional events in CloudTrail for IAM Identity Center console API operations that the console relies on. For more information about these console APIs, see the [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamidentitycenter.html). 


+ [AttachCustomerManagedPolicyReferenceToPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AttachCustomerManagedPolicyReferenceToPermissionSet.html)
+ [ AttachManagedPolicyToPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AttachManagedPolicyToPermissionSet.html) 
+ [ CreateAccountAssignment](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateAccountAssignment.html) 
+ [CreateApplication ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplication.html) 
+ [ CreateApplicationAssignment](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html) 
+ [ CreateInstance ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateInstance.html) 
+ [ CreateInstanceAccessControlAttributeConfiguration ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateInstanceAccessControlAttributeConfiguration.html) 
+ [CreatePermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreatePermissionSet.html) 
+ [CreateTrustedTokenIssuer](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateTrustedTokenIssuer.html) 
+ [DeleteAccountAssignment](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteAccountAssignment.html) 
+  [DeleteApplication](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplication.html)
+ [DeleteApplicationAccessScope](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationAccessScope.html)
+  [DeleteApplicationAssignment](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationAssignment.html)
+ [DeleteApplicationAuthenticationMethod](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationAuthenticationMethod.html)
+ [ DeleteApplicationGrant ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationGrant.html) 
+ [ DeleteInlinePolicyFromPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteInlinePolicyFromPermissionSet.html) 
+ [ DeleteInstance ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteInstance.html)
+ [ DeleteInstanceAccessControlAttributeConfiguration ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteInstanceAccessControlAttributeConfiguration.html)
+ [ DeletePermissionsBoundaryFromPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeletePermissionsBoundaryFromPermissionSet.html)
+ [ DeletePermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeletePermissionSet.html)
+ [ DeleteTrustedTokenIssuer ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteTrustedTokenIssuer.html)
+ [ DescribeAccountAssignmentCreationStatus s](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeAccountAssignmentCreationStatus.html)
+  [ DescribeAccountAssignmentDeletionStatus ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeAccountAssignmentDeletionStatus.html)  
+ [ DescribeApplication ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplication.html) 
+ [ DescribeApplicationAssignment ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplicationAssignment.html)
+ [ DescribeApplicationProvider ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplicationProvider.html)
+ [ DescribeInstance ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstance.html)
+ [ DescribeInstanceAccessControlAttributeConfiguration ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstanceAccessControlAttributeConfiguration.html)
+ [ DescribePermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribePermissionSet.html) 
+ [ DescribePermissionSetProvisioningStatus ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribePermissionSetProvisioningStatus.html)
+ [ DescribeTrustedTokenIssuer ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeTrustedTokenIssuer.html)
+ [ DetachCustomerManagedPolicyReferenceFromPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DetachCustomerManagedPolicyReferenceFromPermissionSet.html)
+ [ DetachManagedPolicyFromPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DetachManagedPolicyFromPermissionSet.html)
+ [ GetApplicationAccessScope ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAccessScope.html) 
+ [ GetApplicationAssignmentConfiguration ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAssignmentConfiguration.html) 
+ [ GetApplicationAuthenticationMethod ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAuthenticationMethod.html) 
+ [ GetApplicationGrant ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationGrant.html) 
+ [ GetInlinePolicyForPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetInlinePolicyForPermissionSet.html) 
+ [ GetPermissionsBoundaryForPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetPermissionsBoundaryForPermissionSet.html) 
+ [ ListAccountAssignmentCreationStatus ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignmentCreationStatus.html)  
+  [ ListAccountAssignmentDeletionStatus ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignmentDeletionStatus.html) 
+  [ ListAccountAssignments ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignments.html)  
+  [ ListAccountAssignmentsForPrincipal ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignmentsForPrincipal.html) 
+ [ ListAccountsForProvisionedPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountsForProvisionedPermissionSet.html) 
+ [ ListApplicationAccessScopes ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAccessScopes.html) 
+  [ ListApplicationAssignments ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAssignments.html) 
+  [ ListApplicationAssignmentsForPrincipal ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAssignmentsForPrincipal.html) 
+  [ ListApplicationAuthenticationMethods ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAuthenticationMethods.html) 
+  [ ListApplicationGrants ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationGrants.html) 
+ [ ListApplicationProviders ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationProviders.html) 
+ [ ListApplications ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplications.html) 
+ [ ListCustomerManagedPolicyReferencesInPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListCustomerManagedPolicyReferencesInPermissionSet.html) 
+ [ ListInstances ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html)  
+ [ ListManagedPoliciesInPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListManagedPoliciesInPermissionSet.html) 
+  [ ListPermissionSetProvisioningStatus ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListPermissionSetProvisioningStatus.html) 
+  [ ListPermissionSets ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListPermissionSets.html) 
+  [ ListPermissionSetsProvisionedToAccount ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListPermissionSetsProvisionedToAccount.html) 
+ [ ListTagsForResource ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListTagsForResource.html)  
+ [ ListTrustedTokenIssuers ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListTrustedTokenIssuers.html) 
+ [ ProvisionPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ProvisionPermissionSet.html) 
+ [ PutApplicationAccessScope ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAccessScope.html) 
+ [ PutApplicationAssignmentConfiguration ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAssignmentConfiguration.html)  
+ [ PutApplicationAuthenticationMethod ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAuthenticationMethod.html) 
+ [ PutApplicationGrant ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationGrant.html) 
+ [ PutInlinePolicyToPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutInlinePolicyToPermissionSet.html) 
+ [ PutPermissionsBoundaryToPermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutPermissionsBoundaryToPermissionSet.html) 
+ [ TagResource ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_TagResource.html)  
+ [ UntagResource ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UntagResource.html) 
+ [ UpdateApplication ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateApplication.html) 
+ [ UpdateInstance ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateInstance.html) 
+ [ UpdateInstanceAccessControlAttributeConfiguration ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateInstanceAccessControlAttributeConfiguration.html) 
+ [ UpdatePermissionSet ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdatePermissionSet.html) 
+ [ UpdateTrustedTokenIssuer ](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateTrustedTokenIssuer.html) 

## CloudTrail events of Identity Store API operations
<a name="cloudtrail-events-identity-store-operations"></a>

The following list contains the CloudTrail events that the public Identity Store operations emit with the `identitystore.amazonaws.com` event source. For more information about the public Identity Store API operations, see the [Identity Store API Reference](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html).

 You might find additional events in CloudTrail for the Identity Store console API operations with the `sso-directory.amazonaws.com` event source. These APIs support the console and AWS access portal. If you need to detect the occurrence of a particular operation, such as adding member to a group, we recommend you consider both public and console API operations. For more information about these console APIs, see the [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentitystore.html). 
+ [CreateGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroup.html)
+ [CreateGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroupMembership.html)
+ [CreateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateUser.html)
+ [DeleteGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroup.html)
+ [DeleteGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroupMembership.html)
+ [DeleteUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteUser.html)
+ [DescribeGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html)
+ [DescribeGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroupMembership.html)
+ [DescribeUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html)
+ [GetGroupId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetGroupId.html)
+ [GetGroupMembershipId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetGroupMembershipId.html)
+ [GetUserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetUserId.html)
+ [IsMemberInGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_IsMemberInGroups.html)
+ [ListGroupMemberships](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMemberships.html)
+ [ListGroupMembershipsForMember](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html)
+ [ListGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroups.html)
+ [ListUsers](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListUsers.html)
+ [UpdateGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateGroup.html)
+ [UpdateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateUser.html)

## CloudTrail events of OIDC API operations
<a name="cloudtrail-events-oidc-operations"></a>

The following list contains the CloudTrail events that the public OIDC operations emit. For more information about the public OIDC API operations, see the [OIDC API Reference](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html).
+ [CreateToken](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html) (event source `sso.amazonaws.com`)
+ [CreateTokenWithIAM](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.html) (event source `sso-oauth.amazonaws.com`)

## CloudTrail events of AWS access portal API operations
<a name="cloudtrail-events-access-portal-operations"></a>

The following list contains the CloudTrail events that the AWS access portal API operations emit with the `sso.amazonaws.com` event source. The API operations noted as being unavailable in the public API support the operations of the AWS access portal. Using the AWS CLI can lead to the emission of CloudTrail events of both the public AWS access portal API operations and those that are unavailable in the public API. For more information about public AWS access portal API operations, see the [AWS access portal API Reference](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/Welcome.html).
+ Authenticate (Not available in the public API. Provides login to the AWS access portal.)
+ Federate (Not available in the public API. Provides federation into applications.)
+  [ListAccountRoles](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_ListAccountRoles.html) 
+  [ListAccounts](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_ListAccounts.html) 
+  ListApplications (Not available in the public API. Provides users’ assigned resources for display in the AWS access portal.) 
+  ListProfilesForApplication (Not available in the public API. Provides application metadata for display in the AWS access portal.) 
+  [GetRoleCredentials](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.html) 
+  [Logout](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_Logout.html) 

## CloudTrail events of SCIM API operations
<a name="cloudtrail-events-scim-api-operations"></a>

For information about public SCIM API operations, see [AWS access portal API Reference](scim-logging-using-cloudtrail.md).

## Identity information in IAM Identity Center CloudTrail events
<a name="identity-info-in-cloudtrail-events"></a>

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root user or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.
+ Whether the request was made by an IAM Identity Center user. If so, the `userId` and `identityStoreArn` fields are available in the CloudTrail events to identify the IAM Identity Center user who initiated the request. For more information, see [Identifying the user in IAM Identity Center user-initiated CloudTrail events](sso-cloudtrail-use-cases.md#user-session-iam-identity-center).

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

**Note**  
Currently, IAM Identity Center doesn't emit CloudTrail events for user sign-in to AWS managed web applications (for example, Amazon SageMaker AI Studio) with the [OIDC API](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html). These web applications are a subset of the broader set of [AWS managed applications](awsapps.md), which also include non-web applications such as Amazon Athena SQL and Amazon S3 Access Grants.