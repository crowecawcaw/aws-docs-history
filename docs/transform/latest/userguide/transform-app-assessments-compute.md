

# Compute assessments
<a name="transform-app-assessments-compute"></a>

AWS Transform analyzes your on-premises servers and recommends the best-fit, lowest-cost Amazon EC2 instance for each one. For every server, AWS Transform produces multiple pricing options, licensing analysis, and right-sizing recommendations so you can build a data-driven total cost of ownership business case in minutes.

## Amazon EC2 right-sizing
<a name="transform-app-assessments-compute-ec2"></a>

AWS Transform matches each server to an Amazon EC2 instance based on its CPU, memory, and performance requirements. When your inventory includes utilization data, AWS Transform sizes against observed utilization—typically P95 CPU utilization and peak memory—rather than the provisioned capacity, so over-provisioned on-premises servers are right-sized to what the workload actually uses. When utilization data is not available, AWS Transform applies configurable default utilization assumptions.

You can control how aggressively AWS Transform right-sizes by choosing a performance tier:
+ **Conservative**—plans for more headroom and recommends larger instances.
+ **Balanced**—the default, which balances headroom against cost.
+ **Aggressive**—plans closer to observed utilization and recommends smaller instances.

AWS Transform considers current-generation instance families that match your workload's operating system and excludes older-generation families by default. You can further include or exclude specific instance families or types through assessment configuration or chat.

## Processor architecture and AWS Graviton
<a name="transform-app-assessments-compute-graviton"></a>

By default, AWS Transform recommends x86 instances (Intel and AMD). You can change the processor architecture preference to include AWS Graviton-based instances, which are AWS-designed Arm processors that deliver better price performance for many workloads. The architecture preference supports three settings:
+ **x86 only**—the default; recommends Intel and AMD instances.
+ **AWS Graviton only**—restricts recommendations to AWS Graviton-based instance families.
+ **Any**—considers both x86 and AWS Graviton instances and selects the best fit.

**Note**  
Moving to AWS Graviton may require recompiling or repackaging applications for the Arm architecture. SQL Server workloads on Amazon EC2 are recommended on x86 instances only.

## Tenancy and Dedicated Hosts
<a name="transform-app-assessments-compute-tenancy"></a>

AWS Transform supports shared tenancy, dedicated tenancy, and mixed tenancy. The tenancy you choose affects both pricing and how AWS Transform accounts for Microsoft licensing.
+ **Shared**—instances are priced using the standard Amazon EC2 instance pricing.
+ **Dedicated**—instances are placed on Amazon EC2 Dedicated Hosts and priced using Dedicated Host pricing. AWS Transform packs your instances onto the fewest hosts needed, which is relevant when your licensing terms require you to license physical cores or use dedicated hardware.
+ **Mixed**—AWS Transform places Bring Your Own License (BYOL)-eligible Windows workloads on Dedicated Hosts to reuse existing licenses, and places other workloads on shared tenancy with License Included pricing.

Bring Your Own License for Windows Server requires Dedicated Hosts and applies to Windows Server 2019 and earlier. Windows Server 2022 and later use License Included pricing on shared tenancy.

## Pricing models
<a name="transform-app-assessments-compute-pricing"></a>

AWS Transform computes and reports multiple pricing models side by side and recommends the option with the lowest total annual cost. Because a three-year commitment is usually the least expensive, it is often the recommended option.
+ **On-Demand**—pay by the hour with no commitment.
+ **Reserved Instances**—one-year and three-year commitments, with No Upfront, Partial Upfront, and All Upfront payment options.
+ **Savings Plans**—one-year and three-year commitments. You can choose Compute Savings Plans, which apply flexibly across instance families, sizes, Regions, and operating systems, or Amazon EC2 Instance Savings Plans, which offer a deeper discount in exchange for committing to a specific instance family in a Region.

## Example prompts
<a name="transform-app-assessments-compute-prompts"></a>
+ "Find the best-fit EC2 instance for each of my servers"
+ "Show me the cost difference between On-Demand, Savings Plans, and Reserved Instances"
+ "Recommend AWS Graviton instances where my workloads support Arm"
+ "Right-size my servers using aggressive utilization assumptions"
+ "What if I only use storage optimized instances?"