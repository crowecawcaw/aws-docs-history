Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'GitHub Actions' action YAML

The following is the YAML definition of the **GitHub
Actions** action.

This action definition exists as a section within a broader workflow definition file. For more
information about this file, see [Workflow YAML definition](workflow-reference.md "workflow-reference.md").

Choose a YAML property in the following code to see a description if it.

###### Note

Most of the YAML properties that follow have corresponding UI elements in the visual
editor. To look up a UI element, use **Ctrl+F**. The element will be
listed with its associated YAML property.

```
# The workflow definition starts here.
# See Top-level properties for details.

Name: MyWorkflow
SchemaVersion: 1.0
Actions:

# The action definition starts here.
  `action-name`:
    Identifier:  aws/github-actions-runner@v1
    DependsOn:
      - `dependent-action-name-1`
    Compute:
      Fleet: `fleet-name`
    Timeout: `timeout-minutes`
    Environment:
      Name: `environment-name`
      Connections:
        - Name: `account-connection-name`
          Role: `iam-role-name`
    Inputs:
      Sources:
        - `source-name-1`
        - `source-name-2`
      Artifacts:
        - `artifact-name`
      Variables:
        - Name: `variable-name-1`
          Value: `variable-value-1`
        - Name: `variable-name-2`
          Value: `variable-value-2`
    Outputs:
      Artifacts:
        - Name: `output-artifact-1`
          Files:
            - github-output/artifact-1.jar
            - "github-output/build*"
        - Name: `output-artifact-2`
          Files:
            - github-output/artifact-2.1.jar
            - github-output/artifact-2.2.jar
      Variables:
        - `variable-name-1`
        - `variable-name-2`
      AutoDiscoverReports:
        Enabled: `true | false`
        ReportNamePrefix: `AutoDiscovered`
        IncludePaths:
          - "**/*"
        ExcludePaths:
          - node_modules/cdk/junit.xml
        SuccessCriteria:
          PassRate: `percent`
          LineCoverage: `percent`
          BranchCoverage: `percent`
          Vulnerabilities:
            Severity: `CRITICAL|HIGH|MEDIUM|LOW|INFORMATIONAL`
            Number: `whole-number`
      Reports:
        `report-name-1:`
          Format: `format`
          IncludePaths:
            - "*.xml"
          ExcludePaths:
            - report2.xml
            - report3.xml
          SuccessCriteria:
            PassRate: `percent`
            LineCoverage: `percent`
            BranchCoverage: `percent`
            Vulnerabilities:
              Severity: `CRITICAL|HIGH|MEDIUM|LOW|INFORMATIONAL`
              Number: `whole-number`
    Configuration
      Steps:
        - `github-actions-code`
```

## action-name

(Required)

Specify the name of the action. All action names must be unique within the workflow. Action names are limited to
alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
You cannot use quotation marks to enable special characters and spaces in action names.

Corresponding UI: Configuration tab/`action-name`

## Identifier

(`action-name`/**Identifier**)

Identifies the action. Do not change this property unless you want to change the version. For
more information, see [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md").

Use `aws/github-actions-runner@v1` for **GitHub
Actions** actions.

Corresponding UI: Workflow
diagram/`action-name`/**aws/github-actions-runner@v1**
label

## DependsOn

(`action-name`/**DependsOn**)

(Optional)

Specify an action, action group, or gate that must run successfully in order for this action to
run.

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md").

Corresponding UI: Inputs tab/**Depends on - optional**

## Compute

(`action-name`/**Compute**)

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level,
but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow
level, you can also run multiple actions on the same instance. For more information, see
[Sharing compute across actions](compute-sharing.md "compute-sharing.md").

Corresponding UI: _none_

## Fleet

(`action-name`/Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand "workflows-working-compute.md#compute.on-demand").

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

Corresponding UI: Configuration tab/**Compute fleet -
optional**

## Timeout

(`action-name`/**Timeout**)

(Optional)

Specify the amount of time in minutes (YAML editor), or hours and minutes (visual editor),
that the action can run before CodeCatalyst ends the action. The minimum is 5 minutes and the maximum is
described in [Quotas for workflows in CodeCatalyst](workflows-quotas.md "workflows-quotas.md"). The default timeout is
the same as the maximum timeout.

Corresponding UI: Configuration tab/**Timeout - optional**

## Environment

(`action-name`/**Environment**)

(Optional)

Specify the CodeCatalyst environment to use with the action. The action connects to
the AWS account and optional Amazon VPC specified in the chosen environment. The action uses the
default IAM role specified in the environment to connect to the AWS account, and uses the
IAM role specified in the [Amazon VPC connection](../adminguide/managing-vpcs.md "../adminguide/managing-vpcs.md") to
connect to the Amazon VPC.

###### Note

If the default IAM role does not have the permissions required by the action, you can
configure the action to use a different role. For more information, see [Changing the IAM role of an action](deploy-environments-switch-role.md "deploy-environments-switch-role.md").

For more information about environments, see [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md") and [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").

Corresponding UI: Configuration
tab/**Environment**

## Name

(`action-name`/Environment/**Name**)

(Required if [Environment](#github.environment "#github.environment") is included)

Specify the name of an existing environment that you want to associate with the action.

Corresponding UI: Configuration
tab/**Environment**

## Connections

(`action-name`/Environment/**Connections**)

(Optional)

Specify the account connection to associate with the action. You can specify a maximum of
one account connection under `Environment`.

If you do not specify an account connection:

- The action uses the AWS account connection and default IAM role specified in the
  environment in the CodeCatalyst console. For information about adding an account connection and
  default IAM role to environment, see [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").
- The default IAM role must include the policies and permissions required by the action.
  To determine what those policies and permissions are, see the description of the **Role** property in the action's YAML definition documentation.

For more information about account connections, see [Allowing access to AWS resources with connected
AWS accounts](ipa-connect-account.md "ipa-connect-account.md"). For information about adding an account connection to
an environment, see [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").

Corresponding UI: Configuration tab/Environment/What's in
`my-environment`?/three dot menu/**Switch role**

## Name

(`action-name`/Environment/Connections/**Name**)

(Required if [Connections](#github.environment.connections "#github.environment.connections") is included)

Specify the name of the account connection.

Corresponding UI: Configuration tab/Environment/What's in
`my-environment`?/three dot menu/**Switch role**

## Role

(`action-name`/Environment/Connections/**Role**)

(Required if [Connections](#github.environment.connections "#github.environment.connections") is included)

Specify the name of the IAM role that this action uses in order to access and operate in
AWS services such as Amazon S3 and Amazon ECR. Make sure this role is added to your AWS account
connection in your space. To add an IAM role to an account connection, see [Adding IAM roles to account
connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").

If you do not specify an IAM role, then the action uses the default IAM role listed in
the [environment](deploy-environments.md "deploy-environments.md") in the CodeCatalyst console. If you use the
default role in the environment, make sure it has the following policies.

###### Note

You can use the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role with this action.
 For more information about this role, see [Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
 and space](ipa-iam-roles.md#ipa-iam-roles-service-create "ipa-iam-roles.md#ipa-iam-roles-service-create"). Understand that the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role has
full access permissions which may pose a security risk. We recommend that you only use this
role in tutorials and scenarios where security is less of a concern.

###### Warning

Limit the permissions to those required by the **GitHub Action**
action. Using a role with broader permissions might pose a security risk.

Corresponding UI: Configuration tab/Environment/What's in
`my-environment`?/three dot menu/**Switch role**

## Inputs

(`action-name`/**Inputs**)

(Optional)

The `Inputs` section defines the data that an action needs during a
workflow run.

###### Note

A maximum of four inputs (one source and three artifacts) are allowed per
**GitHub Actions** action. Variables do not count towards this
total.

If you need to refer to files residing in different inputs (say a source and an
artifact), the source input is the primary input, and the artifact is the secondary
input. References to files in secondary inputs take a special prefix to distiguish them
from the primary. For details, see [Example: Referencing files
in multiple artifacts](workflows-working-artifacts-ex.md#workflows-working-artifacts-ex-ref-file "workflows-working-artifacts-ex.md#workflows-working-artifacts-ex-ref-file").

Corresponding UI: **Inputs** tab

## Sources

(`action-name`/Inputs/**Sources**)

(Optional)

Specify the labels that represent the source repositories that will be needed by the action.
Currently, the only supported label is `WorkflowSource`, which represents the source
repository where your workflow definition file is stored.

If you omit a source, then you must specify at least one input artifact under
``action-name`/Inputs/Artifacts`.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md "workflows-sources.md").

Corresponding UI: Inputs tab/**Sources - optional**

## Artifacts - input

(`action-name`/Inputs/**Artifacts**)

(Optional)

Specify artifacts from previous actions that you want to provide as input to this action.
These artifacts must already be defined as output artifacts in previous actions.

If you do not specify any input artifacts, then you must specify at least one source
repository under ``action-name`/Inputs/Sources`.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

###### Note

If the **Artifacts - optional** drop-down list is unavailable (visual
editor), or if you get errors in when you validate your YAML (YAML editor), it might be because
the action only supports one input. In this case, try removing the source input.

Corresponding UI: Inputs tab/**Artifacts - optional**

## Variables - input

(`action-name`/Inputs/**Variables**)

(Optional)

Specify a sequence of name/value pairs that define the input variables that you want to make
available to the action. Variable names are limited to alphanumeric characters (a-z, A-Z, 0-9),
hyphens (-), and underscores (\_). Spaces are not allowed. You cannot use quotation marks to
enable special characters and spaces in variable names.

For more information about variables, including examples, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

Corresponding UI: Inputs tab/**Variables - optional**

## Outputs

(`action-name`/**Outputs**)

(Optional)

Defines the data that is output by the action during a workflow run.

Corresponding UI: **Outputs** tab

## Artifacts - output

(`action-name`/Outputs/**Artifacts**)

(Optional)

Specify the name of an artifact generated by the action. Artifact names must be unique
within a workflow, and are limited to alphanumeric characters (a-z, A-Z, 0-9) and underscores (\_).
Spaces, hyphens (-), and other special characters are not allowed. You cannot use quotation
marks to enable spaces, hyphens, and other special characters in output artifact names.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Outputs tab/**Artifacts**

## Name

(`action-name`/Outputs/Artifacts/**Name**)

(Required if [Artifacts - output](#github.outputs.artifacts "#github.outputs.artifacts") is included)

Specify the name of an artifact generated by the action. Artifact names must be unique
within a workflow, and are limited to alphanumeric characters (a-z, A-Z, 0-9) and underscores (\_).
Spaces, hyphens (-), and other special characters are not allowed. You cannot use quotation
marks to enable spaces, hyphens, and other special characters in output artifact names.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Outputs tab/Artifacts/Add artifact/**Build artifact
name**

## Files

(`action-name`/Outputs/Artifacts/**Files**)

(Required if [Artifacts - output](#github.outputs.artifacts "#github.outputs.artifacts") is included)

Specify the files that CodeCatalyst includes in the artifact that is output by the action. These
files are generated by the workflow action when it runs, and are also available in your source
repository. File paths can reside in a source repository or an artifact from a previous
action, and are relative to the source repository or artifact root. You can use glob patterns
to specify paths. Examples:

- To specify a single file that is in the root of your build location or source repository
  location, use `my-file.jar`.
- To specify a single file in a subdirectory, use
  `directory/my-file.jar` or
  `directory/subdirectory/my-file.jar`.
- To specify all files, use `"**/*"`. The `**` glob pattern
  indicates to match any number of subdirectories.
- To specify all files and directories in a directory named
  `directory`, use `"directory/**/*"`. The
  `**` glob pattern indicates to match any number of subdirectories.
- To specify all files in a directory named `directory`, but not any of
  its subdirectories, use `"directory/*"`.

###### Note

If your file path includes one or more asterisks (`*`) or other special
character, enclose the path with double quotation marks (`""`). For more
information about special characters, see [Syntax guidelines and conventions](workflow-reference.md#workflow.terms.syntax.conv "workflow-reference.md#workflow.terms.syntax.conv").

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

###### Note

You may need to add a prefix to the file path to indicate which artifact or source to find
it in. For more information, see [Referencing source repository
files](workflows-sources-reference-files.md "workflows-sources-reference-files.md") and [Referencing files in an
artifact](workflows-working-artifacts-refer-files.md "workflows-working-artifacts-refer-files.md").

Corresponding UI: Outputs tab/Artifacts/Add artifact/**Files produced by
build**

## Variables - output

(`action-name`/Outputs/**Variables**)

(Optional)

Specify the variables that you want the
action to export so that they are available for use by subsequent actions.

For more information about variables, including examples, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

Corresponding UI: Outputs tab/Variables/**Add variable**

## variable-name-1

(`action-name`/Outputs/Variables**variable-name-1**)

(Optional)

Specify the name of a variable that you want the action to export. This variable must already be
defined in the `Inputs` or `Steps` section of the same action.

For more information about variables, including examples, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

Corresponding UI: Outputs tab/Variables/Add variable/**Name**

## AutoDiscoverReports

(`action-name`/Outputs/**AutoDiscoverReports**)

(Optional)

Defines the configuration for the auto-discovery feature.

When you enable auto-discovery, CodeCatalyst searches all `Inputs` passed into the action
as well as all files generated by the action itself, looking for test, code coverage, and software
composition analysis (SCA) reports. For each report that is found, CodeCatalyst transforms it into a
CodeCatalyst report. A _CodeCatalyst report_ is a report that is fully integrated into the
CodeCatalyst service and can be viewed and manipulated through the CodeCatalyst console.

###### Note

By default, the auto-discover feature inspects all files. You can limit which
files are inspected using the [IncludePaths](#github.reports.includepaths "#github.reports.includepaths") or [ExcludePaths](#github.reports.excludepaths "#github.reports.excludepaths") properties.

Corresponding UI: _none_

## Enabled

(`action-name`/Outputs/AutoDiscoverReports/**Enabled**)

(Optional)

Enable or disable the auto-discovery feature.

Valid values are `true` or `false`.

If `Enabled` is omitted, the default is `true`.

Corresponding UI: Outputs tab/Reports/**Automatically discover
reports**

## ReportNamePrefix

(`action-name`/Outputs/AutoDiscoverReports/**ReportNamePrefix**)

(Required if [AutoDiscoverReports](#github.outputs.autodiscover "#github.outputs.autodiscover") is included and enabled)

Specify a prefix that CodeCatalyst prepends to all the reports it finds in order to name
their associated CodeCatalyst reports. For example, if you specify a prefix of `AutoDiscovered`, and CodeCatalyst
auto-discovers two test reports, `TestSuiteOne.xml` and
`TestSuiteTwo.xml`, then the associated CodeCatalyst reports will be
named `AutoDiscoveredTestSuiteOne` and
`AutoDiscoveredTestSuiteTwo`.

Corresponding UI: Outputs tab/Reports/Automatically discover reports/**Report
prefix**

## IncludePaths

(`action-name`/Outputs/AutoDiscoverReports/**IncludePaths**)

Or

(`action-name`/Outputs/Reports/`report-name-1`/**IncludePaths**)

(Required if [AutoDiscoverReports](#github.outputs.autodiscover "#github.outputs.autodiscover") is included and enabled, or if [Reports](#github.configuration.reports "#github.configuration.reports") is included)

Specify the files and file paths that CodeCatalyst includes when searching for raw reports. For
example, if you specify `"/test/report/*"`, CodeCatalyst searches the entire [build image](build-images.md "build-images.md") used by the action looking for the
`/test/report/*` directory. When it finds that directory, CodeCatalyst then looks
for reports in that directory.

###### Note

If your file path includes one or more asterisks (`*`) or other special
characters, enclose the path with double quotation marks (`""`). For more
information about special characters, see [Syntax guidelines and conventions](workflow-reference.md#workflow.terms.syntax.conv "workflow-reference.md#workflow.terms.syntax.conv").

If this property is omitted, the default is `"**/*"`, meaning the search
includes all files at all paths.

###### Note

For manually configured reports, `IncludePaths` must be a glob pattern
that matches a single file.

Corresponding UI:

- Outputs tab/Reports/Automatically discover reports/'Include/exclude
  paths'/**Include paths**
- Outputs tab/Reports/Manually configure
  reports/`report-name-1`/'Include/exclude
  paths'/**Include paths**

## ExcludePaths

(`action-name`/Outputs/AutoDiscoverReports/**ExcludePaths**)

Or

(`action-name`/Outputs/Reports/`report-name-1`/**ExcludePaths**)

(Optional)

Specify the files and file paths that CodeCatalyst excludes when searching for raw reports. For
example, if you specify `"/test/my-reports/**/*"`, CodeCatalyst will not search for
files in the `/test/my-reports/` directory. To ignore all files in a
directory, use the `**/*` glob pattern.

###### Note

If your file path includes one or more asterisks (`*`) or other special
characters, enclose the path with double quotation marks (`""`). For more
information about special characters, see [Syntax guidelines and conventions](workflow-reference.md#workflow.terms.syntax.conv "workflow-reference.md#workflow.terms.syntax.conv").

Corresponding UI:

- Outputs tab/Reports/Automatically discover reports/'Include/exclude
  paths'/**Exclude paths**
- Outputs tab/Reports/Manually configure
  reports/`report-name-1`/'Include/exclude
  paths'/**Exclude paths**

## SuccessCriteria

(`action-name`/Outputs/AutoDiscoverReports/**SuccessCriteria**)

Or

(`action-name`/Outputs/Reports/`report-name-1`/**SuccessCriteria**)

(Optional)

Specify the success criteria for the test, code coverage, software
composition analysis (SCA), and static analysis (SA) reports.

For more information, see [Configuring success criteria for reports](test-config-action.md#test.success-criteria "test-config-action.md#test.success-criteria").

Corresponding UI:

- Outputs tab/Reports/Automatically discover reports/**Success
  criteria**
- Outputs tab/Reports/Manually configure
  reports/`report-name-1`/**Success
  criteria**

## PassRate

(`action-name`/Outputs/AutoDiscoverReports/SuccessCriteria/**PassRate**)

Or

(`action-name`/Outputs/Reports/`report-name-1`/SuccessCriteria/**PassRate**)

(Optional)

Specify the percentage of tests in a test report that must pass for the associated CodeCatalyst
report to be marked as passed. Valid values include decimal numbers. For example: `50`,
`60.5`. The pass rate criteria are applied only to test reports. For more information about test reports, see [Test reports](test-workflow-actions.md#test-reports "test-workflow-actions.md#test-reports").

Corresponding UI:

- Outputs tab/Reports/Automatically discover reports/Success
  criteria/**Pass rate**
- Outputs tab/Reports/Manually configure
  reports/`report-name-1`/Success
  criteria/**Pass rate**

## LineCoverage

(`action-name`/Outputs/AutoDiscoverReports/SuccessCriteria/**LineCoverage**)

Or

(`action-name`/Outputs/Reports/`report-name-1`/SuccessCriteria/**LineCoverage**)

(Optional)

Specify the percentage of lines in a code coverage report that must be covered for the
associated CodeCatalyst report to be marked as passed. Valid values include decimal numbers. For
example: `50`, `60.5`. Line coverage criteria are applied only to code
coverage reports. For more information about code coverage reports, see [Code coverage reports](test-workflow-actions.md#test-code-coverage-reports "test-workflow-actions.md#test-code-coverage-reports").

Corresponding UI:

- Outputs tab/Reports/Automatically discover reports/Success
  criteria/**Line coverage**
- Outputs tab/Reports/Manually configure
  reports/`report-name-1`/Success
  criteria/**Line coverage**

## BranchCoverage

(`action-name`/Outputs/AutoDiscoverReports/SuccessCriteria/**BranchCoverage**)

Or

(`action-name`/Outputs/Reports/`report-name-1`/SuccessCriteria/**BranchCoverage**)

(Optional)

Specify the percentage of branches in a code coverage report that must be covered for the
associated CodeCatalyst report to be marked as passed. Valid values include decimal numbers. For
example: `50`, `60.5`. Branch coverage criteria are applied only to code
coverage reports. For more information about code coverage reports, see [Code coverage reports](test-workflow-actions.md#test-code-coverage-reports "test-workflow-actions.md#test-code-coverage-reports").

Corresponding UI:

- Outputs tab/Reports/Automatically discover reports/Success
  criteria/**Branch coverage**
- Outputs tab/Reports/Manually configure
  reports/`report-name-1`/Success
  criteria/**Branch coverage**

## Vulnerabilities

(`action-name`/Outputs/AutoDiscoverReports/SuccessCriteria/**Vulnerabilities**)

Or

(`action-name`/Outputs/Reports/`report-name-1`/SuccessCriteria/**Vulnerabilities**)

(Optional)

Specify the maximum number and severity of vulnerabilities permitted in the SCA
report for the associated CodeCatalyst report to be marked as passed. To specify vulnerabilities,
you must specify:

- The minimum severity of the vulnerabilities you want to include in the
  count. Valid values, from most to least severe, are: `CRITICAL`,
  `HIGH`, `MEDIUM`, `LOW`,
  `INFORMATIONAL`.

For example, if you choose `HIGH`, then `HIGH` and
`CRITICAL` vulnerabilities will be tallied.

- The maximum number of vulnerabilities of the specified severity you want
  permit. Exceeding this number causes the CodeCatalyst report to be marked as
  failed. Valid values are whole numbers.

Vulnerabilities criteria are applied only to SCA reports. For more information about SCA reports, see [Software composition analysis reports](test-workflow-actions.md#test-sca-reports "test-workflow-actions.md#test-sca-reports").

To specify the minimum severity, use the `Severity` property. To specify
the maximum number of vulnerabilities, use the `Number` property.

For more information about SCA reports, see [Quality report types](test-workflow-actions.md#test-reporting "test-workflow-actions.md#test-reporting").

Corresponding UI:

- Outputs tab/Reports/Automatically discover reports/Success
  criteria/**Vulnerabilities**
- Outputs tab/Reports/Manually configure
  reports/`report-name-1`/Success
  criteria/**Vulnerabilities**

## Reports

(`action-name`/Outputs/**Reports** )

(Optional)

A section that specifies the configuration for test reports.

Corresponding UI: Outputs tab/**Reports**

## report-name-1

(`action-name`/Outputs/Reports/**report-name-1** )

(Required if [Reports](#github.configuration.reports "#github.configuration.reports") is included)

The name you want to give to the CodeCatalyst report that will be generated from your raw
reports.

Corresponding UI: Outputs tab/Reports/Manually configure reports/**Report
name**

## Format

(`action-name`/Outputs/Reports/`report-name-1`/**Format**)

(Required if [Reports](#github.configuration.reports "#github.configuration.reports") is included)

Specify the file format that you're using for your reports. Possible values are as follows.

- For test reports:
  - For Cucumber JSON, specify **Cucumber** (visual editor) or `CUCUMBERJSON` (YAML editor).
  - For JUnit XML, specify **JUnit** (visual editor) or `JUNITXML` (YAML editor).
  - For NUnit XML, specify **NUnit** (visual editor) or `NUNITXML` (YAML editor).
  - For NUnit 3 XML, specify **NUnit3** (visual editor) or `NUNIT3XML` (YAML editor).
  - For Visual Studio TRX, specify **Visual Studio TRX** (visual editor) or `VISUALSTUDIOTRX` (YAML editor).
  - For TestNG XML, specify **TestNG** (visual editor) or `TESTNGXML` (YAML editor).

- For code coverage reports:
  - For Clover XML, specify **Clover** (visual editor) or `CLOVERXML` (YAML editor).
  - For Cobertura XML, specify **Cobertura** (visual editor) or `COBERTURAXML` (YAML editor).
  - For JaCoCo XML, specify **JaCoCo** (visual editor) or `JACOCOXML` (YAML editor).
  - For SimpleCov JSON generated by [simplecov](https://github.com/simplecov-ruby/simplecov "https://github.com/simplecov-ruby/simplecov"), not [simplecov-json](https://github.com/vicentllongo/simplecov-json "https://github.com/vicentllongo/simplecov-json"), specify **Simplecov** (visual editor) or `SIMPLECOV` (YAML editor).

- For software composition analysis (SCA) reports:
  - For SARIF, specify **SARIF** (visual editor) or `SARIFSCA` (YAML editor).

Corresponding UI: Outputs tab/Reports/Manually configure reports/Add report/`report-name-1`/**Report type**
and **Report format**

## Configuration

(`action-name`/**Configuration**)

(Required) A section where you can define the configuration properties of the action.

Corresponding UI: **Configuration** tab

## Steps

(`action-name`/Configuration/**Steps**)

(Required)

Specify your GitHub Action code as it appears on the action's details page in [GitHub Marketplace](https://github.com/marketplace "https://github.com/marketplace"). Add the code following these
guidelines:

1. Paste the code from the GitHub Action’s `steps:` section into the
   `Steps:` section of the CodeCatalyst workflow. The code starts with a dash (-) and
   looks similar to the following.

GitHub code to paste:

```
- name: Lint Code Base
  uses: github/super-linter@v4
  env:
    VALIDATE_ALL_CODEBASE: false
    DEFAULT_BRANCH: master
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

2. Review the code you just pasted and modify it as necessary so that it conforms to CodeCatalyst
   standards. For example, with the preceding code block, you might remove the code in
   `red italics`, and add the code in **bold**.

CodeCatalyst workflow yaml:

```
Steps:
   - name: Lint Code Base
     uses: github/super-linter@v4
     env:
       VALIDATE_ALL_CODEBASE: false
       DEFAULT_BRANCH: `master`**main**
       `GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}`
```

3. For additional code that’s included with the GitHub Action but does not exist inside the
   `steps:` section, add it to the CodeCatalyst workflow using CodeCatalyst-equivalent code.
   You can review the [Workflow YAML definition](workflow-reference.md "workflow-reference.md")
   to gain insight into how you might port your GitHub code to CodeCatalyst. Detailed migration steps
   are outside the scope of this guide.

Here is an example of how to specify file paths in a **GitHub Actions** action:

```
Steps:
  - name: Lint Code Base
    uses: github/super-linter@v4
    ...
  - run: cd /sources/WorkflowSource/MyFolder/  && cat file.txt
  - run: cd /artifacts/MyGitHubAction/MyArtifact/MyFolder/  && cat file2.txt
```

For more information about specifying file paths, see [Referencing source repository
files](workflows-sources-reference-files.md "workflows-sources-reference-files.md") and [Referencing files in an
artifact](workflows-working-artifacts-refer-files.md "workflows-working-artifacts-refer-files.md").

Corresponding UI: Configuration tab/**GitHub Actions YAML**
