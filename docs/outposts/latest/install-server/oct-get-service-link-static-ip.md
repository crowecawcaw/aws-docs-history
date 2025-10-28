# get-service-link-static-ip

The **get-service-link-static-ip** command, when used after you set the
static configuration for the service link with the
**set-service-link-static-ip** command, returns the service link static
configuration values. These values are applied only after you reboot the Outposts
server.

**Syntax**

```
`Outpost>`get-service-link-static-ip
```

**Parameters**

This command has no parameters.

###### Example output: Success

```
Outpost> get-service-link-static-ip
---
ip_address: 192.168.1.2
netmask: 255.255.255.0
gateway: 192.168.1.1
success: true
```
