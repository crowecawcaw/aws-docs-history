

# Deploy in Self-deployed mode

In Self-deployed mode, you create an Amazon Elastic VMware Service environment, add hosts, and then install and configure VMware Cloud Foundation (VCF) yourself. Amazon EVS provisions the AWS networking and the VLAN subnets. To deploy VCF 9.x, you use the VCF Installer and connect VCF back to Amazon EVS with connectors.

Charges for the Amazon EC2 bare-metal instances begin when you add hosts. For more information, see [Billing](#self-deployed-costs).

You can also run these steps with the EVS Deployment Orchestrator (EDO), a tool in the [Solutions for Amazon EVS repository](https://github.com/aws/solutions-for-amazon-evs). For more information, see [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md). For the VCF versions and instance types that Self-deployed mode supports, see [Supported VCF versions and instance types](versions-provided.md). If you want Amazon EVS to install VCF 5.2.x, see [Deploy in EVS-deployed mode](evs-deployed-overview.md). To install VCF 5.x yourself in Self-deployed mode, follow the Broadcom documentation for your VCF version. The steps in this guide cover VCF 9.x.

## Steps to deploy
<a name="self-deployed-process"></a>

Before you begin, prepare your AWS account and build the network foundation. For more information, see [Prepare your AWS account](setting-up.md), [Build the network foundation](network-foundation.md), and [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md).

Then complete these steps in order.

1.  [Step 1: Create the environment](self-deployed-create-env.md). Amazon EVS provisions your VLAN subnets.

1.  [Step 2: Create DNS records](self-deployed-host-dns-records.md). Create A and PTR records for your ESX hosts and VCF management appliances.

1.  [Step 3: Add hosts](self-deployed-add-hosts.md). Add EC2 bare-metal hosts to your environment.

1. Install VCF on your hosts. The procedure depends on the storage of your instance type.
   + For hosts with local storage that use vSAN, see [Step 4a (local storage): Prepare the VCF Installer](self-deployed-install-vcf.md), and then [Step 4b (local storage): Run VCF bringup](sd-install-bringup.md).
   + For diskless hosts that use external storage, see [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md), and then [Step 4b (diskless): Create the specification and deploy](deploy-diskless-spec.md). Diskless hosts have no local storage.

1.  [Step 5: Configure NSX networking](self-deployed-nsx-edge.md). Create the NSX Edge cluster and the Tier-0 gateway, and configure routing to your VPC.

1.  [Step 6: Create connectors](self-deployed-create-connectors.md). Create connectors so that Amazon EVS can monitor your deployment.

1.  [Step 7: Verify the environment](self-deployed-verify.md). Confirm that your hosts, management appliances, and connectors are healthy.

For help to choose between local storage and diskless hosts, see [Choose instance types](plan-instance-types.md). When you no longer need the environment, see [Clean up a Self-deployed environment](self-deployed-cleanup.md).

## Billing
<a name="self-deployed-costs"></a>

After you add hosts to your environment, you accrue AWS charges for the EC2 bare-metal instances, as for any other EC2 instance. The charges apply whether or not you have installed VCF on the hosts.

If you have created an environment in Self-deployed mode but not yet added hosts or installed VCF, AWS might contact you at the email address of your AWS account. AWS asks you to either complete setup or remove the environment.

To stop accruing charges for hosts that you no longer use, delete those hosts. For more information, see [Clean up a Self-deployed environment](self-deployed-cleanup.md). For prices, see the [Amazon EVS pricing page](https://aws.amazon.com/evs/pricing). For the billing dimensions, see [Plan costs and licenses](plan-cost.md).

**Topics**