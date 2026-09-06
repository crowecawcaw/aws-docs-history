

# ListBucket (SOAP API)
<a name="SOAPListBucket"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

 The `ListBucket` operation returns information about some of the items in the bucket. 

 For a general introduction to the list operation, see the [Listing Object Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ListingKeysUsingAPIs.html).

## Requests
<a name="SOAPBucketGET_Request"></a>

This example lists up to 1000 keys in the "quotes" bucket that have the prefix "notes."

### Syntax
<a name="SOAPBucketGET_RequestSyntax"></a>

```
1. <ListBucket xmlns="https://doc.s3.amazonaws.com/2006-03-01">
2.   <Bucket>quotes</Bucket>
3.   <Prefix>notes/</Prefix>
4.   <Delimiter>/</Delimiter>
5.   <MaxKeys>1000</MaxKeys>
6.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
7.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
8.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
9. </ListBucket>
```

### Parameters
<a name="SOAPBucketGET_RequestHeaders"></a>


|  Name  |  Description  |  Required  | 
| --- | --- | --- | 
|  prefix  | Limits the response to keys which begin with the indicated prefix. You can use prefixes to separate a bucket into different sets of keys in a way similar to how a file system uses folders.<br />Type: String<br />Default: None |  No  | 
|  marker  | Indicates where in the bucket to begin listing. The list will only include keys that occur lexicographically after marker. This is convenient for pagination: To get the next page of results use the last key of the current page as the marker.<br />Type: String<br />Default: None |  No  | 
|  max-keys  | The maximum number of keys you'd like to see in the response body. The server might return fewer than this many keys, but will not return more.<br />Type: String<br />Default: None |  No  | 
|  delimiter  | Causes keys that contain the same string between the prefix and the first occurrence of the delimiter to be rolled up into a single result element in the CommonPrefixes collection. These rolled-up keys are not returned elsewhere in the response.<br />Type: String<br />Default: None |  No  | 

## Success Response
<a name="SOAPBucketGET_ResponseSuccess"></a>

This response assumes the bucket contains the following keys:

```
1. notes/todos.txt
2. notes/2005-05-23/customer_mtg_notes.txt
3. notes/2005-05-23/phone_notes.txt
4. notes/2005-05-28/sales_notes.txt
```

### Syntax
<a name="SOAPBucketGET_ResponseSuccess-syntax"></a>

```
 1. <?xml version="1.0" encoding="UTF-8"?>
 2. <ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
 3.   <Name>backups</Name>
 4.   <Prefix>notes/</Prefix>
 5.   <MaxKeys>1000</MaxKeys>
 6.   <Delimiter>/</Delimiter>
 7.   <IsTruncated>false</IsTruncated>
 8.   <Contents>
 9.     <Key>notes/todos.txt</Key>
10.     <LastModified>2006-01-01T12:00:00.000Z</LastModified>
11.     <ETag>&quot;828ef3fdfa96f00ad9f27c383fc9ac7f&quot;</ETag>
12.     <Size>5126</Size>
13.     <StorageClass>STANDARD</StorageClass>
14.     <Owner>
15.       <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
16.       <DisplayName>webfile</DisplayName>
17.     </Owner>
18.     <StorageClass>STANDARD</StorageClass>
19.   </Contents>
20.   <CommonPrefixes>
21.     <Prefix>notes/2005-05-23/</Prefix>
22.   </CommonPrefixes>
23.   <CommonPrefixes>
24.     <Prefix>notes/2005-05-28/</Prefix>
25.   </CommonPrefixes>
26.   </ListBucketResult>
```

As you can see, many of the fields in the response echo the request parameters. `IsTruncated`, `Contents`, and `CommonPrefixes` are the only response elements that can contain new information.

### Response Elements
<a name="SOAPBucketGET_ResponseSuccess-response-elements"></a>


|  Name  |  Description  | 
| --- | --- | 
|  Contents  | Metadata about each object returned.<br />Type: XML metadata<br />Ancestor: ListBucketResult | 
|  CommonPrefixes  |  A response can contain `CommonPrefixes` only if you specify a `delimiter`. When you do, `CommonPrefixes` contains all (if there are any) keys between `Prefix` and the next occurrence of the string specified by `delimiter`. In effect, `CommonPrefixes` lists keys that act like subdirectories in the directory specified by `Prefix`. For example, if `prefix` is `notes/` and `delimiter` is a slash (/), in `notes/summer/july`, the common prefix is `notes/summer/`. <br />Type: String<br />Ancestor: ListBucketResult | 
|  Delimiter  | Causes keys that contain the same string between the prefix and the first occurrence of the delimiter to be rolled up into a single result element in the CommonPrefixes collection. These rolled-up keys are not returned elsewhere in the response.<br />Type: String<br />Ancestor: ListBucketResult | 
|  IsTruncated  | Specifies whether (true) or not (false) all of the results were returned. All of the results may not be returned if the number of results exceeds that specified by `MaxKeys`.<br />Type: String<br />Ancestor: boolean | 
|  Marker  | Indicates where in the bucket to begin listing.<br />Type: String<br />Ancestor: ListBucketResult | 
|  MaxKeys  | The maximum number of keys returned in the response body.<br />Type: String<br />Ancestor: ListBucketResult | 
|  Name  | Name of the bucket.<br />Type: String<br />Ancestor: ListBucketResult | 
|  Prefix  | Keys that begin with the indicated prefix.<br />Type: String<br />Ancestor: ListBucketResult | 

## Response Body
<a name="SOAPListBucketResponseBody"></a>

 For information about the list response, see [Listing Keys Response](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ListingKeysUsingAPIs.html). 

## Access Control
<a name="SOAPListBucketAccessControl"></a>

To list the keys of a bucket you need to have been granted `READ` access on the bucket.