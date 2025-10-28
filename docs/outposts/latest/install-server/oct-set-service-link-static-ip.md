# set-service-link-static-ip

The **set-service-link-static-ip** command sets the static configuration
for the service link. These values are applied only after you reboot the Outposts
server.

**Syntax**

```
`Outpost>`set-service-link-static-ip `service-link-IP-address subnet-mask network-gateway-IP-address`
```

For example: `Outpost>`set-service-link-static-ip
`192.168.1.2 255.255.255.0 192.168.1.1`

**Parameters**

You must provide the following values:

- The service link IP address
- subnet mask
- network gateway IP address

###### Example output: Success

```
Outpost> set-service-link-static-ip
---
success: True
```
