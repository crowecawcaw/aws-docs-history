# Enable AMD SEV-SNP for an EC2 instance

You can launch an instance with AMD SEV-SNP enabled. You can't enable AMD SEV-SNP after launch.

## Launch an instance with AMD SEV-SNP enabled

You can't enable AMD SEV-SNP using the Amazon EC2 console.

AWS CLI

###### To launch an instance with AMD SEV-SNP enabled

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command with the `--cpu-options` option. For additional requirements, see
[AMD SEV-SNP requirements](sev-snp.md#snp-requirements "sev-snp.md#snp-requirements").

```
--cpu-options AmdSevSnp=enabled
```

PowerShell

###### To launch an instance with AMD SEV-SNP enabled

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the `-CpuOption` parameter.

```
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
