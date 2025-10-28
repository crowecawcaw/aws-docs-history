# Enable Regional Settings for Your AppStream 2.0

Users

To enable users to configure regional settings for a given stack during their AppStream 2.0
streaming sessions, your stack must be associated with a fleet based on an image that
uses a version of the AppStream 2.0 agent released on or after June 6, 2018. For more
information, see [AppStream 2.0 Agent Release Notes](agent-software-versions.md "agent-software-versions.md"). Additionally, your image must have Windows
PowerShell 5.1 or later installed. Images created from AppStream 2.0 base images published on
or after June 12, 2018 meet both criteria. Images created from AppStream 2.0 base images
published before June 12, 2018 do not have Windows PowerShell 5.1 by default.

###### To update an existing image to include Windows PowerShell 5.1

1.  Launch a new image builder using your existing image as the base image by
    doing the following:
    1. In the left navigation pane in the AppStream 2.0 console, choose
       **Images**.
    2. Choose the **Image Builder** tab, **Launch
       Image Builder**, and then select your existing
       image.
    3. If you are prompted to update the AppStream 2.0 agent when you launch the
       image builder, select the check box, and then choose
       **Start**.

2.  After your image builder is running, connect to it and sign in with an account
    that has local administrator permissions. To do so, do either of the following:
    - [Use the AppStream 2.0
      console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
    - [Create a
      streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or AppStream 2.0 client connections)

    ###### Note

    If the image builder that you want to connect to is joined to an
    Active Directory domain and your organization requires smart card
    sign in, you must create a streaming URL and use the AppStream 2.0 client
    for the connection. For information about smart card sign in, see
    [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

3.  From the image builder desktop, open Windows PowerShell. Choose the Windows
    **Start** button, and then choose **Windows
    PowerShell**.
4.  At the PowerShell command prompt, type the command
    `$PSVersionTable` to determine the version of Windows PowerShell
    that is installed on your image builder. If your image builder does not include
    Windows PowerShell 5.1 or later, use the following steps to install it.
5.  Open a web browser and follow the steps in [Install and Configure WMF 5.1](https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/wmf/setup/install-configure?view=powershell-7 "https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/wmf/setup/install-configure?view=powershell-7") in the Microsoft documentation,
    making sure that you download the Windows Management Framework (WMF) 5.1 package
    for Windows Server 2012 R2. WMF 5.1 includes Windows PowerShell 5.1.
6.  At the end of the WMF 5.1 installation process, the installer prompts you to
    restart your computer. Choose **Restart Now** to restart the
    image builder.
7.  Wait about 10 minutes before logging in to your image builder, even though
    AppStream 2.0 prompts you to do so immediately. Otherwise, you might encounter an
    error.
8.  After logging in to your image builder again, open Windows PowerShell and type
    the command `$PSVersionTable` to confirm that Windows PowerShell 5.1
    is installed on your image builder.
9.  Use the image builder to create a new image. This new image now includes the
    latest versions of the AppStream 2.0 agent and Windows PowerShell.
10. Update your fleet to use the new image by doing the following:

        1. In the left navigation pane in the AppStream 2.0 console, choose
         **Fleets**, and then choose the fleet associated
         with the stack for which you want to enable regional settings.
        2. On the **Fleet Details** tab, choose
         **Edit**.
        3. In **Image name,** choose the new image to use for
         the fleet.

    For more information about using image builders to create images, see [Tutorial: Create a Custom AppStream 2.0 Image by Using the
    AppStream 2.0 Console](tutorial-image-builder.md "tutorial-image-builder.md").
