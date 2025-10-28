This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Simple Network Management Protocol (SNMP) Polling

Rather than passively receiving SNMP traps from AWS Elemental Statmux, you can actively poll the
SNMP interface.

You can interact with AWS Elemental Statmux using a variety of network management systems. AWS
Elemental products ship with the Net-SNMP (http://www.net-snmp.org/) command-line tools to
access the SNMP interface while logged into the system directly or over SSH. Examples in this
document are given using net-snmp commands.

###### To set up SNMP polling

1. Either disable the node firewall, or enable external access to SNMP interface.
   - For help disabling the firewall, see[Open Ports on the Firewall for AWS Elemental Statmux Nodes](config-wrkr-cf-cg-firewall.md "config-wrkr-cf-cg-firewall.md").
   - External access to the SNMP interface is enabled by default. To check the setting, access the **Settings** page on the AWS Elemental Statmux web interface and choose **SNMP**.

2. Query either individual variables, or the entire SNMP interface.

###### To query individual variables

Use the Net-SNMP tools to query variables as follows:

```
snmpget -c elemental_snmp -v2c -m `<MIB>` localhost `MIBvariable`
```

```
snmpget -c elemental_snmp -v2c -m `ELEMENTAL-MIB` localhost `serviceStatus`
```

For a list of MIBs and their variables, see [Management Information Bases (MIBs) in AWS Elemental Statmux](notification-polling-mibs.md "notification-polling-mibs.md").
