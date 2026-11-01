

# Designation permissions
<a name="designation-permissions"></a>

Amazon SageMaker Unified Studio provides managed designations, and domain administrators can create custom designations. The following sections describe the permissions available for custom designations, including the underlying APIs that each permission grants, and the Cedar policies that define the managed designations.

**Note**  
Designations control actions in the Amazon SageMaker Unified Studio project interface, not data access. Data operations in the query editor, such as querying or modifying tables, are governed by the project's IAM role, not by designations.

## Custom designation permissions
<a name="custom-designation-permissions"></a>

With custom designations, domain administrators can select permissions grouped by category in the visual permission selector. The following table lists the available permissions by category and the underlying APIs that each permission grants.


| Category | Permission | API Action | 
| --- | --- | --- | 
| Project | All actions | CreateEnvironment, UpdateEnvironment, DeleteEnvironment, GetEnvironmentActionLink, AssociateEnvironmentRole, DisassociateEnvironmentRole, GetEnvironmentCredentials, CreateProjectMembership, DeleteProjectMembership, UpdateProjectMembership, UpdateProject, DeleteProject, StartCompute, GetCompute, StopCompute | 
| Project | Read-only actions | GetCompute | 
| Project | Manage membership | CreateProjectMembership, DeleteProjectMembership, UpdateProjectMembership | 
| Project | Manage environments | CreateEnvironment, UpdateEnvironment, DeleteEnvironment, GetEnvironmentActionLink, AssociateEnvironmentRole, DisassociateEnvironmentRole, GetEnvironmentCredentials | 
| Project | Manage user compute | StartCompute, GetCompute, StopCompute | 
| Project | Access external links | GetEnvironmentActionLink | 
| Catalog | All actions | CreateAsset, CreateAssetRevision, DeleteAsset, GetAsset, ListAssetRevisions, BatchGetAttributesMetadata, BatchPutAttributesMetadata, CreateDataProduct, CreateDataProductRevision, DeleteDataProduct, GetDataProduct, ListDataProductRevisions, CreateListingChangeSet, DeleteListing, CreateGlossary, UpdateGlossary, DeleteGlossary, CreateGlossaryTerm, UpdateGlossaryTerm, DeleteGlossaryTerm, CreateAssetType, DeleteAssetType, CreateFormType, DeleteFormType, PostTimeSeriesDataPoints, DeleteTimeSeriesDataPoints, GetTimeSeriesDataPoint, ListTimeSeriesDataPoints, AcceptPredictions, RejectPredictions, StartMetadataGenerationRun, CancelMetadataGenerationRun, StopMetadataGenerationRun, GetMetadataGenerationRun, AssociateGovernedTerms, DisassociateGovernedTerms, Search | 
| Catalog | Read-only actions | GetAsset, ListAssetRevisions, BatchGetAttributesMetadata, GetDataProduct, ListDataProductRevisions, GetTimeSeriesDataPoint, ListTimeSeriesDataPoints, GetMetadataGenerationRun, Search | 
| Catalog | Manage assets | CreateAsset, CreateAssetRevision, DeleteAsset, GetAsset, ListAssetRevisions, BatchGetAttributesMetadata, BatchPutAttributesMetadata | 
| Catalog | Manage data products | CreateDataProduct, CreateDataProductRevision, DeleteDataProduct, GetDataProduct, ListDataProductRevisions | 
| Catalog | Manage asset publishing | CreateListingChangeSet, DeleteListing | 
| Catalog | Manage glossaries | CreateGlossary, UpdateGlossary, DeleteGlossary, CreateGlossaryTerm, UpdateGlossaryTerm, DeleteGlossaryTerm | 
| Catalog | Manage asset types | CreateAssetType, DeleteAssetType | 
| Catalog | Manage metadata forms | CreateFormType, DeleteFormType | 
| Catalog | Manage time series data | PostTimeSeriesDataPoints, DeleteTimeSeriesDataPoints, GetTimeSeriesDataPoint, ListTimeSeriesDataPoints | 
| Catalog | Manage predictions | AcceptPredictions, RejectPredictions | 
| Catalog | Execute metadata generation | StartMetadataGenerationRun, CancelMetadataGenerationRun, StopMetadataGenerationRun, GetMetadataGenerationRun | 
| Catalog | Manage governed terms | AssociateGovernedTerms, DisassociateGovernedTerms | 
| Subscriptions | All actions | CreateSubscriptionRequest, UpdateSubscriptionRequest, DeleteSubscriptionRequest, CancelSubscription, AcceptSubscriptionRequest, RejectSubscriptionRequest, RevokeSubscription, CreateSubscriptionGrant, DeleteSubscriptionGrant, CreateAssetFilter, UpdateAssetFilter, DeleteAssetFilter, GetAssetFilter, ListAssetFilters | 
| Subscriptions | Read-only actions | GetAssetFilter, ListAssetFilters | 
| Subscriptions | Manage subscription requests | CreateSubscriptionRequest, UpdateSubscriptionRequest, DeleteSubscriptionRequest, CancelSubscription, DeleteSubscriptionGrant | 
| Subscriptions | Manage subscription approvals | AcceptSubscriptionRequest, RejectSubscriptionRequest, RevokeSubscription, CreateSubscriptionGrant, DeleteSubscriptionGrant | 
| Subscriptions | Manage asset filters | CreateAssetFilter, UpdateAssetFilter, DeleteAssetFilter, GetAssetFilter, ListAssetFilters | 
| Connections | All actions | CreateConnection, UpdateConnection, DeleteConnection, GetConnection, ListConnections, StartDataSourceRun | 
| Connections | Read-only actions | ListConnections | 
| Connections | Use connection | GetConnection | 
| Connections | Manage connections | CreateConnection, UpdateConnection, DeleteConnection, GetConnection, ListConnections, StartDataSourceRun | 
| Notebooks and Querybooks | All actions | CreateNotebook, DeleteNotebook, GetNotebook, UpdateNotebook, ListNotebooks, StartNotebookCompute, StopNotebookCompute, GetNotebookCompute, StartNotebookImport, StartNotebookExport, GetNotebookExport, CreateCell, GetCell, UpdateCell, DeleteCell, BatchGetCell, CreateCellRun, GetCellRun, BatchGetCellRun, DeleteCellRun, UpdateCellRun, ListCellRuns, GetCellRunResult, PutCellRunResult, StartNotebookRun, GetNotebookRun, StopNotebookRun, ListNotebookRuns, StartNotebookSync | 
| Notebooks and Querybooks | Read-only actions | GetNotebook, ListNotebooks, GetNotebookCompute, GetNotebookExport, GetCell, BatchGetCell, GetCellRun, BatchGetCellRun, ListCellRuns, GetCellRunResult, GetNotebookRun, ListNotebookRuns | 
| DataAgent | All actions | StartConversation, GetConversation, ListConversations, UpdateConversation, DeleteConversation, SendMessage, InvokeAgent, CancelMessage, StopAgent, GenerateCode, AssociateAgentContext, DisassociateAgentContext, UpdateAgentContext, ListAgentContexts | 

**Note**  
The Notebooks and Querybooks category governs both notebooks and querybooks. The Query Editor is built on notebooks, and notebook permissions govern both. As a result, granting the Notebooks and Querybooks permissions also applies them to querybooks.

## Managed designations
<a name="managed-designation-permissions"></a>

AWS provides two managed designations, Owner and Contributor, that you cannot edit or delete. A Cedar policy defines each managed designation. The following sections show the Cedar policy for each designation.

```
@name("ProjectOwner-1")
permit (
    principal,
    action in [
    Connections::Action::"DeleteDataSource"
    ],
    resource
);

@name("ProjectOwner-5")
permit (
    principal,
    action in [
    DataZone::Action::"BatchDeleteLinkedTypes",
    DataZone::Action::"BatchPutLinkedTypes"
    ],
    resource
);

@name("ProjectOwner-2")
permit (
    principal,
    action in [
    Project::Action::"UpdateProject",
    Project::Action::"DeleteProject",
    Project::Action::"CreateProjectMembership",
    Project::Action::"DeleteProjectMembership",
    Project::Action::"UpdateProjectMembership"
    ],
    resource
);

@name("ProjectOwner-3")
 permit(
     principal,
     action in [
         Project::Action::"UpdateEnvironment"
     ],
     resource
 ) when {
    (context has domainVersion) && ["V2"].contains(context.domainVersion)
 };

@name("ProjectOwner-4")
 permit (
    principal,
    action in [
        DataZone::Action::"AddPolicyGrant",
        DataZone::Action::"RemovePolicyGrant"
    ],
    resource
 ) when {
    ["USE_ASSET_TYPE", "ATTACH_GOVERNED_GLOSSARY_TERMS"].contains(action.policyType)
 };

@name("ProjectOwner-6")
permit (
    principal,
    action in [
        Catalog::Action::"DeleteAssetType",
        Catalog::Action::"DeleteFormType",

        Catalog::Action::"UpdateGlossary",
        Catalog::Action::"DeleteGlossary",
        Catalog::Action::"UpdateGlossaryTerm",
        Catalog::Action::"DeleteGlossaryTerm",
        Catalog::Action::"RelateGlossaryTerm",
        Catalog::Action::"CreateAsset",
        Catalog::Action::"BatchGetAttributesMetadata",
        Catalog::Action::"BatchPutAttributesMetadata",
        Catalog::Action::"CreateAssetRevision",
        Catalog::Action::"DeleteAsset",
        Catalog::Action::"GetAsset",
        Catalog::Action::"ListAssetRevisions",
        Catalog::Action::"CreateListingChangeSet",
        Catalog::Action::"DeleteListing",
        Catalog::Action::"CreateDataProduct",
        Catalog::Action::"CreateDataProductRevision",
        Catalog::Action::"DeleteDataProduct",
        Catalog::Action::"GetDataProduct",
        Catalog::Action::"ListDataProductRevisions",
        Catalog::Action::"AcceptPredictions",
        Catalog::Action::"RejectPredictions",
        Catalog::Action::"StartMetadataGenerationRun",
        Catalog::Action::"GetMetadataGenerationRun",
        Catalog::Action::"CancelMetadataGenerationRun",

        Connections::Action::"CreateDataSource",
        Connections::Action::"UpdateDataSource",
        Connections::Action::"StartDataSourceRun",
        Connections::Action::"UpdateDataSourceRunActivities",

        Catalog::Action::"PostTimeSeriesDataPoints",
        Catalog::Action::"ListTimeSeriesDataPoints",
        Catalog::Action::"GetTimeSeriesDataPoint",
        Catalog::Action::"DeleteTimeSeriesDataPoints",

        Catalog::Action::"Search"
    ],
    resource
);

@name("ProjectOwner-7")
permit (
    principal,
    action in [
        Subscriptions::Action::"CreateSubscriptionGrant",
        Subscriptions::Action::"CreateSubscriptionRequest",
        Subscriptions::Action::"UpdateSubscriptionRequest",
        Subscriptions::Action::"AcceptSubscriptionRequest",
        Subscriptions::Action::"RejectSubscriptionRequest",
        Subscriptions::Action::"DeleteSubscriptionRequest",
        Subscriptions::Action::"DeleteSubscriptionGrant",
        Subscriptions::Action::"CancelSubscription",
        Subscriptions::Action::"RevokeSubscription"
    ],
    resource
);

@name("ProjectOwner-8")
permit (
    principal,
    action in [
        Subscriptions::Action::"CreateAssetFilter",
        Subscriptions::Action::"GetAssetFilter",
        Subscriptions::Action::"UpdateAssetFilter",
        Subscriptions::Action::"DeleteAssetFilter",
        Subscriptions::Action::"ListAssetFilters",

        DataZone::Action::"ListJobRuns",
        DataZone::Action::"GetJobRun"
    ],
    resource
);

@name("ProjectOwner-9")
permit (
    principal,
    action in [
        Notebooks::Action::"CreateNotebook",
        Notebooks::Action::"GetNotebook",
        Notebooks::Action::"UpdateNotebook",
        Notebooks::Action::"DeleteNotebook",
        Notebooks::Action::"ListNotebooks",
        Notebooks::Action::"StartNotebookSync",
        Notebooks::Action::"StartNotebookImport",
        Notebooks::Action::"StartNotebookExport",
        Notebooks::Action::"GetNotebookExport",
        Notebooks::Action::"StartNotebookCompute",
        Notebooks::Action::"StopNotebookCompute",
        Notebooks::Action::"GetNotebookCompute",
        Notebooks::Action::"StartNotebookRun",
        Notebooks::Action::"GetNotebookRun",
        Notebooks::Action::"StopNotebookRun",
        Notebooks::Action::"ListNotebookRuns",
        Notebooks::Action::"CreateCell",
        Notebooks::Action::"GetCell",
        Notebooks::Action::"BatchGetCell",
        Notebooks::Action::"UpdateCell",
        Notebooks::Action::"DeleteCell",
        Notebooks::Action::"CreateCellRun",
        Notebooks::Action::"UpdateCellRun",
        Notebooks::Action::"DeleteCellRun",
        Notebooks::Action::"GetCellRun",
        Notebooks::Action::"BatchGetCellRun",
        Notebooks::Action::"ListCellRuns",
        Notebooks::Action::"PutCellRunResult",
        Notebooks::Action::"GetCellRunResult",
        Notebooks::Action::"CreateDataApp",
        Notebooks::Action::"GetDataApp",
        Notebooks::Action::"UpdateDataApp",
        Notebooks::Action::"DeleteDataApp",
        Notebooks::Action::"ListDataApps"
    ],
    resource
);

@name("ProjectOwner-10")
permit (
    principal,
    action in [
        SageMakerUnifiedStudio::Action::"ListConversations",
        SageMakerUnifiedStudio::Action::"GetConversation",
        SageMakerUnifiedStudio::Action::"StartConversation",
        SageMakerUnifiedStudio::Action::"GenerateCode",
        SageMakerUnifiedStudio::Action::"SendMessage",
        SageMakerUnifiedStudio::Action::"UpdateNotebookCompute"
    ],
    resource
);

@name("ProjectOwner-11")
permit (
    principal,
    action in [
        Project::Action::"DeleteEnvironment",
        Project::Action::"UpdateEnvironmentStatus",
        Project::Action::"GetEnvironmentCredentials",
        Project::Action::"GetEnvironmentActionLink",
        Project::Action::"AssociateEnvironmentRole",
        Project::Action::"GetEnvironmentRole",
        Project::Action::"UpdateEnvironmentRole",
        Project::Action::"ListEnvironmentRoles",
        Project::Action::"DisassociateEnvironmentRole",
        Project::Action::"CreateEnvironmentAction",
        Project::Action::"UpdateEnvironmentAction",
        Project::Action::"DeleteEnvironmentAction",
        Project::Action::"GetEnvironmentAction",
        Project::Action::"ListEnvironmentActions",

        Project::Action::"UpdateEnvironmentProfile",
        Project::Action::"DeleteEnvironmentProfile",
        Project::Action::"CreateEnvironmentProfile"
    ],
    resource
);

@name("ProjectOwner-12")
permit(
    principal,
    action in [
        Project::Action::"UpdateEnvironment"
    ],
    resource
) when {
    (resource has projectDomainVersion) &&
    resource.projectDomainVersion == "V1"
};

@name("ProjectOwner-13")
permit(
    principal,
    action in [
        Project::Action::"UpdateEnvironment"
    ],
    resource
) when {
    (resource has projectDomainVersion) &&
    resource.projectDomainVersion == "V2" &&
    (
        ((resource has blueprintName) && resource.blueprintName == "AwsServiceBlueprint") ||
        ((resource has sourceDeploymentMode) && ["ON_DEMAND"].contains(resource.sourceDeploymentMode)
        && (resource has destinationDeploymentMode) && ["ON_DEMAND"].contains(resource.destinationDeploymentMode))
    )
};

@name("ProjectOwner-14")
permit(
    principal,
    action in [
        Project::Action::"CreateEnvironment"
    ],
    resource
) when {
    (resource has projectDomainVersion) &&
    resource.projectDomainVersion == "V1" &&
    !(resource has environmentProfileIdentifier) &&
    ["CustomAwsService"].contains(resource.blueprintName)
};

@name("ProjectOwner-15")
permit(
    principal,
    action in [
        Project::Action::"CreateEnvironment"
    ],
    resource
) when {
    (resource has projectDomainVersion) &&
    resource.projectDomainVersion == "V2" &&
    !(resource has environmentConfigurationId) &&
    ["AwsServiceBlueprint"].contains(resource.blueprintName)
};

@name("ProjectOwner-16")
permit(
    principal,
    action in [
        Catalog::Action::"AssociateGovernedTerms",
        Catalog::Action::"DisassociateGovernedTerms"
    ],
    resource
) when {
    (resource has governedGlossary) && (resource.governedGlossary == false)
};

@name("ProjectOwner-17")
permit (
    principal,
    action in [
        Connections::Action::"CreateConnection",
        Connections::Action::"GetConnection",
        Connections::Action::"UpdateConnection",
        Connections::Action::"DeleteConnection",
        Connections::Action::"ListConnections",

        Connections::Action::"CreateCredential",
        Connections::Action::"GetCredential",
        Connections::Action::"UpdateCredential",
        Connections::Action::"DeleteCredential",
        Connections::Action::"ListCredentials"
    ],
    resource
);

@name("ProjectOwner-18")
permit (
    principal,
    action in [
        Catalog::Action::"CreateGlossary",
        Catalog::Action::"CreateGlossaryTerm",
        Catalog::Action::"CreateFormType",
        Catalog::Action::"CreateAssetType"
    ],
    resource
);

@name("ProjectOwner-19")
permit (
    principal,
    action in [
        Project::Action::"CreateEnvironment"
    ],
    resource
) when {
    ((resource has environmentConfigurationId) || (resource has environmentBlueprintId)) &&
    !(resource has environmentProfileIdentifier)
};

@name("ProjectOwner-20")
permit (
    principal,
    action in [
        Project::Action::"CreateEnvironment"
    ],
    resource
) when {
    !(resource has environmentConfigurationId) &&
    !(resource has environmentBlueprintId) &&
    (resource has environmentProfileIdentifier)
};

@name("ProjectOwner-21")
permit (
    principal,
    action in [
        DataAgent::Action::"StartConversation",
        DataAgent::Action::"GetConversation",
        DataAgent::Action::"ListConversations",
        DataAgent::Action::"UpdateConversation",
        DataAgent::Action::"DeleteConversation",
        DataAgent::Action::"SendMessage",
        DataAgent::Action::"InvokeAgent",
        DataAgent::Action::"CancelMessage",
        DataAgent::Action::"StopAgent",
        DataAgent::Action::"GenerateCode",
        DataAgent::Action::"AssociateAgentContext",
        DataAgent::Action::"DisassociateAgentContext",
        DataAgent::Action::"UpdateAgentContext",
        DataAgent::Action::"ListAgentContexts"
    ],
    resource
);
```

```
@name("ProjectContributor-1")
permit (
    principal,
    action in [
        Catalog::Action::"DeleteAssetType",
        Catalog::Action::"DeleteFormType",

        Catalog::Action::"UpdateGlossary",
        Catalog::Action::"DeleteGlossary",
        Catalog::Action::"UpdateGlossaryTerm",
        Catalog::Action::"DeleteGlossaryTerm",
        Catalog::Action::"RelateGlossaryTerm",
        Catalog::Action::"CreateAsset",
        Catalog::Action::"BatchGetAttributesMetadata",
        Catalog::Action::"BatchPutAttributesMetadata",
        Catalog::Action::"CreateAssetRevision",
        Catalog::Action::"DeleteAsset",
        Catalog::Action::"GetAsset",
        Catalog::Action::"ListAssetRevisions",
        Catalog::Action::"CreateListingChangeSet",
        Catalog::Action::"DeleteListing",
        Catalog::Action::"CreateDataProduct",
        Catalog::Action::"CreateDataProductRevision",
        Catalog::Action::"DeleteDataProduct",
        Catalog::Action::"GetDataProduct",
        Catalog::Action::"ListDataProductRevisions",
        Catalog::Action::"AcceptPredictions",
        Catalog::Action::"RejectPredictions",
        Catalog::Action::"StartMetadataGenerationRun",
        Catalog::Action::"GetMetadataGenerationRun",
        Catalog::Action::"CancelMetadataGenerationRun",

        Connections::Action::"CreateDataSource",
        Connections::Action::"UpdateDataSource",
        Connections::Action::"StartDataSourceRun",
        Connections::Action::"UpdateDataSourceRunActivities",

        Catalog::Action::"PostTimeSeriesDataPoints",
        Catalog::Action::"ListTimeSeriesDataPoints",
        Catalog::Action::"GetTimeSeriesDataPoint",
        Catalog::Action::"DeleteTimeSeriesDataPoints",

        Catalog::Action::"Search"
    ],
    resource
);

@name("ProjectContributor-2")
permit (
    principal,
    action in [
        Subscriptions::Action::"CreateSubscriptionGrant",
        Subscriptions::Action::"CreateSubscriptionRequest",
        Subscriptions::Action::"UpdateSubscriptionRequest",
        Subscriptions::Action::"AcceptSubscriptionRequest",
        Subscriptions::Action::"RejectSubscriptionRequest",
        Subscriptions::Action::"DeleteSubscriptionRequest",
        Subscriptions::Action::"DeleteSubscriptionGrant",
        Subscriptions::Action::"CancelSubscription",
        Subscriptions::Action::"RevokeSubscription"
    ],
    resource
);

@name("ProjectContributor-3")
permit (
    principal,
    action in [
        Subscriptions::Action::"CreateAssetFilter",
        Subscriptions::Action::"GetAssetFilter",
        Subscriptions::Action::"UpdateAssetFilter",
        Subscriptions::Action::"DeleteAssetFilter",
        Subscriptions::Action::"ListAssetFilters",

        DataZone::Action::"ListJobRuns",
        DataZone::Action::"GetJobRun"
    ],
    resource
);

@name("ProjectContributor-4")
permit (
    principal,
    action in [
        Notebooks::Action::"CreateNotebook",
        Notebooks::Action::"GetNotebook",
        Notebooks::Action::"UpdateNotebook",
        Notebooks::Action::"DeleteNotebook",
        Notebooks::Action::"ListNotebooks",
        Notebooks::Action::"StartNotebookSync",
        Notebooks::Action::"StartNotebookImport",
        Notebooks::Action::"StartNotebookExport",
        Notebooks::Action::"GetNotebookExport",
        Notebooks::Action::"StartNotebookCompute",
        Notebooks::Action::"StopNotebookCompute",
        Notebooks::Action::"GetNotebookCompute",
        Notebooks::Action::"StartNotebookRun",
        Notebooks::Action::"GetNotebookRun",
        Notebooks::Action::"StopNotebookRun",
        Notebooks::Action::"ListNotebookRuns",
        Notebooks::Action::"CreateCell",
        Notebooks::Action::"GetCell",
        Notebooks::Action::"BatchGetCell",
        Notebooks::Action::"UpdateCell",
        Notebooks::Action::"DeleteCell",
        Notebooks::Action::"CreateCellRun",
        Notebooks::Action::"UpdateCellRun",
        Notebooks::Action::"DeleteCellRun",
        Notebooks::Action::"GetCellRun",
        Notebooks::Action::"BatchGetCellRun",
        Notebooks::Action::"ListCellRuns",
        Notebooks::Action::"PutCellRunResult",
        Notebooks::Action::"GetCellRunResult",
        Notebooks::Action::"CreateDataApp",
        Notebooks::Action::"GetDataApp",
        Notebooks::Action::"UpdateDataApp",
        Notebooks::Action::"DeleteDataApp",
        Notebooks::Action::"ListDataApps"
    ],
    resource
);

@name("ProjectContributor-5")
permit (
    principal,
    action in [
        SageMakerUnifiedStudio::Action::"ListConversations",
        SageMakerUnifiedStudio::Action::"GetConversation",
        SageMakerUnifiedStudio::Action::"StartConversation",
        SageMakerUnifiedStudio::Action::"GenerateCode",
        SageMakerUnifiedStudio::Action::"SendMessage",
        SageMakerUnifiedStudio::Action::"UpdateNotebookCompute"
    ],
    resource
);

@name("ProjectContributor-6")
permit (
    principal,
    action in [
        Project::Action::"DeleteEnvironment",
        Project::Action::"UpdateEnvironmentStatus",
        Project::Action::"GetEnvironmentCredentials",
        Project::Action::"GetEnvironmentActionLink",
        Project::Action::"AssociateEnvironmentRole",
        Project::Action::"GetEnvironmentRole",
        Project::Action::"UpdateEnvironmentRole",
        Project::Action::"ListEnvironmentRoles",
        Project::Action::"DisassociateEnvironmentRole",
        Project::Action::"CreateEnvironmentAction",
        Project::Action::"UpdateEnvironmentAction",
        Project::Action::"DeleteEnvironmentAction",
        Project::Action::"GetEnvironmentAction",
        Project::Action::"ListEnvironmentActions",

        Project::Action::"UpdateEnvironmentProfile",
        Project::Action::"DeleteEnvironmentProfile",
        Project::Action::"CreateEnvironmentProfile"
    ],
    resource
);

@name("ProjectContributor-7")
permit(
    principal,
    action in [
        Project::Action::"UpdateEnvironment"
    ],
    resource
) when {
    (resource has projectDomainVersion) &&
    resource.projectDomainVersion == "V1"
};

@name("ProjectContributor-8")
permit(
    principal,
    action in [
        Project::Action::"UpdateEnvironment"
    ],
    resource
) when {
    (resource has projectDomainVersion) &&
    resource.projectDomainVersion == "V2" &&
    (
        ((resource has blueprintName) && resource.blueprintName == "AwsServiceBlueprint") ||
        ((resource has sourceDeploymentMode) && ["ON_DEMAND"].contains(resource.sourceDeploymentMode)
        && (resource has destinationDeploymentMode) && ["ON_DEMAND"].contains(resource.destinationDeploymentMode))
    )
};

@name("ProjectContributor-9")
permit(
    principal,
    action in [
        Project::Action::"CreateEnvironment"
    ],
    resource
) when {
    (resource has projectDomainVersion) &&
    resource.projectDomainVersion == "V1" &&
    !(resource has environmentProfileIdentifier) &&
    ["CustomAwsService"].contains(resource.blueprintName)
};

@name("ProjectContributor-10")
permit(
    principal,
    action in [
        Project::Action::"CreateEnvironment"
    ],
    resource
) when {
    (resource has projectDomainVersion) &&
    resource.projectDomainVersion == "V2" &&
    !(resource has environmentConfigurationId) &&
    ["AwsServiceBlueprint"].contains(resource.blueprintName)
};

@name("ProjectContributor-11")
permit(
    principal,
    action in [
        Catalog::Action::"AssociateGovernedTerms",
        Catalog::Action::"DisassociateGovernedTerms"
    ],
    resource
) when {
    (resource has governedGlossary) && (resource.governedGlossary == false)
};

@name("ProjectContributor-12")
permit (
    principal,
    action in [
        Connections::Action::"CreateConnection",
        Connections::Action::"GetConnection",
        Connections::Action::"UpdateConnection",
        Connections::Action::"DeleteConnection",
        Connections::Action::"ListConnections",

        Connections::Action::"CreateCredential",
        Connections::Action::"GetCredential",
        Connections::Action::"UpdateCredential",
        Connections::Action::"DeleteCredential",
        Connections::Action::"ListCredentials"
    ],
    resource
);

@name("ProjectContributor-13")
permit (
    principal,
    action in [
        Catalog::Action::"CreateGlossary",
        Catalog::Action::"CreateGlossaryTerm",
        Catalog::Action::"CreateFormType",
        Catalog::Action::"CreateAssetType"
    ],
    resource
);

@name("ProjectContributor-14")
permit (
    principal,
    action in [
        Project::Action::"CreateEnvironment"
    ],
    resource
) when {
    ((resource has environmentConfigurationId) || (resource has environmentBlueprintId)) &&
    !(resource has environmentProfileIdentifier)
};

@name("ProjectContributor-15")
permit (
    principal,
    action in [
        Project::Action::"CreateEnvironment"
    ],
    resource
) when {
    !(resource has environmentConfigurationId) &&
    !(resource has environmentBlueprintId) &&
    (resource has environmentProfileIdentifier)
};

@name("ProjectContributor-16")
permit (
    principal,
    action in [
        DataAgent::Action::"StartConversation",
        DataAgent::Action::"GetConversation",
        DataAgent::Action::"ListConversations",
        DataAgent::Action::"UpdateConversation",
        DataAgent::Action::"DeleteConversation",
        DataAgent::Action::"SendMessage",
        DataAgent::Action::"InvokeAgent",
        DataAgent::Action::"CancelMessage",
        DataAgent::Action::"StopAgent",
        DataAgent::Action::"GenerateCode",
        DataAgent::Action::"AssociateAgentContext",
        DataAgent::Action::"DisassociateAgentContext",
        DataAgent::Action::"UpdateAgentContext",
        DataAgent::Action::"ListAgentContexts"
    ],
    resource
);

@name("ProjectContributor-17")
permit (
    principal,
    action in [
        DataZone::Action::"AddPolicyGrant",
        DataZone::Action::"RemovePolicyGrant",
        DataZone::Action::"ListPolicyGrants"
    ],
    resource
) when { resource has policyType && ["CreateEnvironment", "CREATE_ENVIRONMENT"].contains(resource.policyType) };
```