# IPv6 support

IPv6 support is only available on gateway appliance versions 2.x or higher. Gateway appliance version 1.x can't be updated to version 2.x. You must migrate or replace your gateway appliance version 1.x to get IPv6 support.

The following dual-stack endpoints are required for IPv6.

```
storagegateway.`region`.api.aws:443
activation-storagegateway.`region`.api.aws:443
controlplane-storagegateway.`region`.api.aws:443
proxy-storagegateway.`region`.api.aws:443
dataplane-storagegateway.`region`.api.aws:443
s3.dualstack.`region`.amazonaws.com
```
