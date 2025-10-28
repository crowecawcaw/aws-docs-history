Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Creating a project

With CodeCatalyst projects, you can conduct development tasks with shared continuous
integration/continuous delivery (CI/CD) workflows and repositories, manage resources, track
issues, and add users.

Before you create a project, you must have the **Space administrator** or
**Power user** role.

###### Topics

- [Creating an empty project in Amazon CodeCatalyst](#projects-create-empty "#projects-create-empty")
- [Creating a project with a linked third-party
  repository](#projects-create-3p-repo "#projects-create-3p-repo")
- [Creating a project with a
  blueprint](#projects-create-console-template "#projects-create-console-template")
- [Best practices when using Amazon Q to create projects
  or add functionality with blueprints](#projects-create-amazon-q "#projects-create-amazon-q")
- [Best practices for using blueprints with
  projects](#projects-create-use-blueprints "#projects-create-use-blueprints")
- [Adding resources and tasks to created projects](#projects-create-after-steps "#projects-create-after-steps")

## Creating an empty project in Amazon CodeCatalyst

You can create an empty project with no resources and manually add the resources you want
at a later time.

Before you create a project, you must have the **Space administrator** or
**Power user** role.

###### To create an empty project

1. Navigate to the space where you want to create a project.
2. On the space dashboard, choose **Create project**.
3. Choose **Start from scratch**.
4. Under **Give a name to your project**, enter the name that you want to assign to your project. The name must be unique within your space.
5. Choose **Create project**.

## Creating a project with a linked third-party

repository

You can keep your project's source code in a preferred third-party provider and still
use all the CodeCatalyst features such as blueprints, lifecycle management, workflows, and more. To do
this, you can create a new CodeCatalyst project that links to a GitHub repository, Bitbucket repository,
or a GitLab project repository. You can then use your linked source repository in your CodeCatalyst
project.

Before you create a CodeCatalyst project, you must have the
**Space administrator** or **Power user** role. For
more information, see [Creating a space](spaces-create.md "spaces-create.md") and [Inviting a user directly to a space](spaces-members-add-admin.md "spaces-members-add-admin.md") .

To create a project in CodeCatalyst that links to a source repository in your GitHub account,
you'll need to complete the following three tasks:

1. Install the **GitHub repositories**, **Bitbucket repositories**, or **GitLab repositories** extension. You're
   prompted in an external site to connect and provide CodeCatalyst with access to your repository,
   which is done as part of the next step.

###### Important

To install the **GitHub repositories**, **Bitbucket repositories**, or **GitLab repositories** extension to your
CodeCatalyst space, you must be signed in with an account that has the **Space administrator** role in the
space. 2. Connect your GitHub account or Bitbucket workspace, or GitLab user to CodeCatalyst.

###### Important

To connect your GitHub account, Bitbucket workspace, GitLab user to your CodeCatalyst space, you must be both the
third-party source's administrator and the CodeCatalyst **Space administrator**.

###### Important

After you install a repository extension, any repositories you link to CodeCatalyst will have
their code indexed and stored in CodeCatalyst. This will make the code searchable in
CodeCatalyst. To better understand the data protection for your code when using linked
repositories in CodeCatalyst, see [Data protection](data-protection.md "data-protection.md")
in the _Amazon CodeCatalyst User Guide_. 3. Create a CodeCatalyst project linked to your GitHub repository, Bitbucket repository, or GitLab project repository.

###### Important

While you can link a GitHub repository, Bitbucket repository, or GitLab project repository as a
**Contributor**, you can only unlink a third-party repository as the **Space administrator**
or the **Project administrator**. For more information, see [Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

###### Important

CodeCatalyst doesn't support detecting changes in the default branch for linked
repositories. To change the default branch for a linked repository, you must first unlink it
from CodeCatalyst, change the default branch, and then link it again. For more information,
see [Linking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-link.md "extensions-link.md").

As a best practice, always make sure you have the latest version of the extension
before you link a repository.

###### Note

    * A GitHub repository, Bitbucket repository, or GitLab project repository can only be linked to one CodeCatalyst
     project in a space.
    * You can't use empty or archived GitHub repositories, Bitbucket repositories, or GitLab project
     repositories with CodeCatalyst projects.
    * You can't link a GitHub repository, Bitbucket repository, or GitLab project repository that has the
     same name as a repository in a CodeCatalyst project.
    * The **GitHub repositories** extension isn't compatible with GitHub Enterprise Server repositories.
    * The **Bitbucket repositories** extension isn't compatible with Bitbucket Data Center repositories.
    * The **GitLab repositories** extension isn't compatible with GitLab self-managed project repositories.
    * You can't use the **Write description for me** or
     **Summarize comments** features with linked repositories.
     These features are only available in pull requests in CodeCatalyst.

For more information, see [Add functionality to projects with extensions in CodeCatalyst](extensions.md "extensions.md").

###### To install the third-party extension

1. Navigate to the space where you want to create a project.
2. On the space dashboard, choose **Create project**.
3. Choose **Bring your own code**.
4. Under **Link existing repository**, choose **GitHub repositories**, **Bitbucket repositories**, **GitLab repositories** depending on the third-party repository
   provider you want to use. You're prompted to connect your GitHub account, Bitbucket workspace, or GitLab account if you didn't do
   so previously. If the third-party extension of your choice isn't already installed, an install prompt displays.
5. If prompted, choose **Install**. Review the permissions required by the extension,
   and if you want to continue, choose **Install** again.

After you install the third-party extension, the next step is to connect your GitHub account, Bitbucket workspace, or GitLab user
to your CodeCatalyst space.

**To connect your GitHub account, Bitbucket workspace, or GitLab user to CodeCatalyst**

Do one of the following depending on the third-party extension you chose to configure:

- **GitHub repositories**: Connect to a GitHub account.

      1. Choose **Connect GitHub account** to go to the external site for GitHub.
      2. Sign in to your GitHub account using your GitHub credentials, and then choose the
       account where you want to install Amazon CodeCatalyst.


      ###### Tip

      If you have previously connected a GitHub account to the space, you will not be
       prompted to reauthorize. You will instead see a dialog box asking you where you would
       like to install the extension if you are a member or collaborator in more than one
       GitHub space, or the configuration page for the Amazon CodeCatalyst application if you only
       belong to one GitHub space. Configure the application for the repository access
       that you want to allow, and then choose **Save**. If the
       **Save** button is not active, make a change to the configuration,
       and then try again.
      3. Choose whether you want to allow CodeCatalyst to access all current and future repositories,
       or choose the specific GitHub repositories you want to use in CodeCatalyst.
       The
       default option is to include all GitHub repositories in the GitHub account, including
       future repositories that will be accessed by
       CodeCatalyst.
      4. Review the permissions given to CodeCatalyst, and then choose
       **Install**.

  After connecting your GitHub account to CodeCatalyst, you're taken to the **GitHub repositories** extension details
  page, where you can view and manage connected GitHub accounts and linked GitHub repositories.

- **Bitbucket repositories**: Connect to a Bitbucket workspace.

      1. Choose **Connect Bitbucket workspace** to go to the external site for Bitbucket.
      2. Sign into your Bitbucket workspace using your Bitbucket credentials and review the permissions given to CodeCatalyst.
      3. From the **Authorize for workspace** dropdown menu, choose the Bitbucket workspace you want to
       provide CodeCatalyst access to, and then choose **Grant access**.


      ###### Tip

      If you have previously connected a Bitbucket workspace to the space, you will not be prompted
       to reauthorize. You will instead see a dialog asking you where you would like to
       install the extension if you're a member or collaborator in more than one Bitbucket
       workspace, or the configuration page for the Amazon CodeCatalyst application if you only
       belong to one Bitbucket workspace. Configure the application for the workspace access
       you want to allow, and then choose **Grant access**. If the
       **Grant access** button is not active, make a change to the configuration,
       and then try again.

  After connecting your Bitbucket workspace to CodeCatalyst, you're taken to the **Bitbucket repositories** extension details
  page, where you can view and manage connected Bitbucket workspaces and linked Bitbucket repositories.

- **GitLab repositories**: Connect to a GitLab user.

      1. Choose **Connect GitLab user** to go to the external site for GitLab.
      2. Sign in to your GitLab user using your GitLab credentials and review the permissions given to CodeCatalyst.


      ###### Tip

      If you have previously connected a GitLab user to the space, you will not be
       prompted to reauthorize. You will instead be navigated back to the CodeCatalyst console.
      3. Choose **Authorize AWS Connector for GitLab**.

  After connecting your GitLab user to CodeCatalyst, you're taken to the **GitLab repositories** extension details
  page, where you can view and manage connected GitLab user and linked GitLab project repositories.

After connecting your third-party source to CodeCatalyst, you can link the third-party
repositories to your CodeCatalyst projects.

###### To create your project

1. On the **Create project** page, choose the GitHub account you connected.
2. Depending on the third-party repository provider you connected, choose the **GitHub repositories**, **Bitbucket repositories**, or **GitLab repositories** repository
   dropdown menu to view the third-party repositories, and then choose the repository that you want to link to your project.
3. In the **Name your project** text input field, enter the name that
   you want to assign to your project. The name must be unique within your space.
4. Choose **Create project**.

After installing the **GitHub repositories**, **Bitbucket repositories**, or **GitLab repositories** extension, connecting your resource provider, and linking your
third-party repository to your CodeCatalyst project, you can use it in CodeCatalyst workflows and Dev Environments. You can also
create third-party repositories in the connected GitHub account, Bitbucket workspace, or GitLab user with code generated
from a blueprint. You can also use the linked repositories with Amazon Q Developer, blueprints, and more. For more
information, see [Automatically starting a workflow run after third-party repository events](extensions-workflow-repositories.md "extensions-workflow-repositories.md")
and [Creating a Dev Environment](devenvironment-create.md "devenvironment-create.md").

## Creating a project with a

blueprint

You can provision all of your project resources and sample code with a project
blueprint. For information about blueprints, see the [Creating a comprehensive project with CodeCatalyst blueprints](project-blueprints.md "project-blueprints.md").

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
or add functionality with blueprints](#projects-create-amazon-q "#projects-create-amazon-q"). This feature is only available in
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

## Best practices when using Amazon Q to create projects

or add functionality with blueprints

When you create a project or want to add new components to an existing project, you might
be unsure about which blueprint to use or how to integrate capabilities. CodeCatalyst includes
integration with a generative AI assistant called Amazon Q that can analyze your project
requirements and suggest a blueprint that best fits your needs.

You can use Amazon Q to help you create a project with a blueprint that creates
components based on your requirements, or you can use Amazon Q to help you add a
blueprint to an existing project. For example, to add resources for a web application or
modern application to a project, specify your requirements and then the resources will be
added with a recommended blueprint. Issues for remaining components can be created for
you.

Amazon Q also creates issues for requirements that can't be addressed by a suggested
blueprint. Additionally, you can assign those issues to Amazon Q. If you assign the issue
to Amazon Q, it will attempt to create a draft solution for you to evaluate. This can help
you and your team to focus and optimize work on issues that require your attention, while
Amazon Q works on a solution for problems you don't have resources to address
immediately.

###### Note

**Powered by Amazon Bedrock**: AWS implements [automated abuse detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md").
Because the **Write description for me**, **Create content summary**, **Recommend tasks**, **Use Amazon Q to create or add features to a project**, and **Assign issues to Amazon Q** feature with Amazon Q Developer Agent for software development features are built on Amazon Bedrock, users can take full advantage of the controls implemented in Amazon Bedrock to enforce safety, security, and the responsible use of artificial intelligence (AI).

The following are some best practices to help you create projects and add blueprints with
Amazon Q.

###### Important

Generative AI features are only available in the US West (Oregon) Region.

- **Use the default prompts provided by Amazon Q** .
  Amazon Q does best with choosing blueprints from the provided prompts.
- **Use the configuration options suggested by Amazon Q to preview
  the blueprints**. Choose a blueprint to preview the sample code and
  resources that will be created by the blueprint.
- **Use a space that is enabled for Amazon Q** . To
  create a project with Amazon Q, or to add functionality to a project with blueprints
  using Amazon Q, use a space that is enabled for generative AI features. For more
  information, see [Enabling or disabling generative AI features for a space](../adminguide/managing-generative-ai-features.md#managing-generative-ai-features-enable-disable "../adminguide/managing-generative-ai-features.md#managing-generative-ai-features-enable-disable").
- **Get more information about blueprints recommended by
  Amazon Q**. You might want to find out more about the kind of project
  resources, sample code, and components that are created with a specific recommended
  blueprint. For more information about available blueprints in CodeCatalyst, see [Creating a comprehensive project with CodeCatalyst blueprints](project-blueprints.md "project-blueprints.md").
- **Allow Amazon Q to work with issues**. Allow
  Amazon Q to create issues for you, assign those issues, and track them. For more
  information, see [Tutorial: Using CodeCatalyst generative AI
  features to speed up your development work](getting-started-project-assistance.md "getting-started-project-assistance.md").
- **Unassign Amazon Q from issues that are no longer worked
  on**. After you complete the example, unassign Amazon Q from any issues no
  longer being worked on. If Amazon Q has finished its work on an issue or could not find
  a solution, make sure to unassign Amazon Q to avoid reaching the maximum quota for
  generative AI features. For more information, see [Managing
  generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md") and [Pricing](https://codecatalyst.aws/explore/pricing "https://codecatalyst.aws/explore/pricing").
- **View usage for Amazon Q**. You can view usage of
  generative AI features at the user level. Go to **My
  settings** to manage generative AI quotas and view usage by your Builder ID or
  single sign-on (SSO) identity. For more information, see [Viewing usage of generative AI features in a space](../adminguide/managing-generative-ai-features.md#managing-generative-ai-features-view-usage "../adminguide/managing-generative-ai-features.md#managing-generative-ai-features-view-usage").

###### Important

The generative AI features in CodeCatalyst are subject to quotas. For more information, see
[Amazon Q Developer
Pricing](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/"), [Enabling or disabling generative AI features for a space](../adminguide/managing-generative-ai-features.md#managing-generative-ai-features-enable-disable "../adminguide/managing-generative-ai-features.md#managing-generative-ai-features-enable-disable"), and [Billing](../adminguide/managing-billing.md "../adminguide/managing-billing.md").

## Best practices for using blueprints with

projects

The following are some best practices to help you create a project with blueprints or
add blueprints.

- **Use blueprints provided by CodeCatalyst to create or add to
  projects**. You can use blueprints to create a full project with source code
  and resources for developers. For example, the web application blueprint creates
  application and infrastructure resources and deploys a web application. You can create a
  project with a blueprint or add a custom blueprint to an existing project. For more
  information, see [Creating a project with a blueprint](create-project-with-bp.md "create-project-with-bp.md"). View any blueprint in CodeCatalyst to preview the
  sample code and resources that will be created by the blueprint.
- **Use custom blueprints designed by your
  organization**. You can use custom blueprints to create a full project in your
  space. The custom blueprint designed by your organization can provide
  standardization and best practices, which can also help to cut down on efforts to set up a
  new project. As a custom blueprint author, you can view details about which projects are
  using your blueprint throughout your space. Lifecycle management allows you to
  centrally manage the software development lifecycle of every project, and blueprint
  users can utilize lifecycle management to regenerate a codebase from updated options or
  versions of a blueprint. For more information, see [Working with lifecycle management as a blueprint author](lifecycle-management-dev.md "lifecycle-management-dev.md").
- **Add the developer role or appropriate IAM roles to the account
  for your project**. During or after you complete the project creation steps,
  you can configure your blueprint permissions by choosing or creating IAM roles in an
  AWS account that is connected to the space.

## Adding resources and tasks to created projects

After your project is ready, you can add resources and tasks.

- To learn about the CI/CD workflows created with your project, see [Getting started with workflows](workflows-getting-started.md "workflows-getting-started.md").
- To work with build actions similar to those in your new project that deploy build
  artifacts to an Amazon S3 bucket, see [Building with workflows](build-workflow-actions.md "build-workflow-actions.md") and [Tutorial: Upload artifacts to Amazon S3](build-deploy.md "build-deploy.md").
- To start with an empty project and work with deploying a similar serverless application
  with an AWS CloudFormation stack deployment, see [Tutorial: Deploy a serverless application](deploy-tut-lambda.md "deploy-tut-lambda.md").
- To add an issues planning board, see [Track and organize work with issues in CodeCatalyst](issues.md "issues.md").
- To view the project overview, project status, recent team activity, and assigned work,
  see [Getting a list of projects](projects-view.md "projects-view.md").
- To view source code or create a pull request, see [Store and collaborate on code with source repositories in CodeCatalyst](source.md "source.md").
- To set up notifications that send status alerts for workflow run success or failure, see
  [Sending Slack and email notifications from CodeCatalyst](notifications-manage.md "notifications-manage.md").
- To invite members to your project, see [Granting users project permissions](projects-members.md "projects-members.md").
- To set up Dev Environments, see [Write and modify code with Dev Environments in CodeCatalyst](devenvironment.md "devenvironment.md").
