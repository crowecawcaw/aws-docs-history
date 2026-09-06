

# Builds and deployments
<a name="acxd-builds-deployments"></a>

Builds and deployments are related but are not the same thing.

In agentic CX designer, a *build* packages the current version of your application into a deployable snapshot. A *deployment* makes a selected build available for use through a flow in Amazon Connect Customer.

## Builds
<a name="acxd-builds-deployments-builds"></a>

A build assembles the current application configuration into a package.

This includes:
+ Attached flows
+ Routing descriptions
+ Default behavior
+ Guardrails
+ Slots
+ Language settings
+ Application settings
+ Other configuration available at the time the build is created

Because a build captures the application at a specific moment, edits made after the build are not included in a deployment until you create another build.

Builds are required before application changes can be tested or released through the application experience.

A build is especially important when you change anything that affects how the application understands, routes, or responds to users.

At least one build is also needed for test chats to work when testing from a Canvas flow or on the application's Test tab.

From your application's **Builds** tab, you can create a new build, review build history, deploy a build or roll back to a previous build.

**To create or manage builds**

1. Open **Applications**.

1. Select the application you want to build.

1. Open the **Builds** tab.

1. Choose whether the build is for a development or production environment.

1. Select **Create build** to start the build process.

When you start a build, agentic CX designer walks you through the build process:

1. Review warnings such as disconnected flow paths, incomplete configurations, etc. Critical errors appear in red and should be resolved before creating the build, as they are more likely to cause a failed build. Warnings appear in yellow and should also be reviewed, so you understand the possible impact on the user experience.

1. Add a build description as a simple changelog.

1. Select **Create build**.

When the build completes, it appears in the builds table. From there, you can review the build version, description, status, and environment usage.

For failed builds, select the build from the table to review the full failure message.

Create a new build whenever you want to test or release meaningful application changes.

Examples:
+ You added or removed a flow from the application.
+ You updated the application's default flows.
+ You changed custom slot configuration or values.
+ You updated routing descriptions.
+ You added languages or translations.
+ You changed guardrails.

You can create builds as often as needed while developing. Creating a build does not automatically push changes to an external environment unless you continue through deployment or promotion.

After a build is created, you may use the test chat from a flow's Canvas or use the **Test** tab on the application.

## Deployments
<a name="acxd-builds-deployments-deploy"></a>

Once you are satisfied with testing in your agentic CX designer workspace, you can deploy your application for use in a flow in Amazon Connect Customer.

From the application's **Builds** tab, use the builds table to manage which build becomes active. Only one build can be active in an environment at a time.

**To deploy a build**

1. Open an application and select the **Builds** tab.

1. From the builds table, hover over the selected build's status.

1. Choose **Deploy**.

A deployment may take a few minutes. A successful deployment is indicated by a **Deployed** status.

After deployment, review the application's **Access** details in the application settings. Your frontend or implementation team may need connection values such as the application URL and API key when configuring the application for the intended frontend experience.

You can also return to a previous build version by hovering over a past build and choosing **Roll back**.

Select a build from the builds table to review additional details, such as the build ID, deployment key, and deployment management options. If needed, you can delete a deployment to take the application offline until another build is deployed.

## Connecting to Amazon Connect Customer
<a name="acxd-builds-deployments-connect"></a>

After your agentic CX designer application has been deployed for the first time, configure Amazon Connect Customer to route conversations through it.

### Create or choose a contact flow
<a name="acxd-builds-deployments-connect-flow"></a>

In Connect Customer, create or choose the contact flow that will route incoming calls or chats to your agentic CX designer application.

This contact flow should include the routing logic needed to connect the customer entry point to your deployed application.

### Choose a voice persona
<a name="acxd-builds-deployments-connect-voice"></a>

For voice-enabled conversations, use a **Set voice** block in the Connect Customer flow.

**To configure voice**

1. Add a **Set voice** block.

1. Select the block.

1. Choose the voice provider.

1. Choose the language and voice persona.

1. Listen to available samples, if needed.

1. Confirm the selection.

### Add the Agentic CX block
<a name="acxd-builds-deployments-connect-block"></a>

After your routing and voice setup is in place, add an **Agentic CX** block to the contact flow.

Configure the block by selecting:

1. The workspace where your application lives.

1. The name of the agentic CX designer application.

1. The deployed environment alias, such as `Development` or `Production`.

1. Any required block pathways, including escalation, error, or timeout handling.

The block tells Connect Customer which agentic CX designer application and environment to invoke during the conversation.

Depending on whether the contact is voice or chat, you may also configure additional settings on the **Agentic CX** block.

#### Speech recognition
<a name="acxd-builds-deployments-connect-speech"></a>

For voice interactions, configure **Speech recognition**. This setting determines which engine transcribes the customer's voice input before it is processed by the agentic CX designer application.

You can set speech recognition in two ways:


| Setting | Use when | 
| --- | --- | 
| Set manually | The flow should always use the same speech recognition engine. | 
| Set dynamically | The flow should choose the speech recognition engine based on contact flow logic, contact attributes, language, region, or another available value. | 

#### Audio filler
<a name="acxd-builds-deployments-connect-audio"></a>

For voice interactions, you can enable **Audio filler**. This can make voice conversations feel more natural when the application needs a moment to generate an output, retrieve or send data, or complete a tool call.

#### Idle chat timeout
<a name="acxd-builds-deployments-connect-idle"></a>

For chat interactions, you can enable **Idle chat timeout**. This setting controls how long a chat contact can remain inactive before it is considered idle.

Use idle timeout when you want to handle abandoned or inactive chats consistently. For example, after a period of inactivity, the Connect Customer flow exits the **Agentic CX** block from the **Idle timeout** edge, where the conversation can provide a final message before ending the session.

When using timeout behavior, make sure all timeout paths from the **Agentic CX** block are connected to the appropriate next step in the Connect Customer flow.

### Publish the contact flow
<a name="acxd-builds-deployments-connect-publish"></a>

Publish the Connect Customer flow to make it active and available for use with the appropriate phone numbers or chat endpoints.

Once the contact flow has been published, you do not need to republish it every time you update the agentic CX designer application. The **Agentic CX** block continues to point to the selected application and environment. Any newly deployed build for that environment becomes the version used in live conversations.

If you change the contact flow itself, or any configuration on the **Agentic CX** block, publish the contact flow again.