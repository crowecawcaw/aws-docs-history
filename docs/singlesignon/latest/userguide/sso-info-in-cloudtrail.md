# IAM Identity Center information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in IAM Identity Center, that activity is recorded in a CloudTrail event along with other AWS service events in
**Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Viewing events with CloudTrail event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

###### Note

For more information about how user identification and tracking of user actions in
CloudTrail events is evolving, refer to [Important changes to CloudTrail events for IAM Identity Center](https://aws.amazon.com/blogs/security/modifications-to-aws-cloudtrail-event-data-of-iam-identity-center/ "https://aws.amazon.com/blogs/security/modifications-to-aws-cloudtrail-event-data-of-iam-identity-center/") in the _AWS Security
Blog_.

For an ongoing record of events in your AWS account, including events for IAM Identity Center,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the log
files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following topics in the _AWS CloudTrail User Guide_:

- [Overview for
  creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon
  SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
  log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
  When CloudTrail logging is enabled in your AWS account, API calls made to IAM Identity Center actions are
  tracked in log files. IAM Identity Center records are written together with other AWS service records in
  a log file. CloudTrail determines when to create and write to a new file based on a time period
  and file size.

###### CloudTrail events for supported IAM Identity Center APIs

The following sections provide information about the CloudTrail events associated with the
following APIs that IAM Identity Center supports:

- [IAM Identity Center
  API](#cloudtrail-events-iam-identity-center-operations "#cloudtrail-events-iam-identity-center-operations")
- [Identity Store
  API](#cloudtrail-events-identity-store-operations "#cloudtrail-events-identity-store-operations")
- [OIDC API](#cloudtrail-events-oidc-operations "#cloudtrail-events-oidc-operations")
- [AWS access portal
  API](#cloudtrail-events-access-portal-operations "#cloudtrail-events-access-portal-operations")
- [SCIM
  API](#cloudtrail-events-scim-api-operations "#cloudtrail-events-scim-api-operations")

## CloudTrail events of IAM Identity Center

API operations

The following list contains the CloudTrail events that the public IAM Identity Center operations emit with
the `sso.amazonaws.com` event source. For more information about
the public IAM Identity Center API operations, see the [IAM Identity Center API Reference](../APIReference/welcome.md "../APIReference/welcome.md").

You might find additional events in CloudTrail for IAM Identity Center console API operations that the
console relies on. For more information about these console APIs, see the [Service Authorization Reference](../../../service-authorization/latest/reference/list_awsiamidentitycenter.md "../../../service-authorization/latest/reference/list_awsiamidentitycenter.md").

- [AttachCustomerManagedPolicyReferenceToPermissionSet](../APIReference/API_AttachCustomerManagedPolicyReferenceToPermissionSet.md "../APIReference/API_AttachCustomerManagedPolicyReferenceToPermissionSet.md")
- [AttachManagedPolicyToPermissionSet](../APIReference/API_AttachManagedPolicyToPermissionSet.md "../APIReference/API_AttachManagedPolicyToPermissionSet.md")
- [CreateAccountAssignment](../APIReference/API_CreateAccountAssignment.md "../APIReference/API_CreateAccountAssignment.md")
- [CreateApplication](../APIReference/API_CreateApplication.md "../APIReference/API_CreateApplication.md")
- [CreateApplicationAssignment](../APIReference/API_CreateApplicationAssignment.md "../APIReference/API_CreateApplicationAssignment.md")
- [CreateInstance](../APIReference/API_CreateInstance.md "../APIReference/API_CreateInstance.md")
- [CreateInstanceAccessControlAttributeConfiguration](../APIReference/API_CreateInstanceAccessControlAttributeConfiguration.md "../APIReference/API_CreateInstanceAccessControlAttributeConfiguration.md")
- [CreatePermissionSet](../APIReference/API_CreatePermissionSet.md "../APIReference/API_CreatePermissionSet.md")
- [CreateTrustedTokenIssuer](../APIReference/API_CreateTrustedTokenIssuer.md "../APIReference/API_CreateTrustedTokenIssuer.md")
- [DeleteAccountAssignment](../APIReference/API_DeleteAccountAssignment.md "../APIReference/API_DeleteAccountAssignment.md")
- [DeleteApplication](../APIReference/API_DeleteApplication.md "../APIReference/API_DeleteApplication.md")
- [DeleteApplicationAccessScope](../APIReference/API_DeleteApplicationAccessScope.md "../APIReference/API_DeleteApplicationAccessScope.md")
- [DeleteApplicationAssignment](../APIReference/API_DeleteApplicationAssignment.md "../APIReference/API_DeleteApplicationAssignment.md")
- [DeleteApplicationAuthenticationMethod](../APIReference/API_DeleteApplicationAuthenticationMethod.md "../APIReference/API_DeleteApplicationAuthenticationMethod.md")
- [DeleteApplicationGrant](../APIReference/API_DeleteApplicationGrant.md "../APIReference/API_DeleteApplicationGrant.md")
- [DeleteInlinePolicyFromPermissionSet](../APIReference/API_DeleteInlinePolicyFromPermissionSet.md "../APIReference/API_DeleteInlinePolicyFromPermissionSet.md")
- [DeleteInstance](../APIReference/API_DeleteInstance.md "../APIReference/API_DeleteInstance.md")
- [DeleteInstanceAccessControlAttributeConfiguration](../APIReference/API_DeleteInstanceAccessControlAttributeConfiguration.md "../APIReference/API_DeleteInstanceAccessControlAttributeConfiguration.md")
- [DeletePermissionsBoundaryFromPermissionSet](../APIReference/API_DeletePermissionsBoundaryFromPermissionSet.md "../APIReference/API_DeletePermissionsBoundaryFromPermissionSet.md")
- [DeletePermissionSet](../APIReference/API_DeletePermissionSet.md "../APIReference/API_DeletePermissionSet.md")
- [DeleteTrustedTokenIssuer](../APIReference/API_DeleteTrustedTokenIssuer.md "../APIReference/API_DeleteTrustedTokenIssuer.md")
- [DescribeAccountAssignmentCreationStatus s](../APIReference/API_DescribeAccountAssignmentCreationStatus.md "../APIReference/API_DescribeAccountAssignmentCreationStatus.md")
- [DescribeAccountAssignmentDeletionStatus](../APIReference/API_DescribeAccountAssignmentDeletionStatus.md "../APIReference/API_DescribeAccountAssignmentDeletionStatus.md")
- [DescribeApplication](../APIReference/API_DescribeApplication.md "../APIReference/API_DescribeApplication.md")
- [DescribeApplicationAssignment](../APIReference/API_DescribeApplicationAssignment.md "../APIReference/API_DescribeApplicationAssignment.md")
- [DescribeApplicationProvider](../APIReference/API_DescribeApplicationProvider.md "../APIReference/API_DescribeApplicationProvider.md")
- [DescribeInstance](../APIReference/API_DescribeInstance.md "../APIReference/API_DescribeInstance.md")
- [DescribeInstanceAccessControlAttributeConfiguration](../APIReference/API_DescribeInstanceAccessControlAttributeConfiguration.md "../APIReference/API_DescribeInstanceAccessControlAttributeConfiguration.md")
- [DescribePermissionSet](../APIReference/API_DescribePermissionSet.md "../APIReference/API_DescribePermissionSet.md")
- [DescribePermissionSetProvisioningStatus](../APIReference/API_DescribePermissionSetProvisioningStatus.md "../APIReference/API_DescribePermissionSetProvisioningStatus.md")
- [DescribeTrustedTokenIssuer](../APIReference/API_DescribeTrustedTokenIssuer.md "../APIReference/API_DescribeTrustedTokenIssuer.md")
- [DetachCustomerManagedPolicyReferenceFromPermissionSet](../APIReference/API_DetachCustomerManagedPolicyReferenceFromPermissionSet.md "../APIReference/API_DetachCustomerManagedPolicyReferenceFromPermissionSet.md")
- [DetachManagedPolicyFromPermissionSet](../APIReference/API_DetachManagedPolicyFromPermissionSet.md "../APIReference/API_DetachManagedPolicyFromPermissionSet.md")
- [GetApplicationAccessScope](../APIReference/API_GetApplicationAccessScope.md "../APIReference/API_GetApplicationAccessScope.md")
- [GetApplicationAssignmentConfiguration](../APIReference/API_GetApplicationAssignmentConfiguration.md "../APIReference/API_GetApplicationAssignmentConfiguration.md")
- [GetApplicationAuthenticationMethod](../APIReference/API_GetApplicationAuthenticationMethod.md "../APIReference/API_GetApplicationAuthenticationMethod.md")
- [GetApplicationGrant](../APIReference/API_GetApplicationGrant.md "../APIReference/API_GetApplicationGrant.md")
- [GetInlinePolicyForPermissionSet](../APIReference/API_GetInlinePolicyForPermissionSet.md "../APIReference/API_GetInlinePolicyForPermissionSet.md")
- [GetPermissionsBoundaryForPermissionSet](../APIReference/API_GetPermissionsBoundaryForPermissionSet.md "../APIReference/API_GetPermissionsBoundaryForPermissionSet.md")
- [ListAccountAssignmentCreationStatus](../APIReference/API_ListAccountAssignmentCreationStatus.md "../APIReference/API_ListAccountAssignmentCreationStatus.md")
- [ListAccountAssignmentDeletionStatus](../APIReference/API_ListAccountAssignmentDeletionStatus.md "../APIReference/API_ListAccountAssignmentDeletionStatus.md")
- [ListAccountAssignments](../APIReference/API_ListAccountAssignments.md "../APIReference/API_ListAccountAssignments.md")
- [ListAccountAssignmentsForPrincipal](../APIReference/API_ListAccountAssignmentsForPrincipal.md "../APIReference/API_ListAccountAssignmentsForPrincipal.md")
- [ListAccountsForProvisionedPermissionSet](../APIReference/API_ListAccountsForProvisionedPermissionSet.md "../APIReference/API_ListAccountsForProvisionedPermissionSet.md")
- [ListApplicationAccessScopes](../APIReference/API_ListApplicationAccessScopes.md "../APIReference/API_ListApplicationAccessScopes.md")
- [ListApplicationAssignments](../APIReference/API_ListApplicationAssignments.md "../APIReference/API_ListApplicationAssignments.md")
- [ListApplicationAssignmentsForPrincipal](../APIReference/API_ListApplicationAssignmentsForPrincipal.md "../APIReference/API_ListApplicationAssignmentsForPrincipal.md")
- [ListApplicationAuthenticationMethods](../APIReference/API_ListApplicationAuthenticationMethods.md "../APIReference/API_ListApplicationAuthenticationMethods.md")
- [ListApplicationGrants](../APIReference/API_ListApplicationGrants.md "../APIReference/API_ListApplicationGrants.md")
- [ListApplicationProviders](../APIReference/API_ListApplicationProviders.md "../APIReference/API_ListApplicationProviders.md")
- [ListApplications](../APIReference/API_ListApplications.md "../APIReference/API_ListApplications.md")
- [ListCustomerManagedPolicyReferencesInPermissionSet](../APIReference/API_ListCustomerManagedPolicyReferencesInPermissionSet.md "../APIReference/API_ListCustomerManagedPolicyReferencesInPermissionSet.md")
- [ListInstances](../APIReference/API_ListInstances.md "../APIReference/API_ListInstances.md")
- [ListManagedPoliciesInPermissionSet](../APIReference/API_ListManagedPoliciesInPermissionSet.md "../APIReference/API_ListManagedPoliciesInPermissionSet.md")
- [ListPermissionSetProvisioningStatus](../APIReference/API_ListPermissionSetProvisioningStatus.md "../APIReference/API_ListPermissionSetProvisioningStatus.md")
- [ListPermissionSets](../APIReference/API_ListPermissionSets.md "../APIReference/API_ListPermissionSets.md")
- [ListPermissionSetsProvisionedToAccount](../APIReference/API_ListPermissionSetsProvisionedToAccount.md "../APIReference/API_ListPermissionSetsProvisionedToAccount.md")
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [ListTrustedTokenIssuers](../APIReference/API_ListTrustedTokenIssuers.md "../APIReference/API_ListTrustedTokenIssuers.md")
- [ProvisionPermissionSet](../APIReference/API_ProvisionPermissionSet.md "../APIReference/API_ProvisionPermissionSet.md")
- [PutApplicationAccessScope](../APIReference/API_PutApplicationAccessScope.md "../APIReference/API_PutApplicationAccessScope.md")
- [PutApplicationAssignmentConfiguration](../APIReference/API_PutApplicationAssignmentConfiguration.md "../APIReference/API_PutApplicationAssignmentConfiguration.md")
- [PutApplicationAuthenticationMethod](../APIReference/API_PutApplicationAuthenticationMethod.md "../APIReference/API_PutApplicationAuthenticationMethod.md")
- [PutApplicationGrant](../APIReference/API_PutApplicationGrant.md "../APIReference/API_PutApplicationGrant.md")
- [PutInlinePolicyToPermissionSet](../APIReference/API_PutInlinePolicyToPermissionSet.md "../APIReference/API_PutInlinePolicyToPermissionSet.md")
- [PutPermissionsBoundaryToPermissionSet](../APIReference/API_PutPermissionsBoundaryToPermissionSet.md "../APIReference/API_PutPermissionsBoundaryToPermissionSet.md")
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
- [UpdateApplication](../APIReference/API_UpdateApplication.md "../APIReference/API_UpdateApplication.md")
- [UpdateInstance](../APIReference/API_UpdateInstance.md "../APIReference/API_UpdateInstance.md")
- [UpdateInstanceAccessControlAttributeConfiguration](../APIReference/API_UpdateInstanceAccessControlAttributeConfiguration.md "../APIReference/API_UpdateInstanceAccessControlAttributeConfiguration.md")
- [UpdatePermissionSet](../APIReference/API_UpdatePermissionSet.md "../APIReference/API_UpdatePermissionSet.md")
- [UpdateTrustedTokenIssuer](../APIReference/API_UpdateTrustedTokenIssuer.md "../APIReference/API_UpdateTrustedTokenIssuer.md")

## CloudTrail events of Identity Store API

operations

The following list contains the CloudTrail events that the public Identity Store operations emit
with the `identitystore.amazonaws.com` event source. For more
information about the public Identity Store API operations, see the [Identity Store API
Reference](../IdentityStoreAPIReference/welcome.md "../IdentityStoreAPIReference/welcome.md").

You might find additional events in CloudTrail for the Identity Store console API operations with
the `sso-directory.amazonaws.com` event source. These APIs
support the console and AWS access portal. If you need to detect the occurrence of a particular
operation, such as adding member to a group, we recommend you consider both public and
console API operations. For more information about these console APIs, see the [Service Authorization Reference](../../../service-authorization/latest/reference/list_awsidentitystore.md "../../../service-authorization/latest/reference/list_awsidentitystore.md").

- [CreateGroup](../IdentityStoreAPIReference/API_CreateGroup.md "../IdentityStoreAPIReference/API_CreateGroup.md")
- [CreateGroupMembership](../IdentityStoreAPIReference/API_CreateGroupMembership.md "../IdentityStoreAPIReference/API_CreateGroupMembership.md")
- [CreateUser](../IdentityStoreAPIReference/API_CreateUser.md "../IdentityStoreAPIReference/API_CreateUser.md")
- [DeleteGroup](../IdentityStoreAPIReference/API_DeleteGroup.md "../IdentityStoreAPIReference/API_DeleteGroup.md")
- [DeleteGroupMembership](../IdentityStoreAPIReference/API_DeleteGroupMembership.md "../IdentityStoreAPIReference/API_DeleteGroupMembership.md")
- [DeleteUser](../IdentityStoreAPIReference/API_DeleteUser.md "../IdentityStoreAPIReference/API_DeleteUser.md")
- [DescribeGroup](../IdentityStoreAPIReference/API_DescribeGroup.md "../IdentityStoreAPIReference/API_DescribeGroup.md")
- [DescribeGroupMembership](../IdentityStoreAPIReference/API_DescribeGroupMembership.md "../IdentityStoreAPIReference/API_DescribeGroupMembership.md")
- [DescribeUser](../IdentityStoreAPIReference/API_DescribeUser.md "../IdentityStoreAPIReference/API_DescribeUser.md")
- [GetGroupId](../IdentityStoreAPIReference/API_GetGroupId.md "../IdentityStoreAPIReference/API_GetGroupId.md")
- [GetGroupMembershipId](../IdentityStoreAPIReference/API_GetGroupMembershipId.md "../IdentityStoreAPIReference/API_GetGroupMembershipId.md")
- [GetUserId](../IdentityStoreAPIReference/API_GetUserId.md "../IdentityStoreAPIReference/API_GetUserId.md")
- [IsMemberInGroups](../IdentityStoreAPIReference/API_IsMemberInGroups.md "../IdentityStoreAPIReference/API_IsMemberInGroups.md")
- [ListGroupMemberships](../IdentityStoreAPIReference/API_ListGroupMemberships.md "../IdentityStoreAPIReference/API_ListGroupMemberships.md")
- [ListGroupMembershipsForMember](../IdentityStoreAPIReference/API_ListGroupMembershipsForMember.md "../IdentityStoreAPIReference/API_ListGroupMembershipsForMember.md")
- [ListGroups](../IdentityStoreAPIReference/API_ListGroups.md "../IdentityStoreAPIReference/API_ListGroups.md")
- [ListUsers](../IdentityStoreAPIReference/API_ListUsers.md "../IdentityStoreAPIReference/API_ListUsers.md")
- [UpdateGroup](../IdentityStoreAPIReference/API_UpdateGroup.md "../IdentityStoreAPIReference/API_UpdateGroup.md")
- [UpdateUser](../IdentityStoreAPIReference/API_UpdateUser.md "../IdentityStoreAPIReference/API_UpdateUser.md")

## CloudTrail events of OIDC API

operations

The following list contains the CloudTrail events that the public OIDC operations emit. For
more information about the public OIDC API operations, see the [OIDC API
Reference](../OIDCAPIReference/Welcome.md "../OIDCAPIReference/Welcome.md").

- [CreateToken](../OIDCAPIReference/API_CreateToken.md "../OIDCAPIReference/API_CreateToken.md") (event source
  `sso.amazonaws.com`)
- [CreateTokenWithIAM](../OIDCAPIReference/API_CreateTokenWithIAM.md "../OIDCAPIReference/API_CreateTokenWithIAM.md") (event source
  `sso-oauth.amazonaws.com`)

## CloudTrail events of AWS access portal

API operations

The following list contains the CloudTrail events that the AWS access portal API operations emit
with the `sso.amazonaws.com` event source. The API operations
noted as being unavailable in the public API support the operations of the AWS access portal.
Using the AWS CLI can lead to the emission of CloudTrail events of both the public AWS access portal API
operations and those that are unavailable in the public API. For more information about
public AWS access portal API operations, see the [AWS access portal API
Reference](../PortalAPIReference/Welcome.md "../PortalAPIReference/Welcome.md").

- Authenticate (Not available in the public API. Provides login to
  the AWS access portal.)
- Federate (Not available in the public API. Provides federation into
  applications.)
- [ListAccountRoles](../PortalAPIReference/API_ListAccountRoles.md "../PortalAPIReference/API_ListAccountRoles.md")
- [ListAccounts](../PortalAPIReference/API_ListAccounts.md "../PortalAPIReference/API_ListAccounts.md")
- ListApplications (Not available in the public API. Provides users’
  assigned resources for display in the AWS access portal.)
- ListProfilesForApplication (Not available in the public API. Provides
  application metadata for display in the AWS access portal.)
- [GetRoleCredentials](../PortalAPIReference/API_GetRoleCredentials.md "../PortalAPIReference/API_GetRoleCredentials.md")
- [Logout](../PortalAPIReference/API_Logout.md "../PortalAPIReference/API_Logout.md")

## CloudTrail events of SCIM

API operations

For information about
public SCIM API operations, see [AWS access portal API
Reference](scim-logging-using-cloudtrail.md "scim-logging-using-cloudtrail.md").

## Identity information in IAM Identity Center CloudTrail

events

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root user or AWS Identity and Access Management (IAM) user
  credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
- Whether the request was made by an IAM Identity Center user. If so, the
  `userId` and
  `identityStoreArn` fields are available in the CloudTrail events
  to identify the IAM Identity Center user who initiated the request. For more information, see [Identifying the user in
  IAM Identity Center user-initiated CloudTrail events](sso-cloudtrail-use-cases.md#user-session-iam-identity-center "sso-cloudtrail-use-cases.md#user-session-iam-identity-center") .

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

###### Note

Currently, IAM Identity Center doesn't emit CloudTrail events for user sign-in to AWS managed web applications (for example, Amazon SageMaker AI Studio)
with the [OIDC API](../OIDCAPIReference/Welcome.md "../OIDCAPIReference/Welcome.md"). These
web applications are a subset of the broader set of [AWS managed applications](awsapps.md "awsapps.md"), which
also include non-web applications such as Amazon Athena SQL and Amazon S3 Access
Grants.
