

# Actions, resources, and condition keys for Amazon S3 on Outposts
<a name="list_s3outposts"></a>

Amazon S3 on Outposts (service prefix: `s3-outposts`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonS3/latest/API/Type_API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-overview.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/s3-outposts/s3-outposts.json) for this service.

**Topics**
+ [API operations defined by Amazon S3 on Outposts](#list_s3outposts-operations)
+ [Actions defined by Amazon S3 on Outposts](#list_s3outposts-actions-as-permissions)
+ [Resource types defined by Amazon S3 on Outposts](#list_s3outposts-resources-for-iam-policies)
+ [Condition keys for Amazon S3 on Outposts](#list_s3outposts-policy-keys)

## API operations defined by Amazon S3 on Outposts
<a name="list_s3outposts-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_s3outposts-actions-as-permissions).




- **   CreateEndpoint  **
  - **IAM action:**  [s3-outposts:CreateEndpoint](#list_s3outposts-action-CreateEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpoint  **
  - **IAM action:**  [s3-outposts:DeleteEndpoint](#list_s3outposts-action-DeleteEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListEndpoints  **
  - **IAM action:**  [s3-outposts:ListEndpoints](#list_s3outposts-action-ListEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOutpostsWithS3  **
  - **IAM action:**  [s3-outposts:ListOutpostsWithS3](#list_s3outposts-action-ListOutpostsWithS3) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSharedEndpoints  **
  - **IAM action:**  [s3-outposts:ListSharedEndpoints](#list_s3outposts-action-ListSharedEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List



## Actions defined by Amazon S3 on Outposts
<a name="list_s3outposts-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)  **
  - **Description:** Grants permission to abort a multipart upload
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [CreateAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html)  **
  - **Description:** Grants permission to create a new access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3outposts-resource-accesspoint)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html)  **
  - **Description:** Grants permission to create a new bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [CreateEndpoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html)  **
  - **Description:** Grants permission to create a new endpoint
  - **Resource types (\*required):** [endpoint\*](#list_s3outposts-resource-endpoint)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html)  **
  - **Description:** Grants permission to delete the access point named in the URI
  - **Resource types (\*required):** [accesspoint\*](#list_s3outposts-resource-accesspoint)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html)  **
  - **Description:** Grants permission to delete the policy on a specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3outposts-resource-accesspoint)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucket.html)  **
  - **Description:** Grants permission to delete the bucket named in the URI
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketPolicy.html)  **
  - **Description:** Grants permission to delete the policy on a specified bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteEndpoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html)  **
  - **Description:** Grants permission to delete the endpoint named in the URI
  - **Resource types (\*required):** [endpoint\*](#list_s3outposts-resource-endpoint)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)  **
  - **Description:** Grants permission to remove the null version of an object and insert a delete marker, which becomes the current version of the object
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)  **
  - **Description:** Grants permission to use the tagging subresource to remove the entire tag set from the specified object
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:ExistingObjectTag/<key>](#list_s3outposts-s3-outposts_ExistingObjectTag_key)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [DeleteObjectVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)  **
  - **Description:** Grants permission to remove a specific version of an object
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:versionid](#list_s3outposts-s3-outposts_versionid)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)  **
  - **Description:** Grants permission to remove the entire tag set for a specific version of the object
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:ExistingObjectTag/<key>](#list_s3outposts-s3-outposts_ExistingObjectTag_key)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:versionid](#list_s3outposts-s3-outposts_versionid)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [GetAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html)  **
  - **Description:** Grants permission to return configuration information about the specified access point
  - **Resource types (\*required):** 
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html)  **
  - **Description:** Grants permission to returns the access point policy associated with the specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3outposts-resource-accesspoint)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html)  **
  - **Description:** Grants permission to return the bucket configuration associated with an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html)  **
  - **Description:** Grants permission to return the policy of the specified bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketTagging.html)  **
  - **Description:** Grants permission to return the tag set associated with an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html)  **
  - **Description:** Grants permission to return the versioning state of an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html)  **
  - **Description:** Grants permission to return the lifecycle configuration information set on an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)  **
  - **Description:** Grants permission to retrieve objects from Amazon S3
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:ExistingObjectTag/<key>](#list_s3outposts-s3-outposts_ExistingObjectTag_key)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)  **
  - **Description:** Grants permission to return the tag set of an object
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:ExistingObjectTag/<key>](#list_s3outposts-s3-outposts_ExistingObjectTag_key)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)  **
  - **Description:** Grants permission to retrieve a specific version of an object
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:ExistingObjectTag/<key>](#list_s3outposts-s3-outposts_ExistingObjectTag_key)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:versionid](#list_s3outposts-s3-outposts_versionid)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersionForReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)  **
  - **Description:** Grants permission to replicate both unencrypted objects and objects encrypted with SSE-KMS
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)  **
  - **Description:** Grants permission to return the tag set for a specific version of the object
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:ExistingObjectTag/<key>](#list_s3outposts-s3-outposts_ExistingObjectTag_key)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:versionid](#list_s3outposts-s3-outposts_versionid)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetReplicationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html)  **
  - **Description:** Grants permission to get the replication configuration information set on an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Read

- **   [ListAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html)  **
  - **Description:** Grants permission to list access points
  - **Resource types (\*required):** 
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** List

- **   [ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)  **
  - **Description:** Grants permission to list some or all of the objects in an Amazon S3 bucket (up to 1000)
  - **Resource types (\*required):** [accesspoint\*](#list_s3outposts-resource-accesspoint) / **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:delimiter](#list_s3outposts-s3-outposts_delimiter)<br />[s3-outposts:max-keys](#list_s3outposts-s3-outposts_max-keys)<br />[s3-outposts:prefix](#list_s3outposts-s3-outposts_prefix)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket) / **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:delimiter](#list_s3outposts-s3-outposts_delimiter)<br />[s3-outposts:max-keys](#list_s3outposts-s3-outposts_max-keys)<br />[s3-outposts:prefix](#list_s3outposts-s3-outposts_prefix)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** List

- **   [ListBucketMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)  **
  - **Description:** Grants permission to list in-progress multipart uploads
  - **Resource types (\*required):** [accesspoint\*](#list_s3outposts-resource-accesspoint) / **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket) / **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** List

- **   [ListBucketVersions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html)  **
  - **Description:** Grants permission to list metadata about all the versions of objects in an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:delimiter](#list_s3outposts-s3-outposts_delimiter)<br />[s3-outposts:max-keys](#list_s3outposts-s3-outposts_max-keys)<br />[s3-outposts:prefix](#list_s3outposts-s3-outposts_prefix)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** List

- **   [ListEndpoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html)  **
  - **Description:** Grants permission to list endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMultipartUploadParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)  **
  - **Description:** Grants permission to list the parts that have been uploaded for a specific multipart upload
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** List

- **   [ListOutpostsWithS3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListOutpostsWithS3.html)  **
  - **Description:** Grants permission to list outposts with S3 capacity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegionalBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListRegionalBuckets.html)  **
  - **Description:** Grants permission to list all buckets owned by the authenticated sender of the request
  - **Resource types (\*required):** 
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** List

- **   [ListSharedEndpoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListSharedEndpoints.html)  **
  - **Description:** Grants permission to list shared endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html)  **
  - **Description:** Grants permission to associate an access policy with a specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3outposts-resource-accesspoint)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketPolicy.html)  **
  - **Description:** Grants permission to add or replace a bucket policy on a bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketTagging.html)  **
  - **Description:** Grants permission to add a set of tags to an existing Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html)  **
  - **Description:** Grants permission to set the versioning state of an existing Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html)  **
  - **Description:** Grants permission to create a new lifecycle configuration for the bucket or replace an existing lifecycle configuration
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)  **
  - **Description:** Grants permission to add an object to a bucket
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:RequestObjectTag/<key>](#list_s3outposts-s3-outposts_RequestObjectTag_key)<br />[s3-outposts:RequestObjectTagKeys](#list_s3outposts-s3-outposts_RequestObjectTagKeys)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-acl](#list_s3outposts-s3-outposts_x-amz-acl)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)<br />[s3-outposts:x-amz-copy-source](#list_s3outposts-s3-outposts_x-amz-copy-source)<br />[s3-outposts:x-amz-metadata-directive](#list_s3outposts-s3-outposts_x-amz-metadata-directive)<br />[s3-outposts:x-amz-server-side-encryption](#list_s3outposts-s3-outposts_x-amz-server-side-encryption)<br />[s3-outposts:x-amz-storage-class](#list_s3outposts-s3-outposts_x-amz-storage-class)
  - **Access level:** Write

- **   [PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html)  **
  - **Description:** Grants permission to set the access control list (ACL) permissions for an object that already exists in a bucket
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:ExistingObjectTag/<key>](#list_s3outposts-s3-outposts_ExistingObjectTag_key)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-acl](#list_s3outposts-s3-outposts_x-amz-acl)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)<br />[s3-outposts:x-amz-storage-class](#list_s3outposts-s3-outposts_x-amz-storage-class)
  - **Access level:** Permissions management, Write

- **   [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)  **
  - **Description:** Grants permission to set the supplied tag-set to an object that already exists in a bucket
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:ExistingObjectTag/<key>](#list_s3outposts-s3-outposts_ExistingObjectTag_key)<br />[s3-outposts:RequestObjectTag/<key>](#list_s3outposts-s3-outposts_RequestObjectTag_key)<br />[s3-outposts:RequestObjectTagKeys](#list_s3outposts-s3-outposts_RequestObjectTagKeys)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [PutObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)  **
  - **Description:** Grants permission to set the supplied tag-set for a specific version of an object
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:AccessPointNetworkOrigin](#list_s3outposts-s3-outposts_AccessPointNetworkOrigin)<br />[s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:DataAccessPointAccount](#list_s3outposts-s3-outposts_DataAccessPointAccount)<br />[s3-outposts:DataAccessPointArn](#list_s3outposts-s3-outposts_DataAccessPointArn)<br />[s3-outposts:ExistingObjectTag/<key>](#list_s3outposts-s3-outposts_ExistingObjectTag_key)<br />[s3-outposts:RequestObjectTag/<key>](#list_s3outposts-s3-outposts_RequestObjectTag_key)<br />[s3-outposts:RequestObjectTagKeys](#list_s3outposts-s3-outposts_RequestObjectTagKeys)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:versionid](#list_s3outposts-s3-outposts_versionid)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [PutReplicationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketReplication.html)  **
  - **Description:** Grants permission to create a new replication configuration or replace an existing one
  - **Resource types (\*required):** [bucket\*](#list_s3outposts-resource-bucket)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [ReplicateDelete](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)  **
  - **Description:** Grants permission to replicate delete markers to the destination bucket
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Write

- **   [ReplicateObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)  **
  - **Description:** Grants permission to replicate objects and object tags to the destination bucket
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)<br />[s3-outposts:x-amz-server-side-encryption](#list_s3outposts-s3-outposts_x-amz-server-side-encryption)
  - **Access level:** Write

- **   [ReplicateTags](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)  **
  - **Description:** Grants permission to replicate object tags to the destination bucket
  - **Resource types (\*required):** [object\*](#list_s3outposts-resource-object)
  - **Condition keys:** [s3-outposts:authType](#list_s3outposts-s3-outposts_authType)<br />[s3-outposts:signatureAge](#list_s3outposts-s3-outposts_signatureAge)<br />[s3-outposts:signatureversion](#list_s3outposts-s3-outposts_signatureversion)<br />[s3-outposts:x-amz-content-sha256](#list_s3outposts-s3-outposts_x-amz-content-sha256)
  - **Access level:** Tagging, Write



## Resource types defined by Amazon S3 on Outposts
<a name="list_s3outposts-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [accesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html)  | arn:${Partition}:s3-outposts:${Region}:${Account}:outpost/${OutpostId}/accesspoint/${AccessPointName} |   | 
|  [bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)  | arn:${Partition}:s3-outposts:${Region}:${Account}:outpost/${OutpostId}/bucket/${BucketName} |   | 
|  [endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/outposts-endpoints.html)  | arn:${Partition}:s3-outposts:${Region}:${Account}:outpost/${OutpostId}/endpoint/${EndpointId} |   | 
|  [object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html)  | arn:${Partition}:s3-outposts:${Region}:${Account}:outpost/${OutpostId}/bucket/${BucketName}/object/${ObjectName} |   | 

## Condition keys for Amazon S3 on Outposts
<a name="list_s3outposts-policy-keys"></a>

Amazon S3 on Outposts defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [s3-outposts:AccessPointNetworkOrigin](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies)  | Filters access by the network origin (Internet or VPC) | String | 
|   [s3-outposts:DataAccessPointAccount](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies)  | Filters access by the AWS Account ID that owns the access point | String | 
|   s3-outposts:DataAccessPointArn  | Filters access by an access point Amazon Resource Name (ARN) | ARN | 
|   [s3-outposts:ExistingObjectTag/<key>](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html#tagging-and-policies)  | Filters access by requiring that an existing object tag has a specific tag key and value | String | 
|   [s3-outposts:RequestObjectTag/<key>](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html#tagging-and-policies)  | Filters access by restricting the tag keys and values allowed on objects | String | 
|   [s3-outposts:RequestObjectTagKeys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html#tagging-and-policies)  | Filters access by restricting the tag keys allowed on objects | String | 
|   [s3-outposts:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by restricting incoming requests to a specific authentication method | String | 
|   [s3-outposts:delimiter](https://docs.aws.amazon.com/AmazonS3/latest/userguide/walkthrough1.html)  | Filters access by requiring the delimiter parameter | String | 
|   [s3-outposts:max-keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-numeric-condition-operators)  | Filters access by limiting the maximum number of keys returned in a ListBucket request | Numeric | 
|   [s3-outposts:prefix](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#condition-key-bucket-ops-2)  | Filters access by key name prefix | String | 
|   [s3-outposts:signatureAge](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by identifying the length of time, in milliseconds, that a signature is valid in an authenticated request | Numeric | 
|   [s3-outposts:signatureversion](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by identifying the version of AWS Signature that is supported for authenticated requests | String | 
|   [s3-outposts:versionid](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#getobjectversion-limit-access-to-specific-version-3)  | Filters access by a specific object version | String | 
|   [s3-outposts:x-amz-acl](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions)  | Filters access by requiring the x-amz-acl header with a specific canned ACL in a request | String | 
|   [s3-outposts:x-amz-content-sha256](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by disallowing unsigned content in your bucket | String | 
|   [s3-outposts:x-amz-copy-source](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#putobject-limit-copy-source-3)  | Filters access by restricting the copy source to a specific bucket, prefix, or object | String | 
|   [s3-outposts:x-amz-metadata-directive](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)  | Filters access by enabling enforcement of object metadata behavior (COPY or REPLACE) when objects are copied | String | 
|   [s3-outposts:x-amz-server-side-encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html)  | Filters access by requiring server-side encryption | String | 
|   [s3-outposts:x-amz-storage-class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-howtoset)  | Filters access by storage class | String | 