# Code spaces in IAM domains

In Amazon SageMaker Unified Studio projects for IAM domains, you can create and manage multiple code
spaces—individually configured development environments—within a single project.
Each code space maintains its own persistent Amazon EBS volume, compute instance, and runtime
configuration, enabling parallel experimentation with full isolation.

To access code spaces, choose **Code spaces** from the left sidebar in
your project. The code spaces list displays all your existing spaces with their application
type, status, and last modified time. You can open spaces in a dedicated browser tab or
connect to a local IDE such as VS Code, Kiro, or Cursor using the local IDE icons in the
actions area for each space.

## Creating a code space in IAM domains

To create a code space, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to your project and choose **Code spaces** from the left
   sidebar.
3. Choose **Create**.
4. Select an application type by choosing one of the available cards:
   - **JupyterLab**—A web-based interactive
     development environment for notebooks, code, and data.
   - **Code Editor**—A lightweight code editor
     for writing and editing code.

5. Under **Instance**, choose an instance type (for example,
   ml.t3.medium).
6. Under **Image**, choose the image you want to use (for example,
   SageMaker Distribution 2.11).
7. Under **EBS space storage**, enter a value from 16 to 100
   GB.
8. (Optional) Expand **Advanced settings** to configure additional
   options:
   - Enable remote access for local IDE connections.
   - Attach a lifecycle configuration.
   - Set an idle timeout.
   - Attach a custom filesystem.

9. Choose **Create**.

After the space is created, it appears in the code spaces list. Choose
**Open** to launch the space in a new browser tab, or choose a local IDE
icon (VS Code, Kiro, or Cursor) to open the space in your preferred local IDE.

## Managing code spaces in IAM domains

You can manage your code spaces from the code spaces list view. Choose the three-dot
menu (…) under **Actions** for any space to access the following
options:

- **View details**—View information about the
  space including its configuration and status.
- **Configure**—Change the space configuration
  such as instance type, image, or storage size.
- **Stop**—Stop the running space. Active
  processes are paused and unsaved changes are discarded.
- **Delete**—Permanently delete the space and its
  associated Amazon EBS volume.

###### Note

Saving configuration changes to a running space requires a restart. Active processes
are paused and unsaved changes are discarded during the restart.

## Configuring a code space in IAM domains

To configure an existing code space, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to your project and choose **Code spaces** from the left
   sidebar.
3. Choose the three-dot menu (…) under **Actions** next to the
   space you want to configure, then choose **Configure**.
4. Make the desired changes to the space configuration.
5. Choose one of the following:
   - **Save and restart**—If the space is running, saves
     changes and restarts the space.
   - **Stop space**—Stops the space without saving
     changes.
   - **Cancel**—Discards changes and returns to the code
     spaces list.

## Amazon Q support in code spaces for IAM domains

Amazon Q free tier support is available across all code space types in IAM domains.
When your administrator has subscribed to Amazon Q Developer and added it to your domain,
you can access the Amazon Q chat interface and inline code suggestions in both JupyterLab
and Code Editor spaces.
