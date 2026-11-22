

# Troubleshoot environment status checks

Amazon Elastic VMware Service runs status checks on your environment and reports the result in the environment status. This page applies to both deployment modes.

## Environment status checks
<a name="troubleshoot-env-status"></a>

The environment status combines four checks. They validate the connection to SDDC Manager, the host count, and the VMware Cloud Foundation (VCF) license key. The SDDC Manager connector is the management connector for VCF 5.2.x. In Self-deployed environments that run VCF 9.x, Amazon EVS connects to VCF through the VCF Operations connector and runs a reachability check on each connector. The columns show the check and what it verifies.


| Check | What it verifies | 
| --- | --- | 
| Reachability | Amazon EVS has a persistent connection to SDDC Manager. | 
| Host count | The environment meets the minimum host count of your VCF deployment topology. | 
| Key re-use | The VCF license key isn’t in use by another Amazon EVS environment. | 
| Key coverage | The VCF license key that is assigned to vCenter Server covers the vCPU cores and vSAN storage capacity of all hosts. | 
| Connector reachability | Amazon EVS can reach and sign in to the appliance of each connector. | 

For a connector whose reachability check stays `FAILED` in a Self-deployed environment, see [The connector is `ACTIVE`, but its reachability check stays `FAILED`](troubleshoot-self-deployed.md#troubleshoot-sd-connector-reachability). For a vCenter connector that affects Windows Server entitlements, see [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md).

### Review the status check results
<a name="view-env-status"></a>

To review the status check results, do the following:

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**, and then select your environment.

1. Choose the **Details** tab to see an overview of the environment.

1. Check the **Environment status**. Hover over the field to see the result of each environment status check.

For how to read the status with the AWS CLI, see [Monitor environment status](evs-env-status-check.md).

## The reachability check failed
<a name="troubleshoot-reachability"></a>

 **Cause** 

Amazon EVS can’t reach SDDC Manager. When this check fails, Amazon EVS can’t validate the environment status, and you can’t add hosts to the environment. A reachability failure also makes the key re-use and key coverage checks fail, and the host count check returns **Unknown**.

 **Solution** 

1. Make sure that your certificates are valid and unexpired. You can use the SDDC Manager UI or the vSphere Client to manage certificates in a VCF environment. After deployment, we recommend that you replace all certificates of the VCF management domain. For more information, see [Managing Certificates in VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/certificate-management-admin.html) in the Broadcom documentation.

1. Fix the reachability of your DNS servers, your DNS records, and your firewall rules, as described in [Amazon EVS can’t reach DNS servers or SDDC Manager](troubleshoot-networking.md#troubleshoot-dns-reachability).

## The host count check failed
<a name="troubleshoot-host-count"></a>

 **Cause** 

The environment has fewer hosts than your VCF deployment topology requires.

 **Solution** 

Add hosts so that your environment meets the minimum requirement. For the minimum host counts by VCF version and deployment topology, see the Broadcom documentation for [VCF 9.x](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html) or [VCF 5.2.x](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2.html). To add a host, see [Add a host (VCF 5.x)](evs-env-create-host.md).

## The key re-use check failed
<a name="troubleshoot-key-reuse"></a>

The request to create the environment returns an error that says the environment couldn’t be created.

 **Cause** 

You can use a VCF license key for only one Amazon EVS environment. The check fails if the environment creation request contains a VCF license key that another environment already uses.

 **Solution** 

Review your license settings in SDDC Manager, and replace any license key that is already in use with an unused key.

**Important**  
Manage VCF solution and vSAN license keys in the SDDC Manager user interface. Amazon EVS requires valid VCF solution and vSAN license keys in SDDC Manager to function. Assign the keys to your hosts and vSAN cluster in the vSphere Client. Make sure that the keys appear on the licensing screen of SDDC Manager.

For more information, see [VCF licensing](vcf-license-mgmt.md).

## The key coverage check failed
<a name="troubleshoot-key-coverage"></a>

The request to create the environment returns an error that says the environment couldn’t be created.

 **Cause** 

The cause is one of the following:
+ The VCF license keys aren’t assigned to vCenter Server. You must assign a license key to vCenter Server before its evaluation period expires or before the assigned license key expires.
+ The VCF license keys don’t cover the vCPU cores and vSAN storage capacity that your hosts need. The requirements for the VCF solution key (including the minimum core count) and the vSAN license key (including the minimum vSAN capacity) depend on the instance type.

 **Solution** 

1. Review the license key assignments in SDDC Manager, and assign a license key to vCenter Server if none is assigned.

1. If the license keys don’t cover your hosts, add vSAN license keys in SDDC Manager until they cover your hosts. For the thresholds for your configuration, see [VCF licensing](vcf-license-mgmt.md).

Manage license keys in the SDDC Manager user interface, as described in [The key re-use check failed](#troubleshoot-key-reuse).

If these steps don’t resolve the problem, see [Get help from AWS Support and Broadcom](get-help.md) for who to contact and what to include in a case.