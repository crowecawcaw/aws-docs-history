

# Actions, resources, and condition keys for AWS Elemental MediaPackage VOD
<a name="list_mediapackage-vod"></a>

AWS Elemental MediaPackage VOD (service prefix: `mediapackage-vod`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mediapackage/latest/ug/setting-up.html#setting-up-create-iam-user) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mediapackage-vod/mediapackage-vod.json) for this service.

**Topics**
+ [API operations defined by AWS Elemental MediaPackage VOD](#list_mediapackage-vod-operations)
+ [Actions defined by AWS Elemental MediaPackage VOD](#list_mediapackage-vod-actions-as-permissions)
+ [Resource types defined by AWS Elemental MediaPackage VOD](#list_mediapackage-vod-resources-for-iam-policies)
+ [Condition keys for AWS Elemental MediaPackage VOD](#list_mediapackage-vod-policy-keys)

## API operations defined by AWS Elemental MediaPackage VOD
<a name="list_mediapackage-vod-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mediapackage-vod-actions-as-permissions).




- **   ConfigureLogs  **
  - **IAM action:**  [mediapackage-vod:ConfigureLogs](#list_mediapackage-vod-action-ConfigureLogs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAsset  **
  - **IAM action:**  [mediapackage-vod:CreateAsset](#list_mediapackage-vod-action-CreateAsset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediapackage-vod:TagResource](#list_mediapackage-vod-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediapackage-vod.amazonaws.com / **Access level:** Write

- **   CreatePackagingConfiguration  **
  - **IAM action:**  [mediapackage-vod:CreatePackagingConfiguration](#list_mediapackage-vod-action-CreatePackagingConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediapackage-vod:TagResource](#list_mediapackage-vod-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediapackage-vod.amazonaws.com / **Access level:** Write

- **   CreatePackagingGroup  **
  - **IAM action:**  [mediapackage-vod:CreatePackagingGroup](#list_mediapackage-vod-action-CreatePackagingGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediapackage-vod:TagResource](#list_mediapackage-vod-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediapackage-vod.amazonaws.com / **Access level:** Write

- **   DeleteAsset  **
  - **IAM action:**  [mediapackage-vod:DeleteAsset](#list_mediapackage-vod-action-DeleteAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePackagingConfiguration  **
  - **IAM action:**  [mediapackage-vod:DeletePackagingConfiguration](#list_mediapackage-vod-action-DeletePackagingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePackagingGroup  **
  - **IAM action:**  [mediapackage-vod:DeletePackagingGroup](#list_mediapackage-vod-action-DeletePackagingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAsset  **
  - **IAM action:**  [mediapackage-vod:DescribeAsset](#list_mediapackage-vod-action-DescribeAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePackagingConfiguration  **
  - **IAM action:**  [mediapackage-vod:DescribePackagingConfiguration](#list_mediapackage-vod-action-DescribePackagingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePackagingGroup  **
  - **IAM action:**  [mediapackage-vod:DescribePackagingGroup](#list_mediapackage-vod-action-DescribePackagingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssets  **
  - **IAM action:**  [mediapackage-vod:ListAssets](#list_mediapackage-vod-action-ListAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPackagingConfigurations  **
  - **IAM action:**  [mediapackage-vod:ListPackagingConfigurations](#list_mediapackage-vod-action-ListPackagingConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPackagingGroups  **
  - **IAM action:**  [mediapackage-vod:ListPackagingGroups](#list_mediapackage-vod-action-ListPackagingGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [mediapackage-vod:ListTagsForResource](#list_mediapackage-vod-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [mediapackage-vod:TagResource](#list_mediapackage-vod-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [mediapackage-vod:UntagResource](#list_mediapackage-vod-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdatePackagingGroup  **
  - **IAM action:**  [mediapackage-vod:UpdatePackagingGroup](#list_mediapackage-vod-action-UpdatePackagingGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediapackage-vod.amazonaws.com / **Access level:** Write



## Actions defined by AWS Elemental MediaPackage VOD
<a name="list_mediapackage-vod-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ConfigureLogs](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_groups-id-configure_logs.html#packaging_groups-id-configure_logsput)  **
  - **Description:** Grants permission to configure egress access logs for a PackagingGroup
  - **Resource types (\*required):** [packaging-groups\*](#list_mediapackage-vod-resource-packaging-groups)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAsset](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/assets.html#assetspost)  **
  - **Description:** Grants permission to create an asset in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-vod-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-vod-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePackagingConfiguration](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_configurations.html#packaging_configurationspost)  **
  - **Description:** Grants permission to create a packaging configuration in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-vod-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-vod-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePackagingGroup](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_groups.html#packaging_groupspost)  **
  - **Description:** Grants permission to create a packaging group in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-vod-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-vod-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAsset](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/assets-id.html#assets-iddelete)  **
  - **Description:** Grants permission to delete an asset in AWS Elemental MediaPackage
  - **Resource types (\*required):** [assets\*](#list_mediapackage-vod-resource-assets)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePackagingConfiguration](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_configurations-id.html#packaging_configurations-iddelete)  **
  - **Description:** Grants permission to delete a packaging configuration in AWS Elemental MediaPackage
  - **Resource types (\*required):** [packaging-configurations\*](#list_mediapackage-vod-resource-packaging-configurations)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePackagingGroup](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_groups-id.html#packaging_groups-iddelete)  **
  - **Description:** Grants permission to delete a packaging group in AWS Elemental MediaPackage
  - **Resource types (\*required):** [packaging-groups\*](#list_mediapackage-vod-resource-packaging-groups)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAsset](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/assets-id.html#assets-idget)  **
  - **Description:** Grants permission to view the details of an asset in AWS Elemental MediaPackage
  - **Resource types (\*required):** [assets\*](#list_mediapackage-vod-resource-assets)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePackagingConfiguration](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_configurations-id.html#packaging_configurations-idget)  **
  - **Description:** Grants permission to view the details of a packaging configuration in AWS Elemental MediaPackage
  - **Resource types (\*required):** [packaging-configurations\*](#list_mediapackage-vod-resource-packaging-configurations)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePackagingGroup](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_groups-id.html#packaging_groups-idget)  **
  - **Description:** Grants permission to view the details of a packaging group in AWS Elemental MediaPackage
  - **Resource types (\*required):** [packaging-groups\*](#list_mediapackage-vod-resource-packaging-groups)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAssets](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/assets.html#assetsget)  **
  - **Description:** Grants permission to view a list of assets in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPackagingConfigurations](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_configurations.html#packaging_configurationsget)  **
  - **Description:** Grants permission to view a list of packaging configurations in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPackagingGroups](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_groups.html#packaging_groupsget)  **
  - **Description:** Grants permission to view a list of packaging groups in AWS Elemental MediaPackage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/tags-resource-arn.html#tags-resource-arnget)  **
  - **Description:** Grants permission to list the tags assigned to a PackagingGroup, PackagingConfiguration, or Asset
  - **Resource types (\*required):** [assets](#list_mediapackage-vod-resource-assets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [packaging-configurations](#list_mediapackage-vod-resource-packaging-configurations) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [packaging-groups](#list_mediapackage-vod-resource-packaging-groups) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/tags-resource-arn.html#tags-resource-arnpost)  **
  - **Description:** Grants permission to assign tags to a PackagingGroup, PackagingConfiguration, or Asset
  - **Resource types (\*required):** [assets](#list_mediapackage-vod-resource-assets) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-vod-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-vod-aws_TagKeys)
  - **Resource types (\*required):** [packaging-configurations](#list_mediapackage-vod-resource-packaging-configurations) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-vod-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-vod-aws_TagKeys)
  - **Resource types (\*required):** [packaging-groups](#list_mediapackage-vod-resource-packaging-groups) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediapackage-vod-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-vod-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/tags-resource-arn.html#tags-resource-arndelete)  **
  - **Description:** Grants permission to delete tags from a PackagingGroup, PackagingConfiguration, or Asset
  - **Resource types (\*required):** [assets](#list_mediapackage-vod-resource-assets) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-vod-aws_TagKeys)
  - **Resource types (\*required):** [packaging-configurations](#list_mediapackage-vod-resource-packaging-configurations) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-vod-aws_TagKeys)
  - **Resource types (\*required):** [packaging-groups](#list_mediapackage-vod-resource-packaging-groups) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediapackage-vod-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdatePackagingGroup](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_groups-id.html#packaging_groups-idput)  **
  - **Description:** Grants permission to update a packaging group in AWS Elemental MediaPackage
  - **Resource types (\*required):** [packaging-groups\*](#list_mediapackage-vod-resource-packaging-groups)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Elemental MediaPackage VOD
<a name="list_mediapackage-vod-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [assets](https://docs.aws.amazon.com/mediapackage/latest/ug/asset.html)  | arn:${Partition}:mediapackage-vod:${Region}:${Account}:assets/${AssetIdentifier} | [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_) | 
|  [packaging-configurations](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig.html)  | arn:${Partition}:mediapackage-vod:${Region}:${Account}:packaging-configurations/${PackagingConfigurationIdentifier} | [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_) | 
|  [packaging-groups](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group.html)  | arn:${Partition}:mediapackage-vod:${Region}:${Account}:packaging-groups/${PackagingGroupIdentifier} | [aws:ResourceTag/${TagKey}](#list_mediapackage-vod-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Elemental MediaPackage VOD
<a name="list_mediapackage-vod-policy-keys"></a>

AWS Elemental MediaPackage VOD defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of tag keys in the request | ArrayOfString | 