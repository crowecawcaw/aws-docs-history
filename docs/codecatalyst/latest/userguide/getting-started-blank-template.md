Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Tutorial: Starting with an empty project and

manually adding resources

You can create an empty project without any predefined resources inside it by choosing the
**Empty
project** blueprint when you create the project. After you create
an empty project, you can create and add resources to it according to your project needs.
Because
projects created without a blueprint are empty on creation, this option requires more knowledge
of creating and configuring CodeCatalyst resources to get started.

###### Topics

- [Prerequisites](#getting-started-bt-prerequisites "#getting-started-bt-prerequisites")
- [Create an empty project](#getting-started-bt-proj-create "#getting-started-bt-proj-create")
- [Create a source repository](#getting-started-bt-source-create "#getting-started-bt-source-create")
- [Create a workflow to build, test, and deploy
  a code change](#getting-started-bt-workflow-create "#getting-started-bt-workflow-create")
- [Invite someone to your project](#getting-started-bt-ipa-user "#getting-started-bt-ipa-user")
- [Create issues to collaborate on and track work](#getting-started-bt-issue "#getting-started-bt-issue")

## Prerequisites

To create an empty project, you must have the **Space administrator** or
**Power user** role assigned to you. If this is your first time signing
in to CodeCatalyst, see [Set up and sign in to CodeCatalyst](setting-up-topnode.md "setting-up-topnode.md").

## Create an empty project

Creating a project is the first step in being able to work together.
If
you want to create your own resources, such as source repositories and workflows, you can start
with an empty project.

###### To create an empty project

1. Navigate to the space where you want to create a project.
2. On the space dashboard, choose **Create project**.
3. Choose **Start from scratch**.
4. Under **Give a name to your project**, enter the name that you want to assign to your project. The name must be unique within your space.
5. Choose **Create project**.

Now that you have an empty project, the next step is to create a source repository.

## Create a source repository

Create a source repository to store and collaborate on your project's code. Project members
can clone this repository to their local computers to work on code. Alternatively, you can choose
to link a repository hosted in a supported service, but that is not covered in this tutorial. For
more information, see [Linking a source repository](source-repositories-link.md "source-repositories-link.md").

###### To create a source repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your project.
3. In the navigation pane, choose **Code**, and then choose **Source
   repositories**.
4. Choose **Add repository**, and then choose **Create
   repository**.
5. In **Repository name**, provide a name for the repository. In this guide,
   we use `codecatalyst-source-repository`, but you can choose a
   different name.
   Repository names must be unique within a project. For more information about requirements for
   repository names, see [Quotas for source repositories in CodeCatalyst](source-quotas.md "source-quotas.md").
6. (Optional) In **Description**, add a description for the repository that
   will help other users in the project understand what the repository is used for.
7. Choose **Create repository (default)**. This option creates a repository
   that includes a default branch and a README.md file. Unlike an empty repository, you can use
   this repository as soon as it's created.
8. In **Default branch**, leave the name as _main_ unless you have a reason to choose a different name. The examples in this
   guide all use the name _main_ for the default branch.
9. (Optional) Add a `.gitignore` file for the type of code you plan to push.
10. Choose **Create**.

###### Note

CodeCatalyst adds a `README.md` file to your repository when you create it. CodeCatalyst
also creates an initial commit for the repository in a default branch named
**main**. You can edit or delete the README.md file, but you can't
delete
the default branch.

You can quickly add code in your repository by creating a Dev Environment. For this tutorial,
we recommend that you create a Dev Environment using AWS Cloud9, and choose the option to create a branch from the **main** branch when creating the
Dev Environment. We use the name `test` for this branch, but you can enter a different branch name if you prefer.

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

## Create a workflow to build, test, and deploy

a code change

In CodeCatalyst, you organize the building, testing, and deployment of your applications or
services in workflows. Workflows consist of actions and can be configured to run automatically
after specified source repository events occur, such as code pushes or opening or updating a pull
request. For more information about workflows, see [Build, test, and deploy with workflows](workflow.md "workflow.md").

Follow the instructions in [Getting started with workflows](workflows-getting-started.md "workflows-getting-started.md") to create your first workflow.

## Invite someone to your project

Now
that you've set up your custom project, invite others to work with you.

###### To invite someone to your project

1. Navigate to the project to which you want to invite users.
2. In the navigation pane, choose **Project settings**.
3. On the **Members** tab, choose **Invite**.
4. Type the email addresses of the people you want to invite as users for your project. You
   can type multiple email addresses separated by a space or a comma. You can also choose from
   members of your space who are not members of the project.
5. Choose the role for the user.

When you have finished adding users, choose **Invite**.

## Create issues to collaborate on and track work

CodeCatalyst helps you track features, tasks, bugs, and any other work involved in your project
with issues. You can create issues to track needed work and ideas. By default, when you create an
issue it is added to your backlog. You can move issues to a board where you track work in
progress. You can also assign an issue to a specific project member.

###### To create an issue for a project

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").

Make sure that you are navigating in the project where you want to create issues. To view
all projects, in the navigation pane, choose **Amazon CodeCatalyst**, and if needed,
choose **View all projects**. Choose the project where you want to create or
work with issues. 2. In the navigation pane, choose **Track**, and then choose **Backlog**. 3. Choose **Create issue**. 4. In **Issue title**, provide a name for the issue. Optionally provide a description of the issue. Choose the status, priority, and estimate
for the issue if desired. You can also assign the issue to a project member from the list of project members.

###### Tip

You can choose to assign an issue to **Amazon Q** to have Amazon Q
try to solve the issue. If the attempt is successful, a pull request will be created and the
status of the issue will change to **In review** so that you can review and
test the code. For more information, see [Tutorial: Using CodeCatalyst generative AI
features to speed up your development work](getting-started-project-assistance.md "getting-started-project-assistance.md").

This functionality requires that generative AI features are enabled for the space.
For more information, see [Managing generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md"). 5. Choose **Save**.

After you have created issues, you can assign them to project members, estimate them, and
track them on a Kanban board. For more information, see [Track and organize work with issues in CodeCatalyst](issues.md "issues.md").
