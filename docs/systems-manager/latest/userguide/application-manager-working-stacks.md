AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Working with AWS CloudFormation templates

and stacks in Application Manager

Application Manager, a tool in AWS Systems Manager, helps you provision and manage resources for your
applications by integrating with AWS CloudFormation. You can create, edit, and delete AWS CloudFormation
templates and stacks in Application Manager. A _stack_ is a collection of
AWS resources that you can manage as a single unit. This means you can create,
update, or delete a collection of AWS resources by using CloudFormation stacks. A
_template_ is a formatted text file in JSON or YAML that
specifies the resources you want to provision in your stacks.

Application Manager also includes a template library where you can clone, create, and store
templates. Application Manager and CloudFormation display the same information about the current
status of a stack. Templates and template updates are stored in Systems Manager until you
provision the stack, at which time the changes are also displayed in
CloudFormation.

After you create a stack in Application Manager, the **CloudFormation stacks**
page displays helpful information about it. This includes the template used to
create it, a count of [OpsItems](OpsCenter.md "OpsCenter.md") for
resources in your stack, the [stack status](../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md#cfn-console-view-stack-data-resources-status-codes "../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md#cfn-console-view-stack-data-resources-status-codes"), and [drift status](../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md").

###### About Cost Explorer

Application Manager is integrated with AWS Cost Explorer, a feature of [AWS Cost
Management](../../../account-billing/index.md "../../../account-billing/index.md"), through the **Cost** widget. After you
enable Cost Explorer in the Cost Management console, the **Cost** widget
in Application Manager shows cost data for a specific non-container application or
application component. You can use filters in the widget to view cost data
according to different time periods, granularities, and cost types in either a
bar or line chart.

You can enable this feature by choosing the **Go to AWS Cost Management
console** button. By default, the data is filtered to the past three
months. For a non-container application, if you choose the **View
all** button, Application Manager opens the **Resources** tab.
For container applications, the **View all** button opens the
AWS Cost Explorer console.

###### Note

Cost Explorer uses tags to track your application costs. If your AWS CloudFormation stack-based
application isn't configured with the `AppManagerCFNStackKey` tag
key, Cost Explorer fails to present accurate cost data in Application Manager. When the
`AppManagerCFNStackKey` tag key is not detected, you will be
prompted in the console to add the tag to your CloudFormation stack to enable
cost tracking. Adding it maps the tag key to the Amazon Resource Name (ARN) of
your stack and enables the **Cost** widget to display accurate
cost data.

###### Important

Adding the `AppManagerCFNStackKey` tag will trigger a stack update.
Any manual configurations that were performed after the stack was originally
deployed will not be reflected after the user tag is added. For more information
about resource update behaviors, see [Update behaviors of stack resources](../../../AWSCloudFormation/latest/UserGuide/ using-cfn-updating-stacks-update-behaviors.md "../../../AWSCloudFormation/latest/UserGuide/ using-cfn-updating-stacks-update-behaviors.md") in the
_AWS CloudFormation User Guide_

## Before you

begin

Use the following links to learn about CloudFormation concepts before you create,
edit, or delete CloudFormation templates and stacks by using Application Manager.

- [What is
  AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation best
  practices](../../../AWSCloudFormation/latest/UserGuide/best-practices.md "../../../AWSCloudFormation/latest/UserGuide/best-practices.md")
- [Learn
  template basics](../../../AWSCloudFormation/latest/UserGuide/gettingstarted.md "../../../AWSCloudFormation/latest/UserGuide/gettingstarted.md")
- [Working with AWS CloudFormation
  stacks](../../../AWSCloudFormation/latest/UserGuide/stacks.md "../../../AWSCloudFormation/latest/UserGuide/stacks.md")
- [Working with AWS CloudFormation
  templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md")
- [Sample
  templates](../../../AWSCloudFormation/latest/UserGuide/cfn-sample-templates.md "../../../AWSCloudFormation/latest/UserGuide/cfn-sample-templates.md")

###### Topics

- [Using Application Manager
  to manage AWS CloudFormation templates](application-manager-working-templates-overview.md "application-manager-working-templates-overview.md")
- [Using Application Manager to
  manage AWS CloudFormation stacks](application-manager-working-stacks-overview.md "application-manager-working-stacks-overview.md")
