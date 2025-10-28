# Configure SPANK plugins on AWS PCS

By default, store configuration files in `/etc/aws/pcs/scheduler/slurm-`version`/plugstack.conf.d/`.

To store your SPANK configuration in a different location,
add your locations to a configuration file in the default directory.

The following example shows how to include configuration files from other directories:

```
# content of /etc/aws/pcs/scheduler/slurm-`version`/`any-filename`.conf
include `path-to-your-configuration-folder`/*.conf
include `path-to-a-second-configuration-folder`/*.conf
```

Store each configuration in a dedicated file, or in a common file. You can use multiple configuration files.

The following examples show sample configuration files:

```
# content of `path-to-your-or-default-config-folder`/`filename-1`.conf
required `path-to-plugin-1` `arguments`
optional `path-to-plugin-2` `arguments`
```

```
# content of `path-to-your-or-default-config-folder`/`filename-2`.conf
required `path-to-plugin-3` `arguments`
```

For additional information about how to configure your plugins, see the [SPANK configuration documentation](https://slurm.schedmd.com/spank.html#SECTION_CONFIGURATION "https://slurm.schedmd.com/spank.html#SECTION_CONFIGURATION") on the SchedMD website.

###### Important

Set folder permissions to prevent unauthorized changes to your plugin configuration.

###### Note

AWS PCS doesn't manage your SPANK plugins. If you get errors related to plugins, check the error logs on your compute nodes.

###### Note

Slurm incorrectly logs an error similar to the following when it loads your SPANK configuration:

```
error: "Include" failed in file /etc/slurm/plugstack.conf line 3
```

You can ignore this error. It doesn't affect how SPANK plugins work.
