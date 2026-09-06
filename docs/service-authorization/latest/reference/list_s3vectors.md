

# Actions, resources, and condition keys for Amazon S3 Vectors
<a name="list_s3vectors"></a>

Amazon S3 Vectors (service prefix: `s3vectors`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonS3/latest/API/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-access-management.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/s3vectors/s3vectors.json) for this service.

**Topics**
+ [Actions defined by Amazon S3 Vectors](#list_s3vectors-actions-as-permissions)
+ [Resource types defined by Amazon S3 Vectors](#list_s3vectors-resources-for-iam-policies)
+ [Condition keys for Amazon S3 Vectors](#list_s3vectors-policy-keys)

## Actions defined by Amazon S3 Vectors
<a name="list_s3vectors-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateIndex.html)  **
  - **Description:** Grants permission to create a new vector index within a specified vector bucket
  - **Resource types (\*required):** [Index\*](#list_s3vectors-resource-Index)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3vectors-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3vectors-aws_TagKeys)<br />[s3vectors:kmsKeyArn](#list_s3vectors-s3vectors_kmsKeyArn)<br />[s3vectors:sseType](#list_s3vectors-s3vectors_sseType)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Write

- **   [CreateVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateVectorBucket.html)  **
  - **Description:** Grants permission to create a new vector bucket
  - **Resource types (\*required):** [VectorBucket\*](#list_s3vectors-resource-VectorBucket)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3vectors-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3vectors-aws_TagKeys)<br />[s3vectors:kmsKeyArn](#list_s3vectors-s3vectors_kmsKeyArn)<br />[s3vectors:sseType](#list_s3vectors-s3vectors_sseType)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteIndex.html)  **
  - **Description:** Grants permission to delete a specified vector index
  - **Resource types (\*required):** [Index\*](#list_s3vectors-resource-Index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectorBucket.html)  **
  - **Description:** Grants permission to delete a specified vector bucket
  - **Resource types (\*required):** [VectorBucket\*](#list_s3vectors-resource-VectorBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectorBucketPolicy.html)  **
  - **Description:** Grants permission to delete the IAM resource policy from a specified vector bucket
  - **Resource types (\*required):** [VectorBucket\*](#list_s3vectors-resource-VectorBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectors.html)  **
  - **Description:** Grants permission to delete a batch of vectors from a specified vector index
  - **Resource types (\*required):** [Index\*](#list_s3vectors-resource-Index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Write

- **   [GetIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetIndex.html)  **
  - **Description:** Grants permission to get the attributes of a specified vector index
  - **Resource types (\*required):** [Index\*](#list_s3vectors-resource-Index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucket.html)  **
  - **Description:** Grants permission to get the attributes of a specified vector bucket
  - **Resource types (\*required):** [VectorBucket\*](#list_s3vectors-resource-VectorBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucketPolicy.html)  **
  - **Description:** Grants permission to get the IAM resource policy for a specific vector bucket
  - **Resource types (\*required):** [VectorBucket\*](#list_s3vectors-resource-VectorBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectors.html)  **
  - **Description:** Grants permission to get a batch of vectors by their vector keys
  - **Resource types (\*required):** [Index\*](#list_s3vectors-resource-Index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Read

- **   [ListIndexes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListIndexes.html)  **
  - **Description:** Grants permission to get a paginated list of all indexes in a specified vector bucket
  - **Resource types (\*required):** [VectorBucket\*](#list_s3vectors-resource-VectorBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for specified S3Vector resource
  - **Resource types (\*required):** [Index](#list_s3vectors-resource-Index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Resource types (\*required):** [VectorBucket](#list_s3vectors-resource-VectorBucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** List

- **   [ListVectorBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectorBuckets.html)  **
  - **Description:** Grants permission to get a paginated list of all vector buckets in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectors.html)  **
  - **Description:** Grants permission to get a paginated list of all vectors in a specified vector index
  - **Resource types (\*required):** [Index\*](#list_s3vectors-resource-Index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** List

- **   [PutVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectorBucketPolicy.html)  **
  - **Description:** Grants permission to add an IAM resource policy to a specified vector bucket
  - **Resource types (\*required):** [VectorBucket\*](#list_s3vectors-resource-VectorBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectors.html)  **
  - **Description:** Grants permission to add a batch of vectors to a specified vector index
  - **Resource types (\*required):** [Index\*](#list_s3vectors-resource-Index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Write

- **   [QueryVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryVectors.html)  **
  - **Description:** Grants permission to find approximate nearest neighbors within a specified search vector index for a given query vector
  - **Resource types (\*required):** [Index\*](#list_s3vectors-resource-Index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_TagResource.html)  **
  - **Description:** Grants permission to tag a S3Vector resource
  - **Resource types (\*required):** [Index](#list_s3vectors-resource-Index) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3vectors-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3vectors-aws_TagKeys)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Resource types (\*required):** [VectorBucket](#list_s3vectors-resource-VectorBucket) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3vectors-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3vectors-aws_TagKeys)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_UntagResource.html)  **
  - **Description:** Grants permission to untag a S3Vector resource
  - **Resource types (\*required):** [Index](#list_s3vectors-resource-Index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3vectors-aws_TagKeys)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Resource types (\*required):** [VectorBucket](#list_s3vectors-resource-VectorBucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3vectors-aws_TagKeys)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_)
  - **Access level:** Tagging, Write



## Resource types defined by Amazon S3 Vectors
<a name="list_s3vectors-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Index](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-access-management.html)  | arn:${Partition}:s3vectors:${Region}:${Account}:bucket/${BucketName}/index/${IndexName} | [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_) | 
|  [VectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-access-management.html)  | arn:${Partition}:s3vectors:${Region}:${Account}:bucket/${BucketName} | [aws:ResourceTag/${TagKey}](#list_s3vectors-aws_ResourceTag___TagKey_)<br />[s3vectors:VectorBucketTag/${TagKey}](#list_s3vectors-s3vectors_VectorBucketTag___TagKey_) | 

## Condition keys for Amazon S3 Vectors
<a name="list_s3vectors-policy-keys"></a>

Amazon S3 Vectors defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [s3vectors:VectorBucketTag/${TagKey}](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-access-management.html#s3-vectors-condition-keyss3-vectors-access-management.html)  | Filters access by the tags associated with the vector bucket | String | 
|   [s3vectors:kmsKeyArn](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-access-management.html#s3-vectors-condition-keyss3-vectors-access-management.html)  | Filters access by the AWS KMS key ARN for the key used to encrypt a vector bucket | ARN | 
|   [s3vectors:sseType](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-access-management.html#s3-vectors-condition-keyss3-vectors-access-management.html)  | Filters access by server-side encryption type | String | 