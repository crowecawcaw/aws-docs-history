

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Set up Systems Manager for Microsoft Azure virtual machines
<a name="hybrid-multicloud-ssm-agent-install-azure"></a>

You can register Azure virtual machines (VMs) as Systems Manager managed nodes using the hybrid activation process with native Azure Instance Metadata Service (IMDS) integration. When you specify the `-provider Azure` parameter during registration, SSM Agent reads Azure VM identity data directly from the Azure IMDS endpoint and associates the managed node with the source Azure VM.

This integration provides the following benefits:
+ **Instance identity association**: The SSM managed node (mi-) is automatically linked to the Azure VM ID, enabling consistent resource tracking across clouds.
+ **Rich metadata collection**: Azure VM properties such as subscription ID, resource group, location, and availability zone are captured and surfaced as managed node attributes.
+ **Enhanced security**: Explicit provider designation prevents IMDS impersonation attacks and ensures credentials are scoped to the correct cloud provider.

**Note**  
Before you begin, complete the prerequisite steps to create an IAM service role and a hybrid activation, as described in [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md) and [Create a hybrid activation to register nodes with Systems Manager](hybrid-activation-managed-nodes.md).

## Install SSM Agent on Azure Linux VMs
<a name="hybrid-multicloud-ssm-agent-install-azure-linux"></a>

Use the following procedure to install and register SSM Agent on an Azure Linux VM.

**To install SSM Agent on an Azure Linux VM**

1. Connect to your Azure VM.

1. Run the following commands. Replace the placeholder values with the Activation Code and Activation ID generated during the hybrid activation process, and with the identifier of the AWS Region you want to use.
**Note**  
The following command uses the `linux_amd64` binary. If your Azure VM uses an ARM64 processor (for example, Dpsv5 or Epsv5 series), replace `linux_amd64` with `linux_arm64`.

   ```
   mkdir /tmp/ssm
   curl https://amazon-ssm-{{region}}.s3.{{region}}.amazonaws.com/latest/linux_amd64/ssm-setup-cli -o /tmp/ssm/ssm-setup-cli
   sudo chmod +x /tmp/ssm/ssm-setup-cli
   sudo /tmp/ssm/ssm-setup-cli -register \
       -activation-code "{{activation-code}}" \
       -activation-id "{{activation-id}}" \
       -region "{{region}}" \
       -provider Azure
   ```

1. Verify that SSM Agent is running and that the registration data was written correctly:

   ```
   sudo systemctl status amazon-ssm-agent
   cat /var/lib/amazon/ssm/registration
   ```

## Install SSM Agent on Azure Windows Server VMs
<a name="hybrid-multicloud-ssm-agent-install-azure-windows"></a>

Use the following procedure to install and register SSM Agent on an Azure Windows Server VM.

**To install SSM Agent on an Azure Windows Server VM**

1. Connect to your Azure VM.

1. Open Windows PowerShell in elevated (administrative) mode.

1. Copy and paste the following command block into Windows PowerShell. Replace each {{example resource placeholder}} with your own information.
**Note**  
The following command uses the `windows_amd64` binary. If your Azure VM uses an ARM64 processor, replace `windows_amd64` with `windows_arm64`.

   ```
   [System.Net.ServicePointManager]::SecurityProtocol = 'TLS12'
   $code = "{{activation-code}}"
   $id = "{{activation-id}}"
   $region = "{{us-east-1}}"
   $dir = $env:TEMP + "\ssm"
   New-Item -ItemType directory -Path $dir -Force
   cd $dir
   (New-Object System.Net.WebClient).DownloadFile("https://amazon-ssm-$region.s3.$region.amazonaws.com/latest/windows_amd64/ssm-setup-cli.exe", $dir + "\ssm-setup-cli.exe")
   Start-Process ./ssm-setup-cli.exe -ArgumentList @(
       "-register",
       "-activation-code=$code",
       "-activation-id=$id",
       "-region=$region",
       "-provider=Azure"
   ) -Wait -NoNewWindow
   Get-Content ($env:ProgramData + "\Amazon\SSM\InstanceData\registration")
   Get-Service -Name "AmazonSSMAgent"
   ```

## Azure VM metadata mapping
<a name="hybrid-multicloud-ssm-agent-install-azure-metadata-mapping"></a>

When you register an Azure VM using the `-provider Azure` parameter, SSM Agent reads the following properties from the Azure IMDS endpoint (`http://169.254.169.254/metadata/instance`) and maps them to the corresponding Systems Manager managed node attributes.


| Managed node property | Azure IMDS field | Example value | 
| --- | --- | --- | 
| ComputerName | {compute.subscriptionId}:{compute.resourceGroupName}:{compute.name} | 14724fea-7bad-4c32-8af0-ebde38f42a46:MyRG:my-azure-vm | 
| SourceType | Hardcoded | Microsoft.Compute/virtualMachines | 
| SourceID | {compute.vmId} | 1724afd8-9092-429e-8b04-0708130c38f7 | 
| SourceLocation | {compute.location} | centralus | 
| AvailabilityZone | {compute.zone} | 1 | 
| AvailabilityZoneId | Zone{compute.zone} | Zone1 | 

**Verify the managed node registration using DescribeInstanceInformation**  
After registration, use the [describe-instance-information](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-information.html) command to confirm that the Azure VM metadata was captured correctly. The following example filters by `SourceId` using the Azure VM ID:

```
aws ssm describe-instance-information \
    --filters "Key=SourceIds,Values={{1724afd8-9092-429e-8b04-0708130c38f7}}" \
    --region {{us-east-1}}
```

The response includes the managed node ID (prefixed with `mi-`) and the populated metadata fields such as `ComputerName`, `SourceId`, and `SourceType`:

```
{
    "InstanceInformationList": [
        {
            "InstanceId": "mi-008d36be46EXAMPLE",
            "ComputerName": "14724fea-7bad-4c32-8af0-ebde38f42a46:MyRG:my-azure-vm",
            "SourceId": "1724afd8-9092-429e-8b04-0708130c38f7",
            "SourceType": "Microsoft.Compute/virtualMachines",
            "SourceLocation": "centralus",
            "AvailabilityZone": "1",
            "AvailabilityZoneId": "Zone1",
            "PingStatus": "Online",
            "PlatformType": "Linux",
            "PlatformName": "Ubuntu",
            "PlatformVersion": "24.04"
        }
    ]
}
```