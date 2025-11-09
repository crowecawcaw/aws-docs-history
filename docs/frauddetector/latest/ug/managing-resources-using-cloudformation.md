Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Manage Amazon Fraud Detector resources using AWS CloudFormation

Amazon Fraud Detector is integrated with AWS CloudFormation, a service that helps you to model and set up your Amazon Fraud Detector resources so that you
can spend less time creating and managing your resources and infrastructure. You create a template that describes all the Amazon Fraud Detector resources
that you want (such as Detector, Variables, EntityType, EventType, Outcome, and Label), and AWS CloudFormation provisions and configures those resources for you. You can reuse the template to provision and
configure the resources consistently and repeatedly in multiple AWS accounts and Regions.

There is no additional charge for using AWS CloudFormation.

## Creating Amazon Fraud Detector templates

To provision and configure resources for Amazon Fraud Detector and related services, you must
understand [AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates
are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your AWS CloudFormation stacks. If you're unfamiliar
with JSON or YAML, you can use AWS CloudFormation Designer to help you get started with AWS CloudFormation templates. For more information, see [What is AWS CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

You can also create, update, and delete your Amazon Fraud Detector resources using AWS CloudFormation templates. For more information,
including examples of JSON and YAML templates for your resources, see the [Amazon Fraud Detector resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_FraudDetector.md "../../../AWSCloudFormation/latest/UserGuide/AWS_FraudDetector.md") in the _AWS CloudFormation User Guide_.

If you are already using CloudFormation, there is no need to manage additional IAM policies or CloudTrail logging.

## Managing Amazon Fraud Detector stacks

You can create, update, and delete your Amazon Fraud Detector stacks through the CloudFormation console or through the AWS CLI.

To create a stack, you must have a template that describes what resources AWS CloudFormation will include in your stack.
You can also bring Amazon Fraud Detector resources that you have already created into CloudFormation management by [importing them](../../../AWSCloudFormation/latest/UserGuide/resource-import.md "../../../AWSCloudFormation/latest/UserGuide/resource-import.md") into a new or existing stack.

For detailed instructions for managing your stacks, see the _AWS CloudFormation User Guide_ to learn how to
[create](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md"),
[update](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-get-template.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-get-template.md"), and
[delete](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md") stacks.

### Organizing your Amazon Fraud Detector stacks

The way you organize your AWS CloudFormation stacks is entirely up to you. It is generally a best practice is to organize stacks by lifecycle and
ownership. This means grouping resources by how frequently they change or by teams that are responsible for updating them.

You can choose to organize your stacks by creating a stack for each detector and its detection logic (for example, rules, variables, etc.). If you are
using other services, you should consider whether you want to stack together Amazon Fraud Detector resources with resources from other services. For example, you could create
a stack that includes Kinesis resources that help gather data and Amazon Fraud Detector resources that process the data. This can be an effective way to
ensure that all of your fraud team’s products are working together.

## Understanding Amazon Fraud Detector CloudFormation parameters

In addition to the standard parameters that are available in all CloudFormation templates, Amazon Fraud Detector introduces two additional parameters that will help
you manage deployment behavior. If you do not include one or both of these parameters, CloudFormation will use the default value shown below.

| Parameter             | Values                                                                                                                                                                                                                                       | Default Value |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| DetectorVersionStatus | **ACTIVE:\*<br>• Set the new/updated detector version to Active status<br>**DRAFT:\*<br>• Set the new/updated detector version to Draft status                                                                                               | DRAFT         |
| Inline                | **TRUE:\*<br>• Allow CloudFormation to create/update/delete<br>the resource when creating/updating/deleting the stack.<br>**FALSE:\*<br>• Allow CloudFormation to validate that the<br>object exists but not make any changes to the object. | TRUE          |

## Sample AWS CloudFormation template for Amazon Fraud Detector resources

The following is a sample AWS CloudFormation YAML template for managing a detector and associated detector versions.

```
# Simple Detector resource containing inline Rule, EventType, Variable, EntityType and Label resource definitions
Resources:
  TestDetectorLogicalId:
    Type: AWS::FraudDetector::Detector
    Properties:
      DetectorId: "sample_cfn_created_detector"
      DetectorVersionStatus: "DRAFT"
      Description: "A detector defined and created in a CloudFormation stack!"

      Rules:
        - RuleId: "over_threshold_investigate"
          Description: "Automatically sends transactions of $10000 or more to an investigation queue"
          DetectorId: "sample_cfn_created_detector"
          Expression: "$amount >= 10000"
          Language: "DETECTORPL"
          Outcomes:
            - Name: "investigate"
              Inline: true
        - RuleId: "under_threshold_approve"
          Description: "Automatically approves transactions of less than $10000"
          DetectorId: "sample_cfn_created_detector"
          Expression: "$amount <10000"
          Language: "DETECTORPL"
          Outcomes:
            - Name: "approve"
              Inline: true
      EventType:
        Inline: "true"
        Name: "online_transaction"
        EventVariables:
          - Name: "amount"
            DataSource: 'EVENT'
            DataType: 'FLOAT'
            DefaultValue: '0'
            VariableType: "PRICE"
            Inline: 'true'
        EntityTypes:
          - Name: "customer"
            Inline: 'true'
        Labels:
          - Name: "legitimate"
            Inline: 'true'
          - Name: "fraudulent"
            Inline: 'true'


```

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command
  Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
