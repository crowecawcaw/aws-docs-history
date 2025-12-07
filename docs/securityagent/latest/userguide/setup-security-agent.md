# Set up AWS Security Agent

Configure AWS Security Agent for your organization by creating your first Agent Space and establishing how users will access the web application.

This initial setup enables administrators to configure security capabilities in the AWS Console and provides users with access to design review and penetration testing through the Security Agent Web Application. After this one-time setup, you can create additional Agent Spaces with a simplified process.

## Overview

### Understanding Agent Spaces

An Agent Space is a dedicated workspace for securing a specific application or project. It contains all security reviews, optionally connected GitHub repositories, penetration test configurations, results, and findings for that application.

Agent Spaces help you organize security work by keeping each application’s security assessments separate, allowing teams to focus on their specific application. We recommend creating one Agent Space per application or project to maintain clear boundaries.

Security requirements are defined at the organization level and apply across all Agent Spaces, while each Agent Space maintains its own design documents, code repositories, penetration testing configurations, penetration testing results and security findings.

### What’s included in an Agent Space

Each Agent Space contains:

- Optionally connected GitHub repositories associated with the application or project
- Previous design reviews for the application
- Penetration testing configurations and boundaries specific to the application
- Penetration testing test results and security findings

### What you’ll configure during setup

During this first-time setup, you’ll make organizational decisions that apply to all Agent Spaces:

- **Access method** - Choose how users will access the Security Agent Web Application (IAM Identity Center SSO or IAM-only access through the AWS Console)
- **Permissions** - Configure the IAM role that the web application uses to access AWS services
- **First Agent Space** - Create your initial Agent Space with a name and description

###### Note

After completing this setup, creating additional Agent Spaces is simpler - just provide a name and description. See [Create an Agent Space](create-agent-space.md "create-agent-space.md") for details on creating subsequent Agent Spaces.

## Prerequisites

Before you begin, ensure you have:

- Permissions to create and manage AWS Security Agent resources
- Understanding of your organization’s identity management requirements
- (Optional) AWS account with permissions to create IAM roles and configure IAM Identity Center (if using SSO access)
- (Optional) Existing IAM role if you want to use a custom permissions configuration

## Step 1: Create your first Agent Space

Define the basic properties of your first Agent Space that will be displayed to users in the web application.

1. On the **AWS Security Agent** console page, click **Set up Security Agent**.
2. In the **Agent Space name** field, enter a name for your Agent Space.

###### Note

The Agent Space name is displayed to users in the web application and helps identify which application or project this space represents. 3. (Optional) In the **Description** field, provide a description that assists in distinguishing the Agent Space purpose.

###### Tip

The description helps distinguish the Agent Space’s purpose. We recommend describing the specific application or project this Agent Space will secure, such as "Customer portal web application" or "Payment processing microservices" or "Internal analytics platform."

## Step 2: Choose your access method

Select how users will access the Security Agent Web Application. You’ll choose between enabling SSO access through IAM Identity Center or providing access through the AWS Console.

###### Note

If you choose IAM-only access and later want to use IAM Identity Center, you’ll need to delete your AWS Security Agent setup and complete the setup process again.

1. In the **Access method** section, select one of the following options:
   - **IAM Identity Center (SSO)** - Enable SSO access for your team through IAM Identity Center. This option is recommended for teams that need centralized user management and want users to access the web application directly without going through the AWS Console.
   - **IAM-only access** - Provide access through an admin access link in the AWS Console. This option is simpler to set up and suitable for teams that prefer console-based access or don’t require SSO capabilities.

2. If you selected **IAM Identity Center (SSO)**, continue to Step 2a below.
3. If you selected **IAM-only access**, skip to Step 3.

### Step 2a: Configure IAM Identity Center (SSO access only)

Complete these steps only if you selected IAM Identity Center (SSO) as your access method.

1. In the **Connect to IAM Identity Center** section, review the **AWS Region**.

###### Important

Your application must be configured in the same Region where you enable IAM Identity Center. The displayed Region is where your Agent Space will be created. IAM Identity Center must be enabled in US East (N. Virginia) `us-east-1`. 2. In the **IAM Identity Center** section, choose one of the following:

    * Click **Create account instance** to create a new IAM Identity Center account instance
    * If an organization instance already exists in US East (N. Virginia) `us-east-1`, AWS Security Agent will automatically connect to it


    ###### Note

    After AWS Security Agent is connected to IAM Identity Center, you can manage access by assigning users in IAM Identity Center to the application.

3. If you are connecting Active Directory or an external identity provider, review the informational alert.

###### Important

If you’re already managing users in Active Directory or another identity source and plan to connect that identity source to IAM Identity Center, cancel setup and go to the IAM Identity Center console first. Choose the identity source you want to connect before setting up AWS Security Agent. Changing identity sources later might remove existing user assignments.

## Step 3: Configure permissions (Optional)

Configure the IAM role that your Security Agent Web Application uses to access AWS services, APIs, and accounts.

1. Locate the **Permissions configuration - optional** section.
2. If the section is collapsed, click to expand it.
3. Select one of the following options:
   - **Create default role** - AWS Security Agent automatically creates a new IAM role with the necessary permissions for the web application
   - **Use another role** - Select an existing IAM role from the available options

4. Review the role description:

###### Note

A default IAM role will be created for your web application to access other AWS services, APIs, and accounts. The role will be granted permissions required for security assessment operations.

## Step 4: Complete setup

After configuring all required settings, complete the setup to create your first Agent Space and establish the Security Agent Web Application.

1. Review all configuration sections to ensure accuracy.
2. Click **Set up** at the bottom of the page.
3. AWS Security Agent will create your Agent Space, establish the web application, and configure the necessary AWS resources.

###### Note

After initial setup, you’ll have the option to configure capabilities including penetration testing boundaries, security requirements, and GitHub integration.

## Next steps

After setting up AWS Security Agent:

- Define security requirements for your organization
- Configure penetration testing capabilities including domain verification and VPC access for your Agent Space
- Connect GitHub repositories for code review and penetration testing context
- **(If using IAM Identity Center)** Assign users to the Agent Space in IAM Identity Center
- **(If using IAM-only access)** Launch the web application through the admin access link in the AWS Console
- Create additional Agent Spaces for other applications (see <>)
