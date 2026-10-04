

# Connect AWS Security Agent to Azure DevOps repositories
<a name="connect-azure-devops"></a>

Connect your AWS Security Agent to Azure DevOps repositories to enable code review, threat modeling, penetration testing, and automated remediation capabilities. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md) to understand how a registration is reused across Agent Spaces and shared across capabilities.

Azure DevOps integration serves multiple purposes:
+  **Continuum for code review** – Automatically analyze the code changes in each pull request against your organizational security requirements, and run on-demand full-repository scans
+  **Continuum for threat modeling** – Provide application understanding by analyzing source code, data flows, and architecture
+  **Continuum for penetration testing context** – Provide application understanding for penetration testing
+  **Continuum for automated remediation** – Submit pull requests with fixes for vulnerabilities discovered during security assessments

AWS Security Agent authenticates to Azure DevOps as a Microsoft Entra service principal (a non-human identity managed in your Microsoft Entra tenant). You authorize the AWS Security Agent application, which appears as **AWS Continuum for Azure DevOps** in Microsoft Entra and Azure DevOps, in your Microsoft Entra tenant, add its service principal to your Azure DevOps organization, and grant it the Azure DevOps permissions the agent needs.

**Note**  
AWS Security Agent supports Git repositories in Azure DevOps only. Team Foundation Version Control (TFVC) repositories are not supported.

## How Azure DevOps integration works
<a name="_how_azure_devops_integration_works"></a>

 **Pull request analysis** happens within Azure DevOps. After you register the integration, connect repositories, and enable code review comments in the AWS Management Console, AWS Security Agent installs a service hook (webhook) that notifies it of new pull requests. The agent scans the changes in each pull request (a differential scan of just the changed code) and posts findings as pull request comments.

You create and run **full code reviews**—which scan a repository’s entire codebase—in the AWS Security Agent web application, not in Azure DevOps.

AWS Security Agent installs one set of service hooks per Azure DevOps project. An integration supports code review comments and remediation on repositories in at most 50 projects. For all quotas, see [Service Quotas](quotas.md).

 **Penetration testing** and **threat modeling** are initiated within the AWS Security Agent web application. Users specify target domains and select connected repositories to provide application context.

**Note**  
Automated remediation is not available for public Azure DevOps repositories to avoid disclosing vulnerabilities before they are fixed.

## Prerequisites
<a name="connect-azure-devops-prerequisites"></a>

Before you begin, ensure you have:
+ An Azure DevOps organization with Microsoft Entra ID enabled. A service principal can only be added to an organization that is connected to Microsoft Entra ID.
+  **Project Administrator** or **Project Collection Administrator** permission in Azure DevOps, to add the service principal and grant its permissions.
+ The Azure CLI with the Azure DevOps extension installed (`az extension add --name azure-devops`), signed in as an administrator. The service hook (webhook) permission in the following procedure cannot be granted from the Azure DevOps UI and must be set with the CLI.
+ Permissions to configure integrations in the AWS Security Agent Management Console.
+ If your Microsoft Entra policies require admin consent, a Microsoft Entra administrator who can approve the AWS Continuum for Azure DevOps application in your tenant.

**Important**  
If your Azure DevOps organization or its network restricts access with an IP allow list, add the AWS Security Agent IP addresses for your AWS Region. Do this before you register the integration. For the IP addresses, see [AWS Security Agent IP addresses](about-integrations.md#agent-ip-addresses).

## Register an Azure DevOps connection
<a name="_register_an_azure_devops_connection"></a>

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Choose **Add integration**.

1. Select **Azure DevOps**, then choose **Next**.

1. Choose **Authorize**.

   The console redirects you to Microsoft, where you grant admin consent for the AWS Continuum for Azure DevOps application in your Microsoft Entra tenant. After you approve the consent request, you return to the console.

1. In the **Organization** field, enter your Azure DevOps organization name, for example `ado-organization`.

1. In the **Registration name** field, enter a descriptive name for this connection. Valid characters are letters, numbers, periods, underscores, and hyphens.

1. Choose **Connect**.

   You return to the **Integrations** page, where the new connection appears with its registration name.

**Note**  
Registering the connection authorizes AWS Security Agent in your Microsoft Entra tenant. Before the agent can read repositories or install pull request webhooks, you must also add its service principal to your organization and grant it permissions, as described in the following section.

## Grant AWS Security Agent access in Azure DevOps
<a name="_grant_aws_security_agent_access_in_azure_devops"></a>

After you register the connection, complete the following steps in Azure DevOps so the service principal can access your repositories and install pull request webhooks.

### Add the service principal to your organization
<a name="_add_the_service_principal_to_your_organization"></a>

A service principal is added to your Azure DevOps organization in the same way as a user. You add it to the organization only once. To analyze repositories in more projects later, assign the same service principal to those projects—you do not repeat the authorization or the organization-level Service Hooks grant, which already apply across the organization.

1. In Azure DevOps, go to **Organization settings**, then **Users**, then choose **Add users**.

1. In the **Users** field, search for **AWS Continuum for Azure DevOps**, or paste its **Application (client) ID**, and select it.

1. Set the **Access level** to **Basic**, add it to each project whose repositories the agent will analyze, then choose **Add**. This grants the service principal the repository read and write access the agent needs for those projects.

**Note**  
Adding a service principal to an organization requires the organization to be connected to Microsoft Entra ID. For more information, see [Prerequisites](#connect-azure-devops-prerequisites).

### Grant AWS Continuum for Azure DevOps Service Hooks permissions
<a name="connect-azure-devops-service-hooks"></a>

To install the pull request webhook, the service principal needs **View and Edit Subscriptions** on Service Hooks. This permission cannot be granted from the Azure DevOps UI and must be set with the Azure CLI.

Grant it at the organization level. The Service Hooks security namespace is hierarchical, so an organization-level grant is inherited by every current and future project, and you do not need to repeat it as projects are added.

1. Get the service principal descriptor:

   ```
   az rest --method get \
     --resource 499b84ac-1321-427f-aa17-267ca6975798 \
     --url "https://vssps.dev.azure.com/ORG_NAME/_apis/graph/serviceprincipals?api-version=7.1-preview.1" \
     --query "value[?contains(displayName, 'AWS Continuum for Azure DevOps')].{descriptor:descriptor, displayName:displayName}" \
     -o table
   ```

    `499b84ac-1321-427f-aa17-267ca6975798` is the fixed Azure DevOps resource ID. It is used only to mint the token. Copy the `descriptor` value (it looks like `aadsp.<base64>`) for the AWS Continuum for Azure DevOps service principal.

1. Grant View and Edit Subscriptions for the organization:

   ```
   az devops security permission update \
     --org "https://dev.azure.com/ORG_NAME" \
     --namespace-id "cb594ebe-87dd-4fc9-ac2c-6a10a4c92046" \
     --subject "SP_DESCRIPTOR" \
     --token "PublisherSecurity" \
     --allow-bit 3 \
     --merge true
   ```

   Replace `SP_DESCRIPTOR` with the descriptor from the previous step. The namespace ID identifies the Service Hooks security namespace. `--allow-bit 3` grants View and Edit Subscriptions. `--merge true` preserves the service principal’s other permissions.

**Note**  
To scope the grant to a single project instead of the whole organization, get the project ID and append it to the token as `PublisherSecurity/PROJECT_ID`:  

```
az devops project show \
  --org "https://dev.azure.com/ORG_NAME" \
  --project "PROJECT_NAME" \
  --query id \
  -o tsv
```
Repeat the grant for every project the agent analyzes.

**Important**  
Grant **View and Edit Subscriptions** (`--allow-bit 3`), not Edit Subscriptions alone (`--allow-bit 2`). Without View, the webhook install fails a consumer availability check even though Edit is present. Without this permission, the integration registers successfully but AWS Continuum for Azure DevOps cannot install the pull request webhook, so pull requests are never reviewed.

## Troubleshoot Azure DevOps integration
<a name="_troubleshoot_azure_devops_integration"></a>

### Pull requests are not reviewed
<a name="_pull_requests_are_not_reviewed"></a>

#### Symptoms
<a name="_symptoms"></a>
+ The integration is registered and repositories are connected, but new pull requests are never analyzed and no comments are posted.

#### Resolution
<a name="_resolution"></a>
+ The pull request webhook was not installed because the service principal lacks the Service Hooks permission. Grant **View and Edit Subscriptions** (`--allow-bit 3`) on `PublisherSecurity` for the organization, as described in [Grant AWS Continuum for Azure DevOps Service Hooks permissions](#connect-azure-devops-service-hooks). Edit alone (`--allow-bit 2`) is not sufficient.

  To re-trigger project webhook creation, remove and add the repositories from that project.

### Update rejected for exceeding the project limit
<a name="_update_rejected_for_exceeding_the_project_limit"></a>

#### Symptoms
<a name="_symptoms_2"></a>
+ Saving repository settings fails with "Code review is supported on repositories across at most 50 Azure DevOps projects per integration".

#### Resolution
<a name="_resolution_2"></a>
+ The update would enable code review comments or automated remediation in more than 50 projects on this integration, counted across all Agent Spaces. Disable these capabilities on repositories in projects you no longer need, then save again.

### Can’t sign in with a personal account
<a name="_cant_sign_in_with_a_personal_account"></a>

#### Symptoms
<a name="_symptoms_3"></a>
+ Choosing **Authorize** shows "You can’t sign in here with a personal account. Use your work or school account instead."

#### Resolution
<a name="_resolution_3"></a>
+ Authorizing AWS Security Agent grants tenant-wide admin consent, which requires a Microsoft Entra work or school account. A personal Microsoft account can’t grant it, and neither can a service principal. Sign in with an account in the Microsoft Entra tenant that your Azure DevOps organization is connected to, then start the registration again.

### Your organization lacks a service principal for Azure DevOps
<a name="_your_organization_lacks_a_service_principal_for_azure_devops"></a>

#### Symptoms
<a name="_symptoms_4"></a>
+ Authorization fails with an error containing `AADSTS650052`, which names service `499b84ac-1321-427f-aa17-267ca6975798` (Azure DevOps).

#### Resolution
<a name="_resolution_4"></a>
+ Your Microsoft Entra tenant has no service principal for Azure DevOps. This happens in tenants that have never used Azure DevOps, because the service principal is created the first time the tenant uses it. Sign in to [dev.azure.com](https://dev.azure.com) once with an account in the tenant, then start the registration again.
+ To confirm the service principal exists, in the Azure portal go to **Microsoft Entra ID**, then **Enterprise applications**, and filter **Application type** by **All applications**. The default filter hides Microsoft applications, so **Azure DevOps** does not appear under the **Enterprise Applications** filter even when it is present.

### Consent required
<a name="_consent_required"></a>

#### Symptoms
<a name="_symptoms_5"></a>
+ Authorization fails or **AWS Continuum for Azure DevOps** does not appear when you search in **Add users**.

#### Resolution
<a name="_resolution_5"></a>
+ Your Microsoft Entra policies require an administrator to approve the AWS Continuum for Azure DevOps application. Ask a Microsoft Entra administrator to approve the consent request, then register the connection and add the service principal again.

## Next steps
<a name="_next_steps"></a>

After connecting Azure DevOps to AWS Security Agent:
+ Navigate to the Agent Space where you want to use these repositories
+ Choose **Enable code review** or **Setup penetration testing** to connect specific repositories to your Agent Space (see [Enable code review](enable-code-review-scan.md) and [Enable penetration test](enable-penetration-test.md))
+ Enable **Code review comments** to have AWS Security Agent analyze each pull request and post findings in Azure DevOps (see [Review code security findings in pull requests](review-code-findings-github.md))
+ Enable **Code remediation** to allow AWS Security Agent to submit pull requests with vulnerability fixes (see [Enable users to start remediation of penetration test and code review findings](enable-remediate-findings.md))
+ Create threat models from connected repositories in the web application (see [Enable threat modeling](enable-threat-model.md))