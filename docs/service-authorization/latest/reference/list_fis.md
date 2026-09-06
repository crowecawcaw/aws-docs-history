

# Actions, resources, and condition keys for AWS Fault Injection Service
<a name="list_fis"></a>

AWS Fault Injection Service (service prefix: `fis`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/fis/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/fis/latest/userguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/fis/fis.json) for this service.

**Topics**
+ [API operations defined by AWS Fault Injection Service](#list_fis-operations)
+ [Actions defined by AWS Fault Injection Service](#list_fis-actions-as-permissions)
+ [Permission-only actions for AWS Fault Injection Service](#list_fis-permission-only-actions)
+ [Resource types defined by AWS Fault Injection Service](#list_fis-resources-for-iam-policies)
+ [Condition keys for AWS Fault Injection Service](#list_fis-policy-keys)

## API operations defined by AWS Fault Injection Service
<a name="list_fis-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_fis-actions-as-permissions).




- **   CreateExperimentTemplate  **
  - **IAM action:**  [fis:CreateExperimentTemplate](#list_fis-action-CreateExperimentTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fis:TagResource](#list_fis-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** fis.amazonaws.com / **Access level:** Write

- **   CreateTargetAccountConfiguration  **
  - **IAM action:**  [fis:CreateTargetAccountConfiguration](#list_fis-action-CreateTargetAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExperimentTemplate  **
  - **IAM action:**  [fis:DeleteExperimentTemplate](#list_fis-action-DeleteExperimentTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTargetAccountConfiguration  **
  - **IAM action:**  [fis:DeleteTargetAccountConfiguration](#list_fis-action-DeleteTargetAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAction  **
  - **IAM action:**  [fis:GetAction](#list_fis-action-GetAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExperiment  **
  - **IAM action:**  [fis:GetExperiment](#list_fis-action-GetExperiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExperimentTargetAccountConfiguration  **
  - **IAM action:**  [fis:GetExperimentTargetAccountConfiguration](#list_fis-action-GetExperimentTargetAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExperimentTemplate  **
  - **IAM action:**  [fis:GetExperimentTemplate](#list_fis-action-GetExperimentTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSafetyLever  **
  - **IAM action:**  [fis:GetSafetyLever](#list_fis-action-GetSafetyLever) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTargetAccountConfiguration  **
  - **IAM action:**  [fis:GetTargetAccountConfiguration](#list_fis-action-GetTargetAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTargetResourceType  **
  - **IAM action:**  [fis:GetTargetResourceType](#list_fis-action-GetTargetResourceType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListActions  **
  - **IAM action:**  [fis:ListActions](#list_fis-action-ListActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExperimentResolvedTargets  **
  - **IAM action:**  [fis:ListExperimentResolvedTargets](#list_fis-action-ListExperimentResolvedTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExperimentTargetAccountConfigurations  **
  - **IAM action:**  [fis:ListExperimentTargetAccountConfigurations](#list_fis-action-ListExperimentTargetAccountConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExperimentTemplates  **
  - **IAM action:**  [fis:ListExperimentTemplates](#list_fis-action-ListExperimentTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExperiments  **
  - **IAM action:**  [fis:ListExperiments](#list_fis-action-ListExperiments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [fis:ListTagsForResource](#list_fis-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTargetAccountConfigurations  **
  - **IAM action:**  [fis:ListTargetAccountConfigurations](#list_fis-action-ListTargetAccountConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTargetResourceTypes  **
  - **IAM action:**  [fis:ListTargetResourceTypes](#list_fis-action-ListTargetResourceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartExperiment  **
  - **IAM action:**  [fis:StartExperiment](#list_fis-action-StartExperiment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fis:TagResource](#list_fis-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StopExperiment  **
  - **IAM action:**  [fis:StopExperiment](#list_fis-action-StopExperiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [fis:TagResource](#list_fis-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [fis:UntagResource](#list_fis-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateExperimentTemplate  **
  - **IAM action:**  [fis:UpdateExperimentTemplate](#list_fis-action-UpdateExperimentTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** fis.amazonaws.com / **Access level:** Write

- **   UpdateSafetyLeverState  **
  - **IAM action:**  [fis:UpdateSafetyLeverState](#list_fis-action-UpdateSafetyLeverState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTargetAccountConfiguration  **
  - **IAM action:**  [fis:UpdateTargetAccountConfiguration](#list_fis-action-UpdateTargetAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Fault Injection Service
<a name="list_fis-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateExperimentTemplate](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplate.html)  **
  - **Description:** Grants permission to create an AWS FIS experiment template
  - **Resource types (\*required):** [action\*](#list_fis-resource-action) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Resource types (\*required):** [experiment-template\*](#list_fis-resource-experiment-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateTargetAccountConfiguration.html)  **
  - **Description:** Grants permission to create an AWS FIS target account configuration
  - **Resource types (\*required):** [experiment-template\*](#list_fis-resource-experiment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExperimentTemplate](https://docs.aws.amazon.com/fis/latest/APIReference/API_DeleteExperimentTemplate.html)  **
  - **Description:** Grants permission to delete the AWS FIS experiment template
  - **Resource types (\*required):** [experiment-template\*](#list_fis-resource-experiment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_DeleteTargetAccountConfiguration.html)  **
  - **Description:** Grants permission to delete an AWS FIS target account configuration
  - **Resource types (\*required):** [experiment-template\*](#list_fis-resource-experiment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAction](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetAction.html)  **
  - **Description:** Grants permission to retrieve an AWS FIS action
  - **Resource types (\*required):** [action\*](#list_fis-resource-action)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExperiment](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetExperiment.html)  **
  - **Description:** Grants permission to retrieve an AWS FIS experiment
  - **Resource types (\*required):** [experiment\*](#list_fis-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExperimentTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetExperimentTargetAccountConfiguration.html)  **
  - **Description:** Grants permission to retrieve an AWS FIS target account configuration for an AWS FIS experiment
  - **Resource types (\*required):** [experiment\*](#list_fis-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExperimentTemplate](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetExperimentTemplate.html)  **
  - **Description:** Grants permission to retrieve an AWS FIS Experiment Template
  - **Resource types (\*required):** [experiment-template\*](#list_fis-resource-experiment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSafetyLever](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetSafetyLever.html)  **
  - **Description:** Grants permission to get information about the safety lever
  - **Resource types (\*required):** [safety-lever\*](#list_fis-resource-safety-lever)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetTargetAccountConfiguration.html)  **
  - **Description:** Grants permission to retrieve an AWS FIS target account configuration for an AWS FIS experiment template
  - **Resource types (\*required):** [experiment-template\*](#list_fis-resource-experiment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTargetResourceType](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetTargetResourceType.html)  **
  - **Description:** Grants permission to get information about the specified resource type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListActions](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListActions.html)  **
  - **Description:** Grants permission to list all available AWS FIS actions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExperimentResolvedTargets](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperimentResolvedTargets.html)  **
  - **Description:** Grants permission to list resolved targets for AWS FIS experiments
  - **Resource types (\*required):** [experiment\*](#list_fis-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExperimentTargetAccountConfigurations](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperimentTargetAccountConfigurations.html)  **
  - **Description:** Grants permission to list target account configurations for AWS FIS experiments
  - **Resource types (\*required):** [experiment\*](#list_fis-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExperimentTemplates](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperimentTemplates.html)  **
  - **Description:** Grants permission to list all available AWS FIS experiment templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExperiments](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperiments.html)  **
  - **Description:** Grants permission to list all available AWS FIS experiments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for an AWS FIS resource
  - **Resource types (\*required):** [action](#list_fis-resource-action) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment](#list_fis-resource-experiment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment-template](#list_fis-resource-experiment-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTargetAccountConfigurations](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListTargetAccountConfigurations.html)  **
  - **Description:** Grants permission to list target account configurations for AWS FIS experiment templates
  - **Resource types (\*required):** [experiment-template\*](#list_fis-resource-experiment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTargetResourceTypes](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListTargetResourceTypes.html)  **
  - **Description:** Grants permission to list the resource types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartExperiment](https://docs.aws.amazon.com/fis/latest/APIReference/API_StartExperiment.html)  **
  - **Description:** Grants permission to run an AWS FIS experiment
  - **Resource types (\*required):** [experiment\*](#list_fis-resource-experiment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Resource types (\*required):** [experiment-template\*](#list_fis-resource-experiment-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Access level:** Write

- **   [StopExperiment](https://docs.aws.amazon.com/fis/latest/APIReference/API_StopExperiment.html)  **
  - **Description:** Grants permission to stop an AWS FIS experiment
  - **Resource types (\*required):** [experiment\*](#list_fis-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/fis/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag AWS FIS resources
  - **Resource types (\*required):** [action](#list_fis-resource-action) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Resource types (\*required):** [experiment](#list_fis-resource-experiment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Resource types (\*required):** [experiment-template](#list_fis-resource-experiment-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/fis/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag AWS FIS resources
  - **Resource types (\*required):** [action](#list_fis-resource-action) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Resource types (\*required):** [experiment](#list_fis-resource-experiment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Resource types (\*required):** [experiment-template](#list_fis-resource-experiment-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateExperimentTemplate](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateExperimentTemplate.html)  **
  - **Description:** Grants permission to update the specified AWS FIS experiment template
  - **Resource types (\*required):** [action](#list_fis-resource-action) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Resource types (\*required):** [experiment-template\*](#list_fis-resource-experiment-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fis-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateSafetyLeverState](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateSafetyLeverState.html)  **
  - **Description:** Grants permission to update the state of the safety lever
  - **Resource types (\*required):** [safety-lever\*](#list_fis-resource-safety-lever)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateTargetAccountConfiguration.html)  **
  - **Description:** Grants permission to update an AWS FIS target account configuration
  - **Resource types (\*required):** [experiment-template\*](#list_fis-resource-experiment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Fault Injection Service
<a name="list_fis-permission-only-actions"></a>

The following actions are defined by AWS Fault Injection Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [InjectApiInternalError](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#fis-actions-reference-fis)  **
  - **Description:** Grants permission to inject an API internal error on the provided AWS service from an FIS Experiment
  - **Resource types (\*required):** [experiment\*](#list_fis-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[fis:Operations](#list_fis-fis_Operations)<br />[fis:Percentage](#list_fis-fis_Percentage)<br />[fis:Service](#list_fis-fis_Service)<br />[fis:Targets](#list_fis-fis_Targets)
  - **Access level:** Write

- **   [InjectApiThrottleError](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#fis-actions-reference-fis)  **
  - **Description:** Grants permission to inject an API throttle error on the provided AWS service from an FIS Experiment
  - **Resource types (\*required):** [experiment\*](#list_fis-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[fis:Operations](#list_fis-fis_Operations)<br />[fis:Percentage](#list_fis-fis_Percentage)<br />[fis:Service](#list_fis-fis_Service)<br />[fis:Targets](#list_fis-fis_Targets)
  - **Access level:** Write

- **   [InjectApiUnavailableError](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#fis-actions-reference-fis)  **
  - **Description:** Grants permission to inject an API unavailable error on the provided AWS service from an FIS Experiment
  - **Resource types (\*required):** [experiment\*](#list_fis-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_)<br />[fis:Operations](#list_fis-fis_Operations)<br />[fis:Percentage](#list_fis-fis_Percentage)<br />[fis:Service](#list_fis-fis_Service)<br />[fis:Targets](#list_fis-fis_Targets)
  - **Access level:** Write



## Resource types defined by AWS Fault Injection Service
<a name="list_fis-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [action](https://docs.aws.amazon.com/fis/latest/userguide/actions.html)  | arn:${Partition}:fis:${Region}:${Account}:action/${Id} | [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_) | 
|  [experiment](https://docs.aws.amazon.com/fis/latest/userguide/experiments.html)  | arn:${Partition}:fis:${Region}:${Account}:experiment/${Id} | [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_) | 
|  [experiment-template](https://docs.aws.amazon.com/fis/latest/userguide/working-with-templates.html)  | arn:${Partition}:fis:${Region}:${Account}:experiment-template/${Id} | [aws:ResourceTag/${TagKey}](#list_fis-aws_ResourceTag___TagKey_) | 
|  [safety-lever](https://docs.aws.amazon.com/fis/latest/userguide/safety-lever.html)  | arn:${Partition}:fis:${Region}:${Account}:safety-lever/${Id} |   | 

## Condition keys for AWS Fault Injection Service
<a name="list_fis-policy-keys"></a>

AWS Fault Injection Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [fis:Operations](https://docs.aws.amazon.com/fis/latest/userguide/security_iam_service-with-iam.html)  | Filters access by the list of operations on the AWS service that is being affected by the AWS FIS action | ArrayOfString | 
|   [fis:Percentage](https://docs.aws.amazon.com/fis/latest/userguide/security_iam_service-with-iam.html)  | Filters access by the percentage of calls being affected by the AWS FIS action | Numeric | 
|   [fis:Service](https://docs.aws.amazon.com/fis/latest/userguide/security_iam_service-with-iam.html)  | Filters access by the AWS service that is being affected by the AWS FIS action | String | 
|   [fis:Targets](https://docs.aws.amazon.com/fis/latest/userguide/security_iam_service-with-iam.html)  | Filters access by the list of resource ARNs being targeted by the AWS FIS action | ArrayOfString | 