

# Actions, resources, and condition keys for AWS Deadline Cloud
<a name="list_deadline"></a>

AWS Deadline Cloud (service prefix: `deadline`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/deadline/deadline.json) for this service.

**Topics**
+ [API operations defined by AWS Deadline Cloud](#list_deadline-operations)
+ [Actions defined by AWS Deadline Cloud](#list_deadline-actions-as-permissions)
+ [Permission-only actions for AWS Deadline Cloud](#list_deadline-permission-only-actions)
+ [Resource types defined by AWS Deadline Cloud](#list_deadline-resources-for-iam-policies)
+ [Condition keys for AWS Deadline Cloud](#list_deadline-policy-keys)

## API operations defined by AWS Deadline Cloud
<a name="list_deadline-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_deadline-actions-as-permissions).




- **   AssociateMemberToFarm  **
  - **IAM action:**  [deadline:AssociateMemberToFarm](#list_deadline-action-AssociateMemberToFarm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AssociateMemberToFleet  **
  - **IAM action:**  [deadline:AssociateMemberToFleet](#list_deadline-action-AssociateMemberToFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AssociateMemberToJob  **
  - **IAM action:**  [deadline:AssociateMemberToJob](#list_deadline-action-AssociateMemberToJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AssociateMemberToQueue  **
  - **IAM action:**  [deadline:AssociateMemberToQueue](#list_deadline-action-AssociateMemberToQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AssumeFleetRoleForRead  **
  - **IAM action:**  [deadline:AssumeFleetRoleForRead](#list_deadline-action-AssumeFleetRoleForRead) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssumeFleetRoleForWorker  **
  - **IAM action:**  [deadline:AssumeFleetRoleForWorker](#list_deadline-action-AssumeFleetRoleForWorker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssumeQueueRoleForRead  **
  - **IAM action:**  [deadline:AssumeQueueRoleForRead](#list_deadline-action-AssumeQueueRoleForRead) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssumeQueueRoleForUser  **
  - **IAM action:**  [deadline:AssumeQueueRoleForUser](#list_deadline-action-AssumeQueueRoleForUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssumeQueueRoleForWorker  **
  - **IAM action:**  [deadline:AssumeQueueRoleForWorker](#list_deadline-action-AssumeQueueRoleForWorker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetJob  **
  - **IAM action:**  [deadline:GetJob](#list_deadline-action-GetJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetJobEntity  **
  - **IAM action:**  [deadline:BatchGetJobEntity](#list_deadline-action-BatchGetJobEntity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetSession  **
  - **IAM action:**  [deadline:GetSession](#list_deadline-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetSessionAction  **
  - **IAM action:**  [deadline:GetSessionAction](#list_deadline-action-GetSessionAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetStep  **
  - **IAM action:**  [deadline:GetStep](#list_deadline-action-GetStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetTask  **
  - **IAM action:**  [deadline:GetTask](#list_deadline-action-GetTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetWorker  **
  - **IAM action:**  [deadline:GetWorker](#list_deadline-action-GetWorker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchUpdateJob  **
  - **IAM action:**  [deadline:UpdateJob](#list_deadline-action-UpdateJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateTask  **
  - **IAM action:**  [deadline:UpdateTask](#list_deadline-action-UpdateTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyJobTemplate  **
  - **IAM action:**  [deadline:CopyJobTemplate](#list_deadline-action-CopyJobTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [deadline:GetJobTemplate](#list_deadline-action-GetJobTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateBudget  **
  - **IAM action:**  [deadline:CreateBudget](#list_deadline-action-CreateBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [deadline:TagResource](#list_deadline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFarm  **
  - **IAM action:**  [deadline:CreateFarm](#list_deadline-action-CreateFarm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [deadline:TagResource](#list_deadline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFleet  **
  - **IAM action:**  [deadline:CreateFleet](#list_deadline-action-CreateFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [deadline:TagResource](#list_deadline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** deadline.amazonaws.com / **Access level:** Write

- **   CreateJob  **
  - **IAM action:**  [deadline:CreateJob](#list_deadline-action-CreateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [deadline:GetJobTemplate](#list_deadline-action-GetJobTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [deadline:TagResource](#list_deadline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLicenseEndpoint  **
  - **IAM action:**  [deadline:CreateLicenseEndpoint](#list_deadline-action-CreateLicenseEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [deadline:TagResource](#list_deadline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLimit  **
  - **IAM action:**  [deadline:CreateLimit](#list_deadline-action-CreateLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMonitor  **
  - **IAM action:**  [deadline:CreateMonitor](#list_deadline-action-CreateMonitor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [deadline:TagResource](#list_deadline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** deadline.amazonaws.com / **Access level:** Write

- **   CreateQueue  **
  - **IAM action:**  [deadline:CreateQueue](#list_deadline-action-CreateQueue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [deadline:TagResource](#list_deadline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** deadline.amazonaws.com / **Access level:** Write

- **   CreateQueueEnvironment  **
  - **IAM action:**  [deadline:CreateQueueEnvironment](#list_deadline-action-CreateQueueEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateQueueFleetAssociation  **
  - **IAM action:**  [deadline:CreateQueueFleetAssociation](#list_deadline-action-CreateQueueFleetAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateQueueLimitAssociation  **
  - **IAM action:**  [deadline:CreateQueueLimitAssociation](#list_deadline-action-CreateQueueLimitAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStorageProfile  **
  - **IAM action:**  [deadline:CreateStorageProfile](#list_deadline-action-CreateStorageProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorker  **
  - **IAM action:**  [deadline:CreateWorker](#list_deadline-action-CreateWorker)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [deadline:ListTagsForResource](#list_deadline-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [deadline:TagResource](#list_deadline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteBudget  **
  - **IAM action:**  [deadline:DeleteBudget](#list_deadline-action-DeleteBudget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFarm  **
  - **IAM action:**  [deadline:DeleteFarm](#list_deadline-action-DeleteFarm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFleet  **
  - **IAM action:**  [deadline:DeleteFleet](#list_deadline-action-DeleteFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLicenseEndpoint  **
  - **IAM action:**  [deadline:DeleteLicenseEndpoint](#list_deadline-action-DeleteLicenseEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLimit  **
  - **IAM action:**  [deadline:DeleteLimit](#list_deadline-action-DeleteLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMeteredProduct  **
  - **IAM action:**  [deadline:DeleteMeteredProduct](#list_deadline-action-DeleteMeteredProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMonitor  **
  - **IAM action:**  [deadline:DeleteMonitor](#list_deadline-action-DeleteMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQueue  **
  - **IAM action:**  [deadline:DeleteQueue](#list_deadline-action-DeleteQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQueueEnvironment  **
  - **IAM action:**  [deadline:DeleteQueueEnvironment](#list_deadline-action-DeleteQueueEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQueueFleetAssociation  **
  - **IAM action:**  [deadline:DeleteQueueFleetAssociation](#list_deadline-action-DeleteQueueFleetAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQueueLimitAssociation  **
  - **IAM action:**  [deadline:DeleteQueueLimitAssociation](#list_deadline-action-DeleteQueueLimitAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStorageProfile  **
  - **IAM action:**  [deadline:DeleteStorageProfile](#list_deadline-action-DeleteStorageProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVolume  **
  - **IAM action:**  [deadline:DeleteVolume](#list_deadline-action-DeleteVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorker  **
  - **IAM action:**  [deadline:DeleteWorker](#list_deadline-action-DeleteWorker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateMemberFromFarm  **
  - **IAM action:**  [deadline:DisassociateMemberFromFarm](#list_deadline-action-DisassociateMemberFromFarm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DisassociateMemberFromFleet  **
  - **IAM action:**  [deadline:DisassociateMemberFromFleet](#list_deadline-action-DisassociateMemberFromFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DisassociateMemberFromJob  **
  - **IAM action:**  [deadline:DisassociateMemberFromJob](#list_deadline-action-DisassociateMemberFromJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DisassociateMemberFromQueue  **
  - **IAM action:**  [deadline:DisassociateMemberFromQueue](#list_deadline-action-DisassociateMemberFromQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   GetBudget  **
  - **IAM action:**  [deadline:GetBudget](#list_deadline-action-GetBudget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFarm  **
  - **IAM action:**  [deadline:GetFarm](#list_deadline-action-GetFarm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFleet  **
  - **IAM action:**  [deadline:GetFleet](#list_deadline-action-GetFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJob  **
  - **IAM action:**  [deadline:GetJob](#list_deadline-action-GetJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLicenseEndpoint  **
  - **IAM action:**  [deadline:GetLicenseEndpoint](#list_deadline-action-GetLicenseEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLimit  **
  - **IAM action:**  [deadline:GetLimit](#list_deadline-action-GetLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMonitor  **
  - **IAM action:**  [deadline:GetMonitor](#list_deadline-action-GetMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMonitorSettings  **
  - **IAM action:**  [deadline:GetMonitorSettings](#list_deadline-action-GetMonitorSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueue  **
  - **IAM action:**  [deadline:GetQueue](#list_deadline-action-GetQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueueEnvironment  **
  - **IAM action:**  [deadline:GetQueueEnvironment](#list_deadline-action-GetQueueEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueueFleetAssociation  **
  - **IAM action:**  [deadline:GetQueueFleetAssociation](#list_deadline-action-GetQueueFleetAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueueLimitAssociation  **
  - **IAM action:**  [deadline:GetQueueLimitAssociation](#list_deadline-action-GetQueueLimitAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSession  **
  - **IAM action:**  [deadline:GetSession](#list_deadline-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSessionAction  **
  - **IAM action:**  [deadline:GetSessionAction](#list_deadline-action-GetSessionAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSessionsStatisticsAggregation  **
  - **IAM action:**  [deadline:GetSessionsStatisticsAggregation](#list_deadline-action-GetSessionsStatisticsAggregation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStep  **
  - **IAM action:**  [deadline:GetStep](#list_deadline-action-GetStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStorageProfile  **
  - **IAM action:**  [deadline:GetStorageProfile](#list_deadline-action-GetStorageProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStorageProfileForQueue  **
  - **IAM action:**  [deadline:GetStorageProfileForQueue](#list_deadline-action-GetStorageProfileForQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTask  **
  - **IAM action:**  [deadline:GetTask](#list_deadline-action-GetTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVolume  **
  - **IAM action:**  [deadline:GetVolume](#list_deadline-action-GetVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorker  **
  - **IAM action:**  [deadline:GetWorker](#list_deadline-action-GetWorker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAvailableMeteredProducts  **
  - **IAM action:**  [deadline:ListAvailableMeteredProducts](#list_deadline-action-ListAvailableMeteredProducts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBudgets  **
  - **IAM action:**  [deadline:ListBudgets](#list_deadline-action-ListBudgets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFarmMembers  **
  - **IAM action:**  [deadline:ListFarmMembers](#list_deadline-action-ListFarmMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFarms  **
  - **IAM action:**  [deadline:ListFarms](#list_deadline-action-ListFarms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFleetMembers  **
  - **IAM action:**  [deadline:ListFleetMembers](#list_deadline-action-ListFleetMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFleets  **
  - **IAM action:**  [deadline:ListFleets](#list_deadline-action-ListFleets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobMembers  **
  - **IAM action:**  [deadline:ListJobMembers](#list_deadline-action-ListJobMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobParameterDefinitions  **
  - **IAM action:**  [deadline:ListJobParameterDefinitions](#list_deadline-action-ListJobParameterDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **IAM action:**  [deadline:ListJobs](#list_deadline-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenseEndpoints  **
  - **IAM action:**  [deadline:ListLicenseEndpoints](#list_deadline-action-ListLicenseEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLimits  **
  - **IAM action:**  [deadline:ListLimits](#list_deadline-action-ListLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMeteredProducts  **
  - **IAM action:**  [deadline:ListMeteredProducts](#list_deadline-action-ListMeteredProducts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMonitors  **
  - **IAM action:**  [deadline:ListMonitors](#list_deadline-action-ListMonitors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQueueEnvironments  **
  - **IAM action:**  [deadline:ListQueueEnvironments](#list_deadline-action-ListQueueEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQueueFleetAssociations  **
  - **IAM action:**  [deadline:ListQueueFleetAssociations](#list_deadline-action-ListQueueFleetAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQueueLimitAssociations  **
  - **IAM action:**  [deadline:ListQueueLimitAssociations](#list_deadline-action-ListQueueLimitAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQueueMembers  **
  - **IAM action:**  [deadline:ListQueueMembers](#list_deadline-action-ListQueueMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQueues  **
  - **IAM action:**  [deadline:ListQueues](#list_deadline-action-ListQueues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessionActions  **
  - **IAM action:**  [deadline:ListSessionActions](#list_deadline-action-ListSessionActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessions  **
  - **IAM action:**  [deadline:ListSessions](#list_deadline-action-ListSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessionsForWorker  **
  - **IAM action:**  [deadline:ListSessionsForWorker](#list_deadline-action-ListSessionsForWorker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStepConsumers  **
  - **IAM action:**  [deadline:ListStepConsumers](#list_deadline-action-ListStepConsumers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStepDependencies  **
  - **IAM action:**  [deadline:ListStepDependencies](#list_deadline-action-ListStepDependencies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSteps  **
  - **IAM action:**  [deadline:ListSteps](#list_deadline-action-ListSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStorageProfiles  **
  - **IAM action:**  [deadline:ListStorageProfiles](#list_deadline-action-ListStorageProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStorageProfilesForQueue  **
  - **IAM action:**  [deadline:ListStorageProfilesForQueue](#list_deadline-action-ListStorageProfilesForQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [deadline:ListTagsForResource](#list_deadline-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTasks  **
  - **IAM action:**  [deadline:ListTasks](#list_deadline-action-ListTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVolumes  **
  - **IAM action:**  [deadline:ListVolumes](#list_deadline-action-ListVolumes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkers  **
  - **IAM action:**  [deadline:ListWorkers](#list_deadline-action-ListWorkers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutMeteredProduct  **
  - **IAM action:**  [deadline:PutMeteredProduct](#list_deadline-action-PutMeteredProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchJobs  **
  - **IAM action:**  [deadline:SearchJobs](#list_deadline-action-SearchJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchSteps  **
  - **IAM action:**  [deadline:SearchSteps](#list_deadline-action-SearchSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchTasks  **
  - **IAM action:**  [deadline:SearchTasks](#list_deadline-action-SearchTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchWorkers  **
  - **IAM action:**  [deadline:SearchWorkers](#list_deadline-action-SearchWorkers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartSessionsStatisticsAggregation  **
  - **IAM action:**  [deadline:StartSessionsStatisticsAggregation](#list_deadline-action-StartSessionsStatisticsAggregation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [deadline:TagResource](#list_deadline-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [deadline:UntagResource](#list_deadline-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateBudget  **
  - **IAM action:**  [deadline:UpdateBudget](#list_deadline-action-UpdateBudget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFarm  **
  - **IAM action:**  [deadline:UpdateFarm](#list_deadline-action-UpdateFarm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFleet  **
  - **IAM action:**  [deadline:UpdateFleet](#list_deadline-action-UpdateFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** deadline.amazonaws.com / **Access level:** Write

- **   UpdateJob  **
  - **IAM action:**  [deadline:UpdateJob](#list_deadline-action-UpdateJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLimit  **
  - **IAM action:**  [deadline:UpdateLimit](#list_deadline-action-UpdateLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMonitor  **
  - **IAM action:**  [deadline:UpdateMonitor](#list_deadline-action-UpdateMonitor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** deadline.amazonaws.com / **Access level:** Write

- **   UpdateMonitorSettings  **
  - **IAM action:**  [deadline:UpdateMonitorSettings](#list_deadline-action-UpdateMonitorSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQueue  **
  - **IAM action:**  [deadline:UpdateQueue](#list_deadline-action-UpdateQueue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** deadline.amazonaws.com / **Access level:** Write

- **   UpdateQueueEnvironment  **
  - **IAM action:**  [deadline:UpdateQueueEnvironment](#list_deadline-action-UpdateQueueEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQueueFleetAssociation  **
  - **IAM action:**  [deadline:UpdateQueueFleetAssociation](#list_deadline-action-UpdateQueueFleetAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQueueLimitAssociation  **
  - **IAM action:**  [deadline:UpdateQueueLimitAssociation](#list_deadline-action-UpdateQueueLimitAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSession  **
  - **IAM action:**  [deadline:UpdateSession](#list_deadline-action-UpdateSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStep  **
  - **IAM action:**  [deadline:UpdateStep](#list_deadline-action-UpdateStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStorageProfile  **
  - **IAM action:**  [deadline:UpdateStorageProfile](#list_deadline-action-UpdateStorageProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTask  **
  - **IAM action:**  [deadline:UpdateTask](#list_deadline-action-UpdateTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorker  **
  - **IAM action:**  [deadline:UpdateWorker](#list_deadline-action-UpdateWorker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkerSchedule  **
  - **IAM action:**  [deadline:UpdateWorkerSchedule](#list_deadline-action-UpdateWorkerSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Deadline Cloud
<a name="list_deadline-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateMemberToFarm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssociateMemberToFarm.html)  **
  - **Description:** Grants permission to associate a member to a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:AssociatedMembershipLevel](#list_deadline-deadline_AssociatedMembershipLevel)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:MembershipLevel](#list_deadline-deadline_MembershipLevel)
  - **Access level:** Permissions management, Write

- **   [AssociateMemberToFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssociateMemberToFleet.html)  **
  - **Description:** Grants permission to associate a member to a fleet
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:AssociatedMembershipLevel](#list_deadline-deadline_AssociatedMembershipLevel)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)<br />[deadline:MembershipLevel](#list_deadline-deadline_MembershipLevel)
  - **Access level:** Permissions management, Write

- **   [AssociateMemberToJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssociateMemberToJob.html)  **
  - **Description:** Grants permission to associate a member to a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:AssociatedMembershipLevel](#list_deadline-deadline_AssociatedMembershipLevel)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:MembershipLevel](#list_deadline-deadline_MembershipLevel)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Permissions management, Write

- **   [AssociateMemberToQueue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssociateMemberToQueue.html)  **
  - **Description:** Grants permission to associate a member to a queue
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:AssociatedMembershipLevel](#list_deadline-deadline_AssociatedMembershipLevel)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:MembershipLevel](#list_deadline-deadline_MembershipLevel)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Permissions management, Write

- **   [AssumeFleetRoleForRead](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeFleetRoleForRead.html)  **
  - **Description:** Grants permission to assume a fleet role for read-only access
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write

- **   [AssumeFleetRoleForWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeFleetRoleForWorker.html)  **
  - **Description:** Grants permission to assume a fleet role for a worker
  - **Resource types (\*required):** [worker\*](#list_deadline-resource-worker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write

- **   [AssumeQueueRoleForRead](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeQueueRoleForRead.html)  **
  - **Description:** Grants permission to assume a queue role for read-only access
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [AssumeQueueRoleForUser](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeQueueRoleForUser.html)  **
  - **Description:** Grants permission to assume a queue role for a user
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [AssumeQueueRoleForWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeQueueRoleForWorker.html)  **
  - **Description:** Grants permission to assume a queue role for a worker
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Resource types (\*required):** [worker\*](#list_deadline-resource-worker) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write

- **   [BatchGetJobEntity](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetJobEntity.html)  **
  - **Description:** Grants permission to get a job entity for a worker
  - **Resource types (\*required):** [worker\*](#list_deadline-resource-worker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Read

- **   [CopyJobTemplate](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CopyJobTemplate.html)  **
  - **Description:** Grants permission to copy a job template to an Amazon S3 bucket
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [CreateBudget](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateBudget.html)  **
  - **Description:** Grants permission to create a budget
  - **Resource types (\*required):** [budget\*](#list_deadline-resource-budget)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [CreateFarm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateFarm.html)  **
  - **Description:** Grants permission to create a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [CreateFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateFleet.html)  **
  - **Description:** Grants permission to create a fleet
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write

- **   [CreateJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateJob.html)  **
  - **Description:** Grants permission to create a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [CreateLicenseEndpoint](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateLicenseEndpoint.html)  **
  - **Description:** Grants permission to create a license endpoint for licensed software or products
  - **Resource types (\*required):** [license-endpoint\*](#list_deadline-resource-license-endpoint)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLimit](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateLimit.html)  **
  - **Description:** Grants permission to create a limit for a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [CreateMonitor](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateMonitor.html)  **
  - **Description:** Grants permission to create a monitor
  - **Resource types (\*required):** [monitor\*](#list_deadline-resource-monitor)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)
  - **Access level:** Write

- **   [CreateQueue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateQueue.html)  **
  - **Description:** Grants permission to create a queue
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [CreateQueueEnvironment](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateQueueEnvironment.html)  **
  - **Description:** Grants permission to create a queue environment
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [CreateQueueFleetAssociation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateQueueFleetAssociation.html)  **
  - **Description:** Grants permission to create a queue-fleet association
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [CreateQueueLimitAssociation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateQueueLimitAssociation.html)  **
  - **Description:** Grants permission to create a queue-limit association
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [CreateStorageProfile](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateStorageProfile.html)  **
  - **Description:** Grants permission to create a storage profile for a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [CreateWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateWorker.html)  **
  - **Description:** Grants permission to create a worker
  - **Resource types (\*required):** [worker\*](#list_deadline-resource-worker)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write

- **   [DeleteBudget](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteBudget.html)  **
  - **Description:** Grants permission to delete a budget
  - **Resource types (\*required):** [budget\*](#list_deadline-resource-budget)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [DeleteFarm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteFarm.html)  **
  - **Description:** Grants permission to delete a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [DeleteFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteFleet.html)  **
  - **Description:** Grants permission to delete a fleet
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write

- **   [DeleteLicenseEndpoint](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteLicenseEndpoint.html)  **
  - **Description:** Grants permission to delete a license endpoint
  - **Resource types (\*required):** [license-endpoint\*](#list_deadline-resource-license-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLimit](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteLimit.html)  **
  - **Description:** Grants permission to delete a limit
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [DeleteMeteredProduct](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteMeteredProduct.html)  **
  - **Description:** Grants permission to delete a metered product
  - **Resource types (\*required):** [license-endpoint\*](#list_deadline-resource-license-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMonitor](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteMonitor.html)  **
  - **Description:** Grants permission to delete a monitor
  - **Resource types (\*required):** [monitor\*](#list_deadline-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteQueue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteQueue.html)  **
  - **Description:** Grants permission to delete a queue
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [DeleteQueueEnvironment](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteQueueEnvironment.html)  **
  - **Description:** Grants permission to delete a queue environment
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [DeleteQueueFleetAssociation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteQueueFleetAssociation.html)  **
  - **Description:** Grants permission to delete a queue-fleet association
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [DeleteQueueLimitAssociation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteQueueLimitAssociation.html)  **
  - **Description:** Grants permission to delete a queue-limit association
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [DeleteStorageProfile](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteStorageProfile.html)  **
  - **Description:** Grants permission to delete a storage profile
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [DeleteVolume](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteVolume.html)  **
  - **Description:** Grants permission to delete a volume
  - **Resource types (\*required):** [volume\*](#list_deadline-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write

- **   [DeleteWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteWorker.html)  **
  - **Description:** Grants permission to delete a worker
  - **Resource types (\*required):** [worker\*](#list_deadline-resource-worker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write

- **   [DisassociateMemberFromFarm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DisassociateMemberFromFarm.html)  **
  - **Description:** Grants permission to disassociate a member from a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:AssociatedMembershipLevel](#list_deadline-deadline_AssociatedMembershipLevel)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Permissions management, Write

- **   [DisassociateMemberFromFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DisassociateMemberFromFleet.html)  **
  - **Description:** Grants permission to disassociate a member from a fleet
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:AssociatedMembershipLevel](#list_deadline-deadline_AssociatedMembershipLevel)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Permissions management, Write

- **   [DisassociateMemberFromJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DisassociateMemberFromJob.html)  **
  - **Description:** Grants permission to disassociate a member from a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:AssociatedMembershipLevel](#list_deadline-deadline_AssociatedMembershipLevel)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Permissions management, Write

- **   [DisassociateMemberFromQueue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DisassociateMemberFromQueue.html)  **
  - **Description:** Grants permission to disassociate a member from a queue
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:AssociatedMembershipLevel](#list_deadline-deadline_AssociatedMembershipLevel)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Permissions management, Write

- **   [GetBudget](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetBudget.html)  **
  - **Description:** Grants permission to get a budget
  - **Resource types (\*required):** [budget\*](#list_deadline-resource-budget)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Read

- **   [GetFarm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetFarm.html)  **
  - **Description:** Grants permission to get a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Read

- **   [GetFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetFleet.html)  **
  - **Description:** Grants permission to get a fleet
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Read

- **   [GetJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetJob.html)  **
  - **Description:** Grants permission to get a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetLicenseEndpoint](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetLicenseEndpoint.html)  **
  - **Description:** Grants permission to get a license endpoint
  - **Resource types (\*required):** [license-endpoint\*](#list_deadline-resource-license-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLimit](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetLimit.html)  **
  - **Description:** Grants permission to get a limit
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Read

- **   [GetMonitor](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetMonitor.html)  **
  - **Description:** Grants permission to get a monitor
  - **Resource types (\*required):** [monitor\*](#list_deadline-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMonitorSettings](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetMonitorSettings.html)  **
  - **Description:** Grants permission to get settings for a monitor
  - **Resource types (\*required):** [monitor\*](#list_deadline-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetQueue.html)  **
  - **Description:** Grants permission to get a queue
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetQueueEnvironment](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetQueueEnvironment.html)  **
  - **Description:** Grants permission to get a queue environment
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetQueueFleetAssociation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetQueueFleetAssociation.html)  **
  - **Description:** Grants permission to get a queue-fleet association
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetQueueLimitAssociation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetQueueLimitAssociation.html)  **
  - **Description:** Grants permission to get a queue-limit association
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetSession](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetSession.html)  **
  - **Description:** Grants permission to get a session for a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetSessionAction](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetSessionAction.html)  **
  - **Description:** Grants permission to get a session action for a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetSessionsStatisticsAggregation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetSessionsStatisticsAggregation.html)  **
  - **Description:** Grants permission to get all collected statistics for sessions
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [fleet](#list_deadline-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetStep](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetStep.html)  **
  - **Description:** Grants permission to get a step in a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetStorageProfile](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetStorageProfile.html)  **
  - **Description:** Grants permission to get a storage profile
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Read

- **   [GetStorageProfileForQueue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetStorageProfileForQueue.html)  **
  - **Description:** Grants permission to get a storage profile for a queue
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetTask](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetTask.html)  **
  - **Description:** Grants permission to get a job task
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [GetVolume](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetVolume.html)  **
  - **Description:** Grants permission to get a volume
  - **Resource types (\*required):** [volume\*](#list_deadline-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Read

- **   [GetWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetWorker.html)  **
  - **Description:** Grants permission to get a worker
  - **Resource types (\*required):** [worker\*](#list_deadline-resource-worker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Read

- **   [ListAvailableMeteredProducts](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListAvailableMeteredProducts.html)  **
  - **Description:** Grants permission to list all available metered products within a license endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBudgets](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListBudgets.html)  **
  - **Description:** Grants permission to list all budgets for a farm
  - **Resource types (\*required):** [budget](#list_deadline-resource-budget)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** List

- **   [ListFarmMembers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListFarmMembers.html)  **
  - **Description:** Grants permission to list all members of a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** List

- **   [ListFarms](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListFarms.html)  **
  - **Description:** Grants permission to list all farms
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:PrincipalId](#list_deadline-deadline_PrincipalId)<br />[deadline:RequesterPrincipalId](#list_deadline-deadline_RequesterPrincipalId)
  - **Access level:** List

- **   [ListFleetMembers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListFleetMembers.html)  **
  - **Description:** Grants permission to list all members of a fleet
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** List

- **   [ListFleets](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListFleets.html)  **
  - **Description:** Grants permission to list all fleets
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)<br />[deadline:PrincipalId](#list_deadline-deadline_PrincipalId)<br />[deadline:RequesterPrincipalId](#list_deadline-deadline_RequesterPrincipalId)
  - **Access level:** List

- **   [ListJobMembers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListJobMembers.html)  **
  - **Description:** Grants permission to list all members of a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListJobParameterDefinitions](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListJobParameterDefinitions.html)  **
  - **Description:** Grants permission to get a job's parameter definitions in the job template
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListJobs.html)  **
  - **Description:** Grants permission to list all jobs in a queue
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:PrincipalId](#list_deadline-deadline_PrincipalId)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)<br />[deadline:RequesterPrincipalId](#list_deadline-deadline_RequesterPrincipalId)
  - **Access level:** List

- **   [ListLicenseEndpoints](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListLicenseEndpoints.html)  **
  - **Description:** Grants permission to list all license endpoints
  - **Resource types (\*required):** [license-endpoint\*](#list_deadline-resource-license-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLimits](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListLimits.html)  **
  - **Description:** Grants permission to list all limits in a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** List

- **   [ListMeteredProducts](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListMeteredProducts.html)  **
  - **Description:** Grants permission to list all metered products in a license endpoint
  - **Resource types (\*required):** [license-endpoint\*](#list_deadline-resource-license-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMonitors](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListMonitors.html)  **
  - **Description:** Grants permission to list all monitors
  - **Resource types (\*required):** [monitor\*](#list_deadline-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListQueueEnvironments](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListQueueEnvironments.html)  **
  - **Description:** Grants permission to list all queue environments to which a queue is associated
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListQueueFleetAssociations](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListQueueFleetAssociations.html)  **
  - **Description:** Grants permission to list all queue-fleet associations
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [fleet](#list_deadline-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListQueueLimitAssociations](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListQueueLimitAssociations.html)  **
  - **Description:** Grants permission to list all queue-limit associations
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListQueueMembers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListQueueMembers.html)  **
  - **Description:** Grants permission to list all members in a queue
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListQueues](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListQueues.html)  **
  - **Description:** Grants permission to list all queues on a farm
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:PrincipalId](#list_deadline-deadline_PrincipalId)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)<br />[deadline:RequesterPrincipalId](#list_deadline-deadline_RequesterPrincipalId)
  - **Access level:** List

- **   [ListSessionActions](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListSessionActions.html)  **
  - **Description:** Grants permission to list all session actions for a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListSessions](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListSessions.html)  **
  - **Description:** Grants permission to list all sessions for a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListSessionsForWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListSessionsForWorker.html)  **
  - **Description:** Grants permission to list all sessions for a worker
  - **Resource types (\*required):** [worker](#list_deadline-resource-worker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** List

- **   [ListStepConsumers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListStepConsumers.html)  **
  - **Description:** Grants permission to list the step consumers for a job step
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListStepDependencies](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListStepDependencies.html)  **
  - **Description:** Grants permission to list dependencies for a job step
  - **Resource types (\*required):** [job](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListSteps](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListSteps.html)  **
  - **Description:** Grants permission to list all steps for a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListStorageProfiles](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListStorageProfiles.html)  **
  - **Description:** Grants permission to list all storage profiles in a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** List

- **   [ListStorageProfilesForQueue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListStorageProfilesForQueue.html)  **
  - **Description:** Grants permission to list all storage profiles in a queue
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags on specified Deadline Cloud resources
  - **Resource types (\*required):** [budget](#list_deadline-resource-budget) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [farm](#list_deadline-resource-farm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [fleet](#list_deadline-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [job](#list_deadline-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Resource types (\*required):** [license-endpoint](#list_deadline-resource-license-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)
  - **Resource types (\*required):** [monitor](#list_deadline-resource-monitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Resource types (\*required):** [volume](#list_deadline-resource-volume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [worker](#list_deadline-resource-worker) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Read

- **   [ListTasks](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListTasks.html)  **
  - **Description:** Grants permission to list all tasks for a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** List

- **   [ListVolumes](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListVolumes.html)  **
  - **Description:** Grants permission to list volumes
  - **Resource types (\*required):** [volume\*](#list_deadline-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** List

- **   [ListWorkers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListWorkers.html)  **
  - **Description:** Grants permission to list all workers in a fleet
  - **Resource types (\*required):** [worker\*](#list_deadline-resource-worker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** List

- **   [PutMeteredProduct](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_PutMeteredProduct.html)  **
  - **Description:** Grants permission to add a metered product to a license endpoint
  - **Resource types (\*required):** [license-endpoint\*](#list_deadline-resource-license-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchJobs](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchJobs.html)  **
  - **Description:** Grants permission to search for jobs in multiple queues
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [SearchSteps](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchSteps.html)  **
  - **Description:** Grants permission to search the steps within a single job or to search the steps for multiple queues
  - **Resource types (\*required):** [job](#list_deadline-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [SearchTasks](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchTasks.html)  **
  - **Description:** Grants permission to search the tasks within a single job or to search the tasks for multiple queues
  - **Resource types (\*required):** [job](#list_deadline-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [SearchWorkers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchWorkers.html)  **
  - **Description:** Grants permission to search for workers in multiple fleets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartSessionsStatisticsAggregation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StartSessionsStatisticsAggregation.html)  **
  - **Description:** Grants permission to get all collected statistics for sessions
  - **Resource types (\*required):** [fleet](#list_deadline-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or overwrite one or more tags for the specified Deadline Cloud resource
  - **Resource types (\*required):** [budget](#list_deadline-resource-budget) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [farm](#list_deadline-resource-farm) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [fleet](#list_deadline-resource-fleet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [job](#list_deadline-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Resource types (\*required):** [license-endpoint](#list_deadline-resource-license-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)
  - **Resource types (\*required):** [monitor](#list_deadline-resource-monitor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Resource types (\*required):** [volume](#list_deadline-resource-volume) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [worker](#list_deadline-resource-worker) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_deadline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:CalledAction](#list_deadline-deadline_CalledAction)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to disassociate one or more tags from the specified Deadline Cloud resource
  - **Resource types (\*required):** [budget](#list_deadline-resource-budget) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [farm](#list_deadline-resource-farm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [fleet](#list_deadline-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [job](#list_deadline-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Resource types (\*required):** [license-endpoint](#list_deadline-resource-license-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)
  - **Resource types (\*required):** [monitor](#list_deadline-resource-monitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)
  - **Resource types (\*required):** [queue](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Resource types (\*required):** [volume](#list_deadline-resource-volume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [worker](#list_deadline-resource-worker) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_deadline-aws_TagKeys)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Tagging, Write

- **   [UpdateBudget](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateBudget.html)  **
  - **Description:** Grants permission to update a budget
  - **Resource types (\*required):** [budget\*](#list_deadline-resource-budget)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [UpdateFarm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateFarm.html)  **
  - **Description:** Grants permission to update a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [UpdateFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateFleet.html)  **
  - **Description:** Grants permission to update a fleet
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write

- **   [UpdateJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateJob.html)  **
  - **Description:** Grants permission to update a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [UpdateLimit](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateLimit.html)  **
  - **Description:** Grants permission to update a limit for a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [UpdateMonitor](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateMonitor.html)  **
  - **Description:** Grants permission to update a monitor
  - **Resource types (\*required):** [monitor\*](#list_deadline-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMonitorSettings](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateMonitorSettings.html)  **
  - **Description:** Grants permission to update settings for a monitor
  - **Resource types (\*required):** [monitor\*](#list_deadline-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateQueue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateQueue.html)  **
  - **Description:** Grants permission to update a queue
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [UpdateQueueEnvironment](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateQueueEnvironment.html)  **
  - **Description:** Grants permission to update a queue environment
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [UpdateQueueFleetAssociation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateQueueFleetAssociation.html)  **
  - **Description:** Grants permission to update a queue-fleet association
  - **Resource types (\*required):** [fleet\*](#list_deadline-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [UpdateQueueLimitAssociation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateQueueLimitAssociation.html)  **
  - **Description:** Grants permission to update a queue-limit association
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Resource types (\*required):** [queue\*](#list_deadline-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [UpdateSession](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateSession.html)  **
  - **Description:** Grants permission to update a session for a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [UpdateStep](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateStep.html)  **
  - **Description:** Grants permission to update a step for a job
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [UpdateStorageProfile](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateStorageProfile.html)  **
  - **Description:** Grants permission to update a storage profile for a farm
  - **Resource types (\*required):** [farm\*](#list_deadline-resource-farm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)
  - **Access level:** Write

- **   [UpdateTask](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateTask.html)  **
  - **Description:** Grants permission to update a task
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Write

- **   [UpdateWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateWorker.html)  **
  - **Description:** Grants permission to update a worker
  - **Resource types (\*required):** [worker\*](#list_deadline-resource-worker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write

- **   [UpdateWorkerSchedule](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateWorkerSchedule.html)  **
  - **Description:** Grants permission to update the schedule for a worker
  - **Resource types (\*required):** [worker\*](#list_deadline-resource-worker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels)
  - **Access level:** Write



## Permission-only actions for AWS Deadline Cloud
<a name="list_deadline-permission-only-actions"></a>

The following actions are defined by AWS Deadline Cloud but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetApplicationVersion](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/deadline-cloud-jobs.html)  **
  - **Description:** Grants permission to get the latest version of an application
  - **Resource types (\*required):** [monitor\*](#list_deadline-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJobTemplate](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/working-with-deadline-monitor.html)  **
  - **Description:** Grants permission to read job template
  - **Resource types (\*required):** [job\*](#list_deadline-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels)
  - **Access level:** Read



## Resource types defined by AWS Deadline Cloud
<a name="list_deadline-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [budget](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/manage-costs.html)  | arn:${Partition}:deadline:${Region}:${Account}:farm/${FarmId}/budget/${BudgetId} | [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels) | 
|  [farm](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/farms.html)  | arn:${Partition}:deadline:${Region}:${Account}:farm/${FarmId} | [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels) | 
|  [fleet](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/manage-fleets.html)  | arn:${Partition}:deadline:${Region}:${Account}:farm/${FarmId}/fleet/${FleetId} | [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels) | 
|  [job](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/deadline-cloud-jobs.html)  | arn:${Partition}:deadline:${Region}:${Account}:farm/${FarmId}/queue/${QueueId}/job/${JobId} | [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:JobMembershipLevels](#list_deadline-deadline_JobMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels) | 
|  [license-endpoint](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/cmf-ubl.html)  | arn:${Partition}:deadline:${Region}:${Account}:license-endpoint/${LicenseEndpointId} | [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_) | 
|  [monitor](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/working-with-deadline-monitor.html)  | arn:${Partition}:deadline:${Region}:${Account}:monitor/${MonitorId} | [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_) | 
|  [queue](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/queues.html)  | arn:${Partition}:deadline:${Region}:${Account}:farm/${FarmId}/queue/${QueueId} | [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:QueueMembershipLevels](#list_deadline-deadline_QueueMembershipLevels) | 
|  [volume](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/volumes.html)  | arn:${Partition}:deadline:${Region}:${Account}:farm/${FarmId}/fleet/${FleetId}/volume/${VolumeId} | [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels) | 
|  [worker](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam.html)  | arn:${Partition}:deadline:${Region}:${Account}:farm/${FarmId}/fleet/${FleetId}/worker/${WorkerId} | [aws:ResourceTag/${TagKey}](#list_deadline-aws_ResourceTag___TagKey_)<br />[deadline:FarmMembershipLevels](#list_deadline-deadline_FarmMembershipLevels)<br />[deadline:FleetMembershipLevels](#list_deadline-deadline_FleetMembershipLevels) | 

## Condition keys for AWS Deadline Cloud
<a name="list_deadline-policy-keys"></a>

AWS Deadline Cloud defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [deadline:AssociatedMembershipLevel](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam-service-with-iam.html)  | Filters access by the associated membership level of the principal provided in the request | String | 
|   [deadline:CalledAction](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam-service-with-iam.html)  | Filters access by the allowed action in the request | String | 
|   [deadline:FarmMembershipLevels](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam-service-with-iam.html)  | Filters access by membership levels on the farm | ArrayOfString | 
|   [deadline:FleetMembershipLevels](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam-service-with-iam.html)  | Filters access by membership levels on the fleet | ArrayOfString | 
|   [deadline:JobMembershipLevels](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam-service-with-iam.html)  | Filters access by membership levels on the job | ArrayOfString | 
|   [deadline:MembershipLevel](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam-service-with-iam.html)  | Filters access by the membership level passed in the request | String | 
|   [deadline:PrincipalId](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam-service-with-iam.html)  | Filters access by the principle ID provided in the request | String | 
|   [deadline:QueueMembershipLevels](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam-service-with-iam.html)  | Filters access by membership levels on the queue | ArrayOfString | 
|   [deadline:RequesterPrincipalId](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security-iam-service-with-iam.html)  | Filters access by the user calling the Deadline Cloud API | String | 