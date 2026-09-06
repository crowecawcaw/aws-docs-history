

# Create AWS Entity Resolution resources with AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

AWS Entity Resolution is integrated with AWS CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want (such as AWS::EntityResolution::MatchingWorkflow, AWS::EntityResolution::SchemaMapping, AWS::EntityResolution:IdMappingWorkflow, AWS::EntityResolution::IdNamespace and AWS::EntityResolution::PolicyStatement), and CloudFormation provisions and configures those resources for you. 

When you use CloudFormation, you can reuse your template to set up your AWS Entity Resolution resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

## AWS Entity Resolution and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for AWS Entity Resolution and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

AWS Entity Resolution supports creating AWS::EntityResolution::MatchingWorkflow, AWS::EntityResolution::SchemaMapping, AWS::EntityResolution:IdMappingWorkflow, AWS::EntityResolution::IdNamespace and AWS::EntityResolution::PolicyStatement in CloudFormation. For more information, including examples of JSON and YAML templates for AWS::EntityResolution::MatchingWorkflow, AWS::EntityResolution::SchemaMapping, AWS::EntityResolution:IdMappingWorkflow, AWS::EntityResolution::IdNamespace and AWS::EntityResolution::PolicyStatement, see the [AWS Entity Resolution resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EntityResolution.html) in the *AWS CloudFormation User Guide*.

The following templates are available:
+ *Matching workflow*

  Create a `MatchingWorkflow` object, which stores the configuration of the data processing job to be run.

  For more information, see the following topics:

  [AWS::EntityResolution::MatchingWorkflow](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html) in the *CloudFormation User Guide*

  [CreateMatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateMatchingWorkflow.html) in the *AWS Entity Resolution API Reference*
+ *Schema mapping*

  Create a schema mapping, which defines the schema of the input customer records table.

  For more information, see the following topics:

  [AWS::EntityResolution::SchemaMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html) in the *CloudFormation User Guide*

  [CreateSchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateSchemaMapping.html) in the *AWS Entity Resolution API Reference*
+ *ID mapping workflow*

  Create an `IdMappingWorkflow` object, which stores the configuration of the data processing job to run.

  For more information, see the following topics:

  [AWS::EntityResolution::IdMappingWorkflow](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html) in the *CloudFormation User Guide*

  [CreateIdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateIdMappingWorkflow.html) in the *AWS Entity Resolution API Reference*
+ *ID namespace*

  Create an `IdNamespace` object, which stores the metadata explaining the dataset and how to use it.

  For more information, see the following topics:

  [AWS::EntityResolution::IdNamespace](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idnamespace.html) in the *CloudFormation User Guide*

  [CreateIdNamespace](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateIdNamespace.html) in the *AWS Entity Resolution API Reference*
+ *PolicyStatement*

  Create an `PolicyStatement` object.

  For more information, see the following topics:

  [AWS::EntityResolution::PolicyStatement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-policystatement.html) in the *CloudFormation User Guide*

  [AddPolicyStatement](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_AddPolicyStatement.html) in the *AWS Entity Resolution API Reference*

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)