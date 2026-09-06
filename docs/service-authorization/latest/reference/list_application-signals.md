

# Actions, resources, and condition keys for Amazon CloudWatch Application Signals
<a name="list_application-signals"></a>

Amazon CloudWatch Application Signals (service prefix: `application-signals`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/application-signals/application-signals.json) for this service.

**Topics**
+ [API operations defined by Amazon CloudWatch Application Signals](#list_application-signals-operations)
+ [Actions defined by Amazon CloudWatch Application Signals](#list_application-signals-actions-as-permissions)
+ [Permission-only actions for Amazon CloudWatch Application Signals](#list_application-signals-permission-only-actions)
+ [Resource types defined by Amazon CloudWatch Application Signals](#list_application-signals-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch Application Signals](#list_application-signals-policy-keys)

## API operations defined by Amazon CloudWatch Application Signals
<a name="list_application-signals-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_application-signals-actions-as-permissions).




- **   BatchDeleteInstrumentationConfigurations  **
  - **IAM action:**  [application-signals:BatchDeleteInstrumentationConfigurations](#list_application-signals-action-BatchDeleteInstrumentationConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetServiceLevelObjectiveBudgetReport  **
  - **IAM action:**  [application-signals:BatchGetServiceLevelObjectiveBudgetReport](#list_application-signals-action-BatchGetServiceLevelObjectiveBudgetReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchUpdateExclusionWindows  **
  - **IAM action:**  [application-signals:BatchUpdateExclusionWindows](#list_application-signals-action-BatchUpdateExclusionWindows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateInstrumentationConfiguration  **
  - **IAM action:**  [application-signals:CreateInstrumentationConfiguration](#list_application-signals-action-CreateInstrumentationConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [application-signals:TagResource](#list_application-signals-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServiceLevelObjective  **
  - **IAM action:**  [application-signals:CreateServiceLevelObjective](#list_application-signals-action-CreateServiceLevelObjective)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [application-signals:TagResource](#list_application-signals-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteGroupingConfiguration  **
  - **IAM action:**  [application-signals:DeleteGroupingConfiguration](#list_application-signals-action-DeleteGroupingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInstrumentationConfiguration  **
  - **IAM action:**  [application-signals:DeleteInstrumentationConfiguration](#list_application-signals-action-DeleteInstrumentationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceLevelObjective  **
  - **IAM action:**  [application-signals:DeleteServiceLevelObjective](#list_application-signals-action-DeleteServiceLevelObjective) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetInstrumentationConfiguration  **
  - **IAM action:**  [application-signals:GetInstrumentationConfiguration](#list_application-signals-action-GetInstrumentationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInstrumentationConfigurationStatus  **
  - **IAM action:**  [application-signals:GetInstrumentationConfigurationStatus](#list_application-signals-action-GetInstrumentationConfigurationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetService  **
  - **IAM action:**  [application-signals:GetService](#list_application-signals-action-GetService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceLevelObjective  **
  - **IAM action:**  [application-signals:GetServiceLevelObjective](#list_application-signals-action-GetServiceLevelObjective) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAuditFindings  **
  - **IAM action:**  [application-signals:GetServiceLevelObjective](#list_application-signals-action-GetServiceLevelObjective)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [application-signals:ListAuditFindings](#list_application-signals-action-ListAuditFindings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [application-signals:ListServiceLevelObjectives](#list_application-signals-action-ListServiceLevelObjectives)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListEntityEvents  **
  - **IAM action:**  [application-signals:ListEntityEvents](#list_application-signals-action-ListEntityEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroupingAttributeDefinitions  **
  - **IAM action:**  [application-signals:ListGroupingAttributeDefinitions](#list_application-signals-action-ListGroupingAttributeDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstrumentationConfigurations  **
  - **IAM action:**  [application-signals:ListInstrumentationConfigurations](#list_application-signals-action-ListInstrumentationConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceDependencies  **
  - **IAM action:**  [application-signals:ListServiceDependencies](#list_application-signals-action-ListServiceDependencies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceDependents  **
  - **IAM action:**  [application-signals:ListServiceDependents](#list_application-signals-action-ListServiceDependents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceLevelObjectiveExclusionWindows  **
  - **IAM action:**  [application-signals:ListServiceLevelObjectiveExclusionWindows](#list_application-signals-action-ListServiceLevelObjectiveExclusionWindows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceLevelObjectives  **
  - **IAM action:**  [application-signals:ListServiceLevelObjectives](#list_application-signals-action-ListServiceLevelObjectives) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceOperations  **
  - **IAM action:**  [application-signals:ListServiceOperations](#list_application-signals-action-ListServiceOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceStates  **
  - **IAM action:**  [application-signals:ListServiceStates](#list_application-signals-action-ListServiceStates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServices  **
  - **IAM action:**  [application-signals:ListServices](#list_application-signals-action-ListServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [application-signals:ListTagsForResource](#list_application-signals-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutGroupingConfiguration  **
  - **IAM action:**  [application-signals:PutGroupingConfiguration](#list_application-signals-action-PutGroupingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReportInstrumentationConfigurationStatus  **
  - **IAM action:**  [application-signals:ReportInstrumentationConfigurationStatus](#list_application-signals-action-ReportInstrumentationConfigurationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDiscovery  **
  - **IAM action:**  [application-signals:StartDiscovery](#list_application-signals-action-StartDiscovery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [application-signals:TagResource](#list_application-signals-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [application-signals:UntagResource](#list_application-signals-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateServiceLevelObjective  **
  - **IAM action:**  [application-signals:UpdateServiceLevelObjective](#list_application-signals-action-UpdateServiceLevelObjective) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon CloudWatch Application Signals
<a name="list_application-signals-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchDeleteInstrumentationConfigurations](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchDeleteInstrumentationConfigurations.html)  **
  - **Description:** Grants permission to batch delete instrumentation configurations
  - **Resource types (\*required):** [instrumentationConfig\*](#list_application-signals-resource-instrumentationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetServiceLevelObjectiveBudgetReport](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.html)  **
  - **Description:** Grants permission to batch retrieve a service level objective budget report
  - **Resource types (\*required):** [slo\*](#list_application-signals-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchUpdateExclusionWindows](API_BatchUpdateExclusionWindows.html)  **
  - **Description:** Grants permission to add or remove exclusion windows from Amazon CloudWatch SLOs
  - **Resource types (\*required):** [slo\*](#list_application-signals-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInstrumentationConfiguration](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CreateInstrumentationConfiguration.html)  **
  - **Description:** Grants permission to create an instrumentation configuration for dynamic instrumentation
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_application-signals-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_application-signals-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CreateServiceLevelObjective.html)  **
  - **Description:** Grants permission to create a service level objective
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_application-signals-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_application-signals-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteGroupingConfiguration](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteGroupingConfiguration.html)  **
  - **Description:** Grants permission to delete a grouping configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInstrumentationConfiguration](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteInstrumentationConfiguration.html)  **
  - **Description:** Grants permission to delete an instrumentation configuration
  - **Resource types (\*required):** [instrumentationConfig\*](#list_application-signals-resource-instrumentationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteServiceLevelObjective.html)  **
  - **Description:** Grants permission to delete a service level objective
  - **Resource types (\*required):** [slo\*](#list_application-signals-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetInstrumentationConfiguration](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetInstrumentationConfiguration.html)  **
  - **Description:** Grants permission to retrieve an instrumentation configuration
  - **Resource types (\*required):** [instrumentationConfig\*](#list_application-signals-resource-instrumentationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInstrumentationConfigurationStatus](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetInstrumentationConfigurationStatus.html)  **
  - **Description:** Grants permission to retrieve the status history of an instrumentation configuration
  - **Resource types (\*required):** [instrumentationConfig\*](#list_application-signals-resource-instrumentationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetService](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetService.html)  **
  - **Description:** Grants permission to retrieve information about a service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetServiceLevelObjective.html)  **
  - **Description:** Grants permission to retrieve information about service level objective
  - **Resource types (\*required):** [slo\*](#list_application-signals-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAuditFindings](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListAuditFindings.html)  **
  - **Description:** Grants permission to list service auditing results
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEntityEvents](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListEntityEvents.html)  **
  - **Description:** Grants permission to list events for an entity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGroupingAttributeDefinitions](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListGroupingAttributeDefinitions.html)  **
  - **Description:** Grants permission to list grouping attribute configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInstrumentationConfigurations](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListInstrumentationConfigurations.html)  **
  - **Description:** Grants permission to list instrumentation configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListObservedEntities](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application_Signals_Permissions.html)  **
  - **Description:** Grants permission to list entities associated with other entities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceDependencies](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependencies.html)  **
  - **Description:** Grants permission to list service dependencies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListServiceDependents](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependents.html)  **
  - **Description:** Grants permission to list service dependents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListServiceLevelObjectiveExclusionWindows](API_ListServiceLevelObjectiveExclusionWindows.html)  **
  - **Description:** Grants permission to list exclusion windows for an Amazon CloudWatch SLO
  - **Resource types (\*required):** [slo\*](#list_application-signals-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServiceLevelObjectives](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceLevelObjectives.html)  **
  - **Description:** Grants permission to list service level objectives
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceOperations](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceOperations.html)  **
  - **Description:** Grants permission to list service operations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListServiceStates](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceStates.html)  **
  - **Description:** Grants permission to list service states
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServices](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServices.html)  **
  - **Description:** Grants permission to list services
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an Amazon CloudWatch Application Signals resource
  - **Resource types (\*required):** [instrumentationConfig](#list_application-signals-resource-instrumentationConfig) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [slo](#list_application-signals-resource-slo) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutGroupingConfiguration](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_PutGroupingConfiguration.html)  **
  - **Description:** Grants permission to create or update a grouping configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ReportInstrumentationConfigurationStatus](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ReportInstrumentationConfigurationStatus.html)  **
  - **Description:** Grants permission to report the status of instrumentation configurations
  - **Resource types (\*required):** [instrumentationConfig\*](#list_application-signals-resource-instrumentationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDiscovery](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_StartDiscovery.html)  **
  - **Description:** Grants permission to enable CloudWatch discovery
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to an Amazon CloudWatch Application Signals resource
  - **Resource types (\*required):** [instrumentationConfig](#list_application-signals-resource-instrumentationConfig) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_application-signals-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_application-signals-aws_TagKeys)
  - **Resource types (\*required):** [slo](#list_application-signals-resource-slo) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_application-signals-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_application-signals-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from an Amazon CloudWatch Application Signals resource
  - **Resource types (\*required):** [instrumentationConfig](#list_application-signals-resource-instrumentationConfig) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_application-signals-aws_TagKeys)
  - **Resource types (\*required):** [slo](#list_application-signals-resource-slo) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_application-signals-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UpdateServiceLevelObjective.html)  **
  - **Description:** Grants permission to update a service level objective
  - **Resource types (\*required):** [slo\*](#list_application-signals-resource-slo)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon CloudWatch Application Signals
<a name="list_application-signals-permission-only-actions"></a>

The following actions are defined by Amazon CloudWatch Application Signals but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [Link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.html#CloudWatch-Unified-Cross-Account-Setup-permissions)  | Grants permission to share Application Signals resources with a monitoring account |  |   | Write | 

## Resource types defined by Amazon CloudWatch Application Signals
<a name="list_application-signals-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [instrumentationConfig](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_CreateInstrumentationConfiguration.html)  | arn:${Partition}:application-signals:${Region}:${Account}:instrumentationConfig/${Service}/${Environment}/${SignalType}/${LocationHash} | [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_) | 
|  [slo](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html)  | arn:${Partition}:application-signals:${Region}:${Account}:slo/${SloName} | [aws:ResourceTag/${TagKey}](#list_application-signals-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch Application Signals
<a name="list_application-signals-policy-keys"></a>

Amazon CloudWatch Application Signals defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 