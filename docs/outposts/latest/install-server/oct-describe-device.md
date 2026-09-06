

# describe-device
<a name="oct-describe-device"></a>

The **describe-device** command returns information about the Outposts server, including the protocol version, management device type, server type, asset ID, serial number, and manufacturer.

**Syntax**  

```
Outpost>describe-device
```

**Parameters**  
This command has no parameters.

**Example output: Success**  

```
Outpost> describe-device
success: True
protocol: 0.1
management_device_type: {{management-device}}
server_type: {{server-type}}
server_asset_id: {{asset-id}}
server_serial_number: {{serial-number}}
server_manufacturer: {{manufacturer}}
checksum: {{checksum}}
```