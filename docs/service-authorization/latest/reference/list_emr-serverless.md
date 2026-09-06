

# Actions, resources, and condition keys for Amazon EMR Serverless
<a name="list_emr-serverless"></a>

Amazon EMR Serverless (service prefix: `emr-serverless`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/emr-serverless/emr-serverless.json) for this service.

**Topics**
+ [API operations defined by Amazon EMR Serverless](#list_emr-serverless-operations)
+ [Actions defined by Amazon EMR Serverless](#list_emr-serverless-actions-as-permissions)
+ [Permission-only actions for Amazon EMR Serverless](#list_emr-serverless-permission-only-actions)
+ [Resource types defined by Amazon EMR Serverless](#list_emr-serverless-resources-for-iam-policies)
+ [Condition keys for Amazon EMR Serverless](#list_emr-serverless-policy-keys)

## API operations defined by Amazon EMR Serverless
<a name="list_emr-serverless-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_emr-serverless-actions-as-permissions).




- **   CancelJobRun  **
  - **IAM action:**  [emr-serverless:CancelJobRun](#list_emr-serverless-action-CancelJobRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [emr-serverless:CreateApplication](#list_emr-serverless-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [emr-serverless:TagResource](#list_emr-serverless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteApplication  **
  - **IAM action:**  [emr-serverless:DeleteApplication](#list_emr-serverless-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [emr-serverless:GetApplication](#list_emr-serverless-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDashboardForJobRun  **
  - **IAM action:**  [emr-serverless:AccessSystemProfileLogs](#list_emr-serverless-action-AccessSystemProfileLogs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [emr-serverless:GetDashboardForJobRun](#list_emr-serverless-action-GetDashboardForJobRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:GetDatabases](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-databases.html#aws-glue-api-catalog-databases-GetDatabases)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:SearchTables](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-SearchTables)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetJobRun  **
  - **IAM action:**  [emr-serverless:GetJobRun](#list_emr-serverless-action-GetJobRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceDashboard  **
  - **IAM action:**  [emr-serverless:GetResourceDashboard](#list_emr-serverless-action-GetResourceDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSession  **
  - **IAM action:**  [emr-serverless:GetSession](#list_emr-serverless-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSessionEndpoint  **
  - **IAM action:**  [emr-serverless:GetSessionEndpoint](#list_emr-serverless-action-GetSessionEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplications  **
  - **IAM action:**  [emr-serverless:ListApplications](#list_emr-serverless-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobRunAttempts  **
  - **IAM action:**  [emr-serverless:ListJobRunAttempts](#list_emr-serverless-action-ListJobRunAttempts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobRuns  **
  - **IAM action:**  [emr-serverless:ListJobRuns](#list_emr-serverless-action-ListJobRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessions  **
  - **IAM action:**  [emr-serverless:ListSessions](#list_emr-serverless-action-ListSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [emr-serverless:ListTagsForResource](#list_emr-serverless-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartApplication  **
  - **IAM action:**  [emr-serverless:StartApplication](#list_emr-serverless-action-StartApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartJobRun  **
  - **IAM action:**  [emr-serverless:StartJobRun](#list_emr-serverless-action-StartJobRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [emr-serverless:TagResource](#list_emr-serverless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** emr-serverless.amazonaws.com / **Access level:** Write

- **   StartSession  **
  - **IAM action:**  [emr-serverless:StartSession](#list_emr-serverless-action-StartSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [emr-serverless:TagResource](#list_emr-serverless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** emr-serverless.amazonaws.com / **Access level:** Write

- **   StopApplication  **
  - **IAM action:**  [emr-serverless:StopApplication](#list_emr-serverless-action-StopApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [emr-serverless:TagResource](#list_emr-serverless-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TerminateSession  **
  - **IAM action:**  [emr-serverless:TerminateSession](#list_emr-serverless-action-TerminateSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [emr-serverless:UntagResource](#list_emr-serverless-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **IAM action:**  [emr-serverless:UpdateApplication](#list_emr-serverless-action-UpdateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon EMR Serverless
<a name="list_emr-serverless-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_CancelJobRun.html)  **
  - **Description:** Grants permission to cancel a job run
  - **Resource types (\*required):** [jobRun\*](#list_emr-serverless-resource-jobRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an Application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-serverless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_emr-serverless-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html)  **
  - **Description:** Grants permission to get application
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDashboardForJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetDashboardForJobRun.html)  **
  - **Description:** Grants permission to get job run dashboard
  - **Resource types (\*required):** [jobRun\*](#list_emr-serverless-resource-jobRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetJobRun.html)  **
  - **Description:** Grants permission to get a job run
  - **Resource types (\*required):** [jobRun\*](#list_emr-serverless-resource-jobRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceDashboard](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetResourceDashboard.html)  **
  - **Description:** Grants permission to get the resource dashboard
  - **Resource types (\*required):** [session\*](#list_emr-serverless-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSession](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetSession.html)  **
  - **Description:** Grants permission to get details about a session
  - **Resource types (\*required):** [session\*](#list_emr-serverless-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSessionEndpoint](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetSessionEndpoint.html)  **
  - **Description:** Grants permission to get the endpoint URL and authentication token for connecting to a session
  - **Resource types (\*required):** [session\*](#list_emr-serverless-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplications](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListApplications.html)  **
  - **Description:** Grants permission to list applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobRunAttempts](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListJobRunAttempts.html)  **
  - **Description:** Grants permission to list job run attempts associated with a job run
  - **Resource types (\*required):** [jobRun\*](#list_emr-serverless-resource-jobRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListJobRuns](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListJobRuns.html)  **
  - **Description:** Grants permission to list job runs associated with an application
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSessions](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListSessions.html)  **
  - **Description:** Grants permission to list sessions associated with an application
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for the specified resource
  - **Resource types (\*required):** [application](#list_emr-serverless-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [jobRun](#list_emr-serverless-resource-jobRun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [session](#list_emr-serverless-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StartApplication.html)  **
  - **Description:** Grants permission to Start an application
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StartJobRun.html)  **
  - **Description:** Grants permission to start a job run
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-serverless-aws_TagKeys)
  - **Access level:** Write

- **   [StartSession](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StartSession.html)  **
  - **Description:** Grants permission to start a session in an application
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-serverless-aws_TagKeys)
  - **Access level:** Write

- **   [StopApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StopApplication.html)  **
  - **Description:** Grants permission to Stop an application
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag the specified resource
  - **Resource types (\*required):** [application](#list_emr-serverless-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-serverless-aws_TagKeys)
  - **Resource types (\*required):** [jobRun](#list_emr-serverless-resource-jobRun) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-serverless-aws_TagKeys)
  - **Resource types (\*required):** [session](#list_emr-serverless-resource-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-serverless-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TerminateSession](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_TerminateSession.html)  **
  - **Description:** Grants permission to terminate a session
  - **Resource types (\*required):** [session\*](#list_emr-serverless-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag the specified resource
  - **Resource types (\*required):** [application](#list_emr-serverless-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-serverless-aws_TagKeys)
  - **Resource types (\*required):** [jobRun](#list_emr-serverless-resource-jobRun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-serverless-aws_TagKeys)
  - **Resource types (\*required):** [session](#list_emr-serverless-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-serverless-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to Update an application
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon EMR Serverless
<a name="list_emr-serverless-permission-only-actions"></a>

The following actions are defined by Amazon EMR Serverless but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AccessInteractiveEndpoints](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/interactive-workloads.html)  **
  - **Description:** Grants permission to execute interactive workloads on an application
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AccessLivyEndpoints](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/interactive-workloads-livy-endpoints.html)  **
  - **Description:** Grants permission to execute interactive workloads on Livy Endpoint enabled on an EMR Serverless Application
  - **Resource types (\*required):** [application\*](#list_emr-serverless-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AccessSystemProfileLogs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/logging-monitoring.html)  **
  - **Description:** Grants permission to access system profile logs
  - **Resource types (\*required):** [jobRun\*](#list_emr-serverless-resource-jobRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon EMR Serverless
<a name="list_emr-serverless-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html)  | arn:${Partition}:emr-serverless:${Region}:${Account}:/applications/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_) | 
|  [jobRun](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html)  | arn:${Partition}:emr-serverless:${Region}:${Account}:/applications/${ApplicationId}/jobruns/${JobRunId} | [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_) | 
|  [session](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html)  | arn:${Partition}:emr-serverless:${Region}:${Account}:/applications/${ApplicationId}/sessions/${SessionId} | [aws:ResourceTag/${TagKey}](#list_emr-serverless-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon EMR Serverless
<a name="list_emr-serverless-policy-keys"></a>

Amazon EMR Serverless defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 