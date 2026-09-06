

# Resource types you can use with AWS Resource Groups and Tag Editor
<a name="supported-resources"></a>

You can use the AWS Management Console or the AWS CLI to create resource groups and then interact with the member resources through those groups. You can add tags to many AWS resources and then use those tags to manage group membership. This topic describes the AWS resource types that you can include in resource groups by using AWS Resource Groups, and the resource types that you can tag by using Tag Editor.

**Important**  
A resource group based on a query for **All supported resource types** can add members automatically over time, as new resources are supported by Resource Groups. When you run automations or other bulk tasks on an existing resource group based on **All supported resource types**, be aware that the actions might run on many more resources than were in the group when you first created the group. This might also mean that automations or tasks that you created for other resources are applied to possibly unintended resources, or resources on which the tasks cannot be successfully completed. In those cases, you can add a resource type filter to specify that only resources of the specified types can be part of the group.  

![Query based on All supported resource types.](http://docs.aws.amazon.com/ARG/latest/userguide/images/rg-allsupported-resources.png)


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
| `AWS::DeepComposer::Composition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepComposer::Model` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon API Gateway
<a name="services-apigateway"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ApiGateway::Account` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ApiGateway::ApiKey` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ApiGateway::ClientCertificate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ApiGateway::DomainName` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ApiGateway::RestApi` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ApiGateway::Stage` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ApiGateway::UsagePlan` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon API Gateway V2
<a name="services-apigatewayv2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ApiGatewayV2::Api` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## IAM Access Analyzer
<a name="services-accessanalyzer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AccessAnalyzer::Analyzer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Amplify
<a name="services-amplify"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Amplify::App` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS App Runner
<a name="services-apprunner"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppRunner::AutoScalingConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppRunner::Connection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppRunner::ObservabilityConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppRunner::Service` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppRunner::VpcConnector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppRunner::VpcIngressConnection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS AppConfig
<a name="services-appconfig"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppConfig::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppConfig::ConfigurationProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppConfig::Deployment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppConfig::DeploymentStrategy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppConfig::Extension` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppConfig::ExtensionAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS AppFabric
<a name="services-appfabric"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppFabric::AppAuthorization` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppFabric::AppBundle` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppFabric::Ingestion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon AppFlow
<a name="services-appflow"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppFlow::Connector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppFlow::Flow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AppIntegrations
<a name="services-appintegrations"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppIntegrations::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppIntegrations::DataIntegration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppIntegrations::EventIntegration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS App Mesh
<a name="services-appmesh"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppMesh::GatewayRoute` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::Mesh` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::Route` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::VirtualGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::VirtualNode` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::VirtualRouter` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppMesh::VirtualService` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon AppStream
<a name="services-appstream"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppStream::AppBlock` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppStream::AppBlockBuilder` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppStream::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppStream::Fleet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::AppStream::Image` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppStream::ImageBuilder` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::AppStream::Stack` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS AppSync
<a name="services-appsync"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppSync::Api` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppSync::DataSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::AppSync::DomainName` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppSync::GraphQLApi` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Application Auto Scaling
<a name="services-applicationautoscaling"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ApplicationAutoScaling::ScalableTarget` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Transform MGN
<a name="services-mgn"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MGN::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::Connector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::Job` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::LaunchConfigurationTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::ReplicationConfigurationTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::SourceServer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::VcenterClient` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MGN::Wave` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Artificial intelligence operations (AIOps)
<a name="services-aiops"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AIOps::InvestigationGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Athena
<a name="services-athena"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Athena::CapacityReservation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Athena::DataCatalog` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Athena::WorkGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Audit Manager
<a name="services-auditmanager"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AuditManager::Assessment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AuditManager::AssessmentFramework` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AuditManager::Control` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS B2B Data Interchange
<a name="services-b2bi"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::B2BI::Capability` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::B2BI::Partnership` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::B2BI::Profile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::B2BI::Transformer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Backup
<a name="services-backup"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Backup::BackupPlan` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Backup::BackupVault` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Backup::Framework` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Backup::LegalHold` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Backup::ReportPlan` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Backup::RestoreTestingPlan` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Backup gateway
<a name="services-backupgateway"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BackupGateway::VirtualMachine` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Backup search
<a name="services-backupsearch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BackupSearch::SearchExportJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::BackupSearch::SearchJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Batch
<a name="services-batch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Batch::ComputeEnvironment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Batch::ConsumableResource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Batch::Job` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Batch::JobDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Batch::JobQueue` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Batch::SchedulingPolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Bedrock
<a name="services-bedrock"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Bedrock::Agent` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::AgentAlias` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::ApplicationInferenceProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::AsyncInvoke` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::CustomModel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::EvaluationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::Flow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::FlowAlias` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::Guardrail` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::KnowledgeBase` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::ModelCustomizationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::ModelEvaluationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::ModelImportJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::ModelInvocationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Bedrock::PromptVersion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Billing Conductor
<a name="services-billingconductor"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BillingConductor::BillingGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::BillingConductor::CustomLineItem` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::BillingConductor::PricingPlan` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::BillingConductor::PricingRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Billing and Cost Management
<a name="services-billing"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Billing::BillingView` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Braket
<a name="services-braket"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Braket::Job` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Braket::QuantumTask` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Budgets
<a name="services-budgets"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Budgets::Budget` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Budgets::BudgetsAction` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS BugBust
<a name="services-bugbust"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BugBust::Event` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Certificate Manager
<a name="services-certificatemanager"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CertificateManager::Certificate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Certificate Manager Private Certificate Authority
<a name="services-acmpca"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ACMPCA::CertificateAuthority` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Q Developer in chat applications
<a name="services-chatbot"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Chatbot::ChatbotConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chatbot::CustomAction` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Chime
<a name="services-chime"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Chime::AppInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::AppInstanceBot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::AppInstanceUser` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::Channel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::MediaInsightsPipelineConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::MediaPipeline` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::MediaPipelineKinesisVideoStreamPool` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::SipMediaApplication` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::VoiceConnector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Chime::VoiceProfileDomain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Clean Rooms
<a name="services-cleanrooms"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CleanRooms::AnalysisTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::Collaboration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::ConfiguredAudienceModelAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::ConfiguredTable` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::ConfiguredTableAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::Membership` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRooms::PrivacyBudgetTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Clean Rooms ML
<a name="services-cleanroomsml"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CleanRoomsML::AudienceGenerationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRoomsML::AudienceModel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRoomsML::ConfiguredAudienceModel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRoomsML::ConfiguredModelAlgorithm` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CleanRoomsML::TrainingDataset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Cloud Directory
<a name="services-clouddirectory"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudDirectory::Directory` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Cloud9
<a name="services-cloud9"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Cloud9::Environment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## CloudFormation
<a name="services-cloudformation"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudFormation::Stack` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CloudFormation::StackSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudFront
<a name="services-cloudfront"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudFront::Distribution` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² | 
| `AWS::CloudFront::StreamingDistribution` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² | 
| `AWS::CloudFront::VpcOrigin` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

¹ This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. To use Tag Editor to create or modify tags for this resource type, you must include `us-east-1` from the **Select regions** list under **Find resources to tag** in the Tag Editor console.

² This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. Because Resource Groups are maintained separately for each region, you must switch your AWS Management Console to the AWS Region that contains the resources you want to include in the group. To create a resource group that contains a global resource, you must configure your AWS Management Console to **US East (N. Virginia) us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## AWS CloudHSM
<a name="services-cloudhsm"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudHSM::Backup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudHSM::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Cloud Map
<a name="services-servicediscovery"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ServiceDiscovery::Namespace` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ServiceDiscovery::Service` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudSearch
<a name="services-cloudsearch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudSearch::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CloudTrail
<a name="services-cloudtrail"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudTrail::Channel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudTrail::Dashboard` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudTrail::EventDataStore` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudTrail::Trail` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon CloudWatch
<a name="services-cloudwatch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CloudWatch::Alarm` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CloudWatch::Dashboard` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CloudWatch::InsightRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudWatch::MetricStream` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CloudWatch::ServiceLevelObjective` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudWatch Application Insights
<a name="services-applicationinsights"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ApplicationInsights::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## CloudWatch Application Signals
<a name="services-applicationsignals"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ApplicationSignals::ServiceLevelObjective` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## CloudWatch Evidently
<a name="services-evidently"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Evidently::Feature` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Evidently::Launch` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Evidently::Project` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Evidently::Segment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudWatch Logs
<a name="services-logs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Logs::AnomalyDetector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Logs::Delivery` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Logs::DeliveryDestination` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Logs::DeliverySource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Logs::Destination` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Logs::LogGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon CloudWatch Observability Manager
<a name="services-oam"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Oam::Link` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Oam::Sink` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudWatch RUM
<a name="services-rum"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RUM::AppMonitor` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudWatch Synthetics
<a name="services-synthetics"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Synthetics::Canary` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Synthetics::Group` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodeArtifact
<a name="services-codeartifact"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeArtifact::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CodeArtifact::PackageGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeArtifact::Repository` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS CodeBuild
<a name="services-codebuild"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeBuild::Fleet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeBuild::Project` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeBuild::ReportGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CodeCatalyst
<a name="services-codecatalyst"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeCatalyst::Connection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeCatalyst::IdentityCenterApplication` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeCatalyst::Space` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodeCommit
<a name="services-codecommit"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeCommit::Repository` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodeConnections
<a name="services-codeconnections"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeConnections::Host` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeConnections::RepositoryLink` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodeDeploy
<a name="services-codedeploy"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeDeploy::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CodeDeploy::DeploymentConfig` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CodeDeploy::DeploymentGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeDeploy::Instance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CodeGuru Reviewer
<a name="services-codegurureviewer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeGuruReviewer::RepositoryAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon CodeGuru Profiler
<a name="services-codeguruprofiler"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeGuruProfiler::ProfilingGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodePipeline
<a name="services-codepipeline"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodePipeline::CustomActionType` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodePipeline::Pipeline` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::CodePipeline::Webhook` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS CodeStar Notifications
<a name="services-codestarnotifications"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeStarNotifications::NotificationRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS CodeConnections
<a name="services-codestarconnections"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeStarConnections::Connection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeStarConnections::Host` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeStarConnections::RepositoryLink` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CodeWhisperer
<a name="services-codewhisperer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CodeWhisperer::Customization` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CodeWhisperer::Profile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Cognito
<a name="services-cognito"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Cognito::IdentityPool` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Cognito::UserPool` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Comprehend
<a name="services-comprehend"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Comprehend::DocumentClassificationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::DocumentClassifier` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::DocumentClassifierEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::DominantLanguageDetectionJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::EntitiesDetectionJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::EntityRecognizer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::EntityRecognizerEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::EventsDetectionJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::Flywheel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::KeyPhrasesDetectionJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::PIIEntitiesDetectionJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::SentimentDetectionJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::TargetedSentimentDetectionJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Comprehend::TopicsDetectionJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Config
<a name="services-config"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Config::AggregationAuthorization` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::ConfigRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::ConfigurationAggregator` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::ConfigurationRecorder` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::ConformancePack` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::OrganizationConfigRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::OrganizationConformancePack` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Config::StoredQuery` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Connect Customer
<a name="services-connect"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Connect::AgentStatus` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Contact` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::ContactEvaluation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::ContactFlow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::ContactFlowModule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::EvaluationForm` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::HoursOfOperation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Instance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::IntegrationAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::PhoneNumber` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Prompt` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Queue` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::QuickConnect` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::RoutingProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Rule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::SecurityProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::TaskTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::TrafficDistributionGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::UseCase` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::User` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::UserHierarchyGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Connect::Vocabulary` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Connect Customer Cases
<a name="services-cases"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Cases::Case` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Cases::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Cases::RelatedItem` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Connect Customer Customer Profiles
<a name="services-customerprofiles"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CustomerProfiles::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CustomerProfiles::Integration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CustomerProfiles::ObjectType` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Connect Customer Outbound Campaigns
<a name="services-connectcampaigns"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ConnectCampaigns::Campaign` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Connect Customer Voice ID
<a name="services-voiceid"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::VoiceID::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Connect Customer Wisdom
<a name="services-wisdom"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Wisdom::AIAgent` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::AIGuardrail` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::AIPrompt` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::Assistant` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Wisdom::AssistantAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Wisdom::Content` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::ContentAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::KnowledgeBase` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Wisdom::MessageTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::QuickResponse` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Wisdom::Session` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Control Tower
<a name="services-controltower"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ControlTower::EnabledBaseline` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ControlTower::EnabledControl` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ControlTower::LandingZone` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Cost Explorer
<a name="services-ce"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CE::AnomalyMonitor` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CE::AnomalySubscription` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::CE::CostCategory` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Cost and Usage Report
<a name="services-cur"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::CUR::ReportDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Data Exchange
<a name="services-dataexchange"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DataExchange::DataGrants` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataExchange::DataSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataExchange::Revision` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Data Exports
<a name="services-bcmdataexports"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BCMDataExports::Export` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Data Lifecycle Manager
<a name="services-dlm"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DLM::LifecyclePolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Data Pipeline
<a name="services-datapipeline"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DataPipeline::Pipeline` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS DataSync
<a name="services-datasync"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DataSync::Agent` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataSync::DiscoveryJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataSync::Location` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataSync::StorageSystem` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataSync::Task` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataSync::TaskExecution` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon DataZone
<a name="services-datazone"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DataZone::DataSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataZone::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Database Migration Service
<a name="services-dms"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DMS::Certificate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::DataMigration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::DataProvider` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::Endpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DMS::EventSubscription` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::InstanceProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::MigrationProject` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::ReplicationConfig` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::ReplicationInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DMS::ReplicationSubnetGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::ReplicationTask` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DMS::ReplicationTaskAssessmentRun` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Deadline Cloud
<a name="services-deadline"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Deadline::Farm` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Deadline::LicenseEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Detective
<a name="services-detective"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Detective::Graph` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Device Farm
<a name="services-devicefarm"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DeviceFarm::Device` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeviceFarm::DeviceInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeviceFarm::InstanceProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeviceFarm::Project` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeviceFarm::TestGridProject` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeviceFarm::VPCEConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Diode Messaging
<a name="services-diodemessaging"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DiodeMessaging::AccountMapping` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DiodeMessaging::RequestingFlow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DiodeMessaging::RespondingFlow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Diode Object Transfer
<a name="services-diode"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Diode::AccountMapping` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Diode::Transfer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Direct Connect
<a name="services-directconnect"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DirectConnect::Connection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DirectConnect::Gateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DirectConnect::Lag` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DirectConnect::VirtualInterface` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Directory Service
<a name="services-directoryservice"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DirectoryService::Directory` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon DocumentDB Elastic Clusters
<a name="services-docdbelastic"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DocDBElastic::ClusterSnapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon DynamoDB
<a name="services-dynamodb"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DynamoDB::Table` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## DynamoDB Accelerator
<a name="services-dax"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DAX::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon EMR
<a name="services-emr"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EMR::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EMR::Editor` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMR::NotebookExecution` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMR::Studio` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon EMR Containers
<a name="services-emrcontainers"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EMRContainers::JobRun` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMRContainers::JobTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMRContainers::ManagedEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMRContainers::SecurityConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EMRContainers::VirtualCluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon EMR Serverless
<a name="services-emrserverless"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EMRServerless::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EMRServerless::JobRun` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon ElastiCache
<a name="services-elasticache"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ElastiCache::CacheCluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElastiCache::ParameterGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::ReplicationGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::ReservedInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::SecurityGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::ServerlessCache` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::ServerlessCacheSnapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::Snapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::SubnetGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::User` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElastiCache::UserGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elastic Beanstalk
<a name="services-elasticbeanstalk"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ElasticBeanstalk::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElasticBeanstalk::ApplicationVersion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElasticBeanstalk::ConfigurationTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ElasticBeanstalk::Environment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Elastic Compute Cloud (Amazon EC2)
<a name="services-ec2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EC2::CapacityReservation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::CapacityReservationFleet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::CarrierGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ClientVpnEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::CoipPool` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::CustomerGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::DHCPOptions` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::EC2Fleet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::EgressOnlyInternetGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::EIP` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ElasticGpu` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ExportImageTask` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ExportInstanceTask` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::FlowLog` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::FpgaImage` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Host` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::HostReservation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Image` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ImportImageTask` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ImportSnapshotTask` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Instance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::InstanceConnectEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::InstanceEventWindow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::InternetGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::IPv4Pool` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::IPv6Pool` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::KeyPair` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LaunchTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::LocalGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LocalGatewayRouteTable` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LocalGatewayRouteTableVirtualInterfaceGroupAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LocalGatewayRouteTableVPCAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LocalGatewayVirtualInterface` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::LocalGatewayVirtualInterfaceGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::NatGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::NetworkAcl` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::NetworkInsightsAccessScope` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::NetworkInsightsAccessScopeAnalysis` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::NetworkInsightsAnalysis` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::NetworkInsightsPath` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::NetworkInterface` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::PlacementGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::PrefixList` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ReplaceRootVolumeTask` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::ReservedInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::RouteTable` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::SecurityGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::SecurityGroupRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Snapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::SpotFleet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::SpotInstanceRequest` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Subnet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::SubnetCidrReservation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TrafficMirrorFilter` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TrafficMirrorFilterRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TrafficMirrorSession` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TrafficMirrorTarget` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayAttachment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayConnectPeer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayMulticastDomain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayPolicyTable` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayRouteTable` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::TransitGatewayRouteTableAnnouncement` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VerifiedAccessEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VerifiedAccessGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VerifiedAccessInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VerifiedAccessTrustProvider` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::Volume` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::VPC` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::VPCBlockPublicAccessExclusion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VPCEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VPCEndpointConnection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VPCEndpointService` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VPCEndpointServicePermissions` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EC2::VPCPeeringConnection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::VPNConnection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EC2::VPNGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Elastic Container Registry
<a name="services-ecr"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ECR::Repository` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Elastic Container Service
<a name="services-ecs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ECS::CapacityProvider` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::ContainerInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::Service` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::Task` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::TaskDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ECS::TaskSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elastic Disaster Recovery
<a name="services-drs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DRS::Job` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DRS::RecoveryInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DRS::ReplicationConfigurationTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DRS::SourceNetwork` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DRS::SourceServer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Elastic File System
<a name="services-efs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EFS::AccessPoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EFS::FileSystem` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Elastic Kubernetes Service (Amazon EKS)
<a name="services-eks"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EKS::Addon` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EKS::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::EKS::EKSAnywhereSubscription` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EKS::FargateProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EKS::IdentityProviderConfig` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EKS::Nodegroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EKS::PodIdentityAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Elastic Load Balancing
<a name="services-elasticloadbalancing"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ElasticLoadBalancing::LoadBalancer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElasticLoadBalancingV2::Listener` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElasticLoadBalancingV2::ListenerRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElasticLoadBalancingV2::LoadBalancer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElasticLoadBalancingV2::TargetGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ElasticLoadBalancingV2::TrustStore` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon OpenSearch Service
<a name="services-elasticsearch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Elasticsearch::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Elemental MediaLive
<a name="services-medialive"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaLive::Channel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::ChannelPlacementGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::CloudWatchAlarmTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::CloudWatchAlarmTemplateGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::EventBridgeRuleTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::EventBridgeRuleTemplateGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::Input` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::InputDevice` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::InputSecurityGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::Multiplex` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::Network` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::Node` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::Reservation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaLive::SignalMap` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental MediaConvert
<a name="services-mediaconvert"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaConvert::Job` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConvert::JobTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConvert::Preset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConvert::Queue` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental MediaPackage V2
<a name="services-mediapackagev2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaPackageV2::Channel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackageV2::ChannelGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackageV2::OriginEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental MediaStore
<a name="services-mediastore"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaStore::Container` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## MediaTailor
<a name="services-mediatailor"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaTailor::Channel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaTailor::LiveSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaTailor::PlaybackConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaTailor::SourceLocation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaTailor::VodSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental Support Cases
<a name="services-elementalsupportcases"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ElementalSupportCases::Case` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS End User Messaging Social
<a name="services-socialmessaging"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SocialMessaging::WhatsAppBusinessAccount` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Entity Resolution
<a name="services-entityresolution"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EntityResolution::IdMappingWorkflow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EntityResolution::IdNamespace` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EntityResolution::MatchingWorkflow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EntityResolution::SchemaMapping` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon CloudWatch Events
<a name="services-events"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Events::EventBus` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Events::Rule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

**Note**  
Rules in custom event buses aren't supported in Tag Editor.

## Amazon EventBridge Pipes
<a name="services-pipes"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Pipes::Pipe` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon EventBridge Scheduler
<a name="services-scheduler"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Scheduler::ScheduleGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon EventBridge Schemas
<a name="services-eventschemas"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::EventSchemas::Discoverer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EventSchemas::Registry` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::EventSchemas::Schema` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon FSx
<a name="services-fsx"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FSx::Backup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::DataRepositoryTask` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::FileCache` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::FileSystem` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::Snapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::StorageVirtualMachine` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FSx::Volume` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Fault Injection Service
<a name="services-fis"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FIS::Experiment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FIS::ExperimentTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon FinSpace schemas
<a name="services-finspace"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FinSpace::Environment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxCluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxDatabase` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxDataview` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxEnvironment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxScalingGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxUser` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FinSpace::KxVolume` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Firewall Manager
<a name="services-fms"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FMS::Applicationslist` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FMS::Policy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FMS::ProtocolsList` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FMS::ResourceSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Fleet Hub
<a name="services-iotfleethub"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTFleetHub::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Forecast
<a name="services-forecast"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Forecast::Dataset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::DatasetGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::DatasetImportJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::Explainability` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::ExplainabilityExport` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::Forecast` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::ForecastEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::ForecastExportJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::Predictor` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::PredictorBacktestExportJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Forecast::WhatIfAnalysis` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Fraud Detector
<a name="services-frauddetector"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FraudDetector::BatchImport` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::BatchPrediction` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Detector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::DetectorVersion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::EntityType` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::EventType` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::ExternalModel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Label` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::List` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Model` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::ModelVersion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Outcome` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Rule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::FraudDetector::Variable` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## FreeRTOS
<a name="services-freertos"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::FreeRTOS::Subscription` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon GameLift Servers
<a name="services-gamelift"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::GameLift::Alias` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::ContainerFleet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::ContainerGroupDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::Fleet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::GameServerGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::GameSessionQueue` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::Location` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::MatchmakingConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::MatchmakingRuleSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GameLift::Script` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Global Accelerator
<a name="services-globalaccelerator"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::GlobalAccelerator::Accelerator` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GlobalAccelerator::CrossAccountAttachment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Glue
<a name="services-glue"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Glue::Blueprint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Catalog` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Completion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Connection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Crawler` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::CustomEntityType` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Database` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Glue::DataQualityRuleset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::DevEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Job` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::MLTransform` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Registry` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Schema` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Session` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Trigger` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::UsageProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Glue::Workflow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Glue DataBrew
<a name="services-databrew"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DataBrew::Dataset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DataBrew::Job` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DataBrew::Project` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DataBrew::Recipe` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::DataBrew::Ruleset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DataBrew::Schedule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Ground Station
<a name="services-groundstation"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::GroundStation::Config` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GroundStation::Contact` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GroundStation::DataflowEndpointGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GroundStation::Ephemeris` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GroundStation::MissionProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GroundStation::Satellite` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon GuardDuty
<a name="services-guardduty"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::GuardDuty::Detector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::GuardDuty::Filter` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GuardDuty::IPSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GuardDuty::MalwareProtectionPlan` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GuardDuty::ThreatIntelSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS HealthImaging
<a name="services-healthimaging"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::HealthImaging::Datastore` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::HealthImaging::ImageSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS HealthLake
<a name="services-healthlake"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::HealthLake::FHIRDatastore` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS HealthOmics
<a name="services-omics"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Omics::AnnotationStore` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::AnnotationStoreVersion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::ReadSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::Reference` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::ReferenceStore` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::Run` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::RunCache` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::RunGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::SequenceStore` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::VariantStore` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Omics::Workflow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Interactive Video Service
<a name="services-ivs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IVS::Channel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::Composition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::EncoderConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::IngestConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::PlaybackKeyPair` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::PlaybackRestrictionPolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::PublicKey` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::RecordingConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::Stage` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::StorageConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IVS::StreamKey` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## IAM
<a name="services-sso"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SSO::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSO::Instance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSO::PermissionSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSO::TrustedTokenIssuer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Identity and Access Management
<a name="services-iam"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IAM::InstanceProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IAM::ManagedPolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IAM::OpenIDConnectProvider` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IAM::Role` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² | 
| `AWS::IAM::SAMLProvider` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IAM::ServerCertificate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IAM::VirtualMFADevice` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

¹ This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. To use Tag Editor to create or modify tags for this resource type, you must include `us-east-1` from the **Select regions** list under **Find resources to tag** in the Tag Editor console.

² This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. Because Resource Groups are maintained separately for each region, you must switch your AWS Management Console to the AWS Region that contains the resources you want to include in the group. To create a resource group that contains a global resource, you must configure your AWS Management Console to **US East (N. Virginia) us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## EC2 Image Builder
<a name="services-imagebuilder"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ImageBuilder::Component` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::ContainerRecipe` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::DistributionConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::Image` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::ImagePipeline` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::ImageRecipe` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::InfrastructureConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::LifecyclePolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ImageBuilder::Workflow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Inspector
<a name="services-inspector"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Inspector::AssessmentTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::InspectorV2::CisScanConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::InspectorV2::Filter` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Internet Monitor
<a name="services-internetmonitor"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::InternetMonitor::Monitor` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT
<a name="services-iot"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoT::Authorizer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::BillingGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::CACertificate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::CertificateProvider` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::Command` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::CustomMetric` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::Dimension` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::DomainConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::FleetMetric` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::Job` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::JobTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::MitigationAction` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::OTAUpdate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::Policy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::ProvisioningTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::RoleAlias` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::ScheduledAudit` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::SecurityProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::SoftwarePackage` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::Stream` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::ThingGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::ThingType` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoT::TopicRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoT::Tunnel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Analytics
<a name="services-iotanalytics"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTAnalytics::Channel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTAnalytics::Dataset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTAnalytics::Datastore` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTAnalytics::Pipeline` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Core Device Advisor
<a name="services-iotcoredeviceadvisor"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTCoreDeviceAdvisor::SuiteDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTCoreDeviceAdvisor::SuiteRun` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Events
<a name="services-iotevents"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTEvents::AlarmModel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTEvents::DetectorModel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTEvents::Input` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS IoT FleetWise
<a name="services-iotfleetwise"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTFleetWise::Campaign` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTFleetWise::DecoderManifest` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTFleetWise::Fleet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTFleetWise::ModelManifest` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTFleetWise::SignalCatalog` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::IoTFleetWise::StateTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTFleetWise::Vehicle` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS IoT Greengrass
<a name="services-greengrass"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Greengrass::BulkDeployment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::ConnectorDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::CoreDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::DeviceDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::FunctionDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::Group` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::LoggerDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::ResourceDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Greengrass::SubscriptionDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Greengrass Version 2
<a name="services-greengrassv2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::GreengrassV2::ComponentVersion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::GreengrassV2::CoreDevice` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT SiteWise console
<a name="services-iotsitewise"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTSiteWise::AccessPolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Asset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::AssetModel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Dashboard` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Dataset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Gateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Portal` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::Project` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTSiteWise::TimeSeries` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS IoT Wireless
<a name="services-iotwireless"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::IoTWireless::Destination` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::DeviceProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::FuotaTask` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::ImportTask` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::MulticastGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::NetworkAnalyzerConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::PartnerAccount` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::ServiceProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::TaskDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::WirelessDevice` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::IoTWireless::WirelessGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Kendra
<a name="services-kendra"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Kendra::DataSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Kendra::FeaturedResultsSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Kendra::Index` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Kendra::QuerySuggestionsBlockList` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Kendra::Thesaurus` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Kendra Intelligent Ranking
<a name="services-kendraranking"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KendraRanking::ExecutionPlan` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Key Management Service
<a name="services-kms"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KMS::Alias` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::KMS::Key` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Keyspaces (for Apache Cassandra)
<a name="services-cassandra"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Cassandra::Keyspace` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Cassandra::Table` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Kinesis
<a name="services-kinesis"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Kinesis::Stream` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Managed Service for Apache Flink
<a name="services-kinesisanalytics"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KinesisAnalytics::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::KinesisAnalyticsV2::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Data Firehose
<a name="services-kinesisfirehose"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KinesisFirehose::DeliveryStream` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Kinesis Video Streams
<a name="services-kinesisvideo"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KinesisVideo::SignalingChannel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::KinesisVideo::Stream` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Lambda
<a name="services-lambda"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Lambda::Alias` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Lambda::CodeSigningConfig` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lambda::EventSourceMapping` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Lambda::Function` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Lambda::LayerVersion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Lambda::Version` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Launch Wizard
<a name="services-launchwizard"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LaunchWizard::Deployment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Lex
<a name="services-lex"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Lex::Bot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lex::BotAlias` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LexV2::TestSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS License Manager
<a name="services-licensemanager"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LicenseManager::License` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LicenseManager::LicenseConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LicenseManager::ReportGenerator` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Lightsail
<a name="services-lightsail"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Lightsail::Bucket` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Certificate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Container` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Database` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Disk` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::DiskSnapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Distribution` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::Instance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::InstanceSnapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::KeyPair` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::LoadBalancer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::RelationalDatabaseSnapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Lightsail::StaticIp` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Linux subscriptions in AWS License Manager
<a name="services-licensemanagerlinuxsubscriptions"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LicenseManagerLinuxSubscriptions::SubscriptionProvider` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Location Service
<a name="services-location"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Location::GeofenceCollection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Location::Map` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Location::PlaceIndex` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Location::RouteCalculator` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Location::Tracker` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Lookout for Equipment
<a name="services-lookoutequipment"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LookoutEquipment::Dataset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LookoutEquipment::InferenceScheduler` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LookoutEquipment::LabelGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LookoutEquipment::Model` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Lookout for Metrics
<a name="services-lookoutmetrics"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LookoutMetrics::Alert` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LookoutMetrics::AnomalyDetector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LookoutMetrics::MetricSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Lookout for Vision
<a name="services-lookoutvision"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LookoutVision::Model` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon MQ
<a name="services-amazonmq"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AmazonMQ::Broker` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AmazonMQ::Configuration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Machine Learning
<a name="services-machinelearning"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MachineLearning::BatchPrediction` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MachineLearning::DataSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MachineLearning::Evaluation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MachineLearning::MLModel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Macie
<a name="services-macie"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Macie::ClassificationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Macie::CustomDataIdentifier` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Macie::FindingsFilter` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Macie::Member` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Mainframe Modernization
<a name="services-m2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::M2::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::M2::Environment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Mainframe Modernization Application Testing
<a name="services-apptest"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::AppTest::TestCase` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppTest::TestConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppTest::TestRun` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::AppTest::TestSuite` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Blockchain
<a name="services-managedblockchain"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ManagedBlockchain::Accessor` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ManagedBlockchain::Invitation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ManagedBlockchain::Member` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ManagedBlockchain::Network` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ManagedBlockchain::Node` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ManagedBlockchain::Proposal` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Grafana
<a name="services-grafana"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Grafana::Workspace` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Service for Prometheus
<a name="services-aps"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::APS::RuleGroupsNamespace` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::APS::Scraper` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::APS::Workspace` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Streaming for Apache Kafka
<a name="services-msk"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MSK::Replicator` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MSK::VpcConnection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Kafka::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Streaming for Apache Kafka Connect
<a name="services-kafkaconnect"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::KafkaConnect::Connector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::KafkaConnect::CustomPlugin` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::KafkaConnect::WorkerConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Managed Workflows for Apache Airflow
<a name="services-mwaa"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MWAA::Environment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Marketplace Catalog API
<a name="services-marketplacecatalog"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MarketplaceCatalog::ChangeSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MarketplaceCatalog::Entity` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental MediaConnect
<a name="services-mediaconnect"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaConnect::Flow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConnect::FlowEntitlement` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConnect::FlowOutput` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaConnect::FlowSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Elemental MediaPackage
<a name="services-mediapackage"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MediaPackage::Asset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackage::Channel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackage::OriginEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackage::PackagingConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MediaPackage::PackagingGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon MemoryDB
<a name="services-memorydb"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MemoryDB::ACL` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::MultiRegionCluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::ParameterGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::Snapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::SubnetGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MemoryDB::User` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Migration Hub Orchestrator
<a name="services-migrationhuborchestrator"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::MigrationHubOrchestrator::Template` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::MigrationHubOrchestrator::Workflow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Migration Hub Refactor Spaces
<a name="services-refactorspaces"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RefactorSpaces::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RefactorSpaces::Environment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RefactorSpaces::Route` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RefactorSpaces::Service` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Neptune
<a name="services-neptunegraph"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::NeptuneGraph::Graph` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NeptuneGraph::GraphSnapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Network Firewall
<a name="services-networkfirewall"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::NetworkFirewall::Firewall` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkFirewall::FirewallPolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkFirewall::RuleGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Network Synthetic Monitor
<a name="services-networkmonitor"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::NetworkMonitor::Monitor` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkMonitor::Probe` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Network Manager
<a name="services-networkmanager"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::NetworkManager::Connection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::ConnectPeer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::CoreNetwork` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::Device` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::GlobalNetwork` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::Link` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::Site` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::TransitGatewayPeering` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::NetworkManager::VpcAttachment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon One
<a name="services-one"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::One::DeviceConfigurationTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::One::DeviceInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::One::Site` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon OpenSearch Service OpenSearch
<a name="services-opensearchservice"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::OpenSearchService::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## OpenSearch Serverless
<a name="services-opensearchserverless"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::OpenSearchServerless::Collection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon OpenSearch Service
<a name="services-opensearch"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::OpenSearch::DataSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon OpenSearch Service Ingestion
<a name="services-osis"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::OSIS::Pipeline` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS OpsWorks
<a name="services-opsworks"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::OpsWorks::Instance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::OpsWorks::Layer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::OpsWorks::Stack` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Organizations
<a name="services-organizations"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Organizations::Account` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Organizations::OrganizationalUnit` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Organizations::Policy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Organizations::ResourcePolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Organizations::Root` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Outposts
<a name="services-outposts"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Outposts::Outpost` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Outposts::Site` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Panorama
<a name="services-panorama"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Panorama::ApplicationInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Panorama::Device` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Panorama::Package` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Parallel Computing Service
<a name="services-pcs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::PCS::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Payment Cryptography
<a name="services-paymentcryptography"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::PaymentCryptography::Key` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Payments
<a name="services-payments"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Payments::PaymentInstrument` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Relational Database Service Performance Insights
<a name="services-pi"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Pi::PerformanceAnalysisReport` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Personalize
<a name="services-personalize"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Personalize::BatchInferenceJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::BatchSegmentJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::Campaign` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::Dataset` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::DatasetExportJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::DatasetGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::DatasetImportJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::EventTracker` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::Filter` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::Recommender` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Personalize::Solution` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Pinpoint
<a name="services-pinpoint"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Pinpoint::App` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Pinpoint::EmailTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Pinpoint::PushTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Pinpoint::SmsTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Pinpoint::VoiceTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Pinpoint SMS and Voice API
<a name="services-pinpointsmsvoicev2"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::PinpointSMSVoiceV2::ConfigurationSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::PinpointSMSVoiceV2::OptOutList` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::PinpointSMSVoiceV2::PhoneNumber` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::PinpointSMSVoiceV2::Pool` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Pricing Calculator
<a name="services-bcmpricingcalculator"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::BCMPricingCalculator::BillEstimate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::BCMPricingCalculator::BillScenario` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::BCMPricingCalculator::WorkloadEstimate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Private CA Connector for Active Directory
<a name="services-pcaconnectorad"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::PCAConnectorAD::Connector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Private CA Connector for SCEP
<a name="services-pcaconnectorscep"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::PCAConnectorScep::Connector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Proton
<a name="services-proton"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Proton::Component` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::Deployment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::Environment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::EnvironmentAccountConnection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::EnvironmentTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::Repository` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::Service` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::ServiceInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Proton::ServiceTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Q Business Apps
<a name="services-qapps"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::QApps::QApp` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QApps::QAppSession` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Q Business
<a name="services-qbusiness"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::QBusiness::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QBusiness::DataSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QBusiness::Index` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QBusiness::Plugin` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QBusiness::Retriever` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QBusiness::WebExperience` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Quantum Ledger Database (Amazon QLDB)
<a name="services-qldb"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::QLDB::Ledger` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::QLDB::Stream` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::QLDB::Table` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Quick
<a name="services-quicksight"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::QuickSight::Analysis` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Brand` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::CustomPermissions` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Dashboard` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::DataSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::DataSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Folder` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Namespace` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Template` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Theme` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::Topic` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::User` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::QuickSight::VPCConnection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS DeepRacer
<a name="services-deepracer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::DeepRacer::Car` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepRacer::EvaluationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepRacer::Leaderboard` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepRacer::LeaderboardEvaluationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepRacer::ReinforcementLearningModel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::DeepRacer::TrainingJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Recycle Bin
<a name="services-rbin"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RBin::Rule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Redshift
<a name="services-redshift"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Redshift::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Redshift::ClusterParameterGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Redshift::ClusterSecurityGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Redshift::ClusterSubnetGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Redshift::EventSubscription` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::HSMClientCertificate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::HSMConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::Integration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::Namespace` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::Snapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::SnapshotCopyGrant` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::SnapshotSchedule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Redshift::UsageLimit` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Redshift Serverless
<a name="services-redshiftserverless"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RedshiftServerless::Namespace` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RedshiftServerless::RecoveryPoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RedshiftServerless::Snapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RedshiftServerless::Workgroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Rekognition
<a name="services-rekognition"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Rekognition::Collection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Rekognition::StreamProcessor` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Relational Database Service (Amazon RDS)
<a name="services-rds"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RDS::CustomDBEngineVersion` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBCluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::DBClusterEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBClusterParameterGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::DBClusterSnapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::DBParameterGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::DBProxy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBProxyEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBProxyTargetGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBSecurityGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::DBSnapshot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::DBSubnetGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::RDS::Deployment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::EventSubscription` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::GlobalCluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::Integration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::OptionGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::ReservedDBInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::SnapshotTenantDatabase` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RDS::TenantDatabase` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Resilience Hub
<a name="services-resiliencehub"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ResilienceHub::App` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ResilienceHub::AppAssessment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ResilienceHub::RecommendationTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ResilienceHub::ResiliencyPolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Resource Access Manager
<a name="services-ram"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RAM::ResourceShare` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Resource Groups
<a name="services-resourcegroups"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ResourceGroups::Group` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Robomaker
<a name="services-robomaker"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::RoboMaker::DeploymentJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::Fleet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::Robot` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::RobotApplication` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::SimulationApplication` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::SimulationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::SimulationJobBatch` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::World` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::WorldExportJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::WorldGenerationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::RoboMaker::WorldTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Route 53
<a name="services-route53"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Route53::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53::HealthCheck` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² | 
| `AWS::Route53::HostedZone` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² | 

¹ This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. To use Tag Editor to create or modify tags for this resource type, you must include `us-east-1` from the **Select regions** list under **Find resources to tag** in the Tag Editor console.

² This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. Because Resource Groups are maintained separately for each region, you must switch your AWS Management Console to the AWS Region that contains the resources you want to include in the group. To create a resource group that contains a global resource, you must configure your AWS Management Console to **US East (N. Virginia) us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## Amazon Route 53
<a name="services-route53recoverycontrol"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Route53RecoveryControl::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53RecoveryControl::ControlPanel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53RecoveryControl::SafetyRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Route 53 Profiles
<a name="services-route53profiles"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Route53Profiles::Profile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Profiles::ProfileAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Route 53 Recovery Readiness in Application Recovery Controller (ARC)
<a name="services-route53recoveryreadiness"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Route53RecoveryReadiness::Cell` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53RecoveryReadiness::ReadinessCheck` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53RecoveryReadiness::RecoveryGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53RecoveryReadiness::ResourceSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Route 53 Resolver
<a name="services-route53resolver"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Route53Resolver::FirewallDomainList` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::FirewallRuleGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::FirewallRuleGroupAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::OutpostResolver` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::ResolverEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::ResolverQueryLoggingConfig` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Route53Resolver::ResolverRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes¹ |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes² |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

¹ This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. To use Tag Editor to create or modify tags for this resource type, you must include `us-east-1` from the **Select regions** list under **Find resources to tag** in the Tag Editor console.

² This is a resource for a global service that is hosted in the **US East (N. Virginia)** Region. Because Resource Groups are maintained separately for each region, you must switch your AWS Management Console to the AWS Region that contains the resources you want to include in the group. To create a resource group that contains a global resource, you must configure your AWS Management Console to **US East (N. Virginia) us-east-1** using the Region selector in the upper-right corner of the AWS Management Console.

## Amazon Glacier
<a name="services-glacier"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Glacier::Vault` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS SQL Workbench
<a name="services-sqlworkbench"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SQLWorkbench::Chart` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SQLWorkbench::Connection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SQLWorkbench::Notebook` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SQLWorkbench::SavedQuery` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon SageMaker AI
<a name="services-sagemaker"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SageMaker::Action` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Algorithm` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::App` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::AppImageConfig` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Artifact` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::AutoMLJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Cluster` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ClusterSchedulerConfig` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::CodeRepository` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::CompilationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ComputeQuota` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Context` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::DataQualityJobDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::DeviceFleet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::EdgeDeploymentPlan` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::EdgePackagingJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Endpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::EndpointConfig` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::Experiment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ExperimentTrial` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ExperimentTrialComponent` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::FeatureGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::FlowDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Hub` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::HubContent` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::HumanTaskUi` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::HyperParameterTuningJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Image` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::InferenceComponent` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::InferenceExperiment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::InferenceRecommendationsJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::LabelingJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::LineageGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::MlflowTrackingServer` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Model` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::ModelBiasJobDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ModelCard` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ModelExplainabilityJobDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ModelPackage` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ModelPackageGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::ModelQualityJobDefinition` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::MonitoringSchedule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::NotebookInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::OptimizationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Pipeline` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::ProcessingJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Project` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SageMaker::Space` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::StudioLifecycleConfig` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::TrainingJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::TransformJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::UserProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Workforce` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SageMaker::Workteam` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon SageMaker AI geospatial
<a name="services-sagemakergeospatial"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SagemakerGeospatial::EarthObservationJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SagemakerGeospatial::RasterDataCollection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SagemakerGeospatial::VectorEnrichmentJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Savings Plans
<a name="services-savingsplans"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SavingsPlans::SavingsPlan` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Secrets Manager
<a name="services-secretsmanager"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SecretsManager::Secret` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Security Hub CSPM
<a name="services-securityhub"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SecurityHub::AutomationRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SecurityHub::ConfigurationPolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SecurityHub::Hub` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SecurityHub::ProductSubscription` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Service Catalog
<a name="services-servicecatalog"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ServiceCatalog::CloudFormationProduct` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::ServiceCatalog::Portfolio` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## AWS Service Catalog AppRegistry
<a name="services-servicecatalogappregistry"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ServiceCatalogAppRegistry::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ServiceCatalogAppRegistry::AttributeGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Service Quotas
<a name="services-servicequotas"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ServiceQuotas::Quota` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Shield
<a name="services-shield"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Shield::Protection` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Shield::ProtectionGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS SimSpace Weaver
<a name="services-simspaceweaver"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SimSpaceWeaver::Simulation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Simple Email Service
<a name="services-ses"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SES::ConfigurationSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SES::ContactList` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SES::DedicatedIpPool` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SES::Identity` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SES::MailManagerArchive` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SES::MailManagerIngressPoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SES::MailManagerRuleSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SES::MailManagerTrafficPolicy` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Simple Notification Service
<a name="services-sns"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SNS::Topic` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Simple Queue Service
<a name="services-sqs"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SQS::Queue` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Amazon Simple Storage Service (Amazon S3)
<a name="services-s3"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::S3::AccessGrant` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::S3::AccessGrantsLocation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::S3::Bucket` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::S3::Job` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::S3::StorageLens` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::S3::StorageLensGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Simple Workflow Service
<a name="services-swf"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SWF::Domain` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Snowball Edge Device Management
<a name="services-snowdevicemanagement"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SnowDeviceManagement::ManagedDevice` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SnowDeviceManagement::Task` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Step Functions
<a name="services-stepfunctions"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::StepFunctions::Activity` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::StepFunctions::StateMachine` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 

## Storage Gateway
<a name="services-storagegateway"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::StorageGateway::FileShare` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::StorageGateway::FileSystemAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::StorageGateway::Gateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::StorageGateway::Tape` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::StorageGateway::TapePool` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::StorageGateway::Volume` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Supply Chain
<a name="services-scn"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SCN::Instance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Systems Manager
<a name="services-ssm"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SSM::Association` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::AutomationExecution` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::Document` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SSM::MaintenanceWindow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::ManagedInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::OpsItem` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::OpsMetadata` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSM::Parameter` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SSM::PatchBaseline` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SSM::Session` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Systems Manager Incident Manager
<a name="services-ssmincidents"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SSMIncidents::IncidentRecord` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSMIncidents::ReplicationSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSMIncidents::ResponsePlan` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Systems Manager Incident Manager Contacts
<a name="services-ssmcontacts"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SSMContacts::Contact` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::SSMContacts::Rotation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Systems Manager Quick Setup
<a name="services-ssmquicksetup"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SSMQuickSetup::ConfigurationManager` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Systems Manager for SAP
<a name="services-systemsmanagersap"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::SystemsManagerSAP::Application` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::SystemsManagerSAP::Database` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Telco Network Builder
<a name="services-tnb"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::TNB::FunctionPackage` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::TNB::NetworkInstance` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::TNB::NetworkPackage` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Textract
<a name="services-textract"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Textract::Adapter` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Timestream
<a name="services-timestream"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Timestream::Database` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Timestream::ScheduledQuery` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::Timestream::Table` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Transcribe
<a name="services-transcribe"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Transcribe::LanguageModel` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::MedicalScribeJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::MedicalTranscriptionJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::MedicalVocabulary` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::TranscriptionJob` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::Vocabulary` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transcribe::VocabularyFilter` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Transfer Family
<a name="services-transfer"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Transfer::Agreement` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::Certificate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::Connector` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::HostKey` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::Profile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::Server` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::User` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::WebApp` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Transfer::Workflow` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon Translate
<a name="services-translate"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Translate::ParallelData` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::Translate::Terminology` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS User Notifications
<a name="services-usernotifications"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::UserNotifications::NotificationConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## User subscriptions in AWS License Manager
<a name="services-licensemanagerusersubscriptions"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::LicenseManagerUserSubscriptions::AssociateUser` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LicenseManagerUserSubscriptions::IdentityProvider` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LicenseManagerUserSubscriptions::LicenseServerEndpoint` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::LicenseManagerUserSubscriptions::ProductSubscription` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon VPC Lattice
<a name="services-vpclattice"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::VpcLattice::AccessLogSubscription` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::Listener` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ResourceConfiguration` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ResourceGateway` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::Rule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::Service` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ServiceNetwork` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ServiceNetworkResourceAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ServiceNetworkServiceAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::ServiceNetworkVpcAssociation` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VpcLattice::TargetGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Marketplace Vendor Insights
<a name="services-vendorinsights"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::VendorInsights::DataSource` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::VendorInsights::SecurityProfile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS WAF
<a name="services-waf"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::WAF::RateBasedRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAF::Rule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAF::RuleGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAF::WebACL` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS WAF Classic Regional
<a name="services-wafregional"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::WAFRegional::RateBasedRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAFRegional::Rule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAFRegional::RuleGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WAFRegional::WebACL` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Well-Architected Tool
<a name="services-wellarchitected"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::WellArchitected::Lens` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WellArchitected::Profile` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WellArchitected::ReviewTemplate` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WellArchitected::Workload` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS Wickr
<a name="services-wickr"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Wickr::Network` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon WorkMail
<a name="services-workmail"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::Workmail::Organization` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon WorkSpaces
<a name="services-workspaces"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::WorkSpaces::ConnectionAlias` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpaces::Directory` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpaces::Workspace` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes | 
| `AWS::WorkSpaces::WorkspaceBundle` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpaces::WorkspaceImage` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpaces::WorkspaceIpGroup` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpaces::WorkspacesPool` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon WorkSpaces Secure Browser
<a name="services-workspacesweb"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::WorkSpacesWeb::BrowserSettings` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::DataProtectionSettings` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::IdentityProvider` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::IpAccessSettings` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::NetworkSettings` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::Portal` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::TrustStore` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::UserAccessLoggingSettings` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::WorkSpacesWeb::UserSettings` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Amazon WorkSpaces Thin Client
<a name="services-thinclient"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::ThinClient::Device` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ThinClient::Environment` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::ThinClient::SoftwareSet` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## AWS X-Ray
<a name="services-xray"></a>


| **Resources** | **Tag Editor Tagging** | **Tag-based Groups** | **CloudFormation Stack-based Groups** | 
| --- | --- | --- | --- | 
| `AWS::XRay::Group` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 
| `AWS::XRay::SamplingRule` |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/ARG/latest/userguide/images/icon-no.png) No | 

## Deprecated resource types
<a name="deprecated-types"></a>

The following resource types are no longer supported for the specified functionality.


| **Service** | **Resource type** | **Support change** | **Date** | 
| --- | --- | --- | --- | 
| AWS RoboMaker | [`AWS::RoboMaker::Robot`](https://docs.aws.amazon.com/robomaker/latest/dg/chapter-support-policy.html#software-support-policy-may2022) | No longer supported by Tag Editor. | May 2, 2022 | 
| AWS RoboMaker | [`AWS::RoboMaker::Fleet`](https://docs.aws.amazon.com/robomaker/latest/dg/chapter-support-policy.html#software-support-policy-may2022) | No longer supported by Tag Editor. | May 2, 2022 | 
| AWS RoboMaker | [`AWS::RoboMaker::DeploymentJob`](https://docs.aws.amazon.com/robomaker/latest/dg/chapter-support-policy.html#software-support-policy-may2022) | No longer supported by Tag Editor. | May 2, 2022 | 