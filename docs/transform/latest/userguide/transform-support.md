

# AWS support for AWS Transform
<a name="transform-support"></a>

AWS Transform enables you to create and manage AWS Support cases through the chat if you encounter issues during your transformation jobs. Your cases are automatically enriched with job context and routed to the appropriate support team. If you are an active Countdown Premium customer, your designated engineer will reach out to manage issue resolution. Learn more in [AWS Countdown Premium](https://aws.amazon.com/premiumsupport/aws-countdown/). Otherwise, your case will be investigated by the AWS Transform support team in their support queue. 

## Prerequisites
<a name="support-prerequisites"></a>

Before you can use support case management, you need:
+ An active AWS Support plan - Business, Enterprise On-Ramp, or Enterprise
+ An existing AWS Transform application

## Enabling Support Case Management
<a name="enable-support-management"></a>

1. Open the AWS Transform console.

1. In the navigation pane, choose **Settings**.

1. Under **Support**, choose **Enable Support case management**.

1. Choose **Save changes**.

AWS Transform uses a service-linked role (SLR) to create and manage support cases on your behalf. No additional IAM permissions are required.

## Creating a Support Case
<a name="create-support-case"></a>

To create a support case, use the chat interface:

1. Ask to create a support case. For example:
   + "Create a support case for my failed transformation job"
   + "I need help with job errors, create a case"

1. The chat prompts you for required information:
   + A brief description of your issue
   + A detailed description

1. Confirm the case creation when prompted.

The case is automatically populated with context from your transformation job, including:
+ Job ID and status
+ Job metadata
+ Job execution logs (work logs)
+ Job plan

The case is automatically assigned based on your job type and issue category.

## Viewing Support Cases
<a name="view-support-cases"></a>

To view your support cases, prompt the chat:
+ "List my support cases"
+ "Show me open support cases"
+ "What's the status of my cases?"

The chat will display:
+ Case ID
+ Subject
+ Status, such as Open, Pending, Resolved, or Closed
+ Last updated date
+ Associated job ID

To view details of a specific case:
+ "Show me details for case [case-id]"
+ "What's the latest update on case [case-id]?"

## Adding Communications to a Case
<a name="add-case-communications"></a>

To add a message to an existing case:

1. Ask the chat: "Add a message to case [case-id]"

1. Provide your message when prompted.

1. The chat will confirm the message was added.

You'll receive notifications when AWS Support responds to your case.

## Resolving a Case
<a name="resolve-support-case"></a>

To resolve a support case:

1. Ask the chat: "Resolve case [case-id]"

1. Confirm the resolution when prompted.

**Note**  
You can only resolve cases that have been addressed by AWS Support.

## Disabling Support Case Management
<a name="disable-support-management"></a>

1. Open the AWS Transform console.

1. In the navigation pane, choose **Settings**.

1. Under **Support**, choose **Disable Support case management**.

1. Choose **Save changes**.

**Note**  
Disabling Support case management removes the chat-based case management interface but does not close existing cases. You can still access your cases through the AWS Support Center.