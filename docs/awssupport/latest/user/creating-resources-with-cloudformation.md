# Creating AWS Support App in Slack resources

with AWS CloudFormation

AWS Support App in Slack is integrated with AWS CloudFormation, a service that helps you to model and set up
your AWS resources so that you can spend less time creating and managing your resources
and infrastructure. You create a template that describes all the AWS resources that you
want (such as your AccountAlias and SlackChannelConfiguration), and CloudFormation provisions and configures those resources for
you.

When you use CloudFormation, you can reuse your template to set up your AWS Support App resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

## AWS Support App and CloudFormation templates

To provision and configure resources for AWS Support App and related services, you must
understand [CloudFormation
templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates are formatted text files in JSON or YAML. These templates
describe the resources that you want to provision in your CloudFormation stacks. If you're
unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with
CloudFormation templates. For more information, see [What is CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the
_AWS CloudFormation User Guide_.

AWS Support App supports creating your AccountAlias and SlackChannelConfiguration
in CloudFormation. For more information, including examples of JSON and YAML
templates for the AccountAlias and SlackChannelConfiguration resources, see the [AWS Support App resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_SupportApp.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SupportApp.md") in the
_AWS CloudFormation User Guide_.

## Create Slack

configuration resources for your organization

You can use CloudFormation templates to create the resources that you need for the
AWS Support App. If you're the management account for your organization, you can use the
templates to create these resources for your member accounts in AWS Organizations.

For example, you might use a template to create the same Slack workspace configuration
for all accounts in the organization, but then use separate templates to create
different Slack channel configurations for specific AWS accounts or organizational
units (OUs). You can also use a template to create a Slack workspace configuration so
that member accounts can then configure the Slack channels that they want for their
AWS accounts.

You can choose whether to use CloudFormation templates or not. If you don't use
CloudFormation templates, you can complete the following manual steps instead:

- Create the AWS Support App resources in the AWS Support Center Console.
- Create a support case with AWS Support to [authorize multiple accounts](authorize-slack-workspace.md#authorize-multiple-accounts "authorize-slack-workspace.md#authorize-multiple-accounts") to
  use the AWS Support App.
- Call the [RegisterSlackWorkspaceForOrganization](../../../supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.md "../../../supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.md") API operation
  to register a Slack workspace for your account. The CloudFormation stack calls this
  API operation for you.

Follow these procedures to upload the CloudFormation template to your organization. You
can use the example templates from the [AWS Support App resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_SupportApp.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SupportApp.md") page.

The templates tell CloudFormation to create the following resources:

- A [Slack channel configuration](../../../AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.md").
- A [Slack workspace configuration](../../../AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.md").
- An [IAM
  role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md") with the `AWSSupportSlackAppCFNRole` name. The
  AWSSupportAppFullAccess AWS managed policy is
  attached.

###### Contents

- [Update your CloudFormation templates
  for Slack](creating-resources-with-cloudformation.md#update-the-templates-for-slack "creating-resources-with-cloudformation.md#update-the-templates-for-slack")
- [Create a stack for the
  management account](creating-resources-with-cloudformation.md#create-your-stack-for-slack "creating-resources-with-cloudformation.md#create-your-stack-for-slack")
- [Create a stack set for
  your organization](creating-resources-with-cloudformation.md#create-your-stackset-for-your-organization "creating-resources-with-cloudformation.md#create-your-stackset-for-your-organization")

### Update your CloudFormation templates

for Slack

To get started, use the following templates to create your stack. You must replace
the templates with valid values for your Slack workspace and channel.

###### Note

We don't recommend the use of the template to create an AccountAlias resource for your
organization. The AccountAlias resource uniquely identifies an
AWS account in the AWS Support App. Your member accounts can enter an account name in
the Support Center Console. For more information, see [Authorize a Slack workspace](authorize-slack-workspace.md "authorize-slack-workspace.md").

###### To update your CloudFormation templates for Slack

1. If you're the management account for an organization, you must manually
   authorize a Slack workspace for your account before your member accounts can
   use CloudFormation to create the resources. If you haven't already done so, see
   [Authorize a Slack workspace](authorize-slack-workspace.md "authorize-slack-workspace.md").
2. From the [AWS Support App resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_SupportApp.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SupportApp.md") page, copy the JSON or YAML
   template for the resource that you want.
3. In a text editor, paste the template into a new file.
4. In the template, specify the parameters that you want. At a minimum,
   replace the values for the following fields:
   - `TeamId` with your Slack workspace ID
   - `ChannelId` with the Slack channel ID
   - `ChannelName` with a name to identify the Slack channel
     configuration

###### Tip

To find the workspace and channel IDs, open your Slack channel in a
browser. In the URL, your workspace ID is the first identifier and the channel ID is the
second. For example, in
https://app.slack.com/client/T012ABCDEFG/C01234A5BCD,

T012ABCDEFG is the workspace ID and C01234A5BCD is the channel
ID. 5. Save the file as either a JSON or YAML file.

### Create a stack for the

management account

Next, you must create a stack for the management account in the organization. This
step calls the [RegisterSlackWorkspaceForOrganization](../../../supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.md "../../../supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.md") API operation for
you and authorizes the workspace with Slack.

###### Note

We recommend that you upload the Slack workspace configuration template that
you updated in the previous procedure for the management account. You don't need
to upload the Slack channel configuration template unless you're also
configuring the management account to use the AWS Support App.

###### To create a stack for the management account

1. Sign in to the AWS Management Console as the management account for your
   organization.
2. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. If you haven't already, in the **Region selector**,
   choose one of the following AWS Regions:
   - Europe (Frankfurt)
   - Europe (Ireland)
   - Europe (London)
   - US East (N. Virginia)
   - US East (Ohio)
   - US West (Oregon)
   - Asia Pacific (Singapore)
   - Asia Pacific (Tokyo)
   - Canada (Central)

4. Follow the procedure to create a stack. For more information, see [Creating a stack on the CloudFormation
   console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md").

After CloudFormation successfully creates the stack, you can use the same
template to create a stack set for your organization.

### Create a stack set for

your organization

Next, use the same template for the Slack workspace configuration to create a
stack set with `service-managed` permissions. You can use stack sets to
create the stack for your entire organization or specify the OUs that you want. For
more information, see [Create a stack set](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md").

This procedure also calls the [RegisterSlackWorkspaceForOrganization](../../../supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.md "../../../supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.md") API operation for
you. This API operation authorizes the workspace with Slack for the member
accounts.

###### To create a stack set for your organization

1. Sign in to the AWS Management Console as the management account for your
   organization.
2. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. If you haven't already, in the **Region selector**,
   choose the same AWS Region that you used in the previous procedure.
4. In the navigation pane, choose **StackSets**.
5. Choose **Create StackSet**.
6. On the **Choose a template** page, keep the default
   options for the following options:
   - For **Permissions**, keep
     **Service-managed permissions**.
   - For **Prerequisite - Prepare template**, keep
     **Template is ready**.

7. Under **Specify template**, choose **Upload a
   template file**, and then choose **Choose
   file**.
8. Choose the file and then choose **Next**.
9. On the **Specify StackSet details** page, enter a stack
   name such as `support-app-slack-workspace`, enter a
   description, and then choose **Next**.
10. On the **Configure StackSet options** page, keep the
    default options and then choose **Next**.
11. On the **Set deployment options** page, for **Add
    stacks to stack set**, keep the default **Deploy new
    stacks** option.
12. For **Deployment targets**, choose if you want to create
    the stack for the entire organization or specific OUs. If you choose an OU,
    enter the OU ID.
13. For **Specify regions**, enter only
    _one_ of the following AWS Regions:
    - Europe (Frankfurt)
    - Europe (Ireland)
    - Europe (London)
    - US East (N. Virginia)
    - US East (Ohio)
    - US West (Oregon)
    - Asia Pacific (Singapore)
    - Asia Pacific (Tokyo)
    - Canada (Central)

###### Notes:

    * To streamline your workflow, we recommend that you use the
     same AWS Region that you chose in step 3.
    * Choosing more than one AWS Region can cause conflicts with
     creating your stack.

14. For **Deployment options**, for **Failure
    tolerance - optional**, enter the number of accounts where the
    stacks can fail before CloudFormation stops the operation. We recommend that you
    enter the number of accounts that you want to add, minus one. For example,
    if your specified OU has 10 member accounts, enter 9. This means that even
    if CloudFormation fails the operation 9 times, at least one account will
    succeed.
15. Choose **Next**.
16. On the **Review** page, review your options, and then
    choose **Submit**. You can check the status of your stack
    on the **Stack instances** tab.
17. (Optional) Repeat this procedure to upload a template for a Slack channel
    configuration. The example template also creates the IAM role and attaches
    an AWS managed policy. This role has the required permissions to access
    other services for you. For more information, see [Managing access to the AWS Support App](support-app-permissions.md "support-app-permissions.md").

If you don't create a stack set to create the Slack channel configuration,
your member accounts can manually configure the Slack channel. For more
information, see [Configuring a Slack channel](add-your-slack-channel.md "add-your-slack-channel.md").

After CloudFormation creates the stacks, each member account can sign in to the
Support Center Console and find their configured Slack workspaces and channels. They can
then use the AWS Support App for their AWS account. See [Creating support cases in a Slack channel](create-case-in-slack.md "create-case-in-slack.md").

###### Tip

If you need to upload a new template, we recommend that you use the same
AWS Region that you specified before.

## Learn more about CloudFormation

To learn more about CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User
  Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [CloudFormation API
  Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [AWS CloudFormation Command Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")

## Create AWS Support App resources by using

Terraform

You can also use [Terraform](https://www.terraform.io/ "https://www.terraform.io/") to create
the AWS Support App resources for your AWS account. Terraform is an infrastructure-as-code
tool that you can use for your cloud applications. You can use Terraform to create
AWS Support App resources instead of deploying a CloudFormation stack to an account.

After you install Terraform, you can specify the AWS Support App resources that you want.
Terraform calls the [RegisterSlackWorkspaceForOrganization](../../../supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.md "../../../supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.md")
API operation to register a Slack workspace for you and creates your resources. You can
then sign in the Support Center Console and find your configured Slack workspaces and
channels.

###### Notes

- If you're the management account for an organization, you must manually
  authorize a Slack workspace for your account before your member accounts can
  use Terraform to create the resources. If you haven't already done so, see
  [Authorize a Slack workspace](authorize-slack-workspace.md "authorize-slack-workspace.md").
- Unlike CloudFormation stack sets, you can't use Terraform to create the
  AWS Support App resources for an OU in your organization.
- You can also find the event history for these updates from Terraform in
  AWS CloudTrail. The `eventSource` for these events will be
  `cloudcontrolapi.amazonaws.com` and
  `supportapp.amazonaws.com`. For more information, see [Logging AWS Support App in Slack API calls using
  AWS CloudTrail](logging-using-cloudtrail-support-app.md "logging-using-cloudtrail-support-app.md").

### Learn more

To learn more about Terraform, see the following topics:

- [Terraform installation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli "https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli")
- [Terraform tutorial: Build infrastructure for AWS](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/aws-build "https://developer.hashicorp.com/terraform/tutorials/aws-get-started/aws-build")
- `awscc_support_app_account_alias`
- `awscc_supportapp_slack_workspace_configuration`
- `awscc_supportapp_slack_channel_configuration`
