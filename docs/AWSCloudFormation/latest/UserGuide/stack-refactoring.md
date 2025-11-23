# Stack refactoring

With stack refactoring, you can reorganize resources in your CloudFormation stacks while
preserving existing resource properties and data. You can move resources between stacks,
split large stacks into smaller ones, or combine multiple stacks into one.

###### Topics

- [How stack refactoring works](#stack-refactoring-overview "#stack-refactoring-overview")
- [Stack refactoring
  considerations](#stack-refactoring-considerations "#stack-refactoring-considerations")
- [Prerequisites](#stack-refactoring-prerequisites "#stack-refactoring-prerequisites")
- [Refactor stacks (console)](#stack-refactoring-console "#stack-refactoring-console")
- [Refactor stacks (AWS CLI)](#stack-refactoring-cli "#stack-refactoring-cli")
- [Resource limitations](#stack-refactoring-resource-limitations "#stack-refactoring-resource-limitations")

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
   between at least 2 stacks (using the console), and a maximum of 5 stacks (using
   the AWS CLI). Resources can be moved between nested stacks.
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
destination of the conflicting resources. 7. Execute the refactor – After confirming
the changes align with your refactoring goals, complete the stack
refactor. 8. Monitor – Track the execution status to
ensure the operation completes successfully.

## Stack refactoring

considerations

As you refactor your stacks, keep the following in mind:

- Stack refactoring is limited to reorganizing existing resources. You cannot
  create or delete resources, modify resource configurations, or change or add new
  parameters, conditions, or mappings during refactoring. To make these changes,
  update your stacks first, and then perform the stack refactor.
- You can't refactor the same resource into multiple stacks.
- You can't refactor resources that refer to pseudo parameters whose values
  differ between the source and destination stacks, such as
  `AWS::StackName`.
- CloudFormation doesn't support empty stacks. If refactoring would leave a stack
  with no resources, you must first add at least one resource to that stack before
  you run [create-stack-refactor](../../../cli/latest/reference/cloudformation/create-stack-refactor.md "../../../cli/latest/reference/cloudformation/create-stack-refactor.md"). This can be a simple resource like
  `AWS::SNS::Topic` or
  `AWS::CloudFormation::WaitCondition`. For example:

```
Resources:
  MySimpleSNSTopic:
    Type: AWS::SNS::Topic
    Properties:
      DisplayName: MySimpleTopic
```

- Stack refactor doesn't support stacks that have stack policies attached,
  regardless of what the policies allow or deny.

## Prerequisites

To refactor stacks, you must have already created the revised templates.

Use the [get-template](../../../cli/latest/reference/cloudformation/get-template.md "../../../cli/latest/reference/cloudformation/get-template.md")
command to retrieve the CloudFormation templates for the stacks that you want to
refactor.

```
aws cloudformation get-template --stack-name `Stack1`
```

When you have the templates, use the integrated development environment (IDE) of your
choice to update them to use the desired structure and resource organization.

## Refactor stacks (console)

Use the following procedure to refactor stacks using the console.

###### To refactor stacks

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region where
   your stacks are located.
3. In the navigation pane on the left, choose **Stack
   refactors**.
4. On the **Stack refactors** page, choose **Start stack
   refactor**.
5. For **Description**, provide a description to help you
   identify your stack refactor. Then, choose **Next**.
6. For Stack 1, do the following:
   1. Choose either **Update the template for an existing
      stack** or **Create new stack**.

   If you chose **Update the template for an existing
   stack**, then select an existing stack from the list. Or
   choose **Enter a stack ARN** to enter the ARN of an
   existing stack.

   If you chose **Create new stack**, for
   **Stack name**, provide a name for the new
   stack. 2. Under **Replace existing template with refactored
   template**, choose **Amazon S3 URL** or
   **Upload a template file** to upload the desired
   template for Stack 1. 3. Choose **Next**.

7. For Stack 2, do the following:
   1. Choose either **Update the template for an existing
      stack** or **Create new stack**.

   If you chose **Update the template for an existing
   stack**, then select an existing stack from the list. Or
   choose **Enter a stack ARN** to enter the ARN of an
   existing stack.

   If you chose **Create new stack**, for
   **Stack name**, provide a name for the new
   stack. 2. Under **Replace existing template with refactored
   template**, choose **Amazon S3 URL** or
   **Upload template file** to upload the desired
   template for Stack 2. 3. Choose **Next**.

8. On the **Specify logical resource ID renames** page, make
   sure CloudFormation knows how to refactor stacks by mapping any resources shown to
   their correct logical IDs. As part of the stack refactor, if any resource's
   logical IDs were changed, you need to specify how it was renamed by providing
   the source stack name, the original logical ID, the destination stack name and
   the renamed logical ID. In some instances, the CloudFormation console might
   automatically detect the resource mapping, and you can simply verify that the
   pre-filled resource mapping is correct before proceeding.
9. Choose **Next**.
10. On the **Review and execute** page, review all of your
    selections from the previous steps and confirm that everything is set up
    correctly.
11. When you are ready to refactor the stacks, choose **Execute stack
    refactor**.

## Refactor stacks (AWS CLI)

The AWS CLI commands for stack refactoring include:

- [create-stack-refactor](../../../cli/latest/reference/cloudformation/create-stack-refactor.md "../../../cli/latest/reference/cloudformation/create-stack-refactor.md") to validate and generate a preview of planned
  changes.
- [describe-stack-refactor](../../../cli/latest/reference/cloudformation/describe-stack-refactor.md "../../../cli/latest/reference/cloudformation/describe-stack-refactor.md") to retrieve the status and details of a
  stack refactoring operation.
- [execute-stack-refactor](../../../cli/latest/reference/cloudformation/execute-stack-refactor.md "../../../cli/latest/reference/cloudformation/execute-stack-refactor.md") to complete the validated stack refactoring
  operation.
- [list-stack-refactors](../../../cli/latest/reference/cloudformation/list-stack-refactors.md "../../../cli/latest/reference/cloudformation/list-stack-refactors.md") to list all stack refactoring operations in
  your account with their current status and basic information.
- [list-stack-refactor-actions](../../../cli/latest/reference/cloudformation/list-stack-refactor-actions.md "../../../cli/latest/reference/cloudformation/list-stack-refactor-actions.md") to show a preview of the specific
  actions CloudFormation will perform on each stack and resource during the refactor
  execution.

Use the following procedure to refactor a stack using the AWS CLI.

###### To refactor stacks

1. Use the [create-stack-refactor](../../../cli/latest/reference/cloudformation/create-stack-refactor.md "../../../cli/latest/reference/cloudformation/create-stack-refactor.md") command and provide the stack names and
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
the next step), use the [create-stack-refactor](../../../cli/latest/reference/cloudformation/create-stack-refactor.md "../../../cli/latest/reference/cloudformation/create-stack-refactor.md") command with the
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

2. Use the [describe-stack-refactor](../../../cli/latest/reference/cloudformation/describe-stack-refactor.md "../../../cli/latest/reference/cloudformation/describe-stack-refactor.md") command to make sure the
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

3. Use the [list-stack-refactor-actions](../../../cli/latest/reference/cloudformation/list-stack-refactor-actions.md "../../../cli/latest/reference/cloudformation/list-stack-refactor-actions.md") command to preview the specific actions
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

4. After reviewing and confirming your changes, use the [execute-stack-refactor](../../../cli/latest/reference/cloudformation/execute-stack-refactor.md "../../../cli/latest/reference/cloudformation/execute-stack-refactor.md") command to complete the stack refactoring
   operation.

```
aws cloudformation execute-stack-refactor \
  --stack-refactor-id `9c384f70-4e07-4ed7-a65d-fee5eb430841`
```

5. Use the [describe-stack-refactor](../../../cli/latest/reference/cloudformation/describe-stack-refactor.md "../../../cli/latest/reference/cloudformation/describe-stack-refactor.md") command to monitor the execution
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

- Stack refactoring only supports resource types with a
  `provisioningType` of `FULLY_MUTABLE`, which you can
  check using the [describe-type](../../../cli/latest/reference/cloudformation/describe-type.md "../../../cli/latest/reference/cloudformation/describe-type.md") command.
- CloudFormation will validate resource eligibility during refactor creation and
  report any unsupported resources in the output of the [describe-stack-refactor](../../../cli/latest/reference/cloudformation/describe-stack-refactor.md "../../../cli/latest/reference/cloudformation/describe-stack-refactor.md") command.
- The following resources aren't supported for stack refactoring:
  - `AWS::ACMPCA::Certificate`
  - `AWS::ACMPCA::CertificateAuthority`
  - `AWS::ACMPCA::CertificateAuthorityActivation`
  - `AWS::ApiGateway::BasePathMapping`
  - `AWS::ApiGateway::Method`
  - `AWS::AppConfig::ConfigurationProfile`
  - `AWS::AppConfig::Deployment`
  - `AWS::AppConfig::Environment`
  - `AWS::AppConfig::Extension`
  - `AWS::AppConfig::ExtensionAssociation`
  - `AWS::AppStream::DirectoryConfig`
  - `AWS::AppStream::StackFleetAssociation`
  - `AWS::AppStream::StackUserAssociation`
  - `AWS::AppStream::User`
  - `AWS::BackupGateway::Hypervisor`
  - `AWS::CertificateManager::Certificate`
  - `AWS::CloudFormation::CustomResource`
  - `AWS::CloudFormation::Macro`
  - `AWS::CloudFormation::WaitCondition`
  - `AWS::CloudFormation::WaitConditionHandle`
  - `AWS::CodeDeploy::DeploymentGroup`
  - `AWS::CodePipeline::CustomActionType`
  - `AWS::Cognito::UserPoolRiskConfigurationAttachment`
  - `AWS::Cognito::UserPoolUICustomizationAttachment`
  - `AWS::Cognito::UserPoolUserToGroupAttachment`
  - `AWS::Config::ConfigRule`
  - `AWS::Config::ConfigurationRecorder`
  - `AWS::Config::DeliveryChannel`
  - `AWS::DataBrew::Dataset`
  - `AWS::DataBrew::Job`
  - `AWS::DataBrew::Project`
  - `AWS::DataBrew::Recipe`
  - `AWS::DataBrew::Ruleset`
  - `AWS::DataBrew::Schedule`
  - `AWS::DataZone::DataSource`
  - `AWS::DataZone::Environment`
  - `AWS::DataZone::EnvironmentBlueprintConfiguration`
  - `AWS::DataZone::EnvironmentProfile`
  - `AWS::DataZone::Project`
  - `AWS::DataZone::SubscriptionTarget`
  - `AWS::DirectoryService::MicrosoftAD`
  - `AWS::DynamoDB::GlobalTable`
  - `AWS::EC2::LaunchTemplate`
  - `AWS::EC2::NetworkInterfacePermission`
  - `AWS::EC2::SpotFleet`
  - `AWS::EC2::VPCDHCPOptionsAssociation`
  - `AWS::EC2::VolumeAttachment`
  - `AWS::EMR::Cluster`
  - `AWS::EMR::InstanceFleetConfig`
  - `AWS::EMR::InstanceGroupConfig`
  - `AWS::ElastiCache::CacheCluster`
  - `AWS::ElastiCache::ReplicationGroup`
  - `AWS::ElastiCache::SecurityGroup`
  - `AWS::ElastiCache::SecurityGroupIngress`
  - `AWS::ElasticBeanstalk::ConfigurationTemplate`
  - `AWS::ElasticLoadBalancing::LoadBalancer`
  - `AWS::ElasticLoadBalancingV2::ListenerCertificate`
  - `AWS::Elasticsearch::Domain`
  - `AWS::FIS::ExperimentTemplate`
  - `AWS::Glue::Schema`
  - `AWS::GuardDuty::IPSet`
  - `AWS::GuardDuty::PublishingDestination`
  - `AWS::GuardDuty::ThreatIntelSet`
  - `AWS::IAM::AccessKey`
  - `AWS::IAM::UserToGroupAddition`
  - `AWS::ImageBuilder::Component`
  - `AWS::IoT::PolicyPrincipalAttachment`
  - `AWS::IoT::ThingPrincipalAttachment`
  - `AWS::IoTFleetWise::Campaign`
  - `AWS::IoTWireless::WirelessDeviceImportTask`
  - `AWS::Lambda::EventInvokeConfig`
  - `AWS::Lex::BotVersion`
  - `AWS::M2::Application`
  - `AWS::MSK::Configuration`
  - `AWS::MSK::ServerlessCluster`
  - `AWS::Maester::DocumentType`
  - `AWS::MediaTailor::Channel`
  - `AWS::NeptuneGraph::PrivateGraphEndpoint`
  - `AWS::Omics::AnnotationStore`
  - `AWS::Omics::ReferenceStore`
  - `AWS::Omics::SequenceStore`
  - `AWS::OpenSearchServerless::Collection`
  - `AWS::OpsWorks::App`
  - `AWS::OpsWorks::ElasticLoadBalancerAttachment`
  - `AWS::OpsWorks::Instance`
  - `AWS::OpsWorks::Layer`
  - `AWS::OpsWorks::Stack`
  - `AWS::OpsWorks::UserProfile`
  - `AWS::OpsWorks::Volume`
  - `AWS::PCAConnectorAD::Connector`
  - `AWS::PCAConnectorAD::DirectoryRegistration`
  - `AWS::PCAConnectorAD::Template`
  - `AWS::PCAConnectorAD::TemplateGroupAccessControlEntry`
  - `AWS::Panorama::PackageVersion`
  - `AWS::QuickSight::Theme`
  - `AWS::RDS::DBSecurityGroup`
  - `AWS::RDS::DBSecurityGroupIngress`
  - `AWS::Redshift::ClusterSecurityGroup`
  - `AWS::Redshift::ClusterSecurityGroupIngress`
  - `AWS::RefactorSpaces::Environment`
  - `AWS::RefactorSpaces::Route`
  - `AWS::RefactorSpaces::Service`
  - `AWS::RoboMaker::RobotApplication`
  - `AWS::RoboMaker::SimulationApplication`
  - `AWS::Route53::RecordSet`
  - `AWS::Route53::RecordSetGroup`
  - `AWS::SDB::Domain`
  - `AWS::SageMaker::InferenceComponen`
  - `AWS::ServiceCatalog::PortfolioPrincipalAssociation`
  - `AWS::ServiceCatalog::PortfolioProductAssociation`
  - `AWS::ServiceCatalog::PortfolioShare`
  - `AWS::ServiceCatalog::TagOptionAssociation`
  - `AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation`
  - `AWS::ServiceCatalogAppRegistry::ResourceAssociation`
  - `AWS::StepFunctions::StateMachineVersion`
  - `AWS::Synthetics::Canary`
  - `AWS::VoiceID::Domain`
  - `AWS::WAF::ByteMatchSet`
  - `AWS::WAF::IPSet`
  - `AWS::WAF::Rule`
  - `AWS::WAF::SizeConstraintSet`
  - `AWS::WAF::SqlInjectionMatchSet`
  - `AWS::WAF::WebACL`
  - `AWS::WAF::XssMatchSet`
  - `AWS::WAFv2::IPSet`
  - `AWS::WAFv2::RegexPatternSet`
  - `AWS::WAFv2::RuleGroup`
  - `AWS::WAFv2::WebACL`
  - `AWS::WorkSpaces::Workspace`
