# Export your Amazon Bedrock app

Use the following procedure to export a chat agent app or a flow app to a zip file. You can then
use the app outside of Amazon SageMaker Unified Studio.

###### To export a chat agent app or a flow app

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. If the project that you want to use isn't already open, do the following:
   1. Choose the current project at the top of the page. If a project isn't already open, choose **Select a project**.
   2. Select **Browse all projects**.
   3. In **Projects** select the project that you want
      to use.

4. Choose the **Build** menu option at the top of the page.
5. In **MACHINE LEARNING & GENERATIVE AI** choose **My apps**.
6. In **Apps** choose the app that you want to export.
7. If you haven't already, choose **Save** to save the app.
   You can't export an app unless you first save and run the app.
8. On the app page, choose **Export** to export the app.
   Amazon Bedrock in SageMaker Unified Studio will create and download a zip file with the name
   **amazon-bedrock-ide-app-export-\*.zip**.
9. Next step: [Deploy the app](app-deploy-app.md "app-deploy-app.md").
