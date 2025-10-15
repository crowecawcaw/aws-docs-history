# ResourceDetail

Details about a resource in a generated template


## Contents





**LogicalResourceId** 


The logical id for this resource in the final generated template.


Type: String


Required: No




**ResourceIdentifier** 


 ResourceIdentifier.entry.N.key (key)
 

 ResourceIdentifier.entry.N.value (value)
 

A list of up to 256 key-value pairs that identifies the resource in the generated template.
 The key is the name of one of the primary identifiers for the resource. (Primary identifiers are
 specified in the `primaryIdentifier` list in the resource schema.) The value is the
 value of that primary identifier. For example, for a `AWS::DynamoDB::Table` resource,
 the primary identifiers is `TableName` so the key-value pair could be
 `"TableName": "MyDDBTable"`. For more information, see [primaryIdentifier](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-primaryidentifier "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-primaryidentifier") in the *AWS CloudFormation Command Line Interface (CLI) User Guide*.


Type: String to string map


Map Entries: Maximum number of 256 items.


Key Length Constraints: Minimum length of 1. Maximum length of 2048.


Value Length Constraints: Minimum length of 1. Maximum length of 2048.


Required: No




**ResourceStatus** 


Status of the processing of a resource in a generated template.





`InProgress`


The resource processing is still in progress.




`Complete`


The resource processing is complete.




`Pending`


The resource processing is pending.




`Failed`


The resource processing has failed.




Type: String


Valid Values: `PENDING | IN_PROGRESS | FAILED | COMPLETE`



Required: No




**ResourceStatusReason** 


The reason for the resource detail, providing more information if a failure happened.


Type: String


Required: No




**ResourceType** 


The type of the resource, such as `AWS::DynamoDB::Table`. For the list of
 supported resources, see [Resource type
 support for imports and drift detection](../UserGuide/resource-import-supported-resources.md "../UserGuide/resource-import-supported-resources.md") In the
 *AWS CloudFormation User Guide*



Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: No




**Warnings.member.N** 


The warnings generated for this resource.


Type: Array of [WarningDetail](API_WarningDetail.md "API_WarningDetail.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceDetail "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceDetail")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceDetail "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceDetail")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceDetail "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceDetail")
