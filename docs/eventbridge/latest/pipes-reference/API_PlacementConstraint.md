

# PlacementConstraint
<a name="API_PlacementConstraint"></a>

An object representing a constraint on task placement. To learn more, see [Task Placement Constraints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html) in the Amazon Elastic Container Service Developer Guide.

## Contents
<a name="API_PlacementConstraint_Contents"></a>

 ** expression **   <a name="eventbridge-Type-PlacementConstraint-expression"></a>
A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is `distinctInstance`. To learn more, see [Cluster Query Language](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html) in the Amazon Elastic Container Service Developer Guide.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2000.  
Required: No

 ** type **   <a name="eventbridge-Type-PlacementConstraint-type"></a>
The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates.   
Type: String  
Valid Values: `distinctInstance | memberOf`   
Required: No

## See Also
<a name="API_PlacementConstraint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PlacementConstraint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PlacementConstraint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PlacementConstraint) 