# ImportStacksToStackSet

Import existing stacks into a new StackSets. Use the stack import operation to import up
 to 10 stacks into a new StackSet in the same account as the source stack or in a different
 administrator account and Region, by specifying the stack ID of the stack you intend to
 import.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**CallAs** 


By default, `SELF` is specified. Use `SELF` for StackSets with
 self-managed permissions.



* If you are signed in to the management account, specify
 `SELF`.
* For service managed StackSets, specify `DELEGATED_ADMIN`.

Type: String


Valid Values: `SELF | DELEGATED_ADMIN`



Required: No




**OperationId** 


A unique, user defined, identifier for the StackSet operation.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**OperationPreferences** 


The user-specified preferences for how CloudFormation performs a StackSet operation.


For more information about maximum concurrent accounts and failure tolerance, see [StackSet operation options](../UserGuide/stacksets-concepts.md#stackset-ops-options "../UserGuide/stacksets-concepts.md#stackset-ops-options").


Type: [StackSetOperationPreferences](API_StackSetOperationPreferences.md "API_StackSetOperationPreferences.md") object


Required: No




**OrganizationalUnitIds.member.N**


The list of OU ID's to which the imported stacks must be mapped as deployment
 targets.


Type: Array of strings


Pattern: `^(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}|r-[a-z0-9]{4,32})$`



Required: No




**StackIds.member.N**


The IDs of the stacks you are importing into a StackSet. You import up to 10 stacks per
 StackSet at a time.


Specify either `StackIds` or `StackIdsUrl`.


Type: Array of strings


Required: No




**StackIdsUrl** 


The Amazon S3 URL which contains list of stack ids to be inputted.


Specify either `StackIds` or `StackIdsUrl`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 5120.


Pattern: `(s3://|http(s?)://).+`



Required: No




**StackSetName** 


The name of the StackSet. The name must be unique in the Region where you create your
 StackSet.


Type: String


Pattern: `[a-zA-Z][-a-zA-Z0-9]*(?::[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12})?`



Required: Yes




## Response Elements


The following element is returned by the service.





**OperationId** 


The unique identifier for the StackSet operation.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidOperation** 


The specified operation isn't valid.


HTTP Status Code: 400




**LimitExceeded** 


The quota for the resource has already been reached.


For information about resource and stack limitations, see [AWS CloudFormation quotas](../UserGuide/cloudformation-limits.md "../UserGuide/cloudformation-limits.md") in the
 *AWS CloudFormation User Guide*.


HTTP Status Code: 400




**OperationIdAlreadyExists** 


The specified operation ID already exists.


HTTP Status Code: 409




**OperationInProgress** 


Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack
 set at a given time.


HTTP Status Code: 409




**StackNotFound** 


The specified stack ARN doesn't exist or stack doesn't exist corresponding to the ARN in input.


HTTP Status Code: 404




**StackSetNotFound** 


The specified StackSet doesn't exist.


HTTP Status Code: 404




**StaleRequest** 


Another operation has been performed on this StackSet since the specified operation was performed.


HTTP Status Code: 409




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ImportStacksToStackSet "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ImportStacksToStackSet")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ImportStacksToStackSet "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ImportStacksToStackSet")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ImportStacksToStackSet "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ImportStacksToStackSet")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ImportStacksToStackSet "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ImportStacksToStackSet")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ImportStacksToStackSet "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ImportStacksToStackSet")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ImportStacksToStackSet "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ImportStacksToStackSet")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ImportStacksToStackSet "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ImportStacksToStackSet")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ImportStacksToStackSet "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ImportStacksToStackSet")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ImportStacksToStackSet "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ImportStacksToStackSet")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ImportStacksToStackSet "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ImportStacksToStackSet")
