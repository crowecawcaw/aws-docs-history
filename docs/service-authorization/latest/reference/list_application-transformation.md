

# Actions, resources, and condition keys for AWS Application Transformation Service
<a name="list_application-transformation"></a>

AWS Application Transformation Service (service prefix: `application-transformation`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/application-transformation/application-transformation.json) for this service.

**Topics**
+ [Actions defined by AWS Application Transformation Service](#list_application-transformation-actions-as-permissions)
+ [Resource types defined by AWS Application Transformation Service](#list_application-transformation-resources-for-iam-policies)
+ [Condition keys for AWS Application Transformation Service](#list_application-transformation-policy-keys)

## Actions defined by AWS Application Transformation Service
<a name="list_application-transformation-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetContainerization](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.html)  | Grants permission to get the details of all Containerization jobs |  |   | Read | 
|   [GetDeployment](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.html)  | Grants permission to get the details of all Deployment jobs |  |   | Read | 
|   [GetGroupingAssessment](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)  | Grants permission to Get the details of a Grouping Assessment Operation |  |   | Read | 
|   [GetPortingCompatibilityAssessment](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)  | Grants permission to Get Porting Compatibility Operation |  |   | Read | 
|   [GetPortingRecommendationAssessment](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)  | Grants permission to Get the details of a Porting Recommendation Assessment Operation |  |   | Read | 
|   [GetRuntimeAssessment](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)  | Grants permission to Get the details of a Runtime Assessment Operation |  |   | Read | 
|   [PutLogData](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)  | Grants permission to Push Logs (Intended for Clients Only) |  |   | Write | 
|   [PutMetricData](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)  | Grants permission to Push Metrics Data (Intended for Clients Only) |  |   | Write | 
|   [StartContainerization](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.html)  | Grants permission to start a Containerization job |  |   | Write | 
|   [StartDeployment](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.html)  | Grants permission to start a Deployment job |  |   | Write | 
|   [StartGroupingAssessment](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)  | Grants permission to Start a Grouping Assessment Operation |  |   | Write | 
|   [StartPortingCompatibilityAssessment](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)  | Grants permission to Start Porting Compatibility Operation |  |   | Write | 
|   [StartPortingRecommendationAssessment](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)  | Grants permission to Start the Porting Recommendation Assessment Operation |  |   | Write | 
|   [StartRuntimeAssessment](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)  | Grants permission to Start a Runtime Assessment Operation |  |   | Write | 

## Resource types defined by AWS Application Transformation Service
<a name="list_application-transformation-resources-for-iam-policies"></a>

AWS Application Transformation Service does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Application Transformation Service
<a name="list_application-transformation-policy-keys"></a>

AWS Application Transformation Service has no service-specific condition keys that can be used in the `Condition` element of policy statements.