# Create AWS Entity Resolution resources with

AWS CloudFormation

AWS Entity Resolution is integrated with AWS CloudFormation, a service that helps you to model and set up your
AWS resources so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes all the AWS resources that you want (such
as AWS::EntityResolution::MatchingWorkflow, AWS::EntityResolution::SchemaMapping, AWS::EntityResolution:IdMappingWorkflow, AWS::EntityResolution::IdNamespace and AWS::EntityResolution::PolicyStatement), and CloudFormation provisions and configures those resources for you.

When you use CloudFormation, you can reuse your template to set up your AWS Entity Resolution resources
consistently and repeatedly. Describe your resources once, and then provision the same resources
over and over in multiple AWS accounts and Regions.

## AWS Entity Resolution and CloudFormation templates

To provision and configure resources for AWS Entity Resolution and related services, you must
understand [CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md").
Templates are formatted text files in JSON or YAML. These templates describe the resources
that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you
can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see
[What is
CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

AWS Entity Resolution supports creating AWS::EntityResolution::MatchingWorkflow, AWS::EntityResolution::SchemaMapping, AWS::EntityResolution:IdMappingWorkflow, AWS::EntityResolution::IdNamespace and AWS::EntityResolution::PolicyStatement in CloudFormation. For more information, including examples
of JSON and YAML templates for AWS::EntityResolution::MatchingWorkflow, AWS::EntityResolution::SchemaMapping, AWS::EntityResolution:IdMappingWorkflow, AWS::EntityResolution::IdNamespace and AWS::EntityResolution::PolicyStatement, see the [AWS Entity Resolution resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_EntityResolution.md "../../../AWSCloudFormation/latest/UserGuide/AWS_EntityResolution.md") in the
_AWS CloudFormation User Guide_.

The following templates are available:

- _Matching workflow_

Create a `MatchingWorkflow` object, which stores the configuration of the
data processing job to be run.

For more information, see the following topics:

[AWS::EntityResolution::MatchingWorkflow](../../../AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.md") in the _CloudFormation User Guide_

[CreateMatchingWorkflow](../apireference/API_CreateMatchingWorkflow.md "../apireference/API_CreateMatchingWorkflow.md") in the _AWS Entity Resolution API
Reference_

- _Schema mapping_

Create a schema mapping, which defines the schema of the input customer records
table.

For more information, see the following topics:

[AWS::EntityResolution::SchemaMapping](../../../AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.md") in the
_CloudFormation User Guide_

[CreateSchemaMapping](../apireference/API_CreateSchemaMapping.md "../apireference/API_CreateSchemaMapping.md") in the _AWS Entity Resolution API Reference_

- _ID mapping workflow_

Create an `IdMappingWorkflow` object, which stores the configuration of the
data processing job to run.

For more information, see the following topics:

[AWS::EntityResolution::IdMappingWorkflow](../../../AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.md") in the _CloudFormation User Guide_

[CreateIdMappingWorkflow](../apireference/API_CreateIdMappingWorkflow.md "../apireference/API_CreateIdMappingWorkflow.md") in the _AWS Entity Resolution
API Reference_

- _ID namespace_

Create an `IdNamespace` object, which stores the metadata explaining the
dataset and how to use it.

For more information, see the following topics:

[AWS::EntityResolution::IdNamespace](../../../AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idnamespace.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idnamespace.md") in the _CloudFormation User Guide_

[CreateIdNamespace](../apireference/API_CreateIdNamespace.md "../apireference/API_CreateIdNamespace.md") in the _AWS Entity Resolution API
Reference_

- _PolicyStatement_

Create an `PolicyStatement` object.

For more information, see the following topics:

[AWS::EntityResolution::PolicyStatement](../../../AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-policystatement.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-policystatement.md") in the _CloudFormation User Guide_

[AddPolicyStatement](../apireference/API_AddPolicyStatement.md "../apireference/API_AddPolicyStatement.md") in the _AWS Entity Resolution API
Reference_

## Learn more about CloudFormation

To learn more about CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [CloudFormation
  API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command
  Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
