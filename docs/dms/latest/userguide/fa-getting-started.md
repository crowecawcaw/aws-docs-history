# Understand how to use DMS Fleet Advisor

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service Fleet
Advisor. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet
Advisor console or AWS DMS Fleet Advisor resources. For more information, see [AWS DMS Fleet Advisor
end of support](dms_fleet.md "dms_fleet.md").

You can use DMS Fleet Advisor to discover your source on-premises databases for migration to the
AWS Cloud. Then, you can determine the right migration target in the AWS Cloud for each
of your on-premises databases. Use the following workflow to create an inventory of your
source databases and generate target recommendations.

1. Create an Amazon S3 bucket, IAM policies, roles, and users. For more information,
   see [Creating required resources](fa-resources.md "fa-resources.md").
2. Create database users with the minimum permissions required for the DMS data collector.
   For more information, see [Creating database users](fa-database-users.md "fa-database-users.md").
3. Create and download a data collector. For more information, see [Creating a data collector](fa-data-collectors-create.md "fa-data-collectors-create.md").
4. Install the data collector in your local environment. Next, configure your
   data collector to make sure that it can send the collected data to DMS Fleet Advisor. For more
   information, see [Installing a data
   collector](fa-data-collectors-install.md "fa-data-collectors-install.md").
5. Discover the OS and database servers in your data environment. For more information,
   see [Discovering OS and database servers](fa-discovery.md "fa-discovery.md").
6. Collect database metadata and resource utilization metrics. For more information,
   see [Collecting data](fa-collecting.md "fa-collecting.md").
7. Analyze your source databases and schemas. DMS Fleet Advisor runs the large-scale
   assessment of your databases to identify similar schemas. For more information, see
   [Using inventories for analysis in AWS DMS Fleet Advisor](fa-inventory.md "fa-inventory.md").
8. Generate, view, and save a local copy of the target recommendations
   for your source databases. For more information, see [Target recommendations](fa-recommendations.md "fa-recommendations.md").
   After you determine the migration target for each source database, you can use DMS Schema Conversion
   to convert your database schemas to a new platform. Then, you can use AWS DMS to migrate data.
   For more information, see [Converting database schemas using DMS Schema Conversion](CHAP_SchemaConversion.md "CHAP_SchemaConversion.md")
   and [What is AWS Database Migration Service?](Welcome.md "Welcome.md")

The following video introduces the DMS Fleet Advisor
user interface and helps you get familiar with this service.
