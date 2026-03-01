# Troubleshooting issues with Java transformations

The following information can help you troubleshoot common issues when transforming Java
applications with Amazon Q Developer.

###### Topics

- [Why can't Amazon Q upload my project?](#project-upload-fail "#project-upload-fail")
- [Why are my Maven commands failing?](#maven-commands-failing "#maven-commands-failing")
- [How do I add Maven to my PATH?](#add-maven-to-path "#add-maven-to-path")
- [Why can't Amazon Q build my code?](#build-fail "#build-fail")
- [Why did my transformation fail after 55 minutes?](#build-time-limit "#build-time-limit")
- [Why can’t I download my transformed code?](#download-code-fail "#download-code-fail")
- [How do I access code transformation logs?](#logs "#logs")
- [How do I find my transformation job ID?](#job-id "#job-id")

## Why can't Amazon Q upload my project?

If your project fails to upload, it’s likely due to one of the following issues. See
the topic that corresponds to the error you see from Amazon Q.

###### Topics

- [Reduce project size](#reduce-project-size "#reduce-project-size")
- [Configure proxy settings in your IDE](#configure-proxy "#configure-proxy")
- [Allow access to Amazon S3](#allowlist-s3-bucket "#allowlist-s3-bucket")

### Reduce project size

To transform your code, Amazon Q generates a project artifact, which includes your
source code, project dependencies, and build logs. The maximum project artifact size
for a transformation job is 2 GB. If you get an error related to project artifact
size, you must decrease the size of your project or try transforming a smaller
project. You can view the size of your project artifact file in the code transformation
logs. For more information, see [How do I access code transformation logs?](#logs "#logs")

### Configure proxy settings in your IDE

To transform your code, Amazon Q uploads your project artifact to a service-owned
Amazon S3 bucket. Part of the upload process involves using SSL or TLS certificates to
establish communication between Amazon S3 and your IDE. If you are using a proxy server,
the SSL or TLS certificates used by your proxy server must be trusted, otherwise
Amazon Q is not able to upload your project.

If you receive an error related to your proxy or certificates, you likely need to
configure your IDE or operating system to trust your certificates or update other
proxy settings.

###### Note

You might also encounter issues unrelated to certificates if you are behind
your organization’s proxy server or firewall. If you complete the following
procedures to configure your certificates and still have issues, contact your network
administrator to ensure you are allowed to communicate with Amazon S3 from your IDE.
For more information, see [Allow access to Amazon S3](#allowlist-s3-bucket "#allowlist-s3-bucket").

#### Configure certificates in JetBrains

To configure your JetBrains IDE Java Runtime Environment (JRE) to trust the SSL or
TLS certificates used by your proxy server, you must import the SSL or TLS
certificates to the `cacerts` file in the JRE. The `cacerts`
file is a file that contains trusted root certificates for secure connections such
as HTTPS and SSL, and it's part of the JRE's security settings. To import a
certificate, complete the following procedure.

###### Note

We recommend making a backup of the `cacerts` file before modifying
it, as any mistakes can cause issues with secure connections.

1. Determine the path to the `cacerts` file in your JRE. The path of
   the `cacerts` file in the internal JRE shipped with your JetBrains
   IDE depends on the operating system and the version of the JetBrains IDE
   you’re using.

Following are examples of paths to the `cacerts` file in common
operating systems. Choose your operating system to see examples.

###### Note

`<JetBrains Installation Folder>` refers to the directory
where JetBrains products are installed. This directory is typically chosen
during the installation process.

The `jbr` folder represents the JRE bundled with JetBrains IDEs, which is a
specific version of the JRE tailored for use with JetBrains IDEs.

Windows
The `cacerts` file path for a JetBrains IDE installed on Windows is:

```
<JetBrains Installation Folder>\jbr\bin\cacerts

```

For example, if you installed a JetBrains IDE on Windows in the default
location, the path might be:

```
C:\Program Files\JetBrains\jbr\bin\cacerts

```

macOS
The `cacerts` file path for a JetBrains IDE installed on macOS is:

```
/Applications/JetBrains Toolbox/<version>/JetBrains Toolbox.app/Contents/jbr/Contents/Home/lib/security/cacerts
```

For example, if you installed a JetBrains IDE on macOS in the default
location, the path might be:

```
/Applications/JetBrains Toolbox/2022.3.4/JetBrains Toolbox.app/Contents/jbr/Contents/Home/lib/security/cacerts

```

Linux
The `cacerts` file path for a JetBrains IDE installed on Linux is:

```
/opt/jetbrains/jbr/lib/security/cacerts

```

2. Determine the certificate you need to import to the `cacerts` file. The
   certificate file typically has a `.cer`, `.crt`, or
   `.der` file extension. If you
   aren’t sure which certificates you need to add, contact your network
   administrator.
3. Import the certificate to the `cacerts` keystore. You can do this with the
   Java `keytool` command.
   1. Open a command prompt and enter the following command:

   ```
   keytool -import -alias <alias> -file <certificate_file> -keystore <path_to_cacerts>
   ```

   2. For `<alias>`, you can add a name for the certificate
      you are importing to refer to it later. This option is optional.
   3. For `<certificate_file>`, specify the path to the
      certificate you are importing. This should be a path to the `.cer`, `.crt`, or
      `.der` file containing the certificate.
   4. For `<path_to_cacerts>`, specify the path to the
      `cacerts` keystore
      file you saved in step 1. This is the file where you are importing the
      certificate.For example, if you want to import a certificate named
      `my_certificate.cer` into the `cacerts` keystore of
      the bundled JRE in IntelliJ IDEA on Windows, and you want to
      give the alias `myalias` to the certificate, the command might
      be:

```
keytool -import -alias myalias -file my_certificate.cer -keystore "C:\Program Files\JetBrains\IntelliJ IDEA 2022.3.2\jbr\bin\cacerts"
```

4. During the import process, you'll be prompted to enter the keystore
   password. The default password for the `cacerts` keystore is
   `changeit`.
5. After running the command, you'll be asked to trust the certificate. To
   confirm the certificate is trusted and complete the import, enter `yes`.
6. You might also need to add the certificates to the IDE itself, in addition
   to the JRE. For more information, see
   [Server Certificates](https://www.jetbrains.com/help/idea/settings-tools-server-certificates.html "https://www.jetbrains.com/help/idea/settings-tools-server-certificates.html") in the JetBrains documentation.

[Show moreShow less](# "#")

#### Configure certificates in Visual Studio Code

To configure Visual Studio Code to trust the SSL or TLS certificates used by
your proxy server, make sure you have configured the following proxy
settings for your operating system.

Configure the following proxy settings for Visual Studio Code on macOS.

##### Add certificates to your macOS keychain

If you haven’t already, you must add the certificates used by your proxy
server to your macOS keychain. For information on adding
certificates to your keychain, see [Add certificates to a keychain using Keychain Access on Mac](https://support.apple.com/guide/keychain-access/add-certificates-to-a-keychain-kyca2431/mac "https://support.apple.com/guide/keychain-access/add-certificates-to-a-keychain-kyca2431/mac") in the
Keychain Access User Guide.

##### Install the Mac CA VSCode extension

The
[Mac CA VSCode extension](https://marketplace.visualstudio.com/items?itemName=linhmtran168.mac-ca-vscode "https://marketplace.visualstudio.com/items?itemName=linhmtran168.mac-ca-vscode") allows Amazon Q to access the certificates you added to Keychain Access on your Mac.

To install the extension:

1. Search for `mac-ca-vscode` in the VS Code extensions pane, and choose
   **Install**.
2. Restart VS Code.

##### Update proxy settings in VS Code on macOS

Update the following settings to make sure VS Code is configured properly
for your proxy.

1. Open settings in VS Code.
2. Enter `proxy` in the search bar.
3. In the **Http: Proxy** field, add your proxy URL.
4. Deselect **Http: Proxy Strict SSL**.
5. In the **Http: Proxy Support** dropdown list, choose **on**.
6. In the settings search bar, enter
   `http.experimental.systemCertificatesV2`. Select
   **Http › Experimental: System Certificates V2**.

Configure the following proxy settings for Visual Studio Code on Windows.

##### Add certificate as a trusted root certificate on Windows

If you haven't already, you must add the certificates used by your proxy
server to your Trusted Root Certification Authorities store on Windows. To add a certificate,
complete the following procedure:

1. Open the search tool or a Run command window.
2. Enter the following to open the Certificate Manager tool:

```
certmgr.msc
```

3. Choose the **Trusted Root Certification Authorities** store.
4. Right-click
   **Certificates**, choose
   **All Tasks**, and then choose **Import...**.
5. Follow the instructions given to import your proxy certificate.
6. After you've imported your certificate, confirm the certificate was
   added.

In the **Trusted Root Certification
Authorities** store, double click
**Certificates**. Right-click the certificate
you added and choose **Properties**. Under
**Certificate purposes**, the option
**Enable all purposes for this certificate**
should be selected.

##### Install the Win-CA VSCode extension

The [Win-CA VSCode extension](https://marketplace.visualstudio.com/items?itemName=ukoloff.win-ca "https://marketplace.visualstudio.com/items?itemName=ukoloff.win-ca") allows Amazon Q to access the certificates
you added to Trusted Root Certificates in Windows.

To install the extension:

1. Search for `win-ca` in the VS Code settings pane.
2. In the **Inject** dropdown list, choose **append**.

##### Update proxy settings in VS Code on Windows

Update the following settings to make sure VS Code is configured properly
for your proxy.

1. Open settings in VS Code.
2. Enter `proxy` in the search bar.
3. In the **Http: Proxy** field, add your proxy URL.
4. Deselect **Http: Proxy Strict SSL**.
5. In the **Http: Proxy Support** dropdown list, choose **on**.
6. In the settings search bar, enter
   `http.experimental.systemCertificatesV2`. Select
   **Http › Experimental: System Certificates V2**.
7. Restart VS Code.

### Allow access to Amazon S3

During a transformation, Amazon Q
uploads your code to a service-owned Amazon S3 bucket. If your network or
organization hasn’t configured access to Amazon S3, Amazon Q isn’t able to upload
your project.

To ensure Amazon Q can upload your project, make sure your proxy configuration and
other network components, such as Data Lost Prevention (DLP) policies, are configured
to allow access to Amazon S3. You might also need to allowlist the Amazon S3 bucket where
Amazon Q uploads your project. For more information, see [Amazon S3 bucket URLs and ARNs to allowlist](firewall.md#data-perimeters "firewall.md#data-perimeters").

If you transform a large project, DLP policies or other network components might
cause delays and prevent a successful upload if they aren’t configured to allowlist
the Amazon S3 bucket. If you choose not to allowlist the bucket, you might need to
transform a smaller project so that Amazon Q can upload it.

## Why are my Maven commands failing?

Following are Maven configuration issues that you might see in the JetBrains and Visual Studio Code
IDEs. If you address the issues and still see Maven errors, there might be an issue with
your project. Use the information in the error logs to address any issues with your
project, and then try transforming your project again.

### Update Maven configuration in JetBrains

If a transformation fails in JetBrains due to Maven command issues, the error logs
appear on the **Run** tab. Use the information in the logs to
address the issue. Following are some issues that you might need to address:

- Make sure that your Maven home path is set to **Bundled**.
  Go to **Settings**, and then expand the **Build,
  Execution, Deployment** section. Expand the **Build
  Tools** section and then expand **Maven**. In the
  **Maven home path** dropdown list, choose
  **Bundled**.
- Make sure that the Java runtime environment (JRE) is using
  your project JDK. Go to **Settings**, and then expand the
  **Build, Execution, Deployment** section. Expand
  **Maven** and choose **Runner**. In the
  **JRE** dropdown list, choose **Use Project
  JDK**.
- Make sure that Maven is enabled. Go to **Settings** and
  choose **Plugins**. Search for Maven and choose the Maven
  plugin. If you see an **Enable** button, choose it to enable
  Maven.

### Update Maven configuration in Visual Studio Code

If a transformation fails in VS Code because of Maven command issues, a text
file that contains the error logs opens in a new tab. Use the information in the logs
to address the issue.

Make sure that you have configured either one of the following options:

- Your project contains a Maven wrapper in the project root folder
- A version of Maven supported by Amazon Q is available on your
  `PATH`

For more information, see [How do I add Maven to my PATH?](#add-maven-to-path "#add-maven-to-path")

## How do I add Maven to my `PATH`?

To transform your code in VS Code without using a Maven wrapper, you must install
Maven and add it to your `PATH` variable.

To check if you have Maven installed correctly already, run `mvn -v` in a
new OS terminal outside of Visual Studio Code. You should see an output with your Maven version.

If you get an output in your Visual Studio Code terminal but not in your OS terminal, or if the
command isn't found, you need to add Maven to your `PATH`.

To add Maven to your `PATH`, follow the instructions for your
machine.

macOS
To add Maven to your macOS `PATH`, complete the following
steps.

1. Locate your Maven installation directory, or the folder where you
   installed Maven, and save the path to that folder.
2. Open the configuration file for your shell in an editor of your
   choice. For recent macOS versions, the default shell is `zsh`
   and the default configuration file is located at `~/.zshrc`.

Add the following lines to the bottom of the configuration file. Set
the value of `M2_HOME` to the path you saved in step 1:

```
export M2_HOME="your Maven installation directory"
export PATH="${M2_HOME}/bin:${PATH}"
```

These commands make the `mvn` command available in all
terminals. 3. Close all OS terminal windows and quit all Visual Studio Code instances. 4. To verify that Maven was added to your `PATH`, open a new
OS terminal and run the following command:

```
mvn -v
```

You should see an output with your Maven version. 5. After seeing your Maven output, restart Visual Studio Code. You might also need to
restart your machine. Open a new Visual Studio Code terminal and run the following
command:

```
mvn -v
```

The output should be identical to the output in step 4. If the Visual Studio Code
output is different, try the following to make sure your setup is
correct:

    * Check your `PATH` variable in Visual Studio Code. An IDE extension
     might be altering the `PATH` such that it differs from
     your local `PATH` variable. Uninstall the extension to
     remove it from your `PATH`.
    * Check your default shell in Visual Studio Code. If it's set to something
     other than `zsh`, repeat these steps for your
     shell.

Windows
To add Maven to your Windows
`PATH`, complete the following steps:

1. Locate your Maven installation directory, or the folder where you
   installed Maven, and save the path to that folder.
2. Open the Environment Variables window:
   1. Choose the Windows button to open the search
      bar.
   2. Enter `Edit environment variables for your account`
      and choose it.

3. In the **Environment Variables** window, look for the
   Path variable. If you have a Path variable already, choose
   **Edit...** to update it. If you don't see a Path
   variable, choose **New...** to add one.
4. In the **Edit environment variable** window that
   appears, double click the existing path to edit it, or choose
   **New** to add a new path entry.

Replace the existing Maven path entry with the path you saved in step
1, or add the path as a new entry. At the end of the path, add
`\bin` as a suffix, as in the following example:

```
C:\Users\yourusername\Downloads\apache-maven-3.9.6-bin\apache-maven-3.9.6\bin
```

5. Choose **OK** to save the path entry, and then choose
   **OK** again in the **Environment
   Variables** window.
6. Open a new Command Prompt and run the following command:

```
mvn -v
```

You should see an output with your Maven version.

## Why can't Amazon Q build my code?

If the transformation fails when Amazon Q is building your code, your project may not be
configured properly for the environment where Amazon Q builds your code. You might need
to update your build configuration or code implementation.

Review the build log output Amazon Q provides to determine if there are changes you
can make to your project. Following are some common issues that might prevent Amazon Q
from building your code.

### Remove absolute paths in pom.xml

If you have an absolute path in your pom.xml file, Amazon Q won’t be able to find
the relevant files, and as a result might not be able to build your code.

Following is an example of an absolute path that you could have in your `pom.xml` file:

```
<toolspath>
    <path>/Library/Java/JavaVirtualMachines/jdk-11.0.11.jdk/Contents/Home/lib/tools.jar</path>
</toolspath>
```

Instead of using an absolute path, you can create a relative path using a pointer.
Following is an example of how you can replace the previous absolute path with a
relative path:

```
<toolspath>
    <path>${java.home}/../lib/tools.jar</path>
</toolspath>
```

### Remove local or external databases in unit tests

Amazon Q runs any unit tests in your project when it builds your code. If a unit
test calls a local or external database, Amazon Q won’t have access to the database,
causing the build to fail. To prevent the build from failing, you must either remove
the database call from the unit test or remove the unit test before submitting the
transformation.

## Why did my transformation fail after 55 minutes?

If your code transformation job fails after 55 minutes, your code build time likely
exceeds the build time limit. There is currently a time limit of 55 minutes for building
your code.

If your local build time takes 55 minutes or longer, reduce your project’s build time
to transform your code. If your local build is faster than the build with Code
Transformation, check your project for tasks that might be failing or take a longer time
in a different environment. Consider disabling long-running test cases. Also consider
using timeouts for attempts to access resources that might not be available from the
secure IDE environment or the internet.

## Why can’t I download my transformed code?

If you aren’t able to download your code after your
transformation is complete, it’s likely due to one of the following issues. See the
topic that corresponds to the error you see from Amazon Q.

###### Topics

- [Reduce project size](#reduce-project-size-output "#reduce-project-size-output")
- [Download code diff within 30 days](#download-30-hrs "#download-30-hrs")
- [Configure proxy settings in your IDE](#configure-proxy-download "#configure-proxy-download")
- [Remove wildcard characters in JetBrains proxy settings](#remove-wildcard "#remove-wildcard")

### Reduce project size

After the transformation is complete, Amazon Q generates an output artifact that
contains a diff with your upgraded code and a transformation summary with information
about the changes it made. The output artifact must be 1 GB or less in order for the
IDE to download it.

If the output artifact exceeds the limit, you will not be able to download your
upgraded code or transformation summary. Try transforming a smaller project to
prevent a large output artifact. If the issue persists, contact Support. For
information about contacting Support with Amazon Q, see
[Using Amazon Q Developer to chat with Support](support-chat.md "support-chat.md").

### Download code diff within 30 days

The code diff file with your upgraded code is only available for 30 days after the transformation is
complete. If it’s been over 30 days since the transformation completed, restart the
transformation to download the diff file.

### Configure proxy settings in your IDE

Amazon Q downloads your upgraded code from a service-owned Amazon S3 bucket.
Part of the download process involves using SSL or TLS certificates to establish
communication between Amazon S3 and your IDE. If you are using a proxy server, the SSL or
TLS certificates used by your proxy server must be trusted, otherwise Amazon Q is not
able to upload your project.

To download your code, you might need to configure your IDE to trust certificates or
update other proxy settings. For more information on updating your proxy settings,
see [Configure proxy settings in your IDE](#configure-proxy "#configure-proxy").

### Remove wildcard characters in JetBrains proxy settings

If you have configured proxy settings in your JetBrains IDE, you might see the
following error when downloading your upgraded code:

```
software.amazon.awssdk.core.exception.SdkClientException:
Unable to execute HTTP request: Dangling meta character '*' near index 0
```

This is likely caused by the presence of a wildcard character (\*) in the **No proxy
for** field of your IDE's proxy settings. The Java SDK used by Amazon Q
doesn't support wildcard entries in this field.

To download your code, remove any wildcards from the **No proxy
for** field, and then restart your IDE. If you need to specify hosts that
should bypass the proxy, use a regular expression instead of a wildcard. To update
proxy settings in your JetBrains IDE, see [HTTP
Proxy](https://www.jetbrains.com/help/idea/settings-http-proxy.html "https://www.jetbrains.com/help/idea/settings-http-proxy.html") in the JetBrains documentation.

## How do I access code transformation logs?

### Access logs in JetBrains

For information about how to access JetBrains log files, see [Locating IDE log files](https://intellij-support.jetbrains.com/hc/en-us/articles/207241085-Locating-IDE-log-files "https://intellij-support.jetbrains.com/hc/en-us/articles/207241085-Locating-IDE-log-files") in the JetBrains documentation.

To find logs emitted by Amazon Q in JetBrains, search the IDE logs for the
following string:

```
software.aws.toolkits.jetbrains.services.codemodernizer
```

Code transformation logs start with the preceding string. Logs generated
by Maven are displayed on the **Run** tab and have the preceding string
before and after the log entry.

### Access logs in Visual Studio Code

To find logs emitted by Amazon Q in VS Code, complete the following
steps:

1. Choose **View** in the top navigation bar, and then choose
   **Command Palette**.
2. Search `Amazon Q: View Logs` in the command palette that
   appears.
3. The logs open in the IDE. To search the log files for
   `CodeTransformation`, use `CMD + F` or `Control +
F`.

Code transformation logs in VS Code are prefixed with
`CodeTransformation:`. Following is an example of a log generated in
VS Code for a Maven copy dependencies error:

```
2024-02-12 11:29:16 [ERROR]: CodeTransformation: Error in running Maven copy-dependencies command mvn = /bin/sh: mvn: command not found
```

## How do I find my transformation job ID?

### Find your job ID in JetBrains

To find a transformation job ID in JetBrains, go to the **Transformation
details** tab in the **Transformation Hub** and choose the
**Show Job Status** (clock) icon.

### Find your job ID in Visual Studio Code

To find a transformation job ID in VS Code, go to the **Transformation
Hub** and choose the **Show Job Status** (clock) icon.
