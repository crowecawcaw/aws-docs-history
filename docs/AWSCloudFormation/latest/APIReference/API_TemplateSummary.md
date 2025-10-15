# TemplateSummary

The summary of a generated template.


## Contents





**CreationTime** 


The time the generated template was created.


Type: Timestamp


Required: No




**GeneratedTemplateId** 


The Amazon Resource Name (ARN) of the generated template. The format is
 `arn:${Partition}:cloudformation:${Region}:${Account}:generatedtemplate/${Id}`. For
 example,
 `arn:aws:cloudformation:*us-east-1*:*123456789012*:generatedtemplate/*2e8465c1-9a80-43ea-a3a3-4f2d692fe6dc*`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: No




**GeneratedTemplateName** 


The name of the generated template.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Required: No




**LastUpdatedTime** 


The time the generated template was last updated.


Type: Timestamp


Required: No




**NumberOfResources** 


The number of resources in the generated template. This is a total of resources in pending,
 in-progress, completed, and failed states.


Type: Integer


Valid Range: Minimum value of 0.


Required: No




**Status** 


The status of the template generation. Supported values are:



* `CreatePending` - the creation of the template is pending.
* `CreateInProgress` - the creation of the template is in progress.
* `DeletePending` - the deletion of the template is pending.
* `DeleteInProgress` - the deletion of the template is in progress.
* `UpdatePending` - the update of the template is pending.
* `UpdateInProgress` - the update of the template is in progress.
* `Failed` - the template operation failed.
* `Complete` - the template operation is complete.

Type: String


Valid Values: `CREATE_PENDING | UPDATE_PENDING | DELETE_PENDING | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | FAILED | COMPLETE`



Required: No




**StatusReason** 


The reason for the current template generation status. This will provide more details if a
 failure happened.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TemplateSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TemplateSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TemplateSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TemplateSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TemplateSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TemplateSummary")
