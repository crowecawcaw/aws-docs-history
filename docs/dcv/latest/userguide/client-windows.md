# Windows client

The Amazon DCV Windows client is supported on Windows computers only. The Windows client is a
standalone application that runs on the Windows operating system.

For instructions on how to connect to a Amazon DCV session using the Windows client, see [Connecting to a Amazon DCV session using the Windows
client](using-connecting-win.md "using-connecting-win.md").

The Windows client is available in two versions: an installable version and a portable
version. Both versions have the same minimum system requirements and have the same
features.

###### Contents

- [Installable Windows client](client-windows.md#client-windows-install "client-windows.md#client-windows-install")
- [Portable Windows client](client-windows.md#client-windows-portable "client-windows.md#client-windows-portable")

## Installable Windows client

You can use an installation wizard to install the client. The wizard takes you through a
series of steps where you can customize your client installation. Or, you can use the
command line to perform an unattended installation. This second method uses default settings
to automate the installation procedure.

Before using the wizard or the command line to install the client, make sure that your
computer has the required software. For a complete list of required software, see [Requirements](requirements.md "requirements.md").

###### To install the Windows client using the installation wizard

1. Download the [Windows client installer](https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Clients/nice-dcv-client-Release-2025.0-9800.msi "https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Clients/nice-dcv-client-Release-2025.0-9800.msi").

###### Tip

The [latest packages](http://download.amazondcv.com/latest.html "http://download.amazondcv.com/latest.html") page of the download
website contains links that always point to the newest available version. You can use
these links to automatically retrieve the newest Amazon DCV packages. 2. Run the installer. 3. On the **Welcome** screen, choose
**Next**. 4. On the **End-User License Agreement** screen, read the license
agreement. If you accept the terms, select the **I accept the terms in the
License Agreement** check box. Choose **Next**. 5. On the **Destination Folder** screen, choose
**Next** to keep the default installation folder. To
install the client in a different folder, change the destination path, and
then choose **Next**. 6. (Optional) On the **Drivers Selection** screen, select **USB
device remotization**. Then, choose **Will be installed on local hard
drive**, **Next**. This installs the drivers required to
support some specialized USB devices. These devices include 3D pointing devices and
graphic tablets.

###### Note

Using specialized USB devices requires additional client and server configuration.
For instructions, see [Using USB remotization](using-usb.md "using-usb.md"). 7. On the **Ready to install** screen, choose
**Install**.

###### To install the Windows client using an unattended installation

1. Download the [Windows client installer](https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Clients/nice-dcv-client-Release-2025.0-9800.msi "https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Clients/nice-dcv-client-Release-2025.0-9800.msi").
2. Open a command prompt window and navigate to the folder where you
   downloaded the installer.
3. Run the unattended installer.

```
`C:\>` msiexec.exe /i nice-dcv-client-Release-2025.0-9800.msi /quiet /norestart /l*v dcv_client_install_msi.log
```

To install all of the optional components, including the USB driver, include the
`ADDLOCAL=ALL` option in the command.

```
`C:\>`  msiexec.exe /i nice-dcv-client-Release-2025.0-9800.msi ADDLOCAL=ALL /quiet /norestart /l*v dcv_client_install_msi.log
```

## Portable Windows client

The Windows client is also available in a portable version. You don't need to install the
portable version on your computer. You can copy it to a USB drive and run it directly from
the USB drive on any Windows computer that meets the minimum requirements.

###### To use the portable Windows client

1. Download the portable [Windows client zip file](https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Clients/nice-dcv-client-Release-portable-2025.0-9800.zip "https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Clients/nice-dcv-client-Release-portable-2025.0-9800.zip").

###### Tip

The [latest packages](http://download.amazondcv.com/latest.html "http://download.amazondcv.com/latest.html") page of the download website contains links that always point to the newest available version.
You can use these links to automatically retrieve the newest Amazon DCV packages. 2. Extract the contents of the zip file. 3. To launch the client, open the extracted folder, navigate to
`/bin/`, and double-click `dcvviewer.exe`.
