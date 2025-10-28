# Amazon Corretto 21 Installation Instructions for Windows 10 or

Later

This topic describes how to install and uninstall Amazon Corretto 21 on a host or container
running the Windows 10 or later Windows operating system.

## Install Amazon Corretto 21

1. Download a Windows `.msi` file from the [Downloads](downloads-list.md "downloads-list.md") page.
2. Double-click the .msi file to start the installation wizard.
3. Follow the steps in the wizard.

You have the option of setting a custom installation path. By default,
Amazon Corretto 21 is installed at `C:\Program Files\Amazon
 Corretto\`. If you set a custom path, make a note of it for the next
step. 4. Once the install wizard is finished, set the `JAVA_HOME` and
`PATH` environment variables.

Set `JAVA_HOME` to the installation location, noting that the
directory contains the currently-installed version. For example, if the default
directory is used for 21.0.9, then set `JAVA_HOME` as
`C:\Program Files\Amazon Corretto\jdk21.0.9_10`.

Add `%JAVA_HOME%\bin` to the current `PATH`
variable. 5. Verify the installation by running **java -version** in a command prompt.
You should see the following output.

```
openjdk version "21.0.9" 2025-10-21 LTS
OpenJDK Runtime Environment Corretto-21.0.9.10.1 (build 21.0.9+10-LTS)
OpenJDK 64-Bit Server VM Corretto-21.0.9.10.1 (build 21.0.9+10-LTS, mixed mode, sharing)
```

## Uninstall Amazon Corretto 21

You can uninstall Amazon Corretto 21 by following the standard steps to uninstall an
application from Windows.

1. Open **Programs and Features**.
2. Search for **Amazon Corretto 21** and then select it.
3. Choose **uninstall**.
