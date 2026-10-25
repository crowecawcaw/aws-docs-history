

# Data retrieval APIs for AWS Assurance
<a name="awsassurance"></a>

AWS Assurance provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="assurance-BatchGetComment"></a>[BatchGetComment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_BatchGetComment.html) | Retrieve multiple comments in a single request | Read | 
| <a name="assurance-BatchGetControl"></a>[BatchGetControl](https://docs.aws.amazon.com/assurance/latest/APIReference/API_BatchGetControl.html) | Retrieve multiple controls in a single request | Read | 
| <a name="assurance-BatchGetTask"></a>[BatchGetTask](https://docs.aws.amazon.com/assurance/latest/APIReference/API_BatchGetTask.html) | Retrieve multiple tasks in a single request | Read | 
| <a name="assurance-DownloadEvidence"></a>[DownloadEvidence](https://docs.aws.amazon.com/assurance/latest/APIReference/API_DownloadEvidence.html) | Retrieve the content of an evidence item | Read | 
| <a name="assurance-GetAnnotation"></a>[GetAnnotation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetAnnotation.html) | Retrieve the annotation for a specific piece of evidence | Read | 
| <a name="assurance-GetAssessment"></a>[GetAssessment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetAssessment.html) | Retrieve a single assessment | Read | 
| <a name="assurance-GetAssessmentReportContent"></a>[GetAssessmentReportContent](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetAssessmentReportContent.html) | Retrieve the content of a prepared assessment report | Read | 
| <a name="assurance-GetAssessmentReportExport"></a>[GetAssessmentReportExport](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetAssessmentReportExport.html) | Retrieve the state of an assessment report export | Read | 
| <a name="assurance-GetChatMessages"></a>[GetChatMessages](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetChatMessages.html) | Get messages for a chat session in chronological order | Read | 
| <a name="assurance-GetComment"></a>[GetComment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetComment.html) | Retrieve a specific comment by its identifying fields | Read | 
| <a name="assurance-GetControl"></a>[GetControl](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetControl.html) | Retrieve a single leaf control within a framework version | Read | 
| <a name="assurance-GetControlGroup"></a>[GetControlGroup](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetControlGroup.html) | Retrieve a single control group within a framework version | Read | 
| <a name="assurance-GetControlStatus"></a>[GetControlStatus](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetControlStatus.html) | Retrieve the effective compliance status of a control | Read | 
| <a name="assurance-GetEnvironment"></a>[GetEnvironment](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetEnvironment.html) | Retrieve a governance environment by ARN or domain | Read | 
| <a name="assurance-GetEvidence"></a>[GetEvidence](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetEvidence.html) | Retrieve metadata for an evidence item | Read | 
| <a name="assurance-GetEvidenceContent"></a>[GetEvidenceContent](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetEvidenceContent.html) | Retrieve the content of an evidence item | Read | 
| <a name="assurance-GetFramework"></a>[GetFramework](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetFramework.html) | Retrieve a framework resource by type and key fields | Read | 
| <a name="assurance-GetInvitation"></a>[GetInvitation](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetInvitation.html) | Retrieve an invitation | Read | 
| <a name="assurance-GetPermissionSet"></a>[GetPermissionSet](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetPermissionSet.html) | Retrieve a permission set | Read | 
| <a name="assurance-GetProject"></a>[GetProject](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetProject.html) | Retrieve a project | Read | 
| <a name="assurance-GetTask"></a>[GetTask](https://docs.aws.amazon.com/assurance/latest/APIReference/API_GetTask.html) | Retrieve a specific task by its identifying fields | Read | 
| <a name="assurance-ListAssessmentAnnotations"></a>[ListAssessmentAnnotations](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListAssessmentAnnotations.html) | List the annotations on one assessment, paginated | Read | 
| <a name="assurance-ListAssessmentJournalRecords"></a>[ListAssessmentJournalRecords](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListAssessmentJournalRecords.html) | List assessment journal records, paginated | Read | 
| <a name="assurance-ListAssessmentOutcomes"></a>[ListAssessmentOutcomes](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListAssessmentOutcomes.html) | List a compliance score over time | Read | 
| <a name="assurance-ListAssessments"></a>[ListAssessments](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListAssessments.html) | List assessments, paginated | Read | 
| <a name="assurance-ListChatSessions"></a>[ListChatSessions](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListChatSessions.html) | List chat sessions for the calling user in a governance environment | Read | 
| <a name="assurance-ListComments"></a>[ListComments](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListComments.html) | List comments in a governance environment | Read | 
| <a name="assurance-ListConnectionItems"></a>[ListConnectionItems](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListConnectionItems.html) | List the contents of an environment connection | Read | 
| <a name="assurance-ListControlGroups"></a>[ListControlGroups](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListControlGroups.html) | List control groups in a framework version | Read | 
| <a name="assurance-ListControlResources"></a>[ListControlResources](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListControlResources.html) | List in-scope resources for a control | Read | 
| <a name="assurance-ListControls"></a>[ListControls](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListControls.html) | List controls within a control group | Read | 
| <a name="assurance-ListDiscoveredResources"></a>[ListDiscoveredResources](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListDiscoveredResources.html) | List the resources found by a discovery job (paginated) | Read | 
| <a name="assurance-ListEnabledFrameworks"></a>[ListEnabledFrameworks](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListEnabledFrameworks.html) | List enabled frameworks for a governance environment | Read | 
| <a name="assurance-ListEnvironmentConnections"></a>[ListEnvironmentConnections](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListEnvironmentConnections.html) | List environment connections in a governance environment | Read | 
| <a name="assurance-ListEnvironments"></a>[ListEnvironments](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListEnvironments.html) | List all governance environments with optional pagination | Read | 
| <a name="assurance-ListEvidence"></a>[ListEvidence](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListEvidence.html) | List evidence items (paginated) | Read | 
| <a name="assurance-ListEvidenceAnnotations"></a>[ListEvidenceAnnotations](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListEvidenceAnnotations.html) | List the annotations on one version of a piece of evidence within a project, paginated | Read | 
| <a name="assurance-ListFrameworks"></a>[ListFrameworks](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListFrameworks.html) | List frameworks | Read | 
| <a name="assurance-ListInboundInvitations"></a>[ListInboundInvitations](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListInboundInvitations.html) | List invitations addressed to the caller's account | Read | 
| <a name="assurance-ListOutboundInvitations"></a>[ListOutboundInvitations](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListOutboundInvitations.html) | List invitations extended from an owned environment | Read | 
| <a name="assurance-ListPermissionSetAssignments"></a>[ListPermissionSetAssignments](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListPermissionSetAssignments.html) | List permission set assignments in an environment | Read | 
| <a name="assurance-ListPermissionSets"></a>[ListPermissionSets](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListPermissionSets.html) | List permission sets in an environment | Read | 
| <a name="assurance-ListProjects"></a>[ListProjects](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListProjects.html) | List all projects within a governance environment | Read | 
| <a name="assurance-ListResourcesForControl"></a>[ListResourcesForControl](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListResourcesForControl.html) | List in-scope resources for a control | Read | 
| <a name="assurance-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListTagsForResource.html) | List tags for a resource | Read | 
| <a name="assurance-ListTaskHistory"></a>[ListTaskHistory](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListTaskHistory.html) | List task history for a task | Read | 
| <a name="assurance-ListTasks"></a>[ListTasks](https://docs.aws.amazon.com/assurance/latest/APIReference/API_ListTasks.html) | List all tasks within a governance environment | Read | 