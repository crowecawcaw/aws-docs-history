# ListBucket (SOAP API)

###### Note


 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on October 31, 2025. We recommend that you use either the REST API or the AWS SDKs.
 

 The `ListBucket` operation returns information about some of the items in the
 bucket. 

 For a general introduction to the list operation, see the [Listing Object Keys](../userguide/ListingKeysUsingAPIs.md "../userguide/ListingKeysUsingAPIs.md").

## Requests


This example lists up to 1000 keys in the "quotes" bucket that have the prefix
 "notes."


### Syntax



```
<ListBucket xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <Bucket>quotes</Bucket>
  <Prefix>notes/</Prefix>
  <Delimiter>/</Delimiter>
  <MaxKeys>1000</MaxKeys>
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
</ListBucket>
            
```

### Parameters




|  Name  |  Description  |  Required  |
| --- | --- | --- |
| `prefix` | Limits the response to keys which begin with the indicated
 prefix. You can use prefixes to separate a bucket into different
 sets of keys in a way similar to how a file system uses
 folders.
ImportantReplacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").
Type: String
Default: None |  No  |
| `marker` | Indicates where in the bucket to begin listing. The list
 will only include keys that occur lexicographically after
 marker. This is convenient for pagination: To get the next page
 of results use the last key of the current page as the
 marker.
Type: String
Default: None |  No  |
| `max-keys` | The maximum number of keys you'd like to see in the
 response body. The server might return fewer than this many
 keys, but will not return more.
Type: String
Default: None |  No  |
| `delimiter` | Causes keys that contain the same string between the prefix
 and the first occurrence of the delimiter to be rolled up into a
 single result element in the CommonPrefixes collection. These
 rolled-up keys are not returned elsewhere in the
 response.
Type: String
Default: None |  No  |


## Success Response


This response assumes the bucket contains the following keys:



```
notes/todos.txt
notes/2005-05-23/customer_mtg_notes.txt
notes/2005-05-23/phone_notes.txt
notes/2005-05-28/sales_notes.txt
```

### Syntax



```
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Name>backups</Name>
  <Prefix>notes/</Prefix>
  <MaxKeys>1000</MaxKeys>
  <Delimiter>/</Delimiter>
  <IsTruncated>false</IsTruncated>
  <Contents>
    <Key>notes/todos.txt</Key>
    <LastModified>2006-01-01T12:00:00.000Z</LastModified>
    <ETag>&quot;828ef3fdfa96f00ad9f27c383fc9ac7f&quot;</ETag>
    <Size>5126</Size>
    <StorageClass>STANDARD</StorageClass>
    <Owner>
      <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
      <DisplayName>webfile</DisplayName>
    </Owner>
    <StorageClass>STANDARD</StorageClass>
  </Contents>
  <CommonPrefixes>
    <Prefix>notes/2005-05-23/</Prefix>
  </CommonPrefixes>
  <CommonPrefixes>
    <Prefix>notes/2005-05-28/</Prefix>
  </CommonPrefixes>
  </ListBucketResult>
```

As you can see, many of the fields in the response echo the request parameters.
 `IsTruncated`, `Contents`, and
 `CommonPrefixes` are the only response elements that can
 contain new information.


### Response Elements




|  Name  |  Description  |
| --- | --- |
| `Contents` | Metadata about each object returned.
Type: XML metadata
Ancestor: ListBucketResult |
| `CommonPrefixes` | 
A response can contain `CommonPrefixes` only if you specify a `delimiter`. When you do, `CommonPrefixes` contains all (if there are any) keys between `Prefix` and the next occurrence of the string specified by `delimiter`. In effect, `CommonPrefixes` lists keys that act like subdirectories in the directory specified by `Prefix`. For example, if `prefix` is `notes/` and `delimiter` is a slash (/), in `notes/summer/july`, the common prefix is `notes/summer/`.

Type: String
Ancestor: ListBucketResult |
| `Delimiter` | Causes keys that contain the same string between the prefix
 and the first occurrence of the delimiter to be rolled up into a
 single result element in the CommonPrefixes collection. These
 rolled-up keys are not returned elsewhere in the
 response.
Type: String
Ancestor: ListBucketResult |
| `IsTruncated` | Specifies whether (true) or not (false) all of the results
 were returned. All of the results may not be returned if the
 number of results exceeds that specified by `MaxKeys`.
Type: String
Ancestor: boolean |
| `Marker` | Indicates where in the bucket to begin listing.
Type: String
Ancestor: ListBucketResult |
| `MaxKeys` | The maximum number of keys returned in the response
 body.
Type: String
Ancestor: ListBucketResult |
| `Name` | Name of the bucket.
Type: String
Ancestor: ListBucketResult |
| `Prefix` | Keys that begin with the indicated prefix.
Type: String
Ancestor: ListBucketResult |


## Response Body


 For information about the list response, see [Listing Keys Response](../userguide/ListingKeysUsingAPIs.md "../userguide/ListingKeysUsingAPIs.md"). 


## Access Control


To list the keys of a bucket you need to have been granted `READ` access on
 the bucket.
