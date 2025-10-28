# Modernizing .NET with AWS Transform quick start guide

## .NET step 1: Sign-in and onboarding

1. Follow the steps under [Quick start: Getting started with AWS Transform](transform-setup.md#transform-app-admin-starting-standalone "transform-setup.md#transform-app-admin-starting-standalone").
2. Follow the steps under [Setting up your workspace](transform-app-admin-workspace-setup.md "transform-app-admin-workspace-setup.md") or [Getting started with AWS Organizations](transform-setup.md#transform-app-admin-starting-orgs "transform-setup.md#transform-app-admin-starting-orgs").

## .NET step 2: Job creation

1. On your workspace landing page, choose to create a .NET job.
2. In the chat window, AWS Transform will ask you to confirm job details.

For more information, see [Creating the AWS Transform .NET job plan](dotnet-creating-job-plan.md "dotnet-creating-job-plan.md").

## .NET step 3: Set up a connector

In order for AWS Transform to assess your code and identify the jobs that can be transformed automatically, you must set up a connector to your repositories.

For .NET transformation, AWS Transform supports connectors to repositories of the following type:

- Bitbucket
- GitHub
- GitLab

AWS Transform also needs access to a writable branch in the same repository for submitting the transformed code.

If necessary, chat with AWS Transform in the left pane. It will walk you through setting up your connectors step by step.

This may involve the following steps:

- Creating a separate AWS account for importing your codebase.
- Identifying that AWS account.
- (Required) Adding the Bitbucket, GitHub, or GitLab app to your instance of AWS CodeConnections.
- (Required) Creating an AWS CodeConnections connection with your data source.
- Identifying that connection.
- Asking your AWS administrator to validate your connection in the AWS CodeConnections Console.
- Asking your AWS account administrator to assign an IAM role to the workspace, allowing it to use the connection.
- Confirming to AWS Transform that you are ready to begin the data transfer.

For more information about AWS CodeConnections, see [What are connections?](../../../dtconsole/latest/userguide/connections-create-github.md "../../../dtconsole/latest/userguide/connections-create-github.md") in the _Developer Tools Console User Guide_.

For more information about IAM roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _AWS Identity and Access Management User Guide_.

Limits:

- AWS Transform does not support connectors to AWS CodePipeline
- AWS Transform can only connect to source control using an App ID. AWS Transform cannot connect to a source with a username and password.
- You cannot upload your source code files directly to AWS Transform. You must put them in a supported repository for AWS Transform to access.

When you set up a connector, the administrator of the AWS account to which you are connecting must accept the connection. In order to accept the connection, they must have the permissions given in [the connector acceptance policy](../../../amazonq/latest/qdeveloper-ug/id-based-policy-examples-admins.md#id-based-policy-examples-admin-connector "../../../amazonq/latest/qdeveloper-ug/id-based-policy-examples-admins.md#id-based-policy-examples-admin-connector").

For more information, see [Creating a source code repository connector](dotnet-creating-repo-connector.md "dotnet-creating-repo-connector.md").

## .NET step 4: Analysis

In this step, AWS Transform analyzes the code and proposes a modernization plan, outlining the intermediate steps and tasks required to transform the application to .NET 8.0+.

Once the connector is set up, AWS Transform begins to automatically analyze the source code repositories (repos) to identify a list of repos that have supported project types for porting. Each repo may contain multiple .NET projects. By assessing all the repos and projects, the transformation agents for .NET can identify dependencies between .NET projects across multiple repos to help transform your code successfully.

When the analysis is completed, AWS Transform will provide you with a list of repositories, the number of .NET projects within each of these repos, the default branch to select for the transformation, and the last commit date and time.

By default, AWS Transform selects all .NET projects that are supported within a repo, and you have the option to select specific .NET projects, solutions, and branches to include or exclude from the transformation.

Also, as a part of your transformation job, the AWS Transform .NET agent has the following **Default settings**.

- Exclude .NET Standard projects from the transformation plan

This setting is selected by default. When selected, AWS Transform excludes any .NET Standard projects from the transformation plan. If you deselect this setting, .NET Standard projects will be transformed, which will make them no longer compatible with the .NET Framework.

- Transform Model-View Controller (MVC) Razor Views to ASP.NET Core Razor

This setting is selected by default. When selected, AWS Transform handles the transformation of any MVC Razor View UI layers into ASP.NET Core Razor Views. If you deselect this option, you must transform these UI layers manually.

For the UI layer, only the transformation of MVC Razor Views to
ASP.NET core is supported. UI Layers for WebForms (.aspx),
Windows Presentation Foundation (WPF), WinForms, and
Blazor UI components must be transformed manually.

Once the repo and .NET projects are selected, AWS Transform automatically begins the transformation process.

Legacy versions of .NET supported for transformation to .NET 8.0+:

- .NET Framework versions 3.5+
- .NET Core 3.1, .NET 5
- .NET 6
- .NET 7

For information about the .NET project types that AWS Transform supports, see [AWS Transform supported project types](dotnet.md#capabilities "dotnet.md#capabilities"). For information about unsupported project types, see [AWS Transform limitations for .NET modernization](dotnet.md#limitations "dotnet.md#limitations").

For more information see the following:

- [Confirming your repositories to prepare for transformation](dotnet-confirming-repos.md "dotnet-confirming-repos.md").
- [Resolving package dependencies to prepare for
  transformation](dotnet-resolving-dependencies.md "dotnet-resolving-dependencies.md").
- [Reviewing your plan to prepare for transformation](dotnet-reviewing-plan.md "dotnet-reviewing-plan.md").

## .NET step 5: Bulk transformation

Once you have selected the repo and projects to be transformed, AWS Transform will automatically begin the transformation of the related .NET applications. AWS Transform downloads the source code into a Managed Development Environment (MDE), and encrypts it using your managed KMS keys. Then, AWS Transform builds a dependency tree for the jobs across the repos being modernized. Based on the dependency tree, the agents will start the transformation in parallel across the repo. Along the way, AWS Transform will ask you for input when it needs information, or when it needs you to take some action.

You can track the progress of the transformation in two ways:

- _Worklog_ – This provides a detailed log of the actions AWS Transform takes, along with human input requests, and your responses to those requests.
- _Dashboard_ – This provides high level summary of the transformation. It shows metrics on number of jobs transformed, transformation applied, and estimated time to complete the transformation.

Safeguards:

AWS Transform will refuse questions from users who don't have the proper permissions. For example, a read-only user cannot cancel a job transformation or delete a job.

For more information see [Transforming your .NET code](dotnet-transforming-code.md "dotnet-transforming-code.md").

## .NET Step 6: Code review and completion

At this point, either your jobs have been transformed successfully, or they have been partially transformed, with build errors.

In this step, you transition from the AWS Transform web experience to AWS Transform in the Visual Studio IDE. You can use AWS Transform in Visual Studio to verify the transformation of the projects, and to make modifications if required.

For information about setting up the AWS Transform extension with Visual Studio, see [Modernizing .NET using AWS Transform in Visual Studio](dotnet-ide-vs.md "dotnet-ide-vs.md").

There are two possible scenarios for review, and user input varies depending on the scenario:

- _The job is fully transformed_ – AWS Transform has fully transformed a job. The customer can review this transformed code, and if they are satisfied with the change, they can then proceed to _Complete the transformation_. This prompts an input response required action for the _Code approver_ or the _Administrator_ persona to review this action. Once the administrator approves, AWS Transform marks the job transformation status as _Completed_.
- _The job is partially transformed_ – AWS Transform has partially transformed a job, and the job has build errors that require a human in the loop (HITL) action. For this scenario, you can review the build errors and manually address any issues. After the Administrator has reviewed and approved the code, AWS Transform will continue the transformation and update the build errors for the job. You can continue to track this progress and take further action as required until all build errors are resolved.
