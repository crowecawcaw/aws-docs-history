

# GetObject (SOAP API)
<a name="SOAPGetObject"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

The `GetObject` operation returns the current version of an object. If you try to `GetObject` an object that has a delete marker as its current version, S3 returns a 404 error. You cannot use the SOAP API to retrieve a specified version of an object. To do that, use the REST API. For more information, see [Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html). For more options, use the [GetObjectExtended (SOAP API)](SOAPGetObjectExtended.md) operation.

**Note**  
Object key names with the value "soap" aren't supported for [virtual-hosted-style requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#virtual-hosted-style-access). For object key name values where "soap" is used, a [path-style URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#path-style-access) must be used instead.

**Example**  
This example gets the "Nelson" object from the "quotes" bucket.  
`Sample Request`  

```
 1. <GetObject xmlns="https://doc.s3.amazonaws.com/2006-03-01">
 2.   <Bucket>quotes</Bucket>
 3.   <Key>Nelson</Key>
 4.   <GetMetadata>true</GetMetadata>
 5.   <GetData>true</GetData>
 6.   <InlineData>true</InlineData>
 7.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
 8.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
 9.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
10. </GetObject>
```
`Sample Response`  

```
 1. <GetObjectResponse xmlns="https://s3.amazonaws.com/doc/2006-03-01">
 2.   <GetObjectResponse>
 3.     <Status>
 4.       <Code>200</Code>
 5.       <Description>OK</Description>
 6.     </Status>
 7.     <Metadata>
 8.       <Name>Content-Type</Name>
 9.       <Value>text/plain</Value>
10.     </Metadata>
11.     <Metadata>
12.       <Name>family</Name>
13.       <Value>Muntz</Value>
14.     </Metadata>
15.     <Data>aGEtaGE=</Data>
16.     <LastModified>2006-01-01T12:00:00.000Z</LastModified>
17.     <ETag>&quot;828ef3fdfa96f00ad9f27c383fc9ac7f&quot;</ETag>
18.   </GetObjectResponse>
19. </GetObjectResponse>
```

## Elements
<a name="SOAPGetObjectElements"></a>
+ `Bucket:` The bucket from which to retrieve the object.
+ `Key:` The key that identifies the object.
+ `GetMetadata:` The metadata is returned with the object if this is true.
+ `GetData:` The object data is returned if this is true.
+ `InlineData:` If this is true, then the data is returned, base 64-encoded, as part of the SOAP body of the response. If false, then the data is returned as a SOAP attachment. The InlineData option is not suitable for use with large objects. The system limits this operation to working with 1MB of data or less. A GetObject request with the InlineData flag set will fail with the `InlineDataTooLargeError` status code if the resulting Data parameter would have encoded more than 1MB. To download large objects, consider calling GetObject without setting the InlineData flag, or use the REST API instead.

## Returned Elements
<a name="SOAPGetObjectReturnedElements"></a>
+ `Metadata:` The name-value paired metadata stored with the object.
+ `Data:` If InlineData was true in the request, this contains the base 64 encoded object data.
+ `LastModified:` The time that the object was stored in Amazon S3.
+ `ETag:` The object's entity tag. This is a hash of the object that can be used to do conditional gets. The ETag only reflects changes to the contents of an object, not its metadata.

## Access Control
<a name="SOAPGetObjectAccessControl"></a>

You can read an object only if you have been granted `READ` access to the object.

## SOAP Chunked and Resumable Downloads
<a name="SOAPResumableDownloads"></a>

To provide `GET` flexibility, Amazon S3 supports chunked and resumable downloads.

Select from the following:
+ For large object downloads, you might want to break them into smaller chunks. For more information, see [Range GETs](#SOAPRangeGETs) 
+ For `GET` operations that fail, you can design your application to download the remainder instead of the entire file. For more information, see [REST GET Error Recovery](#SOAPGETErrorRecovery)

### Range GETs
<a name="SOAPRangeGETs"></a>

For some clients, you might want to break large downloads into smaller downloads. To break a GET into smaller units, use Range. 

Before you can break a GET into smaller units, you must determine its size. For example, the following request gets the size of the bigfile object. 

```
1. <ListBucket xmlns="https://doc.s3.amazonaws.com/2006-03-01">
2.   <Bucket>bigbucket</Bucket>
3.   <Prefix>bigfile</Prefix>
4.   <MaxKeys>1</MaxKeys>
5.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
6.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
7.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
8. </ListBucket>
```

Amazon S3 returns the following response.

```
 1. <ListBucketResult xmlns="https://s3.amazonaws.com/doc/2006-03-01">
 2.   <Name>quotes</Name>
 3.   <Prefix>N</Prefix>
 4.   <MaxKeys>1</MaxKeys>
 5.   <IsTruncated>false</IsTruncated>
 6.   <Contents>
 7.     <Key>bigfile</Key>
 8.     <LastModified>2006-01-01T12:00:00.000Z</LastModified>
 9.     <ETag>&quot;828ef3fdfa96f00ad9f27c383fc9ac7f&quot;</ETag>
10.     <Size>2023276</Size>
11.     <StorageClass>STANDARD</StorageClass>
12.     <Owner>
13.       <ID>bcaf1ffd86f41161ca5fb16fd081034f</ID>
14.       <DisplayName>bigfile</DisplayName>
15.      </Owner>
16.   </Contents>
17. </ListBucketResult>
```

Following is a request that downloads the first megabyte from the bigfile object. 

```
 1. <GetObject xmlns="https://doc.s3.amazonaws.com/2006-03-01">
 2.   <Bucket>bigbucket</Bucket>
 3.   <Key>bigfile</Key>
 4.   <GetMetadata>true</GetMetadata>
 5.   <GetData>true</GetData>
 6.   <InlineData>true</InlineData>
 7.   <ByteRangeStart>0</ByteRangeStart>
 8.   <ByteRangeEnd>1048576</ByteRangeEnd>
 9.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
10.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
11.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
12. </GetObject>
```

Amazon S3 returns the first megabyte of the file and the Etag of the file.

```
 1. <GetObjectResponse xmlns="http://s3.amazonaws.com/doc/2006-03-01">
 2.   <GetObjectResponse>
 3.     <Status>
 4.       <Code>200</Code>
 5.       <Description>OK</Description>
 6.     </Status>
 7.     <Metadata>
 8.       <Name>Content-Type</Name>
 9.       <Value>text/plain</Value>
10.     </Metadata>
11.     <Metadata>
12.       <Name>family</Name>
13.       <Value>Muntz</Value>
14.     </Metadata>
15.     <Data>--first megabyte of bigfile--</Data>
16.     <LastModified>2006-01-01T12:00:00.000Z</LastModified>
17.     <ETag>"828ef3fdfa96f00ad9f27c383fc9ac7f"</ETag>
18.   </GetObjectResponse>
19. </GetObjectResponse>
```

To ensure the file did not change since the previous portion was downloaded, specify the IfMatch element. Although the IfMatch element is not required, it is recommended for content that is likely to change. 

The following is a request that gets the remainder of the file, using the IfMatch request header.

```
 1. <GetObject xmlns="https://doc.s3.amazonaws.com/2006-03-01">
 2.   <Bucket>bigbucket</Bucket>
 3.   <Key>bigfile</Key>
 4.   <GetMetadata>true</GetMetadata>
 5.   <GetData>true</GetData>
 6.   <InlineData>true</InlineData>
 7.   <ByteRangeStart>10485761</ByteRangeStart>
 8.   <ByteRangeEnd>2023276</ByteRangeEnd>
 9.   <IfMatch>"828ef3fdfa96f00ad9f27c383fc9ac7f"</IfMatch>
10.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
11.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
12.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
13. </GetObject>
```

Amazon S3 returns the following response and the remainder of the file.

```
 1. <GetObjectResponse xmlns="http://s3.amazonaws.com/doc/2006-03-01">
 2.   <GetObjectResponse>
 3.     <Status>
 4.       <Code>200</Code>
 5.       <Description>OK</Description>
 6.     </Status>
 7.     <Metadata>
 8.       <Name>Content-Type</Name>
 9.       <Value>text/plain</Value>
10.     </Metadata>
11.     <Metadata>
12.       <Name>family</Name>
13.       <Value>>Muntz</Value>
14.     </Metadata>
15.     <Data>--remainder of bigfile--</Data>
16.     <LastModified>2006-01-01T12:00:00.000Z</LastModified>
17.     <ETag>"828ef3fdfa96f00ad9f27c383fc9ac7f"</ETag>
18.   </GetObjectResponse>
19. </GetObjectResponse>
```

### Versioned GetObject
<a name="SOAPResumableDownloads-versioned-getobject"></a>

The following request returns the specified version of the object in the bucket. 

```
 1. <GetObject xmlns="https://doc.s3.amazonaws.com/2006-03-01">
 2. <Bucket>quotes</Bucket>
 3. <Key>Nelson</Key>
 4. <GetMetadata>true</GetMetadata>
 5. <GetData>true</GetData>
 6. <InlineData>true</InlineData>
 7. <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
 8. <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
 9. <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
10. </GetObject>
```

Sample Response

```
 1. <GetObjectResponse xmlns="https://s3.amazonaws.com/doc/2006-03-01">
 2. <GetObjectResponse>
 3. <Status>
 4. <Code>200</Code>
 5. <Description>OK</Description>
 6. </Status>
 7. <Metadata>
 8. <Name>Content-Type</Name>
 9. <Value>text/plain</Value>
10. </Metadata>
11. <Metadata>
12. <Name>family</Name>
13. <Value>Muntz</Value>
14. </Metadata>
15. <Data>aGEtaGE=</Data>
16. <LastModified>2006-01-01T12:00:00.000Z</LastModified>
17. <ETag>&quot;828ef3fdfa96f00ad9f27c383fc9ac7f&quot;</ETag>
18. </GetObjectResponse>
19. </GetObjectResponse>
```

### REST GET Error Recovery
<a name="SOAPGETErrorRecovery"></a>

If an object GET fails, you can get the rest of the file by specifying the range to download. To do so, you must get the size of the object using `ListBucket` and perform a range `GET` on the remainder of the file. For more information, see [GetObjectExtended (SOAP API)](SOAPGetObjectExtended.md).

### Related Resources
<a name="SOAPGettingObjectsRelatedTopics"></a>

[Operations on Objects (SOAP API)](SOAPObjectsOps.md)