

# Actions, resources, and condition keys for Service Quotas
<a name="list_service-quotas"></a>

Service Quotas (service prefix: `servicequotas`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/servicequotas/latest/userguide/identity-access-management.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/servicequotas/servicequotas.json) for this service.

**Topics**
+ [API operations defined by Service Quotas](#list_service-quotas-operations)
+ [Actions defined by Service Quotas](#list_service-quotas-actions-as-permissions)
+ [Resource types defined by Service Quotas](#list_service-quotas-resources-for-iam-policies)
+ [Condition keys for Service Quotas](#list_service-quotas-policy-keys)

## API operations defined by Service Quotas
<a name="list_service-quotas-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_service-quotas-actions-as-permissions).




- **   AssociateServiceQuotaTemplate  **
  - **IAM action:**  [servicequotas:AssociateServiceQuotaTemplate](#list_service-quotas-action-AssociateServiceQuotaTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSupportCase  **
  - **IAM action:**  [servicequotas:CreateSupportCase](#list_service-quotas-action-CreateSupportCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceQuotaIncreaseRequestFromTemplate  **
  - **IAM action:**  [servicequotas:DeleteServiceQuotaIncreaseRequestFromTemplate](#list_service-quotas-action-DeleteServiceQuotaIncreaseRequestFromTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateServiceQuotaTemplate  **
  - **IAM action:**  [servicequotas:DisassociateServiceQuotaTemplate](#list_service-quotas-action-DisassociateServiceQuotaTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAWSDefaultServiceQuota  **
  - **IAM action:**  [servicequotas:GetAWSDefaultServiceQuota](#list_service-quotas-action-GetAWSDefaultServiceQuota) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssociationForServiceQuotaTemplate  **
  - **IAM action:**  [servicequotas:GetAssociationForServiceQuotaTemplate](#list_service-quotas-action-GetAssociationForServiceQuotaTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutoManagementConfiguration  **
  - **IAM action:**  [servicequotas:GetAutoManagementConfiguration](#list_service-quotas-action-GetAutoManagementConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQuotaUtilizationReport  **
  - **IAM action:**  [servicequotas:GetQuotaUtilizationReport](#list_service-quotas-action-GetQuotaUtilizationReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRequestedServiceQuotaChange  **
  - **IAM action:**  [servicequotas:GetRequestedServiceQuotaChange](#list_service-quotas-action-GetRequestedServiceQuotaChange) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceQuota  **
  - **IAM action:**  [servicequotas:GetServiceQuota](#list_service-quotas-action-GetServiceQuota) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceQuotaIncreaseRequestFromTemplate  **
  - **IAM action:**  [servicequotas:GetServiceQuotaIncreaseRequestFromTemplate](#list_service-quotas-action-GetServiceQuotaIncreaseRequestFromTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAWSDefaultServiceQuotas  **
  - **IAM action:**  [servicequotas:ListAWSDefaultServiceQuotas](#list_service-quotas-action-ListAWSDefaultServiceQuotas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRequestedServiceQuotaChangeHistory  **
  - **IAM action:**  [servicequotas:ListRequestedServiceQuotaChangeHistory](#list_service-quotas-action-ListRequestedServiceQuotaChangeHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRequestedServiceQuotaChangeHistoryByQuota  **
  - **IAM action:**  [servicequotas:ListRequestedServiceQuotaChangeHistoryByQuota](#list_service-quotas-action-ListRequestedServiceQuotaChangeHistoryByQuota) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceQuotaIncreaseRequestsInTemplate  **
  - **IAM action:**  [servicequotas:ListServiceQuotaIncreaseRequestsInTemplate](#list_service-quotas-action-ListServiceQuotaIncreaseRequestsInTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceQuotas  **
  - **IAM action:**  [servicequotas:ListServiceQuotas](#list_service-quotas-action-ListServiceQuotas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServices  **
  - **IAM action:**  [servicequotas:ListServices](#list_service-quotas-action-ListServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [servicequotas:ListTagsForResource](#list_service-quotas-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutServiceQuotaIncreaseRequestIntoTemplate  **
  - **IAM action:**  [servicequotas:PutServiceQuotaIncreaseRequestIntoTemplate](#list_service-quotas-action-PutServiceQuotaIncreaseRequestIntoTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RequestServiceQuotaIncrease  **
  - **IAM action:**  [servicequotas:RequestServiceQuotaIncrease](#list_service-quotas-action-RequestServiceQuotaIncrease) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAutoManagement  **
  - **IAM action:**  [servicequotas:StartAutoManagement](#list_service-quotas-action-StartAutoManagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartQuotaUtilizationReport  **
  - **IAM action:**  [servicequotas:StartQuotaUtilizationReport](#list_service-quotas-action-StartQuotaUtilizationReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StopAutoManagement  **
  - **IAM action:**  [servicequotas:StopAutoManagement](#list_service-quotas-action-StopAutoManagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [servicequotas:TagResource](#list_service-quotas-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [servicequotas:UntagResource](#list_service-quotas-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAutoManagement  **
  - **IAM action:**  [servicequotas:UpdateAutoManagement](#list_service-quotas-action-UpdateAutoManagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Service Quotas
<a name="list_service-quotas-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateServiceQuotaTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_AssociateServiceQuotaTemplate.html)  **
  - **Description:** Grants permission to associate the Service Quotas template with your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSupportCase](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_CreateSupportCase.html)  **
  - **Description:** Grants permission to submit a request to create a support case for an existing quota increase request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteServiceQuotaIncreaseRequestFromTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_DeleteServiceQuotaIncreaseRequestFromTemplate.html)  **
  - **Description:** Grants permission to remove the specified service quota from the service quota template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateServiceQuotaTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_DisassociateServiceQuotaTemplate.html)  **
  - **Description:** Grants permission to disassociate the Service Quotas template from your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAWSDefaultServiceQuota](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetAWSDefaultServiceQuota.html)  **
  - **Description:** Grants permission to return the details for the specified service quota, including the AWS default value
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAssociationForServiceQuotaTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetAssociationForServiceQuotaTemplate.html)  **
  - **Description:** Grants permission to retrieve the ServiceQuotaTemplateAssociationStatus value, which tells you if the Service Quotas template is associated with an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAutoManagementConfiguration](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetAutoManagementConfiguration.html)  **
  - **Description:** Grants permission to retrieve the automatic management of Service Quotas configuration, including notification settings, opt-in type, and excluded quotas
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetQuotaUtilizationReport](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetQuotaUtilizationReport.html)  **
  - **Description:** Grants permission to view the generated report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRequestedServiceQuotaChange](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetRequestedServiceQuotaChange.html)  **
  - **Description:** Grants permission to retrieve the details for a particular service quota increase request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceQuota](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetServiceQuota.html)  **
  - **Description:** Grants permission to return the details for the specified service quota, including the applied value
  - **Resource types (\*required):** [quota](#list_service-quotas-resource-quota)
  - **Condition keys:** [servicequotas:service](#list_service-quotas-servicequotas_service)
  - **Access level:** Read

- **   [GetServiceQuotaIncreaseRequestFromTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetServiceQuotaIncreaseRequestFromTemplate.html)  **
  - **Description:** Grants permission to retrieve the details for a service quota increase request from the service quota template
  - **Resource types (\*required):** [quota](#list_service-quotas-resource-quota)
  - **Condition keys:** [servicequotas:service](#list_service-quotas-servicequotas_service)
  - **Access level:** Read

- **   [ListAWSDefaultServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListAWSDefaultServiceQuotas.html)  **
  - **Description:** Grants permission to list all default service quotas for the specified AWS service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRequestedServiceQuotaChangeHistory](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistory.html)  **
  - **Description:** Grants permission to request a list of the changes to quotas for a service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRequestedServiceQuotaChangeHistoryByQuota](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistoryByQuota.html)  **
  - **Description:** Grants permission to request a list of the changes to specific service quotas
  - **Resource types (\*required):** [quota](#list_service-quotas-resource-quota)
  - **Condition keys:** [servicequotas:service](#list_service-quotas-servicequotas_service)
  - **Access level:** Read

- **   [ListServiceQuotaIncreaseRequestsInTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotaIncreaseRequestsInTemplate.html)  **
  - **Description:** Grants permission to return a list of the service quota increase requests from the service quota template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html)  **
  - **Description:** Grants permission to list all service quotas for the specified AWS service, in that account, in that Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListServices](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServices.html)  **
  - **Description:** Grants permission to list the AWS services available in Service Quotas
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to view the existing tags on a SQ resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutServiceQuotaIncreaseRequestIntoTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_PutServiceQuotaIncreaseRequestIntoTemplate.html)  **
  - **Description:** Grants permission to define and add a quota to the service quota template
  - **Resource types (\*required):** [quota](#list_service-quotas-resource-quota)
  - **Condition keys:** [servicequotas:service](#list_service-quotas-servicequotas_service)
  - **Access level:** Write

- **   [RequestServiceQuotaIncrease](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html)  **
  - **Description:** Grants permission to submit the request for a service quota increase
  - **Resource types (\*required):** [quota](#list_service-quotas-resource-quota)
  - **Condition keys:** [servicequotas:service](#list_service-quotas-servicequotas_service)
  - **Access level:** Write

- **   [StartAutoManagement](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_StartAutoManagement.html)  **
  - **Description:** Grants permission to enable automatic management of Service Quotas for an AWS account, including notification preferences and excluded quotas configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartQuotaUtilizationReport](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_StartQuotaUtilizationReport.html)  **
  - **Description:** Grants permission to query quota utilization and create a report for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StopAutoManagement](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_StopAutoManagement.html)  **
  - **Description:** Grants permission to stop automatic management of Service Quotas for an AWS account and remove all associated configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to associate a set of tags with an existing SQ resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_service-quotas-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_service-quotas-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a set of tags from a SQ resource, where tags to be removed match a set of customer-supplied tag keys
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:TagKeys](#list_service-quotas-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAutoManagement](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_UpdateAutoManagement.html)  **
  - **Description:** Grants permission to update the automatic management of Service Quotas configuration, including notification preferences and excluded quotas
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Service Quotas
<a name="list_service-quotas-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [quota](https://docs.aws.amazon.com/servicequotas/latest/userguide/identity-access-management.html#resources)  | arn:${Partition}:servicequotas:${Region}:${Account}:${ServiceCode}/${QuotaCode} |   | 

## Condition keys for Service Quotas
<a name="list_service-quotas-policy-keys"></a>

Service Quotas defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [servicequotas:service](https://docs.aws.amazon.com/servicequotas/latest/userguide/identity-access-management.html#condition-keys)  | Filters access by the specified AWS service | String | 