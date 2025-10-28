# Build an AI text summarizer app with Amazon Bedrock

In this tutorial, you will build an application in App Studio that uses Amazon Bedrock to provide
concise summaries of text input from end users. The application contains a simple user interface
where users can input any text they want summarized. This could be meeting notes, article content,
research findings, or any other textual information. After users enter the text, they can press a
button to send the text to Amazon Bedrock, which will process it using the Claude 3 Sonnet model and return
a summarized version.

###### Contents

- [Prerequisites](tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-prerequisites "tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-prerequisites")
- [Step 1: Create and configure an IAM role and App Studio connector](tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-create-role-connector "tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-create-role-connector")
- [Step 2: Create an application](tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-create-application "tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-create-application")
- [Step 3: Create and configure an automation](tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-create-automation "tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-create-automation")
- [Step 4: Create pages and components](tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-user-interface "tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-user-interface")
  - [Rename the default page](tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-user-interface-create-page "tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-user-interface-create-page")
  - [Add components to the page](tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-user-interface-add-components "tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-user-interface-add-components")
  - [Configure the page components](tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-user-interface-configure-components "tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-user-interface-configure-components")

- [Step 5: Publish the application to the Testing environment](tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-publish "tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-publish")
- [(Optional) Clean up](tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-cleanup "tutorial-conversational-bedrock.md#tutorial-conversational-bedrock-steps-cleanup")

## Prerequisites

Before you get started, review and complete the following prerequisites:

- Access to AWS App Studio. Note that you must have the Admin role to create a connector in this tutorial.
- Optional: Review [AWS App Studio concepts](concepts.md "concepts.md") and the
  [Tutorial: Start building from an empty
  app](getting-started-tutorial-empty.md "getting-started-tutorial-empty.md") to familiarize yourself with important App Studio concepts.

## Step 1: Create and configure an IAM role and App Studio connector

To provide App Studio access to Amazon Bedrock models, you must:

1. Enable the Amazon Bedrock models that you want to use in your app. For this tutorial, you will use **Claude 3 Sonnet**,
   so ensure you enable that model.
2. Create an IAM role with appropriate permissions to Amazon Bedrock.
3. Create an App Studio connector with the IAM role that will be used in your app.

Go to [Connect to Amazon Bedrock](connectors-bedrock.md "connectors-bedrock.md") for detailed
instructions, and return to this tutorial after you have followed the steps and created the
connector.

## Step 2: Create an application

Use the following procedure to create an empty app in App Studio that you will build into the text summarizer app.

1. Sign in to App Studio.
2. Navigate to the builder hub and choose **+ Create app**.
3. Choose **Start from scratch**.
4. In the **App name** field, provide a name for your app, such as `Text Summarizer`.
5. If you're asked to select data sources or a connector, choose **Skip** for
   the purposes of this tutorial.
6. Choose **Next** to proceed.
7. (Optional): Watch the video tutorial for a quick overview of building apps in App Studio.
8. Choose **Edit app**, which will bring you into the application studio.

## Step 3: Create and configure an automation

You define the logic and behavior of an App Studio app in _automations_.
Automations consist of individual steps known as _actions_,
_parameters_ that are used to pass data to the action from other resources,
and an _output_ that can be used by other automations or components. In this
step, you will create an automation that handles the interaction with Amazon Bedrock with the
following:

- Inputs: A parameter to pass the text input from the user to the automation.
- Actions: One **GenAI Prompt** action that sends the text input to Amazon Bedrock and returns the output text summary.
- Outputs: An automation output that consists of the processed summary from Amazon Bedrock, that can be used in your app.

###### To create and configure an automation that sends a prompt to Amazon Bedrock and processes and returns a summary

1. Choose the **Automations** tab at the top of the canvas.
2. Choose **+ Add automation**.
3. In the right-hand panel, choose **Properties**.
4. Update the automation name by choosing the pencil icon. Enter `InvokeBedrock` and press **Enter**.
5. Add a parameter to the automation that will be used to pass the text prompt input from the user into the automation to be
   used in the request to Amazon Bedrock by performing the following steps:
   1. In the canvas, in the parameters box, choose **+ Add**.
   2. In **Name**, enter `input`.
   3. In **Description**, enter any description, such as `Text to be sent to Amazon Bedrock`.
   4. In **Type**, select **String**.
   5. Choose **Add** to create the parameter.

6. Add a **GenAI Prompt** action by performing the following steps:
   1. In the right-hand panel, choose **Actions**.
   2. Choose **GenAI Prompt** to add an action.

7. Configure the action by performing the following steps:
   1. Choose the action from the canvas to open the right-hand **Properties** menu.
   2. Rename the action to `PromptBedrock` by choosing the pencil icon, entering the name, and pressing enter.
   3. In **Connector**, select the connector that was created in
      [Step 1: Create and configure an IAM role and App Studio connector](#tutorial-conversational-bedrock-steps-create-role-connector "#tutorial-conversational-bedrock-steps-create-role-connector").
   4. In **Model**, choose the Amazon Bedrock model you want to use to process the prompt. In this tutorial, you will choose
      **Claude 3.5 Sonnet**.
   5. In **User prompt**, enter `{{params.input}}`. This represents the `input` parameter that you created earlier, and
      will contain the text input by your app users.
   6. In **System prompt**, enter the system prompt instructions you want to send to Amazon Bedrock. For this tutorial, enter the following:

   ```
   You are a highly efficient text summarizer. Provide a concise summary of the prompted text, capturing the key points and main ideas.
   ```

   7. Choose **Request settings** to expand it, and update the following fields:
      - In **Temperature**, enter `0`. The tempearture determines the randomness or creativity of the output on a scale of 0 to 10. The higher the number,
        the more creative the response.
      - In **Max Tokens**, enter `4096` to limit the length of the response.

8. The output of this automation will be the summarized text, however, by default automations do not create outputs.
   Configure the automation to create an automation output by performing the following steps:
   1. In the left-hand navigation, choose the **InvokeBedrock** automation.
   2. In the right-hand **Properties** menu, in **Output**, choose **+ Add**.
   3. In **Output**, enter `{{results.PromptBedrock.text}}`.
      This expression returns the contents of the `processResults` action.

## Step 4: Create pages and components

In App Studio, each page represents a screen of your application's user interface (UI)
that your users will interact with. Within these pages, you can add various components such as tables,
forms, buttons, and more to create the desired layout and functionality.

### Rename the default page

The text summarizer app in this tutorial will only contain one page.
Newly created applications come with a default page, so you will rename that one instead of adding one.

###### To rename the default page

1. In the top bar navigation menu, choose **Pages**.
2. In the left-side panel, choose **Page1** and choose the
   **Properties** panel in the right-side panel.
3. Choose the pencil icon, enter `TextSummarizationTool`, and press
   **Enter**.
4. In **Navigation label** enter `TextSummarizationTool`.

### Add components to the page

For this tutorial, the text summarizer app has one page that contains the following components:

- A **Text input** component that end users use to input a prompt to be summarized.
- A **Button** component that is used to send the prompt to Amazon Bedrock.
- A **Text area** component that displays the summary from Amazon Bedrock.

Add a **Text input** component to the page that users will use to input a text prompt to be summarized.

###### To add a text input component

1. In the right-hand **Components** panel, locate the **Text input** component and
   drag it onto the canvas.
2. Choose the text input in the canvas to select it.
3. In the right-side **Properties** panel, update the following settings:
   1. Choose the pencil icon to rename the text input to `inputPrompt`.
   2. In **Label**, enter `Prompt`.
   3. In **Placeholder**, enter `Enter text to be summarized`.

Now, add a **Button** component that users will choose to send the prompt to Amazon Bedrock.

###### To add a button component

1. In the right-hand **Components** panel, locate the **Button** component and
   drag it onto the canvas.
2. Choose the button in the canvas to select it.
3. In the right-side **Properties** panel, update the following settings:
   1. Choose the pencil icon to rename the button to `sendButton`.
   2. In **Button Label**, enter `Send`.

Now, add a **Text area** component that will display the summary returned by Amazon Bedrock.

###### To add a text area component

1. In the right-hand **Components** panel, locate the **Text area** component and
   drag it onto the canvas.
2. Choose the text area in the canvas to select it.
3. In the right-side **Properties** panel, update the following settings:
   1. Choose the pencil icon to rename the button to `textSummary`.
   2. In **Label**, enter `Summary`.

### Configure the page components

Now that the app contains a page with components, the next step is to configure the components to carry out the appropriate
behavior. To configure a component, such as a button, to take actions when it is interacted with, you must add a
_trigger_ to it. For the app in this tutorial, you will add two triggers to the `sendButton`
button to do the following:

- The first trigger sends the text in the `textPrompt` component to Amazon Bedrock to be analyzed.
- The second trigger displays the returned summary from Amazon Bedrock in the `textSummary` component.

###### To add a trigger that sends the prompt to Amazon Bedrock

1. Choose the button in the canvas to select it.
2. In the right-side **Properties** panel, in the **Triggers** section, choose
   **+ Add**.
3. Choose **Invoke Automation**.
4. Choose the **InvokeAutomation1** trigger that was created to configure it.
5. In **Action Name**, enter `invokeBedrockAutomation`.
6. In **Invoke Automation**, select the **InvokeBedrock** automation that was created earlier.
7. In the parameters box, in the **input** parameter that was created earlier, enter `{{ui.inputPrompt.value}}`, which
   passes the content in the `inputPrompt` text input component.
8. Choose the left arrow at the top of the panel to return to the component properties menu.

Now, you've configured a trigger that invokes the automation to send a request to Amazon Bedrock when the button is clicked, the next step is to configure a second trigger
that displays the results in the `textSummary` component.

###### To add a trigger that displays the Amazon Bedrock results in the text area component

1. In the right-side **Properties** panel of the button, in the **Triggers** section, choose
   **+ Add**.
2. Choose **Run component action**.
3. Choose the **Runcomponentaction1** trigger that was created to configure it.
4. In **Action Name**, enter `setTextSummary`.
5. In **Component**, select the **textSummary** component.
6. In **Action**, select **Set value**.
7. In **Set value to**, enter `{{results.invokeBedrockAutomation}}`.

## Step 5: Publish the application to the **Testing** environment

Typically, while you are building an app, it's good practice to preview it to see how it looks and do initial testing on its functionality.
However, because applications don't interact with external services in
the preview environment, you'll instead publish the app to the Testing environment to be able to test sending requests and receiving responses from Amazon Bedrock.

###### To publish your app to the Testing environment

1. In the top-right corner of the app builder, choose **Publish**.
2. Add a version description for the Testing environment.
3. Review and select the checkbox regarding the SLA.
4. Choose **Start**. Publishing may take up to 15 minutes.
5. (Optional) When you're ready, you can give others access by choosing
   **Share** and following the prompts. For more information about sharing App Studio apps, see
   [Sharing published applications](application-share.md "application-share.md").

After testing your application, choose **Publish** again to promote the application to the Production environment. Note that apps in the Production
environment aren't available to end users until they are shared. For more information about the different
application environments, see
[Application environments](applications-publish.md#application-environments "applications-publish.md#application-environments").

## (Optional) Clean up

You have now successfully completed the tutorial and built a text summarization app in App Studio with Amazon Bedrock. You can continue to use your app, or you can
clean up the resources that were created in this tutorial. The following list contains a list of resources to be cleaned up:

- The Amazon Bedrock connector created in App Studio. For more information, see
  [Viewing, editing, and deleting connectors](viewing-deleting-connectors.md "viewing-deleting-connectors.md").
- The text summarizer app in App Studio. For more information, see [Deleting an application](applications-delete.md "applications-delete.md").
- The IAM role created in the IAM console. For more information, see
  [Delete roles or instance profiles](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in the _AWS Identity and Access Management User Guide_.
- If you requested model access to use Claude 3 Sonnet and want to revert access, see [Manage access to Amazon Bedrock
  foundation models](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md") in the _Amazon Bedrock User Guide_.
