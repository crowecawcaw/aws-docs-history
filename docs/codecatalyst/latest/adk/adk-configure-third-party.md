# Configuring custom actions for third-party integrations

This section details how to develop a custom action with source code that can be used by AWS partners to integrate third-party
capabilities and publish to the CodeCatalyst actions catalog.

###### Important

Currently, only verified AWS partners with approved and allowlisted CodeCatalyst spaces can create custom actions, test
unpublished action versions in workflows, and publish actions to the CodeCatalyst actions catalog. To be allowlisted, reach out to
your AWS Account Manager or Partner Development Manager.

###### Important

As a third-party provider,
you're responsible for testing the custom action, making updates, and publishing the action.

Before you can configure files for third-party capabilities, you must complete the prerequisites and the first four steps from the
[Getting started with the Action Development Kit](getting-started.md "getting-started.md") walkthrough:

- [Prerequisites](getting-started.md#getting-started-prerequisites "getting-started.md#getting-started-prerequisites")
- [Step 1: Set up your project and Dev Environment](getting-started.md#set-up-workspace-first-action "getting-started.md#set-up-workspace-first-action")
- [Step 2: Install tools and packages](getting-started.md#install-tools-packages "getting-started.md#install-tools-packages")
- [Step 3: Initialize your action project](getting-started.md#initialize-action-workspace "getting-started.md#initialize-action-workspace")
- [Step 4: Bootstrap the action code](getting-started.md#bootstrap-action-code "getting-started.md#bootstrap-action-code")

## Configure custom action files

You can configure the generated files to incorporate secrets, include installation, setup instructions, and descriptions. The following
steps provide a walkthrough, including examples, on how you can configure your custom action's files:

**To configure an action's source files**

1. Configure the `.codecatalyst/actions/action.yml` file to update the `Description` of your custom action.
   Additionally, you can add code to accept secrets as user inputs, or use the `Default` value from the CodeCatalyst secrets to access
   secrets. You can also add your own secrets. For more information, [Creating secrets](adk-create-secrets.md "adk-create-secrets.md").

**Example:**

```
SchemaVersion: '1.0'
Name: 'custom-action'
Version: '0.0.0'
Description: 'This Action creates custom Actions source code'
Configuration:
  AwsAccessKeyId:
    Description: 'AWS Access Key ID'
    Required: true
    DisplayName: 'AWS_ACCESS_KEY_ID'
    Type: string
    Default: ${Secrets.AWS_ACCESS_KEY_ID}
  AwsSecretAccessKey:
    Description: 'AWS Secret Access Key'
    Required: true
    DisplayName: 'AWS_SECRET_ACCESS_KEY'
    Type: string
    Default: ${Secrets.AWS_SECRET_ACCESS_KEY}
Inputs:
  Sources:
    Required: true
Environment:
  Required: false
Runs:
  Using: 'node16'
  Main: 'dist/index.js'
```

2. Configure the `.codecatalyst/workflows/custom-action-CI-Validation.yaml` file to pass data like secrets.

**Example:**

```
Name: custom-action-CI-Validation
SchemaVersion: "1.0"
Triggers:
  - Type: PullRequest
    Events: [ open, revision ]
    Branches:
      - feature-.*
Actions:
  Validatecustom-action:
    Identifier: .
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      AwsAccessKeyId : ${Secrets.AWS_ACCESS_KEY_ID}
      AwsSecretAccessKey : ${Secrets.AWS_SECRET_ACCESS_KEY}
```

3. Configure the `lib/index.ts` file to describe the CodeCatalyst action, and identify the installation and setup instructions for
   the solutions or offerings. For example, this tutorial installs AWS CLI, sets up the secrets created, and then installs the Amazon CloudWatch agent.
   Such a setup can be done by running CLI commands like `curl`, `unzip`, `sudo`, and `yum`. Since such commands
   can be run by CLI, the `@aws/codecatalyst-adk-core` can be used to write the commands. You can also add your own code.

**Example:**

```
// @ts-ignore
import * as core from '@aws/codecatalyst-adk-core';
// @ts-ignore
import * as project from '@aws/codecatalyst-project';
// @ts-ignore
import * as runSummaries from '@aws/codecatalyst-run-summaries';
// @ts-ignore
import * as space from '@aws/codecatalyst-space';

try {
    // Get inputs from the action
    const input_AwsAccessKeyId = core.getInput('AwsAccessKeyId');
    console.log(input_AwsAccessKeyId);
    const input_AwsSecretAccessKey = core.getInput('AwsSecretAccessKey');
    console.log(input_AwsSecretAccessKey);

    // Interact with CodeCatalyst entities
    console.log(`Current CodeCatalyst space ${space.getSpace().name}`);
    console.log(`Current CodeCatalyst project ${project.getProject().name}`);

    // Action Code start

    //aws cli install
    core.command('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"');
    core.command('unzip awscliv2.zip');
    core.command('sudo ./aws/install --update');
    core.command(`aws configure set aws_access_key_id '${input_AwsAccessKeyId}'`);
    core.command(`aws configure set aws_secret_access_key '${input_AwsSecretAccessKey}'`);

    //Amazon CloudWatch install
    core.command('wget https://amazoncloudwatch-agent.s3.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm');

    // Set outputs of the action
} catch (error) {
    core.setFailed(`Action Failed, reason: ${error}`);
}
```

4. Configure the `package.json` file to add a description for the custom action.

**Example:**

```
"description": "This Action creates Actions source code",
```

5. Configure the `README.md` file to add necessary content and procedures for the action. This
   documentation should commmunicate the information to successfully work with the action.
6. (Optional) Navigate to the custom action's directory, and use the print working directory (`pwd`) command to list the
   directory's contents.

**Example:**

```
[mde-user@ip-10-4-87-5 custom-action-repo]$ pwd
/projects/custom-action-repo[mde-user@ip-10-4-87-5 custom-action-repo]$ ls -ltr
total 456
-rw-rw-r--   1 mde-user mde-user    497 Sep 25 02:37 tsconfig.json
-rw-rw-r--   1 mde-user mde-user    808 Sep 25 02:37 jest.config.js
-rw-r--r--   1 mde-user root       5923 Sep 25 02:37 README.md
-rw-rw-r--   1 mde-user mde-user   1051 Sep 25 02:37 LICENSE
-rw-rw-r--   1 mde-user mde-user 413245 Sep 25 02:40 package-lock.json
drwxrwxr-x   2 mde-user mde-user   4096 Sep 25 02:41 lib
drwxrwxr-x   2 mde-user mde-user   4096 Sep 25 02:41 test
drwxrwxr-x 352 mde-user mde-user  12288 Sep 25 02:41 node_modules
drwxrwxr-x   3 mde-user mde-user   4096 Sep 25 02:41 coverage
drwxrwxr-x   2 mde-user mde-user   4096 Sep 25 02:41 dist
-rw-rw-r--   1 mde-user mde-user   1157 Sep 27 02:28 package.json
[mde-user@ip-10-4-87-5 custom-action-repo]$
```

7. Continue with [Step 5: Build the package locally](getting-started.md#build-action-code "getting-started.md#build-action-code"). The following steps
   provide examples of possible outputs.
   1. Run the following npm command to install all the dependencies. These are the necessary
      packages your project depends on to run:

   ```
   npm install
   ```

   After running the npm command, you should see the total number of added packages.

   **Example:**

   ```
   [mde-user@ip-10-4-87-5 custom-action-repo]$ npm install

   up to date, audited 492 packages in 3s

   113 packages are looking for funding
     run `npm fund` for details

   found 0 vulnerabilities
   ```

   2. Run the following command to catch action errors in your action definition YAML
      file:

   ```
   adk validate
   ```

   **Example:**

   ```
   [mde-user@ip-10-4-87-5 custom-action-repo]$ adk validate
   Starting action validation
   Command exit code 0
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
   repositories in CodeCatalyst](../userguide/source-quotas.md "../userguide/source-quotas.md").

   **Example:**

   ```
   [mde-user@ip-10-4-87-5 custom-action-repo]$ npm run all

   > custom-action@1.0.0 all
   > npm run build && npm run format && npm run lint && npm run package


   > custom-action@1.0.0 build
   > tsc


   > custom-action@1.0.0 format
   > prettier --write '**/*.ts'

   lib/index.ts 541ms
   test/index.test.ts 14ms

   > custom-action@1.0.0 lint
   > eslint **/*.ts

   =============

   WARNING: You are currently running a version of TypeScript which is not officially supported by @typescript-eslint/typescript-estree.

   You may find that it works just fine, or you may not.

   SUPPORTED TYPESCRIPT VERSIONS: >=3.3.1 <5.2.0

   YOUR TYPESCRIPT VERSION: 5.2.2

   Please only submit bug reports when using the officially supported version.

   =============

   > custom-action@1.0.0 package
   > tsc && jest && ncc build -o dist

    PASS  test/index.test.js
     CodeCatalyst action custom-action
       ✓ should test the action (1 ms)


   =============================== Coverage summary ===============================
   Statements   : Unknown% ( 0/0 )
   Branches     : Unknown% ( 0/0 )
   Functions    : Unknown% ( 0/0 )
   Lines        : Unknown% ( 0/0 )
   ================================================================================
   Test Suites: 1 passed, 1 total
   Tests:       1 passed, 1 total
   Snapshots:   0 total
   Time:        0.943 s
   Ran all test suites.
   ncc: Version 0.36.1
   ncc: Compiling file index.js into CJS
     1kB  dist/exec-child.js
   211kB  dist/index.js
   212kB  [2403ms] - ncc 0.36.1
   ```

   4. After the action is built, run the following commands to commit the changes to your remote
      repository:

   ###### Important

   Make sure the code you're pushing doesn't contain any sensitive information that
   you don't want to be shared publicly.

   (Optional) You can view the changes that took place, as well as new files generated. Use the `git status`
   command to view the updates.

   **Example:**

   ```
   [mde-user@ip-10-4-87-5 custom-action-repo]$ git status
   On branch feature-custom-action
   Your branch is up to date with 'origin/feature-custom-action'.

   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   .codecatalyst/actions/action.yml
           modified:   .codecatalyst/workflows/custom-action-CI-Validation.yaml
           modified:   dist/index.js
           modified:   lib/index.ts
           modified:   package.json

   no changes added to commit (use "git add" and/or "git commit -a")
   ```

   ```
   git add .
   ```

   ```
   git commit -m "`commit message`"
   ```

   **Example:**

   ```
   [mde-user@ip-10-4-87-5 custom-action-repo]$ git commit -m "added changes and generated files"
   [feature-custom-action c5adf30] added changes and generated files
    5 files changed, 40 insertions(+), 20 deletions(-)
   ```

   ```
   git push
   ```

   **Example:**

   ```
   [mde-user@ip-10-4-87-5 custom-action-repo]$ git push
   Enumerating objects: 23, done.
   Counting objects: 100% (23/23), done.
   Delta compression using up to 2 threads
   Compressing objects: 100% (10/10), done.
   Writing objects: 100% (12/12), 2.04 KiB | 94.00 KiB/s, done.
   Total 12 (delta 4), reused 0 (delta 0), pack-reused 0
   remote: Validating objects: 100%
      0564729..c5adf30  feature-custom-action -> feature-custom-action
   ```

   You can also use the source control options available in the IDE you’re using for your Dev Environment.

## Testing a custom action in a workflow

The action can now be tested with the ADK-generated workflow. By default, the
workflow's name is ``ActionName`-CI-Validation`.

**To test an action within a ADK-generated workflow**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the CodeCatalyst project page.
3. In the navigation pane, choose **CI/CD**, and then choose
   **Workflows**.
4. From the repository and branch dropdown menus, select the repository and feature branch
   in which you created the action and its workflow.
5. Choose the ``ActionName`-CI-Validation` workflow, and
   then choose **Definition** to view the YAML code for the workflow.
6. Choose **Run** to perform the actions defined in the workflow
   configuration file and get the associated logs, artifacts, and variables.
7. View the workflow run status and details.

**To view the status and details of the run**

    1. Choose **View Run-`ID`** from the alert message that appears.
    2. In the workflow diagram, choose the **Validateaction-vs-code** action to view the logs.
    3. Choose the **Logs** tab and expand the sections to reveal the log messages, including possible errors.


    **Example:**



    ```
    691
    You can now run: /usr/local/bin/aws --version
    692--2023-09-30 20:15:56--  https://amazoncloudwatch-agent.s3.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
    693Resolving amazoncloudwatch-agent.s3.amazonaws.com (amazoncloudwatch-agent.s3.amazonaws.com)... 54.231.165.137, 52.217.165.169, 3.5.25.69, ...
    694Connecting to amazoncloudwatch-agent.s3.amazonaws.com (amazoncloudwatch-agent.s3.amazonaws.com)|54.231.165.137|:443... connected.
    695HTTP request sent, awaiting response... 200 OK
    696Length: 66425644 (63M) [application/octet-stream]
    697Saving to: 'amazon-cloudwatch-agent.rpm'

    1998
    2023-09-30 20:15:58 (35.8 MB/s) - 'amazon-cloudwatch-agent.rpm' saved [66425644/66425644]
    1999
    ```For more information, see [Viewing

workflow run status and details](../userguide/workflows-view-run.md "../userguide/workflows-view-run.md") and
[Viewing the deployment
logs](../userguide/deploy-consumption-deployment-logs.md "../userguide/deploy-consumption-deployment-logs.md").

**To test an action in a new workflow**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the CodeCatalyst project page.
3. In the navigation pane, choose **CI/CD**, and then choose
   **Workflows**.
4. From the repository and branch dropdown menus, select the repository and feature branch
   in which you created the action.
5. Choose **Create workflow**, confirm the repository and feature branch in
   which you created the action, and then choose **Create**.
6. Choose **+ Actions**, choose the **Actions** dropdown
   menu, and then choose **Local** to view your custom action.
7. (Optional) Choose the name of the custom action to view the action's details, including
   the description, documentation information, YAML preview, and license file.
8. Choose **+** to add your custom action to the workflow and configure the
   workflow to meet your requirements using the YAML editor or the visual editor. For more
   information, see [Build, test, and
   deploy with workflows in CodeCatalyst](../userguide/flows.md "../userguide/flows.md").
9. (Optional) Choose **Validate** to validate the workflow's YAML code
   before committing.
10. Choose **Commit**, and on the **Commit workflow**
    dialog box, do the following:
    1. For **Workflow file name**, leave the default name or enter your
       own.
    2. For **Commit message**, leave the default message or enter your
       own.
    3. For **Repository** and **Branch**, choose the source
       repository and branch for the workflow definition file. These fields should be set to the
       repository and branch that you specified earlier in the **Create workflow**
       dialog box. You can change the repository and branch now, if you'd like.

    ###### Note

    After committing your workflow definition file, it cannot be associated with another
    repository or branch, so make sure to choose them carefully. 4. Choose **Commit** to commit the workflow definition file.

11. View the workflow run status and details. For more information, see [Viewing workflow run status and details](../userguide/workflows-view-run.md "../userguide/workflows-view-run.md").

## Merge changes into default branch and publish action

After a successful workflow run, merge the feature branch to the default branch in order to publish the action to the
CodeCatalyst actions catalog. For more information, see [Publishing an action](actions-publishing.md "actions-publishing.md").
