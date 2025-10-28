This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Simple Network Management Protocol (SNMP) Traps

You can configure AWS Elemental Server to generate Simple Network Management Protocol (SNMPv2)
traps for
activity on the node. For
information about the management information bases (MIBs) in AWS Elemental Server, go to the
**Settings** page in the AWS Elemental Server web interface and choose
**SNMP Interface**.

AWS Elemental Server generates traps for the events described in the following table.

| Notification                   | Event                                                                                                                 | Contents                                                                                                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| ELEMENTAL-MIB::alert           | Any alert that worker nodes in the cluster generate.                                                                  | <br>• ELEMENTAL-MIB::alertSet: `1` if the alert is being set, `0` if the alert is being cleared. <br>• ELEMENTAL-MIB::alertMessage: describes the alert that was set or cleared. | ###### To set up SNMP traps 1. On the AWS Elemental Server web interface, go to the **Settings** page and choose **SNMP**. 2. On the **SNMP** page, complete the fields, using the instructions in the following table as a guide. Choose **Save**: |
| Field                          | Instructions                                                                                                          |                                                                                                                                                                                  | ---                                                                                                                                                                                                                                                 | ---                               |
| **Allow external SNMP access** | Choose **Yes** to open the SNMP port on the firewall. The port must be open if you will send an **snmpwalk** command. |                                                                                                                                                                                  | **Generate SNMP Traps for Alerts**                                                                                                                                                                                                                  | Choose **Yes** to generate traps. |
| **SNMP Management Host**       | Enter the IP address of the trap destination.                                                                         |                                                                                                                                                                                  | **SNMP Management Trap Port**                                                                                                                                                                                                                       | Enter `162`.                      |
| **SNMP Management Community**  | Enter `Public`.                                                                                                       |
