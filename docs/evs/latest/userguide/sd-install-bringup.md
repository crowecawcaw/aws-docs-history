

# Step 4b (local storage): Run VCF bringup

With the VMware Cloud Foundation (VCF) software downloaded, you create your VCF deployment specification, validate it, and run the deployment in the VCF Installer. Bringup deploys the VCF management appliances and creates the vSAN datastore. After bringup, you reclaim the temporary datastore.

Use these steps for hosts with local storage that use vSAN. For diskless hosts, see [Step 4b (diskless): Create the specification and deploy](deploy-diskless-spec.md).

**Important**  
In Self-deployed mode, Amazon Elastic VMware Service doesn’t manage VCF installation. For VCF-specific requests, you can use your active VCF subscription entitlements to contact Broadcom directly through the Broadcom Support Portal. For more information about support boundaries, see [Shared responsibility and support](plan-shared-responsibility.md).

Before you begin, complete [Step 4a (local storage): Prepare the VCF Installer](self-deployed-install-vcf.md).

## Amazon EVS settings for the management cluster
<a name="sd-install-bringup-settings"></a>

When you configure the management cluster in the deployment specification, apply these Amazon EVS-specific settings.

 **vSAN**   
Use vSAN ESA (Express Storage Architecture) with failures to tolerate (FTT) set to at least 1. Amazon EVS doesn’t support vSAN OSA (Original Storage Architecture).

 **Uplink teaming**   
Use a failover teaming policy (an active uplink with a standby uplink) for the distributed switch port groups, rather than a load-balancing policy. Set the NSX teaming policy to `FAILOVER_ORDER`.

 **EVC mode**   
Set the cluster Enhanced vMotion Compatibility (EVC) mode to match your instance type. For `i7i.metal-24xl` and `i7i.metal-48xl`, use `INTEL_SAPPHIRERAPIDS`. For `i4i.metal`, don’t set an EVC mode in the specification. The EVS Deployment Orchestrator (EDO) leaves it unset for this instance type, because setting `INTEL_ICELAKE` can cause bringup to fail on VCF 9.1.

 **Networks**   
Use the Amazon EVS-assigned VLAN IDs and the MTU values in [Amazon EVS network settings for VCF](self-deployed-install-vcf.md#sd-install-network).

 **Passwords**   
Set the passwords for the VCF management appliances. Each appliance enforces its own password complexity requirements, which VCF defines. If an appliance rejects a password, the validation error states the requirement that the password must meet. For the password rules, see [VCF Installer settings for Amazon EVS](vcf-installer-settings.md).

## Run bringup
<a name="sd-install-bringup-run"></a>

**Important**  
Amazon EVS doesn’t support running ESX outside of a full VCF deployment, or workload virtual machines on the Amazon EVS VLAN subnets (the underlay). Deploy workload virtual machines onto NSX overlay networks. For more information, see [Amazon EVS architecture](architecture.md).

To run bringup, do the following.

1. In the VCF Installer, create the deployment specification for your management domain. Apply the Amazon EVS-specific settings in the previous section.

1. Run validation against the specification, and resolve any errors that it reports. Some standard VCF Installer validation checks don’t apply to the Amazon EVS network environment, such as the gateway ping check, the ESX host thumbprint check, and, on hosts with local storage, the vSAN ESA certified disk check. For how to handle them, see [VCF Installer settings for Amazon EVS](vcf-installer-settings.md).

1. Run the deployment.

Bringup is the longest part of the installation and accounts for most of the setup time. When you use vSAN, forming the datastore and deploying the management appliances can take several hours.

**Tip**  
When you run bringup through the VCF Installer wizard, use the wizard to identify and correct specification errors. The wizard shows validation problems more clearly than the API. To generate an example bringup specification, use the [spec-generator tool](https://github.com/aws/solutions-for-amazon-evs/tree/main/Deploy/EVS-Deployment-Orchestrator/spec-generator) in the `Deploy` folder of the [Solutions for Amazon EVS](https://github.com/aws/solutions-for-amazon-evs) repository on GitHub.

## Reclaim the temporary datastore
<a name="sd-install-reclaim"></a>

When bringup finishes, the management appliances run on the vSAN datastore, and the temporary VMFS datastore is empty. Reclaim the temporary datastore to stop accruing storage charges.

1. In the vSphere Client, unmount the temporary VMFS datastore from the host.

1. In the Amazon EC2 console or with the AWS CLI, detach the EBS volume from the host instance. For instructions, see [Detach an Amazon EBS volume from an instance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-detaching-volume.html) in the *Amazon EBS User Guide*.

1. Wait until the volume state is `available`. To check the volume state, see [View Amazon EBS volume information](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-describing-volumes.html).

1. Delete the volume with the EC2 console or the AWS CLI. For instructions, see [Delete an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-volume.html) in the *Amazon EBS User Guide*.

You have installed VCF on your hosts. If bringup fails, see [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).

Next step: [Step 5: Configure NSX networking](self-deployed-nsx-edge.md).