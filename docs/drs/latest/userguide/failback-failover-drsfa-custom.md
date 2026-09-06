

# Custom failback
<a name="failback-failover-drsfa-custom"></a>

The custom failback option provides more control over the failback process. You first generate a configuration file, edit settings for individual machines, and then perform failback using that file.

## Find servers in vCenter
<a name="failback-failover-drsfa-find-servers"></a>

Before configuring custom failback, use the **Find servers in vCenter** menu option to discover the disks and volumes of your vCenter machines. This information is needed when configuring custom device mapping.

You can enter a name filter or press Enter to list all machines. The results include the following details for each server:
+ Name
+ UUID
+ Disk and volume information

Results are exported to the `Results/VMFinder` folder with the naming convention: `{vcenter_host}_{timestamp}.txt`

## Generating the configuration file
<a name="failback-failover-drsfa-custom-generating"></a>

You can create a custom configuration JSON file manually or generate a default configuration file through the client.

To generate a default file, select **Generate a default failback configuration file** from the main menu. Enter a custom prefix for the file name. The configuration file is created as a JSON file in the `/drs_failback_automation_client/Configurations/` folder with the name: `{prefix}_{account_id}_{region}.json`

The file contains these fields for each machine:
+ `NETMASK`
+ `VCENTER_MACHINE_UUID`
+ `PROXY`
+ `DNS`
+ `CONFIG_NETWORK`
+ `IPADDR`
+ `GATEWAY`
+ `SOURCE_SERVER_ID`
+ `DEVICE_MAPPING`

Edit any field to control the failback configuration for each machine, then save your changes.

**Note**  
Set `CONFIG_NETWORK` to "DHCP" for DHCP or "STATIC" for manual network configuration. When set to "DHCP", the `DNS`, `IPADDR`, `GATEWAY`, `NETMASK`, and `PROXY` parameters are ignored but must not be deleted.
If you are not using a proxy server, leave the `PROXY` field as an empty string. Do not remove it.
If a source server does not have an attached recovery instance, the **SOURCE\_SERVER\_ID** field is empty.

## Custom device mapping parameter
<a name="failback-failover-drsfa-device-mapping-override"></a>

The `DEVICE_MAPPING` field is passed to the LiveCD failback process as the `--device-mapping` argument. [Learn more about using the --device-mapping program argument](failback-performing.md#failback-failover-program-arg-device-mapping).

Use the [Find servers in vCenter](#failback-failover-drsfa-find-servers) utility to discover disk names for your machines.

Three formats are supported:

1. Classic CE format — a key-value CSV string on one line. Use either ":" or "=" as the field separator:

   ```
   "DEVICE_MAPPING": "recovery_device1=local_device1,recovery_device2=local_device2,recovery_device3=EXCLUDE"
   ```

   ```
   "DEVICE_MAPPING": "recovery_device1:local_device1,recovery_device2:local_device2"
   ```

1. JSON format:

   ```
   "DEVICE_MAPPING": {
       "/dev/xvdb":"/dev/sdb",
       "/dev/xvdc":"/dev/sdc",
       "recovery_device3":"local_device3"
   }
   ```

1. JSON list DRS API format:

   ```
   [
       {
           "recoveryInstanceDeviceName": "recovery_device1",
           "failbackClientDeviceName": "local_device1"
       },
       {
           "recoveryInstanceDeviceName": "recovery_device2",
           "failbackClientDeviceName": "local_device2"
       }
   ]
   ```

Regardless of format, provide either a valid Failback Client device name or `EXCLUDE` for each Recovery Instance device.

## Performing the custom failback
<a name="failback-failover-drsfa-custom-performing"></a>

After editing your configuration file, rerun the DRSFA client and select **Custom Failback** from the main menu.

1. Select your configuration file. You can define a custom path or use the default path displayed by the client.

1. Enter a custom prefix for the results output file.

1. If failback replication has already started for some Recovery instances, choose whether to skip those instances or restart replication.

1. The client lists the Recovery instances to be failed back. Enter **Y** to continue.

1. The client initiates failback. Monitor progress on the **Recovery instances** page in the DRS console.

Results are exported in the same format described in [Failback results](failback-failover-drsfa-one-click.md#failback-failover-drsfa-results).