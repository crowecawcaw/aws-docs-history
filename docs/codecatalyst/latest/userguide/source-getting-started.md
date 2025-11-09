Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Getting started with CodeCatalyst source repositories and

the Single-page application blueprint

Follow the steps in this tutorial to learn how to work with source repositories in Amazon CodeCatalyst.

The quickest way to get started working with source repositories in Amazon CodeCatalyst is to
create a project using a template. When you create a project using a template, resources are
created for you, including a source repository that includes sample code. You can use this
repository and code example to learn how to:

- View a project's source repositories and browse their contents
- Create a Dev Environment with a new branch where you can work on code
- Change a file, and commit and push your changes
- Create a pull request and review your code changes with other project
  members
- See the workflow for your project automatically build and test the changes in the
  source branch of the pull request
- Merge your changes from your source branch into the destination branch and close
  the pull request
- See the merged changes automatically built and deployed
  To get the most out of this tutorial, invite others to your project so you can work
  together on a pull request. You can also explore additional features in CodeCatalyst, such as
  creating issues and associating them with a pull request, or configuring notifications and
  getting alerts when the associated workflow runs. For a full exploration of CodeCatalyst, see
  [Getting started tutorials](getting-started-topnode.md "getting-started-topnode.md").

## Creating a project with a

blueprint

Creating a project is the first step in being able to work together. You can use a
blueprint to create your project, which will also create a source repository with
sample code and a workflow that will automatically build and deploy your code when you
change it. In this tutorial, we'll walk you through a project created with the
**Single-page application** blueprint, but you can follow the procedures
for any project with a source repository. Make sure to choose an IAM role or add an
IAM role if you don't have one as part of creating the project. We recommend that you
use the **CodeCatalystWorkflowDevelopmentRole-`spaceName`** service role for this project.

If you already have a project, you can skip ahead to [Viewing the repositories for a
project](#source-getting-started-source-view "#source-getting-started-source-view").

###### Note

Only users with the Space administrator or **Power user**
role can create projects in CodeCatalyst. If you do not have this role and you need a
project to work on for this tutorial, ask someone with one of these roles to create
a project for you and add you to the created project. For more information, see
[Granting access with user roles](ipa-roles.md "ipa-roles.md").

###### To create a project with a blueprint

1. In the CodeCatalyst console, navigate to the space where you want to create a
   project.
2. On the space dashboard, choose **Create project**.
3. Choose **Start with a blueprint**.

###### Tip

You can choose to add a blueprint by giving **Amazon Q** your
project requirements to have Amazon Q suggest a blueprint to you. For more information,
see [Using Amazon Q to choose
a blueprint when creating a project or adding functionality](getting-started-project-assistance.md#getting-started-project-assistance-create-apply-bp "getting-started-project-assistance.md#getting-started-project-assistance-create-apply-bp") and [Best practices when using Amazon Q to create projects
or add functionality with blueprints](projects-create.md#projects-create-amazon-q "projects-create.md#projects-create-amazon-q"). This feature is only available in
the US West (Oregon) Region.

This functionality requires that generative AI features are enabled for the space.
For more information, see [Managing
generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md"). 4. From the **CodeCatalyst blueprints** or **Space blueprints**
tab, choose a blueprint, and then choose **Next**. 5. Under **Name your project**, enter the name that you want to
assign to your project and its associated resource names. The name must be unique within your
space. 6. (Optional) By default, the source code created by the blueprint is stored in a CodeCatalyst
repository. Alternatively, you can choose to store the blueprint's source code in a third-party
repository. For more information, see [Add functionality to projects with extensions in CodeCatalyst](extensions.md "extensions.md").

###### Important

CodeCatalyst doesn't support detecting changes in the default branch for linked
repositories. To change the default branch for a linked repository, you must first unlink it
from CodeCatalyst, change the default branch, and then link it again. For more information,
see [Linking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-link.md "extensions-link.md").

As a best practice, always make sure you have the latest version of the extension
before you link a repository.

Do one of the following depending on the third-party repository provider you want to use:

    * **GitHub repositories**: Connect a GitHub account.


    Choose the **Advanced** dropdown menu, choose GitHub
     as the repository provider, and then choose the GitHub account where you want to store the
     source code created by the blueprint.


    ###### Note

    If you're connecting a GitHub account, you must create a personal
     connection to establish identity mapping between your CodeCatalyst identity and your GitHub identity.
     For more information, see [Personal connections](concepts.md#personal-connection-concept "concepts.md#personal-connection-concept") and [Accessing GitHub resources with personal
     connections](ipa-settings-connections.md "ipa-settings-connections.md").
    * **Bitbucket repositories**: Connect a Bitbucket workspace.


    Choose the **Advanced** dropdown menu, choose Bitbucket
     as the repository provider, and then choose the Bitbucket workspace where you want to store the
     source code created by the blueprint.
    * **GitLab repositories**: Connect a GitLab user.


    Choose the **Advanced** dropdown menu, choose GitLab
     as the repository provider, and then choose the GitLab user where you want to store the
     source code created by the blueprint.

7. Under **Project resources**, configure the blueprint parameters. Depending
   on the blueprint, you may have the option to name the source repository name.
8. (Optional) To view definition files with updates based on the project parameter selections
   you made, choose **View code** or **View workflow** from
   **Generate project preview**.
9. (Optional) Choose **View details** from the blueprint's card to view
   specific details about the blueprint, such as an overview of the blueprint's architecture,
   required connections and permissions, and the kind of resources the blueprint
   creates.
10. Choose **Create project**.

The project overview page opens as soon as you create a project or accept an
invitation to a project and complete the sign-in process. The project overview page for
a new project contains no open issues or pull requests. You can optionally choose to
create an issue and assign it to yourself. You can also choose to invite someone else to
your project. For more information, see [Creating an issue in CodeCatalyst](issues-create-issue.md "issues-create-issue.md") and [Inviting
a user to a project](projects-members.md#projects-members-add "projects-members.md#projects-members-add").

## Viewing the repositories for a

project

As a member of a project, you can view the source repositories for the project. You
can also choose to create additional repositories. If someone with the
**Space administrator** role has installed and configured the
**GitHub repositories**, **Bitbucket repositories**, or **GitLab repositories** extension, you can also add links to third-party
repositories in the GitHub accounts, Bitbucket workspaces, or GitLab users configured for
the extension. For more information, see
[Creating a source repository](source-repositories-create.md "source-repositories-create.md") and [Quickstart: Installing extensions, connecting providers, and linking resources in CodeCatalyst](extensions-quickstart.md "extensions-quickstart.md").

###### Note

For projects created with the Single-page application blueprint, the default name for
the source repository that contains the sample code is
**`spa-app`**.

###### To navigate to the source repositories for a project

1. Navigate to your project, and do one of the following:
   - On the summary page for your project, choose the repository you want from the list, and then choose **View repository**.
   - In the navigation pane, choose **Code**, and then choose **Source
     repositories**. In **Source repositories**, choose the name of the repository from the list. You can filter the list of repositories by
     typing part of the repository name in the filter bar.

2. On the home page for the repository, view the contents of the repository and information about the associated resources such as the number of
   pull requests and workflows. By default, the contents for the default branch are shown. You can change the view
   by choosing a different branch from the drop-down list.

The overview page for the repository includes information about the workflows and pull
requests that are configured for the branches of this repository and its files. If you
just created the project, the initial workflows to build, test, and deploy the code will
still be running, as they take a few minutes to complete. You can view the related
workflows and their status by choosing the number beneath **Related
workflows**, but this opens the **Workflows** page in
**CI/CD**. For this tutorial, stay on the overview page and explore
the code in the repository. The contents of the `README.md` file are rendered
on this page below the repository files. In **Files**, the contents of
the default branch are shown. You can change the file view to show the contents of
another branch if you have one. The `.codecatalyst` folder contains code
used for other parts of the project, such as workflow YAML files.

To view the content of folders, choose the arrow next to the folder name to expand it.
For example, choose the arrow next to `src` to view the files for the
single-page web application contained in that folder. To view the contents of a file,
choose it from the list. This will open **View files**, where you can
browse the contents of multiple files. You can edit single files in the console as well,
but to edit multiple files, you'll want to create a Dev Environment.

## Creating a Dev Environment

You can add and change files in a source repository in the Amazon CodeCatalyst console.
However, to work effectively with multiple files and branches, we recommend using a
Dev Environment or cloning the repository to your local computer. In this tutorial, we'll
create an AWS Cloud9 Dev Environment with a branch named `develop`. You
can choose a different branch name, but by naming the branch
`develop`, a workflow will automatically run to build and test
your code when you create a pull request later in this tutorial.

###### Tip

If you decide to clone a repository locally instead of or in addition to using a
Dev Environment, make sure that you have Git on your local computer or that your IDE
includes Git. For more information, see [Setting up for working with source repositories](source-setting-up.md "source-setting-up.md").

###### To create a Dev Environment with a new branch

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project where you want to create a Dev Environment.
3. Choose the name of the repository from the list of source repositories for the project.
   Alternatively, in the navigation pane, choose **Code**, choose
   **Source repositories**, and choose the repository for which you
   want to create a Dev Environment.
4. On the repository home page, choose **Create Dev Environment**.
5. Choose a supported IDE from the drop-down menu. See [Supported integrated development environments
   for Dev Environments](devenvironment-create.md#devenvironment-supported-ide "devenvironment-create.md#devenvironment-supported-ide") for more information.
6. Choose the repository to clone, choose **Work in new branch**, enter a branch name into the **Branch
   name** field, and choose a branch off of which to create the new
   branch from the **Create branch from** drop-down menu.
7. Optionally, add an alias for the Dev Environment.
8. Optionally, choose the **Dev Environment configuration** edit button to edit the Dev Environment's compute, storage, or timeout configuration.
9. Choose **Create**. While your Dev Environment is being created, the Dev Environment status column will display **Starting**, and the status column will display **Running** once the Dev Environment has been created. A new tab will open with your Dev Environment in the IDE of your choice. You can edit code and commit and push your changes.

Once you've created the Dev Environment, you can edit files, commit your changes, and push
your changes to the `test` branch. For this tutorial, edit the
content between the `<p>` tags in `App.tsx` file in the
`src` folder to change the text that's displayed on the webpage. Commit
and push your change, and then return to the CodeCatalyst tab.

## To make and push a change

from an AWS Cloud9 Dev Environment

1. In AWS Cloud9, expand the side navigation menu to browse the files. Expand
   `src`, and open `App.tsx`.
2. Make a change the text inside the `<p>` tags.
3. Save the file, and then commit and push your changes by using the Git menu.
   Alternatively, in the terminal window, commit and push your changes with the
   **git commit** and **git push**
   commands.

```
git commit -am "Making an example change"
git push
```

###### Tip

You might need to change directories in the terminal to the Git repository
directory before you can successfully run the Git commands.

## Creating a pull request

You can use pull requests to review code changes collaboratively for minor changes or
fixes, major feature additions, or new versions of your released software. In this
tutorial, you will create a pull request to review the changes you made to the
`test` branch compared to the **main**
branch. Creating a pull request in a project created with a template will also start a
run of its associated workflows, if any.

###### To create a pull request

1. Navigate to your project.
2. Do one of the following:
   - In the navigation pane, choose **Code**, choose **Pull
     requests**, and then choose **Create pull request**.
   - On the repository home page, choose **More**, and then choose
     **Create pull request**.
   - On the project page, choose **Create pull request**.

3. In **Source repository**, make sure that the specified source repository
   is the one that contains the committed code. This option only appears if you did not create
   the pull request from the repository's main page.
4. In **Destination branch**, choose the branch to merge the code into after
   it is reviewed.
5. In **Source branch**, choose the branch that contains the committed code.
6. In **Pull request title**, enter a title that helps other users
   understand what needs to be reviewed and why.
7. (Optional) In **Pull request description**, provide information such as a
   link to issues or a description of your changes.

###### Tip

You can choose **Write description for me** to have CodeCatalyst automatically
generate a description of the changes contained in the pull request. You can make changes to the
automatically generated description after you add it to the pull request.

This functionality requires that generative AI features are enabled for the space
and is not available for pull requests in linked repositories. For more information, see
[Managing
generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md"). 8. (Optional) In **Issues**, choose **Link issues**, and
then either choose an issue from the list or enter its ID. To unlink an issue, choose the
unlink icon. 9. (Optional) In **Required reviewers**, choose **Add required
reviewers**. Choose from the list of project members to add them. Required
reviewers must approve the changes before the pull request can be merged into the destination
branch.

###### Note

You cannot add a reviewer as both a required reviewer and an optional reviewer. You
cannot add yourself as a reviewer. 10. (Optional) In **Optional reviewers**, choose **Add optional
reviewers**. Choose from the list of project members to add them. Optional
reviewers do not have to approve the changes as a requirement before the pull request can be
merged into the destination branch. 11. Review the differences between the branches. The difference displayed in a pull request is
the changes between the revision in the source branch and the merge base, which is the head
commit of the destination branch at the time the pull request was created. If no changes display, the branches might be
identical, or you might have chosen the same branch for both the source and the destination. 12. When you are satisfied that the pull request contains the code and changes you want
reviewed, choose **Create**.

###### Note

After you create the pull request, you can add comments. Comments can be added to the
pull request or to individual lines in files as well as to the overall pull request. You can
add links to resources, such as files, by using the @ sign followed by the name of the
file.

You can view information about associated workflows started by the creation of this
pull request by choosing **Overview** and then reviewing the
information in the **Pull request details** area under
**Workflow runs**. To view the workflow run, choose the run.

###### Tip

If you named your branch something other than `develop`, a
workflow will not automatically run to build and test your changes. If you want to
configure that, edit the YAML file for the
**onPullRequestBuildAndTest** workflow. For more information,
see [Creating a workflow](workflows-create-workflow.md "workflows-create-workflow.md").

You can comment on this pull request and ask other project members to comment on it.
You can also choose to add or change optional or required reviewers. You can choose to
make more changes to the source branch for the repository, and see how those committed
changes create revisions for the pull request. For more information, see [Reviewing a pull request](pull-requests-review.md "pull-requests-review.md"), [Updating a pull request](pull-requests-update.md "pull-requests-update.md"), [Reviewing code with pull requests in
Amazon CodeCatalyst](source-pull-requests.md "source-pull-requests.md"), and [Viewing workflow run status and details](workflows-view-run.md "workflows-view-run.md") .

## Merging a pull

request

Once a pull request has been reviewed and has received approvals from required
reviewers, you can merge its source branch to the destination branch in the CodeCatalyst
console. Merging a pull request will also start a run of the changes through any
workflows associated with the destination branch. In this tutorial, you'll merge the
test branch into main, which will start a run of the
**onPushToMainDeployPipeline** workflow.

###### To merge a pull request (console)

1. In **Pull requests**, choose the pull request you created in
   the previous step. In the pull request, choose
   **Merge**.
2. Choose from the available merge strategies for the pull request. Optionally
   select or deselect the option to delete the source branch after merging the pull
   request, and then choose **Merge**. After the merge completes,
   the status of the pull request changes to **Merged** and no
   longer appears in the default view of pull requests. The default view shows pull
   requests with a status of **Open**. You can still view a merged
   pull request, but you cannot approve it or change its status.

###### Note

If the **Merge** button is not active, or you see the
**Not mergeable** label, either a required reviewer has
not yet approved the pull request, or the pull request cannot be merged in
the CodeCatalyst console. A reviewer who has not approved a pull request is
indicated by a clock icon in **Overview** in the
**Pull request details** area. If all required
reviewers have approved the pull request but the **Merge**
button is still not active, you might have a merge conflict, or you have
exceeded the storage quota for the space. You can resolve merge conflicts
for the destination branch in a Dev Environment, push the changes, and then
merge the pull request, or you can resolve conflicts and merge locally, and
then push the commit that contains the merge to CodeCatalyst. For more
information, see [Merging a pull request (Git)](pull-requests-merge.md#pull-requests-merge-git "pull-requests-merge.md#pull-requests-merge-git") and your Git documentation.

## Viewing the deployed

code

Now it's time to view the originally deployed code that was in the default branch, and
your merged changes once they are automatically built, tested, and deployed. To do so,
you can return to the overview page for the repository and choose the number next to the
related workflows icon, or in the navigation pane, choose **CI/CD**,
and then choose **Workflows**.

###### To view the deployed code

1. In **Workflows**, in `onPushToMainDeployPipeline`,
   expand **Recent runs**.

###### Note

This is the default name of the workflow for projects created with the
**Single-page application** blueprint. 2. The most recent run is the one started by your merged pull request commit to
the `main` branch and will likely show a status of **In
progress**. Choose a successfully completed run from the list to
open the details of that run. 3. Choose **Variables**. Copy the value for
**AppURL**. This is the URL for the deployed single page
web application. Open a new browser tab and paste in the value to view the built
and deployed code. Leave the tab open. 4. Return to the list of workflow runs and wait for the most recent run to
complete. When it does, return to the tab you opened to view the web application
and refresh your browser. You should see the changes that you made in your
merged pull request.

## Cleaning up resources

Once you've explored working with a source repository and pull request, you might want
to remove any resources you don't need. You cannot delete pull requests, but you can
close them. You can delete any branches you created.

If you no longer need the source repository or the project, you can also delete those resources. For more information, see
[Deleting a source repository](source-repositories-delete.md "source-repositories-delete.md") and [Deleting a project](projects-delete.md "projects-delete.md").
