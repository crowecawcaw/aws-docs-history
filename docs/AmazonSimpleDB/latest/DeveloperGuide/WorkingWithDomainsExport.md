

# Exporting a Domain to Amazon Simple Storage Service
<a name="WorkingWithDomainsExport"></a>

 Amazon SimpleDB allows you to export domain data to Amazon S3 for migration and archival. The export process runs asynchronously in the background and does not affect the performance of your active database operations. Exported data is stored in standard JSON format. 

The new Amazon SimpleDB export operations are only available through the SimpleDBv2 service in newer versions of the AWS SDKs and AWS CLI.

**Important**  
 Exported data cannot be restored back to Amazon SimpleDB. The export feature is designed for one-way data migration and archival. After you have exported your Amazon SimpleDB data to Amazon S3, you can't import the data again. 

 This section covers the following topics: 

**Topics**
+ [Prerequisites and Permissions](ExportPrerequisites.md)
+ [Export a domain to Amazon S3](HowToExportDomainToS3.md)
+ [Export Considerations](ExportConsiderations.md)
+ [Track Export Status](TrackingExportStatus.md)
+ [List Exports in an Account](ListingExports.md)
+ [Log Amazon SimpleDB export calls with AWS CloudTrail](LoggingExportsCloudTrail.md)
+ [Best Practices for Domain Exports](ExportBestPractices.md)