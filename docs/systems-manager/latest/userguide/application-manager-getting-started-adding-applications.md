# Adding

applications and container clusters to Application Manager

Application Manager is a component of AWS Systems Manager. In Application Manager, an
_application_ is a logical group of AWS resources that you want
to operate as a unit. This logical group can represent different versions of an
application, ownership boundaries for operators, or developer environments, to name a
few.

The first time you open Application Manager, the **What Application Manager can do for
you** page displays. When you choose **Get started**,
Application Manager automatically imports metadata about your resources that were created in other
AWS services or Systems Manager tools. Application Manager then displays those resources in a list grouped
by predefined categories.

For **Applications**, the list includes the following:

- AWS CloudFormation stacks
- Custom applications
- AWS Launch Wizard applications
- AppRegistry applications
- AWS SAP Enterprise Workload applications
- Amazon ECS clusters
- Amazon EKS clusters
  After import is complete, you can view operations information for an application or a
  specific resource in these predefined categories. Or, if you want to provide more
  context about a collection of resources, you can manually create an application in
  Application Manager. You can then add resources or groups of resources into that application.
  After you create an application in Application Manager, you can view operations information about
  your resource in the context of an application.

## Creating an application in

Application Manager

Use the following procedure to create an application in Application Manager and add
resources to that application.

###### To create an application in Application Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Application Manager**.
3. Choose choose **Create application**.
4. Choose an option from the drop-down list and complete the fields in the
   page that appears.
