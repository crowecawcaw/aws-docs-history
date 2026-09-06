

# Amazon Corretto 27 Installation Instructions for macOS 11 or later
<a name="macos-install"></a>

 This topic describes how to install and uninstall Amazon Corretto 27 on a host running the Mac OS version 11 or later. You must have administrator permissions to install and uninstall Amazon Corretto 27. 

## Install Amazon Corretto 27
<a name="macos-install-instruct"></a>

1.  Download the Mac `.pkg` file from the [Downloads](downloads-list.md) page. 

1.  Double-click the downloaded file to begin the installation wizard and follow the steps in the wizard. 

1.  Once the wizard completes, Amazon Corretto 27 is installed in `/Library/Java/JavaVirtualMachines/`. 

    You can run the following command in a terminal to get the complete installation path.   
**Example**  

   ```
   /usr/libexec/java_home --verbose
   ```

1.  Run the following command in the terminal to set the `JAVA_HOME` variable to the Amazon Corretto 27 version of the JDK. If this was set to another version previously, it is overridden.   
**Example**  

   ```
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/amazon-corretto-27.jdk/Contents/Home
   ```

## Uninstall Amazon Corretto 27
<a name="macos-uninstall"></a>

You can uninstall Amazon Corretto 27 by running the following commands in a terminal.

**Example**  

```
cd /Library/Java/JavaVirtualMachines/
sudo rm -rf amazon-corretto-27.jdk
```