# Get started using

Amazon Bedrock in SageMaker Unified Studio

Amazon Bedrock in SageMaker Unified Studio offers multiple playgrounds that allow you to easily access and experiment with Amazon Bedrock models. With the
[chat](../../../sagemaker-unified-studio/latest/userguide/bedrock-explore-chat-playground.md "../../../sagemaker-unified-studio/latest/userguide/bedrock-explore-chat-playground.md") playground, you can chat
with a model through text and image prompts. With the [image and video](../../../sagemaker-unified-studio/latest/userguide/explore-image-playground.md "../../../sagemaker-unified-studio/latest/userguide/explore-image-playground.md") playground, you can use a compatible model to generate and edit images and videos.

In addition to the playgrounds, you can also use Amazon Bedrock in SageMaker Unified Studio to create [chat agent apps](../../../sagemaker-unified-studio/latest/userguide/create-chat-app.md "../../../sagemaker-unified-studio/latest/userguide/create-chat-app.md") and
[flows apps](../../../sagemaker-unified-studio/latest/userguide/create-flows-app.md "../../../sagemaker-unified-studio/latest/userguide/create-flows-app.md"). A chat agent app allows users to create a custom app that interacts with a Amazon Bedrock model through a conversational interface. You can enhance chat agent apps with Amazon Bedrock features such as data sources and guardrails and share the app with other users. A flows app allows users to link together prompts, foundation models, and other components to create a visual, end-to-end generative AI workflow.

The following section will walk you through the basic functionalities of Amazon Bedrock in SageMaker Unified Studio. First, you will select a model from the model catalog and chat with it in the chat playground. Then, you will create a chat agent app that can create playlists for a rock and pop radio station.
For more in-depth information on other Amazon Bedrock features you can use with Amazon Bedrock in SageMaker Unified Studio, see [Amazon Bedrock in SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/userguide/bedrock.md "../../../sagemaker-unified-studio/latest/userguide/bedrock.md").

## Step 1: Explore Amazon Bedrock foundation models

The following section shows how to select a model from the model catalog in the Amazon Bedrock in SageMaker Unified Studio
playground. You can also access the model catalog from inside your projects. The models you have access to in your projects might be different from those you can access in the playground, based on your administrator's settings. To check which models you can
access in a project, open or create a project, and then select **Models**
in the navigation pane to open the model catalog.

###### To open the model catalog in the playground

1. Navigate to the Amazon SageMaker landing page by using the URL from your admininstrator.
2. Access Amazon SageMaker using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/userguide/getting-started-access-the-portal.md "../../../sagemaker-unified-studio/latest/userguide/getting-started-access-the-portal.md").
3. At the top of the page, choose **Discover**.
4. Under **Data and model catalog**, choose **Amazon Bedrock
   models**. This opens the model catalog in the Amazon Bedrock in SageMaker Unified Studio playground.
5. (Optional) Choose **Group by: Modality** and select
   **Provider** to sort the list by model provider.
6. Choose a model from the list of models that you have access to. For information about a model, choose **View full model details** in the information panel. If you
   don't have access to an appropriate model, contact your administrator. Some features may not be supported by all models.

If you are ready to begin chatting with the model you chose, proceed to the following step.

## Step 2: Chat with a model in the chat playground

In this section you will chat with your selected model in the chat playground. You
chat by sending a prompt to the model and receiving a response. For more information, see [Experiment with the Amazon Bedrock playgrounds](../../../sagemaker-unified-studio/latest/userguide/bedrock-playgrounds.md "../../../sagemaker-unified-studio/latest/userguide/bedrock-playgrounds.md").

###### Warning

Generative AI may give inaccurate responses. Avoid sharing sensitive information.
Chats may be visible to others in your organization.

###### To chat with a model

1. In the chat playground, enter `What is Avebury stone circle?` in the **Enter prompt** text box.
2. (Optional) If the model you chose is a reasoning model, you can choose
   **Reason** to have the model include its reasoning in the reponse.
   For more information, see [Enhance model responses with
   model reasoning](../../../bedrock/latest/userguide/inference-reasoning.md "../../../bedrock/latest/userguide/inference-reasoning.md") in the _Amazon Bedrock user guide_.
3. Press Enter on your keyboard, or choose the run button, to send the prompt to the
   model. The response from the model will be generated in the playground.
4. Continue chatting with the model by entering the prompt `Is there a museum
there?`.

The model will use the previous prompt as context for generating its response to this question. 5. (Optional) Compare the output from multiple models, or [shared apps](../../../sagemaker-unified-studio/latest/userguide/bedrock-explore-chat-playground-app.md "../../../sagemaker-unified-studio/latest/userguide/bedrock-explore-chat-playground-app.md").

    1. In the playground, turn on **Compare mode**. This will open two panes side-by-side.
    2. In each panes, select a model that you want to compare. If you want to use a
     shared app, select **App** in **Type** and
     then select the app in **App**.
    3. Enter a prompt in the text box and run the prompt. The output from each model is shown in their respective panes. You
     can choose the copy icon to copy the prompt or model response to the clipboard.
    4. (Optional) Choose **Add chat window** to add a third window.
     You can compare up to 3 models or apps.
    5. Turn off **Compare mode** to stop comparing models.

6. Choose **Reset** to start a new chat with the model.

## Step 3: Create a chat agent app

In this section you will learn how to create a simple Amazon Bedrock in SageMaker Unified Studio chat agent app that
creates playlists for a radio station and shares the dates and locations of upcoming shows.

###### To create an Amazon Bedrock chat agent app

1. On the Amazon SageMaker home page, choose **Build chat agent app** to create a new
   chat agent app. The **Select or create a new project to
   continue** dialog box opens.
2. In the **Select or create a new project to continue** dialog box, do one of the following:
   - If you want to use a new project, follow the instructions at
     [Step 2 - Create a new project](setting-up.md#create-new-project "setting-up.md#create-new-project"). For the **Project profile** in step 1, choose
     **Generative AI application development**.
   - If you want to use an existing project, select the project that you
     want to use and then choose **Continue**.

3. On the app creation page, an untitled app will automatically be created for you. In **Untitled App - nnnn**, enter `Radio
show` as the name for your app.
4. In the **Configs** pane, do the following:
   1. For **Model**, select a model that supports
      Guardrails, Data, and Function components. The description of the
      model tells you the components that a model supports. For full
      information about the model, choose **View full model
      details** in the information panel. For more information,
      see [Find serverless models with the model catalog](../../../sagemaker-unified-studio/latest/userguide/model-catalog.md "../../../sagemaker-unified-studio/latest/userguide/model-catalog.md").
      If you don't have
      access to an appropriate model, contact your administrator.
      Different models might not support all features.
   2. For **Enter a system instruction** in **Instructions for chat agent
      & examples**, enter `You are a
chat agent app that creates 2 hour long playlists for a radio
station that plays rock and pop music.`.
   3. In the **UI** section, update the user interface for the app by doing the following:
      1. In **Hint text for empty chat** enter `Hi!
I'm your radio show playlist creator.`.
      2. In **Hint text for user input** enter
         `Enter a prompt that describes the playlist that you want.`.
      3. In **Quick start prompts** choose
         **Edit**.
      4. Choose **Reset** to clear the list of quick start
         prompts
      5. For **Quick-start prompt 1**, enter `Create a
playlist of pop music songs.`.
      6. (Optional). Enter quick start prompts of your choice in the remaining quick start prompt text boxes.
      7. Choose **Back to configs**.

5. Choose **Save** to save the current working draft of your app.
6. In the **Quick start prompts** section of the
   **Preview** pane, run the quick start prompt that you just
   created by choosing the prompt.

The app shows the prompt and the response from the model in the
**Preview** pane. 7. In the prompt text box (the text should read **Enter a prompt that describes the playlist that you
want**), enter
`Create a playlist of songs where each song on the list is related to
 the next song, by musician, bands, or other connections. Be sure to explain
 the connection from one song to the next.` . 8. Choose the run button (or press Enter on your keyboard) to send the prompt to the model.

You have now created a basic chat agent app that can create playlists for a rock and pop radio station.
You can experiment with sending prompts and receiving responses from your chat agent app.

## Additional capabilities

Amazon Bedrock in SageMaker Unified Studio offers many additional capabilities to the ones covered in this walkthrough, including the following.

- You can customize and influence model behavior using inference parameters and system prompts. For more information, see [What is a prompt?](../../../sagemaker-unified-studio/latest/userguide/explore-prompts.md "../../../sagemaker-unified-studio/latest/userguide/explore-prompts.md").
- You can enhance your chat agent app by adding data sources and guardrails. For more information, see [Build a chat agent app](../../../sagemaker-unified-studio/latest/userguide/create-chat-app.md "../../../sagemaker-unified-studio/latest/userguide/create-chat-app.md").
- You can share your chat agent app with other users and use it as a component in a flows app. For more information, see [Share a chat agent app](../../../sagemaker-unified-studio/latest/userguide/app-share.md "../../../sagemaker-unified-studio/latest/userguide/app-share.md") and [Deploy a chat agent app](../../../sagemaker-unified-studio/latest/userguide/app-deploy.md "../../../sagemaker-unified-studio/latest/userguide/app-deploy.md").
- You can create a flows app to link together different components such as knowledge bases and reusable prompts. For more information, see [Build a flow app](../../../sagemaker-unified-studio/latest/userguide/create-flows-app.md "../../../sagemaker-unified-studio/latest/userguide/create-flows-app.md").
