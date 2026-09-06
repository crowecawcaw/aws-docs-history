

# Actions, resources, and condition keys for Amazon WorkLink
<a name="list_worklink"></a>

Amazon WorkLink (service prefix: `worklink`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/worklink/latest/ag/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/worklink/latest/api/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/worklink/latest/ag/configure-network.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/worklink/worklink.json) for this service.

**Topics**
+ [Actions defined by Amazon WorkLink](#list_worklink-actions-as-permissions)
+ [Permission-only actions for Amazon WorkLink](#list_worklink-permission-only-actions)
+ [Resource types defined by Amazon WorkLink](#list_worklink-resources-for-iam-policies)
+ [Condition keys for Amazon WorkLink](#list_worklink-policy-keys)

## Actions defined by Amazon WorkLink
<a name="list_worklink-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateDomain](https://docs.aws.amazon.com/worklink/latest/api/API_AssociateDomain.html)  **
  - **Description:** Grants permission to associate a domain with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateWebsiteAuthorizationProvider](https://docs.aws.amazon.com/worklink/latest/api/API_AssociateWebsiteAuthorizationProvider.html)  **
  - **Description:** Grants permission to associate a website authorization provider with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateWebsiteCertificateAuthority](https://docs.aws.amazon.com/worklink/latest/api/API_AssociateWebsiteCertificateAuthority.html)  **
  - **Description:** Grants permission to associate a website certificate authority with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateFleet](https://docs.aws.amazon.com/worklink/latest/api/API_CreateFleet.html)  **
  - **Description:** Grants permission to create an Amazon WorkLink fleet
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_worklink-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_worklink-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteFleet](https://docs.aws.amazon.com/worklink/latest/api/API_DeleteFleet.html)  **
  - **Description:** Grants permission to delete an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_worklink-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_worklink-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeAuditStreamConfiguration](https://docs.aws.amazon.com/worklink/latest/api/API_DescribeAuditStreamConfiguration.html)  **
  - **Description:** Grants permission to describe the audit stream configuration for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCompanyNetworkConfiguration](https://docs.aws.amazon.com/worklink/latest/api/API_DescribeCompanyNetworkConfiguration.html)  **
  - **Description:** Grants permission to describe the company network configuration for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDevice](https://docs.aws.amazon.com/worklink/latest/api/API_DescribeDevice.html)  **
  - **Description:** Grants permission to describe details of a device associated with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDevicePolicyConfiguration](https://docs.aws.amazon.com/worklink/latest/api/API_DescribeDevicePolicyConfiguration.html)  **
  - **Description:** Grants permission to describe the device policy configuration for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomain](https://docs.aws.amazon.com/worklink/latest/api/API_DescribeDomain.html)  **
  - **Description:** Grants permission to describe details about a domain associated with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFleetMetadata](https://docs.aws.amazon.com/worklink/latest/api/API_DescribeFleetMetadata.html)  **
  - **Description:** Grants permission to describe metadata of an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_worklink-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_worklink-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeIdentityProviderConfiguration](https://docs.aws.amazon.com/worklink/latest/api/API_DescribeIdentityProviderConfiguration.html)  **
  - **Description:** Grants permission to describe the identity provider configuration for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWebsiteCertificateAuthority](https://docs.aws.amazon.com/worklink/latest/api/API_DescribeWebsiteCertificateAuthority.html)  **
  - **Description:** Grants permission to describe a website certificate authority associated with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateDomain](https://docs.aws.amazon.com/worklink/latest/api/API_DisassociateDomain.html)  **
  - **Description:** Grants permission to disassociate a domain from an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateWebsiteAuthorizationProvider](https://docs.aws.amazon.com/worklink/latest/api/API_DisassociateWebsiteAuthorizationProvider.html)  **
  - **Description:** Grants permission to disassociate a website authorization provider from an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateWebsiteCertificateAuthority](https://docs.aws.amazon.com/worklink/latest/api/API_DisassociateWebsiteCertificateAuthority.html)  **
  - **Description:** Grants permission to disassociate a website certificate authority from an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListDevices](https://docs.aws.amazon.com/worklink/latest/api/API_ListDevices.html)  **
  - **Description:** Grants permission to list the devices associated with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomains](https://docs.aws.amazon.com/worklink/latest/api/API_ListDomains.html)  **
  - **Description:** Grants permission to list the associated domains for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFleets](https://docs.aws.amazon.com/worklink/latest/api/API_ListFleets.html)  **
  - **Description:** Grants permission to list the Amazon WorkLink fleets associated with the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/worklink/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWebsiteAuthorizationProviders](https://docs.aws.amazon.com/worklink/latest/api/API_ListWebsiteAuthorizationProviders.html)  **
  - **Description:** Grants permission to list the website authorization providers for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWebsiteCertificateAuthorities](https://docs.aws.amazon.com/worklink/latest/api/API_ListWebsiteCertificateAuthorities.html)  **
  - **Description:** Grants permission to list the website certificate authorities associated with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RestoreDomainAccess](https://docs.aws.amazon.com/worklink/latest/api/API_RestoreDomainAccess.html)  **
  - **Description:** Grants permission to restore access to a domain associated with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeDomainAccess](https://docs.aws.amazon.com/worklink/latest/api/API_RevokeDomainAccess.html)  **
  - **Description:** Grants permission to revoke access to a domain associated with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SignOutUser](https://docs.aws.amazon.com/worklink/latest/api/API_SignOutUser.html)  **
  - **Description:** Grants permission to sign out a user from an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/worklink/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to a resource
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_worklink-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_worklink-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/worklink/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from a resource
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_worklink-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAuditStreamConfiguration](https://docs.aws.amazon.com/worklink/latest/api/API_UpdateAuditStreamConfiguration.html)  **
  - **Description:** Grants permission to update the audit stream configuration for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCompanyNetworkConfiguration](https://docs.aws.amazon.com/worklink/latest/api/API_UpdateCompanyNetworkConfiguration.html)  **
  - **Description:** Grants permission to update the company network configuration for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDevicePolicyConfiguration](https://docs.aws.amazon.com/worklink/latest/api/API_UpdateDevicePolicyConfiguration.html)  **
  - **Description:** Grants permission to update the device policy configuration for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomainMetadata](https://docs.aws.amazon.com/worklink/latest/api/API_UpdateDomainMetadata.html)  **
  - **Description:** Grants permission to update the metadata for a domain associated with an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFleetMetadata](https://docs.aws.amazon.com/worklink/latest/api/API_UpdateFleetMetadata.html)  **
  - **Description:** Grants permission to update the metadata of an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIdentityProviderConfiguration](https://docs.aws.amazon.com/worklink/latest/api/API_UpdateIdentityProviderConfiguration.html)  **
  - **Description:** Grants permission to update the identity provider configuration for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon WorkLink
<a name="list_worklink-permission-only-actions"></a>

The following actions are defined by Amazon WorkLink but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [SearchEntity](https://docs.aws.amazon.com/worklink/latest/ag/manage-devices.html)  **
  - **Description:** Grants permission to list devices for an Amazon WorkLink fleet
  - **Resource types (\*required):** [fleet\*](#list_worklink-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_)
  - **Access level:** List



## Resource types defined by Amazon WorkLink
<a name="list_worklink-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [fleet](${ActionsDocRoot}API_CreateFleet.html)  | arn:${Partition}:worklink::${Account}:fleet/${FleetName} | [aws:ResourceTag/${TagKey}](#list_worklink-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon WorkLink
<a name="list_worklink-policy-keys"></a>

Amazon WorkLink defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of tag keys in the request | ArrayOfString | 