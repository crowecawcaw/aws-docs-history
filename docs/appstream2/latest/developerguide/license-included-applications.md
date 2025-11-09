# Manage License Included Applications on Your Image in Amazon WorkSpaces Applications

You can stream the following Microsoft license included applications using WorkSpaces Applications. You
can install these applications on your Windows Image, use this custom image to create
fleet(s), and then stream these applications. All of the following applications are
available in 32-bit and 64-bit architecture:

- Microsoft Office LTSC Professional Plus 2021/2024
- Microsoft Visio LTSC Professional 2021/2024
- Microsoft Project Professional 2021/2024
- Microsoft Office LTSC Standard 2021/2024
- Microsoft Visio LTSC Standard 2021/2024
- Microsoft Project Standard 2021/2024

###### Important

    + Microsoft Office, Visio, and Project must follow the same
     versions. For example, you can't mix 2021 applications with 2024
     applications.
    + Microsoft Office, Visio, and Project must follow the same
     architecture. For example, you can't mix 32-bit applications with
     64-bit applications.
    + Microsoft Office, Visio, and Project 2021 Standard/Professional
     versions are supported on Microsoft Windows Server 2019 and 2022.
     Microsoft Office, Visio, and Project 2024 Standard/Professional
     versions are supported on Microsoft Windows Server 2022.
    + To enable this feature, you must use an WorkSpaces Applications Image Builder that
     uses an WorkSpaces Applications agent released on or after October 2, 2025. For more
     information, see [Manage WorkSpaces Applications Agent Versions](base-images-agent.md "base-images-agent.md") . Or, your
     image must use managed WorkSpaces Applications image updates released on or after
     October 3, 2025. For more information, see [Keep Your Amazon WorkSpaces Applications Image Up-to-Date](keep-image-updated.md "keep-image-updated.md").
    + Outbound TCP on port 1688 must be open on the management network
     interface of all streaming instances.
    + All users streaming through a fleet powered by an image with one
     or more licensed apps incur billing for these apps monthly,
     regardless of usage. The application entitlement feature doesn't
     restrict access for specific users.
    + License included applications on Image Builder aren't activated
     because they are installed for administrative purposes. Activation
     occurs when users stream through a fleet instance.

###### Contents

- [View the list of license included applications installed on your image](view-list-image.md "view-list-image.md")
- [View the list of license included applications on your image builder](view-list-apps.md "view-list-apps.md")
- [Install or uninstall license included applications](install-uninstall-apps.md "install-uninstall-apps.md")
- [Enable updates for license included applications on image builder](updates-image-builder.md "updates-image-builder.md")
- [Enable updates for license included applications on image builder with
  Powershell](enable-updates-managed-powershell.md "enable-updates-managed-powershell.md")
- [Enable updates for license included applications on image builder with Managed
  Image Update](enable-updates-managed.md "enable-updates-managed.md")
