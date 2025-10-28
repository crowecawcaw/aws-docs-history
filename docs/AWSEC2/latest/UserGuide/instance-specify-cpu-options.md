# Specify CPU options for an Amazon EC2

instance

You can specify CPU options during or after instance launch.

###### Tasks

- [Disable
  simultaneous multithreading](#cpu-options-disable-simultaneous-multithreading "#cpu-options-disable-simultaneous-multithreading")
- [Specify a custom number of
  vCPUs at launch](#cpu-options-customize-vCPUs-launch "#cpu-options-customize-vCPUs-launch")
- [Specify a custom
  number of vCPUs in a launch template](#cpu-options-customize-vCPUs-launch-template "#cpu-options-customize-vCPUs-launch-template")
- [Change CPU options for your EC2 instance](#change-vCPUs-after-launch "#change-vCPUs-after-launch")

## Disable

simultaneous multithreading

To disable simultaneous multithreading (SMT), also known as hyper-threading,
specify 1 thread per core.

Console

###### To disable SMT during instance launch

1. Follow the [Launch an EC2 instance using the launch
   instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md") procedure and
   configure your instance as needed.
2. Expand **Advanced details**, and select the
   **Specify CPU options** checkbox.
3. For **Core count**, choose the number of
   required CPU cores. In this example, to specify the default CPU
   core count for an `r5.4xlarge` instance, choose
   `8`.
4. To disable SMT, for **Threads per core**,
   choose **1**.
5. In the **Summary** panel, review your
   instance configuration, and then choose **Launch
   instance**. For more information, see [Launch an EC2 instance using the launch
   instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

AWS CLI

###### To disable SMT during instance launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") AWS CLI command and specify a value of
`1` for `ThreadsPerCore` for the
`--cpu-options` parameter. For
`CoreCount`, specify the number of CPU cores. In this
example, to specify the default CPU core count for an
`r7i.4xlarge` instance, specify a value of
`8`.

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --instance-type `r7i.4xlarge` \
    --cpu-options "CoreCount=`8`,ThreadsPerCore=`1`" \
    --key-name `my-key-pair`
```

PowerShell

###### To disable SMT during instance launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") command and specify a value of
`1` for `ThreadsPerCore` for the
`-CpuOptions` parameter. For
`CoreCount`, specify the number of CPU cores. In this
example, to specify the default CPU core count for an
`r7i.4xlarge` instance, specify a value of
`8`.

```
New-EC2Instance `
    -ImageId '`ami-0abcdef1234567890`' `
    -InstanceType '`r7i.4xlarge`' `
    -CpuOptions @{CoreCount=`8`; ThreadsPerCore=`1`} `
    -KeyName '`my-key-pair`'
```

###### Note

To disable SMT for an existing instance, follow the process shown in [Change CPU options for your EC2 instance](#change-vCPUs-after-launch "#change-vCPUs-after-launch"), and change the number of
threads that run per core to `1`.

## Specify a custom number of

vCPUs at launch

You can customize the number of CPU cores and threads per core when you launch an
instance from the EC2 console or AWS CLI. The examples in this section use an
`r5.4xlarge` instance type, which has the following default
settings:

- CPU cores: 8
- Threads per core: 2

Instances launch with the maximum number of vCPUs available for the instance type
by default. For this instance type, that's 16 total vCPUs (8 cores running 2 threads
each). For more information about this instance type, see [Memory optimized instances](cpu-options-supported-instances-values.md#cpu-options-mem-optimized "cpu-options-supported-instances-values.md#cpu-options-mem-optimized").

The following example launches an `r5.4xlarge` instance with 4
vCPUs.

Console

###### To specify a custom number of vCPUs during instance

launch

1. Follow the [Launch an EC2 instance using the launch
   instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md") procedure and
   configure your instance as needed.
2. Expand **Advanced details**, and select the
   **Specify CPU options** checkbox.
3. To get 4 vCPUs, specify 2 CPU cores and 2 threads per core, as
   follows:
   - For **Core count**, choose
     **2**.
   - For **Threads per core**, choose
     **2**.

4. In the **Summary** panel, review your
   instance configuration, and then choose **Launch
   instance**. For more information, see [Launch an EC2 instance using the launch
   instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

AWS CLI

###### To specify a custom number of vCPUs during instance

launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") AWS CLI command and specify the number of
CPU cores and number of threads in the `--cpu-options`
parameter. You can specify 2 CPU cores and 2 threads per core to get
4 vCPUs.

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --instance-type `r7i.4xlarge` \
    --cpu-options "CoreCount=`2`,ThreadsPerCore=`2`" \
    --key-name `my-key-pair`
```

Alternatively, specify 4 CPU cores and 1 thread per core (disable SMT)
to get 4 vCPUs:

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --instance-type `r7i.4xlarge` \
    --cpu-options "CoreCount=`4`,ThreadsPerCore=`1`" \
    --key-name `my-key-pair`
```

PowerShell

###### To specify a custom number of vCPUs during instance

launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") command and specify the number of
CPU cores and number of threads in the `-CpuOptions`
parameter. You can specify 2 CPU cores and 2 threads per core to get
4 vCPUs.

```
New-EC2Instance `
    -ImageId '`ami-0abcdef1234567890`' `
    -InstanceType '`r7i.4xlarge`' `
    -CpuOptions @{CoreCount=`2`; ThreadsPerCore=`2`} `
    -KeyName '`my-key-pair`'
```

Alternatively, specify 4 CPU cores and 1 thread per core (disable SMT)
to get 4 vCPUs:

```
New-EC2Instance `
    -ImageId '`ami-0abcdef1234567890`' `
    -InstanceType '`r7i.4xlarge`' `
    -CpuOptions @{CoreCount=`4`; ThreadsPerCore=`1`} `
    -KeyName '`my-key-pair`'
```

## Specify a custom

number of vCPUs in a launch template

You can customize the number of CPU cores and threads per core for the instance in
a launch template. The examples in this section use an `r5.4xlarge`
instance type, which has the following default settings:

- CPU cores: 8
- Threads per core: 2

Instances launch with the maximum number of vCPUs available for the instance type
by default. For this instance type, that's 16 total vCPUs (8 cores running 2 threads
each). For more information about this instance type, see [Memory optimized instances](cpu-options-supported-instances-values.md#cpu-options-mem-optimized "cpu-options-supported-instances-values.md#cpu-options-mem-optimized").

The following example creates a launch template that specifies the configuration
for an `r5.4xlarge` instance with 4 vCPUs.

Console

###### To specify a custom number of vCPUs in a launch template

1. Follow the [Create a launch template
   by specifying parameters](create-launch-template.md#create-launch-template-define-parameters "create-launch-template.md#create-launch-template-define-parameters")
   procedure and configure your launch template as needed.
2. Expand **Advanced details**, and select the
   **Specify CPU options** checkbox.
3. To get 4 vCPUs, specify 2 CPU cores and 2 threads per core, as
   follows:
   - For **Core count**, choose
     **2**.
   - For **Threads per core**, choose
     **2**.

4. In the **Summary** panel, review your
   instance configuration, and then choose **Create launch
   template**. For more information, see [Store instance launch parameters in Amazon EC2 launch templates](ec2-launch-templates.md "ec2-launch-templates.md").

AWS CLI

###### To specify a custom number of vCPUs in a launch template

Use the [create-launch-template](../../../cli/latest/reference/ec2/create-launch-template.md "../../../cli/latest/reference/ec2/create-launch-template.md") AWS CLI command and specify the
number of CPU cores and number of threads in the
`CpuOptions` parameter. You can specify 2 CPU cores
and 2 threads per core to get 4 vCPUs.

```
aws ec2 create-launch-template \
    --launch-template-name `TemplateForCPUOptions` \
    --version-description `CPUOptionsVersion1` \
    --launch-template-data file://`template-data`.json
```

The following is an example JSON file that contains the launch
template data, which includes the CPU options, for the instance
configuration for this example.

```
{
    "NetworkInterfaces": [{
        "AssociatePublicIpAddress": true,
        "DeviceIndex": 0,
        "Ipv6AddressCount": 1,
        "SubnetId": "`subnet-0abcdef1234567890`"
    }],
    "ImageId": "`ami-0abcdef1234567890`",
    "InstanceType": "`r5.4xlarge`",
    "TagSpecifications": [{
        "ResourceType": "instance",
        "Tags": [{
            "Key":"`Name`",
            "Value":"`webserver`"
        }]
    }],
    "CpuOptions": {
        "CoreCount":`2`,
        "ThreadsPerCore":`2`
    }
}
```

Alternatively, specify 4 CPU cores and 1 thread per core (disable SMT)
to get 4 vCPUs:

```
{
    "NetworkInterfaces": [{
        "AssociatePublicIpAddress": true,
        "DeviceIndex": 0,
        "Ipv6AddressCount": 1,
        "SubnetId": "`subnet-0abcdef1234567890`"
    }],
    "ImageId": "`ami-0abcdef1234567890`",
    "InstanceType": "`r5.4xlarge`",
    "TagSpecifications": [{
        "ResourceType": "instance",
        "Tags": [{
            "Key":"`Name`",
            "Value":"`webserver`"
        }]
    }],
    "CpuOptions": {
        "CoreCount":`4`,
        "ThreadsPerCore":`1`
    }
}
```

PowerShell

###### To specify a custom number of vCPUs in a launch template

Use the [New-EC2LaunchTemplate](../../../powershell/latest/reference/items/New-EC2LaunchTemplate.md "../../../powershell/latest/reference/items/New-EC2LaunchTemplate.md").

```
New-EC2LaunchTemplate `
    -LaunchTemplateName '`TemplateForCPUOptions`' `
    -VersionDescription '`CPUOptionsVersion1`' `
    -LaunchTemplateData (Get-Content -Path '`template-data.json`' | ConvertFrom-Json)
```

## Change CPU options for your EC2 instance

As your needs change over time, you might want to change the configuration of CPU options
for an existing instance. Each thread that runs on your instance is known as a virtual CPU (vCPU).
You can change the number of vCPUs that run for an existing instance in the Amazon EC2 console, AWS CLI,
API, or SDKs. The instance state must be `Stopped` before you can make this change.

To view console or command line steps, select the tab that matches your environment. For API
request and response information, see [ModifyInstanceCpuOptions](../APIReference/API_ModifyInstanceCpuOptions.md "../APIReference/API_ModifyInstanceCpuOptions.md") in the _Amazon EC2 API Reference_.

Console
Follow this procedure to change the number of active vCPUs for your instance from
the AWS Management Console.

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **Instances**.
   This opens the list of instances that are defined for the current AWS Region.
3. Select the instance from the **Instances** list. Alternatively,
   you can select the instance link to open the instance detail page.
4. If the instance is running, you must stop it before you proceed. Choose
   **Stop instance** from the **Instance state**
   menu.
5. To change the vCPU configuration, choose **Change CPU options**
   from **Instance settings** in the **Actions** menu.
   This opens the **Change CPU options** page.
6. Choose one of the following CPU options to change the configuration for your instance.

**Use default CPU options**

This option resets your instance to the default number of vCPUs
for the instance type. The default is to run all threads for all
CPU cores.

**Specify CPU options**

This option enables configuration of the number of vCPUs that are
running on your instance. 7. If you chose **Specify CPU options**, the
**Active vCPUs** fields are displayed.

    * Use the first selector to configure the number of
     threads for each CPU core. To disable simultaneous
     multithreading, choose `1`.
    * Use the second selector to configure the number of
     CPUs that run on your instance.

The following fields dynamically update as you make changes to the CPU
option selectors.

    * **Active vCPUs**: The number of CPU cores multiplied
     by the threads per core, based on the selections that you made. For example,
     if you selected 2 threads and 4 cores, that would equal 8 vCPUs.
    * **Total vCPUs**: The maximum number of vCPUs for
     the instance type. For example, for an `m6i.4xlarge` instance
     type, this is 16 vCPUs (8 cores running 2 threads each).

8. To apply your updates, choose **Change**.

AWS CLI
Follow this procedure to change the number of active vCPUs for your instance from
the AWS CLI.

Use the [modify-instance-cpu-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-cpu-options.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-cpu-options.html") command and specify the number of CPU cores
that run in the `--core-count` parameter, and the number of threads that
run per core in the `--threads-per-core` parameter.

The following examples show two possible configurations on an `m6i.4xlarge`
instance type to run 8 vCPUs on the specified instance. The default for this instance type
is 16 vCPUs (8 cores running 2 threads each).

**Example 1:** Run 4 CPU cores with 2 threads per core, for
a total of 8 vCPU.

```
aws ec2 modify-instance-cpu-options \
    --instance-id `i-1234567890abcdef0` \

    --core-count=`4` \
    --threads-per-core=`2`
```

**Example 2:** Disable simultaneous
multi-threading by changing the number of threads that run per core to
`1`. The resulting configuration also runs a total of 8
vCPUs (8 CPU cores with 1 thread per core).

```
aws ec2 modify-instance-cpu-options \
    --instance-id `1234567890abcdef0` \
    --core-count=`8` \
    --threads-per-core=`1`
```

PowerShell

###### To change the number of active vCPUs for an instance

Use the [Edit-EC2InstanceCpuOption](../../../powershell/latest/reference/items/Edit-EC2InstanceCpuOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceCpuOption.md") cmdlet and specify the number
of CPU cores that run in the `-CoreCount` parameter, and
the number of threads that run per core in the
`ThreadsPerCore` parameter.

**Example 1:** Run 4 CPU cores with 2
threads per core, for a total of 8 vCPU.

```
Edit-EC2InstanceCpuOption `
    -InstanceId '`i-1234567890abcdef0`' `
    -CoreCount 4 `
    -ThreadsPerCore 2
```

**Example 2:** Disable simultaneous
multi-threading by changing the number of threads that run per core to
`1`. The resulting configuration also runs a total of 8
vCPUs (8 CPU cores with 1 thread per core).

```
Edit-EC2InstanceCpuOption `
    -InstanceId '`i-1234567890abcdef0`' `
    -CoreCount 8 `
    -ThreadsPerCore 1
```
