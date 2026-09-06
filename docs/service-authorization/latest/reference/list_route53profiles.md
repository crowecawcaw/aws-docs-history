

# Actions, resources, and condition keys for Amazon Route 53 Profiles
<a name="list_route53profiles"></a>

Amazon Route 53 Profiles (service prefix: `route53profiles`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/Route53/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/route53profiles/route53profiles.json) for this service.

**Topics**
+ [API operations defined by Amazon Route 53 Profiles](#list_route53profiles-operations)
+ [Actions defined by Amazon Route 53 Profiles](#list_route53profiles-actions-as-permissions)
+ [Permission-only actions for Amazon Route 53 Profiles](#list_route53profiles-permission-only-actions)
+ [Resource types defined by Amazon Route 53 Profiles](#list_route53profiles-resources-for-iam-policies)
+ [Condition keys for Amazon Route 53 Profiles](#list_route53profiles-policy-keys)

## API operations defined by Amazon Route 53 Profiles
<a name="list_route53profiles-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_route53profiles-actions-as-permissions).




- **   AssociateProfile  **
  - **IAM action:**  [route53profiles:AssociateProfile](#list_route53profiles-action-AssociateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53profiles:TagResource](#list_route53profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   AssociateResourceToProfile  **
  - **IAM action:**  [route53profiles:AssociateResourceToProfile](#list_route53profiles-action-AssociateResourceToProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProfile  **
  - **IAM action:**  [route53profiles:CreateProfile](#list_route53profiles-action-CreateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53profiles:TagResource](#list_route53profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteProfile  **
  - **IAM action:**  [route53profiles:DeleteProfile](#list_route53profiles-action-DeleteProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateProfile  **
  - **IAM action:**  [route53profiles:DisassociateProfile](#list_route53profiles-action-DisassociateProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateResourceFromProfile  **
  - **IAM action:**  [route53profiles:DisassociateResourceFromProfile](#list_route53profiles-action-DisassociateResourceFromProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetProfile  **
  - **IAM action:**  [route53profiles:GetProfile](#list_route53profiles-action-GetProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfileAssociation  **
  - **IAM action:**  [route53profiles:GetProfileAssociation](#list_route53profiles-action-GetProfileAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfileResourceAssociation  **
  - **IAM action:**  [route53profiles:GetProfileResourceAssociation](#list_route53profiles-action-GetProfileResourceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListProfileAssociations  **
  - **IAM action:**  [route53profiles:ListProfileAssociations](#list_route53profiles-action-ListProfileAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfileResourceAssociations  **
  - **IAM action:**  [route53profiles:ListProfileResourceAssociations](#list_route53profiles-action-ListProfileResourceAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfiles  **
  - **IAM action:**  [route53profiles:ListProfiles](#list_route53profiles-action-ListProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [route53profiles:ListTagsForResource](#list_route53profiles-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [route53profiles:TagResource](#list_route53profiles-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [route53profiles:UntagResource](#list_route53profiles-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateProfileResourceAssociation  **
  - **IAM action:**  [route53profiles:UpdateProfileResourceAssociation](#list_route53profiles-action-UpdateProfileResourceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Route 53 Profiles
<a name="list_route53profiles-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateProfile.html)  **
  - **Description:** Grants permission to associates a Profile to the customer VPC
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53profiles-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_route53profiles-aws_TagKeys)<br />[route53profiles:ResourceIds](#list_route53profiles-route53profiles_ResourceIds)
  - **Access level:** Write

- **   [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html)  **
  - **Description:** Grants permission to associates a resource, such as DNS Firewall rule group, private hosted zone, resolver rule, etc. to a specified Profile
  - **Resource types (\*required):** 
  - **Condition keys:** [route53profiles:FirewallRuleGroupPriority](#list_route53profiles-route53profiles_FirewallRuleGroupPriority)<br />[route53profiles:HostedZoneDomains](#list_route53profiles-route53profiles_HostedZoneDomains)<br />[route53profiles:ResolverRuleDomains](#list_route53profiles-route53profiles_ResolverRuleDomains)<br />[route53profiles:ResourceArns](#list_route53profiles-route53profiles_ResourceArns)<br />[route53profiles:ResourceTypes](#list_route53profiles-route53profiles_ResourceTypes)
  - **Access level:** Write

- **   [CreateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_CreateProfile.html)  **
  - **Description:** Grants permission to create a new Profile resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53profiles-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_route53profiles-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DeleteProfile.html)  **
  - **Description:** Grants permission to delete a Profile specified by the ProfileId
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateProfile.html)  **
  - **Description:** Grants permission to delete an association between a customer VPC and the specified Profile
  - **Resource types (\*required):** 
  - **Condition keys:** [route53profiles:ResourceIds](#list_route53profiles-route53profiles_ResourceIds)
  - **Access level:** Write

- **   [DisassociateResourceFromProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateResourceFromProfile.html)  **
  - **Description:** Grants permission to delete the asoociation between the resource. such as DNS Firewall rule group, private hosted zone, resolver rule, etc. and the specified Profile
  - **Resource types (\*required):** 
  - **Condition keys:** [route53profiles:FirewallRuleGroupPriority](#list_route53profiles-route53profiles_FirewallRuleGroupPriority)<br />[route53profiles:HostedZoneDomains](#list_route53profiles-route53profiles_HostedZoneDomains)<br />[route53profiles:ResolverRuleDomains](#list_route53profiles-route53profiles_ResolverRuleDomains)<br />[route53profiles:ResourceArns](#list_route53profiles-route53profiles_ResourceArns)<br />[route53profiles:ResourceTypes](#list_route53profiles-route53profiles_ResourceTypes)
  - **Access level:** Write

- **   [GetProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfile.html)  **
  - **Description:** Grants permission to get a Profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProfileAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfileAssociation.html)  **
  - **Description:** Grants permission to get a Profile to a VPC association specified by the Profile association ID
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfileResourceAssociation.html)  **
  - **Description:** Grants permission to get a Profile resource association based on the ProfileResourceAssociationId
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListProfileAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileAssociations.html)  **
  - **Description:** Grants permission to list all VPCs the specified Profile is associated to
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProfileResourceAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileResourceAssociations.html)  **
  - **Description:** Grants permission to list all the associations between the resources, such as DNS Firewall rule groups, private hosted zones, resolver rules, etc. for the given Profile ID
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProfiles](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfiles.html)  **
  - **Description:** Grants permission to list all the Profiles created by, and shared to the customer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags associated with the resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_TagResource.html)  **
  - **Description:** Grants permission to add a tag to the given resource
  - **Resource types (\*required):** [profile](#list_route53profiles-resource-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53profiles-aws_TagKeys)
  - **Resource types (\*required):** [profile-association](#list_route53profiles-resource-profile-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53profiles-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UntagResource.html)  **
  - **Description:** Grants permission to delete a tag from the given resource
  - **Resource types (\*required):** [profile](#list_route53profiles-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53profiles-aws_TagKeys)
  - **Resource types (\*required):** [profile-association](#list_route53profiles-resource-profile-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53profiles-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UpdateProfileResourceAssociation.html)  **
  - **Description:** Grants permission to update the Profile resource association name or the resource properties or both, if both name and resource properties are null, the api returns the existing Profile resource association
  - **Resource types (\*required):** 
  - **Condition keys:** [route53profiles:FirewallRuleGroupPriority](#list_route53profiles-route53profiles_FirewallRuleGroupPriority)<br />[route53profiles:HostedZoneDomains](#list_route53profiles-route53profiles_HostedZoneDomains)<br />[route53profiles:ResolverRuleDomains](#list_route53profiles-route53profiles_ResolverRuleDomains)<br />[route53profiles:ResourceTypes](#list_route53profiles-route53profiles_ResourceTypes)
  - **Access level:** Write



## Permission-only actions for Amazon Route 53 Profiles
<a name="list_route53profiles-permission-only-actions"></a>

The following actions are defined by Amazon Route 53 Profiles but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetProfilePolicy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sharing-profiles.html)  **
  - **Description:** Grants permission to read the RAM access control policy for a Profile
  - **Resource types (\*required):** [profile\*](#list_route53profiles-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutProfilePolicy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sharing-profiles.html)  **
  - **Description:** Grants permission to define the RAM access control policy for a Profile
  - **Resource types (\*required):** [profile\*](#list_route53profiles-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Route 53 Profiles
<a name="list_route53profiles-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [profile](https://docs.aws.amazon.com/Route53/latest/APIReference/#access-control-resources)  | arn:${Partition}:route53profiles:${Region}:${Account}:profile/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_route53profiles-aws_ResourceTag___TagKey_) | 
|  [profile-association](https://docs.aws.amazon.com/Route53/latest/APIReference/#access-control-resources)  | arn:${Partition}:route53profiles:${Region}:${Account}:profile-association/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_route53profiles-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Route 53 Profiles
<a name="list_route53profiles-policy-keys"></a>

Amazon Route 53 Profiles defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the presence of tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [route53profiles:FirewallRuleGroupPriority](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53profiles.html)  | Filters access by priority range of a Firewall Rule Group | Numeric | 
|   [route53profiles:HostedZoneDomains](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53profiles.html)  | Filters access by Hosted Zone domains | String | 
|   [route53profiles:ResolverRuleDomains](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53profiles.html)  | Filters access by Resolver Rule domains | String | 
|   [route53profiles:ResourceArns](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53profiles.html)  | Filters access by specific resource ARNs | ARN | 
|   [route53profiles:ResourceIds](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53profiles.html)  | Filters access by given VPCs | String | 
|   [route53profiles:ResourceTypes](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53profiles.html)  | Filters access by specific resource type. Possible options include 'HostedZone', 'FirewallRuleGroup', 'ResolverQueryLoggingConfig', 'ResolverRule', and 'VpcEndpoint' | String | 