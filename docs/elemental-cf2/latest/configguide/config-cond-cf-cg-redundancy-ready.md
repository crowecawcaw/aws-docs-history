This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step A: Get Ready

1. Identify the interface that you have configured as the management interface. Typically, this is one of the following:
   - eth0
   - bond0, if you bonded the management interfaces for the two Conductor nodes

2. Find the MAC addresses of the management interface for the primary and secondary Conductor nodes.

If you bonded the management interfaces for the two Conductor nodes, use the `ifconfig` command to obtain the MAC addresses for bond0.

```
[elemental@hostname ~]$ **ifconfig**
```

3. Decide on a virtual IP address that will be used by the management interfaces on both Conductor nodes. This address must meet the following criteria:
   - An address on your network that will never be allocated to any other host.
   - An address on the same subnet as the Conductor nodes.

4. Decide on the ID for a virtual router. The ID can be any arbitrary integer from 1-255. This ID must be unique on the subnet for each AWS Elemental cluster or any other keepalived-managed VIPs that are in the network.
