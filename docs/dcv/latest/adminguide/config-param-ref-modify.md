# Modifying configuration parameters

This section describes how to modify the configuration parameters for your Amazon DCV server. For
more information about the registry keys for Windows servers, sections for Linux
servers, parameter names, types, and valid values, see the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

###### Topics

- [Windows Amazon DCV Servers](#config-param-ref-win "#config-param-ref-win")
- [Linux Amazon DCV servers](#config-param-ref-linux "#config-param-ref-linux")
- [macOS Amazon DCV servers](#config-param-ref-macos "#config-param-ref-macos")

## Windows Amazon DCV Servers

For Windows Amazon DCV servers, modify the configuration parameters using the Windows Registry
Editor, PowerShell, or the command line.

###### To modify a configuration parameter using the Windows Registry Editor

1. Open the Windows Registry Editor.
2. Navigate to the following registry path:

```
`HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\`
```

3. Select the registry key in which the parameter exists. If the registry key does not exist, create it using the exact key name described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").
4. Open (double-click) the parameter. If the parameter does not exist, add it using the type
   and name described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

###### To modify a configuration parameter using the PowerShell

1. Run PowerShell as the administrator.
2. Add the registry key using the key name described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

```
PS `C:\>`  New-Item -Path "Microsoft.PowerShell.Core\Registry::\HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\" -Name `registry_key` -Force
```

3. Create the parameter in the registry key using the type and name described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

```
PS `C:\>`  New-ItemProperty -Path "Microsoft.PowerShell.Core\Registry::\HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\`registry_key`" -Name `parameter_name` -PropertyType `parameter_type` -Value `parameter_value` -Force
```

###### To modify a configuration using the command line

1. Run the command line as the administrator.
2. Create the registry key and add the parameter using the key name, and parameter type and name described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

```
`C:\>`  reg.exe ADD "HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\`registry_key`" /v `parameter_name` /t `parameter_type` /d `parameter_value` /f
```

## Linux Amazon DCV servers

For Linux Amazon DCV servers, the configuration parameters can be modified using a text editor or a command line tool, such as **crudini**.

###### To modify a configuration parameter using a text editor

1. Open `/etc/dcv/dcv.conf` using your preferred text editor.
2. Locate the appropriate section in the file. If the section does not exist, add it using the section name described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

```
[`section`]
```

3. Locate the parameter in the section and modify the value. If the parameter does not exist in the section, add it using the parameter name described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

```
`parameter_name`="`parameter_value`"
```

4. Save and close the file.

###### To modify a configuration parameter using crudini

Create the section and add the parameter using the section and parameter names described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

```
`$`  sudo crudini --set /etc/dcv/dcv.conf `section_name` `parameter_name` '`parameter_value`'
```

## macOS Amazon DCV servers

For macOS Amazon DCV servers, the configuration parameters can be modified using a text editor or a command line tool, such as **crudini**.

###### To modify a configuration parameter using a text editor

1. Open `/etc/dcv/dcv.conf` using your preferred text editor.
2. Locate the appropriate section in the file. If the section does not exist, add it using the section name described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

```
[`section`]
```

3. Locate the parameter in the section and modify the value. If the parameter does not exist in the section, add it using the parameter name described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

```
`parameter_name`="`parameter_value`"
```

4. Save and close the file.

###### To modify a configuration parameter using crudini

Create the section and add the parameter using the section and parameter names described in the [Amazon DCV Server parameter reference](config-param-ref.md "config-param-ref.md").

```
`$`  sudo crudini --set /etc/dcv/dcv.conf `section_name` `parameter_name` '`parameter_value`'
```
