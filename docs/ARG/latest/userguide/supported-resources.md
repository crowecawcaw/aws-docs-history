# Resource types you can use with AWS Resource Groups and

Tag Editor

You can use the AWS Management Console or the AWS CLI to create resource groups and then interact with
the member resources through those groups. You can add tags to many AWS resources and then
use those tags to manage group membership. This topic describes the AWS resource types
that you can include in resource groups by using AWS Resource Groups, and the resource types
that you can tag by using Tag Editor.

###### Important

A resource group based on a query for **All supported resource
types** can add members automatically over time, as new resources are
supported by Resource Groups. When you run automations or other bulk tasks on an existing resource
group based on **All supported resource types**, be aware that the
actions might run on many more resources than were in the group when you first created
the group. This might also mean that automations or tasks that you created for other
resources are applied to possibly unintended resources, or resources on which the tasks
cannot be successfully completed. In those cases, you can add a resource type filter to
specify that only resources of the specified types can be part of the group.

![Query based on All supported resource types.](images/rg-allsupported-resources.png)
The following tables list which resource types are supported for tagging in Tag Editor, for
membership in tag query-based groups, and for membership in AWS CloudFormation stack-based groups.

###### Column definitions

- **Tag Editor Tagging** – You can tag resources of
  this type by using the [Tag Editor console](https://console.aws.amazon.com/resource-groups/tag-editor/ "https://console.aws.amazon.com/resource-groups/tag-editor/"). Otherwise, you must use either the [AWS Resource Groups Tagging API](../../../resourcegroupstagging/latest/APIReference/overview.md "../../../resourcegroupstagging/latest/APIReference/overview.md") or the tagging services supported natively by that
  resource’s owning service.
- **Tag-based Groups** – You can include
  resources of this type in [resource groups whose membership is determined by the tags attached to the
  resources](gettingstarted-query.md#gettingstarted-query-tag-based "gettingstarted-query.md#gettingstarted-query-tag-based"). The group specifies tag key names and values, and any
  resources with tags that match are automatically part of the group
- **AWS CloudFormation Stack-based Groups** – You can include
  resources of this type in [resource groups whose membership consists of the resources created as part of a
  CloudFormation stack](gettingstarted-query.md#gettingstarted-query-stack-based "gettingstarted-query.md#gettingstarted-query-stack-based"). The group specifies the stack’s ARN, and all of
  its resources are automatically members of the group. Adding tags to a AWS CloudFormation stack causes an update of the stack.
  For a list of resource types that are deprecated and no longer supported by Resource Groups, see the
  section [Deprecated resource types](#deprecated-types "#deprecated-types") at the end of
  this topic.

###### Note

Resource Groups and Tag Editor support the resource types in the following table,
but some resource types may not be available in your AWS Region.

## AWS DeepComposer

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DeepComposer::Composition` | No                     | Yes                  | No                                        |
| `AWS::DeepComposer::Model`       | No                     | Yes                  | No                                        |

## Amazon API Gateway

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ApiGateway::Account`           | No                     | No                   | Yes                                       |
| `AWS::ApiGateway::ApiKey`            | No                     | Yes                  | Yes                                       |
| `AWS::ApiGateway::ClientCertificate` | No                     | Yes                  | No                                        |
| `AWS::ApiGateway::DomainName`        | No                     | No                   | Yes                                       |
| `AWS::ApiGateway::RestApi`           | No                     | Yes                  | Yes                                       |
| `AWS::ApiGateway::Stage`             | No                     | Yes                  | No                                        |
| `AWS::ApiGateway::UsagePlan`         | No                     | Yes                  | Yes                                       |

## Amazon API Gateway V2

| **Resources**            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ApiGatewayV2::Api` | No                     | Yes                  | No                                        |

## IAM Access Analyzer

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AccessAnalyzer::Analyzer` | No                     | Yes                  | No                                        |

## AWS Amplify

| **Resources**       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Amplify::App` | No                     | Yes                  | No                                        |

## AWS App Runner

| **Resources**                                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AppRunner::AutoScalingConfiguration`   | No                     | Yes                  | No                                        |
| `AWS::AppRunner::Connection`                 | No                     | Yes                  | No                                        |
| `AWS::AppRunner::ObservabilityConfiguration` | No                     | Yes                  | No                                        |
| `AWS::AppRunner::Service`                    | No                     | Yes                  | No                                        |
| `AWS::AppRunner::VpcConnector`               | No                     | Yes                  | No                                        |
| `AWS::AppRunner::VpcIngressConnection`       | No                     | Yes                  | No                                        |

## AWS AppConfig

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AppConfig::Application`          | No                     | Yes                  | No                                        |
| `AWS::AppConfig::ConfigurationProfile` | No                     | Yes                  | No                                        |
| `AWS::AppConfig::Deployment`           | No                     | Yes                  | No                                        |
| `AWS::AppConfig::DeploymentStrategy`   | No                     | Yes                  | No                                        |
| `AWS::AppConfig::Extension`            | No                     | Yes                  | No                                        |
| `AWS::AppConfig::ExtensionAssociation` | No                     | Yes                  | No                                        |

## AWS AppFabric

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AppFabric::AppAuthorization` | No                     | Yes                  | No                                        |
| `AWS::AppFabric::AppBundle`        | No                     | Yes                  | No                                        |
| `AWS::AppFabric::Ingestion`        | No                     | Yes                  | No                                        |

## Amazon AppFlow

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AppFlow::Connector` | No                     | Yes                  | No                                        |
| `AWS::AppFlow::Flow`      | No                     | Yes                  | No                                        |

## AppIntegrations

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AppIntegrations::Application`      | No                     | Yes                  | No                                        |
| `AWS::AppIntegrations::DataIntegration`  | No                     | Yes                  | No                                        |
| `AWS::AppIntegrations::EventIntegration` | No                     | Yes                  | No                                        |

## AWS App Mesh

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AppMesh::GatewayRoute`   | No                     | Yes                  | No                                        |
| `AWS::AppMesh::Mesh`           | No                     | Yes                  | No                                        |
| `AWS::AppMesh::Route`          | No                     | Yes                  | No                                        |
| `AWS::AppMesh::VirtualGateway` | No                     | Yes                  | No                                        |
| `AWS::AppMesh::VirtualNode`    | No                     | Yes                  | No                                        |
| `AWS::AppMesh::VirtualRouter`  | No                     | Yes                  | No                                        |
| `AWS::AppMesh::VirtualService` | No                     | Yes                  | No                                        |

## Amazon AppStream

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AppStream::AppBlock`        | No                     | Yes                  | No                                        |
| `AWS::AppStream::AppBlockBuilder` | No                     | Yes                  | No                                        |
| `AWS::AppStream::Application`     | No                     | Yes                  | No                                        |
| `AWS::AppStream::Fleet`           | Yes                    | Yes                  | Yes                                       |
| `AWS::AppStream::Image`           | No                     | Yes                  | No                                        |
| `AWS::AppStream::ImageBuilder`    | Yes                    | Yes                  | Yes                                       |
| `AWS::AppStream::Stack`           | Yes                    | Yes                  | Yes                                       |

## AWS AppSync

| **Resources**              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AppSync::Api`        | No                     | Yes                  | No                                        |
| `AWS::AppSync::DataSource` | No                     | No                   | Yes                                       |
| `AWS::AppSync::DomainName` | No                     | Yes                  | No                                        |
| `AWS::AppSync::GraphQLApi` | No                     | No                   | Yes                                       |

## Application Auto Scaling

| **Resources**                                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ApplicationAutoScaling::ScalableTarget` | No                     | Yes                  | No                                        |

## AWS Application Migration Service

| **Resources**                                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MGN::Application`                      | No                     | Yes                  | No                                        |
| `AWS::MGN::Connector`                        | No                     | Yes                  | No                                        |
| `AWS::MGN::Job`                              | No                     | Yes                  | No                                        |
| `AWS::MGN::LaunchConfigurationTemplate`      | No                     | Yes                  | No                                        |
| `AWS::MGN::ReplicationConfigurationTemplate` | No                     | Yes                  | No                                        |
| `AWS::MGN::SourceServer`                     | No                     | Yes                  | No                                        |
| `AWS::MGN::VcenterClient`                    | No                     | Yes                  | No                                        |
| `AWS::MGN::Wave`                             | No                     | Yes                  | No                                        |

## Artificial intelligence operations (AIOps)

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AIOps::InvestigationGroup` | No                     | Yes                  | No                                        |

## Amazon Athena

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Athena::CapacityReservation` | No                     | Yes                  | No                                        |
| `AWS::Athena::DataCatalog`         | No                     | Yes                  | No                                        |
| `AWS::Athena::WorkGroup`           | No                     | Yes                  | No                                        |

## AWS Audit Manager

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AuditManager::Assessment`          | No                     | Yes                  | No                                        |
| `AWS::AuditManager::AssessmentFramework` | No                     | Yes                  | No                                        |
| `AWS::AuditManager::Control`             | No                     | Yes                  | No                                        |

## AWS B2B Data Interchange

| **Resources**            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::B2BI::Capability`  | No                     | Yes                  | No                                        |
| `AWS::B2BI::Partnership` | No                     | Yes                  | No                                        |
| `AWS::B2BI::Profile`     | No                     | Yes                  | No                                        |
| `AWS::B2BI::Transformer` | No                     | Yes                  | No                                        |

## AWS Backup

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Backup::BackupPlan`         | No                     | Yes                  | No                                        |
| `AWS::Backup::BackupVault`        | No                     | Yes                  | No                                        |
| `AWS::Backup::Framework`          | No                     | Yes                  | No                                        |
| `AWS::Backup::LegalHold`          | No                     | Yes                  | No                                        |
| `AWS::Backup::ReportPlan`         | No                     | Yes                  | No                                        |
| `AWS::Backup::RestoreTestingPlan` | No                     | Yes                  | No                                        |

## AWS Backup gateway

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::BackupGateway::VirtualMachine` | No                     | Yes                  | No                                        |

## AWS Backup search

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::BackupSearch::SearchExportJob` | No                     | Yes                  | No                                        |
| `AWS::BackupSearch::SearchJob`       | No                     | Yes                  | No                                        |

## AWS Batch

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Batch::ComputeEnvironment` | No                     | Yes                  | No                                        |
| `AWS::Batch::ConsumableResource` | No                     | Yes                  | No                                        |
| `AWS::Batch::Job`                | No                     | Yes                  | No                                        |
| `AWS::Batch::JobDefinition`      | No                     | Yes                  | No                                        |
| `AWS::Batch::JobQueue`           | No                     | Yes                  | No                                        |
| `AWS::Batch::SchedulingPolicy`   | No                     | Yes                  | No                                        |

## Amazon Bedrock

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Bedrock::Agent`                       | No                     | Yes                  | No                                        |
| `AWS::Bedrock::AgentAlias`                  | No                     | Yes                  | No                                        |
| `AWS::Bedrock::ApplicationInferenceProfile` | No                     | Yes                  | No                                        |
| `AWS::Bedrock::AsyncInvoke`                 | No                     | Yes                  | No                                        |
| `AWS::Bedrock::CustomModel`                 | No                     | Yes                  | No                                        |
| `AWS::Bedrock::EvaluationJob`               | No                     | Yes                  | No                                        |
| `AWS::Bedrock::Flow`                        | No                     | Yes                  | No                                        |
| `AWS::Bedrock::FlowAlias`                   | No                     | Yes                  | No                                        |
| `AWS::Bedrock::Guardrail`                   | No                     | Yes                  | No                                        |
| `AWS::Bedrock::KnowledgeBase`               | No                     | Yes                  | No                                        |
| `AWS::Bedrock::ModelCustomizationJob`       | No                     | Yes                  | No                                        |
| `AWS::Bedrock::ModelEvaluationJob`          | No                     | Yes                  | No                                        |
| `AWS::Bedrock::ModelImportJob`              | No                     | Yes                  | No                                        |
| `AWS::Bedrock::ModelInvocationJob`          | No                     | Yes                  | No                                        |
| `AWS::Bedrock::PromptVersion`               | No                     | Yes                  | No                                        |

## AWS Billing Conductor

| **Resources**                           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::BillingConductor::BillingGroup`   | No                     | Yes                  | Yes                                       |
| `AWS::BillingConductor::CustomLineItem` | No                     | Yes                  | Yes                                       |
| `AWS::BillingConductor::PricingPlan`    | No                     | Yes                  | Yes                                       |
| `AWS::BillingConductor::PricingRule`    | No                     | Yes                  | Yes                                       |

## AWS Billing and Cost Management

| **Resources**               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Billing::BillingView` | No                     | Yes                  | No                                        |

## Amazon Braket

| **Resources**              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Braket::Job`         | No                     | Yes                  | No                                        |
| `AWS::Braket::QuantumTask` | Yes                    | Yes                  | No                                        |

## AWS Budgets

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Budgets::Budget`        | No                     | Yes                  | No                                        |
| `AWS::Budgets::BudgetsAction` | No                     | Yes                  | No                                        |

## AWS BugBust

| **Resources**         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::BugBust::Event` | No                     | Yes                  | No                                        |

## AWS Certificate Manager

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CertificateManager::Certificate` | Yes                    | Yes                  | Yes                                       |

## AWS Certificate Manager Private Certificate Authority

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ACMPCA::CertificateAuthority` | No                     | Yes                  | No                                        |

## Amazon Q Developer in chat applications

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Chatbot::ChatbotConfiguration` | No                     | Yes                  | No                                        |
| `AWS::Chatbot::CustomAction`         | No                     | Yes                  | No                                        |

## Amazon Chime

| **Resources**                                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Chime::AppInstance`                         | No                     | Yes                  | No                                        |
| `AWS::Chime::AppInstanceBot`                      | No                     | Yes                  | No                                        |
| `AWS::Chime::AppInstanceUser`                     | No                     | Yes                  | No                                        |
| `AWS::Chime::Channel`                             | No                     | Yes                  | No                                        |
| `AWS::Chime::MediaInsightsPipelineConfiguration`  | No                     | Yes                  | No                                        |
| `AWS::Chime::MediaPipeline`                       | No                     | Yes                  | No                                        |
| `AWS::Chime::MediaPipelineKinesisVideoStreamPool` | No                     | Yes                  | No                                        |
| `AWS::Chime::SipMediaApplication`                 | No                     | Yes                  | No                                        |
| `AWS::Chime::VoiceConnector`                      | No                     | Yes                  | No                                        |
| `AWS::Chime::VoiceProfileDomain`                  | No                     | Yes                  | No                                        |

## AWS Clean Rooms

| **Resources**                                         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CleanRooms::AnalysisTemplate`                   | No                     | Yes                  | No                                        |
| `AWS::CleanRooms::Collaboration`                      | No                     | Yes                  | No                                        |
| `AWS::CleanRooms::ConfiguredAudienceModelAssociation` | No                     | Yes                  | No                                        |
| `AWS::CleanRooms::ConfiguredTable`                    | No                     | Yes                  | No                                        |
| `AWS::CleanRooms::ConfiguredTableAssociation`         | No                     | Yes                  | No                                        |
| `AWS::CleanRooms::Membership`                         | No                     | Yes                  | No                                        |
| `AWS::CleanRooms::PrivacyBudgetTemplate`              | No                     | Yes                  | No                                        |

## AWS Clean Rooms ML

| **Resources**                                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CleanRoomsML::AudienceGenerationJob`    | No                     | Yes                  | No                                        |
| `AWS::CleanRoomsML::AudienceModel`            | No                     | Yes                  | No                                        |
| `AWS::CleanRoomsML::ConfiguredAudienceModel`  | No                     | Yes                  | No                                        |
| `AWS::CleanRoomsML::ConfiguredModelAlgorithm` | No                     | Yes                  | No                                        |
| `AWS::CleanRoomsML::TrainingDataset`          | No                     | Yes                  | No                                        |

## Amazon Cloud Directory

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CloudDirectory::Directory` | No                     | Yes                  | No                                        |

## AWS Cloud9

| **Resources**              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Cloud9::Environment` | Yes                    | Yes                  | No                                        |

## AWS CloudFormation

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CloudFormation::Stack`    | Yes                    | Yes                  | Yes                                       |
| `AWS::CloudFormation::StackSet` | No                     | Yes                  | No                                        |

## Amazon CloudFront

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CloudFront::Distribution`          | Yes¹                   | Yes²                 | Yes²                                      |
| `AWS::CloudFront::StreamingDistribution` | Yes¹                   | Yes²                 | Yes²                                      |
| `AWS::CloudFront::VpcOrigin`             | No                     | Yes²                 | No                                        |

¹ This is a resource for a global service that is hosted in the
**US East (N. Virginia)** Region. To use Tag Editor to create or
modify tags for this resource type, you must include `us-east-1` from the
**Select regions** list under **Find resources to tag** in the
Tag Editor console.

² This is a resource for a global service that is hosted in the
**US East (N. Virginia)** Region. Because Resource Groups are
maintained separately for each region, you must switch your AWS Management Console to the AWS Region that
contains the resources you want to include in the group. To create a resource group that contains
a global resource, you must configure your AWS Management Console to **US East (N. Virginia)
us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## AWS CloudHSM

| **Resources**            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CloudHSM::Backup`  | No                     | Yes                  | No                                        |
| `AWS::CloudHSM::Cluster` | No                     | Yes                  | No                                        |

## AWS Cloud Map

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ServiceDiscovery::Namespace` | No                     | Yes                  | No                                        |
| `AWS::ServiceDiscovery::Service`   | No                     | Yes                  | No                                        |

## Amazon CloudSearch

| **Resources**              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CloudSearch::Domain` | No                     | Yes                  | No                                        |

## AWS CloudTrail

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CloudTrail::Channel`        | No                     | Yes                  | No                                        |
| `AWS::CloudTrail::Dashboard`      | No                     | Yes                  | No                                        |
| `AWS::CloudTrail::EventDataStore` | No                     | Yes                  | No                                        |
| `AWS::CloudTrail::Trail`          | Yes                    | Yes                  | Yes                                       |

## Amazon CloudWatch

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CloudWatch::Alarm`                 | Yes                    | Yes                  | Yes                                       |
| `AWS::CloudWatch::Dashboard`             | No                     | No                   | Yes                                       |
| `AWS::CloudWatch::InsightRule`           | No                     | Yes                  | No                                        |
| `AWS::CloudWatch::MetricStream`          | No                     | Yes                  | No                                        |
| `AWS::CloudWatch::ServiceLevelObjective` | No                     | Yes                  | No                                        |

## Amazon CloudWatch Application Insights

| **Resources**                           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ApplicationInsights::Application` | No                     | Yes                  | No                                        |

## CloudWatch Application Signals

| **Resources**                                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ApplicationSignals::ServiceLevelObjective` | No                     | Yes                  | No                                        |

## CloudWatch Evidently

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Evidently::Feature` | No                     | Yes                  | No                                        |
| `AWS::Evidently::Launch`  | No                     | Yes                  | No                                        |
| `AWS::Evidently::Project` | No                     | Yes                  | No                                        |
| `AWS::Evidently::Segment` | No                     | Yes                  | No                                        |

## Amazon CloudWatch Logs

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Logs::AnomalyDetector`     | No                     | Yes                  | No                                        |
| `AWS::Logs::Delivery`            | No                     | Yes                  | No                                        |
| `AWS::Logs::DeliveryDestination` | No                     | Yes                  | No                                        |
| `AWS::Logs::DeliverySource`      | No                     | Yes                  | No                                        |
| `AWS::Logs::Destination`         | No                     | Yes                  | No                                        |
| `AWS::Logs::LogGroup`            | No                     | Yes                  | Yes                                       |

## Amazon CloudWatch Observability Manager

| **Resources**    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Oam::Link` | No                     | Yes                  | No                                        |
| `AWS::Oam::Sink` | No                     | Yes                  | No                                        |

## Amazon CloudWatch RUM

| **Resources**          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::RUM::AppMonitor` | No                     | Yes                  | No                                        |

## Amazon CloudWatch Synthetics

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Synthetics::Canary` | No                     | Yes                  | Yes                                       |
| `AWS::Synthetics::Group`  | No                     | Yes                  | No                                        |

## AWS CodeArtifact

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeArtifact::Domain`       | Yes                    | Yes                  | Yes                                       |
| `AWS::CodeArtifact::PackageGroup` | No                     | Yes                  | No                                        |
| `AWS::CodeArtifact::Repository`   | Yes                    | Yes                  | Yes                                       |

## AWS CodeBuild

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeBuild::Fleet`       | No                     | Yes                  | No                                        |
| `AWS::CodeBuild::Project`     | Yes                    | Yes                  | No                                        |
| `AWS::CodeBuild::ReportGroup` | No                     | Yes                  | No                                        |

## Amazon CodeCatalyst

| **Resources**                                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeCatalyst::Connection`                | No                     | Yes                  | No                                        |
| `AWS::CodeCatalyst::IdentityCenterApplication` | No                     | Yes                  | No                                        |
| `AWS::CodeCatalyst::Space`                     | No                     | Yes                  | No                                        |

## AWS CodeCommit

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeCommit::Repository` | Yes                    | Yes                  | No                                        |

## AWS CodeConnections

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeConnections::Host`           | No                     | Yes                  | No                                        |
| `AWS::CodeConnections::RepositoryLink` | No                     | Yes                  | No                                        |

## AWS CodeDeploy

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeDeploy::Application`      | No                     | Yes                  | Yes                                       |
| `AWS::CodeDeploy::DeploymentConfig` | No                     | No                   | Yes                                       |
| `AWS::CodeDeploy::DeploymentGroup`  | No                     | Yes                  | No                                        |
| `AWS::CodeDeploy::Instance`         | No                     | Yes                  | No                                        |

## Amazon CodeGuru Reviewer

| **Resources**                                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeGuruReviewer::RepositoryAssociation` | Yes                    | Yes                  | Yes                                       |

## Amazon CodeGuru Profiler

| **Resources**                           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeGuruProfiler::ProfilingGroup` | No                     | Yes                  | No                                        |

## AWS CodePipeline

| **Resources**                         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodePipeline::CustomActionType` | No                     | Yes                  | No                                        |
| `AWS::CodePipeline::Pipeline`         | Yes                    | Yes                  | Yes                                       |
| `AWS::CodePipeline::Webhook`          | Yes                    | Yes                  | Yes                                       |

## AWS CodeStar Notifications

| **Resources**                                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeStarNotifications::NotificationRule` | No                     | Yes                  | No                                        |

## AWS CodeConnections

| **Resources**                              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeStarConnections::Connection`     | No                     | Yes                  | No                                        |
| `AWS::CodeStarConnections::Host`           | No                     | Yes                  | No                                        |
| `AWS::CodeStarConnections::RepositoryLink` | No                     | Yes                  | No                                        |

## Amazon CodeWhisperer

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CodeWhisperer::Customization` | No                     | Yes                  | No                                        |
| `AWS::CodeWhisperer::Profile`       | No                     | Yes                  | No                                        |

## Amazon Cognito

| **Resources**                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Cognito::IdentityPool` | Yes                    | Yes                  | Yes                                       |
| `AWS::Cognito::UserPool`     | Yes                    | Yes                  | Yes                                       |

## Amazon Comprehend

| **Resources**                                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Comprehend::DocumentClassificationJob`     | No                     | Yes                  | No                                        |
| `AWS::Comprehend::DocumentClassifier`            | Yes                    | Yes                  | No                                        |
| `AWS::Comprehend::DocumentClassifierEndpoint`    | No                     | Yes                  | No                                        |
| `AWS::Comprehend::DominantLanguageDetectionJob`  | No                     | Yes                  | No                                        |
| `AWS::Comprehend::EntitiesDetectionJob`          | No                     | Yes                  | No                                        |
| `AWS::Comprehend::EntityRecognizer`              | Yes                    | Yes                  | No                                        |
| `AWS::Comprehend::EntityRecognizerEndpoint`      | No                     | Yes                  | No                                        |
| `AWS::Comprehend::EventsDetectionJob`            | No                     | Yes                  | No                                        |
| `AWS::Comprehend::Flywheel`                      | No                     | Yes                  | No                                        |
| `AWS::Comprehend::KeyPhrasesDetectionJob`        | No                     | Yes                  | No                                        |
| `AWS::Comprehend::PIIEntitiesDetectionJob`       | No                     | Yes                  | No                                        |
| `AWS::Comprehend::SentimentDetectionJob`         | No                     | Yes                  | No                                        |
| `AWS::Comprehend::TargetedSentimentDetectionJob` | No                     | Yes                  | No                                        |
| `AWS::Comprehend::TopicsDetectionJob`            | No                     | Yes                  | No                                        |

## AWS Config

| **Resources**                              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Config::AggregationAuthorization`    | No                     | Yes                  | No                                        |
| `AWS::Config::ConfigRule`                  | Yes                    | Yes                  | No                                        |
| `AWS::Config::ConfigurationAggregator`     | No                     | Yes                  | No                                        |
| `AWS::Config::ConfigurationRecorder`       | No                     | Yes                  | No                                        |
| `AWS::Config::ConformancePack`             | No                     | Yes                  | No                                        |
| `AWS::Config::OrganizationConfigRule`      | No                     | Yes                  | No                                        |
| `AWS::Config::OrganizationConformancePack` | No                     | Yes                  | No                                        |
| `AWS::Config::StoredQuery`                 | No                     | Yes                  | No                                        |

## Amazon Connect

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Connect::AgentStatus`              | No                     | Yes                  | No                                        |
| `AWS::Connect::Contact`                  | No                     | Yes                  | No                                        |
| `AWS::Connect::ContactEvaluation`        | No                     | Yes                  | No                                        |
| `AWS::Connect::ContactFlow`              | No                     | Yes                  | No                                        |
| `AWS::Connect::ContactFlowModule`        | No                     | Yes                  | No                                        |
| `AWS::Connect::EvaluationForm`           | No                     | Yes                  | No                                        |
| `AWS::Connect::HoursOfOperation`         | No                     | Yes                  | No                                        |
| `AWS::Connect::Instance`                 | No                     | Yes                  | No                                        |
| `AWS::Connect::IntegrationAssociation`   | No                     | Yes                  | No                                        |
| `AWS::Connect::PhoneNumber`              | No                     | Yes                  | No                                        |
| `AWS::Connect::Prompt`                   | No                     | Yes                  | No                                        |
| `AWS::Connect::Queue`                    | No                     | Yes                  | No                                        |
| `AWS::Connect::QuickConnect`             | No                     | Yes                  | No                                        |
| `AWS::Connect::RoutingProfile`           | No                     | Yes                  | No                                        |
| `AWS::Connect::Rule`                     | No                     | Yes                  | No                                        |
| `AWS::Connect::SecurityProfile`          | No                     | Yes                  | No                                        |
| `AWS::Connect::TaskTemplate`             | No                     | Yes                  | No                                        |
| `AWS::Connect::TrafficDistributionGroup` | No                     | Yes                  | No                                        |
| `AWS::Connect::UseCase`                  | No                     | Yes                  | No                                        |
| `AWS::Connect::User`                     | No                     | Yes                  | No                                        |
| `AWS::Connect::UserHierarchyGroup`       | No                     | Yes                  | No                                        |
| `AWS::Connect::Vocabulary`               | No                     | Yes                  | No                                        |

## Amazon Connect Cases

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Cases::Case`        | No                     | Yes                  | No                                        |
| `AWS::Cases::Domain`      | No                     | Yes                  | No                                        |
| `AWS::Cases::RelatedItem` | No                     | Yes                  | No                                        |

## Amazon Connect Customer Profiles

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CustomerProfiles::Domain`      | No                     | Yes                  | No                                        |
| `AWS::CustomerProfiles::Integration` | No                     | Yes                  | No                                        |
| `AWS::CustomerProfiles::ObjectType`  | No                     | Yes                  | No                                        |

## Amazon Connect Outbound Campaigns

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ConnectCampaigns::Campaign` | No                     | Yes                  | No                                        |

## Amazon Connect Voice ID

| **Resources**          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::VoiceID::Domain` | No                     | Yes                  | No                                        |

## Amazon Connect Wisdom

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Wisdom::AIAgent`              | No                     | Yes                  | No                                        |
| `AWS::Wisdom::AIGuardrail`          | No                     | Yes                  | No                                        |
| `AWS::Wisdom::AIPrompt`             | No                     | Yes                  | No                                        |
| `AWS::Wisdom::Assistant`            | No                     | Yes                  | Yes                                       |
| `AWS::Wisdom::AssistantAssociation` | No                     | Yes                  | Yes                                       |
| `AWS::Wisdom::Content`              | No                     | Yes                  | No                                        |
| `AWS::Wisdom::ContentAssociation`   | No                     | Yes                  | No                                        |
| `AWS::Wisdom::KnowledgeBase`        | No                     | Yes                  | Yes                                       |
| `AWS::Wisdom::MessageTemplate`      | No                     | Yes                  | No                                        |
| `AWS::Wisdom::QuickResponse`        | No                     | Yes                  | No                                        |
| `AWS::Wisdom::Session`              | No                     | Yes                  | No                                        |

## AWS Control Tower

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ControlTower::EnabledBaseline` | No                     | Yes                  | No                                        |
| `AWS::ControlTower::EnabledControl`  | No                     | Yes                  | No                                        |
| `AWS::ControlTower::LandingZone`     | No                     | Yes                  | No                                        |

## AWS Cost Explorer

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CE::AnomalyMonitor`      | No                     | Yes                  | No                                        |
| `AWS::CE::AnomalySubscription` | No                     | Yes                  | No                                        |
| `AWS::CE::CostCategory`        | No                     | Yes                  | No                                        |

## AWS Cost and Usage Report

| **Resources**                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::CUR::ReportDefinition` | No                     | Yes                  | No                                        |

## AWS Data Exchange

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DataExchange::DataGrants` | No                     | Yes                  | No                                        |
| `AWS::DataExchange::DataSet`    | Yes                    | Yes                  | No                                        |
| `AWS::DataExchange::Revision`   | No                     | Yes                  | No                                        |

## AWS Data Exports

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::BCMDataExports::Export` | No                     | Yes                  | No                                        |

## Amazon Data Lifecycle Manager

| **Resources**               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DLM::LifecyclePolicy` | No                     | Yes                  | No                                        |

## AWS Data Pipeline

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DataPipeline::Pipeline` | Yes                    | Yes                  | Yes                                       |

## AWS DataSync

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DataSync::Agent`         | No                     | Yes                  | No                                        |
| `AWS::DataSync::DiscoveryJob`  | No                     | Yes                  | No                                        |
| `AWS::DataSync::Location`      | No                     | Yes                  | No                                        |
| `AWS::DataSync::StorageSystem` | No                     | Yes                  | No                                        |
| `AWS::DataSync::Task`          | No                     | Yes                  | No                                        |
| `AWS::DataSync::TaskExecution` | No                     | Yes                  | No                                        |

## Amazon DataZone

| **Resources**               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DataZone::DataSource` | No                     | Yes                  | No                                        |
| `AWS::DataZone::Domain`     | No                     | Yes                  | No                                        |

## AWS Database Migration Service

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DMS::Certificate`                  | Yes                    | Yes                  | No                                        |
| `AWS::DMS::DataMigration`                | No                     | Yes                  | No                                        |
| `AWS::DMS::DataProvider`                 | No                     | Yes                  | No                                        |
| `AWS::DMS::Endpoint`                     | Yes                    | Yes                  | Yes                                       |
| `AWS::DMS::EventSubscription`            | Yes                    | Yes                  | No                                        |
| `AWS::DMS::InstanceProfile`              | No                     | Yes                  | No                                        |
| `AWS::DMS::MigrationProject`             | No                     | Yes                  | No                                        |
| `AWS::DMS::ReplicationConfig`            | No                     | Yes                  | No                                        |
| `AWS::DMS::ReplicationInstance`          | Yes                    | Yes                  | Yes                                       |
| `AWS::DMS::ReplicationSubnetGroup`       | Yes                    | Yes                  | No                                        |
| `AWS::DMS::ReplicationTask`              | Yes                    | Yes                  | No                                        |
| `AWS::DMS::ReplicationTaskAssessmentRun` | No                     | Yes                  | No                                        |

## AWS Deadline Cloud

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Deadline::Farm`            | No                     | Yes                  | No                                        |
| `AWS::Deadline::LicenseEndpoint` | No                     | Yes                  | No                                        |

## Amazon Detective

| **Resources**           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Detective::Graph` | No                     | Yes                  | No                                        |

## AWS Device Farm

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DeviceFarm::Device`            | No                     | Yes                  | No                                        |
| `AWS::DeviceFarm::DeviceInstance`    | No                     | Yes                  | No                                        |
| `AWS::DeviceFarm::InstanceProfile`   | No                     | Yes                  | No                                        |
| `AWS::DeviceFarm::Project`           | No                     | Yes                  | No                                        |
| `AWS::DeviceFarm::TestGridProject`   | No                     | Yes                  | No                                        |
| `AWS::DeviceFarm::VPCEConfiguration` | No                     | Yes                  | No                                        |

## AWS Diode Messaging

| **Resources**                         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DiodeMessaging::AccountMapping` | No                     | Yes                  | No                                        |
| `AWS::DiodeMessaging::RequestingFlow` | No                     | Yes                  | No                                        |
| `AWS::DiodeMessaging::RespondingFlow` | No                     | Yes                  | No                                        |

## AWS Diode Object Transfer

| **Resources**                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Diode::AccountMapping` | No                     | Yes                  | No                                        |
| `AWS::Diode::Transfer`       | No                     | Yes                  | No                                        |

## AWS Direct Connect

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DirectConnect::Connection`       | No                     | Yes                  | No                                        |
| `AWS::DirectConnect::Gateway`          | No                     | Yes                  | No                                        |
| `AWS::DirectConnect::Lag`              | No                     | Yes                  | No                                        |
| `AWS::DirectConnect::VirtualInterface` | No                     | Yes                  | No                                        |

## AWS Directory Service

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DirectoryService::Directory` | No                     | Yes                  | No                                        |

## Amazon DocumentDB Elastic Clusters

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DocDBElastic::ClusterSnapshot` | No                     | Yes                  | No                                        |

## Amazon DynamoDB

| **Resources**          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DynamoDB::Table` | Yes                    | Yes                  | Yes                                       |

## DynamoDB Accelerator

| **Resources**       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DAX::Cluster` | No                     | Yes                  | No                                        |

## Amazon EMR

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::EMR::Cluster`           | Yes                    | Yes                  | Yes                                       |
| `AWS::EMR::Editor`            | No                     | Yes                  | No                                        |
| `AWS::EMR::NotebookExecution` | No                     | Yes                  | No                                        |
| `AWS::EMR::Studio`            | No                     | Yes                  | No                                        |

## Amazon EMR Containers

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::EMRContainers::JobRun`                | No                     | Yes                  | No                                        |
| `AWS::EMRContainers::JobTemplate`           | No                     | Yes                  | No                                        |
| `AWS::EMRContainers::ManagedEndpoint`       | No                     | Yes                  | No                                        |
| `AWS::EMRContainers::SecurityConfiguration` | No                     | Yes                  | No                                        |
| `AWS::EMRContainers::VirtualCluster`        | Yes                    | Yes                  | Yes                                       |

## Amazon EMR Serverless

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::EMRServerless::Application` | No                     | Yes                  | Yes                                       |
| `AWS::EMRServerless::JobRun`      | No                     | Yes                  | No                                        |

## Amazon ElastiCache

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ElastiCache::CacheCluster`            | Yes                    | Yes                  | Yes                                       |
| `AWS::ElastiCache::ParameterGroup`          | No                     | Yes                  | No                                        |
| `AWS::ElastiCache::ReplicationGroup`        | No                     | Yes                  | No                                        |
| `AWS::ElastiCache::ReservedInstance`        | No                     | Yes                  | No                                        |
| `AWS::ElastiCache::SecurityGroup`           | No                     | Yes                  | No                                        |
| `AWS::ElastiCache::ServerlessCache`         | No                     | Yes                  | No                                        |
| `AWS::ElastiCache::ServerlessCacheSnapshot` | No                     | Yes                  | No                                        |
| `AWS::ElastiCache::Snapshot`                | Yes                    | Yes                  | No                                        |
| `AWS::ElastiCache::SubnetGroup`             | No                     | Yes                  | No                                        |
| `AWS::ElastiCache::User`                    | No                     | Yes                  | No                                        |
| `AWS::ElastiCache::UserGroup`               | No                     | Yes                  | No                                        |

## AWS Elastic Beanstalk

| **Resources**                                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ElasticBeanstalk::Application`           | Yes                    | Yes                  | No                                        |
| `AWS::ElasticBeanstalk::ApplicationVersion`    | No                     | Yes                  | No                                        |
| `AWS::ElasticBeanstalk::ConfigurationTemplate` | No                     | Yes                  | No                                        |
| `AWS::ElasticBeanstalk::Environment`           | No                     | Yes                  | No                                        |

## Amazon Elastic Compute Cloud (Amazon EC2)

| **Resources**                                                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::EC2::CapacityReservation`                                    | No                     | Yes                  | No                                        |
| `AWS::EC2::CapacityReservationFleet`                               | No                     | Yes                  | No                                        |
| `AWS::EC2::CarrierGateway`                                         | No                     | Yes                  | No                                        |
| `AWS::EC2::ClientVpnEndpoint`                                      | No                     | Yes                  | No                                        |
| `AWS::EC2::CoipPool`                                               | No                     | Yes                  | No                                        |
| `AWS::EC2::CustomerGateway`                                        | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::DHCPOptions`                                            | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::EC2Fleet`                                               | No                     | Yes                  | No                                        |
| `AWS::EC2::EgressOnlyInternetGateway`                              | No                     | Yes                  | No                                        |
| `AWS::EC2::EIP`                                                    | Yes                    | Yes                  | No                                        |
| `AWS::EC2::ElasticGpu`                                             | No                     | Yes                  | No                                        |
| `AWS::EC2::ExportImageTask`                                        | No                     | Yes                  | No                                        |
| `AWS::EC2::ExportInstanceTask`                                     | No                     | Yes                  | No                                        |
| `AWS::EC2::FlowLog`                                                | No                     | Yes                  | No                                        |
| `AWS::EC2::FpgaImage`                                              | No                     | Yes                  | No                                        |
| `AWS::EC2::Host`                                                   | No                     | Yes                  | No                                        |
| `AWS::EC2::HostReservation`                                        | No                     | Yes                  | No                                        |
| `AWS::EC2::Image`                                                  | Yes                    | Yes                  | No                                        |
| `AWS::EC2::ImportImageTask`                                        | No                     | Yes                  | No                                        |
| `AWS::EC2::ImportSnapshotTask`                                     | No                     | Yes                  | No                                        |
| `AWS::EC2::Instance`                                               | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::InstanceConnectEndpoint`                                | No                     | Yes                  | No                                        |
| `AWS::EC2::InstanceEventWindow`                                    | No                     | Yes                  | No                                        |
| `AWS::EC2::InternetGateway`                                        | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::IPv4Pool`                                               | No                     | Yes                  | No                                        |
| `AWS::EC2::IPv6Pool`                                               | No                     | Yes                  | No                                        |
| `AWS::EC2::KeyPair`                                                | No                     | Yes                  | No                                        |
| `AWS::EC2::LaunchTemplate`                                         | No                     | Yes                  | Yes                                       |
| `AWS::EC2::LocalGateway`                                           | No                     | Yes                  | No                                        |
| `AWS::EC2::LocalGatewayRouteTable`                                 | No                     | Yes                  | No                                        |
| `AWS::EC2::LocalGatewayRouteTableVirtualInterfaceGroupAssociation` | No                     | Yes                  | No                                        |
| `AWS::EC2::LocalGatewayRouteTableVPCAssociation`                   | No                     | Yes                  | No                                        |
| `AWS::EC2::LocalGatewayVirtualInterface`                           | No                     | Yes                  | No                                        |
| `AWS::EC2::LocalGatewayVirtualInterfaceGroup`                      | No                     | Yes                  | No                                        |
| `AWS::EC2::NatGateway`                                             | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::NetworkAcl`                                             | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::NetworkInsightsAccessScope`                             | No                     | Yes                  | No                                        |
| `AWS::EC2::NetworkInsightsAccessScopeAnalysis`                     | No                     | Yes                  | No                                        |
| `AWS::EC2::NetworkInsightsAnalysis`                                | No                     | Yes                  | No                                        |
| `AWS::EC2::NetworkInsightsPath`                                    | No                     | Yes                  | No                                        |
| `AWS::EC2::NetworkInterface`                                       | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::PlacementGroup`                                         | No                     | Yes                  | Yes                                       |
| `AWS::EC2::PrefixList`                                             | No                     | Yes                  | No                                        |
| `AWS::EC2::ReplaceRootVolumeTask`                                  | No                     | Yes                  | No                                        |
| `AWS::EC2::ReservedInstance`                                       | Yes                    | Yes                  | No                                        |
| `AWS::EC2::RouteTable`                                             | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::SecurityGroup`                                          | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::SecurityGroupRule`                                      | No                     | Yes                  | No                                        |
| `AWS::EC2::Snapshot`                                               | Yes                    | Yes                  | No                                        |
| `AWS::EC2::SpotFleet`                                              | No                     | Yes                  | No                                        |
| `AWS::EC2::SpotInstanceRequest`                                    | Yes                    | Yes                  | No                                        |
| `AWS::EC2::Subnet`                                                 | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::SubnetCidrReservation`                                  | No                     | Yes                  | No                                        |
| `AWS::EC2::TrafficMirrorFilter`                                    | No                     | Yes                  | No                                        |
| `AWS::EC2::TrafficMirrorFilterRule`                                | No                     | Yes                  | No                                        |
| `AWS::EC2::TrafficMirrorSession`                                   | No                     | Yes                  | No                                        |
| `AWS::EC2::TrafficMirrorTarget`                                    | No                     | Yes                  | No                                        |
| `AWS::EC2::TransitGateway`                                         | No                     | Yes                  | No                                        |
| `AWS::EC2::TransitGatewayAttachment`                               | No                     | Yes                  | No                                        |
| `AWS::EC2::TransitGatewayConnectPeer`                              | No                     | Yes                  | No                                        |
| `AWS::EC2::TransitGatewayMulticastDomain`                          | No                     | Yes                  | No                                        |
| `AWS::EC2::TransitGatewayPolicyTable`                              | No                     | Yes                  | No                                        |
| `AWS::EC2::TransitGatewayRouteTable`                               | No                     | Yes                  | No                                        |
| `AWS::EC2::TransitGatewayRouteTableAnnouncement`                   | No                     | Yes                  | No                                        |
| `AWS::EC2::VerifiedAccessEndpoint`                                 | No                     | Yes                  | No                                        |
| `AWS::EC2::VerifiedAccessGroup`                                    | No                     | Yes                  | No                                        |
| `AWS::EC2::VerifiedAccessInstance`                                 | No                     | Yes                  | No                                        |
| `AWS::EC2::VerifiedAccessTrustProvider`                            | No                     | Yes                  | No                                        |
| `AWS::EC2::Volume`                                                 | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::VPC`                                                    | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::VPCBlockPublicAccessExclusion`                          | No                     | Yes                  | No                                        |
| `AWS::EC2::VPCEndpoint`                                            | No                     | Yes                  | No                                        |
| `AWS::EC2::VPCEndpointConnection`                                  | No                     | Yes                  | No                                        |
| `AWS::EC2::VPCEndpointService`                                     | No                     | Yes                  | No                                        |
| `AWS::EC2::VPCEndpointServicePermissions`                          | No                     | Yes                  | No                                        |
| `AWS::EC2::VPCPeeringConnection`                                   | No                     | Yes                  | Yes                                       |
| `AWS::EC2::VPNConnection`                                          | Yes                    | Yes                  | Yes                                       |
| `AWS::EC2::VPNGateway`                                             | Yes                    | Yes                  | Yes                                       |

## Amazon Elastic Container Registry

| **Resources**          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ECR::Repository` | No                     | Yes                  | No                                        |

## Amazon Elastic Container Service

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ECS::CapacityProvider`  | No                     | Yes                  | No                                        |
| `AWS::ECS::Cluster`           | Yes                    | Yes                  | No                                        |
| `AWS::ECS::ContainerInstance` | No                     | Yes                  | No                                        |
| `AWS::ECS::Service`           | No                     | Yes                  | No                                        |
| `AWS::ECS::Task`              | No                     | Yes                  | No                                        |
| `AWS::ECS::TaskDefinition`    | Yes                    | Yes                  | No                                        |
| `AWS::ECS::TaskSet`           | No                     | Yes                  | No                                        |

## AWS Elastic Disaster Recovery

| **Resources**                                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DRS::Job`                              | No                     | Yes                  | No                                        |
| `AWS::DRS::RecoveryInstance`                 | No                     | Yes                  | No                                        |
| `AWS::DRS::ReplicationConfigurationTemplate` | No                     | Yes                  | No                                        |
| `AWS::DRS::SourceNetwork`                    | No                     | Yes                  | No                                        |
| `AWS::DRS::SourceServer`                     | No                     | Yes                  | No                                        |

## Amazon Elastic File System

| **Resources**           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::EFS::AccessPoint` | No                     | Yes                  | No                                        |
| `AWS::EFS::FileSystem`  | Yes                    | Yes                  | Yes                                       |

## Amazon Elastic Kubernetes Service (Amazon EKS)

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::EKS::Addon`                   | No                     | Yes                  | No                                        |
| `AWS::EKS::Cluster`                 | Yes                    | Yes                  | Yes                                       |
| `AWS::EKS::EKSAnywhereSubscription` | No                     | Yes                  | No                                        |
| `AWS::EKS::FargateProfile`          | No                     | Yes                  | No                                        |
| `AWS::EKS::IdentityProviderConfig`  | No                     | Yes                  | No                                        |
| `AWS::EKS::Nodegroup`               | No                     | Yes                  | No                                        |
| `AWS::EKS::PodIdentityAssociation`  | No                     | Yes                  | No                                        |

## Elastic Load Balancing

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ElasticLoadBalancing::LoadBalancer`   | Yes                    | Yes                  | Yes                                       |
| `AWS::ElasticLoadBalancingV2::Listener`     | No                     | Yes                  | Yes                                       |
| `AWS::ElasticLoadBalancingV2::ListenerRule` | No                     | Yes                  | Yes                                       |
| `AWS::ElasticLoadBalancingV2::LoadBalancer` | Yes                    | Yes                  | Yes                                       |
| `AWS::ElasticLoadBalancingV2::TargetGroup`  | Yes                    | Yes                  | Yes                                       |
| `AWS::ElasticLoadBalancingV2::TrustStore`   | No                     | Yes                  | No                                        |

## Amazon OpenSearch Service

| **Resources**                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Elasticsearch::Domain` | Yes                    | Yes                  | Yes                                       |

## AWS Elemental MediaLive

| **Resources**                                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MediaLive::Channel`                      | No                     | Yes                  | No                                        |
| `AWS::MediaLive::ChannelPlacementGroup`        | No                     | Yes                  | No                                        |
| `AWS::MediaLive::CloudWatchAlarmTemplate`      | No                     | Yes                  | No                                        |
| `AWS::MediaLive::CloudWatchAlarmTemplateGroup` | No                     | Yes                  | No                                        |
| `AWS::MediaLive::EventBridgeRuleTemplate`      | No                     | Yes                  | No                                        |
| `AWS::MediaLive::EventBridgeRuleTemplateGroup` | No                     | Yes                  | No                                        |
| `AWS::MediaLive::Input`                        | No                     | Yes                  | No                                        |
| `AWS::MediaLive::InputDevice`                  | No                     | Yes                  | No                                        |
| `AWS::MediaLive::InputSecurityGroup`           | No                     | Yes                  | No                                        |
| `AWS::MediaLive::Multiplex`                    | No                     | Yes                  | No                                        |
| `AWS::MediaLive::Network`                      | No                     | Yes                  | No                                        |
| `AWS::MediaLive::Node`                         | No                     | Yes                  | No                                        |
| `AWS::MediaLive::Reservation`                  | No                     | Yes                  | No                                        |
| `AWS::MediaLive::SignalMap`                    | No                     | Yes                  | No                                        |

## AWS Elemental MediaConvert

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MediaConvert::Job`         | No                     | Yes                  | No                                        |
| `AWS::MediaConvert::JobTemplate` | No                     | Yes                  | No                                        |
| `AWS::MediaConvert::Preset`      | No                     | Yes                  | No                                        |
| `AWS::MediaConvert::Queue`       | No                     | Yes                  | No                                        |

## AWS Elemental MediaPackage V2

| **Resources**                         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MediaPackageV2::Channel`        | No                     | Yes                  | No                                        |
| `AWS::MediaPackageV2::ChannelGroup`   | No                     | Yes                  | No                                        |
| `AWS::MediaPackageV2::OriginEndpoint` | No                     | Yes                  | No                                        |

## AWS Elemental MediaStore

| **Resources**                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MediaStore::Container` | No                     | Yes                  | No                                        |

## MediaTailor

| **Resources**                             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MediaTailor::Channel`               | No                     | Yes                  | No                                        |
| `AWS::MediaTailor::LiveSource`            | No                     | Yes                  | No                                        |
| `AWS::MediaTailor::PlaybackConfiguration` | No                     | Yes                  | No                                        |
| `AWS::MediaTailor::SourceLocation`        | No                     | Yes                  | No                                        |
| `AWS::MediaTailor::VodSource`             | No                     | Yes                  | No                                        |

## AWS Elemental Support Cases

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ElementalSupportCases::Case` | No                     | Yes                  | No                                        |

## AWS End User Messaging Social

| **Resources**                                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SocialMessaging::WhatsAppBusinessAccount` | No                     | Yes                  | No                                        |

## AWS Entity Resolution

| **Resources**                              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::EntityResolution::IdMappingWorkflow` | No                     | Yes                  | No                                        |
| `AWS::EntityResolution::IdNamespace`       | No                     | Yes                  | No                                        |
| `AWS::EntityResolution::MatchingWorkflow`  | No                     | Yes                  | No                                        |
| `AWS::EntityResolution::SchemaMapping`     | No                     | Yes                  | No                                        |

## Amazon CloudWatch Events

| **Resources**           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Events::EventBus` | No                     | Yes                  | No                                        |
| `AWS::Events::Rule`     | Yes                    | Yes                  | Yes                                       |

###### Note

Rules in custom event buses aren't supported in Tag Editor.

## Amazon EventBridge Pipes

| **Resources**      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Pipes::Pipe` | No                     | Yes                  | No                                        |

## Amazon EventBridge Scheduler

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Scheduler::ScheduleGroup` | No                     | Yes                  | No                                        |

## Amazon EventBridge Schemas

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::EventSchemas::Discoverer` | No                     | Yes                  | No                                        |
| `AWS::EventSchemas::Registry`   | No                     | Yes                  | No                                        |
| `AWS::EventSchemas::Schema`     | No                     | Yes                  | No                                        |

## Amazon FSx

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::FSx::Backup`                | No                     | Yes                  | No                                        |
| `AWS::FSx::DataRepositoryTask`    | No                     | Yes                  | No                                        |
| `AWS::FSx::FileCache`             | No                     | Yes                  | No                                        |
| `AWS::FSx::FileSystem`            | Yes                    | Yes                  | No                                        |
| `AWS::FSx::Snapshot`              | No                     | Yes                  | No                                        |
| `AWS::FSx::StorageVirtualMachine` | No                     | Yes                  | No                                        |
| `AWS::FSx::Volume`                | No                     | Yes                  | No                                        |

## AWS Fault Injection Service

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::FIS::Experiment`         | No                     | Yes                  | No                                        |
| `AWS::FIS::ExperimentTemplate` | No                     | Yes                  | No                                        |

## Amazon FinSpace schemas

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::FinSpace::Environment`    | No                     | Yes                  | No                                        |
| `AWS::FinSpace::KxCluster`      | No                     | Yes                  | No                                        |
| `AWS::FinSpace::KxDatabase`     | No                     | Yes                  | No                                        |
| `AWS::FinSpace::KxDataview`     | No                     | Yes                  | No                                        |
| `AWS::FinSpace::KxEnvironment`  | No                     | Yes                  | No                                        |
| `AWS::FinSpace::KxScalingGroup` | No                     | Yes                  | No                                        |
| `AWS::FinSpace::KxUser`         | No                     | Yes                  | No                                        |
| `AWS::FinSpace::KxVolume`       | No                     | Yes                  | No                                        |

## AWS Firewall Manager

| **Resources**                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::FMS::Applicationslist` | No                     | Yes                  | No                                        |
| `AWS::FMS::Policy`           | No                     | Yes                  | No                                        |
| `AWS::FMS::ProtocolsList`    | No                     | Yes                  | No                                        |
| `AWS::FMS::ResourceSet`      | No                     | Yes                  | No                                        |

## AWS IoT Fleet Hub

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::IoTFleetHub::Application` | No                     | Yes                  | No                                        |

## Amazon Forecast

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Forecast::Dataset`                    | Yes                    | Yes                  | No                                        |
| `AWS::Forecast::DatasetGroup`               | Yes                    | Yes                  | No                                        |
| `AWS::Forecast::DatasetImportJob`           | Yes                    | Yes                  | No                                        |
| `AWS::Forecast::Explainability`             | No                     | Yes                  | No                                        |
| `AWS::Forecast::ExplainabilityExport`       | No                     | Yes                  | No                                        |
| `AWS::Forecast::Forecast`                   | Yes                    | Yes                  | No                                        |
| `AWS::Forecast::ForecastEndpoint`           | No                     | Yes                  | No                                        |
| `AWS::Forecast::ForecastExportJob`          | Yes                    | Yes                  | No                                        |
| `AWS::Forecast::Predictor`                  | Yes                    | Yes                  | No                                        |
| `AWS::Forecast::PredictorBacktestExportJob` | Yes                    | Yes                  | No                                        |
| `AWS::Forecast::WhatIfAnalysis`             | No                     | Yes                  | No                                        |

## Amazon Fraud Detector

| **Resources**                         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::FraudDetector::BatchImport`     | No                     | Yes                  | No                                        |
| `AWS::FraudDetector::BatchPrediction` | No                     | Yes                  | No                                        |
| `AWS::FraudDetector::Detector`        | Yes                    | Yes                  | No                                        |
| `AWS::FraudDetector::DetectorVersion` | No                     | Yes                  | No                                        |
| `AWS::FraudDetector::EntityType`      | Yes                    | Yes                  | No                                        |
| `AWS::FraudDetector::EventType`       | Yes                    | Yes                  | No                                        |
| `AWS::FraudDetector::ExternalModel`   | Yes                    | Yes                  | No                                        |
| `AWS::FraudDetector::Label`           | Yes                    | Yes                  | No                                        |
| `AWS::FraudDetector::List`            | No                     | Yes                  | No                                        |
| `AWS::FraudDetector::Model`           | Yes                    | Yes                  | No                                        |
| `AWS::FraudDetector::ModelVersion`    | No                     | Yes                  | No                                        |
| `AWS::FraudDetector::Outcome`         | Yes                    | Yes                  | No                                        |
| `AWS::FraudDetector::Rule`            | No                     | Yes                  | No                                        |
| `AWS::FraudDetector::Variable`        | Yes                    | Yes                  | No                                        |

## FreeRTOS

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::FreeRTOS::Subscription` | No                     | Yes                  | No                                        |

## Amazon GameLift Servers

| **Resources**                             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::GameLift::Alias`                    | No                     | Yes                  | No                                        |
| `AWS::GameLift::ContainerFleet`           | No                     | Yes                  | No                                        |
| `AWS::GameLift::ContainerGroupDefinition` | No                     | Yes                  | No                                        |
| `AWS::GameLift::Fleet`                    | No                     | Yes                  | No                                        |
| `AWS::GameLift::GameServerGroup`          | No                     | Yes                  | No                                        |
| `AWS::GameLift::GameSessionQueue`         | No                     | Yes                  | No                                        |
| `AWS::GameLift::Location`                 | No                     | Yes                  | No                                        |
| `AWS::GameLift::MatchmakingConfiguration` | No                     | Yes                  | No                                        |
| `AWS::GameLift::MatchmakingRuleSet`       | No                     | Yes                  | No                                        |
| `AWS::GameLift::Script`                   | No                     | Yes                  | No                                        |

## AWS Global Accelerator

| **Resources**                                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::GlobalAccelerator::Accelerator`            | No                     | Yes                  | No                                        |
| `AWS::GlobalAccelerator::CrossAccountAttachment` | No                     | Yes                  | No                                        |

## AWS Glue

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Glue::Blueprint`          | No                     | Yes                  | No                                        |
| `AWS::Glue::Catalog`            | No                     | Yes                  | No                                        |
| `AWS::Glue::Completion`         | No                     | Yes                  | No                                        |
| `AWS::Glue::Connection`         | No                     | Yes                  | No                                        |
| `AWS::Glue::Crawler`            | Yes                    | Yes                  | No                                        |
| `AWS::Glue::CustomEntityType`   | No                     | Yes                  | No                                        |
| `AWS::Glue::Database`           | No                     | Yes                  | Yes                                       |
| `AWS::Glue::DataQualityRuleset` | No                     | Yes                  | No                                        |
| `AWS::Glue::DevEndpoint`        | No                     | Yes                  | No                                        |
| `AWS::Glue::Job`                | Yes                    | Yes                  | No                                        |
| `AWS::Glue::MLTransform`        | No                     | Yes                  | No                                        |
| `AWS::Glue::Registry`           | No                     | Yes                  | No                                        |
| `AWS::Glue::Schema`             | No                     | Yes                  | No                                        |
| `AWS::Glue::Session`            | No                     | Yes                  | No                                        |
| `AWS::Glue::Trigger`            | Yes                    | Yes                  | No                                        |
| `AWS::Glue::UsageProfile`       | No                     | Yes                  | No                                        |
| `AWS::Glue::Workflow`           | No                     | Yes                  | No                                        |

## AWS Glue DataBrew

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DataBrew::Dataset`  | Yes                    | Yes                  | Yes                                       |
| `AWS::DataBrew::Job`      | Yes                    | Yes                  | Yes                                       |
| `AWS::DataBrew::Project`  | Yes                    | Yes                  | Yes                                       |
| `AWS::DataBrew::Recipe`   | Yes                    | Yes                  | Yes                                       |
| `AWS::DataBrew::Ruleset`  | No                     | Yes                  | No                                        |
| `AWS::DataBrew::Schedule` | Yes                    | Yes                  | Yes                                       |

## AWS Ground Station

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::GroundStation::Config`                | No                     | Yes                  | No                                        |
| `AWS::GroundStation::Contact`               | No                     | Yes                  | No                                        |
| `AWS::GroundStation::DataflowEndpointGroup` | No                     | Yes                  | No                                        |
| `AWS::GroundStation::Ephemeris`             | No                     | Yes                  | No                                        |
| `AWS::GroundStation::MissionProfile`        | No                     | Yes                  | No                                        |
| `AWS::GroundStation::Satellite`             | No                     | Yes                  | No                                        |

## Amazon GuardDuty

| **Resources**                           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::GuardDuty::Detector`              | No                     | Yes                  | Yes                                       |
| `AWS::GuardDuty::Filter`                | No                     | Yes                  | No                                        |
| `AWS::GuardDuty::IPSet`                 | No                     | Yes                  | No                                        |
| `AWS::GuardDuty::MalwareProtectionPlan` | No                     | Yes                  | No                                        |
| `AWS::GuardDuty::ThreatIntelSet`        | No                     | Yes                  | No                                        |

## AWS HealthImaging

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::HealthImaging::Datastore` | No                     | Yes                  | No                                        |
| `AWS::HealthImaging::ImageSet`  | No                     | Yes                  | No                                        |

## AWS HealthLake

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::HealthLake::FHIRDatastore` | No                     | Yes                  | No                                        |

## AWS HealthOmics

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Omics::AnnotationStore`        | No                     | Yes                  | No                                        |
| `AWS::Omics::AnnotationStoreVersion` | No                     | Yes                  | No                                        |
| `AWS::Omics::ReadSet`                | No                     | Yes                  | No                                        |
| `AWS::Omics::Reference`              | No                     | Yes                  | No                                        |
| `AWS::Omics::ReferenceStore`         | No                     | Yes                  | No                                        |
| `AWS::Omics::Run`                    | No                     | Yes                  | No                                        |
| `AWS::Omics::RunCache`               | No                     | Yes                  | No                                        |
| `AWS::Omics::RunGroup`               | No                     | Yes                  | No                                        |
| `AWS::Omics::SequenceStore`          | No                     | Yes                  | No                                        |
| `AWS::Omics::VariantStore`           | No                     | Yes                  | No                                        |
| `AWS::Omics::Workflow`               | No                     | Yes                  | No                                        |

## Amazon Interactive Video Service

| **Resources**                         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::IVS::Channel`                   | No                     | Yes                  | No                                        |
| `AWS::IVS::Composition`               | No                     | Yes                  | No                                        |
| `AWS::IVS::EncoderConfiguration`      | No                     | Yes                  | No                                        |
| `AWS::IVS::IngestConfiguration`       | No                     | Yes                  | No                                        |
| `AWS::IVS::PlaybackKeyPair`           | No                     | Yes                  | No                                        |
| `AWS::IVS::PlaybackRestrictionPolicy` | No                     | Yes                  | No                                        |
| `AWS::IVS::PublicKey`                 | No                     | Yes                  | No                                        |
| `AWS::IVS::RecordingConfiguration`    | No                     | Yes                  | No                                        |
| `AWS::IVS::Stage`                     | No                     | Yes                  | No                                        |
| `AWS::IVS::StorageConfiguration`      | No                     | Yes                  | No                                        |
| `AWS::IVS::StreamKey`                 | No                     | Yes                  | No                                        |

## IAM

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SSO::Application`        | No                     | Yes                  | No                                        |
| `AWS::SSO::Instance`           | No                     | Yes                  | No                                        |
| `AWS::SSO::PermissionSet`      | No                     | Yes                  | No                                        |
| `AWS::SSO::TrustedTokenIssuer` | No                     | Yes                  | No                                        |

## AWS Identity and Access Management

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::IAM::InstanceProfile`       | Yes¹                   | Yes²                 | No                                        |
| `AWS::IAM::ManagedPolicy`         | Yes¹                   | Yes²                 | No                                        |
| `AWS::IAM::OpenIDConnectProvider` | Yes¹                   | Yes²                 | No                                        |
| `AWS::IAM::Role`                  | No                     | No                   | Yes²                                      |
| `AWS::IAM::SAMLProvider`          | Yes¹                   | Yes²                 | No                                        |
| `AWS::IAM::ServerCertificate`     | Yes¹                   | Yes²                 | No                                        |
| `AWS::IAM::VirtualMFADevice`      | Yes¹                   | Yes²                 | No                                        |

¹ This is a resource for a global service that is hosted in the
**US East (N. Virginia)** Region. To use Tag Editor to create or
modify tags for this resource type, you must include `us-east-1` from the
**Select regions** list under **Find resources to tag** in the
Tag Editor console.

² This is a resource for a global service that is hosted in the
**US East (N. Virginia)** Region. Because Resource Groups are
maintained separately for each region, you must switch your AWS Management Console to the AWS Region that
contains the resources you want to include in the group. To create a resource group that contains
a global resource, you must configure your AWS Management Console to **US East (N. Virginia)
us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## EC2 Image Builder

| **Resources**                                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ImageBuilder::Component`                   | No                     | Yes                  | No                                        |
| `AWS::ImageBuilder::ContainerRecipe`             | No                     | Yes                  | No                                        |
| `AWS::ImageBuilder::DistributionConfiguration`   | No                     | Yes                  | No                                        |
| `AWS::ImageBuilder::Image`                       | No                     | Yes                  | No                                        |
| `AWS::ImageBuilder::ImagePipeline`               | No                     | Yes                  | No                                        |
| `AWS::ImageBuilder::ImageRecipe`                 | No                     | Yes                  | No                                        |
| `AWS::ImageBuilder::InfrastructureConfiguration` | No                     | Yes                  | No                                        |
| `AWS::ImageBuilder::LifecyclePolicy`             | No                     | Yes                  | No                                        |
| `AWS::ImageBuilder::Workflow`                    | No                     | Yes                  | No                                        |

## Amazon Inspector

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Inspector::AssessmentTemplate`     | No                     | Yes                  | Yes                                       |
| `AWS::InspectorV2::CisScanConfiguration` | No                     | Yes                  | No                                        |
| `AWS::InspectorV2::Filter`               | No                     | Yes                  | No                                        |

## Internet Monitor

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::InternetMonitor::Monitor` | No                     | Yes                  | No                                        |

## AWS IoT

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::IoT::Authorizer`           | No                     | Yes                  | No                                        |
| `AWS::IoT::BillingGroup`         | No                     | Yes                  | No                                        |
| `AWS::IoT::CACertificate`        | No                     | Yes                  | No                                        |
| `AWS::IoT::CertificateProvider`  | No                     | Yes                  | No                                        |
| `AWS::IoT::Command`              | No                     | Yes                  | No                                        |
| `AWS::IoT::CustomMetric`         | No                     | Yes                  | No                                        |
| `AWS::IoT::Dimension`            | No                     | Yes                  | No                                        |
| `AWS::IoT::DomainConfiguration`  | No                     | Yes                  | No                                        |
| `AWS::IoT::FleetMetric`          | No                     | Yes                  | No                                        |
| `AWS::IoT::Job`                  | No                     | Yes                  | No                                        |
| `AWS::IoT::JobTemplate`          | No                     | Yes                  | No                                        |
| `AWS::IoT::MitigationAction`     | No                     | Yes                  | No                                        |
| `AWS::IoT::OTAUpdate`            | No                     | Yes                  | No                                        |
| `AWS::IoT::Policy`               | No                     | Yes                  | No                                        |
| `AWS::IoT::ProvisioningTemplate` | No                     | Yes                  | No                                        |
| `AWS::IoT::RoleAlias`            | No                     | Yes                  | No                                        |
| `AWS::IoT::ScheduledAudit`       | No                     | Yes                  | No                                        |
| `AWS::IoT::SecurityProfile`      | No                     | Yes                  | No                                        |
| `AWS::IoT::SoftwarePackage`      | No                     | Yes                  | No                                        |
| `AWS::IoT::Stream`               | No                     | Yes                  | No                                        |
| `AWS::IoT::ThingGroup`           | No                     | Yes                  | No                                        |
| `AWS::IoT::ThingType`            | No                     | Yes                  | No                                        |
| `AWS::IoT::TopicRule`            | No                     | Yes                  | Yes                                       |
| `AWS::IoT::Tunnel`               | No                     | Yes                  | No                                        |

## AWS IoT Analytics

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::IoTAnalytics::Channel`   | No                     | Yes                  | No                                        |
| `AWS::IoTAnalytics::Dataset`   | Yes                    | Yes                  | No                                        |
| `AWS::IoTAnalytics::Datastore` | No                     | Yes                  | No                                        |
| `AWS::IoTAnalytics::Pipeline`  | No                     | Yes                  | No                                        |

## AWS IoT Core Device Advisor

| **Resources**                                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::IoTCoreDeviceAdvisor::SuiteDefinition` | No                     | Yes                  | No                                        |
| `AWS::IoTCoreDeviceAdvisor::SuiteRun`        | No                     | Yes                  | No                                        |

## AWS IoT Events

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::IoTEvents::AlarmModel`    | No                     | Yes                  | No                                        |
| `AWS::IoTEvents::DetectorModel` | Yes                    | Yes                  | Yes                                       |
| `AWS::IoTEvents::Input`         | Yes                    | Yes                  | Yes                                       |

## AWS IoT FleetWise

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::IoTFleetWise::Campaign`        | No                     | Yes                  | Yes                                       |
| `AWS::IoTFleetWise::DecoderManifest` | No                     | Yes                  | Yes                                       |
| `AWS::IoTFleetWise::Fleet`           | No                     | Yes                  | Yes                                       |
| `AWS::IoTFleetWise::ModelManifest`   | No                     | Yes                  | Yes                                       |
| `AWS::IoTFleetWise::SignalCatalog`   | No                     | Yes                  | Yes                                       |
| `AWS::IoTFleetWise::StateTemplate`   | No                     | Yes                  | No                                        |
| `AWS::IoTFleetWise::Vehicle`         | No                     | Yes                  | Yes                                       |

## AWS IoT Greengrass

| **Resources**                             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Greengrass::BulkDeployment`         | No                     | Yes                  | No                                        |
| `AWS::Greengrass::ConnectorDefinition`    | Yes                    | Yes                  | No                                        |
| `AWS::Greengrass::CoreDefinition`         | Yes                    | Yes                  | No                                        |
| `AWS::Greengrass::DeviceDefinition`       | Yes                    | Yes                  | No                                        |
| `AWS::Greengrass::FunctionDefinition`     | Yes                    | Yes                  | No                                        |
| `AWS::Greengrass::Group`                  | Yes                    | Yes                  | No                                        |
| `AWS::Greengrass::LoggerDefinition`       | Yes                    | Yes                  | No                                        |
| `AWS::Greengrass::ResourceDefinition`     | Yes                    | Yes                  | No                                        |
| `AWS::Greengrass::SubscriptionDefinition` | Yes                    | Yes                  | No                                        |

## AWS IoT Greengrass Version 2

| **Resources**                         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::GreengrassV2::ComponentVersion` | No                     | Yes                  | No                                        |
| `AWS::GreengrassV2::CoreDevice`       | No                     | Yes                  | No                                        |

## AWS IoT SiteWise console

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::IoTSiteWise::AccessPolicy` | No                     | Yes                  | No                                        |
| `AWS::IoTSiteWise::Asset`        | No                     | Yes                  | No                                        |
| `AWS::IoTSiteWise::AssetModel`   | No                     | Yes                  | No                                        |
| `AWS::IoTSiteWise::Dashboard`    | No                     | Yes                  | No                                        |
| `AWS::IoTSiteWise::Dataset`      | No                     | Yes                  | No                                        |
| `AWS::IoTSiteWise::Gateway`      | No                     | Yes                  | No                                        |
| `AWS::IoTSiteWise::Portal`       | No                     | Yes                  | No                                        |
| `AWS::IoTSiteWise::Project`      | No                     | Yes                  | No                                        |
| `AWS::IoTSiteWise::TimeSeries`   | No                     | Yes                  | No                                        |

## AWS IoT Wireless

| **Resources**                                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::IoTWireless::Destination`                  | No                     | Yes                  | No                                        |
| `AWS::IoTWireless::DeviceProfile`                | No                     | Yes                  | No                                        |
| `AWS::IoTWireless::FuotaTask`                    | No                     | Yes                  | No                                        |
| `AWS::IoTWireless::ImportTask`                   | No                     | Yes                  | No                                        |
| `AWS::IoTWireless::MulticastGroup`               | No                     | Yes                  | No                                        |
| `AWS::IoTWireless::NetworkAnalyzerConfiguration` | No                     | Yes                  | No                                        |
| `AWS::IoTWireless::PartnerAccount`               | No                     | Yes                  | No                                        |
| `AWS::IoTWireless::ServiceProfile`               | No                     | Yes                  | No                                        |
| `AWS::IoTWireless::TaskDefinition`               | No                     | Yes                  | No                                        |
| `AWS::IoTWireless::WirelessDevice`               | No                     | Yes                  | No                                        |
| `AWS::IoTWireless::WirelessGateway`              | No                     | Yes                  | No                                        |

## Amazon Kendra

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Kendra::DataSource`                | No                     | Yes                  | No                                        |
| `AWS::Kendra::FeaturedResultsSet`        | No                     | Yes                  | No                                        |
| `AWS::Kendra::Index`                     | No                     | Yes                  | No                                        |
| `AWS::Kendra::QuerySuggestionsBlockList` | No                     | Yes                  | No                                        |
| `AWS::Kendra::Thesaurus`                 | No                     | Yes                  | No                                        |

## Amazon Kendra Intelligent Ranking

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::KendraRanking::ExecutionPlan` | No                     | Yes                  | No                                        |

## AWS Key Management Service

| **Resources**     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::KMS::Alias` | No                     | No                   | Yes                                       |
| `AWS::KMS::Key`   | Yes                    | Yes                  | Yes                                       |

## Amazon Keyspaces (for Apache Cassandra)

| **Resources**              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Cassandra::Keyspace` | No                     | Yes                  | Yes                                       |
| `AWS::Cassandra::Table`    | No                     | Yes                  | No                                        |

## Amazon Kinesis

| **Resources**          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Kinesis::Stream` | Yes                    | Yes                  | Yes                                       |

## Amazon Managed Service for Apache Flink

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::KinesisAnalytics::Application`   | Yes                    | Yes                  | Yes                                       |
| `AWS::KinesisAnalyticsV2::Application` | No                     | No                   | Yes                                       |

## Amazon Data Firehose

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::KinesisFirehose::DeliveryStream` | No                     | Yes                  | Yes                                       |

## Amazon Kinesis Video Streams

| **Resources**                         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::KinesisVideo::SignalingChannel` | No                     | Yes                  | No                                        |
| `AWS::KinesisVideo::Stream`           | No                     | Yes                  | No                                        |

## AWS Lambda

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Lambda::Alias`              | No                     | No                   | Yes                                       |
| `AWS::Lambda::CodeSigningConfig`  | No                     | Yes                  | No                                        |
| `AWS::Lambda::EventSourceMapping` | No                     | Yes                  | Yes                                       |
| `AWS::Lambda::Function`           | Yes                    | Yes                  | Yes                                       |
| `AWS::Lambda::LayerVersion`       | No                     | No                   | Yes                                       |
| `AWS::Lambda::Version`            | No                     | No                   | Yes                                       |

## AWS Launch Wizard

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::LaunchWizard::Deployment` | No                     | Yes                  | No                                        |

## Amazon Lex

| **Resources**         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Lex::Bot`       | No                     | Yes                  | No                                        |
| `AWS::Lex::BotAlias`  | No                     | Yes                  | No                                        |
| `AWS::LexV2::TestSet` | No                     | Yes                  | No                                        |

## AWS License Manager

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::LicenseManager::License`              | No                     | Yes                  | No                                        |
| `AWS::LicenseManager::LicenseConfiguration` | No                     | Yes                  | No                                        |
| `AWS::LicenseManager::ReportGenerator`      | No                     | Yes                  | No                                        |

## Amazon Lightsail

| **Resources**                                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Lightsail::Bucket`                     | No                     | Yes                  | No                                        |
| `AWS::Lightsail::Certificate`                | No                     | Yes                  | No                                        |
| `AWS::Lightsail::Container`                  | No                     | Yes                  | No                                        |
| `AWS::Lightsail::Database`                   | No                     | Yes                  | No                                        |
| `AWS::Lightsail::Disk`                       | No                     | Yes                  | No                                        |
| `AWS::Lightsail::DiskSnapshot`               | No                     | Yes                  | No                                        |
| `AWS::Lightsail::Distribution`               | No                     | Yes                  | No                                        |
| `AWS::Lightsail::Domain`                     | No                     | Yes                  | No                                        |
| `AWS::Lightsail::Instance`                   | No                     | Yes                  | No                                        |
| `AWS::Lightsail::InstanceSnapshot`           | No                     | Yes                  | No                                        |
| `AWS::Lightsail::KeyPair`                    | No                     | Yes                  | No                                        |
| `AWS::Lightsail::LoadBalancer`               | No                     | Yes                  | No                                        |
| `AWS::Lightsail::RelationalDatabaseSnapshot` | No                     | Yes                  | No                                        |
| `AWS::Lightsail::StaticIp`                   | No                     | Yes                  | No                                        |

## Linux subscriptions in AWS License Manager

| **Resources**                                                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::LicenseManagerLinuxSubscriptions::SubscriptionProvider` | No                     | Yes                  | No                                        |

## Amazon Location Service

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Location::GeofenceCollection` | No                     | Yes                  | No                                        |
| `AWS::Location::Map`                | No                     | Yes                  | No                                        |
| `AWS::Location::PlaceIndex`         | No                     | Yes                  | No                                        |
| `AWS::Location::RouteCalculator`    | No                     | Yes                  | No                                        |
| `AWS::Location::Tracker`            | No                     | Yes                  | No                                        |

## Lookout for Equipment

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::LookoutEquipment::Dataset`            | No                     | Yes                  | No                                        |
| `AWS::LookoutEquipment::InferenceScheduler` | No                     | Yes                  | No                                        |
| `AWS::LookoutEquipment::LabelGroup`         | No                     | Yes                  | No                                        |
| `AWS::LookoutEquipment::Model`              | No                     | Yes                  | No                                        |

## Amazon Lookout for Metrics

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::LookoutMetrics::Alert`           | No                     | Yes                  | No                                        |
| `AWS::LookoutMetrics::AnomalyDetector` | No                     | Yes                  | No                                        |
| `AWS::LookoutMetrics::MetricSet`       | No                     | Yes                  | No                                        |

## Lookout for Vision

| **Resources**               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::LookoutVision::Model` | No                     | Yes                  | No                                        |

## Amazon MQ

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AmazonMQ::Broker`        | Yes                    | Yes                  | No                                        |
| `AWS::AmazonMQ::Configuration` | Yes                    | Yes                  | No                                        |

## Amazon Machine Learning

| **Resources**                           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MachineLearning::BatchPrediction` | No                     | Yes                  | No                                        |
| `AWS::MachineLearning::DataSource`      | No                     | Yes                  | No                                        |
| `AWS::MachineLearning::Evaluation`      | No                     | Yes                  | No                                        |
| `AWS::MachineLearning::MLModel`         | No                     | Yes                  | No                                        |

## Amazon Macie

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Macie::ClassificationJob`    | Yes                    | Yes                  | No                                        |
| `AWS::Macie::CustomDataIdentifier` | Yes                    | Yes                  | Yes                                       |
| `AWS::Macie::FindingsFilter`       | Yes                    | Yes                  | Yes                                       |
| `AWS::Macie::Member`               | Yes                    | Yes                  | No                                        |

## AWS Mainframe Modernization

| **Resources**          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::M2::Application` | No                     | Yes                  | No                                        |
| `AWS::M2::Environment` | No                     | Yes                  | No                                        |

## AWS Mainframe Modernization Application Testing

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::AppTest::TestCase`          | No                     | Yes                  | No                                        |
| `AWS::AppTest::TestConfiguration` | No                     | Yes                  | No                                        |
| `AWS::AppTest::TestRun`           | No                     | Yes                  | No                                        |
| `AWS::AppTest::TestSuite`         | No                     | Yes                  | No                                        |

## Amazon Managed Blockchain

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ManagedBlockchain::Accessor`   | No                     | Yes                  | No                                        |
| `AWS::ManagedBlockchain::Invitation` | No                     | Yes                  | No                                        |
| `AWS::ManagedBlockchain::Member`     | No                     | Yes                  | No                                        |
| `AWS::ManagedBlockchain::Network`    | No                     | Yes                  | No                                        |
| `AWS::ManagedBlockchain::Node`       | No                     | Yes                  | No                                        |
| `AWS::ManagedBlockchain::Proposal`   | No                     | Yes                  | No                                        |

## Amazon Managed Grafana

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Grafana::Workspace` | No                     | Yes                  | No                                        |

## Amazon Managed Service for Prometheus

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::APS::RuleGroupsNamespace` | No                     | Yes                  | No                                        |
| `AWS::APS::Scraper`             | No                     | Yes                  | No                                        |
| `AWS::APS::Workspace`           | No                     | Yes                  | No                                        |

## Amazon Managed Streaming for Apache Kafka

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MSK::Replicator`    | No                     | Yes                  | No                                        |
| `AWS::MSK::VpcConnection` | No                     | Yes                  | No                                        |
| `AWS::Kafka::Cluster`     | Yes                    | Yes                  | No                                        |

## Amazon Managed Streaming for Apache Kafka Connect

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::KafkaConnect::Connector`           | No                     | Yes                  | No                                        |
| `AWS::KafkaConnect::CustomPlugin`        | No                     | Yes                  | No                                        |
| `AWS::KafkaConnect::WorkerConfiguration` | No                     | Yes                  | No                                        |

## Amazon Managed Workflows for Apache Airflow

| **Resources**            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MWAA::Environment` | No                     | Yes                  | No                                        |

## AWS Marketplace Catalog API

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MarketplaceCatalog::ChangeSet` | No                     | Yes                  | No                                        |
| `AWS::MarketplaceCatalog::Entity`    | No                     | Yes                  | No                                        |

## AWS Elemental MediaConnect

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MediaConnect::Flow`            | No                     | Yes                  | No                                        |
| `AWS::MediaConnect::FlowEntitlement` | No                     | Yes                  | No                                        |
| `AWS::MediaConnect::FlowOutput`      | No                     | Yes                  | No                                        |
| `AWS::MediaConnect::FlowSource`      | No                     | Yes                  | No                                        |

## AWS Elemental MediaPackage

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MediaPackage::Asset`                  | No                     | Yes                  | No                                        |
| `AWS::MediaPackage::Channel`                | No                     | Yes                  | No                                        |
| `AWS::MediaPackage::OriginEndpoint`         | No                     | Yes                  | No                                        |
| `AWS::MediaPackage::PackagingConfiguration` | No                     | Yes                  | No                                        |
| `AWS::MediaPackage::PackagingGroup`         | No                     | Yes                  | No                                        |

## Amazon MemoryDB

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MemoryDB::ACL`                | No                     | Yes                  | No                                        |
| `AWS::MemoryDB::Cluster`            | No                     | Yes                  | No                                        |
| `AWS::MemoryDB::MultiRegionCluster` | No                     | Yes                  | No                                        |
| `AWS::MemoryDB::ParameterGroup`     | No                     | Yes                  | No                                        |
| `AWS::MemoryDB::Snapshot`           | No                     | Yes                  | No                                        |
| `AWS::MemoryDB::SubnetGroup`        | No                     | Yes                  | No                                        |
| `AWS::MemoryDB::User`               | No                     | Yes                  | No                                        |

## AWS Migration Hub Orchestrator

| **Resources**                             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::MigrationHubOrchestrator::Template` | No                     | Yes                  | No                                        |
| `AWS::MigrationHubOrchestrator::Workflow` | No                     | Yes                  | No                                        |

## AWS Migration Hub Refactor Spaces

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::RefactorSpaces::Application` | No                     | Yes                  | No                                        |
| `AWS::RefactorSpaces::Environment` | No                     | Yes                  | No                                        |
| `AWS::RefactorSpaces::Route`       | No                     | Yes                  | No                                        |
| `AWS::RefactorSpaces::Service`     | No                     | Yes                  | No                                        |

## Amazon Neptune

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::NeptuneGraph::Graph`         | No                     | Yes                  | No                                        |
| `AWS::NeptuneGraph::GraphSnapshot` | No                     | Yes                  | No                                        |

## AWS Network Firewall

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::NetworkFirewall::Firewall`       | No                     | Yes                  | No                                        |
| `AWS::NetworkFirewall::FirewallPolicy` | No                     | Yes                  | No                                        |
| `AWS::NetworkFirewall::RuleGroup`      | No                     | Yes                  | No                                        |

## Network Synthetic Monitor

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::NetworkMonitor::Monitor` | No                     | Yes                  | No                                        |
| `AWS::NetworkMonitor::Probe`   | No                     | Yes                  | No                                        |

## AWS Network Manager

| **Resources**                                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::NetworkManager::Connection`            | No                     | Yes                  | No                                        |
| `AWS::NetworkManager::ConnectPeer`           | No                     | Yes                  | No                                        |
| `AWS::NetworkManager::CoreNetwork`           | No                     | Yes                  | No                                        |
| `AWS::NetworkManager::Device`                | No                     | Yes                  | No                                        |
| `AWS::NetworkManager::GlobalNetwork`         | No                     | Yes                  | No                                        |
| `AWS::NetworkManager::Link`                  | No                     | Yes                  | No                                        |
| `AWS::NetworkManager::Site`                  | No                     | Yes                  | No                                        |
| `AWS::NetworkManager::TransitGatewayPeering` | No                     | Yes                  | No                                        |
| `AWS::NetworkManager::VpcAttachment`         | No                     | Yes                  | No                                        |

## Amazon One

| **Resources**                           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::One::DeviceConfigurationTemplate` | No                     | Yes                  | No                                        |
| `AWS::One::DeviceInstance`              | No                     | Yes                  | No                                        |
| `AWS::One::Site`                        | No                     | Yes                  | No                                        |

## Amazon OpenSearch Service OpenSearch

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::OpenSearchService::Domain` | Yes                    | Yes                  | Yes                                       |

## OpenSearch Serverless

| **Resources**                           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::OpenSearchServerless::Collection` | No                     | Yes                  | No                                        |

## Amazon OpenSearch Service

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::OpenSearch::DataSource` | No                     | Yes                  | No                                        |

## Amazon OpenSearch Service Ingestion

| **Resources**         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::OSIS::Pipeline` | No                     | Yes                  | No                                        |

## AWS OpsWorks

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::OpsWorks::Instance` | No                     | Yes                  | Yes                                       |
| `AWS::OpsWorks::Layer`    | No                     | Yes                  | Yes                                       |
| `AWS::OpsWorks::Stack`    | No                     | Yes                  | Yes                                       |

## AWS Organizations

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Organizations::Account`            | Yes                    | Yes                  | No                                        |
| `AWS::Organizations::OrganizationalUnit` | No                     | Yes                  | No                                        |
| `AWS::Organizations::Policy`             | No                     | Yes                  | No                                        |
| `AWS::Organizations::ResourcePolicy`     | No                     | Yes                  | No                                        |
| `AWS::Organizations::Root`               | Yes                    | Yes                  | No                                        |

## AWS Outposts

| **Resources**            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Outposts::Outpost` | No                     | Yes                  | No                                        |
| `AWS::Outposts::Site`    | No                     | Yes                  | No                                        |

## AWS Panorama

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Panorama::ApplicationInstance` | No                     | Yes                  | No                                        |
| `AWS::Panorama::Device`              | No                     | Yes                  | No                                        |
| `AWS::Panorama::Package`             | No                     | Yes                  | No                                        |

## AWS Parallel Computing Service

| **Resources**       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::PCS::Cluster` | No                     | Yes                  | No                                        |

## AWS Payment Cryptography

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::PaymentCryptography::Key` | No                     | Yes                  | No                                        |

## Amazon Payments

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Payments::PaymentInstrument` | No                     | Yes                  | No                                        |

## Amazon Relational Database Service Performance Insights

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Pi::PerformanceAnalysisReport` | No                     | Yes                  | No                                        |

## Amazon Personalize

| **Resources**                         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Personalize::BatchInferenceJob` | No                     | Yes                  | No                                        |
| `AWS::Personalize::BatchSegmentJob`   | No                     | Yes                  | No                                        |
| `AWS::Personalize::Campaign`          | No                     | Yes                  | No                                        |
| `AWS::Personalize::Dataset`           | No                     | Yes                  | No                                        |
| `AWS::Personalize::DatasetExportJob`  | No                     | Yes                  | No                                        |
| `AWS::Personalize::DatasetGroup`      | No                     | Yes                  | No                                        |
| `AWS::Personalize::DatasetImportJob`  | No                     | Yes                  | No                                        |
| `AWS::Personalize::EventTracker`      | No                     | Yes                  | No                                        |
| `AWS::Personalize::Filter`            | No                     | Yes                  | No                                        |
| `AWS::Personalize::Recommender`       | No                     | Yes                  | No                                        |
| `AWS::Personalize::Solution`          | No                     | Yes                  | No                                        |

## Amazon Pinpoint

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Pinpoint::App`           | No                     | Yes                  | Yes                                       |
| `AWS::Pinpoint::EmailTemplate` | No                     | Yes                  | Yes                                       |
| `AWS::Pinpoint::PushTemplate`  | No                     | Yes                  | Yes                                       |
| `AWS::Pinpoint::SmsTemplate`   | No                     | Yes                  | Yes                                       |
| `AWS::Pinpoint::VoiceTemplate` | No                     | Yes                  | No                                        |

## Amazon Pinpoint SMS and Voice API

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::PinpointSMSVoiceV2::ConfigurationSet` | No                     | Yes                  | No                                        |
| `AWS::PinpointSMSVoiceV2::OptOutList`       | No                     | Yes                  | No                                        |
| `AWS::PinpointSMSVoiceV2::PhoneNumber`      | No                     | Yes                  | No                                        |
| `AWS::PinpointSMSVoiceV2::Pool`             | No                     | Yes                  | No                                        |

## AWS Pricing Calculator

| **Resources**                                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::BCMPricingCalculator::BillEstimate`     | No                     | Yes                  | No                                        |
| `AWS::BCMPricingCalculator::BillScenario`     | No                     | Yes                  | No                                        |
| `AWS::BCMPricingCalculator::WorkloadEstimate` | No                     | Yes                  | No                                        |

## AWS Private CA Connector for Active Directory

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::PCAConnectorAD::Connector` | No                     | Yes                  | No                                        |

## AWS Private CA Connector for SCEP

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::PCAConnectorScep::Connector` | No                     | Yes                  | No                                        |

## AWS Proton

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Proton::Component`                    | No                     | Yes                  | No                                        |
| `AWS::Proton::Deployment`                   | No                     | Yes                  | No                                        |
| `AWS::Proton::Environment`                  | No                     | Yes                  | No                                        |
| `AWS::Proton::EnvironmentAccountConnection` | No                     | Yes                  | No                                        |
| `AWS::Proton::EnvironmentTemplate`          | No                     | Yes                  | No                                        |
| `AWS::Proton::Repository`                   | No                     | Yes                  | No                                        |
| `AWS::Proton::Service`                      | No                     | Yes                  | No                                        |
| `AWS::Proton::ServiceInstance`              | No                     | Yes                  | No                                        |
| `AWS::Proton::ServiceTemplate`              | No                     | Yes                  | No                                        |

## Amazon Q Business Apps

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::QApps::QApp`        | No                     | Yes                  | No                                        |
| `AWS::QApps::QAppSession` | No                     | Yes                  | No                                        |

## Amazon Q Business

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::QBusiness::Application`   | No                     | Yes                  | No                                        |
| `AWS::QBusiness::DataSource`    | No                     | Yes                  | No                                        |
| `AWS::QBusiness::Index`         | No                     | Yes                  | No                                        |
| `AWS::QBusiness::Plugin`        | No                     | Yes                  | No                                        |
| `AWS::QBusiness::Retriever`     | No                     | Yes                  | No                                        |
| `AWS::QBusiness::WebExperience` | No                     | Yes                  | No                                        |

## Amazon Quantum Ledger Database (Amazon QLDB)

| **Resources**       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::QLDB::Ledger` | Yes                    | Yes                  | Yes                                       |
| `AWS::QLDB::Stream` | No                     | Yes                  | Yes                                       |
| `AWS::QLDB::Table`  | No                     | Yes                  | No                                        |

## Amazon Quick Suite

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::QuickSight::Analysis`          | No                     | Yes                  | No                                        |
| `AWS::QuickSight::Brand`             | No                     | Yes                  | No                                        |
| `AWS::QuickSight::CustomPermissions` | No                     | Yes                  | No                                        |
| `AWS::QuickSight::Dashboard`         | No                     | Yes                  | No                                        |
| `AWS::QuickSight::DataSet`           | No                     | Yes                  | No                                        |
| `AWS::QuickSight::DataSource`        | No                     | Yes                  | No                                        |
| `AWS::QuickSight::Folder`            | No                     | Yes                  | No                                        |
| `AWS::QuickSight::Namespace`         | No                     | Yes                  | No                                        |
| `AWS::QuickSight::Template`          | No                     | Yes                  | No                                        |
| `AWS::QuickSight::Theme`             | No                     | Yes                  | No                                        |
| `AWS::QuickSight::Topic`             | No                     | Yes                  | No                                        |
| `AWS::QuickSight::User`              | No                     | Yes                  | No                                        |
| `AWS::QuickSight::VPCConnection`     | No                     | Yes                  | No                                        |

## AWS DeepRacer

| **Resources**                                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::DeepRacer::Car`                        | No                     | Yes                  | No                                        |
| `AWS::DeepRacer::EvaluationJob`              | No                     | Yes                  | No                                        |
| `AWS::DeepRacer::Leaderboard`                | No                     | Yes                  | No                                        |
| `AWS::DeepRacer::LeaderboardEvaluationJob`   | No                     | Yes                  | No                                        |
| `AWS::DeepRacer::ReinforcementLearningModel` | No                     | Yes                  | No                                        |
| `AWS::DeepRacer::TrainingJob`                | No                     | Yes                  | No                                        |

## Recycle Bin

| **Resources**     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::RBin::Rule` | No                     | Yes                  | No                                        |

## Amazon Redshift

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Redshift::Cluster`               | Yes                    | Yes                  | Yes                                       |
| `AWS::Redshift::ClusterParameterGroup` | Yes                    | Yes                  | Yes                                       |
| `AWS::Redshift::ClusterSecurityGroup`  | No                     | Yes                  | Yes                                       |
| `AWS::Redshift::ClusterSubnetGroup`    | Yes                    | Yes                  | Yes                                       |
| `AWS::Redshift::EventSubscription`     | No                     | Yes                  | No                                        |
| `AWS::Redshift::HSMClientCertificate`  | Yes                    | Yes                  | No                                        |
| `AWS::Redshift::HSMConfiguration`      | No                     | Yes                  | No                                        |
| `AWS::Redshift::Integration`           | No                     | Yes                  | No                                        |
| `AWS::Redshift::Namespace`             | No                     | Yes                  | No                                        |
| `AWS::Redshift::Snapshot`              | No                     | Yes                  | No                                        |
| `AWS::Redshift::SnapshotCopyGrant`     | No                     | Yes                  | No                                        |
| `AWS::Redshift::SnapshotSchedule`      | No                     | Yes                  | No                                        |
| `AWS::Redshift::UsageLimit`            | No                     | Yes                  | No                                        |

## Amazon Redshift Serverless

| **Resources**                            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::RedshiftServerless::Namespace`     | No                     | Yes                  | No                                        |
| `AWS::RedshiftServerless::RecoveryPoint` | No                     | Yes                  | No                                        |
| `AWS::RedshiftServerless::Snapshot`      | No                     | Yes                  | No                                        |
| `AWS::RedshiftServerless::Workgroup`     | No                     | Yes                  | No                                        |

## Amazon Rekognition

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Rekognition::Collection`      | No                     | Yes                  | No                                        |
| `AWS::Rekognition::StreamProcessor` | No                     | Yes                  | No                                        |

## Amazon Relational Database Service (Amazon RDS)

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::RDS::CustomDBEngineVersion`   | No                     | Yes                  | No                                        |
| `AWS::RDS::DBCluster`               | Yes                    | Yes                  | Yes                                       |
| `AWS::RDS::DBClusterEndpoint`       | No                     | Yes                  | No                                        |
| `AWS::RDS::DBClusterParameterGroup` | Yes                    | Yes                  | Yes                                       |
| `AWS::RDS::DBClusterSnapshot`       | Yes                    | Yes                  | No                                        |
| `AWS::RDS::DBInstance`              | Yes                    | Yes                  | Yes                                       |
| `AWS::RDS::DBParameterGroup`        | Yes                    | Yes                  | Yes                                       |
| `AWS::RDS::DBProxy`                 | No                     | Yes                  | No                                        |
| `AWS::RDS::DBProxyEndpoint`         | No                     | Yes                  | No                                        |
| `AWS::RDS::DBProxyTargetGroup`      | No                     | Yes                  | No                                        |
| `AWS::RDS::DBSecurityGroup`         | Yes                    | Yes                  | Yes                                       |
| `AWS::RDS::DBSnapshot`              | Yes                    | Yes                  | No                                        |
| `AWS::RDS::DBSubnetGroup`           | Yes                    | Yes                  | Yes                                       |
| `AWS::RDS::Deployment`              | No                     | Yes                  | No                                        |
| `AWS::RDS::EventSubscription`       | Yes                    | Yes                  | No                                        |
| `AWS::RDS::GlobalCluster`           | No                     | Yes                  | No                                        |
| `AWS::RDS::Integration`             | No                     | Yes                  | No                                        |
| `AWS::RDS::OptionGroup`             | Yes                    | Yes                  | No                                        |
| `AWS::RDS::ReservedDBInstance`      | Yes                    | Yes                  | No                                        |
| `AWS::RDS::SnapshotTenantDatabase`  | No                     | Yes                  | No                                        |
| `AWS::RDS::TenantDatabase`          | No                     | Yes                  | No                                        |

## AWS Resilience Hub

| **Resources**                                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ResilienceHub::App`                    | No                     | Yes                  | No                                        |
| `AWS::ResilienceHub::AppAssessment`          | No                     | Yes                  | No                                        |
| `AWS::ResilienceHub::RecommendationTemplate` | No                     | Yes                  | No                                        |
| `AWS::ResilienceHub::ResiliencyPolicy`       | No                     | Yes                  | No                                        |

## AWS Resource Access Manager

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::RAM::ResourceShare` | Yes                    | Yes                  | No                                        |

## AWS Resource Groups

| **Resources**                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ResourceGroups::Group` | Yes                    | Yes                  | Yes                                       |

## AWS Robomaker

| **Resources**                           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::RoboMaker::DeploymentJob`         | No                     | Yes                  | No                                        |
| `AWS::RoboMaker::Fleet`                 | No                     | Yes                  | No                                        |
| `AWS::RoboMaker::Robot`                 | No                     | Yes                  | No                                        |
| `AWS::RoboMaker::RobotApplication`      | Yes                    | Yes                  | No                                        |
| `AWS::RoboMaker::SimulationApplication` | Yes                    | Yes                  | No                                        |
| `AWS::RoboMaker::SimulationJob`         | Yes                    | Yes                  | No                                        |
| `AWS::RoboMaker::SimulationJobBatch`    | No                     | Yes                  | No                                        |
| `AWS::RoboMaker::World`                 | No                     | Yes                  | No                                        |
| `AWS::RoboMaker::WorldExportJob`        | No                     | Yes                  | No                                        |
| `AWS::RoboMaker::WorldGenerationJob`    | No                     | Yes                  | No                                        |
| `AWS::RoboMaker::WorldTemplate`         | No                     | Yes                  | No                                        |

## Amazon Route 53

| **Resources**               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Route53::Domain`      | Yes¹                   | Yes²                 | No                                        |
| `AWS::Route53::HealthCheck` | Yes¹                   | Yes²                 | Yes²                                      |
| `AWS::Route53::HostedZone`  | Yes¹                   | Yes²                 | Yes²                                      |

¹ This is a resource for a global service that is hosted in the
**US East (N. Virginia)** Region. To use Tag Editor to create or
modify tags for this resource type, you must include `us-east-1` from the
**Select regions** list under **Find resources to tag** in the
Tag Editor console.

² This is a resource for a global service that is hosted in the
**US East (N. Virginia)** Region. Because Resource Groups are
maintained separately for each region, you must switch your AWS Management Console to the AWS Region that
contains the resources you want to include in the group. To create a resource group that contains
a global resource, you must configure your AWS Management Console to **US East (N. Virginia)
us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## Amazon Route 53

| **Resources**                               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Route53RecoveryControl::Cluster`      | No                     | Yes                  | No                                        |
| `AWS::Route53RecoveryControl::ControlPanel` | No                     | Yes                  | No                                        |
| `AWS::Route53RecoveryControl::SafetyRule`   | No                     | Yes                  | No                                        |

## Amazon Route 53 Profiles

| **Resources**                              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Route53Profiles::Profile`            | No                     | Yes                  | No                                        |
| `AWS::Route53Profiles::ProfileAssociation` | No                     | Yes                  | No                                        |

## Amazon Route 53 Recovery Readiness in Application Recovery Controller (ARC)

| **Resources**                                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Route53RecoveryReadiness::Cell`           | No                     | Yes                  | No                                        |
| `AWS::Route53RecoveryReadiness::ReadinessCheck` | No                     | Yes                  | No                                        |
| `AWS::Route53RecoveryReadiness::RecoveryGroup`  | No                     | Yes                  | No                                        |
| `AWS::Route53RecoveryReadiness::ResourceSet`    | No                     | Yes                  | No                                        |

## Amazon Route 53 Resolver

| **Resources**                                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Route53Resolver::FirewallDomainList`           | No                     | Yes²                 | No                                        |
| `AWS::Route53Resolver::FirewallRuleGroup`            | No                     | Yes²                 | No                                        |
| `AWS::Route53Resolver::FirewallRuleGroupAssociation` | No                     | Yes²                 | No                                        |
| `AWS::Route53Resolver::OutpostResolver`              | No                     | Yes²                 | No                                        |
| `AWS::Route53Resolver::ResolverEndpoint`             | Yes¹                   | Yes²                 | No                                        |
| `AWS::Route53Resolver::ResolverQueryLoggingConfig`   | No                     | Yes²                 | No                                        |
| `AWS::Route53Resolver::ResolverRule`                 | Yes¹                   | Yes²                 | No                                        |

¹ This is a resource for a global service that is hosted in the
**US East (N. Virginia)** Region. To use Tag Editor to create or
modify tags for this resource type, you must include `us-east-1` from the
**Select regions** list under **Find resources to tag** in the
Tag Editor console.

² This is a resource for a global service that is hosted in the
**US East (N. Virginia)** Region. Because Resource Groups are
maintained separately for each region, you must switch your AWS Management Console to the AWS Region that
contains the resources you want to include in the group. To create a resource group that contains
a global resource, you must configure your AWS Management Console to **US East (N. Virginia)
us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## Amazon Glacier

| **Resources**         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Glacier::Vault` | Yes                    | Yes                  | No                                        |

## AWS SQL Workbench

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SQLWorkbench::Chart`      | No                     | Yes                  | No                                        |
| `AWS::SQLWorkbench::Connection` | No                     | Yes                  | No                                        |
| `AWS::SQLWorkbench::Notebook`   | No                     | Yes                  | No                                        |
| `AWS::SQLWorkbench::SavedQuery` | No                     | Yes                  | No                                        |

## Amazon SageMaker AI

| **Resources**                                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SageMaker::Action`                           | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Algorithm`                        | No                     | Yes                  | No                                        |
| `AWS::SageMaker::App`                              | No                     | Yes                  | No                                        |
| `AWS::SageMaker::AppImageConfig`                   | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Artifact`                         | No                     | Yes                  | No                                        |
| `AWS::SageMaker::AutoMLJob`                        | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Cluster`                          | No                     | Yes                  | No                                        |
| `AWS::SageMaker::ClusterSchedulerConfig`           | No                     | Yes                  | No                                        |
| `AWS::SageMaker::CodeRepository`                   | No                     | Yes                  | No                                        |
| `AWS::SageMaker::CompilationJob`                   | No                     | Yes                  | No                                        |
| `AWS::SageMaker::ComputeQuota`                     | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Context`                          | No                     | Yes                  | No                                        |
| `AWS::SageMaker::DataQualityJobDefinition`         | No                     | Yes                  | No                                        |
| `AWS::SageMaker::DeviceFleet`                      | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Domain`                           | No                     | Yes                  | No                                        |
| `AWS::SageMaker::EdgeDeploymentPlan`               | No                     | Yes                  | No                                        |
| `AWS::SageMaker::EdgePackagingJob`                 | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Endpoint`                         | No                     | Yes                  | Yes                                       |
| `AWS::SageMaker::EndpointConfig`                   | No                     | Yes                  | Yes                                       |
| `AWS::SageMaker::Experiment`                       | No                     | Yes                  | No                                        |
| `AWS::SageMaker::ExperimentTrial`                  | No                     | Yes                  | No                                        |
| `AWS::SageMaker::ExperimentTrialComponent`         | No                     | Yes                  | No                                        |
| `AWS::SageMaker::FeatureGroup`                     | No                     | Yes                  | No                                        |
| `AWS::SageMaker::FlowDefinition`                   | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Hub`                              | No                     | Yes                  | No                                        |
| `AWS::SageMaker::HubContent`                       | No                     | Yes                  | No                                        |
| `AWS::SageMaker::HumanTaskUi`                      | No                     | Yes                  | No                                        |
| `AWS::SageMaker::HyperParameterTuningJob`          | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Image`                            | No                     | Yes                  | No                                        |
| `AWS::SageMaker::InferenceComponent`               | No                     | Yes                  | No                                        |
| `AWS::SageMaker::InferenceExperiment`              | No                     | Yes                  | No                                        |
| `AWS::SageMaker::InferenceRecommendationsJob`      | No                     | Yes                  | No                                        |
| `AWS::SageMaker::LabelingJob`                      | No                     | Yes                  | No                                        |
| `AWS::SageMaker::LineageGroup`                     | No                     | Yes                  | No                                        |
| `AWS::SageMaker::MlflowTrackingServer`             | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Model`                            | No                     | Yes                  | Yes                                       |
| `AWS::SageMaker::ModelBiasJobDefinition`           | No                     | Yes                  | No                                        |
| `AWS::SageMaker::ModelCard`                        | No                     | Yes                  | No                                        |
| `AWS::SageMaker::ModelExplainabilityJobDefinition` | No                     | Yes                  | No                                        |
| `AWS::SageMaker::ModelPackage`                     | No                     | Yes                  | No                                        |
| `AWS::SageMaker::ModelPackageGroup`                | No                     | Yes                  | Yes                                       |
| `AWS::SageMaker::ModelQualityJobDefinition`        | No                     | Yes                  | No                                        |
| `AWS::SageMaker::MonitoringSchedule`               | No                     | Yes                  | No                                        |
| `AWS::SageMaker::NotebookInstance`                 | Yes                    | Yes                  | Yes                                       |
| `AWS::SageMaker::OptimizationJob`                  | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Pipeline`                         | No                     | Yes                  | No                                        |
| `AWS::SageMaker::ProcessingJob`                    | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Project`                          | No                     | Yes                  | Yes                                       |
| `AWS::SageMaker::Space`                            | No                     | Yes                  | No                                        |
| `AWS::SageMaker::StudioLifecycleConfig`            | No                     | Yes                  | No                                        |
| `AWS::SageMaker::TrainingJob`                      | No                     | Yes                  | No                                        |
| `AWS::SageMaker::TransformJob`                     | No                     | Yes                  | No                                        |
| `AWS::SageMaker::UserProfile`                      | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Workforce`                        | No                     | Yes                  | No                                        |
| `AWS::SageMaker::Workteam`                         | No                     | Yes                  | No                                        |

## Amazon SageMaker AI geospatial

| **Resources**                                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SagemakerGeospatial::EarthObservationJob`  | No                     | Yes                  | No                                        |
| `AWS::SagemakerGeospatial::RasterDataCollection` | No                     | Yes                  | No                                        |
| `AWS::SagemakerGeospatial::VectorEnrichmentJob`  | No                     | Yes                  | No                                        |

## Savings Plans

| **Resources**                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SavingsPlans::SavingsPlan` | No                     | Yes                  | No                                        |

## AWS Secrets Manager

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SecretsManager::Secret` | Yes                    | Yes                  | Yes                                       |

## AWS Security Hub

| **Resources**                           | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SecurityHub::AutomationRule`      | No                     | Yes                  | No                                        |
| `AWS::SecurityHub::ConfigurationPolicy` | No                     | Yes                  | No                                        |
| `AWS::SecurityHub::Hub`                 | No                     | Yes                  | No                                        |
| `AWS::SecurityHub::ProductSubscription` | No                     | Yes                  | No                                        |

## AWS Service Catalog

| **Resources**                                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ServiceCatalog::CloudFormationProduct` | No                     | Yes                  | Yes                                       |
| `AWS::ServiceCatalog::Portfolio`             | No                     | Yes                  | Yes                                       |

## AWS Service Catalog AppRegistry

| **Resources**                                    | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ServiceCatalogAppRegistry::Application`    | No                     | Yes                  | No                                        |
| `AWS::ServiceCatalogAppRegistry::AttributeGroup` | No                     | Yes                  | No                                        |

## Service Quotas

| **Resources**               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ServiceQuotas::Quota` | No                     | Yes                  | No                                        |

## AWS Shield

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Shield::Protection`      | No                     | Yes                  | No                                        |
| `AWS::Shield::ProtectionGroup` | No                     | Yes                  | No                                        |

## AWS SimSpace Weaver

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SimSpaceWeaver::Simulation` | No                     | Yes                  | No                                        |

## Amazon Simple Email Service

| **Resources**                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SES::ConfigurationSet`         | Yes                    | Yes                  | Yes                                       |
| `AWS::SES::ContactList`              | Yes                    | Yes                  | Yes                                       |
| `AWS::SES::DedicatedIpPool`          | Yes                    | Yes                  | No                                        |
| `AWS::SES::Identity`                 | Yes                    | Yes                  | No                                        |
| `AWS::SES::MailManagerArchive`       | No                     | Yes                  | No                                        |
| `AWS::SES::MailManagerIngressPoint`  | No                     | Yes                  | No                                        |
| `AWS::SES::MailManagerRuleSet`       | No                     | Yes                  | No                                        |
| `AWS::SES::MailManagerTrafficPolicy` | No                     | Yes                  | No                                        |

## Amazon Simple Notification Service

| **Resources**     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SNS::Topic` | Yes                    | Yes                  | Yes                                       |

## Amazon Simple Queue Service

| **Resources**     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SQS::Queue` | Yes                    | Yes                  | Yes                                       |

## Amazon Simple Storage Service (Amazon S3)

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::S3::AccessGrant`          | No                     | Yes                  | No                                        |
| `AWS::S3::AccessGrantsLocation` | No                     | Yes                  | No                                        |
| `AWS::S3::Bucket`               | Yes                    | Yes                  | Yes                                       |
| `AWS::S3::Job`                  | No                     | Yes                  | No                                        |
| `AWS::S3::StorageLens`          | No                     | Yes                  | No                                        |
| `AWS::S3::StorageLensGroup`     | No                     | Yes                  | No                                        |

## Amazon Simple Workflow Service

| **Resources**      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SWF::Domain` | No                     | Yes                  | No                                        |

## AWS Snowball Edge Device Management

| **Resources**                              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SnowDeviceManagement::ManagedDevice` | No                     | Yes                  | No                                        |
| `AWS::SnowDeviceManagement::Task`          | No                     | Yes                  | No                                        |

## AWS Step Functions

| **Resources**                      | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::StepFunctions::Activity`     | Yes                    | Yes                  | Yes                                       |
| `AWS::StepFunctions::StateMachine` | Yes                    | Yes                  | Yes                                       |

## Storage Gateway

| **Resources**                                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::StorageGateway::FileShare`             | No                     | Yes                  | No                                        |
| `AWS::StorageGateway::FileSystemAssociation` | No                     | Yes                  | No                                        |
| `AWS::StorageGateway::Gateway`               | Yes                    | Yes                  | No                                        |
| `AWS::StorageGateway::Tape`                  | No                     | Yes                  | No                                        |
| `AWS::StorageGateway::TapePool`              | No                     | Yes                  | No                                        |
| `AWS::StorageGateway::Volume`                | No                     | Yes                  | No                                        |

## AWS Supply Chain

| **Resources**        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SCN::Instance` | No                     | Yes                  | No                                        |

## AWS Systems Manager

| **Resources**                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SSM::Association`         | No                     | Yes                  | No                                        |
| `AWS::SSM::AutomationExecution` | No                     | Yes                  | No                                        |
| `AWS::SSM::Document`            | No                     | Yes                  | Yes                                       |
| `AWS::SSM::MaintenanceWindow`   | No                     | Yes                  | No                                        |
| `AWS::SSM::ManagedInstance`     | No                     | Yes                  | No                                        |
| `AWS::SSM::OpsItem`             | No                     | Yes                  | No                                        |
| `AWS::SSM::OpsMetadata`         | No                     | Yes                  | No                                        |
| `AWS::SSM::Parameter`           | Yes                    | Yes                  | Yes                                       |
| `AWS::SSM::PatchBaseline`       | No                     | Yes                  | Yes                                       |
| `AWS::SSM::Session`             | No                     | Yes                  | No                                        |

## AWS Systems Manager Incident Manager

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SSMIncidents::IncidentRecord` | No                     | Yes                  | No                                        |
| `AWS::SSMIncidents::ReplicationSet` | No                     | Yes                  | No                                        |
| `AWS::SSMIncidents::ResponsePlan`   | No                     | Yes                  | No                                        |

## AWS Systems Manager Incident Manager Contacts

| **Resources**                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SSMContacts::Contact`  | No                     | Yes                  | No                                        |
| `AWS::SSMContacts::Rotation` | No                     | Yes                  | No                                        |

## AWS Systems Manager Quick Setup

| **Resources**                              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SSMQuickSetup::ConfigurationManager` | No                     | Yes                  | No                                        |

## AWS Systems Manager for SAP

| **Resources**                         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::SystemsManagerSAP::Application` | No                     | Yes                  | Yes                                       |
| `AWS::SystemsManagerSAP::Database`    | No                     | Yes                  | No                                        |

## AWS Telco Network Builder

| **Resources**               | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::TNB::FunctionPackage` | No                     | Yes                  | No                                        |
| `AWS::TNB::NetworkInstance` | No                     | Yes                  | No                                        |
| `AWS::TNB::NetworkPackage`  | No                     | Yes                  | No                                        |

## Amazon Textract

| **Resources**            | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Textract::Adapter` | No                     | Yes                  | No                                        |

## Amazon Timestream

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Timestream::Database`       | No                     | Yes                  | No                                        |
| `AWS::Timestream::ScheduledQuery` | No                     | Yes                  | Yes                                       |
| `AWS::Timestream::Table`          | No                     | Yes                  | No                                        |

## Amazon Transcribe

| **Resources**                              | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Transcribe::LanguageModel`           | No                     | Yes                  | No                                        |
| `AWS::Transcribe::MedicalScribeJob`        | No                     | Yes                  | No                                        |
| `AWS::Transcribe::MedicalTranscriptionJob` | No                     | Yes                  | No                                        |
| `AWS::Transcribe::MedicalVocabulary`       | No                     | Yes                  | No                                        |
| `AWS::Transcribe::TranscriptionJob`        | No                     | Yes                  | No                                        |
| `AWS::Transcribe::Vocabulary`              | No                     | Yes                  | No                                        |
| `AWS::Transcribe::VocabularyFilter`        | No                     | Yes                  | No                                        |

## AWS Transfer Family

| **Resources**                | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Transfer::Agreement`   | No                     | Yes                  | No                                        |
| `AWS::Transfer::Certificate` | No                     | Yes                  | No                                        |
| `AWS::Transfer::Connector`   | No                     | Yes                  | No                                        |
| `AWS::Transfer::HostKey`     | No                     | Yes                  | No                                        |
| `AWS::Transfer::Profile`     | No                     | Yes                  | No                                        |
| `AWS::Transfer::Server`      | No                     | Yes                  | No                                        |
| `AWS::Transfer::User`        | No                     | Yes                  | No                                        |
| `AWS::Transfer::WebApp`      | No                     | Yes                  | No                                        |
| `AWS::Transfer::Workflow`    | No                     | Yes                  | No                                        |

## Amazon Translate

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Translate::ParallelData` | No                     | Yes                  | No                                        |
| `AWS::Translate::Terminology`  | No                     | Yes                  | No                                        |

## AWS User Notifications

| **Resources**                                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::UserNotifications::NotificationConfiguration` | No                     | Yes                  | No                                        |

## User subscriptions in AWS License Manager

| **Resources**                                                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::LicenseManagerUserSubscriptions::AssociateUser`         | No                     | Yes                  | No                                        |
| `AWS::LicenseManagerUserSubscriptions::IdentityProvider`      | No                     | Yes                  | No                                        |
| `AWS::LicenseManagerUserSubscriptions::LicenseServerEndpoint` | No                     | Yes                  | No                                        |
| `AWS::LicenseManagerUserSubscriptions::ProductSubscription`   | No                     | Yes                  | No                                        |

## Amazon VPC Lattice

| **Resources**                                        | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ---------------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::VpcLattice::AccessLogSubscription`             | No                     | Yes                  | No                                        |
| `AWS::VpcLattice::Listener`                          | No                     | Yes                  | No                                        |
| `AWS::VpcLattice::ResourceConfiguration`             | No                     | Yes                  | No                                        |
| `AWS::VpcLattice::ResourceGateway`                   | No                     | Yes                  | No                                        |
| `AWS::VpcLattice::Rule`                              | No                     | Yes                  | No                                        |
| `AWS::VpcLattice::Service`                           | No                     | Yes                  | No                                        |
| `AWS::VpcLattice::ServiceNetwork`                    | No                     | Yes                  | No                                        |
| `AWS::VpcLattice::ServiceNetworkResourceAssociation` | No                     | Yes                  | No                                        |
| `AWS::VpcLattice::ServiceNetworkServiceAssociation`  | No                     | Yes                  | No                                        |
| `AWS::VpcLattice::ServiceNetworkVpcAssociation`      | No                     | Yes                  | No                                        |
| `AWS::VpcLattice::TargetGroup`                       | No                     | Yes                  | No                                        |

## AWS Marketplace Vendor Insights

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::VendorInsights::DataSource`      | No                     | Yes                  | No                                        |
| `AWS::VendorInsights::SecurityProfile` | No                     | Yes                  | No                                        |

## AWS WAF

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::WAF::RateBasedRule` | No                     | Yes                  | No                                        |
| `AWS::WAF::Rule`          | No                     | Yes                  | No                                        |
| `AWS::WAF::RuleGroup`     | No                     | Yes                  | No                                        |
| `AWS::WAF::WebACL`        | No                     | Yes                  | No                                        |

## AWS WAF Classic Regional

| **Resources**                     | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::WAFRegional::RateBasedRule` | No                     | Yes                  | No                                        |
| `AWS::WAFRegional::Rule`          | No                     | Yes                  | No                                        |
| `AWS::WAFRegional::RuleGroup`     | No                     | Yes                  | No                                        |
| `AWS::WAFRegional::WebACL`        | No                     | Yes                  | No                                        |

## AWS Well-Architected Tool

| **Resources**                          | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| -------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::WellArchitected::Lens`           | No                     | Yes                  | No                                        |
| `AWS::WellArchitected::Profile`        | No                     | Yes                  | No                                        |
| `AWS::WellArchitected::ReviewTemplate` | No                     | Yes                  | No                                        |
| `AWS::WellArchitected::Workload`       | No                     | Yes                  | No                                        |

## AWS Wickr

| **Resources**         | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| --------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Wickr::Network` | No                     | Yes                  | No                                        |

## Amazon WorkMail

| **Resources**                 | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::Workmail::Organization` | No                     | Yes                  | No                                        |

## Amazon WorkSpaces

| **Resources**                       | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::WorkSpaces::ConnectionAlias`  | No                     | Yes                  | No                                        |
| `AWS::WorkSpaces::Directory`        | No                     | Yes                  | No                                        |
| `AWS::WorkSpaces::Workspace`        | Yes                    | Yes                  | Yes                                       |
| `AWS::WorkSpaces::WorkspaceBundle`  | No                     | Yes                  | No                                        |
| `AWS::WorkSpaces::WorkspaceImage`   | No                     | Yes                  | No                                        |
| `AWS::WorkSpaces::WorkspaceIpGroup` | No                     | Yes                  | No                                        |
| `AWS::WorkSpaces::WorkspacesPool`   | No                     | Yes                  | No                                        |

## Amazon WorkSpaces Secure Browser

| **Resources**                                   | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ----------------------------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::WorkSpacesWeb::BrowserSettings`           | No                     | Yes                  | No                                        |
| `AWS::WorkSpacesWeb::DataProtectionSettings`    | No                     | Yes                  | No                                        |
| `AWS::WorkSpacesWeb::IdentityProvider`          | No                     | Yes                  | No                                        |
| `AWS::WorkSpacesWeb::IpAccessSettings`          | No                     | Yes                  | No                                        |
| `AWS::WorkSpacesWeb::NetworkSettings`           | No                     | Yes                  | No                                        |
| `AWS::WorkSpacesWeb::Portal`                    | No                     | Yes                  | No                                        |
| `AWS::WorkSpacesWeb::TrustStore`                | No                     | Yes                  | No                                        |
| `AWS::WorkSpacesWeb::UserAccessLoggingSettings` | No                     | Yes                  | No                                        |
| `AWS::WorkSpacesWeb::UserSettings`              | No                     | Yes                  | No                                        |

## Amazon WorkSpaces Thin Client

| **Resources**                  | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------------ | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::ThinClient::Device`      | No                     | Yes                  | No                                        |
| `AWS::ThinClient::Environment` | No                     | Yes                  | No                                        |
| `AWS::ThinClient::SoftwareSet` | No                     | Yes                  | No                                        |

## AWS X-Ray

| **Resources**             | **Tag Editor Tagging** | **Tag-based Groups** | **AWS CloudFormation Stack-based Groups** |
| ------------------------- | ---------------------- | -------------------- | ----------------------------------------- |
| `AWS::XRay::Group`        | No                     | Yes                  | No                                        |
| `AWS::XRay::SamplingRule` | No                     | Yes                  | No                                        |

## Deprecated resource types

The following resource types are no longer supported for the specified
functionality.

| **Service**   | **Resource type**                                                                                                                                                                                                  | **Support change**                 | **Date**    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- | ----------- |
| AWS RoboMaker | [`AWS::RoboMaker::Robot`](../../../robomaker/latest/dg/chapter-support-policy.md#software-support-policy-may2022 "../../../robomaker/latest/dg/chapter-support-policy.md#software-support-policy-may2022")         | No longer supported by Tag Editor. | May 2, 2022 |
| AWS RoboMaker | [`AWS::RoboMaker::Fleet`](../../../robomaker/latest/dg/chapter-support-policy.md#software-support-policy-may2022 "../../../robomaker/latest/dg/chapter-support-policy.md#software-support-policy-may2022")         | No longer supported by Tag Editor. | May 2, 2022 |
| AWS RoboMaker | [`AWS::RoboMaker::DeploymentJob`](../../../robomaker/latest/dg/chapter-support-policy.md#software-support-policy-may2022 "../../../robomaker/latest/dg/chapter-support-policy.md#software-support-policy-may2022") | No longer supported by Tag Editor. | May 2, 2022 |
