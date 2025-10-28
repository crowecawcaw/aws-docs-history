# Create an Amazon Bedrock function component

You can create a function as a component in an Amazon Bedrock in SageMaker Unified Studio project. If you are creating an
app, you can can also create a function when you configure the app.

###### To create a function component

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. Choose the **Build** menu at the top of the page.
4. In the **MACHINE LEARNING & GENERATIVE AI** section, choose
   **My apps**.
5. In the **Select or create a new project to continue** dialog box, select the project that you want to use.
6. In the left pane, choose **Asset gallery**.
7. Choose **My components**.
8. In **Asset gallery**, choose **My components**.
9. In the **Components** section, choose **Create
   component** and then **Function**. The **Create
   function** pane is shown.
10. For **Function name**, enter a name for the function in in **Function name**.
11. For **Function description**, enter a description for the function.
12. For **Function schema**, enter the JSON or YAML format OpenAPI schema
    for the API. Alternatively, upload the JSON or YAML for the file by choosing
    **Import JSON/YAML**. You can clear the text box by choosing
    **Reset**.
13. Choose **Validate schema** to validate the schema.
14. For **Authentication method** select the authentication method for
    your API server. By default, Amazon Bedrock in SageMaker Unified Studio preselects the authentication based on
    information it finds in your OpenAPI schema. For information about authentication methods,
    see [Authentication methods](functions.md#functions-authentication "functions.md#functions-authentication").
15. Enter the information for the authention method that you selected in the previous
    step.
16. For **API servers**, enter the URL for your server in **Server
    URL**. This value is autopopulated if the server URL is in the schema.
17. Choose **Create** to create your function.
18. Add your function to a chat agent app by doing [Add a function component to an Amazon Bedrock chat agent app](add-function-component-chat-app.md "add-function-component-chat-app.md").
