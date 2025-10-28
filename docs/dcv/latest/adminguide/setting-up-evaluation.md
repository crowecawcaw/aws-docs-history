# Installing an extended evaluation

license

When you request an extended evaluation license from Amazon DCV, you receive a `license.lic` file
that defines the license.

###### To install the extended evaluation license

Place the `license.lic` file in the following folder on your server:

- Windows server

```
C:\Program Files\NICE\DCV\Server\license\license.lic
```

- Linux server

```
/usr/share/dcv/license/license.lic
```

Or, to place the `license.lic` in a different folder on the server, you must
update the `license-file` configuration parameter so that it specifies the full
path for the license file.

###### Topics

- [Changing the license path on a Windows Server](#change-param-win "#change-param-win")
- [Changing the license path on a Linux server](#change-param-lin "#change-param-lin")

## Changing the license path on a Windows Server

###### To update the `license-file` configuration parameter on a Windows server

1. Open the Windows Registry Editor.
2. Navigate to the **HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\license\*\* key
   and select the **license-file\*\* parameter.

If there is no `license-file` parameter in the registry key, create
one:

    1. Open the context (right-click) menu for the **license** key in the left pane
     and choose **New**, **String Value**.
    2. For **Name**, enter `license-file` and press
     **Enter**.

3. Open the **license-file** parameter. For **Value
   data**, enter the full path to the `license.lic`
   file.
4. Choose **OK** and close the Windows Registry Editor.

## Changing the license path on a Linux server

###### To update the `license-file` configuration parameter on a Linux server

1. Navigate to `/etc/dcv/` and open the `dcv.conf` with your preferred text editor.
2. Locate the `license-file` parameter in the `[license]` section, and
   replace the existing path with the new full path to the `license.lic` file.

If there is no `license-file` parameter in the `[license]` section,
add it manually using the following format:

```
license-file = "/`custom-path`/license.lic"
```

3. Save and close the file.
