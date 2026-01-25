# Amazon Corretto 17 Installation Instructions for Windows 10 or

Later

This topic describes how to install and uninstall Amazon Corretto 17 on a host or container
running the Windows 10 or later Windows operating system.

## Install Amazon Corretto 17

1. Download a Windows `.msi` file from the [Downloads](downloads-list.md "downloads-list.md") page.
2. Double-click the .msi file to start the installation wizard.
3. Follow the steps in the wizard.

You have the option of setting a custom installation path. By default,
Amazon Corretto 17 is installed at `C:\Program Files\Amazon
 Corretto\`. If you set a custom path, make a note of it for the next
step. 4. Once the install wizard is finished, set the `JAVA_HOME` and
`PATH` environment variables.

Set `JAVA_HOME` to the installation location, noting that the
directory contains the currently-installed version. For example, if the default
directory is used for 17.0.18, then set `JAVA_HOME` as
`C:\Program Files\Amazon Corretto\jdk17.0.18_8`.

Add `%JAVA_HOME%\bin` to the current `PATH`
variable. 5. Verify the installation by running **java -version** in a command prompt.
You should see the following output.

```
openjdk version "17.0.18" 2026-01-20 LTS
OpenJDK Runtime Environment Corretto-17.0.18.8.1 (build 17.0.18+8-LTS)
OpenJDK 64-Bit Server VM Corretto-17.0.18.8.1 (build 17.0.18+8-LTS, mixed mode, sharing)
```

## Uninstall Amazon Corretto 17

You can uninstall Amazon Corretto 17 by following the standard steps to uninstall an
application from Windows.

1. Open **Programs and Features**.
2. Search for **Amazon Corretto 17** and then select it.
3. Choose **uninstall**.
