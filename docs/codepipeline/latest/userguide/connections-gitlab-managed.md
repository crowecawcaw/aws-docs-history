# Connections for GitLab self-managed

Connections allow you to authorize and establish configurations that associate your
third-party provider with your AWS resources. To associate your third-party repository as
a source for your pipeline, you use a connection.

###### Note

Instead of creating or using an existing connection in your account, you can use a
shared connection between another AWS account. See [Use a connection shared with another account](connections-shared.md "connections-shared.md").

###### Note

This feature is not available in the Asia Pacific (Hong Kong),
Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne),
Asia Pacific (Osaka), Africa (Cape Town), Middle East (Bahrain),
Middle East (UAE), Europe (Spain), Europe (Zurich),
Israel (Tel Aviv), or AWS GovCloud (US-West) Regions. To reference other available
actions, see [Product and service integrations with CodePipeline](integrations.md "integrations.md"). For
considerations with this action in the Europe (Milan) Region, see the note in [CodeStarSourceConnection for
Bitbucket Cloud, GitHub, GitHub Enterprise Server, GitLab.com, and GitLab self-managed
actions](action-reference-CodestarConnectionSource.md "action-reference-CodestarConnectionSource.md").

To add a GitLab self-managed source action in CodePipeline, you can choose either to:

- Use the CodePipeline console **Create pipeline** wizard or
  **Edit action** page to choose the **GitLab
  self-managed** provider option. See [Create a connection to GitLab
  self-managed (console)](#connections-gitlab-managed-console "#connections-gitlab-managed-console") to add the action. The
  console helps you create a host resource and a connections resource.
- Use the CLI to add the action configuration for the
  `CreateSourceConnection` action with the
  `GitLabSelfManaged` provider and create your resources:
  - To create your connections resources, see [Create a host and connection to GitLab
    self-managed (CLI)](#connections-gitlab-managed-cli "#connections-gitlab-managed-cli") to create a host
    resource and a connections resource with the CLI.
  - Use the `CreateSourceConnection` example action configuration
    in [CodeStarSourceConnection for
    Bitbucket Cloud, GitHub, GitHub Enterprise Server, GitLab.com, and GitLab self-managed
    actions](action-reference-CodestarConnectionSource.md "action-reference-CodestarConnectionSource.md") to add your
    action as shown in [Create a pipeline (CLI)](pipelines-create.md#pipelines-create-cli "pipelines-create.md#pipelines-create-cli").

###### Note

You can also create a connection using the Developer Tools console under
**Settings**. See [Create a
Connection](../../../dtconsole/latest/userguide/connections-create.md "../../../dtconsole/latest/userguide/connections-create.md").

Before you begin:

- You must have already created an account with GitLab and have GitLab Enterprise
  Edition or GitLab Community Edition with a self-managed installation. For more
  information, see [https://docs.gitlab.com/ee/subscriptions/self_managed/](https://docs.gitlab.com/ee/subscriptions/self_managed/ "https://docs.gitlab.com/ee/subscriptions/self_managed/").

###### Note

Connections only provide access for the account that was used to create and
authorize the connection.

###### Note

You can create connections to a repository where you have the **Owner** role in GitLab, and then the connection can be
used with with resources such as CodePipeline. For repositories in groups, you do not
need to be the group owner.

- You must have already created a GitLab personal access token (PAT) with the
  following scoped-down permission only: api. For more information, see [https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html "https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html").
  You must be an administrator to create and use the PAT.

###### Note

Your PAT is used to authorize the host and is not otherwise stored or used by
connections. To set up a host, you can create a temporary PAT and then after you
set up the host, you can delete the PAT.

- You can choose to set up your host ahead of time. You can set up a host with or
  without a VPC. For details about VPC configuration and additional information about
  creating a host, see [Create a host](../../../dtconsole/latest/userguide/connections-host-create.md "../../../dtconsole/latest/userguide/connections-host-create.md").

###### Topics

- [Create a connection to GitLab
  self-managed (console)](#connections-gitlab-managed-console "#connections-gitlab-managed-console")
- [Create a host and connection to GitLab
  self-managed (CLI)](#connections-gitlab-managed-cli "#connections-gitlab-managed-cli")

## Create a connection to GitLab

self-managed (console)

Use these steps to use the CodePipeline console to add a connections action for your GitLab
self-managedr repository.

###### Note

GitLab self-managed connections only provide access to repositories owned by the
GitLab self-managed account that was used to create the connection.

**Before you begin:**

For a host connection to GitLab self-managed, you must have completed the steps to
create a host resource for your connection. See [Manage hosts
for connections](../../../dtconsole/latest/userguide/connections-hosts.md "../../../dtconsole/latest/userguide/connections-hosts.md").

### Step 1: Create or edit

your pipeline

###### To create or edit your pipeline

1. Sign in to the CodePipeline console.
2. Choose one of the following.
   - Choose to create a pipeline. Follow the steps in _Create a Pipeline_ to complete the first
     screen and choose **Next**. On the
     **Source** page, under **Source provider**, choose **GitLab self-managed**.
   - Choose to edit an existing pipeline. Choose **Edit**, and then choose **Edit
     stage**. Choose to add or edit your source action. On
     the **Edit action** page, under
     **Action name**, enter the name for
     your action. In **Action provider**,
     choose **GitLab self-managed**.

3. Do one of the following:
   - Under **Connection**, if you have not already
     created a connection to your provider, choose **Connect to
     GitLab self-managed**. Proceed to Step 2: Create a
     Connection to GitLab self-managed.
   - Under **Connection**, if you have already created
     a connection to your provider, choose the connection, and then
     proceed to Step 3: Save your GitLab self-managed source
     action.

### Step 2: Create a

connection to GitLab self-managed

After you choose to create the connection, the **Connect to GitLab
self-managed** page is shown.

###### To connect to GitLab self-managed

1. In **Connection name**, enter the name for your
   connection.
2. In **URL**, enter the endpoint for your server.

###### Note

If the provided URL has already been used to set up a host for a
connection, you will be prompted to choose the host resource ARN that
was created previously for that endpoint. 3. If you have launched your server into an Amazon VPC and you want to
connect with your VPC, choose **Use a VPC** and complete
the information for the VPC. 4. Choose **Connect to GitLab self-managed**. The created
connection is shown with a **Pending** status. A host
resource is created for the connection with the server information you
provided. For the host name, the URL is used. 5. Choose **Update pending connection**. 6. If a page opens with a redirect message confirming that you want to
continue to the provider, choose **Continue**. Enter the
authorization for the provider. 7. A **Set up
`host_name`** page displays. In
**Provide personal access token**, provide your GitLab
PAT with the following scoped-down permission only: `api`.

###### Note

Only an administrator can create and use the PAT.

Choose **Continue**.

![Console screenshot showing GitLab self-managed personal access token entry for the new host](images/connections-create-glsm-pat.png) 8. The connection page shows the created connection in an
**Available** status.

### Step 3: Save your GitLab

self-managed source action

Use these steps on the wizard or **Edit action** page to save
your source action with your connection information.

###### To complete and save your source action with your connection

1. In **Repository name**, choose the name of your
   third-party repository.
2. Under **Pipeline triggers** you can add triggers if your
   action is an CodeConnections action. To configure the pipeline trigger configuration
   and to optionally filter with triggers, see more details in [Add trigger with code push or pull request event
   types](pipelines-filter.md "pipelines-filter.md").
3. In **Output artifact format**, you must choose the format
   for your artifacts.
   - To store output artifacts from the GitLab self-managed action
     using the default method, choose **CodePipeline
     default**. The action accesses the files from the
     repository and stores the artifacts in a ZIP file in the pipeline
     artifact store.
   - To store a JSON file that contains a URL reference to the
     repository so that downstream actions can perform Git commands
     directly, choose **Full clone**. This option can
     only be used by CodeBuild downstream actions.

4. Choose **Next** on the wizard or
   **Save** on the **Edit action**
   page.

## Create a host and connection to GitLab

self-managed (CLI)

You can use the AWS Command Line Interface (AWS CLI) to create a connection.

To do this, use the **create-connection** command.

###### Important

A connection created through the AWS CLI or AWS CloudFormation is in `PENDING`
status by default. After you create a connection with the CLI or CloudFormation, use the
console to edit the connection to make its status `AVAILABLE`.

You can use the AWS Command Line Interface (AWS CLI) to create a host for installed connections.

You use a host to represent the endpoint for the infrastructure where your third-party
provider is installed. After you complete the host creation with the CLI, the host is in
**Pending** status. You then set up, or register, the host to move
it to an **Available** status. After the host is available, you
complete the steps to create a connection.

To do this, use the **create-host** command.

###### Important

A host created through the AWS CLI is in `Pending` status by default.
After you create a host with the CLI, use the console or the CLI to set up the host
to make its status `Available`.

###### To create a host

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
   the **create-host** command, specifying the `--name`,
   `--provider-type`, and `--provider-endpoint` for your
   connection. In this example, the third-party provider name is
   `GitLabSelfManaged` and the endpoint is
   `my-instance.dev`.

```
aws codestar-connections create-host --name MyHost --provider-type GitLabSelfManaged --provider-endpoint "https://my-instance.dev"
```

If successful, this command returns the host Amazon Resource Name (ARN)
information similar to the following.

```
{
    "HostArn": "arn:aws:codestar-connections:us-west-2:`account_id`:host/My-Host-28aef605"
}
```

After this step, the host is in `PENDING` status. 2. Use the console to complete the host setup and move the host to an
`Available` status.

###### To create a connection to GitLab self-managed

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
   the **create-connection** command, specifying the
   `--host-arn` and `--connection-name` for your
   connection.

```
aws codestar-connections create-connection --host-arn arn:aws:codestar-connections:us-west-2:`account_id`:host/MyHost-234EXAMPLE --connection-name MyConnection
```

If successful, this command returns the connection ARN information similar to
the following.

```
{
    "ConnectionArn": "arn:aws:codestar-connections:us-west-2:`account_id`:connection/aEXAMPLE-8aad"
}
```

2. Use the console to set up the pending connection.
3. The pipeline defaults to detect changes on code push to the connection source
   repository. To configure the pipeline trigger configuration for manual release
   or for Git tags, do one of the following:
   - To configure the pipeline trigger configuration to start with a manual
     release only, add the following line to the configuration:

   ```
   "DetectChanges": "false",
   ```

   - To configure the pipeline trigger configuration to filter with
     triggers, see more details in [Add trigger with code push or pull request event
     types](pipelines-filter.md "pipelines-filter.md"). For example, the following adds
     to the pipeline level of the pipeline JSON definition. In this example,
     `release-v0` and `release-v1` are the Git tags
     to include, and `release-v2` is the Git tag to
     exclude.

   ```
   "triggers": [
               {
                   "providerType": "CodeStarSourceConnection",
                   "gitConfiguration": {
                       "sourceActionName": "Source",
                       "push": [
                           {
                               "tags": {
                                   "includes": [
                                       "release-v0", "release-v1"
                                   ],
                                   "excludes": [
                                       "release-v2"
                                   ]
                               }
                           }
                       ]
                   }
               }
           ]
   ```
