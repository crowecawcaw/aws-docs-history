

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Simple Network Management Protocol (SNMP) Traps
<a name="notification-trap"></a>

You can configure AWS Elemental Statmux to generate Simple Network Management Protocol (SNMPv2) traps for activity on the node. For information about the management information bases (MIBs) in Statmux, go to the **Settings** page in the Statmux web interface and choose **SNMP Interface**.

AWS Elemental Statmux generates traps for the events described in the following table.


| Notification | Event | Contents | 
| --- | --- | --- | 
| ELEMENTAL-MIB::alert | Any alert that worker nodes in the cluster generate. | + ELEMENTAL-MIB::alertSet: `1` if the alert is being set, `0` if the alert is being cleared.<br />+ ELEMENTAL-MIB::alertMessage: describes the alert that was set or cleared. | 

**To set up SNMP traps**

1. On the AWS Elemental Statmux web interface, go to the **Settings** page and choose **SNMP**.

1. On the **SNMP** page, complete the fields, using the instructions in the following table as a guide. Choose **Save**:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-statmux/latest/configguide/notification-trap.html)