

# Deploy the IAM roles with a StackSet
<a name="deploy-iam-roles-stackset"></a>

## Prerequisites for deploying IAM roles with a StackSet
<a name="stackset-prerequisites"></a>
+ You must have an active AWS Security Incident Response membership.
+ You must have trusted access enabled between AWS CloudFormation StackSets and AWS Organizations. For more information, see [Enable trusted access with AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html) in the *AWS CloudFormation User Guide*.
+ You must have permissions to create StackSets in the AWS Organizations management account or a delegated administrator account.

## Create a StackSet for Security Incident Response containment roles
<a name="create-stackset-procedure"></a>

Use the following procedure to create a StackSet with service-managed permissions that deploys the containment roles to your organization accounts.

1. Sign in to the AWS Management Console and open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. In the navigation pane, choose **StackSets**, and then choose **Create StackSet**.

1. For **Permissions**, choose **Service-managed permissions**.

1. For **Template source**, choose **Upload a template file**. Upload the template file you chose from [Select a CloudFormation template for your containment roles](cloudformation-templates.md).

1. Enter a StackSet name (for example, `SIR-Containment-Roles`) and optionally add a description.

1. On the **Configure StackSet options** page, keep the default settings and choose **Next**.

1. For **Deployment targets**, choose **Deploy to organization**. This helps make sure that the roles deploy to all current and future accounts in your organization.

1. For **Specify regions**, select one AWS Region. Because IAM roles are global resources, you only need to deploy the StackSet to a single Region.

1. Review the settings and select the acknowledgment check box that confirms AWS CloudFormation might create IAM resources with custom names. Choose **Submit**.

After the StackSet deployment completes, the containment roles are available in all accounts within your organization. For more information about managing StackSets, see [Update a StackSet with service-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-update.html) in the *AWS CloudFormation User Guide*.