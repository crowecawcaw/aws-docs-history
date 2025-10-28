# Share an Amazon Bedrock prompt version

You can share versions of prompts that you have previously created. You can share a prompt version with all
members of your Amazon SageMaker Unified Studio domain, or with specific users or groups in your
Amazon SageMaker Unified Studio domain.

When you first share a prompt version, you get a share link to the prompt version that you can send to
users. If you share the prompt version with all users, Amazon SageMaker Unified Studio grants permission to a user,
when they first open the share link. Amazon SageMaker Unified Studio also adds the prompt version to the user's shared
assets list. If you share the prompt version with specific users and groups, the prompt version is immediately
available in their shared assets list. They can also use the share link to access the prompt. By
default, sharing a prompt version is restricted to only those users or groups that you select.

If you need the share link again after sharing the prompt version, get the share link by
choosing to share prompt version again and copying the share link. You can also change the users
that you share with the prompt version with.

To see which prompt versions you have shared, Open the project, choose **Asset
gallery** and then **My prompts**. Check the **Share
status** column for the prompt.

###### To share a prompt version

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. Choose the **Build** menu at the top of the page.
4. In the **MACHINE LEARNING & GENERATIVE AI** section, choose
   **My apps**.
5. In the **Select or create a new project to continue** dialog box, select the project that contains the prompt.
6. In the left pane, choose **Asset gallery** and then **My prompts**.
7. In **Prompts**, select the prompt that you want to share.
8. If you haven't previously created a version of your prompt, choose **Create version** to create a version of your prompt.
9. Choose the menu option, and choose choose **Share prompt version** to open the prompt sharing pane.
10. In **Version to publish**, select the version of the prompt that you want to share
11. Do one of the following:
    - If you want to share the prompt version with all members of your Amazon SageMaker Unified Studio domain,
      turn on **Grant access with link**.
    - If you want to share the prompt version with specific Amazon SageMaker Unified Studio domain
      users or groups, do the following in **Share with specific users or groups**:
      1. For **Member type** choose **Individual
         user** or **Group**, depending on the
         type of member that you want share the app with.
      2. Search for the users or groups that you want to share the app with
         by entering the user name or group in the **Search by alias
         to invite members** text box.
      3. In the drop down list, select the matching user name or
         group that want to share the app with.
      4. Choose **Add** to add the user or group.

12. Choose **Share** to share the prompt.
13. When the success message appears, choose **Copy link** and send the link
    to the users that you are sharing the prompt version with. If **Grant access with link** is off,
    the link only works for users that you have explicitly granted access to the prompt.
