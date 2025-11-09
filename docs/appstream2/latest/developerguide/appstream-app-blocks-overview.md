# Overview

To create an app block with WorkSpaces Applications packaging, you need to initiate a streaming
session with an app block builder. After the session is launched, you can
download your application installers and enable the recording options. From that
point onwards, WorkSpaces Applications records the file system and registry changes made on the
app block builder using Application Redirection technology.

Application Redirection uses Windows filter driver framework to intercept and
redirect file-system and registry changes. This redirection is seamless to the
application being installed. The application will continue to interact with the
original file locations on the C: drive. For example, if an installer for
"TestApplication" is run on a machine with App Redirection set up, it will be
installed by default to C:\Program Files\TestApplication. However, behind the
scenes, all files and folders will be redirected to a mounted virtual hard disk
(VHD), and a link will be created from the original file location to the actual
file location. On the machine, TestApplication will still appear to be installed
at C:\Program Files\TestApplication.

After all the installation changes are recorded, the VHD file is uploaded to
an Amazon S3 bucket in your account.

When a user requests a session using an Elastic fleet, WorkSpaces Applications downloads the
VHD file, sets up the application, runs the post-installation setup scripts
(optional), and starts the application streaming.

###### Note

Application Redirection technology does not record any file system changes
under %USERPROFILE%, except new directories created under %APPDATA% and
%LOCALAPPDATA% directories.

Application Redirection technology does not record any registry changes
under the current user, HKEY_CURRENT_USER (HKCU).
