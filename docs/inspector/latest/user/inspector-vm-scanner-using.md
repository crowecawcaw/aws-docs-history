

# Manual installation and configuration
<a name="inspector-vm-scanner-using"></a>

 This section describes how to manually install and configure Inspector VM Scanner on your Amazon EC2 instances. Manual installation is considered *agent-based scanning* and does not require Amazon EC2 Systems Manager (SSM). 

**Note**  
 If you enable Enhanced EC2 Scanning in the Amazon Inspector console, Amazon Inspector automatically installs and manages the VM Scanner using SSM. Manual installation is only required if you cannot use SSM or prefer to manage the scanner independently. 

## Manually installing and uninstalling Inspector VM Scanner
<a name="inspector-vm-scanner-manual-install"></a>

 Inspector VM Scanner is available for standalone installation through the following links: 


**Inspector VM Scanner packages**  

| **Package Type** | **Architecture** | **URL** | 
| --- | --- | --- | 
| .apk | ARM | https://inspector-vm-scanner.s3.amazonaws.com/latest/APK-ARM/inspector-vm-scanner-latest-r0.apk | 
|  | X86\_64 | https://inspector-vm-scanner.s3.amazonaws.com/latest/APK-X86\_64/inspector-vm-scanner-latest-r0.apk | 
| .deb | ARM | https://inspector-vm-scanner.s3.amazonaws.com/latest/DEB-ARM/inspector-vm-scanner\_latest\_arm64.deb | 
|  | X86\_64 | https://inspector-vm-scanner.s3.amazonaws.com/latest/DEB-X86\_64/inspector-vm-scanner\_latest\_amd64.deb | 
| .msi | X86\_64 | https://inspector-vm-scanner.s3.amazonaws.com/latest/MSI-X86\_64/inspector-vm-scanner-x86\_64-latest.msi | 
| .pkg | ARM | https://inspector-vm-scanner.s3.amazonaws.com/latest/PKG-ARM/inspector-vm-scanner.latest.arm64.pkg | 
| .rpm | ARM | https://inspector-vm-scanner.s3.amazonaws.com/latest/RPM-ARM/inspector-vm-scanner-latest.arm64.rpm | 
|  | X86\_64 | https://inspector-vm-scanner.s3.amazonaws.com/latest/RPM-X86\_64/inspector-vm-scanner-latest.x86\_64.rpm | 

 To view the procedure for manually installing Inspector VM Scanner on the specified package manager, choose a link from the following list: 
+ [APK](#inspector-vm-scanner-apk)
+ [DEB](#inspector-vm-scanner-deb)
+ [MSI](#inspector-vm-scanner-msi)
+ [PKG](#inspector-vm-scanner-pkg)
+ [RPM](#inspector-vm-scanner-rpm)

### APK
<a name="inspector-vm-scanner-apk"></a>

#### Installation
<a name="inspector-vm-scanner-apk-install"></a>

 **ARM** 

```
curl --output-dir /etc/apk/keys -O https://inspector-vm-scanner.s3.amazonaws.com/latest/APK-ARM/inspector-vm-scanner.pem.pub
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/APK-ARM/inspector-vm-scanner-latest-r0.apk
apk add inspector-vm-scanner-latest-r0.apk
```

 **X86\_64** 

```
curl --output-dir /etc/apk/keys -O https://inspector-vm-scanner.s3.amazonaws.com/latest/APK-X86_64/inspector-vm-scanner.pem.pub
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/APK-X86_64/inspector-vm-scanner-latest-r0.apk
apk add inspector-vm-scanner-latest-r0.apk
```

#### Uninstallation
<a name="inspector-vm-scanner-apk-uninstall"></a>

```
apk del inspector-vm-scanner
```

### DEB
<a name="inspector-vm-scanner-deb"></a>

#### Installation
<a name="inspector-vm-scanner-deb-install"></a>

 **ARM** 

```
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/DEB-ARM/inspector-vm-scanner.gpg.pub
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/DEB-ARM/inspector-vm-scanner_latest_arm64.deb
gpg --import inspector-vm-scanner.gpg.pub
gpg --verify inspector-vm-scanner_latest_arm64.deb
sudo dpkg -i inspector-vm-scanner_latest_arm64.deb
```

 **X86\_64** 

```
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/DEB-X86_64/inspector-vm-scanner.gpg.pub
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/DEB-X86_64/inspector-vm-scanner_latest_amd64.deb
gpg --import inspector-vm-scanner.gpg.pub
gpg --verify inspector-vm-scanner_latest_amd64.deb
sudo dpkg -i inspector-vm-scanner_latest_amd64.deb
```

#### Uninstallation
<a name="inspector-vm-scanner-deb-uninstall"></a>

```
sudo dpkg -r inspector-vm-scanner
```

### MSI
<a name="inspector-vm-scanner-msi"></a>

#### Installation
<a name="inspector-vm-scanner-msi-install"></a>

 **X86\_64** 

```
Invoke-WebRequest https://inspector-vm-scanner.s3.amazonaws.com/latest/MSI-X86_64/inspector-vm-scanner-x86_64-latest.msi -OutFile inspector-vm-scanner-x86_64-latest.msi
msiexec /i inspector-vm-scanner-x86_64-latest.msi /qn
```

#### Uninstallation
<a name="inspector-vm-scanner-msi-uninstall"></a>

 To uninstall Inspector VM Scanner on Windows, use the Windows Programs and Features control panel or the following PowerShell command: 

```
Get-WmiObject -Class Win32_Product | Where-Object {$_.Name -eq "Inspector VM Scanner"} | ForEach-Object {$_.Uninstall()}
```

### PKG
<a name="inspector-vm-scanner-pkg"></a>

#### Installation
<a name="inspector-vm-scanner-pkg-install"></a>

 **ARM** 

```
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/PKG-ARM/inspector-vm-scanner.latest.arm64.pkg
pkgutil --check-signature inspector-vm-scanner.latest.arm64.pkg
sudo installer -pkg inspector-vm-scanner.latest.arm64.pkg -target /
```

#### Uninstallation
<a name="inspector-vm-scanner-pkg-uninstall"></a>

```
sudo rm /opt/aws/inspector/bin/inspector-vm-scanner
sudo rm -rf /var/lib/amazon/inspector
```

### RPM
<a name="inspector-vm-scanner-rpm"></a>

#### Installation
<a name="inspector-vm-scanner-rpm-install"></a>

 **ARM** 

```
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/RPM-ARM/inspector-vm-scanner.gpg.pub
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/RPM-ARM/inspector-vm-scanner-latest.arm64.rpm
rpm --import inspector-vm-scanner.gpg.pub
rpm --checksig inspector-vm-scanner-latest.arm64.rpm
sudo yum install inspector-vm-scanner-latest.arm64.rpm
```

 **X86\_64** 

```
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/RPM-X86_64/inspector-vm-scanner.gpg.pub
curl -O https://inspector-vm-scanner.s3.amazonaws.com/latest/RPM-X86_64/inspector-vm-scanner-latest.x86_64.rpm
rpm --import inspector-vm-scanner.gpg.pub
rpm --checksig inspector-vm-scanner-latest.x86_64.rpm
sudo yum install inspector-vm-scanner-latest.x86_64.rpm
```

#### Uninstallation
<a name="inspector-vm-scanner-rpm-uninstall"></a>

```
sudo yum remove inspector-vm-scanner
```

## Installation paths
<a name="inspector-vm-scanner-installation-paths"></a>

 On all Unix-based operating systems (including macOS), Inspector VM Scanner installs to `/opt/aws/inspector/bin/inspector-vm-scanner`. The exception is Alpine-based operating systems (including Chainguard), which use the alternate path `/usr/opt/aws/inspector/bin/inspector-vm-scanner`. 

 On Windows, Inspector VM Scanner installs to `C:\Program Files\Amazon\Inspector\inspector-vm-scanner.exe`. 

 These installation paths (aside from Alpine) are identical to Inspector SSM Plugin, which stores all Inspector binaries in a single location. 

## Uninstalling Inspector VM Scanner
<a name="inspector-vm-scanner-uninstalling"></a>

 If you disable Enhanced EC2 Scanning, Inspector automatically uninstalls Inspector VM Scanner on all Inspector-managed instances. To remove a manual installation, see the uninstallation instructions for your package manager in the preceding sections. 

## Running Inspector VM Scanner
<a name="inspector-vm-scanner-running"></a>

 Inspector VM Scanner expects a **Scan Type** to be passed as the first parameter. At this time, the only supported value is `sbom`. 

 Default usage command: 

```
./inspector-vm-scanner sbom --send-results telemetry
```

 Print options for SBOM scan: 

```
./inspector-vm-scanner sbom --help
```

## Viewing output
<a name="inspector-vm-scanner-viewing-output"></a>

 The default Inspector workflow does not save an SBOM locally. However, if any failures occur with sending the resource SBOM through telemetry, it will be written to the following locations: 
+ `/var/lib/amazon/inspector/state/sbom.json` on Unix
+ `C:\ProgramData\Amazon\Inspector\State\sbom.json` on Windows

 Users can override this path during VM Scanner invocation. See [Advanced configuration](inspector-vm-scanner-advanced-config.md) for more details. 