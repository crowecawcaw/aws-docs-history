

# Actions, resources, and condition keys for AWS Route53 Global Resolver
<a name="list_route53globalresolver"></a>

AWS Route53 Global Resolver (service prefix: `route53globalresolver`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/Route53/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/route53globalresolver/route53globalresolver.json) for this service.

**Topics**
+ [API operations defined by AWS Route53 Global Resolver](#list_route53globalresolver-operations)
+ [Actions defined by AWS Route53 Global Resolver](#list_route53globalresolver-actions-as-permissions)
+ [Permission-only actions for AWS Route53 Global Resolver](#list_route53globalresolver-permission-only-actions)
+ [Resource types defined by AWS Route53 Global Resolver](#list_route53globalresolver-resources-for-iam-policies)
+ [Condition keys for AWS Route53 Global Resolver](#list_route53globalresolver-policy-keys)

## API operations defined by AWS Route53 Global Resolver
<a name="list_route53globalresolver-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_route53globalresolver-actions-as-permissions).




- **   AssociateHostedZone  **
  - **IAM action:**  [route53globalresolver:AssociateHostedZone](#list_route53globalresolver-action-AssociateHostedZone) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchCreateFirewallRule  **
  - **IAM action:**  [route53globalresolver:BatchCreateFirewallRule](#list_route53globalresolver-action-BatchCreateFirewallRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteFirewallRule  **
  - **IAM action:**  [route53globalresolver:BatchDeleteFirewallRule](#list_route53globalresolver-action-BatchDeleteFirewallRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateFirewallRule  **
  - **IAM action:**  [route53globalresolver:BatchUpdateFirewallRule](#list_route53globalresolver-action-BatchUpdateFirewallRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccessSource  **
  - **IAM action:**  [route53globalresolver:CreateAccessSource](#list_route53globalresolver-action-CreateAccessSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53globalresolver:TagResource](#list_route53globalresolver-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAccessToken  **
  - **IAM action:**  [route53globalresolver:CreateAccessToken](#list_route53globalresolver-action-CreateAccessToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53globalresolver:TagResource](#list_route53globalresolver-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDNSView  **
  - **IAM action:**  [route53globalresolver:CreateDNSView](#list_route53globalresolver-action-CreateDNSView)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53globalresolver:TagResource](#list_route53globalresolver-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFirewallDomainList  **
  - **IAM action:**  [route53globalresolver:CreateFirewallDomainList](#list_route53globalresolver-action-CreateFirewallDomainList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53globalresolver:TagResource](#list_route53globalresolver-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFirewallRule  **
  - **IAM action:**  [route53globalresolver:CreateFirewallRule](#list_route53globalresolver-action-CreateFirewallRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGlobalResolver  **
  - **IAM action:**  [route53globalresolver:CreateGlobalResolver](#list_route53globalresolver-action-CreateGlobalResolver)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53globalresolver:TagResource](#list_route53globalresolver-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAccessSource  **
  - **IAM action:**  [route53globalresolver:DeleteAccessSource](#list_route53globalresolver-action-DeleteAccessSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccessToken  **
  - **IAM action:**  [route53globalresolver:DeleteAccessToken](#list_route53globalresolver-action-DeleteAccessToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDNSView  **
  - **IAM action:**  [route53globalresolver:DeleteDNSView](#list_route53globalresolver-action-DeleteDNSView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFirewallDomainList  **
  - **IAM action:**  [route53globalresolver:DeleteFirewallDomainList](#list_route53globalresolver-action-DeleteFirewallDomainList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFirewallRule  **
  - **IAM action:**  [route53globalresolver:DeleteFirewallRule](#list_route53globalresolver-action-DeleteFirewallRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGlobalResolver  **
  - **IAM action:**  [route53globalresolver:DeleteGlobalResolver](#list_route53globalresolver-action-DeleteGlobalResolver) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableDNSView  **
  - **IAM action:**  [route53globalresolver:DisableDNSView](#list_route53globalresolver-action-DisableDNSView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateHostedZone  **
  - **IAM action:**  [route53globalresolver:DisassociateHostedZone](#list_route53globalresolver-action-DisassociateHostedZone) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableDNSView  **
  - **IAM action:**  [route53globalresolver:EnableDNSView](#list_route53globalresolver-action-EnableDNSView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccessSource  **
  - **IAM action:**  [route53globalresolver:GetAccessSource](#list_route53globalresolver-action-GetAccessSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessToken  **
  - **IAM action:**  [route53globalresolver:GetAccessToken](#list_route53globalresolver-action-GetAccessToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDNSView  **
  - **IAM action:**  [route53globalresolver:GetDNSView](#list_route53globalresolver-action-GetDNSView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFirewallDomainList  **
  - **IAM action:**  [route53globalresolver:GetFirewallDomainList](#list_route53globalresolver-action-GetFirewallDomainList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFirewallRule  **
  - **IAM action:**  [route53globalresolver:GetFirewallRule](#list_route53globalresolver-action-GetFirewallRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGlobalResolver  **
  - **IAM action:**  [route53globalresolver:GetGlobalResolver](#list_route53globalresolver-action-GetGlobalResolver) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHostedZoneAssociation  **
  - **IAM action:**  [route53globalresolver:GetHostedZoneAssociation](#list_route53globalresolver-action-GetHostedZoneAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedFirewallDomainList  **
  - **IAM action:**  [route53globalresolver:GetManagedFirewallDomainList](#list_route53globalresolver-action-GetManagedFirewallDomainList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportFirewallDomains  **
  - **IAM action:**  [route53globalresolver:ImportFirewallDomains](#list_route53globalresolver-action-ImportFirewallDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAccessSources  **
  - **IAM action:**  [route53globalresolver:ListAccessSources](#list_route53globalresolver-action-ListAccessSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccessTokens  **
  - **IAM action:**  [route53globalresolver:ListAccessTokens](#list_route53globalresolver-action-ListAccessTokens) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDNSViews  **
  - **IAM action:**  [route53globalresolver:ListDNSViews](#list_route53globalresolver-action-ListDNSViews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFirewallDomainLists  **
  - **IAM action:**  [route53globalresolver:ListFirewallDomainLists](#list_route53globalresolver-action-ListFirewallDomainLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFirewallDomains  **
  - **IAM action:**  [route53globalresolver:ListFirewallDomains](#list_route53globalresolver-action-ListFirewallDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFirewallRules  **
  - **IAM action:**  [route53globalresolver:ListFirewallRules](#list_route53globalresolver-action-ListFirewallRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGlobalResolvers  **
  - **IAM action:**  [route53globalresolver:ListGlobalResolvers](#list_route53globalresolver-action-ListGlobalResolvers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHostedZoneAssociations  **
  - **IAM action:**  [route53globalresolver:ListHostedZoneAssociations](#list_route53globalresolver-action-ListHostedZoneAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedFirewallDomainLists  **
  - **IAM action:**  [route53globalresolver:ListManagedFirewallDomainLists](#list_route53globalresolver-action-ListManagedFirewallDomainLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [route53globalresolver:ListTagsForResource](#list_route53globalresolver-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [route53globalresolver:TagResource](#list_route53globalresolver-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [route53globalresolver:UntagResource](#list_route53globalresolver-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccessSource  **
  - **IAM action:**  [route53globalresolver:UpdateAccessSource](#list_route53globalresolver-action-UpdateAccessSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAccessToken  **
  - **IAM action:**  [route53globalresolver:UpdateAccessToken](#list_route53globalresolver-action-UpdateAccessToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDNSView  **
  - **IAM action:**  [route53globalresolver:UpdateDNSView](#list_route53globalresolver-action-UpdateDNSView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFirewallDomains  **
  - **IAM action:**  [route53globalresolver:UpdateFirewallDomains](#list_route53globalresolver-action-UpdateFirewallDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFirewallRule  **
  - **IAM action:**  [route53globalresolver:UpdateFirewallRule](#list_route53globalresolver-action-UpdateFirewallRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGlobalResolver  **
  - **IAM action:**  [route53globalresolver:UpdateGlobalResolver](#list_route53globalresolver-action-UpdateGlobalResolver) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateHostedZoneAssociation  **
  - **IAM action:**  [route53globalresolver:UpdateHostedZoneAssociation](#list_route53globalresolver-action-UpdateHostedZoneAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Route53 Global Resolver
<a name="list_route53globalresolver-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_AssociateHostedZone)  **
  - **Description:** Grants permission to associate a resource to a hosted zone
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchCreateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchCreateFirewallRule)  **
  - **Description:** Grants permission to create multiple firewall rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchDeleteFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchDeleteFirewallRule)  **
  - **Description:** Grants permission to delete multiple firewall rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchUpdateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchUpdateFirewallRule)  **
  - **Description:** Grants permission to update multiple firewall rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAccessSource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateAccessSource)  **
  - **Description:** Grants permission to create an access source
  - **Resource types (\*required):** [dns-view\*](#list_route53globalresolver-resource-dns-view)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53globalresolver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAccessToken](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateAccessToken)  **
  - **Description:** Grants permission to create an access token
  - **Resource types (\*required):** [access-token\*](#list_route53globalresolver-resource-access-token)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53globalresolver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateDNSView)  **
  - **Description:** Grants permission to create a dns view
  - **Resource types (\*required):** [dns-view\*](#list_route53globalresolver-resource-dns-view)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53globalresolver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateFirewallDomainList)  **
  - **Description:** Grants permission to create a firewall domain list
  - **Resource types (\*required):** [firewall-domain-list\*](#list_route53globalresolver-resource-firewall-domain-list)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53globalresolver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateFirewallRule)  **
  - **Description:** Grants permission to create a firewall rule
  - **Resource types (\*required):** [dns-view\*](#list_route53globalresolver-resource-dns-view) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [firewall-domain-list](#list_route53globalresolver-resource-firewall-domain-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateGlobalResolver)  **
  - **Description:** Grants permission to create a global resolver
  - **Resource types (\*required):** [global-resolver\*](#list_route53globalresolver-resource-global-resolver)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53globalresolver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccessSource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteAccessSource)  **
  - **Description:** Grants permission to delete an access source
  - **Resource types (\*required):** [access-source\*](#list_route53globalresolver-resource-access-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAccessToken](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteAccessToken)  **
  - **Description:** Grants permission to delete an access token
  - **Resource types (\*required):** [access-token\*](#list_route53globalresolver-resource-access-token)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteDNSView)  **
  - **Description:** Grants permission to delete a dns view
  - **Resource types (\*required):** [dns-view\*](#list_route53globalresolver-resource-dns-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteFirewallDomainList)  **
  - **Description:** Grants permission to delete a firewall domain list
  - **Resource types (\*required):** [firewall-domain-list\*](#list_route53globalresolver-resource-firewall-domain-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteFirewallRule)  **
  - **Description:** Grants permission to delete a firewall rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteGlobalResolver)  **
  - **Description:** Grants permission to delete a global resolver
  - **Resource types (\*required):** [global-resolver\*](#list_route53globalresolver-resource-global-resolver)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DisableDNSView)  **
  - **Description:** Grants permission to disable a dns view
  - **Resource types (\*required):** [dns-view\*](#list_route53globalresolver-resource-dns-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DisassociateHostedZone)  **
  - **Description:** Grants permission to disassociate a hosted zone from a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnableDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_EnableDNSView)  **
  - **Description:** Grants permission to enable a dns view
  - **Resource types (\*required):** [dns-view\*](#list_route53globalresolver-resource-dns-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccessSource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetAccessSource)  **
  - **Description:** Grants permission to get an access source
  - **Resource types (\*required):** [access-source\*](#list_route53globalresolver-resource-access-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAccessToken](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetAccessToken)  **
  - **Description:** Grants permission to get an access token
  - **Resource types (\*required):** [access-token\*](#list_route53globalresolver-resource-access-token)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetDNSView)  **
  - **Description:** Grants permission to get a dns view
  - **Resource types (\*required):** [dns-view\*](#list_route53globalresolver-resource-dns-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetFirewallDomainList)  **
  - **Description:** Grants permission to get a firewall domain list
  - **Resource types (\*required):** [firewall-domain-list\*](#list_route53globalresolver-resource-firewall-domain-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetFirewallRule)  **
  - **Description:** Grants permission to get a firewall rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetGlobalResolver)  **
  - **Description:** Grants permission to get a global resolver
  - **Resource types (\*required):** [global-resolver\*](#list_route53globalresolver-resource-global-resolver)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHostedZoneAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetHostedZoneAssociation)  **
  - **Description:** Grants permission to get a hosted zone association
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetManagedFirewallDomainList](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetManagedFirewallDomainList)  **
  - **Description:** Grants permission to get a managed firewall domain list
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ImportFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ImportFirewallDomains)  **
  - **Description:** Grants permission to import firewall domains from an S3 bucket
  - **Resource types (\*required):** [firewall-domain-list\*](#list_route53globalresolver-resource-firewall-domain-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAccessSources](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListAccessSources)  **
  - **Description:** Grants permission to list access sources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAccessTokens](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListAccessTokens)  **
  - **Description:** Grants permission to list access tokens
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDNSViews](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListDNSViews)  **
  - **Description:** Grants permission to list dns views
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFirewallDomainLists](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListFirewallDomainLists)  **
  - **Description:** Grants permission to list firewall domain lists
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListFirewallDomains)  **
  - **Description:** Grants permission to list firewall domains
  - **Resource types (\*required):** [firewall-domain-list\*](#list_route53globalresolver-resource-firewall-domain-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFirewallRules](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListFirewallRules)  **
  - **Description:** Grants permission to list firewall rules
  - **Resource types (\*required):** [dns-view\*](#list_route53globalresolver-resource-dns-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGlobalResolvers](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListGlobalResolvers)  **
  - **Description:** Grants permission to list global resolvers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHostedZoneAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListHostedZoneAssociations)  **
  - **Description:** Grants permission to list hosted zone associations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedFirewallDomainLists](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListManagedFirewallDomainLists)  **
  - **Description:** Grants permission to list managed firewall domain lists
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListTagsForResource)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [access-source](#list_route53globalresolver-resource-access-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [access-token](#list_route53globalresolver-resource-access-token) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dns-view](#list_route53globalresolver-resource-dns-view) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [firewall-domain-list](#list_route53globalresolver-resource-firewall-domain-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-resolver](#list_route53globalresolver-resource-global-resolver) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_TagResource)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [access-source](#list_route53globalresolver-resource-access-source) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53globalresolver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Resource types (\*required):** [access-token](#list_route53globalresolver-resource-access-token) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53globalresolver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Resource types (\*required):** [dns-view](#list_route53globalresolver-resource-dns-view) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53globalresolver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Resource types (\*required):** [firewall-domain-list](#list_route53globalresolver-resource-firewall-domain-list) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53globalresolver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Resource types (\*required):** [global-resolver](#list_route53globalresolver-resource-global-resolver) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53globalresolver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UntagResource)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [access-source](#list_route53globalresolver-resource-access-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Resource types (\*required):** [access-token](#list_route53globalresolver-resource-access-token) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Resource types (\*required):** [dns-view](#list_route53globalresolver-resource-dns-view) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Resource types (\*required):** [firewall-domain-list](#list_route53globalresolver-resource-firewall-domain-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Resource types (\*required):** [global-resolver](#list_route53globalresolver-resource-global-resolver) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53globalresolver-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccessSource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateAccessSource)  **
  - **Description:** Grants permission to update an access source
  - **Resource types (\*required):** [access-source\*](#list_route53globalresolver-resource-access-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAccessToken](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateAccessToken)  **
  - **Description:** Grants permission to update an access token
  - **Resource types (\*required):** [access-token\*](#list_route53globalresolver-resource-access-token)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDNSView](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateDNSView)  **
  - **Description:** Grants permission to update a dns view
  - **Resource types (\*required):** [dns-view\*](#list_route53globalresolver-resource-dns-view)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFirewallDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateFirewallDomains)  **
  - **Description:** Grants permission to update firewall domains
  - **Resource types (\*required):** [firewall-domain-list\*](#list_route53globalresolver-resource-firewall-domain-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFirewallRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateFirewallRule)  **
  - **Description:** Grants permission to update an firewall rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateGlobalResolver)  **
  - **Description:** Grants permission to update a global resolver
  - **Resource types (\*required):** [global-resolver\*](#list_route53globalresolver-resource-global-resolver)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateHostedZoneAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateHostedZoneAssociation)  **
  - **Description:** Grants permission to update a hosted zone association
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for AWS Route53 Global Resolver
<a name="list_route53globalresolver-permission-only-actions"></a>

The following actions are defined by AWS Route53 Global Resolver but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_AllowVendedLogDeliveryForResource.html)  **
  - **Description:** Grants permission to deliver logs for a global resolver
  - **Resource types (\*required):** [global-resolver\*](#list_route53globalresolver-resource-global-resolver)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write



## Resource types defined by AWS Route53 Global Resolver
<a name="list_route53globalresolver-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [access-source](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_AccessSource.html)  | arn:${Partition}:route53globalresolver::${Account}:access-source/${Id} | [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_) | 
|  [access-token](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_AccessToken.html)  | arn:${Partition}:route53globalresolver::${Account}:access-token/${Id} | [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_) | 
|  [dns-view](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DNSView.html)  | arn:${Partition}:route53globalresolver::${Account}:dns-view/${Id} | [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_) | 
|  [firewall-domain-list](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_FirewallDomainList.html)  | arn:${Partition}:route53globalresolver::${Account}:firewall-domain-list/${Id} | [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_) | 
|  [global-resolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GlobalResolver.html)  | arn:${Partition}:route53globalresolver::${Account}:global-resolver/${Id} | [aws:ResourceTag/${TagKey}](#list_route53globalresolver-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Route53 Global Resolver
<a name="list_route53globalresolver-policy-keys"></a>

AWS Route53 Global Resolver defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 