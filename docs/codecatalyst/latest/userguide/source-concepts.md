Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Source repository concepts

Here are some concepts to know about as you work with CodeCatalyst source repositories.

###### Topics

- [Projects](#project-concept "#project-concept")
- [Source repositories](#source-repository-concept "#source-repository-concept")
- [Dev Environments](#devenvironment-concept "#devenvironment-concept")
- [Personal access tokens (PATs)](#personal-access-token-concept "#personal-access-token-concept")
- [Branches](#branches-concept "#branches-concept")
- [Default branches](#default-branch-concept "#default-branch-concept")
- [Commits](#commits-concept "#commits-concept")
- [Pull requests](#pull-request-concept "#pull-request-concept")
- [Revisions](#revision-concept "#revision-concept")
- [Workflows](#workflow-concept "#workflow-concept")

## Projects

A _project_ represents a collaborative effort in CodeCatalyst that supports development teams and tasks. After
you have a project, you can add, update, or remove users and resources, customize your project dashboard, and monitor the progress of
your team's work. You can have multiple projects within a space.

Source repositories are specific to the projects where you create or link them in a
space. You can't share a repository between projects, and you can't link a repository to
more than one project in a space. Users with the **Contributor** or **Project administrator**
role in a project can interact with the source repositories associated with that project
according to the permissions granted to those roles. For more information, see [Granting access with user roles](ipa-roles.md "ipa-roles.md").

## Source repositories

A _source repository_ is where you securely store code and files for your
project. It also stores the version history of your files. By default, a source repository is
shared with the other users in your CodeCatalyst project. You can have more than one source
repository for a project. You can create source repositories for projects in CodeCatalyst, or you can
choose to link an existing source repository hosted by another service if that service is supported by
an installed extension. For example, you can link a GitHub repository to a project after you install the
**GitHub Repositories** extension. For more information, see [Storing source code in repositories for a project in
CodeCatalyst](source-repositories.md "source-repositories.md") and [Quickstart: Installing extensions, connecting providers, and linking resources in CodeCatalyst](extensions-quickstart.md "extensions-quickstart.md").

## Dev Environments

A _Dev Environment_ is a cloud-based development environment that you can use
in CodeCatalyst to quickly work on the code stored in the source repositories of your project. The
project tools and application libraries included in your Dev Environment are defined by a devfile in
the source repository of your project. If you do not have a devfile in your source repository, a
default devfile will be applied automatically. The default devfile includes tools for the most
frequently used programming languages and frameworks. By default, a Dev Environment is configured to
have a 2-core processor, 4 GB of RAM, and 16 GiB of persistent storage.

You can choose to clone an existing branch of your source repository into your Dev Environment,
or you can choose to create a new branch as part of creating the Dev Environment.

## Personal access tokens (PATs)

A _personal access token_ (PAT) is similar to a password. It
is associated with your user identity for use across all spaces and projects in CodeCatalyst. You
use PATs to access CodeCatalyst resources that include integrated development environments (IDEs) and
Git-based source repositories. PATs represent you in CodeCatalyst and you can manage them in your user
settings. A user can have more than one PAT. Personal access tokens only display once. As a best
practice, be sure to store them securely on your local computer. By default, PATs expire after one
year.

When working with integrated development environments (IDEs), PATs are the equivalent of a
Git password. Provide the PAT when asked for a password when setting up your IDE to work with a
Git repository. For more information about how to connect your IDE with a Git-based repository,
see the documentation for your IDE.

## Branches

A _branch_ is a pointer or reference to a commit in Git and in CodeCatalyst. You
can use branches to organize your work. For example, you can use branches to work on a new or
different version of files without affecting files in other branches. You can use branches to
develop new features, store a specific version of your project, and more. A source repository can
have one branch or many branches. When you create a project using a template, the source
repository created for the project contains sample files in a branch called
**main**. The **main** branch is the default branch for the
repository.

## Default branches

Source repositories in CodeCatalyst have a default branch regardless of how you create them. If
you choose to create a project using a template, the source repository created for that project
includes a README.md file in addition to sample code, workflow definitions, and other resources.
If you create a source repository without using a template, a README.md file is added for you as
a first commit and a default branch is created for you as part of creating the repository. This
default branch is named _main_. This default branch is the one used as the
base or default branch in local repositories (repos) when users clone the repository. You can
change which branch is used as the default branch. For more information, see [Managing the default branch for a
repository](source-branches-default-branch.md "source-branches-default-branch.md").

You can't delete the default branch for a source repository. Search results only
include results from the default branch.

## Commits

A _commit_ is a change to a file or set of files. In the Amazon CodeCatalyst
console, a commit saves your changes and pushes them to a source repository. The
commit includes information about the change, including the identity of the user who made the
change, the time and date of the change, the commit title, and any message included about the
change. For more information, see [Understanding
changes in source code with commits in Amazon CodeCatalyst](source-commits.md "source-commits.md").

In the context of a source repository in CodeCatalyst, commits are snapshots of the contents and
changes to the contents of your repository. You can also add Git tags to commits, to identify
specific commits.

## Pull requests

A _pull request_ is the primary way you and other users review, comment on,
and merge code changes from one branch to another in a source repository. You can use pull
requests to review code changes collaboratively for minor changes or fixes, major feature
additions, or new versions of your released software. In a pull request, you can review the
changes between the source and destination branches or the differences between revisions of those
branches. You can add comments to individual lines of code changes as well as comments on the pull
request overall.

###### Tip

While you are creating a pull request, the difference displayed is the difference between
the tip of the source branch and the tip of the destination branch. Once the pull request has
been created, the displayed difference will be between the revision of the pull request you
choose and the commit that was the tip of the destination branch when you created the pull
request. For more information about differences and merge bases in Git, see [git-merge-base](https://git-scm.com/docs/git-merge-base "https://git-scm.com/docs/git-merge-base") in the Git
documentation.

## Revisions

A _revision_ is an updated version of a pull request. Each push to the
source branch of a pull request creates a revision that contains the changes made in the commits
included in that push. You can view the differences between revisions of a pull request in
addition to the differences between the source and destination branches. For more information, see
[Reviewing code with pull requests in
Amazon CodeCatalyst](source-pull-requests.md "source-pull-requests.md").

## Workflows

A _workflow_ is an automated procedure that describes how to build, test,
and deploy your code as part of a continuous integration and continuous delivery (CI/CD) system.
A workflow defines a series of steps, or _actions_, to take during a workflow
run. A workflow also defines the events, or _triggers_, that cause the
workflow to start. To set up a workflow, you create a _workflow definition
file_ using the CodeCatalyst console's
[visual
or YAML editor](flows.md#workflow.editors "flows.md#workflow.editors").

###### Tip

For a quick look at how you might use workflows in a project, [create a project with a blueprint](projects-create.md#projects-create-console-template "projects-create.md#projects-create-console-template"). Each blueprint deploys a functioning workflow
that you can review, run, and experiment with.

A source repository can also store the configuration files and other information for
workflows, notifications, issues, and other configuration information for the project. The
configuration files are created and stored in the source repository when you create resources
that require configuration files, or when you specify the repository as a source action for a
workflow. If you create a project from a blueprint, you will have configuration files already
stored in the source repository created for you as part of the project. This configuration
information is stored in a folder named `.codecatalyst` in the default branch of your
repository. Whenever you create a branch of the default branch, you create a copy of this folder
and its configuration in addition to all the other files and folders in that branch.
