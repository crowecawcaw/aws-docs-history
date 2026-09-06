

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Manage Amazon Fraud Detector resources using AWS CloudFormation
<a name="managing-resources-using-cloudformation"></a>

Amazon Fraud Detector is integrated with AWS CloudFormation, a service that helps you to model and set up your Amazon Fraud Detector resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the Amazon Fraud Detector resources that you want (such as Detector, Variables, EntityType, EventType, Outcome, and Label), and CloudFormation provisions and configures those resources for you. You can reuse the template to provision and configure the resources consistently and repeatedly in multiple AWS accounts and Regions.

There is no additional charge for using AWS CloudFormation.

## Creating Amazon Fraud Detector templates
<a name="working-with-templates"></a>

To provision and configure resources for Amazon Fraud Detector and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

You can also create, update, and delete your Amazon Fraud Detector resources using CloudFormation templates. For more information, including examples of JSON and YAML templates for your resources, see the [Amazon Fraud Detector resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FraudDetector.html) in the *AWS CloudFormation User Guide*.

If you are already using CloudFormation, there is no need to manage additional IAM policies or CloudTrail logging.

## Managing Amazon Fraud Detector stacks
<a name="working-with-stacks"></a>

You can create, update, and delete your Amazon Fraud Detector stacks through the CloudFormation console or through the AWS CLI.

To create a stack, you must have a template that describes what resources AWS CloudFormation will include in your stack. You can also bring Amazon Fraud Detector resources that you have already created into CloudFormation management by [importing them](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html) into a new or existing stack.

For detailed instructions for managing your stacks, see the *AWS CloudFormation User Guide* to learn how to [create](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html), [update](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-get-template.html), and [delete](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) stacks. 

### Organizing your Amazon Fraud Detector stacks
<a name="organize-your-stacks"></a>

The way you organize your AWS CloudFormation stacks is entirely up to you. It is generally a best practice is to organize stacks by lifecycle and ownership. This means grouping resources by how frequently they change or by teams that are responsible for updating them. 

You can choose to organize your stacks by creating a stack for each detector and its detection logic (for example, rules, variables, etc.). If you are using other services, you should consider whether you want to stack together Amazon Fraud Detector resources with resources from other services. For example, you could create a stack that includes Kinesis resources that help gather data and Amazon Fraud Detector resources that process the data. This can be an effective way to ensure that all of your fraud team’s products are working together.

## Understanding Amazon Fraud Detector CloudFormation parameters
<a name="understanding-afd-cfn-parameters"></a>

In addition to the standard parameters that are available in all CloudFormation templates, Amazon Fraud Detector introduces two additional parameters that will help you manage deployment behavior. If you do not include one or both of these parameters, CloudFormation will use the default value shown below.


| Parameter | Values | Default Value | 
| --- | --- | --- | 
| DetectorVersionStatus | **ACTIVE:** Set the new/updated detector version to Active status<br />**DRAFT:** Set the new/updated detector version to Draft status | DRAFT | 
| Inline | **TRUE:** Allow CloudFormation to create/update/delete the resource when creating/updating/deleting the stack.<br />**FALSE:** Allow CloudFormation to validate that the object exists but not make any changes to the object. | TRUE | 

## Sample CloudFormation template for Amazon Fraud Detector resources
<a name="sample-afd-cfn-template"></a>

The following is a sample CloudFormation YAML template for managing a detector and associated detector versions.

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

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)