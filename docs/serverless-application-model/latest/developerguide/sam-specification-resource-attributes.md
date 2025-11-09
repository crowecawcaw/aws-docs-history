# Resource attributes supported by AWS SAM

Resource attributes are attributes that you can add to AWS SAM and AWS CloudFormation resources to
control additional behaviors and relationships. For more information about resource
attributes, see [Resource
Attribute Reference](../../../AWSCloudFormation/latest/UserGuide/aws-product-attribute-reference.md "../../../AWSCloudFormation/latest/UserGuide/aws-product-attribute-reference.md") in the _AWS CloudFormation User Guide_.

AWS SAM support a subset of resource attributes that are defined by AWS CloudFormation. Of the supported
resource attributes, some are copied to only the base generated AWS CloudFormation resource of the
corresponding AWS SAM resource, and some are copied to all generated AWS CloudFormation resources resulting
from the corresponding AWS SAM resource. For more information about AWS CloudFormation resources generated
from corresponding AWS SAM resources, see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

The following table summarizes resource attribute support by AWS SAM, subject to the [Exceptions](#sam-specification-resource-attributes-exceptions "#sam-specification-resource-attributes-exceptions") listed below.

| Resource attributes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Destination generated resource(s)                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[DependsOn](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.md "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.md")**<br>**[Metadata](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-metadata.md "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-metadata.md")**1, 2                                                                                                                                                                                                                           | Base AWS CloudFormation generated resource only. For information about the mapping between AWS SAM resources and base AWS CloudFormation resources, see<br>[Generated AWS CloudFormation resource<br>scenarios](sam-specification-generated-resources.md#sam-specification-generated-resources-scenarios "sam-specification-generated-resources.md#sam-specification-generated-resources-scenarios").                |
| **[Condition](../../../AWSCloudFormation/latest/UserGuide/conditions-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/conditions-section-structure.md")**<br>**[DeletionPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.md")**<br>**[UpdateReplacePolicy](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.md")** | All generated AWS CloudFormation resources from the corresponding AWS SAM<br>resource. For information about scenarios for generated AWS CloudFormation resources, see<br>[Generated AWS CloudFormation resource<br>scenarios](sam-specification-generated-resources.md#sam-specification-generated-resources-scenarios "sam-specification-generated-resources.md#sam-specification-generated-resources-scenarios"). |

**Notes:**

1. For more information about using the `Metadata` resource attribute
   with the `AWS::Serverless::Function` resource type, see [Building Lambda functions with custom runtimes in AWS SAM](building-custom-runtimes.md "building-custom-runtimes.md").
2. For more information about using the `Metadata` resource attribute
   with the `AWS::Serverless::LayerVersion` resource type, see [Building Lambda layers in AWS SAM](building-layers.md "building-layers.md").

## Exceptions

There are a number of exceptions to the resource attribute rules described
previously:

- For `AWS::Lambda::LayerVersion`, the AWS SAM-only custom field
  `RetentionPolicy` sets the `DeletionPolicy` for the
  generated AWS CloudFormation resources. This has a higher precedence than
  `DeletionPolicy` itself. If neither is set, then by default
  `DeletionPolicy` is set to `Retain`.
- For `AWS::Lambda::Version`, if `DeletionPolicy` is not
  specified, the default is `Retain`.
- For the scenario where `DeploymentPreferences` is specified for a
  serverless function, resource attributes are not copied to the following
  generated AWS CloudFormation resources:
  - `AWS::CodeDeploy::Application`
  - `AWS::CodeDeploy::DeploymentGroup`
  - The `AWS::IAM::Role` named
    `CodeDeployServiceRole` that is created for this
    scenario

- If your AWS SAM template contains multiple functions with API event sources that
  are implicitly created, then the functions will share the generated
  `AWS::ApiGateway::RestApi` resource. In this scenario, if the
  functions have different resource attributes, then for the generated
  `AWS::ApiGateway::RestApi` resource, AWS SAM copies the resource
  attributes according to the following prioritized lists:
  - `UpdateReplacePolicy`:
    1. `Retain`
    2. `Snapshot`
    3. `Delete`

  - `DeletionPolicy`:
    1. `Retain`
    2. `Delete`
