# Image Builder Actions

You can perform the following actions on an image builder, depending on the current
state (status) of the image builder instance.

**Delete**

Permanently delete an image builder.

The instance must be in a **Stopped** state.

**Connect**

Connect to a running image builder. This action starts a desktop streaming
session with the image builder to install and add applications to the image,
and create an image.

The instance must be in a **Running** state.

**Start**

Start a stopped image builder. A running instance is billed to your
account.

The instance must be in a **Stopped** state.

**Stop**

Stop a running image builder. A stopped instance is not billed to your
account.

The instance must be in a **Running** state.

**Manage license included applications**

Install or uninstall license included applications.

- Select one or more license included applications that you want to
  install on your image.
  - Already installed license included applications display a
    checked checkbox next to them, and the status says
    **Installed**.
  - If you want to uninstall an already installed license
    included application, uncheck the checkbox next to
    it.
  - If one or more applications are in **Failed to
    install**, **Installation timed
    out**, or **Installation
    skipped** status, the service retries the
    installation after you select **Apply
    Changes**. If you want to uninstall these
    applications, uncheck the checkbox next to them.
  - If one or more applications are in **Failed to
    uninstall**, **Uninstallation timed
    out**, or **Uninstallation
    skipped** status, and you want to uninstall
    these applications, uncheck the checkbox next to them

- Select **Apply Changes**.
- Verify the **Manage license included applications
  summary** and select **Confirm and deploy
  updates**.
- After connecting to the Image Builder, you can see the apps you
  selected already installed there.

None of these actions can be performed on an instance in any of the following
intermediate states:

- **Pending**
- **Snapshotting**
- **Stopping**
- **Starting**
- **Deleting**
- **Updating**
- **Pending Qualification**
- **Pending Syncing Apps**
- **Syncing Apps**
