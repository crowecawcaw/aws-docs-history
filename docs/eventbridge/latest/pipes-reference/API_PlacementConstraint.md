# PlacementConstraint

An object representing a constraint on task placement. To learn more, see [Task Placement
Constraints](../../../AmazonECS/latest/developerguide/task-placement-constraints.md "../../../AmazonECS/latest/developerguide/task-placement-constraints.md") in the Amazon Elastic Container Service Developer Guide.

## Contents

**expression**

A cluster query language expression to apply to the constraint. You cannot specify an
expression if the constraint type is `distinctInstance`. To learn more, see
[Cluster Query
Language](../../../AmazonECS/latest/developerguide/cluster-query-language.md "../../../AmazonECS/latest/developerguide/cluster-query-language.md") in the Amazon Elastic Container Service Developer Guide.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2000.

Required: No

**type**

The type of constraint. Use distinctInstance to ensure that each task in a particular
group is running on a different container instance. Use memberOf to restrict the selection
to a group of valid candidates.

Type: String

Valid Values: `distinctInstance | memberOf`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PlacementConstraint.md "../../../goto/SdkForCpp/pipes-2015-10-07/PlacementConstraint.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PlacementConstraint.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PlacementConstraint.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PlacementConstraint.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PlacementConstraint.md")
