# API actions for Lightsail objects

Use the following API actions for Amazon Simple Storage Service (Amazon S3) to manage buckets and objects in the
Amazon Lightsail object storage service. Choose the name of an API action to view the
documentation for it in the _Amazon S3 API reference_. For more information
about buckets in Lightsail, see [Store and manage data with Lightsail object storage buckets](buckets-in-amazon-lightsail.md "buckets-in-amazon-lightsail.md").

###### Uploading files to buckets

- [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") - Adds a file to a bucket. For more information, see [Uploading files to a bucket in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket.md "amazon-lightsail-uploading-files-to-a-bucket.md").

###### Uploading objects to buckets using multipart upload

- [CreateMultipartUpload](../../../AmazonS3/latest/API/API_CreateMultipartUpload.md "../../../AmazonS3/latest/API/API_CreateMultipartUpload.md") - Initiates a multipart upload and returns an
  upload ID. For more information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md "amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md").
- [UploadPart](../../../AmazonS3/latest/API/API_UploadPart.md "../../../AmazonS3/latest/API/API_UploadPart.md") - Uploads a part in a specific multipart upload. For more
  information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md "amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md").
- [ListParts](../../../AmazonS3/latest/API/API_ListParts.md "../../../AmazonS3/latest/API/API_ListParts.md") - Lists the parts that have been uploaded for a specific
  multipart upload. For more information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md "amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md").
- [CompleteMultipartUpload](../../../AmazonS3/latest/API/API_CompleteMultipartUpload.md "../../../AmazonS3/latest/API/API_CompleteMultipartUpload.md") - Completes a multipart upload by assembling
  previously uploaded parts. For more information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md "amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md").
- [ListMultipartUploads](../../../AmazonS3/latest/API/API_ListMultipartUploads.md "../../../AmazonS3/latest/API/API_ListMultipartUploads.md") - Lists all in-progress multipart uploads for a
  bucket. For more information, see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md "amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md").
- [AbortMultipartUpload](../../../AmazonS3/latest/API/API_AbortMultipartUpload.md "../../../AmazonS3/latest/API/API_AbortMultipartUpload.md") - Stops a multipart upload. For more information,
  see [Uploading files to a bucket using multipart upload in Amazon Lightsail](amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md "amazon-lightsail-uploading-files-to-a-bucket-using-multipart-upload.md").

###### Listing objects and object details

- [ListObjectsV2](../../../AmazonS3/latest/API/API_ListObjectsV2.md "../../../AmazonS3/latest/API/API_ListObjectsV2.md") - Returns a list of the objects (up to 1,000 in each
  request) in a bucket. For more information, see [Viewing objects in a bucket in Amazon Lightsail](amazon-lightsail-viewing-objects-in-a-bucket.md "amazon-lightsail-viewing-objects-in-a-bucket.md").
- [HeadObject](../../../AmazonS3/latest/API/API_HeadObject.md "../../../AmazonS3/latest/API/API_HeadObject.md") - Returns metadata from an object without returning the
  object itself. This action is useful if you're only interested in an object's
  metadata. For more information, see [Viewing objects in a bucket in Amazon Lightsail](amazon-lightsail-viewing-objects-in-a-bucket.md "amazon-lightsail-viewing-objects-in-a-bucket.md").
- [GetObject](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md") - Downloads an object from a bucket. For more information,
  see [Downloading objects from a bucket in Amazon Lightsail](amazon-lightsail-downloading-bucket-objects.md "amazon-lightsail-downloading-bucket-objects.md").
- [GetObjectTagging](../../../AmazonS3/latest/API/API_GetObjectTagging.md "../../../AmazonS3/latest/API/API_GetObjectTagging.md") - Returns the tags of an object. For more information,
  see [Tagging objects in a bucket in Amazon Lightsail](amazon-lightsail-tagging-bucket-objects.md "amazon-lightsail-tagging-bucket-objects.md").
- [ListObjectVersions](../../../AmazonS3/latest/API/API_ListObjectVersions.md "../../../AmazonS3/latest/API/API_ListObjectVersions.md") - Returns metadata about all versions of objects in
  a bucket. For more information, see [Enabling and suspending object versioning in a bucket in
  Amazon Lightsail](amazon-lightsail-managing-bucket-object-versioning.md "amazon-lightsail-managing-bucket-object-versioning.md").

###### Copying and moving objects

- [CopyObject](../../../AmazonS3/latest/API/API_CopyObject.md "../../../AmazonS3/latest/API/API_CopyObject.md") - Creates a copy of an object. For more information, see
  [Copying or moving objects in a bucket in Amazon Lightsail](amazon-lightsail-copying-moving-bucket-objects.md "amazon-lightsail-copying-moving-bucket-objects.md").

###### Editing individual object permissions

- [PutObjectAcl](../../../AmazonS3/latest/API/API_PutObjectAcl.md "../../../AmazonS3/latest/API/API_PutObjectAcl.md") - Sets the access control list (ACL) permissions for an
  object, which is how you can control the access permissions for an individual
  object. For more information, see [Configuring access permissions for individual objects in a bucket in
  Amazon Lightsail](amazon-lightsail-configuring-individual-object-access.md "amazon-lightsail-configuring-individual-object-access.md").
- [GetObjectAcl](../../../AmazonS3/latest/API/API_GetObjectAcl.md "../../../AmazonS3/latest/API/API_GetObjectAcl.md") - Returns the access control list (ACL) set for an object,
  which controls the access permissions for the individual object. For more
  information, see [Configuring access permissions for individual objects in a bucket in
  Amazon Lightsail](amazon-lightsail-configuring-individual-object-access.md "amazon-lightsail-configuring-individual-object-access.md").

###### Editing object tags

- [PutObjectTagging](../../../AmazonS3/latest/API/API_PutObjectTagging.md "../../../AmazonS3/latest/API/API_PutObjectTagging.md") - Sets the supplied tag to an object. For more
  information, see [Tagging objects in a bucket in Amazon Lightsail](amazon-lightsail-tagging-bucket-objects.md "amazon-lightsail-tagging-bucket-objects.md").

###### Listing and restoring object versions

- [ListObjectVersions](../../../AmazonS3/latest/API/API_ListObjectVersions.md "../../../AmazonS3/latest/API/API_ListObjectVersions.md") - Returns metadata about all versions of objects in
  a bucket. For more information, see [Enabling and suspending object versioning in a bucket in
  Amazon Lightsail](amazon-lightsail-managing-bucket-object-versioning.md "amazon-lightsail-managing-bucket-object-versioning.md") and [Restoring previous versions of objects in a bucket in Amazon Lightsail](amazon-lightsail-restoring-bucket-object-versions.md "amazon-lightsail-restoring-bucket-object-versions.md").
- [CopyObject](../../../AmazonS3/latest/API/API_CopyObject.md "../../../AmazonS3/latest/API/API_CopyObject.md") - Creates a copy of an object in a bucket, including
  previous versions of an object. To restore an object version, use the
  `CopyObject` action to copy a previous version of an object and make
  it the latest version. For more information, see [Restoring previous versions of objects in a bucket in Amazon Lightsail](amazon-lightsail-restoring-bucket-object-versions.md "amazon-lightsail-restoring-bucket-object-versions.md").
- [DeleteObject](../../../AmazonS3/latest/API/API_DeleteObject.md "../../../AmazonS3/latest/API/API_DeleteObject.md") - Deletes an object from a bucket, including previous
  versions of an object. For more information, see [Deleting objects in a bucket in Amazon Lightsail](amazon-lightsail-deleting-bucket-objects.md "amazon-lightsail-deleting-bucket-objects.md").

###### Deleting objects

- [DeleteObject](../../../AmazonS3/latest/API/API_DeleteObject.md "../../../AmazonS3/latest/API/API_DeleteObject.md") - Deletes an object from a bucket. For more information,
  see [Deleting objects in a bucket in Amazon Lightsail](amazon-lightsail-deleting-bucket-objects.md "amazon-lightsail-deleting-bucket-objects.md").
- [DeleteObjects](../../../AmazonS3/latest/API/API_DeleteObjects.md "../../../AmazonS3/latest/API/API_DeleteObjects.md") - Deletes multiple objects from a bucket using a single
  request. For more information, see [Deleting objects in a bucket in Amazon Lightsail](amazon-lightsail-deleting-bucket-objects.md "amazon-lightsail-deleting-bucket-objects.md").
