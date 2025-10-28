# Stop and delete your Studio running

applications and spaces

The following page includes information and instructions on how to stop and delete unused
Amazon SageMaker Studio resources to avoid unwanted additional costs. For the Studio resources
you no longer you wish to use, you will need to both:

- Stop the application: This stops both the application and deletes the instance
  that the application is running on. Once you stop an application you can start it
  back up again.
- Delete the space: This deletes the Amazon EBS volume that was created for the
  application and instance.

###### Important

If you delete the space, you will lose access to the data within that space.
Do not delete the space unless you're sure that you want to.
For more information about the differences between Studio spaces and applications,
see [View your Studio running instances,
applications, and spaces](studio-updated-running.md "studio-updated-running.md").

###### Topics

- [Stop your Amazon SageMaker Studio
  application](#studio-updated-running-stop-app "#studio-updated-running-stop-app")
- [Delete a Studio space](#studio-updated-running-stop-space "#studio-updated-running-stop-space")

## Stop your Amazon SageMaker Studio

application

To avoid additional charges from unused running applications, you must stop them. The
following includes information on what stopping an application does and how to do
it.

- The following instructions uses the [`DeleteApp`](../APIReference/API_DeleteApp.md "../APIReference/API_DeleteApp.md") API to stop the application. This also
  stops the instance that the application is running on.
- After you stop an application, you can start up the application again
  later.
  - When you stop an application, the files in the space will persist. You
    can run the application again and expect to have access to the same
    files that are stored in the space, as you did before deleting the
    application.
  - When you stop an application, the _metadata_ for the application will be deleted within 24
    hours. For more information, see the note in the
    `CreationTime` response element for the [DescribeApp](../APIReference/API_DescribeApp.md#sagemaker-DescribeApp-response-CreationTime "../APIReference/API_DescribeApp.md#sagemaker-DescribeApp-response-CreationTime") API.

###### Note

If the service detects that an application is unhealthy, it assumes the [AmazonSageMakerNotebooksServiceRolePolicy](security-iam-awsmanpol-notebooks.md#security-iam-awsmanpol-AmazonSageMakerNotebooksServiceRolePolicy "security-iam-awsmanpol-notebooks.md#security-iam-awsmanpol-AmazonSageMakerNotebooksServiceRolePolicy") service linked role and deletes the application using the [`DeleteApp`](../APIReference/API_DeleteApp.md "../APIReference/API_DeleteApp.md") API.

The following tabs provide instructions to stop an application from your domain
using the Studio UI, the SageMaker AI console, or the AWS CLI.

###### Note

To view and stop all of your Studio running instances in one location, we
recommend the [Stop
applications using the Studio UI](#studio-updated-running-stop-app-using-studio-updated-ui "#studio-updated-running-stop-app-using-studio-updated-ui")
workflow from the following options.

To stop your Studio applications using the Studio UI, use the
following instructions.

###### To delete your applications (Studio UI)

1. Launch Studio. This process may differ depending on your setup.
   For information about launching Studio, see [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. From the left navigation pane, choose **Running
   instances**.

If the table on the page is empty, you don't have any running
instances or applications in your spaces. 3. In the table under the **Name** and
**Application** columns, find the space name and
the application that you want to stop. 4. Choose the corresponding **Stop** button to stop the
application.
To view or stop Studio running instances from a centralized location, see
[Stop
applications using the Studio UI](#studio-updated-running-stop-app-using-studio-updated-ui "#studio-updated-running-stop-app-using-studio-updated-ui").
Otherwise, use the following instructions.

In the SageMaker AI console, you can only stop the running Studio applications
for the spaces that you are able to view in the **Spaces**
section of the console. For a list of the viewable spaces, see [View your Studio spaces](studio-updated-running.md#studio-updated-running-view-space "studio-updated-running.md#studio-updated-running-view-space").

These steps show how to stop your Studio applications by using the SageMaker AI
console.

###### To stop your applications (SageMaker AI console)

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. From the left navigation pane, expand **Admin
   configurations** and choose **Domains**.
3. Choose the domain that you want to revert.
4. On the **Domain details** page, choose the
   **Space management** tab.
5. ###### Important

In the **Space management** tab, you have the
option to delete the space. There is a difference between deleting
the space and deleting an application. If you delete the space, you
will lose access to the data within that space. Do not delete the
space unless you're sure that you want to.

To stop the application, in the **Space management**
tab and under the **Name** column, choose the space for
the application. 6. In the **Apps** section and under the **App
type** column, search for the app to stop. 7. Under the **Action** column, choose the corresponding
**Delete app** button. 8. In the pop-up box, choose **Yes, delete app**. After
you do so the delete input field becomes available. 9. Enter `delete` in the delete input field to
confirm deletion. 10. Choose **Delete**.
To view or stop any of your Studio running instances from a centralized
location, see [Stop
applications using the Studio UI](#studio-updated-running-stop-app-using-studio-updated-ui "#studio-updated-running-stop-app-using-studio-updated-ui").
Otherwise, use the following instructions.

The following code examples use the [`DeleteApp`](../APIReference/API_DeleteApp.md "../APIReference/API_DeleteApp.md") API to stop an application in an example
domain.

To stop your running **JupyterLab** or **Code Editor** instances, use the following code
example:

```
aws sagemaker delete-app \
--domain-id `example-domain-id` \
--region `AWS Region` \
--app-name default \
--app-type `example-app-type` \
--space-name `example-space-name`
```

- To obtain your
  `example-domain-id`, use the
  following instructions:

###### To get

`example-domain-id`

    1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
    2. From the left navigation pane, expand **Admin
     configurations** and choose
     **Domains**.
    3. Choose the relevant domain.
    4. On the **Domain details** page, choose the
     **Domain settings** tab.
    5. Copy the **Domain ID**.

- To obtain your `AWS Region`,
  use the following instructions to ensure you are using the correct
  AWS Region for your domain:

###### To get

`AWS Region`

    1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
    2. From the left navigation pane, expand **Admin
     configurations** and choose
     **Domains**.
    3. Choose the relevant domain.
    4. On the **Domain details** page, verify that
     this is the relevant domain.
    5. Expand the region dropdown list from the top right of the SageMaker AI
     console, and use the corresponding AWS Region ID to the right
     of your AWS Region name. For example,
     `us-west-1`.

- For `example-app-type`, use the
  application type that's relevant to the application that you want to
  stop. For example, replace
  `example-app-type` with
  one of the following application types:
  - JupyterLab application type: `JupyterLab`. For
    information about JupyterLab, see [SageMaker JupyterLab](studio-updated-jl.md "studio-updated-jl.md").
  - Code Editor application type: `CodeEditor`. For
    information about Code Editor, based on Code-OSS, Visual Studio Code - Open Source, see [Code Editor in Amazon SageMaker Studio](code-editor.md "code-editor.md").

- To obtain your
  `example-space-name`, use the
  following steps:

###### To get

`example-space-name`

    1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
    2. From the left navigation pane, expand **Admin
     configurations** and choose
     **Domains**.
    3. Choose the relevant domain.
    4. On the **Domain details** page, choose the
     **Space management** tab.
    5. Copy the relevant space name.

To stop running instances for **SageMaker Canvas**,
**Studio Classic**, or **RStudio**, use the following code example:

```
aws sagemaker delete-app \
--domain-id `example-domain-id` \
--region `AWS Region` \
--app-name default \
--app-type `example-app-type` \
--user-profile `example-user-name`
```

- For `example-app-type`, use the
  application type relevant to the application that you want to stop. For
  example, replace
  `example-app-type` with one of
  the following application types:
  - SageMaker Canvas application type: `Canvas`. For information
    about SageMaker Canvas, see [Amazon SageMaker Canvas](canvas.md "canvas.md").
  - Studio Classic application type: `JupyterServer`. For
    information about Studio Classic, see [Amazon SageMaker Studio Classic](studio.md "studio.md").
  - RStudio application type: `RStudioServerPro`. For
    information about RStudio, see [RStudio on Amazon SageMaker AI](rstudio.md "rstudio.md").

- To obtain your
  `example-user-name`, navigate
  to the **Domain details** page.
  - Next, choose the **User profiles** tab, and
    copy the relevant space name.

For alternative instructions to stop your running Studio applications, see:

- JupyterLab: [Delete unused resources](studio-updated-jl-admin-guide-clean-up.md "studio-updated-jl-admin-guide-clean-up.md").
- Code Editor: [Shut down Code Editor resources](code-editor-use-log-out.md "code-editor-use-log-out.md").
- SageMaker Canvas: [Logging out of Amazon SageMaker Canvas](canvas-log-out.md "canvas-log-out.md").
- Studio Classic: [Shut Down and Update Amazon SageMaker Studio Classic and Apps](studio-tasks-update.md "studio-tasks-update.md").
- RStudio: [Shut down RStudio](rstudio-shutdown.md "rstudio-shutdown.md").

## Delete a Studio space

###### Important

After you delete your space, you will lose all of the data stored in the space. We
recommend that you back up your data before deleting your space.

You will need to have administrator permissions, or at least have permissions to
update domain, IAM, and Amazon S3, to delete a Studio space.

- Spaces are used to manage the storage and resource needs of the relevant
  application. When you delete a space, the storage volume also deletes.
  Therefore, you lose access to the files stored on that space. For more
  information about Studio spaces, see [Amazon SageMaker Studio spaces](studio-updated-spaces.md "studio-updated-spaces.md").

We recommend that you back up your data if you choose to delete a
space.

- After you delete a space, you can't access that space again.

You can delete the Studio spaces that are viewable in the
**Spaces** section of the console. For a list of the viewable
spaces, see [View your Studio spaces](studio-updated-running.md#studio-updated-running-view-space "studio-updated-running.md#studio-updated-running-view-space").

There are no spaces for SageMaker Canvas, Studio Classic (private), and RStudio. To stop and delete
your SageMaker Canvas, Studio Classic (private), or RStudio applications, see [Stop your Amazon SageMaker Studio
application](#studio-updated-running-stop-app "#studio-updated-running-stop-app").

The **Spaces** section within your **Domain
details** page gives information about Studio spaces within
your domain. You can view, create, and delete spaces on this page.

###### To view Studio spaces in a domain

1.  Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2.  From the left navigation pane, expand **Admin
    configurations** and choose **Domains**.
3.  Choose the domain where you want to view the spaces.
4.  On the **Domain details**, choose **Space
    management** to open the **Spaces**
    section.
5.  Select the space to delete.
6.  Choose **Delete**.
7.  In the pop-up box titled **Delete space**, you have
    two options:
    - If you already shut down all applications in the space, choose
      **Yes, delete space**.
    - If you still have applications running in the space, choose
      **Yes, shut down all apps and delete
      space**.

8.  Enter `delete` in the delete input field to
    confirm deletion.
9.  To delete the space, you have two options:

        * If you already shut down all applications in the space, choose
         **Delete space**.
        * If you still have applications running in the space, choose
         **Shut down all apps and delete
         space**.

    Before you can delete a space using the AWS CLI, you must delete the application
    associated with it. For information about stopping your Studio
    applications, see [Stop your Amazon SageMaker Studio
    application](#studio-updated-running-stop-app "#studio-updated-running-stop-app").

Use the following AWS CLI command to delete a space within a domain:

```
aws sagemaker delete-space \
--domain-id `example-domain-id` \
--region `AWS Region` \
--space-name `example-space-name`
```

- To obtain your
  `example-domain-id`, use the
  following instructions:

###### To get

`example-domain-id`

    1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
    2. From the left navigation pane, expand **Admin
     configurations** and choose
     **Domains**.
    3. Choose the relevant domain.
    4. On the **Domain details** page, choose the
     **Domain settings** tab.
    5. Copy the **Domain ID**.

- To obtain your `AWS Region`,
  use the following instructions to ensure you are using the correct
  AWS Region for your domain:

###### To get

`AWS Region`

    1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
    2. From the left navigation pane, expand **Admin
     configurations** and choose
     **Domains**.
    3. Choose the relevant domain.
    4. On the **Domain details** page, verify that
     this is the relevant domain.
    5. Expand the region dropdown list from the top right of the SageMaker AI
     console, and use the corresponding AWS Region ID to the right
     of your AWS Region name. For example,
     `us-west-1`.

- To obtain your
  `example-space-name`, use the
  following steps:

###### To get

`example-space-name`

    1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
    2. From the left navigation pane, expand **Admin
     configurations** and choose
     **Domains**.
    3. Choose the relevant domain.
    4. On the **Domain details** page, choose the
     **Space management** tab.
    5. Copy the relevant space name.
