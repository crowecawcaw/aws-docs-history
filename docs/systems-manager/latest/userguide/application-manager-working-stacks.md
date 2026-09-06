

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Working with CloudFormation templates and stacks in Application Manager
<a name="application-manager-working-stacks"></a>

Application Manager helps you provision and manage resources for your applications by integrating with AWS CloudFormation. You can create, edit, and delete CloudFormation templates and stacks in Application Manager. A *stack* is a collection of AWS resources that you can manage as a single unit. This means you can create, update, or delete a collection of AWS resources by using CloudFormation stacks. A *template* is a formatted text file in JSON or YAML that specifies the resources you want to provision in your stacks. 

Application Manager also includes a template library where you can clone, create, and store templates. Application Manager and CloudFormation display the same information about the current status of a stack. Templates and template updates are stored in Systems Manager until you provision the stack, at which time the changes are also displayed in CloudFormation.

After you create a stack in Application Manager, the **CloudFormation stacks** page displays helpful information about it. This includes the template used to create it, a count of [OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) for resources in your stack, the [stack status](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.html#cfn-console-view-stack-data-resources-status-codes), and [drift status](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html).

**About Cost Explorer**  
Application Manager is integrated with AWS Cost Explorer, a feature of [AWS Cost Management](https://docs.aws.amazon.com/account-billing/index.html), through the **Cost** widget. After you enable Cost Explorer in the Cost Management console, the **Cost** widget in Application Manager shows cost data for a specific non-container application or application component. You can use filters in the widget to view cost data according to different time periods, granularities, and cost types in either a bar or line chart. 

You can enable this feature by choosing the **Go to AWS Cost Management console** button. By default, the data is filtered to the past three months. For a non-container application, if you choose the **View all** button, Application Manager opens the **Resources** tab. For container applications, the **View all** button opens the AWS Cost Explorer console.

**Note**  
Cost Explorer uses tags to track your application costs. If your CloudFormation stack-based application isn't configured with the `AppManagerCFNStackKey` tag key, Cost Explorer fails to present accurate cost data in Application Manager. When the `AppManagerCFNStackKey` tag key is not detected, you be prompted in the console to add the tag to your CloudFormation stack to enable cost tracking. Adding it maps the tag key to the Amazon Resource Name (ARN) of your stack and enables the **Cost** widget to display accurate cost data.

**Important**  
Adding the `AppManagerCFNStackKey` tag will trigger a stack update. Any manual configurations that were performed after the stack was originally deployed will not be reflected after the user tag is added. For more information about resource update behaviors, see [Update behaviors of stack resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html) in the *AWS CloudFormation User Guide* 

## Before you begin
<a name="application-manager-working-stacks-before-you-begin"></a>

Use the following links to learn about CloudFormation concepts before you create, edit, or delete CloudFormation templates and stacks by using Application Manager.
+ [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)
+ [Learn template basics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html)
+ [Working with AWS CloudFormation stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html)
+ [Working with AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html)
+ [Sample templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates.html)

**Topics**
+ [Before you begin](#application-manager-working-stacks-before-you-begin)
+ [Using Application Manager to manage CloudFormation templates](application-manager-working-templates-overview.md)
+ [Using Application Manager to manage CloudFormation stacks](application-manager-working-stacks-overview.md)