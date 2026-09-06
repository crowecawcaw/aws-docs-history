

# DeleteObject (SOAP API)
<a name="SOAPDeleteObject"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

The `DeleteObject` operation removes the specified object from Amazon S3. Once deleted, there is no method to restore or undelete an object.

**Note**  
If you delete an object that does not exist, Amazon S3 will return a success (not an error message). 

**Example**  
This example deletes the "Nelson" object from the "quotes" bucket.  
`Sample Request`  

```
1. <DeleteObject xmlns="https://doc.s3.amazonaws.com/2006-03-01">
2.   <Bucket>quotes</Bucket>
3.   <Key>Nelson</Key>
4.   <AWSAccessKeyId> AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
5.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
6.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
7. </DeleteObject>
```
`Sample Response`  

```
1. <DeleteObjectResponse xmlns="https://s3.amazonaws.com/doc/2006-03-01">
2.   <DeleteObjectResponse>
3.     <Code>200</Code>
4.     <Description>OK</Description>
5.   </DeleteObjectResponse>
6. </DeleteObjectResponse>
```

## Elements
<a name="SOAPDeleteObjectElements"></a>
+ `Bucket:` The bucket that holds the object.
+ `Key:` The key that identifies the object.

## Access Control
<a name="SOAPDeleteObjectAccessControl"></a>

You can delete an object only if you have `WRITE` access to the bucket, regardless of who owns the object or what rights are granted to it. 