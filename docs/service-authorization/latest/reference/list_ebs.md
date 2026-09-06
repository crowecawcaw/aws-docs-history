

# Actions, resources, and condition keys for Amazon Elastic Block Store
<a name="list_ebs"></a>

Amazon Elastic Block Store (service prefix: `ebs`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ebs/latest/APIReference/Welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ebs/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-accessing-snapshot.html#ebsapi-permissions) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ebs/ebs.json) for this service.

**Topics**
+ [API operations defined by Amazon Elastic Block Store](#list_ebs-operations)
+ [Actions defined by Amazon Elastic Block Store](#list_ebs-actions-as-permissions)
+ [Resource types defined by Amazon Elastic Block Store](#list_ebs-resources-for-iam-policies)
+ [Condition keys for Amazon Elastic Block Store](#list_ebs-policy-keys)

## API operations defined by Amazon Elastic Block Store
<a name="list_ebs-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ebs-actions-as-permissions).




- **   CompleteSnapshot  **
  - **IAM action:**  [ebs:CompleteSnapshot](#list_ebs-action-CompleteSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetSnapshotBlock  **
  - **IAM action:**  [ebs:GetSnapshotBlock](#list_ebs-action-GetSnapshotBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListChangedBlocks  **
  - **IAM action:**  [ebs:ListChangedBlocks](#list_ebs-action-ListChangedBlocks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSnapshotBlocks  **
  - **IAM action:**  [ebs:ListSnapshotBlocks](#list_ebs-action-ListSnapshotBlocks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutSnapshotBlock  **
  - **IAM action:**  [ebs:PutSnapshotBlock](#list_ebs-action-PutSnapshotBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSnapshot  **
  - **IAM action:**  [ebs:StartSnapshot](#list_ebs-action-StartSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ec2:CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write



## Actions defined by Amazon Elastic Block Store
<a name="list_ebs-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CompleteSnapshot](https://docs.aws.amazon.com/ebs/latest/APIReference/API_CompleteSnapshot.html)  **
  - **Description:** Grants permission to seal and complete the snapshot after all of the required blocks of data have been written to it
  - **Resource types (\*required):** [snapshot\*](#list_ebs-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ebs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ebs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ebs-aws_TagKeys)<br />[ebs:Description](#list_ebs-ebs_Description)<br />[ebs:ParentSnapshot](#list_ebs-ebs_ParentSnapshot)<br />[ebs:VolumeSize](#list_ebs-ebs_VolumeSize)
  - **Access level:** Write

- **   [GetSnapshotBlock](https://docs.aws.amazon.com/ebs/latest/APIReference/API_GetSnapshotBlock.html)  **
  - **Description:** Grants permission to return the data of a block in an Amazon Elastic Block Store (EBS) snapshot
  - **Resource types (\*required):** [snapshot\*](#list_ebs-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ebs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ebs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ebs-aws_TagKeys)<br />[ebs:Description](#list_ebs-ebs_Description)<br />[ebs:ParentSnapshot](#list_ebs-ebs_ParentSnapshot)<br />[ebs:VolumeSize](#list_ebs-ebs_VolumeSize)
  - **Access level:** Read

- **   [ListChangedBlocks](https://docs.aws.amazon.com/ebs/latest/APIReference/API_ListChangedBlocks.html)  **
  - **Description:** Grants permission to list the blocks that are different between two Amazon Elastic Block Store (EBS) snapshots of the same volume/snapshot lineage
  - **Resource types (\*required):** [snapshot\*](#list_ebs-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ebs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ebs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ebs-aws_TagKeys)<br />[ebs:Description](#list_ebs-ebs_Description)<br />[ebs:ParentSnapshot](#list_ebs-ebs_ParentSnapshot)<br />[ebs:VolumeSize](#list_ebs-ebs_VolumeSize)
  - **Access level:** Read

- **   [ListSnapshotBlocks](https://docs.aws.amazon.com/ebs/latest/APIReference/API_ListSnapshotBlocks.html)  **
  - **Description:** Grants permission to list the blocks in an Amazon Elastic Block Store (EBS) snapshot
  - **Resource types (\*required):** [snapshot\*](#list_ebs-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ebs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ebs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ebs-aws_TagKeys)<br />[ebs:Description](#list_ebs-ebs_Description)<br />[ebs:ParentSnapshot](#list_ebs-ebs_ParentSnapshot)<br />[ebs:VolumeSize](#list_ebs-ebs_VolumeSize)
  - **Access level:** Read

- **   [PutSnapshotBlock](https://docs.aws.amazon.com/ebs/latest/APIReference/API_PutSnapshotBlock.html)  **
  - **Description:** Grants permission to write a block of data to a snapshot created by the StartSnapshot operation
  - **Resource types (\*required):** [snapshot\*](#list_ebs-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ebs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ebs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ebs-aws_TagKeys)<br />[ebs:Description](#list_ebs-ebs_Description)<br />[ebs:ParentSnapshot](#list_ebs-ebs_ParentSnapshot)<br />[ebs:VolumeSize](#list_ebs-ebs_VolumeSize)
  - **Access level:** Write

- **   [StartSnapshot](https://docs.aws.amazon.com/ebs/latest/APIReference/API_StartSnapshot.html)  **
  - **Description:** Grants permission to create a new EBS snapshot
  - **Resource types (\*required):** [snapshot](#list_ebs-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ebs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ebs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ebs-aws_TagKeys)<br />[ebs:Description](#list_ebs-ebs_Description)<br />[ebs:ParentSnapshot](#list_ebs-ebs_ParentSnapshot)<br />[ebs:VolumeSize](#list_ebs-ebs_VolumeSize)
  - **Access level:** Write



## Resource types defined by Amazon Elastic Block Store
<a name="list_ebs-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)  | arn:${Partition}:ec2:${Region}::snapshot/${SnapshotId} | [aws:RequestTag/${TagKey}](#list_ebs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ebs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ebs-aws_TagKeys)<br />[ebs:Description](#list_ebs-ebs_Description)<br />[ebs:ParentSnapshot](#list_ebs-ebs_ParentSnapshot)<br />[ebs:VolumeSize](#list_ebs-ebs_VolumeSize) | 

## Condition keys for Amazon Elastic Block Store
<a name="list_ebs-policy-keys"></a>

Amazon Elastic Block Store defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [ebs:Description](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticblockstore.html#amazonelasticblockstore-policy-keys)  | Filters access by the description of the snapshot being created | String | 
|   [ebs:ParentSnapshot](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticblockstore.html#amazonelasticblockstore-policy-keys)  | Filters access by the ARN of the parent snapshot | ARN | 
|   [ebs:VolumeSize](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticblockstore.html#amazonelasticblockstore-policy-keys)  | Filters access by the size of the volume for the snapshot being created, in GiB | Numeric | 