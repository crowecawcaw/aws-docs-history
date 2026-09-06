

# Discover source data
<a name="transform-vmware-discover-source-data"></a>

Upload your on-premises server data and AWS Transform automatically detects file format and structure, parses and extracts structured entity records, removes duplicates across multiple files, validates data quality and reports issues, and then prepares a summary ready for downstream migration planning.

AWS Transform accepts data from the following sources:
+ [AWS Transform discovery tool](discovery-tool.md) (CSV and JSON in ZIP format)
+ AWS Migration Evaluator collector
+ RVTools (Excel file or a ZIP file containing CSV files)
+ modelizeIT (CSV in ZIP format)
+ AWS Migration Portfolio Assessment (MPA) format exports (for example, Cloudamize)

For each data source, AWS Transform accepts the primary server file individually. Supplementary files such as connections are only processed when included in a ZIP file with the server files or in an Excel file with the server sheet.

Upload the most detailed data available. Before you upload, review your export files to ensure data completeness and accuracy. Verify that all required files are included, and confirm that the data reflects your current environment state. This helps AWS Transform capture your on-premises environment more accurately and better support migration planning, including application grouping and wave planning. You can incrementally add data as you obtain it. AWS Transform automatically de-duplicates records across multiple uploads.

After upload, review your discovery data by expanding **Discover on-premises data** in the **Job Plan** and choosing **Inventory readiness summary**. You can ask questions in the chat to verify ingestion or identify issues. For example, you can ask about operating system and versions. To correct mistakes, re-upload your data and AWS Transform merges the updated records automatically. You can also remove a previously uploaded file if you no longer want to use that inventory data.