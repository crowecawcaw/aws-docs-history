# SNMP polling

AWS Elemental Conductor Live generates SNMP traps for activity on the cluster. You can set up to poll the
SNMP interface for messages. (If you prefer to receive traps, see SNMP polling.)

You can interact with Conductor Live using a variety of network
management systems. AWS Elemental products ship with the Net-SNMP
([http://www.net-snmp.org/](http://www.net-snmp.org/ "http://www.net-snmp.org/"))
command line tools. These tools let you access the SNMP interface while
you are logged into the system directly or over SSH. Examples in this
document are given using `net-snmp` commands.

###### To set up SNMP polling

1. Either disable the node firewall, or enable external access to SNMP interface.
   - For help disabling the firewall, see [Configuring a firewall and opening
     ports](network-firewall.md "network-firewall.md").
   - External access to the SNMP interface is enabled by default. To check the
     setting, access the **Settings** page on the Conductor Live web interface
     and choose **SNMP**.

2. Query either individual variables, or the entire SNMP interface.

###### To query individual variables

Use the Net-SNMP tools to query variables as follows.

```
snmpget -c elemental_snmp -v2c -m `<MIB>`
        localhost `MIBvariable`
```

```
snmpget -c elemental_snmp -v2c -m `ELEMENTAL-MIB`
          localhost `serviceStatus`
```

For a list of MIBs and their variables, see [MIBs in Conductor Live](notification-polling-mibs.md "notification-polling-mibs.md").

###### To query the entire SNMP interface

Use the Net-SNMP tools to do an snmpwalk to gather information about all of the running
channels in the cluster.

```
snmpwalk -c elemental_snmp -v2c -m ELEMENTAL-MIB:ELEMENTAL-CONDUCTOR-MIB localhost
    elemental
```
