

# Tutorial: Generating estimates for Windows Servers and SQL Servers on EC2
<a name="estimate-workload-tutorial"></a>

This tutorial shows you how to use the Microsoft Windows Server and Microsoft SQL Server on Amazon EC2 in AWS Pricing Calculator to generate an estimate. 

## Procedure
<a name="estimate-workload-tutorial-process"></a>

**Topics**
+ [Step 1: Choose your AWS Region](#estimate-workload-tutorial-region)
+ [Step 2: Choose your licensing and tenancy recommendation](#estimate-workload-tutorial-step1)
+ [Step 3: Configure your machine specifications](#estimate-workload-tutorial-step2)
+ [Step 4: Choose a pricing strategy](#estimate-workload-tutorial-step3)
+ [Step 5: Review calculations and cost details](#estimate-workload-tutorial-step4)
+ [Step 6: Add a Windows LI and SQL Server LI to your estimate](#estimate-workload-tutorial-step5)

### Step 1: Choose your AWS Region
<a name="estimate-workload-tutorial-region"></a>

**To name your estimate and select your Region**

1. Open the **Configure Windows Server and SQL Server on Amazon EC2** section of AWS Pricing Calculator at [https://calculator.aws/\#/createCalculator/EC2WinSQL](https://calculator.aws/#/createCalculator/EC2WinSQL).

1. Enter the following estimate description: `Workload_SQL_BYOL`.

1. Make sure that your location type is set to **Region**. Then, choose the Region `US East (Ohio)`.
**Note**  
All AWS resources are priced based on the Region you choose.

### Step 2: Choose your licensing and tenancy recommendation
<a name="estimate-workload-tutorial-step1"></a>

In this section, you can specify your license details to determine your cost-optimized tenancy qualifications. For more information about licensing and tenancy supported by AWS Pricing Calculator, see [Licensing and tenancy recommendations](windows-workload-estimates.md#estimate-workload-tenancy).

**To determine your licensing and tenancy recommendations for this example**

1. Open the **Configure Windows Server and SQL Server on Amazon EC2** section of AWS Pricing Calculator at [https://calculator.aws/\#/createCalculator/EC2WinSQL](https://calculator.aws/#/createCalculator/EC2WinSQL).

1. In the **Licensing and tenancy recommendation** section, clear the **Windows Server** checkbox.

1. Under **SQL Server**, select both options.

1. Keep the default selection of the shared tenancy.

   You will notice that the recommended tenancy options are **Shared** and **Dedicated Hosts**. You can use the [Amazon EC2 Dedicated Hosts calculator](https://calculator.aws/#/EC2DedicatedHosts) to estimate Dedicated Host tenancy.

![Licensing and tenancy recommendation with Amazon EC2 shared tenancy selected](http://docs.aws.amazon.com/pricing-calculator/latest/userguide/images/t2_licensing_options_win_byol_sql.png)


### Step 3: Configure your machine specifications
<a name="estimate-workload-tutorial-step2"></a>

In this step, you can input machine specifications to configure your AWS Pricing Calculator estimate.

The following table provides an example workload scenario to show several capabilities in the AWS Pricing Calculator. You can use these values for the purpose of this tutorial.


| Host description | vCPUs | Ram | Storage (GB) | IOPS | Software | Optimize vCPUs | Quantity | Passive node count | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Server 1 | 16 | 800 | 5000 | 60000 | SQL Enterprise Edition | 16 | 10 | 5 | 
| Server 2 | 16 | 64 | 3000 | 15000 | SQL Standard Edition | 16 | 8 | 4 | 
| Server 3 | 8 | 16 | 1000 |  | SQL Web Edition | 8 | 10 | 0 | 
| Server 4 | 4 | 32 | 500 |  | Windows | N/A | 8 | N/A | 

**To specify your machine specifications for this example**

1. Open the **Configure Windows Server and SQL Server on Amazon EC2** section of AWS Pricing Calculator at [https://calculator.aws/\#/createCalculator/EC2WinSQL](https://calculator.aws/#/createCalculator/EC2WinSQL).

1. In the **Configure machine specifications** section, choose the **Add new machine specification** button.

1. For **Machine description**, keep the name **Server 1**.

1. For **Operating system**, choose **Windows Server**.

1. For **SQL Server edition (BYOL)**, choose **SQL Server Enterprise**.

1. Under **Storage volumes per specifications**, enter the storage amount (GiB) as **5000** and **IOPS** as **60000**. 

   For more information, see [Machine specifications details](#estimate-workload-tutorial-step2-machinedetails).

1. For **Amazon EC2 instance type**, choose the **Obtain an Amazon EC2 instance type recommendation**. 

   For more information, see [Amazon EC2 instance type details](#estimate-workload-tutorial-step2-ec2details).

1. For **Optimize vCPU**, keep the optimize CPU value as `16`. 

   For more information, see [Benefits of Optimize vCPUs](#estimate-workload-tutorial-step2-optcpudetails).

1. For **Quantity**, enter **10**.

1. For number of passive instances, choose **5**. 

1. Choose **Add machine** to add more machine specification types. 

   For this tutorial, add the remaining three workloads from the example workload table.

#### Machine specifications details
<a name="estimate-workload-tutorial-step2-machinedetails"></a>

If you enter the storage size (GB) only, the calculator provides you with the most cost-effective Amazon Elastic Block Store (Amazon EBS) storage option. If you enter a value between **16000** and **64000** for IOPS, the AWS Pricing Calculator recommends the io2 EBS volume type. Anything value beyond that range, AWS Pricing Calculator recommends io2 Block Express with tiered pricing. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html).

#### Amazon EC2 instance type details
<a name="estimate-workload-tutorial-step2-ec2details"></a>

You can choose **Obtain an Amazon EC2 instance type recommendation** for the server type specifications. AWS recommendations always default to the latest, cost-optimized instances for Windows Server and SQL Server workloads.

You can also choose **Search** for an Amazon EC2 instance type if you want the ability to filter the instance types. You can filter by instance category, memory, CPU, and other options.

#### Benefits of Optimize vCPUs
<a name="estimate-workload-tutorial-step2-optcpudetails"></a>

You have the flexibility to specify a custom number of vCPUs while using the same memory, storage, and bandwidth of a full-sized instance. This means that BYOL customers can optimize vCPU-based licensing costs. 

Even though the CPU optimized instance has the same price as the instance that's not optimized for CPU, it offers flexibility to choose the CPU count, so you can bring the right SQL Server license to avoid extra costs. For example, an `x1e.8xlarge` instance has 32 vCPUs by default. But you can specify `x1e.8xlarge` with Optimize CPU value to 16, 14, or 12. 

The passive SQL Server nodes allow for additional cost optimization. A passive SQL Server node doesn't serve SQL Server data or run active SQL Server workloads. If you bring SQL Server to AWS with Software Assurance, you aren’t required to license SQL Server on a passive node. 

### Step 4: Choose a pricing strategy
<a name="estimate-workload-tutorial-step3"></a>

In this step, you use the pricing strategy section in AWS Pricing Calculator to choose a pricing model.

**To choose a pricing strategy for this example**

1. Open the **Configure Windows Server and SQL Server on Amazon EC2** section of AWS Pricing Calculator at [ https://calculator.aws/\#/createCalculator/EC2WinSQL](https://calculator.aws/#/createCalculator/EC2WinSQL).

1. In the **Choose a pricing strategy** section - under **Pricing model**, choose **Standard Reserved Instance**.

1. Under **Reservation term**, choose **1 year**.

1. Under **Payment options**, choose **No Upfront**.

**Note**  
This is a default pricing strategy that offers up to 75 percent savings over On-Demand pricing. For more information, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/).

### Step 5: Review calculations and cost details
<a name="estimate-workload-tutorial-step4"></a>

At this stage in the example tutorial, you can view the breakdown your cost estimates.

**To view the calculation and cost details of this example**

1. Open the **Configure Windows Server and SQL Server on Amazon EC2** section of AWS Pricing Calculator at [ https://calculator.aws/\#/createCalculator/EC2WinSQL](https://calculator.aws/#/createCalculator/EC2WinSQL).

1. To view the breakdown of the calculations, select the arrow next **Show calculations**.

1. The view the cost details of the EC2 instance, storage, and BYOL SQL license specifications, select the arrow next to **Cost details** section.

1. After you review the calculations and cost details of all four example workloads, choose **Save and add service**.

At this point, you successfully estimated workload costs for Windows Server License Included and SQL Server Bring Your Own License (BYOL) licensing. If want to clone your existing estimate to generate an estimate for the License Included option for an SQL Server, navigate to [Step 6: Add a Windows LI and SQL Server LI to your estimate](#estimate-workload-tutorial-step5).

### Step 6: Add a Windows LI and SQL Server LI to your estimate
<a name="estimate-workload-tutorial-step5"></a>

**To add a Windows LI and SQL Server LI to your estimate**

1. Navigate to the **My Estimate** section in AWS Pricing Calculator.

1. Select the checkbox of the service you want to duplicate. Then, choose **Duplicate**.

1. Choose the **Edit** icon on the duplicate version of the estimate.

1. For the **Estimate details** description, enter **Workload\_LI**.

1. Keep the **Region** as is.

1. In the **Licensing and tenancy recommendation** section, keep the **Windows Server** and **SQL Server** check boxes cleared.

1. For the SQL Server section, review and adjust the machine specifications.

1. Review the new monthly cost estimate and aggregated monthly costs.

1. Choose **Update**.

On the** My Estimate** page, you can now compare the price under both the licensing options. In this example, the shared tenancy with Windows License Included and SQL Server BYOL option is approximately half of the cost of shared tenancy with Windows License Included and SQL Server License Included.

You have now completed the tutorial for using the Microsoft Windows Server and Microsoft SQL Server to generate a pricing estimate.