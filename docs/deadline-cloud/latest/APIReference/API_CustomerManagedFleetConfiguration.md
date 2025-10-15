# CustomerManagedFleetConfiguration

The details of a customer managed fleet configuration.


## Contents





**mode** 


The AWS Auto Scaling mode for the customer managed fleet configuration.


Type: String


Valid Values: `NO_SCALING | EVENT_BASED_AUTO_SCALING`



Required: Yes




**workerCapabilities** 


The worker capabilities for a customer managed fleet configuration.


Type: [CustomerManagedWorkerCapabilities](API_CustomerManagedWorkerCapabilities.md "API_CustomerManagedWorkerCapabilities.md") object


Required: Yes




**storageProfileId** 


The storage profile ID.


Type: String


Pattern: `sp-[0-9a-f]{32}`



Required: No




**tagPropagationMode** 


Specifies whether tags associated with a fleet are attached to workers when the worker
 is launched. 


When the `tagPropagationMode` is set to
 `PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH` any tag associated with a fleet is
 attached to workers when they launch. If the tags for a fleet change, the tags associated
 with running workers **do not** change.


If you don't specify `tagPropagationMode`, the default is
 `NO_PROPAGATION`.


Type: String


Valid Values: `NO_PROPAGATION | PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CustomerManagedFleetConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CustomerManagedFleetConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CustomerManagedFleetConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CustomerManagedFleetConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CustomerManagedFleetConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CustomerManagedFleetConfiguration")
