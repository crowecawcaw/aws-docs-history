# Connecting GitLab

GitLab integration enables AWS DevOps Agent to monitor deployments from GitLab Pipelines to inform causal investigations during incident response. This integration follows a two-step process: account-level registration of GitLab, followed by connecting specific projects to individual Agent Spaces.

## Registering GitLab (account-level)

GitLab is registered at the AWS account level and shared among all Agent Spaces in that account. Individual Agent Spaces can then choose which specific projects apply to their Agent Space.

### Step 1: Navigate to pipeline providers

1. Sign in to the AWS Management Console
2. Navigate to the AWS DevOps Agent console
3. Go to the **Capability Providers** page (accessible from the side navigation)
4. Find **GitLab** in the **Available** providers section under **Pipeline** and click **Register**

### Step 2: Configure GitLab connection

On the GitLab registration page, configure the following:

**Connection type** – Select whether you're connecting as a person or a group:

- **Personal** (default) – Your individual GitLab user account with a username and profile
- **Group** – In GitLab, you use groups to manage one or more related projects at the same time

**GitLab instance type** – Choose which type of GitLab instance you're connecting to:

- **GitLab.com** (default) – The public GitLab service
- **Publicly accessible self-hosted GitLab** – Check the **Use GitLab self hosted endpoint** box and provide the URL to your GitLab instance

###### Note

Currently, only publicly accessible GitLab instances are supported.

**Access token** – Provide a GitLab personal access token:

1. In a separate browser tab, log in to your GitLab account
2. Navigate to your user settings and select **Access Tokens**
3. Create a new personal access token with the following permissions:
   - `read_repository` – Required to access repository content
   - `read_virtual_registry` – Required to access virtual registry information
   - `read_registry` – Required to access registry information
   - `api` – Required for read and write API access
   - `self_rotate` - Required for rotating tokens. This feature is currently unsupported by AWS DevOps Agent but will be supported at a later date. Adding now prevents the need to create a new token in the future.

4. Set the token expiration to a maximum of 365 days from the current date
5. Copy the generated token
6. Return to the AWS DevOps Agent console
7. Paste the token into the "Access Token" field

### Step 3: Complete registration

**(Optional) Tags** – Add AWS tags to the GitLab registration for organizational purposes.

Click **Next** to review your configuration, then click **Submit** to complete the GitLab registration process. The system will validate your access token and establish the connection.

## Connecting projects to an Agent Space

After registering GitLab at the account level, you can connect specific projects to individual Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space
2. Go to the **Capabilities** tab
3. In the **Pipeline** section, click **Add**
4. Select **GitLab** from the list of available providers
5. Select the GitLab projects relevant to your Agent Space
6. Click **Save**

AWS DevOps Agent will monitor these projects for deployments from GitLab Pipelines to inform causal investigations.

## Managing GitLab connections

- **Updating access token** – If your access token expires or needs to be updated, you can update it in the AWS DevOps Agent console by modifying the GitLab registration at the account level.
- **Viewing connected projects** – In the AWS DevOps Agent console, select your Agent Space and go to the Capabilities tab to view connected projects in the Pipeline section.
- **Removing GitLab connection** – To disconnect GitLab projects from an Agent Space, select the connection in the Pipeline section and click **Remove**. To remove the GitLab registration completely, remove it from all Agent Spaces first, then delete the registration at the account level.
