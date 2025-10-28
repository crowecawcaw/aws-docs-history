Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Getting started with workflows

In this tutorial, you'll learn how to create and configure your first workflow.

###### Tip

Prefer to start with a preconfigured workflow? See [Creating a project with a
blueprint](projects-create.md#projects-create-console-template "projects-create.md#projects-create-console-template"), which includes instructions for
setting up a project with a functioning workflow, sample application, and other
resources.

###### Topics

- [Prerequisites](#get-started-create-workflow-prerequisites "#get-started-create-workflow-prerequisites")
- [Step 1: Create and configure
  your workflow](#get-started-create-workflow-create "#get-started-create-workflow-create")
- [Step 2: Save your workflow with a
  commit](#get-started-create-workflow-commit "#get-started-create-workflow-commit")
- [Step 3: View run results](#get-started-create-workflow-results "#get-started-create-workflow-results")
- [(Optional) Step 4: Clean
  up](#get-started-create-workflow-cleanup "#get-started-create-workflow-cleanup")

## Prerequisites

Before you begin:

- You need a CodeCatalyst **space**. For more information, see
  [Creating a space](spaces-create.md "spaces-create.md").
- In your CodeCatalyst space, you need an empty project called:

```
codecatalyst-project
```

For more information, see [Creating an empty project in Amazon CodeCatalyst](projects-create.md#projects-create-empty "projects-create.md#projects-create-empty").

- In your project, you need a CodeCatalyst **repository** called:

```
codecatalyst-source-repository
```

For more information, see [Creating a source repository](source-repositories-create.md "source-repositories-create.md").

###### Note

If you have an existing project and source repository, you can use them; however,
creating new ones makes cleanup easier at the end of this tutorial.

## Step 1: Create and configure

your workflow

In this step, you create and configure a workflow that automatically builds and tests
your source code when changes are made.

###### To create your workflow

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
2. Choose **Create workflow**.

The workflow definition file appears in the CodeCatalyst console's YAML
editor.

###### To configure your workflow

You can configure your workflow in the **Visual** editor, or the
**YAML** editor. Let's start with the YAML editor and then
switch to the visual editor.

1. Choose **+ Actions** to see a list of workflow actions that you
   can add to your workflow.
2. In the **Build** action, choose **+** to add
   the action's YAML to your workflow definition file. Your workflow now looks similar to the
   following.

```
Name: Workflow_fe47
SchemaVersion: "1.0"

# Optional - Set automatic triggers.
Triggers:
  - Type: Push
    Branches:
      - main

# Required - Define action configurations.
Actions:
  Build_f0:
    Identifier: aws/build@v1

    Inputs:
      Sources:
        - WorkflowSource # This specifies that the action requires this workflow as a source

    Outputs:
      AutoDiscoverReports:
        Enabled: true
        # Use as prefix for the report files
        ReportNamePrefix: rpt

    Configuration:
      Steps:
        - Run: echo "Hello, World!"
        - Run: echo "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>" >> report.xml
        - Run: echo "<testsuite tests=\"1\" name=\"TestAgentJunit\" >" >> report.xml
        - Run: echo "<testcase classname=\"TestAgentJunit\" name=\"Dummy
            Test\"/></testsuite>" >> report.xml
```

The workflow copies the files in the `WorkflowSource` source
repository to the compute machine running the `Build_f0` action,
prints `Hello, World!` to the logs, discovers test reports on the
compute machine, and outputs them to the CodeCatalyst console's
**Reports** page. 3. Choose **Visual** to view the workflow definition file in the
visual editor. The fields in the visual editor let you configure the YAML
properties shown in the YAML editor.

## Step 2: Save your workflow with a

commit

In this step, you save your changes. Because workflows are stored as
`.yaml` files in your repository, you save your changes with
commits.

###### To commit your workflow changes

1. (Optional) Choose **Validate** to make sure the workflow's
   YAML code is valid.
2. Choose **Commit**.
3. In **Workflow file name**, enter a name for your workflow
   configuration file, like `my-first-workflow`.
4. In **Commit message**, enter a message to identify your
   commit, like `create my-first-workflow.yaml`.
5. In **Repository**, choose the repository you want to save the
   workflow in (`codecatalyst-repository`).
6. In **Branch name**, choose the branch you want to save the
   workflow in (`main`).
7. Choose **Commit**.

Your new workflow appears in the list of workflows. It might take several moments to
appear.

Because workflows are saved with commits, and because the workflow has a code push
trigger configured, saving the workflow starts a workflow run automatically.

## Step 3: View run results

In this step, you navigate to the run that was started from your commit and view the
results.

###### To view run results

1. Choose the name of your workflow, for example,
   `Workflow_fe47`.

A workflow diagram showing the label of your source repository
(**WorkflowSource**) and the build action (for example,
**Build_f0**). 2. In the workflow run diagram, choose the build action (for example,
**Build_f0**). 3. Review the contents of the **Logs**,
**Reports**, **Configuration**, and
**Variables** tabs. These tabs show you the results of your
build action.

For more information, see [Viewing the results of a build action](build-view-results.md "build-view-results.md").

## (Optional) Step 4: Clean

up

In this step, you clean up the resources that you created in this tutorial.

###### To delete resources

- If you created a new project for this tutorial, delete it. For instructions,
  see [Deleting a project](projects-delete.md "projects-delete.md"). Deleting
  the project also deletes the source repository and workflow.
