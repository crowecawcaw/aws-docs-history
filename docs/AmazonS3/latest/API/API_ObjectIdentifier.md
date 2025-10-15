# ObjectIdentifier

Object Identifier is unique value to identify objects.


## Contents





**Key** 


Key name of the object.


###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").


Type: String


Length Constraints: Minimum length of 1.


Required: Yes




**ETag** 


An entity tag (ETag) is an identifier assigned by a web server to a specific version of a resource
 found at a URL. This header field makes the request method conditional on `ETags`. 


###### Note

Entity tags (ETags) for S3 Express One Zone are random alphanumeric strings unique to the object.
 


Type: String


Required: No




**LastModifiedTime** 


If present, the objects are deleted only if its modification times matches the provided
 `Timestamp`. 


###### Note

This functionality is only supported for directory buckets.


Type: Timestamp


Required: No




**Size** 


If present, the objects are deleted only if its size matches the provided size in bytes. 


###### Note

This functionality is only supported for directory buckets.


Type: Long


Required: No




**VersionId** 


Version ID for the specific version of the object to delete.


###### Note

This functionality is not supported for directory buckets.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ObjectIdentifier "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ObjectIdentifier")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ObjectIdentifier "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ObjectIdentifier")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ObjectIdentifier "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ObjectIdentifier")
