

# Actions, resources, and condition keys for Amazon Bedrock Powered by AWS Mantle
<a name="list_bedrock-mantle"></a>

Amazon Bedrock Powered by AWS Mantle (service prefix: `bedrock-mantle`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/bedrock/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-awsmanpol.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/bedrock-mantle/bedrock-mantle.json) for this service.

**Topics**
+ [Actions defined by Amazon Bedrock Powered by AWS Mantle](#list_bedrock-mantle-actions-as-permissions)
+ [Permission-only actions for Amazon Bedrock Powered by AWS Mantle](#list_bedrock-mantle-permission-only-actions)
+ [Resource types defined by Amazon Bedrock Powered by AWS Mantle](#list_bedrock-mantle-resources-for-iam-policies)
+ [Condition keys for Amazon Bedrock Powered by AWS Mantle](#list_bedrock-mantle-policy-keys)

## Actions defined by Amazon Bedrock Powered by AWS Mantle
<a name="list_bedrock-mantle-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ArchiveProject](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to archive a specific project
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateCustomizedModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to associate a customized model with a project
  - **Resource types (\*required):** [customized-model\*](#list_bedrock-mantle-resource-customized-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:CustomizedModelArn](#list_bedrock-mantle-bedrock-mantle_CustomizedModelArn)<br />[bedrock-mantle:ProjectArn](#list_bedrock-mantle-bedrock-mantle_ProjectArn)
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:CustomizedModelArn](#list_bedrock-mantle-bedrock-mantle_CustomizedModelArn)<br />[bedrock-mantle:ProjectArn](#list_bedrock-mantle-bedrock-mantle_ProjectArn)
  - **Access level:** Write

- **   [CancelFineTuningJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to cancel an in-progress fine tuning job
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:FineTuningJob](#list_bedrock-mantle-bedrock-mantle_FineTuningJob)
  - **Access level:** Write

- **   [CancelInference](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to cancel an in-progress inference request
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CountTokens](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to count the tokens in an inference request
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:Model](#list_bedrock-mantle-bedrock-mantle_Model)
  - **Access level:** Read

- **   [CreateCustomizedModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to import a customized model with custom weights
  - **Resource types (\*required):** [customized-model\*](#list_bedrock-mantle-resource-customized-model)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-mantle-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-mantle-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFile](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to create a file in a project
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateFineTuningJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to create a fine tuning job
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:Files](#list_bedrock-mantle-bedrock-mantle_Files)<br />[bedrock-mantle:Model](#list_bedrock-mantle-bedrock-mantle_Model)
  - **Access level:** Write

- **   [CreateInference](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to create an inference request
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:Model](#list_bedrock-mantle-bedrock-mantle_Model)<br />[bedrock-mantle:ServiceTier](#list_bedrock-mantle-bedrock-mantle_ServiceTier)
  - **Access level:** Write

- **   [CreateProject](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to create a project
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-mantle-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-mantle-aws_TagKeys)<br />[bedrock-mantle:DataRetentionMode](#list_bedrock-mantle-bedrock-mantle_DataRetentionMode)
  - **Access level:** Write

- **   [CreateReservation](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to create a capacity reservation for a model
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-mantle-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-mantle-aws_TagKeys)<br />[bedrock-mantle:ProjectArn](#list_bedrock-mantle-bedrock-mantle_ProjectArn)<br />[bedrock-mantle:ReservationArn](#list_bedrock-mantle-bedrock-mantle_ReservationArn)
  - **Resource types (\*required):** [reservation\*](#list_bedrock-mantle-resource-reservation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-mantle-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-mantle-aws_TagKeys)<br />[bedrock-mantle:ProjectArn](#list_bedrock-mantle-bedrock-mantle_ProjectArn)<br />[bedrock-mantle:ReservationArn](#list_bedrock-mantle-bedrock-mantle_ReservationArn)
  - **Access level:** Write

- **   [DeleteCustomizedModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to delete a customized model
  - **Resource types (\*required):** [customized-model\*](#list_bedrock-mantle-resource-customized-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFile](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to delete a specific file
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:Files](#list_bedrock-mantle-bedrock-mantle_Files)
  - **Access level:** Write

- **   [DeleteInference](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to delete a specific inference request
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReservation](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to delete a capacity reservation
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:ProjectArn](#list_bedrock-mantle-bedrock-mantle_ProjectArn)<br />[bedrock-mantle:ReservationArn](#list_bedrock-mantle-bedrock-mantle_ReservationArn)
  - **Resource types (\*required):** [reservation\*](#list_bedrock-mantle-resource-reservation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:ProjectArn](#list_bedrock-mantle-bedrock-mantle_ProjectArn)<br />[bedrock-mantle:ReservationArn](#list_bedrock-mantle-bedrock-mantle_ReservationArn)
  - **Access level:** Write

- **   [DisassociateCustomizedModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to disassociate a customized model from a project
  - **Resource types (\*required):** [customized-model\*](#list_bedrock-mantle-resource-customized-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:CustomizedModelArn](#list_bedrock-mantle-bedrock-mantle_CustomizedModelArn)<br />[bedrock-mantle:ProjectArn](#list_bedrock-mantle-bedrock-mantle_ProjectArn)
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:CustomizedModelArn](#list_bedrock-mantle-bedrock-mantle_CustomizedModelArn)<br />[bedrock-mantle:ProjectArn](#list_bedrock-mantle-bedrock-mantle_ProjectArn)
  - **Access level:** Write

- **   [GetAccountDataRetention](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to retrieve the account-wide data retention setting
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCustomizedModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to get customized model
  - **Resource types (\*required):** [customized-model\*](#list_bedrock-mantle-resource-customized-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFile](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to retrieve information about a specific file
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:Files](#list_bedrock-mantle-bedrock-mantle_Files)
  - **Access level:** Read

- **   [GetFineTuningJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to retrieve details of a specific fine tuning job
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:FineTuningJob](#list_bedrock-mantle-bedrock-mantle_FineTuningJob)
  - **Access level:** Read

- **   [GetInference](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to retrieve details of a specific inference request
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to retrieve information about a specific model
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProject](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to retrieve details of a specific project
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReservation](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to get reservation
  - **Resource types (\*required):** [reservation\*](#list_bedrock-mantle-resource-reservation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCustomizedModelAssociations](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to list project associations for a customized model
  - **Resource types (\*required):** [customized-model\*](#list_bedrock-mantle-resource-customized-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCustomizedModels](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to list customized models
  - **Resource types (\*required):** [customized-model\*](#list_bedrock-mantle-resource-customized-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFiles](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to list all available files in a project
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFineTuningJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to list all available fine tuning jobs in a project
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListModels](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to list all available models in a project
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProjects](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to list projects
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReservations](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to list reservations
  - **Resource types (\*required):** [reservation\*](#list_bedrock-mantle-resource-reservation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [customized-model](#list_bedrock-mantle-resource-customized-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [project](#list_bedrock-mantle-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [reservation](#list_bedrock-mantle-resource-reservation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutAccountDataRetention](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to set the account-wide data retention setting
  - **Resource types (\*required):** 
  - **Condition keys:** [bedrock-mantle:DataRetentionMode](#list_bedrock-mantle-bedrock-mantle_DataRetentionMode)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [customized-model](#list_bedrock-mantle-resource-customized-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-mantle-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-mantle-aws_TagKeys)
  - **Resource types (\*required):** [project](#list_bedrock-mantle-resource-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-mantle-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-mantle-aws_TagKeys)
  - **Resource types (\*required):** [reservation](#list_bedrock-mantle-resource-reservation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-mantle-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-mantle-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [customized-model](#list_bedrock-mantle-resource-customized-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-mantle-aws_TagKeys)
  - **Resource types (\*required):** [project](#list_bedrock-mantle-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-mantle-aws_TagKeys)
  - **Resource types (\*required):** [reservation](#list_bedrock-mantle-resource-reservation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-mantle-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateProject](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to update a specific project
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:DataRetentionMode](#list_bedrock-mantle-bedrock-mantle_DataRetentionMode)
  - **Access level:** Write

- **   [UpdateReservation](https://docs.aws.amazon.com/bedrock/latest/APIReference/#welcome)  **
  - **Description:** Grants permission to update reservation
  - **Resource types (\*required):** [project\*](#list_bedrock-mantle-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:ProjectArn](#list_bedrock-mantle-bedrock-mantle_ProjectArn)<br />[bedrock-mantle:ReservationArn](#list_bedrock-mantle-bedrock-mantle_ReservationArn)
  - **Resource types (\*required):** [reservation\*](#list_bedrock-mantle-resource-reservation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_)<br />[bedrock-mantle:ProjectArn](#list_bedrock-mantle-bedrock-mantle_ProjectArn)<br />[bedrock-mantle:ReservationArn](#list_bedrock-mantle-bedrock-mantle_ReservationArn)
  - **Access level:** Write



## Permission-only actions for Amazon Bedrock Powered by AWS Mantle
<a name="list_bedrock-mantle-permission-only-actions"></a>

The following actions are defined by Amazon Bedrock Powered by AWS Mantle but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CallWithBearerToken](#welcome)  | Grants permission to make API calls using bearer token authentication |  | [bedrock-mantle:BearerTokenType](#list_bedrock-mantle-bedrock-mantle_BearerTokenType) | List | 

## Resource types defined by Amazon Bedrock Powered by AWS Mantle
<a name="list_bedrock-mantle-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [customized-model](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html#CustomizedModel)  | arn:${Partition}:bedrock-mantle:${Region}:${Account}:customized-model/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_) | 
|  [project](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html#Project)  | arn:${Partition}:bedrock-mantle:${Region}:${Account}:project/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_) | 
|  [reservation](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html#Reservation)  | arn:${Partition}:bedrock-mantle:${Region}:${Account}:reservation/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-mantle-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Bedrock Powered by AWS Mantle
<a name="list_bedrock-mantle-policy-keys"></a>

Amazon Bedrock Powered by AWS Mantle defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [bedrock-mantle:BearerTokenType](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrockmantle.html#amazonbedrockmantle-policy-keys)  | Filters access by the Short-term or Long-term bearer tokens | String | 
|   [bedrock-mantle:CustomizedModelArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrockmantle.html#amazonbedrockmantle-policy-keys)  | Filters access by the ARN of the customized model being associated or referenced in cross-resource operations | String | 
|   [bedrock-mantle:DataRetentionMode](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrockmantle.html#amazonbedrockmantle-policy-keys)  | Filters access by the data retention mode being set on a project or account | String | 
|   [bedrock-mantle:Files](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrockmantle.html#amazonbedrockmantle-policy-keys)  | Filters access by the specified file identifiers | ArrayOfString | 
|   [bedrock-mantle:FineTuningJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrockmantle.html#amazonbedrockmantle-policy-keys)  | Filters access by the specified fine-tuning job identifier | String | 
|   [bedrock-mantle:Model](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrockmantle.html#amazonbedrockmantle-policy-keys)  | Filters access by the specified Model | String | 
|   [bedrock-mantle:ProjectArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrockmantle.html#amazonbedrockmantle-policy-keys)  | Filters access by the ARN of the project being associated or referenced in cross-resource operations | String | 
|   [bedrock-mantle:ReservationArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrockmantle.html#amazonbedrockmantle-policy-keys)  | Filters access by the ARN of the reservation being referenced in cross-resource operations | String | 
|   [bedrock-mantle:ServiceTier](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrockmantle.html#amazonbedrockmantle-policy-keys)  | Filters access by the specified ServiceTier | String | 