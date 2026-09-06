

# CreateBucket (SOAP API)
<a name="SOAPCreateBucket"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

The `CreateBucket` operation creates a bucket. Not every string is an acceptable bucket name. For information on bucket naming restrictions, see [Working with Amazon S3 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) .

**Note**  
 To determine whether a bucket name exists, use `ListBucket` and set `MaxKeys` to 0. A NoSuchBucket response indicates that the bucket is available, an AccessDenied response indicates that someone else owns the bucket, and a Success response indicates that you own the bucket or have permission to access it. 

**Example Create a bucket named "quotes"**  
`Sample Request`  

```
1. <CreateBucket xmlns="https://doc.s3.amazonaws.com/2006-03-01">
2.   <Bucket>quotes</Bucket>
3.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
4.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
5.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
6. </CreateBucket>
```
`Sample Response`  

```
1. <CreateBucketResponse xmlns="https://s3.amazonaws.com/doc/2006-03-01">
2.   <CreateBucketResponse>
3.     <Bucket>quotes</Bucket>
4.   </CreateBucketResponse>
5. </CreateBucketResponse>
```

## Elements
<a name="SOAPCreateBucketElements"></a>
+ `Bucket:` The name of the bucket you are trying to create. 

  
+ `AccessControlList:` The access control list for the new bucket. This element is optional. If not provided, the bucket is created with an access policy that give the requester FULL\_CONTROL access.

  

## Access Control
<a name="SOAPCreateBucketAccessControl"></a>

You must authenticate with a valid AWS Access Key ID. Anonymous requests are never allowed to create buckets.

## Related Resources
<a name="SOAPCreateBucket_RelatedResources"></a>
+  [ListBucket (SOAP API)](SOAPListBucket.md) 