

# Actions, resources, and condition keys for AWS AppFabric
<a name="list_appfabric"></a>

AWS AppFabric (service prefix: `appfabric`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/appfabric/latest/adminguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/appfabric/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/appfabric/latest/adminguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/appfabric/appfabric.json) for this service.

**Topics**
+ [API operations defined by AWS AppFabric](#list_appfabric-operations)
+ [Actions defined by AWS AppFabric](#list_appfabric-actions-as-permissions)
+ [Resource types defined by AWS AppFabric](#list_appfabric-resources-for-iam-policies)
+ [Condition keys for AWS AppFabric](#list_appfabric-policy-keys)

## API operations defined by AWS AppFabric
<a name="list_appfabric-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_appfabric-actions-as-permissions).




- **   BatchGetUserAccessTasks  **
  - **IAM action:**  [appfabric:BatchGetUserAccessTasks](#list_appfabric-action-BatchGetUserAccessTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConnectAppAuthorization  **
  - **IAM action:**  [appfabric:ConnectAppAuthorization](#list_appfabric-action-ConnectAppAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAppAuthorization  **
  - **IAM action:**  [appfabric:CreateAppAuthorization](#list_appfabric-action-CreateAppAuthorization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appfabric:TagResource](#list_appfabric-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAppBundle  **
  - **IAM action:**  [appfabric:CreateAppBundle](#list_appfabric-action-CreateAppBundle)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appfabric:TagResource](#list_appfabric-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIngestion  **
  - **IAM action:**  [appfabric:CreateIngestion](#list_appfabric-action-CreateIngestion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appfabric:TagResource](#list_appfabric-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIngestionDestination  **
  - **IAM action:**  [appfabric:CreateIngestionDestination](#list_appfabric-action-CreateIngestionDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appfabric:TagResource](#list_appfabric-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAppAuthorization  **
  - **IAM action:**  [appfabric:DeleteAppAuthorization](#list_appfabric-action-DeleteAppAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAppBundle  **
  - **IAM action:**  [appfabric:DeleteAppBundle](#list_appfabric-action-DeleteAppBundle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIngestion  **
  - **IAM action:**  [appfabric:DeleteIngestion](#list_appfabric-action-DeleteIngestion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIngestionDestination  **
  - **IAM action:**  [appfabric:DeleteIngestionDestination](#list_appfabric-action-DeleteIngestionDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAppAuthorization  **
  - **IAM action:**  [appfabric:GetAppAuthorization](#list_appfabric-action-GetAppAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAppBundle  **
  - **IAM action:**  [appfabric:GetAppBundle](#list_appfabric-action-GetAppBundle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIngestion  **
  - **IAM action:**  [appfabric:GetIngestion](#list_appfabric-action-GetIngestion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIngestionDestination  **
  - **IAM action:**  [appfabric:GetIngestionDestination](#list_appfabric-action-GetIngestionDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAppAuthorizations  **
  - **IAM action:**  [appfabric:ListAppAuthorizations](#list_appfabric-action-ListAppAuthorizations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppBundles  **
  - **IAM action:**  [appfabric:ListAppBundles](#list_appfabric-action-ListAppBundles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIngestionDestinations  **
  - **IAM action:**  [appfabric:ListIngestionDestinations](#list_appfabric-action-ListIngestionDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIngestions  **
  - **IAM action:**  [appfabric:ListIngestions](#list_appfabric-action-ListIngestions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [appfabric:ListTagsForResource](#list_appfabric-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartIngestion  **
  - **IAM action:**  [appfabric:StartIngestion](#list_appfabric-action-StartIngestion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartUserAccessTasks  **
  - **IAM action:**  [appfabric:StartUserAccessTasks](#list_appfabric-action-StartUserAccessTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopIngestion  **
  - **IAM action:**  [appfabric:StopIngestion](#list_appfabric-action-StopIngestion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [appfabric:TagResource](#list_appfabric-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [appfabric:UntagResource](#list_appfabric-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAppAuthorization  **
  - **IAM action:**  [appfabric:UpdateAppAuthorization](#list_appfabric-action-UpdateAppAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIngestionDestination  **
  - **IAM action:**  [appfabric:UpdateIngestionDestination](#list_appfabric-action-UpdateIngestionDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS AppFabric
<a name="list_appfabric-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetUserAccessTasks](https://docs.aws.amazon.com/appfabric/latest/api/API_BatchGetUserAccessTasks.html)  **
  - **Description:** Grants permission to start user access tasks for multiple users
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ConnectAppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_ConnectAppAuthorization.html)  **
  - **Description:** Grants permission to connect app authorizations
  - **Resource types (\*required):** [appauthorization\*](#list_appfabric-resource-appauthorization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_CreateAppAuthorization.html)  **
  - **Description:** Grants permission to create app authorizations for app bundles
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAppBundle](https://docs.aws.amazon.com/appfabric/latest/api/API_CreateAppBundle.html)  **
  - **Description:** Grants permission to create app bundles in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appfabric-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIngestion](https://docs.aws.amazon.com/appfabric/latest/api/API_CreateIngestion.html)  **
  - **Description:** Grants permission to create ingestions for app bundles
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIngestionDestination](https://docs.aws.amazon.com/appfabric/latest/api/API_CreateIngestionDestination.html)  **
  - **Description:** Grants permission to create ingestion destinations for app bundles
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Resource types (\*required):** [ingestion\*](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_DeleteAppAuthorization.html)  **
  - **Description:** Grants permission to delete app authorizations within an app bundle
  - **Resource types (\*required):** [appauthorization\*](#list_appfabric-resource-appauthorization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAppBundle](https://docs.aws.amazon.com/appfabric/latest/api/API_DeleteAppBundle.html)  **
  - **Description:** Grants permission to delete app bundles in your account
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIngestion](https://docs.aws.amazon.com/appfabric/latest/api/API_DeleteIngestion.html)  **
  - **Description:** Grants permission to delete ingestions within an app bundle
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestion\*](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIngestionDestination](https://docs.aws.amazon.com/appfabric/latest/api/API_DeleteIngestionDestination.html)  **
  - **Description:** Grants permission to delete destinations within an ingestion
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestion\*](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestiondestination\*](#list_appfabric-resource-ingestiondestination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_GetAppAuthorization.html)  **
  - **Description:** Grants permission to view details about app authorizations
  - **Resource types (\*required):** [appauthorization\*](#list_appfabric-resource-appauthorization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAppBundle](https://docs.aws.amazon.com/appfabric/latest/api/API_GetAppBundle.html)  **
  - **Description:** Grants permission to view details about app bundles
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIngestion](https://docs.aws.amazon.com/appfabric/latest/api/API_GetIngestion.html)  **
  - **Description:** Grants permission to view details about ingestions
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestion\*](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIngestionDestination](https://docs.aws.amazon.com/appfabric/latest/api/API_GetIngestionDestination.html)  **
  - **Description:** Grants permission to view details about ingestion destinations
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestion\*](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestiondestination\*](#list_appfabric-resource-ingestiondestination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAppAuthorizations](https://docs.aws.amazon.com/appfabric/latest/api/API_ListAppAuthorizations.html)  **
  - **Description:** Grants permission to retrieve a list of app authorizations within an app bundle
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppBundles](https://docs.aws.amazon.com/appfabric/latest/api/API_ListAppBundles.html)  **
  - **Description:** Grants permission to retrieve a list of app bundles in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIngestionDestinations](https://docs.aws.amazon.com/appfabric/latest/api/API_ListIngestionDestinations.html)  **
  - **Description:** Grants permission to retrieve a list of destinations within an ingestion
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestion\*](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIngestions](https://docs.aws.amazon.com/appfabric/latest/api/API_ListIngestions.html)  **
  - **Description:** Grants permission to retrieve a list of ingestions within an app bundle
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/appfabric/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for AppFabric resources
  - **Resource types (\*required):** [appauthorization](#list_appfabric-resource-appauthorization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [appbundle](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestion](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestiondestination](#list_appfabric-resource-ingestiondestination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartIngestion](https://docs.aws.amazon.com/appfabric/latest/api/API_StartIngestion.html)  **
  - **Description:** Grants permission to start ingestions
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestion\*](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartUserAccessTasks](https://docs.aws.amazon.com/appfabric/latest/api/API_StartUserAccessTasks.html)  **
  - **Description:** Grants permission to start user access tasks
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopIngestion](https://docs.aws.amazon.com/appfabric/latest/api/API_StopIngestion.html)  **
  - **Description:** Grants permission to stop ingestions
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestion\*](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/appfabric/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to tag AppFabric resources
  - **Resource types (\*required):** [appauthorization](#list_appfabric-resource-appauthorization) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Resource types (\*required):** [appbundle](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Resource types (\*required):** [ingestion](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Resource types (\*required):** [ingestiondestination](#list_appfabric-resource-ingestiondestination) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/appfabric/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to untag AppFabric resources
  - **Resource types (\*required):** [appauthorization](#list_appfabric-resource-appauthorization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Resource types (\*required):** [appbundle](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Resource types (\*required):** [ingestion](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Resource types (\*required):** [ingestiondestination](#list_appfabric-resource-ingestiondestination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appfabric-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_UpdateAppAuthorization.html)  **
  - **Description:** Grants permission to update app authorizations within app bundles
  - **Resource types (\*required):** [appauthorization\*](#list_appfabric-resource-appauthorization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIngestionDestination](https://docs.aws.amazon.com/appfabric/latest/api/API_UpdateIngestionDestination.html)  **
  - **Description:** Grants permission to update destinations within ingestions
  - **Resource types (\*required):** [appbundle\*](#list_appfabric-resource-appbundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestion\*](#list_appfabric-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ingestiondestination\*](#list_appfabric-resource-ingestiondestination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS AppFabric
<a name="list_appfabric-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [appauthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_AppAuthorization.html)  | arn:${Partition}:appfabric:${Region}:${Account}:appbundle/${AppbundleId}/appauthorization/${AppAuthorizationIdentifier} | [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_) | 
|  [appbundle](https://docs.aws.amazon.com/appfabric/latest/api/API_AppBundle.html)  | arn:${Partition}:appfabric:${Region}:${Account}:appbundle/${AppBundleIdentifier} | [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_) | 
|  [ingestion](https://docs.aws.amazon.com/appfabric/latest/api/API_Ingestion.html)  | arn:${Partition}:appfabric:${Region}:${Account}:appbundle/${AppbundleId}/ingestion/${IngestionIdentifier} | [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_) | 
|  [ingestiondestination](https://docs.aws.amazon.com/appfabric/latest/api/API_IngestionDestination.html)  | arn:${Partition}:appfabric:${Region}:${Account}:appbundle/${AppbundleId}/ingestion/${IngestionIdentifier}/ingestiondestination/${IngestionDestinationIdentifier} | [aws:ResourceTag/${TagKey}](#list_appfabric-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS AppFabric
<a name="list_appfabric-policy-keys"></a>

AWS AppFabric defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 