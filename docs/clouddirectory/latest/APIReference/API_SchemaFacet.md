Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# SchemaFacet

A facet.


## Contents





**FacetName** 


The name of the facet. If this value is set, SchemaArn must also be set.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `^[a-zA-Z0-9._-]*$`



Required: No




**SchemaArn** 


The ARN of the schema that contains the facet with no minor component. See [Arn Examples](arns.md "arns.md") and [In-Place Schema Upgrade](../developerguide/schemas_inplaceschemaupgrade.md "../developerguide/schemas_inplaceschemaupgrade.md") for a description of when to provide minor versions.
 If this value is set, FacetName must also be set.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/SchemaFacet "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/SchemaFacet")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/SchemaFacet "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/SchemaFacet")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/SchemaFacet "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/SchemaFacet")
