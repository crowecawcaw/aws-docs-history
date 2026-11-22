

# What is Amazon EVS?

Amazon Elastic VMware Service (Amazon EVS) allows you to run VMware Cloud Foundation (VCF) workloads directly on AWS. Amazon EVS runs VCF on bare-metal Amazon EC2 instances inside your own Amazon Virtual Private Cloud (VPC). Your teams keep the same VCF tools, skills, and operating procedures that they use on premises. You don’t need to re-platform, refactor applications, or retrain staff, and you can bring your existing VCF subscription with its portability entitlement.

You can use Amazon EVS to accelerate cloud migrations, to extend on-premises environments for hybrid scaling, and for disaster recovery.

To start, see [Get started with Amazon Elastic VMware Service](getting-started.md).

## Features of Amazon EVS
<a name="servicename-feature-overview"></a>

The following are key features of Amazon EVS:
+  **Run VCF in your own VPC.** VCF runs inside your own Amazon VPC, next to the other AWS resources that your applications use.
+  **Accelerate your migration** by keeping your existing skills, processes, and technology solutions.
+  **Keep full control** of your virtualization stack, including add-ons and third-party solutions.
+  **Extend with AWS services.** Expand your VMware-based workloads with direct access to a broad range of AWS services, such as managed databases, analytics, serverless, containers, and generative AI.
+  **Bring your own VCF subscription** and use its portability entitlement on AWS.
+  **Scale your environment.** Add hosts to your environment as your workloads grow.

## Who manages what
<a name="what-is-evs-responsibilities"></a>

 AWS provides the infrastructure, and you’re responsible for the virtualization platform and your workloads. This split follows the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). Responsibilities for each area are as follows.


| Area |  AWS  | You | 
| --- | --- | --- | 
| Infrastructure | The AWS networking and VPC connectivity that Amazon EVS provisions, the bare metal hosts and their firmware. | Your VPC design, route tables, network access control lists, and connectivity to your other networks. | 
| VCF software | Provides the Amazon Machine Images (AMIs) for the VMware ESX hypervisor. | The VCF components and the workloads that run on them. You upgrade and patch the VCF stack. | 
| VCF subscriptions | Not applicable. | Bring your own VCF subscription, and keep valid license keys in your VCF management appliance. | 
| Workloads | Not applicable. | Your virtual machines, their guest operating systems and your data. | 

You can also work with AWS Partners to manage and operate the environment for you. For the full model, see [Shared responsibility and support](plan-shared-responsibility.md) and [Security in Amazon Elastic VMware Service](security.md).

## How you work with Amazon EVS
<a name="get-started-evs"></a>

You work with Amazon EVS in three stages: Plan, Deploy, and Operate.

1.  [Plan](plan-overview.md). Successfully deploying Amazon EVS starts with a clear plan. Plan your AWS resources, such as VPCs, Route Servers, and DNS, along with your VCF resources and Amazon EC2 instance types.

1.  [Deploy](deploy-overview.md). To deploy, you prepare your AWS account and network, create an Amazon EVS environment, add hosts, and deploy VCF.

1.  [Operate](operate-overview.md). Configure VCF in the vSphere Client to meet your needs, such as logins, policies, and monitoring. Connect your environment to your on-premises data center, and migrate your workloads ([Migrate workloads with HCX](migrate-evs-hcx.md)). Monitor the environment, manage hosts and connectors, and apply updates.

## Tools
<a name="what-is-evs-tools"></a>

The [Solutions for Amazon EVS](https://github.com/aws/solutions-for-amazon-evs) repository on GitHub is where Amazon EVS provides tooling and solutions that you can use. The tooling for deployment is in the `Deploy` folder.

The EVS Deployment Orchestrator (EDO) is one of the tools in the repository, in the `Deploy` folder. You can use EDO to deploy VCF 9.x environments from one AWS CloudFormation stack. For more information, see [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md).

## Accessing Amazon EVS
<a name="accessing-evs"></a>

You can create and manage Amazon EVS resources with the interfaces in the following table.


| Interface | What it is | More information | 
| --- | --- | --- | 
| Amazon EVS console | A web interface to create and manage Amazon EVS environments. | None | 
|  AWS CLI  | Commands to create and manage Amazon EVS resources, supported on Windows, macOS, and Linux. |  [AWS Command Line Interface](https://aws.amazon.com/cli)  | 
|  AWS CloudFormation | Templates that provision Amazon EVS resources, such as the resource type `AWS::EVS::Environment`. |  [Amazon Elastic VMware Service resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_EVS.html) in the * AWS CloudFormation Template Reference*  | 

For the API, SDKs, and CLI reference, see [Use the AWS CLI, SDKs, and API with Amazon EVS](evs-api-cli-reference.md).

## Pricing
<a name="what-is-evs-pricing"></a>

You pay for the Amazon EC2 bare metal instances that run your hosts and for the other AWS resources that you use. For prices, see [Amazon EVS pricing](https://aws.amazon.com/evs/pricing). To plan costs and VCF subscriptions, see [Plan costs and licenses](plan-cost.md).

## Regions
<a name="what-is-evs-regions"></a>

For the AWS Regions where Amazon EVS is available, see [AWS Regions for Amazon EVS](regions-reference.md).

**Topics**