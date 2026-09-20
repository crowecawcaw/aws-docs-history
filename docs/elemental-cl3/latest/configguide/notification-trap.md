

# SNMP traps
<a name="notification-trap"></a>

AWS Elemental Conductor Live generates SNMP traps for activity on the cluster. You can set up to receive SNMP traps from Conductor Live. (If you prefer to poll the SNMP interface for messages, see [SNMP polling](notification-polling.md).)

Conductor Live generates SNMP traps for the following events.
+ Type of notification: `ELEMENTAL-MIB::alert`
+ Type of event: Any alert that worker nodes in the cluster generate.
+ Contents of the notification:
  + `ELEMENTAL-MIB::alertSet`. The value is `1` if the alert is being set, `0` if the alert is being cleared.
  + `ELEMENTAL-MIB::alertMessage`. Describes the alert that was set or cleared.

**To set up SNMP traps**

1. On the Conductor Live web interface, go to the **Settings** page and choose **SNMP**.

1. On the **SNMP** page, complete the fields. Use the instructions in the following table as a guide. Choose **Save**:


<table>
<thead>
  <tr><th>Field</th><th>Instructions</th></tr>
</thead>
<tbody>
  <tr><td><b>Allow external SNMP access</b></td><td>Choose <b>Yes</b> to open the SNMP port on the firewall. The port must be open if you will send an <b>snmpwalk</b> command.</td></tr>
  <tr><td><b>Generate SNMP Traps for Alerts</b></td><td>Choose <b>Yes</b> to generate traps.</td></tr>
  <tr><td><b>SNMP Management Host</b></td><td>Enter the IP address of the trap destination.</td></tr>
  <tr><td><b>SNMP Management Trap Port</b></td><td>Enter <b>162</b>.</td></tr>
  <tr><td><b>SNMP Management Community</b></td><td>Enter <b>Public</b>.</td></tr>
</tbody>
</table>
