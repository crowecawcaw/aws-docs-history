# SNMP traps

AWS Elemental Conductor Live generates SNMP traps for activity on the cluster. You can set up to receive
SNMP traps from Conductor Live. (If you prefer to poll the SNMP interface for messages, see [SNMP polling](notification-polling.md "notification-polling.md").)

Conductor Live generates SNMP traps for the following
events.

- Type of notification: `ELEMENTAL-MIB::alert`
- Type of event: Any alert that worker nodes in the cluster
  generate.

- Contents of the notification:
  - `ELEMENTAL-MIB::alertSet`. The value is
    `1` if the alert is being set, `0` if the
    alert is being cleared.

  - `ELEMENTAL-MIB::alertMessage`. Describes the alert
    that was set or cleared.

###### To set up SNMP traps

1. On the Conductor Live web interface, go to the **Settings** page
   and choose **SNMP**.
2. On the **SNMP** page, complete the fields. Use the
   instructions in the following table as a guide. Choose
   **Save**:

| Field                              | Instructions                                                                                                          |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Allow external SNMP access**     | Choose **Yes** to open the SNMP port on the firewall. The port must be open if you will send an **snmpwalk** command. |
| **Generate SNMP Traps for Alerts** | Choose **Yes** to generate traps.                                                                                     |
| **SNMP Management Host**           | Enter the IP address of the trap destination.                                                                         |
| **SNMP Management Trap Port**      | Enter `162`.                                                                                                          |
| **SNMP Management Community**      | Enter `Public`.                                                                                                       |
