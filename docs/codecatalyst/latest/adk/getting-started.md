# Getting started with the Action Development Kit

Learn how to create your action workspace, bootstrap and develop your action, and then test
and validate it.

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Step 1: Set up your project and Dev Environment](#set-up-workspace-first-action "#set-up-workspace-first-action")
- [Step 2: Install tools and packages](#install-tools-packages "#install-tools-packages")
- [Step 3: Initialize your action project](#initialize-action-workspace "#initialize-action-workspace")
- [Step 4: Bootstrap the action code](#bootstrap-action-code "#bootstrap-action-code")
- [Step 5: Build the package locally](#build-action-code "#build-action-code")
- [Step 5: Set action results](#error-handling "#error-handling")
- [Step 6: Test the action](#test-action-integration "#test-action-integration")
- [Step 7: Publish the action](#publish-action "#publish-action")
- [Next steps](#next-steps "#next-steps")

## Prerequisites

To create an action, you must have completed the tasks in [Setting up CodeCatalyst](../userguide/setting-up-topnode.md "../userguide/setting-up-topnode.md").

###### Important

Currently, only verified partners can create custom actions, test unpublished action versions in workflows, and
publish actions to the CodeCatalyst actions catalog.

## Step 1: Set up your project and Dev Environment

Create a Dev Environment to work on code stored in source repositories of your CodeCatalyst project.
For more information, see [Dev Environments](../userguide/devenvironment.md "../userguide/devenvironment.md").

You can also build actions on your local machine and push the code to your CodeCatalyst remote repository. For more information,
see [Setting up your project on a local machine](set-up-workspace-local.md "set-up-workspace-local.md").

**To set up your project**

1. Create an empty project in CodeCatalyst.

###### Note

Before you create a project, you must have the **Space administrator**
role, and you must create or join the space where you want to create the project.
For more information, see [Creating a space in CodeCatalyst](../userguide/spaces-create.md "../userguide/spaces-create.md").

    1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
    2. Navigate to the space where you want to create a project.
    3. On the space dashboard, choose **Create project**.
    4. Choose **Start from scratch**.
    5. Under **Give a name to your project**, enter the name that you
     want to assign to your project. The name must be unique within your space.
    6. Choose **Create project**.

2. Create an empty repository in your new project.

###### Note

Third-party repositories, such as GitHub repositories, aren't
supported for developing, testing, and publishing actions. The actions must
be developed in a CodeCatalyst repository.

    1. Navigate to your project.
    2. In the navigation pane, choose **Code**, and then choose
     **Source repositories**.
    3. Choose **Add repository**, and then choose **Create
     repository**.
    4. In **Repository name**, provide a name for the repository. Repository
     names must be unique within a project. For more information about the requirements for
     repository names, see [Quotas for source repositories in CodeCatalyst](../userguide/source-quotas.md "../userguide/source-quotas.md").


    The action name defaults to the repository name, but it can be changed in CodeCatalyst.
    5. (Optional) In **Description**, add a description for the
     repository that will help other users in the project understand what the repository is
     used for.
    6. (Optional) Add a `.gitignore` file for the type of code you plan to
     push.
    7. Choose **Create**.


    ###### Note

    CodeCatalyst adds a `README.md` file to your repository when you create it.
     CodeCatalyst also creates an initial commit for the repository in a default branch named
     **main**. You can edit or delete the `README.md` file,
     but you can't change or delete the default branch.

3. Create a new feature branch.
   1. In the navigation pane, choose **Code**, choose **Source
      repositories**, and then choose the empty repository you created.
   2. Choose **Actions**, and then choose **Create
      branch**.
   3. In the **Branch name** text input field, enter a
      `feature-action-name`.
   4. In the **Create branch from** dropdown menu, ensure
      **main**, the source branch you're creating the new branch from, is
      selected, and then choose **Create**.

4. Create a Dev Environment to work on code with a supported integrated development environment (IDE).
   1. In the navigation pane, do one of the following:
      1. Choose **Overview**, and then navigate to the **My Dev Environments** section.
      2. Choose **Code**, and then choose **Dev Environments**.
      3. Choose **Code**, choose **Source repositories** and choose the repository for which you
         want to create a Dev Environment.

   2. Choose **Create Dev Environment**.
   3. Choose a supported IDE from the drop-down menu. See [Supported integrated development environments for Dev Environments](../userguide/devenvironment-create.md#devenvironment-supported-ide "../userguide/devenvironment-create.md#devenvironment-supported-ide") for more information.
   4. Choose **Work in existing branch**, and from the **Existing branch** dropdown menu,
      choose the feature branch you created.
   5. (Optional) In the **Alias - _optional_** text input field, enter an alias to identify the
      Dev Environment.
   6. Choose **Create**. While your Dev Environment is being created, the Dev Environment status column will display
      **Starting**, and the status column will display **Running** once the Dev Environment has been created.

After setting up your project, you can create secrets for your custom actions if you're working with sensitive data that will be used in
your action's workflow. For more information, see [Creating secrets](adk-create-secrets.md "adk-create-secrets.md").

## Step 2: Install tools and packages

The first step in authoring actions is to install the following required tools and
packages. To develop actions, you will need npm and TypeScript.

###### Note

ADK supports the following versions of tools and packages:

- npm – 8+ (for example, 8.15.0)
- node – 16+ (for example, v16.17.1)
- tsc (TypeScript) – 4+ (for example, Version 4.9.5)
- AWS CLI – aws-cli/2.7.27 Python/3.9.11 Darwin/22.3.0 exe/x86_64 prompt/off
  (minimum)
  For node 17+, you may run into an error: `ERR_OSSL_EVP_UNSUPPORTED`. If so,
  run the following:

```
npm audit fix --force
```

Open a working terminal in your Dev Environment to install the necessary tools and packages.

**To navigate to your Dev Environment and open terminal**

1. In the navigation pane, choose **Code**, and then choose **Dev Environments**.
2. From the **IDE** column, choose **Resume in (IDE)** for the Dev Environment.
   - For JetBrains IDEs, choose **Open Link** to confirm when prompted to **Allow this site to
     open the JetBrains-gateway link with JetBrains Gateway?**.
   - For the VS Code IDE, choose **Open Link** to confirm when prompted to **Allow this site to
     open the VS Code link with Visual Studio Code?**.

###### Note

Resuming a Dev Environment may take a few minutes.

For more information, see [Resuming a Dev Environment](../userguide/devenvironment-resume.md "../userguide/devenvironment-resume.md"). 3. Open a new terminal window in the Dev Environment.

**To install npm**

Download the [latest
version of npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm "https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"). We recommend using a Node version manager like
[nvm](https://github.com/nvm-sh/nvm "https://github.com/nvm-sh/nvm") to
install
Node.js and npm.

**To install the AWS CLI**

Follow the instructions for
[Installing
or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

You'll use the TypeScript programming language along with npm to build actions. It's the
only language supported by the ADK.

**To install TypeScript**

Download [tsc through npm](https://www.typescriptlang.org/download "https://www.typescriptlang.org/download"). You can
also run the following npm command:

```
npm i typescript
```

The ADK Command Line Interface (CLI) is necessary to manage and interact with
the ADK files.

**To install the ADK CLI**

1. Run the following npm command to install the ADK CLI package:

```
npm install -g @aws/codecatalyst-adk
```

2. Validate that the ADK is running with the following command:

```
adk help
```

## Step 3: Initialize your action project

Initializing the action project provides the CodeCatalyst ADK with essential
information about your action such as the development language, action name, and CodeCatalyst
metadata. The initialization creates an action definition file used by CodeCatalyst workflows to
integrate the action within the workflow.

**To initialize your action workspace**

Run the following command in the `feature-action-name` branch to create an
action definition YAML file (`.codecatalyst/actions/action.yml`).

```
adk init --lang typescript --space `[CODECATALYST-SPACE-NAME]` --proj `[CODECATALYST-PROJECT-NAME]` --repo `[CODECATALYST-REPO-NAME]` --action `[ACTION-NAME]`
```

For example:

```
adk init --lang typescript --space MySpace --proj HelloWorldProject --repo HelloWorldAction --action HelloWorldAction
```

Ensure your space, project, and repository names are entered correctly.

## Step 4: Bootstrap the action code

After the action project is initialized, you must bootstrap the action itself.
Bootstrapping provides all the language-specific tools and libraries preconfigured to build,
test, and release the action project.

**To create an action**

1. Run the following ADK CLI command in the directory for your remote
   repository:

```
adk bootstrap
```

(Optional) By default, the `adk bootstrap` command searches for the action
definition file in `.codecatalyst/actions/action.yml`. You can use the
following argument to specify a different path to the action definition file:

```
adk bootstrap -f .codecatalyst/actions/action.yml
```

Because TypeScript is used to develop the action, the bootstrap command creates TypeScript
code to set up the workspace with all the node- and npm-specific toolchains and libraries. You
should see the following contents:

    * `.codecatalyst/actions/action.yml` – Action definition file
     that contains interface and implementation metadata for the action to be ingested into CodeCatalyst.
     This action definition file is the interface that is used by CodeCatalyst workflows to integrate
     the action within the workflow itself. The file defines inputs, outputs, and resource
     integrations within CodeCatalyst.
    * `.codecatalyst/workflows/`actionName`-CI-Validation.yml`
     – Workflow definition file that describes a continuous integration (CI) workflow
     generated by the ADK bootstrap.
    * `README.md` – Readme file that contains information about
     what the action does and how to use the action with CodeCatalyst workflows. It is used for the
     action documentation.
    * `package.json` – File that records metadata about your
     project that is necessary before publishing to npm.
    * `lib/index.ts` – Main file referred to in the package.json
     file. It is the main entry into the action.
    * `test/index.test.ts` – Test file for the index.ts
     file.
    * `tsconfig.json` – TypeScript configuration file that
     provides configuration options that are passed on to the tsc command.
    * `jest.config.js` – Jest configuration file that is used
     during test runs.
    * `.prettierrc.json` – Opinionated code formatter that remove
     original styling and makes sure for outputted code conforms to a consistent style.
    * `.gitignore` – Specifies intentionally untracked files that
     Git should ignore.
    * `.eslintrc.js` – Configuration file for ESLINT tool used to
     make the code consistent and avoid bugs.
    * `LICENSE` – Plain text file that supplies required license
     information.

After your custom action's files are generated, you can configure them to your requirements,
including integrating third-party functionality. To learn about specific files you can configure,
see [Configuring custom actions for third-party integrations](adk-configure-third-party.md "adk-configure-third-party.md").

The ADK bootstrapping runs a pre-validation check that verifies if any of the
generated files already exist. If so, the ADK will print an error message and fail.
For example:

```
% adk bootstrap
   Starting action bootstrap based on definition file .codecatalyst/actions/action.yml
   File 'tsconfig.json' already exists
   File '.prettierrc.json' already exists
   File '.gitignore' already exists
   File '.eslintrc.js' already exists
   File 'jest.config.js' already exists
   File 'LICENSE' already exists
   File 'package.json' already exists
   File 'README.md' already exists
   File 'lib/index.ts' already exists
   File 'test/index.test.ts' already exists
    => Either bootstrap in an empty directory or use 'adk bootstrap -o' to override existing files
   Bootstrap pre-validation failed
   Command exit code 1
```

(Optional) You can give the ADK permission to override existing files by running the
following command:

```
adk bootstrap -o
```

###### Important

Running the `adk bootstrap -o` command will overwrite any
code changes you make and regenerates the initial code. Any changes that aren't committed will
be overwritten if the command is run.

The action definition generated by the ADK should look something like the
following:

```
SchemaVersion: '1.0'
 Name: 'MyAction'
 Version: '0.0.0'
 Description: 'This Action greets someone and records the time'
 Configuration:
   WhoToGreet:
     Description: 'Who are we greeting here'
     Required: true
     DisplayName: 'Who to greet'
     Type: string
   HowToGreet:
     Description: 'How to greet the person'
     Required: false
     DisplayName: 'How to greet'
     Type: string
     Default: 'Hello there,'
 Inputs:
   Sources:
     Required: true
 Environment:
   Required: false
 Runs:
   Using: 'node16'
   Main: 'dist/index.js'
```

The CI workflow generated by the ADK should look something like
this:

```
Name: MyAction-CI-Validation
 SchemaVersion: "1.0"
 Triggers:
   - Type: PullRequest
     Events: [ open, revision ]
     Branches:
       - feature-.*
 Actions:
   ValidateMyAction:
     Identifier: .
     Inputs:
       Sources:
         - WorkflowSource
     Configuration:
       WhoToGreet : 'TEST'
       HowToGreet : 'TEST'
```

2. After the bootstrapping is complete, run the following commands to commit the changes to your
   `feature-action-name` branch:

```
git add .
```

```
git commit -m "`commit message`"
```

You can also use the source control options available in the IDE you’re using for your Dev Environment.

## Step 5: Build the package locally

As an action author, you must build and package the action using `npm`
commands. The ADK only supports actions implemented in
JavaScript
(js) and TypeScript (tsc). Building an action will produce
`.js` files, including source code bundled with dependencies under the
`dist/` folder. The bundle must be updated and pushed to the action's
repository when changes are made to the source or dependencies.

**To build your package locally**

1. Run the following npm command to install all the dependencies. These are the necessary
   packages your project depends on to run:

```
npm install
```

After running the npm command, you should see the total number of added packages. 2. Run the following command to catch action errors in your action definition YAML
file:

```
adk validate
```

(Optional) By default, the `adk validate` command searches for the action
definition file in `.codecatalyst/actions/action.yml`. You can use the
following argument to specify a different path to the action definition file:

```
adk validate -f .codecatalyst/actions/action.yml
```

3. Run the following npm command to run npm scripts:

```
npm run all
```

A successful build generates an `index.js` that contains the action's
source code bundled with dependencies under the `dist/` folder. This file
is ready to be run by the action runner without any other dependencies needed. To rebuild the
action after making changes to the source code, run `npm run all` and commit the
updated content of the `dist/` folder.

###### Important

If the size of the bundle (`dist/index.js`) is more than 10 MB,
you will not be able to publish the action to the CodeCatalyst actions catalog. The bundle grows to 10 MB or more when
an action has many large dependencies . For more information
[Quotas for source
repositories in CodeCatalyst](../userguide/source-quotas.md "../userguide/source-quotas.md"). 4. After the action is built, run the following commands to commit the changes to your remote
repository:

###### Important

Make sure the code you're pushing doesn't contain any sensitive information that
you don't want to be shared publicly.

```
git add .
```

```
git commit -m "`commit message`"
```

```
git push
```

You can also use the source control options available in the IDE you’re using for your Dev Environment.

## Step 5: Set action results

If you don't set status feedback for your action, the action will succeed by default. You can set an action failure status and return an error
message to troubleshoot the error. Run the workflow to test your action and view the results, including results, in CodeCatalyst. For more information,
[Testing actions in workflows](testing-action.md#test-action-workflows "testing-action.md#test-action-workflows").

We recommend running business logic in a try-catch block to set errors or action feedback. The ADK provides two APIs to configure
error messages and surface them:

- `core.setFailed('Action Failed, reason: ${error});` – Logs the error message. The workflow stops running and any
  remaining steps are skipped.
- `RunSummaries.addRunSummary(Action Failed, reason: ${error},
codecatalystRunSummaries.RunSummaryLevel.ERROR);` – Sets the
  workflow summary run message. This provides context
  about the run such as the number of tests that passed or failed, time to complete,
  and other relevant information added to the output variable.

The following example shows how you can use a try-catch block for error handling:

```
export function main(): void {
        try {
            // action business logic
        } catch (error) {
            // the recommended error handling approach
            console.log(`Action Failed, reason: ${error}`);
            RunSummaries.addRunSummary(`${error}`, RunSummaryLevel.ERROR);
            core.setFailed(`Action Failed, reason: ${error}`);
        }
    }
```

Use `setFailed` to indicate that a step has failed, and use
`RunSummaries` to provide additional context when the action fails
in the workflow. For more information, see
[ADK Core's setFailed
details](https://aws.github.io/actions-dev-kit/functions/_aws_codecatalyst_adk_core.setFailed.html "https://aws.github.io/actions-dev-kit/functions/_aws_codecatalyst_adk_core.setFailed.html") and
[RunSummaries construct details](https://aws.github.io/actions-dev-kit/modules/_aws_codecatalyst_run_summaries.html "https://aws.github.io/actions-dev-kit/modules/_aws_codecatalyst_run_summaries.html").

## Step 6: Test the action

### Adding unit tests

The ADK CLI bootstraps actions with an empty unit test that you can use as a starting
point to write sophisticated unit tests. For more information, see [Adding unit tests](testing-action.md#test-action-locally "testing-action.md#test-action-locally").

### Testing actions in workflows

Test your custom action before publishing to the CodeCatalyst actions catalog. To make sure
your action works as expected, you can run it within the workflow and view the run's
details. For more information, see [Testing actions in workflows](testing-action.md#test-action-workflows "testing-action.md#test-action-workflows").

###### Important

Currently, only verified partners can test unpublished action versions in workflows.

The ADK generates a continuous integration (CI) workflow that is ready to be used in CodeCatalyst. By
default, a bootstrapped action produces a `dist/` folder with an artifact
that contains the dependencies the workflow requires to run successfully in CodeCatalyst. You must
build the actions locally and push the content of the `dist/` folder to
the action's source repository before testing the actions in a workflow.

After making changes to your source code following [Step 4: Bootstrap the action code](#bootstrap-action-code "#bootstrap-action-code"), build your action locally and push your code again to your CodeCatalyst repository before
testing the action in a workflow.

**To build and push action source code and the
bundle**

1. Run the following npm commands to build your action:

```
npm install
```

```
npm run all
```

2. Run the following commands to commit the changes to your remote repository:

###### Important

Make sure the code you're pushing doesn't contain any sensitive information that
you don't want to be shared publicly.

```
git add .
```

```
git commit -m "`commit message`"
```

```
git push
```

You can also use the source control options available in the IDE you’re using for your Dev Environment.

The action can now be tested with the ADK-generated workflow. By default, the
workflow's name is ``ActionName`-CI-Validation`.

**To test an action within a ADK-generated CI workflow**

1. Navigate to the CodeCatalyst project page.
2. Choose the **CI/CD** dropdown menu, and then choose
   **Workflows**.
3. From the repository and branch dropdown menus, select the repository and feature branch in
   which you created the action and its workflow.
4. Choose the workflow you want to test.
5. Choose **Run** to perform the actions defined in the workflow
   configuration file and get the associated logs, artifacts, and variables.
6. View the workflow run status and details. For more information, see [Viewing workflow run status and details](../userguide/workflows-view-run.md "../userguide/workflows-view-run.md").

## Step 7: Publish the action

You can publish the actions in your local catalog to the CodeCatalyst actions catalog so that
other CodeCatalyst users can use them.

###### Important

Currently, only verified partners can publish actions to the CodeCatalyst actions catalog.

###### Important

When your action is published to the CodeCatalyst actions catalog, it is available to all CodeCatalyst
users, so make sure that you want the action to be publicly available. Other users don't
have to be in your space or project to view your published action.

###### Important

If the size of the bundle (`dist/index.js`) is more than 10 MB,
you will not be able to publish the action to the CodeCatalyst actions catalog. The bundle grows to 10 MB or more when
an action has many large dependencies. For more information
[Quotas for source
repositories in CodeCatalyst](../userguide/source-quotas.md "../userguide/source-quotas.md").

The action can only published from the default branch of the source repository. If you developed
the action on a feature branch, merge your feature branch with the action to the default branch.

**To merge your feature branch to the default branch**

Create a pull request for other members to review and merge the changes from the feature branch
to the default branch. For more information, see
[Working with
pull requests in Amazon CodeCatalyst](../userguide/source-pull-requests.md "../userguide/source-pull-requests.md").

After the action information is merged to the default branch, you can publish the action to the CodeCatalyst
actions catalog. Before publishing, you can also edit the metadata details of the action version.

**To edit details and publish the action**

1. Navigate to the CodeCatalyst project page
2. In the navigation pane, choose **CI/CD**, choose **Actions**,
   and then choose the action you want to publish.
3. Choose **Edit details** to edit the details for your action:
   1. (Optional) In the **Action display name** field, change the
      action display name. This is the name that appears in the **Actions** list before
      the action is published, as well as in the CodeCatalyst actions catalog after the
      action is published.
   2. (Optional) In the **Action name** field, change the
      action name. This name is combined with the space name and action version to form
      the action identifier (for example, test-space/test-45tzuy@v1.0.0). In your workflow,
      the action identifier is used to specify the action.

   ###### Note

   The **Action name** can't be changed after the action is published. 3. (Optional) In the **Description** field, change the
   description. This description appears for the action in the **Actions** list and the
   Amazon CodeCatalyst catalog (after the action is published). 4. From the **Categories** dropdown list, choose the type of actions
   that are part of your workflow. These categories appear when you or other CodeCatalyst users choose the action's
   name from CodeCatalyst catalog while working with workflows. 5. (Optional) In the **Support contact** field, enter an email other CodeCatalyst users can reach out to
   regarding the action you published. 6. Choose **Save**

4. (Optional) Edit the license file. This file is created when the action is bootstrapped and is stored at the root
   of action's source repository.
   1. Choose **View license file** to open the file.
   2. Choose **Edit** and make your changes.
   3. Choose **Commit**, add a message in the **Commit
      message** field, and then choose **Commit**.

5. Choose **Publish version** to view the publish version details.
6. Choose the **Commit** dropdown list, and then choose the commit from the
   default branch you want to publish.

###### Note

The commit must meet publishing requirements, including a valid action definition, a readme file,
a license file, and entry files.

The **Code quality** section displays the code quality of your results. Not
meeting the quality results doesn't block you from publishing the action version. The
**Test details** section provides testing and code coverage results. You can add and
run unit tests to meet your requirements for the action. For more information, see [Testing an action](testing-action.md "testing-action.md"). 7. Choose **Publish** to publish the action to the CodeCatalyst actions catalog. In the
**Versions** table, the status of the version displays **Published**
once the action version has been successfully published.

## Next steps

After developing your custom action, you can update and publish new action versions to the CodeCatalyst
actions catalog:

- [Publishing a new action version](actions-update.md "actions-update.md")
