

# ListAllMyBuckets (SOAP API)
<a name="SOAPListAllMyBuckets"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

The `ListAllMyBuckets` operation returns a list of all buckets owned by the sender of the request.

**Example**  
`Sample Request`  

```
1. <ListAllMyBuckets xmlns="https://doc.s3.amazonaws.com/2006-03-01">
2.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
3.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
4.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
5. </ListAllMyBuckets>
```
`Sample Response`  

```
 1. <ListAllMyBucketsResult xmlns="https://s3.amazonaws.com/doc/2006-03-01">
 2.   <Owner>
 3.     <ID>bcaf1ffd86f41161ca5fb16fd081034f</ID>
 4.     <DisplayName>webfile</DisplayName>
 5.   </Owner>
 6.   <Buckets>
 7.     <Bucket>
 8.       <Name>quotes;/Name>
 9.       <CreationDate>2006-02-03T16:45:09.000Z</CreationDate>
10.     </Bucket>
11.     <Bucket>
12.       <Name>samples</Name>
13.       <CreationDate>2006-02-03T16:41:58.000Z</CreationDate>
14.     </Bucket>
15.  </Buckets>
16. </ListAllMyBucketsResult>
```

## Response Body
<a name="SOAPListAllMyBucketsResponseBody"></a>
+ `Owner:`

  This provides information that Amazon S3 uses to represent your identity for purposes of authentication and access control. ID is a unique and permanent identifier for the developer who made the request. DisplayName is a human-readable name representing the developer who made the request. It is not unique, and might change over time.We recommend that you match your DisplayName to your Forum name.
+ `Name:`

  The name of a bucket. Note that if one of your buckets was recently deleted, the name of the deleted bucket might still be present in this list for a period of time.
+ `CreationDate:`

   The time that the bucket was created.

## Access Control
<a name="SOAPListAllMyBucketsAccessControl"></a>

You must authenticate with a valid AWS Access Key ID. Anonymous requests are never allowed to list buckets, and you can only list buckets for which you are the owner.