Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Troubleshooting problems with workflows

Consult the following sections to troubleshoot problems related to workflows in
Amazon CodeCatalyst. For more information about workflows, see [Build, test, and deploy with workflows](workflow.md "workflow.md").

###### Topics

- [How do I fix "Workflow is inactive"
  messages?](#troubleshooting-workflows-inactive "#troubleshooting-workflows-inactive")
- [How do I fix "Workflow definition
  has n errors" errors?](#troubleshooting-workflows-asterisks "#troubleshooting-workflows-asterisks")
- [How do I fix "Unable to
  locate credentials" and "ExpiredToken" errors?](#troubleshooting-workflows-auth-errors-eks "#troubleshooting-workflows-auth-errors-eks")
- [How do I fix "Unable to
  connect to the server" errors?](#troubleshooting-workflows-unable-connect-eks "#troubleshooting-workflows-unable-connect-eks")
- [Why are CodeDeploy fields missing from
  the visual editor?](#troubleshooting-workflows-codedeploy "#troubleshooting-workflows-codedeploy")
- [How do I fix IAM capabilities
  errors?](#troubleshooting-workflows-capabilities "#troubleshooting-workflows-capabilities")
- [How do I fix "npm install"
  errors?](#troubleshooting-workflows-npm "#troubleshooting-workflows-npm")
- [Why do multiple workflows have the same
  name?](#troubleshooting-workflows-name "#troubleshooting-workflows-name")
- [Can I store my workflow definition
  files in another folder?](#troubleshooting-workflows-folder "#troubleshooting-workflows-folder")
- [How do I add actions in sequence to
  my workflow?](#troubleshooting-workflows-visual "#troubleshooting-workflows-visual")
- [Why does my workflow successfully
  validate but fail at runtime?](#troubleshooting-workflows-validation "#troubleshooting-workflows-validation")
- [Auto-discovery doesn't discover
  any reports for my action](#troubleshooting-reports-auto-discovery "#troubleshooting-reports-auto-discovery")
- [My action fails on
  auto-discovered reports after I configure success criteria](#troubleshooting-success-auto-discovery "#troubleshooting-success-auto-discovery")
- [Auto-discovery generates
  reports that I don't want](#troubleshooting-unwanted-auto-discovery "#troubleshooting-unwanted-auto-discovery")
- [Auto-discovery generates many small
  reports for a single test framework](#troubleshooting-reports-combined "#troubleshooting-reports-combined")
- [Workflows listed under CI/CD don't
  match those in the source repository](#troubleshooting-workflow-source "#troubleshooting-workflow-source")
- [I can't create or update
  workflows](#troubleshooting-workflows-branchrules "#troubleshooting-workflows-branchrules")

## How do I fix "Workflow is inactive"

messages?

**Problem**: In the CodeCatalyst console, under
**CI/CD**, **Workflows**, your workflow appears
with the following message:

`Workflow is inactive.`

This message indicates that the workflow definition file contains a trigger that
doesn't apply to the branch that you're currently on. For example, your workflow
definition file might contain a `PUSH` trigger that references your
`main` branch, but you're on a feature branch. Since the changes you're
making in your feature branch don't apply to `main`, and will not start
workflow runs in `main`, CodeCatalyst decommissions the workflow on the branch and
marks it as `Inactive`.

**Possible fixes**:

If you want to start a workflow on your feature branch, you can do the
following:

- In your feature branch, in the workflow definition file, remove the
  `Branches` property from the `Triggers` section so
  that it looks like this:

```
Triggers:
  - Type: PUSH
```

This configuration causes the trigger to activate on a push to any branch,
including your feature branch. If the trigger is activated, CodeCatalyst will start a
workflow run using the workflow definition file and source files in whatever
branch you're pushing to.

- In your feature branch, in the workflow definition file, remove the
  `Triggers` section and run the workflow manually.
- In your feature branch, in the workflow definition file, change the
  `PUSH` section so that it references your feature branch rather
  than another branch (like `main`, for example).

###### Important

Be careful not to commit these changes if you don't intend to merge them to back
to your `main` branch.

For more information about editing the workflow definition file, see [Creating a workflow](workflows-create-workflow.md "workflows-create-workflow.md").

For more information about triggers, see [Starting a workflow run automatically using
triggers](workflows-add-trigger.md "workflows-add-trigger.md").

## How do I fix "Workflow definition

has `n` errors" errors?

**Problem**: You see any of the following error
messages:

**Error 1:**

In the **CI/CD**, **Workflows** page, under your
workflow's name, you see:

`Workflow definition has `n` errors`

**Error 2:**

While editing a workflow, you choose the **Validate** button and the
following message appears at the top of the CodeCatalyst console:

`The workflow definition has errors. Fix the errors and choose Validate to verify
 your changes.`

**Error 3:**

After navigating to your workflow's details page, you see the following error in the
**Workflow definition** field:

``n` errors`

**Possible fixes**:

- Choose **CI/CD**, choose **Workflows**, and
  choose the name of the workflow that has the error. In the **Workflow
  definition** field near the top, choose the link to the error.
  Details about the error appear at the bottom of the page. Follow the
  troubleshooting tips in the error to fix the issue.
- Make sure that the workflow definition file is a YAML file.
- Make sure that the YAML properties in the workflow definition file are nested
  at the right level. To see how properties should be nested in the workflow
  definition file, refer to the [Workflow YAML definition](workflow-reference.md "workflow-reference.md"), or consult your action's
  documentation, which is linked to from [Adding an action to a workflow](workflows-add-action.md "workflows-add-action.md").
- Make sure that asterisks (`*`) and other special characters are
  escaped properly. To escape them, add single or double quotes. For
  example:

```
Outputs:
  Artifacts:
    - Name: myartifact
      Files:
        - `"**/*"`
```

For more information about special characters in the workflow definition file,
see [Syntax guidelines and conventions](workflow-reference.md#workflow.terms.syntax.conv "workflow-reference.md#workflow.terms.syntax.conv").

- Make sure that the YAML properties in the workflow definition file use the
  right capitalization. For more information about casing rules, see [Syntax guidelines and conventions](workflow-reference.md#workflow.terms.syntax.conv "workflow-reference.md#workflow.terms.syntax.conv"). To determine the correct
  casing of each property, refer to the [Workflow YAML definition](workflow-reference.md "workflow-reference.md"), or consult your action's
  documentation, which is linked to from [Adding an action to a workflow](workflows-add-action.md "workflows-add-action.md").
- Make sure that the `SchemaVersion` property is present and set to
  the correct version in the workflow definition file. For more information, see
  [SchemaVersion](workflow-reference.md#workflow.schemaversion "workflow-reference.md#workflow.schemaversion").
- Make sure that the `Triggers` section in the workflow definition
  file includes all required properties. To determine the required properties,
  choose the trigger in the [visual editor](workflow.md#workflow.editors "workflow.md#workflow.editors")
  and look for fields that are missing information, or consult the trigger
  reference documentation at [Triggers](workflow-reference.md#triggers-reference "workflow-reference.md#triggers-reference").
- Make sure that the `DependsOn` property in the workflow definition
  file is properly configured and does not introduce circular dependencies. For
  more information, see [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md").
- Make sure that the `Actions` section in the workflow definition
  file includes at least one action. For more information, see [Actions](workflow-reference.md#actions-reference "workflow-reference.md#actions-reference").
- Make sure that each action includes all required properties. To determine the
  required properties, choose the action in the [visual editor](workflow.md#workflow.editors "workflow.md#workflow.editors") and look for fields that are missing information, or
  consult your action's documentation, which is linked to from [Adding an action to a workflow](workflows-add-action.md "workflows-add-action.md").
- Make sure that all input artifacts have corresponding output artifacts. For
  more information, see [Defining an output artifact](workflows-working-artifacts-output.md "workflows-working-artifacts-output.md").
- Make sure that variables defined in one action are exported so that they can
  be used in other actions. For more information, see [Exporting a variable
  so that other actions can use it](workflows-working-with-variables-export-input.md "workflows-working-with-variables-export-input.md").

## How do I fix "Unable to

locate credentials" and "ExpiredToken" errors?

**Problem**: While working through [Tutorial: Deploy an application to Amazon EKS](deploy-tut-eks.md "deploy-tut-eks.md"), you see one or both of
the following error messages in your development machine's terminal window:

`Unable to locate credentials. You can configure credentials by running "aws
 configure".`

`ExpiredToken: The security token included in the request is expired`

**Possible fixes**:

These errors indicate that the credentials that you're using to access AWS services
have expired. In this case, do not run the `aws configure` command. Instead,
use the following instructions to refresh your AWS access key and session
token.

###### To refresh your AWS access key and session token

1. Make sure you have the AWS access portal URL, username, and password for the
   user that you're using the complete the Amazon EKS tutorial
   (`codecatalyst-eks-user`). You should have configured these
   items when you completed [Step 1: Set up your development
   machine](deploy-tut-eks.md#deploy-tut-eks-dev-env-create "deploy-tut-eks.md#deploy-tut-eks-dev-env-create") of the tutorial.

###### Note

If you do not have this information, go to the
`codecatalyst-eks-user` details page in IAM Identity Center, choose
**Reset password**, **Generate a one-time
password [...]**, and **Reset password** again
to display the information on the screen. 2. Do one of the following:

    * Paste the AWS access portal URL into your browser's address
     bar.


    Or
    * Refresh the AWS access portal page if it's already loaded.

3. Sign in with the `codecatalyst-eks-user`'s username and
   password, if you're not already signed in.
4. Choose **AWS account**, and then choose the name of the
   AWS account to which you assigned the `codecatalyst-eks-user`
   user and permission set.
5. Next to the permission set name
   (`codecatalyst-eks-permission-set`), choose **Command
   line or programmatic access**.
6. Copy the commands in the middle of the page. They look similar to the
   following:

```
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
export AWS_SESSION_TOKEN="`session-token`"
```

...where `session-token` is a long random
string. 7. Paste the commands into your terminal prompt on your development machine and
press Enter.

The new keys and session token are loaded.

You have now refreshed your credentials. The AWS CLI, `eksctl`, and
`kubectl` commands should now work.

## How do I fix "Unable to

connect to the server" errors?

**Problem**: While working through the tutorial described
in [Tutorial: Deploy an application to Amazon EKS](deploy-tut-eks.md "deploy-tut-eks.md"), you see an error
message similar to the following in your development machine's terminal window:

`Unable to connect to the server: dial tcp: lookup
 `long-string`.gr7.us-west-2.eks.amazonaws.com on
 `1.2.3.4:5`: no such host`

**Possible fixes**:

This error usually indicates that the credentials that the `kubectl`
utility is using to connect to your Amazon EKS cluster have expired. To solve the issue,
refresh the credentials by entering the following command at the terminal prompt:

```
aws eks update-kubeconfig --name `codecatalyst-eks-cluster` --region `us-west-2`
```

Where:

- `codecatalyst-eks-cluster` is replaced with the name
  of your Amazon EKS cluster.
- `us-west-2` is replaced with the AWS Region where
  your cluster is deployed.

## Why are CodeDeploy fields missing from

the visual editor?

**Problem**: You are using a [Deploy to Amazon ECS](deploy-action-ecs.md "deploy-action-ecs.md") action, and you are not seeing
the CodeDeploy fields such as **CodeDeploy AppSpec** in the workflow's visual
editor. This problem may occur because the Amazon ECS service that you specified in the
**Service** field is not configured to perform blue/green
deployments.

**Possible fixes**:

- Choose a different Amazon ECS service on the **Deploy to Amazon ECS**
  action's **Configuration** tab. For more information, see [Deploying to Amazon ECS with a workflow](deploy-action-ecs.md "deploy-action-ecs.md").
- Configure the selected Amazon ECS service to perform blue/green deployments. For
  more information about configuring blue/green deployments, see [Blue/Green deployment with CodeDeploy](../../../AmazonECS/latest/developerguide/deployment-type-bluegreen.md "../../../AmazonECS/latest/developerguide/deployment-type-bluegreen.md") in the
  _Amazon Elastic Container Service Developer Guide_.

## How do I fix IAM capabilities

errors?

**Problem**: You are using a [Deploy CloudFormation stack](deploy-action-cfn.md "deploy-action-cfn.md") action, and you see
`##[error] requires capabilities:
 [`capability-name`]` in your **Deploy CloudFormation
stack** action's logs.

**Possible fixes**: Complete the following procedure to
add the capability to the workflow definition file. For more information about IAM
capabilities, see [Acknowledging IAM resources in CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md#using-iam-capabilities "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md#using-iam-capabilities") in the
_IAM User Guide_.

Visual

###### To add an IAM capability using the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, choose your **Deploy CloudFormation
   stack** action.
8. Choose the **Configuration** tab.
9. At the bottom, choose **Advanced -
   optional**.
10. In the **Capabilities** drop-down list, select
    the check box next to the capability mentioned in the error message.
    If the capability is not available in the list, use the YAML editor
    to add it.
11. (Optional) Choose **Validate** to validate the
    workflow's YAML code before committing.
12. Choose **Commit**, enter a commit message, and
    choose **Commit** again.
13. If a new workflow run doesn't start automatically, run the
    workflow manually to see if the changes fix the error. For more
    information about running a workflow manually, see [Starting a workflow run manually](workflows-manually-start.md "workflows-manually-start.md").

YAML

###### To add an IAM capability using the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In the **Deploy CloudFormation stack** action, add a
   `capabilities` property, like this:

```
DeployCloudFormationStack:
  Configuration:
    capabilities: `capability-name`
```

Replace `capability-name` with the name
of the IAM capability shown in the error message. Use commas and
no spaces to list multiple capabilities. For more information, see
the description of the `capabilities` property in the
['Deploy CloudFormation stack' action YAML](deploy-action-ref-cfn.md "deploy-action-ref-cfn.md"). 8. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message, and
choose **Commit** again. 10. If a new workflow run doesn't start automatically, run the
workflow manually to see if the changes fix the error. For more
information about running a workflow manually, see [Starting a workflow run manually](workflows-manually-start.md "workflows-manually-start.md").

## How do I fix "npm install"

errors?

**Problem**: Your [AWS CDK
deploy action](cdk-dep-action.md "cdk-dep-action.md") or [AWS CDK bootstrap
action](cdk-boot-action.md "cdk-boot-action.md") fails with an `npm install` error. This error may occur
because you are storing your AWS CDK app dependencies in a private node package manager
(npm) registry that cannot be accessed by the action.

**Possible fixes**: Use the following instructions to
update your AWS CDK app's `cdk.json` file with additional registry and
authentication information.

###### Before you begin

1. Create secrets for your authentication information. You'll reference these
   secrets in the `cdk.json` file instead of providing the
   cleartext equivalents. To create the secrets:
   1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
   2. Choose your project.
   3. In the navigation pane, choose **CI/CD**, and then
      choose **Secrets**.
   4. Create two secrets with the following properties:

   | First secret                                                                                                                                                                                                                                                       | Second secret                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Name**:<br>`npmUsername`<br>**Value**:<br>`npm-username`, where<br>`npm-username` is the<br>username used to authenticate to your private npm<br>registry.<br>(Optional) **Description**:<br>`The username used to authenticate to the<br>private npm registry.` | **Name**:<br>`npmAuthToken`<br>**Value**:<br>`npm-auth-token`, where<br>`npm-auth-token` is the<br>access token used to authenticate to your private<br>npm registry. For more information about npm access<br>tokens, see [About access tokens](https://docs.npmjs.com/about-access-tokens "https://docs.npmjs.com/about-access-tokens") in the npm<br>documentation.<br>(Optional) **Description**:<br>`The access token used to authenticate to the<br>private npm registry.` |

   For more information about secrets, see [Masking data using secrets](workflows-secrets.md "workflows-secrets.md").

2. Add the secrets as environment variables to your AWS CDK action. The action will
   replace the variables with real values when it runs. To add the secrets:
   1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
   2. Choose the name of your workflow. You can filter by the source
      repository or branch name where the workflow is defined, or filter
      by workflow name or status.
   3. Choose **Edit**.
   4. Choose **Visual**.
   5. In the workflow diagram, choose your AWS CDK action.
   6. Choose the **Inputs** tab.
   7. Add two variables with the following properties:

   | First variable                                                   | Second variable                                                    |
   | ---------------------------------------------------------------- | ------------------------------------------------------------------ |
   | **Name**:<br>`NPMUSER`<br>**Value**:<br>`${Secrets.npmUsername}` | **Name**:<br>`NPMTOKEN`<br>**Value**:<br>`${Secrets.npmAuthToken}` |

   You now have two variables containing references to secrets.Your workflow definition file YAML code should look similar to the
   following:

###### Note

The following code sample is from an **AWS CDK bootstrap**
action; a **AWS CDK deploy** action will look similar.

```
Name: CDK_Bootstrap_Action
SchemaVersion: 1.0
Actions:
  CDKBootstrapAction:
    Identifier: aws/cdk-bootstrap@v2
    Inputs:
      Variables:
        - Name: NPMUSER
          Value: ${Secrets.npmUsername}
        - Name: NPMTOKEN
          Value: ${Secrets.npmAuthToken}
      Sources:
        - WorkflowSource
    Environment:
      Name: Dev2
      Connections:
        - Name: account-connection
          Role: codecatalystAdmin
    Configuration:
      Parameters:
        Region: "us-east-2"
```

You are now ready to use the `NPMUSER` and `NPMTOKEN`
variables in your `cdk.json` file. Go to the next
procedure.

###### To update your cdk.json file

1. Change to the root directory of your AWS CDK project, and open the
   `cdk.json` file.
2. Find the `"app":` property, and change it to include the code shown
   in `red italics`:

###### Note

The following sample code is from a TypeScript project. If you're using a
JavaScript project, the code will look similar though not identical.

```
{
  "app": `"npm set registry=https://your-registry/folder/CDK-package/ --userconfig .npmrc && npm set //your-registry/folder/CDK-package/:always-auth=true --userconfig .npmrc && npm set //your-registry/folder/CDK-package/:_authToken=\"${NPMUSER}\":\"${NPMTOKEN}\" && npm install && npx ts-node --prefer-ts-exts bin/hello-cdk.ts|js",`
  "watch": {
    "include": [
      "**"
    ],
    "exclude": [
      "README.md",
      "cdk*.json",
      "**/*.d.ts",
      "**/*.js",
      "tsconfig.json",
      "package*.json",
...
```

3. In the code highlighted in `red italics`,
   replace:
   - `your-registry/folder/CDK-package/`
     with the path to your AWS CDK project dependencies in your private
     registry.
   - `hello-cdk.ts|.js` with the name of your
     entrypoint file. This may be a `.ts` (TypeScript) or
     `.js` (JavaScript) file depending on the language you're
     using.

   ###### Note

   The action will replace the `NPMUSER` and
   `NPMTOKEN` variables with the npm
   username and access token that you specified in
   **Secrets**.

4. Save your `cdk.json` file.
5. Re-run the action manually to see if the changes fix the error. For more
   information about running actions manually, see [Starting a workflow run manually](workflows-manually-start.md "workflows-manually-start.md").

## Why do multiple workflows have the same

name?

Workflows are stored per branch per repository. Two different workflows can have the
same name if they exist in different branches. In the Workflows page, you can
differentiate workflows of the same name by looking at the branch name. For more
information, see [Organizing your source code work with branches in
Amazon CodeCatalyst](source-branches.md "source-branches.md").

![Workflow branch](images/flows/workflow-branch.png)

## Can I store my workflow definition

files in another folder?

No, you must store all workflow definition files in the
`.codecatalyst/workflows` folder, or in subfolders of that folder. If
you are using a mono repo with multiple logical projects, place all your workflow
definition files in the `.codecatalyst/workflows` folder or one of its
subfolders, and then use the **Files changed** field (visual editor) or
`FilesChanged` property (YAML editor) inside a trigger to trigger the
workflow automatically at a specified project path. For more information,
see [Adding triggers to workflows](workflows-add-trigger-add.md "workflows-add-trigger-add.md") and [Example: A trigger with
a push, branches, and files](workflows-add-trigger-examples.md#workflows-add-trigger-examples-push-multi "workflows-add-trigger-examples.md#workflows-add-trigger-examples-push-multi").

## How do I add actions in sequence to

my workflow?

By default, when you add an action to your workflow, it will have no dependencies and
will run in parallel with other actions.

If you want to arrange actions in sequence, you can set a dependency on another action
by setting the `DependsOn` field. You can also configure an action to consume
artifacts or variables which are outputs of other actions. For more information, see
[Sequencing actions](workflows-depends-on.md "workflows-depends-on.md").

## Why does my workflow successfully

validate but fail at runtime?

If you validated your workflow using the `Validate` button, but your
workflow failed anyway, it might because a limitation in the validator.

Any errors in reference to a CodeCatalyst resource like secrets, environments, or fleets in
the workflow configuration will not register during a commit. If any references that
aren't valid are used, the error will only be identified when a workflow is run.
Similarly, if there are any errors in your action configuration like missing a required
field or typos in action attributes, they will be identified only when the workflow is
run. For more information, see [Creating a workflow](workflows-create-workflow.md "workflows-create-workflow.md").

## Auto-discovery doesn't discover

any reports for my action

**Problem:** I configured auto-discovery for an action
that runs tests, but no reports are discovered by CodeCatalyst.

**Possible fixes:** This might be caused by a number of
issues. Try one or more of the following solutions:

- Make sure that the tool used to run tests produces outputs in one of the
  formats that CodeCatalyst understands. For example, if you would like
  `pytest` to allow CodeCatalyst to discover test and code coverage
  reports, include the following arguments:

```
--junitxml=test_results.xml --cov-report xml:test_coverage.xml
```

For more information, see [Quality report types](test-workflow-actions.md#test-reporting "test-workflow-actions.md#test-reporting").

- Make sure that the file extension for the outputs are consistent with the
  chosen format. For example, when configuring `pytest` to produce
  results in `JUnitXML` format, check that the file extension is
  `.xml`. For more information, see [Quality report types](test-workflow-actions.md#test-reporting "test-workflow-actions.md#test-reporting").
- Make sure that `IncludePaths` is configured to include the entire
  file system (`**/*`) unless you are excluding certain folders on
  purpose. Similarly, make sure that `ExcludePaths` don't exclude
  directories where you expect your reports to be located.
- If you manually configured a report to use a specific output file, it will be
  excluded from auto-discovery. For more information, see [Quality reports YAML example](test-config-action.md#test.success-criteria-example "test-config-action.md#test.success-criteria-example").
- Auto-discovery may not find reports because the action failed before any
  outputs were generated. For example, the build may have failed before any unit
  tests have been run.

## My action fails on

auto-discovered reports after I configure success criteria

**Problem:** When I enable auto-discovery and configure
success criteria, some of the reports don't meet the success criteria and the action
fails as a result.

**Possible fixes:** To resolve this, try one or more of
the following solutions:

- Modify `IncludePaths` or `ExcludePaths` to exclude
  reports that you are not interested in.
- Update success criteria to allow all reports to pass. For example, if two
  reports were discovered with one having line coverage of 50% and another one of
  70%, adjust the minimum line coverage to 50%. For more information, see [Success criteria](test-best-practices.md#test.best-success-criteria "test-best-practices.md#test.best-success-criteria")
- Turn the failing report into a manually configured report. This allows you to
  configure different success criteria for that specific report. For more
  information, see [Configuring success criteria for reports](test-config-action.md#test.success-criteria "test-config-action.md#test.success-criteria").

## Auto-discovery generates

reports that I don't want

**Problem:** When I enable auto-discovery, it generates
reports that I don't want. For example, CodeCatalyst generates code coverage reports for files
included in my application’s dependencies stored in `node_modules`.

**Possible fixes:** You can adjust the
`ExcludePaths` configuration to exclude unwanted files. For example, to
exclude `node_modules`, add `node_modules/**/*`. For more
information, see [Include/exclude paths](test-best-practices.md#test.best-include-exclude "test-best-practices.md#test.best-include-exclude").

## Auto-discovery generates many small

reports for a single test framework

**Problem:** When I use certain test and code coverage
reporting frameworks, I noticed that auto-discovery generates a large number of reports.
For example, when using the [Maven Surefire
Plugin](https://maven.apache.org/surefire/maven-surefire-plugin/ "https://maven.apache.org/surefire/maven-surefire-plugin/"), auto-discovery produces a different report for each test class.

**Possible fixes:** Your framework may be able to
aggregate outputs into a single file. For example, if you are using Maven Surefire
Plugin, you can use `npx junit-merge` to aggregate the files manually. The
full expression may look like this:

```
mvn test; cd `test-package-path`/surefire-reports && npx junit-merge -d ./ && rm *Test.xml
```

## Workflows listed under CI/CD don't

match those in the source repository

**Problem:** The workflows displayed on the
**CI/CD**, **Workflows** page do not match those
in the `~/.codecatalyst/workflows/` folder in your [source repository](source.md "source.md"). You may see the following
mismatches:

- A workflow appears on the **Workflows** page, but a
  corresponding workflow definition file does not exist in your source
  repository.
- A workflow definition file exists in your source repository, but a
  corresponding workflow does not appear on the **Workflows**
  page.
- A workflow exists in both the source repository and
  **Workflows** page, but the two are different.

This problem may occur if the **Workflows** page hasn't had time to
refresh, or if a workflow quota was exceeded.

**Possible fixes:**

- Wait. You usually have to wait two or three seconds after a commit to source
  before you see the change on the **Workflows** page.
- If you've exceeded a workflow quota, do one of the following:

###### Note

To determine whether a workflow quota was exceeded, review [Quotas for workflows in CodeCatalyst](workflows-quotas.md "workflows-quotas.md"), and
cross-check the documented quotas against the workflows in your source
repository or on the **Workflows** page. There is no
error message to indicate that a quota was exceeded, so you'll have to
investigate on your own.

    + If you've exceeded the **Maximum number of
     workflows per space** quota, delete some workflows and then
     perform a test commit against the workflow definition file. An example
     of a test commit might be to add a space to the file.
    + If you've exceeded the **Maximum workflow
     definition file size** quota, change the workflow
     definition file to reduce its length.
    + If you've exceeded the **Maximum number of
     workflow files processed in a single source event** quota,
     perform several test commits. Modify fewer than the maximum number of
     workflows in each commit.

## I can't create or update

workflows

**Problem:** I want create or update a workflow, but I
see an error when I try to commit the change.

**Possible fixes:** Depending on your role in the project
or space, you might not have permissions to push code to source repositories in the
project. The YAML files for workflows are stored in repositories. For more information,
see [Workflow definition files](workflows-concepts.md#workflows-concepts-workflows-def "workflows-concepts.md#workflows-concepts-workflows-def"). The
**Space administrator** role,
**Project administrator** role, and
**Contributor** role all have permission to commit and push
code to repositories in a project.

If you have the **Contributor** role but cannot create or
commit changes to workflow YAML in a specific branch, there might be a branch rule
configured for that branch that prevents users with that role from pushing code to that
particular branch. Try creating a workflow in a different branch, or commiting your
changes to a different branch. For more information, see [Manage allowed actions for a branch with
branch rules](source-branches-branch-rules.md "source-branches-branch-rules.md").
