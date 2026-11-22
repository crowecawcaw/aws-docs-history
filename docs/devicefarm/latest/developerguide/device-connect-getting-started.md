

# Installing Device Connect and attaching a device

With Device Connect for AWS Device Farm, most Android Debug Bridge (adb) workflows need no change. Device Connect runs a bridge in the background. The bridge takes the place of your local adb server.

Cost: Device Farm bills each device minute of the remote access session until you stop it. Device Connect adds no charge. For more information, see [Device Farm pricing](https://aws.amazon.com/device-farm/pricing/).

**Topics**
+ [Prerequisites](#device-connect-prerequisites)
+ [Step 1: Install Device Connect](#device-connect-install)
+ [Step 2: Create a remote access session](#device-connect-create-session)
+ [Step 3: Attach the device and run adb](#device-connect-attach-device)
+ [Step 4: Clean up](#device-connect-clean-up)
+ [Next steps](#device-connect-next-steps)

## Prerequisites
<a name="device-connect-prerequisites"></a>

Before you start, make sure that you have the following:
+ An AWS account, and credentials for it on your computer. Device Connect uses the default AWS credential chain, such as environment variables, a named profile, or an IAM Identity Center (SSO) profile. The bridge reads the credentials of the shell that starts it. For more information, see [Authentication and access credentials for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html).
+ AWS Identity and Access Management (IAM) permissions for Device Farm. Device Connect needs only `devicefarm:GetRemoteAccessSession` on the sessions that you attach. To create and stop a session, you also need actions such as `devicefarm:CreateRemoteAccessSession` and `devicefarm:StopRemoteAccessSession`. For more information, see [Identity and access management in AWS Device Farm](security-iam.md).
+ The AWS CLI, to create and stop sessions. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ Android SDK Platform-Tools 29.0.0 or later. The `adb version` command must print `Android Debug Bridge version 1.0.41`, because other adb versions can't connect through the bridge. For more information, see [SDK Platform Tools release notes](https://developer.android.com/tools/releases/platform-tools) on the Android Developers website.

  Put the `platform-tools` folder on your `PATH`, so that `adb version` works in a new terminal.
+ A computer that runs macOS 13 or later, Linux, or Windows 10 or later. For the supported versions and architectures, see [Supported operating systems](device-connect-support.md#device-connect-supported-platforms).

## Step 1: Install Device Connect
<a name="device-connect-install"></a>

Device Connect is a command-line tool, `devicefarm-connect`. You can install it in two ways. The install script downloads the release file for your computer, verifies it, and installs it. Or you download the release file yourself, and then verify and install it.

### Option 1: Install with the script
<a name="device-connect-install-script"></a>

On macOS or Linux, run the following command in a terminal.

```bash
curl -fsSL https://github.com/aws/device-connect-devicefarm/releases/latest/download/install.sh | sh
```

On Windows, run the following command in PowerShell.

```powershell
irm https://github.com/aws/device-connect-devicefarm/releases/latest/download/install.ps1 | iex
```

The script checks the SHA-256 checksum of the release file, the Authenticode signature on Windows, and the Apple signature and notarization on macOS. With `gpg` and `gpgv` on your computer, the script also checks the signature of the checksum list. Without them, the script says that it skips this check. If a check fails, the script installs nothing.

The script needs no administrator rights. It installs `devicefarm-connect` in `~/.local/bin` on macOS and Linux, and in `%USERPROFILE%\.local\bin` on Windows. If the folder is not on your `PATH`, the script prints how to add it. To use another folder, first set the `DEVICEFARM_CONNECT_INSTALL_DIR` environment variable. On macOS and Linux, run `export DEVICEFARM_CONNECT_INSTALL_DIR={{folder}}`. In PowerShell, run `$env:DEVICEFARM_CONNECT_INSTALL_DIR = '{{folder}}'`.

The script is a plain text file. To read it before you run it, download it first. On macOS or Linux, run the following commands.

```bash
curl -fsSLO https://github.com/aws/device-connect-devicefarm/releases/latest/download/install.sh
less install.sh
```

In PowerShell, run the following commands.

```powershell
irm https://github.com/aws/device-connect-devicefarm/releases/latest/download/install.ps1 -OutFile install.ps1
notepad install.ps1
```

After you read the file, run it. On macOS or Linux, run `sh install.sh`. In PowerShell, run `Get-Content -Raw .\install.ps1 | iex`.

To install a specific version, use `releases/download/v{{X.Y.Z}}` in each URL instead of `releases/latest/download`.

To confirm the installation, run `devicefarm-connect --version`.

### Option 2: Install manually
<a name="device-connect-install-manual"></a>

The following steps do by hand what the install script does for you: download the release file, verify it, and install it.

On the [Device Connect Releases page](https://github.com/aws/device-connect-devicefarm/releases) on the GitHub website, choose a release. Download `SHA256SUMS`, `SHA256SUMS.sig`, and one of the following files from that release into the same directory. On Linux, `uname -m` prints the architecture.
+ macOS, Apple silicon or Intel: `devicefarm-connect_darwin_universal`
+ Linux, x86-64 (`x86_64`): `devicefarm-connect_linux_amd64`
+ Linux, ARM64 (`aarch64`): `devicefarm-connect_linux_arm64`
+ Windows, x86-64: `devicefarm-connect_windows_amd64.exe`

Then verify the files and install the program, as the following sections describe.

#### Verify your download
<a name="device-connect-verify-download"></a>

`SHA256SUMS` lists the SHA-256 checksum of every file in the release. `SHA256SUMS.sig` is the signature of that list. A good signature proves that the list comes from Device Farm. A matching checksum proves that your file is on the list. If a check fails, don't run the file. The list uses the original file names, so do both checks before you rename the file.

To check the signature, you need GNU Privacy Guard (GnuPG). Most Linux distributions include it. For macOS and Windows, see [GnuPG downloads](https://gnupg.org/download/) on the GnuPG website. On Windows, GnuPG is optional, because the Authenticode signature also proves who signed the file. On Windows without GnuPG, skip the next procedure and go to the Windows tab.

Use the following public key to check the signature. Its user ID is `Device Connect for AWS Device Farm <aws-devicefarm-support@amazon.com>`.

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

xsFNBGr8hMwBEACQTMhDZ0tuEkysoiZZXcCquLJKlbuVP4rUFKSi4qofc3TlMk2g
Q1DjMsSknZhBg+oYFxXWvhbr43WK8TL7sv9LlEAUR4jZzKQqpmCLqMc6uxEX6tuX
tuob3N6iEe6ODo1WG5XTvJCuHF6w+2al8pVVpJ+rkPHchTTqr2DM3z4SBBTPzPNG
5YLYtOx4+Ezah73Rk8eDF19WZYa0V6ROlPMkMW1As6mSlXJZ0zdueiICwBee7k1Q
wzdFfbGMDws25sMAuXEJDDBKmAsjCUK8l9okBkZryCuJ5y8bApEwWHNNtqCHIZr2
nfLCqu8nvTPpQRa8ls9QF0SULHqeDYuQ3SXZVRnwp0q2LvneV0yz4llEQhhoIMc4
iACJl8lbYzQT5TECbebtV3BaxxPmtQPxbr7pYIwqJJbsuAVuDr6OiggUXI2pNykf
RY5Px+dKdaxlZUeZhR7Ws5FZF52McMLwZQbqcOaGb1VyQpT7VgnSrvUUVxRZowOj
VKgGJbir4eOtdil0azRtvA15gO5jkFRy0Yx9WpD1h9pwnUxfUR3ywpnCroeiWZ8o
8fHozYyHm/4t8pcwH6Tzuhc9ggBdzdGVyn1Jp4vnMWPfspMJqTR6COOyeosCU+8d
vpxc8xtNdbZswirqfkz+pq/h3EqL/c72N8oKRsPJkXjOJi4dkfWbOVgQ8QARAQAB
zUZEZXZpY2UgQ29ubmVjdCBmb3IgQVdTIERldmljZSBGYXJtIDxhd3MtZGV2aWNl
ZmFybS1zdXBwb3J0QGFtYXpvbi5jb20+wsG+BBMBCgByBYJq/lh5CRAjauf/+g0I
bkcUAAAAAAAeACBzYWx0QG5vdGF0aW9ucy5zZXF1b2lhLXBncC5vcmelZsyeD18R
C6+TbEYMAOqoWPoQosEmqdc8WWm3sTPW4QKbAxYhBEkslsCDiTyWC6SG3iNq5//6
DQhuAAD/cw/+MTRDSXrUfRl7k2LOcHuezQ8wOLg96+Yr2y/uTlELpsvrRAxmT/Il
Y8ma6h9mgy5Xk+VlbrOY9FPD5HN4a3j0IHrCJFX0ruUyUgus6lf+GejNwkXh2/Z/
qwDJDPcOAHLm6f/jvcFxK8DnTEG4ZfkWgXH7Epqok4nAzmdrvDHTnCLDsQj/4gi7
RjSQsD0OdGMr3X9kaGLEvNibwpUUvXcQd2WCerW3OOIWbs+ruW8SyHzYQcWsat6N
mAmhVqp0q0HOVDJ0Tr4vXRISXbZ4KpDXbOaIAeHzTauR+RRJehz7ZoWQA+QcT062
r+goT7WI691VCYGlo3UdC8Hkroo4490Hp2RE/pMRbIv7v71lKd60/pQ9IhB1vuI5
16SNtFsFosx1pg88AGW/f6HtAwI2Iowrl2EQqX9Wa5+7R2uArIdT35P0jXFY3mAt
p1RStDtSbiKdyOQVwZZ710tEh6gp0C+psSpVtuoTHcnFJXjRDujMZAVxWddCrW8Y
J37f5H0FQrbQGJLJxptkJgrggVWVWUbe7DBRqqZLL2AD3q1OTyVD9eby2m0mOAu5
/HVcBBtT85iuSF1Ie+FVcimK4WWODnKuA/yTRsEnw7sjNx7U48EEEfunsmEtncxB
Rrqtp8537D/2lxbsri9Zb1p4kHHcQJ6Gs/f3v2sJ2lqdRUpW+39r4L0=
=w0bv
-----END PGP PUBLIC KEY BLOCK-----
```

The fingerprint of this key is `492C 96C0 8389 3C96 0BA4 86DE 236A E7FF FA0D 086E`. The release notes list the same fingerprint.

**To check the signature of the checksum list**

1. Copy the key block above, paste it into a new plain text file, and save the file as `release-key.asc` in the directory that holds your downloads.

1. Convert the key to a keyring file. The command prints nothing.

   ```bash
   gpg --dearmor -o release-key.gpg release-key.asc
   ```

1. Check the signature. On macOS and Linux, run the following command. `LC_ALL=C` makes `gpgv` print its English messages.

   ```bash
   LC_ALL=C gpgv --keyring ./release-key.gpg SHA256SUMS.sig SHA256SUMS
   ```

   The output must contain `Good signature from`.

   ```
   gpgv: Good signature from "Device Connect for AWS Device Farm <aws-devicefarm-support@amazon.com>"
   ```

   On Windows, `gpgv` can print its messages in your language, so check its exit code instead. Run the following commands in PowerShell. The second command must print `0`.

   ```powershell
   gpgv --keyring ./release-key.gpg SHA256SUMS.sig SHA256SUMS
   $LASTEXITCODE
   ```

   If PowerShell can't find `gpgv`, the exit code proves nothing. Install GnuPG, open a new PowerShell window, and run the commands again.

Then check your file. Choose the tab for your operating system.

------
#### [ macOS ]

**To verify the file on macOS**

1. Compare the file with its line in the list.

   ```bash
   grep ' devicefarm-connect_darwin_universal$' SHA256SUMS | shasum -a 256 -c -
   ```

   The output must end with `OK`.

   ```
   devicefarm-connect_darwin_universal: OK
   ```

   If not, make sure that the file is in this directory under its original name. If the check still fails, delete the file and download it again.

1. Print the Apple signature of the file.

   ```bash
   codesign -dv --verbose=4 devicefarm-connect_darwin_universal
   ```

   The first `Authority=` line must be `Authority=Developer ID Application: AMZN Mobile LLC (94KV3E626L)`, and the `TeamIdentifier=` line must be `TeamIdentifier=94KV3E626L`.

1. Check that Apple notarized the file.

   ```bash
   codesign --verify --verbose=2 -R="notarized" --check-notarization devicefarm-connect_darwin_universal
   ```

   The output must end with `explicit requirement satisfied`.

   ```
   devicefarm-connect_darwin_universal: explicit requirement satisfied
   ```

   If it doesn't, make sure that your Mac is online, and run the command again.

------
#### [ Linux ]

**To check the checksum on Linux**
+ Compare the file with its line in the list. For ARM64, use `devicefarm-connect_linux_arm64` in the `grep` pattern.

  ```bash
  grep ' devicefarm-connect_linux_amd64$' SHA256SUMS | LC_ALL=C sha256sum -c -
  ```

  The output must end with `OK`.

  ```
  devicefarm-connect_linux_amd64: OK
  ```

  If not, make sure that the file is in this directory under its original name. If the check still fails, delete the file and download it again.

------
#### [ Windows ]

**To verify the file on Windows**

1. In PowerShell, print the Authenticode signature of the file.

   ```powershell
   Get-AuthenticodeSignature .\devicefarm-connect_windows_amd64.exe | Format-List Status, StatusMessage, SignerCertificate, TimeStamperCertificate
   ```

   Check the output for all of the following. If one check fails, stop. Don't run the file.
   + `Status` is `Valid`.
   + In the subject of `SignerCertificate`, `O` is `Amazon Web Services, Inc.` and `OU` is `AWS Dev Tools`. PowerShell prints the `O` value in double quotes.
   + `TimeStamperCertificate` is not empty.

1. Compare the file with its line in the list.

   ```powershell
   $hash = (Get-FileHash .\devicefarm-connect_windows_amd64.exe -Algorithm SHA256).Hash
   [bool](Select-String -Path SHA256SUMS -Pattern "^$hash  devicefarm-connect_windows_amd64\.exe$" -Quiet)
   ```

   The output must be `True`. If the output is `False`, make sure that both files are in the current folder under their original names. If they are, delete the file and download it again.

------

**Note**  
You can also build `devicefarm-connect` from its source code in the [aws/device-connect-devicefarm](https://github.com/aws/device-connect-devicefarm) repository on the GitHub website. For build instructions, see `README.md` in the source code. A rebuild can differ from the release file, so don't use a rebuild to verify a download.

#### Install the file
<a name="device-connect-install-file"></a>

After the checks pass, install the file in `.local/bin` in your home directory, the directory that the install script uses. Choose the tab for your operating system.

------
#### [ macOS ]

In a terminal, create the directory `~/.local/bin`, make the file executable, and move it there under the name `devicefarm-connect`.

```bash
mkdir -p ~/.local/bin
chmod 755 devicefarm-connect_darwin_universal
mv devicefarm-connect_darwin_universal ~/.local/bin/devicefarm-connect
```

If `devicefarm-connect --version` doesn't work yet, add the directory to your `PATH`. Run the following command in the open terminal. For new terminals, also add the same line to your shell profile: `~/.zshrc` for zsh, or `~/.bash_profile` for bash.

```bash
export PATH="$HOME/.local/bin:$PATH"
```

------
#### [ Linux ]

In a terminal, create the directory `~/.local/bin`, make the file executable, and move it there under the name `devicefarm-connect`. For ARM64, use `devicefarm-connect_linux_arm64`.

```bash
mkdir -p ~/.local/bin
chmod 755 devicefarm-connect_linux_amd64
mv devicefarm-connect_linux_amd64 ~/.local/bin/devicefarm-connect
```

If `devicefarm-connect --version` doesn't work yet, add the directory to your `PATH`. Run the following command in the open terminal. For new terminals, also add the same line to your shell profile: `~/.bashrc` for bash, or `~/.zshrc` for zsh.

```bash
export PATH="$HOME/.local/bin:$PATH"
```

------
#### [ Windows ]

In PowerShell, create the folder `%USERPROFILE%\.local\bin`, and move the file there under the name `devicefarm-connect.exe`.

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.local\bin" | Out-Null
Move-Item -Force .\devicefarm-connect_windows_amd64.exe "$env:USERPROFILE\.local\bin\devicefarm-connect.exe"
```

If `devicefarm-connect --version` doesn't work yet, add the folder to your `PATH` one time. The first command saves the folder in the `PATH` of your user account for new windows. The second command adds it to the open window.

```powershell
[Environment]::SetEnvironmentVariable('Path', "$env:USERPROFILE\.local\bin;" + [Environment]::GetEnvironmentVariable('Path', 'User'), 'User')
$env:Path += ";$env:USERPROFILE\.local\bin"
```

To replace an older copy, first run `devicefarm-connect bridge stop`. While the bridge runs, `Move-Item` fails, and the older copy stays installed.

Run `devicefarm-connect` from PowerShell or `cmd.exe`, not from File Explorer.

If Windows shows a SmartScreen notice, see [Problems on Windows](device-connect-troubleshooting.md#device-connect-troubleshooting-windows).

------

Then run `devicefarm-connect --version` to confirm the installation.

### Update Device Connect
<a name="device-connect-update"></a>

To update Device Connect to the latest release, run the same install command again. The script replaces the installed file. If you installed the file manually, install the new release file the same way.

A bridge that runs during the update keeps the earlier version. Run `devicefarm-connect doctor`. The doctor warns when the bridge runs another version than the command, and prints the `devicefarm-connect bridge start` command that starts the bridge again with the new version. Then attach the device again with `devicefarm-connect device add`.

## Step 2: Create a remote access session
<a name="device-connect-create-session"></a>

Device Connect attaches a device through its remote access session. Create a session in the Device Farm console or with the AWS CLI. For the steps, see [Creating a session](how-to-create-session.md). Choose a device that runs Android 9 or later. For now, Device Connect supports only public devices that use the metered, pay-as-you-go billing method.

You need the Amazon Resource Name (ARN) of the session in the next step. A session ARN contains `:session:`. It is not the same as the device ARN.
+ In the console, after the session starts, in the menu on the left-hand side of the device, choose **Session ARN**. The console copies the ARN. The same menu can also show an **ADB session** action, which lists the Device Connect commands with the session ARN.
+ With the AWS CLI, the output of `create-remote-access-session` includes the session ARN.

Each session leases one device and can last up to 150 minutes. For more information, see [Service limits](limits.md#service-limits).

## Step 3: Attach the device and run adb
<a name="device-connect-attach-device"></a>

After the status of the session is `RUNNING`, attach its device to Device Connect. In the commands, replace the session ARN with your session ARN.

**Note**  
Device Connect stops a local adb server that uses port 5037. Your local devices then disappear from adb. To keep them, see [Using a different port](device-connect-interaction.md#device-connect-custom-port).

**To attach the device and run adb**

1. Attach the device. If no bridge runs, this command starts one on port 5037.

   ```bash
   devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

   The last line of the output names the port and the device.

   ```
   devicefarm-connect listening on port 5037 with connected device: Google Pixel 9 (OS 16)
   ```

1. List the devices that adb sees. The attached device appears with its serial.

   ```bash
   adb devices
   ```

1. Run a command on the device. For example, print its Android version.

   ```bash
   adb shell getprop ro.build.version.release
   ```

   On some devices, the first adb command after you attach can take several seconds.

You can now use adb and tools such as Android Studio with the device. If a step fails, run the following command and follow the fixes that it lists. For more information, see [Run the `doctor` command](device-connect-troubleshooting.md#device-connect-doctor).

```bash
devicefarm-connect doctor --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
```

## Step 4: Clean up
<a name="device-connect-clean-up"></a>

When you finish, detach the device, stop the bridge, and stop the session.

**Important**  
Device Farm bills the remote access session until you stop it. `device remove` and `bridge stop` don't stop the session.

**To clean up**

1. Detach the device.

   ```bash
   devicefarm-connect device remove
   ```

1. Stop the bridge.

   ```bash
   devicefarm-connect bridge stop
   ```

1. Stop the session with the AWS CLI, or choose **Stop session** on the session page in the console.

   ```bash
   aws devicefarm stop-remote-access-session --arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}" --region us-west-2
   ```

## Next steps
<a name="device-connect-next-steps"></a>

Now that you can attach a device, you can do more with Device Connect:
+ To run more adb commands, use Android Studio, forward ports, and switch to another device, see [Interacting with devices using adb](device-connect-interaction.md).
+ To check the bridge and find its log file, see [Working with the Device Connect bridge](device-connect-status-logs.md).
+ To fix a problem, see [Troubleshooting Device Connect](device-connect-troubleshooting.md).
+ To keep Device Connect secure, see [Infrastructure security for Device Connect](infrastructure-security.md#infrastructure-security-device-connect).