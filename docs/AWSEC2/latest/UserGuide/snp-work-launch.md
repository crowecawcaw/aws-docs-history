# Enable AMD SEV-SNP for an EC2 instance

You can launch an instance with AMD SEV-SNP enabled. You can't enable AMD SEV-SNP after launch.

###### Contents

- [Allocate a Dedicated Host with AMD SEV-SNP](#snp-allocate-dh "#snp-allocate-dh")
- [Launch instances on a AMD SEV-SNP Dedicated Host](#snp-launch-instance "#snp-launch-instance")
- [Update firmware on a AMD SEV-SNP Dedicated Host](#snp-firmware "#snp-firmware")
- [Launch an instance with AMD SEV-SNP on shared tenancy](#snp-shared-tenancy "#snp-shared-tenancy")
- [Check if an EC2 instance is enabled for AMD SEV-SNP](#snp-work-check "#snp-work-check")

## Allocate a Dedicated Host with AMD SEV-SNP

Before you can launch instances with AMD SEV-SNP on a Dedicated Host, you must allocate a Dedicated Host
with AMD SEV-SNP support enabled. You allocate a Dedicated Host by instance family (for example,
m6a, r6a, or c6a), and then you can run any supported instance type from that family
on the host. You can allocate a Dedicated Host with AMD SEV-SNP in any commercial
AWS Region.

Console

###### To allocate a Dedicated Host with AMD SEV-SNP enabled

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Dedicated Hosts**.
3. Choose **Allocate Dedicated Host**.
4. For **AMD SEV-SNP**, choose
   **Enable**.
5. Configure the remaining host settings as needed, and then choose
   **Allocate**.

AWS CLI

###### To allocate a Dedicated Host with AMD SEV-SNP enabled

Use the [allocate-hosts](../../../cli/latest/reference/ec2/allocate-hosts.md "../../../cli/latest/reference/ec2/allocate-hosts.md") command with the
`--instance-type` and `--cpu-options`
parameters.

```
aws ec2 allocate-hosts \
    --instance-type "`m6a.large`" \
    --availability-zone "`us-east-1a`" \
    --auto-placement "off" \
    --cpu-options AmdSevSnp=enabled \
    --quantity 1
```

The following is example output.

```
{
    "HostIds": [
        "h-0123456789abcdef0"
    ]
}
```

###### Note

When you allocate a Dedicated Host with AMD SEV-SNP enabled, the host enters a
`configuring` state while AWS applies the latest firmware. This
can take from a few minutes up to 2 hours. You are charged during the
`configuring` state.

## Launch instances on a AMD SEV-SNP Dedicated Host

You can launch an instance with AMD SEV-SNP enabled after the Dedicated Host is
configured.

###### Note

You can also launch instances without AMD SEV-SNP enabled on a Dedicated Host that was
allocated with AMD SEV-SNP. Both AMD SEV-SNP and non-AMD SEV-SNP instances can run
alongside each other on the same host.

AWS CLI

###### To launch an instance with AMD SEV-SNP on a Dedicated Host

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command with the `--cpu-options` and `--placement` options.
Replace `h-0123456789abcdef0` with the ID of your
allocated Dedicated Host.

```
aws ec2 run-instances \
    --instance-type `m6a.xlarge` \
    --image-id `ami-0123456789example` \
    --cpu-options AmdSevSnp=enabled \
    --placement HostId=`h-0123456789abcdef0`
```

PowerShell

###### To launch an instance with AMD SEV-SNP on a Dedicated Host

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the `-CpuOption` and `-Placement_HostId`
parameters.

```
New-EC2Instance `
    -InstanceType `m6a.xlarge` `
    -ImageId `ami-0123456789example` `
    -CpuOption @{AmdSevSnp="enabled"} `
    -Placement_HostId `h-0123456789abcdef0`
```

## Update firmware on a AMD SEV-SNP Dedicated Host

When you allocate a Dedicated Host with AMD SEV-SNP enabled, AWS applies the latest available
firmware to the host. Firmware updates can include security patches and feature
improvements from AMD.

To apply firmware updates, allocate a new host (which receives the latest firmware),
move your instances to the new host, and then release the old host.

1. Allocate a new Dedicated Host with AMD SEV-SNP enabled. The new host receives the latest
   available firmware. For more information, see
   [Allocate a Dedicated Host with AMD SEV-SNP](#snp-allocate-dh "#snp-allocate-dh").
2. Stop the running instances on the old Dedicated Host.

```
aws ec2 stop-instances \
    --instance-ids `i-0123456789example`
```

3. Modify the instance placement to target the new Dedicated Host. Use the
   [modify-instance-placement](../../../cli/latest/reference/ec2/modify-instance-placement.md "../../../cli/latest/reference/ec2/modify-instance-placement.md") command.

```
aws ec2 modify-instance-placement \
    --instance-id `i-0123456789example` \
    --host-id `h-09876543210abcdef`
```

4. Start the instances on the new Dedicated Host.

```
aws ec2 start-instances \
    --instance-ids `i-0123456789example`
```

5. Release the old Dedicated Host. Use the [release-hosts](../../../cli/latest/reference/ec2/release-hosts.md "../../../cli/latest/reference/ec2/release-hosts.md") command.

```
aws ec2 release-hosts \
    --host-ids `h-0123456789abcdef0`
```

###### Note

You receive maintenance notifications for your Dedicated Hosts the same way you receive them
for other Dedicated Host maintenance events. When you receive a notification, follow the
preceding steps to move to a new host with updated firmware.

## Launch an instance with AMD SEV-SNP on shared tenancy

You can launch an instance with AMD SEV-SNP on shared tenancy in US East (Ohio)
and Europe (Ireland).

AWS CLI

###### To launch an instance with AMD SEV-SNP on shared tenancy

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command with the `--cpu-options` option.

```
aws ec2 run-instances \
    --instance-type `m6a.xlarge` \
    --image-id `ami-0123456789example` \
    --cpu-options AmdSevSnp=enabled
```

PowerShell

###### To launch an instance with AMD SEV-SNP on shared tenancy

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the `-CpuOption` parameter.

```
New-EC2Instance `
    -InstanceType `m6a.xlarge` `
    -ImageId `ami-0123456789example` `
    -CpuOption @{AmdSevSnp="enabled"}
```

## Check if an EC2 instance is enabled for AMD SEV-SNP

You can find instances that are enabled for AMD SEV-SNP. The Amazon EC2 console does not display
this information.

AWS CLI

###### To check whether AMD SEV-SNP is enabled for an instance

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
    --query Reservations[].Instances[].CpuOptions
```

The following is example output. If `AmdSevSnp` is not present
in `CpuOptions`, then AMD SEV-SNP is disabled.

```
[
    {
        "AmdSevSnp": "enabled",
        "CoreCount": 1,
        "ThreadsPerCore": 2
    }
]
```

PowerShell

###### To check whether AMD SEV-SNP is enabled for an instance

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
cmdlet.

```
(Get-EC2Instance `
    -InstanceId `i-1234567890abcdef0`).Instances.CpuOptions
```

The following is example output. If the value of `AmdSevSnp`
is not present, then AMD SEV-SNP is disabled.

```
AmdSevSnp CoreCount ThreadsPerCore
--------- --------- --------------
enabled   1         2
```

AWS CloudTrail
In the AWS CloudTrail event for the instance launch request, the following property
indicates that AMD SEV-SNP is enabled for the instance.

```
"cpuOptions": {"AmdSevSnp": "enabled"}
```
