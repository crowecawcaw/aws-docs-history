# Create an Agent Space

Create Agent Spaces to secure applications or projects in your organization. Each Agent Space provides a workspace for security assessments, findings, and configurations specific to that application or project and can be accessed by multiple users.

This procedure assumes you have already completed the initial AWS Security Agent setup. If you haven’t set up AWS Security Agent yet, see [Set up AWS Security Agent](setup-security-agent.md "setup-security-agent.md").

## Overview

### Understanding Agent Spaces

An Agent Space is a dedicated workspace for securing a specific application or project. It contains all security reviews, optionally connected code repositories, penetration test configurations, results, and findings for that application.

Agent Spaces help you organize security work by keeping each application’s security assessments separate, allowing teams to focus on their specific application. We recommend creating one Agent Space per application or project to maintain clear boundaries.

For a comprehensive explanation of Agent Spaces and how they fit into your organization’s security structure, see [Understand the resource hierarchy and lifecycle](understand-lifecycle.md "understand-lifecycle.md").

### What’s included in an Agent Space

Each Agent Space contains:

- Optionally connected code repositories associated with the application or project
- Previous design reviews for the application or project
- Penetration testing configurations and boundaries specific to the application
- Penetration testing test results and security findings

## Create an Agent Space

Create a new Agent Space for an application or project you want to secure.

1. In the AWS Security Agent console, navigate to the **Agent Spaces** page.
2. Click **Create Agent Space**.
3. In the **Agent Space name** field, enter a name for your Agent Space.

###### Note

The Agent Space name is displayed to users in the web application and helps identify which application or project this space represents. 4. (Optional) In the **Description** field, provide a description that assists in distinguishing the Agent Space purpose.

###### Tip

The description helps distinguish the Agent Space’s purpose. We recommend describing the specific application or project this Agent Space will secure, such as "Customer portal web application" or "Payment processing microservices" or "Internal analytics platform." 5. Click **Create**.

###### Note

AWS Security Agent will create your Agent Space. You can now configure capabilities and connect resources specific to this application.

## Next steps

After creating your Agent Space:

- Connect GitHub repositories for code review and penetration testing context
- Enable code review capability for connected repositories (see [Enable code review capability for a GitHub repository](enable-code-review.md "enable-code-review.md"))
- Configure penetration testing capabilities including domain verification
- **(If using IAM Identity Center)** Assign users to this Agent Space under the Web App section of the Agent Space page. (see [Grant users access to the AWS Security Agent web app](grant-user-access.md "grant-user-access.md"))
- **(If using IAM-only access)** Users with console access can launch the web application through the admin access link for this Agent Space
