

# Actions, resources, and condition keys for AWS Systems Manager Incident Manager
<a name="list_ssm-incidents"></a>

AWS Systems Manager Incident Manager (service prefix: `ssm-incidents`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/incident-manager/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/incident-manager/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ssm-incidents/ssm-incidents.json) for this service.

**Topics**
+ [API operations defined by AWS Systems Manager Incident Manager](#list_ssm-incidents-operations)
+ [Actions defined by AWS Systems Manager Incident Manager](#list_ssm-incidents-actions-as-permissions)
+ [Resource types defined by AWS Systems Manager Incident Manager](#list_ssm-incidents-resources-for-iam-policies)
+ [Condition keys for AWS Systems Manager Incident Manager](#list_ssm-incidents-policy-keys)

## API operations defined by AWS Systems Manager Incident Manager
<a name="list_ssm-incidents-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ssm-incidents-actions-as-permissions).




- **   BatchGetIncidentFindings  **
  - **IAM action:**  [ssm-incidents:BatchGetIncidentFindings](#list_ssm-incidents-action-BatchGetIncidentFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateReplicationSet  **
  - **IAM action:**  [ssm-incidents:CreateReplicationSet](#list_ssm-incidents-action-CreateReplicationSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ssm-incidents:TagResource](#list_ssm-incidents-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateResponsePlan  **
  - **IAM action:**  [ssm-incidents:CreateResponsePlan](#list_ssm-incidents-action-CreateResponsePlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ssm-incidents:TagResource](#list_ssm-incidents-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm-incidents.amazonaws.com / **Access level:** Write

- **   CreateTimelineEvent  **
  - **IAM action:**  [ssm-incidents:CreateTimelineEvent](#list_ssm-incidents-action-CreateTimelineEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIncidentRecord  **
  - **IAM action:**  [ssm-incidents:DeleteIncidentRecord](#list_ssm-incidents-action-DeleteIncidentRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicationSet  **
  - **IAM action:**  [ssm-incidents:DeleteReplicationSet](#list_ssm-incidents-action-DeleteReplicationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [ssm-incidents:DeleteResourcePolicy](#list_ssm-incidents-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteResponsePlan  **
  - **IAM action:**  [ssm-incidents:DeleteResponsePlan](#list_ssm-incidents-action-DeleteResponsePlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTimelineEvent  **
  - **IAM action:**  [ssm-incidents:DeleteTimelineEvent](#list_ssm-incidents-action-DeleteTimelineEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetIncidentRecord  **
  - **IAM action:**  [ssm-incidents:GetIncidentRecord](#list_ssm-incidents-action-GetIncidentRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReplicationSet  **
  - **IAM action:**  [ssm-incidents:GetReplicationSet](#list_ssm-incidents-action-GetReplicationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicies  **
  - **IAM action:**  [ssm-incidents:GetResourcePolicies](#list_ssm-incidents-action-GetResourcePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResponsePlan  **
  - **IAM action:**  [ssm-incidents:GetResponsePlan](#list_ssm-incidents-action-GetResponsePlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTimelineEvent  **
  - **IAM action:**  [ssm-incidents:GetTimelineEvent](#list_ssm-incidents-action-GetTimelineEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListIncidentFindings  **
  - **IAM action:**  [ssm-incidents:ListIncidentFindings](#list_ssm-incidents-action-ListIncidentFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIncidentRecords  **
  - **IAM action:**  [ssm-incidents:ListIncidentRecords](#list_ssm-incidents-action-ListIncidentRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRelatedItems  **
  - **IAM action:**  [ssm-incidents:ListRelatedItems](#list_ssm-incidents-action-ListRelatedItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReplicationSets  **
  - **IAM action:**  [ssm-incidents:ListReplicationSets](#list_ssm-incidents-action-ListReplicationSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResponsePlans  **
  - **IAM action:**  [ssm-incidents:ListResponsePlans](#list_ssm-incidents-action-ListResponsePlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ssm-incidents:ListTagsForResource](#list_ssm-incidents-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTimelineEvents  **
  - **IAM action:**  [ssm-incidents:ListTimelineEvents](#list_ssm-incidents-action-ListTimelineEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutResourcePolicy  **
  - **IAM action:**  [ssm-incidents:PutResourcePolicy](#list_ssm-incidents-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   StartIncident  **
  - **IAM action:**  [ssm-incidents:StartIncident](#list_ssm-incidents-action-StartIncident) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ssm-incidents:TagResource](#list_ssm-incidents-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ssm-incidents:UntagResource](#list_ssm-incidents-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDeletionProtection  **
  - **IAM action:**  [ssm-incidents:UpdateDeletionProtection](#list_ssm-incidents-action-UpdateDeletionProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIncidentRecord  **
  - **IAM action:**  [ssm-incidents:UpdateIncidentRecord](#list_ssm-incidents-action-UpdateIncidentRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRelatedItems  **
  - **IAM action:**  [ssm-incidents:UpdateRelatedItems](#list_ssm-incidents-action-UpdateRelatedItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReplicationSet  **
  - **IAM action:**  [ssm-incidents:UpdateReplicationSet](#list_ssm-incidents-action-UpdateReplicationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResponsePlan  **
  - **IAM action:**  [ssm-incidents:TagResource](#list_ssm-incidents-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm-incidents:UpdateResponsePlan](#list_ssm-incidents-action-UpdateResponsePlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm-incidents.amazonaws.com / **Access level:** Write

- **   UpdateTimelineEvent  **
  - **IAM action:**  [ssm-incidents:UpdateTimelineEvent](#list_ssm-incidents-action-UpdateTimelineEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Systems Manager Incident Manager
<a name="list_ssm-incidents-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetIncidentFindings](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_BatchGetIncidentFindings.html)  **
  - **Description:** Grants permission to retrieve details about specified findings for an incident record
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateReplicationSet](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_CreateReplicationSet.html)  **
  - **Description:** Grants permission to create a replication set
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-incidents-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ssm-incidents-aws_TagKeys)
  - **Access level:** Write

- **   [CreateResponsePlan](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_CreateResponsePlan.html)  **
  - **Description:** Grants permission to create a response plan
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-incidents-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ssm-incidents-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTimelineEvent](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_CreateTimelineEvent.html)  **
  - **Description:** Grants permission to create a timeline event for an incident record
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIncidentRecord](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_DeleteIncidentRecord.html)  **
  - **Description:** Grants permission to delete an incident record
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReplicationSet](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_DeleteReplicationSet.html)  **
  - **Description:** Grants permission to delete a replication set
  - **Resource types (\*required):** [replication-set\*](#list_ssm-incidents-resource-replication-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete resource policy from a response plan
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteResponsePlan](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_DeleteResponsePlan.html)  **
  - **Description:** Grants permission to delete a response plan
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTimelineEvent](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_DeleteTimelineEvent.html)  **
  - **Description:** Grants permission to delete a timeline event
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetIncidentRecord](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_GetIncidentRecord.html)  **
  - **Description:** Grants permission to view the contents of an incident record
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReplicationSet](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_GetReplicationSet.html)  **
  - **Description:** Grants permission to view the replication set
  - **Resource types (\*required):** [replication-set\*](#list_ssm-incidents-resource-replication-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicies](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_GetResourcePolicies.html)  **
  - **Description:** Grants permission to view resource policies of a response plan
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResponsePlan](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_GetResponsePlan.html)  **
  - **Description:** Grants permission to view the contents of a specified response plan
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTimelineEvent](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_GetTimelineEvent.html)  **
  - **Description:** Grants permission to view a timeline event
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListIncidentFindings](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListIncidentFindings.html)  **
  - **Description:** Grants permission to list findings for an incident record
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIncidentRecords](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListIncidentRecords.html)  **
  - **Description:** Grants permission to list the contents of all incident records
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRelatedItems](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListRelatedItems.html)  **
  - **Description:** Grants permission to list related items of an incident record
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReplicationSets](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListReplicationSets.html)  **
  - **Description:** Grants permission to list all replication sets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResponsePlans](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListResponsePlans.html)  **
  - **Description:** Grants permission to list all response plans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to view a list of resource tags for a specified resource
  - **Resource types (\*required):** [incident-record](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [replication-set](#list_ssm-incidents-resource-replication-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTimelineEvents](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListTimelineEvents.html)  **
  - **Description:** Grants permission to list all timeline events for an incident record
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutResourcePolicy](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to put resource policy on a response plan
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [StartIncident](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_StartIncident.html)  **
  - **Description:** Grants permission to start a new incident using a response plan
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a response plan
  - **Resource types (\*required):** [incident-record](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-incidents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-incidents-aws_TagKeys)
  - **Resource types (\*required):** [replication-set](#list_ssm-incidents-resource-replication-set) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-incidents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-incidents-aws_TagKeys)
  - **Resource types (\*required):** [response-plan](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-incidents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-incidents-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a response plan
  - **Resource types (\*required):** [incident-record](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-incidents-aws_TagKeys)
  - **Resource types (\*required):** [replication-set](#list_ssm-incidents-resource-replication-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-incidents-aws_TagKeys)
  - **Resource types (\*required):** [response-plan](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-incidents-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDeletionProtection](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_UpdateDeletionProtection.html)  **
  - **Description:** Grants permission to update replication set deletion protection
  - **Resource types (\*required):** [replication-set\*](#list_ssm-incidents-resource-replication-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIncidentRecord](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_UpdateIncidentRecord.html)  **
  - **Description:** Grants permission to update the contents of an incident record
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRelatedItems](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_UpdateRelatedItems.html)  **
  - **Description:** Grants permission to update related items of an incident record
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReplicationSet](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_UpdateReplicationSet.html)  **
  - **Description:** Grants permission to update a replication set
  - **Resource types (\*required):** [replication-set\*](#list_ssm-incidents-resource-replication-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateResponsePlan](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_UpdateResponsePlan.html)  **
  - **Description:** Grants permission to update the contents of a response plan
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-incidents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-incidents-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateTimelineEvent](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_UpdateTimelineEvent.html)  **
  - **Description:** Grants permission to update a timeline event
  - **Resource types (\*required):** [incident-record\*](#list_ssm-incidents-resource-incident-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [response-plan\*](#list_ssm-incidents-resource-response-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Systems Manager Incident Manager
<a name="list_ssm-incidents-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [incident-record](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html)  | arn:${Partition}:ssm-incidents::${Account}:incident-record/${ResponsePlan}/${IncidentRecord} | [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_) | 
|  [replication-set](https://docs.aws.amazon.com/incident-manager/latest/userguide/disaster-recovery-resiliency.html#replication)  | arn:${Partition}:ssm-incidents::${Account}:replication-set/${ReplicationSet} | [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_) | 
|  [response-plan](https://docs.aws.amazon.com/incident-manager/latest/userguide/response-plans.html)  | arn:${Partition}:ssm-incidents::${Account}:response-plan/${ResponsePlan} | [aws:ResourceTag/${TagKey}](#list_ssm-incidents-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Systems Manager Incident Manager
<a name="list_ssm-incidents-policy-keys"></a>

AWS Systems Manager Incident Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 