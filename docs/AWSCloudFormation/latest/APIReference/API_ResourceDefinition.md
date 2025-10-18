# ResourceDefinition

A resource included in a generated template. This data type is used with the
 `CreateGeneratedTemplate` and `UpdateGeneratedTemplate` API
 actions.


## Contents





**ResourceIdentifier** 


 ResourceIdentifier.entry.N.key (key)
 

 ResourceIdentifier.entry.N.value (value)
 

A list of up to 256 key-value pairs that identifies the scanned resource. The key is the
 name of one of the primary identifiers for the resource. (Primary identifiers are specified in
 the `primaryIdentifier` list in the resource schema.) The value is the value of that
 primary identifier. For example, for a `AWS::DynamoDB::Table` resource, the primary
 identifiers is `TableName` so the key-value pair could be `"TableName":
 "MyDDBTable"`. For more information, see [primaryIdentifier](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-primaryidentifier "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-primaryidentifier") in the *AWS CloudFormation Command Line Interface (CLI) User Guide*.


Type: String to string map


Map Entries: Maximum number of 256 items.


Key Length Constraints: Minimum length of 1. Maximum length of 2048.


Value Length Constraints: Minimum length of 1. Maximum length of 2048.


Required: Yes




**ResourceType** 


The type of the resource, such as `AWS::DynamoDB::Table`. For the list of
 supported resources, see [Resource type
 support for imports and drift detection](../UserGuide/resource-import-supported-resources.md "../UserGuide/resource-import-supported-resources.md") in the
 *AWS CloudFormation User Guide*



Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: Yes




**LogicalResourceId** 


The logical resource id for this resource in the generated template.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceDefinition "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceDefinition")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceDefinition "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceDefinition")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceDefinition "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceDefinition")
