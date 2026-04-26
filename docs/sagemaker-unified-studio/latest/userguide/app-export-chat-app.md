# Export your Amazon Bedrock app

Use the following procedure to export a chat agent app or a flow app to a zip file. You can then
use the app outside of Amazon SageMaker Unified Studio.

###### To export a chat agent app or a flow app

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. From the project selector dropdown at the top of the page, choose the project that you want to use.
4. In the left navigation pane, under **Generative AI**, choose **AI apps**.
5. In **Apps** choose the app that you want to export.
6. If you haven't already, choose **Save** to save the app.
   You can't export an app unless you first save and run the app.
7. On the app page, choose **Export** to export the app.
   Amazon Bedrock in SageMaker Unified Studio will create and download a zip file with the name
   **amazon-bedrock-ide-app-export-\*.zip**.
8. Next step: [Deploy the app](app-deploy-app.md "app-deploy-app.md").
