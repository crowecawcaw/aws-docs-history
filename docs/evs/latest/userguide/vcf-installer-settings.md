

# VCF Installer settings for Amazon EVS

This page applies to Self-deployed environments that run VCF 9.x. For how EVS-deployed environments (VCF 5.2.x) differ, see [Differences between deployment modes](deployment-mode-differences.md).

When you install VMware Cloud Foundation (VCF) 9.x, you enter some settings in the VCF Installer that are specific to Amazon Elastic VMware Service. Both installation procedures in the Self-deployed path use these settings, one for hosts with local storage and one for diskless hosts. For the procedures, see [Step 4a (local storage): Prepare the VCF Installer](self-deployed-install-vcf.md) and [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).

The rest of the installation follows the standard Broadcom VCF process. For the installation mechanics, see the [Broadcom documentation for VMware Cloud Foundation 9.0](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0.html).

## Network settings
<a name="installer-settings-network"></a>

Amazon EVS assigns a VLAN ID to each network function in your environment. You use these VLAN IDs and the MTU values when you configure the distributed switch, port groups, and host networking during installation. For the VLAN subnets, how to find their VLAN IDs, and the MTU of each network function, see [VLAN subnets, VLAN IDs, and IP addresses](vlan-subnet-reference.md).

The following table lists the network settings that Amazon EVS requires in the VCF Installer. The columns show the setting, the value to use, and where you set it.


| Setting | Value | Where you set it | 
| --- | --- | --- | 
|  `VM Network` port group on the host that runs the VCF Installer | The VLAN ID of the VM management (`vmManagement`) network | VMware Host Client, before you deploy the VCF Installer appliance | 
|  `Management` port group on that host | Untagged, with VLAN ID `0`  | VMware Host Client | 
| VCF Installer appliance IP address | The SDDC Manager address from your DNS plan, because the appliance becomes SDDC Manager during bringup | VCF Installer OVA deployment | 
| Uplink teaming for distributed switch port groups | A failover teaming policy (an active uplink with a standby uplink), not a load-balancing policy | Deployment specification | 
| NSX teaming policy |  `FAILOVER_ORDER`  | Deployment specification | 

You don’t need to turn on SSH on the hosts. The VCF Installer migrates host networking to a distributed switch during bringup.

## Time (NTP) settings
<a name="installer-settings-ntp"></a>

You enter NTP servers in two places, when you deploy the VCF Installer OVA and in the deployment specification. You also set an NTP server in the DHCP option set of your VPC. For more information, see [Configure DNS and NTP with a DHCP option set](network-dhcp-dns-ntp.md).

Amazon EVS hosts use the link-local Amazon Time Sync Service address `169.254.169.123` as their NTP source. For diskless hosts, the specification example uses `time.aws.com`, and validation reports NTP warnings that you can acknowledge. For the list of warnings, see [Validate and deploy](deploy-diskless-spec.md#getting-started-diskless-deploy).

## Passwords
<a name="installer-settings-passwords"></a>

During installation, you set passwords for the VCF Installer appliance and the VCF management appliances. Each appliance enforces its own password complexity rules, which VCF defines. If an appliance rejects a password, the validation error states the rule that the password must meet.

When you deploy the VCF Installer OVA, the root user password and the local user password must be at least 15 characters long. They must contain an uppercase letter, a lowercase letter, a digit, and one of the special characters `! % @ $ ^ # ? *`.

The deployment specification also needs the ESX root password of each host. Amazon EVS stores the ESX root password of each host in AWS Secrets Manager. For more information, see [Get secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the * AWS Secrets Manager User Guide*.

## Broadcom online depot settings
<a name="installer-settings-depot"></a>

The VCF Installer downloads the VCF software from the Broadcom online depot. You connect it to the Broadcom online depot with a credential from your Broadcom account, and your Broadcom account must have a valid VCF entitlement.

The credential and the screens differ between VCF 9.0 and VCF 9.1. For the steps, see [Step 4a (local storage): Prepare the VCF Installer](self-deployed-install-vcf.md) for hosts with local storage or [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md) for diskless hosts.

The Broadcom online depot requires outbound internet access from the VCF Installer. The NAT gateway in your network foundation provides this access. For more information, see [Create a VPC with subnets and route tables](network-create-vpc.md).

The Amazon EVS custom add-on depot is separate from the Broadcom online depot. It provides the Amazon EVS add-on for ESX cluster images, and you don’t enter it in the VCF Installer during installation. For more information, see [Use the Amazon EVS custom add-on depot](addon-depot.md).

## Management cluster settings
<a name="installer-settings-cluster"></a>

When you configure the management cluster in the deployment specification, apply the following Amazon EVS-specific settings.

vSAN, for hosts with local storage  
Use vSAN Express Storage Architecture (ESA) with failures to tolerate (FTT) set to at least 1. Amazon EVS doesn’t support vSAN Original Storage Architecture (OSA). For more information, see [VCF feature support on Amazon EVS](vcf-feature-support.md).

Principal storage, for diskless hosts  
Diskless hosts have no local NVMe storage and don’t use vSAN. They use a datastore on external storage as principal storage. For more information, see [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).

EVC mode  
Set the cluster Enhanced vMotion Compatibility (EVC) mode to match your instance type. Use `INTEL_SAPPHIRERAPIDS` for `i7i.metal-24xl` and `i7i.metal-48xl`. For `i4i.metal`, don’t set an EVC mode, because setting `INTEL_ICELAKE` can cause bringup to fail on VCF 9.1. For `r7i.metal-24xl` diskless hosts, the hosts report Intel Sapphire Rapids as their highest EVC mode. The VCF Installer doesn’t apply the EVC mode to a diskless management cluster, so you set it after deployment. For more information, see [Verify the result](deploy-diskless-spec.md#getting-started-diskless-verify).

## Bringup validation settings
<a name="installer-settings-validation"></a>

Some standard VCF Installer validation checks don’t apply to the Amazon EVS network. For example, Amazon EVS VLAN subnet gateways don’t respond to ICMP ping from outside the subnet, so the gateway ping check fails even when routing is correct. How you handle these checks depends on whether you run bringup with a specification file or with the VCF Installer wizard. The following table lists the checks. The columns show the check and what to do in a specification file and in the wizard.


| Check | Specification file | Wizard | 
| --- | --- | --- | 
| Gateway ping validation | Set `skipGatewayPingValidation` to `true`. | Acknowledge the failed gateway ping check and continue. | 
| ESX host thumbprint validation | Set `skipEsxThumbprintValidation` to `true`, or get the correct thumbprints for all hosts and enter them in the specification. | Thumbprint validation is mandatory. Review and accept the thumbprint at the hosts step to continue. | 
| vSAN ESA certified disk validation (hosts with local storage) | Set `skipVsanEsaCertifiedDiskValidation` to `true`. The Amazon EC2 instance store NVMe disks aren’t on the vSAN ESA certified disk list, so this check can fail. | If the wizard reports a failed disk check that you can’t acknowledge, run bringup with a specification file. | 

When you run bringup through the VCF Installer wizard, use the wizard to find and correct errors in the specification. The wizard shows validation problems more clearly than the API, whose errors are less descriptive.

To generate an example bringup specification, use the [spec-generator tool](https://github.com/aws/solutions-for-amazon-evs/tree/main/Deploy/EVS-Deployment-Orchestrator/spec-generator) in the `Deploy` folder of the [Solutions for Amazon EVS](https://github.com/aws/solutions-for-amazon-evs) repository on GitHub.

## Support boundaries
<a name="installer-settings-support"></a>

Amazon EVS doesn’t support running ESX outside of a full VCF deployment. VMware workload virtual machines must be deployed onto NSX overlay networks.

**Important**  
In Self-deployed mode, Amazon EVS doesn’t manage the VCF installation. For VCF-specific requests, you can use your active VCF subscription entitlements to contact Broadcom through the Broadcom Support Portal. For more information, see [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).