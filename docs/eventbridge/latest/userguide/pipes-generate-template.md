# Generating an CloudFormation template from EventBridge Pipes

AWS CloudFormation enables you to configure and manage your AWS resources across accounts and
regions in a centralized and repeatable manner by treating infrastructure as code.
CloudFormation does this by letting you create _templates_, which define the
resources you want to provision and manage.

EventBridge enables you to generate templates from the existing pipes in your account, as an aid
to help you jumpstart developing CloudFormation templates. You can select a single pipe, or
multiple pipes to include in the template. You can then use these templates as the basis for
[creating
stacks](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") of resources under CloudFormation management.

For more information on CloudFormation, see [_The CloudFormation User
Guide_.](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")

For event buses, you can generate CloudFormation templates from [event buses](eb-generate-event-bus-template.md "eb-generate-event-bus-template.md") and [event bus rules](rule-generate-template.md "rule-generate-template.md").

## Resources included in EventBridge Pipe

templates

When EventBridge generates the CloudFormation template, it creates an
[AWS::Pipes::Pipe](../../../AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.md") resource for each selected pipe. In addition, EventBridge includes the following resources under the described conditions:

- [AWS::Events::ApiDestination](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.md")

If your pipes include API destinations, either as enrichments or targets, EventBridge
includes them in the CloudFormation template as AWS::Events::ApiDestination
resources.

- [AWS::Events::EventBus](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.md")

If your pipes includes an event bus as a target, EventBridge includes it in the
CloudFormation template as an AWS::Events::EventBus resource.

- [AWS::IAM::Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md")

If you had EventBridge create a new execution role when you [configured the pipe](eb-pipes-create.md#pipes-configure-pipe-settings "eb-pipes-create.md#pipes-configure-pipe-settings"), you can choose to have EventBridge
include that role in the template as an AWS::IAM::Role resource. EventBridge does not include roles you create. (In either case, the `RoleArn`
property of the AWS::Pipes::Pipe resource contains the ARN of the role.)

## Considerations when using

CloudFormation templates generated from EventBridge Pipes

Consider the following factors when using a CloudFormation template you generated from
EventBridge:

- EventBridge does not include any passwords in the generate template.

You can edit the template to include [template parameters](../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md") that enable users to specify passwords or other
sensitive information when using the template to create or update a CloudFormation
stack.

In addition, users can use Secrets Manager to create a secret in the desired region and
then edit the generated template to employ [dynamic parameters](../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md#dynamic-references-secretsmanager "../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md#dynamic-references-secretsmanager").

- Targets in the generated template remain exactly as they were specified in the
  original pipe. This can lead to cross-region issues if you do not appropriately
  edit the template before using it to create stacks in other regions.

Additionally, the generated template does not create the downstream targets
automatically.

## Generating a CloudFormation template from

EventBridge Pipes

To generate a CloudFormation template from one or more pipes using the EventBridge console, do
the following:

###### To generate an CloudFormation template from one or more pipes

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Pipes**.
3. Under **Pipes**, choose one or more pipes you want to include
   in the generated CloudFormation template.

For a single pipe, you can also choose the pipe name to display the pipe's
details page. 4. Choose **CloudFormation Template**, and then choose which
format you want EventBridge to generate the template in: **JSON** or
**YAML**.

EventBridge displays the template, generated in the selected format. 5. If you had EventBridge create a new execution role for any of the
selected pipes, and you want EventBridge to include those roles in the
template, choose **Include IAM roles created by console
on your behalf**. 6. EventBridge gives you the option of downloading the template file, or
copying the template to the clipboard.

    * To download the template file, choose
     **Download**.
    * To copy the template to the clipboard, choose
     **Copy**.

7. To exit the template, choose **Cancel**.
