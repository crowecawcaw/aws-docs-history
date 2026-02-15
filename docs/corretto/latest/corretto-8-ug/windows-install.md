# Amazon Corretto 8 Installation Instructions for Windows 10 or

Later

This topic describes how to install and uninstall Amazon Corretto 8 on a host or container
running the Windows 10 or later Windows operating system.

## Install Amazon Corretto 8

**Prerequisite**: Amazon Corretto 8 requires Visual C++ Redistributable Package for Visual Studio 2013 or newer. If it's not installed
in your system, you can find it from [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=40784 "https://www.microsoft.com/en-us/download/details.aspx?id=40784") page.

1. Download a Windows `.msi` file from the [Downloads](downloads-list.md "downloads-list.md") page.
2. Double-click the .msi file to start the installation wizard.
3. Follow the steps in the wizard.

You have the option of setting a custom installation path. By default,
Amazon Corretto 8 is installed at `C:\Program Files\Amazon
 Corretto\`. If you set a custom path, make a note of it for the next
step. 4. Once the install wizard is finished, set the `JAVA_HOME` and
`PATH` environment variables.

Set `JAVA_HOME` to the installation location, noting that the
directory contains the currently-installed version. For example, if the default
directory is used for 8u482, then set `JAVA_HOME` as
`C:\Program Files\Amazon Corretto\jdk1.8.0_482`.

Add `%JAVA_HOME%\bin` to the current `PATH`
variable. 5. Verify the installation by running **java -version** in a command prompt.
You should see the following output.

###### Example

```
openjdk version "1.8.0_482"
OpenJDK Runtime Environment Corretto-8.482.08.1 (build 1.8.0_482-b08)
OpenJDK 64-Bit Server VM Corretto-8.482.08.1 (build 25.482-b08, mixed mode)
```

## Uninstall Amazon Corretto 8

You can uninstall Amazon Corretto 8 by following the standard steps to uninstall an
application from Windows.

1. Open **Programs and Features**.
2. Search for **Amazon Corretto 8** and then select it.
3. Choose **uninstall**.
