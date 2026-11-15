

# Discovery
<a name="transform-vmware-discover-source-data"></a>

Discovery imports your inventory into AWS Transform, so that you can assess costs and plan your migration.

Upload your server data in the chat. AWS Transform recognizes each file, parses it, and merges everything into one inventory without duplicate records. It then checks the data quality and summarizes the results in the chat.

Assessment and migration planning both use this inventory. For more information, see [Discovery, assessment, and planning](transform-migrations-discover-assess-plan.md).

## Supported data sources
<a name="transform-vmware-discover-sources"></a>

You aren't limited to the formats in this list. AWS Transform recognizes the following formats directly:
+ [AWS Transform discovery tool](discovery-tool.md) export (ZIP file)
+ RVTools export
+ Migration Portfolio Assessment (MPA) export, including MPA-format exports from Cloudamize
+ Migration Evaluator inventory workbook or Migration Evaluator Collector export
+ modelizeIT export
+ AWS Transform inventory template
+ NetApp storage export
+ InsightIQ directory report
+ AWS Backup import template
+ VMware NSX export
+ An enrichment CSV file that you exported from AWS Transform and filled in

A ZIP file can contain several of these.

For any other format, such as a configuration management database (CMDB) export or a spreadsheet that your team maintains, AWS Transform generates a parser for the file. It samples the file to learn its structure. It then writes and runs code that extracts your servers, storage, databases, and other records. Before it adds the records, it checks them against its inventory schema. You can upload CSV, Excel, and JSON files this way. Review the summary to confirm what AWS Transform found.

Each file can be up to 2 GB. A ZIP file can contain up to 60 files, and an Excel workbook up to 30 worksheets. An inventory can hold up to 200,000 servers.

## If you don't have inventory files
<a name="transform-vmware-discover-no-files"></a>

If you don't have an export yet, AWS Transform can build an estimated inventory from what you tell it. It asks for your total server count, the split between Linux and Windows, and whether any servers run databases. Sizing and utilization are optional. Any value that you don't give takes a default. AWS Transform shows you a preview and creates the inventory only after you confirm it. When you get real data later, upload it.

For example, "Ingest my inventory," followed by "I don't have a file yet."

## Reviewing your inventory
<a name="transform-vmware-discover-review"></a>

After each upload, AWS Transform summarizes the results in the chat. The summary shows what it recognized, the record counts for each type, the counts before and after duplicates were removed, and anything that needs your attention.

AWS Transform also checks the data quality. It reports missing fields, duplicate IDs, how many servers have utilization data, and IP addresses or host names that look wrong or are placeholders. It doesn't remove servers on its own. AWS Transform automatically leaves out the discovery tool's own virtual machine, and flags hypervisor and appliance servers for you to review.

You can ask questions in the chat to check your data. For example, "Run the quality check and tell me if anything about my uploads needs attention."

## Adding and correcting data
<a name="transform-vmware-discover-update"></a>
+ **Add data** – upload more files at any time. AWS Transform merges them into your inventory and removes duplicate records.
+ **Correct data** – tell AWS Transform what to change in the chat. Your corrections still apply after later uploads. To correct many servers at once, ask for an enrichment CSV file, fill it in, and upload it.
+ **Remove a file** – ask AWS Transform to remove a file that you uploaded. It removes everything that the file contributed and rebuilds the inventory from your other files.

After an upload that includes applications, AWS Transform also attaches a questionnaire for your application owners. For more information, see [Application owner questionnaire](transform-vmware-application-questionnaire.md).

## Best practices for discovery
<a name="transform-vmware-discovery-best-practices"></a>

Discovery works best in stages. Collect the data that your next decision needs, use it in AWS Transform, and add more data as you go. The following practices help you get an accurate business case and migration plan without a long discovery project.

### Match discovery to the decision you need to make
<a name="transform-vmware-discovery-bp-scope"></a>

A directional business case and a detailed migration plan need different data. The following table shows the minimum data for each stage.


**Data needed at each stage**  

| Stage | Purpose | Minimum data | 
| --- | --- | --- | 
| Directional business case | Estimate costs and agree on scope | A server inventory, such as an RVTools export, an Export for vCenter export, or a configuration management database (CMDB) extract | 
| Detailed assessment and migration plan | Right-size servers, analyze licensing, and plan migration waves | Utilization over time, database engines and editions, network connections, and business attributes such as owner, environment, criticality, and recovery objectives | 

### Work in stages
<a name="transform-vmware-discovery-bp-stages"></a>

1. **Start with the inventory you have.** Upload an RVTools or Export for vCenter export to get a directional business case and agree on scope. For more information, see [Quick start guide for migration assessments](transform-app-assessments-quick-start.md).

1. **Add detailed data.** Deploy the AWS Transform discovery tool, upload its export, and rerun your assessment to refine the results.

1. **Keep iterating.** Assessment and planning results often show what data is still missing. You can add data at any time, and AWS Transform merges it with what you already uploaded. AWS Prescriptive Guidance recommends that you don't wait for a complete dataset before you move forward. For more information, see [Discovery acceleration and initial planning](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/portfolio-discovery-initial-planning.html) in *AWS Prescriptive Guidance*.

### Choose a data source for the data you need
<a name="transform-vmware-discovery-bp-sources"></a>

The following table shows when to use each data source, and its limitations.


**Choosing a data source**  

| Source | Use when | Limitations | 
| --- | --- | --- | 
| RVTools | You need a quick business case for a VMware environment. | Reports a single point in time. Contains no network connections and no database engines or editions. | 
| Export for vCenter | You need a quick business case, with the performance statistics that vCenter already collects. | Uses a 60-minute window by default, which can miss peaks. Skips powered-off virtual machines. | 
| AWS Transform discovery tool | You need utilization over time, SQL Server or Oracle data, network connections, or Microsoft Hyper-V coverage. | Needs credentials and network access to your servers. For more information, see [Confirm access before you deploy the discovery tool](#transform-vmware-discovery-bp-access). | 
| Partner discovery tools | You already use them, or you need coverage that the discovery tool doesn't provide. | Upload their exports to AWS Transform and do your assessment and planning in AWS Transform. | 
| CMDB extracts and spreadsheets | You need business context, such as application definitions and owners. | Formats vary, so review what AWS Transform reports after the upload. | 

For the full list of supported formats, see [Supported data sources](#transform-vmware-discover-sources).

### Confirm access before you deploy the discovery tool
<a name="transform-vmware-discovery-bp-access"></a>

Most discovery delays come from access, not from the tool. Before you deploy the discovery tool, confirm the following. For the complete requirements and setup instructions, see [Setting up the discovery tool](discovery-tool-setup.md) and [Required permissions for the discovery tool](discovery-tool-permissions.md).
+ **Accounts** – for vCenter, a user with the Read-Only role at the root datacenter level. For Oracle, a read-only account with the SELECT\_CATALOG\_ROLE grant. For Linux, an SSH user with passwordless `sudo`. Without `sudo`, server UUIDs, LVM details, and process-level network details are missing.
+ **Ports** – 443 to vCenter, 22 for SSH, 5985 and 5986 for Windows Remote Management (WinRM) and Hyper-V, UDP 161 for Simple Network Management Protocol (SNMP), and 1521 for Oracle. Custom ports are supported.
+ **Network** – Dynamic Host Configuration Protocol (DHCP) must be available on the network segment that the appliance connects to.
+ **Guest tools** – VMware Tools or Hyper-V Integration Services must be running in each guest. Without them, the discovery tool has no guest IP address to connect to. It then can't collect OS metrics, network connections, or database data. For those servers, use a CSV import.
+ **Credentials for a subset of servers** – you can assign a credential to specific servers. In Active Directory environments, use the `username@DOMAIN` format.
+ **Appliance** – size the appliance with 4 vCPU, 16 GB of RAM, and a 100 GB disk, and keep it up to date. For more information, see [Disk and memory sizing](discovery-tool-disk-sizing.md).
+ **Security review** – start your security review early. The discovery tool uses read-only accounts and installs no agent or software on the servers that it discovers. It needs outbound internet access only if you turn on self-update.

### Collect long enough to capture peaks
<a name="transform-vmware-discovery-bp-duration"></a>
+ AWS Prescriptive Guidance considers two weeks of automated data collection enough for a first analysis. For more information, see [Discovery acceleration and initial planning](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/portfolio-discovery-initial-planning.html) in *AWS Prescriptive Guidance*. The discovery tool keeps 30 days of data, so plan collection to include month-end or other regular peaks.
+ Without utilization data, AWS Transform sizes servers from default assumptions instead of observed use. As a result, servers aren't right-sized to what they actually use. When a volume reports no used capacity, AWS Transform assumes that 50 percent of its provisioned capacity is in use.
+ Without SQL Server editions and versions, AWS Transform can't analyze your SQL Server licensing.

### Validate your inventory
<a name="transform-vmware-discovery-bp-validate"></a>
+ **Review the summary in the chat.** Check server counts by operating system, physical and virtual servers, storage, and detected databases.
+ **Reconcile counts when you combine sources.** AWS Transform removes duplicate records across uploads. After you combine sources, confirm that the server count matches what you expect.
+ **Check that key fields have values.** A server can be present but missing the fields that an assessment needs, such as utilization, storage performance, or hypervisor type.
+ **Exclude servers that you plan to retire.** They inflate both your on-premises baseline and your AWS estimate. AWS Transform also excludes some resources automatically, so confirm the in-scope count. For more information, see [Managing inventory scope](transform-app-assessments.md#transform-app-assessments-manage-scope).
+ **Read the unmapped storage report.** The discovery tool export includes `unmapped_storage_devices.csv`, which explains why each storage device wasn't mapped.
+ **State your assumptions.** Stakeholders often question the on-premises cost baseline. You can adjust it with your own costs. For more information, see [Additional cost components](transform-app-assessments-cost-components.md).

### Collect what migration planning needs
<a name="transform-vmware-discovery-bp-planning"></a>
+ **Network connections** – the discovery tool collects connections only from servers that it can reach with OS credentials. Without connection data, AWS Transform plans each application on its own. That doesn't mean that the applications are independent, so confirm dependencies with your application owners.
+ **Dependencies belong in planning** – assessments don't map application dependencies. AWS Transform groups dependent applications during migration planning.
+ **Business context** – collect owner, location, business function, criticality, and recovery objectives from your application owners. For more information, see [Application owner questionnaire](transform-vmware-application-questionnaire.md).
+ **Move groups and waves** – group applications that share databases, message queues, criticality, location, or ownership. Migrate non-production environments before production, and keep each move group in a single wave.

### Mistakes to avoid
<a name="transform-vmware-discovery-bp-avoid"></a>
+ Treating an RVTools export as a complete inventory. It contains no database or connection data.
+ Waiting for complete data before you build a directional business case.
+ Assuming that combined sources merged correctly without checking the server counts.