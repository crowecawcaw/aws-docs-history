# PlacementStrategy

The task placement strategy for a task or service. To learn more, see [Task Placement
Strategies](../../../AmazonECS/latest/developerguide/task-placement-strategies.md "../../../AmazonECS/latest/developerguide/task-placement-strategies.md") in the Amazon Elastic Container Service Service Developer Guide.

## Contents

**field**

The field to apply the placement strategy against. For the spread placement strategy,
valid values are instanceId (or host, which has the same effect), or any platform or custom
attribute that is applied to a container instance, such as attribute:ecs.availability-zone.
For the binpack placement strategy, valid values are cpu and memory. For the random
placement strategy, this field is not used.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 255.

Required: No

**type**

The type of placement strategy. The random placement strategy randomly places tasks on
available candidates. The spread placement strategy spreads placement across available
candidates evenly based on the field parameter. The binpack strategy places tasks on
available candidates that have the least available amount of the resource that is specified
with the field parameter. For example, if you binpack on memory, a task is placed on the
instance with the least amount of remaining memory (but still enough to run the task).

Type: String

Valid Values: `random | spread | binpack`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PlacementStrategy.md "../../../goto/SdkForCpp/pipes-2015-10-07/PlacementStrategy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PlacementStrategy.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PlacementStrategy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PlacementStrategy.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PlacementStrategy.md")
