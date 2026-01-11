# Supported submitters

The following sections guide you through the steps to launch the available Deadline Cloud
submitter plugins.

You can install other submitters not listed here. We use Deadline Cloud libraries to build
submitters. Some of the other submitters include Unreal Engine and 3ds Max.
You can find the source code for these libraries and submitters in the [aws-deadline GitHub](https://github.com/aws-deadline "https://github.com/aws-deadline") organization.

|                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Download for Windows](https://downloads.deadlinecloud.amazonaws.com/submitters/latest/windows/DeadlineCloudSubmitter-windows-x64-installer.exe "https://downloads.deadlinecloud.amazonaws.com/submitters/latest/windows/DeadlineCloudSubmitter-windows-x64-installer.exe") | [Download for MacOS (arm64)](https://downloads.deadlinecloud.amazonaws.com/submitters/latest/macos/DeadlineCloudSubmitter-osx-installer.app.zip "https://downloads.deadlinecloud.amazonaws.com/submitters/latest/macos/DeadlineCloudSubmitter-osx-installer.app.zip") | [Download for Linux](https://downloads.deadlinecloud.amazonaws.com/submitters/latest/linux/DeadlineCloudSubmitter-linux-x64-installer.run "https://downloads.deadlinecloud.amazonaws.com/submitters/latest/linux/DeadlineCloudSubmitter-linux-x64-installer.run") |

| Software                      | Supported versions | Windows installer                                                     | Linux installer                                                   | MacOS (arm64) installer                                               |
| ----------------------------- | ------------------ | --------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| Adobe After Effects           | 2024<br>• 2025     | Included                                                              | Not included                                                      | Included                                                              |
| Autodesk 3ds Max              | 2024<br>• 2026     | Included                                                              | Not included                                                      | Not included                                                          |
| Autodesk Arnold for Cinema 4D | 4.8.4.1            | Included                                                              | Not included                                                      | Included                                                              |
| Autodesk Arnold for Maya      | 7.1<br>• 7.4       | Included                                                              | Included                                                          | Included                                                              |
| Autodesk Maya                 | 2023<br>• 2026     | [Included](#submitter-launch-maya "#submitter-launch-maya")           | [Included](#submitter-launch-maya "#submitter-launch-maya")       | [Included](#submitter-launch-maya "#submitter-launch-maya")           |
| Autodesk VRED                 | 2025<br>• 2026     | Included                                                              | Not included                                                      | Not included                                                          |
| Blender                       | 3.6<br>• 4.5       | [Included](#submitter-launch-blender "#submitter-launch-blender")     | [Included](#submitter-launch-blender "#submitter-launch-blender") | [Included](#submitter-launch-blender "#submitter-launch-blender")     |
| Chaos V-Ray for Maya          | 6<br>• 7           | Included                                                              | Included                                                          | Included                                                              |
| Foundry Nuke                  | 15<br>• 16         | [Included](#submitter-launch-nuke "#submitter-launch-nuke")           | [Included](#submitter-launch-nuke "#submitter-launch-nuke")       | [Included](#submitter-launch-nuke "#submitter-launch-nuke")           |
| KeyShot Studio                | 2023<br>• 2025     | [Included](#submitter-launch-keyshot "#submitter-launch-keyshot")     | Not included                                                      | [Included](#submitter-launch-keyshot "#submitter-launch-keyshot")     |
| Maxon Cinema 4D               | 2024<br>• 2026     | [Included](#submitter-launch-cinema-4d "#submitter-launch-cinema-4d") | Not included                                                      | [Included](#submitter-launch-cinema-4d "#submitter-launch-cinema-4d") |
| Maxon Redshift for Maya       | 2025               | Included                                                              | Included                                                          | Included                                                              |
| SideFX Houdini                | 19.5<br>• 21.0     | [Included](#submitter-launch-houdini "#submitter-launch-houdini")     | [Included](#submitter-launch-houdini "#submitter-launch-houdini") | [Included](#submitter-launch-houdini "#submitter-launch-houdini")     |

For mnore detailed instructions on how to use the submitters and troubleshoot issues, see the
[AWS Deadline Cloud integrations user guide](https://aws-deadline.github.io/ "https://aws-deadline.github.io/").

## Adobe After

Effects

###### To launch the Deadline Cloud submitter in Adobe After Effects

1. Open **After Effects**.

###### Note

If you performed a system install of the Deadline Cloud submitter, run
After Effects as Admin. 2. Update the following settings:

    * For Windows, choose **Edit** > **Preferences** >
     **Scripting & Expressions**, and then choose
     **Allow scripts to write files and access networks**.
    * For macOS, choose **After Effects** > **Settings** >
     **Scripting & Expressions**, and then choose
     **Allow scripts to write files and access networks**.

3. Choose **Allow scripts to write files and access
   networks**.
4. Restart After Effects.
5. To open Deadline Cloud submitter:
   - On a system install, select **Window**, then choose
     **DeadlineCloudSubmitter.jsx**.
   - On a user install, choose **File** >
     **Scripts** > **Run Script File**,
     and then locate and select **DeadlineCloudSubmitter.jsx**.

###### To use the After Effects submitter

1. Choose **Open render queue** on the submitter
   panel.
2. Add a composition to your render queue and set up the render settings,
   output module, and output path.
3. Choose **Refresh** on the submitter panel.
4. Choose your composition from the list and then choose
   **Submit**. You can choose **Refresh**
   again when you add or remove compositions from your render queue.

You can dock the submitter into the side panels by choosing the top right corner
of the submitter and dropping it in any highlighted section in After
Effects.

## Autodesk 3ds Max

###### To launch the Deadline Cloud submitter in Autodesk 3ds Max

1. Open **Autodesk 3ds Max.**
2. From the menu, choose **AWS Deadline**,
   and then choose **Submit to Deadline Cloud.**

## Autodesk VRED

###### To launch the Deadline Cloud submitter in Autodesk VRED

1. Open **VRED Professional**.
2. Choose **Edit** > **Preferences**.
3. In the Preferences window, select **General Settings**,
   and then choose **Script**.
4. Verify the **Enable Python Sandbox** option is not selected.
5. In the **Script** section, add the following text to the end of the section:

```
from DeadlineCloudForVRED import DeadlineCloudForVRED
DeadlineCloudForVRED()
```

6. Choose **Save**.
7. Restart **VRED Professional**. When VRED
   opens, the Deadline Cloud button displays in the menu bar.

###### To use the Deadline Cloud submitter in Autodesk VRED

1. Open an Autodesk VRED scene file.
2. To launch the submitter, from the menu bar, choose **Deadline Cloud**,
   and then choose **Submit to Deadline Cloud**.
   1. If you are not already authenticated in the Deadline Cloud submitter, the
      **Credentials Status** shows as
      **NEEDS_LOGIN**.
   2. Choose **Login**.
   3. In the login browser window, log in with your user
      credentials.
   4. Choose **Allow**. You are now logged in and the
      **Credentials Status** shows as
      **AUTHENTICATED**.

3. In the **Submit to Deadline Cloud** dialog box, configure your settings, including
   the render settings in the **Job-specific settings** tab.
4. To submit your render to Deadline Cloud, choose **Submit**.

## Blender

###### To launch the Deadline Cloud submitter in Blender

###### Note

Support for Blender is provided using the
Conda environment for service-managed fleets. For more
information, see [Default Conda queue
environment](create-queue-environment.md#conda-queue-environment "create-queue-environment.md#conda-queue-environment").

1. Open **Blender**.
2. Choose **Edit**, then **Preferences**.
   Under **File Paths** choose **Script
   Directories**, then choose **Add**. Add a
   script directory for the python folder where the Blender
   submitter was installed:

```
Windows:
   %USERPROFILE%\DeadlineCloudSubmitter\Submitters\Blender\python\
Linux:
   ~/DeadlineCloudSubmitter/Submitters/Blender/python/
```

3. Restart Blender.
4. Choose **Edit**, then **Preferences**.
   Next, choose **Add-ons**, then search for **Deadline Cloud
   for Blender**. Select the checkbox to enable the
   add-on.
5. Open a Blender scene with dependencies that exist within
   the asset root directory.
6. In the **Render** menu, select the Deadline Cloud dialog.
   1. If you are not already authenticated in the Deadline Cloud submitter, the
      **Credentials Status** shows as
      **NEEDS_LOGIN**.
   2. Choose **Login**.
   3. A login browser window displays. Log in with your user
      credentials.
   4. Choose **Allow**. You are now logged in and the
      **Credentials Status** shows as
      **AUTHENTICATED**.

7. Choose **Submit**.

## Cinema 4D

###### To launch the Deadline Cloud submitter in \*\*Cinema

4D\*\*

###### Note

Support for Cinema 4D is provided using the
Conda environment for service-managed fleets. For more
information, see [Default Conda queue
environment](create-queue-environment.md#conda-queue-environment "create-queue-environment.md#conda-queue-environment").

1. Open **Cinema 4D**.
2. If prompted to install GUI components for AWS Deadline Cloud, complete the
   following steps:
   1. When the prompt displays, choose **Yes**, and
      wait for dependencies to install.
   2. Restart Cinema 4D to ensure the changes are
      applied.

3. Choose **Extensions** > **AWS Deadline Cloud
   Submitter**.

## Houdini

###### To launch the Deadline Cloud submitter in Houdini

###### Note

Support for Houdini is provided using the
Conda environment for service-managed fleets. For more
information, see [Default Conda queue
environment](create-queue-environment.md#conda-queue-environment "create-queue-environment.md#conda-queue-environment").

1. Open **Houdini**.
2. In the **Network Editor**, select the
   **/out** network.
3. Press **tab**, and enter
   `deadline`.
4. Select the Deadline Cloud option, and connect it to your existing network.
5. Double-click the **Deadline Cloud node**.

## KeyShot

###### To launch the Deadline Cloud submitter in KeyShot

1. Open KeyShot.
2. Choose **Windows** >
   **Scripting console** > **Submit to
   AWS Deadline Cloud** and **Run**.

There are two submission modes for the KeyShot submitter. Select the submission
mode to open the submitter.

- _Attach the scene BIP file and all external file
  references_ – The open scene file and all external
  files referenced in the BIP are included as job attachments.
- _Attach only the scene BIP file_ – Only the
  open scene file is attached to the submission. Any external files referenced
  in the scene must be available to workers through network storage or another
  method.

## Maya

###### To launch the Deadline Cloud submitter in Maya

1. Open **Maya**.
2. Set your project, and open a file that exists within the asset root
   directory.
3. Choose **Windows → Settings/Preferences → Plugin
   Manager**.
4. Search for **DeadlineCloudSubmitter**.
5. To load the Deadline Cloud submitter plugin, select
   **Loaded**.
   1. If you are not already authenticated in the Deadline Cloud submitter, the
      **Credentials Status** shows as
      **NEEDS_LOGIN**.
   2. Choose **Login**.
   3. A login browser window displays. Log in with your user
      credentials.
   4. Choose **Allow**. You are now logged in and the
      **Credentials Status** shows as
      **AUTHENTICATED**.

6. (Optional) To load the Deadline Cloud submitter plugin every time you open
   Maya, choose **Auto-load**.
7. Select the Deadline Cloud shelf, then select the green button to launch the
   submitter.

## Nuke

###### To launch the Deadline Cloud submitter in Nuke

###### Note

Support for Nuke is provided using the Conda
environment for service-managed fleets. For more information, see [Default Conda queue
environment](create-queue-environment.md#conda-queue-environment "create-queue-environment.md#conda-queue-environment").

1. Open **Nuke**.
2. Open a Nuke script with dependencies that exist within the
   asset root directory.
3. Choose **AWS Deadline**, and then choose
   **Submit to Deadline Cloud** to launch the
   submitter.
   1. If you are not already authenticated in the Deadline Cloud submitter, the
      **Credentials Status** shows as
      **NEEDS_LOGIN**.
   2. Choose **Login**.
   3. In the login browser window, log in with your user
      credentials.
   4. Choose **Allow**. You are now logged in and the
      **Credentials Status** shows as
      **AUTHENTICATED**.

4. Choose **Submit**.
