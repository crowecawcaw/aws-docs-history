

# Resource types you can use with AWS Resource Groups and Tag Editor
<a name="supported-resources"></a>

You can use the AWS Management Console or the AWS CLI to create resource groups and then interact with the member resources through those groups. You can add tags to many AWS resources and then use those tags to manage group membership. This topic describes the AWS resource types that you can include in resource groups by using AWS Resource Groups, and the resource types that you can tag by using Tag Editor.

**Important**  
A resource group based on a query for **All supported resource types** can add members automatically over time, as new resources are supported by Resource Groups. When you run automations or other bulk tasks on an existing resource group based on **All supported resource types**, be aware that the actions might run on many more resources than were in the group when you first created the group. This might also mean that automations or tasks that you created for other resources are applied to possibly unintended resources, or resources on which the tasks cannot be successfully completed. In those cases, you can add a resource type filter to specify that only resources of the specified types can be part of the group.  

![Query based on All supported resource types.](https://docs.aws.amazon.com/ARG/latest/userguide/images/rg-allsupported-resources.png)


The following tables list which resource types are supported for tagging in Tag Editor, for membership in tag query-based groups, and for membership in CloudFormation stack-based groups. 

**Column definitions**
+ **Tag Editor Tagging** – You can tag resources of this type by using the [Tag Editor console](https://console.aws.amazon.com/resource-groups/tag-editor/). Otherwise, you must use either the [AWS Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html) or the tagging services supported natively by that resource’s owning service.
+ **Tag-based Groups** – You can include resources of this type in [resource groups whose membership is determined by the tags attached to the resources](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-tag-based). The group specifies tag key names and values, and any resources with tags that match are automatically part of the group
+ **CloudFormation Stack-based Groups** – You can include resources of this type in [resource groups whose membership consists of the resources created as part of a CloudFormation stack](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-stack-based). The group specifies the stack’s ARN, and all of its resources are automatically members of the group. Adding tags to a CloudFormation stack causes an update of the stack.

For a list of resource types that are deprecated and no longer supported by Resource Groups, see the section [Deprecated resource types](#deprecated-types) at the end of this topic.

**Note**  
Resource Groups and Tag Editor support the resource types in the following table, but some resource types may not be available in your AWS Region. 

## AWS DeepComposer
<a name="services-deepcomposer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DeepComposer::Composition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepComposer::Model` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon API Gateway
<a name="services-apigateway"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ApiGateway::Account` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ApiGateway::ApiKey` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ApiGateway::ClientCertificate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ApiGateway::DomainName` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ApiGateway::RestApi` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ApiGateway::Stage` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ApiGateway::UsagePlan` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon API Gateway V2
<a name="services-apigatewayv2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ApiGatewayV2::Api` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## IAM Access Analyzer
<a name="services-accessanalyzer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AccessAnalyzer::Analyzer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Amplify
<a name="services-amplify"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Amplify::App` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS App Runner
<a name="services-apprunner"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppRunner::AutoScalingConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppRunner::Connection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppRunner::ObservabilityConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppRunner::Service` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppRunner::VpcConnector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppRunner::VpcIngressConnection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS AppConfig
<a name="services-appconfig"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppConfig::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppConfig::ConfigurationProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppConfig::Deployment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppConfig::DeploymentStrategy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppConfig::Extension` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppConfig::ExtensionAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS AppFabric
<a name="services-appfabric"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppFabric::AppAuthorization` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppFabric::AppBundle` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppFabric::Ingestion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon AppFlow
<a name="services-appflow"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppFlow::Connector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppFlow::Flow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AppIntegrations
<a name="services-appintegrations"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppIntegrations::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppIntegrations::DataIntegration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppIntegrations::EventIntegration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS App Mesh
<a name="services-appmesh"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppMesh::GatewayRoute` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::Mesh` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::Route` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::VirtualGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::VirtualNode` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::VirtualRouter` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::VirtualService` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon AppStream
<a name="services-appstream"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppStream::AppBlock` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppStream::AppBlockBuilder` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppStream::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppStream::Fleet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::AppStream::Image` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppStream::ImageBuilder` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::AppStream::Stack` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS AppSync
<a name="services-appsync"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppSync::Api` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppSync::DataSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::AppSync::DomainName` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppSync::GraphQLApi` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Application Auto Scaling
<a name="services-applicationautoscaling"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ApplicationAutoScaling::ScalableTarget` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Transform MGN
<a name="services-mgn"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MGN::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::Connector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::Job` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::LaunchConfigurationTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::ReplicationConfigurationTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::SourceServer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::VcenterClient` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::Wave` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Artificial intelligence operations (AIOps)
<a name="services-aiops"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AIOps::InvestigationGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Athena
<a name="services-athena"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Athena::CapacityReservation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Athena::DataCatalog` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Athena::WorkGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Audit Manager
<a name="services-auditmanager"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AuditManager::Assessment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AuditManager::AssessmentFramework` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AuditManager::Control` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS B2B Data Interchange
<a name="services-b2bi"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::B2BI::Capability` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::B2BI::Partnership` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::B2BI::Profile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::B2BI::Transformer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Backup
<a name="services-backup"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Backup::BackupPlan` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Backup::BackupVault` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Backup::Framework` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Backup::LegalHold` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Backup::ReportPlan` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Backup::RestoreTestingPlan` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Backup gateway
<a name="services-backupgateway"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BackupGateway::VirtualMachine` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Backup search
<a name="services-backupsearch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BackupSearch::SearchExportJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::BackupSearch::SearchJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Batch
<a name="services-batch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Batch::ComputeEnvironment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Batch::ConsumableResource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Batch::Job` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Batch::JobDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Batch::JobQueue` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Batch::SchedulingPolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Bedrock
<a name="services-bedrock"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Bedrock::Agent` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::AgentAlias` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::ApplicationInferenceProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::AsyncInvoke` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::CustomModel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::EvaluationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::Flow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::FlowAlias` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::Guardrail` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::KnowledgeBase` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::ModelCustomizationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::ModelEvaluationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::ModelImportJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::ModelInvocationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::PromptVersion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Billing Conductor
<a name="services-billingconductor"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BillingConductor::BillingGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::BillingConductor::CustomLineItem` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::BillingConductor::PricingPlan` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::BillingConductor::PricingRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Billing and Cost Management
<a name="services-billing"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Billing::BillingView` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Braket
<a name="services-braket"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Braket::Job` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Braket::QuantumTask` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Budgets
<a name="services-budgets"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Budgets::Budget` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Budgets::BudgetsAction` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS BugBust
<a name="services-bugbust"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BugBust::Event` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Certificate Manager
<a name="services-certificatemanager"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CertificateManager::Certificate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Certificate Manager Private Certificate Authority
<a name="services-acmpca"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ACMPCA::CertificateAuthority` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Q Developer in chat applications
<a name="services-chatbot"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Chatbot::ChatbotConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chatbot::CustomAction` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Chime
<a name="services-chime"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Chime::AppInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::AppInstanceBot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::AppInstanceUser` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::Channel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::MediaInsightsPipelineConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::MediaPipeline` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::MediaPipelineKinesisVideoStreamPool` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::SipMediaApplication` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::VoiceConnector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::VoiceProfileDomain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Clean Rooms
<a name="services-cleanrooms"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CleanRooms::AnalysisTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::Collaboration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::ConfiguredAudienceModelAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::ConfiguredTable` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::ConfiguredTableAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::Membership` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::PrivacyBudgetTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Clean Rooms ML
<a name="services-cleanroomsml"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CleanRoomsML::AudienceGenerationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRoomsML::AudienceModel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRoomsML::ConfiguredAudienceModel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRoomsML::ConfiguredModelAlgorithm` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRoomsML::TrainingDataset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Cloud Directory
<a name="services-clouddirectory"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudDirectory::Directory` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Cloud9
<a name="services-cloud9"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Cloud9::Environment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## CloudFormation
<a name="services-cloudformation"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudFormation::Stack` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CloudFormation::StackSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudFront
<a name="services-cloudfront"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudFront::Distribution` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² | 
| `AWS::CloudFront::StreamingDistribution` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² | 
| `AWS::CloudFront::VpcOrigin` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

¹ This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. To use Tag Editor to create or modify tags for this resource type, you must include `us-east-1` from the **Select regions** list under **Find resources to tag** in the Tag Editor console.

² This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. Because Resource Groups are maintained separately for each region, you must switch your AWS Management Console to the AWS Region that contains the resources you want to include in the group. To create a resource group that contains a global resource, you must configure your AWS Management Console to **US East (N. Virginia) us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## AWS CloudHSM
<a name="services-cloudhsm"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudHSM::Backup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudHSM::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Cloud Map
<a name="services-servicediscovery"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ServiceDiscovery::Namespace` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ServiceDiscovery::Service` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudSearch
<a name="services-cloudsearch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudSearch::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CloudTrail
<a name="services-cloudtrail"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudTrail::Channel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudTrail::Dashboard` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudTrail::EventDataStore` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudTrail::Trail` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon CloudWatch
<a name="services-cloudwatch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudWatch::Alarm` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CloudWatch::Dashboard` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CloudWatch::InsightRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudWatch::MetricStream` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudWatch::ServiceLevelObjective` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudWatch Application Insights
<a name="services-applicationinsights"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ApplicationInsights::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## CloudWatch Application Signals
<a name="services-applicationsignals"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ApplicationSignals::ServiceLevelObjective` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## CloudWatch Evidently
<a name="services-evidently"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Evidently::Feature` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Evidently::Launch` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Evidently::Project` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Evidently::Segment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudWatch Logs
<a name="services-logs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Logs::AnomalyDetector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Logs::Delivery` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Logs::DeliveryDestination` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Logs::DeliverySource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Logs::Destination` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Logs::LogGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon CloudWatch Observability Manager
<a name="services-oam"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Oam::Link` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Oam::Sink` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudWatch RUM
<a name="services-rum"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RUM::AppMonitor` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudWatch Synthetics
<a name="services-synthetics"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Synthetics::Canary` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Synthetics::Group` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodeArtifact
<a name="services-codeartifact"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeArtifact::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CodeArtifact::PackageGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeArtifact::Repository` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS CodeBuild
<a name="services-codebuild"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeBuild::Fleet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeBuild::Project` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeBuild::ReportGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CodeCatalyst
<a name="services-codecatalyst"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeCatalyst::Connection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeCatalyst::IdentityCenterApplication` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeCatalyst::Space` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodeCommit
<a name="services-codecommit"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeCommit::Repository` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodeConnections
<a name="services-codeconnections"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeConnections::Host` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeConnections::RepositoryLink` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodeDeploy
<a name="services-codedeploy"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeDeploy::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CodeDeploy::DeploymentConfig` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CodeDeploy::DeploymentGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeDeploy::Instance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CodeGuru Reviewer
<a name="services-codegurureviewer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeGuruReviewer::RepositoryAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon CodeGuru Profiler
<a name="services-codeguruprofiler"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeGuruProfiler::ProfilingGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodePipeline
<a name="services-codepipeline"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodePipeline::CustomActionType` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodePipeline::Pipeline` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CodePipeline::Webhook` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS CodeStar Notifications
<a name="services-codestarnotifications"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeStarNotifications::NotificationRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodeConnections
<a name="services-codestarconnections"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeStarConnections::Connection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeStarConnections::Host` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeStarConnections::RepositoryLink` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CodeWhisperer
<a name="services-codewhisperer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeWhisperer::Customization` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeWhisperer::Profile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Cognito
<a name="services-cognito"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Cognito::IdentityPool` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Cognito::UserPool` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Comprehend
<a name="services-comprehend"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Comprehend::DocumentClassificationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::DocumentClassifier` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::DocumentClassifierEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::DominantLanguageDetectionJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::EntitiesDetectionJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::EntityRecognizer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::EntityRecognizerEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::EventsDetectionJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::Flywheel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::KeyPhrasesDetectionJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::PIIEntitiesDetectionJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::SentimentDetectionJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::TargetedSentimentDetectionJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::TopicsDetectionJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Config
<a name="services-config"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Config::AggregationAuthorization` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::ConfigRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::ConfigurationAggregator` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::ConfigurationRecorder` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::ConformancePack` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::OrganizationConfigRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::OrganizationConformancePack` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::StoredQuery` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Connect Customer
<a name="services-connect"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Connect::AgentStatus` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Contact` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::ContactEvaluation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::ContactFlow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::ContactFlowModule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::EvaluationForm` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::HoursOfOperation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Instance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::IntegrationAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::PhoneNumber` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Prompt` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Queue` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::QuickConnect` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::RoutingProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Rule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::SecurityProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::TaskTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::TrafficDistributionGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::UseCase` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::User` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::UserHierarchyGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Vocabulary` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Connect Customer Cases
<a name="services-cases"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Cases::Case` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Cases::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Cases::RelatedItem` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Connect Customer Customer Profiles
<a name="services-customerprofiles"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CustomerProfiles::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CustomerProfiles::Integration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CustomerProfiles::ObjectType` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Connect Customer Outbound Campaigns
<a name="services-connectcampaigns"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ConnectCampaigns::Campaign` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Connect Customer Voice ID
<a name="services-voiceid"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::VoiceID::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Connect Customer Wisdom
<a name="services-wisdom"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Wisdom::AIAgent` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::AIGuardrail` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::AIPrompt` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::Assistant` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Wisdom::AssistantAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Wisdom::Content` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::ContentAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::KnowledgeBase` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Wisdom::MessageTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::QuickResponse` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::Session` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Control Tower
<a name="services-controltower"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ControlTower::EnabledBaseline` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ControlTower::EnabledControl` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ControlTower::LandingZone` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Cost Explorer
<a name="services-ce"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CE::AnomalyMonitor` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CE::AnomalySubscription` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CE::CostCategory` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Cost and Usage Report
<a name="services-cur"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CUR::ReportDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Data Exchange
<a name="services-dataexchange"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DataExchange::DataGrants` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataExchange::DataSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataExchange::Revision` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Data Exports
<a name="services-bcmdataexports"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BCMDataExports::Export` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Data Lifecycle Manager
<a name="services-dlm"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DLM::LifecyclePolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Data Pipeline
<a name="services-datapipeline"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DataPipeline::Pipeline` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS DataSync
<a name="services-datasync"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DataSync::Agent` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataSync::DiscoveryJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataSync::Location` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataSync::StorageSystem` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataSync::Task` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataSync::TaskExecution` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon DataZone
<a name="services-datazone"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DataZone::DataSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataZone::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Database Migration Service
<a name="services-dms"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DMS::Certificate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::DataMigration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::DataProvider` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::Endpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DMS::EventSubscription` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::InstanceProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::MigrationProject` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::ReplicationConfig` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::ReplicationInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DMS::ReplicationSubnetGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::ReplicationTask` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::ReplicationTaskAssessmentRun` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Deadline Cloud
<a name="services-deadline"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Deadline::Farm` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Deadline::LicenseEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Detective
<a name="services-detective"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Detective::Graph` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Device Farm
<a name="services-devicefarm"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DeviceFarm::Device` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeviceFarm::DeviceInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeviceFarm::InstanceProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeviceFarm::Project` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeviceFarm::TestGridProject` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeviceFarm::VPCEConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Diode Messaging
<a name="services-diodemessaging"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DiodeMessaging::AccountMapping` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DiodeMessaging::RequestingFlow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DiodeMessaging::RespondingFlow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Diode Object Transfer
<a name="services-diode"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Diode::AccountMapping` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Diode::Transfer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Direct Connect
<a name="services-directconnect"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DirectConnect::Connection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DirectConnect::Gateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DirectConnect::Lag` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DirectConnect::VirtualInterface` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Directory Service
<a name="services-directoryservice"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DirectoryService::Directory` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon DocumentDB Elastic Clusters
<a name="services-docdbelastic"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DocDBElastic::ClusterSnapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon DynamoDB
<a name="services-dynamodb"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DynamoDB::Table` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## DynamoDB Accelerator
<a name="services-dax"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DAX::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon EMR
<a name="services-emr"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EMR::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EMR::Editor` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMR::NotebookExecution` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMR::Studio` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon EMR Containers
<a name="services-emrcontainers"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EMRContainers::JobRun` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMRContainers::JobTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMRContainers::ManagedEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMRContainers::SecurityConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMRContainers::VirtualCluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon EMR Serverless
<a name="services-emrserverless"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EMRServerless::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EMRServerless::JobRun` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon ElastiCache
<a name="services-elasticache"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ElastiCache::CacheCluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElastiCache::ParameterGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::ReplicationGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::ReservedInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::SecurityGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::ServerlessCache` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::ServerlessCacheSnapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::Snapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::SubnetGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::User` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::UserGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elastic Beanstalk
<a name="services-elasticbeanstalk"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ElasticBeanstalk::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElasticBeanstalk::ApplicationVersion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElasticBeanstalk::ConfigurationTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElasticBeanstalk::Environment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Elastic Compute Cloud (Amazon EC2)
<a name="services-ec2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EC2::CapacityReservation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::CapacityReservationFleet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::CarrierGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ClientVpnEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::CoipPool` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::CustomerGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::DHCPOptions` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::EC2Fleet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::EgressOnlyInternetGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::EIP` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ElasticGpu` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ExportImageTask` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ExportInstanceTask` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::FlowLog` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::FpgaImage` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Host` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::HostReservation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Image` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ImportImageTask` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ImportSnapshotTask` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Instance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::InstanceConnectEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::InstanceEventWindow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::InternetGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::IPv4Pool` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::IPv6Pool` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::KeyPair` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LaunchTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::LocalGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LocalGatewayRouteTable` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LocalGatewayRouteTableVirtualInterfaceGroupAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LocalGatewayRouteTableVPCAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LocalGatewayVirtualInterface` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LocalGatewayVirtualInterfaceGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::NatGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::NetworkAcl` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::NetworkInsightsAccessScope` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::NetworkInsightsAccessScopeAnalysis` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::NetworkInsightsAnalysis` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::NetworkInsightsPath` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::NetworkInterface` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::PlacementGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::PrefixList` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ReplaceRootVolumeTask` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ReservedInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::RouteTable` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::SecurityGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::SecurityGroupRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Snapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::SpotFleet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::SpotInstanceRequest` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Subnet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::SubnetCidrReservation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TrafficMirrorFilter` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TrafficMirrorFilterRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TrafficMirrorSession` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TrafficMirrorTarget` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayAttachment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayConnectPeer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayMulticastDomain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayPolicyTable` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayRouteTable` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayRouteTableAnnouncement` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VerifiedAccessEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VerifiedAccessGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VerifiedAccessInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VerifiedAccessTrustProvider` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Volume` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::VPC` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::VPCBlockPublicAccessExclusion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VPCEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VPCEndpointConnection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VPCEndpointService` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VPCEndpointServicePermissions` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VPCPeeringConnection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::VPNConnection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::VPNGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Elastic Container Registry
<a name="services-ecr"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ECR::Repository` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Elastic Container Service
<a name="services-ecs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ECS::CapacityProvider` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::ContainerInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::Service` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::Task` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::TaskDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::TaskSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elastic Disaster Recovery
<a name="services-drs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DRS::Job` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DRS::RecoveryInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DRS::ReplicationConfigurationTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DRS::SourceNetwork` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DRS::SourceServer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Elastic File System
<a name="services-efs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EFS::AccessPoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EFS::FileSystem` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Elastic Kubernetes Service (Amazon EKS)
<a name="services-eks"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EKS::Addon` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EKS::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EKS::EKSAnywhereSubscription` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EKS::FargateProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EKS::IdentityProviderConfig` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EKS::Nodegroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EKS::PodIdentityAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Elastic Load Balancing
<a name="services-elasticloadbalancing"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ElasticLoadBalancing::LoadBalancer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElasticLoadBalancingV2::Listener` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElasticLoadBalancingV2::ListenerRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElasticLoadBalancingV2::LoadBalancer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElasticLoadBalancingV2::TargetGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElasticLoadBalancingV2::TrustStore` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon OpenSearch Service
<a name="services-elasticsearch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Elasticsearch::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Elemental MediaLive
<a name="services-medialive"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaLive::Channel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::ChannelPlacementGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::CloudWatchAlarmTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::CloudWatchAlarmTemplateGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::EventBridgeRuleTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::EventBridgeRuleTemplateGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::Input` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::InputDevice` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::InputSecurityGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::Multiplex` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::Network` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::Node` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::Reservation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::SignalMap` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental MediaConvert
<a name="services-mediaconvert"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaConvert::Job` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConvert::JobTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConvert::Preset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConvert::Queue` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental MediaPackage V2
<a name="services-mediapackagev2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaPackageV2::Channel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackageV2::ChannelGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackageV2::OriginEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental MediaStore
<a name="services-mediastore"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaStore::Container` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## MediaTailor
<a name="services-mediatailor"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaTailor::Channel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaTailor::LiveSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaTailor::PlaybackConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaTailor::SourceLocation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaTailor::VodSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental Support Cases
<a name="services-elementalsupportcases"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ElementalSupportCases::Case` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS End User Messaging Social
<a name="services-socialmessaging"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SocialMessaging::WhatsAppBusinessAccount` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Entity Resolution
<a name="services-entityresolution"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EntityResolution::IdMappingWorkflow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EntityResolution::IdNamespace` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EntityResolution::MatchingWorkflow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EntityResolution::SchemaMapping` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudWatch Events
<a name="services-events"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Events::EventBus` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Events::Rule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

**Note**  
Rules in custom event buses aren't supported in Tag Editor.

## Amazon EventBridge Pipes
<a name="services-pipes"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Pipes::Pipe` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon EventBridge Scheduler
<a name="services-scheduler"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Scheduler::ScheduleGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon EventBridge Schemas
<a name="services-eventschemas"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EventSchemas::Discoverer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EventSchemas::Registry` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EventSchemas::Schema` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon FSx
<a name="services-fsx"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FSx::Backup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::DataRepositoryTask` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::FileCache` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::FileSystem` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::Snapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::StorageVirtualMachine` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::Volume` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Fault Injection Service
<a name="services-fis"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FIS::Experiment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FIS::ExperimentTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon FinSpace schemas
<a name="services-finspace"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FinSpace::Environment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxCluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxDatabase` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxDataview` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxEnvironment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxScalingGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxUser` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxVolume` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Firewall Manager
<a name="services-fms"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FMS::Applicationslist` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FMS::Policy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FMS::ProtocolsList` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FMS::ResourceSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Fleet Hub
<a name="services-iotfleethub"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTFleetHub::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Forecast
<a name="services-forecast"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Forecast::Dataset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::DatasetGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::DatasetImportJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::Explainability` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::ExplainabilityExport` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::Forecast` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::ForecastEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::ForecastExportJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::Predictor` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::PredictorBacktestExportJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::WhatIfAnalysis` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Fraud Detector
<a name="services-frauddetector"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FraudDetector::BatchImport` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::BatchPrediction` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Detector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::DetectorVersion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::EntityType` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::EventType` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::ExternalModel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Label` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::List` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Model` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::ModelVersion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Outcome` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Rule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Variable` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## FreeRTOS
<a name="services-freertos"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FreeRTOS::Subscription` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon GameLift Servers
<a name="services-gamelift"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::GameLift::Alias` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::ContainerFleet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::ContainerGroupDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::Fleet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::GameServerGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::GameSessionQueue` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::Location` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::MatchmakingConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::MatchmakingRuleSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::Script` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Global Accelerator
<a name="services-globalaccelerator"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::GlobalAccelerator::Accelerator` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GlobalAccelerator::CrossAccountAttachment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Glue
<a name="services-glue"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Glue::Blueprint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Catalog` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Completion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Connection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Crawler` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::CustomEntityType` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Database` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Glue::DataQualityRuleset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::DevEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Job` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::MLTransform` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Registry` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Schema` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Session` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Trigger` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::UsageProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Workflow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Glue DataBrew
<a name="services-databrew"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DataBrew::Dataset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DataBrew::Job` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DataBrew::Project` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DataBrew::Recipe` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DataBrew::Ruleset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataBrew::Schedule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Ground Station
<a name="services-groundstation"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::GroundStation::Config` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GroundStation::Contact` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GroundStation::DataflowEndpointGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GroundStation::Ephemeris` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GroundStation::MissionProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GroundStation::Satellite` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon GuardDuty
<a name="services-guardduty"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::GuardDuty::Detector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::GuardDuty::Filter` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GuardDuty::IPSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GuardDuty::MalwareProtectionPlan` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GuardDuty::ThreatIntelSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS HealthImaging
<a name="services-healthimaging"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::HealthImaging::Datastore` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::HealthImaging::ImageSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS HealthLake
<a name="services-healthlake"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::HealthLake::FHIRDatastore` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS HealthOmics
<a name="services-omics"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Omics::AnnotationStore` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::AnnotationStoreVersion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::ReadSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::Reference` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::ReferenceStore` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::Run` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::RunCache` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::RunGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::SequenceStore` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::VariantStore` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::Workflow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Interactive Video Service
<a name="services-ivs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IVS::Channel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::Composition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::EncoderConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::IngestConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::PlaybackKeyPair` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::PlaybackRestrictionPolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::PublicKey` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::RecordingConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::Stage` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::StorageConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::StreamKey` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## IAM
<a name="services-sso"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SSO::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSO::Instance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSO::PermissionSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSO::TrustedTokenIssuer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Identity and Access Management
<a name="services-iam"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IAM::InstanceProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IAM::ManagedPolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IAM::OpenIDConnectProvider` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IAM::Role` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² | 
| `AWS::IAM::SAMLProvider` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IAM::ServerCertificate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IAM::VirtualMFADevice` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

¹ This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. To use Tag Editor to create or modify tags for this resource type, you must include `us-east-1` from the **Select regions** list under **Find resources to tag** in the Tag Editor console.

² This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. Because Resource Groups are maintained separately for each region, you must switch your AWS Management Console to the AWS Region that contains the resources you want to include in the group. To create a resource group that contains a global resource, you must configure your AWS Management Console to **US East (N. Virginia) us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## EC2 Image Builder
<a name="services-imagebuilder"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ImageBuilder::Component` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::ContainerRecipe` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::DistributionConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::Image` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::ImagePipeline` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::ImageRecipe` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::InfrastructureConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::LifecyclePolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::Workflow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Inspector
<a name="services-inspector"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Inspector::AssessmentTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::InspectorV2::CisScanConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::InspectorV2::Filter` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Internet Monitor
<a name="services-internetmonitor"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::InternetMonitor::Monitor` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT
<a name="services-iot"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoT::Authorizer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::BillingGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::CACertificate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::CertificateProvider` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::Command` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::CustomMetric` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::Dimension` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::DomainConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::FleetMetric` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::Job` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::JobTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::MitigationAction` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::OTAUpdate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::Policy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::ProvisioningTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::RoleAlias` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::ScheduledAudit` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::SecurityProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::SoftwarePackage` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::Stream` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::ThingGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::ThingType` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::TopicRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoT::Tunnel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Analytics
<a name="services-iotanalytics"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTAnalytics::Channel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTAnalytics::Dataset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTAnalytics::Datastore` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTAnalytics::Pipeline` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Core Device Advisor
<a name="services-iotcoredeviceadvisor"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTCoreDeviceAdvisor::SuiteDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTCoreDeviceAdvisor::SuiteRun` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Events
<a name="services-iotevents"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTEvents::AlarmModel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTEvents::DetectorModel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTEvents::Input` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS IoT FleetWise
<a name="services-iotfleetwise"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTFleetWise::Campaign` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTFleetWise::DecoderManifest` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTFleetWise::Fleet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTFleetWise::ModelManifest` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTFleetWise::SignalCatalog` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTFleetWise::StateTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTFleetWise::Vehicle` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS IoT Greengrass
<a name="services-greengrass"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Greengrass::BulkDeployment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::ConnectorDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::CoreDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::DeviceDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::FunctionDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::Group` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::LoggerDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::ResourceDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::SubscriptionDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Greengrass Version 2
<a name="services-greengrassv2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::GreengrassV2::ComponentVersion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GreengrassV2::CoreDevice` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT SiteWise console
<a name="services-iotsitewise"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTSiteWise::AccessPolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Asset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::AssetModel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Dashboard` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Dataset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Gateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Portal` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Project` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::TimeSeries` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Wireless
<a name="services-iotwireless"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTWireless::Destination` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::DeviceProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::FuotaTask` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::ImportTask` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::MulticastGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::NetworkAnalyzerConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::PartnerAccount` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::ServiceProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::TaskDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::WirelessDevice` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::WirelessGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Kendra
<a name="services-kendra"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Kendra::DataSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Kendra::FeaturedResultsSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Kendra::Index` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Kendra::QuerySuggestionsBlockList` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Kendra::Thesaurus` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Kendra Intelligent Ranking
<a name="services-kendraranking"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KendraRanking::ExecutionPlan` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Key Management Service
<a name="services-kms"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KMS::Alias` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::KMS::Key` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Keyspaces (for Apache Cassandra)
<a name="services-cassandra"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Cassandra::Keyspace` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Cassandra::Table` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Kinesis
<a name="services-kinesis"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Kinesis::Stream` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Managed Service for Apache Flink
<a name="services-kinesisanalytics"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KinesisAnalytics::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::KinesisAnalyticsV2::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Data Firehose
<a name="services-kinesisfirehose"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KinesisFirehose::DeliveryStream` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Kinesis Video Streams
<a name="services-kinesisvideo"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KinesisVideo::SignalingChannel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::KinesisVideo::Stream` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Lambda
<a name="services-lambda"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Lambda::Alias` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Lambda::CodeSigningConfig` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lambda::EventSourceMapping` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Lambda::Function` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Lambda::LayerVersion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Lambda::Version` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Launch Wizard
<a name="services-launchwizard"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LaunchWizard::Deployment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Lex
<a name="services-lex"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Lex::Bot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lex::BotAlias` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LexV2::TestSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS License Manager
<a name="services-licensemanager"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LicenseManager::License` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LicenseManager::LicenseConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LicenseManager::ReportGenerator` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Lightsail
<a name="services-lightsail"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Lightsail::Bucket` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Certificate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Container` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Database` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Disk` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::DiskSnapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Distribution` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Instance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::InstanceSnapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::KeyPair` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::LoadBalancer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::RelationalDatabaseSnapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::StaticIp` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Linux subscriptions in AWS License Manager
<a name="services-licensemanagerlinuxsubscriptions"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LicenseManagerLinuxSubscriptions::SubscriptionProvider` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Location Service
<a name="services-location"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Location::GeofenceCollection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Location::Map` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Location::PlaceIndex` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Location::RouteCalculator` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Location::Tracker` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Lookout for Equipment
<a name="services-lookoutequipment"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LookoutEquipment::Dataset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LookoutEquipment::InferenceScheduler` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LookoutEquipment::LabelGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LookoutEquipment::Model` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Lookout for Metrics
<a name="services-lookoutmetrics"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LookoutMetrics::Alert` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LookoutMetrics::AnomalyDetector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LookoutMetrics::MetricSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Lookout for Vision
<a name="services-lookoutvision"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LookoutVision::Model` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon MQ
<a name="services-amazonmq"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AmazonMQ::Broker` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AmazonMQ::Configuration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Machine Learning
<a name="services-machinelearning"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MachineLearning::BatchPrediction` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MachineLearning::DataSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MachineLearning::Evaluation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MachineLearning::MLModel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Macie
<a name="services-macie"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Macie::ClassificationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Macie::CustomDataIdentifier` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Macie::FindingsFilter` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Macie::Member` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Mainframe Modernization
<a name="services-m2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::M2::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::M2::Environment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Mainframe Modernization Application Testing
<a name="services-apptest"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppTest::TestCase` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppTest::TestConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppTest::TestRun` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppTest::TestSuite` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Blockchain
<a name="services-managedblockchain"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ManagedBlockchain::Accessor` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ManagedBlockchain::Invitation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ManagedBlockchain::Member` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ManagedBlockchain::Network` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ManagedBlockchain::Node` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ManagedBlockchain::Proposal` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Grafana
<a name="services-grafana"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Grafana::Workspace` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Service for Prometheus
<a name="services-aps"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::APS::RuleGroupsNamespace` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::APS::Scraper` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::APS::Workspace` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Streaming for Apache Kafka
<a name="services-msk"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MSK::Replicator` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MSK::VpcConnection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Kafka::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Streaming for Apache Kafka Connect
<a name="services-kafkaconnect"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KafkaConnect::Connector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::KafkaConnect::CustomPlugin` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::KafkaConnect::WorkerConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Workflows for Apache Airflow
<a name="services-mwaa"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MWAA::Environment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Marketplace Catalog API
<a name="services-marketplacecatalog"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MarketplaceCatalog::ChangeSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MarketplaceCatalog::Entity` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental MediaConnect
<a name="services-mediaconnect"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaConnect::Flow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConnect::FlowEntitlement` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConnect::FlowOutput` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConnect::FlowSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental MediaPackage
<a name="services-mediapackage"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaPackage::Asset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackage::Channel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackage::OriginEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackage::PackagingConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackage::PackagingGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon MemoryDB
<a name="services-memorydb"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MemoryDB::ACL` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::MultiRegionCluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::ParameterGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::Snapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::SubnetGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::User` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Migration Hub Orchestrator
<a name="services-migrationhuborchestrator"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MigrationHubOrchestrator::Template` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MigrationHubOrchestrator::Workflow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Migration Hub Refactor Spaces
<a name="services-refactorspaces"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RefactorSpaces::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RefactorSpaces::Environment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RefactorSpaces::Route` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RefactorSpaces::Service` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Neptune
<a name="services-neptunegraph"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::NeptuneGraph::Graph` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NeptuneGraph::GraphSnapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Network Firewall
<a name="services-networkfirewall"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::NetworkFirewall::Firewall` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkFirewall::FirewallPolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkFirewall::RuleGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Network Synthetic Monitor
<a name="services-networkmonitor"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::NetworkMonitor::Monitor` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkMonitor::Probe` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Network Manager
<a name="services-networkmanager"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::NetworkManager::Connection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::ConnectPeer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::CoreNetwork` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::Device` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::GlobalNetwork` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::Link` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::Site` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::TransitGatewayPeering` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::VpcAttachment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon One
<a name="services-one"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::One::DeviceConfigurationTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::One::DeviceInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::One::Site` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon OpenSearch Service OpenSearch
<a name="services-opensearchservice"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::OpenSearchService::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## OpenSearch Serverless
<a name="services-opensearchserverless"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::OpenSearchServerless::Collection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon OpenSearch Service
<a name="services-opensearch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::OpenSearch::DataSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon OpenSearch Service Ingestion
<a name="services-osis"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::OSIS::Pipeline` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS OpsWorks
<a name="services-opsworks"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::OpsWorks::Instance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::OpsWorks::Layer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::OpsWorks::Stack` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Organizations
<a name="services-organizations"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Organizations::Account` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Organizations::OrganizationalUnit` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Organizations::Policy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Organizations::ResourcePolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Organizations::Root` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Outposts
<a name="services-outposts"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Outposts::Outpost` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Outposts::Site` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Panorama
<a name="services-panorama"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Panorama::ApplicationInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Panorama::Device` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Panorama::Package` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Parallel Computing Service
<a name="services-pcs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::PCS::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Payment Cryptography
<a name="services-paymentcryptography"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::PaymentCryptography::Key` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Payments
<a name="services-payments"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Payments::PaymentInstrument` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Relational Database Service Performance Insights
<a name="services-pi"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Pi::PerformanceAnalysisReport` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Personalize
<a name="services-personalize"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Personalize::BatchInferenceJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::BatchSegmentJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::Campaign` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::Dataset` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::DatasetExportJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::DatasetGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::DatasetImportJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::EventTracker` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::Filter` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::Recommender` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::Solution` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Pinpoint
<a name="services-pinpoint"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Pinpoint::App` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Pinpoint::EmailTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Pinpoint::PushTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Pinpoint::SmsTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Pinpoint::VoiceTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Pinpoint SMS and Voice API
<a name="services-pinpointsmsvoicev2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::PinpointSMSVoiceV2::ConfigurationSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::PinpointSMSVoiceV2::OptOutList` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::PinpointSMSVoiceV2::PhoneNumber` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::PinpointSMSVoiceV2::Pool` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Pricing Calculator
<a name="services-bcmpricingcalculator"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BCMPricingCalculator::BillEstimate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::BCMPricingCalculator::BillScenario` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::BCMPricingCalculator::WorkloadEstimate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Private CA Connector for Active Directory
<a name="services-pcaconnectorad"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::PCAConnectorAD::Connector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Private CA Connector for SCEP
<a name="services-pcaconnectorscep"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::PCAConnectorScep::Connector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Proton
<a name="services-proton"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Proton::Component` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::Deployment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::Environment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::EnvironmentAccountConnection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::EnvironmentTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::Repository` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::Service` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::ServiceInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::ServiceTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Q Business Apps
<a name="services-qapps"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::QApps::QApp` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QApps::QAppSession` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Q Business
<a name="services-qbusiness"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::QBusiness::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QBusiness::DataSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QBusiness::Index` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QBusiness::Plugin` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QBusiness::Retriever` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QBusiness::WebExperience` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Quantum Ledger Database (Amazon QLDB)
<a name="services-qldb"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::QLDB::Ledger` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::QLDB::Stream` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::QLDB::Table` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Quick
<a name="services-quicksight"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::QuickSight::Analysis` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Brand` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::CustomPermissions` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Dashboard` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::DataSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::DataSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Folder` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Namespace` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Template` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Theme` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Topic` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::User` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::VPCConnection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS DeepRacer
<a name="services-deepracer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DeepRacer::Car` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepRacer::EvaluationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepRacer::Leaderboard` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepRacer::LeaderboardEvaluationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepRacer::ReinforcementLearningModel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepRacer::TrainingJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Recycle Bin
<a name="services-rbin"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RBin::Rule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Redshift
<a name="services-redshift"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Redshift::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Redshift::ClusterParameterGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Redshift::ClusterSecurityGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Redshift::ClusterSubnetGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Redshift::EventSubscription` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::HSMClientCertificate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::HSMConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::Integration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::Namespace` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::Snapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::SnapshotCopyGrant` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::SnapshotSchedule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::UsageLimit` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Redshift Serverless
<a name="services-redshiftserverless"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RedshiftServerless::Namespace` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RedshiftServerless::RecoveryPoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RedshiftServerless::Snapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RedshiftServerless::Workgroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Rekognition
<a name="services-rekognition"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Rekognition::Collection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Rekognition::StreamProcessor` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Relational Database Service (Amazon RDS)
<a name="services-rds"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RDS::CustomDBEngineVersion` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBCluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::DBClusterEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBClusterParameterGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::DBClusterSnapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::DBParameterGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::DBProxy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBProxyEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBProxyTargetGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBSecurityGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::DBSnapshot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBSubnetGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::Deployment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::EventSubscription` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::GlobalCluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::Integration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::OptionGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::ReservedDBInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::SnapshotTenantDatabase` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::TenantDatabase` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Resilience Hub
<a name="services-resiliencehub"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ResilienceHub::App` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ResilienceHub::AppAssessment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ResilienceHub::RecommendationTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ResilienceHub::ResiliencyPolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Resource Access Manager
<a name="services-ram"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RAM::ResourceShare` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Resource Groups
<a name="services-resourcegroups"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ResourceGroups::Group` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Robomaker
<a name="services-robomaker"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RoboMaker::DeploymentJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::Fleet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::Robot` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::RobotApplication` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::SimulationApplication` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::SimulationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::SimulationJobBatch` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::World` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::WorldExportJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::WorldGenerationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::WorldTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Route 53
<a name="services-route53"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Route53::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53::HealthCheck` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² | 
| `AWS::Route53::HostedZone` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² | 

¹ This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. To use Tag Editor to create or modify tags for this resource type, you must include `us-east-1` from the **Select regions** list under **Find resources to tag** in the Tag Editor console.

² This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. Because Resource Groups are maintained separately for each region, you must switch your AWS Management Console to the AWS Region that contains the resources you want to include in the group. To create a resource group that contains a global resource, you must configure your AWS Management Console to **US East (N. Virginia) us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## Amazon Route 53
<a name="services-route53recoverycontrol"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Route53RecoveryControl::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53RecoveryControl::ControlPanel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53RecoveryControl::SafetyRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Route 53 Profiles
<a name="services-route53profiles"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Route53Profiles::Profile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Profiles::ProfileAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Route 53 Recovery Readiness in Application Recovery Controller (ARC)
<a name="services-route53recoveryreadiness"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Route53RecoveryReadiness::Cell` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53RecoveryReadiness::ReadinessCheck` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53RecoveryReadiness::RecoveryGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53RecoveryReadiness::ResourceSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Route 53 Resolver
<a name="services-route53resolver"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Route53Resolver::FirewallDomainList` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::FirewallRuleGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::FirewallRuleGroupAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::OutpostResolver` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::ResolverEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::ResolverQueryLoggingConfig` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::ResolverRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

¹ This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. To use Tag Editor to create or modify tags for this resource type, you must include `us-east-1` from the **Select regions** list under **Find resources to tag** in the Tag Editor console.

² This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. Because Resource Groups are maintained separately for each region, you must switch your AWS Management Console to the AWS Region that contains the resources you want to include in the group. To create a resource group that contains a global resource, you must configure your AWS Management Console to **US East (N. Virginia) us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## Amazon Glacier
<a name="services-glacier"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Glacier::Vault` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS SQL Workbench
<a name="services-sqlworkbench"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SQLWorkbench::Chart` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SQLWorkbench::Connection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SQLWorkbench::Notebook` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SQLWorkbench::SavedQuery` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon SageMaker AI
<a name="services-sagemaker"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SageMaker::Action` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Algorithm` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::App` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::AppImageConfig` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Artifact` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::AutoMLJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Cluster` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ClusterSchedulerConfig` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::CodeRepository` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::CompilationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ComputeQuota` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Context` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::DataQualityJobDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::DeviceFleet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::EdgeDeploymentPlan` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::EdgePackagingJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Endpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::EndpointConfig` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::Experiment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ExperimentTrial` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ExperimentTrialComponent` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::FeatureGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::FlowDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Hub` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::HubContent` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::HumanTaskUi` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::HyperParameterTuningJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Image` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::InferenceComponent` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::InferenceExperiment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::InferenceRecommendationsJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::LabelingJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::LineageGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::MlflowTrackingServer` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Model` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::ModelBiasJobDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ModelCard` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ModelExplainabilityJobDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ModelPackage` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ModelPackageGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::ModelQualityJobDefinition` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::MonitoringSchedule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::NotebookInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::OptimizationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Pipeline` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ProcessingJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Project` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::Space` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::StudioLifecycleConfig` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::TrainingJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::TransformJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::UserProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Workforce` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Workteam` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon SageMaker AI geospatial
<a name="services-sagemakergeospatial"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SagemakerGeospatial::EarthObservationJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SagemakerGeospatial::RasterDataCollection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SagemakerGeospatial::VectorEnrichmentJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Savings Plans
<a name="services-savingsplans"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SavingsPlans::SavingsPlan` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Secrets Manager
<a name="services-secretsmanager"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SecretsManager::Secret` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Security Hub CSPM
<a name="services-securityhub"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SecurityHub::AutomationRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SecurityHub::ConfigurationPolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SecurityHub::Hub` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SecurityHub::ProductSubscription` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Service Catalog
<a name="services-servicecatalog"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ServiceCatalog::CloudFormationProduct` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ServiceCatalog::Portfolio` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Service Catalog AppRegistry
<a name="services-servicecatalogappregistry"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ServiceCatalogAppRegistry::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ServiceCatalogAppRegistry::AttributeGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Service Quotas
<a name="services-servicequotas"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ServiceQuotas::Quota` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Shield
<a name="services-shield"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Shield::Protection` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Shield::ProtectionGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS SimSpace Weaver
<a name="services-simspaceweaver"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SimSpaceWeaver::Simulation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Simple Email Service
<a name="services-ses"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SES::ConfigurationSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SES::ContactList` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SES::DedicatedIpPool` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SES::Identity` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SES::MailManagerArchive` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SES::MailManagerIngressPoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SES::MailManagerRuleSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SES::MailManagerTrafficPolicy` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Simple Notification Service
<a name="services-sns"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SNS::Topic` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Simple Queue Service
<a name="services-sqs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SQS::Queue` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Simple Storage Service (Amazon S3)
<a name="services-s3"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::S3::AccessGrant` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::S3::AccessGrantsLocation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::S3::Bucket` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::S3::Job` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::S3::StorageLens` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::S3::StorageLensGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Simple Workflow Service
<a name="services-swf"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SWF::Domain` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Snowball Edge Device Management
<a name="services-snowdevicemanagement"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SnowDeviceManagement::ManagedDevice` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SnowDeviceManagement::Task` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Step Functions
<a name="services-stepfunctions"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::StepFunctions::Activity` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::StepFunctions::StateMachine` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Storage Gateway
<a name="services-storagegateway"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::StorageGateway::FileShare` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::StorageGateway::FileSystemAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::StorageGateway::Gateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::StorageGateway::Tape` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::StorageGateway::TapePool` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::StorageGateway::Volume` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Supply Chain
<a name="services-scn"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SCN::Instance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Systems Manager
<a name="services-ssm"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SSM::Association` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::AutomationExecution` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::Document` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SSM::MaintenanceWindow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::ManagedInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::OpsItem` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::OpsMetadata` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::Parameter` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SSM::PatchBaseline` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SSM::Session` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Systems Manager Incident Manager
<a name="services-ssmincidents"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SSMIncidents::IncidentRecord` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSMIncidents::ReplicationSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSMIncidents::ResponsePlan` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Systems Manager Incident Manager Contacts
<a name="services-ssmcontacts"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SSMContacts::Contact` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSMContacts::Rotation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Systems Manager Quick Setup
<a name="services-ssmquicksetup"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SSMQuickSetup::ConfigurationManager` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Systems Manager for SAP
<a name="services-systemsmanagersap"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SystemsManagerSAP::Application` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SystemsManagerSAP::Database` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Telco Network Builder
<a name="services-tnb"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::TNB::FunctionPackage` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::TNB::NetworkInstance` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::TNB::NetworkPackage` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Textract
<a name="services-textract"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Textract::Adapter` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Timestream
<a name="services-timestream"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Timestream::Database` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Timestream::ScheduledQuery` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Timestream::Table` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Transcribe
<a name="services-transcribe"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Transcribe::LanguageModel` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::MedicalScribeJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::MedicalTranscriptionJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::MedicalVocabulary` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::TranscriptionJob` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::Vocabulary` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::VocabularyFilter` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Transfer Family
<a name="services-transfer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Transfer::Agreement` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::Certificate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::Connector` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::HostKey` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::Profile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::Server` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::User` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::WebApp` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::Workflow` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Translate
<a name="services-translate"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Translate::ParallelData` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Translate::Terminology` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS User Notifications
<a name="services-usernotifications"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::UserNotifications::NotificationConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## User subscriptions in AWS License Manager
<a name="services-licensemanagerusersubscriptions"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LicenseManagerUserSubscriptions::AssociateUser` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LicenseManagerUserSubscriptions::IdentityProvider` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LicenseManagerUserSubscriptions::LicenseServerEndpoint` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LicenseManagerUserSubscriptions::ProductSubscription` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon VPC Lattice
<a name="services-vpclattice"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::VpcLattice::AccessLogSubscription` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::Listener` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ResourceConfiguration` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ResourceGateway` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::Rule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::Service` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ServiceNetwork` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ServiceNetworkResourceAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ServiceNetworkServiceAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ServiceNetworkVpcAssociation` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::TargetGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Marketplace Vendor Insights
<a name="services-vendorinsights"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::VendorInsights::DataSource` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VendorInsights::SecurityProfile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS WAF
<a name="services-waf"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::WAF::RateBasedRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAF::Rule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAF::RuleGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAF::WebACL` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS WAF Classic Regional
<a name="services-wafregional"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::WAFRegional::RateBasedRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAFRegional::Rule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAFRegional::RuleGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAFRegional::WebACL` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Well-Architected Tool
<a name="services-wellarchitected"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::WellArchitected::Lens` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WellArchitected::Profile` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WellArchitected::ReviewTemplate` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WellArchitected::Workload` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Wickr
<a name="services-wickr"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Wickr::Network` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon WorkMail
<a name="services-workmail"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Workmail::Organization` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon WorkSpaces
<a name="services-workspaces"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::WorkSpaces::ConnectionAlias` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpaces::Directory` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpaces::Workspace` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::WorkSpaces::WorkspaceBundle` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpaces::WorkspaceImage` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpaces::WorkspaceIpGroup` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpaces::WorkspacesPool` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon WorkSpaces Secure Browser
<a name="services-workspacesweb"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::WorkSpacesWeb::BrowserSettings` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::DataProtectionSettings` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::IdentityProvider` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::IpAccessSettings` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::NetworkSettings` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::Portal` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::TrustStore` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::UserAccessLoggingSettings` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::UserSettings` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon WorkSpaces Thin Client
<a name="services-thinclient"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ThinClient::Device` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ThinClient::Environment` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ThinClient::SoftwareSet` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS X-Ray
<a name="services-xray"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::XRay::Group` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::XRay::SamplingRule` |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](https://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Deprecated resource types
<a name="deprecated-types"></a>

The following resource types are no longer supported for the specified functionality.


| **Service** | **Resource type** | **Support change** | **Date** | 
| --- | --- | --- | --- | 
| AWS RoboMaker | [`AWS::RoboMaker::Robot`](https://docs.aws.amazon.com/robomaker/latest/dg/chapter-support-policy.html#software-support-policy-may2022) | No longer supported by Tag Editor. | May 2, 2022 | 
| AWS RoboMaker | [`AWS::RoboMaker::Fleet`](https://docs.aws.amazon.com/robomaker/latest/dg/chapter-support-policy.html#software-support-policy-may2022) | No longer supported by Tag Editor. | May 2, 2022 | 
| AWS RoboMaker | [`AWS::RoboMaker::DeploymentJob`](https://docs.aws.amazon.com/robomaker/latest/dg/chapter-support-policy.html#software-support-policy-may2022) | No longer supported by Tag Editor. | May 2, 2022 | 