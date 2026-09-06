

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Simple Network Management Protocol (SNMP) Traps
<a name="notification-trap"></a>

You can configure AWS Elemental Server to generate Simple Network Management Protocol (SNMPv2) traps for activity on the node. For information about the management information bases (MIBs) in AWS Elemental Server, go to the **Settings** page in the AWS Elemental Server web interface and choose **SNMP Interface**.

AWS Elemental Server generates traps for the events described in the following table.


| Notification | Event | Contents | 
| --- | --- | --- | 
| ELEMENTAL-MIB::alert | Any alert that worker nodes in the cluster generate. | + ELEMENTAL-MIB::alertSet: `1` if the alert is being set, `0` if the alert is being cleared.<br />+ ELEMENTAL-MIB::alertMessage: describes the alert that was set or cleared. | 

**To set up SNMP traps**

1. On the AWS Elemental Server web interface, go to the **Settings** page and choose **SNMP**.

1. On the **SNMP** page, complete the fields, using the instructions in the following table as a guide. Choose **Save**:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-server/latest/configguide/notification-trap.html)