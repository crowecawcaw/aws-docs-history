# Windows Update and Antivirus Software on Amazon AppStream 2.0

AppStream 2.0 streaming instances are non-persistent. When a user streaming session ends, AppStream 2.0 terminates the instance used by the session and, depending on your scaling policies, provisions a new instance to replace it in your fleet. All fleet instances are provisioned from the same image. Because images cannot be changed once created, all fleet instances used in user streaming sessions have only the Windows and application updates that were installed on the underlying image when the image was created. In addition, because a fleet instance used for a streaming session terminates at the end of the session, any updates made to Windows or to applications on the instance during the streaming session will not persist to future sessions by the same user or other users.

###### Note

If you enabled application settings persistence for your stack, AppStream 2.0 persists Windows and application configuration changes made by a user to future sessions for the same user if those configuration changes are stored in the user’s Windows profile. However, the application settings persistence feature persists only Windows and application configuration settings. It does not persist software updates to Windows or applications on the streaming instance.

For these reasons, AppStream 2.0 takes the following approach to Windows Update and antivirus software on AppStream 2.0 instances.

## Windows Update

Windows Update is not enabled by default on AppStream 2.0 base images. If you enable Windows Update on an image builder and then try to create an image, Image Assistant displays a warning and disables Windows Update during the image creation process. To ensure that your fleet instances have the latest Windows updates installed, we recommend that you install Windows updates on your image builder, create a new image, and update your fleet with the new image on a regular basis.

## Antivirus Software

If you choose to install antivirus software on your image, we recommend that you do not enable automatic updates for the antivirus software. Otherwise, the antivirus software may attempt to update itself with the latest definition files or other updates during user sessions. This may affect performance. In addition, any updates made to the antivirus software will not persist beyond the current user session. To ensure that your fleet instances always have the latest antivirus updates, we recommend that you do either of the following:

- Update your image builder and create a new image on a regular basis (for example, by using the [Image Assistant CLI operations](programmatically-create-image.md "programmatically-create-image.md")).
- Use an antivirus application that delegates scanning or other operations to an always-up-to-date external server.

###### Note

Even if you do not enable automatic updates for your antivirus software, the antivirus software may perform hard drive scans or other operations that may impact the performance of your fleet instances during user sessions.

AppStream 2.0 Windows Server 2012 R2 base images do not include any antivirus software. On AppStream 2.0 Windows Server 2016 and Windows Server 2019 base images published on or after September 10, 2019, Windows Defender is not enabled by default. On AppStream 2.0 Windows Server 2016 and Windows Server 2019 base images published on June 24, 2019, Windows Defender is enabled by default.

###### To enable Windows Defender manually

If Windows Defender is not enabled on your base image, you can enable it manually. To do
so, complete the following steps.

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Images**, **Image Builder**.
3. Choose the image builder on which to enable Windows Defender, verify that it is in the **Running** state, and choose **Connect**.
4. Log in to the image builder with the local **Administrator** account or with
   a domain account that has local administrator permissions.
5. Open Registry Editor.
6. Navigate to the following location in the registry: **HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\DisableAntiSpyware**.
7. To edit this registry key, double-click it, or right-click the registry key, and choose **Modify**.
8. In the **Edit DWORD (32-bit) Value** dialog box, in **Value data**, change **1** to **0**.
9. Choose **OK**.
10. Close Registry Editor.
11. Open the Microsoft Management Console (MMC) **Services** snap-in (`services.msc`).
12. In the list of services, do one of the following.

If you are using Microsoft Windows Server 2022, do either of the
following:

    * Right-click **Microsoft Defender Antivirus Service**, and choose
     **Start**.
    * Double-click **Microsoft Defender Antivirus Service**, choose
     **Start** in the properties dialog box, and
     then choose **OK**.

If you are using Microsoft Windows Server 2019 or 2016, do either of the
following:

    * Right-click **Windows Defender Antivirus Service**, and choose
     **Start**.
    * Double-click **Windows Defender Antivirus Service**, choose
     **Start** in the properties dialog box, and
     then choose **OK**.

13. Close the **Services** snap-in.
