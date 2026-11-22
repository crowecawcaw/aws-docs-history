

# Deploy in EVS-deployed mode

This page applies to EVS-deployed environments (VCF 5.2.x). For Self-deployed environments that run VCF 9.x, see [Deploy in Self-deployed mode](getting-started-self-deployed.md).

In EVS-deployed mode, Amazon Elastic VMware Service deploys VMware Cloud Foundation (VCF) 5.2.x on your hosts when you create the environment. You supply the network, license keys, and host names, and Amazon EVS builds the VCF environment in your VPC. For a side-by-side comparison with Self-deployed mode, see [Differences between deployment modes](deployment-mode-differences.md).

## What Amazon EVS deploys for you
<a name="evs-deployed-what-evs-deploys"></a>

When you create an environment in EVS-deployed mode, Amazon EVS does the following:
+ Creates the Amazon EVS VLAN subnets in your VPC from the CIDR blocks that you specify.
+ Adds the four hosts that the environment requires for initial deployment.
+ Deploys the VCF management appliances (vCenter Server, NSX Manager, NSX Edge nodes, and SDDC Manager) with the DNS host names that you specify.
+ Stores the VCF credentials as secrets in AWS Secrets Manager in your account, encrypted with the AWS KMS key that you choose.

Diskless hosts aren’t available with VCF 5.2.x. For the VCF versions, ESX versions, and instance types that each VCF version supports, see [Supported VCF versions by instance type](versions-provided.md#current-vcf-versions).

## Before you begin
<a name="evs-deployed-before-you-begin"></a>

Before you create the environment, complete the prerequisites in [Before you begin](getting-started-create-env.md#create-env-evs-deployed-before-you-begin).

## Tasks in this section
<a name="evs-deployed-tasks"></a>

Do these tasks in order:

1.  [Create an environment](getting-started-create-env.md). Use the Amazon EVS console or the AWS CLI to create the environment, including license keys.

1.  [Verify environment creation](verify-env-creation.md). Check that the environment and its hosts are ready.

1.  [Retrieve VCF credentials and access appliances](access-vcf.md). Get the VCF credentials from Secrets Manager and sign in to the management appliances.

When you no longer need the environment, see [Delete an EVS-deployed environment](getting-started-cleanup-env-hosts.md).

## Next steps
<a name="evs-deployed-next-steps"></a>

After you verify the environment, associate the Amazon EVS VLAN subnets with a route table. For instructions, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md). Then you can migrate workloads with VMware HCX. For more information, see [Migrate workloads with HCX](migrate-evs-hcx.md).

**Topics**