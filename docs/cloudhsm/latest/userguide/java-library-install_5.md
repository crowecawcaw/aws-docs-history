# Install the JCE provider for AWS CloudHSM Client SDK 5

The JCE provider for AWS CloudHSM Client SDK 5 is compatible with OpenJDK 8, OpenJDK 11, OpenJDK 17, and
 OpenJDK 21. You can download both from the [OpenJDK
 website](https://openjdk.java.net/ "https://openjdk.java.net/").

Use the following sections to install and provide credentials to the provider.

###### Note

To run a single HSM cluster with Client SDK 5, you must first manage
 client key durability settings by setting
 `disable_key_availability_check` to `True`.
 For more information, see [Key
 Synchronization](manage-key-sync.md "manage-key-sync.md") and [Client SDK 5 Configure Tool](configure-sdk-5.md "configure-sdk-5.md").

###### Topics

* [Step 1: Install the JCE provider](#install-java-library_5 "#install-java-library_5")
* [Step 2: Provide credentials to the
 JCE provider](#java-library-credentials_5 "#java-library-credentials_5")

## Step 1: Install the JCE provider


1. Use the following commands to download and install the JCE provider. 



Amazon Linux 2023
Install the JCE provider for Amazon Linux 2023 on x86\_64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-latest.amzn2023.x86_64.rpm`
```


```
`$` `sudo yum install ./cloudhsm-jce-latest.amzn2023.x86_64.rpm`
```

Install the JCE provider for Amazon Linux 2023 on ARM64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-latest.amzn2023.aarch64.rpm`
```


```
`$` `sudo yum install ./cloudhsm-jce-latest.amzn2023.aarch64.rpm`
```


Amazon Linux 2
Install the JCE provider for Amazon Linux 2 on x86\_64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-latest.el7.x86_64.rpm`
```


```
`$` `sudo yum install ./cloudhsm-jce-latest.el7.x86_64.rpm`
```

Install the JCE provider for Amazon Linux 2 on ARM64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-latest.el7.aarch64.rpm`
```


```
`$` `sudo yum install ./cloudhsm-jce-latest.el7.aarch64.rpm`
```


RHEL 9 (9.2+)
Install the JCE provider for RHEL 9 (9.2+) on x86\_64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-latest.el9.x86_64.rpm`
```


```
`$` `sudo yum install ./cloudhsm-jce-latest.el9.x86_64.rpm`
```

Install the JCE provider for RHEL 9 (9.2+) on ARM64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-latest.el9.aarch64.rpm`
```


```
`$` `sudo yum install ./cloudhsm-jce-latest.el9.aarch64.rpm`
```


RHEL 8 (8.3+)
Install the JCE provider for RHEL 8 on x86\_64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-latest.el8.x86_64.rpm`
```


```
`$` `sudo yum install ./cloudhsm-jce-latest.el8.x86_64.rpm`
```


Ubuntu 24.04 LTS
Install the JCE provider for Ubuntu 24.04 LTS on x86\_64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_latest_u24.04_amd64.deb`
```


```
`$` `sudo apt install ./cloudhsm-jce_latest_u24.04_amd64.deb`
```

Install the JCE provider for Ubuntu 24.04 LTS on ARM64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_latest_u24.04_arm64.deb`
```


```
`$` `sudo apt install ./cloudhsm-jce_latest_u24.04_arm64.deb`
```


Ubuntu 22.04 LTS
Install the JCE provider for Ubuntu 22.04 LTS on x86\_64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_latest_u22.04_amd64.deb`
```


```
`$` `sudo apt install ./cloudhsm-jce_latest_u22.04_amd64.deb`
```

Install the JCE provider for Ubuntu 22.04 LTS on ARM64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_latest_u22.04_arm64.deb`
```


```
`$` `sudo apt install ./cloudhsm-jce_latest_u22.04_arm64.deb`
```


Ubuntu 20.04 LTS
Install the JCE provider for Ubuntu 20.04 LTS on x86\_64 architecture:



```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Focal/cloudhsm-jce_latest_u20.04_amd64.deb`
```


```
`$` `sudo apt install ./cloudhsm-jce_latest_u20.04_amd64.deb`
```


Windows Server
Install the JCE provider for Windows Server on x86\_64 architecture, open PowerShell as an administrator and run the following command:



```
`PS C:\>` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-latest.msi -Outfile C:\AWSCloudHSMJCE-latest.msi`
```


```
`PS C:\>` `Start-Process msiexec.exe -ArgumentList '/i C:\AWSCloudHSMJCE-latest.msi /quiet /norestart /log C:\client-install.txt' -Wait`
```
2. Bootstrap Client SDK 5. For more information about bootstrapping, see
 [Bootstrap the Client SDK](cluster-connect.md#connect-how-to "cluster-connect.md#connect-how-to").
3. Locate the following JCE provider files:



Linux


	* `/opt/cloudhsm/java/cloudhsm-`<version>`.jar`
	* `/opt/cloudhsm/bin/configure-jce`
	* `/opt/cloudhsm/bin/jce-info`

Windows


	* `C:\Program Files\Amazon\CloudHSM\java\cloudhsm-`<version>`.jar>`
	* `C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe`
	* `C:\Program Files\Amazon\CloudHSM\bin\jce_info.exe`

## Step 2: Provide credentials to the
 JCE provider


Before your Java application can use an HSM, the HSM needs to first authenticate the application. 
 HSMs authenticate using either an explicit login or implicit login method.


**Explicit login** – This method lets you provide
 AWS CloudHSM credentials directly in the application. It uses the method from the [`AuthProvider`](https://docs.oracle.com/javase/8/docs/api/java/security/AuthProvider.html "https://docs.oracle.com/javase/8/docs/api/java/security/AuthProvider.html"), where you pass a CU username and password in
 the pin pattern. For more information, see [Login to an HSM](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/sdk5/src/main/java/com/amazonaws/cloudhsm/examples/LoginRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/sdk5/src/main/java/com/amazonaws/cloudhsm/examples/LoginRunner.java") code example.


**Implicit login** – This method lets you set
 AWS CloudHSM credentials either in a new property file, system properties, or as environment
 variables.



* **System properties** – Set credentials through
 system properties when running your application. The following examples show two
 different ways that you can do this:



Linux

```
`$` `java -DHSM_USER=`<HSM user name>` -DHSM_PASSWORD=`<password>``
```


```
System.setProperty("HSM_USER","`<HSM user name>`");
System.setProperty("HSM_PASSWORD","`<password>`");
```


Windows

```
`PS C:\>` `java -DHSM_USER=`<HSM user name>` -DHSM_PASSWORD=`<password>``
```


```
System.setProperty("HSM_USER","`<HSM user name>`");
System.setProperty("HSM_PASSWORD","`<password>`");
```
* **Environment variables** – Set credentials as
 environment variables.



Linux

```
`$` `export HSM_USER=`<HSM user name>``
`$` `export HSM_PASSWORD=`<password>``
```


Windows

```
`PS C:\>` `$Env:HSM_USER="`<HSM user name>`"`
`PS C:\>` `$Env:HSM_PASSWORD="`<password>`"`
```

Credentials might not be available if the application does not provide them or if you
 attempt an operation before the HSM authenticates session. In those cases, the CloudHSM
 software library for Java searches for the credentials in the following order:



1. System properties
2. Environment variables
