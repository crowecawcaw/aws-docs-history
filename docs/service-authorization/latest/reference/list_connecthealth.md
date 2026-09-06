

# Actions, resources, and condition keys for Amazon Connect Health
<a name="list_connecthealth"></a>

Amazon Connect Health (service prefix: `health-agent`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/connecthealth/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/connecthealth/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/connecthealth/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/health-agent/health-agent.json) for this service.

**Topics**
+ [API operations defined by Amazon Connect Health](#list_connecthealth-operations)
+ [Actions defined by Amazon Connect Health](#list_connecthealth-actions-as-permissions)
+ [Permission-only actions for Amazon Connect Health](#list_connecthealth-permission-only-actions)
+ [Resource types defined by Amazon Connect Health](#list_connecthealth-resources-for-iam-policies)
+ [Condition keys for Amazon Connect Health](#list_connecthealth-policy-keys)

## API operations defined by Amazon Connect Health
<a name="list_connecthealth-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_connecthealth-actions-as-permissions).




- **   ActivateSubscription  **
  - **IAM action:**  [health-agent:ActivateSubscription](#list_connecthealth-action-ActivateSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDomain  **
  - **IAM action:**  [health-agent:CreateDomain](#list_connecthealth-action-CreateDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [health-agent:TagResource](#list_connecthealth-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** health-agent.amazonaws.com / **Access level:** Write

- **   CreateSubscription  **
  - **IAM action:**  [health-agent:CreateSubscription](#list_connecthealth-action-CreateSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeactivateSubscription  **
  - **IAM action:**  [health-agent:DeactivateSubscription](#list_connecthealth-action-DeactivateSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomain  **
  - **IAM action:**  [health-agent:DeleteDomain](#list_connecthealth-action-DeleteDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDomain  **
  - **IAM action:**  [health-agent:GetDomain](#list_connecthealth-action-GetDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMedicalScribeListeningSession  **
  - **IAM action:**  [health-agent:GetMedicalScribeListeningSession](#list_connecthealth-action-GetMedicalScribeListeningSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPatientInsightsJob  **
  - **IAM action:**  [health-agent:GetPatientInsightsJob](#list_connecthealth-action-GetPatientInsightsJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSubscription  **
  - **IAM action:**  [health-agent:GetSubscription](#list_connecthealth-action-GetSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDomains  **
  - **IAM action:**  [health-agent:ListDomains](#list_connecthealth-action-ListDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscriptions  **
  - **IAM action:**  [health-agent:ListSubscriptions](#list_connecthealth-action-ListSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [health-agent:ListTagsForResource](#list_connecthealth-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartMedicalScribeListeningSession  **
  - **IAM action:**  [health-agent:StartMedicalScribeListeningSession](#list_connecthealth-action-StartMedicalScribeListeningSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartPatientInsightsJob  **
  - **IAM action:**  [health-agent:StartPatientInsightsJob](#list_connecthealth-action-StartPatientInsightsJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [health-agent:TagResource](#list_connecthealth-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [health-agent:UntagResource](#list_connecthealth-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by Amazon Connect Health
<a name="list_connecthealth-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivateSubscription](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ActivateSubscription.html)  **
  - **Description:** Grants permission to activate a subscription to enable billing for a user
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Subscription\*](#list_connecthealth-resource-Subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDomain](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CreateDomain.html)  **
  - **Description:** Grants permission to create a new domain for managing HealthAgent resources
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_connecthealth-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_connecthealth-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSubscription](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CreateSubscription.html)  **
  - **Description:** Grants permission to create a new subscription within a domain for billing and user management
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Subscription\*](#list_connecthealth-resource-Subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeactivateSubscription](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_DeactivateSubscription.html)  **
  - **Description:** Grants permission to deactivate a subscription to stop billing for a user
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Subscription\*](#list_connecthealth-resource-Subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomain](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete a domain and all associated resources
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDomain](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetDomain.html)  **
  - **Description:** Grants permission to retrieve information about a domain
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomainAnalytics](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetDomainAnalytics.html)  **
  - **Description:** Grants permission to retrieve aggregated analytics for a domain
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMedicalScribeListeningSession](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetMedicalScribeListeningSession.html)  **
  - **Description:** Grants permission to retrieve details about an existing Medical Scribe listening session
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Subscription\*](#list_connecthealth-resource-Subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPatientInsightsJob](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetPatientInsightsJob.html)  **
  - **Description:** Grants permission to get details of a started patient insights job
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PatientInsightsJob\*](#list_connecthealth-resource-PatientInsightsJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSubscription](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetSubscription.html)  **
  - **Description:** Grants permission to retrieve information about a subscription
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Subscription\*](#list_connecthealth-resource-Subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDomains](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ListDomains.html)  **
  - **Description:** Grants permission to list domains for a given account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSessionRecords](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ListSessionRecords.html)  **
  - **Description:** Grants permission to list session records for a domain
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSubscriptions](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ListSubscriptions.html)  **
  - **Description:** Grants permission to list all subscriptions within a domain
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for the specified resource
  - **Resource types (\*required):** [Domain](#list_connecthealth-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [StartMedicalScribeListeningSession](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_StartMedicalScribeListeningSession.html)  **
  - **Description:** Grants permission to start a new Medical Scribe listening session for real-time audio transcription
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Subscription\*](#list_connecthealth-resource-Subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartPatientInsightsJob](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_StartPatientInsightsJob.html)  **
  - **Description:** Grants permission to start a new patient insights job
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PatientInsightsJob\*](#list_connecthealth-resource-PatientInsightsJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add the specified tags to the specified resource
  - **Resource types (\*required):** [Domain](#list_connecthealth-resource-Domain)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_connecthealth-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connecthealth-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the tags identified by the TagKeys list from a resource
  - **Resource types (\*required):** [Domain](#list_connecthealth-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connecthealth-aws_TagKeys)
  - **Access level:** Tagging, Write



## Permission-only actions for Amazon Connect Health
<a name="list_connecthealth-permission-only-actions"></a>

The following actions are defined by Amazon Connect Health but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CancelAppointment](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to cancel an appointment
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAgent](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to create a new agent with an initial version in DRAFT state
  - **Resource types (\*required):** [Agent\*](#list_connecthealth-resource-Agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateIntegration](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to create a new integration for a domain
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSession](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to create a new session with specified agent configurations
  - **Resource types (\*required):** [Agent\*](#list_connecthealth-resource-Agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Session\*](#list_connecthealth-resource-Session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgent](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to delete an agent configuration and all its versions
  - **Resource types (\*required):** [Agent\*](#list_connecthealth-resource-Agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to delete an integration
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAgent](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to retrieve an agent configuration, defaulting to the most recent version if not specified
  - **Resource types (\*required):** [Agent\*](#list_connecthealth-resource-Agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCareTeamProvider](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to retrieve the care team provider of a patient
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntegration](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to get an existing integration
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPatient](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to retrieve patient information
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPractitioner](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to retrieve practitioner information
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSessionContext](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to retrieve structured session context including attributes and collected data
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Session\*](#list_connecthealth-resource-Session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeAgent](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to invoke an agent within a session with streaming response support
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Session\*](#list_connecthealth-resource-Session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAgents](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to list all agents in a domain
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppointmentSlots](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to list available appointment slots
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListIntegrations](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to list integrations for a domain
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPatientAppointments](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to list patient appointments
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPatientInsuranceCoverages](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to list patient insurance coverages
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPatientMedications](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to list patient medications
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListProviders](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to retrieve active providers available for scheduling appointments with a patient
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [MatchPatient](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to match a patient
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PublishAgent](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to publish an agent configuration version
  - **Resource types (\*required):** [Agent\*](#list_connecthealth-resource-Agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RescheduleAppointment](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to reschedule an appointment
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResetPassword](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to reset a patient MyChart password via email or SMS
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ScheduleAppointment](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to schedule an appointment for a patient
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SubmitMedicationRenewal](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to submit a medication renewal for a patient
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgent](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to update a draft agent configuration, creating a new draft version if none exists
  - **Resource types (\*required):** [Agent\*](#list_connecthealth-resource-Agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIntegration](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to update an existing integration
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration\*](#list_connecthealth-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSession](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  **
  - **Description:** Grants permission to update session attributes such as departmentId and appointmentType
  - **Resource types (\*required):** [Domain\*](#list_connecthealth-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Session\*](#list_connecthealth-resource-Session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Connect Health
<a name="list_connecthealth-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Agent](https://docs.aws.amazon.com/connecthealth/latest/userguide/agent-customization.html)  | arn:${Partition}:health-agent:${Region}:${Account}:domain/${DomainId}/agent/${AgentId} | [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_) | 
|  [Domain](https://docs.aws.amazon.com/connecthealth/latest/userguide/setting-up.html#setting-up-create-domain)  | arn:${Partition}:health-agent:${Region}:${Account}:domain/${DomainId} | [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_) | 
|  [Integration](https://docs.aws.amazon.com/connecthealth/latest/userguide/configuring-testing-pe-agents.html)  | arn:${Partition}:health-agent:${Region}:${Account}:domain/${DomainId}/integration/${IntegrationId} | [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_) | 
|  [PatientInsightsJob](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-insights.html)  | arn:${Partition}:health-agent:${Region}:${Account}:domain/${DomainId}/patient-insights-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_) | 
|  [Session](https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html)  | arn:${Partition}:health-agent:${Region}:${Account}:domain/${DomainId}/session/${SessionId} | [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_) | 
|  [Subscription](https://docs.aws.amazon.com/connecthealth/latest/userguide/ambient-documentation.html#al-subscription-management)  | arn:${Partition}:health-agent:${Region}:${Account}:domain/${DomainId}/subscription/${SubscriptionId} | [aws:ResourceTag/${TagKey}](#list_connecthealth-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Connect Health
<a name="list_connecthealth-policy-keys"></a>

Amazon Connect Health defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/connecthealth/latest/userguide/security-iam-service-with-iam.htmlsecurity-iam-service-with-iam.html#security-iam-service-with-iam-tags)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/connecthealth/latest/userguide/security-iam-service-with-iam.htmlsecurity-iam-service-with-iam.html#security-iam-service-with-iam-tags)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/connecthealth/latest/userguide/security-iam-service-with-iam.htmlsecurity-iam-service-with-iam.html#security-iam-service-with-iam-tags)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 