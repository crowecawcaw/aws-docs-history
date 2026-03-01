# Automating AWS services with Amazon Q Developer Console-to-Code

## What is Console-to-Code?

Console-to-Code is a feature of Amazon Q Developer that can help you write code to automate your use of other
AWS services. Console-to-Code records your console actions, then uses generative AI to suggest the
equivalent AWS CLI commands and code in your preferred language and format.

### Tiers of service

Since Console-to-Code is a part of Amazon Q Developer, your use of it is subject to Amazon Q Developer’s tiers of
service.

- At the Free tier, there is no fixed monthly limit to the number of times you can
  record your console actions and generate CLI commands based on those actions. However,
  there is a limit to how many times per month you can generate code to use with the
  AWS CDK or AWS CloudFormation based on your recorded actions.

To access the Free tier, sign into the AWS Management Console. After you reach the monthly code
generations limit, you must authenticate to the Pro tier in order to generate more
code.

- At the Pro tier, there is no fixed monthly limit to the number of times you can
  generate code for the AWS CDK or CloudFormation.

To access the Pro tier, you must be a user registered with IAM Identity Center, and your IAM Identity Center
identity must be subscribed to Amazon Q Developer Pro. For more information, see [Authenticating to your Amazon Q Developer Pro subscription](q-on-aws.md#qdevpro-authentication "q-on-aws.md#qdevpro-authentication") or
contact your AWS administrator.

For more information on pricing tiers, visit the [Amazon Q Developer pricing page](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/").

###### Note

When you record an action, you will still be charged for the action itself, if
applicable. For example, if you record yourself provisioning an Amazon EC2 instance, then you
will still be charged for the instance. There is no additional cost for recording the
action.

### Supported code formats

Console-to-Code can currently generate infrastructure-as-code (IaC) in the following languages and formats:

- CDK Java
- CDK Python
- CDK TypeScript
- CloudFormation JSON
- CloudFormation YAML

## Where can you use Console-to-Code?

### Using Console-to-Code across multiple services

Console-to-Code works across multiple services, saving its own state for as long as your browser tab
is open.

For example, you may record your actions during a complete setup of a web server:

- In the Amazon VPC console, you provision two subnets (one public and one private),
  security groups, NACLs, a custom routing table, and an internet gateway.
- In the Amazon EC2 console, you provision an Amazon EC2 instance and place it in the public
  subnet.
- In the Amazon RDS console, you provision an Amazon RDS DB instance and place it in the private
  subnet.

Even if you perform your actions in different parts of the console and they use different
AWS services, Console-to-Code can include them in a single recording.

### AWS services that support Console-to-Code

Currently, Console-to-Code is available to record your actions when using the AWS management
console with the following services:

- Amazon DynamoDB
- AWS IoT
- Amazon Cognito
- Amazon EC2
- Amazon VPC
- Amazon RDS

## Granting permissions to use Console-to-Code

To use Console-to-Code, the following permissions are required:

- `q:GenerateCodeFromCommands` to use Console-to-Code. For an example IAM policy that
  grants the needed permission, see [Allow users to generate code from CLI commands with Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-console-to-code "id-based-policy-examples-users.md#id-based-policy-examples-allow-console-to-code").
- Permissions to take the actions that you're going to record.

## Using Console-to-Code

Using Console-to-Code consists of three steps.

### Step 1: Start recording

To start recording with Console-to-Code, use the following procedure.

1. Go to the console of one of the integrated services (Amazon VPC, Amazon RDS, or Amazon EC2).
2. On the right edge of the browser window, choose the Console-to-Code icon:
   ![The console-to-code icon.](images/c2c-icon.png)
3. In the Console-to-Code side panel, choose **Start recording**.

### Step 2: Take actions

In the consoles of any of the integrated services, proceed to take any actions that you want
to record.

The Console-to-Code side panel retains its own state. You can move between the consoles of the
integrated services, creating one recording that involves actions for multiple
services.

The Console-to-Code side panel will retain your actions until your Console-to-Code session ends. The session
will end when you close the browser tab, or when your AWS Management Console session ends, whichever comes
first.

When you have finished taking actions that you want to convert to code, choose
**Stop** from the top of the Console-to-Code panel.

### Step 3: Gather CLI commands and generating code

You can follow either Step 3a or Step 3b.

#### Step 3a: Gather CLI commands

To use Console-to-Code to generate CLI commands based on your actions, use the following
procedure.

1. In the Console-to-Code panel, review your recorded actions.

You can filter the recorded actions using the dropdown, search box, or filter
widget at the top of the Console-to-Code panel. 2. Do one of the following:

    * To copy an individual CLI command, choose the copy button to the left of
     the command.
    * To run an individual CLI command in AWS CloudShell, choose the CloudShell
     icon
    ![The console-to-code icon.](images/cloudshell-icon.png)
     to the left of the command. This opens CloudShell
     and populates it with the CLI command ready for you to execute.
    * To view or run a set of CLI commands, select the commands and choose
     either **Copy CLI** to copy all selected commands, or
     **Run CLI** to open CloudShell and populate it with
     all commands.

To learn more about the AWS CLI, see [What is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the
_AWS Command Line Interface User Guide._

#### Step 3b: Generate code

1. In the Console-to-Code panel, review your recorded actions. You can filter the recorded
   actions using the dropdown, search box, or filter widget at the top of the Console-to-Code
   panel.
2. Select the actions that you want to convert into code. Only the actions with
   checked boxes will be used in the following steps.
3. Indicate the type of code that you want to generate. From the reverse dropdown
   menu at the lower right of the Console-to-Code panel, select the language and (if
   applicable) format of the code to be generated.
4. Choose **Generate chosen language**.

The generated code will appear, along with the equivalent CLI commands.
