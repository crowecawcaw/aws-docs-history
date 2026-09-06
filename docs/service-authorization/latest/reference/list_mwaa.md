

# Actions, resources, and condition keys for Amazon Managed Workflows for Apache Airflow
<a name="list_mwaa"></a>

Amazon Managed Workflows for Apache Airflow (service prefix: `airflow`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mwaa/latest/API/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mwaa/latest/userguide/manage-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/airflow/airflow.json) for this service.

**Topics**
+ [API operations defined by Amazon Managed Workflows for Apache Airflow](#list_mwaa-operations)
+ [Actions defined by Amazon Managed Workflows for Apache Airflow](#list_mwaa-actions-as-permissions)
+ [Resource types defined by Amazon Managed Workflows for Apache Airflow](#list_mwaa-resources-for-iam-policies)
+ [Condition keys for Amazon Managed Workflows for Apache Airflow](#list_mwaa-policy-keys)

## API operations defined by Amazon Managed Workflows for Apache Airflow
<a name="list_mwaa-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mwaa-actions-as-permissions).




- **   CreateCliToken  **
  - **IAM action:**  [airflow:CreateCliToken](#list_mwaa-action-CreateCliToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEnvironment  **
  - **IAM action:**  [airflow:CreateEnvironment](#list_mwaa-action-CreateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [airflow:TagResource](#list_mwaa-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** airflow.amazonaws.com / **Access level:** Write

- **   CreateWebLoginToken  **
  - **IAM action:**  [airflow:CreateWebLoginToken](#list_mwaa-action-CreateWebLoginToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironment  **
  - **IAM action:**  [airflow:DeleteEnvironment](#list_mwaa-action-DeleteEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetEnvironment  **
  - **IAM action:**  [airflow:GetEnvironment](#list_mwaa-action-GetEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeRestApi  **
  - **IAM action:**  [airflow:InvokeRestApi](#list_mwaa-action-InvokeRestApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListEnvironments  **
  - **IAM action:**  [airflow:ListEnvironments](#list_mwaa-action-ListEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [airflow:ListTagsForResource](#list_mwaa-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PublishMetrics  **
  - **IAM action:**  [airflow:PublishMetrics](#list_mwaa-action-PublishMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [airflow:TagResource](#list_mwaa-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [airflow:UntagResource](#list_mwaa-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateEnvironment  **
  - **IAM action:**  [airflow:UpdateEnvironment](#list_mwaa-action-UpdateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** airflow.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Managed Workflows for Apache Airflow
<a name="list_mwaa-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateCliToken](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateCliToken.html)  **
  - **Description:** Grants permission to create a short-lived token that allows a user to invoke Airflow CLI via an endpoint on the Apache Airflow Webserver
  - **Resource types (\*required):** [environment\*](#list_mwaa-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create an Amazon MWAA environment
  - **Resource types (\*required):** [environment\*](#list_mwaa-resource-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mwaa-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mwaa-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWebLoginToken](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateWebLoginToken.html)  **
  - **Description:** Grants permission to create a short-lived token that allows a user to log into Apache Airflow web UI
  - **Resource types (\*required):** [rbac-role\*](#list_mwaa-resource-rbac-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete an Amazon MWAA environment
  - **Resource types (\*required):** [environment\*](#list_mwaa-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_GetEnvironment.html)  **
  - **Description:** Grants permission to view details about an Amazon MWAA environment
  - **Resource types (\*required):** [environment\*](#list_mwaa-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeRestApi](https://docs.aws.amazon.com/mwaa/latest/API/API_InvokeRestApi.html)  **
  - **Description:** Grants permission to invoke Airflow REST API via an endpoint on the Apache Airflow Webserver
  - **Resource types (\*required):** [rbac-role\*](#list_mwaa-resource-rbac-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListEnvironments](https://docs.aws.amazon.com/mwaa/latest/API/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list the Amazon MWAA environments in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/mwaa/latest/API/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to lists tag for an Amazon MWAA environment
  - **Resource types (\*required):** [environment](#list_mwaa-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PublishMetrics](https://docs.aws.amazon.com/mwaa/latest/API/API_PublishMetrics.html)  **
  - **Description:** Grants permission to publish metrics for an Amazon MWAA environment
  - **Resource types (\*required):** [environment\*](#list_mwaa-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/mwaa/latest/API/API_TagResource.html)  **
  - **Description:** Grants permission to tag an Amazon MWAA environment
  - **Resource types (\*required):** [environment](#list_mwaa-resource-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mwaa-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mwaa-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/mwaa/latest/API/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an Amazon MWAA environment
  - **Resource types (\*required):** [environment](#list_mwaa-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mwaa-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to modify an Amazon MWAA environment
  - **Resource types (\*required):** [environment\*](#list_mwaa-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Managed Workflows for Apache Airflow
<a name="list_mwaa-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [environment](https://docs.aws.amazon.com/mwaa/latest/userguide/using-mwaa.html)  | arn:${Partition}:airflow:${Region}:${Account}:environment/${EnvironmentName} | [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_) | 
|  [rbac-role](https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html)  | arn:${Partition}:airflow:${Region}:${Account}:role/${EnvironmentName}/${RoleName} | [aws:ResourceTag/${TagKey}](#list_mwaa-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Managed Workflows for Apache Airflow
<a name="list_mwaa-policy-keys"></a>

Amazon Managed Workflows for Apache Airflow defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [airflow:DagAccessEntity](https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html)  | Filters access by the DAG sub-resource being accessed | String | 
|   [airflow:ResourceAction](https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html)  | Filters access by the action being performed on the Airflow resource | String | 
|   [airflow:ResourceId](https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html)  | Filters access by the identifier of the specific Airflow resource, such as a DAG ID or connection ID | String | 
|   [airflow:ResourceType](https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html)  | Filters access by the Airflow resource type specified in the request | String | 
|   [airflow:TeamNames](https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html)  | Filters access by the team names associated with the caller's identity, enabling team-based access control for Airflow resources | ArrayOfString | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys in the request | ArrayOfString | 