# PutBucketAcl

###### Important

End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs). If you attempt to use an Email Grantee ACL in a request after October 1, 2025, 
 the request will receive an `HTTP 405` (Method Not Allowed) error.

This change affects the following AWS Regions: US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Ireland), and South America (São Paulo).

###### Note

This operation is not supported for directory buckets.

Sets the permissions on an existing bucket using access control lists (ACL). For more information,
 see [Using ACLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html"). To
 set the ACL of a bucket, you must have the `WRITE_ACP` permission.

You can use one of the following two ways to set a bucket's permissions:


* Specify the ACL in the request body
* Specify permissions using request headers
###### Note

You cannot specify access permission using both the body and the request headers.

Depending on your application needs, you may choose to set the ACL on a bucket using either the
 request body or the headers. For example, if you have an existing application that updates a bucket ACL
 using the request body, then you can continue to use that approach.

###### Important

If your bucket uses the bucket owner enforced setting for S3 Object Ownership, ACLs are disabled
 and no longer affect permissions. You must use policies to grant access to your bucket and the objects
 in it. Requests to set ACLs or update ACLs fail and return the
 `AccessControlListNotSupported` error code. Requests to read ACLs are still supported.
 For more information, see [Controlling object ownership](../userguide/about-object-ownership.md "../userguide/about-object-ownership.md") in
 the *Amazon S3 User Guide*.



Permissions

You can set access permissions by using one of the following methods:



* Specify a canned ACL with the `x-amz-acl` request header. Amazon S3 supports a set
 of predefined ACLs, known as *canned ACLs*. Each canned ACL has a
 predefined set of grantees and permissions. Specify the canned ACL name as the value of
 `x-amz-acl`. If you use this header, you cannot use other access control-specific
 headers in your request. For more information, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL "https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL").
* Specify access permissions explicitly with the `x-amz-grant-read`,
 `x-amz-grant-read-acp`, `x-amz-grant-write-acp`, and
 `x-amz-grant-full-control` headers. When using these headers, you specify
 explicit access permissions and grantees (AWS accounts or Amazon S3 groups) who will receive the
 permission. If you use these ACL-specific headers, you cannot use the `x-amz-acl`
 header to set a canned ACL. These parameters map to the set of permissions that Amazon S3 supports
 in an ACL. For more information, see [Access Control List (ACL)
 Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html").


You specify each grantee as a type=value pair, where the type is one of the
 following:




	+ `id` – if the value specified is the canonical user ID of an
	 AWS account
	+ `uri` – if you are granting permissions to a predefined group
	+ `emailAddress` – if the value specified is the email address of an
	 AWS account
	 
	
	
	###### Note
	
	Using email addresses to specify a grantee is only supported in the following AWS Regions: 
	
	
	
		- US East (N. Virginia)
		- US West (N. California)
		- US West (Oregon)
		- Asia Pacific (Singapore)
		- Asia Pacific (Sydney)
		- Asia Pacific (Tokyo)
		- Europe (Ireland)
		- South America (São Paulo)For a list of all the Amazon S3 supported Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the AWS General Reference.
For example, the following `x-amz-grant-write` header grants create, overwrite,
 and delete objects permission to LogDelivery group predefined by Amazon S3 and two AWS accounts
 identified by their email addresses.



`x-amz-grant-write: uri="http://acs.amazonaws.com/groups/s3/LogDelivery",
 id="111122223333", id="555566667777"`

You can use either a canned ACL or specify access permissions explicitly. You cannot do
 both.



Grantee Values

You can specify the person (grantee) to whom you're assigning access rights (using request
 elements) in the following ways. For examples of how to specify these grantee values in JSON
 format, see the AWS CLI example in  [Enabling Amazon S3 server
 access logging](../userguide/enable-server-access-logging.md "../userguide/enable-server-access-logging.md") in the *Amazon S3 User Guide*.



* By the person's ID:



`<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:type="CanonicalUser"><ID><>ID<></ID><DisplayName><>GranteesEmail<></DisplayName>
 </Grantee>`



DisplayName is optional and ignored in the request
* By URI:



`<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:type="Group"><URI><>http://acs.amazonaws.com/groups/global/AuthenticatedUsers<></URI></Grantee>`
* By Email address:



`<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:type="AmazonCustomerByEmail"><EmailAddress><>Grantees@email.com<></EmailAddress>&</Grantee>`



The grantee is resolved to the CanonicalUser and, in a response to a GET Object acl
 request, appears as the CanonicalUser. 


###### Note

Using email addresses to specify a grantee is only supported in the following AWS Regions: 



	+ US East (N. Virginia)
	+ US West (N. California)
	+ US West (Oregon)
	+ Asia Pacific (Singapore)
	+ Asia Pacific (Sydney)
	+ Asia Pacific (Tokyo)
	+ Europe (Ireland)
	+ South America (São Paulo)For a list of all the Amazon S3 supported Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the AWS General Reference.


The following operations are related to `PutBucketAcl`:


* [CreateBucket](API_CreateBucket.md "API_CreateBucket.md")
* [DeleteBucket](API_DeleteBucket.md "API_DeleteBucket.md")
* [GetObjectAcl](API_GetObjectAcl.md "API_GetObjectAcl.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?acl HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-acl: `ACL`
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-grant-full-control: `GrantFullControl`
x-amz-grant-read: `GrantRead`
x-amz-grant-read-acp: `GrantReadACP`
x-amz-grant-write: `GrantWrite`
x-amz-grant-write-acp: `GrantWriteACP`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[AccessControlPolicy](#AmazonS3-PutBucketAcl-request-AccessControlPolicy "#AmazonS3-PutBucketAcl-request-AccessControlPolicy") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[AccessControlList](#AmazonS3-PutBucketAcl-request-Grants "#AmazonS3-PutBucketAcl-request-Grants")>
      <Grant>
         <[Grantee](API_Grant.md#AmazonS3-Type-Grant-Grantee "API_Grant.md#AmazonS3-Type-Grant-Grantee")>
            <[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>`string`</[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>
            <[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>`string`</[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>
            <[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>`string`</[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>
            <[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>`string`</[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>
            <[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>`string`</[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>
         </[Grantee](API_Grant.md#AmazonS3-Type-Grant-Grantee "API_Grant.md#AmazonS3-Type-Grant-Grantee")>
         <[Permission](API_Grant.md#AmazonS3-Type-Grant-Permission "API_Grant.md#AmazonS3-Type-Grant-Permission")>`string`</[Permission](API_Grant.md#AmazonS3-Type-Grant-Permission "API_Grant.md#AmazonS3-Type-Grant-Permission")>
      </Grant>
   </[AccessControlList](#AmazonS3-PutBucketAcl-request-Grants "#AmazonS3-PutBucketAcl-request-Grants")>
   <[Owner](#AmazonS3-PutBucketAcl-request-Owner "#AmazonS3-PutBucketAcl-request-Owner")>
      <[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>`string`</[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>
      <[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>`string`</[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>
   </[Owner](#AmazonS3-PutBucketAcl-request-Owner "#AmazonS3-PutBucketAcl-request-Owner")>
</[AccessControlPolicy](#AmazonS3-PutBucketAcl-request-AccessControlPolicy "#AmazonS3-PutBucketAcl-request-AccessControlPolicy")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


The bucket to which to apply the ACL.


Required: Yes




**[Content-MD5](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


The Base64 encoded 128-bit `MD5` digest of the data. This header must be used as a
 message integrity check to verify that the request body was not corrupted in transit. For more
 information, go to [RFC 1864.](http://www.ietf.org/rfc/rfc1864.txt "http://www.ietf.org/rfc/rfc1864.txt")



For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-acl](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


The canned ACL to apply to the bucket.


Valid Values: `private | public-read | public-read-write | authenticated-read`





**[x-amz-expected-bucket-owner](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-grant-full-control](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.




**[x-amz-grant-read](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


Allows grantee to list the objects in the bucket.




**[x-amz-grant-read-acp](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


Allows grantee to read the bucket ACL.




**[x-amz-grant-write](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


Allows grantee to create new objects in the bucket.


For the bucket and object owners of existing objects, also allows deletions and overwrites of those
 objects.




**[x-amz-grant-write-acp](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


Allows grantee to write the ACL for the applicable bucket.




**[x-amz-sdk-checksum-algorithm](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[AccessControlPolicy](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


Root level tag for the AccessControlPolicy parameters.


Required: Yes




**[Grants](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


A list of grants.


Type: Array of [Grant](API_Grant.md "API_Grant.md") data types


Required: No




**[Owner](#API_PutBucketAcl_RequestSyntax "#API_PutBucketAcl_RequestSyntax")**


Container for the bucket owner's display name and ID.


Type: [Owner](API_Owner.md "API_Owner.md") data type


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample Request: Access permissions specified in the body


The following request grants access permission to the existing `examplebucket`
 bucket. The request specifies the ACL in the body. In addition to granting full control to the
 bucket owner, the XML specifies the following grants.



* Grant the `AllUsers` group READ permission on the bucket.
* Grant the `LogDelivery` group WRITE permission on the bucket.
* Grant an AWS account, identified by email address, WRITE\_ACP permission.
* Grant an AWS account, identified by canonical user ID, READ\_ACP permission.


```

PUT ?acl HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Content-Length: 1660
x-amz-date: Thu, 12 Apr 2012 20:04:21 GMT
Authorization: authorization string

<AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Owner>
    <ID>852b113e7a2f25102679df27bb0ae12b3f85be6BucketOwnerCanonicalUserID</ID>
    <DisplayName>OwnerDisplayName</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
        <ID>852b113e7a2f25102679df27bb0ae12b3f85be6BucketOwnerCanonicalUserID</ID>
        <DisplayName>OwnerDisplayName</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
        <URI xmlns="">http://acs.amazonaws.com/groups/global/AllUsers</URI>
      </Grantee>
      <Permission xmlns="">READ</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
        <URI xmlns="">http://acs.amazonaws.com/groups/s3/LogDelivery</URI>
      </Grantee>
      <Permission xmlns="">WRITE</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="AmazonCustomerByEmail">
        <EmailAddress xmlns="">xyz@amazon.com</EmailAddress>
      </Grantee>
      <Permission xmlns="">WRITE_ACP</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
        <ID xmlns="">f30716ab7115dcb44a5ef76e9d74b8e20567f63TestAccountCanonicalUserID</ID>
      </Grantee>
      <Permission xmlns="">READ_ACP</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
         
```

### Sample Response


This example illustrates one usage of PutBucketAcl.



```

HTTP/1.1 200 OK
x-amz-id-2: NxqO3PNiMHXXGwjgv15LLgUoAmPVmG0xtZw2sxePXLhpIvcyouXDrcQUaWWXcOK0
x-amz-request-id: C651BC9B4E1BD401
Date: Thu, 12 Apr 2012 20:04:28 GMT
Content-Length: 0
Server: AmazonS3
         
```

### Sample Request: Access permissions specified using headers


The following request uses ACL-specific request headers to grant the following
 permissions:



* Write permission to the Amazon S3 `LogDelivery` group and an AWS account identified
 by the email `xyz@amazon.com`.
* Read permission to the Amazon S3 `AllUsers` group


```

PUT ?acl HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
x-amz-date: Sun, 29 Apr 2012 22:00:57 GMT
x-amz-grant-write: uri="http://acs.amazonaws.com/groups/s3/LogDelivery", emailAddress="xyz@amazon.com"
x-amz-grant-read: uri="http://acs.amazonaws.com/groups/global/AllUsers"
Accept: */*
Authorization: authorization string
         
```

### Sample Response


This example illustrates one usage of PutBucketAcl.



```

HTTP/1.1 200 OK
x-amz-id-2: 0w9iImt23VF9s6QofOTDzelF7mrryz7d04Mw23FQCi4O205Zw28Zn+d340/RytoQ
x-amz-request-id: A6A8F01A38EC7138
Date: Sun, 29 Apr 2012 22:01:10 GMT
Content-Length: 0
Server: AmazonS3
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketAcl "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketAcl")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketAcl "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketAcl")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketAcl "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketAcl")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketAcl "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketAcl")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketAcl "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketAcl")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketAcl "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketAcl")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketAcl "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketAcl")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketAcl "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketAcl")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketAcl "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketAcl")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketAcl "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketAcl")
