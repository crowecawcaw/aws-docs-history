# Connecting Azure DevOps

Azure DevOps integration enables AWS DevOps Agent to access repositories and pipeline execution history in your Azure DevOps organization. The agent can correlate code changes and deployments with operational incidents to help identify potential root causes.

This integration follows a two-step process: register Azure DevOps at the AWS account level, then associate specific projects with individual Agent Spaces. Each registration corresponds to one Azure DevOps organization. To register additional organizations, repeat the registration process for each one.

## Prerequisites

Before connecting Azure DevOps, ensure you have:

- Access to the AWS DevOps Agent console
- An Azure DevOps organization with at least one project containing a repository and pipeline history
- Permissions to add users to your Azure DevOps organization
- For Admin Consent method: an account with permission to perform admin consent in Microsoft Entra ID
- For App Registration method: an Entra application with permissions to configure federated identity credentials, and [Outbound Identity Federation](../../../IAM/latest/UserGuide/id_roles_providers_enable-federation.md "../../../IAM/latest/UserGuide/id_roles_providers_enable-federation.md") enabled in your AWS account

## Registering Azure DevOps via Admin Consent

The Admin Consent method uses a consent-based flow with the AWS DevOps Agent managed application.

### Step 1: Start the registration

1. Sign in to the AWS Management Console and navigate to the AWS DevOps Agent console
2. Go to the **Capability Providers** page
3. Locate the **Azure DevOps** section and choose **Register**
4. Enter your **Azure DevOps organization name** when prompted

### Step 2: Complete Admin Consent

1. Choose to proceed - you are redirected to the Microsoft Entra admin consent page
2. Sign in with a user principal account that has permission to perform admin consent
3. Review and grant consent for the AWS DevOps Agent application

### Step 3: Complete user authorization

1. After admin consent, you are prompted for user authorization to verify your identity as a member of the authorized tenant
2. Sign in with an account belonging to the same Azure tenant
3. After authorization, you are redirected back to the AWS DevOps Agent console with a success status

### Step 4: Grant access in Azure DevOps

See [Granting access in Azure DevOps](#granting-access-in-azure-devops "#granting-access-in-azure-devops") below. Search for **AWS DevOps Agent** when adding users.

## Registering Azure DevOps via App Registration

App Registration is shared between Azure Resources and Azure DevOps. If you have already completed App Registration for Azure Resources, you can skip to [Granting access in Azure DevOps](#granting-access-in-azure-devops "#granting-access-in-azure-devops").

### Step 1: Start the ADO App Registration

1. In the AWS DevOps Agent console, go to the **Capability Providers** page
2. Locate the **Azure Cloud** section and choose **Register**
3. Select the **App Registration** method

### Step 2: Create and configure your Entra application

Follow the instructions displayed in the console to:

1. Enable Outbound Identity Federation in your AWS account (in the IAM console, go to **Account settings** → **Outbound Identity Federation**)
2. Create an Entra application in your Microsoft Entra ID, or use an existing one
3. Configure federated identity credentials on the application

### Step 3: Provide registration details

Fill in the registration form with:

- **Tenant ID** – Your Azure tenant identifier
- **Tenant Name** – A display name for the tenant
- **Client ID** – The application (client) ID of the Entra application
- **Audience** – The audience identifier for the federated credential

### Step 4: Create the IAM role

An IAM role will be automatically created when you submit the registration through the console. It permits AWS DevOps Agent to assume credentials and invoke `sts:GetWebIdentityToken`.

### Step 5: Complete the registration

1. Confirm the configuration in the AWS DevOps Agent console
2. Choose **Submit** to complete the registration

### Step 6: Grant access in Azure DevOps

See [Granting access in Azure DevOps](#granting-access-in-azure-devops "#granting-access-in-azure-devops") below. Search for the Entra application you created during App Registration when adding users.

## Granting access in Azure DevOps

After registration, grant the application access to your Azure DevOps organization. This step is the same for both the Admin Consent and App Registration methods.

1. In Azure DevOps, go to **Organization Settings** > **Users** > **Add Users**
2. Search for the application (either **AWS DevOps Agent** for Admin Consent, or your own Entra application for App Registration)
3. Set the access level to **Basic**
4. Under **Add to projects**, select the projects you want the agent to access
5. Under **Azure DevOps Groups**, select **Project Readers**
6. Choose **Add** to complete

## Associating a project with an Agent Space

After registering Azure DevOps at the account level, associate specific projects with your Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space
2. Go to the **Capabilities** tab
3. In the **Pipelines** section, choose **Add**
4. Choose the **Azure DevOps** registration that contains the project you want to use.
5. Select the project from the dropdown of available projects
6. Choose **Add** to complete the association

A single Agent Space can use projects from multiple registrations. To associate another project, from the same registration or a different one, repeat these steps.

## Managing Azure DevOps connections

- **Viewing connected projects** – In the **Capabilities** tab, the **Pipelines** section lists all connected Azure DevOps projects.
- **Removing a project** – To disconnect a project from an Agent Space, select it in the **Pipelines** section and choose **Remove**.
- **Removing the registration** – To remove the Azure DevOps registration entirely, go to the **Capability Providers** page and delete the registration. All Agent Space associations must be removed first.
