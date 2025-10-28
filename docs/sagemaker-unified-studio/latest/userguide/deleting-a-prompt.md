# Delete an Amazon Bedrock prompt

You can delete prompts that you have previously created. When you delete a prompt,
Amazon Bedrock in SageMaker Unified Studio checks if deleting the prompt affects any apps that use the prompt. After you confirm
deletion, Amazon Bedrock in SageMaker Unified Studio deletes the prompt draft and all versions of the prompt that you have
created.

###### To delete a prompt

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. Choose the **Build** menu at the top of the page.
4. In the **MACHINE LEARNING & GENERATIVE AI** section, choose
   **My apps**.
5. In the **Select or create a new project to continue** dialog box, select the project that contains the prompt.
6. In the left pane, choose **Asset gallery** and then **My prompts**.
7. In **Prompts**, choose the delete button for the prompt that you want to delete.
8. In the **Delete** dialog box, check if deleting the prompt affects any of
   your apps. You can still delete the prompt, but you will need to make changes to the apps that
   use the prompt.
9. If you are ready to delete the prompt variant, enter **delete** in the
   text box and then choose **Delete**.
