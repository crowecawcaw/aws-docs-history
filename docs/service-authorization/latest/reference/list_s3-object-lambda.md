

# Actions, resources, and condition keys for Amazon S3 Object Lambda
<a name="list_s3-object-lambda"></a>

Amazon S3 Object Lambda (service prefix: `s3-object-lambda`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonS3/latest/dev/olap-best-practices.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonS3/latest/API/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-overview.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/s3-object-lambda/s3-object-lambda.json) for this service.

**Topics**
+ [Actions defined by Amazon S3 Object Lambda](#list_s3-object-lambda-actions-as-permissions)
+ [Resource types defined by Amazon S3 Object Lambda](#list_s3-object-lambda-resources-for-iam-policies)
+ [Condition keys for Amazon S3 Object Lambda](#list_s3-object-lambda-policy-keys)

## Actions defined by Amazon S3 Object Lambda
<a name="list_s3-object-lambda-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)  **
  - **Description:** Grants permission to abort a multipart upload
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Write

- **   [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)  **
  - **Description:** Grants permission to remove the null version of an object and insert a delete marker, which becomes the current version of the object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Write

- **   [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)  **
  - **Description:** Grants permission to use the tagging subresource to remove the entire tag set from the specified object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Tagging, Write

- **   [DeleteObjectVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)  **
  - **Description:** Grants permission to remove a specific version of an object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)<br />[s3-object-lambda:versionid](#list_s3-object-lambda-s3-object-lambda_versionid)
  - **Access level:** Write

- **   [DeleteObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)  **
  - **Description:** Grants permission to remove the entire tag set for a specific version of the object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)<br />[s3-object-lambda:versionid](#list_s3-object-lambda-s3-object-lambda_versionid)
  - **Access level:** Tagging, Write

- **   [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)  **
  - **Description:** Grants permission to retrieve objects from Amazon S3
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Read

- **   [GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)  **
  - **Description:** Grants permission to return the access control list (ACL) of an object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Read

- **   [GetObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html)  **
  - **Description:** Grants permission to get an object's current Legal Hold status
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Read

- **   [GetObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html)  **
  - **Description:** Grants permission to retrieve the retention settings for an object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Read

- **   [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)  **
  - **Description:** Grants permission to return the tag set of an object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Read

- **   [GetObjectVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)  **
  - **Description:** Grants permission to retrieve a specific version of an object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)<br />[s3-object-lambda:versionid](#list_s3-object-lambda-s3-object-lambda_versionid)
  - **Access level:** Read

- **   [GetObjectVersionAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)  **
  - **Description:** Grants permission to return the access control list (ACL) of a specific object version
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)<br />[s3-object-lambda:versionid](#list_s3-object-lambda-s3-object-lambda_versionid)
  - **Access level:** Read

- **   [GetObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/dev/setting-repl-config-perm-overview.html)  **
  - **Description:** Grants permission to return the tag set for a specific version of the object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)<br />[s3-object-lambda:versionid](#list_s3-object-lambda-s3-object-lambda_versionid)
  - **Access level:** Read

- **   [ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)  **
  - **Description:** Grants permission to list some or all of the objects in an Amazon S3 bucket (up to 1000)
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** List

- **   [ListBucketMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)  **
  - **Description:** Grants permission to list in-progress multipart uploads
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** List

- **   [ListBucketVersions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html)  **
  - **Description:** Grants permission to list metadata about all the versions of objects in an Amazon S3 bucket
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** List

- **   [ListMultipartUploadParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)  **
  - **Description:** Grants permission to list the parts that have been uploaded for a specific multipart upload
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** List

- **   [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)  **
  - **Description:** Grants permission to add an object to a bucket
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Write

- **   [PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html)  **
  - **Description:** Grants permission to set the access control list (ACL) permissions for new or existing objects in an S3 bucket
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Permissions management, Write

- **   [PutObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLegalHold.html)  **
  - **Description:** Grants permission to apply a Legal Hold configuration to the specified object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Write

- **   [PutObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html)  **
  - **Description:** Grants permission to place an Object Retention configuration on an object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Write

- **   [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)  **
  - **Description:** Grants permission to set the supplied tag-set to an object that already exists in a bucket
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Tagging, Write

- **   [PutObjectVersionAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html)  **
  - **Description:** Grants permission to use the acl subresource to set the access control list (ACL) permissions for an object that already exists in a bucket
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)<br />[s3-object-lambda:versionid](#list_s3-object-lambda-s3-object-lambda_versionid)
  - **Access level:** Permissions management, Write

- **   [PutObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)  **
  - **Description:** Grants permission to set the supplied tag-set for a specific version of an object
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)<br />[s3-object-lambda:versionid](#list_s3-object-lambda-s3-object-lambda_versionid)
  - **Access level:** Tagging, Write

- **   [RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html)  **
  - **Description:** Grants permission to restore an archived copy of an object back into Amazon S3
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Write

- **   [WriteGetObjectResponse](https://docs.aws.amazon.com/AmazonS3/latest/API/API_WriteGetObjectResponse.html)  **
  - **Description:** Grants permission to provide data for GetObject requests send to S3 Object Lambda
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-object-lambda-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3-object-lambda:authType](#list_s3-object-lambda-s3-object-lambda_authType)<br />[s3-object-lambda:signatureAge](#list_s3-object-lambda-s3-object-lambda_signatureAge)<br />[s3-object-lambda:TlsVersion](#list_s3-object-lambda-s3-object-lambda_TlsVersion)
  - **Access level:** Write



## Resource types defined by Amazon S3 Object Lambda
<a name="list_s3-object-lambda-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [objectlambdaaccesspoint](https://docs.aws.amazon.com/AmazonS3/latest/dev/transforming-objects.html)  | arn:${Partition}:s3-object-lambda:${Region}:${Account}:accesspoint/${AccessPointName} |   | 

## Condition keys for Amazon S3 Object Lambda
<a name="list_s3-object-lambda-policy-keys"></a>

Amazon S3 Object Lambda defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [s3-object-lambda:TlsVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by the TLS version used by the client | Numeric | 
|   [s3-object-lambda:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by authentication method | String | 
|   [s3-object-lambda:signatureAge](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by the age in milliseconds of the request signature | Numeric | 
|   [s3-object-lambda:versionid](https://docs.aws.amazon.com/AmazonS3/latest/dev/amazon-s3-policy-keys.html/#getobjectversion-limit-access-to-specific-version-3)  | Filters access by a specific object version | String | 