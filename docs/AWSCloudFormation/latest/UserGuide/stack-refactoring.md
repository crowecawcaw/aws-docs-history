# Stack refactoring

With stack refactoring, you can reorganize resources in your CloudFormation stacks while
 preserving existing resource properties and data. You can move resources between stacks,
 split large stacks into smaller ones, or combine multiple stacks into one stack.

###### Topics

* [How stack refactoring works](#stack-refactoring-overview "#stack-refactoring-overview")
* [Stack refactoring
 considerations](#stack-refactoring-considerations "#stack-refactoring-considerations")
* [AWS CLI commands for stack
 refactoring](#stack-refactoring-cli-commands "#stack-refactoring-cli-commands")
* [Refactor a stack using the AWS CLI](#stack-refactoring-cli "#stack-refactoring-cli")
* [Resource limitations](#stack-refactoring-resource-limitations "#stack-refactoring-resource-limitations")

## How stack refactoring works


Refactoring stacks involves these phases:


1. Assess your current infrastructure –
 Review your existing CloudFormation stacks and resources to identify stack
 refactoring opportunities.
2. Plan your refactor – Define how
 resources should be organized. Consider your dependencies, naming conventions,
 and operational limits. These can affect the CloudFormation validation later.
3. Determine the destination stacks –
 Decide which stacks you will refactor resources into. You can move resources
 between at least 2 stacks, and a maximum of 5 stacks. Resources can be moved
 between nested stacks.
4. Update your templates – Change your
 CloudFormation templates to reflect the planned change, such as moving resource
 definitions between templates. You can rename logical IDs during this
 process.
5. Create the stack refactor – Provide a
 list of stack names and templates that you want to refactor.
6. Review the refactor impact and resolve any
 conflicts – CloudFormation validates the templates you provide
 and checks cross-stack dependencies, resource types with tag update problems,
 and resource logical ID conflicts.


If the validation succeeds, CloudFormation will generate a preview of the refactor
 actions that will occur during execution.


If the validation fails, resolve the identified issues and retry. For
 conflicts, provide a resource logical ID mapping that shows the source and
 destination of the conflicting resources.
7. Execute the refactor – After confirming
 the changes align with your refactoring goals, complete the stack
 refactor.
8. Monitor – Track the execution status to
 ensure the operation completes successfully.

## Stack refactoring
 considerations


As you refactor your stacks, keep the following in mind:



* Refactor operations don't allow new resource creations, resource deletions, or
 changes to resource configurations.
* You can't change or add new parameters, conditions, or mappings during a stack
 refactor. A possible workaround is to update your stack before performing the
 refactor.
* You can't refactor the same resource into multiple stacks.
* You can't refactor resources that refer to pseudo parameters whose values
 differ between the source and destination stacks, such as
 `AWS::StackName`.
* CloudFormation doesn't support empty stacks. If refactoring would leave a stack
 with no resources, you must first add at least one resource to that stack before
 you run [create-stack-refactor](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack-refactor.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack-refactor.html"). This can be a simple resource like
 `AWS::SNS::Topic` or
 `AWS::CloudFormation::WaitCondition`. For example:



```
Resources:
  MySimpleSNSTopic:
    Type: AWS::SNS::Topic
    Properties:
      DisplayName: MySimpleTopic
```
* Stack refactor doesn't support stacks that have stack policies attached,
 regardless of what the policies allow or deny.

## AWS CLI commands for stack
 refactoring


The AWS CLI commands for stack refactoring include:



* [create-stack-refactor](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack-refactor.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack-refactor.html") to validate and generate a preview of planned
 changes.
* [describe-stack-refactor](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-refactor.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-refactor.html") to retrieve the status and details of a
 stack refactoring operation.
* [execute-stack-refactor](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/execute-stack-refactor.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/execute-stack-refactor.html") to complete the validated stack refactoring
 operation.
* [get-template](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/get-template.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/get-template.html") to retrieve the template for an existing stack.
* [list-stack-refactors](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-stack-refactors.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-stack-refactors.html") to list all stack refactoring operations in
 your account with their current status and basic information.
* [list-stack-refactor-actions](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-stack-refactor-actions.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-stack-refactor-actions.html") to show a preview of the specific
 actions CloudFormation will perform on each stack and resource during the refactor
 execution.

## Refactor a stack using the AWS CLI


Use the following procedure to refactor a stack using the AWS CLI. 


1. Use the [get-template](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/get-template.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/get-template.html") command to retrieve the CloudFormation templates for the
 stacks that you want to refactor.



```
aws cloudformation get-template --stack-name `Stack1`
```

When you have the templates, use the integrated development environment (IDE)
 of your choice to update them to use the desired structure and resource
 organization.
2. Use the [create-stack-refactor](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack-refactor.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack-refactor.html") command and provide the stack names and
 updated templates for the stacks to refactor. Include the
 `--enable-stack-creation` option to allow CloudFormation to create
 new stacks if they don't already exist. 



```
aws cloudformation create-stack-refactor \
  --stack-definitions \
    StackName=`Stack1`,TemplateBody@=`file://template1-updated.yaml` \
    StackName=`Stack2`,TemplateBody@=`file://template2-updated.yaml` \
  --enable-stack-creation
```

The command returns a `StackRefactorId` that you'll use in later
 steps.



```
{
    "StackRefactorId": "9c384f70-4e07-4ed7-a65d-fee5eb430841"
}
```

If conflicts are detected during template validation (which you can confirm in
 the next step), use the [create-stack-refactor](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack-refactor.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack-refactor.html") command with the
 `--resource-mappings` option.



```
aws cloudformation create-stack-refactor \
  --stack-definitions \
    StackName=`Stack1`,TemplateBody@=`file://template1-updated.yaml` \
    StackName=`Stack2`,TemplateBody@=`file://template2-updated.yaml` \
  --enable-stack-creation \ 
  --resource-mappings `file://resource-mapping.json`
```

The following is an example `resource-mapping.json` file.



```
[
    {
        "Source": {
            "StackName": "`Stack1`",
            "LogicalResourceId": "`MySNSTopic`"
        },
        "Destination": {
            "StackName": "`Stack2`",
            "LogicalResourceId": "`MyLambdaSNSTopic`"
        }
    }
]
```
3. Use the [describe-stack-refactor](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-refactor.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-refactor.html") command to make sure the
 `Status` is `CREATE_COMPLETE`. This verifies that the
 validation is complete.



```
aws cloudformation describe-stack-refactor \
  --stack-refactor-id `9c384f70-4e07-4ed7-a65d-fee5eb430841`
```

Example output:



```
{
    "StackRefactorId": "9c384f70-4e07-4ed7-a65d-fee5eb430841",
    "StackIds": [
        "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack1/3e6a1ff0-94b1-11f0-aa6f-0a88d2e03acf",
        "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack2/5da91650-94b1-11f0-81cf-0a23500e151b"
    ],
    "ExecutionStatus": "AVAILABLE",
    "Status": "CREATE_COMPLETE"
}
```
4. Use the [list-stack-refactor-actions](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-stack-refactor-actions.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-stack-refactor-actions.html") command to preview the specific actions
 that will be performed.



```
aws cloudformation list-stack-refactor-actions \
  --stack-refactor-id `9c384f70-4e07-4ed7-a65d-fee5eb430841`
```

Example output:



```
{
    "StackRefactorActions": [
        {
            "Action": "MOVE",
            "Entity": "RESOURCE",
            "PhysicalResourceId": "MyTestLambdaRole",
            "Description": "No configuration changes detected.",
            "Detection": "AUTO",
            "TagResources": [],
            "UntagResources": [],
            "ResourceMapping": {
                "Source": {
                    "StackName": "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack1/3e6a1ff0-94b1-11f0-aa6f-0a88d2e03acf",
                    "LogicalResourceId": "MyLambdaRole"
                },
                "Destination": {
                    "StackName": "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack2/5da91650-94b1-11f0-81cf-0a23500e151b",
                    "LogicalResourceId": "MyLambdaRole"
                }
            }
        },
        {
            "Action": "MOVE",
            "Entity": "RESOURCE",
            "PhysicalResourceId": "MyTestFunction",
            "Description": "Resource configuration changes will be validated during refactor execution.",
            "Detection": "AUTO",
            "TagResources": [
                {
                    "Key": "aws:cloudformation:stack-name",
                    "Value": "Stack2"
                },
                {
                    "Key": "aws:cloudformation:logical-id",
                    "Value": "MyFunction"
                },
                {
                    "Key": "aws:cloudformation:stack-id",
                    "Value": "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack2/5da91650-94b1-11f0-81cf-0a23500e151b"
                }
            ],
            "UntagResources": [
                "aws:cloudformation:stack-name",
                "aws:cloudformation:logical-id",
                "aws:cloudformation:stack-id"
            ],
            "ResourceMapping": {
                "Source": {
                    "StackName": "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack1/3e6a1ff0-94b1-11f0-aa6f-0a88d2e03acf",
                    "LogicalResourceId": "MyFunction"
                },
                "Destination": {
                    "StackName": "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack2/5da91650-94b1-11f0-81cf-0a23500e151b",
                    "LogicalResourceId": "MyFunction"
                }
            }
        }
    ]
}
```
5. After reviewing and confirming your changes, use the [execute-stack-refactor](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/execute-stack-refactor.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/execute-stack-refactor.html") command to complete the stack refactoring
 operation.



```
aws cloudformation execute-stack-refactor \
  --stack-refactor-id `9c384f70-4e07-4ed7-a65d-fee5eb430841`
```
6. Use the [describe-stack-refactor](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-refactor.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-refactor.html") command to monitor the execution
 status.



```
aws cloudformation describe-stack-refactor \
  --stack-refactor-id `9c384f70-4e07-4ed7-a65d-fee5eb430841`
```

Example output:



```
{
    "StackRefactorId": "9c384f70-4e07-4ed7-a65d-fee5eb430841",
    "StackIds": [
        "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack1/3e6a1ff0-94b1-11f0-aa6f-0a88d2e03acf",
        "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack2/5da91650-94b1-11f0-81cf-0a23500e151b"
    ],
    "ExecutionStatus": "SUCCEEDED",
    "Status": "COMPLETE"
}         
```

## Resource limitations



* Stack refactoring only supports resource types with a
 `provisioningType` of `FULLY_MUTABLE`, which you can
 check using the [describe-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html") command.
* CloudFormation will validate resource eligibility during refactor creation and
 report any unsupported resources in the output of the [describe-stack-refactor](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-refactor.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-refactor.html") command.
* The following resources aren't supported for stack refactoring:




	+ `AWS::ACMPCA::Certificate`
	+ `AWS::ACMPCA::CertificateAuthority`
	+ `AWS::ACMPCA::CertificateAuthorityActivation`
	+ `AWS::ApiGateway::BasePathMapping`
	+ `AWS::ApiGateway::Method`
	+ `AWS::AppConfig::ConfigurationProfile`
	+ `AWS::AppConfig::Deployment`
	+ `AWS::AppConfig::Environment`
	+ `AWS::AppConfig::Extension`
	+ `AWS::AppConfig::ExtensionAssociation`
	+ `AWS::AppStream::DirectoryConfig`
	+ `AWS::AppStream::StackFleetAssociation`
	+ `AWS::AppStream::StackUserAssociation`
	+ `AWS::AppStream::User`
	+ `AWS::BackupGateway::Hypervisor`
	+ `AWS::CertificateManager::Certificate`
	+ `AWS::CloudFormation::CustomResource`
	+ `AWS::CloudFormation::Macro`
	+ `AWS::CloudFormation::WaitCondition`
	+ `AWS::CloudFormation::WaitConditionHandle`
	+ `AWS::CodeDeploy::DeploymentGroup`
	+ `AWS::CodePipeline::CustomActionType`
	+ `AWS::Cognito::UserPoolRiskConfigurationAttachment`
	+ `AWS::Cognito::UserPoolUICustomizationAttachment`
	+ `AWS::Cognito::UserPoolUserToGroupAttachment`
	+ `AWS::Config::ConfigRule`
	+ `AWS::Config::ConfigurationRecorder`
	+ `AWS::Config::DeliveryChannel`
	+ `AWS::DataBrew::Dataset`
	+ `AWS::DataBrew::Job`
	+ `AWS::DataBrew::Project`
	+ `AWS::DataBrew::Recipe`
	+ `AWS::DataBrew::Ruleset`
	+ `AWS::DataBrew::Schedule`
	+ `AWS::DataZone::DataSource`
	+ `AWS::DataZone::Environment`
	+ `AWS::DataZone::EnvironmentBlueprintConfiguration`
	+ `AWS::DataZone::EnvironmentProfile`
	+ `AWS::DataZone::Project`
	+ `AWS::DataZone::SubscriptionTarget`
	+ `AWS::DirectoryService::MicrosoftAD`
	+ `AWS::DynamoDB::GlobalTable`
	+ `AWS::EC2::LaunchTemplate`
	+ `AWS::EC2::NetworkInterfacePermission`
	+ `AWS::EC2::SpotFleet`
	+ `AWS::EC2::VPCDHCPOptionsAssociation`
	+ `AWS::EC2::VolumeAttachment`
	+ `AWS::EMR::Cluster`
	+ `AWS::EMR::InstanceFleetConfig`
	+ `AWS::EMR::InstanceGroupConfig`
	+ `AWS::ElastiCache::CacheCluster`
	+ `AWS::ElastiCache::ReplicationGroup`
	+ `AWS::ElastiCache::SecurityGroup`
	+ `AWS::ElastiCache::SecurityGroupIngress`
	+ `AWS::ElasticBeanstalk::ConfigurationTemplate`
	+ `AWS::ElasticLoadBalancing::LoadBalancer`
	+ `AWS::ElasticLoadBalancingV2::ListenerCertificate`
	+ `AWS::Elasticsearch::Domain`
	+ `AWS::FIS::ExperimentTemplate`
	+ `AWS::Glue::Schema`
	+ `AWS::GuardDuty::IPSet`
	+ `AWS::GuardDuty::PublishingDestination`
	+ `AWS::GuardDuty::ThreatIntelSet`
	+ `AWS::IAM::AccessKey`
	+ `AWS::IAM::UserToGroupAddition`
	+ `AWS::ImageBuilder::Component`
	+ `AWS::IoT::PolicyPrincipalAttachment`
	+ `AWS::IoT::ThingPrincipalAttachment`
	+ `AWS::IoTFleetWise::Campaign`
	+ `AWS::IoTWireless::WirelessDeviceImportTask`
	+ `AWS::Lambda::EventInvokeConfig`
	+ `AWS::Lex::BotVersion`
	+ `AWS::M2::Application`
	+ `AWS::MSK::Configuration`
	+ `AWS::MSK::ServerlessCluster`
	+ `AWS::Maester::DocumentType`
	+ `AWS::MediaTailor::Channel`
	+ `AWS::NeptuneGraph::PrivateGraphEndpoint`
	+ `AWS::Omics::AnnotationStore`
	+ `AWS::Omics::ReferenceStore`
	+ `AWS::Omics::SequenceStore`
	+ `AWS::OpenSearchServerless::Collection`
	+ `AWS::OpsWorks::App`
	+ `AWS::OpsWorks::ElasticLoadBalancerAttachment`
	+ `AWS::OpsWorks::Instance`
	+ `AWS::OpsWorks::Layer`
	+ `AWS::OpsWorks::Stack`
	+ `AWS::OpsWorks::UserProfile`
	+ `AWS::OpsWorks::Volume`
	+ `AWS::PCAConnectorAD::Connector`
	+ `AWS::PCAConnectorAD::DirectoryRegistration`
	+ `AWS::PCAConnectorAD::Template`
	+ `AWS::PCAConnectorAD::TemplateGroupAccessControlEntry`
	+ `AWS::Panorama::PackageVersion`
	+ `AWS::QuickSight::Theme`
	+ `AWS::RDS::DBSecurityGroup`
	+ `AWS::RDS::DBSecurityGroupIngress`
	+ `AWS::Redshift::ClusterSecurityGroup`
	+ `AWS::Redshift::ClusterSecurityGroupIngress`
	+ `AWS::RefactorSpaces::Environment`
	+ `AWS::RefactorSpaces::Route`
	+ `AWS::RefactorSpaces::Service`
	+ `AWS::RoboMaker::RobotApplication`
	+ `AWS::RoboMaker::SimulationApplication`
	+ `AWS::Route53::RecordSet`
	+ `AWS::Route53::RecordSetGroup`
	+ `AWS::SDB::Domain`
	+ `AWS::SageMaker::InferenceComponen`
	+ `AWS::ServiceCatalog::PortfolioPrincipalAssociation`
	+ `AWS::ServiceCatalog::PortfolioProductAssociation`
	+ `AWS::ServiceCatalog::PortfolioShare`
	+ `AWS::ServiceCatalog::TagOptionAssociation`
	+ `AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation`
	+ `AWS::ServiceCatalogAppRegistry::ResourceAssociation`
	+ `AWS::StepFunctions::StateMachineVersion`
	+ `AWS::Synthetics::Canary`
	+ `AWS::VoiceID::Domain`
	+ `AWS::WAF::ByteMatchSet`
	+ `AWS::WAF::IPSet`
	+ `AWS::WAF::Rule`
	+ `AWS::WAF::SizeConstraintSet`
	+ `AWS::WAF::SqlInjectionMatchSet`
	+ `AWS::WAF::WebACL`
	+ `AWS::WAF::XssMatchSet`
	+ `AWS::WAFv2::IPSet`
	+ `AWS::WAFv2::RegexPatternSet`
	+ `AWS::WAFv2::RuleGroup`
	+ `AWS::WAFv2::WebACL`
	+ `AWS::WorkSpaces::Workspace`
