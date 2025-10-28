# Install the Session Manager plugin on

macOS

Choose one of the following topics to install the Session Manager plugin on macOS.

###### Note

The signed installer is a signed `.pkg` file. The
bundled installer uses a `.zip` file. After the file is
unzipped, you can install the plugin using the binary.

## Install the Session Manager plugin on

macOS with the signed installer

This section describes how to install the Session Manager plugin on macOS using the
signed installer.

###### To install the Session Manager plugin using the signed installer (macOS)

1. Download the signed installer.

x86_64

```
curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/mac/session-manager-plugin.pkg" -o "session-manager-plugin.pkg"
```

Mac with Apple silicon

```
curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/mac_arm64/session-manager-plugin.pkg" -o "session-manager-plugin.pkg"
```

2. Run the install commands. If the command fails, verify that the
   `/usr/local/bin` folder exists. If it doesn't, create
   it and run the command again.

```
sudo installer -pkg session-manager-plugin.pkg -target /
sudo ln -s /usr/local/sessionmanagerplugin/bin/session-manager-plugin /usr/local/bin/session-manager-plugin
```

3. Verify that the installation was successful. For information, see
   [Verify the Session Manager plugin installation](install-plugin-verify.md "install-plugin-verify.md").

## Install the Session Manager plugin on

macOS

This section describes how to install the Session Manager plugin on macOS using the
bundled installer.

###### Important

Note the following important information.

- By default, the installer requires sudo access to run, because
  the script installs the plugin to the
  `/usr/local/sessionmanagerplugin` system
  directory. If you don't want to install the plugin using sudo,
  manually update the installer script to install the plugin to a
  directory that doesn't require sudo access.
- The bundled installer doesn't support installing to paths that
  contain spaces.

###### To install the Session Manager plugin using the bundled installer (macOS)

1. Download the bundled installer.

x86_64

```
curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/mac/sessionmanager-bundle.zip" -o "sessionmanager-bundle.zip"
```

Mac with Apple silicon

```
curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/mac_arm64/sessionmanager-bundle.zip" -o "sessionmanager-bundle.zip"
```

2. Unzip the package.

```
unzip sessionmanager-bundle.zip
```

3. Run the install command.

```
sudo ./sessionmanager-bundle/install -i /usr/local/sessionmanagerplugin -b /usr/local/bin/session-manager-plugin
```

###### Note

The plugin requires Python 3.10 or later. By default, the
install script runs under the system default version of Python.
If you have installed an alternative version of Python and want
to use that to install the Session Manager plugin, run the install script with
that version by absolute path to the Python executable. The
following is an example.

```
sudo /usr/local/bin/python3.11 sessionmanager-bundle/install -i /usr/local/sessionmanagerplugin -b /usr/local/bin/session-manager-plugin
```

The installer installs the Session Manager plugin at
`/usr/local/sessionmanagerplugin` and creates
the symlink `session-manager-plugin` in the
`/usr/local/bin` directory. This eliminates
the need to specify the install directory in the user's
`$PATH` variable.

To see an explanation of the `-i` and
`-b` options, use the `-h`
option.

```
./sessionmanager-bundle/install -h
```

4. Verify that the installation was successful. For information, see
   [Verify the Session Manager plugin installation](install-plugin-verify.md "install-plugin-verify.md").

###### Note

To uninstall the plugin, run the following two commands in the order
shown.

```
sudo rm -rf /usr/local/sessionmanagerplugin
```

```
sudo rm /usr/local/bin/session-manager-plugin
```
