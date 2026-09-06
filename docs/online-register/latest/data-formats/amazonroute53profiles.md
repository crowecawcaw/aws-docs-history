

# Data retrieval APIs for Amazon Route 53 Profiles
<a name="amazonroute53profiles"></a>

Amazon Route 53 Profiles provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="route53profiles-GetProfile"></a>[GetProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfile.html) | Get a Profile | Read | 
| <a name="route53profiles-GetProfileAssociation"></a>[GetProfileAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfileAssociation.html) | Get a Profile to a VPC association specified by the Profile association ID | Read | 
| <a name="route53profiles-GetProfilePolicy"></a>[GetProfilePolicy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sharing-profiles.html) | Read the RAM access control policy for a Profile | Read | 
| <a name="route53profiles-GetProfileResourceAssociation"></a>[GetProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfileResourceAssociation.html) | Get a Profile resource association based on the ProfileResourceAssociationId | Read | 
| <a name="route53profiles-ListProfileAssociations"></a>[ListProfileAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileAssociations.html) | List all VPCs the specified Profile is associated to | List | 
| <a name="route53profiles-ListProfileResourceAssociations"></a>[ListProfileResourceAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileResourceAssociations.html) | List all the associations between the resources, such as DNS Firewall rule groups, private hosted zones, resolver rules, etc. for the given Profile ID | List | 
| <a name="route53profiles-ListProfiles"></a>[ListProfiles](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfiles.html) | List all the Profiles created by, and shared to the customer | List | 
| <a name="route53profiles-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListTagsForResource.html) | List all tags associated with the resource | List | 