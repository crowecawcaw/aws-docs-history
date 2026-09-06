

# Actions, resources, and condition keys for AWS Marketplace Vendor Insights
<a name="list_vendor-insights"></a>

AWS Marketplace Vendor Insights (service prefix: `vendor-insights`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/marketplace/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/marketplace/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/marketplace/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/vendor-insights/vendor-insights.json) for this service.

**Topics**
+ [Actions defined by AWS Marketplace Vendor Insights](#list_vendor-insights-actions-as-permissions)
+ [Resource types defined by AWS Marketplace Vendor Insights](#list_vendor-insights-resources-for-iam-policies)
+ [Condition keys for AWS Marketplace Vendor Insights](#list_vendor-insights-policy-keys)

## Actions defined by AWS Marketplace Vendor Insights
<a name="list_vendor-insights-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivateSecurityProfile](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to activate the security profile
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write

- **   [AssociateDataSource](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to associate security profile with a data source
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataSource](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to create a new data source
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSecurityProfile](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to create a new security profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write

- **   [DeactivateSecurityProfile](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to deactivate the security profile
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDataSource](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to delete a data source
  - **Resource types (\*required):** [DataSource\*](#list_vendor-insights-resource-DataSource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write

- **   [DisassociateDataSource](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to disassociate security profile from a data source
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write

- **   [GetDataSource](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to retrieve the details of an existing data source
  - **Resource types (\*required):** [DataSource\*](#list_vendor-insights-resource-DataSource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Read

- **   [GetEntitledSecurityProfileSnapshot](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-vendor-insights-controlling-access.html)  **
  - **Description:** Grants permission to return the details of a security profile snapshot that requester is entitled to read
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Read

- **   [GetProfileAccessTerms](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-vendor-insights-controlling-access.html)  **
  - **Description:** Grants permission to get the access terms for a vendor insights profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSecurityProfile](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to return the details of an existing security profile
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Read

- **   [GetSecurityProfileSnapshot](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to return the details of a security profile snapshot
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Read

- **   [ListDataSources](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to list existing data sources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEntitledSecurityProfileSnapshots](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-vendor-insights-controlling-access.html)  **
  - **Description:** Grants permission to return the snapshot summary list for an existing security profile that requester is entitled to list
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** List

- **   [ListEntitledSecurityProfiles](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-vendor-insights-controlling-access.html)  **
  - **Description:** Grants permission to list entitled security profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSecurityProfileSnapshots](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to return the snapshot summary list for an existing security profile
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** List

- **   [ListSecurityProfiles](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to list existing security profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to list tags for vendor insights resource
  - **Resource types (\*required):** [DataSource](#list_vendor-insights-resource-DataSource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Resource types (\*required):** [SecurityProfile](#list_vendor-insights-resource-SecurityProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to tag vendor insights resource
  - **Resource types (\*required):** [DataSource](#list_vendor-insights-resource-DataSource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Resource types (\*required):** [SecurityProfile](#list_vendor-insights-resource-SecurityProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to untag vendor insights resource
  - **Resource types (\*required):** [DataSource](#list_vendor-insights-resource-DataSource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Resource types (\*required):** [SecurityProfile](#list_vendor-insights-resource-SecurityProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDataSource](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to update an existing data source
  - **Resource types (\*required):** [DataSource\*](#list_vendor-insights-resource-DataSource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateSecurityProfile](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to update the security profile
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateSecurityProfileSnapshotCreationConfiguration](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to update the security profile snapshot creation configuration
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateSecurityProfileSnapshotReleaseConfiguration](https://docs.aws.amazon.com/marketplace/latest/userguide/vendor-insights-seller-controlling-access.html)  **
  - **Description:** Grants permission to update the security profile snapshot release configuration
  - **Resource types (\*required):** [SecurityProfile\*](#list_vendor-insights-resource-SecurityProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys)
  - **Access level:** Write



## Resource types defined by AWS Marketplace Vendor Insights
<a name="list_vendor-insights-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [DataSource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacevendorinsights.html#awsmarketplacevendorinsights-resources-for-iam-policies)  | arn:${Partition}:vendor-insights:::data-source:${ResourceId} | [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys) | 
|  [SecurityProfile](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacevendorinsights.html#awsmarketplacevendorinsights-resources-for-iam-policies)  | arn:${Partition}:vendor-insights:::security-profile:${ResourceId} | [aws:RequestTag/${TagKey}](#list_vendor-insights-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vendor-insights-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vendor-insights-aws_TagKeys) | 

## Condition keys for AWS Marketplace Vendor Insights
<a name="list_vendor-insights-policy-keys"></a>

AWS Marketplace Vendor Insights defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 