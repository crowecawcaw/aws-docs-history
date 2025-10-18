# TemplateConfiguration

The configuration details of a generated template.


## Contents





**DeletionPolicy** 


The `DeletionPolicy` assigned to resources in the generated template. Supported
 values are:



* `DELETE` - delete all resources when the stack is deleted.
* `RETAIN` - retain all resources when the stack is deleted.

For more information, see [DeletionPolicy
 attribute](../UserGuide/aws-attribute-deletionpolicy.md "../UserGuide/aws-attribute-deletionpolicy.md") in the *AWS CloudFormation User Guide*.


Type: String


Valid Values: `DELETE | RETAIN`



Required: No




**UpdateReplacePolicy** 


The `UpdateReplacePolicy` assigned to resources in the generated template.
 Supported values are:



* `DELETE` - delete all resources when the resource is replaced during an update
 operation.
* `RETAIN` - retain all resources when the resource is replaced during an update
 operation.

For more information, see [UpdateReplacePolicy attribute](../UserGuide/aws-attribute-updatereplacepolicy.md "../UserGuide/aws-attribute-updatereplacepolicy.md") in the *AWS CloudFormation User Guide*.


Type: String


Valid Values: `DELETE | RETAIN`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TemplateConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TemplateConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TemplateConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TemplateConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TemplateConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TemplateConfiguration")
