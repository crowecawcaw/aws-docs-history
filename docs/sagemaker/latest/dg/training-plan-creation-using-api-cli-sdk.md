

# SageMaker training plans creation using the SageMaker API, or AWS CLI
<a name="training-plan-creation-using-api-cli-sdk"></a>

SageMaker training plans support the programmatic creation of training plans through its API. You can interact with the training plans API using the AWS CLI or SageMaker SDKs.

SageMaker training plans's API actions provide a comprehensive workflow for managing training plans programmatically:
+ **`SearchTrainingPlanOfferings`:** Enables users to query and discover available compute resources by specifying parameters like instance type, count, and desired time window. The API returns a ranked list of training plan offerings that best match the user's requirements.
+ **`CreateTrainingPlan`:** Allows reservation of a specific training plan offering, transforming a potential compute capacity into scheduled reserved capacities with a unique training plan ARN.
+ **`ListTrainingPlans`:** Provides a method to retrieve and review all existing training plans in a user's AWS account, with optional filtering and sorting capabilities.
+ **`DescribeTrainingPlan`:** Offers detailed insights into a specific training plan, including its lifecycle stages from `Pending` to `Active` to `Expired`.
+ **`ExtendTrainingPlan`:** Extends an existing training plan by purchasing an extension offering. For more information, see [Training plans extension](training-plan-extension.md).
+ **`DescribeTrainingPlanExtensionHistory`:** Retrieves the extension history for a training plan. For more information, see [Training plans extension](training-plan-extension.md).

**Topics**
+ [Search training plan offerings](search-training-plan-offerings-api-cli-sdk.md)
+ [Reserve the best training plan](choose-best-training-plan-using-api-cli-sdk.md)
+ [List training plans](list-training-plans-using-api-cli-sdk.md)
+ [View training plan details](training-plan-details-using-api-cli-sdk.md)