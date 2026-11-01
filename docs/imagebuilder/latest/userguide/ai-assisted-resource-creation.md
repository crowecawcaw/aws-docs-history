

# Create and update resources with AI - Preview
<a name="ai-assisted-resource-creation"></a>

**Preview feature**  
This feature is in preview and is subject to change.

Configuring EC2 Image Builder resources means working through many settings. The Create with AI feature in Image Builder, powered by AWS DevOps Agent, suggests values from a natural language description of the resource that you want to create or edit.

For example, describe a component that installs software, or distribution settings that copy an Amazon Machine Image (AMI) to several AWS Regions. You review and apply the suggested values, and then create or update the resource yourself.

**Topics**
+ [Prerequisites](#ai-assisted-resource-creation-prereqs)
+ [Set up Create with AI](#ai-assisted-resource-creation-setup)
+ [DevOps Agent pricing for Create with AI](#ai-assisted-resource-creation-pricing)
+ [Create a resource with AI](#ai-assisted-resource-creation-create)
+ [Update a resource with AI](#ai-assisted-resource-creation-update)
+ [What Create with AI does](#ai-assisted-resource-creation-checks)
+ [Considerations](#ai-assisted-resource-creation-considerations)

## Prerequisites
<a name="ai-assisted-resource-creation-prereqs"></a>

To use Create with AI, the IAM user or role that you use needs the following permissions:
+ `aidevops:ListAgentSpaces` – Required to discover available agent spaces.
+ `aidevops:CreateChat` – Required to start a chat with the assistant.
+ `aidevops:SendChatMessage` – Required to send messages to the assistant.
+ `aidevops:CreateAgentSpace` – Required only if you want Image Builder to create an agent space for you. You can omit this permission if you bring your own agent space.
+ Image Builder permissions – Required to create or update the resources when you apply the suggested values.

Create with AI uses the same agent space setup as the Troubleshoot feature. For more information, see [Prerequisites](devops-agent-troubleshooting.md#devops-agent-troubleshooting-prereqs) and [Set up troubleshooting](devops-agent-troubleshooting.md#devops-agent-troubleshooting-setup).

## Set up Create with AI
<a name="ai-assisted-resource-creation-setup"></a>

Create with AI requires an AWS DevOps Agent agent space. The first time that you open the assistant, choose one of the following options in the drawer:
+ **Set up for me** – Image Builder creates an agent space and configures permissions for you.
+ **Use a different agent space** – Select an agent space that you already configured.

Create with AI is available only in commercial AWS Regions. If AWS DevOps Agent isn't available in your current Region, you select a supported Region for the chat. The resources that you create stay in your current Region. For more information, see [Supported Regions for AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-supported-regions.html).

## DevOps Agent pricing for Create with AI
<a name="ai-assisted-resource-creation-pricing"></a>

Create with AI uses AWS DevOps Agent. AWS bills DevOps Agent usage separately from Image Builder, based on the time that the agent spends working on your requests, per agent-second. Creating an agent space is free. Charges appear in your AWS bill and in Cost Explorer under **AWS DevOps Agent**. For current rates, see [AWS DevOps Agent pricing](https://aws.amazon.com/devops-agent/pricing/).

## Create a resource with AI
<a name="ai-assisted-resource-creation-create"></a>

You can use Create with AI for the following resources:
+ Components
+ Image recipes
+ Container recipes
+ Image pipelines
+ Image workflows
+ Infrastructure configurations
+ Distribution settings

The following are examples of requests that you can send to the assistant:
+ Component: `Install and configure nginx on Amazon Linux 2023`
+ Image recipe: `Create an Ubuntu 22 web server image with the CloudWatch agent`
+ Distribution settings: `Distribute my AMI to us-east-1, us-west-2 and eu-west-1 with a build-dated name`

To create a resource with AI, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Open the create page for the type of resource that you want to create.

1. In the page header, choose **Create with AI**. If the drawer shows a setup step, complete it first.

1. In the **Create with AI** drawer, describe the resource that you want, and then choose **Send**. If the assistant asks a follow-up question, reply in the drawer.

1. On the **Suggested values** card, review the values, and then choose **Apply to form**.

1. In the form, review every field and edit the values as needed.

1. Submit the form as you normally do. For example, choose **Create component**.

To refine the values before or after you apply them, send another message in the drawer.

If the assistant can't produce values that pass validation, the drawer shows a warning. You can still choose **Apply to form** and fix the fields in the form.

## Update a resource with AI
<a name="ai-assisted-resource-creation-update"></a>

Use Update with AI to change several fields from one description. Update with AI doesn't change fields that you can't edit, such as the resource name.

To update a resource with AI, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Open the edit page for the resource. For versioned resources such as components and recipes, open the create new version page.

1. In the page header, choose **Update with AI**.

1. In the drawer, describe the change that you want, and then choose **Send**.

1. On the **Suggested values** card, review the values, and then choose **Apply to form**. Fields that the update removes show **Will be cleared**.

1. In the form, review every field and edit the values as needed.

1. Save or submit the form as you normally do.

## What Create with AI does
<a name="ai-assisted-resource-creation-checks"></a>

When you describe a resource, the assistant can do the following:
+ **Look up your resources** – Finds your existing images, components, and recipes to use in its suggestions.
+ **Check the suggested values** – Validates the values with a dry run before it shows them, and fixes values that Image Builder rejects. For more information about dry runs, see [Validate Image Builder resource creation with a dry run](dry-run-resources.md).
+ **Suggest dependent resources** – For recipes and pipelines, suggests new resources that they need, such as a recipe, components, an infrastructure configuration, distribution settings, or workflows. Image Builder creates these resources when you create the parent resource.

## Considerations
<a name="ai-assisted-resource-creation-considerations"></a>

Note the following when you use Create with AI:
+ You create or update the resource yourself. The AI doesn't create or modify resources.
+ AWS DevOps Agent processes your requests in the agent space in your account, in the AWS Region of that agent space.
+ Lifecycle policies aren't supported.

**Important**  
Suggested dependent resources are real resources in your account. They can incur costs when you use them in builds.

**Note**  
AI generates these suggestions. Review every value before you create or update the resource.

For more information about AWS DevOps Agent, see the [*AWS DevOps Agent User Guide*](https://docs.aws.amazon.com/devopsagent/latest/userguide/).