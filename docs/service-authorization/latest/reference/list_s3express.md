

# Actions, resources, and condition keys for Amazon S3 Express
<a name="list_s3express"></a>

Amazon S3 Express (service prefix: `s3express`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonS3/latest/API/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/s3express/s3express.json) for this service.

**Topics**
+ [Actions defined by Amazon S3 Express](#list_s3express-actions-as-permissions)
+ [Resource types defined by Amazon S3 Express](#list_s3express-resources-for-iam-policies)
+ [Condition keys for Amazon S3 Express](#list_s3express-policy-keys)

## Actions defined by Amazon S3 Express
<a name="list_s3express-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html)  **
  - **Description:** Grants permission to create a new access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3express-resource-accesspoint)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3express-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3express-aws_TagKeys)<br />[s3express:AccessPointNetworkOrigin](#list_s3express-s3express_AccessPointNetworkOrigin)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:DataAccessPointAccount](#list_s3express-s3express_DataAccessPointAccount)<br />[s3express:DataAccessPointArn](#list_s3express-s3express_DataAccessPointArn)<br />[s3express:LocationName](#list_s3express-s3express_LocationName)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Write

- **   [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)  **
  - **Description:** Grants permission to create a new bucket
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3express-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3express-aws_TagKeys)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:LocationName](#list_s3express-s3express_LocationName)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Write

- **   [CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html)  **
  - **Description:** Grants permission to Create Session token which is used for object APIs such as PutObject, GetObject, etc
  - **Resource types (\*required):** [accesspoint](#list_s3express-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:AllAccessRestrictedToLocalZoneGroup](#list_s3express-s3express_AllAccessRestrictedToLocalZoneGroup)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:Permissions](#list_s3express-s3express_Permissions)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:SessionMode](#list_s3express-s3express_SessionMode)<br />[s3express:signatureAge](#list_s3express-s3express_signatureAge)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)<br />[s3express:x-amz-server-side-encryption](#list_s3express-s3express_x-amz-server-side-encryption)<br />[s3express:x-amz-server-side-encryption-aws-kms-key-id](#list_s3express-s3express_x-amz-server-side-encryption-aws-kms-key-id)
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AllAccessRestrictedToLocalZoneGroup](#list_s3express-s3express_AllAccessRestrictedToLocalZoneGroup)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:Permissions](#list_s3express-s3express_Permissions)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:SessionMode](#list_s3express-s3express_SessionMode)<br />[s3express:signatureAge](#list_s3express-s3express_signatureAge)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)<br />[s3express:x-amz-server-side-encryption](#list_s3express-s3express_x-amz-server-side-encryption)<br />[s3express:x-amz-server-side-encryption-aws-kms-key-id](#list_s3express-s3express_x-amz-server-side-encryption-aws-kms-key-id)
  - **Access level:** Write

- **   [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html)  **
  - **Description:** Grants permission to delete the access point named in the URI
  - **Resource types (\*required):** [accesspoint\*](#list_s3express-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointNetworkOrigin](#list_s3express-s3express_AccessPointNetworkOrigin)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:DataAccessPointAccount](#list_s3express-s3express_DataAccessPointAccount)<br />[s3express:DataAccessPointArn](#list_s3express-s3express_DataAccessPointArn)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html)  **
  - **Description:** Grants permission to delete the policy on a specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3express-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointNetworkOrigin](#list_s3express-s3express_AccessPointNetworkOrigin)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:DataAccessPointAccount](#list_s3express-s3express_DataAccessPointAccount)<br />[s3express:DataAccessPointArn](#list_s3express-s3express_DataAccessPointArn)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteAccessPointScope](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointScope.html)  **
  - **Description:** Grants permission to delete the scope configuration on a specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3express-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointNetworkOrigin](#list_s3express-s3express_AccessPointNetworkOrigin)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:DataAccessPointAccount](#list_s3express-s3express_DataAccessPointAccount)<br />[s3express:DataAccessPointArn](#list_s3express-s3express_DataAccessPointArn)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)  **
  - **Description:** Grants permission to delete the bucket named in the URI
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html)  **
  - **Description:** Grants permission to delete the policy on a specified bucket
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [GetAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html)  **
  - **Description:** Grants permission to return configuration information about the specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3express-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointNetworkOrigin](#list_s3express-s3express_AccessPointNetworkOrigin)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:DataAccessPointAccount](#list_s3express-s3express_DataAccessPointAccount)<br />[s3express:DataAccessPointArn](#list_s3express-s3express_DataAccessPointArn)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html)  **
  - **Description:** Grants permission to return the access point policy associated with the specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3express-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointNetworkOrigin](#list_s3express-s3express_AccessPointNetworkOrigin)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:DataAccessPointAccount](#list_s3express-s3express_DataAccessPointAccount)<br />[s3express:DataAccessPointArn](#list_s3express-s3express_DataAccessPointArn)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessPointScope](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointScope.html)  **
  - **Description:** Grants permission to return the scope configuration associated with the specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3express-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointNetworkOrigin](#list_s3express-s3express_AccessPointNetworkOrigin)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:DataAccessPointAccount](#list_s3express-s3express_DataAccessPointAccount)<br />[s3express:DataAccessPointArn](#list_s3express-s3express_DataAccessPointArn)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html)  **
  - **Description:** Grants permission to return the policy of the specified bucket
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetEncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html)  **
  - **Description:** Grants permission to return the default encryption configuration for a directory bucket
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html)  **
  - **Description:** Grants permission to return an inventory configuration identified by the inventory configuration ID for a S3 directory bucket
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)  **
  - **Description:** Grants permission to return the lifecycle configuration information set on a directory bucket
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetricsConfiguration.html)  **
  - **Description:** Grants permission to get a metrics configuration of a directory bucket
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Read

- **   [ListAccessPointsForDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForDirectoryBuckets.html)  **
  - **Description:** Grants permission to list access points
  - **Resource types (\*required):** 
  - **Condition keys:** [s3express:authType](#list_s3express-s3express_authType)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** List

- **   [ListAllMyDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html)  **
  - **Description:** Grants permission to list all directory buckets owned by the authenticated sender of the request
  - **Resource types (\*required):** 
  - **Condition keys:** [s3express:authType](#list_s3express-s3express_authType)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListTagsForResource.html)  **
  - **Description:** Grants permission to lists all of the tags for a specified resource
  - **Resource types (\*required):** [accesspoint](#list_s3express-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3express-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** List

- **   [PutAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html)  **
  - **Description:** Grants permission to associate an access policy with a specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3express-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointNetworkOrigin](#list_s3express-s3express_AccessPointNetworkOrigin)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:DataAccessPointAccount](#list_s3express-s3express_DataAccessPointAccount)<br />[s3express:DataAccessPointArn](#list_s3express-s3express_DataAccessPointArn)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutAccessPointScope](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointScope.html)  **
  - **Description:** Grants permission to associate an access point with a specified access point scope configuration
  - **Resource types (\*required):** [accesspoint\*](#list_s3express-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointNetworkOrigin](#list_s3express-s3express_AccessPointNetworkOrigin)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:DataAccessPointAccount](#list_s3express-s3express_DataAccessPointAccount)<br />[s3express:DataAccessPointArn](#list_s3express-s3express_DataAccessPointArn)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html)  **
  - **Description:** Grants permission to add or replace a bucket policy on a bucket
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutEncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html)  **
  - **Description:** Grants permission to set the encryption configuration for a directory bucket
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html)  **
  - **Description:** Grants permission to add an inventory configuration to the bucket, identified by the inventory ID
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:InventoryAccessibleOptionalFields](#list_s3express-s3express_InventoryAccessibleOptionalFields)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)  **
  - **Description:** Grants permission to create a new lifecycle configuration for the directory bucket or replace an existing lifecycle configuration
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketMetricsConfiguration.html)  **
  - **Description:** Grants permission to set or update a metrics configuration for the CloudWatch request metrics of a directory bucket
  - **Resource types (\*required):** [bucket\*](#list_s3express-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html)  **
  - **Description:** Grants permission to create a new user-defined tag or update an existing tag
  - **Resource types (\*required):** [accesspoint](#list_s3express-resource-accesspoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3express-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3express-aws_TagKeys)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3express-resource-bucket) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3express-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3express-aws_TagKeys)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified user-defined tags from an S3 resource
  - **Resource types (\*required):** [accesspoint](#list_s3express-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3express-aws_TagKeys)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3express-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3express-aws_TagKeys)<br />[s3express:authType](#list_s3express-s3express_authType)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_)<br />[s3express:ResourceAccount](#list_s3express-s3express_ResourceAccount)<br />[s3express:signatureversion](#list_s3express-s3express_signatureversion)<br />[s3express:TlsVersion](#list_s3express-s3express_TlsVersion)<br />[s3express:x-amz-content-sha256](#list_s3express-s3express_x-amz-content-sha256)
  - **Access level:** Tagging, Write



## Resource types defined by Amazon S3 Express
<a name="list_s3express-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [accesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html)  | arn:${Partition}:s3express:${Region}:${Account}:accesspoint/${AccessPointName} | [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:AccessPointTag/${TagKey}](#list_s3express-s3express_AccessPointTag___TagKey_) | 
|  [bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html)  | arn:${Partition}:s3express:${Region}:${Account}:bucket/${BucketName} | [aws:ResourceTag/${TagKey}](#list_s3express-aws_ResourceTag___TagKey_)<br />[s3express:BucketTag/${TagKey}](#list_s3express-s3express_BucketTag___TagKey_) | 

## Condition keys for Amazon S3 Express
<a name="list_s3express-policy-keys"></a>

Amazon S3 Express defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html#example-user-policy-request-tag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html#example-user-policy-resource-tag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html#example-user-policy-tag-keys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [s3express:AccessPointNetworkOrigin](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies)  | Filters access by the network origin (Internet or VPC) | String | 
|   [s3express:AccessPointTag/${TagKey}](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-db-tagging.html#example-access-points-db-policy-bucket-tag)  | Filters access by tag key-value pairs attached to the access point | String | 
|   [s3express:AllAccessRestrictedToLocalZoneGroup](#example-all-access-restricted-to-localzone-group)  | Filters access by AWS Local Zone network border group(s) provided in this condition key | String | 
|   [s3express:BucketTag/${TagKey}](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html#example-policy-bucket-tag)  | Filters access by tag key-value pairs attached to the bucket | String | 
|   [s3express:DataAccessPointAccount](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies)  | Filters access by the AWS Account ID that owns the access point | String | 
|   [s3express:DataAccessPointArn](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies)  | Filters access by an access point Amazon Resource Name (ARN) | ARN | 
|   [s3express:InventoryAccessibleOptionalFields](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-s3-inventory-3)  | Filters access by restricting which optional metadata fields a user can add when configuring S3 Inventory reports | ArrayOfString | 
|   [s3express:LocationName](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-express-zonal-policy-keys.html#example-location-name)  | Filters access by a specific Availability Zone or Local Zone ID | String | 
|   [s3express:Permissions](#example-permissions)  | Filters access by the permission requested by Access Point Scope configuration, such as GetObject, PutObject | ArrayOfString | 
|   [s3express:ResourceAccount](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-express-zonal-policy-keys.html#example-object-resource-account)  | Filters access by the resource owner AWS account ID | String | 
|   [s3express:SessionMode](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-express-zonal-policy-keys.html#example-session-mode)  | Filters access by the permission requested by CreateSession API, such as ReadOnly and ReadWrite | String | 
|   [s3express:TlsVersion](#example-object-tls-version)  | Filters access by the TLS version used by the client | Numeric | 
|   [s3express:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by authentication method | String | 
|   [s3express:signatureAge](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by the age in milliseconds of the request signature | Numeric | 
|   [s3express:signatureversion](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by the AWS Signature Version used on the request | String | 
|   [s3express:x-amz-content-sha256](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by unsigned content in your bucket | String | 
|   [s3express:x-amz-server-side-encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-data-protection.html)  | Filters access by server-side encryption | String | 
|   [s3express:x-amz-server-side-encryption-aws-kms-key-id](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-UsingKMSEncryption.html#s3-express-require-sse-kms)  | Filters access by AWS KMS customer managed key for server-side encryption | ARN | 