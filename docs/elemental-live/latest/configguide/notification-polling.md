# Simple Network Management Protocol (SNMP) polling

Rather than passively receiving SNMP traps from
AWS Elemental Live, you can actively poll the
SNMP interface.

You can interact with Elemental Live using a variety of network management systems. AWS
Elemental products ship with the Net-SNMP (http://www.net-snmp.org/) command line tools to
access the SNMP interface while logged into the system directly or over SSH. Examples in this
document are given using net-snmp commands.

###### To set up SNMP polling

1. Either disable the node firewall, or enable external access to SNMP interface.
   - For help disabling the firewall, see [Open ports on the firewall for Elemental Live nodes](config-wrkr-cf-cg-firewall.md "config-wrkr-cf-cg-firewall.md").
   - External access to the SNMP interface is enabled by default. To check the
     setting, access the **Settings** page on the Elemental Live web interface
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

For a list of MIBs and their variables, see [Management Information Bases (MIBs) in Elemental Live](notification-polling-mibs.md "notification-polling-mibs.md").

###### To query the entire SNMP interface

Use the Net-SNMP tools to do an snmpwalk to gather information about all of the running
channels.

```
snmpwalk -c elemental_snmp -v2c -m ELEMENTAL-MIB:ELEMENTAL-LIVE-MIB localhost
    elemental
```
