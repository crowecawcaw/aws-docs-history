# Versioning

If you enable versioning for a bucket, `POST` automatically generates a unique
 version ID for the object being added. Amazon S3 returns this ID in the response by using the
 `x-amz-version-id` response header. 

If you suspend versioning for a bucket, Amazon S3 always uses `null` as the version
 ID of the object stored in a bucket. 

For more information about returning the versioning state of a bucket, see [GET Bucket (Versioning Status)](API_GetBucketVersioning.md "API_GetBucketVersioning.md").

Amazon S3 is a distributed system. If you enable versioning for a bucket and Amazon S3 receives
 multiple write requests for the same object simultaneously, all versions of the object are
 stored. 

To see sample requests that use versioning, see [Sample Request](RESTObjectPOST.md#ExampleVersionObjectPost "RESTObjectPOST.md#ExampleVersionObjectPost").
