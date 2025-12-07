# Source configuration for WIZ CNAPP

## Integrating with Wiz CNAPP

Wiz is a cloud-native application protection platform (CNAPP) that provides comprehensive visibility and security across multi-cloud environments. CloudWatch Pipeline uses the Wiz GraphQL API to retrieve information about security posture, vulnerabilities, misconfigurations, threats, and audit activities from your cloud infrastructure. The Wiz GraphQL API enables access to security data through flexible GraphQL queries, allowing retrieval of audit logs, issues, vulnerability findings, configuration findings, and detections from the Wiz platform.

## Authenticating with Wiz CNAPP

To read Wiz Cnapp audit Logs, the pipeline needs to authenticate with your account. The plugin supports OAuth2 Authentication. Follow these instructions to get started.

- Create a Service Account in Wiz with appropriate permissions. You must be logged in as a Wiz user with Write (W) permission on service accounts.
- Configure the Service Account and get newly created Client ID and Client Secret.
- In the AWS Secrets Manager, create a secret and store the Application (client) ID under the key `client_id` and the client secret under the key `client_secret`.
- Configure API permissions (scopes) for your Service Account.

Required scope: `read:issues`, `read:detections`, `read:cloud_events_cloud`, `read:cloud_events_sensor`, `read:security_scans`, `read:vulnerabilities`, `read:cloud_configuration`, `admin:audit`

- Identify your GraphQL API endpoint: To find your specific endpoint check Tenant Info in the Wiz portal. The Wiz GraphQL API endpoint is `https://api.<region>.app.wiz.io/graphql`, where `<region>` corresponds to your Wiz tenant's datacenter (e.g., us1, us2, eu1, eu2).

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read audit logs from Wiz, choose Wiz CNAPP as the data source. Fill in the required information like Region. Once you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and events that map to Detection Finding (2004), Vulnerability Finding (2002), Compliance Finding (2003), Authentication (3002), and API Activity (6003).

**Detection Finding** contains all events from following sources:

- Issues
- Detections

**Vulnerability Finding** contains all events from following sources:

- Vulnerability Findings

**Compliance Finding** contains all events from following sources:

- Cloud Configuration Findings

**Authentication** contains events from following sources and given actions:

- Audit logs
- DeviceLogin
- Login

**API Activity** contains events from following sources and given actions:

- Audit logs
- AddSecurityScan
- AddSupportTicketContext
- AiAssistantSendMessage
- ApproveCopyResourceForensicsSettings...
- AssociateServiceTicket
- CancelReportRun
- ClearUIUserPreferences
- CompleteAuthMigration
- ConvertGitHubAppRegistrationCode
- CopyResourceForensicsToExternalAccount
- CreateActionTemplate
- CreateApplicationServiceDiscoveryRule
- CreateAutomationRule
- CreateCICDScanPolicy
- CreateCloudConfigurationFindingNote
- CreateCloudConfigurationRule
- CreateCloudConfigurationRules
- CreateCloudEventRule
- CreateComputeGroupTagsSet
- CreateConnector
- CreateControl
- CreateCustomIPRange
- CreateDashboard
- CreateDashboardWidget
- CreateDataClassifier
- CreateDigitalTrustCustomDomain
- CreateFileIntegrityMonitoringExclusion
- CreateHostConfigurationAssessmentNote
- CreateHostConfigurationRule
- CreateIgnoreRule
- CreateImageIntegrityValidator
- CreateIntegration
- CreateIssueNote
- CreateMalwareExclusion
- CreateMonitoredMetric
- CreateOutpost
- CreateOutpostCluster
- CreatePolicyPackage
- CreatePortalView
- CreateProject
- CreateRemediationAndResponseDeployment
- CreateRemediationPullRequest
- CreateReport
- CreateRuntimeResponsePolicy
- CreateSAMLIdentityProvider
- CreateSAMLUser
- CreateSavedCloudEventFilter
- CreateSavedGraphQuery
- CreateScannerAPIRateLimit
- CreateSecurityFramework
- CreateServiceAccount
- CreateSupportTicket
- CreateTestNode
- CreateUser
- CreateUserRole
- CreateVulnerabilityFindingNote
- DeleteActionTemplate
- DeleteApplicationServiceDiscoveryRule
- DeleteAutomationRule
- DeleteCICDScan
- DeleteCICDScanPolicy
- DeleteCloudConfigurationFindingNote
- DeleteCloudConfigurationRule
- DeleteCloudEventRule
- DeleteComputeGroupTagsSet
- DeleteConnector
- DeleteControl
- DeleteCustomIPRange
- DeleteDashboard
- DeleteDashboardWidget
- DeleteDataClassifier
- DeleteDigitalTrustCustomDomain
- DeleteFileIntegrityMonitoringExclusion
- DeleteHostConfigurationAssessmentNote
- DeleteHostConfigurationRule
- DeleteIgnoreRule
- DeleteImageIntegrityValidator
- DeleteIntegration
- DeleteIssueNote
- DeleteMalwareExclusion
- DeleteMonitoredMetric
- DeleteOutpost
- DeleteOutpostCluster
- DeletePolicyPackage
- DeletePortalView
- DeleteProject
- DeleteRemediationAndResponseDeployment
- DeleteReport
- DeleteRuntimeResponsePolicy
- DeleteSAMLIdentityProvider
- DeleteSavedCloudEventFilter
- DeleteSavedGraphQuery
- DeleteScannerAPIRateLimit
- DeleteSecurityFramework
- DeleteSecurityScan
- DeleteServiceAccount
- DeleteTestNode
- DeleteUser
- DeleteUserRole
- DeleteVulnerabilityFindingNote
- DisassociateServiceTicket
- DuplicateDashboard
- DuplicateDataClassifier
- DuplicateHostConfigurationRule
- DuplicateSecurityFramework
- DuplicateUserRole
- FinalizeCICDScan
- FinalizeCICDScanTelemetry
- GenerateWizContainerRegistryToken
- GraphSearch
- InitiateCICDScanTelemetry
- InitiateDiskScanContainerImage
- InitiateDiskScanDirectory
- InitiateDiskScanVirtualMachine
- InitiateDiskScanVirtualMachineImage
- InitiateIACScan
- InvokeOutpostClusterUpdate
- LegalConsent
- MergeDiscoveredApplicationService
- MigrateUsers
- ModifySAMLIdentityProviderGroupMappings
- ModifySAMLIdentityProviderPortalView...
- PromoteDiscoveredApplicationService
- ProvideAiFeedback
- ProvideAiGraphQueryExample
- ProvideAiGraphQueryFeedback
- ProvideIssueFeedback
- ReassessIssue
- RefreshResponseActions
- RegisterAgent
- ReportIDEActivityHeartbeat
- ReportIDEAnalytics
- RequestConnectorEntityScan
- RequestConnectorScan
- RerunReport
- ResetUserPassword
- RevokeSessions
- RevokeUserSessions
- RotateServiceAccountSecret
- RunAllControls
- RunCloudConfigurationRule
- RunControl
- RunControlsIntegrationAction
- RunIssuesIntegrationAction
- RunOutpostClusterUpdate
- RunResponseAction
- SAMLUserInitialProvision
- SendUserEmailInvite
- TagCICDScan
- TokenDeviceRefresh
- TokenRefresh
- UninstallOutpost
- UpdateAiSettings
- UpdateApplicationServiceDiscoveryRule
- UpdateAutomationRule
- UpdateBasicAuthSettings
- UpdateCICDScanPolicy
- UpdateChampionCenterJourneyItem
- UpdateCloudConfigurationFinding
- UpdateCloudConfigurationRule
- UpdateCloudConfigurationRules
- UpdateCloudCostSettings
- UpdateCloudEventRule
- UpdateCloudEventRules
- UpdateCloudEventSettings
- UpdateComputeGroupTagsSet
- UpdateConnector
- UpdateContainerRegistryCustomScannin...
- UpdateContainerRegistryGlobalScannin...
- UpdateControl
- UpdateControls
- UpdateCopyResourceForensicsSettings
- UpdateCustomIPRange
- UpdateCustomIPRangesSettings
- UpdateCustomUserRolesSettings
- UpdateDashboard
- UpdateDashboardSettings
- UpdateDashboardWidget
- UpdateDataClassifier
- UpdateDataFinding
- UpdateDataScannerSettings
- UpdateDigitalTrustCustomDomain
- UpdateDigitalTrustDashboardSettings
- UpdateDigitalTrustSAMLIdentityProvider
- UpdateDiscoveredApplicationServices
- UpdateEventTriggeredScanningSettings
- UpdateExternalExposureScannerSettings
- UpdateExternalExposureSettings
- UpdateFileIntegrityMonitoringExclusion
- UpdateFileIntegrityMonitoringSettings
- UpdateForensicsPackageSettings
- UpdateGraphEntity
- UpdateHostConfigurationRule
- UpdateHostConfigurationRuleAssessment
- UpdateHostConfigurationRules
- UpdateIPRestrictions
- UpdateIgnoreRule
- UpdateImageIntegrityValidator
- UpdateIntegration
- UpdateInternalExposureSettings
- UpdateIssue
- UpdateIssueNote
- UpdateIssueSettings
- UpdateIssues
- UpdateKubernetesGlobalScanningConfig...
- UpdateLoginSettings
- UpdateMalwareExclusion
- UpdateMonitoredMetric
- UpdateMonitoredMetricSettings
- UpdateNode
- UpdateNonOSDiskScanningSettings
- UpdateNotificationSettings
- UpdateOutpost
- UpdateOutpostCluster
- UpdatePolicyPackage
- UpdatePortalInactivityTimeoutSettings
- UpdatePortalSettings
- UpdatePortalView
- UpdatePreviewHubItem
- UpdateProject
- UpdateRemediationAndResponseDeployment
- UpdateReport
- UpdateReportSettings
- UpdateRepositorySettings
- UpdateResponseAction
- UpdateResponseActions
- UpdateRuntimeResponsePolicy
- UpdateSAMLIdentityProvider
- UpdateSavedCloudEventFilter
- UpdateSavedGraphQuery
- UpdateScannerAPIRateLimit
- UpdateScannerExclusionSettingsConstr...
- UpdateScannerExclusionSettingsTimeLi...
- UpdateScannerExclusionSizeLimits
- UpdateScannerExclusionTags
- UpdateScannerResourceTagSettings
- UpdateScannerResourceTags
- UpdateScannerSettings
- UpdateSecretInstance
- UpdateSecurityFramework
- UpdateSecurityScan
- UpdateServiceAccount
- UpdateSessionLifetimeSettings
- UpdateSupportContactList
- UpdateSystemHealthIssue
- UpdateSystemHealthIssues
- UpdateTechnology
- UpdateTenantNewsletterSettings
- UpdateUIUserPreferences
- UpdateUser
- UpdateUserRole
- UpdateUserSelectedPortalView
- UpdateVersionControlOrganizationSett...
- UpdateVersionControlRepositorySettings
- UpdateViewerPreferences
- UpdateVulnerability
- UpdateVulnerabilityAssessmentSettings
- UpdateVulnerabilityFinding
- UpdateVulnerabilityFindingStatus
- UpsertAgentTelemetry

[Show moreShow less](# "#")
