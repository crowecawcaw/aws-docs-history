# GetObject (SOAP API)

###### Note


 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on October 31, 2025. We recommend that you use either the REST API or the AWS SDKs.
 

The `GetObject` operation returns the current version of an object. If you try to
 `GetObject` an object that has a delete marker as its current version, S3
 returns a 404 error. You cannot use the SOAP API to retrieve a specified version of an object.
 To do that, use the REST API. For more information, see [Versioning](../userguide/Versioning.md "../userguide/Versioning.md"). For more options, use the [GetObjectExtended (SOAP API)](SOAPGetObjectExtended.md "SOAPGetObjectExtended.md") operation.

###### Note

Object key names with the value "soap" aren't supported for [virtual-hosted-style requests](../userguide/VirtualHosting.md#virtual-hosted-style-access "../userguide/VirtualHosting.md#virtual-hosted-style-access"). For object key name values where "soap" is used, a
 [path-style
 URL](../userguide/VirtualHosting.md#path-style-access "../userguide/VirtualHosting.md#path-style-access") must be used instead.

###### Example

This example gets the "Nelson" object from the "quotes" bucket.

`Sample Request`


```
<GetObject xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <Bucket>quotes</Bucket>
  <Key>Nelson</Key>
  <GetMetadata>true</GetMetadata>
  <GetData>true</GetData>
  <InlineData>true</InlineData>
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
</GetObject>
```
`Sample Response`


```
<GetObjectResponse xmlns="http://s3.amazonaws.com/doc/2006-03-01">
  <GetObjectResponse>
    <Status>
      <Code>200</Code>
      <Description>OK</Description>
    </Status>
    <Metadata>
      <Name>Content-Type</Name>
      <Value>text/plain</Value>
    </Metadata>
    <Metadata>
      <Name>family</Name>
      <Value>Muntz</Value>
    </Metadata>
    <Data>aGEtaGE=</Data>
    <LastModified>2006-01-01T12:00:00.000Z</LastModified>
    <ETag>&quot;828ef3fdfa96f00ad9f27c383fc9ac7f&quot;</ETag>
  </GetObjectResponse>
</GetObjectResponse>
```
## Elements



* `Bucket:` The bucket from which to retrieve the object.
* `Key:` The key that identifies the object.


###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").
* `GetMetadata:` The metadata is returned with the object if this
 is true.
* `GetData:` The object data is returned if this is true.
* `InlineData:` If this is true, then the data is returned, base
 64-encoded, as part of the SOAP body of the response. If false, then the data is returned
 as a SOAP attachment. The InlineData option is not suitable for use with large objects.
 The system limits this operation to working with 1MB of data or less. A GetObject request
 with the InlineData flag set will fail with the `InlineDataTooLargeError` status code if the resulting Data parameter would
 have encoded more than 1MB. To download large objects, consider calling GetObject without
 setting the InlineData flag, or use the REST API instead.

## Returned Elements



* `Metadata:` The name-value paired metadata stored with the
 object.
* `Data:` If InlineData was true in the request, this contains the
 base 64 encoded object data.
* `LastModified:` The time that the object was stored in
 Amazon S3.
* `ETag:` The object's entity tag. This is a hash of the object
 that can be used to do conditional gets. The ETag only reflects changes to the contents of an object, not its metadata.

## Access Control


You can read an object only if you have been granted `READ` access to the
 object.


## SOAP Chunked and Resumable Downloads


To provide `GET` flexibility, Amazon S3 supports chunked and resumable
 downloads.


Select from the following:



* For large object downloads, you might want to break them into smaller chunks. For more
 information, see [Range GETs](#SOAPRangeGETs "#SOAPRangeGETs")
* For `GET` operations that fail, you can design your application to
 download the remainder instead of the entire file. For more information, see [REST GET Error Recovery](#SOAPGETErrorRecovery "#SOAPGETErrorRecovery")

### Range GETs


For some clients, you might want to break large downloads into smaller downloads. To
 break a GET into smaller units, use Range. 


Before you can break a GET into smaller units, you must determine its size. For example,
 the following request gets the size of the bigfile object. 



```
<ListBucket xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <Bucket>bigbucket</Bucket>
  <Prefix>bigfile</Prefix>
  <MaxKeys>1</MaxKeys>
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
</ListBucket>
```

Amazon S3 returns the following response.



```
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01">
  <Name>quotes</Name>
  <Prefix>N</Prefix>
  <MaxKeys>1</MaxKeys>
  <IsTruncated>false</IsTruncated>
  <Contents>
    <Key>bigfile</Key>
    <LastModified>2006-01-01T12:00:00.000Z</LastModified>
    <ETag>&quot;828ef3fdfa96f00ad9f27c383fc9ac7f&quot;</ETag>
    <Size>2023276</Size>
    <StorageClass>STANDARD</StorageClass>
    <Owner>
      <ID>bcaf1ffd86f41161ca5fb16fd081034f</ID>
      <DisplayName>bigfile</DisplayName>
     </Owner>
  </Contents>
</ListBucketResult>
```

Following is a request that downloads the first megabyte from the bigfile object. 



```
<GetObject xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <Bucket>bigbucket</Bucket>
  <Key>bigfile</Key>
  <GetMetadata>true</GetMetadata>
  <GetData>true</GetData>
  <InlineData>true</InlineData>
  <ByteRangeStart>0</ByteRangeStart>
  <ByteRangeEnd>1048576</ByteRangeEnd>
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
</GetObject>
```

Amazon S3 returns the first megabyte of the file and the Etag of the file.



```
<GetObjectResponse xmlns="http://s3.amazonaws.com/doc/2006-03-01">
  <GetObjectResponse>
    <Status>
      <Code>200</Code>
      <Description>OK</Description>
    </Status>
    <Metadata>
      <Name>Content-Type</Name>
      <Value>text/plain</Value>
    </Metadata>
    <Metadata>
      <Name>family</Name>
      <Value>Muntz</Value>
    </Metadata>
    <Data>--first megabyte of bigfile--</Data>
    <LastModified>2006-01-01T12:00:00.000Z</LastModified>
    <ETag>"828ef3fdfa96f00ad9f27c383fc9ac7f"</ETag>
  </GetObjectResponse>
</GetObjectResponse>
```

To ensure the file did not change since the previous portion was downloaded, specify the
 IfMatch element. Although the IfMatch element is not required, it is recommended for content
 that is likely to change. 


The following is a request that gets the remainder of the file, using the IfMatch
 request header.



```
<GetObject xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <Bucket>bigbucket</Bucket>
  <Key>bigfile</Key>
  <GetMetadata>true</GetMetadata>
  <GetData>true</GetData>
  <InlineData>true</InlineData>
  <ByteRangeStart>10485761</ByteRangeStart>
  <ByteRangeEnd>2023276</ByteRangeEnd>
  <IfMatch>"828ef3fdfa96f00ad9f27c383fc9ac7f"</IfMatch>
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
</GetObject>
```

Amazon S3 returns the following response and the remainder of the file.



```
<GetObjectResponse xmlns="http://s3.amazonaws.com/doc/2006-03-01">
  <GetObjectResponse>
    <Status>
      <Code>200</Code>
      <Description>OK</Description>
    </Status>
    <Metadata>
      <Name>Content-Type</Name>
      <Value>text/plain</Value>
    </Metadata>
    <Metadata>
      <Name>family</Name>
      <Value>>Muntz</Value>
    </Metadata>
    <Data>--remainder of bigfile--</Data>
    <LastModified>2006-01-01T12:00:00.000Z</LastModified>
    <ETag>"828ef3fdfa96f00ad9f27c383fc9ac7f"</ETag>
  </GetObjectResponse>
</GetObjectResponse>
```

### Versioned GetObject


The following request returns the specified version of the object in the bucket. 



```
<GetObject xmlns="http://doc.s3.amazonaws.com/2006-03-01">
<Bucket>quotes</Bucket>
<Key>Nelson</Key>
<GetMetadata>true</GetMetadata>
<GetData>true</GetData>
<InlineData>true</InlineData>
<AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
<Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
<Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
</GetObject>
```

Sample Response



```
<GetObjectResponse xmlns="http://s3.amazonaws.com/doc/2006-03-01">
<GetObjectResponse>
<Status>
<Code>200</Code>
<Description>OK</Description>
</Status>
<Metadata>
<Name>Content-Type</Name>
<Value>text/plain</Value>
</Metadata>
<Metadata>
<Name>family</Name>
<Value>Muntz</Value>
</Metadata>
<Data>aGEtaGE=</Data>
<LastModified>2006-01-01T12:00:00.000Z</LastModified>
<ETag>&quot;828ef3fdfa96f00ad9f27c383fc9ac7f&quot;</ETag>
</GetObjectResponse>
</GetObjectResponse>
```

### REST GET Error Recovery


If an object GET fails, you can get the rest of the file by specifying the range to
 download. To do so, you must get the size of the object using `ListBucket` and perform a range `GET` on the remainder of
 the file. For more information, see [GetObjectExtended (SOAP API)](SOAPGetObjectExtended.md "SOAPGetObjectExtended.md").


### Related Resources


[Operations on Objects (SOAP API)](SOAPObjectsOps.md "SOAPObjectsOps.md")
