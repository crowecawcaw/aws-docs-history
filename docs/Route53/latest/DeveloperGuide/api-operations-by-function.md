# Amazon Route 53 API actions by function

This topic lists all Route 53 and Route 53 Resolver API actions in groups by the function they perform.

###### Topics

- [Types of function](#API-actions-by-function-types "#API-actions-by-function-types")
- [Actions by function](#API-actions-by-function-actions "#API-actions-by-function-actions")

## Types of function

**[DNS](#API-actions-by-function-dns "#API-actions-by-function-dns")**

- [Public and private hosted zones](#actions-by-function-public-private-hosted-zones "#actions-by-function-public-private-hosted-zones")
- [Public hosted zones](#actions-by-function-public-hosted-zones "#actions-by-function-public-hosted-zones")
- [Private hosted zones](#actions-by-function-private-hosted-zones "#actions-by-function-private-hosted-zones")
- [Resource record sets](#actions-by-function-resource-record-sets "#actions-by-function-resource-record-sets")
- [Public DNS query logs](#actions-by-function-public-dns-query-logs "#actions-by-function-public-dns-query-logs")
- [Reusable delegation sets](#actions-by-function-reusable-delegation-sets "#actions-by-function-reusable-delegation-sets")

**[DNS—Traffic flow](#API-actions-by-function-dns-traffic-flow "#API-actions-by-function-dns-traffic-flow")**

- [Traffic policies](#actions-by-function-traffic-policies "#actions-by-function-traffic-policies")
- [Traffic policy instances](#actions-by-function-traffic-policy-instances "#actions-by-function-traffic-policy-instances")

**[Domain registration](#API-actions-by-function-domain-registration "#API-actions-by-function-domain-registration")**

- [Register, renew, and transfer domains](#actions-by-function-register-renew-transfer-domains "#actions-by-function-register-renew-transfer-domains")
- [Transfer domains between AWS accounts](#actions-by-function-transfer-domains-between-accounts "#actions-by-function-transfer-domains-between-accounts")
- [Get domain information](#actions-by-function-get-domain-info "#actions-by-function-get-domain-info")
- [Change domain settings](#actions-by-function-change-domain-settings "#actions-by-function-change-domain-settings")

**[DNS—DNSSEC](#API-actions-by-function-dnssec "#API-actions-by-function-dnssec")**

- [DNSSEC signing](#actions-by-function-dnssec-signing "#actions-by-function-dnssec-signing")
- [DNSSEC validation](#actions-by-function-dnssec-validation "#actions-by-function-dnssec-validation")

**[DNS—IP-based routing](#API-actions-by-function-ip-routing "#API-actions-by-function-ip-routing")**

**[Health checking](#API-actions-by-function-health-checking "#API-actions-by-function-health-checking")**

- [Health checks](#actions-by-function-health-checks "#actions-by-function-health-checks")
- [Health checker IP ranges](#actions-by-function-health-checks-ip-ranges "#actions-by-function-health-checks-ip-ranges")

**[Limits (quotas) for accounts, hosted zones, and reusable delegation sets](#API-actions-by-function-limits "#API-actions-by-function-limits")**

**[Route 53 profiles](#API-actions-by-function-profiles "#API-actions-by-function-profiles")**

- [Route 53 profiles](#actions-by-function-profiles-managing "#actions-by-function-profiles-managing")
- [Profile VPC associations](#actions-by-function-profiles-vpc-associations "#actions-by-function-profiles-vpc-associations")
- [Profile resource associations](#actions-by-function-profiles-resource-associations "#actions-by-function-profiles-resource-associations")

**[Route 53 Resolver](#API-actions-by-function-resolver "#API-actions-by-function-resolver")**

- [Route 53 Resolver endpoints](#actions-by-function-resolver-endpoints "#actions-by-function-resolver-endpoints")
- [Private DNS query logs](#actions-by-function-resolver-query-logs "#actions-by-function-resolver-query-logs")
- [Route 53 Resolver rules](#actions-by-function-resolver-rules "#actions-by-function-resolver-rules")
- [Route 53 Resolver DNS Firewall](#actions-by-function-resolver-dns-firewall "#actions-by-function-resolver-dns-firewall")
- [Amazon Route 53 Resolver on Outposts](#actions-by-function-outpost-resolver "#actions-by-function-outpost-resolver")
- [Resolver configuration](#actions-by-function-resolver-configuration "#actions-by-function-resolver-configuration")

**[Tags](#API-actions-by-function-tags "#API-actions-by-function-tags")**

- [Tags for hosted zones and health checks](#actions-by-function-tags-for-hosted-zones "#actions-by-function-tags-for-hosted-zones")
- [Tags for domains](#actions-by-function-tags-for-domains "#actions-by-function-tags-for-domains")
- [Tags for Route 53 Resolver](#actions-by-function-resolver-tags "#actions-by-function-resolver-tags")

## Actions by function

[DNS](#API-actions-by-function-dns "#API-actions-by-function-dns") |
[DNS—Traffic flow](#API-actions-by-function-dns-traffic-flow "#API-actions-by-function-dns-traffic-flow") |
[Domain registration](#API-actions-by-function-domain-registration "#API-actions-by-function-domain-registration") |
[DNS—DNSSEC](#API-actions-by-function-dnssec "#API-actions-by-function-dnssec") |
[DNS—IP-based routing](#API-actions-by-function-ip-routing "#API-actions-by-function-ip-routing") |
[Health checking](#API-actions-by-function-health-checking "#API-actions-by-function-health-checking") |
[Limits (quotas) for accounts, hosted zones, and reusable delegation sets](#API-actions-by-function-limits "#API-actions-by-function-limits") |
[Route 53 profiles](#API-actions-by-function-profiles "#API-actions-by-function-profiles") |
[Route 53 Resolver](#API-actions-by-function-resolver "#API-actions-by-function-resolver") |
[Tags](#API-actions-by-function-tags "#API-actions-by-function-tags")

**DNS**

Public and private hosted zones

- [CreateHostedZone](../APIReference/API_CreateHostedZone.md "../APIReference/API_CreateHostedZone.md")
- [DeleteHostedZone](../APIReference/API_DeleteHostedZone.md "../APIReference/API_DeleteHostedZone.md")
- [GetHostedZone](../APIReference/API_GetHostedZone.md "../APIReference/API_GetHostedZone.md")
- [GetHostedZoneCount](../APIReference/API_GetHostedZoneCount.md "../APIReference/API_GetHostedZoneCount.md")
- [ListHostedZones](../APIReference/API_ListHostedZones.md "../APIReference/API_ListHostedZones.md")
- [ListHostedZonesByName](../APIReference/API_ListHostedZonesByName.md "../APIReference/API_ListHostedZonesByName.md")
- [UpdateHostedZoneComment](../APIReference/API_UpdateHostedZoneComment.md "../APIReference/API_UpdateHostedZoneComment.md")

Public hosted zones

- [TestDNSAnswer](../APIReference/API_TestDNSAnswer.md "../APIReference/API_TestDNSAnswer.md")

Private hosted zones

- [AssociateVPCWithHostedZone](../APIReference/API_AssociateVPCWithHostedZone.md "../APIReference/API_AssociateVPCWithHostedZone.md")
- [DisassociateVPCFromHostedZone](../APIReference/API_DisassociateVPCFromHostedZone.md "../APIReference/API_DisassociateVPCFromHostedZone.md")
- [CreateVPCAssociationAuthorization](../APIReference/API_CreateVPCAssociationAuthorization.md "../APIReference/API_CreateVPCAssociationAuthorization.md")
- [DeleteVPCAssociationAuthorization](../APIReference/API_DeleteVPCAssociationAuthorization.md "../APIReference/API_DeleteVPCAssociationAuthorization.md")
- [ListHostedZonesByVPC](../APIReference/API_ListHostedZonesByVPC.md "../APIReference/API_ListHostedZonesByVPC.md")
- [ListVPCAssociationAuthorizations](../APIReference/API_ListVPCAssociationAuthorizations.md "../APIReference/API_ListVPCAssociationAuthorizations.md")

Resource record sets

- [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md")
- [GetChange](../APIReference/API_GetChange.md "../APIReference/API_GetChange.md")
- [ListResourceRecordSets](../APIReference/API_ListResourceRecordSets.md "../APIReference/API_ListResourceRecordSets.md")
- [GetGeoLocation](../APIReference/API_GetGeoLocation.md "../APIReference/API_GetGeoLocation.md")
- [ListGeoLocations](../APIReference/API_ListGeoLocations.md "../APIReference/API_ListGeoLocations.md")

Public DNS query logs

- [CreateQueryLoggingConfig](../APIReference/API_CreateQueryLoggingConfig.md "../APIReference/API_CreateQueryLoggingConfig.md")
- [DeleteQueryLoggingConfig](../APIReference/API_DeleteQueryLoggingConfig.md "../APIReference/API_DeleteQueryLoggingConfig.md")
- [GetQueryLoggingConfig](../APIReference/API_GetQueryLoggingConfig.md "../APIReference/API_GetQueryLoggingConfig.md")
- [ListQueryLoggingConfigs](../APIReference/API_ListQueryLoggingConfigs.md "../APIReference/API_ListQueryLoggingConfigs.md")

Reusable delegation sets

- [CreateReusableDelegationSet](../APIReference/API_CreateReusableDelegationSet.md "../APIReference/API_CreateReusableDelegationSet.md")
- [DeleteReusableDelegationSet](../APIReference/API_DeleteReusableDelegationSet.md "../APIReference/API_DeleteReusableDelegationSet.md")
- [GetReusableDelegationSet](../APIReference/API_GetReusableDelegationSet.md "../APIReference/API_GetReusableDelegationSet.md")
- [ListReusableDelegationSets](../APIReference/API_ListReusableDelegationSets.md "../APIReference/API_ListReusableDelegationSets.md")

**DNS—Traffic flow**

Traffic policies

- [CreateTrafficPolicy](../APIReference/API_CreateTrafficPolicy.md "../APIReference/API_CreateTrafficPolicy.md")
- [CreateTrafficPolicyVersion](../APIReference/API_CreateTrafficPolicyVersion.md "../APIReference/API_CreateTrafficPolicyVersion.md")
- [DeleteTrafficPolicy](../APIReference/API_DeleteTrafficPolicy.md "../APIReference/API_DeleteTrafficPolicy.md")
- [GetTrafficPolicy](../APIReference/API_GetTrafficPolicy.md "../APIReference/API_GetTrafficPolicy.md")
- [ListTrafficPolicies](../APIReference/API_ListTrafficPolicies.md "../APIReference/API_ListTrafficPolicies.md")
- [ListTrafficPolicyVersions](../APIReference/API_ListTrafficPolicyVersions.md "../APIReference/API_ListTrafficPolicyVersions.md")
- [UpdateTrafficPolicyComment](../APIReference/API_UpdateTrafficPolicyComment.md "../APIReference/API_UpdateTrafficPolicyComment.md")

Traffic policy instances

- [CreateTrafficPolicyInstance](../APIReference/API_CreateTrafficPolicyInstance.md "../APIReference/API_CreateTrafficPolicyInstance.md")
- [DeleteTrafficPolicyInstance](../APIReference/API_DeleteTrafficPolicyInstance.md "../APIReference/API_DeleteTrafficPolicyInstance.md")
- [GetTrafficPolicyInstance](../APIReference/API_GetTrafficPolicyInstance.md "../APIReference/API_GetTrafficPolicyInstance.md")
- [GetTrafficPolicyInstanceCount](../APIReference/API_GetTrafficPolicyInstanceCount.md "../APIReference/API_GetTrafficPolicyInstanceCount.md")
- [ListTrafficPolicyInstances](../APIReference/API_ListTrafficPolicyInstances.md "../APIReference/API_ListTrafficPolicyInstances.md")
- [ListTrafficPolicyInstancesByHostedZone](../APIReference/API_ListTrafficPolicyInstancesByHostedZone.md "../APIReference/API_ListTrafficPolicyInstancesByHostedZone.md")
- [ListTrafficPolicyInstancesByPolicy](../APIReference/API_ListTrafficPolicyInstancesByPolicy.md "../APIReference/API_ListTrafficPolicyInstancesByPolicy.md")
- [UpdateTrafficPolicyInstance](../APIReference/API_UpdateTrafficPolicyInstance.md "../APIReference/API_UpdateTrafficPolicyInstance.md")

**Domain registration**

Register, renew, and transfer domains

- [RegisterDomain](../APIReference/API_domains_RegisterDomain.md "../APIReference/API_domains_RegisterDomain.md")
- [RenewDomain](../APIReference/API_domains_RenewDomain.md "../APIReference/API_domains_RenewDomain.md")
- [ResendContactReachabilityEmail](../APIReference/API_domains_ResendContactReachabilityEmail.md "../APIReference/API_domains_ResendContactReachabilityEmail.md")
- [RetrieveDomainAuthCode](../APIReference/API_domains_RetrieveDomainAuthCode.md "../APIReference/API_domains_RetrieveDomainAuthCode.md")
- [TransferDomain](../APIReference/API_domains_TransferDomain.md "../APIReference/API_domains_TransferDomain.md")
- [DeleteDomain](../APIReference/API_domains_DeleteDomain.md "../APIReference/API_domains_DeleteDomain.md")
- [PushDomain](../APIReference/API_domains_PushDomain.md "../APIReference/API_domains_PushDomain.md")
- [ResendOperationAuthorization](../APIReference/API_domains_ResendOperationAuthorization.md "../APIReference/API_domains_ResendOperationAuthorization.md")

Transfer domains between AWS accounts

- [AcceptDomainTransferFromAnotherAwsAccount](../APIReference/API_domains_AcceptDomainTransferFromAnotherAwsAccount.md "../APIReference/API_domains_AcceptDomainTransferFromAnotherAwsAccount.md")
- [CancelDomainTransferToAnotherAwsAccount](../APIReference/API_domains_CancelDomainTransferToAnotherAwsAccount.md "../APIReference/API_domains_CancelDomainTransferToAnotherAwsAccount.md")
- [RejectDomainTransferFromAnotherAwsAccount](../APIReference/API_domains_RejectDomainTransferFromAnotherAwsAccount.md "../APIReference/API_domains_RejectDomainTransferFromAnotherAwsAccount.md")
- [TransferDomainToAnotherAwsAccount](../APIReference/API_domains_TransferDomainToAnotherAwsAccount.md "../APIReference/API_domains_TransferDomainToAnotherAwsAccount.md")

Get domain information

- [CheckDomainAvailability](../APIReference/API_domains_CheckDomainAvailability.md "../APIReference/API_domains_CheckDomainAvailability.md")
- [CheckDomainTransferability](../APIReference/API_domains_CheckDomainTransferability.md "../APIReference/API_domains_CheckDomainTransferability.md")
- [GetContactReachabilityStatus](../APIReference/API_domains_GetContactReachabilityStatus.md "../APIReference/API_domains_GetContactReachabilityStatus.md")
- [GetDomainDetail](../APIReference/API_domains_GetDomainDetail.md "../APIReference/API_domains_GetDomainDetail.md")
- [GetDomainSuggestions](../APIReference/API_domains_GetDomainSuggestions.md "../APIReference/API_domains_GetDomainSuggestions.md")
- [GetOperationDetail](../APIReference/API_domains_GetOperationDetail.md "../APIReference/API_domains_GetOperationDetail.md")
- [ListDomains](../APIReference/API_domains_ListDomains.md "../APIReference/API_domains_ListDomains.md")
- [ListOperations](../APIReference/API_domains_ListOperations.md "../APIReference/API_domains_ListOperations.md")
- [ListPrices](../APIReference/API_domains_ListPrices.md "../APIReference/API_domains_ListPrices.md")
- [ViewBilling](../APIReference/API_domains_ViewBilling.md "../APIReference/API_domains_ViewBilling.md")

Change domain settings

- [DisableDomainAutoRenew](../APIReference/API_domains_DisableDomainAutoRenew.md "../APIReference/API_domains_DisableDomainAutoRenew.md")
- [DisableDomainTransferLock](../APIReference/API_domains_DisableDomainTransferLock.md "../APIReference/API_domains_DisableDomainTransferLock.md")
- [EnableDomainAutoRenew](../APIReference/API_domains_EnableDomainAutoRenew.md "../APIReference/API_domains_EnableDomainAutoRenew.md")
- [EnableDomainTransferLock](../APIReference/API_domains_EnableDomainTransferLock.md "../APIReference/API_domains_EnableDomainTransferLock.md")
- [UpdateDomainContact](../APIReference/API_domains_UpdateDomainContact.md "../APIReference/API_domains_UpdateDomainContact.md")
- [UpdateDomainContactPrivacy](../APIReference/API_domains_UpdateDomainContactPrivacy.md "../APIReference/API_domains_UpdateDomainContactPrivacy.md")
- [UpdateDomainNameservers](../APIReference/API_domains_UpdateDomainNameservers.md "../APIReference/API_domains_UpdateDomainNameservers.md")

**DNS—DNSSEC**

DNSSEC signing

- [ActivateKeySigningKey](../APIReference/API_ActivateKeySigningKey.md "../APIReference/API_ActivateKeySigningKey.md")
- [CreateKeySigningKey](../APIReference/API_CreateKeySigningKey.md "../APIReference/API_CreateKeySigningKey.md")
- [DeactivateKeySigningKey](../APIReference/API_DeactivateKeySigningKey.md "../APIReference/API_DeactivateKeySigningKey.md")
- [GetDNSSEC](../APIReference/API_GetDNSSEC.md "../APIReference/API_GetDNSSEC.md")
- [AssociateDelegationSignerToDomain](../APIReference/API_domains_AssociateDelegationSignerToDomain.md "../APIReference/API_domains_AssociateDelegationSignerToDomain.md")
- [DisassociateDelegationSignerFromDomain](../APIReference/API_domains_DisassociateDelegationSignerFromDomain.md "../APIReference/API_domains_DisassociateDelegationSignerFromDomain.md")

DNSSEC validation

- [GetResolverDnssecConfig](../APIReference/API_route53resolver_GetResolverDnssecConfig.md "../APIReference/API_route53resolver_GetResolverDnssecConfig.md")
- [ListResolverDnssecConfigs](../APIReference/API_route53resolver_ListResolverDnssecConfigs.md "../APIReference/API_route53resolver_ListResolverDnssecConfigs.md")
- [UpdateResolverDnssecConfig](../APIReference/API_route53resolver_UpdateResolverDnssecConfig.md "../APIReference/API_route53resolver_UpdateResolverDnssecConfig.md")

**DNS—IP-based routing**

- [ChangeCidrCollection](../APIReference/API_ChangeCidrCollection.md "../APIReference/API_ChangeCidrCollection.md")
- [CreateCidrCollection](../APIReference/API_CreateCidrCollection.md "../APIReference/API_CreateCidrCollection.md")
- [DeleteCidrCollection](../APIReference/API_DeleteCidrCollection.md "../APIReference/API_DeleteCidrCollection.md")
- [ListCidrBlocks](../APIReference/API_ListCidrBlocks.md "../APIReference/API_ListCidrBlocks.md")
- [ListCidrCollections](../APIReference/API_ListCidrCollections.md "../APIReference/API_ListCidrCollections.md")
- [ListCidrLocations](../APIReference/API_ListCidrLocations.md "../APIReference/API_ListCidrLocations.md")

**Health checking**

Health checks

- [CreateHealthCheck](../APIReference/API_CreateHealthCheck.md "../APIReference/API_CreateHealthCheck.md")
- [DeleteHealthCheck](../APIReference/API_DeleteHealthCheck.md "../APIReference/API_DeleteHealthCheck.md")
- [GetHealthCheck](../APIReference/API_GetHealthCheck.md "../APIReference/API_GetHealthCheck.md")
- [GetHealthCheckCount](../APIReference/API_GetHealthCheckCount.md "../APIReference/API_GetHealthCheckCount.md")
- [GetHealthCheckLastFailureReason](../APIReference/API_GetHealthCheckLastFailureReason.md "../APIReference/API_GetHealthCheckLastFailureReason.md")
- [GetHealthCheckStatus](../APIReference/API_GetHealthCheckStatus.md "../APIReference/API_GetHealthCheckStatus.md")
- [ListHealthChecks](../APIReference/API_ListHealthChecks.md "../APIReference/API_ListHealthChecks.md")
- [UpdateHealthCheck](../APIReference/API_UpdateHealthCheck.md "../APIReference/API_UpdateHealthCheck.md")

Health checker IP ranges

- [GetCheckerIpRanges](../APIReference/API_GetCheckerIpRanges.md "../APIReference/API_GetCheckerIpRanges.md")

**Limits (quotas) for
accounts, hosted zones, and reusable delegation sets**

- [GetAccountLimit](../APIReference/API_GetAccountLimit.md "../APIReference/API_GetAccountLimit.md")
- [GetHostedZoneLimit](../APIReference/API_GetHostedZoneLimit.md "../APIReference/API_GetHostedZoneLimit.md")
- [GetReusableDelegationSetLimit](../APIReference/API_GetReusableDelegationSetLimit.md "../APIReference/API_GetReusableDelegationSetLimit.md")

**Route 53 profiles**

Route 53 profiles

- [CreateProfile](../APIReference/API_route53profiles_CreateProfile.md "../APIReference/API_route53profiles_CreateProfile.md")
- [DeleteProfile](../APIReference/API_route53profiles_DeleteProfile.md "../APIReference/API_route53profiles_DeleteProfile.md")
- [GetProfile](../APIReference/API_route53profiles_GetProfile.md "../APIReference/API_route53profiles_GetProfile.md")
- [ListProfiles](../APIReference/API_route53profiles_ListProfiles.md "../APIReference/API_route53profiles_ListProfiles.md")

Profile VPC associations

- [AssociateProfile](../APIReference/API_route53profiles_AssociateProfile.md "../APIReference/API_route53profiles_AssociateProfile.md")
- [DisassociateProfile](../APIReference/API_route53profiles_DisassociateProfile.md "../APIReference/API_route53profiles_DisassociateProfile.md")
- [GetProfileAssociation](../APIReference/API_route53profiles_GetProfileAssociation.md "../APIReference/API_route53profiles_GetProfileAssociation.md")
- [ListProfileAssociations](../APIReference/API_route53profiles_ListProfileAssociations.md "../APIReference/API_route53profiles_ListProfileAssociations.md")

Profile resource associations

- [AssociateResourceToProfile](../APIReference/API_route53profiles_AssociateResourceToProfile.md "../APIReference/API_route53profiles_AssociateResourceToProfile.md")
- [DisassociateResourceFromProfile](../APIReference/API_route53profiles_DisassociateResourceFromProfile.md "../APIReference/API_route53profiles_DisassociateResourceFromProfile.md")
- [GetProfileResourceAssociation](../APIReference/API_route53profiles_GetProfileResourceAssociation.md "../APIReference/API_route53profiles_GetProfileResourceAssociation.md")
- [ListProfileResourceAssociations](../APIReference/API_route53profiles_ListProfileResourceAssociations.md "../APIReference/API_route53profiles_ListProfileResourceAssociations.md")
- [UpdateProfileResourceAssociation](../APIReference/API_route53profiles_UpdateProfileResourceAssociation.md "../APIReference/API_route53profiles_UpdateProfileResourceAssociation.md")

**Route 53 Resolver**

Route 53 Resolver endpoints

- [AssociateResolverEndpointIpAddress](../APIReference/API_route53resolver_AssociateResolverEndpointIpAddress.md "../APIReference/API_route53resolver_AssociateResolverEndpointIpAddress.md")
- [CreateResolverEndpoint](../APIReference/API_route53resolver_CreateResolverEndpoint.md "../APIReference/API_route53resolver_CreateResolverEndpoint.md")
- [DeleteResolverEndpoint](../APIReference/API_route53resolver_DeleteResolverEndpoint.md "../APIReference/API_route53resolver_DeleteResolverEndpoint.md")
- [DisassociateResolverEndpointIpAddress](../APIReference/API_route53resolver_DisassociateResolverEndpointIpAddress.md "../APIReference/API_route53resolver_DisassociateResolverEndpointIpAddress.md")
- [GetResolverEndpoint](../APIReference/API_route53resolver_GetResolverEndpoint.md "../APIReference/API_route53resolver_GetResolverEndpoint.md")
- [ListResolverEndpointIpAddresses](../APIReference/API_route53resolver_ListResolverEndpointIpAddresses.md "../APIReference/API_route53resolver_ListResolverEndpointIpAddresses.md")
- [ListResolverEndpoints](../APIReference/API_route53resolver_ListResolverEndpoints.md "../APIReference/API_route53resolver_ListResolverEndpoints.md")
- [UpdateResolverEndpoint](../APIReference/API_route53resolver_UpdateResolverEndpoint.md "../APIReference/API_route53resolver_UpdateResolverEndpoint.md")

DNS query logs

- [AssociateResolverQueryLogConfig](../APIReference/API_route53resolver_AssociateResolverQueryLogConfig.md "../APIReference/API_route53resolver_AssociateResolverQueryLogConfig.md")
- [CreateResolverQueryLogConfig](../APIReference/API_route53resolver_CreateResolverQueryLogConfig.md "../APIReference/API_route53resolver_CreateResolverQueryLogConfig.md")
- [DeleteResolverQueryLogConfig](../APIReference/API_route53resolver_DeleteResolverQueryLogConfig.md "../APIReference/API_route53resolver_DeleteResolverQueryLogConfig.md")
- [DisassociateResolverQueryLogConfig](../APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.md "../APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.md")
- [GetResolverQueryLogConfig](../APIReference/API_route53resolver_GetResolverQueryLogConfig.md "../APIReference/API_route53resolver_GetResolverQueryLogConfig.md")
- [GetResolverQueryLogConfigAssociation](../APIReference/API_route53resolver_GetResolverQueryLogConfigAssociation.md "../APIReference/API_route53resolver_GetResolverQueryLogConfigAssociation.md")
- [GetResolverQueryLogConfigPolicy](../APIReference/API_route53resolver_GetResolverQueryLogConfigPolicy.md "../APIReference/API_route53resolver_GetResolverQueryLogConfigPolicy.md")
- [ListResolverQueryLogConfigAssociations](../APIReference/API_route53resolver_ListResolverQueryLogConfigAssociations.md "../APIReference/API_route53resolver_ListResolverQueryLogConfigAssociations.md")
- [ListResolverQueryLogConfigs](../APIReference/API_route53resolver_ListResolverQueryLogConfigs.md "../APIReference/API_route53resolver_ListResolverQueryLogConfigs.md")
- [PutResolverQueryLogConfigPolicy](../APIReference/API_route53resolver_PutResolverQueryLogConfigPolicy.md "../APIReference/API_route53resolver_PutResolverQueryLogConfigPolicy.md")

Route 53 Resolver rules

- [AssociateResolverRule](../APIReference/API_route53resolver_AssociateResolverRule.md "../APIReference/API_route53resolver_AssociateResolverRule.md")
- [CreateResolverRule](../APIReference/API_route53resolver_CreateResolverRule.md "../APIReference/API_route53resolver_CreateResolverRule.md")
- [DeleteResolverRule](../APIReference/API_route53resolver_DeleteResolverRule.md "../APIReference/API_route53resolver_DeleteResolverRule.md")
- [DisassociateResolverRule](../APIReference/API_route53resolver_DisassociateResolverRule.md "../APIReference/API_route53resolver_DisassociateResolverRule.md")
- [GetResolverRule](../APIReference/API_route53resolver_GetResolverRule.md "../APIReference/API_route53resolver_GetResolverRule.md")
- [GetResolverRuleAssociation](../APIReference/API_route53resolver_GetResolverRuleAssociation.md "../APIReference/API_route53resolver_GetResolverRuleAssociation.md")
- [GetResolverRulePolicy](../APIReference/API_route53resolver_GetResolverRulePolicy.md "../APIReference/API_route53resolver_GetResolverRulePolicy.md")
- [ListResolverRuleAssociations](../APIReference/API_route53resolver_ListResolverRuleAssociations.md "../APIReference/API_route53resolver_ListResolverRuleAssociations.md")
- [ListResolverRules](../APIReference/API_route53resolver_ListResolverRules.md "../APIReference/API_route53resolver_ListResolverRules.md")
- [PutResolverRulePolicy](../APIReference/API_route53resolver_PutResolverRulePolicy.md "../APIReference/API_route53resolver_PutResolverRulePolicy.md")
- [UpdateResolverRule](../APIReference/API_route53resolver_UpdateResolverRule.md "../APIReference/API_route53resolver_UpdateResolverRule.md")

Route 53 Resolver DNS Firewall

- [AssociateFirewallRuleGroup](../APIReference/API_route53resolver_AssociateFirewallRuleGroup.md "../APIReference/API_route53resolver_AssociateFirewallRuleGroup.md")
- [CreateFirewallDomainList](../APIReference/API_route53resolver_CreateFirewallDomainList.md "../APIReference/API_route53resolver_CreateFirewallDomainList.md")
- [CreateFirewallRule](../APIReference/API_route53resolver_CreateFirewallRule.md "../APIReference/API_route53resolver_CreateFirewallRule.md")
- [CreateFirewallRuleGroup](../APIReference/API_route53resolver_CreateFirewallRuleGroup.md "../APIReference/API_route53resolver_CreateFirewallRuleGroup.md")
- [DeleteFirewallDomainList](../APIReference/API_route53resolver_DeleteFirewallDomainList.md "../APIReference/API_route53resolver_DeleteFirewallDomainList.md")
- [DeleteFirewallRule](../APIReference/API_route53resolver_DeleteFirewallRule.md "../APIReference/API_route53resolver_DeleteFirewallRule.md")
- [DeleteFirewallRuleGroup](../APIReference/API_route53resolver_DeleteFirewallRuleGroup.md "../APIReference/API_route53resolver_DeleteFirewallRuleGroup.md")
- [DisassociateFirewallRuleGroup](../APIReference/API_route53resolver_DisassociateFirewallRuleGroup.md "../APIReference/API_route53resolver_DisassociateFirewallRuleGroup.md")
- [GetFirewallConfig](../APIReference/API_route53resolver_GetFirewallConfig.md "../APIReference/API_route53resolver_GetFirewallConfig.md")
- [GetFirewallDomainList](../APIReference/API_route53resolver_GetFirewallDomainList.md "../APIReference/API_route53resolver_GetFirewallDomainList.md")
- [GetFirewallRuleGroup](../APIReference/API_route53resolver_GetFirewallRuleGroup.md "../APIReference/API_route53resolver_GetFirewallRuleGroup.md")
- [GetFirewallRuleGroupAssociation](../APIReference/API_route53resolver_GetFirewallRuleGroupAssociation.md "../APIReference/API_route53resolver_GetFirewallRuleGroupAssociation.md")
- [GetFirewallRuleGroupPolicy](../APIReference/API_route53resolver_GetFirewallRuleGroupPolicy.md "../APIReference/API_route53resolver_GetFirewallRuleGroupPolicy.md")
- [ImportFirewallDomains](../APIReference/API_route53resolver_ImportFirewallDomains.md "../APIReference/API_route53resolver_ImportFirewallDomains.md")
- [ListFirewallConfigs](../APIReference/API_route53resolver_ListFirewallConfigs.md "../APIReference/API_route53resolver_ListFirewallConfigs.md")
- [ListFirewallDomainLists](../APIReference/API_route53resolver_ListFirewallDomainLists.md "../APIReference/API_route53resolver_ListFirewallDomainLists.md")
- [ListFirewallDomains](../APIReference/API_route53resolver_ListFirewallDomains.md "../APIReference/API_route53resolver_ListFirewallDomains.md")
- [ListFirewallRuleGroupAssociations](../APIReference/API_route53resolver_ListFirewallRuleGroupAssociations.md "../APIReference/API_route53resolver_ListFirewallRuleGroupAssociations.md")
- [ListFirewallRuleGroups](../APIReference/API_route53resolver_ListFirewallRuleGroups.md "../APIReference/API_route53resolver_ListFirewallRuleGroups.md")
- [ListFirewallRules](../APIReference/API_route53resolver_ListFirewallRules.md "../APIReference/API_route53resolver_ListFirewallRules.md")
- [PutFirewallRuleGroupPolicy](../APIReference/API_route53resolver_PutFirewallRuleGroupPolicy.md "../APIReference/API_route53resolver_PutFirewallRuleGroupPolicy.md")
- [UpdateFirewallConfig](../APIReference/API_route53resolver_UpdateFirewallConfig.md "../APIReference/API_route53resolver_UpdateFirewallConfig.md")
- [UpdateFirewallDomains](../APIReference/API_route53resolver_UpdateFirewallDomains.md "../APIReference/API_route53resolver_UpdateFirewallDomains.md")
- [UpdateFirewallRule](../APIReference/API_route53resolver_UpdateFirewallRule.md "../APIReference/API_route53resolver_UpdateFirewallRule.md")
- [UpdateFirewallRuleGroupAssociation](../APIReference/API_route53resolver_UpdateFirewallRuleGroupAssociation.md "../APIReference/API_route53resolver_UpdateFirewallRuleGroupAssociation.md")

Route 53 Resolver on Outposts

- [CreateOutpostResolver](../APIReference/API_route53resolver_CreateOutpostResolver.md "../APIReference/API_route53resolver_CreateOutpostResolver.md")
- [DeleteOutpostResolver](../APIReference/API_route53resolver_DeleteOutpostResolver.md "../APIReference/API_route53resolver_DeleteOutpostResolver.md")
- [GetOutpostResolver](../APIReference/API_route53resolver_GetOutpostResolver.md "../APIReference/API_route53resolver_GetOutpostResolver.md")
- [ListOutpostResolvers](../APIReference/API_route53resolver_ListOutpostResolvers.md "../APIReference/API_route53resolver_ListOutpostResolvers.md")
- [UpdateOutpostResolver](../APIReference/API_route53resolver_UpdateOutpostResolver.md "../APIReference/API_route53resolver_UpdateOutpostResolver.md")

VPC Resolver configuration

- [GetResolverConfig](../APIReference/API_route53resolver_GetResolverConfig.md "../APIReference/API_route53resolver_GetResolverConfig.md")
- [ListResolverConfigs](../APIReference/API_route53resolver_ListResolverConfigs.md "../APIReference/API_route53resolver_ListResolverConfigs.md")
- [UpdateResolverConfig](../APIReference/API_route53resolver_UpdateResolverConfig.md "../APIReference/API_route53resolver_UpdateResolverConfig.md")

**Tags**

Tags for hosted zones and health checks

- [ChangeTagsForResource](../APIReference/API_ChangeTagsForResource.md "../APIReference/API_ChangeTagsForResource.md")
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [ListTagsForResources](../APIReference/API_ListTagsForResources.md "../APIReference/API_ListTagsForResources.md")

Tags for domains

- [DeleteTagsForDomain](../APIReference/API_domains_DeleteTagsForDomain.md "../APIReference/API_domains_DeleteTagsForDomain.md")
- [ListTagsForDomain](../APIReference/API_domains_ListTagsForDomain.md "../APIReference/API_domains_ListTagsForDomain.md")
- [UpdateTagsForDomain](../APIReference/API_domains_UpdateTagsForDomain.md "../APIReference/API_domains_UpdateTagsForDomain.md")

Tags for Route 53 Resolver

- [ListTagsForResource](../APIReference/API_route53resolver_ListTagsForResource.md "../APIReference/API_route53resolver_ListTagsForResource.md")
- [TagResource](../APIReference/API_route53resolver_TagResource.md "../APIReference/API_route53resolver_TagResource.md")
- [UntagResource](../APIReference/API_route53resolver_UntagResource.md "../APIReference/API_route53resolver_UntagResource.md")
