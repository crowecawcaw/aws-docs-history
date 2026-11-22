

# Flows

Flows are multi-step workflows in AWS Quick that automate repetitive tasks without writing code. You describe a process in chat the way you explain it to a new teammate, and Quick builds the flow. You run and refine the flow through conversation, and then you share it.

You build and run flows on the web and in the desktop app, and both run in the cloud. From the mobile app and browser extensions, you can start a flow and follow its progress. You manage your flows from the **Flows** tab under **Customize**.

## When to use a flow
<a name="flows-when-to-use"></a>

Skills and flows both let an agent do more work for you, but they differ in who decides the steps. With a skill, the agent decides the steps as it works. With a flow, you set the steps in advance.

Use a skill when you know how the work should be done but the steps vary from run to run. For more information about skills, see [Teach agents with skills](working-with-skills.md). Use a flow when the steps are well-defined and you repeat them the same way each time.

Skills and flows work together. A flow can include agents that use skills, so you can combine fixed steps with steps that adapt to each run.

The following are common use cases for flows:
+ **Reporting** – Gather data from several sources, summarize it, and produce a report on a regular schedule.
+ **Customer support** – Triage incoming requests, draft responses, and route each request to the right team.
+ **Operations** – Run recurring tasks such as onboarding steps, data cleanup, or status checks.

## Flow definition
<a name="flows-definition"></a>

A flow is made up of inputs and outputs, steps, flow logic, and the capabilities that its steps can use.

### Inputs and outputs
<a name="flows-inputs-outputs"></a>

Inputs are the values a flow needs when it runs. Outputs are the results it produces. A flow can have up to 50 inputs and up to 50 outputs.

Each input has the following settings:
+ A name and a description.
+ A type: text, number, true/false, list, group, or file.
+ A required or optional setting.
+ A default value, which the flow uses when you don't provide one.

Each output has a name, a value, and a location where it appears after the flow runs.

### Step types
<a name="flows-step-types"></a>

A flow runs as a series of steps. There are two step types:
+ **Agent steps** – Use these steps for work that needs judgment. An agent reads the instructions you give it and decides how to complete the step.
+ **Deterministic steps** – Use these steps for exact work that runs the same way every time. Quick writes the code for the step, and the step has no direct internet access.

### Flow logic
<a name="flows-flow-logic"></a>

Flow logic controls the order in which steps run. You can use the following types of logic:
+ **Condition** – Runs a path only when a condition is true.
+ **Match** – Chooses one of several paths based on a value.
+ **Loop** – Repeats steps once for each item in a list.
+ **While** – Repeats steps for as long as a condition stays true.
+ **Parallel** – Runs several paths at the same time.

### Capabilities a flow can use
<a name="flows-capabilities"></a>

A flow and its steps can use the following capabilities:
+ **Agents** – For more information, see [Agents in AWS Quick](working-with-agents.md).
+ **Skills** – For more information, see [Teach agents with skills](working-with-skills.md).
+ **Connectors**, including cloud and local MCP connectors. For more information, see [Work with integrations in AWS Quick](working-with-integrations.md).
+ **System tools** – For more information, see [Built-in system tools](system-tools.md).
+ **Spaces and knowledge bases** – For more information, see [Organize, collaborate, and share resources with spaces in AWS Quick](working-with-spaces.md).
+ **Data** that you provide to the flow.
+ **Other flows** that the flow runs as a step.

## Running another flow
<a name="flows-running-another-flow"></a>

A flow can run another flow as one of its steps. When it does, it runs the latest published version of that flow. To add this step, describe it in chat and tell Quick which flow to run.

## Validations
<a name="flows-validations"></a>

A validation is a rule that an agent step's output must meet before the flow continues. You use validations to confirm that a step produced an acceptable result before the next step runs.

A validation has the following settings:
+ **Rules** – The conditions that the step's output must meet.
+ **Max retries** – The number of times the step runs again when the output fails a rule. The default is one.
+ **Continue if validations fail** – Controls whether the flow continues when the output still fails after the retries.

## Creating a flow
<a name="flows-creating"></a>

To create a flow, describe the process in chat. Quick builds the flow, you test and refine it, and then you publish it. Flow runs do not use memory, so each run starts fresh.<a name="flows-create-from-tab"></a>

**To create a flow from the Flows tab**

1. Choose **Customize**, and then choose **Flows**.

1. Choose **Create**.

1. Describe the process you want to automate in chat.

1. Review the flow that Quick builds, and refine it in chat.

1. Publish the flow when you are ready to run or share it.

**A test run takes real actions**  
A test run takes real actions, so review the steps before you run it.<a name="flows-create-from-chat"></a>

**To create a flow from chat**

1. In chat, describe the process you want to automate.

1. Review the flow that Quick builds, and refine it in chat.

1. Choose **Run** to test the flow.

1. Publish the flow when you are ready to run or share it.

## Flow design considerations
<a name="flows-design-considerations"></a>

Keep the following points in mind as you design a flow:
+ Steps run in order, so each step can use the results of the steps before it.
+ Each step has its own access to capabilities. A step can use only what you give it.
+ Some steps need your computer. Steps that use local files, browser automation, or local connectors run in the desktop app only, and only while the app is open and connected. If a routine starts the flow when the app isn't connected, the flow skips that run.

## Editing a flow
<a name="flows-editing"></a>

You can change any part of a flow in chat, and you can change some step settings on the flowchart. Only the owner can edit a flow. Your changes are saved to your draft until you publish them.<a name="flows-edit-in-chat"></a>

**To edit a flow in chat**

1. Open the flow that you want to edit.

1. In chat, describe the change you want to make.

1. Review the updated flow, and keep refining it in chat.

### Editing a step's settings
<a name="flows-edit-step-settings"></a>

The settings you can change depend on the step type:
+ **Agent steps** – Instructions, capabilities, and validations.
+ **Deterministic steps** – Capabilities. The code is read-only.
+ **Loop steps** – The list to loop over and the concurrency.
+ **Condition, Match, While, and Parallel steps** – The paths that the step controls.

### Choosing what a step can use
<a name="flows-choosing-capabilities"></a>

For each step, you choose what it can use:
+ **None** – The step uses no additional capabilities.
+ **All**, with **Let agent choose** – The agent picks from all available capabilities.
+ **Specific items** – The step uses only the capabilities you select.

Agent steps always include a set of core tools: code execution, file operations, date and time, transcription, image generation, and document-creation skills. Web search and browser automation are available only when you give them to the step.<a name="flows-change-step-capabilities"></a>

**To change the capabilities a step can use**

1. Open the flow, and then open the step you want to change.

1. For the step's capabilities, choose **None**, **All**, or **Specific items**.

1. If you chose **Specific items**, select the capabilities that the step can use.

1. Save your change to your draft.

### Adding validations
<a name="flows-adding-validations"></a><a name="flows-add-validation"></a>

**To add a validation**

1. Open the flow, and then open the agent step you want to validate.

1. Open the step's validations, and then add a rule that the output must meet.

1. For **Max retries**, enter the number of times the step runs again when the output fails.

1. Set **Continue if validations fail** based on whether you want the flow to continue when the output still fails.

1. Save your change to your draft.

### Undoing changes
<a name="flows-undoing-changes"></a>

Each change you make in chat shows an **Undo** option, so you can reverse a change right after you make it. Your draft also keeps a version history, so you can return to an earlier draft.

## Running and monitoring a flow
<a name="flows-running-monitoring"></a>

You can run a flow on demand or on a routine. A flow runs as the user who runs it, and it uses that user's access. When a step needs your approval, the run shows **Needs input** and pauses until you respond. If Smart Approvals is turned on, Quick can approve some actions for you based on your past choices.<a name="flows-run-from-page"></a>

**To run a flow from its page**

1. Open the flow that you want to run.

1. Provide any inputs that the flow needs.

1. Choose **Run**.

You can also run a flow by name in chat. Flow runs count toward your agent hours.

### Running a flow on a routine
<a name="flows-run-on-routine"></a>

You can run a flow automatically on a schedule by adding it to a routine. For more information about routines, see [Routines](working-with-routines.md). To manage running flows and routines in one place, see [Monitor and manage agents and flows with Mission Control](mission-control.md).

### Monitoring runs
<a name="flows-monitoring-runs"></a>

You monitor a flow's runs on the **Activity** tab of the flow and in Mission Control. The following table describes the status of a flow run.


| Status | Description | 
| --- | --- | 
| Running | The run is in progress. | 
| Needs input | The run is paused and waiting for your approval before it continues. | 
| Completed | The run finished with no issues. | 
| Failed | The run ended with an error. | 
| Canceled | Someone stopped the run before it finished. | 
| Skipped | The run didn't start because a required resource, such as a connected desktop app, wasn't available. | 

### When a run fails
<a name="flows-when-run-fails"></a>

When a run fails, it starts from the first step when you run it again. To fix the problem, open the failed step and ask Quick to fix it.

## Publishing a draft
<a name="flows-publishing"></a>

A flow has a draft version and a published (live) version. You must publish a flow before you can share it or run it on a routine. Only the owner can publish a flow, and every skill the flow uses must be published first.

**Publishing clears your draft**  
Publishing clears your draft and its version history. You can't restore an earlier published version, so test the flow before you publish it.<a name="flows-publish"></a>

**To publish a flow**

1. Open the flow that you want to publish.

1. Test the flow, and confirm that it works as you expect.

1. Choose **Publish**.

To continue working after you publish, choose **Copy to draft** to start a new draft from the published version. Choose **Delete draft** to discard a draft you no longer want. If your administrator requires approval, you request approval before the flow is published.

## Sharing a flow
<a name="flows-sharing"></a>

You must publish a flow before you can share it. When you share a flow, you give each person the **Viewer** or **Owner** role. Viewers can install and run the flow, and owners can also edit, publish, and share it.<a name="flows-share"></a>

**To share a flow**

1. Open the flow that you want to share, and confirm that it is published.

1. Choose **Share**.

1. Enter the people you want to share with, and choose a role for each person.

1. Choose **Share** to confirm.

## Approval for flows
<a name="flows-approval"></a>

Your administrator might require approval before you can share or publish a flow. You can have one pending request at a time. Approvers see requests in Mission Control. For more information, see [Monitor and manage agents and flows with Mission Control](mission-control.md).

## Adding a flow to a plugin
<a name="flows-add-to-plugin"></a>

You can bundle a flow with other capabilities in a plugin so that people install them together. For more information, see [Plugins](working-with-plugins.md).

## Browsing and installing a flow
<a name="flows-browsing-installing"></a>

You can find flows that other people share through **Browse all** or through Discover. For more information, see [Discover](working-with-discover.md).<a name="flows-install"></a>

**To install a flow**

1. Choose **Customize**, and then choose **Discover**.

1. Find the flow you want, using search or filters.

1. Choose the flow, and then choose **Install**.

1. If the flow needs a connector, select or create one, and then continue.

## Managing flows
<a name="flows-managing"></a>

The **Flows** tab under **Customize** lists the flows you own and the flows you installed. You can own up to 100 flows, and your account can have up to 10,000 flows.

A flow's page has the following tabs:
+ **Overview** – The flow's steps and details.
+ **Activity** – The flow's runs and their status.
+ **Routines** – The routines that run the flow.
+ **Capabilities** – The capabilities the flow uses.

The following table describes the actions you can take on a flow.


| Action | Description | 
| --- | --- | 
| Open | Opens the flow's page. | 
| Run | Runs the flow. | 
| Edit | Opens the flow so you can change it. | 
| Duplicate | Creates a copy of the flow. | 
| Publish | Publishes your draft as the live version. | 
| Copy to draft | Starts a new draft from the published version. | 
| Delete draft | Discards your current draft. | 
| Manage routines | Manages the routines that run the flow. | 
| Add to favorites | Adds the flow to your favorites. | 
| Copy link | Copies a link to the flow. | 
| Share | Shares the flow with other people. | 
| Export | Exports the flow's definition. | 
| Uninstall | Removes a flow that you installed. | 
| Delete | Deletes a flow that you own. | 

## Administrator controls
<a name="flows-admin-controls"></a>

Administrators use custom permissions to control how people work with flows. The **Flows** permission is the parent permission, and it includes **Share flows with individuals** and **Share flows with all**. For more information, see [Custom permissions](custom-permissions.md).

Administrators can also share a flow on behalf of a user, transfer ownership of a flow, and unlist a flow.

## Managing flows with the API
<a name="flows-api"></a>

You can manage flows programmatically with the API. The API works on published flows only. To get the definition format for a flow, use `DescribeFlow`. The API includes the following operations:
+ `CreateFlow`
+ `UpdateFlow`
+ `DescribeFlow`
+ `ListFlows`
+ `SearchFlows`
+ `DeleteFlow`
+ `GetFlowPermissions`
+ `UpdateFlowPermissions`
+ `GetFlowMetadata`