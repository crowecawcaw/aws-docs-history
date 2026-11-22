

# Plan costs and licenses

An Amazon Elastic VMware Service environment has charges from more than one AWS service. You also bring your own VMware Cloud Foundation (VCF) subscription from Broadcom. Plan all of them before you deploy, so that your estimate matches your bill. For current prices in each AWS Region, see [Amazon EVS pricing](https://aws.amazon.com/evs/pricing).

## Billing dimensions
<a name="plan-cost-dimensions"></a>

The following table lists the charges for an Amazon EVS environment. The first three apply to every environment.


| Charge | What it covers | 
| --- | --- | 
| Amazon EC2 instances | The bare metal instances that run as your ESX hosts, billed at standard EC2 rates for the instance type. This is usually the largest part of the cost. | 
| Amazon VPC Route Server endpoints | The route server endpoints that your environment uses for dynamic routing between NSX and the VPC. | 
| Amazon EVS control plane | The Amazon EVS service charge. The rate varies by AWS Region and doesn’t depend on the instance type of your hosts. | 
| Windows Server license included (optional) | The Windows Server entitlements that you create for virtual machines, billed hourly for each vCPU. The rate is the same in every AWS Region. For more information, see [Windows Server entitlements](entitlements.md). | 
| External storage (optional) | Datastores on Amazon FSx or on another storage product, billed by that service. | 
| Capacity Reservations (optional) | Reserved EC2 capacity, billed from the time that the reservation becomes active, whether or not hosts use it. For more information, see [Reserve capacity for hosts](plan-capacity.md). | 

VCF subscriptions aren’t billed by AWS. You buy them from Broadcom or a qualified reseller. For more information, see [VCF licensing](vcf-license-mgmt.md).

## Estimate costs with the AWS Pricing Calculator
<a name="plan-cost-calculator"></a>

In the [AWS Pricing Calculator](https://calculator.aws/), the **Amazon EVS** line item covers only the Amazon EVS control plane. To estimate the full cost, also add the EC2 instances for your hosts and the route server endpoints. For the number of hosts, see [Size your environment](plan-sizing.md).

## Lower the cost of hosts
<a name="plan-cost-savings"></a>

You can lower the cost of the EC2 instances that run as your hosts with Savings Plans and Reserved Instances. For the options and an example, see [Amazon EVS pricing](https://aws.amazon.com/evs/pricing).

## Choose a tenancy
<a name="plan-cost-tenancy"></a>

When you create the VPC for your environment, keep the VPC **Tenancy** setting as `Default`. For the steps, see [Create a VPC with subnets and route tables](network-create-vpc.md).

## Common cost questions
<a name="plan-cost-questions"></a>

Stop hosts to save cost  
You can’t stop hosts to save cost, for example on weekends. Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. For more information, see [Host maintenance and retirement events](evs-host-maintenance.md).

Buy VCF through AWS   
You can’t buy VCF through AWS. You must bring your own VCF subscription. You can get it from Broadcom or from a qualified reseller. For more information, see [VCF licensing](vcf-license-mgmt.md).

Next, plan your VCF subscription. See [VCF licensing](vcf-license-mgmt.md).

**Topics**