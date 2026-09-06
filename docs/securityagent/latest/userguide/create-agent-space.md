

# Create an Agent Space
<a name="create-agent-space"></a>

Create Agent Spaces to secure applications or projects in your organization. Each Agent Space provides a workspace for security assessments, findings, and configurations specific to that application or project and can be accessed by multiple users.

This procedure assumes you have already completed the initial AWS Security Agent setup. If you haven’t set up AWS Security Agent yet, see [Set up AWS Security Agent](setup-security-agent.md).

## Overview
<a name="_overview"></a>

### Understanding Agent Spaces
<a name="_understanding_agent_spaces"></a>

An Agent Space is a dedicated workspace for securing a specific application or project. It contains all security reviews, optionally connected code repositories, penetration test configurations, results, and findings for that application.

Agent Spaces help you organize security work by keeping each application’s security assessments separate, allowing teams to focus on their specific application. We recommend creating one Agent Space per application or project to maintain clear boundaries.

For a comprehensive explanation of Agent Spaces and how they fit into your organization’s security structure, see [Understand the resource hierarchy and lifecycle](understand-lifecycle.md).

### What’s included in an Agent Space
<a name="_whats_included_in_an_agent_space"></a>

Each Agent Space contains:
+ Optionally connected code repositories associated with the application or project
+ Previous design reviews for the application or project
+ Penetration testing configurations and boundaries specific to the application
+ Penetration testing test results and security findings

## Create an Agent Space
<a name="_create_an_agent_space"></a>

Create a new Agent Space for an application or project you want to secure.

1. In the AWS Security Agent console, navigate to the **Agent Spaces** page.

1. Choose **Create Agent Space**.

1. In the **Agent Space name** field, enter a name for your Agent Space.
**Note**  
The Agent Space name is displayed to users in the web application and helps identify which application or project this space represents.

1. (Optional) In the **Description** field, provide a description that assists in distinguishing the Agent Space purpose.
**Tip**  
The description helps distinguish the Agent Space’s purpose. We recommend describing the specific application or project this Agent Space will secure, such as "Customer portal web application" or "Payment processing microservices" or "Internal analytics platform."

1. Choose **Create**.
**Note**  
AWS Security Agent will create your Agent Space. You can now configure capabilities and connect resources specific to this application.

## Next steps
<a name="_next_steps"></a>

After creating your Agent Space:
+ Connect source code repositories (GitHub, GitLab, Bitbucket, or GitHub Enterprise Server) for code review and penetration testing context
+ Connect Confluence for documentation context in design reviews and penetration testing
+ Enable code review capability for connected repositories (see [Enable pull request code review for GitHub repositories](enable-code-review.md))
+ Configure penetration testing capabilities including domain verification
+  **(If using IAM Identity Center)** Assign users to this Agent Space under the **Web app** section of the Agent Space page. (see [Grant users access to the AWS Security Agent web application](grant-user-access.md))
+  **(If using IAM-only access)** Users with console access can launch the web application through the admin access link for this Agent Space