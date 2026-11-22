

# Get started with Amazon Elastic VMware Service

Choose how you deploy VMware Cloud Foundation (VCF) on Amazon Elastic VMware Service (Amazon EVS), and find the pages for each stage of the journey.

The procedures in [Deploy in Self-deployed mode](getting-started-self-deployed.md) deploy VCF 9.x. Pages in [Deploy in EVS-deployed mode](evs-deployed-overview.md) cover VCF 5.2.x. A page with no line and outside those sections covers both.

## Choose your path
<a name="getting-started-choose-path"></a>

Find the row that matches what you want to do, and go to the page in the second column.


| If you want to | Go to | 
| --- | --- | 
| Deploy VCF 9.x in Self-deployed mode with one AWS CloudFormation stack |  [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md)  | 
| Deploy VCF 9.x in Self-deployed mode, step by step |  [Deploy in Self-deployed mode](getting-started-self-deployed.md)  | 
| Use diskless hosts, for example r7i instance types (Self-deployed mode, VCF 9.x) |  [Choose storage](plan-storage.md), then [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md)  | 
| Deploy VCF 5.2.x in EVS-deployed mode, where Amazon EVS installs VCF for you |  [Deploy in EVS-deployed mode](evs-deployed-overview.md)  | 
| Run or change an existing environment |  [Operate](operate-overview.md)  | 
| Compare the deployment modes first |  [Differences between deployment modes](deployment-mode-differences.md)  | 
| Size, price, or plan first |  [Plan](plan-overview.md)  | 
| Check whether an instance type, VCF version, or VCF feature is supported |  [Supported VCF versions and instance types](versions-provided.md) and [VCF feature support on Amazon EVS](vcf-feature-support.md)  | 

## From plan to operations
<a name="getting-started-journey"></a>

Every deployment follows the same three stages. Complete them in order.

1.  **Plan.** Choose the VCF version, instance types, storage and network design, and estimate costs and VCF subscriptions. Start at [Plan](plan-overview.md), and use the [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md) to record your values.

1.  **Deploy.** Prepare your AWS account, then deploy the environment in the way that you chose.

   1.  [Prepare your AWS account](setting-up.md) 

   1. For a manual deployment, build the network foundation ([Build the network foundation](network-foundation.md)). If you use EDO, skip this step because EDO builds the network for you.

   1. For VCF 9.x in Self-deployed mode, use [Deploy in Self-deployed mode](getting-started-self-deployed.md) or [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md). For VCF 5.2.x in EVS-deployed mode, use [Deploy in EVS-deployed mode](evs-deployed-overview.md).

   1. (Optional) [Connect external storage](external-storage-connect.md) 

1.  **Operate.** Monitor the environment, manage hosts, connectors and entitlements, apply updates, and migrate workloads. Start at [Operate](operate-overview.md).

**Important**  
You incur AWS charges for the Amazon EC2 bare metal instances from the time you add hosts to an environment, even if you haven’t installed VCF on them. For prices, see [Amazon EVS pricing](https://aws.amazon.com/evs/pricing). For costs and VCF subscriptions, see [Plan costs and licenses](plan-cost.md).

## Next steps
<a name="getting-started-next-steps"></a>

After your environment is running, migrate your workloads to Amazon EVS with VMware Hybrid Cloud Extension (HCX). For more information, see [Operate](operate-overview.md) and [Migrate workloads with HCX](migrate-evs-hcx.md).