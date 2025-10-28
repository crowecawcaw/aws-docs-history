# Generating an AWS CloudFormation template from an existing EventBridge rule

AWS CloudFormation enables you to configure and manage your AWS resources across accounts and regions in a centralized and repeatable manner by treating infrastructure as code. CloudFormation does this by letting you create _templates_, which define the resources you want to provision and manage.

EventBridge enables you to generate templates from the existing rules in your account, as
an aid to help you jumpstart developing CloudFormation templates. You can select a single
rule, or multiple rules to include in the template. You can then use these templates as the basis for [creating stacks](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") of resources under CloudFormation management.

For more information on CloudFormation see [_The AWS CloudFormation User Guide_.](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")

###### Note

EventBridge does not include [managed rules](eb-rules.md "eb-rules.md") in the
generated template.

You can also [generate a template from an existing event bus](eb-generate-event-bus-template.md "eb-generate-event-bus-template.md"), including the rules that event bus contains.

###### To generate an AWS CloudFormation template from one or more rules

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Under **Select event bus**, choose the event bus that contains the rules you want to include in the template.
4. Under **Rules**, choose the rules you want to include in the generated AWS CloudFormation template.

For a single rule, you can also choose the rule name to display the rule's details page. 5. Choose **CloudFormation Template**, and then choose which format you want EventBridge to generate the template in: **JSON** or **YAML**.

EventBridge displays the template, generated in the selected format. 6. EventBridge gives you the option of downloading the template file, or copying the template to the clipboard.

    * To download the template file, choose **Download**.
    * To copy the template to the clipboard, choose **Copy**.

7. To exit the template, choose **Cancel**.
   Once you've customized your AWS CloudFormation template as necessary for your use case, you can use it
   to [create stacks](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") in
   AWS CloudFormation.

## Considerations when

using CloudFormation templates generated from Amazon EventBridge

Consider the following factors when using a CloudFormation template you generated from EventBridge:

- EventBridge does not include any passwords in the generate template.

You can edit the template to include [template parameters](../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md") that enable users to specify passwords or other
sensitive information when using the template to create or update a CloudFormation
stack.

In addition, users can use Secrets Manager to create a secret in the desired region and then edit the generated template to employ [dynamic parameters](../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md#dynamic-references-secretsmanager "../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md#dynamic-references-secretsmanager").

- Targets in the generated template remain exactly as they were specified in the original event
  bus. This can lead to cross-region issues if you do not appropriately edit the
  template before using it to create stacks in other regions.

Additionally, the generated template does not create the downstream targets automatically.
