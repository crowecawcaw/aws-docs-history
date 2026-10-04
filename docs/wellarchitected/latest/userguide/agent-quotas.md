

AWS Well-Architected Agent is in preview release and is subject to change.

# AWS Well-Architected Agent Quotas and limits
<a name="agent-quotas"></a>

## Access and entitlements
<a name="agent-access"></a>

AWS WA Agent access and entitlements depend on your AWS Support plan tier.


**Support tier entitlements**  

| Support tier | Access | Max profiles | Max applications per profile | 
| --- | --- | --- | --- | 
| Developer | No | — | — | 
| Business | No | — | — | 
| Business\+ | Yes | 2 | 7 | 
| Enterprise On-Ramp | Yes | 10 | 30 | 
| Enterprise Support | Yes | 10 | 30 | 
| Unified Operations | Yes | 10 | 30 | 

## Quotas and limits
<a name="agent-quotas-limits"></a>


| Resource | Default limit | Notes | 
| --- | --- | --- | 
| Accounts per profile | 100 | Maximum AWS accounts that a single profile can analyze. | 
| Goals per profile | 10 | Maximum active business goals per profile. | 
| Profile hosting Regions | 3 | Profiles can be hosted in US East (N. Virginia), US East (Ohio), or US West (Oregon). | 
| Scannable Regions | All commercial | AWS WA Agent can scan resources in any commercial AWS Region, regardless of where the profile is hosted. | 
| Recommendations per generation run | 30 | Maximum recommendations produced per scheduled or manual generation run. There is no limit on total stored recommendations. Future runs can add new recommendations. | 
| Architecture reviews per day | 5 | Maximum architecture review generations per day, per profile. Reviews can be run consecutively without cooldown while quota remains. | 
| Scheduled recommendation generation cooldown | 7 days (1 week) | Minimum time between scheduled recommendation generation runs for the same profile. | 
| Maximum .zip file upload size | 25 MB | Maximum compressed size of an uploaded .zip file for architecture reviews. | 
| Maximum Amazon S3 folder size | 100 MB | Maximum total size of an Amazon S3 folder referenced for architecture reviews. | 
| Maximum individual file size (Amazon S3 folder) | 1 MB | Maximum size of each individual file in an Amazon S3 folder referenced for architecture reviews. | 

## Unsupported resource types
<a name="agent-unsupported-resources"></a>

AWS WA Agent does not analyze the CloudFormation resource types in the following table. If your application uses these resource types, AWS WA Agent does not retrieve their configuration data and does not include them in resource-level recommendations.

For more information about specifying the services and resource types your application uses, see [Updating application context](agent-update-app-context.md).


**Resource types not supported by AWS WA Agent**  

| Service | Unsupported resource types | 
| --- | --- | 
| `AWS::ACMPCA` |  + `AWS::ACMPCA::Certificate`<br />+ `AWS::ACMPCA::CertificateAuthorityActivation`<br />+ `AWS::ACMPCA::Permission`  | 
| `AWS::AmplifyUIBuilder` |  + `AWS::AmplifyUIBuilder::Component`<br />+ `AWS::AmplifyUIBuilder::Form`<br />+ `AWS::AmplifyUIBuilder::Theme`  | 
| `AWS::ApiGateway` |  + `AWS::ApiGateway::Account`<br />+ `AWS::ApiGateway::Method`  | 
| `AWS::ApiGatewayV2` |  + `AWS::ApiGatewayV2::IntegrationResponse`<br />+ `AWS::ApiGatewayV2::RouteResponse`  | 
| `AWS::AppConfig` |  + `AWS::AppConfig::Deployment`<br />+ `AWS::AppConfig::HostedConfigurationVersion`  | 
| `AWS::ApplicationAutoScaling` |  + `AWS::ApplicationAutoScaling::ScalableTarget`<br />+ `AWS::ApplicationAutoScaling::ScalingPolicy`  | 
| `AWS::AppStream` |  + `AWS::AppStream::AppBlock`<br />+ `AWS::AppStream::Application`<br />+ `AWS::AppStream::ApplicationEntitlementAssociation`<br />+ `AWS::AppStream::ApplicationFleetAssociation`<br />+ `AWS::AppStream::Entitlement`  | 
| `AWS::AppSync` |  + `AWS::AppSync::DomainNameApiAssociation`  | 
| `AWS::AppTest` |  + `AWS::AppTest::TestCase`  | 
| `AWS::AuditManager` |  + `AWS::AuditManager::Assessment`  | 
| `AWS::Bedrock` |  + `AWS::Bedrock::GuardrailVersion`  | 
| `AWS::BillingConductor` |  + `AWS::BillingConductor::BillingGroup`<br />+ `AWS::BillingConductor::CustomLineItem`<br />+ `AWS::BillingConductor::PricingPlan`<br />+ `AWS::BillingConductor::PricingRule`  | 
| `AWS::Cassandra` |  + `AWS::Cassandra::Keyspace`<br />+ `AWS::Cassandra::Type`  | 
| `AWS::CE` |  + `AWS::CE::AnomalyMonitor`<br />+ `AWS::CE::AnomalySubscription`  | 
| `AWS::CertificateManager` |  + `AWS::CertificateManager::Account`  | 
| `AWS::CloudFormation` |  + `AWS::CloudFormation::ModuleVersion`<br />+ `AWS::CloudFormation::Publisher`<br />+ `AWS::CloudFormation::ResourceDefaultVersion`<br />+ `AWS::CloudFormation::ResourceVersion`  | 
| `AWS::CloudFront` |  + `AWS::CloudFront::MonitoringSubscription`  | 
| `AWS::CloudTrail` |  + `AWS::CloudTrail::ResourcePolicy`  | 
| `AWS::Cognito` |  + `AWS::Cognito::LogDeliveryConfiguration`<br />+ `AWS::Cognito::ManagedLoginBranding`<br />+ `AWS::Cognito::UserPoolDomain`<br />+ `AWS::Cognito::UserPoolRiskConfigurationAttachment`<br />+ `AWS::Cognito::UserPoolUICustomizationAttachment`<br />+ `AWS::Cognito::UserPoolUserToGroupAttachment`  | 
| `AWS::Config` |  + `AWS::Config::OrganizationConformancePack`  | 
| `AWS::Connect` |  + `AWS::Connect::ContactFlowVersion`<br />+ `AWS::Connect::DataTableAttribute`<br />+ `AWS::Connect::DataTableRecord`<br />+ `AWS::Connect::InstanceStorageConfig`<br />+ `AWS::Connect::UserHierarchyStructure`<br />+ `AWS::Connect::ViewVersion`  | 
| `AWS::ControlTower` |  + `AWS::ControlTower::EnabledBaseline`<br />+ `AWS::ControlTower::EnabledControl`  | 
| `AWS::DataZone` |  + `AWS::DataZone::DataSource`<br />+ `AWS::DataZone::DomainUnit`<br />+ `AWS::DataZone::Environment`<br />+ `AWS::DataZone::EnvironmentActions`<br />+ `AWS::DataZone::FormType`<br />+ `AWS::DataZone::Owner`<br />+ `AWS::DataZone::PolicyGrant`<br />+ `AWS::DataZone::ProjectMembership`<br />+ `AWS::DataZone::ProjectProfile`  | 
| `AWS::Deadline` |  + `AWS::Deadline::QueueEnvironment`  | 
| `AWS::Detective` |  + `AWS::Detective::OrganizationAdmin`  | 
| `AWS::DeviceFarm` |  + `AWS::DeviceFarm::DevicePool`<br />+ `AWS::DeviceFarm::InstanceProfile`<br />+ `AWS::DeviceFarm::NetworkProfile`<br />+ `AWS::DeviceFarm::Project`<br />+ `AWS::DeviceFarm::TestGridProject`<br />+ `AWS::DeviceFarm::VPCEConfiguration`  | 
| `AWS::EC2` |  + `AWS::EC2::EnclaveCertificateIamRoleAssociation`<br />+ `AWS::EC2::GatewayRouteTableAssociation`<br />+ `AWS::EC2::VPCBlockPublicAccessOptions`  | 
| `AWS::ECS` |  + `AWS::ECS::ExpressGatewayService`<br />+ `AWS::ECS::PrimaryTaskSet`<br />+ `AWS::ECS::TaskSet`  | 
| `AWS::ElasticLoadBalancingV2` |  + `AWS::ElasticLoadBalancingV2::ListenerRule`  | 
| `AWS::EMR` |  + `AWS::EMR::Step`  | 
| `AWS::EventSchemas` |  + `AWS::EventSchemas::RegistryPolicy`  | 
| `AWS::Evidently` |  + `AWS::Evidently::Experiment`<br />+ `AWS::Evidently::Feature`<br />+ `AWS::Evidently::Launch`<br />+ `AWS::Evidently::Project`<br />+ `AWS::Evidently::Segment`  | 
| `AWS::FMS` |  + `AWS::FMS::NotificationChannel`<br />+ `AWS::FMS::Policy`<br />+ `AWS::FMS::ResourceSet`  | 
| `AWS::GlobalAccelerator` |  + `AWS::GlobalAccelerator::EndpointGroup`  | 
| `AWS::Glue` |  + `AWS::Glue::IdentityCenterConfiguration`<br />+ `AWS::Glue::SchemaVersionMetadata`  | 
| `AWS::IAM` |  + `AWS::IAM::GroupPolicy`<br />+ `AWS::IAM::RolePolicy`<br />+ `AWS::IAM::ServiceLinkedRole`<br />+ `AWS::IAM::UserPolicy`  | 
| `AWS::IdentityStore` |  + `AWS::IdentityStore::GroupMembership`  | 
| `AWS::Inspector` |  + `AWS::Inspector::AssessmentTarget`<br />+ `AWS::Inspector::AssessmentTemplate`<br />+ `AWS::Inspector::ResourceGroup`  | 
| `AWS::InspectorV2` |  + `AWS::InspectorV2::CisScanConfiguration`  | 
| `AWS::IoT` |  + `AWS::IoT::ThingType`  | 
| `AWS::IoTAnalytics` |  + `AWS::IoTAnalytics::Channel`<br />+ `AWS::IoTAnalytics::Dataset`<br />+ `AWS::IoTAnalytics::Datastore`<br />+ `AWS::IoTAnalytics::Pipeline`  | 
| `AWS::IoTEvents` |  + `AWS::IoTEvents::AlarmModel`<br />+ `AWS::IoTEvents::DetectorModel`<br />+ `AWS::IoTEvents::Input`  | 
| `AWS::IoTFleetWise` |  + `AWS::IoTFleetWise::Campaign`<br />+ `AWS::IoTFleetWise::DecoderManifest`<br />+ `AWS::IoTFleetWise::Fleet`<br />+ `AWS::IoTFleetWise::ModelManifest`<br />+ `AWS::IoTFleetWise::SignalCatalog`<br />+ `AWS::IoTFleetWise::StateTemplate`<br />+ `AWS::IoTFleetWise::Vehicle`  | 
| `AWS::IoTSiteWise` |  + `AWS::IoTSiteWise::Dashboard`  | 
| `AWS::Kinesis` |  + `AWS::Kinesis::ResourcePolicy`  | 
| `AWS::LakeFormation` |  + `AWS::LakeFormation::PrincipalPermissions`<br />+ `AWS::LakeFormation::TagAssociation`  | 
| `AWS::Lambda` |  + `AWS::Lambda::LayerVersion`<br />+ `AWS::Lambda::LayerVersionPermission`  | 
| `AWS::LicenseManager` |  + `AWS::LicenseManager::Grant`<br />+ `AWS::LicenseManager::License`  | 
| `AWS::Logs` |  + `AWS::Logs::AccountPolicy`  | 
| `AWS::LookoutVision` |  + `AWS::LookoutVision::Project`  | 
| `AWS::Macie` |  + `AWS::Macie::AllowList`<br />+ `AWS::Macie::CustomDataIdentifier`<br />+ `AWS::Macie::FindingsFilter`  | 
| `AWS::MediaConnect` |  + `AWS::MediaConnect::BridgeOutput`<br />+ `AWS::MediaConnect::BridgeSource`  | 
| `AWS::MediaLive` |  + `AWS::MediaLive::ChannelPlacementGroup`<br />+ `AWS::MediaLive::Cluster`<br />+ `AWS::MediaLive::Network`<br />+ `AWS::MediaLive::SdiSource`  | 
| `AWS::MediaPackageV2` |  + `AWS::MediaPackageV2::ChannelPolicy`<br />+ `AWS::MediaPackageV2::OriginEndpoint`<br />+ `AWS::MediaPackageV2::OriginEndpointPolicy`  | 
| `AWS::MediaTailor` |  + `AWS::MediaTailor::ChannelPolicy`  | 
| `AWS::NetworkFirewall` |  + `AWS::NetworkFirewall::LoggingConfiguration`  | 
| `AWS::Notifications` |  + `AWS::Notifications::ManagedNotificationAccountContactAssociation`<br />+ `AWS::Notifications::ManagedNotificationAdditionalChannelAssociation`  | 
| `AWS::ObservabilityAdmin` |  + `AWS::ObservabilityAdmin::OrganizationCentralizationRule`<br />+ `AWS::ObservabilityAdmin::OrganizationTelemetryRule`<br />+ `AWS::ObservabilityAdmin::TelemetryRule`  | 
| `AWS::ODB` |  + `AWS::ODB::CloudAutonomousVmCluster`<br />+ `AWS::ODB::CloudExadataInfrastructure`<br />+ `AWS::ODB::CloudVmCluster`<br />+ `AWS::ODB::OdbNetwork`<br />+ `AWS::ODB::OdbPeeringConnection`  | 
| `AWS::OpenSearchServerless` |  + `AWS::OpenSearchServerless::AccessPolicy`<br />+ `AWS::OpenSearchServerless::LifecyclePolicy`<br />+ `AWS::OpenSearchServerless::SecurityConfig`<br />+ `AWS::OpenSearchServerless::SecurityPolicy`  | 
| `AWS::OpenSearchService` |  + `AWS::OpenSearchService::Domain`  | 
| `AWS::Organizations` |  + `AWS::Organizations::Account`<br />+ `AWS::Organizations::OrganizationalUnit`<br />+ `AWS::Organizations::Policy`<br />+ `AWS::Organizations::ResourcePolicy`  | 
| `AWS::Panorama` |  + `AWS::Panorama::PackageVersion`  | 
| `AWS::PCAConnectorAD` |  + `AWS::PCAConnectorAD::TemplateGroupAccessControlEntry`  | 
| `AWS::QLDB` |  + `AWS::QLDB::Stream`  | 
| `AWS::QuickSight` |  + `AWS::QuickSight::Analysis`<br />+ `AWS::QuickSight::Dashboard`<br />+ `AWS::QuickSight::DataSet`<br />+ `AWS::QuickSight::DataSource`<br />+ `AWS::QuickSight::RefreshSchedule`<br />+ `AWS::QuickSight::Template`<br />+ `AWS::QuickSight::Theme`<br />+ `AWS::QuickSight::Topic`<br />+ `AWS::QuickSight::VPCConnection`  | 
| `AWS::Rbin` |  + `AWS::Rbin::Rule`  | 
| `AWS::RefactorSpaces` |  + `AWS::RefactorSpaces::Application`<br />+ `AWS::RefactorSpaces::Route`<br />+ `AWS::RefactorSpaces::Service`  | 
| `AWS::ResourceExplorer2` |  + `AWS::ResourceExplorer2::DefaultViewAssociation`  | 
| `AWS::RTBFabric` |  + `AWS::RTBFabric::InboundExternalLink`<br />+ `AWS::RTBFabric::Link`<br />+ `AWS::RTBFabric::OutboundExternalLink`  | 
| `AWS::S3` |  + `AWS::S3::AccessGrant`<br />+ `AWS::S3::AccessGrantsLocation`<br />+ `AWS::S3::MultiRegionAccessPointPolicy`  | 
| `AWS::S3ObjectLambda` |  + `AWS::S3ObjectLambda::AccessPointPolicy`  | 
| `AWS::S3Outposts` |  + `AWS::S3Outposts::AccessPoint`<br />+ `AWS::S3Outposts::Bucket`<br />+ `AWS::S3Outposts::BucketPolicy`  | 
| `AWS::S3Tables` |  + `AWS::S3Tables::Table`<br />+ `AWS::S3Tables::TablePolicy`  | 
| `AWS::SageMaker` |  + `AWS::SageMaker::Device`<br />+ `AWS::SageMaker::DeviceFleet`  | 
| `AWS::SecurityHub` |  + `AWS::SecurityHub::AggregatorV2`<br />+ `AWS::SecurityHub::AutomationRule`<br />+ `AWS::SecurityHub::AutomationRuleV2`<br />+ `AWS::SecurityHub::ConfigurationPolicy`<br />+ `AWS::SecurityHub::ConnectorV2`<br />+ `AWS::SecurityHub::DelegatedAdmin`<br />+ `AWS::SecurityHub::FindingAggregator`<br />+ `AWS::SecurityHub::Insight`<br />+ `AWS::SecurityHub::OrganizationConfiguration`<br />+ `AWS::SecurityHub::PolicyAssociation`<br />+ `AWS::SecurityHub::ProductSubscription`<br />+ `AWS::SecurityHub::SecurityControl`<br />+ `AWS::SecurityHub::Standard`  | 
| `AWS::SecurityLake` |  + `AWS::SecurityLake::AWSLogSource`<br />+ `AWS::SecurityLake::Subscriber`<br />+ `AWS::SecurityLake::SubscriberNotification`  | 
| `AWS::ServiceCatalog` |  + `AWS::ServiceCatalog::CloudFormationProvisionedProduct`<br />+ `AWS::ServiceCatalog::PortfolioProductAssociation`<br />+ `AWS::ServiceCatalog::ServiceActionAssociation`<br />+ `AWS::ServiceCatalog::TagOption`<br />+ `AWS::ServiceCatalog::TagOptionAssociation`  | 
| `AWS::SES` |  + `AWS::SES::VdmAttributes`  | 
| `AWS::Shield` |  + `AWS::Shield::DRTAccess`<br />+ `AWS::Shield::ProactiveEngagement`<br />+ `AWS::Shield::Protection`<br />+ `AWS::Shield::ProtectionGroup`  | 
| `AWS::SimSpaceWeaver` |  + `AWS::SimSpaceWeaver::Simulation`  | 
| `AWS::SNS` |  + `AWS::SNS::TopicInlinePolicy`  | 
| `AWS::SQS` |  + `AWS::SQS::QueueInlinePolicy`  | 
| `AWS::SSMContacts` |  + `AWS::SSMContacts::Rotation`  | 
| `AWS::SSO` |  + `AWS::SSO::Application`<br />+ `AWS::SSO::ApplicationAssignment`<br />+ `AWS::SSO::Assignment`<br />+ `AWS::SSO::InstanceAccessControlAttributeConfiguration`<br />+ `AWS::SSO::PermissionSet`  | 
| `AWS::Timestream` |  + `AWS::Timestream::Database`<br />+ `AWS::Timestream::ScheduledQuery`<br />+ `AWS::Timestream::Table`  | 
| `AWS::VoiceID` |  + `AWS::VoiceID::Domain`  | 
| `AWS::VpcLattice` |  + `AWS::VpcLattice::AuthPolicy`<br />+ `AWS::VpcLattice::ResourcePolicy`<br />+ `AWS::VpcLattice::Rule`  | 
| `AWS::WAFv2` |  + `AWS::WAFv2::IPSet`<br />+ `AWS::WAFv2::RegexPatternSet`<br />+ `AWS::WAFv2::RuleGroup`<br />+ `AWS::WAFv2::WebACL`<br />+ `AWS::WAFv2::WebACLAssociation`  | 
| `AWS::Wisdom` |  + `AWS::Wisdom::AIAgentVersion`<br />+ `AWS::Wisdom::AIGuardrailVersion`<br />+ `AWS::Wisdom::AIPromptVersion`  | 