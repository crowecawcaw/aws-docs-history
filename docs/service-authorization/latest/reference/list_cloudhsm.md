

# Actions, resources, and condition keys for AWS CloudHSM
<a name="list_cloudhsm"></a>

AWS CloudHSM (service prefix: `cloudhsm`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cloudhsm/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/identity-access-management.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudhsm/cloudhsm.json) for this service.

**Topics**
+ [API operations defined by AWS CloudHSM](#list_cloudhsm-operations)
+ [Actions defined by AWS CloudHSM](#list_cloudhsm-actions-as-permissions)
+ [Resource types defined by AWS CloudHSM](#list_cloudhsm-resources-for-iam-policies)
+ [Condition keys for AWS CloudHSM](#list_cloudhsm-policy-keys)

## API operations defined by AWS CloudHSM
<a name="list_cloudhsm-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudhsm-actions-as-permissions).




- **   CreateHsm  **
  - **SDK client:** cloudhsm
  - **IAM action:**  [cloudhsm:CreateHsm](#list_cloudhsm-action-CreateHsm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:AuthorizeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:AuthorizeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:CreateNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:CreateSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:DeleteNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:DescribeNetworkInterfaces](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:RevokeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteHsm  **
  - **SDK client:** cloudhsm
  - **IAM action:**  [cloudhsm:DeleteHsm](#list_cloudhsm-action-DeleteHsm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:DeleteNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopyBackupToRegion  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:CopyBackupToRegion](#list_cloudhsm-action-CopyBackupToRegion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudhsm:TagResource](#list_cloudhsm-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudhsm:UntagResource](#list_cloudhsm-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCluster  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:CreateCluster](#list_cloudhsm-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudhsm:TagResource](#list_cloudhsm-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ec2:AuthorizeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:AuthorizeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:CreateSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:RevokeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateHsm  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:CreateHsm](#list_cloudhsm-action-CreateHsm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:AuthorizeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:AuthorizeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:CreateNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:CreateSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:DeleteNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:DescribeNetworkInterfaces](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:RevokeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBackup  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:DeleteBackup](#list_cloudhsm-action-DeleteBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCluster  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:DeleteCluster](#list_cloudhsm-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHsm  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:DeleteHsm](#list_cloudhsm-action-DeleteHsm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:DeleteNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteResourcePolicy  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:DeleteResourcePolicy](#list_cloudhsm-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DescribeBackups  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:DescribeBackups](#list_cloudhsm-action-DescribeBackups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusters  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:DescribeClusters](#list_cloudhsm-action-DescribeClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:GetResourcePolicy](#list_cloudhsm-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InitializeCluster  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:InitializeCluster](#list_cloudhsm-action-InitializeCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListTags  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:ListTags](#list_cloudhsm-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ModifyBackupAttributes  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:ModifyBackupAttributes](#list_cloudhsm-action-ModifyBackupAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyCluster  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:ModifyCluster](#list_cloudhsm-action-ModifyCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:PutResourcePolicy](#list_cloudhsm-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RestoreBackup  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:RestoreBackup](#list_cloudhsm-action-RestoreBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:TagResource](#list_cloudhsm-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** cloudhsmv2
  - **IAM action:**  [cloudhsm:UntagResource](#list_cloudhsm-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS CloudHSM
<a name="list_cloudhsm-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CopyBackupToRegion](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CopyBackupToRegion.html)  **
  - **Description:** Grants permission to create a copy of a backup in the specified region
  - **Resource types (\*required):** [backup\*](#list_cloudhsm-resource-backup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudhsm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudhsm-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCluster](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permission to create a new AWS CloudHSM cluster
  - **Resource types (\*required):** [backup](#list_cloudhsm-resource-backup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudhsm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudhsm-aws_TagKeys)
  - **Access level:** Write

- **   [CreateHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm.html)  **
  - **Description:** Grants permission to create a new hardware security module (HSM) in the specified AWS CloudHSM cluster
  - **Resource types (\*required):** [cluster\*](#list_cloudhsm-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBackup](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DeleteBackup.html)  **
  - **Description:** Grants permission to delete the specified CloudHSM backup
  - **Resource types (\*required):** [backup\*](#list_cloudhsm-resource-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DeleteCluster.html)  **
  - **Description:** Grants permission to delete the specified AWS CloudHSM cluster
  - **Resource types (\*required):** [cluster\*](#list_cloudhsm-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DeleteHsm.html)  **
  - **Description:** Grants permission to delete the specified HSM
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete the policy attached to CloudHSM resources
  - **Resource types (\*required):** [backup\*](#list_cloudhsm-resource-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DescribeBackups](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeBackups.html)  **
  - **Description:** Grants permission to get information about backups of AWS CloudHSM clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeClusters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html)  **
  - **Description:** Grants permission to get information about AWS CloudHSM clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get information about the policy attached to a AWS CloudHSM resource
  - **Resource types (\*required):** [backup\*](#list_cloudhsm-resource-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InitializeCluster](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_InitializeCluster.html)  **
  - **Description:** Grants permission to claim an AWS CloudHSM cluster
  - **Resource types (\*required):** [cluster\*](#list_cloudhsm-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListTags](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_ListTags.html)  **
  - **Description:** Grants permission to get a list of tags for the specified AWS CloudHSM cluster
  - **Resource types (\*required):** [backup](#list_cloudhsm-resource-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_cloudhsm-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ModifyBackupAttributes](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_ModifyBackupAttributes.html)  **
  - **Description:** Grants permission to modify attributes for an AWS CloudHSM backup
  - **Resource types (\*required):** [backup\*](#list_cloudhsm-resource-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyCluster](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_ModifyCluster.html)  **
  - **Description:** Grants permission to modify AWS CloudHSM cluster
  - **Resource types (\*required):** [cluster\*](#list_cloudhsm-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach a policy to an AWS CloudHSM resource
  - **Resource types (\*required):** [backup\*](#list_cloudhsm-resource-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RestoreBackup](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_RestoreBackup.html)  **
  - **Description:** Grants permission to restore the specified CloudHSM backup
  - **Resource types (\*required):** [backup\*](#list_cloudhsm-resource-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or overwrite one or more tags for the specified AWS CloudHSM cluster
  - **Resource types (\*required):** [backup](#list_cloudhsm-resource-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudhsm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudhsm-aws_TagKeys)
  - **Resource types (\*required):** [cluster](#list_cloudhsm-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudhsm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudhsm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tag or tags from the specified AWS CloudHSM cluster
  - **Resource types (\*required):** [backup](#list_cloudhsm-resource-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudhsm-aws_TagKeys)
  - **Resource types (\*required):** [cluster](#list_cloudhsm-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudhsm-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS CloudHSM
<a name="list_cloudhsm-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [backup](https://docs.aws.amazon.com/cloudhsm/latest/userguide/backups.html)  | arn:${Partition}:cloudhsm:${Region}:${Account}:backup/${CloudHsmBackupInstanceName} | [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_) | 
|  [cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/clusters.html)  | arn:${Partition}:cloudhsm:${Region}:${Account}:cluster/${CloudHsmClusterInstanceName} | [aws:ResourceTag/${TagKey}](#list_cloudhsm-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS CloudHSM
<a name="list_cloudhsm-policy-keys"></a>

AWS CloudHSM defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 