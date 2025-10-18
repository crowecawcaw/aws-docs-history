# Entity

An entity associated with metrics, to allow for finding related telemetry. An entity
 is typically a resource or service within your system. For example, metrics from an
 Amazon EC2 instance could be associated with that instance as the entity. 
 Similarly, metrics from a service that you own could be associated with that service as 
 the entity.


## Contents





**Attributes** 


Additional attributes of the entity that are not used to specify the identity of the
 entity. A list of key-value pairs.


For details about how to use the attributes, see [How 
 to add related information to 
 telemetry](../monitoring/adding-your-own-related-telemetry.md "../monitoring/adding-your-own-related-telemetry.md") in the *CloudWatch User Guide*.


Type: String to string map


Map Entries: Minimum number of 0 items. Maximum number of 10 items.


Key Length Constraints: Minimum length of 1. Maximum length of 256.


Value Length Constraints: Minimum length of 1. Maximum length of 2048.


Required: No




**KeyAttributes** 


The attributes of the entity which identify the specific entity, as a list of 
 key-value pairs. Entities with the same `KeyAttributes` are considered to be
 the same entity. For an entity to be valid, the `KeyAttributes` must exist
 and be formatted correctly.


There are five allowed attributes (key names): `Type`,
 `ResourceType`, `Identifier`, `Name`, and
 `Environment`.


For details about how to use the key attributes to specify an entity, see [How 
 to add related 
 information to telemetry](../monitoring/adding-your-own-related-telemetry.md "../monitoring/adding-your-own-related-telemetry.md") in the *CloudWatch User 
 Guide*.


Type: String to string map


Map Entries: Minimum number of 2 items. Maximum number of 4 items.


Key Length Constraints: Minimum length of 1. Maximum length of 32.


Value Length Constraints: Minimum length of 1. Maximum length of 2048.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/Entity "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/Entity")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/Entity "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/Entity")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/Entity "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/Entity")
