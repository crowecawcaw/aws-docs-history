

# Connect AWS Security Agent to Bitbucket repositories
<a name="connect-bitbucket"></a>

Connect your AWS Security Agent to Bitbucket Cloud repositories to enable code review, threat modeling, penetration testing, and automated remediation capabilities. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md) to understand how a registration is reused across Agent Spaces and shared across capabilities.

Bitbucket integration serves multiple purposes:
+  **Continuum for code review** - Automatically analyze the code changes in each pull request against your organizational security requirements, and run on-demand full-repository scans
+  **Continuum for threat modeling** - Provide application understanding by analyzing source code, data flows, and architecture
+  **Continuum for penetration testing context** - Provide application understanding for penetration testing
+  **Continuum for automated remediation** - Submit pull requests with fixes for vulnerabilities discovered during security assessments

Connecting Bitbucket to AWS Security Agent requires installing the AWS Security Agent Forge app on your Atlassian site and completing the OAuth authorization flow.

**Note**  
AWS Security Agent supports Bitbucket Cloud only. Bitbucket Server and Bitbucket Data Center are not supported.

## How Bitbucket integration works
<a name="_how_bitbucket_integration_works"></a>

 **Pull request analysis** happens within Bitbucket. After you install the Forge app, connect repositories, and enable code review comments in the AWS Management Console, AWS Security Agent automatically scans the changes in each new pull request (a differential scan of just the changed code) and posts findings as pull request comments.

You create and run **full code reviews** — which scan a repository’s entire codebase — in the AWS Security Agent web application, not in Bitbucket.

 **Penetration testing** and **threat modeling** are initiated within the AWS Security Agent web application. Users specify target domains and select connected repositories to provide application context.

**Note**  
Automated remediation is not available for public Bitbucket repositories to avoid disclosing vulnerabilities before they are fixed.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ A Bitbucket Cloud workspace with admin access
+ An Atlassian account with site administrator privileges
+ Permissions to configure integrations in the AWS Security Agent Management Console

**Important**  
If your Bitbucket workspace or the network in front of it restricts access with an IP allow list, add the AWS Security Agent IP addresses for your AWS Region before you register the integration. For the IP addresses, see [AWS Security Agent IP addresses](about-integrations.md#agent-ip-addresses).

**Important**  
One Atlassian site can only be associated with one AWS account per region. If you need to connect the same Bitbucket site to AWS Security Agent in a different AWS account within the same region, you must first remove the existing integration.

**Note**  
Atlassian Forge app pricing applies to this integration. For more information, see [Forge platform pricing](https://developer.atlassian.com/platform/forge/forge-platform-pricing/) in the Atlassian documentation.

## Register a Bitbucket connection
<a name="_register_a_bitbucket_connection"></a>

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Choose **Add integration**.

1. Select **Bitbucket**, then choose **Next**.

1. Install the AWS Security Agent Forge app in your Bitbucket workspace, following the on-screen instructions. After installation, copy the installation ID. See [Find your Atlassian installation ID](find-atlassian-installation-id.md).

1. In the **Installation ID** field, paste the installation ID you copied from Bitbucket.

1. In the **Bitbucket workspace** field, enter your Bitbucket workspace slug, for example `acme-corp`.

1. Choose **Authorize**.

   You are redirected to Atlassian to authorize AWS Security Agent to access your Bitbucket workspace. After authorization completes, you return to the console.

1. In the **Register details** section, enter a **Registration name** for this connection. Valid characters are letters, numbers, periods, underscores, and hyphens.

1. Choose **Connect**.
**Note**  
After you choose **Connect**, provisioning on the Atlassian side can take a few minutes. During this time, the integration reports a pending status. If you try to select repositories or enable code review before provisioning completes, you might see a message that the installation is not yet available. Wait a few minutes and try again.

## Troubleshoot Bitbucket integration
<a name="_troubleshoot_bitbucket_integration"></a>

If you encounter issues during the Bitbucket integration process, use the following guidance to resolve common problems.

### Unable to complete registration
<a name="_unable_to_complete_registration"></a>

If the registration process is interrupted (browser closed, session timeout), the Forge app may be installed on your Atlassian site but not registered in the AWS Console.

#### Resolution
<a name="_resolution"></a>
+ Return to the AWS Security Agent console and restart the integration process.
+ The Forge app remains installed and does not need to be reinstalled.

### Site already connected to another AWS account
<a name="_site_already_connected_to_another_aws_account"></a>

#### Symptoms
<a name="_symptoms"></a>
+ Error indicating the Atlassian site is already associated with another account

#### Resolution
<a name="_resolution_2"></a>
+ One Atlassian site can only be connected to one AWS account per region.
+ Identify which AWS account has the existing integration and use that account, or remove the existing integration first.

### Installation is not available
<a name="installation-not-available"></a>

#### Symptoms
<a name="_symptoms_2"></a>
+ When you select repositories or enable code review, you see a message that the Bitbucket installation is in status `PENDING_INSTALLATION`, not `AVAILABLE`.

#### Resolution
<a name="_resolution_3"></a>
+ The installation is still provisioning on the Atlassian side. Provisioning normally completes within a few minutes. Wait a few minutes, then try again.
+ If the status does not become available after several minutes, remove the integration and register it again. Before re-registering, uninstall the Forge app from your Bitbucket workspace. For instructions, see [Remove a Bitbucket integration](remove-bitbucket.md). If you re-register without uninstalling the previous Forge app, the installation can get stuck in a pending state.

## Next steps
<a name="_next_steps"></a>

After connecting Bitbucket to AWS Security Agent:
+ Navigate to the Agent Space where you want to use these repositories
+ Choose **Enable code review** or **Setup penetration testing** to connect specific repositories to your Agent Space (see [Enable code review](enable-code-review-scan.md) and [Enable penetration test](enable-penetration-test.md))
+ Enable **Code review comments** to have AWS Security Agent analyze each pull request and post findings in Bitbucket (see [Review code security findings in pull requests](review-code-findings-github.md))
+ Enable **Code remediation** to allow AWS Security Agent to submit pull requests with vulnerability fixes (see [Enable users to start remediation of penetration test and code review findings](enable-remediate-findings.md))
+ Create threat models from connected repositories in the web application (see [Enable threat modeling](enable-threat-model.md))