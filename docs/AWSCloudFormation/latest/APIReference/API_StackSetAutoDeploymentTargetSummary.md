# StackSetAutoDeploymentTargetSummary

One of the targets for the StackSet. Returned by the [ListStackSetAutoDeploymentTargets](API_ListStackSetAutoDeploymentTargets.md "API_ListStackSetAutoDeploymentTargets.md") API operation.


## Contents





**OrganizationalUnitId** 


The organization root ID or organizational unit (OU) IDs where the StackSet is
 targeted.


Type: String


Pattern: `^(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}|r-[a-z0-9]{4,32})$`



Required: No




**Regions.member.N** 


The list of Regions targeted for this organization or OU.


Type: Array of strings


Pattern: `^[a-zA-Z0-9-]{1,128}$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetAutoDeploymentTargetSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetAutoDeploymentTargetSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetAutoDeploymentTargetSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetAutoDeploymentTargetSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetAutoDeploymentTargetSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetAutoDeploymentTargetSummary")
