

# Quick start guide for migration assessments
<a name="transform-app-assessments-quick-start"></a>

This guide explains how to get the inventory data that an assessment needs, how to run an assessment, how to review the results, and which prompts to use. Start here if you want to produce a first business case quickly. Before you start, confirm that you have the items in [Prerequisites](transform-app-assessments.md#transform-app-assessments-prerequisites).

This guide covers the following topics, which take you from an inventory file to a finished business case:
+ Get data for a migration assessment
+ Run an assessment
+ Review and refine the results
+ Use the example prompts

## Getting data for a migration assessment
<a name="transform-app-assessments-quick-start-data"></a>

Every assessment starts with a server inventory, and AWS Transform accepts many formats. Three routes cover most cases: export your inventory from your hypervisor, run the AWS Transform discovery tool, or use data you already have. For more information about supported formats, see [Uploading inventory data](transform-app-assessments.md#transform-app-assessments-upload-inventory).

### Exporting your inventory from vCenter
<a name="transform-app-assessments-quick-start-data-export"></a>

If your workloads run on VMware, an export from vCenter is the fastest way to get data. Both of the following tools run in minutes, and neither needs agents on your servers.
+ **Export for vCenter** – an open-source Python script from AWS. It collects only the vCenter data that AWS Transform needs, and writes files that match the names and column headers of RVTools CSV files. You need Python 3.10 or later and read-only vCenter credentials. The script creates a `vcexport.zip` file that you upload to your assessment. Because the output matches the RVTools format, AWS Transform reads it as an RVTools export. For instructions on installing and running the script, see [export-for-vcenter](https://github.com/awslabs/export-for-vcenter) on the GitHub website.
+ **RVTools** – a widely used third-party Windows tool from Dell that reports on VMware vSphere environments. Many teams already run it, so your infrastructure team may have a recent export. It exports to an Excel file or a ZIP file of CSV files, both of which AWS Transform accepts. Download RVTools only from [RVTools](https://www.dell.com/en-us/shop/vmware/sl/rvtools) on the Dell website.

Both tools report how your virtual machines are configured. Export for vCenter also reads the performance statistics that vCenter already collects, and RVTools does not. For each powered-on VM, it adds maximum and average CPU and memory use, and the largest virtual disk read and write request sizes.

That data matters, because AWS Transform sizes instances from the peak utilization in your inventory when it is there, and falls back to default assumptions when it is not. To get a first business case, an RVTools export is still a good option, and you can add usage data later.

Data from a hypervisor has limits. It covers only the virtual machines that vCenter manages. Add physical servers, other hypervisors, and cloud workloads separately. It also cannot see inside the guest, so you get no database engines or editions, and no connections between servers. Without SQL Server editions and versions, AWS Transform cannot analyze your SQL Server licensing.

Export for vCenter has two limits of its own. It skips powered-off VMs, VMs with no IP address, and VMs in a `notRunning` guest state. Its usage data also defaults to a 60-minute window, which can miss month-end or seasonal peaks.

### Collecting richer data with the discovery tool
<a name="transform-app-assessments-quick-start-data-discovery-tool"></a>

The AWS Transform discovery tool is a virtual appliance that you deploy in your own environment to discover your inventory. It supports VMware vCenter and Microsoft Hyper-V, and you can import more servers from a comma-separated values (CSV) file. The tool collects data without agents. It reads from your hypervisors, and it connects to your operating systems over Secure Shell (SSH) and Windows Remote Management (WinRM). You supply the credentials. For instructions on setting up the appliance, see [Discovery tool](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html).

The tool takes longer to set up than an export, because you deploy the appliance, configure your sources, and supply credentials. In return, it collects data that an export cannot give you:
+ **Usage data over time** – operating system and storage metrics, collected as the tool runs. AWS Transform can then size servers against real demand instead of assumptions. This has the largest effect on the accuracy of your estimate.
+ **Database discovery** – the SQL Server and Oracle databases on your servers. SQL Server editions and versions are what make license and edition analysis possible. Your inventory records Oracle databases, and AWS Transform assesses their host servers as general compute.
+ **Network connections** – connections between your servers, and the process behind each one. AWS Transform assessments do not map application dependencies, so use this data for your own wave planning.
+ **Wider coverage** – one inventory across vCenter, Hyper-V, and imported servers, so you avoid merging separate exports.

Many teams run both. Start with an export to get a directional business case and agree on scope. Then run the assessment again with the discovery tool data to firm up the numbers.

### Using data you already have
<a name="transform-app-assessments-quick-start-data-existing"></a>

You can often use data you already have. AWS Transform recognizes the common discovery and inventory formats, and falls back to a flexible parser for files that it does not recognize. A spreadsheet, a configuration management database (CMDB) export, a storage report, or an export from a third-party discovery tool are all reasonable starting points, as are the tools in [Migration discovery](https://aws.amazon.com/marketplace/solutions/migration/migration-discovery) in AWS Marketplace. AWS Transform detects the format when you upload, and accepts partial data when fields are missing. Check what AWS Transform reports back for an unrecognized file, because a flexible parse is best-effort. For a spreadsheet that you build yourself, the AWS Transform Assessment Data template gives you the columns that AWS Transform expects. For more information about commonly used sources, see [Uploading inventory data](transform-app-assessments.md#transform-app-assessments-upload-inventory).

## Running an assessment
<a name="transform-app-assessments-quick-start-running"></a>

After you upload your inventory, an assessment takes three steps. Define the scope, define the assumptions, and run it. You can work through the steps one at a time, which lets you check each one before you move on. You can also combine all three in a single prompt when you already know what you want.

AWS Transform uses default values for anything you leave out, so you get a result either way. Being explicit gives you a better result. The defaults cannot know which servers you plan to migrate, which AWS Region you want, or what commitments your finance team will make. A business case built on unstated assumptions is also hard to defend when stakeholders question the numbers. When you state your inputs, you know which inputs produced which result.

The assumptions that you set in the second step shape the result more than any other input, and they are where your organization's constraints belong. The pricing model and term is often the largest cost variable in an assessment.

**To run an assessment**

1. 

**Define the scope**

   Decide which servers and workloads belong in the assessment. An export usually holds more than you plan to migrate, and servers that you plan to retire inflate both your on-premises baseline and your AWS estimate. For more information about scope, see [Managing inventory scope](transform-app-assessments.md#transform-app-assessments-manage-scope).

   Take the following scoping actions:
   + Exclude the servers that you plan to decommission rather than migrate, and the servers you want to keep out of this business case.
   + Move your non-production servers into a separate scenario, so that the main business case covers production.
   + Add servers that the export missed, such as physical servers that vCenter does not manage.
   + Check that AWS Transform found your SQL Server workloads, because it assesses them differently from other servers.

   AWS Transform also excludes some resources on its own, including powered-off and suspended servers, virtual machine templates, and the appliances that discovery tools and collectors run on. Check the in-scope count against what you expect, because these exclusions change your server count.

1. 

**Define the assumptions**

   Set the pricing and infrastructure assumptions that AWS Transform uses.

   The following are basic examples. You can configure many more assumptions than these, including processor architecture, instance type exclusions, and your on-premises costs. For more information about assumptions, see [Configuring assessment scenarios](transform-app-assessments.md#transform-app-assessments-configure-scenarios).
   + **Target AWS Region** – for example, the US East (N. Virginia) AWS Region, or the AWS Region closest to your users. Prices vary by AWS Region.
   + **Pricing model and term** – for example, three-year Reserved Instances if your finance team will commit to a term, or On-Demand if it will not.
   + **Right-sizing** – the CPU and memory utilization that AWS Transform assumes for servers with no performance data.
   + **Tenancy and licensing** – for example, mixed tenancy, so that Bring Your Own License Windows workloads go on Dedicated Hosts. Choose Bring Your Own Media for SQL Server on Amazon Relational Database Service (Amazon RDS) if you own the licenses.

   Lower assumed utilization leaves more headroom and recommends larger instances. Higher assumed utilization trades headroom for cost.

1. 

**Run the assessment**

   Run the assessment. A run can take several minutes, and the time depends on the size of your inventory.

After the run finishes, check the results before you share them, as described in the following section.

## Reviewing and refining the results
<a name="transform-app-assessments-quick-start-review"></a>

After the assessment runs, review the output. AWS Transform answers in chat, so you can ask about the results, drill into a group of servers, and question a recommendation without generating a file. When you need something to share, AWS Transform produces the following deliverables:

Microsoft PowerPoint presentation (PPTX)  
An executive presentation with summary findings and recommendations.

Microsoft Excel workbook (XLSX)  
A detailed export with recommendations and cost breakdowns for each server.

Portable Document Format (PDF)  
A report that covers compute, storage, licensing, and cost comparisons.

Of the three deliverables, the PDF is the one that you can customize through chat. AWS Transform delivers all three files together in a ZIP file. The sheets and slides that you get depend on the workloads that your assessment covered.

Treat the first run as a draft. Verify the following in the results:
+ Confirm that the server count in the total cost of ownership (TCO) summary matches the scope you set.
+ Confirm that the recommendations that AWS Transform generates for your highest-cost servers look reasonable. The XLSX file lists the estimated cost for each server.
+ Investigate anything that seems wrong, such as a recommended instance type that is larger than the source server.

When the numbers look right, take the following actions:
+ Create a scenario for each option that you are weighing, such as Amazon RDS compared with SQL Server on Amazon EC2, and then compare the scenarios side by side. An assessment holds up to five scenarios.
+ Generate the reports and presentations that you need to share.

You can change your assumptions and run the scenario again, create new scenarios with different assumptions, and compare scenarios side by side to find the option that fits. Re-uploading your inventory isn't required, but a changed scenario does run again in full. Start with your best understanding, and refine it as stakeholders weigh in.

## Example prompts
<a name="transform-app-assessments-quick-start-prompts"></a>

You do each of these steps through chat. The following examples show one prompt for each step. Each prompt asks for several things at once, and that is deliberate. AWS Transform keeps context across messages, so a prompt that names your scope, your assumptions, and the output you want works better than a series of short questions. Change the details to match your environment.

### Defining scope
<a name="transform-app-assessments-quick-start-prompts-scope"></a>

This prompt checks how AWS Transform read your inventory, then narrows the scope:

"How many servers are in my inventory, and which of them run SQL Server? List any data quality warnings you found. Then take srv-101, srv-102, and srv-103 out of scope, because you plan to decommission them. Confirm the final server count in scope, with its CPU, memory, and storage."

### Defining assumptions
<a name="transform-app-assessments-quick-start-prompts-assumptions"></a>

This prompt states your pricing, infrastructure, and licensing assumptions instead of leaving them on the defaults:

"Assess the servers in scope in the US East (N. Virginia) AWS Region. Price them with three-year Reserved Instances, No Upfront. Allow AWS Graviton where my workloads support Arm, and keep the rest on x86. Use mixed tenancy, so that my Bring Your Own License Windows servers go on Dedicated Hosts. Assume Bring Your Own Media for SQL Server on Amazon RDS. Use gp3 volumes for block storage. Compare the TCO over five years."

### Running the assessment
<a name="transform-app-assessments-quick-start-prompts-run"></a>

This step is simple once the scope and the assumptions are set. Run the assessment, and ask for detail so that you can check the result:

"Run the assessment and give me a detailed breakdown of the results."

From there, stay in the same conversation to compare scenarios, run what-if analysis, and generate reports.

### Combining the steps in one prompt
<a name="transform-app-assessments-quick-start-prompts-single"></a>

When you already know your scope and your assumptions, state them together and run the assessment in one prompt:

"Assess my inventory, but take srv-101, srv-102, and srv-103 out of scope, because you plan to decommission them. Price the rest in us-east-1 with three-year Reserved Instances, No Upfront. Use mixed tenancy, so that my Bring Your Own License Windows servers go on Dedicated Hosts. Assume Bring Your Own Media for SQL Server on Amazon RDS. Then run the assessment and give me a detailed breakdown of the results."

## Related resources
<a name="transform-app-assessments-quick-start-related"></a>

For more information about migration assessments, see the following topics:
+ For more information about inventory formats, see [Uploading inventory data](transform-app-assessments.md#transform-app-assessments-upload-inventory).
+ For more information about scope, see [Managing inventory scope](transform-app-assessments.md#transform-app-assessments-manage-scope).
+ For more information about assumptions, see [Configuring assessment scenarios](transform-app-assessments.md#transform-app-assessments-configure-scenarios).
+ For instructions on collecting inventory automatically, see [Discovery tool](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html).