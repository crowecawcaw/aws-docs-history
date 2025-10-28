# Share a code workflow with other project members in an Amazon SageMaker Unified Studio workflow environment

**For Git storage:** After a workflow environment has been created by a project owner, any project member can sync their
files to share them in the environment. After you sync your files, all project members can view the workflows you have added in the workflow
environment. Files that are not synced can only be viewed by the project member that created them.

**For S3 storage:** After a workflow environment has been created by a project owner, and once you’ve saved your
workflows workflows DAG files in JupyterLab, they are automatically synced to the project. After the files are synced, all project
members can view the workflows you have added in the workflow environment. Files that are not synced can only be viewed by the project
member that created them.

To share your workflows with other project members a workflow environment, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to a project that was created with the **Data analytics and AI-ML model development** project profile.
   You can do this by using the center menu at the top of the page and choosing **Browse all projects**, then choosing the name of the project that you want to navigate to.
3. In the **Build** menu, choose **JupyterLab**.
4. Locate the workflow you want to share in the `workflows/dags` folder.
5. Choose the **Git** icon in the left navigation.
6. Choose the **+** icon next to the files you want to commit.
7. Enter a brief summary of the commit in the **Summary** text entry field.
8. (Optional) Enter a longer description of the commit in the **Description** text entry field.
9. Choose **Commit**.
10. Choose the **Push committed changes** icon to do a git push.
11. In the **Build** menu, choose **Workflows**. This takes you to the Workflows page.
12. On the **Shared environment** tab, choose **Sync files from project**.
13. Choose **Confirm**.
