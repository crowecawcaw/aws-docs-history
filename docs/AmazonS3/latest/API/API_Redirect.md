# Redirect

Specifies how requests are redirected. In the event of an error, you can specify a different error
 code to return.


## Contents





**HostName** 


The host name to use in the redirect request.


Type: String


Required: No




**HttpRedirectCode** 


The HTTP redirect code to use on the response. Not required if one of the siblings is
 present.


Type: String


Required: No




**Protocol** 


Protocol to use when redirecting requests. The default is the protocol that is used in the original
 request.


Type: String


Valid Values: `http | https`



Required: No




**ReplaceKeyPrefixWith** 


The object key prefix to use in the redirect request. For example, to redirect requests for all
 pages with prefix `docs/` (objects in the `docs/` folder) to
 `documents/`, you can set a condition block with `KeyPrefixEquals` set to
 `docs/` and in the Redirect set `ReplaceKeyPrefixWith` to
 `/documents`. Not required if one of the siblings is present. Can be present only if
 `ReplaceKeyWith` is not provided.


###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").


Type: String


Required: No




**ReplaceKeyWith** 


The specific object key to use in the redirect request. For example, redirect request to
 `error.html`. Not required if one of the siblings is present. Can be present only if
 `ReplaceKeyPrefixWith` is not provided.


###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Redirect "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Redirect")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Redirect "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Redirect")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Redirect "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Redirect")
