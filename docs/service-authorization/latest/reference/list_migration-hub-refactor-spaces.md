

# Actions, resources, and condition keys for AWS Migration Hub Refactor Spaces
<a name="list_migration-hub-refactor-spaces"></a>

AWS Migration Hub Refactor Spaces (service prefix: `refactor-spaces`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/refactor-spaces/refactor-spaces.json) for this service.

**Topics**
+ [API operations defined by AWS Migration Hub Refactor Spaces](#list_migration-hub-refactor-spaces-operations)
+ [Actions defined by AWS Migration Hub Refactor Spaces](#list_migration-hub-refactor-spaces-actions-as-permissions)
+ [Resource types defined by AWS Migration Hub Refactor Spaces](#list_migration-hub-refactor-spaces-resources-for-iam-policies)
+ [Condition keys for AWS Migration Hub Refactor Spaces](#list_migration-hub-refactor-spaces-policy-keys)

## API operations defined by AWS Migration Hub Refactor Spaces
<a name="list_migration-hub-refactor-spaces-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_migration-hub-refactor-spaces-actions-as-permissions).




- **   CreateApplication  **
  - **IAM action:**  [refactor-spaces:CreateApplication](#list_migration-hub-refactor-spaces-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [refactor-spaces:TagResource](#list_migration-hub-refactor-spaces-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEnvironment  **
  - **IAM action:**  [refactor-spaces:CreateEnvironment](#list_migration-hub-refactor-spaces-action-CreateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [refactor-spaces:TagResource](#list_migration-hub-refactor-spaces-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRoute  **
  - **IAM action:**  [refactor-spaces:CreateRoute](#list_migration-hub-refactor-spaces-action-CreateRoute)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [refactor-spaces:TagResource](#list_migration-hub-refactor-spaces-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateService  **
  - **IAM action:**  [refactor-spaces:CreateService](#list_migration-hub-refactor-spaces-action-CreateService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [refactor-spaces:TagResource](#list_migration-hub-refactor-spaces-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteApplication  **
  - **IAM action:**  [refactor-spaces:DeleteApplication](#list_migration-hub-refactor-spaces-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironment  **
  - **IAM action:**  [refactor-spaces:DeleteEnvironment](#list_migration-hub-refactor-spaces-action-DeleteEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [refactor-spaces:DeleteResourcePolicy](#list_migration-hub-refactor-spaces-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRoute  **
  - **IAM action:**  [refactor-spaces:DeleteRoute](#list_migration-hub-refactor-spaces-action-DeleteRoute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteService  **
  - **IAM action:**  [refactor-spaces:DeleteService](#list_migration-hub-refactor-spaces-action-DeleteService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [refactor-spaces:GetApplication](#list_migration-hub-refactor-spaces-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironment  **
  - **IAM action:**  [refactor-spaces:GetEnvironment](#list_migration-hub-refactor-spaces-action-GetEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [refactor-spaces:GetResourcePolicy](#list_migration-hub-refactor-spaces-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRoute  **
  - **IAM action:**  [refactor-spaces:GetRoute](#list_migration-hub-refactor-spaces-action-GetRoute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetService  **
  - **IAM action:**  [refactor-spaces:GetService](#list_migration-hub-refactor-spaces-action-GetService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplications  **
  - **IAM action:**  [refactor-spaces:ListApplications](#list_migration-hub-refactor-spaces-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEnvironmentVpcs  **
  - **IAM action:**  [refactor-spaces:ListEnvironmentVpcs](#list_migration-hub-refactor-spaces-action-ListEnvironmentVpcs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEnvironments  **
  - **IAM action:**  [refactor-spaces:ListEnvironments](#list_migration-hub-refactor-spaces-action-ListEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRoutes  **
  - **IAM action:**  [refactor-spaces:ListRoutes](#list_migration-hub-refactor-spaces-action-ListRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServices  **
  - **IAM action:**  [refactor-spaces:ListServices](#list_migration-hub-refactor-spaces-action-ListServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [refactor-spaces:ListTagsForResource](#list_migration-hub-refactor-spaces-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutResourcePolicy  **
  - **IAM action:**  [refactor-spaces:PutResourcePolicy](#list_migration-hub-refactor-spaces-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [refactor-spaces:TagResource](#list_migration-hub-refactor-spaces-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [refactor-spaces:UntagResource](#list_migration-hub-refactor-spaces-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateRoute  **
  - **IAM action:**  [refactor-spaces:UpdateRoute](#list_migration-hub-refactor-spaces-action-UpdateRoute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Migration Hub Refactor Spaces
<a name="list_migration-hub-refactor-spaces-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateApplication](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application within an environment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create an environment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRoute](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateRoute.html)  **
  - **Description:** Grants permission to create a route within an application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Access level:** Write

- **   [CreateService](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateService.html)  **
  - **Description:** Grants permission to create a service within an application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application from an environment
  - **Resource types (\*required):** [application\*](#list_migration-hub-refactor-spaces-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete an environment
  - **Resource types (\*required):** [environment\*](#list_migration-hub-refactor-spaces-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRoute](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteRoute.html)  **
  - **Description:** Grants permission to delete a route from an application
  - **Resource types (\*required):** [route\*](#list_migration-hub-refactor-spaces-resource-route)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Access level:** Write

- **   [DeleteService](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteService.html)  **
  - **Description:** Grants permission to delete a service from an application
  - **Resource types (\*required):** [service\*](#list_migration-hub-refactor-spaces-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetApplication.html)  **
  - **Description:** Grants permission to get more information about an application
  - **Resource types (\*required):** [application\*](#list_migration-hub-refactor-spaces-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetEnvironment.html)  **
  - **Description:** Grants permission to get more information for an environment
  - **Resource types (\*required):** [environment\*](#list_migration-hub-refactor-spaces-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get the details about a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRoute](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetRoute.html)  **
  - **Description:** Grants permission to get more information about a route
  - **Resource types (\*required):** [route\*](#list_migration-hub-refactor-spaces-resource-route)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Access level:** Read

- **   [GetService](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetService.html)  **
  - **Description:** Grants permission to get more information about a service
  - **Resource types (\*required):** [service\*](#list_migration-hub-refactor-spaces-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)
  - **Access level:** Read

- **   [ListApplications](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListApplications.html)  **
  - **Description:** Grants permission to list all the applications in an environment
  - **Resource types (\*required):** [application\*](#list_migration-hub-refactor-spaces-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)
  - **Access level:** Read

- **   [ListEnvironmentVpcs](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListEnvironmentVpcs.html)  **
  - **Description:** Grants permission to list all the VPCs for the environment
  - **Resource types (\*required):** [environment\*](#list_migration-hub-refactor-spaces-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEnvironments](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list all environments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRoutes](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListRoutes.html)  **
  - **Description:** Grants permission to list all the routes in an application
  - **Resource types (\*required):** [route\*](#list_migration-hub-refactor-spaces-resource-route)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Access level:** Read

- **   [ListServices](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListServices.html)  **
  - **Description:** Grants permission to list all the services in an environment
  - **Resource types (\*required):** [environment\*](#list_migration-hub-refactor-spaces-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all the tags for a given resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutResourcePolicy](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to add a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [application](#list_migration-hub-refactor-spaces-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Resource types (\*required):** [environment](#list_migration-hub-refactor-spaces-resource-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Resource types (\*required):** [route](#list_migration-hub-refactor-spaces-resource-route) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Resource types (\*required):** [service](#list_migration-hub-refactor-spaces-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from a resource
  - **Resource types (\*required):** [application](#list_migration-hub-refactor-spaces-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Resource types (\*required):** [environment](#list_migration-hub-refactor-spaces-resource-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Resource types (\*required):** [route](#list_migration-hub-refactor-spaces-resource-route) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Resource types (\*required):** [service](#list_migration-hub-refactor-spaces-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-refactor-spaces-aws_TagKeys)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Access level:** Tagging, Write

- **   [UpdateRoute](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UpdateRoute.html)  **
  - **Description:** Grants permission to update a route from an application
  - **Resource types (\*required):** [route\*](#list_migration-hub-refactor-spaces-resource-route)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath)
  - **Access level:** Write



## Resource types defined by AWS Migration Hub Refactor Spaces
<a name="list_migration-hub-refactor-spaces-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources)  | arn:${Partition}:refactor-spaces:${Region}:${Account}:environment/${EnvironmentId}/application/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds) | 
|  [environment](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources)  | arn:${Partition}:refactor-spaces:${Region}:${Account}:environment/${EnvironmentId} | [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_) | 
|  [route](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources)  | arn:${Partition}:refactor-spaces:${Region}:${Account}:environment/${EnvironmentId}/application/${ApplicationId}/route/${RouteId} | [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:RouteCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_RouteCreatedByAccount)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount)<br />[refactor-spaces:SourcePath](#list_migration-hub-refactor-spaces-refactor-spaces_SourcePath) | 
|  [service](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources)  | arn:${Partition}:refactor-spaces:${Region}:${Account}:environment/${EnvironmentId}/application/${ApplicationId}/service/${ServiceId} | [aws:ResourceTag/${TagKey}](#list_migration-hub-refactor-spaces-aws_ResourceTag___TagKey_)<br />[refactor-spaces:ApplicationCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ApplicationCreatedByAccount)<br />[refactor-spaces:CreatedByAccountIds](#list_migration-hub-refactor-spaces-refactor-spaces_CreatedByAccountIds)<br />[refactor-spaces:ServiceCreatedByAccount](#list_migration-hub-refactor-spaces-refactor-spaces_ServiceCreatedByAccount) | 

## Condition keys for AWS Migration Hub Refactor Spaces
<a name="list_migration-hub-refactor-spaces-policy-keys"></a>

AWS Migration Hub Refactor Spaces defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [refactor-spaces:ApplicationCreatedByAccount](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by restricting the action to only those accounts that created the application within an environment | String | 
|   [refactor-spaces:CreatedByAccountIds](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the accounts that created the resource | ArrayOfString | 
|   [refactor-spaces:RouteCreatedByAccount](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by restricting the action to only those accounts that created the route within an application | String | 
|   [refactor-spaces:ServiceCreatedByAccount](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by restricting the action to only those accounts that created the service within an application | String | 
|   [refactor-spaces:SourcePath](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the path of the route | String | 