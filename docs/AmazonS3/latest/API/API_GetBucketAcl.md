# GetBucketAcl

###### Important

End of support notice: Beginning November 21, 2025, Amazon S3 will stop returning `DisplayName`. Update your applications to use canonical IDs (unique identifier for 
 AWS accounts), AWS account ID (12 digit identifier) or IAM ARNs (full resource naming) as a direct replacement of `DisplayName`.


Between July 15, 2025 and November 21, 2025, you will begin to see an increasing rate of missing `DisplayName` in the Owner object.

This change affects the following AWS Regions: US East (N. Virginia) Region, US West (N. California) Region, US West (Oregon) Region, Asia Pacific (Singapore) Region, Asia Pacific (Sydney) Region, 
 Asia Pacific (Tokyo) Region, Europe (Ireland) Region, and South America (São Paulo) Region.

###### Note

This operation is not supported for directory buckets.

This implementation of the `GET` action uses the `acl` subresource to return
 the access control list (ACL) of a bucket. To use `GET` to return the ACL of the bucket, you
 must have the `READ_ACP` access to the bucket. If `READ_ACP` permission is granted
 to the anonymous user, you can return the ACL of the bucket without using an authorization
 header.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").

###### Note

If your bucket uses the bucket owner enforced setting for S3 Object Ownership, requests to read
 ACLs are still supported and return the `bucket-owner-full-control` ACL with the owner
 being the account that created the bucket. For more information, see  [Controlling object ownership and
 disabling ACLs](../userguide/about-object-ownership.md "../userguide/about-object-ownership.md") in the *Amazon S3 User Guide*.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

The following operations are related to `GetBucketAcl`:


* [ListObjects](API_ListObjects.md "API_ListObjects.md")

## Request Syntax



```
GET /?acl HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketAcl_RequestSyntax "#API_GetBucketAcl_RequestSyntax")**


Specifies the S3 bucket whose ACL is being requested.


When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.


When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketAcl_RequestSyntax "#API_GetBucketAcl_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[AccessControlPolicy](#AmazonS3-GetBucketAcl-response-GetBucketAclOutput "#AmazonS3-GetBucketAcl-response-GetBucketAclOutput")>
   <[Owner](#AmazonS3-GetBucketAcl-response-Owner "#AmazonS3-GetBucketAcl-response-Owner")>
      <[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>***string***</[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>
      <[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>***string***</[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>
   </[Owner](#AmazonS3-GetBucketAcl-response-Owner "#AmazonS3-GetBucketAcl-response-Owner")>
   <[AccessControlList](#AmazonS3-GetBucketAcl-response-Grants "#AmazonS3-GetBucketAcl-response-Grants")>
      <Grant>
         <[Grantee](API_Grant.md#AmazonS3-Type-Grant-Grantee "API_Grant.md#AmazonS3-Type-Grant-Grantee")>
            <[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>***string***</[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>
            <[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>***string***</[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>
            <[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>***string***</[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>
            <[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>***string***</[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>
            <[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>***string***</[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>
         </[Grantee](API_Grant.md#AmazonS3-Type-Grant-Grantee "API_Grant.md#AmazonS3-Type-Grant-Grantee")>
         <[Permission](API_Grant.md#AmazonS3-Type-Grant-Permission "API_Grant.md#AmazonS3-Type-Grant-Permission")>***string***</[Permission](API_Grant.md#AmazonS3-Type-Grant-Permission "API_Grant.md#AmazonS3-Type-Grant-Permission")>
      </Grant>
   </[AccessControlList](#AmazonS3-GetBucketAcl-response-Grants "#AmazonS3-GetBucketAcl-response-Grants")>
</[AccessControlPolicy](#AmazonS3-GetBucketAcl-response-GetBucketAclOutput "#AmazonS3-GetBucketAcl-response-GetBucketAclOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[AccessControlPolicy](#API_GetBucketAcl_ResponseSyntax "#API_GetBucketAcl_ResponseSyntax")**


Root level tag for the AccessControlPolicy parameters.


Required: Yes




**[Grants](#API_GetBucketAcl_ResponseSyntax "#API_GetBucketAcl_ResponseSyntax")**


A list of grants.


Type: Array of [Grant](API_Grant.md "API_Grant.md") data types




**[Owner](#API_GetBucketAcl_ResponseSyntax "#API_GetBucketAcl_ResponseSyntax")**


Container for the bucket owner's display name and ID.


Type: [Owner](API_Owner.md "API_Owner.md") data type




## Examples


### Sample Request


The following request returns the ACL of the specified bucket.



```
GET ?acl HTTP/1.1
Host: bucket.s3.<Region>.amazonaws.com
Date: Wed, 28 Oct 2009 22:32:00 GMT
Authorization: authorization string
           
```

### Sample Response




```
HTTP/1.1 200 OK
x-amz-id-2: eftixk72aD6Ap51TnqcoF8eFidJG9Z/2mkiDFu8yU9AS1ed4OpIszj7UDNEHGran
x-amz-request-id: 318BC8BC148832E5
Date: Wed, 28 Oct 2009 22:32:00 GMT
Last-Modified: Sun, 1 Jan 2006 12:00:00 GMT
Content-Length: 124
Content-Type: text/plain
Connection: close
Server: AmazonS3
<AccessControlPolicy>
  <Owner>
    <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
    <DisplayName>CustomersName@amazon.com</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
			xsi:type="CanonicalUser">
        <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
        <DisplayName>CustomersName@amazon.com</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy> 
           
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketAcl "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketAcl")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketAcl "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketAcl")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketAcl "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketAcl")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketAcl "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketAcl")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketAcl "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketAcl")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketAcl "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketAcl")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketAcl "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketAcl")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketAcl "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketAcl")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketAcl "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketAcl")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketAcl "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketAcl")
