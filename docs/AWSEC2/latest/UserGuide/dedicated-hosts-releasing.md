

# Release an Amazon EC2 Dedicated Host
<a name="dedicated-hosts-releasing"></a>

If you no longer need Dedicated Host, you can stop the instances running on the host, direct them to launch on a different host, and then *release* the host.

Any running instances on the Dedicated Host must be stopped before you can release the host. These instances can be migrated to other Dedicated Hosts in your account so that you can continue to use them. These steps apply only to On-Demand Dedicated Hosts.

------
#### [ Console ]

**To release a Dedicated Host**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dedicated Hosts**.

1. On the **Dedicated Hosts** page, select the Dedicated Host to release.

1. Choose **Actions**, **Release host**.

1. To confirm, choose **Release**.

------
#### [ AWS CLI ]

**To release a Dedicated Host**  
Use the [release-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/release-hosts.html) command.

```
aws ec2 release-hosts --host-ids {{h-012a3456b7890cdef}}
```

------
#### [ PowerShell ]

**To release a Dedicated Host**  
Use the [Remove-EC2Host](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2Host.html) cmdlet.

```
Remove-EC2Host -HostId {{h-012a3456b7890cdef}}
```

------

After you release a Dedicated Host, you can't reuse the same host or host ID again, and you are no longer charged On-Demand billing rates for it. The state of the Dedicated Host is changed to `released`, and you are not able to launch any instances onto that host.

**Note**  
If you have recently released Dedicated Hosts, it can take some time for them to stop counting towards your limit. During this time, you might experience `LimitExceeded` errors when trying to allocate new Dedicated Hosts. If this is the case, try allocating new hosts again after a few minutes.

The instances that were stopped are still available for use and are listed on the **Instances** page. They retain their `host` tenancy setting.