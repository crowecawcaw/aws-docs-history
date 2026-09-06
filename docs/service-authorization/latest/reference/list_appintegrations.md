

# Actions, resources, and condition keys for Amazon AppIntegrations
<a name="list_appintegrations"></a>

Amazon AppIntegrations (service prefix: `app-integrations`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/connect/latest/adminguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/appintegrations/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/connect/latest/adminguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/app-integrations/app-integrations.json) for this service.

**Topics**
+ [API operations defined by Amazon AppIntegrations](#list_appintegrations-operations)
+ [Actions defined by Amazon AppIntegrations](#list_appintegrations-actions-as-permissions)
+ [Permission-only actions for Amazon AppIntegrations](#list_appintegrations-permission-only-actions)
+ [Resource types defined by Amazon AppIntegrations](#list_appintegrations-resources-for-iam-policies)
+ [Condition keys for Amazon AppIntegrations](#list_appintegrations-policy-keys)

## API operations defined by Amazon AppIntegrations
<a name="list_appintegrations-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_appintegrations-actions-as-permissions).




- **   CreateApplication  **
  - **IAM action:**  [app-integrations:CreateApplication](#list_appintegrations-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [app-integrations:TagResource](#list_appintegrations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataIntegration  **
  - **IAM action:**  [app-integrations:CreateDataIntegration](#list_appintegrations-action-CreateDataIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [app-integrations:TagResource](#list_appintegrations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataIntegrationAssociation  **
  - **IAM action:**  [app-integrations:CreateDataIntegrationAssociation](#list_appintegrations-action-CreateDataIntegrationAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEventIntegration  **
  - **IAM action:**  [app-integrations:CreateEventIntegration](#list_appintegrations-action-CreateEventIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [app-integrations:TagResource](#list_appintegrations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteApplication  **
  - **IAM action:**  [app-integrations:DeleteApplication](#list_appintegrations-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataIntegration  **
  - **IAM action:**  [app-integrations:DeleteDataIntegration](#list_appintegrations-action-DeleteDataIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventIntegration  **
  - **IAM action:**  [app-integrations:DeleteEventIntegration](#list_appintegrations-action-DeleteEventIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [app-integrations:GetApplication](#list_appintegrations-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataIntegration  **
  - **IAM action:**  [app-integrations:GetDataIntegration](#list_appintegrations-action-GetDataIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventIntegration  **
  - **IAM action:**  [app-integrations:GetEventIntegration](#list_appintegrations-action-GetEventIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplicationAssociations  **
  - **IAM action:**  [app-integrations:ListApplicationAssociations](#list_appintegrations-action-ListApplicationAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplications  **
  - **IAM action:**  [app-integrations:ListApplications](#list_appintegrations-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataIntegrationAssociations  **
  - **IAM action:**  [app-integrations:ListDataIntegrationAssociations](#list_appintegrations-action-ListDataIntegrationAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataIntegrations  **
  - **IAM action:**  [app-integrations:ListDataIntegrations](#list_appintegrations-action-ListDataIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventIntegrationAssociations  **
  - **IAM action:**  [app-integrations:ListEventIntegrationAssociations](#list_appintegrations-action-ListEventIntegrationAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEventIntegrations  **
  - **IAM action:**  [app-integrations:ListEventIntegrations](#list_appintegrations-action-ListEventIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [app-integrations:ListTagsForResource](#list_appintegrations-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [app-integrations:TagResource](#list_appintegrations-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [app-integrations:UntagResource](#list_appintegrations-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **IAM action:**  [app-integrations:UpdateApplication](#list_appintegrations-action-UpdateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataIntegration  **
  - **IAM action:**  [app-integrations:UpdateDataIntegration](#list_appintegrations-action-UpdateDataIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataIntegrationAssociation  **
  - **IAM action:**  [app-integrations:UpdateDataIntegrationAssociation](#list_appintegrations-action-UpdateDataIntegrationAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEventIntegration  **
  - **IAM action:**  [app-integrations:UpdateEventIntegration](#list_appintegrations-action-UpdateEventIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon AppIntegrations
<a name="list_appintegrations-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateApplication](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create a new Application
  - **Resource types (\*required):** [application\*](#list_appintegrations-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html)  **
  - **Description:** Grants permission to create a new DataIntegration
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataIntegrationAssociation](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html)  **
  - **Description:** Grants permission to create a DataIntegrationAssociation
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataIntegrationSchedule](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegrationSchedule.html)  **
  - **Description:** Grants permission to create a data integration schedule
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEventIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateEventIntegration.html)  **
  - **Description:** Grants permission to create a new EventIntegration
  - **Resource types (\*required):** [event-integration\*](#list_appintegrations-resource-event-integration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an Application
  - **Resource types (\*required):** [application\*](#list_appintegrations-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html)  **
  - **Description:** Grants permission to delete a DataIntegration
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteEventIntegration.html)  **
  - **Description:** Grants permission to delete an EventIntegration
  - **Resource types (\*required):** [event-integration\*](#list_appintegrations-resource-event-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_GetApplication.html)  **
  - **Description:** Grants permission to view details about Application
  - **Resource types (\*required):** [application\*](#list_appintegrations-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_GetDataIntegration.html)  **
  - **Description:** Grants permission to view details about DataIntegrations
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataIntegrationExecution](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_GetDataIntegrationExecution.html)  **
  - **Description:** Grants permission to get details about a data integration execution
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataIntegrationSchedule](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_GetDataIntegrationSchedule.html)  **
  - **Description:** Grants permission to get details about a data integration schedule
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_GetEventIntegration.html)  **
  - **Description:** Grants permission to view details about EventIntegrations
  - **Resource types (\*required):** [event-integration\*](#list_appintegrations-resource-event-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplicationAssociations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListApplicationAssociations.html)  **
  - **Description:** Grants permission to list ApplicationAssociations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApplications](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListApplications.html)  **
  - **Description:** Grants permission to list Applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataIntegrationAssociations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListDataIntegrationAssociations.html)  **
  - **Description:** Grants permission to list DataIntegrationAssociations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataIntegrationExecutions](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListDataIntegrationExecutions.html)  **
  - **Description:** Grants permission to list data integration executions
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataIntegrationSchedules](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListDataIntegrationSchedules.html)  **
  - **Description:** Grants permission to list data integration schedules
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataIntegrations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListDataIntegrations.html)  **
  - **Description:** Grants permission to list DataIntegrations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEventIntegrationAssociations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListEventIntegrationAssociations.html)  **
  - **Description:** Grants permission to list EventIntegrationAssociations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEventIntegrations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListEventIntegrations.html)  **
  - **Description:** Grants permission to list EventIntegrations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to lists tag for an Amazon AppIntegration resource
  - **Resource types (\*required):** [application](#list_appintegrations-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-integration](#list_appintegrations-resource-data-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-integration-association](#list_appintegrations-resource-data-integration-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-integration](#list_appintegrations-resource-event-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-integration-association](#list_appintegrations-resource-event-integration-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartDataIntegrationExecution](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_StartDataIntegrationExecution.html)  **
  - **Description:** Grants permission to start a data integration execution
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an Amazon AppIntegration resource
  - **Resource types (\*required):** [application](#list_appintegrations-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Resource types (\*required):** [application-association](#list_appintegrations-resource-application-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Resource types (\*required):** [data-integration](#list_appintegrations-resource-data-integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Resource types (\*required):** [data-integration-association](#list_appintegrations-resource-data-integration-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Resource types (\*required):** [event-integration](#list_appintegrations-resource-event-integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Resource types (\*required):** [event-integration-association](#list_appintegrations-resource-event-integration-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an Amazon AppIntegration resource
  - **Resource types (\*required):** [application](#list_appintegrations-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Resource types (\*required):** [application-association](#list_appintegrations-resource-application-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Resource types (\*required):** [data-integration](#list_appintegrations-resource-data-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Resource types (\*required):** [data-integration-association](#list_appintegrations-resource-data-integration-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Resource types (\*required):** [event-integration](#list_appintegrations-resource-event-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Resource types (\*required):** [event-integration-association](#list_appintegrations-resource-event-integration-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to modify an Application
  - **Resource types (\*required):** [application\*](#list_appintegrations-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateDataIntegration.html)  **
  - **Description:** Grants permission to modify a DataIntegration
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataIntegrationAssociation](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateDataIntegrationAssociation.html)  **
  - **Description:** Grants permission to modify a DataIntegrationAssociation
  - **Resource types (\*required):** [data-integration-association\*](#list_appintegrations-resource-data-integration-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataIntegrationSchedule](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateDataIntegrationSchedule.html)  **
  - **Description:** Grants permission to update a data integration schedule
  - **Resource types (\*required):** [data-integration\*](#list_appintegrations-resource-data-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEventIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateEventIntegration.html)  **
  - **Description:** Grants permission to modify an EventIntegration
  - **Resource types (\*required):** [event-integration\*](#list_appintegrations-resource-event-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon AppIntegrations
<a name="list_appintegrations-permission-only-actions"></a>

The following actions are defined by Amazon AppIntegrations but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateApplicationAssociation](https://docs.aws.amazon.com/connect/latest/adminguide/onboard-3p-apps.html)  **
  - **Description:** Grants permission to create an ApplicationAssociation
  - **Resource types (\*required):** [application\*](#list_appintegrations-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventIntegrationAssociation](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateEventIntegration.html)  **
  - **Description:** Grants permission to create an EventIntegrationAssociation
  - **Resource types (\*required):** [event-integration\*](#list_appintegrations-resource-event-integration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appintegrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appintegrations-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteApplicationAssociation](https://docs.aws.amazon.com/connect/latest/adminguide/onboard-3p-apps.html)  **
  - **Description:** Grants permission to delete an ApplicationAssociation
  - **Resource types (\*required):** [application-association\*](#list_appintegrations-resource-application-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataIntegrationAssociation](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html)  **
  - **Description:** Grants permission to delete a DataIntegrationAssociation
  - **Resource types (\*required):** [data-integration-association\*](#list_appintegrations-resource-data-integration-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventIntegrationAssociation](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteEventIntegration.html)  **
  - **Description:** Grants permission to delete an EventIntegrationAssociation
  - **Resource types (\*required):** [event-integration-association\*](#list_appintegrations-resource-event-integration-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon AppIntegrations
<a name="list_appintegrations-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationSummary.html)  | arn:${Partition}:app-integrations:${Region}:${Account}:application/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_) | 
|  [application-association](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationAssociationSummary.html)  | arn:${Partition}:app-integrations:${Region}:${Account}:application-association/${ApplicationId}/${ApplicationAssociationId} | [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_) | 
|  [data-integration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DataIntegrationSummary.html)  | arn:${Partition}:app-integrations:${Region}:${Account}:data-integration/${DataIntegrationId} | [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_) | 
|  [data-integration-association](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DataIntegrationAssociationSummary.html)  | arn:${Partition}:app-integrations:${Region}:${Account}:data-integration-association/${DataIntegrationId}/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_) | 
|  [event-integration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_EventIntegration.html)  | arn:${Partition}:app-integrations:${Region}:${Account}:event-integration/${EventIntegrationName} | [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_) | 
|  [event-integration-association](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_EventIntegrationAssociation.html)  | arn:${Partition}:app-integrations:${Region}:${Account}:event-integration-association/${EventIntegrationName}/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_appintegrations-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon AppIntegrations
<a name="list_appintegrations-policy-keys"></a>

Amazon AppIntegrations defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 