

# Connecting GitLab
<a name="connecting-to-cicd-pipelines-connecting-gitlab"></a>

GitLab integration enables AWS DevOps Agent to monitor deployments from GitLab Pipelines to inform causal investigations during incident response. This integration follows a two-step process: account-level registration of GitLab, followed by connecting specific projects to individual Agent Spaces.

## Registering GitLab (account-level)
<a name="registering-gitlab-account-level"></a>

GitLab is registered at the AWS account level and shared among all Agent Spaces in that account. Each registration links to one GitLab user or one GitLab group.

### Step 1: Navigate to pipeline providers
<a name="step-1-navigate-to-pipeline-providers"></a>

1. Sign in to the AWS Management Console

1. Navigate to the AWS DevOps Agent console

1. Go to the **Capability Providers** page (accessible from the side navigation)

1. Find **GitLab** in the **Available** providers section under **Pipeline** and choose **Register**

### Step 2: Configure GitLab connection
<a name="step-2-configure-gitlab-connection"></a>

On the GitLab registration page, configure the following:

**Connection type** – Select whether you're connecting as a person or a group:
+ **Personal** (default) – Your individual GitLab user account with a username and profile
+ **Group** – In GitLab, you use groups to manage one or more related projects at the same time

**GitLab instance type** – Choose which type of GitLab instance you're connecting to:
+ **GitLab.com** (default) – The public GitLab service
+ **GitLab Self-Managed** – Check the **Use GitLab self hosted endpoint** box and provide the URL to your GitLab instance

#### Private connectivity for GitLab Self-Managed
<a name="private-connectivity-for-gitlab-self-managed"></a>

**Connect to endpoint using a private connection** – If your GitLab Self-Managed instance isn't reachable over the public internet, select this option to have AWS DevOps Agent reach it through a private connection to your VPC. Create the private connection before you register GitLab, then select the existing connection here. For more information, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).

**Access token** – Provide a GitLab personal access token:

1. In a separate browser tab, log in to your GitLab account

1. Navigate to your user settings and select **Access Tokens**

1. Create a new personal access token with the following permissions:
   + `read_repository` – Required to access repository content
   + `read_virtual_registry` – Required to access virtual registry information
   + `read_registry` – Required to access registry information
   + `api` – Required for read and write API access
   + `self_rotate` - Required for rotating tokens. This feature is currently unsupported by AWS DevOps Agent but will be supported at a later date. Adding now prevents the need to create a new token in the future.

1. Set the token expiration to a maximum of 365 days from the current date

1. Copy the generated token

1. Return to the AWS DevOps Agent console

1. Paste the token into the "Access Token" field

### Step 3: Complete registration
<a name="step-3-complete-registration"></a>

**(Optional) Tags** – Add AWS tags to the GitLab registration for organizational purposes.

Choose **Next** to review your configuration, then choose **Submit** to complete the GitLab registration process. The system will validate your access token and establish the connection.

## Connecting projects to an Agent Space
<a name="connecting-projects-to-an-agent-space"></a>

After registering GitLab at the account level, you can connect specific projects to individual Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space

1. Go to the **Capabilities** tab

1. In the **Pipeline** section, choose **Add**

1. Select **GitLab** from the list of available providers

1. Select the GitLab registration that contains the projects you want to use

1. Select the GitLab projects relevant to your Agent Space

1. Choose **Save**

AWS DevOps Agent monitors these projects for deployments from GitLab Pipelines to inform causal investigations. A single Agent Space can use projects from multiple registrations. To add projects from another registration, repeat these steps.

## Configuring Code Review and Automated Testing
<a name="configuring-code-review-and-automated-testing"></a>

When you select projects in the GitLab connection step, they are automatically added to the **Code Review and Automated Testing** section. This section configures which projects automatically trigger a [Release readiness code reviews](release-management-release-readiness-code-review.md) and automated testing capabilities.

The Code Review and Automated Testing configuration includes:
+ **Capabilities** — Choose code review and automated testing capabilities for each project. The section provides two per-project settings:
  + **Auto trigger change review** — When enabled for a project, DevOps Agent automatically runs a [Release readiness code reviews](release-management-release-readiness-code-review.md) each time a merge request is opened or updated. Review findings appear as inline comments on the merge request. This is enabled by default for all connected projects.
  + **Automated verification testing** — When enabled for a project, DevOps Agent builds, runs, and tests your code changes in a managed verification environment during code reviews. This provides functional validation beyond static analysis. For more information, see [Automated verification testing](release-management-release-readiness-code-review.md). This is enabled by default for all connected projects.
+ **Project list** — Shows all projects you selected during the connection step. Use the search field to filter projects by name. Each project has independent checkboxes for both capabilities.
+ **Runtime role** (optional) — Choose the IAM role that DevOps Agent assumes to run automated capabilities on your selected projects. This role is used when accessing internal services needed during builds, such as private package registries and artifact storage systems. We recommend using a different role from your primary agent role.

To configure automated reviews:

1. After connecting your projects, navigate to the **Code Review and Automated Testing** section in your GitLab integration settings.

1. For each project, enable or disable the **Auto trigger change review** capability depending on whether you want automatic merge request reviews.

1. For each project, enable or disable the **Automated verification testing** capability depending on whether you want [automated verification testing](release-management-release-readiness-code-review.md) in a managed verification environment.

1. Optionally, select an IAM role from the **Runtime role** dropdown that DevOps Agent will assume when running automated capabilities on your selected projects.

1. Choose **Save** to apply your configuration.

Once configured, any new merge request in a project with **Auto trigger change review** enabled will automatically trigger a release readiness code review. If **Automated verification testing** is also enabled, the review includes functional validation in a verification environment. For more information about code reviews, see [Release readiness code reviews](release-management-release-readiness-code-review.md).

### Advanced settings: trigger filters
<a name="advanced-settings-trigger-filters"></a>

By default, a project with **Auto trigger change review** enabled runs a release readiness code review on every applicable merge request event, on any target branch. Use **Advanced settings** to add trigger filters that control exactly when automated reviews run for each project.

Each filter is a *filter group* that combines two conditions:
+ **Target branches** (required) — One or more branch names or patterns, entered as regular expressions (for example, `main` or `release/.*`). The review triggers only when the merge request's target branch matches one of these patterns.
+ **Trigger events** (optional) — The merge request events that trigger a review: **Merge request ready for review** or **Merge request drafted**. Leave this empty to match all applicable events.

Within a filter group, all conditions must match (AND). You can add multiple filter groups, and a review triggers when any group matches (OR).

To configure trigger filters:

1. Open the **Advanced settings** section in the connection flow. (To change filters on an existing connection, select the connection in the **Pipeline** section, choose **Edit**, and then open **Advanced settings**.)

1. Find the project you want to configure and select the **Change review** tab.

1. Choose **Add filter group**, then define the group's conditions:
   + Under **Target branches**, enter a branch name or pattern and press Enter or choose **Add**. Repeat to add more patterns.
   + (Optional) Under **Trigger events**, select **Merge request ready for review**, **Merge request drafted**, or both. Leave it empty to match all events.

1. (Optional) Choose **Add filter group** again to express alternative conditions.

1. Choose **Save** to apply your configuration.

You can define up to 5 filter groups per project, with up to 20 patterns per group. Each pattern must be a valid regular expression of up to 256 characters. If you don't add any filter groups, reviews trigger on all applicable events for all target branches.

## Troubleshooting
<a name="troubleshooting"></a>

For DNS, network reachability, security group, or TLS errors when you use GitLab Self-Managed with a private connection, see [Troubleshooting private connections](configuring-integrations-and-knowledge-troubleshooting-private-connections.md).

### Some projects don't appear in the project list
<a name="some-projects-dont-appear-in-the-project-list"></a>

**Symptom**

You can register GitLab successfully, but one or more projects that you expect to connect do not appear in the project list.

**Cause**

For a Personal connection, AWS DevOps Agent lists projects where the access token's user is a member. A project does not appear if that user is not a member, even if the user can view the project through another GitLab access path.

**Resolution**
+ Confirm that the access token's user is a member of each project that you want to connect.
+ Confirm that the token has not expired and includes the scopes listed in [Step 2: Configure GitLab connection](#step-2-configure-gitlab-connection).
+ After changing project membership or replacing the token, refresh the project list.

### A GitLab project can't be connected
<a name="a-gitlab-project-cant-be-connected"></a>

**Symptom**

Connecting a project fails with `GitLab project '<path>' (ID: <id>) is not accessible to this GitLab token.` or `GitLab is currently throttling requests (HTTP 429). Please retry the association later.`

**Cause**

The token cannot read the selected project, or GitLab is temporarily throttling project validation requests.

**Resolution**
+ Confirm that the token is valid and its user or group can access the selected project.
+ Confirm that the token includes the required scopes from [Step 2: Configure GitLab connection](#step-2-configure-gitlab-connection).
+ If GitLab returns HTTP 429, wait and retry the association.

## Managing GitLab connections
<a name="managing-gitlab-connections"></a>
+ **Updating access token** – If your access token expires or needs to be updated, you can rotate it without deregistering. On the **Capability Providers** page, select your GitLab registration, choose **Update** from the **Actions** menu, and enter the new token. Your Agent Space associations and project connections are preserved.
+ **Viewing connected projects** – In the AWS DevOps Agent console, select your Agent Space and go to the Capabilities tab to view connected projects in the Pipeline section.
+ **Removing GitLab connection** – To disconnect GitLab projects from an Agent Space, select the connection in the Pipeline section and choose **Remove**. To remove the GitLab registration completely, remove it from all Agent Spaces first, then delete the registration at the account level.