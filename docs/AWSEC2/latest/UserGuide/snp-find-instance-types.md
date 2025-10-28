# Find EC2 instance types that support AMD SEV-SNP

You can find instance types that support AMD SEV-SNP. The Amazon EC2 console
does not display this information for an instance type.

AWS CLI

###### To find the instance types that support AMD SEV-SNP

Use the following [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command.

```
aws ec2 describe-instance-types \
    --filters Name=processor-info.supported-features,Values=amd-sev-snp \
    --query 'InstanceTypes[*].[InstanceType]' \
    --output text | sort
```

The following is example output.

```
c6a.12xlarge
c6a.16xlarge
c6a.2xlarge
c6a.4xlarge
c6a.8xlarge
c6a.large
c6a.xlarge
m6a.2xlarge
m6a.4xlarge
m6a.8xlarge
m6a.large
m6a.xlarge
r6a.2xlarge
r6a.4xlarge
r6a.large
r6a.xlarge
```

PowerShell

###### To find the instance types that support AMD SEV-SNP

Use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md")
cmdlet.

```
(Get-EC2InstanceType `
    -Filter @{Name="processor-info.supported-features"; Values="amd-sev-snp"}).InstanceType.Value | Sort-Object
```

The following is example output.

```
c6a.12xlarge
c6a.16xlarge
c6a.2xlarge
c6a.4xlarge
c6a.8xlarge
c6a.large
c6a.xlarge
m6a.2xlarge
m6a.4xlarge
m6a.8xlarge
m6a.large
m6a.xlarge
r6a.2xlarge
r6a.4xlarge
r6a.large
r6a.xlarge
```
