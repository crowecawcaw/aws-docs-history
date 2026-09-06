# Connecting GitHub

GitHub integration enables AWS DevOps Agent to access code repositories and receive deployment events during incident investigations. This integration follows a two-step process: account-level registration of GitHub, followed by connecting specific repositories to individual Agent Spaces.

AWS DevOps Agent supports GitHub.com (SaaS), GitHub Enterprise Cloud with data residency (`*.ghe.com`), and GitHub Enterprise Server (self-hosted) instances.

You can register GitHub in two ways. **App registration** installs the AWS DevOps Agent GitHub App in your account or organization. The GitHub App supports webhooks and fine-grained permissions, and we recommend it for most use cases. **Personal access token** authenticates with a token from your GitHub account. Use it for individual access when you do not need webhook-based features. For more information, see [Registering GitHub with a personal access token](#registering-github-with-a-personal-access-token "#registering-github-with-a-personal-access-token").

## Prerequisites

Before you connect GitHub, confirm that you meet the following prerequisites:

- You have access to the AWS DevOps Agent admin console.
- You have a GitHub user account or organization with admin permissions.
- For App registration, you have authorization to install GitHub Apps in your account or organization.
- For personal access token registration, you have a personal access token with the permissions described in [Creating a personal access token](#creating-a-personal-access-token "#creating-a-personal-access-token").

For GitHub Enterprise Server, also confirm the following:

- You have a GitHub Enterprise Server instance (version 3.x or later) that is accessible over HTTPS.
- You have the HTTPS URL of your GitHub Enterprise Server instance (for example, `https://github.example.com`).
- (Optional) You have a private connection, if your GitHub Enterprise Server instance is not publicly accessible.

For GitHub Enterprise Cloud with data residency, also confirm the following:

- You have a GitHub Enterprise Cloud organization with data residency enabled, hosted on your dedicated `*.ghe.com` subdomain.
- You have organization admin permissions, including permission to create and install GitHub Apps.
- You have the HTTPS URL of your data residency instance (for example, `https://octocorp.ghe.com`).

## Registering GitHub (account-level)

GitHub is registered at the AWS account level and shared among all Agent Spaces in that account. Each registration corresponds to one GitHub user, one organization, or one GitHub Enterprise Server instance.

### Step 1: Navigate to pipeline providers

1. Sign in to the AWS Management Console
2. Navigate to the AWS DevOps Agent console
3. Go to the **Capabilities** tab
4. In the **Pipeline** section, choose **Add**
5. Select **GitHub** from the list of available providers

If GitHub hasn't been registered yet, you'll be prompted to register it first.

### Step 2: Choose connection type

On the **Register GitHub account / organization** screen, under **Connection type**, choose how AWS DevOps Agent connects to GitHub:

- **App registration** (recommended) – Install the AWS DevOps Agent GitHub App in your account or organization. The GitHub App supports webhooks and fine-grained permissions. Continue with [Step 3](#step-3-configure-the-github-app-registration "#step-3-configure-the-github-app-registration").
- **Personal access token** – Authenticate with a personal access token from your GitHub account. This option provides individual access and does not support webhooks. Skip the remaining steps in this section and see [Registering GitHub with a personal access token](#registering-github-with-a-personal-access-token "#registering-github-with-a-personal-access-token").

### Step 3: Configure the GitHub App registration

Select whether you're connecting as a user or organization:

- **User** – Your personal GitHub account with a username and profile
- **Organization** – A shared GitHub account where multiple people can collaborate across many projects at once. If you select **Organization**, enter the GitHub organization name. The name must match your GitHub organization name exactly, because you must authorize and install the app on that organization in the following steps.

Select the **GitHub App permissions** for your GitHub App. The permission level determines the actions the GitHub App can perform in your repository:

- **Read & Write** (default): The GitHub App requests both read and write permissions. This enables all features. DevOps Agent can post inline pull request comments, propose fixes, and trigger workflows.
- **Read Only**: The GitHub App requests only read permissions. DevOps Agent can view code and pull requests but cannot post comments, propose fixes, or trigger workflows.

#### Verification method

Under **Verification method**, choose how AWS DevOps Agent confirms that the GitHub App is installed in the account or organization you specified:

- **Browser-based callback** (default) – After you choose **Submit**, AWS DevOps Agent redirects you to GitHub to authorize the GitHub App and, if needed, install it. Continue with [Step 4](#step-4-set-up-the-github-app "#step-4-set-up-the-github-app").
- **Verify with a personal access token** – Enter a personal access token. AWS DevOps Agent uses the token once to confirm that the GitHub App is installed in the account or organization you specified, and then discards it. The token is not stored. Registration completes when you choose **Submit**, with no redirect to GitHub.

Use **Verify with a personal access token** when the GitHub App is already installed. For example, use it when you connect the same organization from another AWS account or Region. If the GitHub App is not installed yet, register with **Browser-based callback** first.

The verification token needs the following permissions:

- For an organization, the token owner must be an organization owner. The token also needs organization read permission. For a classic token, use the `read:org` scope. For a fine-grained token, use the **Administration: Read-only** organization permission.
- For a personal account, the token needs no additional scopes.

###### Note

Verification with a personal access token is available only for GitHub.com. For GitHub Enterprise Server and GitHub Enterprise Cloud with data residency, use **Browser-based callback**.

If you are connecting to a GitHub Enterprise Server instance, choose **Use GitHub Enterprise** and enter the HTTPS URL of your instance (for example, `https://github.example.com`).

If your GitHub Enterprise Server instance is not publicly accessible, you can optionally configure a private connection to allow AWS DevOps Agent to securely reach your instance. For more information, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md").

###### Note

Do not include `/api/v3` or any trailing path in the URL — enter only the base URL.

For GitHub Enterprise Cloud with data residency, choose **Use GitHub Enterprise** and enter the HTTPS URL of your data residency instance (for example, `https://octocorp.ghe.com`).

### Step 4: Set up the GitHub App

Choose **Submit** to begin the app setup process. The next steps differ depending on whether you connect to GitHub.com, GitHub Enterprise Server, or GitHub Enterprise Cloud with data residency.

If you chose **Verify with a personal access token** in Step 3, registration completes without a redirect. Skip Step 4 and Step 5.

#### For GitHub.com

1. GitHub redirects you to sign in and authorize AWS DevOps Agent.
2. Review the authorization request and authorize AWS DevOps Agent.
3. After you authorize, AWS DevOps Agent completes the registration. If the GitHub App is not yet installed on the account or organization you specified, you continue to the installation page (see Step 5). If the app is already installed, registration completes without reinstalling it.
4. After installation, AWS DevOps Agent receives events from your connected repositories, including deployment events.

###### Note

You must authorize and install the app on the same User or Organization you specified during registration. If you authorize or install on a different account or organization, registration fails and you must restart the process, selecting the correct account or organization.

###### Note

AWS DevOps Agent uses a separate GitHub App for each permission level (Read & Write and Read Only), and each app is authorized independently. GitHub remembers an authorization until you revoke it under Settings > Applications > Authorized GitHub Apps. If you previously authorized the app at this permission level, GitHub might skip the authorization screen. If you change the permission level, GitHub prompts you to authorize the corresponding app the first time.

#### For GitHub Enterprise Server and GitHub Enterprise Cloud with data residency

GitHub Enterprise Server and GitHub Enterprise Cloud with data residency both use the GitHub App Manifest flow, which automatically sets up a new GitHub App on your instance. During setup, your browser is redirected twice: once to your instance and once back to AWS DevOps Agent.

1. AWS DevOps Agent redirects your browser to your GitHub Enterprise instance's **Create GitHub App** page.
2. The app name is pre-filled. Change the name if needed, then choose **Create GitHub App**.
3. After AWS DevOps Agent redirects your browser back, it exchanges the manifest code for app credentials.

### Step 5: Select repositories and complete installation

Skip this step if the GitHub App is already installed on your account or organization.

1. The **Install & Authorize** page for the GitHub App appears.
2. Select which repositories to allow the app to access:

   - **All repositories** – Grant access to all current and future repositories
   - **Only select repositories** – Choose specific repositories from your account or organization

3. Choose **Install & Authorize**.
4. You'll be redirected back to the AWS DevOps Agent console, where GitHub will appear as registered at the account level.

## Registering GitHub with a personal access token

A personal access token registration connects GitHub without installing the AWS DevOps Agent GitHub App. AWS DevOps Agent stores the token and uses it to authenticate GitHub API requests on your behalf. Use this option when you cannot install a GitHub App, or when you need only individual repository access without webhook-based features.

A personal access token registration supports GitHub.com, GitHub Enterprise Server, and GitHub Enterprise Cloud with data residency. For a GitHub Enterprise Server instance that is not publicly accessible, you can use a private connection.

Consider the following limitations before you choose this option:

- **No webhooks** – GitHub does not send webhook events to a personal access token registration. AWS DevOps Agent does not receive real-time events such as pull request, push, or deployment notifications. Automated release readiness code reviews and automated verification testing do not trigger for repositories connected through a personal access token registration. You can still request a release readiness code review through DevOps Agent chat or through coding agent integrations. For more information, see [Release readiness code reviews](release-management-release-readiness-code-review.md "release-management-release-readiness-code-review.md"). If you need real-time events, use App registration.
- **Repository access follows the token** – When you scope the registration to an organization, AWS DevOps Agent lists the repositories in that organization that the token can access. When you connect the token owner's personal account, AWS DevOps Agent lists only the repositories that the token owner owns. The agent can perform only the operations that the token permits.
- **No token update** – You cannot update the token of an existing GitHub registration. To replace an expired or rotated token, deregister the registration and register GitHub again with the new token. Then reconnect the repositories to your Agent Spaces.

### Creating a personal access token

Create the token in GitHub before you register. You can use a classic token or a fine-grained token.

For a classic token, select the following scopes:

- `repo` – Required to read repository contents and metadata
- `read:org` – Required when you scope the registration to an organization. AWS DevOps Agent uses it to confirm that the token owner is an active member of the organization.

For a fine-grained token, configure the following:

- If you scope the registration to an organization, set the **Resource owner** to that organization. Select the repositories that AWS DevOps Agent can access.
- Under **Repository permissions**, grant **Contents: Read-only** and **Metadata: Read-only**.
- Under **Organization permissions**, grant **Members: Read-only** when you scope the registration to an organization.

Set an expiration that fits your security policy. AWS DevOps Agent cannot renew the token. Before the token expires, create a new token, deregister the GitHub registration, and register again.

### Registering with a personal access token

1. Complete [Step 1: Navigate to pipeline providers](#step-1-navigate-to-pipeline-providers "#step-1-navigate-to-pipeline-providers").
2. On the **Register GitHub account / organization** screen, under **Connection type**, choose **Personal access token**.
3. In **Personal access token**, enter your token.
4. (Optional) Configure the following fields:

   - **GitHub organization** – Enter the name of the organization to scope the registration to. The token owner must be an active member of the organization. Leave this field blank to connect the token owner's personal GitHub account. This field is required when you enter a GitHub Enterprise Cloud with data residency URL.
   - **GitHub Enterprise URL** – Enter the HTTPS root URL of your GitHub Enterprise instance (for example, `https://github.example.com` or `https://octocorp.ghe.com`). This applies to GitHub Enterprise Server and GitHub Enterprise Cloud with data residency. Leave this field blank to connect to GitHub.com. Do not include `/api/v3` or any trailing path.
   - **Private connection** – If your GitHub Enterprise Server instance is not publicly accessible, select a private connection. For more information, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md").

5. Choose **Submit**. AWS DevOps Agent validates the token with GitHub and confirms the identity of the token owner. When you enter an organization, it also confirms that the token owner is an active member of that organization.

After registration completes, GitHub appears as registered at the account level. Connect repositories to your Agent Spaces as described in [Connecting repositories to an Agent Space](#connecting-repositories-to-an-agent-space "#connecting-repositories-to-an-agent-space").

### Troubleshooting personal access token registration

If registration with a personal access token fails, compare the error message with the following list.

- `Invalid GitHub personal access token` – The token is invalid or has expired. Create a new token and try again.
- `GitHub personal access token does not have sufficient permissions` – Add the `repo` scope to a classic token, or grant read access to the repositories that you intend to use with a fine-grained token.
- `The GitHub token's user is not a member of organization "<name>"` – Verify the organization name. Confirm that the token has the `read:org` scope (classic) or organization members read access (fine-grained).
- `membership in organization "<name>" is "<state>", not active` – The token owner has a pending invitation to the organization. Accept the invitation and try again.
- `Failed to reach GitHub` – Check the GitHub Enterprise URL and your network configuration. For a private connection, see [Troubleshooting private connections](configuring-integrations-and-knowledge-troubleshooting-private-connections.md "configuring-integrations-and-knowledge-troubleshooting-private-connections.md").
- `A GitHub service for "<owner>" is already registered with this account` – The AWS account already has a registration for this GitHub account or organization. Use the existing registration, or deregister it first.

The following errors apply to **Verify with a personal access token**:

- `The DevOps Agent GitHub App is not installed on the requested organization or account` – Register with **Browser-based callback** first to install the GitHub App, and then try again.
- `You do not have permission to install or access the DevOps Agent GitHub App on this organization` – Use a GitHub account with owner (admin) permissions on the organization.
- `GitHub App verification is only supported for github.com` – For GitHub Enterprise Server and GitHub Enterprise Cloud with data residency, use **Browser-based callback**.

## Connecting repositories to an Agent Space

After registering GitHub at the account level, you can connect specific repositories to individual Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space
2. Go to the **Capabilities** tab
3. In the **Pipeline** section, choose **Add**
4. Select **GitHub** from the list of available providers
5. Select the GitHub registration that contains the repositories you want to use
6. Select the subset of repositories relevant to this Agent Space
7. Choose **Add** to complete the connection

You can connect different sets of repositories to different Agent Spaces based on your organizational needs. A single Agent Space can use repositories from multiple registrations. To add repositories from another registration, repeat these steps.

## Configuring Code Review and Automated Testing

When you select repositories in the GitHub connection step, they are automatically added to the **Code Review and Automated Testing** section. This section configures which repositories automatically trigger a [Release readiness code reviews](release-management-release-readiness-code-review.md "release-management-release-readiness-code-review.md") and automated testing capabilities.

###### Note

Automated triggers depend on webhook events from the GitHub App. For repositories connected through a [personal access token registration](#registering-github-with-a-personal-access-token "#registering-github-with-a-personal-access-token"), automated reviews and automated testing do not run. Request a release readiness code review through DevOps Agent chat or coding agent integrations instead.

The Code Review and Automated Testing configuration includes:

- **Capabilities** — Choose code review and automated testing capabilities for each repository. The section provides two per-repository settings:

  - **Auto trigger change review** — When enabled for a repository, DevOps Agent automatically runs a [Release readiness code reviews](release-management-release-readiness-code-review.md "release-management-release-readiness-code-review.md") each time a pull request is opened or updated. Review findings appear as inline comments on the pull request. This is enabled by default for all connected repositories.
  - **Automated verification testing** — When enabled for a repository, DevOps Agent builds, runs, and tests your code changes in a managed verification environment during code reviews. This provides functional validation beyond static analysis. For more information, see [Automated verification testing](release-management-release-readiness-code-review.md "release-management-release-readiness-code-review.md"). This is enabled by default for all connected repositories.

- **Repository list** — Shows all repositories you selected during the connection step. Use the search field to filter repositories by name. Each repository has independent checkboxes for both capabilities.
- **Runtime role** (optional) — Choose the IAM role that DevOps Agent assumes to run automated capabilities on your selected repositories. This role is used when accessing internal services needed during builds, such as private package registries and artifact storage systems. We recommend using a different role from your primary agent role.

To configure automated reviews:

1. After connecting your repositories, navigate to the **Code Review and Automated Testing** section in your GitHub integration settings.
2. For each repository, enable or disable the **Auto trigger change review** capability depending on whether you want automatic pull request reviews.
3. For each repository, enable or disable the **Automated verification testing** capability depending on whether you want [automated verification testing](release-management-release-readiness-code-review.md "release-management-release-readiness-code-review.md") in a managed verification environment.
4. Optionally, select an IAM role from the **Runtime role** dropdown that DevOps Agent will assume when running automated capabilities on your selected repositories.
5. Choose **Save** to apply your configuration.

Once configured, any new pull request in a repository with **Auto trigger change review** enabled will automatically trigger a release readiness code review. If **Automated verification testing** is also enabled, the review includes functional validation in a verification environment. For more information about code reviews, see [Release readiness code reviews](release-management-release-readiness-code-review.md "release-management-release-readiness-code-review.md").

### Advanced settings: trigger filters

By default, a repository with **Auto trigger change review** enabled runs a release readiness code review on every applicable pull request event, on any target branch. Use **Advanced settings** to add trigger filters that control exactly when automated reviews run for each repository.

Each filter is a _filter group_ that combines two conditions:

- **Target branches** (required) — One or more branch names or patterns, entered as regular expressions (for example, `main` or `release/.*`). The review triggers only when the pull request's target (base) branch matches one of these patterns.
- **Trigger events** (optional) — The pull request events that trigger a review: **Pull request ready for review** or **Pull request drafted**. Leave this empty to match all applicable events.

Within a filter group, all conditions must match (AND). You can add multiple filter groups, and a review triggers when any group matches (OR).

To configure trigger filters:

1. Open the **Advanced settings** section in the connection flow. (To change filters on an existing connection, select the connection in the **Pipeline** section, choose **Edit**, and then open **Advanced settings**.)
2. Find the repository you want to configure and select the **Change review** tab.
3. Choose **Add filter group**, then define the group's conditions:

   - Under **Target branches**, enter a branch name or pattern and press Enter or choose **Add**. Repeat to add more patterns.
   - (Optional) Under **Trigger events**, select **Pull request ready for review**, **Pull request drafted**, or both. Leave it empty to match all events.

4. (Optional) Choose **Add filter group** again to express alternative conditions.
5. Choose **Save** to apply your configuration.

You can define up to 5 filter groups per repository, with up to 20 patterns per group. Each pattern must be a valid regular expression of up to 256 characters. If you don't add any filter groups, reviews trigger on all applicable events for all target branches.

## Understanding the GitHub App

The AWS DevOps Agent GitHub App:

- Requests access to your repositories — you can review the specific permissions during GitHub App installation
- Receives deployment events and other repository events
- Allows AWS DevOps Agent to correlate code changes with operational incidents
- Can be uninstalled at any time through your GitHub settings

For GitHub Enterprise Server and GitHub Enterprise Cloud with data residency, AWS DevOps Agent automatically creates the GitHub App on your instance during registration. You can manage the app's repository access or uninstall it through **Settings > Applications > Installed GitHub Apps**. To delete the app definition entirely, go to **Settings > Developer settings > GitHub Apps**.

## GitHub App permission updates

AWS DevOps Agent may request permission updates after you install the GitHub App to support new features. When this happens:

1. You will receive a notification from GitHub regarding the permission update request.
2. Review the update details to understand what new permissions are being requested.
3. Choose **Accept new permissions** to grant the updated permissions.

No changes are required in your service or application. After you accept the updated permissions, the next installation access token that AWS DevOps Agent requests from GitHub will automatically include the new permissions.

###### Note

Until you accept a permission update, AWS DevOps Agent continues to operate with the previously granted permissions. New capabilities that depend on the updated permissions will not be available until you approve the request. The app will retain its current permissions if you choose not to accept the new permissions.

### Requested permissions

The following table describes each permission the AWS DevOps Agent GitHub App requests and why it is needed.

If you selected **Read Only** during registration, the GitHub App requests read-level access only for each permission in the following table. With Read Only permissions, the GitHub App cannot perform write-level actions listed in the **Purpose** column.

| Permission                  | Access level   | Purpose                                                                                                                                               |
| --------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checks                      | Read and write | Post release readiness code review results as check runs on pull requests, allowing review status to appear directly in the GitHub UI.                |
| Workflows                   | Read and write | Read workflow definitions and trigger GitHub Actions workflows for release testing in your CI/CD pipelines.                                           |
| Actions                     | Read and write | Monitor GitHub Actions workflow runs and access run logs during incident investigations and release testing.                                          |
| Contents                    | Read and write | Read repository source code for code review analysis and dependency mapping. Write access enables the agent to propose fixes for identified issues.   |
| Pull requests               | Read and write | Read pull request details to trigger automated code reviews. Write access enables posting inline review comments with findings and recommended fixes. |
| Organization administration | Read           | Read the list of applications installed in the target organization to verify that the AWS DevOps Agent GitHub App is installed.                       |

## Managing GitHub connections

- **Updating repository access** – To change which repositories the GitHub App can access, go to your GitHub account or organization settings. For GitHub Enterprise Server or GitHub Enterprise Cloud with data residency, go to your instance settings. Then navigate to installed GitHub Apps and modify the AWS DevOps Agent app configuration.
- **Viewing connected repositories** – In the AWS DevOps Agent console, select your Agent Space and go to the Capabilities tab to view connected repositories in the Pipeline section.
- **Replacing a personal access token** – You cannot update the token of an existing GitHub registration. To replace a token, deregister the registration from the **Capability Providers** page. Then register GitHub again with the new token, and reconnect the repositories to your Agent Spaces. Revoke the old token in your GitHub settings.
- **Removing GitHub connection** – To disconnect GitHub from an Agent Space, choose the connection in the Pipeline section, then choose **Remove**. To remove the GitHub registration from your account, navigate to the **Capability Providers** page, locate your registration within the **GitHub** section, and choose **Deregister**.

To fully remove the GitHub integration, do the following:

- To uninstall the GitHub App, go to your GitHub account or organization settings.
- To reconnect, re-register GitHub in the AWS DevOps Agent console.

For GitHub Enterprise Server and GitHub Enterprise Cloud with data residency, AWS DevOps Agent creates the GitHub App on your instance during registration. To clean up the app entirely, do both of the following:

- **Uninstall the app** – Go to **Settings > Applications > Installed GitHub Apps**, choose **Configure** on the app, then uninstall it.
- **Delete the app** – Go to **Settings > Developer settings > GitHub Apps**, choose the app, go to the **Advanced** tab, and choose **Delete GitHub App**. **Warning:** Deleting the GitHub App is permanent and cannot be undone. To create a new app, re-register GitHub in the AWS DevOps Agent console.
