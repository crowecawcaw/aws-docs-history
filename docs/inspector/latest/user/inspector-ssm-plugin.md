# The Amazon Inspector SSM plugin for Linux and Windows

This topic describes the Amazon Inspector SSM plugin for Linux and Windows instances.

## The Amazon Inspector SSM plugin for Linux

Amazon Inspector uses the Amazon Inspector SSM plugin to perform deep inspection scans on Linux instances.
The Amazon Inspector SSM plugin is automatically installed on Linux instances in the `/opt/aws/inspector/bin` directory.
The name of the executable is `inspectorssmplugin`.

Amazon Inspector uses Systems Manager Distributor to deploy the plugin on your instance.
To perform deep inspection scans, Systems Manager Distributor and Amazon Inspector must support your Amazon EC2 instance operating system.
For information about operating systems that Systems Manager Distributor supports, see [Supported package platforms and architectures](../../../systems-manager/latest/userguide/distributor.md#what-is-a-package-platforms "../../../systems-manager/latest/userguide/distributor.md#what-is-a-package-platforms") in the _AWS Systems Manager User Guide_.

Amazon Inspector creates file directories to manage data collected for deep inspection by the Amazon Inspector SSM plugin.
These file directories include `/opt/aws/inspector/var/input` and `/opt/aws/inspector/var/output`.

The `packages.txt` file in `/opt/aws/inspector/var/output` stores the full paths to packages that deep inspection discovers.
If Amazon Inspector detects the same package multiple times on your instance, the `packages.txt` file lists each location where the package was found.

Amazon Inspector stores logs for the plugin in the `/var/log/amazon/inspector` directory.

### Uninstalling the Amazon Inspector SSM plugin

If the `inspectorssmplugin` file is inadvertently deleted, the SSM association `InspectorLinuxDistributor-do-not-delete` will try to reinstall the `inspectorssmplugin` file at the next scan interval.

If you deactivate Amazon EC2 scanning, the plugin will be automatically uninstalled from all Linux hosts.

## The Amazon Inspector SSM plugin for Windows

The Amazon Inspector SSM plugin is required for Amazon Inspector to scan your Windows instances.
The Amazon Inspector SSM plugin is automatically installed on your Windows instances in `C:\Program Files\Amazon\Inspector`, and the executable binary file is named `InspectorSsmPlugin.exe`.

The following file locations are created to store data the Amazon Inspector SSM plugin collects:

- `C:\ProgramData\Amazon\Inspector\Input`
- `C:\ProgramData\Amazon\Inspector\Output`
- `C:\ProgramData\Amazon\Inspector\Logs`

###### Note

By default, the Amazon Inspector SSM plugin runs at below normal priority.

###### Note

You can use Windows instances with the [Default Host Management Configuration setting](../../../systems-manager/latest/userguide/managed-instances-default-host-management.md "../../../systems-manager/latest/userguide/managed-instances-default-host-management.md").
However, you must create or use a role that's configured with the `ssm:PutInventory` and `ssm:GetParameter` permissions.

### Uninstalling the Amazon Inspector SSM plugin

If the `InspectorSsmPlugin.exe` file is inadvertently deleted, the `InspectorDistributor-do-not-delete` association will reinstall the `InspectorSsmPlugin.exe` file at the next Windows scan interval.
If you want to uninstall the Amazon Inspector SSM plugin, you can use the **Uninstall** action in the `AmazonInspector2-ConfigureInspectorSsmPlugin` document.
However, the Amazon Inspector SSM plugin will be automatically uninstalled from all Windows hosts if you deactivate Amazon EC2 scanning.

###### Note

If you uninstall the SSM Agent before deactivating Amazon Inspector, the Amazon Inspector SSM plugin will remain on the Windows host, but will not send data to the Amazon Inspector SSM plugin.
For more information, see [Deactivating Amazon Inspector](deactivating-best-practices.md "deactivating-best-practices.md").
