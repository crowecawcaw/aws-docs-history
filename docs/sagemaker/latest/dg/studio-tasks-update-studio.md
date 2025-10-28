# Shut Down and Update Amazon SageMaker Studio Classic

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

To update Amazon SageMaker Studio Classic to the latest release, you must shut down the
JupyterServer app. You can shut down the JupyterServer app from the SageMaker AI console, from
Amazon SageMaker Studio or from within Studio Classic. After the JupyterServer app is shut down, you
must reopen Studio Classic through the SageMaker AI console or from Studio which creates a new
version of the JupyterServer app.

You cannot delete the JupyterServer application while the Studio Classic UI is still open in
the browser. If you delete the JupyterServer application while the Studio Classic UI is still
open in the browser, SageMaker AI automatically re-creates the JupyterServer application.

Any unsaved notebook information is lost in the process. The user data in the Amazon EFS
volume isn't impacted.

Some of the services within Studio Classic, like Data Wrangler, run on their own app. To update these
services you must delete the app for that service. To learn more, see [Shut Down and Update Amazon SageMaker Studio Classic Apps](studio-tasks-update-apps.md "studio-tasks-update-apps.md").

###### Note

A JupyterServer app is associated with a single Studio Classic user. When you update the
app for one user it doesn't affect other users.

The following page shows how to update the JupyterServer App from the SageMaker AI console, from
Studio, or from inside Studio Classic.

1. Navigate to [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations**.
3. Under **Admin configurations**, choose
   **domains**.
4. Select the domain that includes the Studio Classic application that you want to
   update.
5. Under **User profiles**, select your user name.
6. Under **Apps**, in the row displaying
   **JupyterServer**, choose **Action**, then choose
   **Delete**.
7. Choose **Yes, delete app**.
8. Type `delete` in the confirmation box.
9. Choose **Delete**.
10. After the app has been deleted, launch a new Studio Classic app to get the latest
    version.
11. Navigate to Studio following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
12. From the Studio UI, find the applications pane on the left side.
13. From the applications pane, select **Studio Classic**.
14. From the Studio Classic landing page, select the Studio Classic instance to
    stop.
15. Choose **Stop**.
16. After the app has been stopped, select **Run** to use the latest
    version.
17. Launch Studio Classic.
18. On the top menu, choose **File** then **Shut
    Down**.
19. Choose one of the following options:
    - **Shutdown Server** – Shuts down the JupyterServer app.
      Terminal sessions, kernel sessions, SageMaker images, and instances aren't shut down.
      These resources continue to accrue charges.
    - **Shutdown All** – Shuts down all apps, terminal
      sessions, kernel sessions, SageMaker images, and instances. These resources no longer
      accrue charges.

20. Close the window.
21. After the app has been deleted, launch a new Studio Classic app to use the latest
    version.
