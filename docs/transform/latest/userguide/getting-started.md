# Getting started with AWS Transform

###### Topics

- [Setting up AWS Transform](transform-setup.md "transform-setup.md")
- [Enable AWS Transform](#transform-enable "#transform-enable")
- [Quick start: Trying AWS Transform](#transform-app-admin-starting-standalone "#transform-app-admin-starting-standalone")
- [Managing users](transform-user-management.md "transform-user-management.md")
- [AWS Transform environment](transform-environment.md "transform-environment.md")
- [AWS Transform Connectors](transform-user-connectors.md "transform-user-connectors.md")

## Enable AWS Transform

To enable AWS Transform:

1. Sign in to the AWS Management Console.
2. In the search bar at the top of the console, search for _AWS Transform_.
3. Select **AWS Transform** from the search results.
4. Choose **Get started** to enable the service in your current
   Region.
5. Optional: configure IAM Identity Center. You will also be able to choose to use a [third-party identity provider (IdP)](transform-setup.md#transform-third-party-identity "transform-setup.md#transform-third-party-identity") in a
   later step.
6. Select an **Encryption key**: **default
   AWS managed key** or **Customize encryption settings.**
7. Optional: Use your own Amazon S3 bucket. By default, AWS Transform uses a service-managed Amazon S3
   bucket to store transformation artifacts. You can choose to use your own bucket instead.
   For more information, see [Using your own Amazon S3 bucket](custom-s3-bucket.md "custom-s3-bucket.md").
8. Choose which AWS Transform capabilities you want to enable:

   - **Command line interface** (CLI), needed to create and run
     [custom transformations](transform-app-custom.md "transform-app-custom.md"). To enable the CLI, view
     and follow the download instructions.
   - **Web application**, the agentic user interface for modernization.
     Choose **Enable web application** to use it.

9. Choose **Enable AWS Transform**.
10. Optional: choose **Enable View profile** to access the AWS Transform **Users**, **Settings**, and **Connectors** tabs, or **Manage users** to manage
    users.

You can access the **Users**, **Settings**, and **Connectors** tabs at any time by
choosing the menu icon in the top left corner of the console. 11. Configure User access by choosing one of the following options:

    * IAM Identity Center
    * A [third-party identity provider (IdP)](transform-setup.md#transform-third-party-identity "transform-setup.md#transform-third-party-identity")
    * [IAM-only access](transform-setup.md#transform-iam-only-access "transform-setup.md#transform-iam-only-access")

###### Note

This choice is finalized and cannot be changed when you enable AWS Transform. 12. Choose **Enable web application**. 13. The system displays "Enabling AWS Transform" while it creates the necessary resources.

After AWS Transform is enabled, the **Settings** tab displays the following information:

- **Web application URL** - The URL for accessing the AWS Transform web application
- **Start URL for IDE** - The URL for accessing AWS Transform in integrated development environments
- **Region** - The AWS Region where AWS Transform is enabled

## Quick start: Trying AWS Transform

The easiest way to try out AWS Transform is with a standalone AWS account. You may want to do this as a proof-of-concept or for test environments. Use this procedure:

1. Sign in to the AWS Management Console.
2. Navigate to the AWS Transform service.
3. Choose **Get started** to enable the service.
4. Select and set up your identity provider.
5. Assign users to AWS Transform service.
6. After the service is enabled, you'll see the AWS Transform web application URL.
7. Open that URL in a new browser window to access the AWS Transform web experience.

Now you're ready to set up your workspace.
