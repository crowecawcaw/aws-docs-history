# Actions, resources, and condition keys for AWS Application Transformation Service

AWS Application Transformation Service (service prefix: `application-transformation`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md").
- View a list of the [API operations available for
  this service](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/application-transformation/application-transformation.json "https://servicereference.us-east-1.amazonaws.com/v1/application-transformation/application-transformation.json") for this service.

###### Topics

- [Actions defined by AWS Application Transformation Service](#list_application-transformation-actions-as-permissions "#list_application-transformation-actions-as-permissions")
- [Resource types defined by AWS Application Transformation Service](#list_application-transformation-resources-for-iam-policies "#list_application-transformation-resources-for-iam-policies")
- [Condition keys for AWS Application Transformation Service](#list_application-transformation-policy-keys "#list_application-transformation-policy-keys")

## Actions defined by AWS Application Transformation Service

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                         | Description                                                                           | Resource types (\*required) | Condition keys | Access level |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetContainerization](../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md "../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md")                      | Grants permission to get the details of all Containerization jobs                     |                             |                | Read         |
| [GetDeployment](../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md "../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md")                            | Grants permission to get the details of all Deployment jobs                           |                             |                | Read         |
| [GetGroupingAssessment](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md")                | Grants permission to Get the details of a Grouping Assessment Operation               |                             |                | Read         |
| [GetPortingCompatibilityAssessment](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md")    | Grants permission to Get Porting Compatibility Operation                              |                             |                | Read         |
| [GetPortingRecommendationAssessment](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md")   | Grants permission to Get the details of a Porting Recommendation Assessment Operation |                             |                | Read         |
| [GetRuntimeAssessment](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md")                 | Grants permission to Get the details of a Runtime Assessment Operation                |                             |                | Read         |
| [PutLogData](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md")                           | Grants permission to Push Logs (Intended for Clients Only)                            |                             |                | Write        |
| [PutMetricData](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md")                        | Grants permission to Push Metrics Data (Intended for Clients Only)                    |                             |                | Write        |
| [StartContainerization](../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md "../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md")                    | Grants permission to start a Containerization job                                     |                             |                | Write        |
| [StartDeployment](../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md "../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md")                          | Grants permission to start a Deployment job                                           |                             |                | Write        |
| [StartGroupingAssessment](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md")              | Grants permission to Start a Grouping Assessment Operation                            |                             |                | Write        |
| [StartPortingCompatibilityAssessment](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md")  | Grants permission to Start Porting Compatibility Operation                            |                             |                | Write        |
| [StartPortingRecommendationAssessment](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md") | Grants permission to Start the Porting Recommendation Assessment Operation            |                             |                | Write        |
| [StartRuntimeAssessment](../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md "../../../microservice-extractor/latest/userguide/what-is-microservice-extractor.md")               | Grants permission to Start a Runtime Assessment Operation                             |                             |                | Write        |

## Resource types defined by AWS Application Transformation Service

AWS Application Transformation Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Application Transformation Service

AWS Application Transformation Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
