

# Amazon Route 53 API actions by function
<a name="api-operations-by-function"></a>

This topic lists all Route 53 and Route 53 Resolver API actions in groups by the function they perform. 

**Topics**
+ [Types of function](#API-actions-by-function-types)
+ [Actions by function](#API-actions-by-function-actions)

## Types of function
<a name="API-actions-by-function-types"></a>

**[DNS](#API-actions-by-function-dns)**  
+ [Public and private hosted zones](#actions-by-function-public-private-hosted-zones)
+ [Public hosted zones](#actions-by-function-public-hosted-zones)
+ [Private hosted zones](#actions-by-function-private-hosted-zones)
+ [Resource record sets](#actions-by-function-resource-record-sets)
+ [Public DNS query logs](#actions-by-function-public-dns-query-logs)
+ [Reusable delegation sets](#actions-by-function-reusable-delegation-sets)

**[DNS—Traffic flow](#API-actions-by-function-dns-traffic-flow)**  
+ [Traffic policies](#actions-by-function-traffic-policies)
+ [Traffic policy instances](#actions-by-function-traffic-policy-instances)

**[Domain registration](#API-actions-by-function-domain-registration)**  
+ [Register, renew, and transfer domains](#actions-by-function-register-renew-transfer-domains)
+ [Transfer domains between AWS accounts](#actions-by-function-transfer-domains-between-accounts)
+ [Get domain information](#actions-by-function-get-domain-info)
+ [Change domain settings](#actions-by-function-change-domain-settings)

**[DNS—DNSSEC](#API-actions-by-function-dnssec)**  
+ [DNSSEC signing](#actions-by-function-dnssec-signing)
+ [DNSSEC validation](#actions-by-function-dnssec-validation)

**[DNS—IP-based routing](#API-actions-by-function-ip-routing)**  

**[Health checking](#API-actions-by-function-health-checking)**  
+ [Health checks](#actions-by-function-health-checks)
+ [Health checker IP ranges](#actions-by-function-health-checks-ip-ranges)

**[Limits (quotas) for accounts, hosted zones, and reusable delegation sets](#API-actions-by-function-limits)**  

**[Route 53 profiles](#API-actions-by-function-profiles)**  
+ [Route 53 profiles](#actions-by-function-profiles-managing)
+ [Profile VPC associations](#actions-by-function-profiles-vpc-associations)
+ [Profile resource associations](#actions-by-function-profiles-resource-associations)

**[Route 53 Resolver](#API-actions-by-function-resolver)**  
+ [Route 53 Resolver endpoints](#actions-by-function-resolver-endpoints)
+ [Private DNS query logs](#actions-by-function-resolver-query-logs)
+ [Route 53 Resolver rules](#actions-by-function-resolver-rules)
+ [Route 53 Resolver DNS Firewall](#actions-by-function-resolver-dns-firewall)
+ [Amazon Route 53 Resolver on Outposts](#actions-by-function-outpost-resolver)
+ [Resolver configuration](#actions-by-function-resolver-configuration)

**[Tags](#API-actions-by-function-tags)**  
+ [Tags for hosted zones and health checks](#actions-by-function-tags-for-hosted-zones)
+ [Tags for domains](#actions-by-function-tags-for-domains)
+ [Tags for Route 53 Resolver](#actions-by-function-resolver-tags)

## Actions by function
<a name="API-actions-by-function-actions"></a>

 [DNS](#API-actions-by-function-dns) \| [DNS—Traffic flow](#API-actions-by-function-dns-traffic-flow) \| [Domain registration](#API-actions-by-function-domain-registration) \| [DNS—DNSSEC](#API-actions-by-function-dnssec) \| [DNS—IP-based routing](#API-actions-by-function-ip-routing) \| [Health checking](#API-actions-by-function-health-checking) \| [Limits (quotas) for accounts, hosted zones, and reusable delegation sets](#API-actions-by-function-limits) \| [Route 53 profiles](#API-actions-by-function-profiles) \| [Route 53 Resolver](#API-actions-by-function-resolver) \| [Tags](#API-actions-by-function-tags) 

**DNS**    
Public and private hosted zones  
+ [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html)
+ [DeleteHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteHostedZone.html)
+ [GetHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZone.html)
+ [GetHostedZoneCount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZoneCount.html)
+ [ListHostedZones](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZones.html)
+ [ListHostedZonesByName](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByName.html)
+ [UpdateHostedZoneComment](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneComment.html)  
Public hosted zones  
+ [TestDNSAnswer](https://docs.aws.amazon.com/Route53/latest/APIReference/API_TestDNSAnswer.html)  
Private hosted zones  
+ [AssociateVPCWithHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html)
+ [DisassociateVPCFromHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DisassociateVPCFromHostedZone.html)
+ [CreateVPCAssociationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateVPCAssociationAuthorization.html)
+ [DeleteVPCAssociationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteVPCAssociationAuthorization.html)
+ [ListHostedZonesByVPC](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByVPC.html)
+ [ListVPCAssociationAuthorizations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListVPCAssociationAuthorizations.html)  
Resource record sets  
+ [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html)
+ [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html)
+ [ListResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResourceRecordSets.html)
+ [GetGeoLocation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html)
+ [ListGeoLocations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html)  
Public DNS query logs  
+ [CreateQueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html)
+ [DeleteQueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteQueryLoggingConfig.html)
+ [GetQueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetQueryLoggingConfig.html)
+ [ListQueryLoggingConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html)  
Reusable delegation sets  
+ [CreateReusableDelegationSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateReusableDelegationSet.html)
+ [DeleteReusableDelegationSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteReusableDelegationSet.html)
+ [GetReusableDelegationSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSet.html)
+ [ListReusableDelegationSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListReusableDelegationSets.html)

**DNS—Traffic flow**    
Traffic policies  
+ [CreateTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicy.html)
+ [CreateTrafficPolicyVersion](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicyVersion.html)
+ [DeleteTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html)
+ [GetTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicy.html)
+ [ListTrafficPolicies](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicies.html)
+ [ListTrafficPolicyVersions](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicyVersions.html)
+ [UpdateTrafficPolicyComment](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateTrafficPolicyComment.html)  
Traffic policy instances  
+ [CreateTrafficPolicyInstance](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicyInstance.html)
+ [DeleteTrafficPolicyInstance](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicyInstance.html)
+ [GetTrafficPolicyInstance](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicyInstance.html)
+ [GetTrafficPolicyInstanceCount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicyInstanceCount.html)
+ [ListTrafficPolicyInstances](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicyInstances.html)
+ [ListTrafficPolicyInstancesByHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicyInstancesByHostedZone.html)
+ [ListTrafficPolicyInstancesByPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicyInstancesByPolicy.html)
+ [UpdateTrafficPolicyInstance](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateTrafficPolicyInstance.html)

**Domain registration**    
Register, renew, and transfer domains  
+ [RegisterDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RegisterDomain.html)
+ [RenewDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RenewDomain.html)
+ [ResendContactReachabilityEmail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendContactReachabilityEmail.html)
+ [RetrieveDomainAuthCode](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RetrieveDomainAuthCode.html)
+ [TransferDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomain.html)
+ [DeleteDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DeleteDomain.html)
+ [PushDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_PushDomain.html)
+ [ResendOperationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendOperationAuthorization.html)  
Transfer domains between AWS accounts  
+ [AcceptDomainTransferFromAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AcceptDomainTransferFromAnotherAwsAccount.html)
+ [CancelDomainTransferToAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CancelDomainTransferToAnotherAwsAccount.html)
+ [RejectDomainTransferFromAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RejectDomainTransferFromAnotherAwsAccount.html)
+ [TransferDomainToAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html)  
Get domain information  
+ [CheckDomainAvailability](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CheckDomainAvailability.html)
+ [CheckDomainTransferability](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CheckDomainTransferability.html)
+ [GetContactReachabilityStatus](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetContactReachabilityStatus.html)
+ [GetDomainDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainDetail.html)
+ [GetDomainSuggestions](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainSuggestions.html)
+ [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html)
+ [ListDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListDomains.html)
+ [ListOperations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html)
+ [ListPrices](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListPrices.html)
+ [ViewBilling](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ViewBilling.html)  
Change domain settings  
+ [DisableDomainAutoRenew](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisableDomainAutoRenew.html)
+ [DisableDomainTransferLock](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisableDomainTransferLock.html)
+ [EnableDomainAutoRenew](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_EnableDomainAutoRenew.html)
+ [EnableDomainTransferLock](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_EnableDomainTransferLock.html)
+ [UpdateDomainContact](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainContact.html)
+ [UpdateDomainContactPrivacy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainContactPrivacy.html)
+ [UpdateDomainNameservers](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainNameservers.html)

**DNS—DNSSEC**    
DNSSEC signing  
+ [ActivateKeySigningKey](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ActivateKeySigningKey.html)
+ [CreateKeySigningKey](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateKeySigningKey.html)
+ [DeactivateKeySigningKey](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeactivateKeySigningKey.html)
+ [GetDNSSEC](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetDNSSEC.html)
+ [AssociateDelegationSignerToDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html)
+ [DisassociateDelegationSignerFromDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisassociateDelegationSignerFromDomain.html)  
DNSSEC validation  
+ [GetResolverDnssecConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverDnssecConfig.html)
+ [ListResolverDnssecConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverDnssecConfigs.html)
+ [UpdateResolverDnssecConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverDnssecConfig.html)

**DNS—IP-based routing**  
+ [ChangeCidrCollection](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeCidrCollection.html)
+ [CreateCidrCollection](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateCidrCollection.html)
+ [DeleteCidrCollection](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteCidrCollection.html)
+ [ListCidrBlocks](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListCidrBlocks.html)
+ [ListCidrCollections](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListCidrCollections.html)
+ [ListCidrLocations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListCidrLocations.html)

**Health checking**    
Health checks  
+ [CreateHealthCheck](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHealthCheck.html)
+ [DeleteHealthCheck](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteHealthCheck.html)
+ [GetHealthCheck](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheck.html)
+ [GetHealthCheckCount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheckCount.html)
+ [GetHealthCheckLastFailureReason](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheckLastFailureReason.html)
+ [GetHealthCheckStatus](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheckStatus.html)
+ [ListHealthChecks](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHealthChecks.html)
+ [UpdateHealthCheck](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html)  
Health checker IP ranges  
+ [GetCheckerIpRanges](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetCheckerIpRanges.html)

**Limits (quotas) for accounts, hosted zones, and reusable delegation sets**  
+ [GetAccountLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetAccountLimit.html)
+ [GetHostedZoneLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZoneLimit.html)
+ [GetReusableDelegationSetLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSetLimit.html)

**Route 53 profiles**    
Route 53 profiles  
+ [CreateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_CreateProfile.html)
+ [DeleteProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DeleteProfile.html)
+ [GetProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfile.html)
+ [ListProfiles](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfiles.html)  
Profile VPC associations  
+ [AssociateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateProfile.html)
+ [DisassociateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateProfile.html)
+ [GetProfileAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfileAssociation.html)
+ [ListProfileAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileAssociations.html)  
Profile resource associations  
+ [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html)
+ [DisassociateResourceFromProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateResourceFromProfile.html)
+ [GetProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfileResourceAssociation.html)
+ [ListProfileResourceAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileResourceAssociations.html)
+ [UpdateProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UpdateProfileResourceAssociation.html)

**Route 53 Resolver**    
Route 53 Resolver endpoints  
+ [AssociateResolverEndpointIpAddress](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverEndpointIpAddress.html)
+ [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html)
+ [DeleteResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverEndpoint.html)
+ [DisassociateResolverEndpointIpAddress](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverEndpointIpAddress.html)
+ [GetResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html)
+ [ListResolverEndpointIpAddresses](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverEndpointIpAddresses.html)
+ [ListResolverEndpoints](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverEndpoints.html)
+ [UpdateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverEndpoint.html)  
DNS query logs  
+ [AssociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverQueryLogConfig.html)
+ [CreateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverQueryLogConfig.html)
+ [DeleteResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverQueryLogConfig.html)
+ [DisassociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html)
+ [GetResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfig.html)
+ [GetResolverQueryLogConfigAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfigAssociation.html)
+ [GetResolverQueryLogConfigPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfigPolicy.html)
+ [ListResolverQueryLogConfigAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigAssociations.html)
+ [ListResolverQueryLogConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigs.html)
+ [PutResolverQueryLogConfigPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_PutResolverQueryLogConfigPolicy.html)  
Route 53 Resolver rules  
+ [AssociateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverRule.html)
+ [CreateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html)
+ [DeleteResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverRule.html)
+ [DisassociateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverRule.html)
+ [GetResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRule.html)
+ [GetResolverRuleAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRuleAssociation.html)
+ [GetResolverRulePolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRulePolicy.html)
+ [ListResolverRuleAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html)
+ [ListResolverRules](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html)
+ [PutResolverRulePolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_PutResolverRulePolicy.html)
+ [UpdateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverRule.html)  
Route 53 Resolver DNS Firewall  
+ [AssociateFirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateFirewallRuleGroup.html)
+ [CreateFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateFirewallDomainList.html)
+ [CreateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateFirewallRule.html)
+ [CreateFirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateFirewallRuleGroup.html)
+ [DeleteFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteFirewallDomainList.html)
+ [DeleteFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteFirewallRule.html)
+ [DeleteFirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteFirewallRuleGroup.html)
+ [DisassociateFirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateFirewallRuleGroup.html)
+ [GetFirewallConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallConfig.html)
+ [GetFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallDomainList.html)
+ [GetFirewallRuleGroup](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallRuleGroup.html)
+ [GetFirewallRuleGroupAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallRuleGroupAssociation.html)
+ [GetFirewallRuleGroupPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallRuleGroupPolicy.html)
+ [ImportFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ImportFirewallDomains.html)
+ [ListFirewallConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallConfigs.html)
+ [ListFirewallDomainLists](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallDomainLists.html)
+ [ListFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallDomains.html)
+ [ListFirewallRuleGroupAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallRuleGroupAssociations.html)
+ [ListFirewallRuleGroups](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallRuleGroups.html)
+ [ListFirewallRules](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallRules.html)
+ [PutFirewallRuleGroupPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_PutFirewallRuleGroupPolicy.html)
+ [UpdateFirewallConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateFirewallConfig.html)
+ [UpdateFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateFirewallDomains.html)
+ [UpdateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateFirewallRule.html)
+ [UpdateFirewallRuleGroupAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateFirewallRuleGroupAssociation.html)  
Route 53 Resolver on Outposts  
+ [CreateOutpostResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateOutpostResolver.html)
+ [DeleteOutpostResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteOutpostResolver.html)
+ [GetOutpostResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetOutpostResolver.html)
+ [ListOutpostResolvers](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListOutpostResolvers.html)
+ [UpdateOutpostResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateOutpostResolver.html)  
VPC Resolver configuration  
+ [GetResolverConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverConfig.html)
+ [ListResolverConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverConfigs.html)
+ [UpdateResolverConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverConfig.html)

**Tags**    
Tags for hosted zones and health checks  
+ [ChangeTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeTagsForResource.html)
+ [ListTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTagsForResource.html)
+ [ListTagsForResources](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTagsForResources.html)  
Tags for domains  
+ [DeleteTagsForDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DeleteTagsForDomain.html)
+ [ListTagsForDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListTagsForDomain.html)
+ [UpdateTagsForDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateTagsForDomain.html)  
Tags for Route 53 Resolver  
+ [ListTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListTagsForResource.html)
+ [TagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UntagResource.html)