

# Identity and Access management in S3 Vectors
<a name="s3-vectors-access-management"></a>

Access management in S3 Vectors follows AWS security best practices, providing multiple layers of control to ensure that only authorized users and applications can access your vector data. The service integrates with IAM and supports both identity-based and resource-based policies, giving you flexibility in how you structure and manage permissions across your organization.

## Authenticating and authorizing requests
<a name="s3-vectors-authenticating-authorizing"></a>

S3 Vectors uses AWS standard authentication and authorization mechanisms to secure access to vector buckets and their contents. Every request to S3 Vectors must be authenticated using valid AWS credentials, and the service evaluates permissions based on the combination of identity-based policies, resource-based policies, and any applicable service control policies.

The authentication process begins when a client makes a request to S3 Vectors using AWS credentials (access keys, temporary credentials from AWS STS, or IAM roles). The service validates these credentials and then evaluates the permissions associated with the authenticated identity against the requested action and target resource. This evaluation process considers multiple policy types and applies the principle of least privilege to determine whether the request should be allowed or denied.

Authorization in S3 Vectors operates at multiple levels of granularity. You can control access at the vector bucket level, individual vector index level, or even specific operations within an index. This hierarchical permission model allows you to implement sophisticated access control schemes that align with your organizational structure and data governance requirements.

## Resource types defined for vector buckets
<a name="s3-vectors-resource-types"></a>

S3 Vectors defines specific resource types that can be referenced in IAM policies and resource-based policies. Understanding these resource types is essential for creating effective access control policies that provide the right level of access to the right users and applications.

The following table describes the resource types available in S3 Vectors.


**Resource types available in S3 Vectors**  

| Resource type | ARN format | Description | 
| --- | --- | --- | 
| VectorBucket | arn:aws:s3vectors:{{region}}:{{123456789012}}:bucket/{{bucket-name}} | Represents a vector bucket and is used for bucket-level operations such as creating, deleting, or configuring the bucket | 
| Index | arn:aws:s3vectors:{{region}}:{{123456789012}}:bucket/{{bucket-name}}/index/{{index-name}} | Represents a vector index within a bucket and is used for index-specific operations such as querying vectors or managing index contents | 

## Policy actions for vector buckets
<a name="s3-vectors-policy-actions"></a>

S3 Vectors provides a comprehensive set of policy actions that correspond to the various operations you can perform on vector buckets and indexes. These actions are designed to provide fine-grained control over who can perform specific operations, allowing you to implement the principle of least privilege effectively.

The following table lists all available policy actions for S3 Vectors resources.


**Policy actions for S3 Vectors resources**  

| Resource type | API operations | Policy actions | Description of policy actions | Access level | Condition keys | 
| --- | --- | --- | --- | --- | --- | 
| Account | [ListVectorBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectorBuckets.html) | s3vectors:ListVectorBuckets | Grants permission to list all vector buckets in the account and region | List |  | 
| VectorBucket | [CreateVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateVectorBucket.html) | s3vectors:CreateVectorBucket | Grants permission to create a new vector bucket with specified configuration | Write | s3vectors:sseType, s3vectors:kmsKeyArn | 
| VectorBucket | [GetVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucket.html) | s3vectors:GetVectorBucket | Grants permission to retrieve vector bucket attributes and configuration | Read |  | 
| VectorBucket | [DeleteVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectorBucket.html) | s3vectors:DeleteVectorBucket | Grants permission to delete an empty vector bucket | Write |  | 
| VectorBucket | [ListIndexes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListIndexes.html) | s3vectors:ListIndexes | Grants permission to list all indexes within a vector bucket | List |  | 
| VectorBucket | [PutVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectorBucketPolicy.html) | s3vectors:PutVectorBucketPolicy | Grants permission to apply or update a resource-based policy on a vector bucket | Permissions management |  | 
| VectorBucket | [GetVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucketPolicy.html) | s3vectors:GetVectorBucketPolicy | Grants permission to retrieve the resource-based policy attached to a vector bucket | Read |  | 
| VectorBucket | [DeleteVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectorBucketPolicy.html) | s3vectors:DeleteVectorBucketPolicy | Grants permission to remove the resource-based policy from a vector bucket | Permissions management |  | 
| Index | [CreateIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateIndex.html) | s3vectors:CreateIndex | Grants permission to create a new vector index with specified dimensions and metadata configuration | Write |  | 
| Index | [GetIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetIndex.html) | s3vectors:GetIndex | Grants permission to retrieve vector index attributes and configuration | Read |  | 
| Index | [DeleteIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteIndex.html) | s3vectors:DeleteIndex | Grants permission to delete a vector index and all its contents | Write |  | 
| Index | [QueryVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryVectors.html) | (Required) s3vectors:QueryVectors | Grants permission to perform similarity queries against vectors in an index.<br /> **With `s3vectors:QueryVectors` only**, you can retrieve vector keys of approximate nearest neighbors and their computed distances from the query vector. This permission is sufficient only when you don't set any metadata filters and don't request metadata (by keeping the `returnMetadata` parameter set to false or not specified). | Read |  | 
|  |  | (Conditionally required): s3vectors:GetVectors | Required if you set metadata filters, set `returnMetadata` to true in your request.<br /> **With both `s3vectors:QueryVectors` and `s3vectors:GetVectors`**, you can filter results by using metadata criteria and retrieve vector keys along with their associated data, metadata, and computed distances from the query vector. | Read |  | 
| Index | [PutVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectors.html) | s3vectors:PutVectors | Grants permission to add or update vectors in an index | Write |  | 
| Index | [GetVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectors.html) | s3vectors:GetVectors | Grants permission to retrieve specific vectors and their metadata by vector key | Read |  | 
| Index | [ListVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectors.html) | (Required) s3vectors:ListVectors | Grants permission to list vector keys in an index. <br />**With `s3vectors:ListVectors` only**, you can list vector keys when both `returnData` and `returnMetadata` parameters are false or not specified. | Read |  | 
|  |  | (Conditionally required): s3vectors:GetVectors | Required if you set either `returnData` or `returnMetadata` parameter to true in your request.<br /> **With both `s3vectors:ListVectors` and `s3vectors:GetVectors`**, you can retrieve vector keys along with their associated data and metadata by setting `returnData` and `returnMetadata` to true. | Read |  | 
| Index | [DeleteVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectors.html) | s3vectors:DeleteVectors | Grants permission to delete specific vectors from an index | Write |  | 

These actions can be combined in various ways to create policies that match your specific access requirements. For example, you might create a read-only policy that includes `s3vectors:GetVectorBucket`, `s3vectors:ListIndexes`, `s3vectors:QueryVectors`, and `s3vectors:GetVectors` actions, or a policy that includes query and vector retrieval permissions but excludes administrative actions like creating or deleting indexes.

## Condition keys for vector buckets
<a name="s3-vectors-condition-keys"></a>


**Condition keys for vector buckets**  

|  | Condition keys | Description | Type | 
| --- | --- | --- | --- | 
| 1 | s3vectors:sseType | Filters access by server-side encryption type Valid values: AES256 \| aws:kms | String | 
| 2 | s3vectors:kmsKeyArn | Filters access by the AWS AWS KMS key ARN for the key used to encrypt a vector bucket | ARN | 