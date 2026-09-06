

# Actions, resources, and condition keys for AWS IoT Core Device Advisor
<a name="list_iotdeviceadvisor"></a>

AWS IoT Core Device Advisor (service prefix: `iotdeviceadvisor`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iot/latest/apireference/API_Operations_AWS_IoT_Core_Device_Advisor.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iot/latest/developerguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iotdeviceadvisor/iotdeviceadvisor.json) for this service.

**Topics**
+ [API operations defined by AWS IoT Core Device Advisor](#list_iotdeviceadvisor-operations)
+ [Actions defined by AWS IoT Core Device Advisor](#list_iotdeviceadvisor-actions-as-permissions)
+ [Resource types defined by AWS IoT Core Device Advisor](#list_iotdeviceadvisor-resources-for-iam-policies)
+ [Condition keys for AWS IoT Core Device Advisor](#list_iotdeviceadvisor-policy-keys)

## API operations defined by AWS IoT Core Device Advisor
<a name="list_iotdeviceadvisor-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iotdeviceadvisor-actions-as-permissions).




- **   CreateSuiteDefinition  **
  - **IAM action:**  [iotdeviceadvisor:CreateSuiteDefinition](#list_iotdeviceadvisor-action-CreateSuiteDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotdeviceadvisor:TagResource](#list_iotdeviceadvisor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotdeviceadvisor.amazonaws.com / **Access level:** Write

- **   DeleteSuiteDefinition  **
  - **IAM action:**  [iotdeviceadvisor:DeleteSuiteDefinition](#list_iotdeviceadvisor-action-DeleteSuiteDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetEndpoint  **
  - **IAM action:**  [iotdeviceadvisor:GetEndpoint](#list_iotdeviceadvisor-action-GetEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotdeviceadvisor.amazonaws.com / **Access level:** Write

- **   GetSuiteDefinition  **
  - **IAM action:**  [iotdeviceadvisor:GetSuiteDefinition](#list_iotdeviceadvisor-action-GetSuiteDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSuiteRun  **
  - **IAM action:**  [iotdeviceadvisor:GetSuiteRun](#list_iotdeviceadvisor-action-GetSuiteRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSuiteRunReport  **
  - **IAM action:**  [iotdeviceadvisor:GetSuiteRunReport](#list_iotdeviceadvisor-action-GetSuiteRunReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSuiteDefinitions  **
  - **IAM action:**  [iotdeviceadvisor:ListSuiteDefinitions](#list_iotdeviceadvisor-action-ListSuiteDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSuiteRuns  **
  - **IAM action:**  [iotdeviceadvisor:ListSuiteRuns](#list_iotdeviceadvisor-action-ListSuiteRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [iotdeviceadvisor:ListTagsForResource](#list_iotdeviceadvisor-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartSuiteRun  **
  - **IAM action:**  [iotdeviceadvisor:StartSuiteRun](#list_iotdeviceadvisor-action-StartSuiteRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotdeviceadvisor:TagResource](#list_iotdeviceadvisor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotdeviceadvisor.amazonaws.com / **Access level:** Write

- **   StopSuiteRun  **
  - **IAM action:**  [iotdeviceadvisor:StopSuiteRun](#list_iotdeviceadvisor-action-StopSuiteRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [iotdeviceadvisor:TagResource](#list_iotdeviceadvisor-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [iotdeviceadvisor:UntagResource](#list_iotdeviceadvisor-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateSuiteDefinition  **
  - **IAM action:**  [iotdeviceadvisor:UpdateSuiteDefinition](#list_iotdeviceadvisor-action-UpdateSuiteDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotdeviceadvisor.amazonaws.com / **Access level:** Write



## Actions defined by AWS IoT Core Device Advisor
<a name="list_iotdeviceadvisor-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateSuiteDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_CreateSuiteDefinition.html)  **
  - **Description:** Grants permission to create a suite definition
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotdeviceadvisor-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotdeviceadvisor-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteSuiteDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_DeleteSuiteDefinition.html)  **
  - **Description:** Grants permission to delete a suite definition
  - **Resource types (\*required):** [Suitedefinition\*](#list_iotdeviceadvisor-resource-Suitedefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetEndpoint](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetEndpoint.html)  **
  - **Description:** Grants permission to get a Device Advisor endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSuiteDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetSuiteDefinition.html)  **
  - **Description:** Grants permission to get a suite definition
  - **Resource types (\*required):** [Suitedefinition\*](#list_iotdeviceadvisor-resource-Suitedefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSuiteRun](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetSuiteRun.html)  **
  - **Description:** Grants permission to get a suite run
  - **Resource types (\*required):** [Suiterun\*](#list_iotdeviceadvisor-resource-Suiterun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSuiteRunReport](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetSuiteRunReport.html)  **
  - **Description:** Grants permission to get the qualification report for a suite run
  - **Resource types (\*required):** [Suiterun\*](#list_iotdeviceadvisor-resource-Suiterun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSuiteDefinitions](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListSuiteDefinitions.html)  **
  - **Description:** Grants permission to list suite definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSuiteRuns](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListSuiteRuns.html)  **
  - **Description:** Grants permission to list suite runs
  - **Resource types (\*required):** [Suitedefinition\*](#list_iotdeviceadvisor-resource-Suitedefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags (metadata) assigned to a resource
  - **Resource types (\*required):** [Suitedefinition](#list_iotdeviceadvisor-resource-Suitedefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Suiterun](#list_iotdeviceadvisor-resource-Suiterun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartSuiteRun](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_StartSuiteRun.html)  **
  - **Description:** Grants permission to start a suite run
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotdeviceadvisor-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotdeviceadvisor-aws_TagKeys)
  - **Access level:** Write

- **   [StopSuiteRun](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_StopSuiteRun.html)  **
  - **Description:** Grants permission to stop a suite run
  - **Resource types (\*required):** [Suiterun\*](#list_iotdeviceadvisor-resource-Suiterun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_TagResource.html)  **
  - **Description:** Grants permission to add to or modify the tags of the given resource. Tags are metadata which can be used to manage a resource
  - **Resource types (\*required):** [Suitedefinition](#list_iotdeviceadvisor-resource-Suitedefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotdeviceadvisor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotdeviceadvisor-aws_TagKeys)
  - **Resource types (\*required):** [Suiterun](#list_iotdeviceadvisor-resource-Suiterun) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotdeviceadvisor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotdeviceadvisor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_UntagResource.html)  **
  - **Description:** Grants permission to remove the given tags (metadata) from a resource
  - **Resource types (\*required):** [Suitedefinition](#list_iotdeviceadvisor-resource-Suitedefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotdeviceadvisor-aws_TagKeys)
  - **Resource types (\*required):** [Suiterun](#list_iotdeviceadvisor-resource-Suiterun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotdeviceadvisor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateSuiteDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_UpdateSuiteDefinition.html)  **
  - **Description:** Grants permission to update a suite definition
  - **Resource types (\*required):** [Suitedefinition\*](#list_iotdeviceadvisor-resource-Suitedefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS IoT Core Device Advisor
<a name="list_iotdeviceadvisor-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Suitedefinition](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-create-suite-definition)  | arn:${Partition}:iotdeviceadvisor:${Region}:${Account}:suitedefinition/${SuiteDefinitionId} | [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_) | 
|  [Suiterun](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-start-suite-run)  | arn:${Partition}:iotdeviceadvisor:${Region}:${Account}:suiterun/${SuiteDefinitionId}/${SuiteRunId} | [aws:ResourceTag/${TagKey}](#list_iotdeviceadvisor-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS IoT Core Device Advisor
<a name="list_iotdeviceadvisor-policy-keys"></a>

AWS IoT Core Device Advisor defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 