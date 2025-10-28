# Amazon Corretto 17 Installation Instructions for macOS 11 or

later

This topic describes how to install and uninstall Amazon Corretto 17 on a host running the Mac
OS version 11 or later. You must have administrator permissions to install
and uninstall Amazon Corretto 17.

## Install Amazon Corretto 17

1. Download the Mac `.pkg` file from the [Downloads](downloads-list.md "downloads-list.md") page.
2. Double-click the downloaded file to begin the installation wizard and follow
   the steps in the wizard.
3. Once the wizard completes, Amazon Corretto 17 is installed in
   `/Library/Java/JavaVirtualMachines/`.

You can run the following command in a terminal to get the complete installation path.

```
/usr/libexec/java_home --verbose
```

4. Run the following command in the terminal to set the `JAVA_HOME`
   variable to the Amazon Corretto 17 version of the JDK. If this was set to another version
   previously, it is overridden.

```
export JAVA_HOME=/Library/Java/JavaVirtualMachines/amazon-corretto-17.jdk/Contents/Home
```

## Uninstall Amazon Corretto 17

You can uninstall Amazon Corretto 17 by running the following commands in a terminal.

```
cd /Library/Java/JavaVirtualMachines/
sudo rm -rf amazon-corretto-17.jdk
```
