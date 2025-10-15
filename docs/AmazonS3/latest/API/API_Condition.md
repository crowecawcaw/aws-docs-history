# Condition

A container for describing a condition that must be met for the specified redirect to apply. For
 example, 1. If request is for pages in the `/docs` folder, redirect to the
 `/documents` folder. 2. If request results in HTTP error 4xx, redirect request to another
 host where you might process the error.


## Contents





**HttpErrorCodeReturnedEquals** 


The HTTP error code when the redirect is applied. In the event of an error, if the error code equals
 this value, then the specified redirect is applied. Required when parent element `Condition`
 is specified and sibling `KeyPrefixEquals` is not specified. If both are specified, then both
 must be true for the redirect to be applied.


Type: String


Required: No




**KeyPrefixEquals** 


The object key name prefix when the redirect is applied. For example, to redirect requests for
 `ExamplePage.html`, the key prefix will be `ExamplePage.html`. To redirect
 request for all pages with the prefix `docs/`, the key prefix will be `/docs`,
 which identifies all objects in the `docs/` folder. Required when the parent element
 `Condition` is specified and sibling `HttpErrorCodeReturnedEquals` is not
 specified. If both conditions are specified, both must be true for the redirect to be applied.


###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Condition "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Condition")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Condition "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Condition")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Condition "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Condition")
