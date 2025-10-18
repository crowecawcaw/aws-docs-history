# EnvironmentLifecycle

Information about the current creation or deletion lifecycle state of an AWS Cloud9 development
 environment.


## Contents





**failureResource** 


If the environment failed to delete, the Amazon Resource Name (ARN) of the related AWS
 resource.


Type: String


Required: No




**reason** 


Any informational message about the lifecycle state of the environment.


Type: String


Required: No




**status** 


The current creation or deletion lifecycle state of the environment.



* `CREATING`: The environment is in the process of being created.
* `CREATED`: The environment was successfully created.
* `CREATE_FAILED`: The environment failed to be created.
* `DELETING`: The environment is in the process of being deleted.
* `DELETE_FAILED`: The environment failed to delete.

Type: String


Valid Values: `CREATING | CREATED | CREATE_FAILED | DELETING | DELETE_FAILED`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/EnvironmentLifecycle "https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/EnvironmentLifecycle")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/EnvironmentLifecycle "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/EnvironmentLifecycle")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/EnvironmentLifecycle "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/EnvironmentLifecycle")
