

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Workflows concepts
<a name="workflows-concepts"></a>

Here are some concepts and terms to know when building, testing, or deploying your code with workflows in CodeCatalyst.

## Workflows
<a name="workflows-concepts-workflows"></a>

A *workflow* is an automated procedure that describes how to build, test, and deploy your code as part of a continuous integration and continuous delivery (CI/CD) system. A workflow defines a series of steps, or *actions*, to take during a workflow run. A workflow also defines the events, or *triggers*, that cause the workflow to start. To set up a workflow, you create a *workflow definition file* using the CodeCatalyst console's [visual or YAML editor](https://docs.aws.amazon.com/codecatalyst/latest/userguide/flows.html#workflow.editors).

**Tip**  
For a quick look at how you might use workflows in a project, [create a project with a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-create.html#projects-create-console-template). Each blueprint deploys a functioning workflow that you can review, run, and experiment with.

## Workflow definition files
<a name="workflows-concepts-workflows-def"></a>

A *workflow definition file* is a YAML file that describes your workflow. By default, the file is stored in a `~/.codecatalyst/workflows/` folder in the root of your [source repository](source-repositories.md). The file can have a .yml or .yaml extension, and the extension must be lowercase.

For more information about the workflow definition file, see [Workflow YAML definition](workflow-reference.md).

## Actions
<a name="workflows-concepts-actions"></a>

An *action* is the main building block of a workflow, and defines a logical unit of work, or task, to perform during a workflow run. Typically, a workflow includes multiple actions that run sequentially or in parallel depending on how you've configured them.

For more information about actions, see [Configuring workflow actions](workflows-actions.md).

## Action groups
<a name="workflows-concepts-action-groups"></a>

An *action group* contains one or more actions. Grouping actions into action groups helps you keep your workflow organized, and also allows you to configure dependencies between different groups.

For more information about action groups, see [Grouping actions into action groups](workflows-group-actions.md).

## Artifacts
<a name="workflows-concepts-artifacts"></a>

An *artifact* is the output of a workflow action, and typically consists of a folder or archive of files. Artifacts are important because they allow you to share files and information between actions.

For more information about artifacts, see [Sharing artifacts and files between actions](workflows-working-artifacts.md).

## Compute
<a name="workflows-concepts-compute"></a>

*Compute* refers to the computing engine (the CPU, memory, and operating system) managed and maintained by CodeCatalyst to run workflow actions.

For more information about compute, see [Configuring compute and runtime images](workflows-working-compute.md).

## Environments
<a name="workflows-concepts-environments"></a>

A CodeCatalyst *environment*, not to be confused with a [Dev Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html), defines the target AWS account and optional Amazon VPC that a CodeCatalyst [workflow](workflow.md) connects to. An environment also defines the [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a workflow needs to access the AWS services and resources within the target account.

You can set up multiple environments and give them names such as development, test, staging, and production. When you deploy into these environments, information about the deployments appears on the CodeCatalyst **Deployment activity** and **Deployment targets** tabs in the environment.

For more information about environments, see [Deploying into AWS accounts and VPCs](deploy-environments.md).

## Gates
<a name="workflows-concepts-gates"></a>

A *gate* is a workflow component that you can use to prevent a workflow run from proceeding unless certain conditions are met. An example of a gate is the **Approval** gate where users must submit an approval in the CodeCatalyst console before the workflow run is allowed to continue.

You can add gates between sequences of actions in a workflow, or before the first action (which runs immediately after the **Source** downloads). You can also add gates after the last action, if you have a need to do so.

For more information about gates, see [Gating a workflow run](workflows-gates.md).

## Reports
<a name="workflows-concepts-test-reports"></a>

A *report* contains details about tests that occur during a workflow run. You can create reports such as a test report, a code coverage report, a software composition analysis report, and a static analysis report. You can use a report to help troubleshoot a problem during a workflow. If you have many reports from multiple workflows, you can use your reports to view trends and failure rates to help you optimize your applications and deployment configurations.

For more information about reports, see [Quality report types](test-workflow-actions.md#test-reporting).

## Runs
<a name="workflows-concepts-runs"></a>

A *run* is a single iteration of a workflow. During a run, CodeCatalyst performs the actions defined in the workflow configuration file and outputs the associated logs, artifacts, and variables.

For more information about runs, see [Running a workflow](workflows-working-runs.md).

## Sources
<a name="workflows-concepts-sources"></a>

A *source*, also called an *input source*, is a source repository to which a [workflow action](workflows-actions.md) connects in order to obtain the files it needs to carry out its operations. For example, a workflow action might connect to a source repository to obtain application source files in order to build an application.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md).

## Variables
<a name="workflows-concepts-variables"></a>

 A *variable* is a key-value pair that contains information that you can reference in your Amazon CodeCatalyst workflow. The value portion of the variable is replaced with an actual value when the workflow runs.

For more information about variables, see [Using variables in workflows](workflows-working-with-variables.md).

## Workflow triggers
<a name="workflows-concepts-triggers"></a>

A *workflow trigger*, or simply a *trigger*, allows you to start a workflow run automatically when certain events occur, like a code push. You might want to configure triggers to free your software developers from having to start workflow runs manually through the CodeCatalyst console.

You can use three types of trigger:
+ **Push** – A code push trigger causes a workflow run to start whenever a commit is pushed.
+ **Pull request** – A pull request trigger causes a workflow run to start whenever a pull request is either created, revised, or closed.
+ **Schedule** – A schedule trigger causes a workflow run to start on a schedule that you define. Consider using a schedule trigger to run nightly builds of your software so that the latest build is ready for your software developers to work on the next morning.

You can use push, pull request, and schedule triggers alone or in combination in the same workflow.

Triggers are optional—if you don't configure any, you can only start a workflow manually.

For more information about triggers, see [Starting a workflow run automatically using triggers](workflows-add-trigger.md).