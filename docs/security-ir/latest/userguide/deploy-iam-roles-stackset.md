# Deploy the IAM roles with a StackSet

## Prerequisites for deploying IAM roles with a StackSet

- You must have an active AWS Security Incident Response membership.
- You must have trusted access enabled between AWS CloudFormation StackSets and AWS Organizations. For more information, see [Enable trusted access with AWS Organizations](../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.md") in the _AWS CloudFormation User Guide_.
- You must have permissions to create StackSets in the AWS Organizations management account or a delegated administrator account.

## Create a StackSet for Security Incident Response containment roles

Use the following procedure to create a StackSet with service-managed permissions that deploys the containment roles to your organization accounts.

1. Sign in to the AWS Management Console and open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. In the navigation pane, choose **StackSets**, and then choose **Create StackSet**.
3. For **Permissions**, choose **Service-managed permissions**.
4. For **Template source**, choose **Upload a template file**. Upload the template file you chose from [Select a CloudFormation template for your containment roles](cloudformation-templates.md "cloudformation-templates.md").
5. Enter a StackSet name (for example, `SIR-Containment-Roles`) and optionally add a description.
6. On the **Configure StackSet options** page, keep the default settings and choose **Next**.
7. For **Deployment targets**, choose **Deploy to organization**. This helps make sure that the roles deploy to all current and future accounts in your organization.
8. For **Specify regions**, select one AWS Region. Because IAM roles are global resources, you only need to deploy the StackSet to a single Region.
9. Review the settings and select the acknowledgment check box that confirms AWS CloudFormation might create IAM resources with custom names. Choose **Submit**.

After the StackSet deployment completes, the containment roles are available in all accounts within your organization. For more information about managing StackSets, see [Update a StackSet with service-managed permissions](../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-update.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-update.md") in the _AWS CloudFormation User Guide_.
