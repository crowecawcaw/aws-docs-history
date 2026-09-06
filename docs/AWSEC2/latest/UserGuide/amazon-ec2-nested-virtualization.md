

# Use nested virtualization to run hypervisors in Amazon EC2 instances
<a name="amazon-ec2-nested-virtualization"></a>

Nested virtualization allows you to run hypervisors such as Hyper-V and KVM inside virtual Amazon EC2 instances. Virtual EC2 instances are non-bare metal instances. This capability extends virtualization flexibility by adding processor-level virtualization support to virtual EC2 instances, enabling a hypervisor running in your instance to create and manage virtual machines.

Nested virtualization can help when you're running development tools like Docker Desktop, Windows Subsystem for Linux 2 (WSL2), Android Studio emulators, or QEMU in your development workflow, as it allows you to choose from a wide range of standard virtual Amazon EC2 instance types that meet your specific performance and price requirements.

There is no additional cost for using nested virtualization.

**Topics**
+ [How it works](#nested-virtualization-how-it-works)
+ [Considerations](#nested-virtualization-considerations)
+ [Launch a new instance with nested virtualization enabled](#nested-virtualization-launch-new-instance)
+ [Configure an existing instance to use nested virtualization](#nested-virtualization-configure-existing-instance)
+ [Find the instance types that support nested virtualization](#nested-virtualization-find-supported-instance-types)

## How it works
<a name="nested-virtualization-how-it-works"></a>

Virtual EC2 instances run on a physical host that has the Nitro hypervisor. To support nested virtualization, the Nitro System passes the processor extensions, such as Intel VT-x, to instances to facilitate running nested virtual machines. The nested virtualization architecture consists of three layers: the physical AWS infrastructure and Nitro hypervisor (L0), your EC2 instance running a hypervisor (L1), and one or more virtual machines created within that instance (L2).

## Considerations
<a name="nested-virtualization-considerations"></a>

Before you begin using nested virtualization, consider the following:
+ **Supported instance types** – Nested virtualization is currently supported on the following instance types:
  + **General Purpose**: M7i \| M7i-flex \| M8i \| M8id \| M8i-flex
  + **Compute Optimized**: C7i \| C7i-flex \| C8i \| C8id \| C8i-flex
  + **Memory Optimized**: R7i \| R7iz \| R8i \| R8id \| R8i-flex \| X8i
  + **Storage Optimized**: I7i \| I7ie
+ **Supported hypervisors** – Currently, KVM and Hyper-V are the supported L1 hypervisors.
+ **Windows instances** – When nested virtualization is enabled on a Windows instance:
  + **[Credential Guard](credential-guard.md)** – Virtual Secure Mode (VSM) is automatically disabled.
  + **Hibernation** – Instance hibernate and resume is not supported.
  + **CPU limit** – Not supported on Windows instances with more than 192 CPUs, such as `m8i.96xl`.
+ **Security responsibilities** – When using nested virtualization on EC2 instances, AWS is responsible for "security *of* the cloud," protecting the underlying infrastructure and maintaining the strong isolation boundaries between EC2 instances provided by the AWS Nitro System. Customers are responsible for "security *in* the cloud," which includes securing the operating system, hypervisor, nested virtual machines, guest operating systems, applications, and data within the EC2 instances.
+ **Performance** – AWS recommends that customers who want to run workloads that require access to hardware virtualization extensions, and are performance sensitive or have strict latency requirements, to evaluate bare metal instances.

## Launch a new instance with nested virtualization enabled
<a name="nested-virtualization-launch-new-instance"></a>

When you launch a new instance, you can turn on nested virtualization to run hypervisors and virtual machines on it.

------
#### [ Console ]

**To enable nested virtualization during instance launch**

1. Follow the [Launch an EC2 instance using the launch instance wizard in the console](ec2-launch-instance-wizard.md) procedure and configure your instance as needed.

1. Ensure a supported instance type is selected.

1. Expand **Advanced details**, and for **Nested virtualization**, choose **Enable**.

1. In the **Summary** panel, review your instance configuration, and then choose **Launch instance**.

------
#### [ AWS CLI ]

**To launch an instance with nested virtualization enabled**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command.

```
aws ec2 run-instances \
    --image-id {{ami-0abcdef1234567890}} \
    --instance-type {{r8i.4xlarge}} \
    --cpu-options "NestedVirtualization=enabled" \
    --key-name {{my-key-pair}}
```

------
#### [ PowerShell ]

**To launch an instance with nested virtualization enabled**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) command.

```
New-EC2Instance `
    -ImageId {{ami-0abcdef1234567890}} `
    -InstanceType {{r8i.4xlarge}} `
    -CpuOption @{NestedVirtualization='enabled'} `
    -KeyName {{my-key-pair}}
```

------

## Configure an existing instance to use nested virtualization
<a name="nested-virtualization-configure-existing-instance"></a>

You can turn on nested virtualization on an existing Amazon EC2 instance.

**Prerequisites**
+ The instance must be in a `stopped` state. 
+ The instance type must support nested virtualization.

------
#### [ Console ]

**To enable nested virtualization on an existing instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instance you want to modify from the instances table.

1. Choose **Actions**, **Instance settings**, **Change CPU options**.

1. On the **Change CPU options** page, for **Nested virtualization**, choose one of the following options:
   + **Enable** – Turns on nested virtualization for the instance
   + **Disable** – Turns off nested virtualization for the instance

1. Review your changes, and then choose **Change** to apply the new CPU options.

------
#### [ AWS CLI ]

**To enable nested virtualization on an existing instance**  
First stop the instance, and then use the [modify-instance-cpu-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-cpu-options.html) command.

```
aws ec2 modify-instance-cpu-options \
    --instance-id {{i-1234567890abcdef0}} \
    --core-count {{4}} \
    --threads-per-core {{2}} \
    --nested-virtualization enabled
```

------
#### [ PowerShell ]

**To enable nested virtualization on an existing instance**  
First stop the instance, and then use the [Edit-EC2InstanceCpuOption](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceCpuOption.html) command.

```
Edit-EC2InstanceCpuOption `
    -InstanceId {{i-1234567890abcdef0}} `
    -CoreCount {{4}} `
    -ThreadsPerCore {{2}} `
    -NestedVirtualization enabled
```

------

## Find the instance types that support nested virtualization
<a name="nested-virtualization-find-supported-instance-types"></a>

You can find which Amazon EC2 instance types support nested virtualization. You can query across an entire AWS Region or check a specific instance type.

------
#### [ AWS CLI ]

**To list all instance families that support nested virtualization in a Region**  
Use the [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html) command with the `processor-info.supported-features` filter set to the value of `nested-virtualization`:

```
aws ec2 describe-instance-types --region {{us-east-1}} \
  --filters "Name=processor-info.supported-features,Values=nested-virtualization" \
  --query "InstanceTypes[].InstanceType" --output text \
  | tr '\t' '\n' | cut -d. -f1 | sort -u
```

**To check whether a specific instance type supports nested virtualization**  
Use the [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html) command and query the `ProcessorInfo.SupportedFeatures` field of the specified instance type:

```
aws ec2 describe-instance-types \
  --instance-types {{m8i.2xlarge}} \
  --query "InstanceTypes[].ProcessorInfo.SupportedFeatures"
```

If the instance type supports nested virtualization, the output includes `nested-virtualization`. If not, the command returns an empty array (`[]`).

------
#### [ PowerShell ]

**To list all instance families that support nested virtualization in a Region**  
Use the [Get-EC2InstanceType](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceType.html) command with the `processor-info.supported-features` filter set to the value of `nested-virtualization`:

```
Get-EC2InstanceType -Region {{us-east-1}} -Filter @{ Name='processor-info.supported-features'; Values='nested-virtualization' } |
  ForEach-Object { ($_.InstanceType -split '\.')[0] } |
  Sort-Object -Unique
```

**To check whether a specific instance type supports nested virtualization**  
Use the [Get-EC2InstanceType](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceType.html) command and query the `ProcessorInfo.SupportedFeatures` property of the specified instance type:

```
(Get-EC2InstanceType -InstanceType {{m8i.2xlarge}}).ProcessorInfo.SupportedFeatures
```

If the instance type supports nested virtualization, the output includes `nested-virtualization`. If not, the command returns no output.

------