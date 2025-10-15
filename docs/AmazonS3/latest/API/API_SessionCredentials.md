# SessionCredentials

The established temporary security credentials of the session.

###### Note


**Directory buckets** - These session credentials are only
 supported for the authentication and authorization of Zonal endpoint API operations on directory buckets.


## Contents





**AccessKeyId** 


A unique identifier that's associated with a secret access key. The access key ID and the secret
 access key are used together to sign programmatic AWS requests cryptographically. 


Type: String


Required: Yes




**Expiration** 


Temporary security credentials expire after a specified interval. After temporary credentials
 expire, any calls that you make with those credentials will fail. So you must generate a new set of
 temporary credentials. Temporary credentials cannot be extended or refreshed beyond the original
 specified interval.


Type: Timestamp


Required: Yes




**SecretAccessKey** 


A key that's used with the access key ID to cryptographically sign programmatic AWS requests.
 Signing a request identifies the sender and prevents the request from being altered. 


Type: String


Required: Yes




**SessionToken** 


A part of the temporary security credentials. The session token is used to validate the temporary
 security credentials.
 
 


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/SessionCredentials "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/SessionCredentials")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/SessionCredentials "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/SessionCredentials")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/SessionCredentials "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/SessionCredentials")
