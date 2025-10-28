Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# How to migrate from CodeCatalyst

_After careful consideration, we have made the decision to close
new customer access to Amazon CodeCatalyst, effective November 7, 2025. Existing Amazon
CodeCatalyst customers can continue to use the service with existing spaces, but will
not be able to create new spaces. AWS continues to invest in security and availability
for Amazon CodeCatalyst, but we do not plan to introduce new features._

Customers can manually migrate their data from Amazon CodeCatalyst to other providers.
This document describes the basic ways to migrate, extract or delete data from the
CodeCatalyst and AWS Management consoles. Resources and data created in other AWS or 3P
services through the CodeCatalyst console will need to be deleted through those services to
stop accruing charges (if applicable).

Customers can consider migrating to [GitLab Duo with Amazon Q](https://aws.amazon.com/blogs/devops/announcing-general-availability-of-gitlab-duo-with-amazon-q/ "https://aws.amazon.com/blogs/devops/announcing-general-availability-of-gitlab-duo-with-amazon-q/") which announced General Availability April 17, 2025.
This new offering is an integrated product, bringing together [GitLab’s](https://about.gitlab.com/ "https://about.gitlab.com/") DevSecOps platform with Amazon Q’s
generative AI capabilities. Gitlab Duo with Amazon Q embeds Amazon Q agent capabilities
directly in GitLab’s DevSecOps platform to accelerate complex, multi-step tasks across the
entire software development lifecycle.

## Migrating your repositories

### Migrating your CodeCatalyst repository to a GitLab repository

Using the prerequisite URL in combination with the HTTPS Git repository
credentials, follow the guidance in GitLab’s documentation regarding [importing source
code](https://docs.gitlab.com/ee/user/project/import/ "https://docs.gitlab.com/ee/user/project/import/") from a [repository
by URL](https://docs.gitlab.com/ee/user/project/import/repo_by_url.html "https://docs.gitlab.com/ee/user/project/import/repo_by_url.html").

### Migrating your CodeCatalyst repository to a GitHub repository

Using the prerequisite URL in combination with the HTTPS Git repository
credentials, follow the guidance in GitHub’s documentation regarding [importing source code](https://docs.github.com/en/migrations/importing-source-code/using-github-importer/about-github-importer "https://docs.github.com/en/migrations/importing-source-code/using-github-importer/about-github-importer").

### Generic migration to a different repository provider

1. **Clone the CodeCatalyst repository**

Clone the Amazon CodeCatalyst repository to your local machine using Git.
If you’re using HTTPS, you can do this by running the following
command:

```
git clone --mirror https://your-aws-repository-url your-aws-repository
```

Replace `your-aws-repository-url` with the URL of your Amazon
CodeCatalyst repository.

Replace `your-aws-repository` with a name for this
repository.

Example:

```
git clone https://git-codecatalyst.us-east-2.amazonaws.com/v1/repos/MyDemoRepo my-demo-repo
```

2. **Set up new remote repository
   pointer**

Navigate to the directory of your cloned Amazon CodeCatalyst repository.
Then, add the repository url from the new repository provider as a remote:

```
git remote add <provider name> <provider-repository-url>
```

Replace `<provider name>` with the provider name of your
choice. (Example: gitlab)

Replace <provider-repository-url> with the URL of your new repository
provider’s repository. 3. **Push your local repository to the new remote
repository:**

This will push all branches and tags to your new repository provider’s
repository. Provider name must match the provider name from step 2.

```
git push <provider name> --mirror
```

Notes:

    * The remote repository should be empty
    * The remote repository may have protected branches not allowing
     force push, depending on the provider. If this happens, you have to
     navigate to your new repository provider and disable branch
     protections to allow for force push.

4. **Verify the migration**

Once the push is complete, verify that all files, branches, and tags have
been successfully migrated to the new repository provider. You can do this
by browsing your repository online or by cloning it to another location and
checking it locally. 5. \***\*Update Remote URLs
(Optional)\*\***

If you plan to continue working with the migrated repository locally, you
may want to update the remote URL to point to the new provider’s repository
instead of Amazon CodeCatalyst. You can do this using the following
command:

```
git remote set-url origin <provider-repository-url>
```

Replace <provider-repository-url> with the URL of your new repository
provider’s repository.

## Extracting your data from CodeCatalyst

### Download artifacts

You can download and inspect artifacts generated by your Amazon CodeCatalyst
workflow actions. There are two types of artifacts you can download:

- Source artifacts – An artifact that contains a snapshot of the source
  repository content as it existed when the run started.
- Workflow artifacts – An artifact defined in the Outputs property of your
  workflow's configuration file.

To download artifacts output by the workflow:

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and
   then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source repository
   or branch name where the workflow is defined, or filter by workflow name or
   status.
5. Under the workflow's name, choose **Runs**.
6. In **Run history**, in the **Run ID** column, choose a run. For example,
   Run-95a4d.
7. Under the run's name, choose **Artifacts**.
8. Next to an artifact, choose **Download**. An
   archive file will download. Its file name consists of seven random
   characters.
9. Extract the archive using an archive extraction utility of your
   choice.

### Download your Issue attachments

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose the issue for which you want to manage attachments. For help on
   finding your issue, see [Finding and viewing issues](issues-view.md "issues-view.md")
3. To download an attachment, choose the ellipses menu next to the attachment
   you want to download and choose **Download**.

### Download an action's source code

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. Find the action whose code you want to view:
   1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
   2. Choose the name of any workflow, or create one. For information
      about creating a workflow, see [Creating a workflow](workflows-create-workflow.md "workflows-create-workflow.md").
   3. Choose **Edit**.
   4. At the top-left, choose **+ Actions**
      to open the action catalog.
   5. In the drop-down list, choose **Amazon
      CodeCatalyst** to view CodeCatalyst, CodeCatalyst Labs,
      and third-party actions.
   6. Search for an action, and choose its name. Do not choose the plus
      sign (**+**). Details about the action appear.

4. In the action details dialog box, near the bottom, choose **Download**.

A page appears, showing the Amazon S3 bucket where the action's source
code resides. For information about Amazon S3, see [What is Amazon S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") in the _Amazon Simple
Storage Service User Guide_.

## Deleting your data from CodeCatalyst

Prior to deleting your data from CodeCatalyst, inform your team about the service
migration and validate no resources are still needed. Once data and resources are
deleted, they cannot be recovered.

### Request the service team to delete data on your behalf

A Space Admin can request the service team delete a space on their behalf by
contacting us via the Support Center in the CodeCatalyst console. Space admins must
be authenticated in the CodeCatalyst console to request space deletion. Once you
submit your request, the service team will contact you to confirm the request before
taking action on your behalf.

### Delete your CodeCatalyst space

You can delete a space to remove access to all of the space's resources. You must
have the **Space administrator** role to delete a
space.

**Note:** You cannot undo a space deletion and there
is no way to retrieve the data once a space is deleted.

After you have deleted a space, all space members will be unable to access space
resources. Billing for space resources will also stop, and any workflows that are
prompted by third-party source repositories will be stopped.

If you belong to more than one space, choose the space in the top navigation
bar.

###### To delete a space

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space.

###### Tip

If you belong to more than one space, choose a space in the
top navigation bar. 3. Choose **Settings**, and then choose
**Delete**. 4. Type `delete` to confirm the deletion. 5. Choose **Delete**.

###### Note

If you belong to more than one space, you're redirected to the
space overview page. If you belong to one space, you're
redirected to the space creation page.

If you delete a space but belong to more than one space, you're redirected to the
space overview page. If you belong to one space, you're redirected to the space
creation page.

If you created resources in other AWS or third-party services from the
CodeCatalyst console, you will need to go to those services individually to shut
down resources from the billing account they were created in. Deleting a space will
only delete the CodeCatalyst data and resources.

### Delete a project

You can delete a project to remove all access to the project's resources. You must
have the **Space administrator** or **Project administrator** role to delete a project. Once you
have deleted a project, project members will be unable to access project resources,
and any workflows that are prompted by third-party source repositories will be
stopped.

To delete your project:

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the space with the project you want to view. Under
   **Projects**, choose your project.
3. In the navigation pane, choose **Project
   settings**.
4. Choose **Delete project**.
5. Enter `delete` to confirm the deletion.
6. Choose **Delete project**.

If you created resources in other AWS or third-party services from a
CodeCatalyst project, you will need to go to those services individually to shut
down resources from the billing account they were created in. Deleting a space will
only delete the CodeCatalyst data and resources.

### Delete a source repository

You can delete your source repositories for an Amazon CodeCatalyst project.
Deleting a source repository also deletes any project information stored in the
repository. If any workflows depend on the source repository, those workflows will
be deleted from the list of project workflows after the repository is deleted.
Issues that reference the source repository will not be deleted or altered, but any
links to the source repository added to issues will fail once the repository is
deleted.

Important:Deleting a
source repository cannot be undone. After you delete a source repository, you are no
longer able to clone it, pull data from it, or push data to it. Deleting a source
repository does not delete any local copies of that repository (local repos). To
delete a local repo, use your local computer's directory and file management
tools.

Note:You cannot
delete a linked repository in the CodeCatalyst console. To delete a linked
repository, choose the link in the list of repositories to open that repository in
the service that hosts it, and then delete it. For more information, see the
documentation for the service that hosts the linked repository.

To remove a linked repository from a project, see [Unlinking GitHub repositories, Bitbucket repositories, GitLab project
repositories, and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

###### To delete a source repository

1. Navigate to the project that contains the source repository you want to delete.
2. On
   the summary page for your project, choose the repository you want from the list, and then choose
   **View repository**. Alternatively, in the navigation pane,
   choose **Code**, and then choose **Source
   repositories**.
   Choose the name of the repository from the list of source repositories for the project.
3. On the home page for the repository, choose
   **More**, choose **Manage settings**,
   and then choose **Delete repository**.
4. Review the branch, pull request, and related workflow information to help ensure that you
   are not deleting a repository that is still in use or has unfinished work. If you want to
   continue, type **delete**, and then choose **Delete**.

### Delete a custom blueprint

When you delete a blueprint from your Amazon CodeCatalyst space, all your access
is removed to the resources of the blueprint project or blueprint version. When you
delete a blueprint, project members will be unable to access project resources, and
any workflows that are prompted by third-party source repositories will be
stopped.

If you delete a blueprint, it doesn’t affect a project that is applied the
blueprint. Resources of the blueprint aren't removed from the project.

Important: To delete a published custom
blueprint or a custom blueprint's catalog version from your space, you must be
signed in with an account that has the Space administrator or Power user role in the
space.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space where you want to delete a
   custom blueprint.
3. On the space dashboard, choose the **Settings** tab, and
   then choose **Blueprints**.
4. On the **Settings** table, choose the radio button for
   the custom blueprint that you want to delete, and then choose
   **Delete blueprint**.
5. Enter `delete` to confirm the deletion of the blueprint catalog
   version.
6. Choose **Delete**.

### Delete your Issue attachments

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose the issue for which you want to manage attachments. For help on
   finding your issue, see [Finding and viewing issues](issues-view.md "issues-view.md") .
3. To remove an attachment, choose the ellipses menu next to the attachment
   you want to remove and choose **Delete**.

### Deleting a file in Dev Environments accessed through Amazon CodeCatalyst

You can delete files in a Dev Environment, locally on your computer, or in an
integrated development environment (IDE). You can't delete files in the Amazon
CodeCatalyst console.

### Deleting a Dev Environment for your space

For more information about considerations for deleting a Dev Environment, see
[Deleting a Dev Environment](devenvironment-delete.md "devenvironment-delete.md").

You must have the **Space administrator** role to
view this page and to manage Dev Environments at the space level. If you belong to
more than one space, choose a space in the top navigation bar.

###### To delete a Dev Environment

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space
3. Choose **Settings**, and then choose
   **Dev Environments**.
4. Choose the selector next to the Dev Environment you want to manage. Choose
   **Delete**.
5. Enter `delete` to confirm the Dev Environment
   deletion.
6. Choose **Delete**.

### Deleting account connections

You can delete an account connection in the CodeCatalyst console that you
previously added to your space. After an account connection is deleted, you cannot
reconnect the connection and have to establish a new one.

A billing account must be designated for your CodeCatalyst space, even if usage
for the space will not exceed the Free tier. Before you can remove a space for an
account that is a designated billing account, you will need to add another account
for your space. If you are looking to delete your billing account for the space, you
need to delete your space. See [Managing billing](../adminguide/managing-billing.md "../adminguide/managing-billing.md") in the Amazon CodeCatalyst Administrator Guide.

To manage account connections for your space, you must have the **Space administrator** or **Power
user** role.

An account that has been removed can be added again later, but you must create a
new connection between the account and the space. You will need to re-associate any
IAM roles to the account.

###### To delete an account connection

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space. Choose **Settings**,
   and then choose **AWS accounts**.
3. Under **Amazon CodeCatalyst display name**, choose the selector
   next to the account connection that you want to remove.
4. Choose **Remove AWS account**. Confirm the deletion by
   entering the name in the field, and then choose
   **Remove**.

A success banner displays, and the account connection is removed from the
list of connections.

### Remove an account from a CodeCatalyst space in the AWS Management

Console

You can use the page for CodeCatalyst in AWS to remove an account that has been
added to a space. For this procedure, using administrative permissions for the
specific account you are managing, sign in to the Amazon CodeCatalyst Spaces page in
the AWS Management Console to remove an AWS account from your space. To remove
an account that is a designated billing account for your CodeCatalyst space, make
sure to first specify a new billing account.

An account that has been removed can be added again later, but you must create a
new connection between the account and the space. You will need to re-associate any
IAM roles to the added account.

A billing account must be designated for your CodeCatalyst space, even if usage
for the space will not exceed the Free tier. Before you can remove a space for an
account that is a designated billing account, you will need to add another account
for your space.

You must have the **Space administrator** or
**Power user** role to manage account connections
for your space.

###### To remove an added account

1. In the AWS Management Console, make sure you are logged in with the same account that
   you want to manage.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. Navigate to your CodeCatalyst space. Choose **Settings**,
   and then choose **Billing**.
4. View the billing account information on the page to make sure the account
   you want to remove is not the designated billing account for the space.
5. Choose **Manage billing in AWS**. This opens the
   Amazon CodeCatalyst Spaces in the AWS Management Console. If you're prompted to log in, log in to
   AWS, and then choose the button again to load the page.
6. On the **Amazon CodeCatalyst
   Spaces**
   page, choose the space with the account that you want to remove. The
   details page for the space displays.
7. Choose **Remove space**.
8. In **Remove CodeCatalyst space from this account**, enter
   the space name to confirm. Choose **Remove**.

### Deleting a secret

Use the following procedure to delete a secret and the secret reference
identifier. Before deleting a secret, we recommend that you remove the secret's
reference identifier from all workflow actions. If you delete the secret without
deleting the reference identifier, the action will fail the next time it
runs.

###### To delete a secret's reference identifier from a workflow

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
3. Choose the name of your workflow. You can filter by the source repository
   or branch name where the workflow is defined, or filter by workflow name or
   status.
4. Choose **Edit**.
5. Choose **YAML**.
6. Search the workflow for the following string:

```
${Secrets.
```

This finds all reference identifiers of all secrets. 7. Delete the reference identifier of the chosen secret, or replace it with a
plaintext value. 8. (Optional) Choose **Validate** to validate the workflow's
YAML code before committing. 9. Choose **Commit**, enter a commit message, and choose
**Commit** again.

###### To delete a secret

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose
   **Secrets**.
3. In the secrets list, choose the secret you want to delete.
4. Choose **Delete**.
5. Enter `delete` to confirm the deletion.
6. Choose **Delete**.

### Deleting a team

You can delete a team that you no longer need. When you delete a team, the
associated permissions will be removed for all team members from all projects and
resources in the space. You must have the **Space
administrator** role to manage teams.

###### Delete a team

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space. Choose **Settings**, and
   then choose **Teams**.
3. In **Actions**, choose **Delete team**.
   This changes the role for the entire team.
4. Choose **Delete**.

### Deleting a provisioned fleet

Use the following instructions to delete a provisioned fleet.

Before deleting a provisioned fleet, remove it from all actions by deleting the
Fleet property from the action's YAML code. Any action that continues to reference a
provisioned fleet after it is deleted will fail the next time the action
runs.

###### To delete a provisioned fleet

1. In the navigation pane, choose **CI/CD**, and then choose **Compute**.
2. In the **Provisioned fleet** list, choose the fleet you
   want to delete.
3. Choose **Delete**.
4. Enter `delete` to confirm the deletion.
5. Choose **Delete**.

### Deleting a package repository

Perform the following steps to delete a package repository in CodeCatalyst.

###### To delete a package repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project that contains the package repository that you want to delete.
3. From the navigation pane, choose **Packages**.
4. On the **Package repositories** page, choose the repository you want to delete.
5. Choose **Delete**.
6. Review the information provided about the effects of deleting a package repository.
7. Enter `delete` into the input field and choose **Delete**.

All other resources stored in Amazon CodeCatalyst will be deleted when your space
is deleted. This does not include resources and data created in other AWS or 3P
services through the CodeCatalyst console. All resources created in services outside
of CodeCatalyst console will need to be deleted through those services to stop
accruing charges.

If you have additional questions, please contact us at
aws-codecatalyst-service@amazon.com or reach out through the Support Center in the
Amazon CodeCatalyst console.
