# Use app history to view and restore versions of an Amazon Bedrock app

As you develop an Amazon Bedrock in SageMaker Unified Studio app (chat agent app or flow app), you make changes
and improvements. When you save an app, Amazon Bedrock in SageMaker Unified Studio saves the current draft of the app
(including its configuration information), as a version in the _app
history_. At some point, you might want to view and restore a previous version
of an app. For example, you might want to check the guardrail that a previous version of a
chat agent app uses, or you might want continue development starting from a previous
version of the app. You can use the app history to view and restore previous app
versions.

Within the app history, you can restore a previous version of the app. If you don't save
the current draft before restoring a previous version, Amazon Bedrock in SageMaker Unified Studio automatically saves
the draft for you. While you are viewing the app history for an app, you can't make changes to the app.

###### To view or restore a previous version of an app

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. If the project that you want to use isn't already open, do the following:
   1. Choose the current project at the top of the page. If a project isn't already open, choose **Select a project**.
   2. Select **Browse all projects**.
   3. In **Projects** select the project that you want
      to use.

4. Choose the **Build** menu option at the top of the page.
5. In **MACHINE LEARNING & GENERATIVE AI** choose **My apps**.
6. In **Apps** choose the app that you want to use.
7. On the **Save** button, choose the menu selector and then select
   **View history**.
8. In the **History pane**, select the version of the app that you
   want to view. The center pane refreshes to contain the selected app version.
9. In the center pane, view the app version and its configuration. You can't make
   changes to app. To return to the editable draft, choose **Close App
   history**.
10. (Optional) In the **App history** pane, choose
    **Restore** to restore the app version. After restoring the
    app, Amazon Bedrock in SageMaker Unified Studio closes the app history pane and you can edit the restored app
    version.

If you don't save the current draft before restoring a previous version,
Amazon Bedrock in SageMaker Unified Studio automatically saves the draft for you.
