

# Actions, resources, and condition keys for AWS Security Agent
<a name="list_securityagent"></a>

AWS Security Agent (service prefix: `securityagent`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/securityagent/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/securityagent/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/securityagent/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/securityagent/securityagent.json) for this service.

**Topics**
+ [API operations defined by AWS Security Agent](#list_securityagent-operations)
+ [Actions defined by AWS Security Agent](#list_securityagent-actions-as-permissions)
+ [Resource types defined by AWS Security Agent](#list_securityagent-resources-for-iam-policies)
+ [Condition keys for AWS Security Agent](#list_securityagent-policy-keys)

## API operations defined by AWS Security Agent
<a name="list_securityagent-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_securityagent-actions-as-permissions).




- **   AddArtifact  **
  - **IAM action:**  [securityagent:AddArtifact](#list_securityagent-action-AddArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchCreateSecurityRequirements  **
  - **IAM action:**  [securityagent:BatchCreateSecurityRequirements](#list_securityagent-action-BatchCreateSecurityRequirements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteCodeReviews  **
  - **IAM action:**  [securityagent:BatchDeleteCodeReviews](#list_securityagent-action-BatchDeleteCodeReviews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeletePentests  **
  - **IAM action:**  [securityagent:BatchDeletePentests](#list_securityagent-action-BatchDeletePentests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteSecurityRequirements  **
  - **IAM action:**  [securityagent:BatchDeleteSecurityRequirements](#list_securityagent-action-BatchDeleteSecurityRequirements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteThreatModels  **
  - **IAM action:**  [securityagent:BatchDeleteThreatModels](#list_securityagent-action-BatchDeleteThreatModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetAgentSpaces  **
  - **IAM action:**  [securityagent:BatchGetAgentSpaces](#list_securityagent-action-BatchGetAgentSpaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetArtifactMetadata  **
  - **IAM action:**  [securityagent:BatchGetArtifactMetadata](#list_securityagent-action-BatchGetArtifactMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetCodeReviewJobTasks  **
  - **IAM action:**  [securityagent:BatchGetCodeReviewJobTasks](#list_securityagent-action-BatchGetCodeReviewJobTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetCodeReviewJobs  **
  - **IAM action:**  [securityagent:BatchGetCodeReviewJobs](#list_securityagent-action-BatchGetCodeReviewJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetCodeReviews  **
  - **IAM action:**  [securityagent:BatchGetCodeReviews](#list_securityagent-action-BatchGetCodeReviews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetFindings  **
  - **IAM action:**  [securityagent:BatchGetFindings](#list_securityagent-action-BatchGetFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetPentestJobTasks  **
  - **IAM action:**  [securityagent:BatchGetPentestJobTasks](#list_securityagent-action-BatchGetPentestJobTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetPentestJobs  **
  - **IAM action:**  [securityagent:BatchGetPentestJobs](#list_securityagent-action-BatchGetPentestJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetPentests  **
  - **IAM action:**  [securityagent:BatchGetPentests](#list_securityagent-action-BatchGetPentests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetSecurityRequirements  **
  - **IAM action:**  [securityagent:BatchGetSecurityRequirements](#list_securityagent-action-BatchGetSecurityRequirements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetTargetDomains  **
  - **IAM action:**  [securityagent:BatchGetTargetDomains](#list_securityagent-action-BatchGetTargetDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetThreatModelJobTasks  **
  - **IAM action:**  [securityagent:BatchGetThreatModelJobTasks](#list_securityagent-action-BatchGetThreatModelJobTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetThreatModelJobs  **
  - **IAM action:**  [securityagent:BatchGetThreatModelJobs](#list_securityagent-action-BatchGetThreatModelJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetThreatModels  **
  - **IAM action:**  [securityagent:BatchGetThreatModels](#list_securityagent-action-BatchGetThreatModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetThreats  **
  - **IAM action:**  [securityagent:BatchGetThreats](#list_securityagent-action-BatchGetThreats) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchUpdateSecurityRequirements  **
  - **IAM action:**  [securityagent:BatchUpdateSecurityRequirements](#list_securityagent-action-BatchUpdateSecurityRequirements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAgentSpace  **
  - **IAM action:**  [securityagent:CreateAgentSpace](#list_securityagent-action-CreateAgentSpace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityagent:TagResource](#list_securityagent-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** securityagent.amazonaws.com / **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [securityagent:CreateApplication](#list_securityagent-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityagent:TagResource](#list_securityagent-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** securityagent.amazonaws.com / **Access level:** Write

- **   CreateCodeReview  **
  - **IAM action:**  [securityagent:CreateCodeReview](#list_securityagent-action-CreateCodeReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIntegration  **
  - **IAM action:**  [securityagent:CreateIntegration](#list_securityagent-action-CreateIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityagent:TagResource](#list_securityagent-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMembership  **
  - **IAM action:**  [securityagent:CreateMembership](#list_securityagent-action-CreateMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePentest  **
  - **IAM action:**  [securityagent:CreatePentest](#list_securityagent-action-CreatePentest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePrivateConnection  **
  - **IAM action:**  [securityagent:CreatePrivateConnection](#list_securityagent-action-CreatePrivateConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityagent:TagResource](#list_securityagent-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSecurityRequirementPack  **
  - **IAM action:**  [securityagent:CreateSecurityRequirementPack](#list_securityagent-action-CreateSecurityRequirementPack)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityagent:TagResource](#list_securityagent-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTargetDomain  **
  - **IAM action:**  [securityagent:CreateTargetDomain](#list_securityagent-action-CreateTargetDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securityagent:TagResource](#list_securityagent-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateThreat  **
  - **IAM action:**  [securityagent:CreateThreat](#list_securityagent-action-CreateThreat) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateThreatModel  **
  - **IAM action:**  [securityagent:CreateThreatModel](#list_securityagent-action-CreateThreatModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAgentSpace  **
  - **IAM action:**  [securityagent:DeleteAgentSpace](#list_securityagent-action-DeleteAgentSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplication  **
  - **IAM action:**  [securityagent:DeleteApplication](#list_securityagent-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteArtifact  **
  - **IAM action:**  [securityagent:DeleteArtifact](#list_securityagent-action-DeleteArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegration  **
  - **IAM action:**  [securityagent:DeleteIntegration](#list_securityagent-action-DeleteIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMembership  **
  - **IAM action:**  [securityagent:DeleteMembership](#list_securityagent-action-DeleteMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePrivateConnection  **
  - **IAM action:**  [securityagent:DeletePrivateConnection](#list_securityagent-action-DeletePrivateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSecurityRequirementPack  **
  - **IAM action:**  [securityagent:DeleteSecurityRequirementPack](#list_securityagent-action-DeleteSecurityRequirementPack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTargetDomain  **
  - **IAM action:**  [securityagent:DeleteTargetDomain](#list_securityagent-action-DeleteTargetDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribePrivateConnection  **
  - **IAM action:**  [securityagent:DescribePrivateConnection](#list_securityagent-action-DescribePrivateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplication  **
  - **IAM action:**  [securityagent:GetApplication](#list_securityagent-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetArtifact  **
  - **IAM action:**  [securityagent:GetArtifact](#list_securityagent-action-GetArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegration  **
  - **IAM action:**  [securityagent:GetIntegration](#list_securityagent-action-GetIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSecurityRequirementPack  **
  - **IAM action:**  [securityagent:GetSecurityRequirementPack](#list_securityagent-action-GetSecurityRequirementPack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportSecurityRequirements  **
  - **IAM action:**  [securityagent:ImportSecurityRequirements](#list_securityagent-action-ImportSecurityRequirements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InitiateProviderRegistration  **
  - **IAM action:**  [securityagent:InitiateProviderRegistration](#list_securityagent-action-InitiateProviderRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAgentSpaces  **
  - **IAM action:**  [securityagent:ListAgentSpaces](#list_securityagent-action-ListAgentSpaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplications  **
  - **IAM action:**  [securityagent:ListApplications](#list_securityagent-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListArtifacts  **
  - **IAM action:**  [securityagent:ListArtifacts](#list_securityagent-action-ListArtifacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCodeReviewJobTasks  **
  - **IAM action:**  [securityagent:ListCodeReviewJobTasks](#list_securityagent-action-ListCodeReviewJobTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCodeReviewJobsForCodeReview  **
  - **IAM action:**  [securityagent:ListCodeReviewJobsForCodeReview](#list_securityagent-action-ListCodeReviewJobsForCodeReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCodeReviews  **
  - **IAM action:**  [securityagent:ListCodeReviews](#list_securityagent-action-ListCodeReviews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDiscoveredEndpoints  **
  - **IAM action:**  [securityagent:ListDiscoveredEndpoints](#list_securityagent-action-ListDiscoveredEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFindings  **
  - **IAM action:**  [securityagent:ListFindings](#list_securityagent-action-ListFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntegratedResources  **
  - **IAM action:**  [securityagent:ListIntegratedResources](#list_securityagent-action-ListIntegratedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntegrations  **
  - **IAM action:**  [securityagent:ListIntegrations](#list_securityagent-action-ListIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMemberships  **
  - **IAM action:**  [securityagent:ListMemberships](#list_securityagent-action-ListMemberships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPentestJobTasks  **
  - **IAM action:**  [securityagent:ListPentestJobTasks](#list_securityagent-action-ListPentestJobTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPentestJobsForPentest  **
  - **IAM action:**  [securityagent:ListPentestJobsForPentest](#list_securityagent-action-ListPentestJobsForPentest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPentests  **
  - **IAM action:**  [securityagent:ListPentests](#list_securityagent-action-ListPentests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrivateConnections  **
  - **IAM action:**  [securityagent:ListPrivateConnections](#list_securityagent-action-ListPrivateConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSecurityRequirementPacks  **
  - **IAM action:**  [securityagent:ListSecurityRequirementPacks](#list_securityagent-action-ListSecurityRequirementPacks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSecurityRequirements  **
  - **IAM action:**  [securityagent:ListSecurityRequirements](#list_securityagent-action-ListSecurityRequirements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [securityagent:ListTagsForResource](#list_securityagent-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTargetDomains  **
  - **IAM action:**  [securityagent:ListTargetDomains](#list_securityagent-action-ListTargetDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThreatModelJobTasks  **
  - **IAM action:**  [securityagent:ListThreatModelJobTasks](#list_securityagent-action-ListThreatModelJobTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThreatModelJobs  **
  - **IAM action:**  [securityagent:ListThreatModelJobs](#list_securityagent-action-ListThreatModelJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThreatModels  **
  - **IAM action:**  [securityagent:ListThreatModels](#list_securityagent-action-ListThreatModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThreats  **
  - **IAM action:**  [securityagent:ListThreats](#list_securityagent-action-ListThreats) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartCodeRemediation  **
  - **IAM action:**  [securityagent:StartCodeRemediation](#list_securityagent-action-StartCodeRemediation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCodeReviewJob  **
  - **IAM action:**  [securityagent:StartCodeReviewJob](#list_securityagent-action-StartCodeReviewJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartPentestJob  **
  - **IAM action:**  [securityagent:StartPentestJob](#list_securityagent-action-StartPentestJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartThreatModelJob  **
  - **IAM action:**  [securityagent:StartThreatModelJob](#list_securityagent-action-StartThreatModelJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopCodeReviewJob  **
  - **IAM action:**  [securityagent:StopCodeReviewJob](#list_securityagent-action-StopCodeReviewJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopPentestJob  **
  - **IAM action:**  [securityagent:StopPentestJob](#list_securityagent-action-StopPentestJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopThreatModelJob  **
  - **IAM action:**  [securityagent:StopThreatModelJob](#list_securityagent-action-StopThreatModelJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [securityagent:TagResource](#list_securityagent-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [securityagent:UntagResource](#list_securityagent-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAgentSpace  **
  - **IAM action:**  [securityagent:UpdateAgentSpace](#list_securityagent-action-UpdateAgentSpace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** securityagent.amazonaws.com / **Access level:** Write

- **   UpdateApplication  **
  - **IAM action:**  [securityagent:UpdateApplication](#list_securityagent-action-UpdateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** securityagent.amazonaws.com / **Access level:** Write

- **   UpdateCodeReview  **
  - **IAM action:**  [securityagent:UpdateCodeReview](#list_securityagent-action-UpdateCodeReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFinding  **
  - **IAM action:**  [securityagent:UpdateFinding](#list_securityagent-action-UpdateFinding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIntegratedResources  **
  - **IAM action:**  [securityagent:UpdateIntegratedResources](#list_securityagent-action-UpdateIntegratedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePentest  **
  - **IAM action:**  [securityagent:UpdatePentest](#list_securityagent-action-UpdatePentest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePrivateConnectionCertificate  **
  - **IAM action:**  [securityagent:UpdatePrivateConnectionCertificate](#list_securityagent-action-UpdatePrivateConnectionCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSecurityRequirementPack  **
  - **IAM action:**  [securityagent:UpdateSecurityRequirementPack](#list_securityagent-action-UpdateSecurityRequirementPack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTargetDomain  **
  - **IAM action:**  [securityagent:UpdateTargetDomain](#list_securityagent-action-UpdateTargetDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThreat  **
  - **IAM action:**  [securityagent:UpdateThreat](#list_securityagent-action-UpdateThreat) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThreatModel  **
  - **IAM action:**  [securityagent:UpdateThreatModel](#list_securityagent-action-UpdateThreatModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyTargetDomain  **
  - **IAM action:**  [securityagent:VerifyTargetDomain](#list_securityagent-action-VerifyTargetDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Security Agent
<a name="list_securityagent-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddArtifact](https://docs.aws.amazon.com/securityagent/API_AddArtifact.html)  **
  - **Description:** Grants permission to add an Artifact for the given Agent Space
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchCreateSecurityRequirements](https://docs.aws.amazon.com/securityagent/API_BatchCreateSecurityRequirements.html)  **
  - **Description:** Grants permission to batch create security requirements in a customer managed pack
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteCodeReviews](https://docs.aws.amazon.com/securityagent/API_BatchDeleteCodeReviews.html)  **
  - **Description:** Grants permission to delete multiple code reviews in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeletePentests](https://docs.aws.amazon.com/securityagent/API_BatchDeletePentests.html)  **
  - **Description:** Grants permission to delete multiple penetration tests in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteSecurityRequirements](https://docs.aws.amazon.com/securityagent/API_BatchDeleteSecurityRequirements.html)  **
  - **Description:** Grants permission to batch delete security requirements from a customer managed pack
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteThreatModels](https://docs.aws.amazon.com/securityagent/API_BatchDeleteThreatModels.html)  **
  - **Description:** Grants permission to delete multiple threat models in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteThreats](https://docs.aws.amazon.com/securityagent/API_BatchDeleteThreats.html)  **
  - **Description:** Grants permission to delete multiple threats
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetAgentSpaces](https://docs.aws.amazon.com/securityagent/API_BatchGetAgentSpaces.html)  **
  - **Description:** Grants permission to retrieve multiple agent spaces in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetArtifactMetadata](https://docs.aws.amazon.com/securityagent/API_BatchGetArtifactMetadata.html)  **
  - **Description:** Grants permission to retrieve one or more Artifact Metadata records for the given Agent Space
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetCodeReviewJobTasks](https://docs.aws.amazon.com/securityagent/API_BatchGetCodeReviewJobTasks.html)  **
  - **Description:** Grants permission to retrieve multiple code review job tasks in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetCodeReviewJobs](https://docs.aws.amazon.com/securityagent/API_BatchGetCodeReviewJobs.html)  **
  - **Description:** Grants permission to retrieve multiple code review jobs in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetCodeReviews](https://docs.aws.amazon.com/securityagent/API_BatchGetCodeReviews.html)  **
  - **Description:** Grants permission to retrieve multiple code reviews in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetFindings](https://docs.aws.amazon.com/securityagent/API_BatchGetFindings.html)  **
  - **Description:** Grants permission to retrieve multiple security testing findings in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetPentestJobContentMetadata](https://docs.aws.amazon.com/securityagent/API_BatchGetPentestJobContentMetadata.html)  **
  - **Description:** Grants permission to retrieve multiple pentest job contents metadata in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetPentestJobTasks](https://docs.aws.amazon.com/securityagent/API_BatchGetPentestJobTasks.html)  **
  - **Description:** Grants permission to retrieve multiple pentest job tasks in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetPentestJobs](https://docs.aws.amazon.com/securityagent/API_BatchGetPentestJobs.html)  **
  - **Description:** Grants permission to retrieve multiple security testing jobs in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetPentests](https://docs.aws.amazon.com/securityagent/API_BatchGetPentests.html)  **
  - **Description:** Grants permission to retrieve multiple penetration tests in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetSecurityRequirements](https://docs.aws.amazon.com/securityagent/API_BatchGetSecurityRequirements.html)  **
  - **Description:** Grants permission to retrieve multiple security requirements in a single request
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetTargetDomains](https://docs.aws.amazon.com/securityagent/API_BatchGetTargetDomains.html)  **
  - **Description:** Grants permission to retrieve multiple target domains in a single request
  - **Resource types (\*required):** [TargetDomain\*](#list_securityagent-resource-TargetDomain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetThreatModelJobTasks](https://docs.aws.amazon.com/securityagent/API_BatchGetThreatModelJobTasks.html)  **
  - **Description:** Grants permission to retrieve multiple tasks for a threat model job in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetThreatModelJobs](https://docs.aws.amazon.com/securityagent/API_BatchGetThreatModelJobs.html)  **
  - **Description:** Grants permission to retrieve details for one or more threat model jobs
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetThreatModels](https://docs.aws.amazon.com/securityagent/API_BatchGetThreatModels.html)  **
  - **Description:** Grants permission to retrieve multiple threat models in a single request
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetThreats](https://docs.aws.amazon.com/securityagent/API_BatchGetThreats.html)  **
  - **Description:** Grants permission to retrieve details for one or more threats
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchUpdateSecurityRequirements](https://docs.aws.amazon.com/securityagent/API_BatchUpdateSecurityRequirements.html)  **
  - **Description:** Grants permission to batch update security requirements within a customer managed pack
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAgentSpace](https://docs.aws.amazon.com/securityagent/API_CreateAgentSpace.html)  **
  - **Description:** Grants permission to create an agent space record
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/securityagent/API_CreateApplication.html)  **
  - **Description:** Grants permission to create a new application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCodeReview](https://docs.aws.amazon.com/securityagent/API_CreateCodeReview.html)  **
  - **Description:** Grants permission to create a new code review configuration
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDesignReview](https://docs.aws.amazon.com/securityagent/API_CreateDesignReview.html)  **
  - **Description:** Grants permission to create a design review
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateIntegration](https://docs.aws.amazon.com/securityagent/API_CreateIntegration.html)  **
  - **Description:** Grants permission to create a security testing integration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMembership](https://docs.aws.amazon.com/securityagent/API_CreateMembership.html)  **
  - **Description:** Grants permission to add a single member to a agent space with specified role
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateOneTimeLoginSession](https://docs.aws.amazon.com/securityagent/API_CreateOneTimeLoginSession.html)  **
  - **Description:** Grants permission to create a one time login session
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePentest](https://docs.aws.amazon.com/securityagent/API_CreatePentest.html)  **
  - **Description:** Grants permission to create a new penetration test configuration
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePrivateConnection](https://docs.aws.amazon.com/securityagent/API_CreatePrivateConnection.html)  **
  - **Description:** Grants permission to create a private connection for VPC Lattice integration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSecurityRequirement](https://docs.aws.amazon.com/securityagent/API_CreateSecurityRequirement.html)  **
  - **Description:** Grants permission to add a customer managed Security Requirement
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSecurityRequirementPack](https://docs.aws.amazon.com/securityagent/API_CreateSecurityRequirementPack.html)  **
  - **Description:** Grants permission to create a customer managed security requirement pack
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTargetDomain](https://docs.aws.amazon.com/securityagent/API_CreateTargetDomain.html)  **
  - **Description:** Grants permission to create a target domain record
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateThreat](https://docs.aws.amazon.com/securityagent/API_CreateThreat.html)  **
  - **Description:** Grants permission to create a threat in a threat model
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateThreatModel](https://docs.aws.amazon.com/securityagent/API_CreateThreatModel.html)  **
  - **Description:** Grants permission to create a new threat model configuration
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentSpace](https://docs.aws.amazon.com/securityagent/API_DeleteAgentSpace.html)  **
  - **Description:** Grants permission to delete an agent space record
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/securityagent/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete application
  - **Resource types (\*required):** [Application\*](#list_securityagent-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteArtifact](https://docs.aws.amazon.com/securityagent/API_DeleteArtifact.html)  **
  - **Description:** Grants permission to delete an Artifact
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDesignReview](https://docs.aws.amazon.com/securityagent/API_DeleteDesignReview.html)  **
  - **Description:** Grants permission to delete a design review
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/securityagent/API_DeleteIntegration.html)  **
  - **Description:** Grants permission to delete the integration of an application
  - **Resource types (\*required):** [Integration\*](#list_securityagent-resource-Integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMembership](https://docs.aws.amazon.com/securityagent/API_DeleteMembership.html)  **
  - **Description:** Grants permission to remove a single member associated to an agent space
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePrivateConnection](https://docs.aws.amazon.com/securityagent/API_DeletePrivateConnection.html)  **
  - **Description:** Grants permission to delete a private connection
  - **Resource types (\*required):** [PrivateConnection\*](#list_securityagent-resource-PrivateConnection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSecurityRequirement](https://docs.aws.amazon.com/securityagent/API_DeleteSecurityRequirement.html)  **
  - **Description:** Grants permission to delete a customer managed Security Requirement
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSecurityRequirementPack](https://docs.aws.amazon.com/securityagent/API_DeleteSecurityRequirementPack.html)  **
  - **Description:** Grants permission to delete a customer managed security requirement pack and all its associated security requirements
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTargetDomain](https://docs.aws.amazon.com/securityagent/API_DeleteTargetDomain.html)  **
  - **Description:** Grants permission to delete a target domain record
  - **Resource types (\*required):** [TargetDomain\*](#list_securityagent-resource-TargetDomain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribePrivateConnection](https://docs.aws.amazon.com/securityagent/API_DescribePrivateConnection.html)  **
  - **Description:** Grants permission to describe a private connection
  - **Resource types (\*required):** [PrivateConnection\*](#list_securityagent-resource-PrivateConnection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetApplication](https://docs.aws.amazon.com/securityagent/API_GetApplication.html)  **
  - **Description:** Grants permission to get application details by application ID
  - **Resource types (\*required):** [Application\*](#list_securityagent-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetArtifact](https://docs.aws.amazon.com/securityagent/API_GetArtifact.html)  **
  - **Description:** Grants permission to retrieve an Artifact for the given Agent Space
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDesignReview](https://docs.aws.amazon.com/securityagent/API_GetDesignReview.html)  **
  - **Description:** Grants permission to get the status of the associated agent space design review
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDesignReviewArtifact](https://docs.aws.amazon.com/securityagent/API_GetDesignReviewArtifact.html)  **
  - **Description:** Grants permission to get design review artifact for a specific document
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDesignReviewFeedback](https://docs.aws.amazon.com/securityagent/API_GetDesignReviewFeedback.html)  **
  - **Description:** Grants permission to get feedback for a design review comment
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntegration](https://docs.aws.amazon.com/securityagent/API_GetIntegration.html)  **
  - **Description:** Grants permission to get the integration metadata by ID
  - **Resource types (\*required):** [Integration\*](#list_securityagent-resource-Integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProviderRegistrationManifest](https://docs.aws.amazon.com/securityagent/API_GetProviderRegistrationManifest.html)  **
  - **Description:** Grants permission to retrieve the provider registration manifest used for browser-based integration registration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSecurityRequirement](https://docs.aws.amazon.com/securityagent/API_GetSecurityRequirement.html)  **
  - **Description:** Grants permission to retrieve a Security Requirement
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSecurityRequirementPack](https://docs.aws.amazon.com/securityagent/API_GetSecurityRequirementPack.html)  **
  - **Description:** Grants permission to retrieve a security requirement pack
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [HandleProviderRegistrationCallback](https://docs.aws.amazon.com/securityagent/API_HandleProviderRegistrationCallback.html)  **
  - **Description:** Grants permission to handle the provider OAuth registration callback that completes integration setup
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ImportSecurityRequirements](https://docs.aws.amazon.com/securityagent/API_ImportSecurityRequirements.html)  **
  - **Description:** Grants permission to import security requirements from uploaded documents for a customer managed security requirement pack
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InitiateProviderRegistration](https://docs.aws.amazon.com/securityagent/API_InitiateProviderRegistration.html)  **
  - **Description:** Grants permission to initiate the registration of Security Agent App for the given provider (eg: GitHub)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListAgentSpaces](https://docs.aws.amazon.com/securityagent/API_ListAgentSpaces.html)  **
  - **Description:** Grants permission to list agent spaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApplications](https://docs.aws.amazon.com/securityagent/API_ListApplications.html)  **
  - **Description:** Grants permission to list all applications in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListArtifacts](https://docs.aws.amazon.com/securityagent/API_ListArtifacts.html)  **
  - **Description:** Grants permission to list all artifacts for the given agent space
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCodeReviewJobTasks](https://docs.aws.amazon.com/securityagent/API_ListCodeReviewJobTasks.html)  **
  - **Description:** Grants permission to list tasks associated with a code review job
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCodeReviewJobsForCodeReview](https://docs.aws.amazon.com/securityagent/API_ListCodeReviewJobsForCodeReview.html)  **
  - **Description:** Grants permission to list code review jobs associated with a code review
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCodeReviews](https://docs.aws.amazon.com/securityagent/API_ListCodeReviews.html)  **
  - **Description:** Grants permission to list code reviews with optional filtering by status
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDesignReviewComments](https://docs.aws.amazon.com/securityagent/API_ListDesignReviewComments.html)  **
  - **Description:** Grants permission to list design review comments
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDesignReviews](https://docs.aws.amazon.com/securityagent/API_ListDesignReviews.html)  **
  - **Description:** Grants permission to list all design reviews for the given agent space
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDiscoveredEndpoints](https://docs.aws.amazon.com/securityagent/API_ListDiscoveredEndpoints.html)  **
  - **Description:** Grants permission to list discovered endpoints associated with a pentest job with optional URI prefix filtering
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFindings](https://docs.aws.amazon.com/securityagent/API_ListFindings.html)  **
  - **Description:** Grants permission to list findings with filtering and pagination support
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIntegratedResources](https://docs.aws.amazon.com/securityagent/API_ListIntegratedResources.html)  **
  - **Description:** Grants permission to list integrated resources for an agent space
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIntegrations](https://docs.aws.amazon.com/securityagent/API_ListIntegrations.html)  **
  - **Description:** Grants permission to get the integrations owned by the caller's AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMemberships](https://docs.aws.amazon.com/securityagent/API_ListMemberships.html)  **
  - **Description:** Grants permission to list all members associated to an agent space with pagination support
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPentestJobTasks](https://docs.aws.amazon.com/securityagent/API_ListPentestJobTasks.html)  **
  - **Description:** Grants permission to list pentest job tasks associated with a pentest job
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPentestJobsForPentest](https://docs.aws.amazon.com/securityagent/API_ListPentestJobsForPentest.html)  **
  - **Description:** Grants permission to list penetration test jobs associated with a penetration test
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPentests](https://docs.aws.amazon.com/securityagent/API_ListPentests.html)  **
  - **Description:** Grants permission to list penetration tests with optional filtering by status
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPrivateConnections](https://docs.aws.amazon.com/securityagent/API_ListPrivateConnections.html)  **
  - **Description:** Grants permission to list private connections in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourcesFromIntegration](https://docs.aws.amazon.com/securityagent/API_ListResourcesFromIntegration.html)  **
  - **Description:** Grants permission to list resources from Integration
  - **Resource types (\*required):** [Integration\*](#list_securityagent-resource-Integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSecurityRequirementPacks](https://docs.aws.amazon.com/securityagent/API_ListSecurityRequirementPacks.html)  **
  - **Description:** Grants permission to list all security requirement packs in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSecurityRequirements](https://docs.aws.amazon.com/securityagent/API_ListSecurityRequirements.html)  **
  - **Description:** Grants permission to list all Security Requirements
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/securityagent/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [AgentSpace](#list_securityagent-resource-AgentSpace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Application](#list_securityagent-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration](#list_securityagent-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PrivateConnection](#list_securityagent-resource-PrivateConnection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SecurityRequirementPack](#list_securityagent-resource-SecurityRequirementPack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [TargetDomain](#list_securityagent-resource-TargetDomain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTargetDomains](https://docs.aws.amazon.com/securityagent/API_ListTargetDomains.html)  **
  - **Description:** Grants permission to list target domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListThreatModelJobTasks](https://docs.aws.amazon.com/securityagent/API_ListThreatModelJobTasks.html)  **
  - **Description:** Grants permission to list tasks associated with a specific threat model job
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListThreatModelJobs](https://docs.aws.amazon.com/securityagent/API_ListThreatModelJobs.html)  **
  - **Description:** Grants permission to list threat model jobs for a threat model
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListThreatModels](https://docs.aws.amazon.com/securityagent/API_ListThreatModels.html)  **
  - **Description:** Grants permission to list threat models for an agent space
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListThreats](https://docs.aws.amazon.com/securityagent/API_ListThreats.html)  **
  - **Description:** Grants permission to list threats for a threat model job with filtering and pagination support
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutDesignReviewFeedback](https://docs.aws.amazon.com/securityagent/API_PutDesignReviewFeedback.html)  **
  - **Description:** Grants permission to submit feedback for a design review comment
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartCodeRemediation](https://docs.aws.amazon.com/securityagent/API_StartCodeRemediation.html)  **
  - **Description:** Grants permission to start code remediation for the findings
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartCodeReviewJob](https://docs.aws.amazon.com/securityagent/API_StartCodeReviewJob.html)  **
  - **Description:** Grants permission to initiate the execution of a code review
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartPentestJob](https://docs.aws.amazon.com/securityagent/API_StartPentestJob.html)  **
  - **Description:** Grants permission to initiate the execution of a penetration test
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartThreatModelJob](https://docs.aws.amazon.com/securityagent/API_StartThreatModelJob.html)  **
  - **Description:** Grants permission to initiate the execution of a threat model job
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopCodeReviewJob](https://docs.aws.amazon.com/securityagent/API_StopCodeReviewJob.html)  **
  - **Description:** Grants permission to stop the execution of a running code review
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopPentestJob](https://docs.aws.amazon.com/securityagent/API_StopPentestJob.html)  **
  - **Description:** Grants permission to stop the execution of a running penetration test
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopThreatModelJob](https://docs.aws.amazon.com/securityagent/API_StopThreatModelJob.html)  **
  - **Description:** Grants permission to stop a running threat model job
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/securityagent/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [AgentSpace](#list_securityagent-resource-AgentSpace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Resource types (\*required):** [Application](#list_securityagent-resource-Application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Resource types (\*required):** [Integration](#list_securityagent-resource-Integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Resource types (\*required):** [PrivateConnection](#list_securityagent-resource-PrivateConnection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Resource types (\*required):** [SecurityRequirementPack](#list_securityagent-resource-SecurityRequirementPack) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Resource types (\*required):** [TargetDomain](#list_securityagent-resource-TargetDomain) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securityagent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [ToggleManagedSecurityRequirement](https://docs.aws.amazon.com/securityagent/API_ToggleManagedSecurityRequirement.html)  **
  - **Description:** Grants permission to toggle the status of a managed Security Requirement
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/securityagent/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [AgentSpace](#list_securityagent-resource-AgentSpace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Resource types (\*required):** [Application](#list_securityagent-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Resource types (\*required):** [Integration](#list_securityagent-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Resource types (\*required):** [PrivateConnection](#list_securityagent-resource-PrivateConnection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Resource types (\*required):** [SecurityRequirementPack](#list_securityagent-resource-SecurityRequirementPack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Resource types (\*required):** [TargetDomain](#list_securityagent-resource-TargetDomain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securityagent-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAgentSpace](https://docs.aws.amazon.com/securityagent/API_UpdateAgentSpace.html)  **
  - **Description:** Grants permission to update an agent space record
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateApplication](https://docs.aws.amazon.com/securityagent/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update application configuration
  - **Resource types (\*required):** [Application\*](#list_securityagent-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCodeReview](https://docs.aws.amazon.com/securityagent/API_UpdateCodeReview.html)  **
  - **Description:** Grants permission to update an existing code review with new configuration or settings
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFinding](https://docs.aws.amazon.com/securityagent/API_UpdateFinding.html)  **
  - **Description:** Grants permission to update an existing security finding with new details or status
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIntegratedResources](https://docs.aws.amazon.com/securityagent/API_UpdateIntegratedResources.html)  **
  - **Description:** Grants permission to update integrated resources for an agent space
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_securityagent-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePentest](https://docs.aws.amazon.com/securityagent/API_UpdatePentest.html)  **
  - **Description:** Grants permission to update an existing penetration test with new configuration or settings
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePrivateConnectionCertificate](https://docs.aws.amazon.com/securityagent/API_UpdatePrivateConnectionCertificate.html)  **
  - **Description:** Grants permission to update the certificate associated with a private connection
  - **Resource types (\*required):** [PrivateConnection\*](#list_securityagent-resource-PrivateConnection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSecurityRequirement](https://docs.aws.amazon.com/securityagent/API_UpdateSecurityRequirement.html)  **
  - **Description:** Grants permission to update a customer managed Security Requirement
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSecurityRequirementPack](https://docs.aws.amazon.com/securityagent/API_UpdateSecurityRequirementPack.html)  **
  - **Description:** Grants permission to update a security requirement pack
  - **Resource types (\*required):** [SecurityRequirementPack\*](#list_securityagent-resource-SecurityRequirementPack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTargetDomain](https://docs.aws.amazon.com/securityagent/API_UpdateTargetDomain.html)  **
  - **Description:** Grants permission to update a target domain record
  - **Resource types (\*required):** [TargetDomain\*](#list_securityagent-resource-TargetDomain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThreat](https://docs.aws.amazon.com/securityagent/API_UpdateThreat.html)  **
  - **Description:** Grants permission to update a threat
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThreatModel](https://docs.aws.amazon.com/securityagent/API_UpdateThreatModel.html)  **
  - **Description:** Grants permission to update an existing threat model with new configuration
  - **Resource types (\*required):** [AgentSpace\*](#list_securityagent-resource-AgentSpace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VerifyTargetDomain](https://docs.aws.amazon.com/securityagent/API_VerifyTargetDomain.html)  **
  - **Description:** Grants permission to verify ownership for a registered target domain
  - **Resource types (\*required):** [TargetDomain\*](#list_securityagent-resource-TargetDomain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Security Agent
<a name="list_securityagent-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AgentSpace](https://docs.aws.amazon.com/securityagent/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:securityagent:${Region}:${Account}:agent-space/${AgentId} | [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_) | 
|  [Application](https://docs.aws.amazon.com/securityagent/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:securityagent:${Region}:${Account}:application/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_) | 
|  [Integration](https://docs.aws.amazon.com/securityagent/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:securityagent:${Region}:${Account}:integration/${IntegrationId} | [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_) | 
|  [PrivateConnection](https://docs.aws.amazon.com/securityagent/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:securityagent:${Region}:${Account}:private-connection/${PrivateConnectionName} | [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_) | 
|  [SecurityRequirementPack](https://docs.aws.amazon.com/securityagent/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:securityagent:${Region}:${Account}:security-requirement-pack/${SecurityRequirementPackId} | [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_) | 
|  [TargetDomain](https://docs.aws.amazon.com/securityagent/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:securityagent:${Region}:${Account}:target-domain/${TargetDomainId} | [aws:ResourceTag/${TagKey}](#list_securityagent-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Security Agent
<a name="list_securityagent-policy-keys"></a>

AWS Security Agent defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 