# Shut Down and Update Amazon SageMaker Studio Classic Apps

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

To update an Amazon SageMaker Studio Classic app to the latest release, you must first shut down the
corresponding KernelGateway app from the SageMaker AI console. After the KernelGateway app is shut
down, you must reopen it through SageMaker Studio Classic by running a new kernel. The kernel
automatically updates. Any unsaved notebook information is lost in the process. The user
data in the Amazon EFS volume isn't impacted.

After an application has been shut down for 24 hours, SageMaker AI deletes all metadata for the
application. To be considered an update and retain application metadata, applications must
be restarted within 24 hours after the previous application has been shut down. After this
time window, creation of an application is considered a new application rather than an
update of the previous application.

###### Note

A KernelGateway app is associated with a single Studio Classic user. When you update the
app for one user it doesn't effect other users.

###### To update the KernelGateway app

1. Navigate to [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations**.
3. Under **Admin configurations**, choose
   **domains**.
4. Select the domain that includes the application that you want to update.
5. Under **User profiles**, select your user name.
6. Under **Apps**, in the row displaying the **App
   name**, choose **Action**, then choose
   **Delete**

To update Data Wrangler, delete the app that starts with
**sagemaker-data-wrang**. 7. Choose **Yes, delete app**. 8. Type `delete` in the confirmation box. 9. Choose **Delete**. 10. After the app has been deleted, launch a new kernel from within Studio Classic to use
the latest version.
