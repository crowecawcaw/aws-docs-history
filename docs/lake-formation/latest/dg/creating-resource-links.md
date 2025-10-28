# Creating resource links

Resource links are Data Catalog objects that are links to metadata databases and
tables—typically to shared databases and tables from other AWS accounts. They help to
enable cross-account access to data in the data lake across all AWS Regions.

###### Note

Lake Formation supports querying Data Catalog tables across AWS Regions.
You can access the Data Catalog databases and tables from any AWS Region by creating resource links in those regions that point to shared databases and tables in different Regions.

###### Topics

- [How resource links work in Lake Formation](resource-links-about.md "resource-links-about.md")
- [Creating a resource link to a shared Data Catalog
  table](create-resource-link-table.md "create-resource-link-table.md")
- [Creating a resource link to a shared Data Catalog
  database](create-resource-link-database.md "create-resource-link-database.md")
- [Resource link handling in AWS Glue
  APIs](resource-links-glue-apis.md "resource-links-glue-apis.md")
