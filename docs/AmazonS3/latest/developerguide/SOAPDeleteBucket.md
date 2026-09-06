

# DeleteBucket (SOAP API)
<a name="SOAPDeleteBucket"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

The `DeleteBucket` operation deletes a bucket. All objects in the bucket must be deleted before the bucket itself can be deleted.

**Example**  
This example deletes the "quotes" bucket.  
`Sample Request`  

```
1. <DeleteBucket xmlns="https://doc.s3.amazonaws.com/2006-03-01">
2.   <Bucket>quotes</Bucket>
3.   <AWSAccessKeyId> AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
4.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
5.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
6. </DeleteBucket>
```
`Sample Response`  

```
1. <DeleteBucketResponse xmlns="https://s3.amazonaws.com/doc/2006-03-01">
2.   <DeleteBucketResponse>
3.     <Code>204</Code>
4.     <Description>No Content</Description>
5.   </DeleteBucketResponse>
6. </DeleteBucketResponse>
```

## Elements
<a name="SOAPDeleteBucketElements"></a>
+ `Bucket:` The name of the bucket you want to delete.

## Access Control
<a name="SOAPDeleteBucketAccessControl"></a>

Only the owner of a bucket is allowed to delete it, regardless the access control policy on the bucket.