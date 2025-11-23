# Download NoSQL Workbench for DynamoDB

Follow these instructions to download NoSQL Workbench and DynamoDB local\* for
Amazon DynamoDB.

**Prerequisites**

There are two prerequisite pieces of software required for Ubuntu installs: libfuse2
and curl.

**libfuse2**

As of Ubuntu 22.04, libfuse2 is no longer installed by default. To solve
this, run `sudo add-apt-repository universe && sudo apt install
 libfuse2` to install for the [newest Ubuntu
version](https://github.com/AppImage/AppImageKit/wiki/FUSE "https://github.com/AppImage/AppImageKit/wiki/FUSE").

**curl**

Update Ubuntu, run `sudo apt update && sudo apt
 upgrade`

Next, install `cURL`, execute: `sudo apt install
 curl`

###### To download NoSQL Workbench and DynamoDB local

1. Download the appropriate version of NoSQL Workbench for your operating
   system.

| Operating system      | Download link                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| macOS (Intel)\*\*     | [Download for macOS (Intel)](https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench-x64.dmg "https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench-x64.dmg")             |
| macOS (Apple silicon) | [Download for macOS (Apple silicon)](https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench-arm64.dmg "https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench-arm64.dmg") |
| Windows               | [Download for Windows](https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench.exe "https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench.exe")                           |
| Linux\*\*\*           | [Download for Linux](https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench.AppImage "https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench.AppImage")                   |

\* NoSQL Workbench includes DynamoDB local as an optional part of the installation
process.

\*\* If a warning message appears when you try to open NoSQL Workbench stating
that the app isn't registered with Apple by an identified developer, do the
following:

    1. Locate the app and then open it.
    2. Control+click the app icon, then choose Open from the shortcut
     menu.


    This saves the app as an exception to your security settings. Open the
     app by double-clicking it just as you can open any registered
     app.

\*\*\* NoSQL Workbench supports Ubuntu 12.04, Fedora 21, and Debian 8, or any
newer versions of these Linux distributions. 2. Start the application that you downloaded, and then follow the steps in
Install NoSQL Workbench.

###### Note

Java Runtime Environment (JRE) version 11.x or newer is required for running
DynamoDB local.
