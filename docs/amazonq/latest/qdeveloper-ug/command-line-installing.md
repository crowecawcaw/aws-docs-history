# Installing Amazon Q for command line

You can install Amazon Q for command line for macOS by initiating a file download for the
Amazon Q application. For more information, see [Supported command line
environments](command-line-supported-envs.md "command-line-supported-envs.md").

There are two installation options to consider when installing Amazon Q for command line. The minimal
installation includes only the binaries needed on Linux for Amazon Q chat and for the
autocomplete feature to function over SSH (`q` and `qterm`). The full
installation contains the desktop application and requires the autocomplete feature to be
used. If you want to only use the Amazon Q chat, consider that the minimal installation also
ships and installs `qterm` to your shell. You can use `qterm` for
zsh to support inline completions and a full version isn't required. For more
information, see [Installing with a zip file](command-line-installing-ssh-setup-autocomplete.md "command-line-installing-ssh-setup-autocomplete.md").

###### Note

For information about using the Amazon Q CLI with Windows, see [this blog post](https://dev.to/aws/the-essential-guide-to-installing-amazon-q-developer-cli-on-windows-lmh "https://dev.to/aws/the-essential-guide-to-installing-amazon-q-developer-cli-on-windows-lmh") on dev.to.

## macOS

You can install Amazon Q for command line for macOS by downloading the application or by
using Homebrew.

After installing Amazon Q for command line for macOS, you can enable shell integration to
be able to use autocomplete for over 500 command line tools. For more information, see
[Local macOS Integration](command-line-remote-machines.md#command-line-remote-machines-local-mac "command-line-remote-machines.md#command-line-remote-machines-local-mac").

To install Amazon Q for command line for macOS, complete the following procedure.

1. [Download Amazon Q for command line for macOS.](https://desktop-release.q.us-east-1.amazonaws.com/latest/Amazon%20Q.dmg "https://desktop-release.q.us-east-1.amazonaws.com/latest/Amazon%20Q.dmg")
2. (Optional) Verify the downloaded file for Amazon Q for command line on macOS.
   For more information, see [To verify
   the download (optional).](command-line-verify-download.md "command-line-verify-download.md")
3. Double-click on the downloaded .dmg file, and drag the app into your
   applications folder.
4. In your applications folder, double-click on Amazon Q. The GUI will open.
5. Enable the shell integrations. This will allow you to run Amazon Q from the shell, and will also allow Amazon Q to help you with shell command auto-completions.
6. Authenticate with [Builder ID](../../../general/latest/gr/aws_builder_id.md "../../../general/latest/gr/aws_builder_id.md"), or with
   [IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") using the start URL given to you by your account
   administrator.
7. Follow the instructions to install the shell integrations, and to grant macOS
   accessibility permissions.

![Amazon Q Developer automated checks interface showing Shell integrations with a green checkmark and Enable accessibility with a red X, indicating shell integrations are complete but accessibility permissions still need to be granted](images/shell_access_checks2.png)

## Linux AppImage

###### Warning

This installation method requires a GUI. If you are installing on Linux without a
GUI, see [Installing with a zip file](command-line-installing-ssh-setup-autocomplete.md "command-line-installing-ssh-setup-autocomplete.md")
.

You can install Amazon Q for command line for Linux using the AppImage format, which is
a portable format that works on most Linux distributions without requiring
installation.

To install Amazon Q for command line for Linux using AppImage, complete the following procedure.

1. [Download Amazon Q for command line for Linux AppImage.](https://desktop-release.q.us-east-1.amazonaws.com/latest/amazon-q.appimage "https://desktop-release.q.us-east-1.amazonaws.com/latest/amazon-q.appimage")
2. Make the AppImage executable:

```
chmod +x amazon-q.appimage
```

3. Run the AppImage:

```
./amazon-q.appimage
```

4. Authenticate with [Builder ID](../../../general/latest/gr/aws_builder_id.md "../../../general/latest/gr/aws_builder_id.md"), or with
   [IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") using the start URL given to you by your account
   administrator.

## Ubuntu

###### Warning

This installation method requires a GUI. If you are installing on Linux without a
GUI, see [Installing with a zip file](command-line-installing-ssh-setup-autocomplete.md "command-line-installing-ssh-setup-autocomplete.md")
.

You can install Amazon Q for command line for Ubuntu using the .deb package.

To install Amazon Q for command line for Ubuntu, complete the following procedure.

1. [Download Amazon Q for command line for Ubuntu.](https://desktop-release.q.us-east-1.amazonaws.com/latest/amazon-q.deb "https://desktop-release.q.us-east-1.amazonaws.com/latest/amazon-q.deb")

```
wget https://desktop-release.q.us-east-1.amazonaws.com/latest/amazon-q.deb
```

2. Install the package:

```
sudo dpkg -i amazon-q.deb
sudo apt-get install -f
```

3. Launch Amazon Q for command line:

```
q
```

4. Authenticate with [Builder ID](../../../general/latest/gr/aws_builder_id.md "../../../general/latest/gr/aws_builder_id.md"), or with
   [IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") using the start URL given to you by your account
   administrator.

## Homebrew

To install Amazon Q Developer CLI with Homebrew, run the following command:

```
brew install --cask amazon-q
```

## Proxy configuration

Amazon Q Developer CLI (v1.8.0 and later) supports proxy servers commonly used in enterprise environments. The CLI automatically respects standard proxy environment variables.

### Setting proxy environment variables

Configure proxy settings by setting these environment variables in your shell:

```
# HTTP proxy for non-SSL traffic
export HTTP_PROXY=http://proxy.company.com:8080

# HTTPS proxy for SSL traffic
export HTTPS_PROXY=http://proxy.company.com:8080

# Bypass proxy for specific domains
export NO_PROXY=localhost,127.0.0.1,.company.com
```

### Proxy with authentication

For proxies requiring authentication:

```
export HTTP_PROXY=http://username:password@proxy.company.com:8080
export HTTPS_PROXY=http://username:password@proxy.company.com:8080
```

### SOCKS proxy support

Amazon Q CLI also supports SOCKS proxies:

```
export HTTP_PROXY=socks5://proxy.company.com:1080
export HTTPS_PROXY=socks5://proxy.company.com:1080
```

### Verifying proxy configuration

After setting proxy environment variables, test connectivity:

```
q doctor
```

### Troubleshooting proxy issues

If you encounter proxy-related connection issues:

- Verify proxy server accessibility and credentials
- Ensure your corporate firewall allows connections to AWS endpoints
- Contact your IT administrator if SSL certificate validation fails
- Check that the proxy server supports the required protocols

## Uninstalling Amazon Q for command

line

You can uninstall Amazon Q for command line if you no longer need it.

To uninstall Amazon Q for command line on macOS, complete the following procedure.

1. Open the Applications folder in Finder.
2. Locate the Amazon Q Developer application.
3. Drag the application to the Trash, or right-click and select "Move to
   Trash".
4. Empty the Trash to complete the uninstallation.

To uninstall Amazon Q for command line on Ubuntu, complete the following procedure.

1. Use the apt package manager to remove the package:

```
sudo apt-get remove amazon-q
```

2. Remove any remaining configuration files:

```
sudo apt-get purge amazon-q
```

## Debugging Amazon Q Developer for the command

line

If you're having a problem with Amazon Q Developer for command line, run `q
 doctor` to identify and fix common issues.

### Expected output

```
$ q doctor

✔ Everything looks good!

Amazon Q still not working? Run q issue to let us know!
```

If your output doesn't look like the expected output, follow the prompts to
resolve your issue. If it's still not working, use `q issue` to
report the bug.

### Common issues

Here are some common issues you might encounter when using Amazon Q for command
line:

Authentication failures

If you're having trouble authenticating, try running `q
 login` to re-authenticate.

Autocomplete not working

Ensure your shell integration is properly installed by running
`q doctor`.

SSH integration issues

Verify that your SSH server is properly configured to accept the
required environment variables.

### Troubleshooting

steps

Follow these steps to troubleshoot issues with Amazon Q for command line:

1. Run `q doctor` to identify and fix common issues.
2. Check your internet connection.
3. Verify that you're using a supported environment. For more
   information, see [Supported command line
   environments](command-line-supported-envs.md "command-line-supported-envs.md")
   .
4. Try reinstalling Amazon Q for command line.
5. If the issue persists, report it using `q issue`.
