

# Actions, resources, and condition keys for Amazon DataZone
<a name="list_datazone"></a>

Amazon DataZone (service prefix: `datazone`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/datazone/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/datazone/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/datazone/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/datazone/datazone.json) for this service.

**Topics**
+ [API operations defined by Amazon DataZone](#list_datazone-operations)
+ [Actions defined by Amazon DataZone](#list_datazone-actions-as-permissions)
+ [Permission-only actions for Amazon DataZone](#list_datazone-permission-only-actions)
+ [Resource types defined by Amazon DataZone](#list_datazone-resources-for-iam-policies)
+ [Condition keys for Amazon DataZone](#list_datazone-policy-keys)

## API operations defined by Amazon DataZone
<a name="list_datazone-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_datazone-actions-as-permissions).




- **   AcceptPredictions  **
  - **IAM action:**  [datazone:AcceptPredictions](#list_datazone-action-AcceptPredictions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AcceptSubscriptionRequest  **
  - **IAM action:**  [datazone:AcceptSubscriptionRequest](#list_datazone-action-AcceptSubscriptionRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddEntityOwner  **
  - **IAM action:**  [datazone:AddEntityOwner](#list_datazone-action-AddEntityOwner) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddPolicyGrant  **
  - **IAM action:**  [datazone:AddPolicyGrant](#list_datazone-action-AddPolicyGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AssociateEnvironmentRole  **
  - **IAM action:**  [datazone:AssociateEnvironmentRole](#list_datazone-action-AssociateEnvironmentRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   AssociateGovernedTerms  **
  - **IAM action:**  [datazone:AssociateGovernedTerms](#list_datazone-action-AssociateGovernedTerms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetAttributesMetadata  **
  - **IAM action:**  [datazone:BatchGetAttributesMetadata](#list_datazone-action-BatchGetAttributesMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchPutAttributesMetadata  **
  - **IAM action:**  [datazone:BatchPutAttributesMetadata](#list_datazone-action-BatchPutAttributesMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelMetadataGenerationRun  **
  - **IAM action:**  [datazone:CancelMetadataGenerationRun](#list_datazone-action-CancelMetadataGenerationRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelSubscription  **
  - **IAM action:**  [datazone:CancelSubscription](#list_datazone-action-CancelSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccountPool  **
  - **IAM action:**  [datazone:CreateAccountPool](#list_datazone-action-CreateAccountPool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   CreateAsset  **
  - **IAM action:**  [datazone:CreateAsset](#list_datazone-action-CreateAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAssetFilter  **
  - **IAM action:**  [datazone:CreateAssetFilter](#list_datazone-action-CreateAssetFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAssetRevision  **
  - **IAM action:**  [datazone:CreateAssetRevision](#list_datazone-action-CreateAssetRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAssetType  **
  - **IAM action:**  [datazone:CreateAssetType](#list_datazone-action-CreateAssetType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnection  **
  - **IAM action:**  [datazone:CreateConnection](#list_datazone-action-CreateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataProduct  **
  - **IAM action:**  [datazone:CreateDataProduct](#list_datazone-action-CreateDataProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataProductRevision  **
  - **IAM action:**  [datazone:CreateDataProductRevision](#list_datazone-action-CreateDataProductRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataSource  **
  - **IAM action:**  [datazone:CreateDataSource](#list_datazone-action-CreateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   CreateDomain  **
  - **IAM action:**  [datazone:CreateDomain](#list_datazone-action-CreateDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datazone:TagResource](#list_datazone-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   CreateDomainUnit  **
  - **IAM action:**  [datazone:CreateDomainUnit](#list_datazone-action-CreateDomainUnit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEnvironment  **
  - **IAM action:**  [datazone:CreateEnvironment](#list_datazone-action-CreateEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEnvironmentAction  **
  - **IAM action:**  [datazone:CreateEnvironmentAction](#list_datazone-action-CreateEnvironmentAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEnvironmentBlueprint  **
  - **IAM action:**  [datazone:CreateEnvironmentBlueprint](#list_datazone-action-CreateEnvironmentBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEnvironmentProfile  **
  - **IAM action:**  [datazone:CreateEnvironmentProfile](#list_datazone-action-CreateEnvironmentProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateFormType  **
  - **IAM action:**  [datazone:CreateFormType](#list_datazone-action-CreateFormType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGlossary  **
  - **IAM action:**  [datazone:CreateGlossary](#list_datazone-action-CreateGlossary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGlossaryTerm  **
  - **IAM action:**  [datazone:CreateGlossaryTerm](#list_datazone-action-CreateGlossaryTerm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGroupProfile  **
  - **IAM action:**  [datazone:CreateGroupProfile](#list_datazone-action-CreateGroupProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateListingChangeSet  **
  - **IAM action:**  [datazone:CreateListingChangeSet](#list_datazone-action-CreateListingChangeSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateNotebook  **
  - **IAM action:**  [datazone:CreateNotebook](#list_datazone-action-CreateNotebook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProject  **
  - **IAM action:**  [datazone:CreateProject](#list_datazone-action-CreateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   CreateProjectMembership  **
  - **IAM action:**  [datazone:CreateProjectMembership](#list_datazone-action-CreateProjectMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProjectProfile  **
  - **IAM action:**  [datazone:CreateProjectProfile](#list_datazone-action-CreateProjectProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRule  **
  - **IAM action:**  [datazone:CreateRule](#list_datazone-action-CreateRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSubscriptionGrant  **
  - **IAM action:**  [datazone:CreateSubscriptionGrant](#list_datazone-action-CreateSubscriptionGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSubscriptionRequest  **
  - **IAM action:**  [datazone:CreateSubscriptionRequest](#list_datazone-action-CreateSubscriptionRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSubscriptionTarget  **
  - **IAM action:**  [datazone:CreateSubscriptionTarget](#list_datazone-action-CreateSubscriptionTarget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   CreateUserProfile  **
  - **IAM action:**  [datazone:CreateUserProfile](#list_datazone-action-CreateUserProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccountPool  **
  - **IAM action:**  [datazone:DeleteAccountPool](#list_datazone-action-DeleteAccountPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAsset  **
  - **IAM action:**  [datazone:DeleteAsset](#list_datazone-action-DeleteAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssetFilter  **
  - **IAM action:**  [datazone:DeleteAssetFilter](#list_datazone-action-DeleteAssetFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssetType  **
  - **IAM action:**  [datazone:DeleteAssetType](#list_datazone-action-DeleteAssetType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnection  **
  - **IAM action:**  [datazone:DeleteConnection](#list_datazone-action-DeleteConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataExportConfiguration  **
  - **IAM action:**  [datazone:DeleteDataExportConfiguration](#list_datazone-action-DeleteDataExportConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataProduct  **
  - **IAM action:**  [datazone:DeleteDataProduct](#list_datazone-action-DeleteDataProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataSource  **
  - **IAM action:**  [datazone:DeleteDataSource](#list_datazone-action-DeleteDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomain  **
  - **IAM action:**  [datazone:DeleteDomain](#list_datazone-action-DeleteDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomainUnit  **
  - **IAM action:**  [datazone:DeleteDomainUnit](#list_datazone-action-DeleteDomainUnit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironment  **
  - **IAM action:**  [datazone:DeleteEnvironment](#list_datazone-action-DeleteEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironmentAction  **
  - **IAM action:**  [datazone:DeleteEnvironmentAction](#list_datazone-action-DeleteEnvironmentAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironmentBlueprint  **
  - **IAM action:**  [datazone:DeleteEnvironmentBlueprint](#list_datazone-action-DeleteEnvironmentBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironmentBlueprintConfiguration  **
  - **IAM action:**  [datazone:DeleteEnvironmentBlueprintConfiguration](#list_datazone-action-DeleteEnvironmentBlueprintConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironmentProfile  **
  - **IAM action:**  [datazone:DeleteEnvironmentProfile](#list_datazone-action-DeleteEnvironmentProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFormType  **
  - **IAM action:**  [datazone:DeleteFormType](#list_datazone-action-DeleteFormType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGlossary  **
  - **IAM action:**  [datazone:DeleteGlossary](#list_datazone-action-DeleteGlossary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGlossaryTerm  **
  - **IAM action:**  [datazone:DeleteGlossaryTerm](#list_datazone-action-DeleteGlossaryTerm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLineageEvent  **
  - **IAM action:**  [datazone:DeleteLineageEvent](#list_datazone-action-DeleteLineageEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteListing  **
  - **IAM action:**  [datazone:DeleteListing](#list_datazone-action-DeleteListing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNotebook  **
  - **IAM action:**  [datazone:DeleteNotebook](#list_datazone-action-DeleteNotebook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProject  **
  - **IAM action:**  [datazone:DeleteProject](#list_datazone-action-DeleteProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProjectMembership  **
  - **IAM action:**  [datazone:DeleteProjectMembership](#list_datazone-action-DeleteProjectMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProjectProfile  **
  - **IAM action:**  [datazone:DeleteProjectProfile](#list_datazone-action-DeleteProjectProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRule  **
  - **IAM action:**  [datazone:DeleteRule](#list_datazone-action-DeleteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSubscriptionGrant  **
  - **IAM action:**  [datazone:DeleteSubscriptionGrant](#list_datazone-action-DeleteSubscriptionGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSubscriptionRequest  **
  - **IAM action:**  [datazone:DeleteSubscriptionRequest](#list_datazone-action-DeleteSubscriptionRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSubscriptionTarget  **
  - **IAM action:**  [datazone:DeleteSubscriptionTarget](#list_datazone-action-DeleteSubscriptionTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTimeSeriesDataPoints  **
  - **IAM action:**  [datazone:DeleteTimeSeriesDataPoints](#list_datazone-action-DeleteTimeSeriesDataPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateEnvironmentRole  **
  - **IAM action:**  [datazone:DisassociateEnvironmentRole](#list_datazone-action-DisassociateEnvironmentRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateGovernedTerms  **
  - **IAM action:**  [datazone:DisassociateGovernedTerms](#list_datazone-action-DisassociateGovernedTerms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountPool  **
  - **IAM action:**  [datazone:GetAccountPool](#list_datazone-action-GetAccountPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAsset  **
  - **IAM action:**  [datazone:GetAsset](#list_datazone-action-GetAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssetFilter  **
  - **IAM action:**  [datazone:GetAssetFilter](#list_datazone-action-GetAssetFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssetType  **
  - **IAM action:**  [datazone:GetAssetType](#list_datazone-action-GetAssetType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnection  **
  - **IAM action:**  [datazone:GetConnection](#list_datazone-action-GetConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataExportConfiguration  **
  - **IAM action:**  [datazone:GetDataExportConfiguration](#list_datazone-action-GetDataExportConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataProduct  **
  - **IAM action:**  [datazone:GetDataProduct](#list_datazone-action-GetDataProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataSource  **
  - **IAM action:**  [datazone:GetDataSource](#list_datazone-action-GetDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataSourceRun  **
  - **IAM action:**  [datazone:GetDataSourceRun](#list_datazone-action-GetDataSourceRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomain  **
  - **IAM action:**  [datazone:GetDomain](#list_datazone-action-GetDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainUnit  **
  - **IAM action:**  [datazone:GetDomainUnit](#list_datazone-action-GetDomainUnit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironment  **
  - **IAM action:**  [datazone:GetEnvironment](#list_datazone-action-GetEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironmentAction  **
  - **IAM action:**  [datazone:GetEnvironmentAction](#list_datazone-action-GetEnvironmentAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironmentBlueprint  **
  - **IAM action:**  [datazone:GetEnvironmentBlueprint](#list_datazone-action-GetEnvironmentBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironmentBlueprintConfiguration  **
  - **IAM action:**  [datazone:GetEnvironmentBlueprintConfiguration](#list_datazone-action-GetEnvironmentBlueprintConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironmentCredentials  **
  - **IAM action:**  [datazone:GetEnvironmentCredentials](#list_datazone-action-GetEnvironmentCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironmentProfile  **
  - **IAM action:**  [datazone:GetEnvironmentProfile](#list_datazone-action-GetEnvironmentProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFormType  **
  - **IAM action:**  [datazone:GetFormType](#list_datazone-action-GetFormType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGlossary  **
  - **IAM action:**  [datazone:GetGlossary](#list_datazone-action-GetGlossary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGlossaryTerm  **
  - **IAM action:**  [datazone:GetGlossaryTerm](#list_datazone-action-GetGlossaryTerm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroupProfile  **
  - **IAM action:**  [datazone:GetGroupProfile](#list_datazone-action-GetGroupProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIamPortalLoginUrl  **
  - **IAM action:**  [datazone:GetIamPortalLoginUrl](#list_datazone-action-GetIamPortalLoginUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   GetJobRun  **
  - **IAM action:**  [datazone:GetJobRun](#list_datazone-action-GetJobRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLineageEvent  **
  - **IAM action:**  [datazone:GetLineageEvent](#list_datazone-action-GetLineageEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLineageNode  **
  - **IAM action:**  [datazone:GetLineageNode](#list_datazone-action-GetLineageNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetListing  **
  - **IAM action:**  [datazone:GetListing](#list_datazone-action-GetListing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetadataGenerationRun  **
  - **IAM action:**  [datazone:GetMetadataGenerationRun](#list_datazone-action-GetMetadataGenerationRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNotebook  **
  - **IAM action:**  [datazone:GetNotebook](#list_datazone-action-GetNotebook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNotebookExport  **
  - **IAM action:**  [datazone:GetNotebookExport](#list_datazone-action-GetNotebookExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNotebookRun  **
  - **IAM action:**  [datazone:GetNotebookRun](#list_datazone-action-GetNotebookRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProject  **
  - **IAM action:**  [datazone:GetProject](#list_datazone-action-GetProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProjectProfile  **
  - **IAM action:**  [datazone:GetProjectProfile](#list_datazone-action-GetProjectProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRule  **
  - **IAM action:**  [datazone:GetRule](#list_datazone-action-GetRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSubscription  **
  - **IAM action:**  [datazone:GetSubscription](#list_datazone-action-GetSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSubscriptionGrant  **
  - **IAM action:**  [datazone:GetSubscriptionGrant](#list_datazone-action-GetSubscriptionGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSubscriptionRequestDetails  **
  - **IAM action:**  [datazone:GetSubscriptionRequestDetails](#list_datazone-action-GetSubscriptionRequestDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSubscriptionTarget  **
  - **IAM action:**  [datazone:GetSubscriptionTarget](#list_datazone-action-GetSubscriptionTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTimeSeriesDataPoint  **
  - **IAM action:**  [datazone:GetTimeSeriesDataPoint](#list_datazone-action-GetTimeSeriesDataPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUserProfile  **
  - **IAM action:**  [datazone:GetUserProfile](#list_datazone-action-GetUserProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccountPools  **
  - **IAM action:**  [datazone:ListAccountPools](#list_datazone-action-ListAccountPools) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccountsInAccountPool  **
  - **IAM action:**  [datazone:ListAccountsInAccountPool](#list_datazone-action-ListAccountsInAccountPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssetFilters  **
  - **IAM action:**  [datazone:ListAssetFilters](#list_datazone-action-ListAssetFilters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssetRevisions  **
  - **IAM action:**  [datazone:ListAssetRevisions](#list_datazone-action-ListAssetRevisions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnections  **
  - **IAM action:**  [datazone:ListConnections](#list_datazone-action-ListConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataProductRevisions  **
  - **IAM action:**  [datazone:ListDataProductRevisions](#list_datazone-action-ListDataProductRevisions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSourceRunActivities  **
  - **IAM action:**  [datazone:ListDataSourceRunActivities](#list_datazone-action-ListDataSourceRunActivities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSourceRuns  **
  - **IAM action:**  [datazone:ListDataSourceRuns](#list_datazone-action-ListDataSourceRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSources  **
  - **IAM action:**  [datazone:ListDataSources](#list_datazone-action-ListDataSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainUnitsForParent  **
  - **IAM action:**  [datazone:ListDomainUnitsForParent](#list_datazone-action-ListDomainUnitsForParent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomains  **
  - **IAM action:**  [datazone:ListDomains](#list_datazone-action-ListDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEntityOwners  **
  - **IAM action:**  [datazone:ListEntityOwners](#list_datazone-action-ListEntityOwners) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentActions  **
  - **IAM action:**  [datazone:ListEnvironmentActions](#list_datazone-action-ListEnvironmentActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentBlueprintConfigurations  **
  - **IAM action:**  [datazone:ListEnvironmentBlueprintConfigurations](#list_datazone-action-ListEnvironmentBlueprintConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentBlueprints  **
  - **IAM action:**  [datazone:ListEnvironmentBlueprints](#list_datazone-action-ListEnvironmentBlueprints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentProfiles  **
  - **IAM action:**  [datazone:ListEnvironmentProfiles](#list_datazone-action-ListEnvironmentProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironments  **
  - **IAM action:**  [datazone:ListEnvironments](#list_datazone-action-ListEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobRuns  **
  - **IAM action:**  [datazone:ListJobRuns](#list_datazone-action-ListJobRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLineageEvents  **
  - **IAM action:**  [datazone:ListLineageEvents](#list_datazone-action-ListLineageEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLineageNodeHistory  **
  - **IAM action:**  [datazone:ListLineageNodeHistory](#list_datazone-action-ListLineageNodeHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMetadataGenerationRuns  **
  - **IAM action:**  [datazone:ListMetadataGenerationRuns](#list_datazone-action-ListMetadataGenerationRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotebookRuns  **
  - **IAM action:**  [datazone:ListNotebookRuns](#list_datazone-action-ListNotebookRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotebooks  **
  - **IAM action:**  [datazone:ListNotebooks](#list_datazone-action-ListNotebooks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotifications  **
  - **IAM action:**  [datazone:ListNotifications](#list_datazone-action-ListNotifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyGrants  **
  - **IAM action:**  [datazone:ListPolicyGrants](#list_datazone-action-ListPolicyGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProjectMemberships  **
  - **IAM action:**  [datazone:ListProjectMemberships](#list_datazone-action-ListProjectMemberships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProjectProfiles  **
  - **IAM action:**  [datazone:ListProjectProfiles](#list_datazone-action-ListProjectProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProjects  **
  - **IAM action:**  [datazone:ListProjects](#list_datazone-action-ListProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRules  **
  - **IAM action:**  [datazone:ListRules](#list_datazone-action-ListRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscriptionGrants  **
  - **IAM action:**  [datazone:ListSubscriptionGrants](#list_datazone-action-ListSubscriptionGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscriptionRequests  **
  - **IAM action:**  [datazone:ListSubscriptionRequests](#list_datazone-action-ListSubscriptionRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscriptionTargets  **
  - **IAM action:**  [datazone:ListSubscriptionTargets](#list_datazone-action-ListSubscriptionTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscriptions  **
  - **IAM action:**  [datazone:ListSubscriptions](#list_datazone-action-ListSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [datazone:ListTagsForResource](#list_datazone-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTimeSeriesDataPoints  **
  - **IAM action:**  [datazone:ListTimeSeriesDataPoints](#list_datazone-action-ListTimeSeriesDataPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PostLineageEvent  **
  - **IAM action:**  [datazone:PostLineageEvent](#list_datazone-action-PostLineageEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PostTimeSeriesDataPoints  **
  - **IAM action:**  [datazone:PostTimeSeriesDataPoints](#list_datazone-action-PostTimeSeriesDataPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDataExportConfiguration  **
  - **IAM action:**  [datazone:PutDataExportConfiguration](#list_datazone-action-PutDataExportConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEnvironmentBlueprintConfiguration  **
  - **IAM action:**  [datazone:PutEnvironmentBlueprintConfiguration](#list_datazone-action-PutEnvironmentBlueprintConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   QueryGraph  **
  - **IAM action:**  [datazone:QueryGraph](#list_datazone-action-QueryGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RejectPredictions  **
  - **IAM action:**  [datazone:RejectPredictions](#list_datazone-action-RejectPredictions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectSubscriptionRequest  **
  - **IAM action:**  [datazone:RejectSubscriptionRequest](#list_datazone-action-RejectSubscriptionRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveEntityOwner  **
  - **IAM action:**  [datazone:RemoveEntityOwner](#list_datazone-action-RemoveEntityOwner) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemovePolicyGrant  **
  - **IAM action:**  [datazone:RemovePolicyGrant](#list_datazone-action-RemovePolicyGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RevokeSubscription  **
  - **IAM action:**  [datazone:RevokeSubscription](#list_datazone-action-RevokeSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   Search  **
  - **IAM action:**  [datazone:Search](#list_datazone-action-Search) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchGroupProfiles  **
  - **IAM action:**  [datazone:SearchGroupProfiles](#list_datazone-action-SearchGroupProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchListings  **
  - **IAM action:**  [datazone:SearchListings](#list_datazone-action-SearchListings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchTypes  **
  - **IAM action:**  [datazone:SearchTypes](#list_datazone-action-SearchTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchUserProfiles  **
  - **IAM action:**  [datazone:SearchUserProfiles](#list_datazone-action-SearchUserProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartDataSourceRun  **
  - **IAM action:**  [datazone:StartDataSourceRun](#list_datazone-action-StartDataSourceRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMetadataGenerationRun  **
  - **IAM action:**  [datazone:StartMetadataGenerationRun](#list_datazone-action-StartMetadataGenerationRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNotebookExport  **
  - **IAM action:**  [datazone:StartNotebookExport](#list_datazone-action-StartNotebookExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNotebookImport  **
  - **IAM action:**  [datazone:StartNotebookImport](#list_datazone-action-StartNotebookImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNotebookRun  **
  - **IAM action:**  [datazone:StartNotebookRun](#list_datazone-action-StartNotebookRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopNotebookRun  **
  - **IAM action:**  [datazone:StopNotebookRun](#list_datazone-action-StopNotebookRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [datazone:TagResource](#list_datazone-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [datazone:UntagResource](#list_datazone-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountPool  **
  - **IAM action:**  [datazone:UpdateAccountPool](#list_datazone-action-UpdateAccountPool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   UpdateAssetFilter  **
  - **IAM action:**  [datazone:UpdateAssetFilter](#list_datazone-action-UpdateAssetFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnection  **
  - **IAM action:**  [datazone:UpdateConnection](#list_datazone-action-UpdateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataSource  **
  - **IAM action:**  [datazone:UpdateDataSource](#list_datazone-action-UpdateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   UpdateDomain  **
  - **IAM action:**  [datazone:UpdateDomain](#list_datazone-action-UpdateDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   UpdateDomainUnit  **
  - **IAM action:**  [datazone:UpdateDomainUnit](#list_datazone-action-UpdateDomainUnit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnvironment  **
  - **IAM action:**  [datazone:UpdateEnvironment](#list_datazone-action-UpdateEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnvironmentAction  **
  - **IAM action:**  [datazone:UpdateEnvironmentAction](#list_datazone-action-UpdateEnvironmentAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnvironmentBlueprint  **
  - **IAM action:**  [datazone:UpdateEnvironmentBlueprint](#list_datazone-action-UpdateEnvironmentBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnvironmentProfile  **
  - **IAM action:**  [datazone:UpdateEnvironmentProfile](#list_datazone-action-UpdateEnvironmentProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGlossary  **
  - **IAM action:**  [datazone:UpdateGlossary](#list_datazone-action-UpdateGlossary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGlossaryTerm  **
  - **IAM action:**  [datazone:UpdateGlossaryTerm](#list_datazone-action-UpdateGlossaryTerm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGroupProfile  **
  - **IAM action:**  [datazone:UpdateGroupProfile](#list_datazone-action-UpdateGroupProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNotebook  **
  - **IAM action:**  [datazone:UpdateNotebook](#list_datazone-action-UpdateNotebook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProject  **
  - **IAM action:**  [datazone:UpdateProject](#list_datazone-action-UpdateProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProjectProfile  **
  - **IAM action:**  [datazone:UpdateProjectProfile](#list_datazone-action-UpdateProjectProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRule  **
  - **IAM action:**  [datazone:UpdateRule](#list_datazone-action-UpdateRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubscriptionGrantStatus  **
  - **IAM action:**  [datazone:UpdateSubscriptionGrantStatus](#list_datazone-action-UpdateSubscriptionGrantStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubscriptionRequest  **
  - **IAM action:**  [datazone:UpdateSubscriptionRequest](#list_datazone-action-UpdateSubscriptionRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubscriptionTarget  **
  - **IAM action:**  [datazone:UpdateSubscriptionTarget](#list_datazone-action-UpdateSubscriptionTarget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datazone.amazonaws.com / **Access level:** Write

- **   UpdateUserProfile  **
  - **IAM action:**  [datazone:UpdateUserProfile](#list_datazone-action-UpdateUserProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon DataZone
<a name="list_datazone-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptPredictions](${APIReferenceDocPage}API_AcceptPredictions.html)  **
  - **Description:** Grants permission to accept prediction
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AcceptSubscriptionRequest](${APIReferenceDocPage}API_AcceptSubscriptionRequest.html)  **
  - **Description:** Grants permission to approve a subscription request for a Data Asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AddEntityOwner](${APIReferenceDocPage}API_AddEntityOwner.html)  **
  - **Description:** Grants permission to add an owner to an entity like domain unit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AddPolicyGrant](${APIReferenceDocPage}API_AddPolicyGrant.html)  **
  - **Description:** Grants permission to add a policy grant
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [AssociateEnvironmentRole](${APIReferenceDocPage}API_AssociateEnvironmentRole.html)  **
  - **Description:** Grants permission to associate a role in a default service blueprint environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateGovernedTerms](${APIReferenceDocPage}API_AssociateGovernedTerms.html)  **
  - **Description:** Grants permission to associate governed terms to an asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchGetAttributesMetadata](${APIReferenceDocPage}API_BatchGetAttributesMetadata.html)  **
  - **Description:** Grants permission to retrieve attributes metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetCell](${APIReferenceDocPage}API_BatchGetCell.html)  **
  - **Description:** Grants permission to batch get cells
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetCellRun](${APIReferenceDocPage}API_BatchGetCellRun.html)  **
  - **Description:** Grants permission to batch get cell runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchPutAttributesMetadata](${APIReferenceDocPage}API_BatchPutAttributesMetadata.html)  **
  - **Description:** Grants permission to create and update attributes metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelMessage](${APIReferenceDocPage}API_CancelMessage.html)  **
  - **Description:** Grants permission to cancel an in-progress agent response
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelMetadataGenerationRun](${APIReferenceDocPage}API_CancelMetadataGenerationRun.html)  **
  - **Description:** Grants permission to cancel metadata generation run
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelSubscription](${APIReferenceDocPage}API_CancelSubscription.html)  **
  - **Description:** Grants permission to revoke or unsubscribe an approved subscription to Data Asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAccountPool](${APIReferenceDocPage}API_CreateAccountPool.html)  **
  - **Description:** Grants permission to create an account pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAsset](${APIReferenceDocPage}API_CreateAsset.html)  **
  - **Description:** Grants permission to create asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAssetFilter](${APIReferenceDocPage}API_CreateAssetFilter.html)  **
  - **Description:** Grants permission to create asset filter
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAssetRevision](${APIReferenceDocPage}API_CreateAssetRevision.html)  **
  - **Description:** Grants permission to create new revision of an asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAssetType](${APIReferenceDocPage}API_CreateAssetType.html)  **
  - **Description:** Grants permission to create an asset type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateCell](${APIReferenceDocPage}API_CreateCell.html)  **
  - **Description:** Grants permission to create cells
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateCellRun](${APIReferenceDocPage}API_CreateCellRun.html)  **
  - **Description:** Grants permission to create cell runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateConnection](${APIReferenceDocPage}API_CreateConnection.html)  **
  - **Description:** Grants permission to create connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDataProduct](${APIReferenceDocPage}API_CreateDataProduct.html)  **
  - **Description:** Grants permission to create data product
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDataProductRevision](${APIReferenceDocPage}API_CreateDataProductRevision.html)  **
  - **Description:** Grants permission to create data product revision
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDataSource](${APIReferenceDocPage}API_CreateDataSource.html)  **
  - **Description:** Grants permission to create a new DataSource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDesignation](${APIReferenceDocPage}API_CreateDesignation.html)  **
  - **Description:** Grants permission to create a designation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDomain](${APIReferenceDocPage}API_CreateDomain.html)  **
  - **Description:** Grants permission to provision a domain which is a top level entity that contains other Amazon DataZone resources
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datazone-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datazone-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDomainUnit](${APIReferenceDocPage}API_CreateDomainUnit.html)  **
  - **Description:** Grants permission to create a domain unit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEnvironment](${APIReferenceDocPage}API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create a collection of configurated resources used to publish and subscribe to data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEnvironmentAction](${APIReferenceDocPage}API_CreateEnvironmentAction.html)  **
  - **Description:** Grants permission to create an environment action in a default service blueprint environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEnvironmentBlueprint](${APIReferenceDocPage}API_CreateEnvironmentBlueprint.html)  **
  - **Description:** Grants permission to create a custom Environment Blueprint that allow user to add Environments to their Project
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEnvironmentProfile](${APIReferenceDocPage}API_CreateEnvironmentProfile.html)  **
  - **Description:** Grants permission to create a template from a Blueprint that can be used to create a Environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateFormType](${APIReferenceDocPage}API_CreateFormType.html)  **
  - **Description:** Grants permission to create a form type or a new revision of it
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGlossary](${APIReferenceDocPage}API_CreateGlossary.html)  **
  - **Description:** Grants permission to create a business glossary
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGlossaryTerm](${APIReferenceDocPage}API_CreateGlossaryTerm.html)  **
  - **Description:** Grants permission to create a glossary term
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGroupProfile](${APIReferenceDocPage}API_CreateGroupProfile.html)  **
  - **Description:** Grants permission to create a DataZone group profile for an IAM Identity Center group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateListingChangeSet](${APIReferenceDocPage}API_CreateListingChangeSet.html)  **
  - **Description:** Grants permission to create listing change set
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateNotebook](${APIReferenceDocPage}API_CreateNotebook.html)  **
  - **Description:** Grants permission to create notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateProject](${APIReferenceDocPage}API_CreateProject.html)  **
  - **Description:** Grants permission to create a Project to enable your team to publish and subscribe to data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateProjectMembership](${APIReferenceDocPage}API_CreateProjectMembership.html)  **
  - **Description:** Grants permission to add a user to a Project
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateProjectProfile](${APIReferenceDocPage}API_CreateProjectProfile.html)  **
  - **Description:** Grants permission to create a project profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRule](${APIReferenceDocPage}API_CreateRule.html)  **
  - **Description:** Grants permission to create rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSubscriptionGrant](${APIReferenceDocPage}API_CreateSubscriptionGrant.html)  **
  - **Description:** Grants permission to create a grant for an approved subscription on a subscription target
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSubscriptionRequest](${APIReferenceDocPage}API_CreateSubscriptionRequest.html)  **
  - **Description:** Grants permission to create a subscription request for a Data Asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSubscriptionTarget](${APIReferenceDocPage}API_CreateSubscriptionTarget.html)  **
  - **Description:** Grants permission to create a subscription target for a Environment in the project
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateUserProfile](${APIReferenceDocPage}API_CreateUserProfile.html)  **
  - **Description:** Grants permission to create a user profile for an existing user in the customers IAM Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAccountPool](${APIReferenceDocPage}API_DeleteAccountPool.html)  **
  - **Description:** Grants permission to delete an account pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAsset](${APIReferenceDocPage}API_DeleteAsset.html)  **
  - **Description:** Grants permission to delete an asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAssetFilter](${APIReferenceDocPage}API_DeleteAssetFilter.html)  **
  - **Description:** Grants permission to delete asset filter
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAssetType](${APIReferenceDocPage}API_DeleteAssetType.html)  **
  - **Description:** Grants permission to delete an asset type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCell](${APIReferenceDocPage}API_DeleteCell.html)  **
  - **Description:** Grants permission to delete cells
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCellRun](${APIReferenceDocPage}API_DeleteCellRun.html)  **
  - **Description:** Grants permission to delete cell runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConnection](${APIReferenceDocPage}API_DeleteConnection.html)  **
  - **Description:** Grants permission to delete connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDataExportConfiguration](${APIReferenceDocPage}API_DeleteDataExportConfiguration.html)  **
  - **Description:** Grants permission to delete DataZone catalog data export configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDataProduct](${APIReferenceDocPage}API_DeleteDataProduct.html)  **
  - **Description:** Grants permission to delete data product
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDataSource](${APIReferenceDocPage}API_DeleteDataSource.html)  **
  - **Description:** Grants permission to update existing DataSource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDesignation](${APIReferenceDocPage}API_DeleteDesignation.html)  **
  - **Description:** Grants permission to delete a designation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDomain](${APIReferenceDocPage}API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete a provisioned domain
  - **Resource types (\*required):** [domain\*](#list_datazone-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomainUnit](${APIReferenceDocPage}API_DeleteDomainUnit.html)  **
  - **Description:** Grants permission to delete an existing domain unit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEnvironment](${APIReferenceDocPage}API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to Delete Environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEnvironmentAction](${APIReferenceDocPage}API_DeleteEnvironmentAction.html)  **
  - **Description:** Grants permission to delete an environment action in a default service blueprint environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEnvironmentBlueprint](${APIReferenceDocPage}API_DeleteEnvironmentBlueprint.html)  **
  - **Description:** Grants permission to delete Environment Blueprint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEnvironmentBlueprintConfiguration](${APIReferenceDocPage}API_DeleteEnvironmentBlueprintConfiguration.html)  **
  - **Description:** Grants permission to delete environment blueprint configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEnvironmentProfile](${APIReferenceDocPage}API_DeleteEnvironmentProfile.html)  **
  - **Description:** Grants permission to delete Environment Profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteFormType](${APIReferenceDocPage}API_DeleteFormType.html)  **
  - **Description:** Grants permission to delete a form type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGlossary](${APIReferenceDocPage}API_DeleteGlossary.html)  **
  - **Description:** Grants permission to delete a business glossary
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGlossaryTerm](${APIReferenceDocPage}API_DeleteGlossaryTerm.html)  **
  - **Description:** Grants permission to delete a glossary term
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteLineageEvent](${APIReferenceDocPage}API_DeleteLineageEvent.html)  **
  - **Description:** Grants permission to delete lineage events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteListing](${APIReferenceDocPage}API_DeleteListing.html)  **
  - **Description:** Grants permission to delete listing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteNotebook](${APIReferenceDocPage}API_DeleteNotebook.html)  **
  - **Description:** Grants permission to delete notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteProject](${APIReferenceDocPage}API_DeleteProject.html)  **
  - **Description:** Grants permission to delete a Project that enables your team to publish and subscribe to data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteProjectMembership](${APIReferenceDocPage}API_DeleteProjectMembership.html)  **
  - **Description:** Grants permission to remove a user from a project
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteProjectProfile](${APIReferenceDocPage}API_DeleteProjectProfile.html)  **
  - **Description:** Grants permission to delete a project profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRule](${APIReferenceDocPage}API_DeleteRule.html)  **
  - **Description:** Grants permission to delete rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSubscriptionGrant](${APIReferenceDocPage}API_DeleteSubscriptionGrant.html)  **
  - **Description:** Grants permission to delete a subscription grant from a subscription target
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSubscriptionRequest](${APIReferenceDocPage}API_DeleteSubscriptionRequest.html)  **
  - **Description:** Grants permission to delete a pending subscription request for a Data Asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSubscriptionTarget](${APIReferenceDocPage}API_DeleteSubscriptionTarget.html)  **
  - **Description:** Grants permission to delete a subscription target from a Environment in the project
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteTimeSeriesDataPoints](${APIReferenceDocPage}API_DeleteTimeSeriesDataPoints.html)  **
  - **Description:** Grants permission to delete existing TimeSeriesDataPoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateEnvironmentRole](${APIReferenceDocPage}API_AssociateEnvironmentRole.html)  **
  - **Description:** Grants permission to disassociate a role in a default service blueprint environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateGovernedTerms](${APIReferenceDocPage}API_DisassociateGovernedTerms.html)  **
  - **Description:** Grants permission to disassociate governed terms to an asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GenerateCode](${APIReferenceDocPage}API_GenerateCode.html)  **
  - **Description:** Grants permission to generate code
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAccountPool](${APIReferenceDocPage}API_GetAccountPool.html)  **
  - **Description:** Grants permission to get account pool details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAsset](${APIReferenceDocPage}API_GetAsset.html)  **
  - **Description:** Grants permission to retrieve an asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAssetFilter](${APIReferenceDocPage}API_GetAssetFilter.html)  **
  - **Description:** Grants permission to get asset filter
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAssetType](${APIReferenceDocPage}API_GetAssetType.html)  **
  - **Description:** Grants permission to get an asset type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCell](${APIReferenceDocPage}API_GetCell.html)  **
  - **Description:** Grants permission to get cells
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCellRun](${APIReferenceDocPage}API_GetCellRun.html)  **
  - **Description:** Grants permission to get cell runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCellRunResult](${APIReferenceDocPage}API_GetCellRunResult.html)  **
  - **Description:** Grants permission to get cell run result
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCompute](${APIReferenceDocPage}API_GetCompute.html)  **
  - **Description:** Grants permission to get compute
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnection](${APIReferenceDocPage}API_GetConnection.html)  **
  - **Description:** Grants permission to get connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConversation](${APIReferenceDocPage}API_GetConversation.html)  **
  - **Description:** Grants permission to get conversations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCurrentEffectivePolicy](${APIReferenceDocPage}API_GetCurrentEffectivePolicy.html)  **
  - **Description:** Grants permission to Get Current Effective Policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataExportConfiguration](${APIReferenceDocPage}API_GetDataExportConfiguration.html)  **
  - **Description:** Grants permission to retrieve DataZone catalog data export configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataProduct](${APIReferenceDocPage}API_GetDataProduct.html)  **
  - **Description:** Grants permission to get data product
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataSource](${APIReferenceDocPage}API_GetDataSource.html)  **
  - **Description:** Grants permission to Get a existing DataSource in Amazon DataZone using its identifier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataSourceRun](${APIReferenceDocPage}API_GetDataSourceRun.html)  **
  - **Description:** Grants permission to get DataSource run job in Amazon DataZone using it's identifier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDesignation](${APIReferenceDocPage}API_GetDesignation.html)  **
  - **Description:** Grants permission to retrieve information about a designation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDomain](${APIReferenceDocPage}API_GetDomain.html)  **
  - **Description:** Grants permission to retrieve information about a domain
  - **Resource types (\*required):** [domain\*](#list_datazone-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomainUnit](${APIReferenceDocPage}API_GetDomainUnit.html)  **
  - **Description:** Grants permission to get an existing domain unit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEnvironment](${APIReferenceDocPage}API_GetEnvironment.html)  **
  - **Description:** Grants permission to get Environment details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEnvironmentAction](${APIReferenceDocPage}API_GetEnvironmentAction.html)  **
  - **Description:** Grants permission to get an environment action in a default service blueprint environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEnvironmentBlueprint](${APIReferenceDocPage}API_GetEnvironmentBlueprint.html)  **
  - **Description:** Grants permission to get Environment Blueprint details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEnvironmentBlueprintConfiguration](${APIReferenceDocPage}API_GetEnvironmentBlueprintConfiguration.html)  **
  - **Description:** Grants permission to get environment blueprint configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEnvironmentCredentials](${APIReferenceDocPage}API_GetEnvironmentCredentials.html)  **
  - **Description:** Grants permission to get short term credentials that assume the Environment user role
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEnvironmentProfile](${APIReferenceDocPage}API_GetEnvironmentProfile.html)  **
  - **Description:** Grants permission to get Environment Profile details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFormType](${APIReferenceDocPage}API_GetFormType.html)  **
  - **Description:** Grants permission to get a form type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGlossary](${APIReferenceDocPage}API_GetGlossary.html)  **
  - **Description:** Grants permission to get a business glossary
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGlossaryTerm](${APIReferenceDocPage}API_GetGlossaryTerm.html)  **
  - **Description:** Grants permission to get a glossary term
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGroupProfile](${APIReferenceDocPage}API_GetGroupProfile.html)  **
  - **Description:** Grants permission to retrieve an existing DataZone group profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIamPortalLoginUrl](${APIReferenceDocPage}API_GetIamPortalLoginUrl.html)  **
  - **Description:** Grants permission to an IAM principal to log into the DataZone Portal
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetJobRun](${APIReferenceDocPage}API_GetJobRun.html)  **
  - **Description:** Grants permission to get job runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLineageEvent](${APIReferenceDocPage}API_GetLineageEvent.html)  **
  - **Description:** Grants permission to get lineage events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLineageNode](${APIReferenceDocPage}API_GetLineageNode.html)  **
  - **Description:** Grants permission to get the lineage node
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetListing](${APIReferenceDocPage}API_GetListing.html)  **
  - **Description:** Grants permission to get listing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMetadataGenerationRun](${APIReferenceDocPage}API_GetMetadataGenerationRun.html)  **
  - **Description:** Grants permission to get metadata generation run
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNotebook](${APIReferenceDocPage}API_GetNotebook.html)  **
  - **Description:** Grants permission to get notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNotebookCompute](${APIReferenceDocPage}API_GetNotebookCompute.html)  **
  - **Description:** Grants permission to get notebook compute
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNotebookExport](${APIReferenceDocPage}API_GetNotebookExport.html)  **
  - **Description:** Grants permission to get notebook exports
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNotebookRun](${APIReferenceDocPage}API_GetNotebookRun.html)  **
  - **Description:** Grants permission to get a notebook run
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProject](${APIReferenceDocPage}API_GetProject.html)  **
  - **Description:** Grants permission to get Project details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProjectProfile](${APIReferenceDocPage}API_GetProjectProfile.html)  **
  - **Description:** Grants permission to get project profile details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRule](${APIReferenceDocPage}API_GetRule.html)  **
  - **Description:** Grants permission to get rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSubscription](${APIReferenceDocPage}API_GetSubscription.html)  **
  - **Description:** Grants permission to retrieve a subscription
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSubscriptionGrant](${APIReferenceDocPage}API_GetSubscriptionGrant.html)  **
  - **Description:** Grants permission to retireve a subscription grant
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSubscriptionRequestDetails](${APIReferenceDocPage}API_GetSubscriptionRequestDetails.html)  **
  - **Description:** Grants permission to reject a subscription request for a Data Asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSubscriptionTarget](${APIReferenceDocPage}API_GetSubscriptionTarget.html)  **
  - **Description:** Grants permission to retireve details of subscription target
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTimeSeriesDataPoint](${APIReferenceDocPage}API_GetTimeSeriesDataPoint.html)  **
  - **Description:** Grants permission to get an existing TimeSeriesDataPoints in Amazon DataZone using its identifier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUpdateEligibility](${APIReferenceDocPage}API_GetUpdateEligibility.html)  **
  - **Description:** Grants permission to get update eligibility status for project constructs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUserProfile](${APIReferenceDocPage}API_GetUserProfile.html)  **
  - **Description:** Grants permission to retrieve a user profile for an existing user in the DataZone Domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAccountEnvironments](${APIReferenceDocPage}API_ListAccountEnvironments.html)  **
  - **Description:** Grants permission to list Environments across all domains in an AWS Account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAccountPools]({APIReferenceDocPage}API_ListAccountPools.html)  **
  - **Description:** Grants permission to list account pools
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAccountsInAccountPool]({APIReferenceDocPage}API_ListAccountsInAccountPool.html)  **
  - **Description:** Grants permission to list accounts in an account pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssetFilters](${APIReferenceDocPage}API_ListAssetFilters.html)  **
  - **Description:** Grants permission to list asset filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssetRevisions](${APIReferenceDocPage}API_ListAssetRevisions.html)  **
  - **Description:** Grants permission to list revisions of an asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCellRuns](${APIReferenceDocPage}API_ListCellRuns.html)  **
  - **Description:** Grants permission to list cell runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnections](${APIReferenceDocPage}API_ListConnections.html)  **
  - **Description:** Grants permission to list connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConversations](${APIReferenceDocPage}API_ListConversations.html)  **
  - **Description:** Grants permission to list conversations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataProductRevisions](${APIReferenceDocPage}API_ListDataProductRevisions.html)  **
  - **Description:** Grants permission to list data product revisions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataSourceRunActivities](${APIReferenceDocPage}API_ListDataSourceRunActivities.html)  **
  - **Description:** Grants permission to list DataSource runs job's activities on Asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataSourceRuns](${APIReferenceDocPage}API_ListDataSourceRuns.html)  **
  - **Description:** Grants permission to list DataSource runs job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataSources](${APIReferenceDocPage}API_ListDataSources.html)  **
  - **Description:** Grants permission to list existing DataSources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDesignations](${APIReferenceDocPage}API_ListDesignations.html)  **
  - **Description:** Grants permission to list designations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDomainUnitsForParent](${APIReferenceDocPage}API_ListDomainUnitsForParent.html)  **
  - **Description:** Grants permission to list child domain units for a given parent domain unit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDomains](${APIReferenceDocPage}API_ListDomains.html)  **
  - **Description:** Grants permission to retrieve all domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEntityOwners](${APIReferenceDocPage}API_ListEntityOwners.html)  **
  - **Description:** Grants permission to list owners of an entity like domain unit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironmentActions](${APIReferenceDocPage}API_ListEnvironmentActions.html)  **
  - **Description:** Grants permission to list environment actions in a default service blueprint environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironmentBlueprintConfigurations](${APIReferenceDocPage}API_ListEnvironmentBlueprintConfigurations.html)  **
  - **Description:** Grants permission to list environment blueprint configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironmentBlueprints](${APIReferenceDocPage}API_ListEnvironmentBlueprints.html)  **
  - **Description:** Grants permission to list Domain for Environment Blueprints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironmentProfiles](${APIReferenceDocPage}API_ListEnvironmentProfiles.html)  **
  - **Description:** Grants permission to list Domain for Environment Profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironments](${APIReferenceDocPage}API_ListEnvironments.html)  **
  - **Description:** Grants permission to show Environments in the Domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGroupsForUser](${APIReferenceDocPage}API_ListGroupsForUser.html)  **
  - **Description:** Grants permission to list all the DataZone group profiles that the DataZone user profile is a member of
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobRuns](${APIReferenceDocPage}API_ListJobRuns.html)  **
  - **Description:** Grants permission to list job runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLineageEvents](${APIReferenceDocPage}API_ListLineageEvents.html)  **
  - **Description:** Grants permission to list lineage events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLineageNodeHistory](${APIReferenceDocPage}API_ListLineageNodeHistory.html)  **
  - **Description:** Grants permission to list historical versions of lineage node
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMetadataGenerationRuns](${APIReferenceDocPage}API_ListMetadataGenerationRuns.html)  **
  - **Description:** Grants permission to list metadata generation runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotebookRuns](${APIReferenceDocPage}API_ListNotebookRuns.html)  **
  - **Description:** Grants permission to list notebook runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotebooks](${APIReferenceDocPage}API_ListNotebooks.html)  **
  - **Description:** Grants permission to list notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotifications](${APIReferenceDocPage}API_ListNotifications.html)  **
  - **Description:** Grants permission to list notifications and events for a datazone user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicyGrants](${APIReferenceDocPage}API_ListPolicyGrants.html)  **
  - **Description:** Grants permission to list policy grants
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProjectMemberships](${APIReferenceDocPage}API_ListProjectMemberships.html)  **
  - **Description:** Grants permission to list Project Members
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProjectProfiles](${APIReferenceDocPage}API_ListProjectProfiles.html)  **
  - **Description:** Grants permission to list project profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProjects](${APIReferenceDocPage}API_ListProjects.html)  **
  - **Description:** Grants permission to list Projects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRules](${APIReferenceDocPage}API_ListRules.html)  **
  - **Description:** Grants permission to list rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscriptionGrants](${APIReferenceDocPage}API_ListSubscriptionGrants.html)  **
  - **Description:** Grants permission to List subscription grants for a subscribed principal
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscriptionRequests](${APIReferenceDocPage}API_ListSubscriptionRequests.html)  **
  - **Description:** Grants permission to list subscription requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscriptionTargets](${APIReferenceDocPage}API_ListSubscriptionTargets.html)  **
  - **Description:** Grants permission to list subscription targets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscriptions](${APIReferenceDocPage}API_ListSubscriptions.html)  **
  - **Description:** Grants permission to list subscriptions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](${APIReferenceDocPage}API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve all tags associated with a resource
  - **Resource types (\*required):** [domain](#list_datazone-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTimeSeriesDataPoints](${APIReferenceDocPage}API_ListTimeSeriesDataPoints.html)  **
  - **Description:** Grants permission to list existing TimeSeriesDataPoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PostLineageEvent](${APIReferenceDocPage}API_PostLineageEvent.html)  **
  - **Description:** Grants permission to post lineage events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PostTimeSeriesDataPoints](${APIReferenceDocPage}API_PostTimeSeriesDataPoints.html)  **
  - **Description:** Grants permission to post a new TimeSeriesDataPoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutCellRunResult](${APIReferenceDocPage}API_PutCellRunResult.html)  **
  - **Description:** Grants permission to put cell run results
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutDataExportConfiguration](${APIReferenceDocPage}API_PutDataExportConfiguration.html)  **
  - **Description:** Grants permission to create and update DataZone catalog data export configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutEnvironmentBlueprintConfiguration](${APIReferenceDocPage}API_PutEnvironmentBlueprintConfiguration.html)  **
  - **Description:** Grants permission to put environment blueprint configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [QueryGraph](${APIReferenceDocPage}API_QueryGraph.html)  **
  - **Description:** Grants permission to query graph
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [RejectPredictions](${APIReferenceDocPage}API_RejectPredictions.html)  **
  - **Description:** Grants permission to reject prediction
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectSubscriptionRequest](${APIReferenceDocPage}API_RejectSubscriptionRequest.html)  **
  - **Description:** Grants permission to reject a subscription request for a Data Asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveEntityOwner](${APIReferenceDocPage}API_RemoveEntityOwner.html)  **
  - **Description:** Grants permission to remove an existing owner of an entity like domain unit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemovePolicyGrant](${APIReferenceDocPage}API_RemovePolicyGrant.html)  **
  - **Description:** Grants permission to remove a policy grant
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [RevokeSubscription](${APIReferenceDocPage}API_RevokeSubscription.html)  **
  - **Description:** Grants permission to revoke a subscription
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [Search](${APIReferenceDocPage}API_Search.html)  **
  - **Description:** Grants permission to search datazone entities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchGroupProfiles](${APIReferenceDocPage}API_SearchGroupProfiles.html)  **
  - **Description:** Grants permission to search DataZone group profiles and IAM Identity Center groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchListings](${APIReferenceDocPage}API_SearchListings.html)  **
  - **Description:** Grants permission to search listings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchTypes](${APIReferenceDocPage}API_SearchTypes.html)  **
  - **Description:** Grants permission to search types such asset types and form types in a domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchUserProfiles](${APIReferenceDocPage}API_SearchUserProfiles.html)  **
  - **Description:** Grants permission to search DataZone user profiles, IAM Identity Center users, and DataZone IAM principal profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SendMessage](${APIReferenceDocPage}API_SendMessage.html)  **
  - **Description:** Grants permission to send messages
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartCompute](${APIReferenceDocPage}API_StartCompute.html)  **
  - **Description:** Grants permission to start compute
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartConversation](${APIReferenceDocPage}API_StartConversation.html)  **
  - **Description:** Grants permission to start conversations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartDataSourceRun](${APIReferenceDocPage}API_StartDataSourceRun.html)  **
  - **Description:** Grants permission to start a DataSource run job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMetadataGenerationRun](${APIReferenceDocPage}API_StartMetadataGenerationRun.html)  **
  - **Description:** Grants permission to start metadata generation run
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartNotebookCompute](${APIReferenceDocPage}API_StartNotebookCompute.html)  **
  - **Description:** Grants permission to start notebook compute
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartNotebookExport](${APIReferenceDocPage}API_StartNotebookExport.html)  **
  - **Description:** Grants permission to export notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartNotebookImport](${APIReferenceDocPage}API_StartNotebookImport.html)  **
  - **Description:** Grants permission to import notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartNotebookRun](${APIReferenceDocPage}API_StartNotebookRun.html)  **
  - **Description:** Grants permission to start a notebook run
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartNotebookSync](${APIReferenceDocPage}API_StartNotebookSync.html)  **
  - **Description:** Grants permission to start notebook sync
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopCompute](${APIReferenceDocPage}API_StopCompute.html)  **
  - **Description:** Grants permission to stop compute
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopMetadataGenerationRun](${APIReferenceDocPage}API_StopMetadataGenerationRun.html)  **
  - **Description:** Grants permission to stop metadata generation run
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopNotebookCompute](${APIReferenceDocPage}API_StopNotebookCompute.html)  **
  - **Description:** Grants permission to stop notebook compute
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopNotebookRun](${APIReferenceDocPage}API_StopNotebookRun.html)  **
  - **Description:** Grants permission to stop a notebook run
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](${APIReferenceDocPage}API_TagResource.html)  **
  - **Description:** Grants permission to add or update tags to a resource
  - **Resource types (\*required):** [domain\*](#list_datazone-resource-domain)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datazone-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datazone-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](${APIReferenceDocPage}API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags associated with a resource
  - **Resource types (\*required):** [domain\*](#list_datazone-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datazone-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountPool](${APIReferenceDocPage}API_UpdateAccountPool.html)  **
  - **Description:** Grants permission to update an account pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAssetFilter](${APIReferenceDocPage}API_UpdateAssetFilter.html)  **
  - **Description:** Grants permission to update asset filter
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateCell](${APIReferenceDocPage}API_UpdateCell.html)  **
  - **Description:** Grants permission to update cells
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateCellRun](${APIReferenceDocPage}API_UpdateCellRun.html)  **
  - **Description:** Grants permission to update cell runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConnection](${APIReferenceDocPage}API_UpdateConnection.html)  **
  - **Description:** Grants permission to update connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDataSource](${APIReferenceDocPage}API_UpdateDataSource.html)  **
  - **Description:** Grants permission to update existing DataSource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDesignation](${APIReferenceDocPage}API_UpdateDesignation.html)  **
  - **Description:** Grants permission to update a designation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDomain](${APIReferenceDocPage}API_UpdateDomain.html)  **
  - **Description:** Grants permission to update information for a domain
  - **Resource types (\*required):** [domain\*](#list_datazone-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomainUnit](${APIReferenceDocPage}API_UpdateDomainUnit.html)  **
  - **Description:** Grants permission to update an existing domain unit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEnvironment](${APIReferenceDocPage}API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to update Environment settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEnvironmentAction](${APIReferenceDocPage}API_UpdateEnvironmentAction.html)  **
  - **Description:** Grants permission to update an environment action in a default service blueprint environment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEnvironmentBlueprint](${APIReferenceDocPage}API_UpdateEnvironmentBlueprint.html)  **
  - **Description:** Grants permission to update Environment Blueprint settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEnvironmentProfile](${APIReferenceDocPage}API_UpdateEnvironmentProfile.html)  **
  - **Description:** Grants permission to update EnvironmentProfile configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGlossary](${APIReferenceDocPage}API_UpdateGlossary.html)  **
  - **Description:** Grants permission to update a business glossary
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGlossaryTerm](${APIReferenceDocPage}API_UpdateGlossaryTerm.html)  **
  - **Description:** Grants permission to update a glossary term
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGroupProfile](${APIReferenceDocPage}API_UpdateGroupProfile.html)  **
  - **Description:** Grants permission to update a DataZone group profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateNotebook](${APIReferenceDocPage}API_UpdateNotebook.html)  **
  - **Description:** Grants permission to update notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateProject](${APIReferenceDocPage}API_UpdateProject.html)  **
  - **Description:** Grants permission to update a Project that enables your team to publish and subscribe to data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateProjectProfile](${APIReferenceDocPage}API_UpdateProjectProfile.html)  **
  - **Description:** Grants permission to update a project profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRule](${APIReferenceDocPage}API_UpdateRule.html)  **
  - **Description:** Grants permission to update rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSubscriptionGrantStatus](${APIReferenceDocPage}API_UpdateSubscriptionGrantStatus.html)  **
  - **Description:** Grants permission to update a subscription grant status for custom grants
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSubscriptionRequest](${APIReferenceDocPage}API_UpdateSubscriptionRequest.html)  **
  - **Description:** Grants permission to update business reason for subscription request for a Data Asset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSubscriptionTarget](${APIReferenceDocPage}API_UpdateSubscriptionTarget.html)  **
  - **Description:** Grants permission to update a subscription target
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateUserProfile](${APIReferenceDocPage}API_UpdateUserProfile.html)  **
  - **Description:** Grants permission to update a DataZone user profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ValidatePolicy](${APIReferenceDocPage}API_ValidatePolicy.html)  **
  - **Description:** Valite the Cedar Policy's correctness
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Permission-only actions for Amazon DataZone
<a name="list_datazone-permission-only-actions"></a>

The following actions are defined by Amazon DataZone but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [BatchDeleteLinkedTypes](${APIReferenceDocPage}API_BatchDeleteLinkedTypes.html)  **
  - **Description:** Grants permission to remove linked type items from an Amazon DataZone Domain
  - **Resource types (\*required):** [domain\*](#list_datazone-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchPutLinkedTypes](${APIReferenceDocPage}API_BatchPutLinkedTypes.html)  **
  - **Description:** Grants permission to put linked type items to an Amazon DataZone Domain
  - **Resource types (\*required):** [domain\*](#list_datazone-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchUpdateNotifications](${APIReferenceDocPage}API_BatchUpdateNotifications.html)  **
  - **Description:** Grants permission to update mutable fields of the calling user's own notifications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDomainSharingPolicy](${APIReferenceDocPage}API_DeleteDomainSharingPolicy.html)  **
  - **Description:** Grants permission to delete a resource policy for a DataZone Domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetDomainExecutionRoleCredentials](${APIReferenceDocPage}API_GetDomainExecutionRoleCredentials.html)  **
  - **Description:** Grants permission to use features that require access to domain execution role credentials
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDomainSharingPolicy](${APIReferenceDocPage}API_GetDomainSharingPolicy.html)  **
  - **Description:** Grants permission to retrieve a resource policy for a DataZone Domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEnvironmentActionLink](${APIReferenceDocPage}API_GetEnvironmentActionLink.html)  **
  - **Description:** Grants permission to get environment action link
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSubscriptionEligibility](${APIReferenceDocPage}API_GetSubscriptionEligibility.html)  **
  - **Description:** Grants permission to get subscription eligibilty
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEnvironmentBlueprintConfigurationSummaries](${APIReferenceDocPage}API_ListEnvironmentBlueprintConfigurationSummaries.html)  **
  - **Description:** Grants permission to list environment blueprint configuration summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLinkedTypes](${APIReferenceDocPage}API_ListLinkedTypes.html)  **
  - **Description:** Grants permission to list linked type items linked to an Amazon DataZone Domain
  - **Resource types (\*required):** [domain\*](#list_datazone-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWarehouseMetadata](${APIReferenceDocPage}API_ListWarehouseMetadata.html)  **
  - **Description:** Grants permission to list available Manager Secrets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ProvisionDomain](${APIReferenceDocPage}API_ProvisionDomain.html)  **
  - **Description:** Grants permission to provision domain with default project setup
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutDomainSharingPolicy](${APIReferenceDocPage}API_PutDomainSharingPolicy.html)  **
  - **Description:** Grants permission to add a resource policy for a DataZone Domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [RefreshToken](${APIReferenceDocPage}API_RefreshToken.html)  **
  - **Description:** Grants permission to refresh token
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SearchRules](${APIReferenceDocPage}API_SearchRules.html)  **
  - **Description:** Grants permission to search rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SsoLogin](${APIReferenceDocPage}API_SsoLogin.html)  **
  - **Description:** Grants permission to login using SSO
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SsoLogout](${APIReferenceDocPage}API_SsoLogout.html)  **
  - **Description:** Grants permission to logout as SSO user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartAccountBootstrapAction](${APIReferenceDocPage}API_StartAccountBootstrapAction.html)  **
  - **Description:** Grants permission to start account bootstrap action for a domain
  - **Resource types (\*required):** [domain\*](#list_datazone-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataSourceRunActivities](${APIReferenceDocPage}API_UpdateDataSourceRunActivities.html)  **
  - **Description:** Grants permission to update data source run activities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEnvironmentConfiguration](${APIReferenceDocPage}API_UpdateEnvironmentConfiguration.html)  **
  - **Description:** Grants permission to update environment configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEnvironmentDeploymentStatus](${APIReferenceDocPage}API_UpdateEnvironmentDeploymentStatus.html)  **
  - **Description:** Grants permission to update status of the Environment deployment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ValidatePassRole](${APIReferenceDocPage}API_ValidatePassRole.html)  **
  - **Description:** Grants permission to validate pass role
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon DataZone
<a name="list_datazone-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [domain](https://docs.aws.amazon.com/datazone/latest/userguide/create-domain.html)  | arn:${Partition}:datazone:${Region}:${Account}:domain/${DomainId} | [aws:ResourceTag/${TagKey}](#list_datazone-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon DataZone
<a name="list_datazone-policy-keys"></a>

Amazon DataZone defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [datazone:domainId](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#amazondatazone-policy-keys)  | Filters access by the domain ID passed in the request | String | 
|   [datazone:projectId](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#amazondatazone-policy-keys)  | Filters access by the project ID passed in the request | String | 
|   [datazone:userId](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#amazondatazone-policy-keys)  | Filters access by the user ID passed in the request | String | 