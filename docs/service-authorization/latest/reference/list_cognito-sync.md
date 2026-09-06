

# Actions, resources, and condition keys for Amazon Cognito Sync
<a name="list_cognito-sync"></a>

Amazon Cognito Sync (service prefix: `cognito-sync`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cognitosync/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cognito/latest/developerguide/resource-permissions.html#amazon-cognito-amazon-resource-names) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cognito-sync/cognito-sync.json) for this service.

**Topics**
+ [API operations defined by Amazon Cognito Sync](#list_cognito-sync-operations)
+ [Actions defined by Amazon Cognito Sync](#list_cognito-sync-actions-as-permissions)
+ [Permission-only actions for Amazon Cognito Sync](#list_cognito-sync-permission-only-actions)
+ [Resource types defined by Amazon Cognito Sync](#list_cognito-sync-resources-for-iam-policies)
+ [Condition keys for Amazon Cognito Sync](#list_cognito-sync-policy-keys)

## API operations defined by Amazon Cognito Sync
<a name="list_cognito-sync-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cognito-sync-actions-as-permissions).




- **   BulkPublish  **
  - **IAM action:**  [cognito-sync:BulkPublish](#list_cognito-sync-action-BulkPublish) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataset  **
  - **IAM action:**  [cognito-sync:DeleteDataset](#list_cognito-sync-action-DeleteDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDataset  **
  - **IAM action:**  [cognito-sync:DescribeDataset](#list_cognito-sync-action-DescribeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIdentityPoolUsage  **
  - **IAM action:**  [cognito-sync:DescribeIdentityPoolUsage](#list_cognito-sync-action-DescribeIdentityPoolUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIdentityUsage  **
  - **IAM action:**  [cognito-sync:DescribeIdentityUsage](#list_cognito-sync-action-DescribeIdentityUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBulkPublishDetails  **
  - **IAM action:**  [cognito-sync:GetBulkPublishDetails](#list_cognito-sync-action-GetBulkPublishDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCognitoEvents  **
  - **IAM action:**  [cognito-sync:GetCognitoEvents](#list_cognito-sync-action-GetCognitoEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentityPoolConfiguration  **
  - **IAM action:**  [cognito-sync:GetIdentityPoolConfiguration](#list_cognito-sync-action-GetIdentityPoolConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDatasets  **
  - **IAM action:**  [cognito-sync:ListDatasets](#list_cognito-sync-action-ListDatasets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdentityPoolUsage  **
  - **IAM action:**  [cognito-sync:ListIdentityPoolUsage](#list_cognito-sync-action-ListIdentityPoolUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRecords  **
  - **IAM action:**  [cognito-sync:ListRecords](#list_cognito-sync-action-ListRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterDevice  **
  - **IAM action:**  [cognito-sync:RegisterDevice](#list_cognito-sync-action-RegisterDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetCognitoEvents  **
  - **IAM action:**  [cognito-sync:SetCognitoEvents](#list_cognito-sync-action-SetCognitoEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetIdentityPoolConfiguration  **
  - **IAM action:**  [cognito-sync:SetIdentityPoolConfiguration](#list_cognito-sync-action-SetIdentityPoolConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SubscribeToDataset  **
  - **IAM action:**  [cognito-sync:SubscribeToDataset](#list_cognito-sync-action-SubscribeToDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UnsubscribeFromDataset  **
  - **IAM action:**  [cognito-sync:UnsubscribeFromDataset](#list_cognito-sync-action-UnsubscribeFromDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRecords  **
  - **IAM action:**  [cognito-sync:UpdateRecords](#list_cognito-sync-action-UpdateRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Cognito Sync
<a name="list_cognito-sync-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BulkPublish](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_BulkPublish.html)  **
  - **Description:** Grants permission to initiate a bulk publish of all existing datasets for an Identity Pool to the configured stream
  - **Resource types (\*required):** [identitypool\*](#list_cognito-sync-resource-identitypool)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DeleteDataset.html)  **
  - **Description:** Grants permission to delete a specific dataset
  - **Resource types (\*required):** [dataset\*](#list_cognito-sync-resource-dataset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeDataset](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeDataset.html)  **
  - **Description:** Grants permission to get metadata about a dataset by identity and dataset name
  - **Resource types (\*required):** [dataset\*](#list_cognito-sync-resource-dataset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeIdentityPoolUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeIdentityPoolUsage.html)  **
  - **Description:** Grants permission to get usage details (for example, data storage) about a particular identity pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-sync-resource-identitypool)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeIdentityUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeIdentityUsage.html)  **
  - **Description:** Grants permission to get usage information for an identity, including number of datasets and data usage
  - **Resource types (\*required):** [identity\*](#list_cognito-sync-resource-identity)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBulkPublishDetails](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetBulkPublishDetails.html)  **
  - **Description:** Grants permission to get the status of the last BulkPublish operation for an identity pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-sync-resource-identitypool)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCognitoEvents](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetCognitoEvents.html)  **
  - **Description:** Grants permission to get the events and the corresponding Lambda functions associated with an identity pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-sync-resource-identitypool)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIdentityPoolConfiguration](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetIdentityPoolConfiguration.html)  **
  - **Description:** Grants permission to get the configuration settings of an identity pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-sync-resource-identitypool)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDatasets](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListDatasets.html)  **
  - **Description:** Grants permission to list datasets for an identity
  - **Resource types (\*required):** [dataset\*](#list_cognito-sync-resource-dataset)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIdentityPoolUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListIdentityPoolUsage.html)  **
  - **Description:** Grants permission to get a list of identity pools registered with Cognito
  - **Resource types (\*required):** [identitypool\*](#list_cognito-sync-resource-identitypool)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRecords](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListRecords.html)  **
  - **Description:** Grants permission to get paginated records, optionally changed after a particular sync count for a dataset and identity
  - **Resource types (\*required):** [dataset\*](#list_cognito-sync-resource-dataset)
  - **Condition keys:**  
  - **Access level:** Read

- **   [RegisterDevice](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_RegisterDevice.html)  **
  - **Description:** Grants permission to register a device to receive push sync notifications
  - **Resource types (\*required):** [identity\*](#list_cognito-sync-resource-identity)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetCognitoEvents](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_SetCognitoEvents.html)  **
  - **Description:** Grants permission to set the AWS Lambda function for a given event type for an identity pool
  - **Resource types (\*required):** [identitypool\*](#list_cognito-sync-resource-identitypool)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetIdentityPoolConfiguration](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_SetIdentityPoolConfiguration.html)  **
  - **Description:** Grants permission to set the necessary configuration for push sync
  - **Resource types (\*required):** [identitypool\*](#list_cognito-sync-resource-identitypool)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SubscribeToDataset](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_SubscribeToDataset.html)  **
  - **Description:** Grants permission to subscribe to receive notifications when a dataset is modified by another device
  - **Resource types (\*required):** [dataset\*](#list_cognito-sync-resource-dataset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UnsubscribeFromDataset](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_UnsubscribeFromDataset.html)  **
  - **Description:** Grants permission to unsubscribe from receiving notifications when a dataset is modified by another device
  - **Resource types (\*required):** [dataset\*](#list_cognito-sync-resource-dataset)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRecords](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_UpdateRecords.html)  **
  - **Description:** Grants permission to post updates to records and add and delete records for a dataset and user
  - **Resource types (\*required):** [dataset\*](#list_cognito-sync-resource-dataset)
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for Amazon Cognito Sync
<a name="list_cognito-sync-permission-only-actions"></a>

The following actions are defined by Amazon Cognito Sync but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   QueryRecords  **
  - **Description:** Grants permission to query records
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   SetDatasetConfiguration  **
  - **Description:** Grants permission to configure datasets
  - **Resource types (\*required):** [dataset\*](#list_cognito-sync-resource-dataset)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Cognito Sync
<a name="list_cognito-sync-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [dataset](https://docs.aws.amazon.com/cognito/latest/developerguide/synchronizing-data.html#understanding-datasets)  | arn:${Partition}:cognito-sync:${Region}:${Account}:identitypool/${IdentityPoolId}/identity/${IdentityId}/dataset/${DatasetName} |   | 
|  [identity](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html#authenticated-and-unauthenticated-identities)  | arn:${Partition}:cognito-sync:${Region}:${Account}:identitypool/${IdentityPoolId}/identity/${IdentityId} |   | 
|  [identitypool](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html)  | arn:${Partition}:cognito-sync:${Region}:${Account}:identitypool/${IdentityPoolId} |   | 

## Condition keys for Amazon Cognito Sync
<a name="list_cognito-sync-policy-keys"></a>

Amazon Cognito Sync has no service-specific condition keys that can be used in the `Condition` element of policy statements.