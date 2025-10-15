# AutoDeployment

Describes whether StackSets automatically deploys to AWS Organizations accounts that are
 added to a target organization or organizational unit (OU). For more information, see [Enable or
 disable automatic deployments for StackSets in AWS Organizations](../UserGuide/stacksets-orgs-manage-auto-deployment.md "../UserGuide/stacksets-orgs-manage-auto-deployment.md") in the
 *AWS CloudFormation User Guide*.


## Contents





**Enabled** 


If set to `true`, StackSets automatically deploys additional stack instances to
 AWS Organizations accounts that are added to a target organization or organizational unit
 (OU) in the specified Regions. If an account is removed from a target organization or OU,
 StackSets deletes stack instances from the account in the specified Regions.


Type: Boolean


Required: No




**RetainStacksOnAccountRemoval** 


If set to `true`, stack resources are retained when an account is removed from a
 target organization or OU. If set to `false`, stack resources are deleted. Specify
 only if `Enabled` is set to `True`.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/AutoDeployment "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/AutoDeployment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/AutoDeployment "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/AutoDeployment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/AutoDeployment "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/AutoDeployment")
