

# View CPU threads and cores for an Amazon EC2 instance
<a name="view-cpu-options"></a>

You can view the CPU options for an existing instance by describing the instance.

------
#### [ Console ]

**To view the CPU options for an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the left navigation pane, choose **Instances** and select the instance.

1. On the **Details** tab, under **Host and placement group**, find **Number of vCPUs**.

------
#### [ AWS CLI ]

**To view the CPU options for an instance**  
Use the [describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html) command.

```
aws ec2 describe-instances \
    --instance-ids {{i-1234567890abcdef0}} \
    --query Reservations[].Instances[].CpuOptions
```

The following is example output. The `CoreCount` field indicates the number of cores for the instance. The `ThreadsPerCore` field indicates the number of threads per core.

```
[
    {
        "CoreCount": 24, 
        "ThreadsPerCore": 2
    }, 
]
```

------
#### [ PowerShell ]

**To view the CPU options for an instance**  
Use the [Get-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Instance.html) cmdlet.

```
(Get-EC2Instance `
    -InstanceId '{{i-1234567890abcdef0}}').Instances.CpuOptions
```

The following is example output.

```
AmdSevSnp CoreCount ThreadsPerCore
--------- --------- --------------
          24        2
```

------

Alternatively, to view CPU information, you can connect to your instance and use one of the following system tools:
+ Windows `Task Manager` on your Windows instance
+ The **lscpu** command on your Linux instance

You can use AWS Config to record, assess, audit, and evaluate configuration changes for instances, including terminated instances. For more information, see [Getting Started with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) in the *AWS Config Developer Guide*.