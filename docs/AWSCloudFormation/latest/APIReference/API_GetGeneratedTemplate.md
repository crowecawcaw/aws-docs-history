# GetGeneratedTemplate

Retrieves a generated template. If the template is in an `InProgress` or
 `Pending` status then the template returned will be the template when the
 template was last in a `Complete` status. If the template has not yet been in a
 `Complete` status then an empty template will be returned.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Format** 


The language to use to retrieve for the generated template. Supported values are:



* `JSON`
* `YAML`

Type: String


Valid Values: `JSON | YAML`



Required: No




**GeneratedTemplateName** 


The name or Amazon Resource Name (ARN) of the generated template. The format is
 `arn:${Partition}:cloudformation:${Region}:${Account}:generatedtemplate/${Id}`.
 For example,
 `arn:aws:cloudformation:*us-east-1*:*123456789012*:generatedtemplate/*2e8465c1-9a80-43ea-a3a3-4f2d692fe6dc*`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Required: Yes




## Response Elements


The following elements are returned by the service.





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





**TemplateBody** 


The template body of the generated template, in the language specified by the
 `Language` parameter.


Type: String


Length Constraints: Minimum length of 1.




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**GeneratedTemplateNotFound** 


The generated template was not found.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/GetGeneratedTemplate "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/GetGeneratedTemplate")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/GetGeneratedTemplate "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/GetGeneratedTemplate")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/GetGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/GetGeneratedTemplate")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/GetGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/GetGeneratedTemplate")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/GetGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/GetGeneratedTemplate")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/GetGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/GetGeneratedTemplate")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/GetGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/GetGeneratedTemplate")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/GetGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/GetGeneratedTemplate")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/GetGeneratedTemplate "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/GetGeneratedTemplate")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/GetGeneratedTemplate "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/GetGeneratedTemplate")
