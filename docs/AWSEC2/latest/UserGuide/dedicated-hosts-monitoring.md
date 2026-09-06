

# Monitor the state of your Amazon EC2 Dedicated Hosts
<a name="dedicated-hosts-monitoring"></a>

Amazon EC2 constantly monitors the state of your Dedicated Hosts. Updates are communicated on the Amazon EC2 console. You can view information about a Dedicated Host using the following methods.

------
#### [ Console ]

**To view the state of a Dedicated Host**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dedicated Hosts**.

1. Locate the Dedicated Host in the list and review the value in the **State** column.

------
#### [ AWS CLI ]

**To view the state of a Dedicated Host**  
Use the [describe-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-hosts.html) command.

```
aws ec2 describe-hosts --host-id {{h-012a3456b7890cdef}}
```

------
#### [ PowerShell ]

**To view the state of a Dedicated Host**  
Use the [Get-EC2Host](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Host.html) cmdlet.

```
Get-EC2Host -HostId {{h-012a3456b7890cdef}}
```

------

The following table explains the possible Dedicated Host states.


| **State** | **Description** | 
| --- | --- | 
| available | AWS hasn't detected an issue with the Dedicated Host. No maintenance or repairs are scheduled. Instances can be launched onto this Dedicated Host. | 
| released | The Dedicated Host has been released. The host ID is no longer in use. Released hosts can't be reused. | 
| under-assessment | AWS is exploring a possible issue with the Dedicated Host. If action must be taken, you are notified through the AWS Management Console or email. Instances can't be launched onto a Dedicated Host in this state. | 
| pending | The Dedicated Host can't be used for new instance launches. It is either being [ modified to support multiple instance types](modify-host-support.md), or a [host recovery](dedicated-hosts-recovery.md) is in progress. | 
| permanent-failure | An unrecoverable failure has been detected. You receive an eviction notice through your instances and by email. Your instances might continue to run. If you stop or terminate all instances on a Dedicated Host with this state, AWS retires the host. AWS does not restart instances in this state. Instances can't be launched onto Dedicated Hosts in this state. | 
| released-permanent-failure | AWS permanently releases Dedicated Hosts that have failed and no longer have running instances on them. The Dedicated Host ID is no longer available for use. | 