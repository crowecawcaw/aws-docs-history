

# Data retrieval APIs for Amazon WorkMail
<a name="amazonworkmail"></a>

Amazon WorkMail provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="workmail-DescribeEmailMonitoringConfiguration"></a>[DescribeEmailMonitoringConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeEmailMonitoringConfiguration.html) | Retrieve the email monitoring configuration for an organization | Read | 
| <a name="workmail-DescribeEntity"></a>[DescribeEntity](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeEntity.html) | Read details of an entity | Read | 
| <a name="workmail-DescribeGroup"></a>[DescribeGroup](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeGroup.html) | Read the details for a group | List | 
| <a name="workmail-DescribeIdentityProviderConfiguration"></a>[DescribeIdentityProviderConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeIdentityProviderConfiguration.html) | Read the identity provider configuration for the organization | Read | 
| <a name="workmail-DescribeInboundDmarcSettings"></a>[DescribeInboundDmarcSettings](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeInboundDmarcSettings.html) | Read the settings in a DMARC policy for a specified organization | Read | 
| <a name="workmail-DescribeInboundMailFlowRule"></a>[DescribeInboundMailFlowRule](https://docs.aws.amazon.com/workmail/latest/adminguide/email-flows.html#email-flows-rule-actions) | Read the details of an inbound mail flow rule configured for an organization | Read | 
| <a name="workmail-DescribeMailDomains"></a>[DescribeMailDomains](https://docs.aws.amazon.com/workmail/latest/adminguide/domains_overview.html) | Show the details of all mail domains associated with the organization | List | 
| <a name="workmail-DescribeMailboxExportJob"></a>[DescribeMailboxExportJob](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeMailboxExportJob.html) | Retrieve details of a mailbox export job | Read | 
| <a name="workmail-DescribeOrganization"></a>[DescribeOrganization](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeOrganization.html) | Read details of an organization | List | 
| <a name="workmail-DescribeOutboundMailFlowRule"></a>[DescribeOutboundMailFlowRule](https://docs.aws.amazon.com/workmail/latest/adminguide/email-flows.html#email-flows-rule-outbound) | Read the details of an outbound mail flow rule configured for an organization | Read | 
| <a name="workmail-DescribeResource"></a>[DescribeResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeResource.html) | Read the details for a resource | List | 
| <a name="workmail-DescribeSmtpGateway"></a>[DescribeSmtpGateway](https://docs.aws.amazon.com/workmail/latest/adminguide/smtp-gateway.html) | Read the details of an SMTP gateway registered to an organization | Read | 
| <a name="workmail-DescribeUser"></a>[DescribeUser](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeUser.html) | Read details for a user | List | 
| <a name="workmail-GetAccessControlEffect"></a>[GetAccessControlEffect](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetAccessControlEffect.html) | Get the effects of access control rules as they apply to a specified IPv4 address, access protocol action, or user ID | Read | 
| <a name="workmail-GetDefaultRetentionPolicy"></a>[GetDefaultRetentionPolicy](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetDefaultRetentionPolicy.html) | Retrieve the retention policy associated at an organizational level | Read | 
| <a name="workmail-GetImpersonationRole"></a>[GetImpersonationRole](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetImpersonationRole.html) | Retrieve an impersonation role for the given Amazon WorkMail organization | Read | 
| <a name="workmail-GetImpersonationRoleEffect"></a>[GetImpersonationRoleEffect](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetImpersonationRoleEffect.html) | Get the effect of the rules associated to an impersonation role for a specific user | Read | 
| <a name="workmail-GetJournalingRules"></a>[GetJournalingRules](https://docs.aws.amazon.com/workmail/latest/adminguide/journaling_overview.html) | Read the configured journaling and fallback email addresses for email journaling | Read | 
| <a name="workmail-GetMailDomain"></a>[GetMailDomain](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMailDomain.html) | Retrieve details of a given mail domain in an organization | Read | 
| <a name="workmail-GetMailDomainDetails"></a>[GetMailDomainDetails](https://docs.aws.amazon.com/workmail/latest/adminguide/domains_overview.html) | Get the details of the mail domain | Read | 
| <a name="workmail-GetMailboxDetails"></a>[GetMailboxDetails](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMailboxDetails.html) | Read the details of the user's mailbox | Read | 
| <a name="workmail-GetMobileDeviceAccessEffect"></a>[GetMobileDeviceAccessEffect](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMobileDeviceAccessEffect.html) | Simulate the effect of the mobile device access rules for the given attributes of a sample access event | Read | 
| <a name="workmail-GetMobileDeviceAccessOverride"></a>[GetMobileDeviceAccessOverride](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMobileDeviceAccessOverride.html) | Retrieve a mobile device access override | Read | 
| <a name="workmail-GetMobileDeviceDetails"></a>[GetMobileDeviceDetails](https://docs.aws.amazon.com/workmail/latest/adminguide/manage-devices.html) | Get the details of the mobile device | Read | 
| <a name="workmail-GetMobileDevicesForUser"></a>[GetMobileDevicesForUser](https://docs.aws.amazon.com/workmail/latest/adminguide/manage-devices.html) | Get a list of the mobile devices associated with the user | Read | 
| <a name="workmail-GetMobilePolicyDetails"></a>[GetMobilePolicyDetails](https://docs.aws.amazon.com/workmail/latest/adminguide/edit_organization_mobile_policy.html) | Get the details of the mobile device policy associated with the organization | Read | 
| <a name="workmail-GetPersonalAccessTokenMetadata"></a>[GetPersonalAccessTokenMetadata](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetPersonalAccessTokenMetadata.html) | Read metadata for a personal access token | Read | 
| <a name="workmail-ListAccessControlRules"></a>[ListAccessControlRules](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListAccessControlRules.html) | List the access control rules | Read | 
| <a name="workmail-ListAliases"></a>[ListAliases](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListAliases.html) | List the aliases associated with a given entity | List | 
| <a name="workmail-ListAvailabilityConfigurations"></a>[ListAvailabilityConfigurations](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListAvailabilityConfigurations.html) | List all the AvailabilityConfiguration's for the given Amazon WorkMail organization | Read | 
| <a name="workmail-ListGroupMembers"></a>[ListGroupMembers](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListGroupMembers.html) | Read an overview of the members of a group. Users and groups can be members of a group | List | 
| <a name="workmail-ListGroups"></a>[ListGroups](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListGroups.html) | List summaries of the organization's groups | List | 
| <a name="workmail-ListGroupsForEntity"></a>[ListGroupsForEntity](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListGroupsForEntity.html) | List the groups to which an entity belongs | List | 
| <a name="workmail-ListImpersonationRoles"></a>[ListImpersonationRoles](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListImpersonationRoles.html) | List the impersonation roles for the given Amazon WorkMail organization | List | 
| <a name="workmail-ListInboundMailFlowRules"></a>[ListInboundMailFlowRules](https://docs.aws.amazon.com/workmail/latest/adminguide/email-flows.html#email-flows-rule-actions) | List inbound mail flow rules configured for an organization | List | 
| <a name="workmail-ListMailDomains"></a>[ListMailDomains](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMailDomains.html) | List the mail domains for a given organization | List | 
| <a name="workmail-ListMailboxExportJobs"></a>[ListMailboxExportJobs](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMailboxExportJobs.html) | List mailbox export jobs | List | 
| <a name="workmail-ListMailboxPermissions"></a>[ListMailboxPermissions](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMailboxPermissions.html) | List the mailbox permissions associated with a user, group, or resource mailbox | List | 
| <a name="workmail-ListMobileDeviceAccessOverrides"></a>[ListMobileDeviceAccessOverrides](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMobileDeviceAccessOverrides.html) | List the mobile device access overrides | Read | 
| <a name="workmail-ListMobileDeviceAccessRules"></a>[ListMobileDeviceAccessRules](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMobileDeviceAccessRules.html) | List the mobile device access rules | Read | 
| <a name="workmail-ListOrganizations"></a>[ListOrganizations](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListOrganizations.html) | List the non-deleted organizations | List | 
| <a name="workmail-ListOutboundMailFlowRules"></a>[ListOutboundMailFlowRules](https://docs.aws.amazon.com/workmail/latest/adminguide/email-flows.html#email-flows-rule-outbound) | List outbound mail flow rules configured for an organization | List | 
| <a name="workmail-ListPersonalAccessTokens"></a>[ListPersonalAccessTokens](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListPersonalAccessTokens.html) | List metadata for personal access tokens | List | 
| <a name="workmail-ListResourceDelegates"></a>[ListResourceDelegates](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListResourceDelegates.html) | List the delegates associated with a resource | List | 
| <a name="workmail-ListResources"></a>[ListResources](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListResources.html) | List the organization's resources | List | 
| <a name="workmail-ListSmtpGateways"></a>[ListSmtpGateways](https://docs.aws.amazon.com/workmail/latest/adminguide/smtp-gateway.html) | List SMTP gateways registered to the organization | List | 
| <a name="workmail-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListTagsForResource.html) | List the tags applied to an Amazon WorkMail organization resource | List | 
| <a name="workmail-ListUsers"></a>[ListUsers](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListUsers.html) | List the organization's users | List | 
| <a name="workmail-SearchMembers"></a>[SearchMembers](https://docs.aws.amazon.com/workmail/latest/adminguide/groups_overview.html) | Perform a prefix search to find a specific user in a mail group | Read | 
| <a name="workmail-TestAvailabilityConfiguration"></a>[TestAvailabilityConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_TestAvailabilityConfiguration.html) | Performs a test on an availability provider to ensure that access is allowed | Read | 