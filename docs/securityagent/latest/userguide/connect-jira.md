

# Connect AWS Security Agent to Jira
<a name="connect-jira"></a>

Connect AWS Security Agent to Jira Cloud, Atlassian’s issue tracking service, so you can track security findings as Jira issues. After you connect a Jira project to an Agent Space, you can create a Jira issue for a finding, and AWS Security Agent can add comments and links to that issue as the finding progresses. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md) to understand how a registration is reused across Agent Spaces.

When you connect Jira, you can do the following in the projects you choose:
+  **Create issues** – Create a Jira issue for a security finding, so your team can track and resolve it with your usual Jira workflow.
+  **Comment on issues** – Add comments to a linked issue, such as the result when you revalidate a finding.

To connect Jira to AWS Security Agent, install the AWS Security Agent Forge app on your Atlassian site and complete the authorization flow.

**Supported Jira version**  
AWS Security Agent supports Jira Cloud only.

## Reviewing prerequisites
<a name="_reviewing_prerequisites"></a>

Connect Jira to AWS Security Agent when you want to create and track security findings as Jira issues. Before you begin, ensure you have:
+ A Jira Cloud site with admin access
+ An Atlassian account with site administrator privileges
+ Permissions to configure integrations in the AWS Security Agent Management Console

**One site per AWS account**  
You can associate one Atlassian site with only one AWS account per Region. If you need to connect the same Jira site to AWS Security Agent in a different AWS account within the same Region, you must first remove the existing integration.

## Registering a Jira connection
<a name="_registering_a_jira_connection"></a>

A Jira connection links AWS Security Agent to your Jira Cloud site so you can create and comment on Jira issues for your security findings. Register a connection before you connect projects to an Agent Space.

### Part 1: Installing and authorizing the Forge app
<a name="_part_1_installing_and_authorizing_the_forge_app"></a>

1. On the AWS Security Agent Management Console, navigate to **Integrations**.

1. On the **Integrations** page, choose **Add integration**.

1. Choose **Jira**, then choose **Next**.

1. Install the AWS Security Agent Forge app in your Atlassian site, following the on-screen instructions.

1. After installation, copy the installation ID. For information about finding your installation ID, see [Find your Atlassian installation ID](find-atlassian-installation-id.md).

1. In the **Jira site URL** field, enter your site URL, for example `https://example.atlassian.net`.

1. In the **Installation ID** field, paste the installation ID you copied from Jira.

1. Choose **Authorize**.

   Atlassian redirects you to authorize AWS Security Agent to access your Jira site. After authorization completes, you return to the console.

### Part 2: Registering the connection
<a name="_part_2_registering_the_connection"></a>

1. In the **Register details** section, enter a **Registration name** for this connection. Valid characters are letters, numbers, periods, underscores, and hyphens.

1. In the **Register details** section, choose **Connect**.

## Connecting projects to an Agent Space
<a name="_connecting_projects_to_an_agent_space"></a>

After you register the Jira integration, connect the Jira projects you want to use to an Agent Space. Connecting projects lets AWS Security Agent create and comment on Jira issues directly from findings, so your team can track and resolve security issues without leaving Jira. For each connected project, you choose whether AWS Security Agent can create issues, comment on issues, or both.

1. Open the Agent Space where you want to use Jira.

1. Start the Jira connection.

1. Select the projects you want to connect.

1. For each project, select the actions you want to allow:
   +  **Create issues** – With this permission, AWS Security Agent can create issues in the project.
   +  **Comment on issues** – With this permission, AWS Security Agent can comment on issues in the project.

1. Choose **Save** to apply your selection.

After you connect a project, you can create Jira issues for findings from the AWS Security Agent web application. For more information about creating Jira issues for findings, see [Create Jira issues for findings](export-findings-to-issue-tracker.md).

## Troubleshooting Jira integration
<a name="_troubleshooting_jira_integration"></a>

Jira integration issues can occur during registration, when the Forge app is uninstalled, or when a site is already connected to another AWS account. The following guidance helps you diagnose and resolve these common problems.

### Resolving an incomplete registration
<a name="_resolving_an_incomplete_registration"></a>

If the registration process is interrupted, the Forge app can be installed on your Atlassian site but not registered in the AWS Management Console.

#### Resolution
<a name="_resolution"></a>

To resolve this issue, do the following:
+ Return to the AWS Security Agent console and restart the integration process.
+ Don’t reinstall the Forge app, because it remains installed.

### Resolving an uninstalled Forge app
<a name="_resolving_an_uninstalled_forge_app"></a>

If you uninstall the AWS Security Agent Forge app from your Atlassian site while the integration still exists in AWS Security Agent, the integration can no longer create or comment on issues. Use the following guidance to restore it.

#### Symptoms
<a name="_symptoms"></a>

You might encounter the following symptoms:
+ The integration appears in the AWS Management Console, but it cannot create or comment on issues.
+ You receive errors when you create a Jira issue for a finding.

#### Resolution
<a name="_resolution_2"></a>

To resolve this issue, do the following:
+ Reinstall the Forge app from the Atlassian Marketplace.
+ If the issue persists, remove the integration in the AWS Management Console and re-register it.

### Resolving a site already connected to another AWS account
<a name="_resolving_a_site_already_connected_to_another_aws_account"></a>

#### Resolution
<a name="_resolution_3"></a>

To resolve this issue, do the following:
+ You can connect one Atlassian site to only one AWS account per Region.
+ Identify which AWS account has the existing integration and use that account, or remove the existing integration first.

## Next steps
<a name="_next_steps"></a>

After you connect Jira to AWS Security Agent, you can do the following:
+ Connect the Jira projects you want to use to an Agent Space.
+ Create Jira issues for findings from a penetration test or code review. For more information, see [Create Jira issues for findings](export-findings-to-issue-tracker.md).

This integration uses an Atlassian Forge app, and Atlassian Forge pricing applies. For more information about Forge platform pricing, see [Forge platform pricing](https://developer.atlassian.com/platform/forge/forge-platform-pricing/) on the Atlassian website.