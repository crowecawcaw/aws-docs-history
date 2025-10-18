# DescribeGeneratedTemplate

Describes a generated template. The output includes details about the progress of the
 creation of a generated template started by a `CreateGeneratedTemplate` API action
 or the update of a generated template started with an `UpdateGeneratedTemplate` API
 action.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**GeneratedTemplateName** 


The name or Amazon Resource Name (ARN) of a generated template.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Required: Yes




## Response Elements


The following elements are returned by the service.





**CreationTime** 


The time the generated template was created.


Type: Timestamp




**GeneratedTemplateId** 


The Amazon Resource Name (ARN) of the generated template. The format is
 `arn:${Partition}:cloudformation:${Region}:${Account}:generatedtemplate/${Id}`.
 For example,
 `arn:aws:cloudformation:*us-east-1*:*123456789012*:generatedtemplate/*2e8465c1-9a80-43ea-a3a3-4f2d692fe6dc*`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.




**GeneratedTemplateName** 


The name of the generated template.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.




**LastUpdatedTime** 


The time the generated template was last updated.


Type: Timestamp




**Progress** 


An object describing the progress of the template generation.


Type: [TemplateProgress](API_TemplateProgress.md "API_TemplateProgress.md") object




**Resources.member.N**


A list of objects describing the details of the resources in the template
 generation.


Type: Array of [ResourceDetail](API_ResourceDetail.md "API_ResourceDetail.md") objects


Array Members: Minimum number of 1 item. Maximum number of 500 items.




**StackId** 


The stack ARN of the base stack if a base stack was provided when generating the
 template.


Type: String




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





**StatusReason** 


The reason for the current template generation status. This will provide more details if a
 failure happened.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.




**TemplateConfiguration** 


The configuration details of the generated template, including the
 `DeletionPolicy` and `UpdateReplacePolicy`.


Type: [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") object




**TotalWarnings** 


The number of warnings generated for this template. The warnings are found in the details
 of each of the resources in the template.


Type: Integer


Valid Range: Minimum value of 0.




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**GeneratedTemplateNotFound** 


The generated template was not found.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeGeneratedTemplate "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeGeneratedTemplate")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeGeneratedTemplate "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeGeneratedTemplate")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeGeneratedTemplate")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeGeneratedTemplate")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeGeneratedTemplate")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeGeneratedTemplate")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeGeneratedTemplate")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeGeneratedTemplate")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeGeneratedTemplate "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeGeneratedTemplate")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeGeneratedTemplate")
