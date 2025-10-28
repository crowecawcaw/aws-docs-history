# Modify the version of an Amazon Bedrock chat agent app

You can change the version of a chat agent app that an agent node in a flow app
uses, or the version of a chat agent app that is shared with other users. To change
the version, you modify the alias for the chat agent app to reference the new version.
After updating the alias, you don't need to update the flow app or shares of
the chat agent app for them to use the new version.

The following procedure shows you how to change the version of a chat agent app that
an alias for the app references.

###### To modify the version that an alias references

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. If the project that you want to use isn't already open, do the following:
   1. Choose the current project at the top of the page. If a project isn't already open, choose **Select a project**.
   2. Select **Browse all projects**.
   3. In **Projects** select the project that you want
      to use.

4. Choose the **Build** menu option at the top of the page.
5. In **MACHINE LEARNING & GENERATIVE AI** choose **My apps**.
6. Open the app that you want to use.
7. Choose the selector on the **Deploy** button and select
   **View aliases**. The **View and manage
   aliases** pane opens.
8. For the alias that you want modify, choose **Edit**.
9. In the **Edit alias** pane, select the version that you want
   the alias to use in **Select version to associate with this
   alias**.
10. (Optional) Update the name and description for the alias.
11. Choose **Save** to save your changes.
