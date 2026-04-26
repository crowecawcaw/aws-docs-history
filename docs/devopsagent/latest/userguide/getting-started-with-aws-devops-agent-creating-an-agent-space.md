# Creating an Agent Space

An Agent Space defines the tools and infrastructure that AWS DevOps Agent has access to. This guide walks you through creating an Agent Space, configuring primary account access, and enabling the DevOps Agent Web App. See “What is an Agent Space” to learn more about the Agent Space concept.

## Creating an Agent Space

### Access the AWS DevOps Agent console

1. Sign in to the AWS Management Console
2. Navigate to the AWS DevOps Agent console

### Name the Agent Space

1. Click **Create Agent Space**

In the **Agent Space details** section, provide:

1. In the **Name** field, enter a name for your Agent Space
2. (Optional) In the **Description** field, add details about the Agent Space's purpose
3. (Optional) From the **Agent response language** dropdown, select the language the agent uses when generating responses, findings, and investigation output. Options include: Bahasa Indonesian, Chinese (Simplified/PRC), Chinese (Traditional/Taiwan), English (UK), French (France), German (Germany), Italian (Italy), Japanese (Japan), Korean (Korea), Portuguese (Brazil), Spanish (Latin America), Turkish (Turkey), Arabic (Saudi Arabia), Thai (Thailand), and Vietnamese (Vietnam). If no language is selected, the agent responds in the language of the input. This setting is also used to determine the language for AWS Support cases created through the [Ask for human support](working-with-devops-agent-autonomous-incident-response.md "working-with-devops-agent-autonomous-incident-response.md") feature.

### Configuring primary account access

In the **Give this Agent Space AWS resource access** section, you will set up an IAM role to grant the Agent Space access to the primary AWS account. The primary account is the AWS account where you create your Agent Space. AWS DevOps Agent requires an IAM role to discover and access AWS resources in this account during investigations.

Choose a role configuration method. Select one of the following options:

#### Option 1: Auto-create a new AWS DevOps Agent role (recommended)

This option automatically creates a role with appropriate permissions for AWS DevOps Agent to investigate resources in your account.

###### Note

You must have IAM permissions to create new roles to use this option.

1. Select **Auto-create a new AWS DevOps Agent role**
2. (Optional) Update the Agent Space role name to be created

#### Option 2: Assign an existing role

Use this option when another administrator has previously created a role specifically for AWS DevOps Agent.

1. Select **Assign an existing role**
2. From the dropdown menu, select an existing role that has appropriate permissions

#### Option 3: Create a new AWS DevOps Agent role using a policy template

Use this option when you need to limit the services and resources the agent can access in the primary account.

1. Select **Create a new AWS DevOps Agent role using a policy template**
2. Follow the instructions to create the new role’s trust policy and inline policy.

### Enabling the Agent Space Web App

The Web App is where personnel interact with AWS DevOps Agent for incident investigations and reviewing recommendations. See AWS DevOps Agent Console Architecture[link] to learn more. When enabled, users can access the Agent Space Web App through an IAM authentication link from the AWS Management Console.

Select one of the following options:

#### Option 1: Auto-create a new AWS DevOps Agent role (recommended)

This option automatically creates a role with appropriate permissions for accessing the DevOps Agent Web App.

###### Note

You must have IAM permissions to create new roles to use this option.

1. Select **Auto-create a new AWS DevOps Agent role**
2. Review the permissions that will be granted to the role

#### Option 2: Assign an existing role

Use this option when another administrator has previously created an operator role.

1. Select **Assign an existing role**
2. From the dropdown menu, select an existing role that has appropriate permissions

#### Option 3: Create a new AWS DevOps Agent role using a policy template

Use this option when you need to customize permissions for web app access.

1. Select **Create a new AWS DevOps Agent role using a policy template**
2. Follow the instructions to create the new role’s trust policy and inline policy.

### Adding tags (optional)

You can add AWS tags to your Agent Space during creation. Tags are key-value pairs that help you organize and identify your resources. You can add up to 50 tags per Agent Space. To add tags, expand the **Tags** section on the Create Agent Space page and click **Add new tag**.

### Complete agent space creation

Once all sections are filled out, click **Create**

## Verifying your Agent Space setup

Once configured, the **Operator access** button will appear on the Agent Space details page. Clicking it will open the Web App in a new tab and authenticate successfully.

## Next steps

After setting up your Agent Space, consider these next steps:

- Add secondary accounts if your applications span multiple AWS accounts
- Configure third-party integrations like observability tools or ticketing systems
- Set up AWS Identity Center authentication for production environments
- Explore your application resource mapping to help AWS DevOps Agent understand your infrastructure
