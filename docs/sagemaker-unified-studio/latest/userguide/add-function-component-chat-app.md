# Add a function component to an Amazon Bedrock chat agent app

In this procedure, you add a function component to an existing [chat agent app](create-chat-app.md "create-chat-app.md"). You can add up to 5 functions to an app.
For each function you add, be sure to update the system instruction with information about the
function.

###### To add a function component to a chat agent app

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. If the project that you want to use isn't already open, do the following:
   1. Choose the current project at the top of the page. If a project isn't already open, choose **Select a project**.
   2. Select **Browse all projects**.
   3. In **Projects** select the project that you want
      to use.

4. Choose the **Build** menu option at the top of the page.
5. In **MACHINE LEARNING & GENERATIVE AI** choose **My apps**.
6. In **Apps** choose the chat agent app that you want to add the
   function component to.
7. In the **Configs** pane, do the following:
   1. For **Enter a system instruction**, enter or update the system
      prompt so that it describes the function.
   2. Choose **Functions**.
   3. For **Functions**, select the function component that you created
      in [Create an Amazon Bedrock function component](creating-a-function-component.md "creating-a-function-component.md").

8. Choose **Save** to save your changes.
