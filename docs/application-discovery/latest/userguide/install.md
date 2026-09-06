

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Installing Discovery Agent
<a name="install"></a>

This page covers how to install the Discovery Agent on Linux and Microsoft Windows.

## Install Discovery Agent on Linux
<a name="install_on_linux"></a>

Complete the following procedure on Linux. Be sure that your [Migration Hub home region](https://docs.aws.amazon.com/migrationhub/latest/ug/home-region.html) has been set before you begin this procedure.

**Note**  
If you are using a non-current Linux version, see [Considerations with older Linux platforms](#old_linux).<a name="linux_steps"></a>

**To install AWS Application Discovery Agent in your data center**

1. Sign in to your Linux-based server or VM and create a new directory to contain your agent components.

1. Switch to the new directory and download the installation script from either the command line or the console.

   1. To download from the command line, run the following command.

      ```
      curl -o ./aws-discovery-agent.tar.gz https://s3.{{region}}.amazonaws.com/aws-discovery-agent.{{region}}/linux/latest/aws-discovery-agent.tar.gz
      ```

   1. To download from the Migration Hub console, do the following: 

      1. Sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/). 

      1. In the left navigation page, under **Discover**, choose **Tools**.

      1. In the **AWS Discovery Agent** box, choose **Download agents**, then choose **Download for Linux**. Your download begins immediately.

1. Verify the cryptographic signature of the installation package with the following three commands:

   ```
   curl -o ./agent.sig https://s3.{{region}}.amazonaws.com/aws-discovery-agent.{{region}}/linux/latest/aws-discovery-agent.tar.gz.sig
   ```

   ```
   curl -o ./discovery.gpg https://s3.{{region}}.amazonaws.com/aws-discovery-agent.{{region}}/linux/latest/discovery.gpg
   ```

   ```
   gpg --no-default-keyring --keyring ./discovery.gpg --verify agent.sig aws-discovery-agent.tar.gz
   ```

   The agent public key (`discovery.gpg`) fingerprint is `7638 F24C 6717 F97C 4F1B 3BC0 5133 255E 4DF4 2DA2`.

1. Extract from the tarball as shown following.

   ```
   tar -xzf aws-discovery-agent.tar.gz
   ```

1. To install the agent, choose one of the following installation methods.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/application-discovery/latest/userguide/install.html)

1. If outbound connections from your network are restricted, you'll need to update your firewall settings. Agents require access to `arsenal` over TCP port 443. They don't require any inbound ports to be open.

   For example, if your home Region is `eu-central-1`, you'd use `https://arsenal-discovery.{{eu-central-1}}.amazonaws.com:443`

### Considerations with older Linux platforms
<a name="old_linux"></a>

Some older Linux platforms such as SUSE 10, CentOS 5, and RHEL 5 are either at end of life or only minimally supported. These platforms can suffer from out-of-date cipher suites that prevent the agent update script from downloading installation packages. 

**Curl**  
The Application Discovery agent requires `curl` for secure communications with the AWS server. Some old versions of `curl` are not able to communicate securely with a modern web service.   
To use the version of `curl` included with the Application Discovery agent for all operations, run the installation script with the `-c true` parameter. 

**Certificate Authority Bundle**  
Older Linux systems might have an out-of-date Certificate Authority (CA) bundle, which is critical to secure internet communication.   
To use the CA bundle included with the Application Discovery agent for all operations, run the installation script with the `-b true` parameter.

These installation script options can be used together. In the following example command, both of the script parameters are passed to the installation script: 

```
sudo bash install -r {{your-home_region}} -k {{aws-access-key-id}} -s {{aws-secret-access-key}} -c true -b true
```

 

## Install Discovery Agent on Microsoft Windows
<a name="install_on_windows"></a>

Complete the following procedure to install an agent on Microsoft Windows. Be sure that your [Migration Hub home region](https://docs.aws.amazon.com/migrationhub/latest/ug/home-region.html) has been set before you begin this procedure.<a name="windows_steps"></a>

**To install AWS Application Discovery Agent in your data center**

1. Download the [Windows agent installer](https://s3.us-west-2.amazonaws.com/aws-discovery-agent.us-west-2/windows/latest/AWSDiscoveryAgentInstaller.exe) *but do not double-click to run the installer within Windows*.
**Important**  
Do not double-click to run the installer within Windows as it will fail to install. *Agent installation only works from the command prompt*. (If you already double-clicked on the installer, you must go to **Add/Remove Programs** and uninstall the agent before continuing on with the remaining installation steps.)   
If the Windows agent installer doesn't detect any version of the Visual C\+\+ x86 runtime on the host, it automatically installs the Visual C\+\+ x86 2015–2019 runtime before installing the agent software.

1. Open a command prompt as an administrator and navigate to the location where you saved the installation package.

1. To install the agent, choose one of the following installation methods.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/application-discovery/latest/userguide/install.html)

1. If outbound connections from your network are restricted, you must update your firewall settings. Agents require access to `arsenal` over TCP port 443. They don't require any inbound ports to be open.

   For example, if your home Region is `eu-central-1`, you'd use the following: `https://arsenal-discovery.{{eu-central-1}}.amazonaws.com:443`

### Package signing and automatic upgrades
<a name="win2003"></a>

For Windows Server 2008 and later, Amazon cryptographically signs the Application Discovery Service agent installation package with an SHA256 certificate. For SHA2-signed autoupdates on Windows Server 2008 SP2, ensure that hosts have a hotfix installed to support SHA2 signature authentication. Microsoft's latest support [hotfix](https://support.microsoft.com/en-us/topic/update-to-add-sha-2-code-signing-support-for-windows-server-2008-sp2-f120e4d0-da06-6860-3610-59c5cd0b7cd2) helps support SHA2 authentication on Windows Server 2008 SP2. 



**Note**  
The hotfixes for SHA256 support for Windows 2003 are no longer publicly available from Microsoft. If these fixes are not already installed in your Windows 2003 host, manual upgrades are necessary.

**To perform upgrades manually**

1. Download the [Windows Agent Updater](https://s3.us-west-2.amazonaws.com/aws-discovery-agent.us-west-2/windows/latest/AWSDiscoveryAgentUpdater.exe).

1. Open command prompt as an administrator.

1. Navigate to the location where the updater was saved.

1. Run the following command.

   ```
   AWSDiscoveryAgentUpdater.exe /Q
   ```