

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# CodeCatalyst concepts
<a name="concepts"></a>

Get familiar with the key concepts to help speed up your collaboration and application development in Amazon CodeCatalyst. These concepts include terms used in source control, continuous integration and continuous delivery (CI/CD), and modeling and configuring automated release processes.

For additional conceptual information, see the following topics:
+ [Source repository concepts](source-concepts.md)
+ [Workflows concepts](workflows-concepts.md)

**Topics**
+ [AWS Builder ID spaces in CodeCatalyst](#concepts-spaces)
+ [Spaces that support identity federation in CodeCatalyst](#space-federated)
+ [Projects](#project-concept)
+ [Blueprints](#templates-concept)
+ [Account connections](#account-connections-concept)
+ [VPC connections](#vpc-connections-concept)
+ [AWS Builder ID](#sign-in-concept)
+ [User profiles in CodeCatalyst](#user-profile-concept)
+ [Source repositories](#source-repositories-concept)
+ [Commits](#commits-concept)
+ [Dev Environments](#devenvironment-concept)
+ [Workflows](#workflow-concept)
+ [Actions](#action-concept)
+ [Issues](#issues-concept)
+ [Personal access tokens (PATs)](#personal-access-token-concept)
+ [Personal connections](#personal-connection-concept)
+ [Roles](#role-concept)

## AWS Builder ID spaces in CodeCatalyst
<a name="concepts-spaces"></a>

The space administrator invites users to CodeCatalyst by sending individual invitation emails from the members page. Users who are invited or sign up to CodeCatalyst create their own AWS Builder ID. The profile is managed in AWS Builder ID and displays as the user name and profile information in the user settings in CodeCatalyst.

## Spaces that support identity federation in CodeCatalyst
<a name="space-federated"></a>

Users who have been added to the SSO users and groups for the IAM Identity Center instance and are managed in the identity store and are invited to your space through IAM Identity Center. The **Space administrator** syncs the CodeCatalyst members page for the latest updates. Users sign in using the SSO sign-in portal as set up in the company IAM Identity Center instance. Spaces that support identity federation are connected to the identity store instance through the Identity Center application and its mapping to the identity store ID.

## Projects
<a name="project-concept"></a>

A *project* represents a collaborative effort in CodeCatalyst that supports development teams and tasks. After you have a project, you can add, update, or remove users and resources, customize your project dashboard, and monitor the progress of your team's work. You can have multiple projects within a space.

For more information about projects, see [Organize work with projects in CodeCatalyst](projects.md).

## Blueprints
<a name="templates-concept"></a>

A *blueprint* is a project synthesizer that generates and extends application support files and dependencies for you, along with creating your CodeCatalyst project in the console. You choose a project type from a selection of blueprints in CodeCatalyst, view the README file, and preview the project repository and resources that will be generated. Your project is generated from the base configuration specified by the blueprint. You synthesize to the project blueprint periodically, which updates your project files, such as software dependencies, and regenerates resources. Projects use a tool called Projen to synthesize projects by syncing the latest project updates and generating support files. These files may include `package.json`, `Makefile`, `eslint`, and more based on your application type and language. Project blueprints can generate files supporting AWS resources such as CDK constructs, CloudFormation templates, and AWS Serverless Application Model templates.

For more information about project blueprints, see [Creating a comprehensive project with CodeCatalyst blueprints](project-blueprints.md).

## Account connections
<a name="account-connections-concept"></a>

An *account connection* associates a CodeCatalyst space with your AWS account. After your account connection is set up, the AWS account is made available to the space. You can then add IAM roles to CodeCatalyst so that it can access resources in your AWS account. You can also use these roles for your CodeCatalyst workflow actions.

You can limit which projects and resources have access to account connections by enabling project-restricted account connections. *Project-restricted account connections* are connected AWS accounts that can only be accessed by specified projects in the space. This allows teams in a space to restrict use of AWS accounts for integrated AWS resources by project. For example, the account used for deployment workflows and VPC connections in specific projects will only be available with a project-restricted account connection. For more information, see [Configuring project-restricted account connections](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-accounts.html#managing-accounts-restriction).

For more information about account connections, see [Allowing access to AWS resources with connected AWS accounts](ipa-connect-account.md).

## VPC connections
<a name="vpc-connections-concept"></a>

A *VPC connection* is a CodeCatalyst resource which contains all of the configurations needed for your workflow to access a VPC. Space administrators can add their own VPC connections in the Amazon CodeCatalyst console on behalf of space members. By adding a VPC connection, space members can run workflow actions and create Dev Environments that adhere to network rules and can access resources in the associated VPC.

For more information about VPC connections, see [ Managing Amazon Virtual Private Clouds](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.html) in the *CodeCatalyst Administrator Guide*.

## AWS Builder ID
<a name="sign-in-concept"></a>

An AWS Builder ID is a personal identity you can use to sign up and sign in to CodeCatalyst and other participating applications. It is not the same as an AWS account. Your AWS Builder ID manages metadata such as user alias and email address. Your AWS Builder ID is a unique identity that supports users across all spaces in CodeCatalyst. For information about accessing your AWS Builder ID profile, see [Updating a profile](your-profile.md). To learn more about AWS Builder ID, see [AWS Builder ID](https://docs.aws.amazon.com/general/latest/gr/aws_builder_id.html) in the AWS General Reference. 

For more information about signing up and signing in, see [Set up and sign in to CodeCatalyst](setting-up-topnode.md).

## User profiles in CodeCatalyst
<a name="user-profile-concept"></a>

You access your CodeCatalyst user profile by choosing the profile option from the drop-down under your login initials on any page in CodeCatalyst. You can create personal access tokens (PATs) from your profile page, but you can only view or delete PATs using the AWS CLI. Your user name is the alias you chose when you signed up. You cannot change your user name. To view the profile page for another CodeCatalyst user, go to the **Members** tab for your project and choose the appropriate user.

You access your AWS Builder ID by viewing your CodeCatalyst profile and then choosing to go to AWS Builder ID. You will be redirected to your AWS Builder ID profile page. Your profile's full name, email address, and password are managed by your AWS Builder ID, and you can edit that information using the AWS Builder ID page. You entered this information when you signed up. When you are ready to set up MFA to use an authenticator application for signing in, you will use the AWS Builder ID page. For more information about viewing your AWS Builder ID profile, see [Updating a profile](your-profile.md).

For more information about signing up and signing in, see [Set up and sign in to CodeCatalyst](setting-up-topnode.md).

## Source repositories
<a name="source-repositories-concept"></a>

A *source repository* is where you securely store code and files for your project. It also stores the version history of your files. By default, a source repository is shared with the other users in your CodeCatalyst project. You can have more than one source repository for a project. You can create source repositories for projects in CodeCatalyst, or you can choose to link an existing source repository hosted by another service if that service is supported by an installed extension. For example, you can link a GitHub repository to a project after you install the **GitHub Repositories** extension. For more information, see [Storing source code in repositories for a project in CodeCatalyst](source-repositories.md) and [Quickstart: Installing extensions, connecting providers, and linking resources in CodeCatalyst](extensions-quickstart.md).

Source repositories are also where configuration information is stored for your CodeCatalyst project, such as the configuration file that defines the attributes and actions of your CI/CD workflow. If you create your project using a blueprint, a source repository will be created with project configuration information stored inside it. If you create an empty project, you must create a source repository before you can create resources that require configuration information, such as workflows.

For more concepts that can help you work with source repositories and source control, see [Source repository concepts](source-concepts.md).

## Commits
<a name="commits-concept"></a>

A *commit* is a change to a file or set of files. In the Amazon CodeCatalyst console, a commit saves your changes and pushes them to a source repository. The commit includes information about the change, including the identity of the user who made the change, the time and date of the change, the commit title, and any message included about the change. For more information, see [Understanding changes in source code with commits in Amazon CodeCatalyst](source-commits.md).

In the context of a source repository in CodeCatalyst, commits are snapshots of the changes to the contents of your repository. Every time a user commits and pushes a change, CodeCatalyst saves information that includes who committed the change, the date and time of the commit, and the changes made as part of the commit. You can also add Git tags to commits to help identify specific commits.

For more information about commits, see [Understanding changes in source code with commits in Amazon CodeCatalyst](source-commits.md).

## Dev Environments
<a name="devenvironment-concept"></a>

A *Dev Environment* is a cloud-based development environment that you can use in CodeCatalyst to quickly work on the code stored in the source repositories of your project. The project tools and application libraries included in your Dev Environment are defined by a devfile in the source repository of your project. If you do not have a devfile in your source repository, a default devfile will be applied automatically. The default devfile includes tools for the most frequently used programming languages and frameworks. By default, a Dev Environment is configured to have a 2-core processor, 4 GB of RAM, and 16 GiB of persistent storage.

## Workflows
<a name="workflow-concept"></a>

A *workflow* is an automated procedure that describes how to build, test, and deploy your code as part of a continuous integration and continuous delivery (CI/CD) system. A workflow defines a series of steps, or *actions*, to take during a workflow run. A workflow also defines the events, or *triggers*, that cause the workflow to start. To set up a workflow, you create a *workflow definition file* using the CodeCatalyst console's [visual or YAML editor](https://docs.aws.amazon.com/codecatalyst/latest/userguide/flows.html#workflow.editors).

**Tip**  
For a quick look at how you might use workflows in a project, [create a project with a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-create.html#projects-create-console-template). Each blueprint deploys a functioning workflow that you can review, run, and experiment with.

For more information about workflows, see [Build, test, and deploy with workflows](workflow.md).

## Actions
<a name="action-concept"></a>

An *action* is the main building block of a workflow, and defines a logical unit of work, or task, to perform during a workflow run. Typically, a workflow includes multiple actions that run sequentially or in parallel depending on how you've configured them.

For more information about actions, see [Configuring workflow actions](workflows-actions.md).

## Issues
<a name="issues-concept"></a>

An *issue* is a record that tracks the work related to your project. You can create an issue for a feature, a task, a bug, or any other body of work related to your project. If you're using agile development, an issue can also describe an epic or user story. 

For more information about issues, see [Track and organize work with issues in CodeCatalyst](issues.md).

## Personal access tokens (PATs)
<a name="personal-access-token-concept"></a>

A *personal access token* (PAT) is similar to a password. It is associated with your user identity for use across all spaces and projects in CodeCatalyst. You use PATs to access CodeCatalyst resources that include integrated development environments (IDEs) and Git-based source repositories. PATs represent you in CodeCatalyst and you can manage them in your user settings. A user can have more than one PAT. Personal access tokens only display once. As a best practice, be sure to store them securely on your local computer. By default, PATs expire after one year.

For more information about PATs, see [Grant users repository access with personal access tokens](ipa-tokens-keys.md).

## Personal connections
<a name="personal-connection-concept"></a>

A *personal connection* is an authorization between your CodeCatalyst identity and your external source provider, such as GitHub. You use personal connections to allow a CodeCatalyst user to add third-party source repositories. For example, you can connect a GitHub repository to a CodeCatalyst space. An installed connector application is installed in the GitHub account for use with repositories designated by the account owner. You can create one personal connection for one user identity (CodeCatalyst alias) across all spaces for a specific provider type, such as GitHub. Personal connections are either associated with your AWS Builder ID or your SSO user.

For more information, see [Accessing GitHub resources with personal connections](ipa-settings-connections.md).

## Roles
<a name="role-concept"></a>

A *role* defines a user's access to the resources for a project or a space and which actions that user can take. You choose the role for a user when you invite them to a project. There are space-level roles and project-level roles in CodeCatalyst. A user with an administrative role at the correct level can change assigned roles. For example, a user with the **Project administrator** role for a project has full control over that project and can change the roles of users in that project. For information about which roles are available and which permissions each role has, see [Granting access with user roles](ipa-roles.md).

For more information about roles, see [Granting access with user roles](ipa-roles.md).