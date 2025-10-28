# IPv6 support

IPv6 support is only available on gateway appliance versions 3.x or higher. Gateway appliance versions 1.x and 2.x can't be updated to 3.x. You must migrate or replace your gateway appliance version 1.x or 2.x to get IPv6 support.

The following dual-stack endpoints are required for IPv6. For more information, see [Endpoint types](Requirements.md#endpoint-types "Requirements.md#endpoint-types").

```
storagegateway.`region`.api.aws:443
activation-storagegateway.`region`.api.aws:443
controlplane-storagegateway.`region`.api.aws:443
proxy-storagegateway.`region`.api.aws:443
dataplane-storagegateway.`region`.api.aws:443
```
