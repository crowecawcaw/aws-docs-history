

# Actions, resources, and condition keys for AWS Assurance
<a name="list_assurance"></a>

AWS Assurance (service prefix: `assurance`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/assurance/latest/userguide/what-is-assurance.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/assurance/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/assurance/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/assurance/assurance.json) for this service.

**Topics**
+ [Actions defined by AWS Assurance](#list_assurance-actions-as-permissions)
+ [Permission-only actions for AWS Assurance](#list_assurance-permission-only-actions)
+ [Resource types defined by AWS Assurance](#list_assurance-resources-for-iam-policies)
+ [Condition keys for AWS Assurance](#list_assurance-policy-keys)

## Actions defined by AWS Assurance
<a name="list_assurance-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptInvitation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_AcceptInvitation.html)  **
  - **Description:** Grants permission to accept an invitation to connect an account to an environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssignPermissionSet](https://docs.aws.amazon.com/assurance/latest/APIReference/API_AssignPermissionSet.html)  **
  - **Description:** Grants permission to assign a permission set to a principal
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetComment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_BatchGetComment.html)  **
  - **Description:** Grants permission to retrieve multiple comments in a single request
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetControl](https://docs.aws.amazon.com/assurance/latest/APIReference/API_BatchGetControl.html)  **
  - **Description:** Grants permission to retrieve multiple controls in a single request
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetTask](https://docs.aws.amazon.com/assurance/latest/APIReference/API_BatchGetTask.html)  **
  - **Description:** Grants permission to retrieve multiple tasks in a single request
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [Chat](https://docs.aws.amazon.com/assurance/latest/APIReference/API_Chat.html)  **
  - **Description:** Grants permission to start a streaming chat session with the AI Governance agent
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateComment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreateComment.html)  **
  - **Description:** Grants permission to add a new comment to a specific control
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateControl](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreateControl.html)  **
  - **Description:** Grants permission to create a leaf control within a custom framework
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateControlGroup](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreateControlGroup.html)  **
  - **Description:** Grants permission to create a control group within a custom framework
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create a new governance environment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_assurance-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_assurance-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEnvironmentConnection](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreateEnvironmentConnection.html)  **
  - **Description:** Grants permission to create an environment connection
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateFramework](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreateFramework.html)  **
  - **Description:** Grants permission to create a custom customer-owned framework
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInvitation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreateInvitation.html)  **
  - **Description:** Grants permission to invite an account to connect to an environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePermissionSet](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreatePermissionSet.html)  **
  - **Description:** Grants permission to create a permission set in an environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateProject](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreateProject.html)  **
  - **Description:** Grants permission to create a project
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteComment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeleteComment.html)  **
  - **Description:** Grants permission to delete a specific comment by its identifying fields
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteControl](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeleteControl.html)  **
  - **Description:** Grants permission to delete a custom control
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteControlGroup](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeleteControlGroup.html)  **
  - **Description:** Grants permission to delete a control group
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete a governance environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironmentConnection](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeleteEnvironmentConnection.html)  **
  - **Description:** Grants permission to delete an environment connection
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEvidence](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeleteEvidence.html)  **
  - **Description:** Grants permission to remove an evidence item
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFramework](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeleteFramework.html)  **
  - **Description:** Grants permission to delete a custom framework
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInvitation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeleteInvitation.html)  **
  - **Description:** Grants permission to delete an invitation or unlink a connected account
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePermissionSet](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeletePermissionSet.html)  **
  - **Description:** Grants permission to delete a permission set
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProject](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeleteProject.html)  **
  - **Description:** Grants permission to delete a project and all its associated resources
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterOrganizationDelegatedAdmin](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeregisterOrganizationDelegatedAdmin.html)  **
  - **Description:** Grants permission to deregister the delegated administrator for AWS Assurance in the caller's organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisableFramework](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DisableFramework.html)  **
  - **Description:** Grants permission to disable a previously enabled framework for a specific project
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableFramework](https://docs.aws.amazon.com/assurance/latest/APIReference/API_EnableFramework.html)  **
  - **Description:** Grants permission to enable a framework for a project
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAnnotation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetAnnotation.html)  **
  - **Description:** Grants permission to retrieve the annotation for a specific piece of evidence
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssessment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetAssessment.html)  **
  - **Description:** Grants permission to retrieve a single assessment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssessmentReportContent](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetAssessmentReportContent.html)  **
  - **Description:** Grants permission to retrieve the content of a prepared assessment report
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssessmentReportExport](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetAssessmentReportExport.html)  **
  - **Description:** Grants permission to retrieve the state of an assessment report export
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChatMessages](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetChatMessages.html)  **
  - **Description:** Grants permission to get messages for a chat session in chronological order
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetComment.html)  **
  - **Description:** Grants permission to retrieve a specific comment by its identifying fields
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetControl](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetControl.html)  **
  - **Description:** Grants permission to retrieve a single leaf control within a framework version
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetControlGroup](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetControlGroup.html)  **
  - **Description:** Grants permission to retrieve a single control group within a framework version
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetControlStatus](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetControlStatus.html)  **
  - **Description:** Grants permission to retrieve the effective compliance status of a control
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetEnvironment.html)  **
  - **Description:** Grants permission to retrieve a governance environment by ARN or domain
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEvidence](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetEvidence.html)  **
  - **Description:** Grants permission to retrieve metadata for an evidence item
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEvidenceContent](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetEvidenceContent.html)  **
  - **Description:** Grants permission to retrieve the content of an evidence item
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFramework](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetFramework.html)  **
  - **Description:** Grants permission to retrieve a framework resource by type and key fields
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvitation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetInvitation.html)  **
  - **Description:** Grants permission to retrieve an invitation
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPermissionSet](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetPermissionSet.html)  **
  - **Description:** Grants permission to retrieve a permission set
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProject](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetProject.html)  **
  - **Description:** Grants permission to retrieve a project
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTask](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetTask.html)  **
  - **Description:** Grants permission to retrieve a specific task by its identifying fields
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAssessmentAnnotations](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListAssessmentAnnotations.html)  **
  - **Description:** Grants permission to list the annotations on one assessment, paginated
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAssessmentJournalRecords](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListAssessmentJournalRecords.html)  **
  - **Description:** Grants permission to list assessment journal records, paginated
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAssessmentOutcomes](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListAssessmentOutcomes.html)  **
  - **Description:** Grants permission to list a compliance score over time
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAssessments](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListAssessments.html)  **
  - **Description:** Grants permission to list assessments, paginated
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListChatSessions](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListChatSessions.html)  **
  - **Description:** Grants permission to list chat sessions for the calling user in a governance environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListComments](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListComments.html)  **
  - **Description:** Grants permission to list comments in a governance environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListConnectionItems](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListConnectionItems.html)  **
  - **Description:** Grants permission to list the contents of an environment connection
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListControlGroups](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListControlGroups.html)  **
  - **Description:** Grants permission to list control groups in a framework version
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListControlResources](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListControlResources.html)  **
  - **Description:** Grants permission to list in-scope resources for a control
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListControls](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListControls.html)  **
  - **Description:** Grants permission to list controls within a control group
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDiscoveredResources](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListDiscoveredResources.html)  **
  - **Description:** Grants permission to list the resources found by a discovery job (paginated)
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEnabledFrameworks](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListEnabledFrameworks.html)  **
  - **Description:** Grants permission to list enabled frameworks for a governance environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEnvironmentConnections](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListEnvironmentConnections.html)  **
  - **Description:** Grants permission to list environment connections in a governance environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEnvironments](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list all governance environments with optional pagination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEvidence](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListEvidence.html)  **
  - **Description:** Grants permission to list evidence items (paginated)
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEvidenceAnnotations](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListEvidenceAnnotations.html)  **
  - **Description:** Grants permission to list the annotations on one version of a piece of evidence within a project, paginated
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFrameworks](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListFrameworks.html)  **
  - **Description:** Grants permission to list frameworks
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListInboundInvitations](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListInboundInvitations.html)  **
  - **Description:** Grants permission to list invitations addressed to the caller's account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListOutboundInvitations](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListOutboundInvitations.html)  **
  - **Description:** Grants permission to list invitations extended from an owned environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPermissionSetAssignments](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListPermissionSetAssignments.html)  **
  - **Description:** Grants permission to list permission set assignments in an environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPermissionSets](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListPermissionSets.html)  **
  - **Description:** Grants permission to list permission sets in an environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListProjects](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListProjects.html)  **
  - **Description:** Grants permission to list all projects within a governance environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListResourcesForControl](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListResourcesForControl.html)  **
  - **Description:** Grants permission to list in-scope resources for a control
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTaskHistory](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListTaskHistory.html)  **
  - **Description:** Grants permission to list task history for a task
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTasks](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListTasks.html)  **
  - **Description:** Grants permission to list all tasks within a governance environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PublishFramework](https://docs.aws.amazon.com/assurance/latest/APIReference/API_PublishFramework.html)  **
  - **Description:** Grants permission to publish a custom framework
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutControlStatusOverride](https://docs.aws.amazon.com/assurance/latest/APIReference/API_PutControlStatusOverride.html)  **
  - **Description:** Grants permission to declare or remove an applicability override on a control or requirement
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutEvidence](https://docs.aws.amazon.com/assurance/latest/APIReference/API_PutEvidence.html)  **
  - **Description:** Grants permission to add evidence, or a new version of existing evidence, to support a compliance assessment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterOrganizationDelegatedAdmin](https://docs.aws.amazon.com/assurance/latest/APIReference/API_RegisterOrganizationDelegatedAdmin.html)  **
  - **Description:** Grants permission to register a delegated administrator for AWS Assurance in the caller's organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectInvitation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_RejectInvitation.html)  **
  - **Description:** Grants permission to reject an invitation
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokePermissionSet](https://docs.aws.amazon.com/assurance/latest/APIReference/API_RevokePermissionSet.html)  **
  - **Description:** Grants permission to revoke a permission set assignment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAssessment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_StartAssessment.html)  **
  - **Description:** Grants permission to begin a new assessment for a control or framework
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAssessmentReportExport](https://docs.aws.amazon.com/assurance/latest/APIReference/API_StartAssessmentReportExport.html)  **
  - **Description:** Grants permission to start preparing an assessment report
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartResourceDiscovery](https://docs.aws.amazon.com/assurance/latest/APIReference/API_StartResourceDiscovery.html)  **
  - **Description:** Grants permission to start discovery of in-scope resources
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/assurance/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or overwrite tags on a resource
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_assurance-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_assurance-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_assurance-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateComment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdateComment.html)  **
  - **Description:** Grants permission to modify the content of an existing comment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateControl](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdateControl.html)  **
  - **Description:** Grants permission to update a custom control
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateControlGroup](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdateControlGroup.html)  **
  - **Description:** Grants permission to update a control group's mutable attributes
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to update a governance environment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEvidence](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdateEvidence.html)  **
  - **Description:** Grants permission to update evidence metadata and manage control links
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFramework](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdateFramework.html)  **
  - **Description:** Grants permission to update a custom framework
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePermissionSet](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdatePermissionSet.html)  **
  - **Description:** Grants permission to update a permission set
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProject](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdateProject.html)  **
  - **Description:** Grants permission to update a project
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTask](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdateTask.html)  **
  - **Description:** Grants permission to update an existing task's mutable fields
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Assurance
<a name="list_assurance-permission-only-actions"></a>

The following actions are defined by AWS Assurance but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateAnnotation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreateAnnotation.html)  **
  - **Description:** Grants permission to create an annotation on a piece of evidence
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTask](https://docs.aws.amazon.com/assurance/latest/APIReference/API_CreateTask.html)  **
  - **Description:** Grants permission to create a new task for a specific control and assessment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAnnotation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DeleteAnnotation.html)  **
  - **Description:** Grants permission to delete an annotation from a piece of evidence
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DownloadEvidence](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DownloadEvidence.html)  **
  - **Description:** Grants permission to retrieve the content of an evidence item
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [UpdateAnnotation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdateAnnotation.html)  **
  - **Description:** Grants permission to update the reviewer notes on an existing annotation
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssessment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UpdateAssessment.html)  **
  - **Description:** Grants permission to update an assessment's status and result
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UploadEvidence](https://docs.aws.amazon.com/assurance/latest/APIReference/API_UploadEvidence.html)  **
  - **Description:** Grants permission to upload new evidence to support a compliance assessment
  - **Resource types (\*required):** [environment\*](#list_assurance-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VendConnectionAccessToken](https://docs.aws.amazon.com/assurance/latest/APIReference/API_VendConnectionAccessToken.html)  **
  - **Description:** Grants permission to retrieve a short-lived access token for a third-party connection in an environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Assurance
<a name="list_assurance-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [environment](https://docs.aws.amazon.com/assurance/latest/APIReference/security-iam.html)  | arn:${Partition}:assurance:${Region}:${Account}:environment/${Environment} | [aws:ResourceTag/${TagKey}](#list_assurance-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Assurance
<a name="list_assurance-policy-keys"></a>

AWS Assurance defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 